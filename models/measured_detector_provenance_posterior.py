"""T76: measured detector-provenance posterior adapter.

T75 mapped one realistic detector stack into the T74 engineered recovery
region, but several ranges were plausible engineering posteriors rather than
deployment measurements. T76 makes that gap executable: deployment evidence is
converted into T74 ``PriorFamily`` coordinates before the Monte Carlo audit.

This is still not a detector-dynamics model. It is a protocol-audit adapter for
already formed detector records.
"""

from __future__ import annotations

from dataclasses import dataclass
import random

from models.provenance_protocol_monte_carlo import (
    FamilyOutcome,
    PriorFamily,
    Range,
    sample_family,
)


SAMPLE_COUNT = 400
SEED = 76019


@dataclass(frozen=True)
class ProportionEvidence:
    """A measured Bernoulli rate used to build a conservative interval."""

    observed: int
    total: int
    description: str

    def posterior_range(self) -> Range:
        if self.total <= 0:
            raise ValueError(f"{self.description} must have positive total")
        if self.observed < 0 or self.observed > self.total:
            raise ValueError(f"{self.description} observed count out of range")

        # Laplace-smoothed two-sigma normal interval. This is intentionally
        # simple and conservative enough for a fixture-level audit.
        center = (self.observed + 1.0) / (self.total + 2.0)
        variance = center * (1.0 - center) / (self.total + 2.0)
        radius = max(0.005, 2.0 * variance**0.5)
        return Range(max(0.0, center - radius), min(1.0, center + radius))


@dataclass(frozen=True)
class TimingEvidence:
    """Normalized timing measurement in the T72/T74 clock units."""

    estimate: float
    uncertainty: float
    description: str

    def posterior_range(self) -> Range:
        if self.estimate < 0.0:
            raise ValueError(f"{self.description} estimate must be non-negative")
        if self.uncertainty < 0.0:
            raise ValueError(f"{self.description} uncertainty must be non-negative")
        return Range(
            max(0.0, self.estimate - self.uncertainty),
            self.estimate + self.uncertainty,
        )


@dataclass(frozen=True)
class AuditPolicy:
    """Pre-registered acceptance policy, separated from deployment evidence."""

    confidence_floor: Range = Range(0.78, 0.85)
    max_false_risk: Range = Range(0.12, 0.22)


@dataclass(frozen=True)
class DeploymentEvidence:
    name: str
    local_sigma: TimingEvidence
    archive_sigma: TimingEvidence
    batching_window: TimingEvidence
    tag_retention: ProportionEvidence
    signature_verification: ProportionEvidence
    accepted_forged_tags: ProportionEvidence
    accepted_spoofed_independent_tags: ProportionEvidence
    independent_unique_tags: ProportionEvidence
    detector_boundary_integrity: ProportionEvidence
    archive_boundary_integrity: ProportionEvidence
    transport_boundary_integrity: ProportionEvidence
    dependent_perturbation_changes: ProportionEvidence
    independent_perturbation_false_changes: ProportionEvidence
    perturbation_back_action_events: ProportionEvidence
    dag_observability: ProportionEvidence
    signed_dag_edges: ProportionEvidence
    dag_truncation_events: ProportionEvidence
    false_shared_dag_edges: ProportionEvidence
    pre_registered_threshold_coverage: ProportionEvidence
    purpose: str


@dataclass(frozen=True)
class DeploymentAudit:
    evidence: DeploymentEvidence
    policy: AuditPolicy
    posterior: PriorFamily
    outcome: FamilyOutcome
    verdict: str
    interpretation: str


