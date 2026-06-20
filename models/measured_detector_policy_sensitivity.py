"""T77: policy sensitivity audit for measured detector provenance.

T76 made the detector branch measurable by mapping deployment evidence into
posterior ranges, but the positive result still depended on an acceptance
policy. T77 asks whether the positive measured verdict survives stricter
pre-registered confidence and false-risk bounds, or whether it only appears
inside a permissive policy corridor.
"""

from __future__ import annotations

from dataclasses import dataclass
import random

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
    incomplete_preregistration_control_fixture,
    unsigned_timing_only_control_fixture,
)
from models.provenance_protocol_monte_carlo import FamilyOutcome, Range, sample_family


SAMPLE_COUNT = 400
SEED = 77023


@dataclass(frozen=True)
class PolicyScenario:
    name: str
    policy: AuditPolicy
    purpose: str


@dataclass(frozen=True)
class PolicyAudit:
    policy_name: str
    deployment_name: str
    outcome: FamilyOutcome
    verdict: str
    confidence_floor: Range
    max_false_risk: Range


@dataclass(frozen=True)
class T77Result:
    sample_count: int
    seed: int
    audits: tuple[PolicyAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    recommended_next: str
    blocker: str


def policy_scenarios() -> tuple[PolicyScenario, ...]:
    return (
        PolicyScenario(
            name="strict",
            policy=AuditPolicy(
                confidence_floor=Range(0.90, 0.95),
                max_false_risk=Range(0.05, 0.10),
            ),
            purpose=(
                "Demand near-forensic confidence and very low false-class risk."
            ),
        ),
        PolicyScenario(
            name="baseline",
            policy=AuditPolicy(),
            purpose="Use the T76 default pre-registered audit corridor.",
        ),
        PolicyScenario(
            name="permissive",
            policy=AuditPolicy(
                confidence_floor=Range(0.65, 0.75),
                max_false_risk=Range(0.25, 0.35),
            ),
            purpose=(
                "Allow weaker confidence and higher false-class risk to test for "
                "policy-induced upgrades."
            ),
        ),
    )


def deployment_fixtures() -> tuple[DeploymentEvidence, ...]:
    return (
        calibrated_signed_deployment_fixture(),
        unsigned_timing_only_control_fixture(),
        incomplete_preregistration_control_fixture(),
    )


def run_t77_analysis() -> T77Result:
    rng = random.Random(SEED)
    audits = tuple(
        _audit(policy_case, evidence, rng)
        for policy_case in policy_scenarios()
        for evidence in deployment_fixtures()
    )
    signed = {
        audit.policy_name: audit
        for audit in audits
        if audit.deployment_name == "measured_signed_time_tag_stack"
    }
    unsigned = {
        audit.policy_name: audit
        for audit in audits
        if audit.deployment_name == "timing_only_unsigned_control"
    }
    incomplete = {
        audit.policy_name: audit
        for audit in audits
        if audit.deployment_name == "signed_stack_incomplete_preregistration_control"
    }

    strict_signed = signed["strict"]
    baseline_signed = signed["baseline"]
    permissive_signed = signed["permissive"]

    if (
        strict_signed.outcome.robust_rate >= 0.8
        and baseline_signed.outcome.robust_rate >= 0.8
        and permissive_signed.outcome.robust_rate >= 0.8
        and unsigned["strict"].outcome.robust_rate == 0.0
        and unsigned["baseline"].outcome.robust_rate == 0.0
        and unsigned["permissive"].outcome.robust_rate > 0.0
        and incomplete["strict"].outcome.threshold_dependent_rate > 0.1
        and incomplete["baseline"].outcome.threshold_dependent_rate > 0.1
        and incomplete["permissive"].outcome.threshold_dependent_rate > 0.1
    ):
        strongest_claim = (
            "The measured signed detector fixture is robust across strict, "
            "baseline, and permissive audit policies, but permissive policy "
            "loosening contaminates the discriminator by allowing a small "
            "timing-only unsigned recovery rate."
        )
        q1_update = (
            "Keep Q1 partially supported only as a measured detector-provenance "
            "claim inside an explicitly pre-registered policy corridor that "
            "preserves signed-versus-unsigned separation. The signed positive "
            "result is robust, but permissive policy already leaks timing-only "
            "false positives."
        )
    else:
        strongest_claim = (
            "The measured detector-provenance branch is too policy-sensitive "
            "to support even the narrowed detector claim."
        )
        q1_update = (
            "Demote detector Q1 until one measured deployment remains robust "
            "across stricter pre-registered policy bounds."
        )

    return T77Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        audits=audits,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "T77 weakens the detector branch by exposing policy dependence "
            "directly. The signed fixture is not the fragile part; the fragile "
            "part is the control separation. Once policy becomes too "
            "permissive, the unsigned timing-only control begins to earn "
            "spurious positive classifications."
        ),
        falsification_condition=(
            "Demote the detector branch if no pre-registered policy corridor "
            "keeps the signed measured deployment robust while simultaneously "
            "forcing the timing-only unsigned control to withhold and the "
            "incomplete-pre-registration control to remain threshold-dependent."
        ),
        q1_update=q1_update,
        recommended_next=(
            "Derive a lab-facing policy floor: the loosest confidence and "
            "false-risk corridor that still preserves signed recovery, unsigned "
            "withhold, and incomplete-pre-registration failure."
        ),
        blocker=(
            "T77 still uses fixture-level measured counts rather than a real "
            "deployment log, so the policy corridor is executable but not yet "
            "empirically anchored."
        ),
    )


def t77_result_to_dict(result: T77Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "audits": [
            {
                "policy_name": audit.policy_name,
                "deployment_name": audit.deployment_name,
                "verdict": audit.verdict,
                "confidence_floor": _range_to_list(audit.confidence_floor),
                "max_false_risk": _range_to_list(audit.max_false_risk),
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
    policy_case: PolicyScenario,
    evidence: DeploymentEvidence,
    rng: random.Random,
) -> PolicyAudit:
    posterior = evidence_to_prior_family(evidence, policy_case.policy)
    outcome = sample_family(posterior, rng, SAMPLE_COUNT)
    return PolicyAudit(
        policy_name=policy_case.name,
        deployment_name=evidence.name,
        outcome=outcome,
        verdict=_verdict(outcome),
        confidence_floor=policy_case.policy.confidence_floor,
        max_false_risk=policy_case.policy.max_false_risk,
    )


def _verdict(outcome: FamilyOutcome) -> str:
    if outcome.robust_rate >= 0.8:
        return "robust_under_policy"
    if outcome.false_independence_rate > 0.0:
        return "false_independence_risk_under_policy"
    if outcome.false_dependence_rate > 0.0:
        return "false_dependence_risk_under_policy"
    if outcome.threshold_dependent_rate > 0.1:
        return "threshold_dependent_under_policy"
    return "withhold_under_policy"


def _range_to_list(value: Range) -> list[float]:
    return [round(value.low, 6), round(value.high, 6)]


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
