"""T79: coarse dashboard summaries do not identify detector provenance verdicts.

T78 moved the detector branch onto a raw-log contract. T79 tests whether that
requirement is merely procedural or mathematically load-bearing. The core
question is whether a coarse deployment dashboard can uniquely determine the
T76/T77 detector-provenance verdict.

This model constructs two deployments with the same dashboard-visible metrics
but opposite hidden provenance structure. If they produce different T76-style
audit outcomes, then dashboard summaries are non-identifying and raw logs are
not optional bookkeeping.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import random

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
)
from models.provenance_protocol_monte_carlo import FamilyOutcome, sample_family


SAMPLE_COUNT = 400
SEED = 79031


@dataclass(frozen=True)
class DashboardSummary:
    """Deployment metrics commonly exposed in a coarse lab dashboard."""

    local_sigma_estimate: float
    local_sigma_uncertainty: float
    archive_sigma_estimate: float
    archive_sigma_uncertainty: float
    batching_window_estimate: float
    batching_window_uncertainty: float
    tag_retention_observed: int
    tag_retention_total: int
    signature_verification_observed: int
    signature_verification_total: int
    threshold_coverage_observed: int
    threshold_coverage_total: int


@dataclass(frozen=True)
class CompletionAudit:
    name: str
    dashboard: DashboardSummary
    verdict: str
    outcome: FamilyOutcome
    interpretation: str


@dataclass(frozen=True)
class T79Result:
    sample_count: int
    seed: int
    dashboard_equal: bool
    audits: tuple[CompletionAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    recommended_next: str
    blocker: str


def dashboard_projection(evidence: DeploymentEvidence) -> DashboardSummary:
    return DashboardSummary(
        local_sigma_estimate=evidence.local_sigma.estimate,
        local_sigma_uncertainty=evidence.local_sigma.uncertainty,
        archive_sigma_estimate=evidence.archive_sigma.estimate,
        archive_sigma_uncertainty=evidence.archive_sigma.uncertainty,
        batching_window_estimate=evidence.batching_window.estimate,
        batching_window_uncertainty=evidence.batching_window.uncertainty,
        tag_retention_observed=evidence.tag_retention.observed,
        tag_retention_total=evidence.tag_retention.total,
        signature_verification_observed=evidence.signature_verification.observed,
        signature_verification_total=evidence.signature_verification.total,
        threshold_coverage_observed=(
            evidence.pre_registered_threshold_coverage.observed
        ),
        threshold_coverage_total=evidence.pre_registered_threshold_coverage.total,
    )


def robust_signed_raw_log_fixture() -> DeploymentEvidence:
    return calibrated_signed_deployment_fixture()


def ambiguous_dashboard_spoof_fixture() -> DeploymentEvidence:
    base = calibrated_signed_deployment_fixture()
    return replace(
        base,
        name="dashboard_matched_spoofable_completion",
        accepted_forged_tags=type(base.accepted_forged_tags)(
            180,
            1000,
            "accepted forged tags despite matching dashboard summary",
        ),
        accepted_spoofed_independent_tags=type(
            base.accepted_spoofed_independent_tags
        )(
            220,
            1000,
            "accepted spoofed independent tags despite matching dashboard summary",
        ),
        independent_unique_tags=type(base.independent_unique_tags)(
            710,
            1000,
            "independent records with unique tags",
        ),
        archive_boundary_integrity=type(base.archive_boundary_integrity)(
            620,
            1000,
            "archive trust-boundary checks",
        ),
        transport_boundary_integrity=type(base.transport_boundary_integrity)(
            690,
            1000,
            "transport trust-boundary checks",
        ),
        independent_perturbation_false_changes=type(
            base.independent_perturbation_false_changes
        )(
            140,
            1000,
            "independent-channel perturbation false changes",
        ),
        perturbation_back_action_events=type(base.perturbation_back_action_events)(
            130,
            1000,
            "perturbation back-action events",
        ),
        dag_observability=type(base.dag_observability)(
            410,
            1000,
            "complete ancestry DAG observations",
        ),
        signed_dag_edges=type(base.signed_dag_edges)(
            260,
            1000,
            "verified signed DAG edges",
        ),
        dag_truncation_events=type(base.dag_truncation_events)(
            260,
            1000,
            "DAG truncation events",
        ),
        false_shared_dag_edges=type(base.false_shared_dag_edges)(
            180,
            1000,
            "false shared-ancestry edges",
        ),
        purpose=(
            "A completion compatible with the same dashboard-visible timing, "
            "retention, and signature-pass summary as the signed stack, but "
            "with hidden spoof, trust, back-action, and DAG failures."
        ),
    )


def run_t79_analysis() -> T79Result:
    rng = random.Random(SEED)
    policy = AuditPolicy()
    deployments = (
        robust_signed_raw_log_fixture(),
        ambiguous_dashboard_spoof_fixture(),
    )
    audits = tuple(_audit(evidence, policy, rng) for evidence in deployments)
    dashboards = [audit.dashboard for audit in audits]
    dashboard_equal = dashboards[0] == dashboards[1]
    verdicts = {audit.verdict for audit in audits}

    if dashboard_equal and len(verdicts) == 2:
        strongest_claim = (
            "Coarse deployment dashboards are non-identifying for the detector "
            "branch: two completions with the same timing, retention, "
            "signature-pass, and threshold-coverage summary can still yield "
            "opposite T76-style provenance verdicts."
        )
        q1_update = (
            "Keep Q1 partially supported only for event-level raw-log "
            "provenance audits. Dashboard summaries are insufficient because "
            "they do not identify spoof, trust-boundary, perturbation, or DAG "
            "structure."
        )
    else:
        strongest_claim = (
            "The chosen dashboard projection unexpectedly identified the "
            "detector-provenance verdict."
        )
        q1_update = (
            "The raw-log requirement would need re-justification if a coarse "
            "dashboard uniquely fixed the detector verdict."
        )

    return T79Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        dashboard_equal=dashboard_equal,
        audits=audits,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "T79 weakens the detector branch by ruling out a common shortcut: "
            "strong timing, high tag retention, and high signature-pass rates "
            "do not by themselves support Q1. Opposite provenance verdicts can "
            "hide beneath the same coarse deployment dashboard."
        ),
        falsification_condition=(
            "T79 fails if one can project deployment evidence to a coarse "
            "dashboard that omits raw ancestry, replay, spoof, perturbation, "
            "and trust-boundary logs while still uniquely determining the "
            "T76/T77 verdict for all completions compatible with that summary."
        ),
        q1_update=q1_update,
        recommended_next=(
            "Demand one real event-level detector log with ancestry, replay, "
            "spoof, perturbation, and trust-boundary evidence, then run the "
            "locked T76/T77/T78/T79 audit without replacing it by a dashboard "
            "summary."
        ),
        blocker=(
            "No real event-level deployment log is present; T79 only proves "
            "that dashboard-level evidence cannot close that gap."
        ),
    )


def t79_result_to_dict(result: T79Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "dashboard_equal": result.dashboard_equal,
        "audits": [
            {
                "name": audit.name,
                "dashboard": {
                    "local_sigma": [
                        audit.dashboard.local_sigma_estimate,
                        audit.dashboard.local_sigma_uncertainty,
                    ],
                    "archive_sigma": [
                        audit.dashboard.archive_sigma_estimate,
                        audit.dashboard.archive_sigma_uncertainty,
                    ],
                    "batching_window": [
                        audit.dashboard.batching_window_estimate,
                        audit.dashboard.batching_window_uncertainty,
                    ],
                    "tag_retention": [
                        audit.dashboard.tag_retention_observed,
                        audit.dashboard.tag_retention_total,
                    ],
                    "signature_verification": [
                        audit.dashboard.signature_verification_observed,
                        audit.dashboard.signature_verification_total,
                    ],
                    "threshold_coverage": [
                        audit.dashboard.threshold_coverage_observed,
                        audit.dashboard.threshold_coverage_total,
                    ],
                },
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
                "outcome": _outcome_to_dict(audit.outcome),
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "recommended_next": result.recommended_next,
        "blocker": result.blocker,
    }


def _audit(
    evidence: DeploymentEvidence,
    policy: AuditPolicy,
    rng: random.Random,
) -> CompletionAudit:
    outcome = sample_family(evidence_to_prior_family(evidence, policy), rng, SAMPLE_COUNT)
    verdict = _verdict(outcome)
    return CompletionAudit(
        name=evidence.name,
        dashboard=dashboard_projection(evidence),
        verdict=verdict,
        outcome=outcome,
        interpretation=_interpretation(verdict),
    )


def _verdict(outcome: FamilyOutcome) -> str:
    if outcome.robust_rate >= 0.8:
        return "robust_measured_recovery"
    if outcome.false_independence_rate > 0.0:
        return "measured_false_independence_risk"
    if outcome.false_dependence_rate > 0.0:
        return "measured_false_dependence_risk"
    if outcome.threshold_dependent_rate > 0.1:
        return "threshold_dependent_failure"
    return "measured_conservative_withhold"


def _interpretation(verdict: str) -> str:
    return {
        "robust_measured_recovery": (
            "The completion supports the signed provenance branch under T76."
        ),
        "measured_false_independence_risk": (
            "The completion leaks copied or spoofed records as if they were "
            "independent."
        ),
        "measured_false_dependence_risk": (
            "The completion spuriously collapses independent records together."
        ),
        "threshold_dependent_failure": (
            "The completion still depends on incompletely fixed thresholds."
        ),
        "measured_conservative_withhold": (
            "The completion is too weak to support detector-level D1."
        ),
    }[verdict]


def _outcome_to_dict(outcome: FamilyOutcome) -> dict[str, object]:
    return {
        "sample_count": outcome.sample_count,
        "robust_rate": outcome.robust_rate,
        "withhold_rate": outcome.withhold_rate,
        "threshold_dependent_rate": outcome.threshold_dependent_rate,
        "false_independence_rate": outcome.false_independence_rate,
        "false_dependence_rate": outcome.false_dependence_rate,
        "computable_d1_rate": outcome.computable_d1_rate,
        "robust_count": outcome.robust_count,
        "withhold_count": outcome.withhold_count,
        "threshold_dependent_count": outcome.threshold_dependent_count,
        "false_independence_count": outcome.false_independence_count,
        "false_dependence_count": outcome.false_dependence_count,
        "computable_d1_count": outcome.computable_d1_count,
    }