@dataclass(frozen=True)
class T76Result:
    sample_count: int
    seed: int
    audits: tuple[DeploymentAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    recommended_next: str


def calibrated_signed_deployment_fixture() -> DeploymentEvidence:
    return DeploymentEvidence(
        name="measured_signed_time_tag_stack",
        local_sigma=TimingEvidence(0.003, 0.002, "local TDC rms timing"),
        archive_sigma=TimingEvidence(0.025, 0.015, "archive clock rms timing"),
        batching_window=TimingEvidence(0.090, 0.040, "event-batch latency window"),
        tag_retention=ProportionEvidence(9975, 10000, "retained event tags"),
        signature_verification=ProportionEvidence(9990, 10000, "verified signatures"),
        accepted_forged_tags=ProportionEvidence(0, 5000, "accepted forged tags"),
        accepted_spoofed_independent_tags=ProportionEvidence(
            1,
            5000,
            "accepted copied records with spoofed independent tags",
        ),
        independent_unique_tags=ProportionEvidence(
            9980,
            10000,
            "independent records with unique tags",
        ),
        detector_boundary_integrity=ProportionEvidence(
            9970,
            10000,
            "detector trust-boundary checks",
        ),
        archive_boundary_integrity=ProportionEvidence(
            9960,
            10000,
            "archive trust-boundary checks",
        ),
        transport_boundary_integrity=ProportionEvidence(
            9975,
            10000,
            "transport trust-boundary checks",
        ),
        dependent_perturbation_changes=ProportionEvidence(
            980,
            1000,
            "dependent-copy perturbation responses",
        ),
        independent_perturbation_false_changes=ProportionEvidence(
            8,
            1000,
            "independent-channel perturbation false changes",
        ),
        perturbation_back_action_events=ProportionEvidence(
            3,
            1000,
            "perturbation back-action events",
        ),
        dag_observability=ProportionEvidence(
            9960,
            10000,
            "complete ancestry DAG observations",
        ),
        signed_dag_edges=ProportionEvidence(
            9990,
            10000,
            "verified signed DAG edges",
        ),
        dag_truncation_events=ProportionEvidence(
            12,
            10000,
            "DAG truncation events",
        ),
        false_shared_dag_edges=ProportionEvidence(
            4,
            10000,
            "false shared-ancestry edges",
        ),
        pre_registered_threshold_coverage=ProportionEvidence(
            20,
            20,
            "pre-registered threshold fields",
        ),
        purpose=(
            "Measured-style fixture for a signed photon time-tagging stack with "
            "explicit provenance logging."
        ),
    )


def unsigned_timing_only_control_fixture() -> DeploymentEvidence:
    signed = calibrated_signed_deployment_fixture()
    return DeploymentEvidence(
        name="timing_only_unsigned_control",
        local_sigma=signed.local_sigma,
        archive_sigma=signed.archive_sigma,
        batching_window=signed.batching_window,
        tag_retention=ProportionEvidence(720, 1000, "retained unsigned tags"),
        signature_verification=ProportionEvidence(460, 1000, "signature checks"),
        accepted_forged_tags=ProportionEvidence(140, 1000, "accepted forged tags"),
        accepted_spoofed_independent_tags=ProportionEvidence(
            160,
            1000,
            "accepted copied records with spoofed independent tags",
        ),
        independent_unique_tags=ProportionEvidence(
            680,
            1000,
            "independent records with unique tags",
        ),
        detector_boundary_integrity=signed.detector_boundary_integrity,
        archive_boundary_integrity=ProportionEvidence(
            660,
            1000,
            "archive trust-boundary checks",
        ),
        transport_boundary_integrity=ProportionEvidence(
            700,
            1000,
            "transport trust-boundary checks",
        ),
        dependent_perturbation_changes=signed.dependent_perturbation_changes,
        independent_perturbation_false_changes=signed.independent_perturbation_false_changes,
        perturbation_back_action_events=signed.perturbation_back_action_events,
        dag_observability=ProportionEvidence(
            420,
            1000,
            "complete ancestry DAG observations",
        ),
        signed_dag_edges=ProportionEvidence(120, 1000, "verified signed DAG edges"),
        dag_truncation_events=ProportionEvidence(
            280,
            1000,
            "DAG truncation events",
        ),
        false_shared_dag_edges=ProportionEvidence(
            160,
            1000,
            "false shared-ancestry edges",
        ),
        pre_registered_threshold_coverage=signed.pre_registered_threshold_coverage,
        purpose=(
            "Control with the same timing evidence but weak or absent signed "
            "provenance infrastructure."
        ),
    )


def incomplete_preregistration_control_fixture() -> DeploymentEvidence:
    signed = calibrated_signed_deployment_fixture()
    return DeploymentEvidence(
        name="signed_stack_incomplete_preregistration_control",
        local_sigma=signed.local_sigma,
        archive_sigma=signed.archive_sigma,
        batching_window=signed.batching_window,
        tag_retention=signed.tag_retention,
        signature_verification=signed.signature_verification,
        accepted_forged_tags=signed.accepted_forged_tags,
        accepted_spoofed_independent_tags=signed.accepted_spoofed_independent_tags,
        independent_unique_tags=signed.independent_unique_tags,
        detector_boundary_integrity=signed.detector_boundary_integrity,
        archive_boundary_integrity=signed.archive_boundary_integrity,
        transport_boundary_integrity=signed.transport_boundary_integrity,
        dependent_perturbation_changes=signed.dependent_perturbation_changes,
        independent_perturbation_false_changes=(
            signed.independent_perturbation_false_changes
        ),
        perturbation_back_action_events=signed.perturbation_back_action_events,
        dag_observability=signed.dag_observability,
        signed_dag_edges=signed.signed_dag_edges,
        dag_truncation_events=signed.dag_truncation_events,
        false_shared_dag_edges=signed.false_shared_dag_edges,
        pre_registered_threshold_coverage=ProportionEvidence(
            14,
            20,
            "pre-registered threshold fields",
        ),
        purpose=(
            "Control with strong deployment evidence but incomplete "
            "pre-registration of acceptance thresholds."
        ),
    )


def measured_fixture_audits() -> tuple[DeploymentEvidence, ...]:
    return (
        calibrated_signed_deployment_fixture(),
        unsigned_timing_only_control_fixture(),
        incomplete_preregistration_control_fixture(),
    )


def evidence_to_prior_family(
    evidence: DeploymentEvidence,
    policy: AuditPolicy | None = None,
) -> PriorFamily:
    policy = policy or AuditPolicy()
    return PriorFamily(
        name=evidence.name,
        local_sigma=evidence.local_sigma.posterior_range(),
        archive_sigma=evidence.archive_sigma.posterior_range(),
        batching_window=evidence.batching_window.posterior_range(),
        tag_retention=evidence.tag_retention.posterior_range(),
        verification=evidence.signature_verification.posterior_range(),
        forgery=evidence.accepted_forged_tags.posterior_range(),
        spoof_independent=evidence.accepted_spoofed_independent_tags.posterior_range(),
        unique_independent_tag=evidence.independent_unique_tags.posterior_range(),
        detector_trust=evidence.detector_boundary_integrity.posterior_range(),
        archive_trust=evidence.archive_boundary_integrity.posterior_range(),
        transport_trust=evidence.transport_boundary_integrity.posterior_range(),
        p_change_dependent=evidence.dependent_perturbation_changes.posterior_range(),
        p_change_independent=(
            evidence.independent_perturbation_false_changes.posterior_range()
        ),
        back_action=evidence.perturbation_back_action_events.posterior_range(),
        observability=evidence.dag_observability.posterior_range(),
        signed_edge=evidence.signed_dag_edges.posterior_range(),
        truncation=evidence.dag_truncation_events.posterior_range(),
        false_shared_edge=evidence.false_shared_dag_edges.posterior_range(),
        confidence_floor=policy.confidence_floor,
        max_false_risk=policy.max_false_risk,
        declared_threshold_prob=_observed_fraction(
            evidence.pre_registered_threshold_coverage
        ),
        purpose=evidence.purpose,
    )


def run_t76_analysis() -> T76Result:
    rng = random.Random(SEED)
    policy = AuditPolicy()
    audits = tuple(
        _audit_deployment(evidence, policy, rng)
        for evidence in measured_fixture_audits()
    )
    signed, unsigned, incomplete = audits
    if (
        signed.outcome.robust_rate >= 0.8
        and unsigned.outcome.robust_rate < 0.5
        and incomplete.outcome.threshold_dependent_rate > 0.1
    ):
        strongest_claim = (
            "Detector-level D1 finality can be tested as a measured "
            "provenance-protocol claim: deployment evidence can be converted "
            "into T72/T74 posterior coordinates before D1 scoring."
        )
        q1_update = (
            "Keep Q1 partially supported only for measured, pre-registered "
            "detector provenance protocols; do not treat timing resolution "
            "alone as support."
        )
    else:
        strongest_claim = (
            "The measured-posterior adapter fails to preserve the T75 signed "
            "versus unsigned discriminator."
        )
        q1_update = (
            "Demote detector Q1 until a measured-posterior protocol preserves "
            "the signed versus unsigned control separation."
        )
    return T76Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        audits=audits,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "The measured-posterior adapter weakens T75 by replacing "
            "narrative posterior ranges with a required evidence schema. A "
            "detector stack without measured authentication, trust-boundary, "
            "perturbation, and DAG evidence does not earn D1 provenance "
            "recovery even when its timing evidence is unchanged."
        ),
        falsification_condition=(
            "The detector branch should be demoted if a real deployment's "
            "measured posterior either withholds D1, produces false "
            "independence/dependence risk, or only succeeds after weakening "
            "pre-registered confidence and false-risk policy bounds."
        ),
        q1_update=q1_update,
        recommended_next=(
            "Populate this schema from an actual lab run: event-loss logs, "
            "signature failures, replay/forgery trials, perturbation controls, "
            "trust-boundary audits, and DAG truncation counts."
        ),
    )


