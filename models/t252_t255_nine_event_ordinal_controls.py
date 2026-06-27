"""T252-T255: nine-event ordinal controls after the T249 grid demotion.

T249 built a T54-native nine-event product-grid colimit. T250 and T251 showed
that the grid is stably too ordered for the declared flat 1+1 ordering-fraction
band. This module adds a controlled contrast: a fixed nine-event ordinal
permutation that is T54-native, clears T126, lands inside the T156 band, and
stays inside the band after every single-event deletion.

The comparison is finite and control-only. It does not override the existing
T223 finite no-go for the uniform ordinal ensemble and does not upgrade S1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    CausetAudit,
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.finality_descent_theorem import (
    AxisProfile,
    CompletionResult,
    EventIdentityMap,
    LocalEvent,
    ObserverDescentDatum,
    ObserverView,
    complete_observer_descent_datum,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    OrderingFractionTarget,
    T156Audit,
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t249_larger_t54_t126_colimit import run_t249_analysis
from models.t251_t249_deletion_stability import run_t251_analysis


Event = str
OrderPair = tuple[Event, Event]

NINE_EVENT_ORDINAL_PERMUTATION: tuple[int, ...] = (0, 5, 6, 7, 8, 1, 2, 3, 4)


@dataclass(frozen=True)
class T252Result:
    permutation: tuple[int, ...]
    completion: CompletionResult
    t126_audit: CausetAudit
    t156_audit: T156Audit
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T253DeletionAudit:
    removed_event: Event
    t126_classification: str
    t126_filter_passed: bool
    event_count: int
    strict_pair_count: int
    ordering_fraction: Fraction
    ordering_band_passed: bool
    height: int
    width: int
    verdict: str


@dataclass(frozen=True)
class T253Result:
    parent_ordering_fraction: Fraction
    parent_band_passed: bool
    deletion_audits: tuple[T253DeletionAudit, ...]
    deletion_case_count: int
    deletion_t126_pass_count: int
    deletion_band_pass_count: int
    deletion_band_pass_rate: Fraction
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T254Result:
    grid_ordering_fraction: Fraction
    grid_band_passed: bool
    grid_deletion_band_pass_count: int
    ordinal_ordering_fraction: Fraction
    ordinal_band_passed: bool
    ordinal_deletion_band_pass_count: int
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


@dataclass(frozen=True)
class T255MutationAudit:
    swapped_positions: tuple[int, int]
    permutation: tuple[int, ...]
    t126_classification: str
    t126_filter_passed: bool
    ordering_fraction: Fraction
    ordering_band_passed: bool
    height: int
    width: int


@dataclass(frozen=True)
class T255Result:
    mutation_audits: tuple[T255MutationAudit, ...]
    mutation_count: int
    t126_pass_and_band_count: int
    t126_pass_outside_band_count: int
    t126_blocked_inside_band_count: int
    band_total_count: int
    verdict: str
    strongest_claim: str
    improved: str
    weakened_or_falsified: str
    falsification_condition: str
    s1_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str
    not_claimed: str


NOT_CLAIMED = (
    "These controls do not estimate dimension, prove faithful embedding, "
    "validate random sprinkling, derive metric structure, or settle S1."
)


def run_t252_analysis() -> T252Result:
    completion = complete_observer_descent_datum(_ordinal_datum())
    t126_audit = audit_finality_colimit_causet(_completion_to_t126_datum(completion))
    t156_audit = audit_ordering_fraction_target(
        _completion_to_t126_datum(completion),
        target=flat_1p1_interval_target(),
    )
    verdict = (
        "nine_event_t54_ordinal_band_control"
        if completion.theorem_applies
        and t126_audit.manifold_filter_passed
        and t156_audit.verdict == "passes_ordering_fraction_control_only"
        else "unexpected_nine_event_ordinal_status"
    )
    return T252Result(
        permutation=NINE_EVENT_ORDINAL_PERMUTATION,
        completion=completion,
        t126_audit=t126_audit,
        t156_audit=t156_audit,
        verdict=verdict,
        strongest_claim=(
            "A fixed nine-event ordinal T54 datum clears T126 and lands inside "
            "the declared flat 1+1 ordering-fraction band with fraction 5/9."
        ),
        improved=(
            "T252 gives the T249 grid a same-scale, T54-native contrast case "
            "that is not a product lattice and is not automatically over-ordered."
        ),
        weakened_or_falsified=(
            "This falsifies the narrow post-T251 blocker that no T54-native "
            "nine-event witness can match the declared ordering-fraction band. "
            "It does not weaken the broader T223 rare-tail/no-concentration "
            "verdict for the uniform ordinal ensemble."
        ),
        falsification_condition=(
            "T252 fails if the T54 completion is not canonical, if T126 and "
            "T156 are not run on the same strict relation, or if this selected "
            "finite witness is treated as typical or continuum-facing."
        ),
        s1_update=(
            "S1 remains requires_added_assumption/open_formal_target. This is "
            "a selected finite control, not a generative spacetime route."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T252 alone. Safe future "
            "wording: one selected nine-event T54-native ordinal control "
            "passes T126 and the declared T156 ordering-fraction band."
        ),
        open_blocker=(
            "No generative law, abundance result, locality diagnostic, "
            "sprinkling comparison, embedding theorem, or continuum bridge is "
            "attached to this selected witness."
        ),
        suggested_next=(
            "Test deletion stability and mutation sensitivity before treating "
            "the witness as more than a same-scale control."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t253_analysis() -> T253Result:
    t252 = run_t252_analysis()
    assert t252.t126_audit.diagnostics is not None
    target = flat_1p1_interval_target()
    deletion_audits = tuple(
        _deletion_audit(event, target)
        for event in _event_names(NINE_EVENT_ORDINAL_PERMUTATION)
    )
    t126_pass_count = sum(1 for audit in deletion_audits if audit.t126_filter_passed)
    band_pass_count = sum(1 for audit in deletion_audits if audit.ordering_band_passed)
    case_count = len(deletion_audits)
    pass_rate = _fraction(band_pass_count, case_count)
    verdict = (
        "nine_event_ordinal_deletion_stable_band_control"
        if t126_pass_count == case_count and band_pass_count == case_count
        else "mixed_nine_event_ordinal_deletion_status"
    )
    return T253Result(
        parent_ordering_fraction=t252.t126_audit.diagnostics.comparable_fraction,
        parent_band_passed=target.accepts(t252.t126_audit.diagnostics.comparable_fraction),
        deletion_audits=deletion_audits,
        deletion_case_count=case_count,
        deletion_t126_pass_count=t126_pass_count,
        deletion_band_pass_count=band_pass_count,
        deletion_band_pass_rate=pass_rate,
        verdict=verdict,
        strongest_claim=(
            "The selected T252 nine-event ordinal witness is stable under every "
            "single-event deletion for the current finite screens: all nine "
            "deletions pass T126 and stay inside the declared ordering band."
        ),
        improved=(
            "T253 supplies the deletion-stability contrast missing from T252 "
            "and separates it from the T249 grid, whose deletions all failed "
            "the same band."
        ),
        weakened_or_falsified=(
            "This weakens only the specific T249-style over-ordering concern. "
            "It does not show that such witnesses are common, natural, local, "
            "sprinkling-like, or continuum-relevant."
        ),
        falsification_condition=(
            "T253 fails if deletion suborders are not restrictions of the "
            "T252 quotient-union relation, if any deletion leaves the declared "
            "band without being reported, or if finite deletion stability is "
            "promoted into a continuum claim."
        ),
        s1_update=(
            "S1 remains guarded. The selected witness is deletion-stable under "
            "the declared finite screens only."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T253 alone. Safe future "
            "wording: the selected T252 witness is single-deletion stable for "
            "T126 and T156."
        ),
        open_blocker=(
            "Deletion stability has not been connected to a selection measure, "
            "locality law, random sprinkling ensemble, or Lorentzian data."
        ),
        suggested_next=(
            "Compare the T252 witness against the T249 grid and run a small "
            "mutation screen to estimate finite sensitivity."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t254_analysis() -> T254Result:
    target = flat_1p1_interval_target()
    grid = run_t249_analysis()
    grid_deletions = run_t251_analysis()
    ordinal = run_t252_analysis()
    ordinal_deletions = run_t253_analysis()
    assert grid.t126_audit.diagnostics is not None
    assert ordinal.t126_audit.diagnostics is not None
    grid_fraction = grid.t126_audit.diagnostics.comparable_fraction
    ordinal_fraction = ordinal.t126_audit.diagnostics.comparable_fraction
    verdict = (
        "same_scale_contrast_control_only"
        if not target.accepts(grid_fraction)
        and target.accepts(ordinal_fraction)
        and grid_deletions.deletion_band_pass_count == 0
        and ordinal_deletions.deletion_band_pass_count == 9
        else "mixed_same_scale_comparison_status"
    )
    return T254Result(
        grid_ordering_fraction=grid_fraction,
        grid_band_passed=target.accepts(grid_fraction),
        grid_deletion_band_pass_count=grid_deletions.deletion_band_pass_count,
        ordinal_ordering_fraction=ordinal_fraction,
        ordinal_band_passed=target.accepts(ordinal_fraction),
        ordinal_deletion_band_pass_count=ordinal_deletions.deletion_band_pass_count,
        verdict=verdict,
        strongest_claim=(
            "At the same nine-event scale, T249 and T252 separate two finite "
            "behaviors: the grid is stably over-ordered, while the selected "
            "ordinal witness is deletion-stable inside the declared band."
        ),
        improved=(
            "T254 turns the T249/T252 pair into an explicit comparison rather "
            "than two isolated examples."
        ),
        weakened_or_falsified=(
            "The comparison weakens product-grid optimism, not the existing "
            "T223 finite no-go. A selected positive control does not imply "
            "typicality or concentration."
        ),
        falsification_condition=(
            "T254 fails if the compared witnesses are not audited through the "
            "same T126/T156 targets, if deletion pass counts are misreported, "
            "or if the contrast is read as an S1 upgrade."
        ),
        s1_update=(
            "S1 remains guarded. The contrast identifies candidate shape as "
            "important but does not provide a generative or continuum argument."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T254 alone. Safe future "
            "wording: same-scale T54-native controls can diverge sharply under "
            "the T156 band and deletion screen."
        ),
        open_blocker=(
            "The repo still lacks a principled rule selecting the ordinal "
            "control over the grid or over the broader rare-tail ensemble."
        ),
        suggested_next=(
            "Run a local mutation screen around the selected ordinal witness "
            "to see whether the positive behavior is isolated or nearby."
        ),
        not_claimed=NOT_CLAIMED,
    )


def run_t255_analysis() -> T255Result:
    target = flat_1p1_interval_target()
    audits = tuple(
        _mutation_audit(left, right, target)
        for left, right in combinations(range(len(NINE_EVENT_ORDINAL_PERMUTATION)), 2)
    )
    t126_pass_and_band = sum(
        1 for audit in audits if audit.t126_filter_passed and audit.ordering_band_passed
    )
    t126_pass_outside = sum(
        1 for audit in audits if audit.t126_filter_passed and not audit.ordering_band_passed
    )
    blocked_inside = sum(
        1 for audit in audits if (not audit.t126_filter_passed) and audit.ordering_band_passed
    )
    band_total = sum(1 for audit in audits if audit.ordering_band_passed)
    verdict = (
        "mutation_neighborhood_mixed_but_band_common"
        if len(audits) == 36
        and t126_pass_and_band == 21
        and t126_pass_outside == 2
        and blocked_inside == 13
        else "unexpected_mutation_neighborhood_status"
    )
    return T255Result(
        mutation_audits=audits,
        mutation_count=len(audits),
        t126_pass_and_band_count=t126_pass_and_band,
        t126_pass_outside_band_count=t126_pass_outside,
        t126_blocked_inside_band_count=blocked_inside,
        band_total_count=band_total,
        verdict=verdict,
        strongest_claim=(
            "In the 36 one-transposition neighbors of the T252 permutation, "
            "21 still pass both T126 and the ordering band, 13 remain inside "
            "the band but are blocked by T126, and 2 pass T126 outside the band."
        ),
        improved=(
            "T255 shows the T252 witness is not a single isolated permutation, "
            "but the T126 shape filter still matters inside its local mutation "
            "neighborhood."
        ),
        weakened_or_falsified=(
            "The result weakens both extremes: T252 is not unique, but its "
            "neighborhood is not uniformly good enough to support an S1 upgrade."
        ),
        falsification_condition=(
            "T255 fails if mutations are not single transpositions of the "
            "declared permutation, if T126/T156 targets differ from T252, or "
            "if local mutation abundance is treated as a global ensemble result."
        ),
        s1_update=(
            "S1 remains guarded. Mutation-local abundance is a search hint, not "
            "a selection law or continuum bridge."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T255 alone. Safe future "
            "wording: the selected ordinal witness has nearby finite controls, "
            "but the local neighborhood is mixed under T126."
        ),
        open_blocker=(
            "No global abundance, measure, locality, sprinkling, or Lorentzian "
            "selection principle has been derived for the positive neighborhood."
        ),
        suggested_next=(
            "If continuing, run a bounded exact n=9 class count or a stricter "
            "locality diagnostic, rather than adding more hand-picked examples."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _ordinal_datum() -> ObserverDescentDatum:
    permutation = NINE_EVENT_ORDINAL_PERMUTATION
    profiles = {
        _event_name(index): AxisProfile(causal=index + 1, info=value + 1)
        for index, value in enumerate(permutation)
    }
    strict_pairs = _strict_pairs_for_permutation(permutation)
    observers = ("A", "B")
    views = tuple(
        ObserverView(
            observer,
            tuple(
                _local_event(
                    observer=observer,
                    event=event,
                    profile=profiles[event],
                    predecessors=frozenset(
                        left for left, right in strict_pairs if right == event
                    ),
                )
                for event in sorted(profiles)
            ),
        )
        for observer in observers
    )
    identity_maps = tuple(
        EventIdentityMap(observer=observer, local_event=event, global_event=event)
        for observer in observers
        for event in sorted(profiles)
    )
    return ObserverDescentDatum(
        name="T252_nine_event_ordinal_band_control",
        description=(
            "Two agreeing observer views whose T54 quotient-union realizes a "
            "selected nine-event ordinal 1+1 control."
        ),
        observer_views=views,
        identity_maps=identity_maps,
        overlap_witnesses=frozenset(profiles),
        expected_classification="canonical",
    )


def _local_event(
    *,
    observer: str,
    event: Event,
    profile: AxisProfile,
    predecessors: frozenset[Event],
) -> LocalEvent:
    return LocalEvent(
        observer=observer,
        name=event,
        source_records=frozenset({f"raw_{event}"} | {f"locked_{p}" for p in predecessors}),
        target_records=frozenset({f"locked_{event}"}),
        profile=profile,
    )


def _event_name(index: int) -> Event:
    return f"e{index}"


def _event_names(permutation: tuple[int, ...]) -> tuple[Event, ...]:
    return tuple(_event_name(index) for index in range(len(permutation)))


def _strict_pairs_for_permutation(permutation: tuple[int, ...]) -> frozenset[OrderPair]:
    return frozenset(
        (_event_name(left), _event_name(right))
        for left in range(len(permutation))
        for right in range(len(permutation))
        if left < right and permutation[left] < permutation[right]
    )


def _completion_to_t126_datum(completion: CompletionResult) -> FinalityColimitCausetDatum:
    events = frozenset(event.name for event in completion.global_events)
    relation = (
        frozenset(completion.partial_order.order_pairs)
        if completion.partial_order is not None
        else non_strict_relation(events, frozenset())
    )
    return FinalityColimitCausetDatum(
        name="t252_nine_event_ordinal_band_control",
        events=events,
        relation=relation,
        descent_gate_passed=completion.theorem_applies,
        canonical_colimit=completion.classification == "canonical",
        phantom_gap_resolved=completion.theorem_applies,
        observer_only_gap_changes_strict_order=False,
        source="T252 selected nine-event ordinal T54 quotient-union completion",
    )


def _permutation_to_t126_datum(
    permutation: tuple[int, ...],
    *,
    name: str,
    minimum_events_for_manifold_filter: int | None = None,
) -> FinalityColimitCausetDatum:
    events = frozenset(_event_names(permutation))
    strict = _strict_pairs_for_permutation(permutation)
    return FinalityColimitCausetDatum(
        name=name,
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source="T252/T255 ordinal permutation control",
        minimum_events_for_manifold_filter=(
            minimum_events_for_manifold_filter
            if minimum_events_for_manifold_filter is not None
            else len(events)
        ),
    )


def _deletion_datum(removed_event: Event) -> FinalityColimitCausetDatum:
    parent_events = frozenset(_event_names(NINE_EVENT_ORDINAL_PERMUTATION))
    parent_strict = _strict_pairs_for_permutation(NINE_EVENT_ORDINAL_PERMUTATION)
    events = frozenset(event for event in parent_events if event != removed_event)
    strict = frozenset(
        (left, right)
        for left, right in parent_strict
        if left in events and right in events
    )
    return FinalityColimitCausetDatum(
        name=f"t253_t252_delete_{removed_event}",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source=f"single-event deletion of T252 removing {removed_event}",
        minimum_events_for_manifold_filter=len(events),
    )


def _deletion_audit(
    removed_event: Event,
    target: OrderingFractionTarget,
) -> T253DeletionAudit:
    datum = _deletion_datum(removed_event)
    t126_audit = audit_finality_colimit_causet(datum)
    t156_audit = audit_ordering_fraction_target(datum, target=target)
    diagnostics = t126_audit.diagnostics
    if diagnostics is None:
        raise AssertionError("T252 deletion audits should produce diagnostics")
    ordering_band_passed = target.accepts(diagnostics.comparable_fraction)
    verdict = (
        "t126_pass_and_ordering_fraction_pass"
        if t126_audit.manifold_filter_passed and ordering_band_passed
        else t156_audit.verdict
    )
    return T253DeletionAudit(
        removed_event=removed_event,
        t126_classification=t126_audit.classification,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        event_count=diagnostics.event_count,
        strict_pair_count=diagnostics.strict_pair_count,
        ordering_fraction=diagnostics.comparable_fraction,
        ordering_band_passed=ordering_band_passed,
        height=diagnostics.height,
        width=diagnostics.width,
        verdict=verdict,
    )


def _mutation_audit(
    left: int,
    right: int,
    target: OrderingFractionTarget,
) -> T255MutationAudit:
    mutated = list(NINE_EVENT_ORDINAL_PERMUTATION)
    mutated[left], mutated[right] = mutated[right], mutated[left]
    permutation = tuple(mutated)
    datum = _permutation_to_t126_datum(
        permutation,
        name=f"t255_swap_{left}_{right}",
    )
    t126_audit = audit_finality_colimit_causet(datum)
    diagnostics = t126_audit.diagnostics
    if diagnostics is None:
        raise AssertionError("T252 mutation audits should produce diagnostics")
    return T255MutationAudit(
        swapped_positions=(left, right),
        permutation=permutation,
        t126_classification=t126_audit.classification,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        ordering_fraction=diagnostics.comparable_fraction,
        ordering_band_passed=target.accepts(diagnostics.comparable_fraction),
        height=diagnostics.height,
        width=diagnostics.width,
    )


def t252_result_to_dict(result: T252Result) -> dict[str, Any]:
    diagnostics = result.t126_audit.diagnostics
    return {
        "permutation": list(result.permutation),
        "t54_classification": result.completion.classification,
        "t54_theorem_applies": result.completion.theorem_applies,
        "condition_failures": list(result.completion.condition_failures),
        "t126_classification": result.t126_audit.classification,
        "t126_filter_passed": result.t126_audit.manifold_filter_passed,
        "event_count": diagnostics.event_count if diagnostics is not None else None,
        "strict_pair_count": diagnostics.strict_pair_count if diagnostics is not None else None,
        "ordering_fraction": (
            _fraction_to_dict(diagnostics.comparable_fraction)
            if diagnostics is not None
            else None
        ),
        "height": diagnostics.height if diagnostics is not None else None,
        "width": diagnostics.width if diagnostics is not None else None,
        "t156_verdict": result.t156_audit.verdict,
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def t253_result_to_dict(result: T253Result) -> dict[str, Any]:
    return {
        "parent_ordering_fraction": _fraction_to_dict(result.parent_ordering_fraction),
        "parent_band_passed": result.parent_band_passed,
        "deletion_audits": [_t253_deletion_to_dict(audit) for audit in result.deletion_audits],
        "deletion_case_count": result.deletion_case_count,
        "deletion_t126_pass_count": result.deletion_t126_pass_count,
        "deletion_band_pass_count": result.deletion_band_pass_count,
        "deletion_band_pass_rate": _fraction_to_dict(result.deletion_band_pass_rate),
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def t254_result_to_dict(result: T254Result) -> dict[str, Any]:
    return {
        "grid_ordering_fraction": _fraction_to_dict(result.grid_ordering_fraction),
        "grid_band_passed": result.grid_band_passed,
        "grid_deletion_band_pass_count": result.grid_deletion_band_pass_count,
        "ordinal_ordering_fraction": _fraction_to_dict(result.ordinal_ordering_fraction),
        "ordinal_band_passed": result.ordinal_band_passed,
        "ordinal_deletion_band_pass_count": result.ordinal_deletion_band_pass_count,
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def t255_result_to_dict(result: T255Result) -> dict[str, Any]:
    return {
        "mutation_audits": [_mutation_to_dict(audit) for audit in result.mutation_audits],
        "mutation_count": result.mutation_count,
        "t126_pass_and_band_count": result.t126_pass_and_band_count,
        "t126_pass_outside_band_count": result.t126_pass_outside_band_count,
        "t126_blocked_inside_band_count": result.t126_blocked_inside_band_count,
        "band_total_count": result.band_total_count,
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened_or_falsified": result.weakened_or_falsified,
        "falsification_condition": result.falsification_condition,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
        "not_claimed": result.not_claimed,
    }


def _t253_deletion_to_dict(audit: T253DeletionAudit) -> dict[str, Any]:
    return {
        "removed_event": audit.removed_event,
        "t126_classification": audit.t126_classification,
        "t126_filter_passed": audit.t126_filter_passed,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "ordering_band_passed": audit.ordering_band_passed,
        "height": audit.height,
        "width": audit.width,
        "verdict": audit.verdict,
    }


def _mutation_to_dict(audit: T255MutationAudit) -> dict[str, Any]:
    return {
        "swapped_positions": list(audit.swapped_positions),
        "permutation": list(audit.permutation),
        "t126_classification": audit.t126_classification,
        "t126_filter_passed": audit.t126_filter_passed,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "ordering_band_passed": audit.ordering_band_passed,
        "height": audit.height,
        "width": audit.width,
    }


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
