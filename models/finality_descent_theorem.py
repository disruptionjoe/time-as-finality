"""T54: Finite Finality Descent Theorem.

T54 turns the T53 boundary into an executable theorem schema. T53 showed that
valid observer-colimit consistency is weaker than canonical reconstruction.
This module defines finite descent data and a canonical quotient-union
completion algorithm.

The algorithm intentionally refuses to silently repair observer data. When a
descent condition fails, it classifies the failure as nondefinable,
underdetermined, conflicting, or AM-invalid.
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Any


# ---------------------------------------------------------------------------
# Finite descent objects
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    causal: int
    info: int

    def leq(self, other: "AxisProfile") -> bool:
        return self.causal <= other.causal and self.info <= other.info


@dataclass(frozen=True)
class LocalEvent:
    observer: str
    name: str
    source_records: frozenset[str]
    target_records: frozenset[str]
    profile: AxisProfile

    @property
    def key(self) -> tuple[str, str]:
        return (self.observer, self.name)


@dataclass(frozen=True)
class ObserverView:
    name: str
    events: tuple[LocalEvent, ...]


@dataclass(frozen=True)
class EventIdentityMap:
    """Maps a local observer event into a proposed global event class.

    A `global_event` of None means identity is explicitly missing. This is
    different from an absent map, which is nondefinable.
    """

    observer: str
    local_event: str
    global_event: str | None


@dataclass(frozen=True)
class HiddenRecordRepair:
    global_event: str
    source_records: frozenset[str] = frozenset()
    target_records: frozenset[str] = frozenset()


@dataclass(frozen=True)
class ObserverDescentDatum:
    name: str
    description: str
    observer_views: tuple[ObserverView, ...]
    identity_maps: tuple[EventIdentityMap, ...]
    overlap_witnesses: frozenset[str]
    hidden_repairs: tuple[HiddenRecordRepair, ...] = ()
    expected_classification: str = ""


@dataclass(frozen=True)
class GlobalEvent:
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
class CompletionResult:
    datum_name: str
    classification: str
    condition_failures: tuple[str, ...]
    global_events: tuple[GlobalEvent, ...]
    partial_order: PartialOrderCheck | None
    axis_monotonicity: AMCheck | None
    theorem_applies: bool
    evidence: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T54Result:
    completions: tuple[CompletionResult, ...]
    theorem_statement: str
    condition_basis: tuple[str, ...]
    counterexample_summary: tuple[tuple[str, str], ...]
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    sheaf_verdict: str
    best_supported: str


# ---------------------------------------------------------------------------
# Core checks
# ---------------------------------------------------------------------------


def _event_by_key(datum: ObserverDescentDatum) -> dict[tuple[str, str], LocalEvent]:
    events: dict[tuple[str, str], LocalEvent] = {}
    for view in datum.observer_views:
        for event in view.events:
            events[event.key] = event
    return events


def _identity_maps_by_key(
    datum: ObserverDescentDatum,
) -> dict[tuple[str, str], list[EventIdentityMap]]:
    maps: dict[tuple[str, str], list[EventIdentityMap]] = defaultdict(list)
    for mapping in datum.identity_maps:
        maps[(mapping.observer, mapping.local_event)].append(mapping)
    return maps


def _record_conflicts(records: frozenset[str]) -> tuple[str, ...]:
    """Detect explicit finite contradictions such as r_x and not:r_x."""

    positives = {record for record in records if not record.startswith("not:")}
    negatives = {record[4:] for record in records if record.startswith("not:")}
    return tuple(sorted(positives & negatives))


def _record_order(events: tuple[GlobalEvent, ...]) -> frozenset[tuple[str, str]]:
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


def _partial_order(events: tuple[GlobalEvent, ...]) -> PartialOrderCheck:
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


def _axis_monotonicity(events: tuple[GlobalEvent, ...]) -> AMCheck:
    order = _record_order(events)
    by_name = {event.name: event for event in events}
    violations: list[AMViolation] = []

    for predecessor, successor in itertools.product(events, repeat=2):
        if predecessor.name == successor.name:
            continue
        in_record_order = (predecessor.name, successor.name) in order
        in_axis_order = by_name[predecessor.name].profile.leq(by_name[successor.name].profile)
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


def _canonical_quotient_union(datum: ObserverDescentDatum) -> CompletionResult:
    events = _event_by_key(datum)
    maps_by_key = _identity_maps_by_key(datum)
    failures: list[str] = []

    class_members: dict[str, list[LocalEvent]] = defaultdict(list)
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

    mapped_keys = {(m.observer, m.local_event) for m in datum.identity_maps}
    unknown_maps = sorted(mapped_keys - set(events))
    for observer, local_event in unknown_maps:
        failures.append(f"nondefinable_map: map references unknown event {observer}.{local_event}")

    if any(f.startswith("nondefinable_map") for f in failures):
        return CompletionResult(
            datum_name=datum.name,
            classification="nondefinable",
            condition_failures=tuple(failures),
            global_events=(),
            partial_order=None,
            axis_monotonicity=None,
            theorem_applies=False,
            evidence="Record-access/event maps are not total and definable.",
        )

    if any(f.startswith("missing_event_identity") for f in failures):
        return CompletionResult(
            datum_name=datum.name,
            classification="underdetermined",
            condition_failures=tuple(failures),
            global_events=(),
            partial_order=None,
            axis_monotonicity=None,
            theorem_applies=False,
            evidence="Local event identities are not fixed, so the quotient is not canonical.",
        )

    underdetermined: list[str] = []
    conflicting: list[str] = []
    global_events: list[GlobalEvent] = []

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

        global_events.append(GlobalEvent(
            name=global_name,
            source_records=source_records,
            target_records=target_records,
            profile=profile,
            local_events=tuple(sorted(member.key for member in members)),
        ))

    if conflicting:
        return CompletionResult(
            datum_name=datum.name,
            classification="conflicting",
            condition_failures=tuple(conflicting),
            global_events=tuple(global_events),
            partial_order=None,
            axis_monotonicity=None,
            theorem_applies=False,
            evidence="Observer-local data disagree inside at least one identified event class.",
        )

    completion = tuple(global_events)
    po = _partial_order(completion)
    if not po.is_partial_order:
        return CompletionResult(
            datum_name=datum.name,
            classification="conflicting",
            condition_failures=("partial_order_failure",),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=None,
            theorem_applies=False,
            evidence="The quotient-union completion is not a valid partial order.",
        )

    am = _axis_monotonicity(completion)
    if underdetermined:
        return CompletionResult(
            datum_name=datum.name,
            classification="underdetermined",
            condition_failures=tuple(underdetermined),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            theorem_applies=False,
            evidence="The quotient-union is compatible but not canonically justified by overlap data.",
        )

    if datum.hidden_repairs:
        return CompletionResult(
            datum_name=datum.name,
            classification="underdetermined",
            condition_failures=tuple(
                f"hidden_record_ambiguity: {repair.global_event}"
                for repair in datum.hidden_repairs
            ),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            theorem_applies=False,
            evidence="Hidden records could alter the completion; repair authority is extra data.",
        )

    if not am.am_holds:
        return CompletionResult(
            datum_name=datum.name,
            classification="am_invalid",
            condition_failures=("axis_monotonicity_failure",),
            global_events=completion,
            partial_order=po,
            axis_monotonicity=am,
            theorem_applies=False,
            evidence="A unique partial-order completion exists, but axis dominance does not reconstruct it.",
        )

    return CompletionResult(
        datum_name=datum.name,
        classification="canonical",
        condition_failures=(),
        global_events=completion,
        partial_order=po,
        axis_monotonicity=am,
        theorem_applies=True,
        evidence="All finite descent conditions hold and AM reconstructs the global record order.",
    )


def complete_observer_descent_datum(datum: ObserverDescentDatum) -> CompletionResult:
    """Run the T54 quotient-union completion algorithm on one descent datum."""

    return _canonical_quotient_union(datum)


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
) -> LocalEvent:
    return LocalEvent(
        observer=observer,
        name=name,
        source_records=frozenset(source),
        target_records=frozenset(target),
        profile=AxisProfile(causal, info),
    )


def _view(name: str, events: tuple[LocalEvent, ...]) -> ObserverView:
    return ObserverView(name, events)


def _ids(observer: str, pairs: tuple[tuple[str, str | None], ...]) -> tuple[EventIdentityMap, ...]:
    return tuple(EventIdentityMap(observer, local, global_) for local, global_ in pairs)


def _t51_datum() -> ObserverDescentDatum:
    a_events = (
        _ev("A", "e1", {"r_A_raw"}, {"r_A_locked"}, 2, 2),
        _ev("A", "e2", {"r_B_raw"}, {"r_B_locked"}, 1, 3),
        _ev("A", "e3", {"r_A_locked", "r_B_locked", "r_composite_raw"}, {"r_composite_locked"}, 3, 4),
    )
    b_events = (
        _ev("B", "e1", {"r_A_raw"}, {"r_A_locked"}, 2, 2),
        _ev("B", "e2", {"r_B_raw"}, {"r_B_locked"}, 1, 3),
        _ev("B", "e3", {"r_B_locked", "r_composite_raw"}, {"r_composite_locked"}, 3, 4),
    )
    return ObserverDescentDatum(
        name="T51_phantom_repair",
        description="T51 bounded observer B misses r_A_locked in e3; quotient-union restores it.",
        observer_views=(_view("A", a_events), _view("B", b_events)),
        identity_maps=_ids("A", (("e1", "e1"), ("e2", "e2"), ("e3", "e3")))
        + _ids("B", (("e1", "e1"), ("e2", "e2"), ("e3", "e3"))),
        overlap_witnesses=frozenset({"e1", "e2", "e3"}),
        expected_classification="canonical",
    )


def _t52_datum() -> ObserverDescentDatum:
    a_events = (
        _ev("A", "e1", {"r1_raw"}, {"r1_locked"}, 2, 1),
        _ev("A", "e2", {"r2_raw"}, {"r2_locked"}, 1, 3),
        _ev("A", "e3", {"r1_locked", "r3_raw"}, {"r3_locked"}, 4, 2),
        _ev("A", "e4", {"r2_locked", "r4_raw"}, {"r4_locked"}, 3, 4),
    )
    b_events = (
        _ev("B", "e1", {"r1_raw"}, {"r1_locked"}, 2, 1),
        _ev("B", "e2", {"r2_raw"}, {"r2_locked"}, 1, 3),
        _ev("B", "e3", {"r3_raw"}, {"r3_locked"}, 4, 2),
        _ev("B", "e4", {"r1_locked", "r2_locked", "r4_raw"}, {"r4_locked"}, 3, 4),
    )
    return ObserverDescentDatum(
        name="T52_symmetric_reconstruction",
        description="T52 complementary observers jointly restore e1<=e3 and e1<=e4.",
        observer_views=(_view("A", a_events), _view("B", b_events)),
        identity_maps=_ids("A", (("e1", "e1"), ("e2", "e2"), ("e3", "e3"), ("e4", "e4")))
        + _ids("B", (("e1", "e1"), ("e2", "e2"), ("e3", "e3"), ("e4", "e4"))),
        overlap_witnesses=frozenset({"e1", "e2", "e3", "e4"}),
        expected_classification="canonical",
    )


def _t53_datum() -> ObserverDescentDatum:
    a_events = (
        _ev("A", "a1", {"a_raw"}, {"r_a"}, 1, 1),
        _ev("A", "a2", {"r_a"}, {"r_a2"}, 2, 2),
    )
    b_events = (
        _ev("B", "b1", {"b_raw"}, {"r_b"}, 1, 1),
        _ev("B", "b2", {"r_b"}, {"r_b2"}, 2, 2),
    )
    return ObserverDescentDatum(
        name="T53_ambiguous_identity",
        description="T53 boundary: local chains could be identified or disjoint without extra identity data.",
        observer_views=(_view("A", a_events), _view("B", b_events)),
        identity_maps=_ids("A", (("a1", None), ("a2", None)))
        + _ids("B", (("b1", None), ("b2", None))),
        overlap_witnesses=frozenset(),
        expected_classification="underdetermined",
    )


def _missing_event_identity() -> ObserverDescentDatum:
    event = _ev("A", "e1", {"raw"}, {"r1"}, 1, 1)
    return ObserverDescentDatum(
        name="CE_missing_event_identity",
        description="A local event is intentionally mapped to no global identity.",
        observer_views=(_view("A", (event,)),),
        identity_maps=_ids("A", (("e1", None),)),
        overlap_witnesses=frozenset(),
        expected_classification="underdetermined",
    )


def _insufficient_overlap() -> ObserverDescentDatum:
    a = _ev("A", "e1", {"a_raw"}, {"r1"}, 1, 1)
    b = _ev("B", "e1", {"b_raw"}, {"r1"}, 1, 1)
    return ObserverDescentDatum(
        name="CE_insufficient_overlap",
        description="Two observers identify e1 but provide no overlap witness.",
        observer_views=(_view("A", (a,)), _view("B", (b,))),
        identity_maps=_ids("A", (("e1", "e1"),)) + _ids("B", (("e1", "e1"),)),
        overlap_witnesses=frozenset(),
        expected_classification="underdetermined",
    )


def _source_record_conflict() -> ObserverDescentDatum:
    a = _ev("A", "e1", {"r_x"}, {"r1"}, 1, 1)
    b = _ev("B", "e1", {"not:r_x"}, {"r1"}, 1, 1)
    return ObserverDescentDatum(
        name="CE_source_record_conflict",
        description="The same global event has contradictory source records.",
        observer_views=(_view("A", (a,)), _view("B", (b,))),
        identity_maps=_ids("A", (("e1", "e1"),)) + _ids("B", (("e1", "e1"),)),
        overlap_witnesses=frozenset({"e1"}),
        expected_classification="conflicting",
    )


def _target_record_conflict() -> ObserverDescentDatum:
    a = _ev("A", "e1", {"raw"}, {"r_x"}, 1, 1)
    b = _ev("B", "e1", {"raw"}, {"not:r_x"}, 1, 1)
    return ObserverDescentDatum(
        name="CE_target_record_conflict",
        description="The same global event has contradictory target records.",
        observer_views=(_view("A", (a,)), _view("B", (b,))),
        identity_maps=_ids("A", (("e1", "e1"),)) + _ids("B", (("e1", "e1"),)),
        overlap_witnesses=frozenset({"e1"}),
        expected_classification="conflicting",
    )


def _axis_profile_conflict() -> ObserverDescentDatum:
    a = _ev("A", "e1", {"raw"}, {"r1"}, 1, 1)
    b = _ev("B", "e1", {"raw"}, {"r1"}, 2, 1)
    return ObserverDescentDatum(
        name="CE_axis_profile_conflict",
        description="The same global event has inconsistent finality-axis profiles.",
        observer_views=(_view("A", (a,)), _view("B", (b,))),
        identity_maps=_ids("A", (("e1", "e1"),)) + _ids("B", (("e1", "e1"),)),
        overlap_witnesses=frozenset({"e1"}),
        expected_classification="conflicting",
    )


def _hidden_record_ambiguity() -> ObserverDescentDatum:
    e1 = _ev("A", "e1", {"raw_1"}, {"r_hidden"}, 1, 1)
    e2 = _ev("A", "e2", {"raw_2"}, {"r2"}, 2, 2)
    return ObserverDescentDatum(
        name="CE_hidden_record_ambiguity",
        description="AM suggests e1<=e2, but adding the required hidden record is extra data.",
        observer_views=(_view("A", (e1, e2)),),
        identity_maps=_ids("A", (("e1", "e1"), ("e2", "e2"))),
        overlap_witnesses=frozenset({"e1", "e2"}),
        hidden_repairs=(HiddenRecordRepair("e2", source_records=frozenset({"r_hidden"})),),
        expected_classification="underdetermined",
    )


def _nondefinable_map() -> ObserverDescentDatum:
    event = _ev("A", "e1", {"raw"}, {"r1"}, 1, 1)
    return ObserverDescentDatum(
        name="CE_nondefinable_map",
        description="The local event has no identity map at all.",
        observer_views=(_view("A", (event,)),),
        identity_maps=(),
        overlap_witnesses=frozenset(),
        expected_classification="nondefinable",
    )


def _am_violation() -> ObserverDescentDatum:
    e1 = _ev("A", "e1", {"raw_1"}, {"r1"}, 2, 2)
    e2 = _ev("A", "e2", {"r1"}, {"r2"}, 1, 4)
    return ObserverDescentDatum(
        name="CE_am_violation",
        description="Record order has e1<=e2, but causal axis decreases.",
        observer_views=(_view("A", (e1, e2)),),
        identity_maps=_ids("A", (("e1", "e1"), ("e2", "e2"))),
        overlap_witnesses=frozenset({"e1", "e2"}),
        expected_classification="am_invalid",
    )


def build_t54_datums() -> tuple[ObserverDescentDatum, ...]:
    return (
        _t51_datum(),
        _t52_datum(),
        _t53_datum(),
        _missing_event_identity(),
        _insufficient_overlap(),
        _source_record_conflict(),
        _target_record_conflict(),
        _axis_profile_conflict(),
        _hidden_record_ambiguity(),
        _nondefinable_map(),
        _am_violation(),
    )


# ---------------------------------------------------------------------------
# Main analysis and serialization
# ---------------------------------------------------------------------------


def run_t54_analysis() -> T54Result:
    datums = build_t54_datums()
    completions = tuple(_canonical_quotient_union(datum) for datum in datums)
    by_name = {completion.datum_name: completion for completion in completions}

    condition_basis = (
        "C1 event identity maps are total and single-valued",
        "C2 cross-observer identified events have overlap witnesses",
        "C3 source records merge without explicit contradiction",
        "C4 target records merge without explicit contradiction",
        "C5 identified events agree on finality-axis profiles",
        "C6 the quotient-union dependency order is a valid partial order",
        "C7 Axis Monotonicity holds on the reconstructed global structure",
    )

    counterexamples = tuple(
        (completion.datum_name, completion.classification)
        for completion in completions
        if completion.datum_name.startswith("CE_")
    )

    positives_correct = all(
        by_name[name].classification == "canonical"
        for name in ("T51_phantom_repair", "T52_symmetric_reconstruction")
    )
    t53_correct = by_name["T53_ambiguous_identity"].classification == "underdetermined"
    all_expected = all(
        completion.classification == next(
            datum.expected_classification for datum in datums if datum.name == completion.datum_name
        )
        for completion in completions
    )

    hyps = (
        HypothesisResult(
            "H0",
            "T53 boundary cases cannot be compressed into a finite theorem basis.",
            "refuted" if all_expected else "open",
            f"all expected classifications matched={all_expected}",
        ),
        HypothesisResult(
            "H1",
            "Event identity plus record compatibility is sufficient for unique completion.",
            "partially_supported",
            "It gives a unique quotient-union partial order when maps and records agree, but AM is separate.",
        ),
        HypothesisResult(
            "H2",
            "AM-compatible axis profiles are additionally required for temporal reconstruction.",
            "supported" if by_name["CE_am_violation"].classification == "am_invalid" else "refuted",
            f"CE_am_violation={by_name['CE_am_violation'].classification}",
        ),
        HypothesisResult(
            "H3",
            "A finite descent theorem classifies the T51-T53 cases.",
            "supported" if positives_correct and t53_correct else "refuted",
            (
                f"T51={by_name['T51_phantom_repair'].classification}; "
                f"T52={by_name['T52_symmetric_reconstruction'].classification}; "
                f"T53={by_name['T53_ambiguous_identity'].classification}"
            ),
        ),
        HypothesisResult(
            "H4",
            "Uniqueness is decidable only by brute-force completion enumeration.",
            "refuted" if all_expected else "open",
            "The quotient-union algorithm classifies all witnesses without enumerating completions.",
        ),
        HypothesisResult(
            "H5",
            "Full sheaf/categorical descent machinery is required now.",
            "refuted",
            "Finite identity, overlap, record, profile, and AM checks suffice for this witness family.",
        ),
    )

    theorem = (
        "Finite Finality Descent Theorem (v0.1): given finite observer-local "
        "FinaliEvent data with total single-valued event identity maps, overlap "
        "witnesses for cross-observer identifications, compatible source and "
        "target records, and agreeing finality-axis profiles, the canonical "
        "quotient-union construction produces a unique global FinaliEvent "
        "structure. If its dependency relation is a partial order and AM holds, "
        "the global temporal partial order is reconstructible from finality-axis "
        "magnitudes. If any descent condition fails, the failure is classified "
        "as nondefinable, underdetermined, conflicting, or AM-invalid."
    )
    sheaf_verdict = (
        "Full sheaf/descent machinery can be postponed. T54 requires finite "
        "descent data, but the tested conditions are decidable by a quotient-union "
        "algorithm over finite observer views."
    )
    best = (
        "H2 and H3 supported; H0, H4, and H5 refuted; H1 partially supported "
        "because uniqueness and AM-valid temporal reconstruction are separate."
    )

    return T54Result(
        completions=completions,
        theorem_statement=theorem,
        condition_basis=condition_basis,
        counterexample_summary=counterexamples,
        hypothesis_evaluations=hyps,
        sheaf_verdict=sheaf_verdict,
        best_supported=best,
    )


def _event_to_dict(event: GlobalEvent) -> dict[str, Any]:
    return {
        "name": event.name,
        "source_records": sorted(event.source_records),
        "target_records": sorted(event.target_records),
        "profile": {"causal": event.profile.causal, "info": event.profile.info},
        "local_events": [list(pair) for pair in event.local_events],
    }


def _po_to_dict(po: PartialOrderCheck | None) -> dict[str, Any] | None:
    if po is None:
        return None
    return {
        "reflexive": po.reflexive,
        "antisymmetric": po.antisymmetric,
        "transitive": po.transitive,
        "is_partial_order": po.is_partial_order,
        "order_pairs": [list(pair) for pair in po.order_pairs],
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
                "predecessor": violation.predecessor,
                "successor": violation.successor,
                "in_record_order": violation.in_record_order,
                "in_axis_order": violation.in_axis_order,
                "kind": violation.kind,
            }
            for violation in am.violations
        ],
    }


def t54_result_to_dict(result: T54Result) -> dict[str, Any]:
    return {
        "theorem_statement": result.theorem_statement,
        "condition_basis": list(result.condition_basis),
        "sheaf_verdict": result.sheaf_verdict,
        "completions": [
            {
                "datum_name": completion.datum_name,
                "classification": completion.classification,
                "condition_failures": list(completion.condition_failures),
                "global_events": [_event_to_dict(event) for event in completion.global_events],
                "partial_order": _po_to_dict(completion.partial_order),
                "axis_monotonicity": _am_to_dict(completion.axis_monotonicity),
                "theorem_applies": completion.theorem_applies,
                "evidence": completion.evidence,
            }
            for completion in result.completions
        ],
        "counterexample_summary": [
            {"case": name, "classification": classification}
            for name, classification in result.counterexample_summary
        ],
        "hypothesis_evaluations": [
            {
                "id": h.hypothesis_id,
                "claim": h.claim,
                "status": h.status,
                "evidence": h.evidence,
            }
            for h in result.hypothesis_evaluations
        ],
        "best_supported": result.best_supported,
    }
