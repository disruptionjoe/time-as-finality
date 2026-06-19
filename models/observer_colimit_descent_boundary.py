"""T53: Observer-colimit uniqueness and descent boundary audit.

T51 showed that merging observer record bases can recover an ordering that a
bounded observer could not see. T53 tests the next boundary: even when every
candidate merge is a valid partial order, the observer data may fail to
determine a unique event-finality structure.

This model separates three questions:

1. Partial-order existence: does a candidate completion produce a valid order?
2. Descent uniqueness: do the observer views determine one canonical completion?
3. Axis reconstruction: does finality-axis dominance reproduce record order?

The important negative result is not "colimits break." T47 protects the
partial-order side for well-formed PO1-admissible event structures. The T53
boundary is that consistency does not imply uniqueness or axis reconstructability.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Any


# ---------------------------------------------------------------------------
# Core finite objects
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    """Two-axis finality profile used by T49/T50: causal and information axes."""

    causal: int
    info: int

    def leq(self, other: "AxisProfile") -> bool:
        return self.causal <= other.causal and self.info <= other.info


@dataclass(frozen=True)
class EventRecord:
    """A finite event with source records, target records, and axis profile."""

    name: str
    source_records: frozenset[str]
    target_records: frozenset[str]
    profile: AxisProfile


@dataclass(frozen=True)
class ObserverView:
    """Observer-local apparent event data."""

    name: str
    events: tuple[EventRecord, ...]


@dataclass(frozen=True)
class EventMap:
    """Maps an observer-local event label to a global completion event label."""

    observer: str
    local_event: str
    global_event: str


@dataclass(frozen=True)
class CompletionCandidate:
    """A candidate global event-finality completion of several observer views."""

    name: str
    events: tuple[EventRecord, ...]
    event_maps: tuple[EventMap, ...]
    hidden_records: tuple[str, ...] = ()
    repair_kind: str = "none"
    interpretation: str = ""


@dataclass(frozen=True)
class DescentCase:
    """A T53 test case: observer views plus candidate completions."""

    name: str
    question: str
    observer_views: tuple[ObserverView, ...]
    completions: tuple[CompletionCandidate, ...]
    expected_boundary: str


@dataclass(frozen=True)
class PartialOrderCheck:
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    is_partial_order: bool
    order_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class AMViolation:
    event_j: str
    event_i: str
    in_record_order: bool
    in_axis_order: bool
    kind: str


@dataclass(frozen=True)
class AxisMonotonicityCheck:
    am_holds: bool
    violations: tuple[AMViolation, ...]
    spurious_count: int
    missing_count: int


@dataclass(frozen=True)
class CompletionEvaluation:
    completion_name: str
    compatible_with_views: bool
    compatibility_failures: tuple[str, ...]
    partial_order: PartialOrderCheck
    axis_monotonicity: AxisMonotonicityCheck
    hidden_records: tuple[str, ...]
    repair_kind: str
    signature: tuple[Any, ...]


@dataclass(frozen=True)
class CaseEvaluation:
    case_name: str
    expected_boundary: str
    evaluations: tuple[CompletionEvaluation, ...]
    compatible_completion_names: tuple[str, ...]
    distinct_compatible_signatures: int
    unique_completion: bool
    has_axis_valid_completion: bool
    has_axis_failing_completion: bool
    has_hidden_record_repair: bool
    verdict: str
    evidence: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T53Result:
    cases: tuple[CaseEvaluation, ...]
    theorem_statement: str
    descent_data_required: tuple[str, ...]
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# Order and axis checks
# ---------------------------------------------------------------------------


def _event_map(events: tuple[EventRecord, ...]) -> dict[str, EventRecord]:
    return {event.name: event for event in events}


def _record_order(events: tuple[EventRecord, ...]) -> frozenset[tuple[str, str]]:
    """Reflexive-transitive closure of target-record containment in source records."""

    names = [event.name for event in events]
    order: set[tuple[str, str]] = {(name, name) for name in names}

    for pred, succ in itertools.product(events, repeat=2):
        if pred.name == succ.name:
            continue
        if pred.target_records and pred.target_records <= succ.source_records:
            order.add((pred.name, succ.name))

    changed = True
    while changed:
        changed = False
        for a, b, c in itertools.product(names, repeat=3):
            if (a, b) in order and (b, c) in order and (a, c) not in order:
                order.add((a, c))
                changed = True

    return frozenset(order)


def _partial_order_check(events: tuple[EventRecord, ...]) -> PartialOrderCheck:
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


def _axis_monotonicity(events: tuple[EventRecord, ...]) -> AxisMonotonicityCheck:
    order = _record_order(events)
    event_by_name = _event_map(events)
    violations: list[AMViolation] = []

    for event_j, event_i in itertools.product(events, repeat=2):
        if event_j.name == event_i.name:
            continue
        in_record_order = (event_j.name, event_i.name) in order
        in_axis_order = event_by_name[event_j.name].profile.leq(event_by_name[event_i.name].profile)
        if in_record_order != in_axis_order:
            kind = "spurious_axis_order" if in_axis_order else "missing_axis_order"
            violations.append(AMViolation(
                event_j=event_j.name,
                event_i=event_i.name,
                in_record_order=in_record_order,
                in_axis_order=in_axis_order,
                kind=kind,
            ))

    return AxisMonotonicityCheck(
        am_holds=len(violations) == 0,
        violations=tuple(violations),
        spurious_count=sum(1 for v in violations if v.kind == "spurious_axis_order"),
        missing_count=sum(1 for v in violations if v.kind == "missing_axis_order"),
    )


def _completion_signature(completion: CompletionCandidate) -> tuple[Any, ...]:
    """Coarse finite signature used to detect non-isomorphic completions."""

    non_reflexive_order = tuple(
        pair for pair in _partial_order_check(completion.events).order_pairs if pair[0] != pair[1]
    )
    profile_signature = tuple(
        sorted((event.name, event.profile.causal, event.profile.info) for event in completion.events)
    )
    return (
        len(completion.events),
        non_reflexive_order,
        profile_signature,
        tuple(sorted(completion.hidden_records)),
    )


def _local_event(view: ObserverView, event_name: str) -> EventRecord | None:
    for event in view.events:
        if event.name == event_name:
            return event
    return None


def _check_completion_compatibility(
    case: DescentCase,
    completion: CompletionCandidate,
) -> tuple[bool, tuple[str, ...]]:
    global_events = _event_map(completion.events)
    failures: list[str] = []

    for view in case.observer_views:
        for local in view.events:
            mappings = [
                mapping for mapping in completion.event_maps
                if mapping.observer == view.name and mapping.local_event == local.name
            ]
            if not mappings:
                failures.append(f"{completion.name}: no event map for {view.name}.{local.name}")
                continue
            if len(mappings) > 1:
                failures.append(f"{completion.name}: multiple event maps for {view.name}.{local.name}")
                continue
            global_name = mappings[0].global_event
            global_event = global_events.get(global_name)
            if global_event is None:
                failures.append(f"{completion.name}: mapped global event missing: {global_name}")
                continue
            if not local.source_records <= global_event.source_records:
                failures.append(
                    f"{completion.name}: {view.name}.{local.name} source records are not a subset of {global_name}"
                )
            if not local.target_records <= global_event.target_records:
                failures.append(
                    f"{completion.name}: {view.name}.{local.name} target records are not a subset of {global_name}"
                )
            if local.profile != global_event.profile:
                failures.append(
                    f"{completion.name}: {view.name}.{local.name} profile conflicts with {global_name}"
                )

    return len(failures) == 0, tuple(failures)


def _evaluate_case(case: DescentCase) -> CaseEvaluation:
    evaluations: list[CompletionEvaluation] = []

    for completion in case.completions:
        compatible, failures = _check_completion_compatibility(case, completion)
        po = _partial_order_check(completion.events)
        am = _axis_monotonicity(completion.events)
        evaluations.append(CompletionEvaluation(
            completion_name=completion.name,
            compatible_with_views=compatible,
            compatibility_failures=failures,
            partial_order=po,
            axis_monotonicity=am,
            hidden_records=completion.hidden_records,
            repair_kind=completion.repair_kind,
            signature=_completion_signature(completion),
        ))

    compatible = tuple(ev for ev in evaluations if ev.compatible_with_views)
    compatible_names = tuple(ev.completion_name for ev in compatible)
    distinct_signatures = len({ev.signature for ev in compatible})
    unique_completion = len(compatible) == 1 and distinct_signatures == 1
    has_axis_valid = any(ev.axis_monotonicity.am_holds for ev in compatible)
    has_axis_failing = any(not ev.axis_monotonicity.am_holds for ev in compatible)
    has_repair = any(ev.repair_kind == "hidden_record_repair" for ev in compatible)

    if not compatible:
        verdict = "nondefinable_projection"
        evidence = "No candidate completion is compatible with all observer views."
    elif has_repair and has_axis_valid and has_axis_failing:
        verdict = "repairable_by_hidden_record"
        evidence = (
            "At least one compatible completion fails axis reconstruction, while a "
            "hidden-record completion restores AM."
        )
    elif distinct_signatures > 1:
        verdict = "underdetermined_noncanonical"
        evidence = (
            f"{len(compatible)} compatible completions remain, with "
            f"{distinct_signatures} distinct signatures."
        )
    elif unique_completion and has_axis_valid:
        verdict = "canonical_axis_reconstructable"
        evidence = "Exactly one compatible completion exists and AM holds."
    elif unique_completion and has_axis_failing:
        verdict = "valid_partial_order_axis_failure"
        evidence = "The completion is a valid partial order, but AM fails."
    else:
        verdict = "boundary_unclassified"
        evidence = "The finite diagnostics did not select a sharper class."

    return CaseEvaluation(
        case_name=case.name,
        expected_boundary=case.expected_boundary,
        evaluations=tuple(evaluations),
        compatible_completion_names=compatible_names,
        distinct_compatible_signatures=distinct_signatures,
        unique_completion=unique_completion,
        has_axis_valid_completion=has_axis_valid,
        has_axis_failing_completion=has_axis_failing,
        has_hidden_record_repair=has_repair,
        verdict=verdict,
        evidence=evidence,
    )


# ---------------------------------------------------------------------------
# Witness construction
# ---------------------------------------------------------------------------


def _ev(name: str, src: set[str], tgt: set[str], causal: int, info: int) -> EventRecord:
    return EventRecord(
        name=name,
        source_records=frozenset(src),
        target_records=frozenset(tgt),
        profile=AxisProfile(causal, info),
    )


def _maps(observer: str, pairs: tuple[tuple[str, str], ...]) -> tuple[EventMap, ...]:
    return tuple(EventMap(observer, local, global_) for local, global_ in pairs)


def _t51_positive_control() -> DescentCase:
    e1 = _ev("e1_A_locking", {"r_A_raw"}, {"r_A_locked"}, 2, 2)
    e2 = _ev("e2_B_locking", {"r_B_raw"}, {"r_B_locked"}, 1, 3)
    e3_full = _ev(
        "e3_composite_locking",
        {"r_A_locked", "r_B_locked", "r_composite_raw"},
        {"r_A_locked", "r_B_locked", "r_composite_locked"},
        3,
        4,
    )
    e3_restricted = _ev(
        "e3_composite_locking",
        {"r_B_locked", "r_composite_raw"},
        {"r_A_locked", "r_B_locked", "r_composite_locked"},
        3,
        4,
    )

    observer_a = ObserverView("Observer_A", (e1, e2, e3_full))
    observer_b = ObserverView("Observer_B", (e1, e2, e3_restricted))
    completion = CompletionCandidate(
        name="t51_colimit_completion",
        events=(e1, e2, e3_full),
        event_maps=_maps("Observer_A", (("e1_A_locking", "e1_A_locking"), ("e2_B_locking", "e2_B_locking"), ("e3_composite_locking", "e3_composite_locking")))
        + _maps("Observer_B", (("e1_A_locking", "e1_A_locking"), ("e2_B_locking", "e2_B_locking"), ("e3_composite_locking", "e3_composite_locking"))),
        hidden_records=("r_A_locked_for_Observer_B",),
        interpretation="Inherited T51-style positive control: one unique colimit restores a hidden ordering.",
    )
    return DescentCase(
        name="t51_positive_control",
        question="Can a bounded observer's phantom incomparability be repaired by a unique colimit?",
        observer_views=(observer_a, observer_b),
        completions=(completion,),
        expected_boundary="positive_control",
    )


def _ambiguous_event_identity_case() -> DescentCase:
    a1 = _ev("a1", {"a_raw"}, {"r_a"}, 1, 1)
    a2 = _ev("a2", {"r_a"}, {"r_a2"}, 2, 2)
    b1 = _ev("b1", {"b_raw"}, {"r_b"}, 1, 1)
    b2 = _ev("b2", {"r_b"}, {"r_b2"}, 2, 2)

    observer_a = ObserverView("Observer_A", (a1, a2))
    observer_b = ObserverView("Observer_B", (b1, b2))

    identified = CompletionCandidate(
        name="identified_two_event_completion",
        events=(
            _ev("e1", {"a_raw", "b_raw"}, {"r_a", "r_b"}, 1, 1),
            _ev("e2", {"r_a", "r_b"}, {"r_a2", "r_b2"}, 2, 2),
        ),
        event_maps=_maps("Observer_A", (("a1", "e1"), ("a2", "e2")))
        + _maps("Observer_B", (("b1", "e1"), ("b2", "e2"))),
        interpretation="Observers saw the same two events through different record labels.",
    )
    disjoint = CompletionCandidate(
        name="disjoint_four_event_completion",
        events=(a1, a2, b1, b2),
        event_maps=_maps("Observer_A", (("a1", "a1"), ("a2", "a2")))
        + _maps("Observer_B", (("b1", "b1"), ("b2", "b2"))),
        interpretation="Observers saw two independent chains with no shared event identity.",
    )
    return DescentCase(
        name="ambiguous_event_identity",
        question="Do observer views determine whether similarly-shaped local chains are identical or disjoint?",
        observer_views=(observer_a, observer_b),
        completions=(identified, disjoint),
        expected_boundary="underdetermined_noncanonical",
    )


def _axis_failing_case() -> DescentCase:
    e1 = _ev("e1_high_causal", {"raw_1"}, {"r_1"}, 2, 2)
    e2 = _ev("e2_lower_causal_successor", {"r_1"}, {"r_2"}, 1, 4)
    observer = ObserverView("Observer_A", (e1, e2))
    completion = CompletionCandidate(
        name="record_valid_axis_failing_completion",
        events=(e1, e2),
        event_maps=_maps("Observer_A", (("e1_high_causal", "e1_high_causal"), ("e2_lower_causal_successor", "e2_lower_causal_successor"))),
        interpretation="Record containment gives e1 <= e2, but causal axis decreases.",
    )
    return DescentCase(
        name="axis_failing_valid_colimit",
        question="Can the record colimit be valid while finality-axis reconstruction fails?",
        observer_views=(observer,),
        completions=(completion,),
        expected_boundary="valid_partial_order_axis_failure",
    )


def _hidden_record_repair_case() -> DescentCase:
    e1 = _ev("e1", {"raw_1"}, {"r_hidden_lock"}, 1, 1)
    e2_apparent = _ev("e2", {"raw_2"}, {"r_2"}, 2, 2)
    e2_repaired = _ev("e2", {"raw_2", "r_hidden_lock"}, {"r_2"}, 2, 2)

    observer_a = ObserverView("Observer_A", (e1, e2_apparent))
    observer_b = ObserverView("Observer_B", (e1, e2_apparent))

    unrepaired = CompletionCandidate(
        name="unrepaired_completion",
        events=(e1, e2_apparent),
        event_maps=_maps("Observer_A", (("e1", "e1"), ("e2", "e2")))
        + _maps("Observer_B", (("e1", "e1"), ("e2", "e2"))),
        interpretation="No hidden source record is added; axis order predicts an ordering absent from records.",
    )
    repaired = CompletionCandidate(
        name="hidden_record_repair_completion",
        events=(e1, e2_repaired),
        event_maps=_maps("Observer_A", (("e1", "e1"), ("e2", "e2")))
        + _maps("Observer_B", (("e1", "e1"), ("e2", "e2"))),
        hidden_records=("r_hidden_lock",),
        repair_kind="hidden_record_repair",
        interpretation="Adding the hidden predecessor record to e2 restores e1 <= e2 and AM.",
    )
    return DescentCase(
        name="hidden_record_repair",
        question="Can a hidden common record repair a mismatch between axis dominance and record order?",
        observer_views=(observer_a, observer_b),
        completions=(unrepaired, repaired),
        expected_boundary="repairable_by_hidden_record",
    )


def _nondefinable_overlap_case() -> DescentCase:
    a1 = _ev("a1", {"raw_a"}, {"r_a"}, 1, 1)
    b1 = _ev("b1", {"raw_b"}, {"r_b"}, 1, 1)
    observer_a = ObserverView("Observer_A", (a1,))
    observer_b = ObserverView("Observer_B", (b1,))
    bad_completion = CompletionCandidate(
        name="bad_incomplete_overlap_map",
        events=(a1,),
        event_maps=_maps("Observer_A", (("a1", "a1"),)),
        interpretation="Observer_B has no event map into the proposed completion.",
    )
    return DescentCase(
        name="nondefinable_overlap_boundary",
        question="What if a proposed completion lacks a map for one observer's event labels?",
        observer_views=(observer_a, observer_b),
        completions=(bad_completion,),
        expected_boundary="nondefinable_projection",
    )


def build_t53_cases() -> tuple[DescentCase, ...]:
    return (
        _t51_positive_control(),
        _ambiguous_event_identity_case(),
        _axis_failing_case(),
        _hidden_record_repair_case(),
        _nondefinable_overlap_case(),
    )


# ---------------------------------------------------------------------------
# Main analysis and serialization
# ---------------------------------------------------------------------------


def run_t53_analysis() -> T53Result:
    case_results = tuple(_evaluate_case(case) for case in build_t53_cases())
    case_by_name = {case.case_name: case for case in case_results}

    h0_supported = all(case.verdict == "canonical_axis_reconstructable" for case in case_results)
    h1_supported = all(case.unique_completion for case in case_results if case.compatible_completion_names)
    all_compatible_pos_are_po = all(
        ev.partial_order.is_partial_order
        for case in case_results
        for ev in case.evaluations
        if ev.compatible_with_views
    )
    h2_supported = (
        all_compatible_pos_are_po
        and case_by_name["ambiguous_event_identity"].verdict == "underdetermined_noncanonical"
    )
    h3_supported = (
        case_by_name["axis_failing_valid_colimit"].verdict == "valid_partial_order_axis_failure"
    )
    h4_supported = (
        case_by_name["hidden_record_repair"].verdict == "repairable_by_hidden_record"
        and case_by_name["ambiguous_event_identity"].verdict == "underdetermined_noncanonical"
    )
    h5_status = "partially_supported" if h2_supported and h4_supported else "open"

    hyps = (
        HypothesisResult(
            "H0",
            "T51/T52-style positive colimits cover all meaningful multi-observer merges.",
            "refuted" if not h0_supported else "supported",
            "Boundary cases include underdetermined identity, AM failure, repair, and non-definable overlap.",
        ),
        HypothesisResult(
            "H1",
            "Every compatible observer merge has a unique canonical event-finality completion.",
            "refuted" if not h1_supported else "supported",
            f"ambiguous_event_identity unique={case_by_name['ambiguous_event_identity'].unique_completion}",
        ),
        HypothesisResult(
            "H2",
            "Partial-order validity can hold while uniqueness requires extra descent data.",
            "supported" if h2_supported else "refuted",
            (
                f"all compatible completions partial orders={all_compatible_pos_are_po}; "
                f"ambiguous verdict={case_by_name['ambiguous_event_identity'].verdict}"
            ),
        ),
        HypothesisResult(
            "H3",
            "Record-order colimits can remain valid while finality-axis reconstruction fails.",
            "supported" if h3_supported else "refuted",
            f"axis case verdict={case_by_name['axis_failing_valid_colimit'].verdict}",
        ),
        HypothesisResult(
            "H4",
            "Some boundary failures are hidden-record repairable; others remain noncanonical.",
            "supported" if h4_supported else "refuted",
            (
                f"repair verdict={case_by_name['hidden_record_repair'].verdict}; "
                f"identity verdict={case_by_name['ambiguous_event_identity'].verdict}"
            ),
        ),
        HypothesisResult(
            "H5",
            "A stronger descent-style formalism is required beyond pointwise record union.",
            h5_status,
            "Finite descent data are required, but full sheaf machinery is not yet forced.",
        ),
    )

    theorem = (
        "Observer-Colimit Descent Boundary Theorem (finite v0.1): "
        "For finite FinaliEvent-style record systems, T47-style acyclicity can "
        "protect partial-order consistency of each compatible completion, but "
        "it does not guarantee that bounded observer views determine a unique "
        "global event-finality structure. Canonical reconstruction additionally "
        "requires event-identity maps, sufficient overlap data, and AM-compatible "
        "axis profiles when temporal order is reconstructed from finality axes."
    )

    best = (
        "H2, H3, and H4 supported; H0 and H1 refuted; H5 partially supported "
        "as finite descent data, not full sheaf machinery."
    )

    return T53Result(
        cases=case_results,
        theorem_statement=theorem,
        descent_data_required=(
            "event identity maps across observer-local labels",
            "record-overlap data sufficient to distinguish hidden repair from arbitrary completion",
            "axis profiles satisfying AM when axis dominance is used as temporal reconstruction",
            "a nondefinable-boundary check for missing site/event maps",
        ),
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


def _po_to_dict(po: PartialOrderCheck) -> dict[str, Any]:
    return {
        "reflexive": po.reflexive,
        "antisymmetric": po.antisymmetric,
        "transitive": po.transitive,
        "is_partial_order": po.is_partial_order,
        "order_pairs": [list(pair) for pair in po.order_pairs],
    }


def _am_to_dict(am: AxisMonotonicityCheck) -> dict[str, Any]:
    return {
        "am_holds": am.am_holds,
        "spurious_count": am.spurious_count,
        "missing_count": am.missing_count,
        "violations": [
            {
                "event_j": violation.event_j,
                "event_i": violation.event_i,
                "in_record_order": violation.in_record_order,
                "in_axis_order": violation.in_axis_order,
                "kind": violation.kind,
            }
            for violation in am.violations
        ],
    }


def t53_result_to_dict(result: T53Result) -> dict[str, Any]:
    return {
        "theorem_statement": result.theorem_statement,
        "descent_data_required": list(result.descent_data_required),
        "cases": [
            {
                "case_name": case.case_name,
                "expected_boundary": case.expected_boundary,
                "compatible_completion_names": list(case.compatible_completion_names),
                "distinct_compatible_signatures": case.distinct_compatible_signatures,
                "unique_completion": case.unique_completion,
                "has_axis_valid_completion": case.has_axis_valid_completion,
                "has_axis_failing_completion": case.has_axis_failing_completion,
                "has_hidden_record_repair": case.has_hidden_record_repair,
                "verdict": case.verdict,
                "evidence": case.evidence,
                "evaluations": [
                    {
                        "completion_name": ev.completion_name,
                        "compatible_with_views": ev.compatible_with_views,
                        "compatibility_failures": list(ev.compatibility_failures),
                        "partial_order": _po_to_dict(ev.partial_order),
                        "axis_monotonicity": _am_to_dict(ev.axis_monotonicity),
                        "hidden_records": list(ev.hidden_records),
                        "repair_kind": ev.repair_kind,
                        "signature": repr(ev.signature),
                    }
                    for ev in case.evaluations
                ],
            }
            for case in result.cases
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
