"""T159: interval-abundance and jackknife screen for the T157 survivor.

T157 showed that a constructed T54 canonical quotient-union colimit can reach
the T126 scale floor and match the declared flat 1+1 ordering-fraction band.
That is still a weak finite control. This module adds a stricter audit before
any robust spacetime-like language is allowed: the candidate must avoid large
Alexandrov intervals at this scale and remain inside the declared ordering
band after every single-event deletion.

The jackknife condition is intentionally a finite fragility screen, not a
causal-set theorem. Failing it demotes the candidate to calibration-only; it
does not prove the candidate is not a valid small causal set.
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
from models.finality_descent_theorem import complete_observer_descent_datum
from models.myrheim_meyer_ordering_fraction_screen import (
    OrderingFractionTarget,
    audit_ordering_fraction_target,
    flat_1p1_interval_target,
)
from models.t54_ordering_fraction_bridge import (
    _completion_to_t126_datum,
    canonical_t157_datums,
)


Event = str
OrderPair = tuple[Event, Event]


@dataclass(frozen=True)
class IntervalJackknifeTarget:
    name: str
    ordering_target: OrderingFractionTarget
    max_parent_interval_size: int
    required_deletion_pass_rate: Fraction
    basis: str


@dataclass(frozen=True)
class DeletionAudit:
    removed_event: Event
    event_count: int
    strict_pair_count: int
    ordering_fraction: Fraction
    ordering_band_passed: bool
    interval_counts_by_size: tuple[tuple[int, int], ...]
    largest_interval_size: int
    interval_support_passed: bool


@dataclass(frozen=True)
class T159Audit:
    name: str
    t54_classification: str
    t54_theorem_applies: bool
    t126_classification: str
    t126_filter_passed: bool
    t156_verdict: str
    event_count: int
    strict_pair_count: int | None
    ordering_fraction: Fraction | None
    interval_counts_by_size: tuple[tuple[int, int], ...]
    largest_interval_size: int | None
    parent_interval_support_passed: bool
    deletion_audits: tuple[DeletionAudit, ...]
    deletion_pass_count: int
    deletion_case_count: int
    deletion_pass_rate: Fraction
    deletion_stability_passed: bool
    verdict: str
    reason: str
    required_next: str


@dataclass(frozen=True)
class T159Result:
    target: IntervalJackknifeTarget
    audits: tuple[T159Audit, ...]
    flat_parent_interval_support_passes: bool
    flat_jackknife_stability_fails: bool
    product_grid_parent_interval_support_fails: bool
    chain_control_blocked_before_interval_screen: bool
    t157_survivor_demoted_to_calibration_only: bool
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
    "T159 does not estimate dimension, prove faithful embedding, validate a "
    "sprinkling process, derive a Lorentzian metric, or prove a continuum "
    "limit. The single-deletion screen is a finite fragility diagnostic only."
)


def flat_1p1_interval_jackknife_target() -> IntervalJackknifeTarget:
    ordering_target = flat_1p1_interval_target()
    return IntervalJackknifeTarget(
        name="flat_1p1_interval_abundance_jackknife",
        ordering_target=ordering_target,
        max_parent_interval_size=1,
        required_deletion_pass_rate=Fraction(1, 1),
        basis=(
            "At the six-event T157 scale, the declared deterministic flat "
            "1+1 target has Alexandrov intervals with at most one interior "
            "event. A candidate promoted beyond calibration-only must also "
            "keep every single-event deletion inside the same ordering-"
            "fraction band. This is a hostile finite robustness screen, not "
            "a continuum causal-set criterion."
        ),
    )


def run_t159_analysis() -> T159Result:
    target = flat_1p1_interval_jackknife_target()
    audits = tuple(_audit_t157_datum(datum, target=target) for datum in canonical_t157_datums())
    by_name = {audit.name: audit for audit in audits}

    flat = by_name["t157_flat_1p1_t54_colimit"]
    grid = by_name["t157_product_grid_2x3_t54_colimit"]
    chain = by_name["t157_chain_6_t54_colimit"]

    flat_interval_passes = flat.parent_interval_support_passed
    flat_stability_fails = not flat.deletion_stability_passed
    grid_interval_fails = not grid.parent_interval_support_passed
    chain_blocked = chain.verdict == "blocked_before_interval_jackknife"
    demoted = flat.verdict == "calibration_only_fragile_jackknife"

    return T159Result(
        target=target,
        audits=audits,
        flat_parent_interval_support_passes=flat_interval_passes,
        flat_jackknife_stability_fails=flat_stability_fails,
        product_grid_parent_interval_support_fails=grid_interval_fails,
        chain_control_blocked_before_interval_screen=chain_blocked,
        t157_survivor_demoted_to_calibration_only=demoted,
        strongest_claim=(
            "The T157 six-event T54 control still passes T126, T156, and the "
            "parent interval-support screen, but it is not deletion-stable: "
            "removing event p4 drops the ordering fraction to 1/5, outside "
            "the declared 1/2 +/- 1/10 band. It should be treated as a "
            "calibration artifact, not a robust S1 survivor."
        ),
        improved=(
            "T159 adds a stronger post-T157 finite diagnostic that combines "
            "Alexandrov interval-size support with a jackknife stability "
            "check, making the S1 causal-set bridge harder to overread."
        ),
        weakened_or_falsified=(
            "This weakens the positive reading of T157. The narrow claim that "
            "T54 can realize the ordering-fraction control survives, but the "
            "candidate fails the stricter robustness gate and therefore does "
            "not support spacetime-facing residue beyond calibration."
        ),
        falsification_condition=(
            "T159 fails if deletion suborders are not computed from the same "
            "T54-completed relation, if parent interval sizes are read from a "
            "different causal relation than T126/T156, or if a finite "
            "jackknife failure is described as a continuum no-go theorem "
            "rather than a demotion of this small control."
        ),
        s1_update=(
            "S1 remains open_formal_target. A finite T54 colimit must now "
            "clear T126, T156, interval-abundance, and robustness screens "
            "before it can be discussed as more than a calibration control."
        ),
        claim_ledger_update=(
            "Add T159 to S1: the T157 flat T54 control passes parent interval "
            "support but fails the single-deletion ordering-fraction stability "
            "screen, so the current positive S1 boundary is calibration-only."
        ),
        open_blocker=(
            "No non-hand-built T54 family, deletion-stable finite sample, "
            "sprinkling/locality diagnostic, faithful embedding theorem, "
            "continuum bridge, covariance result, or metric reconstruction "
            "exists for S1."
        ),
        suggested_next=(
            "Search for a small non-hand-built T54 family with several "
            "deletion-stable members, or move to a proper random-sprinkling "
            "comparison with declared finite-size tolerances."
        ),
        not_claimed=NOT_CLAIMED,
    )


def _audit_t157_datum(
    datum: Any,
    *,
    target: IntervalJackknifeTarget,
) -> T159Audit:
    completion = complete_observer_descent_datum(datum)
    t126_datum = _completion_to_t126_datum(completion)
    t126_audit = audit_finality_colimit_causet(t126_datum)
    t156_audit = audit_ordering_fraction_target(
        t126_datum,
        target=target.ordering_target,
    )
    diagnostics = t126_audit.diagnostics

    interval_counts = (
        diagnostics.interval_counts_by_size
        if diagnostics is not None
        else tuple()
    )
    largest_interval_size = _largest_interval_size(interval_counts)
    parent_interval_support = (
        largest_interval_size is not None
        and largest_interval_size <= target.max_parent_interval_size
    )
    deletion_audits = _deletion_audits(t126_datum, target=target)
    deletion_pass_count = sum(
        1
        for audit in deletion_audits
        if audit.ordering_band_passed and audit.interval_support_passed
    )
    deletion_case_count = len(deletion_audits)
    deletion_pass_rate = _fraction(deletion_pass_count, deletion_case_count)
    deletion_stability_passed = deletion_pass_rate >= target.required_deletion_pass_rate

    if not completion.theorem_applies:
        verdict = "blocked_at_t54"
        reason = completion.evidence
        required_next = "Repair T54 descent data before interval or robustness screening."
    elif not t126_audit.manifold_filter_passed:
        verdict = "blocked_before_interval_jackknife"
        reason = t126_audit.reason
        required_next = t126_audit.required_next
    elif t156_audit.verdict != "passes_ordering_fraction_control_only":
        verdict = "blocked_at_ordering_fraction"
        reason = t156_audit.reason
        required_next = t156_audit.required_next
    elif not parent_interval_support:
        verdict = "fails_parent_interval_abundance"
        reason = (
            "The parent candidate has Alexandrov intervals with too many "
            "interior events for the declared six-event target support."
        )
        required_next = (
            "Do not promote this candidate as flat 1+1-like under the declared "
            "finite target; choose a different target or build a less lattice-"
            "ordered colimit."
        )
    elif not deletion_stability_passed:
        verdict = "calibration_only_fragile_jackknife"
        reason = (
            "The parent candidate passes the declared ordering and interval "
            "screens, but at least one single-event deletion leaves the target "
            "band, so the pass is fragile at this finite scale."
        )
        required_next = (
            "Treat the candidate as calibration-only; search for a family or "
            "larger sample with stable suborders before S1 residue language."
        )
    else:
        verdict = "passes_interval_jackknife_control_only"
        reason = (
            "The finite candidate passes the parent interval-support and "
            "single-deletion stability checks. This remains control-only."
        )
        required_next = (
            "Apply random-sprinkling, locality, embedding, covariance, and "
            "continuum diagnostics before spacetime-facing claims."
        )

    return T159Audit(
        name=datum.name,
        t54_classification=completion.classification,
        t54_theorem_applies=completion.theorem_applies,
        t126_classification=t126_audit.classification,
        t126_filter_passed=t126_audit.manifold_filter_passed,
        t156_verdict=t156_audit.verdict,
        event_count=diagnostics.event_count if diagnostics is not None else len(t126_datum.events),
        strict_pair_count=diagnostics.strict_pair_count if diagnostics is not None else None,
        ordering_fraction=(
            diagnostics.comparable_fraction
            if diagnostics is not None
            else None
        ),
        interval_counts_by_size=interval_counts,
        largest_interval_size=largest_interval_size,
        parent_interval_support_passed=parent_interval_support,
        deletion_audits=deletion_audits,
        deletion_pass_count=deletion_pass_count,
        deletion_case_count=deletion_case_count,
        deletion_pass_rate=deletion_pass_rate,
        deletion_stability_passed=deletion_stability_passed,
        verdict=verdict,
        reason=reason,
        required_next=required_next,
    )


def _deletion_audits(
    datum: FinalityColimitCausetDatum,
    *,
    target: IntervalJackknifeTarget,
) -> tuple[DeletionAudit, ...]:
    strict = _strict_pairs(datum.relation)
    audits: list[DeletionAudit] = []
    for removed_event in sorted(datum.events):
        events = frozenset(event for event in datum.events if event != removed_event)
        sub_strict = frozenset(
            (left, right)
            for left, right in strict
            if left in events and right in events
        )
        sub_datum = FinalityColimitCausetDatum(
            name=f"{datum.name}_delete_{removed_event}",
            events=events,
            relation=non_strict_relation(events, sub_strict),
            descent_gate_passed=True,
            canonical_colimit=True,
            phantom_gap_resolved=True,
            observer_only_gap_changes_strict_order=False,
            source=f"single-event deletion of {datum.name}",
            minimum_events_for_manifold_filter=max(1, len(events)),
        )
        diagnostics = audit_finality_colimit_causet(sub_datum).diagnostics
        if diagnostics is None:
            raise AssertionError("single-deletion subdatum should have diagnostics")
        largest_interval_size = _largest_interval_size(diagnostics.interval_counts_by_size)
        if largest_interval_size is None:
            largest_interval_size = 0
        audits.append(
            DeletionAudit(
                removed_event=removed_event,
                event_count=diagnostics.event_count,
                strict_pair_count=diagnostics.strict_pair_count,
                ordering_fraction=diagnostics.comparable_fraction,
                ordering_band_passed=target.ordering_target.accepts(
                    diagnostics.comparable_fraction
                ),
                interval_counts_by_size=diagnostics.interval_counts_by_size,
                largest_interval_size=largest_interval_size,
                interval_support_passed=(
                    largest_interval_size <= target.max_parent_interval_size
                ),
            )
        )
    return tuple(audits)


def t159_result_to_dict(result: T159Result) -> dict[str, Any]:
    return {
        "target": {
            "name": result.target.name,
            "ordering_target": {
                "name": result.target.ordering_target.name,
                "target_fraction": _fraction_to_dict(
                    result.target.ordering_target.target_fraction
                ),
                "tolerance": _fraction_to_dict(
                    result.target.ordering_target.tolerance
                ),
                "basis": result.target.ordering_target.basis,
            },
            "max_parent_interval_size": result.target.max_parent_interval_size,
            "required_deletion_pass_rate": _fraction_to_dict(
                result.target.required_deletion_pass_rate
            ),
            "basis": result.target.basis,
        },
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "flat_parent_interval_support_passes": (
            result.flat_parent_interval_support_passes
        ),
        "flat_jackknife_stability_fails": result.flat_jackknife_stability_fails,
        "product_grid_parent_interval_support_fails": (
            result.product_grid_parent_interval_support_fails
        ),
        "chain_control_blocked_before_interval_screen": (
            result.chain_control_blocked_before_interval_screen
        ),
        "t157_survivor_demoted_to_calibration_only": (
            result.t157_survivor_demoted_to_calibration_only
        ),
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


def _audit_to_dict(audit: T159Audit) -> dict[str, Any]:
    return {
        "name": audit.name,
        "t54_classification": audit.t54_classification,
        "t54_theorem_applies": audit.t54_theorem_applies,
        "t126_classification": audit.t126_classification,
        "t126_filter_passed": audit.t126_filter_passed,
        "t156_verdict": audit.t156_verdict,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": (
            _fraction_to_dict(audit.ordering_fraction)
            if audit.ordering_fraction is not None
            else None
        ),
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in audit.interval_counts_by_size
        ],
        "largest_interval_size": audit.largest_interval_size,
        "parent_interval_support_passed": audit.parent_interval_support_passed,
        "deletion_audits": [
            _deletion_audit_to_dict(deletion_audit)
            for deletion_audit in audit.deletion_audits
        ],
        "deletion_pass_count": audit.deletion_pass_count,
        "deletion_case_count": audit.deletion_case_count,
        "deletion_pass_rate": _fraction_to_dict(audit.deletion_pass_rate),
        "deletion_stability_passed": audit.deletion_stability_passed,
        "verdict": audit.verdict,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def _deletion_audit_to_dict(audit: DeletionAudit) -> dict[str, Any]:
    return {
        "removed_event": audit.removed_event,
        "event_count": audit.event_count,
        "strict_pair_count": audit.strict_pair_count,
        "ordering_fraction": _fraction_to_dict(audit.ordering_fraction),
        "ordering_band_passed": audit.ordering_band_passed,
        "interval_counts_by_size": [
            {"size": size, "count": count}
            for size, count in audit.interval_counts_by_size
        ],
        "largest_interval_size": audit.largest_interval_size,
        "interval_support_passed": audit.interval_support_passed,
    }


def _strict_pairs(relation: frozenset[OrderPair]) -> frozenset[OrderPair]:
    return frozenset((left, right) for left, right in relation if left != right)


def _largest_interval_size(
    interval_counts: tuple[tuple[int, int], ...],
) -> int | None:
    if not interval_counts:
        return None
    return max(size for size, _count in interval_counts)


def _fraction(numerator: int, denominator: int) -> Fraction:
    if denominator == 0:
        return Fraction(0, 1)
    return Fraction(numerator, denominator)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


if __name__ == "__main__":
    import json

    print(json.dumps(t159_result_to_dict(run_t159_analysis()), indent=2))
