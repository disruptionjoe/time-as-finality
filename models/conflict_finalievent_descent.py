"""T55: Conflict-enriched FinaliEvent descent.

T48-T54 used empty conflict. This module adds an explicit finite conflict
relation to FinaliEvent descent and tests whether the T54 quotient-union
theorem survives when events may be mutually exclusive.

The implementation deliberately keeps conflict finite and explicit. It does
not import full event-structure machinery. Instead it checks the NPW-shaped
conditions needed by the current witness family:

* conflict is irreflexive;
* conflict is symmetric, represented by normalized unordered pairs;
* conflict is not asserted between comparable events;
* conflict is upward inherited along the reconstructed record order.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Any


# ---------------------------------------------------------------------------
# Finite conflict descent objects
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    causal: int
    info: int

    def leq(self, other: "AxisProfile") -> bool:
        return self.causal <= other.causal and self.info <= other.info


@dataclass(frozen=True)
class LocalConflictEvent:
    observer: str
    name: str
    source_records: frozenset[str]
    target_records: frozenset[str]
    profile: AxisProfile

    @property
    def key(self) -> tuple[str, str]:
        return (self.observer, self.name)


@dataclass(frozen=True)
class ObserverConflictView:
    name: str
    events: tuple[LocalConflictEvent, ...]
    conflict_pairs: tuple[tuple[str, str], ...] = ()
    compatibility_pairs: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class EventIdentityMap:
    observer: str
    local_event: str
    global_event: str | None


@dataclass(frozen=True)
class ConflictDescentDatum:
    name: str
    description: str
    observer_views: tuple[ObserverConflictView, ...]
    identity_maps: tuple[EventIdentityMap, ...]
    overlap_witnesses: frozenset[str]
    expected_classification: str


@dataclass(frozen=True)
class GlobalConflictEvent:
    name: str
    source_records: frozenset[str]
    target_records: frozenset[str]
    profile: AxisProfile
    local_events: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class PartialOrderCheck:
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    is_partial_order: bool
    order_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class AMViolation:
    predecessor: str
    successor: str
    in_record_order: bool
    in_axis_order: bool
    kind: str


@dataclass(frozen=True)
class AMCheck:
    am_holds: bool
    violations: tuple[AMViolation, ...]
    spurious_count: int
    missing_count: int


@dataclass(frozen=True)
class ConflictCheck:
    conflict_pairs: tuple[tuple[str, str], ...]
    explicit_compatibility_pairs: tuple[tuple[str, str], ...]
    irreflexive: bool
    symmetric: bool
    upward_inherited: bool
    comparable_conflict_free: bool
    valid: bool
    failures: tuple[str, ...]


@dataclass(frozen=True)
class ConflictCompletionResult:
    datum_name: str
    classification: str
    condition_failures: tuple[str, ...]
    global_events: tuple[GlobalConflictEvent, ...]
    partial_order: PartialOrderCheck | None
    axis_monotonicity: AMCheck | None
    conflict_check: ConflictCheck | None
    theorem_applies: bool
    evidence: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T55Result:
    completions: tuple[ConflictCompletionResult, ...]
    theorem_statement: str
    condition_basis: tuple[str, ...]
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    event_structure_verdict: str
    best_supported: str


# ---------------------------------------------------------------------------
# Core checks
# ---------------------------------------------------------------------------


def _norm_pair(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))


def _event_by_key(datum: ConflictDescentDatum) -> dict[tuple[str, str], LocalConflictEvent]:
    events: dict[tuple[str, str], LocalConflictEvent] = {}
    for view in datum.observer_views:
        for event in view.events:
            events[event.key] = event
    return events


def _views_by_name(datum: ConflictDescentDatum) -> dict[str, ObserverConflictView]:
    return {view.name: view for view in datum.observer_views}


def _identity_maps_by_key(
    datum: ConflictDescentDatum,
) -> dict[tuple[str, str], list[EventIdentityMap]]:
    maps: dict[tuple[str, str], list[EventIdentityMap]] = defaultdict(list)
    for mapping in datum.identity_maps:
        maps[(mapping.observer, mapping.local_event)].append(mapping)
    return maps


def _record_conflicts(records: frozenset[str]) -> tuple[str, ...]:
    positives = {record for record in records if not record.startswith("not:")}
    negatives = {record[4:] for record in records if record.startswith("not:")}
    return tuple(sorted(positives & negatives))


def _record_order(events: tuple[GlobalConflictEvent, ...]) -> frozenset[tuple[str, str]]:
    names = [event.name for event in events]
    order: set[tuple[str, str]] = {(name, name) for name in names}

    for predecessor, successor in itertools.product(events, repeat=2):
        if predecessor.name == successor.name:
            continue
        if predecessor.target_records and predecessor.target_records <= successor.source_records:
            order.add((predecessor.name, successor.name))

    changed = True
    while changed:
        changed = False
        for a, b, c in itertools.product(names, repeat=3):
            if (a, b) in order and (b, c) in order and (a, c) not in order:
                order.add((a, c))
                changed = True

    return frozenset(order)


def _partial_order(events: tuple[GlobalConflictEvent, ...]) -> PartialOrderCheck:
    names = [event.name for event in events]
    order = _record_order(events)
    reflexive = all((name, name) in order for name in names)
    antisymmetric = not any(
        (a, b) in order and (b, a) in order
        for a, b in itertools.product(names, repeat=2)
        if a != b
    )
    transitive = all(
        (a, c) in order
        for a, b, c in itertools.product(names, repeat=3)
        if (a, b) in order and (b, c) in order
    )
    return PartialOrderCheck(
        reflexive=reflexive,
        antisymmetric=antisymmetric,
        transitive=transitive,
        is_partial_order=reflexive and antisymmetric and transitive,
        order_pairs=tuple(sorted(order)),
    )


def _axis_monotonicity(events: tuple[GlobalConflictEvent, ...]) -> AMCheck:
    order = _record_order(events)
    violations: list[AMViolation] = []

    for predecessor, successor in itertools.product(events, repeat=2):
        if predecessor.name == successor.name:
            continue
        in_record_order = (predecessor.name, successor.name) in order
        in_axis_order = predecessor.profile.leq(successor.profile)
        if in_record_order != in_axis_order:
            kind = "spurious_axis_order" if in_axis_order else "missing_axis_order"
            violations.append(AMViolation(
                predecessor=predecessor.name,
                successor=successor.name,
                in_record_order=in_record_order,
                in_axis_order=in_axis_order,
                kind=kind,
            ))

    return AMCheck(
        am_holds=len(violations) == 0,
        violations=tuple(violations),
        spurious_count=sum(1 for v in violations if v.kind == "spurious_axis_order"),
        missing_count=sum(1 for v in violations if v.kind == "missing_axis_order"),
    )


def _conflict_check(
    conflict_pairs: frozenset[tuple[str, str]],
    compatibility_pairs: frozenset[tuple[str, str]],
    order: PartialOrderCheck,
) -> ConflictCheck:
    failures: list[str] = []

    for left, right in sorted(conflict_pairs):
        if left == right:
            failures.append(f"self_conflict: {left}")

    overlap = conflict_pairs & compatibility_pairs
    for left, right in sorted(overlap):
        failures.append(f"explicit_conflict_disagreement: {left}#{right}")

    order_pairs = set(order.order_pairs)
    for left, right in sorted(conflict_pairs):
        if left != right and ((left, right) in order_pairs or (right, left) in order_pairs):
            failures.append(f"conflict_between_comparable_events: {left}#{right}")

    for left, right in sorted(conflict_pairs):
        if left == right:
            continue
        for predecessor, successor in order_pairs:
            if predecessor == successor:
                continue
            if predecessor == left and successor != right:
                inherited = _norm_pair(successor, right)
                if inherited not in conflict_pairs:
                    failures.append(
                        f"missing_inherited_conflict: {left}<={successor} requires {inherited[0]}#{inherited[1]}"
                    )
            if predecessor == right and successor != left:
                inherited = _norm_pair(left, successor)
                if inherited not in conflict_pairs:
                    failures.append(
                        f"missing_inherited_conflict: {right}<={successor} requires {inherited[0]}#{inherited[1]}"
                    )

    comparable_conflict_free = not any(
        failure.startswith("conflict_between_comparable_events") for failure in failures
    )
    irreflexive = not any(failure.startswith("self_conflict") for failure in failures)
    upward_inherited = not any(failure.startswith("missing_inherited_conflict") for failure in failures)
    explicit_consistent = not any(
        failure.startswith("explicit_conflict_disagreement") for failure in failures
    )

    return ConflictCheck(
        conflict_pairs=tuple(sorted(conflict_pairs)),
        explicit_compatibility_pairs=tuple(sorted(compatibility_pairs)),
        irreflexive=irreflexive,
        symmetric=True,
        upward_inherited=upward_inherited,
        comparable_conflict_free=comparable_conflict_free,
        valid=irreflexive and upward_inherited and comparable_conflict_free and explicit_consistent,
        failures=tuple(dict.fromkeys(failures)),
    )


def _canonical_conflict_completion(datum: ConflictDescentDatum) -> ConflictCompletionResult:
    events = _event_by_key(datum)
    views = _views_by_name(datum)
    maps_by_key = _identity_maps_by_key(datum)
    failures: list[str] = []

    class_members: dict[str, list[LocalConflictEvent]] = defaultdict(list)
    local_to_global: dict[tuple[str, str], str] = {}
    for key, event in events.items():
        maps = maps_by_key.get(key, [])
        if len(maps) == 0:
            failures.append(f"nondefinable_map: missing identity map for {event.observer}.{event.name}")
            continue
        if len(maps) > 1:
            failures.append(f"nondefinable_map: multiple identity maps for {event.observer}.{event.name}")
            continue
        global_event = maps[0].global_event
        if global_event is None:
            failures.append(f"missing_event_identity: {event.observer}.{event.name}")
            continue
        class_members[global_event].append(event)
        local_to_global[key] = global_event

    mapped_keys = {(m.observer, m.local_event) for m in datum.identity_maps}
    unknown_maps = sorted(mapped_keys - set(events))
    for observer, local_event in unknown_maps:
        failures.append(f"nondefinable_map: map references unknown event {observer}.{local_event}")

    conflict_reference_failures: list[str] = []
    for view in datum.observer_views:
        local_event_names = {event.name for event in view.events}
        for left, right in view.conflict_pairs + view.compatibility_pairs:
            if left not in local_event_names or right not in local_event_names:
                conflict_reference_failures.append(
                    f"nondefinable_conflict_reference: {view.name}.{left},{right}"
                )

    failures.extend(conflict_reference_failures)

    if any(f.startswith("nondefinable") for f in failures):
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="nondefinable",
            condition_failures=tuple(failures),
            global_events=(),
            partial_order=None,
            axis_monotonicity=None,
            conflict_check=None,
            theorem_applies=False,
            evidence="Required event, identity, or conflict maps are not definable.",
        )

    if any(f.startswith("missing_event_identity") for f in failures):
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="underdetermined",
            condition_failures=tuple(failures),
            global_events=(),
            partial_order=None,
            axis_monotonicity=None,
            conflict_check=None,
            theorem_applies=False,
            evidence="Local event identities are not fixed, so conflict descent is not canonical.",
        )

    underdetermined: list[str] = []
    conflicting: list[str] = []
    global_events: list[GlobalConflictEvent] = []

    for global_name in sorted(class_members):
        members = class_members[global_name]
        observers = {member.observer for member in members}
        if len(observers) > 1 and global_name not in datum.overlap_witnesses:
            underdetermined.append(f"insufficient_overlap: {global_name}")

        source_records = frozenset().union(*(member.source_records for member in members))
        target_records = frozenset().union(*(member.target_records for member in members))
        source_conflicts = _record_conflicts(source_records)
        target_conflicts = _record_conflicts(target_records)
        if source_conflicts:
            conflicting.append(f"source_record_conflict: {global_name}: {source_conflicts}")
        if target_conflicts:
            conflicting.append(f"target_record_conflict: {global_name}: {target_conflicts}")

        profiles = {member.profile for member in members}
        if len(profiles) != 1:
            conflicting.append(f"axis_profile_conflict: {global_name}")
            profile = sorted(profiles, key=lambda p: (p.causal, p.info))[0]
        else:
            profile = next(iter(profiles))

        global_events.append(GlobalConflictEvent(
            name=global_name,
            source_records=source_records,
            target_records=target_records,
            profile=profile,
            local_events=tuple(sorted(member.key for member in members)),
        ))

    completion = tuple(global_events)
    if conflicting:
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="conflicting",
            condition_failures=tuple(conflicting),
            global_events=completion,
            partial_order=None,
            axis_monotonicity=None,
            conflict_check=None,
            theorem_applies=False,
            evidence="Observer-local event data disagree before conflict can be checked.",
        )

    conflict_pairs: set[tuple[str, str]] = set()
    compatibility_pairs: set[tuple[str, str]] = set()
    for view_name, view in views.items():
        for left, right in view.conflict_pairs:
            conflict_pairs.add(_norm_pair(
                local_to_global[(view_name, left)],
                local_to_global[(view_name, right)],
            ))
        for left, right in view.compatibility_pairs:
            compatibility_pairs.add(_norm_pair(
                local_to_global[(view_name, left)],
                local_to_global[(view_name, right)],
            ))

    po = _partial_order(completion)
    if not po.is_partial_order:
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="conflicting",
            condition_failures=("partial_order_failure",),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=None,
            conflict_check=None,
            theorem_applies=False,
            evidence="The quotient-union completion is not a valid partial order.",
        )

    am = _axis_monotonicity(completion)
    conflict = _conflict_check(frozenset(conflict_pairs), frozenset(compatibility_pairs), po)
    if not conflict.valid:
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="conflict_invalid",
            condition_failures=conflict.failures,
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            conflict_check=conflict,
            theorem_applies=False,
            evidence="The quotient-union order exists, but the conflict relation is not event-structure valid.",
        )

    if underdetermined:
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="underdetermined",
            condition_failures=tuple(underdetermined),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            conflict_check=conflict,
            theorem_applies=False,
            evidence="The quotient-union is compatible but not canonically justified by overlap data.",
        )

    if not am.am_holds:
        return ConflictCompletionResult(
            datum_name=datum.name,
            classification="am_invalid",
            condition_failures=("axis_monotonicity_failure",),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            conflict_check=conflict,
            theorem_applies=False,
            evidence="A unique conflict-compatible partial order exists, but axis dominance does not reconstruct it.",
        )

    return ConflictCompletionResult(
        datum_name=datum.name,
        classification="canonical",
        condition_failures=(),
        global_events=completion,
        partial_order=po,
        axis_monotonicity=am,
        conflict_check=conflict,
        theorem_applies=True,
        evidence="Finite descent conditions, AM, and conflict validity all hold.",
    )


# ---------------------------------------------------------------------------
# Witness builders
# ---------------------------------------------------------------------------


def _ev(
    observer: str,
    name: str,
    source: set[str],
    target: set[str],
    causal: int,
    info: int,
) -> LocalConflictEvent:
    return LocalConflictEvent(
        observer=observer,
        name=name,
        source_records=frozenset(source),
        target_records=frozenset(target),
        profile=AxisProfile(causal, info),
    )


def _view(
    name: str,
    events: tuple[LocalConflictEvent, ...],
    conflicts: tuple[tuple[str, str], ...] = (),
    compatibilities: tuple[tuple[str, str], ...] = (),
) -> ObserverConflictView:
    return ObserverConflictView(
        name=name,
        events=events,
        conflict_pairs=conflicts,
        compatibility_pairs=compatibilities,
    )


def _ids(observer: str, pairs: tuple[tuple[str, str | None], ...]) -> tuple[EventIdentityMap, ...]:
    return tuple(EventIdentityMap(observer, local, global_) for local, global_ in pairs)


def _base_conflict_events(observer: str) -> tuple[LocalConflictEvent, ...]:
    return (
        _ev(observer, "e1", {"r1_raw"}, {"r1_locked"}, 1, 1),
        _ev(observer, "e2", {"r2_raw"}, {"r2_locked"}, 3, 0),
        _ev(observer, "e3", {"r1_locked", "r3_raw"}, {"r3_locked"}, 2, 2),
    )


def _base_identity_maps(observer: str) -> tuple[EventIdentityMap, ...]:
    return _ids(observer, (("e1", "e1"), ("e2", "e2"), ("e3", "e3")))


def _empty_conflict_special_case() -> ConflictDescentDatum:
    events = (
        _ev("A", "e1", {"r_A_raw"}, {"r_A_locked"}, 2, 2),
        _ev("A", "e2", {"r_B_raw"}, {"r_B_locked"}, 1, 3),
        _ev("A", "e3", {"r_A_locked", "r_B_locked", "r_composite_raw"}, {"r_composite_locked"}, 3, 4),
    )
    return ConflictDescentDatum(
        name="T48_empty_conflict_special_case",
        description="T48/T54-compatible empty-conflict FinaliEvent structure.",
        observer_views=(_view("A", events),),
        identity_maps=_ids("A", (("e1", "e1"), ("e2", "e2"), ("e3", "e3"))),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="canonical",
    )


def _canonical_conflict_descent() -> ConflictDescentDatum:
    events = _base_conflict_events("A")
    return ConflictDescentDatum(
        name="canonical_conflict_descent",
        description="One observer supplies an upward-inherited conflict relation.",
        observer_views=(_view("A", events, conflicts=(("e1", "e2"), ("e2", "e3"))),),
        identity_maps=_base_identity_maps("A"),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="canonical",
    )


def _same_order_no_conflict_control() -> ConflictDescentDatum:
    events = _base_conflict_events("A")
    return ConflictDescentDatum(
        name="same_order_no_conflict_control",
        description="Same records and profiles as the conflict witness, but no conflict relation.",
        observer_views=(_view("A", events),),
        identity_maps=_base_identity_maps("A"),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="canonical",
    )


def _hidden_conflict_repaired_by_colimit() -> ConflictDescentDatum:
    a_events = _base_conflict_events("A")
    b_events = _base_conflict_events("B")
    return ConflictDescentDatum(
        name="hidden_conflict_repaired_by_colimit",
        description="Neither local conflict view is complete, but their union is upward-inherited.",
        observer_views=(
            _view("A", a_events, conflicts=(("e1", "e2"),)),
            _view("B", b_events, conflicts=(("e2", "e3"),)),
        ),
        identity_maps=_base_identity_maps("A") + _base_identity_maps("B"),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="canonical",
    )


def _explicit_conflict_disagreement() -> ConflictDescentDatum:
    a_events = _base_conflict_events("A")
    b_events = _base_conflict_events("B")
    return ConflictDescentDatum(
        name="explicit_conflict_disagreement",
        description="One observer asserts conflict while another explicitly asserts compatibility.",
        observer_views=(
            _view("A", a_events, conflicts=(("e1", "e2"), ("e2", "e3"))),
            _view("B", b_events, compatibilities=(("e1", "e2"),)),
        ),
        identity_maps=_base_identity_maps("A") + _base_identity_maps("B"),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="conflict_invalid",
    )


def _upward_inheritance_failure() -> ConflictDescentDatum:
    events = _base_conflict_events("A")
    return ConflictDescentDatum(
        name="upward_inheritance_failure",
        description="e1#e2 is asserted, e1<=e3 holds, but e2#e3 is missing.",
        observer_views=(_view("A", events, conflicts=(("e1", "e2"),)),),
        identity_maps=_base_identity_maps("A"),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="conflict_invalid",
    )


def _self_conflict_after_identity_collapse() -> ConflictDescentDatum:
    events = (
        _ev("A", "a", {"raw_a"}, {"r_locked"}, 1, 1),
        _ev("A", "b", {"raw_b"}, {"r_locked"}, 1, 1),
    )
    return ConflictDescentDatum(
        name="self_conflict_after_identity_collapse",
        description="Two locally conflicting labels are identified as one global event.",
        observer_views=(_view("A", events, conflicts=(("a", "b"),)),),
        identity_maps=_ids("A", (("a", "e1"), ("b", "e1"))),
        overlap_witnesses=frozenset({"e1"}),
        expected_classification="conflict_invalid",
    )


def build_t55_datums() -> tuple[ConflictDescentDatum, ...]:
    return (
        _empty_conflict_special_case(),
        _canonical_conflict_descent(),
        _same_order_no_conflict_control(),
        _hidden_conflict_repaired_by_colimit(),
        _explicit_conflict_disagreement(),
        _upward_inheritance_failure(),
        _self_conflict_after_identity_collapse(),
    )


# ---------------------------------------------------------------------------
# Main analysis and serialization
# ---------------------------------------------------------------------------


def run_t55_analysis() -> T55Result:
    datums = build_t55_datums()
    completions = tuple(_canonical_conflict_completion(datum) for datum in datums)
    by_name = {completion.datum_name: completion for completion in completions}

    theorem_statement = (
        "Conflict-Enriched FinaliEvent Descent Theorem (finite v0.1): given "
        "finite observer-local FinaliEvent data with T54 identity, overlap, "
        "record, profile, partial-order, and AM conditions, plus a merged "
        "conflict relation that is irreflexive, symmetric, comparable-conflict "
        "free, and upward inherited along the reconstructed record order, the "
        "canonical quotient-union construction produces a unique conflict-valid "
        "global FinaliEvent structure. If conflict validity fails, the failure "
        "is classified rather than silently repaired."
    )

    condition_basis = (
        "C1 event identity maps are total and single-valued",
        "C2 cross-observer identified events have overlap witnesses",
        "C3 source records merge without explicit contradiction",
        "C4 target records merge without explicit contradiction",
        "C5 identified events agree on finality-axis profiles",
        "C6 the quotient-union dependency order is a valid partial order",
        "C7 Axis Monotonicity holds on the reconstructed global structure",
        "C8 conflict is irreflexive and symmetric",
        "C9 conflict is not asserted between comparable events",
        "C10 conflict is upward inherited along the reconstructed order",
        "C11 explicit conflict and explicit compatibility do not disagree",
    )

    h0_supported = by_name["canonical_conflict_descent"].theorem_applies
    h2_supported = by_name["upward_inheritance_failure"].classification == "conflict_invalid"
    h3_refuted = by_name["hidden_conflict_repaired_by_colimit"].theorem_applies
    conflict_order = set(by_name["canonical_conflict_descent"].partial_order.order_pairs)
    no_conflict_order = set(by_name["same_order_no_conflict_control"].partial_order.order_pairs)
    same_order_conflict_variation = (
        conflict_order == no_conflict_order
        and set(by_name["canonical_conflict_descent"].conflict_check.conflict_pairs)
        != set(by_name["same_order_no_conflict_control"].conflict_check.conflict_pairs)
    )
    h4_status = "supported" if same_order_conflict_variation else "partially_supported"

    hypothesis_evaluations = (
        HypothesisResult(
            "H0",
            "T54 descent only works for empty-conflict FinaliEvent structures.",
            "refuted" if h0_supported else "open",
            "canonical_conflict_descent theorem_applies=True",
        ),
        HypothesisResult(
            "H1",
            "Conflict can be added as an independent finite relation without changing T54.",
            "partially_supported",
            "Conflict is finite and independent, but T55 adds C8-C11 beyond T54.",
        ),
        HypothesisResult(
            "H2",
            "Conflict introduces new descent conditions beyond the T54 basis.",
            "supported" if h2_supported else "open",
            "upward_inheritance_failure is AM-valid and partial-order valid but conflict_invalid.",
        ),
        HypothesisResult(
            "H3",
            "Conflict forces full event-structure machinery beyond finite quotient-union checks.",
            "refuted" if h3_refuted else "open",
            "The tested witness family is decided by finite conflict checks over the quotient-union.",
        ),
        HypothesisResult(
            "H4",
            "FinaliEvent order and conflict cannot be reconstructed from the same data.",
            h4_status,
            "canonical_conflict_descent and same_order_no_conflict_control have the same record order and AM-valid axis profiles but different conflict relations.",
        ),
    )

    event_structure_verdict = (
        "Full NPW event-structure machinery can still be postponed for the "
        "tested finite witness family. T55 needs an NPW-shaped conflict "
        "relation, but irreflexivity, comparable-conflict freedom, upward "
        "inheritance, and explicit disagreement checks are finite conflict "
        "checks decidable directly on the quotient-union completion."
    )

    best_supported = (
        "H2 supported and H0/H3 refuted: T54 generalizes to non-empty conflict, "
        "but only after adding explicit finite conflict-descent conditions. "
        "Conflict is not reducible to order or AM metadata in the tested cases."
    )

    return T55Result(
        completions=completions,
        theorem_statement=theorem_statement,
        condition_basis=condition_basis,
        hypothesis_evaluations=hypothesis_evaluations,
        event_structure_verdict=event_structure_verdict,
        best_supported=best_supported,
    )


def _axis_profile_to_dict(profile: AxisProfile) -> dict[str, int]:
    return {"causal": profile.causal, "info": profile.info}


def _event_to_dict(event: GlobalConflictEvent) -> dict[str, Any]:
    return {
        "name": event.name,
        "source_records": sorted(event.source_records),
        "target_records": sorted(event.target_records),
        "profile": _axis_profile_to_dict(event.profile),
        "local_events": [list(key) for key in event.local_events],
    }


def _partial_order_to_dict(order: PartialOrderCheck | None) -> dict[str, Any] | None:
    if order is None:
        return None
    return {
        "reflexive": order.reflexive,
        "antisymmetric": order.antisymmetric,
        "transitive": order.transitive,
        "is_partial_order": order.is_partial_order,
        "order_pairs": [list(pair) for pair in order.order_pairs],
    }


def _am_to_dict(am: AMCheck | None) -> dict[str, Any] | None:
    if am is None:
        return None
    return {
        "am_holds": am.am_holds,
        "spurious_count": am.spurious_count,
        "missing_count": am.missing_count,
        "violations": [
            {
                "predecessor": v.predecessor,
                "successor": v.successor,
                "in_record_order": v.in_record_order,
                "in_axis_order": v.in_axis_order,
                "kind": v.kind,
            }
            for v in am.violations
        ],
    }


def _conflict_to_dict(conflict: ConflictCheck | None) -> dict[str, Any] | None:
    if conflict is None:
        return None
    return {
        "conflict_pairs": [list(pair) for pair in conflict.conflict_pairs],
        "explicit_compatibility_pairs": [list(pair) for pair in conflict.explicit_compatibility_pairs],
        "irreflexive": conflict.irreflexive,
        "symmetric": conflict.symmetric,
        "upward_inherited": conflict.upward_inherited,
        "comparable_conflict_free": conflict.comparable_conflict_free,
        "valid": conflict.valid,
        "failures": list(conflict.failures),
    }


def _completion_to_dict(completion: ConflictCompletionResult) -> dict[str, Any]:
    return {
        "datum_name": completion.datum_name,
        "classification": completion.classification,
        "condition_failures": list(completion.condition_failures),
        "global_events": [_event_to_dict(event) for event in completion.global_events],
        "partial_order": _partial_order_to_dict(completion.partial_order),
        "axis_monotonicity": _am_to_dict(completion.axis_monotonicity),
        "conflict_check": _conflict_to_dict(completion.conflict_check),
        "theorem_applies": completion.theorem_applies,
        "evidence": completion.evidence,
    }


def t55_result_to_dict(result: T55Result) -> dict[str, Any]:
    return {
        "theorem_statement": result.theorem_statement,
        "condition_basis": list(result.condition_basis),
        "completions": [_completion_to_dict(completion) for completion in result.completions],
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
        "event_structure_verdict": result.event_structure_verdict,
        "best_supported": result.best_supported,
    }


__all__ = [
    "AMCheck",
    "AMViolation",
    "AxisProfile",
    "ConflictCheck",
    "ConflictCompletionResult",
    "ConflictDescentDatum",
    "EventIdentityMap",
    "GlobalConflictEvent",
    "HypothesisResult",
    "LocalConflictEvent",
    "ObserverConflictView",
    "PartialOrderCheck",
    "T55Result",
    "build_t55_datums",
    "run_t55_analysis",
    "t55_result_to_dict",
]