def t76_result_to_dict(result: T76Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "audits": [
            {
                "name": audit.evidence.name,
                "verdict": audit.verdict,
                "interpretation": audit.interpretation,
                "posterior_ranges": _posterior_to_dict(audit.posterior),
                "outcome": _outcome_to_dict(audit.outcome),
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "recommended_next": result.recommended_next,
    }


def _audit_deployment(
    evidence: DeploymentEvidence,
    policy: AuditPolicy,
    rng: random.Random,
) -> DeploymentAudit:
    posterior = evidence_to_prior_family(evidence, policy)
    outcome = sample_family(posterior, rng, SAMPLE_COUNT)
    verdict = _verdict(outcome)
    return DeploymentAudit(
        evidence=evidence,
        policy=policy,
        posterior=posterior,
        outcome=outcome,
        verdict=verdict,
        interpretation=_interpretation(verdict),
    )


def _observed_fraction(evidence: ProportionEvidence) -> float:
    if evidence.total <= 0:
        raise ValueError(f"{evidence.description} must have positive total")
    if evidence.observed < 0 or evidence.observed > evidence.total:
        raise ValueError(f"{evidence.description} observed count out of range")
    return evidence.observed / evidence.total


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
            "Measured evidence maps into the engineered recovery region."
        ),
        "measured_false_independence_risk": (
            "Measured evidence sometimes accepts copied records as independent."
        ),
        "measured_false_dependence_risk": (
            "Measured evidence sometimes accepts independent records as copied."
        ),
        "threshold_dependent_failure": (
            "The audit depends on thresholds not covered by the deployment record."
        ),
        "measured_conservative_withhold": (
            "Measured evidence is insufficient; D1 provenance is withheld."
        ),
    }[verdict]


