"""T530: route next S1 generator work after T528's failed preflight.

T528 was useful because it rejected the first two-receipt finality-native
generator without importing Lorentzian coordinates. T530 does not try a new
generator. It turns that miss into a small executable router: which repaired
suite axes failed, and which future packet shapes are admissible for review.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any

from models.t528_s1_finality_native_generator_preflight import (
    GeneratedSampleAudit,
    run_t528_analysis,
)


ARTIFACT = "T530-t528-generator-failure-router-v0.1"
VERDICT = "t528_failure_router_built_review_only"

AXIS_ORDER = (
    "ordering_fraction",
    "height",
    "largest_interval",
    "width",
    "hard_t126_gate",
)

AXIS_READINGS = {
    "ordering_fraction": (
        "The two-receipt packet most often misses the random-control ordering "
        "fraction envelope; a next packet must address comparability density "
        "before tuning secondary diagnostics."
    ),
    "height": (
        "Height failures are secondary and cannot be repaired alone while the "
        "ordering-fraction miss remains."
    ),
    "largest_interval": (
        "Largest-interval failures appear in fewer samples and are not the "
        "primary blocker."
    ),
    "width": (
        "Width fails only once in the T528 sample set, so width-only repair is "
        "not a credible next primary packet."
    ),
    "hard_t126_gate": (
        "No executed T528 generator sample failed a hard T126 gate; the issue "
        "is repaired-suite calibration, not descent/canonicality collapse."
    ),
}

NOT_CLAIMED = (
    "T530 does not derive spacetime, prove manifoldlikeness, establish a "
    "finality-native sprinkling law, repair T528, reverse T223, promote S1, "
    "change claim status, change canon, change public posture, authorize "
    "external publication, or support cross-repo truth."
)


@dataclass(frozen=True)
class FailureAxisSummary:
    axis: str
    failed_sample_count: int
    event_counts: tuple[int, ...]
    representative_samples: tuple[str, ...]
    reading: str


@dataclass(frozen=True)
class SizeFailureSummary:
    event_count: int
    sample_count: int
    pass_count: int
    failed_count: int
    pass_rate: Fraction


@dataclass(frozen=True)
class CandidatePacket:
    packet_id: str
    description: str
    predeclared_packet: bool
    finality_native_descent: bool
    targets_primary_failure_axis: bool
    targets_secondary_axis_only: bool
    supplies_independent_naturality: bool
    supplies_hostile_controls: bool
    imports_lorentzian_reference: bool = False
    conditions_on_t528_result: bool = False
    uses_screen_tuned_parameters: bool = False
    requests_s1_or_claim_movement: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_s1_evidence: bool
    action: str
    missing_requirements: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T530Result:
    artifact: str
    source_artifact: str
    t528_verdict: str
    t528_sample_count: int
    t528_pass_count: int
    t528_failed_count: int
    t528_pass_rate: Fraction
    size_summaries: tuple[SizeFailureSummary, ...]
    failure_axis_summaries: tuple[FailureAxisSummary, ...]
    primary_failure_axis: str
    secondary_failure_axes: tuple[str, ...]
    hard_gate_failure_count: int
    packet_decisions: tuple[PacketDecision, ...]
    verdict: str
    strongest_reading: str
    recommended_next: str
    s1_update: str
    claim_ledger_update: str
    not_claimed: str


def run_t530_analysis() -> T530Result:
    t528 = run_t528_analysis()
    failed = tuple(audit for audit in t528.sample_audits if not audit.repaired_suite_passed)
    axis_summaries = _summarize_failure_axes(failed)
    primary_axis = axis_summaries[0].axis
    secondary_axes = tuple(summary.axis for summary in axis_summaries[1:] if summary.failed_sample_count)
    packet_decisions = tuple(
        _evaluate_packet(packet, primary_axis=primary_axis)
        for packet in _candidate_packets()
    )
    admitted = [
        decision.packet_id
        for decision in packet_decisions
        if decision.admitted_as_future_review_target
    ]
    hard_gate_count = _axis_count(failed, "hard_t126_gate")
    verdict = (
        VERDICT
        if primary_axis == "ordering_fraction"
        and t528.pass_count == 25
        and t528.sample_count == 32
        and hard_gate_count == 0
        and admitted == ["predeclared_ordering_fraction_measure_law"]
        and all(not decision.counts_as_s1_evidence for decision in packet_decisions)
        else "t528_failure_router_unexpected_status"
    )
    return T530Result(
        artifact=ARTIFACT,
        source_artifact="T528-s1-finality-native-generator-preflight-v0.1",
        t528_verdict=t528.verdict,
        t528_sample_count=t528.sample_count,
        t528_pass_count=t528.pass_count,
        t528_failed_count=len(failed),
        t528_pass_rate=t528.pass_rate,
        size_summaries=tuple(
            SizeFailureSummary(
                event_count=summary.event_count,
                sample_count=summary.sample_count,
                pass_count=summary.pass_count,
                failed_count=summary.sample_count - summary.pass_count,
                pass_rate=summary.pass_rate,
            )
            for summary in t528.pass_summary_by_size
        ),
        failure_axis_summaries=axis_summaries,
        primary_failure_axis=primary_axis,
        secondary_failure_axes=secondary_axes,
        hard_gate_failure_count=hard_gate_count,
        packet_decisions=packet_decisions,
        verdict=verdict,
        strongest_reading=(
            "T528 did not fail because the two-receipt generator collapsed the "
            "hard T126 gates. It failed because repaired-suite calibration "
            "axes, especially ordering fraction and then height, were not "
            "stable across sizes. The next packet should therefore be a "
            "predeclared finality-native measure or bridge that directly "
            "targets comparability density while keeping independent naturality "
            "and hostile controls visible."
        ),
        recommended_next=(
            "Attempt a predeclared ordering-fraction measure-law packet: fix the "
            "record-domain law before sampling, justify its naturality outside "
            "the T525/T528 diagnostic, include hostile controls, and treat any "
            "pass as review-only until later Lorentzian, locality, covariance, "
            "embedding, and continuum burdens are paid."
        ),
        s1_update=(
            "S1 remains `requires_added_assumption`. T530 routes the next S1 "
            "generator burden but supplies no new generator success and no S1 "
            "evidence."
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T530 is test-registry routing "
            "infrastructure only: no claim row, no S1 status movement, and no "
            "T223 reversal."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t530_result_to_dict(result: T530Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_artifact": result.source_artifact,
        "t528_verdict": result.t528_verdict,
        "t528_sample_count": result.t528_sample_count,
        "t528_pass_count": result.t528_pass_count,
        "t528_failed_count": result.t528_failed_count,
        "t528_pass_rate": _fraction_to_dict(result.t528_pass_rate),
        "size_summaries": [_size_to_dict(summary) for summary in result.size_summaries],
        "failure_axis_summaries": [
            _axis_to_dict(summary) for summary in result.failure_axis_summaries
        ],
        "primary_failure_axis": result.primary_failure_axis,
        "secondary_failure_axes": list(result.secondary_failure_axes),
        "hard_gate_failure_count": result.hard_gate_failure_count,
        "packet_decisions": [
            _decision_to_dict(decision) for decision in result.packet_decisions
        ],
        "verdict": result.verdict,
        "strongest_reading": result.strongest_reading,
        "recommended_next": result.recommended_next,
        "s1_update": result.s1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _summarize_failure_axes(
    failed: tuple[GeneratedSampleAudit, ...],
) -> tuple[FailureAxisSummary, ...]:
    summaries: list[FailureAxisSummary] = []
    for axis in AXIS_ORDER:
        axis_samples = tuple(audit for audit in failed if axis in _audit_axes(audit))
        summaries.append(
            FailureAxisSummary(
                axis=axis,
                failed_sample_count=len(axis_samples),
                event_counts=tuple(sorted({audit.event_count for audit in axis_samples})),
                representative_samples=tuple(
                    f"n={audit.event_count}/seed={audit.seed}" for audit in axis_samples[:4]
                ),
                reading=AXIS_READINGS[axis],
            )
        )
    return tuple(
        sorted(
            summaries,
            key=lambda item: (-item.failed_sample_count, AXIS_ORDER.index(item.axis)),
        )
    )


def _audit_axes(audit: GeneratedSampleAudit) -> tuple[str, ...]:
    axes: list[str] = []
    if not audit.hard_gate_passed:
        axes.append("hard_t126_gate")
    if not audit.ordering_fraction_in_band:
        axes.append("ordering_fraction")
    if not audit.height_in_band:
        axes.append("height")
    if not audit.width_in_band:
        axes.append("width")
    if not audit.largest_interval_in_band:
        axes.append("largest_interval")
    return tuple(axes)


def _axis_count(failed: tuple[GeneratedSampleAudit, ...], axis: str) -> int:
    return sum(axis in _audit_axes(audit) for audit in failed)


def _candidate_packets() -> tuple[CandidatePacket, ...]:
    return (
        CandidatePacket(
            packet_id="axis_blind_more_receipts",
            description=(
                "Add more receipt channels without predeclaring why the change "
                "should repair ordering-fraction failures."
            ),
            predeclared_packet=True,
            finality_native_descent=True,
            targets_primary_failure_axis=False,
            targets_secondary_axis_only=False,
            supplies_independent_naturality=False,
            supplies_hostile_controls=True,
        ),
        CandidatePacket(
            packet_id="screen_tuned_receipt_mixture",
            description=(
                "Tune receipt-channel mixtures after observing which samples "
                "clear the repaired suite."
            ),
            predeclared_packet=False,
            finality_native_descent=True,
            targets_primary_failure_axis=True,
            targets_secondary_axis_only=False,
            supplies_independent_naturality=False,
            supplies_hostile_controls=False,
            conditions_on_t528_result=True,
            uses_screen_tuned_parameters=True,
        ),
        CandidatePacket(
            packet_id="lorentzian_reference_reuse",
            description=(
                "Reuse the T526 external u/v reference law and count the pass "
                "as S1 progress."
            ),
            predeclared_packet=True,
            finality_native_descent=False,
            targets_primary_failure_axis=True,
            targets_secondary_axis_only=False,
            supplies_independent_naturality=True,
            supplies_hostile_controls=True,
            imports_lorentzian_reference=True,
            requests_s1_or_claim_movement=True,
        ),
        CandidatePacket(
            packet_id="height_only_repair",
            description=(
                "Target height-band failures while leaving the primary "
                "ordering-fraction miss unaddressed."
            ),
            predeclared_packet=True,
            finality_native_descent=True,
            targets_primary_failure_axis=False,
            targets_secondary_axis_only=True,
            supplies_independent_naturality=True,
            supplies_hostile_controls=True,
        ),
        CandidatePacket(
            packet_id="ordering_fraction_repair_without_naturality",
            description=(
                "Predeclare a comparability-density repair but provide no "
                "independent naturality or neighboring-theory reason."
            ),
            predeclared_packet=True,
            finality_native_descent=True,
            targets_primary_failure_axis=True,
            targets_secondary_axis_only=False,
            supplies_independent_naturality=False,
            supplies_hostile_controls=True,
        ),
        CandidatePacket(
            packet_id="predeclared_ordering_fraction_measure_law",
            description=(
                "Future packet shape: a finality-native measure or bridge that "
                "predeclares a comparability-density law, justifies naturality "
                "outside the screen, and includes hostile controls."
            ),
            predeclared_packet=True,
            finality_native_descent=True,
            targets_primary_failure_axis=True,
            targets_secondary_axis_only=False,
            supplies_independent_naturality=True,
            supplies_hostile_controls=True,
        ),
    )


def _evaluate_packet(packet: CandidatePacket, *, primary_axis: str) -> PacketDecision:
    missing = _missing_requirements(packet, primary_axis=primary_axis)
    if packet.requests_s1_or_claim_movement:
        classification = "blocked_s1_or_claim_movement_shortcut"
        admitted = False
        action = "stop"
        reason = "A failure router cannot move S1, claims, canon, or public posture."
    elif packet.imports_lorentzian_reference:
        classification = "rejected_lorentzian_reference_import"
        admitted = False
        action = "reject"
        reason = "The packet imports the T526 target spacetime reference law."
    elif packet.conditions_on_t528_result or packet.uses_screen_tuned_parameters:
        classification = "rejected_screen_conditioned_repair"
        admitted = False
        action = "reject"
        reason = "The packet tunes the law from the diagnostic it must clear."
    elif not packet.predeclared_packet or not packet.finality_native_descent:
        classification = "rejected_missing_source_law_contract"
        admitted = False
        action = "reject"
        reason = "The packet lacks a predeclared finality-native source contract."
    elif not packet.targets_primary_failure_axis:
        classification = "rejected_primary_axis_not_addressed"
        admitted = False
        action = "reject"
        reason = f"The packet does not address the primary T528 failure axis: {primary_axis}."
    elif missing:
        classification = "rejected_missing_review_requirements"
        admitted = False
        action = "revise_before_review"
        reason = "The packet addresses the right axis but lacks review requirements."
    else:
        classification = "admitted_future_review_target"
        admitted = True
        action = "future_review_only"
        reason = (
            "The shape is admissible for future review, but no generator "
            "success or S1 evidence is created by T530."
        )
    return PacketDecision(
        packet_id=packet.packet_id,
        classification=classification,
        admitted_as_future_review_target=admitted,
        counts_as_s1_evidence=False,
        action=action,
        missing_requirements=missing,
        reason=reason,
    )


def _missing_requirements(
    packet: CandidatePacket,
    *,
    primary_axis: str,
) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.predeclared_packet:
        missing.append("predeclared_packet")
    if not packet.finality_native_descent:
        missing.append("finality_native_descent")
    if not packet.targets_primary_failure_axis:
        missing.append(f"addresses_{primary_axis}_failure")
    if packet.targets_secondary_axis_only:
        missing.append("not_secondary_axis_only")
    if not packet.supplies_independent_naturality:
        missing.append("independent_naturality_or_neighbor_theory")
    if not packet.supplies_hostile_controls:
        missing.append("hostile_controls")
    if packet.imports_lorentzian_reference:
        missing.append("no_imported_lorentzian_reference")
    if packet.conditions_on_t528_result or packet.uses_screen_tuned_parameters:
        missing.append("not_conditioned_on_t528_failure_screen")
    if packet.requests_s1_or_claim_movement:
        missing.append("no_s1_or_claim_movement")
    return tuple(missing)


def _fraction_to_dict(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _axis_to_dict(summary: FailureAxisSummary) -> dict[str, Any]:
    return {
        "axis": summary.axis,
        "failed_sample_count": summary.failed_sample_count,
        "event_counts": list(summary.event_counts),
        "representative_samples": list(summary.representative_samples),
        "reading": summary.reading,
    }


def _size_to_dict(summary: SizeFailureSummary) -> dict[str, Any]:
    return {
        "event_count": summary.event_count,
        "sample_count": summary.sample_count,
        "pass_count": summary.pass_count,
        "failed_count": summary.failed_count,
        "pass_rate": _fraction_to_dict(summary.pass_rate),
    }


def _decision_to_dict(decision: PacketDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_s1_evidence": decision.counts_as_s1_evidence,
        "action": decision.action,
        "missing_requirements": list(decision.missing_requirements),
        "reason": decision.reason,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t530_result_to_dict(run_t530_analysis()), indent=2))
