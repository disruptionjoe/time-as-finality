"""T251: single-deletion stability screen for the T249 grid witness.

T250 shows that the T249 grid is too ordered for the declared flat 1+1
ordering-fraction band. T251 asks whether that failure is fragile. It is not:
every single-event deletion still clears T126 but remains outside the declared
ordering-fraction band.

This is a robustness demotion of one finite witness, not a general no-go.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.finality_colimit_causal_set_embeddability import (
    FinalityColimitCausetDatum,
    audit_finality_colimit_causet,
    non_strict_relation,
)
from models.myrheim_meyer_ordering_fraction_screen import (
    OrderingFractionTarget,
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t249_larger_t54_t126_colimit import run_t249_analysis


Event = str
OrderPair = tuple[Event, Event]


@dataclass(frozen=True)
class T251DeletionAudit:
    removed_event: Event
    t126_classification: str
    t126_filter_passed: bool
    event_count: int
    strict_pair_count: int
    ordering_fraction: Fraction
    ordering_band_passed: bool
    height: int
    width: int
    interval_counts_by_size: tuple[tuple[int, int], ...]
    verdict: str


@dataclass(frozen=True)
class T251Result:
    target: OrderingFractionTarget
    parent_ordering_fraction: Fraction
    parent_band_passed: bool
    deletion_audits: tuple[T251DeletionAudit, ...]
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


NOT_CLAIMED = (
    "T251 does not prove a continuum no-go, estimate dimension, validate or "
    "falsify random sprinkling in general, derive metric structure, or settle S1."
)


def run_t251_analysis() -> T251Result:
    target = flat_1p1_interval_target()
    t249 = run_t249_analysis()
    assert t249.t126_audit.diagnostics is not None
    parent_fraction = t249.t126_audit.diagnostics.comparable_fraction
    parent_band_passed = target.accepts(parent_fraction)
    deletion_audits = tuple(_deletion_audit(event, target) for event in _event_names())
    t126_pass_count = sum(1 for audit in deletion_audits if audit.t126_filter_passed)
    band_pass_count = sum(1 for audit in deletion_audits if audit.ordering_band_passed)
    case_count = len(deletion_audits)
    pass_rate = _fraction(band_pass_count, case_count)
    verdict = (
        "stable_over_ordering_under_single_deletion"
        if t126_pass_count == case_count and band_pass_count == 0
        else "mixed_t249_deletion_status"
    )

    return T251Result(
        target=target,
        parent_ordering_fraction=parent_fraction,
        parent_band_passed=parent_band_passed,
        deletion_audits=deletion_audits,
        deletion_case_count=case_count,
        deletion_t126_pass_count=t126_pass_count,
        deletion_band_pass_count=band_pass_count,
        deletion_band_pass_rate=pass_rate,
        verdict=verdict,
        strongest_claim=(
            "The T249 grid's ordering-fraction failure is stable under every "
            "single-event deletion tested here: all nine deletions still clear "
            "T126, and none enter the declared flat 1+1 band."
        ),
        improved=(
            "T251 distinguishes a fragile diagnostic failure from a structural "
            "one for the T249 witness. The over-ordering is not caused by one "
            "special grid event."
        ),
        weakened_or_falsified=(
            "This further weakens T249 as an S1-facing candidate. The witness "
            "is useful as a T54/T126 construction control, but its mismatch "
            "with the declared 1+1 ordering band survives all single deletions."
        ),
        falsification_condition=(
            "T251 fails if deletion suborders are not computed from the same "
            "T249 quotient-union relation, if T126 and T156 use different "
            "strict relations, or if this finite deletion result is treated as "
            "a general continuum or sprinkling theorem."
        ),
        s1_update=(
            "S1 remains open_formal_target. T249 should be treated as a stable "
            "over-ordered finite control, not as spacetime-facing residue."
        ),
        claim_ledger_update=(
            "Do not update the claim ledger from T251 alone. Safe future "
            "wording: T249's T156 failure is stable under all single-event "
            "deletions while T126 continues to pass."
        ),
        open_blocker=(
            "No deletion-stable T54-native nine-event witness has been found "
            "inside the declared flat 1+1 ordering-fraction band."
        ),
        suggested_next=(
            "Search beyond lattice-grid witnesses for T54-native candidates "
            "whose parent and deletion suborders both match the declared band, "
            "then apply locality and sprinkling comparisons."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _event_names() -> tuple[Event, ...]:
    return tuple(sorted(event.name for event in run_t249_analysis().completion.global_events))


def _parent_relation() -> tuple[frozenset[Event], frozenset[OrderPair]]:
    completion = run_t249_analysis().completion
    events = frozenset(event.name for event in completion.global_events)
    strict = frozenset(
        (left, right)
        for left, right in completion.partial_order.order_pairs
        if left != right
    )
    return events, strict


def _deletion_datum(removed_event: Event) -> FinalityColimitCausetDatum:
    parent_events, parent_strict = _parent_relation()
    events = frozenset(event for event in parent_events if event != removed_event)
    strict = frozenset(
        (left, right)
        for left, right in parent_strict
        if left in events and right in events
    )
    return FinalityColimitCausetDatum(
        name=f"t251_t249_delete_{removed_event}",
        events=events,
        relation=non_strict_relation(events, strict),
        descent_gate_passed=True,
        canonical_colimit=True,
        phantom_gap_resolved=True,
        observer_only_gap_changes_strict_order=False,
        source=f"single-event deletion of T249 removing {removed_event}",
        minimum_events_for_manifold_filter=max(1, len(events)),
    )


def _deletion_audit(
    removed_event: Event,
    target: OrderingFractionTarget,
) -> T251DeletionAudit:
    datum = _deletion_datum(removed_event)
    t126_audit = audit_finality_colimit_causet(datum)
    t156_audit = audit_ordering_fraction_target(datum, target=target)
    diagnostics = t126_audit.diagnostics
    if diagnostics is None:
        raise AssertionError("T249 deletion audits should produce diagnostics")
    ordering_band_passed = target.accepts(diagnostics.comparable_fraction)
    verdict = (
        "t126_pass_but_ordering_fraction_fail"
        if t126_audit.manifold_filter_passed and not ordering_band_passed
        else t156_audit.verdict
    )
    return T251DeletionAudit(
        removed_event=removed_event,
        t126_classification=t126_audit.classification,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        event_count=diagnostics.event_count,
        strict_pair_count=diagnostics.strict_pair_count,
        ordering_fraction=diagnostics.comparable_fraction,
        ordering_band_passed=ordering_band_passed,
        height=diagnostics.height,
        width=diagnostics.width,
        interval_counts_by_size=diagnostics.interval_counts_by_size,
        verdict=verdict,
    )


def t251_result_to_dict(result: T251Result) -> dict[str, Any]:
    return {
        "target": {
            "name": result.target.name,
            "target_fraction": _fraction_to_dict(result.target.target_fraction),
            "tolerance": _fraction_to_dict(result.target.tolerance),
            "basis": result.target.basis,
        },
        "parent_ordering_fraction": _fraction_to_dict(result.parent_ordering_fraction),
        "parent_band_passed": result.parent_band_passed,
        "deletion_audits": [_deletion_to_dict(audit) for audit in result.deletion_audits],
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


def _deletion_to_dict(audit: T251DeletionAudit) -> dict[str, Any]:
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
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in audit.interval_counts_by_size
        ],
        "verdict": audit.verdict,
    }


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}