def _range_to_list(value: Range) -> list[float]:
    return [round(value.low, 6), round(value.high, 6)]


def _posterior_to_dict(family: PriorFamily) -> dict[str, object]:
    return {
        "local_sigma": _range_to_list(family.local_sigma),
        "archive_sigma": _range_to_list(family.archive_sigma),
        "batching_window": _range_to_list(family.batching_window),
        "tag_retention": _range_to_list(family.tag_retention),
        "verification": _range_to_list(family.verification),
        "forgery": _range_to_list(family.forgery),
        "spoof_independent": _range_to_list(family.spoof_independent),
        "unique_independent_tag": _range_to_list(family.unique_independent_tag),
        "detector_trust": _range_to_list(family.detector_trust),
        "archive_trust": _range_to_list(family.archive_trust),
        "transport_trust": _range_to_list(family.transport_trust),
        "p_change_dependent": _range_to_list(family.p_change_dependent),
        "p_change_independent": _range_to_list(family.p_change_independent),
        "back_action": _range_to_list(family.back_action),
        "observability": _range_to_list(family.observability),
        "signed_edge": _range_to_list(family.signed_edge),
        "truncation": _range_to_list(family.truncation),
        "false_shared_edge": _range_to_list(family.false_shared_edge),
        "confidence_floor": _range_to_list(family.confidence_floor),
        "max_false_risk": _range_to_list(family.max_false_risk),
        "declared_threshold_prob": round(family.declared_threshold_prob, 6),
        "purpose": family.purpose,
    }


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
