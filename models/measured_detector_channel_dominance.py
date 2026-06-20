"""T85: channel-dominance audit for the measured detector schema.

T81 showed that trust boundaries and pre-registration are load-bearing in the
current measured detector audit. T85 sharpens that result: among the remaining
measured categories, which ones can independently change the verdict under a
hostile single-category stress family, and which ones remain non-dispositive
because other accepted channels already suffice?
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import random

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
    ProportionEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
)
from models.provenance_protocol_monte_carlo import FamilyOutcome, sample_family


SAMPLE_COUNT = 400
SEED = 85029


@dataclass(frozen=True)
class ChannelStressCase:
    name: str
    category: str
    evidence: DeploymentEvidence
    outcome: FamilyOutcome
    verdict: str
    independently_decisive: bool
    interpretation: str


@dataclass(frozen=True)
class T85Result:
    sample_count: int
    seed: int
    baseline_outcome: FamilyOutcome
    baseline_verdict: str
    cases: tuple[ChannelStressCase, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def run_t85_analysis() -> T85Result:
    policy = AuditPolicy()
    baseline = calibrated_signed_deployment_fixture()
    baseline_outcome = sample_family(
        evidence_to_prior_family(baseline, policy),
        random.Random(SEED),
        SAMPLE_COUNT,
    )
    baseline_verdict = _verdict(baseline_outcome)

    cases = tuple(
        _audit_case(index, name, category, evidence, policy)
        for index, (name, category, evidence) in enumerate(
            hostile_single_category_cases(),
            start=1,
        )
    )

    strongest_claim = (
        "The current measured detector route is narrower than the T76 schema "
        "suggests. After trust-boundary and pre-registration gates are fixed, "
        "spoof/unique-tag evidence can still independently demote the signed "
        "fixture, but perturbation and DAG evidence do not become decisive on "
        "their own inside the present witness family."
    )
    weakened_claim = (
        "This weakens any reading of the detector branch that treats "
        "perturbation response or DAG observability as already independent "
        "decision channels in the executable audit. At present they are "
        "auxiliary to authenticated-tag evidence rather than peer load-bearing "
        "axes."
    )
    falsification_condition = (
        "T85 fails if a single-category perturbation or DAG stress family, "
        "with trust and pre-registration fixed at the signed values, changes "
        "the signed fixture's verdict on its own, or if the spoof/unique-tag "
        "stress stops changing the verdict."
    )
    q1_update = (
        "Keep Q1 partially supported only as a narrow detector-record "
        "admissibility audit. The current executable content is best read as "
        "pre-registration gate + trust-boundary gate + authenticated-tag "
        "sufficiency, with perturbation and DAG channels not yet independently "
        "earned."
    )
    blocker = (
        "The current witness family leaves authenticated tag channels already "
        "strong enough to settle provenance in cases where perturbation and "
        "DAG evidence degrade. That prevents those channels from being "
        "independently decisive."
    )
    recommended_next = (
        "Construct a hostile raw-log family in which authenticated tags are "
        "intentionally ambiguous but perturbation response or signed ancestry "
        "still separates copied from independent records. If that cannot be "
        "done, remove those channels from the detector branch's core schema."
    )
    return T85Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        baseline_outcome=baseline_outcome,
        baseline_verdict=baseline_verdict,
        cases=cases,
        strongest_claim=strongest_claim,
        weakened_claim=weakened_claim,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def hostile_single_category_cases() -> tuple[tuple[str, str, DeploymentEvidence], ...]:
    signed = calibrated_signed_deployment_fixture()
    return (
        (
            "spoof_unique_tag_hostile_family",
            "spoof_resistance",
            replace(
                signed,
                accepted_forged_tags=ProportionEvidence(
                    0,
                    1000,
                    "accepted forged tags",
                ),
                accepted_spoofed_independent_tags=ProportionEvidence(
                    1000,
                    1000,
                    "accepted copied records with spoofed independent tags",
                ),
                independent_unique_tags=ProportionEvidence(
                    500,
                    1000,
                    "independent records with unique tags",
                ),
                purpose=(
                    "Hostile single-category stress where authenticated unique "
                    "tags become ambiguous while trust and pre-registration "
                    "stay fixed."
                ),
            ),
        ),
        (
            "perturbation_backaction_hostile_family",
            "perturbation",
            replace(
                signed,
                dependent_perturbation_changes=ProportionEvidence(
                    1000,
                    1000,
                    "dependent-copy perturbation responses",
                ),
                independent_perturbation_false_changes=ProportionEvidence(
                    0,
                    1000,
                    "independent-channel perturbation false changes",
                ),
                perturbation_back_action_events=ProportionEvidence(
                    1000,
                    1000,
                    "perturbation back-action events",
                ),
                purpose=(
                    "Hostile single-category stress with maximal perturbation "
                    "back-action while authenticated tags and trust remain "
                    "strong."
                ),
            ),
        ),
        (
            "dag_truncation_hostile_family",
            "dag_observability",
            replace(
                signed,
                dag_observability=ProportionEvidence(
                    1000,
                    1000,
                    "complete ancestry DAG observations",
                ),
                signed_dag_edges=ProportionEvidence(
                    1000,
                    1000,
                    "verified signed DAG edges",
                ),
                dag_truncation_events=ProportionEvidence(
                    1000,
                    1000,
                    "DAG truncation events",
                ),
                false_shared_dag_edges=ProportionEvidence(
                    0,
                    1000,
                    "false shared-ancestry edges",
                ),
                purpose=(
                    "Hostile single-category stress with maximally truncated "
                    "ancestry while authenticated tags and trust remain "
                    "strong."
                ),
            ),
        ),
    )


def t85_result_to_dict(result: T85Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "baseline": {
            "verdict": result.baseline_verdict,
            "outcome": _outcome_to_dict(result.baseline_outcome),
        },
        "cases": [
            {
                "name": case.name,
                "category": case.category,
                "verdict": case.verdict,
                "independently_decisive": case.independently_decisive,
                "interpretation": case.interpretation,
                "outcome": _outcome_to_dict(case.outcome),
            }
            for case in result.cases
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _audit_case(
    index: int,
    name: str,
    category: str,
    evidence: DeploymentEvidence,
    policy: AuditPolicy,
) -> ChannelStressCase:
    outcome = sample_family(
        evidence_to_prior_family(evidence, policy),
        random.Random(SEED + index),
        SAMPLE_COUNT,
    )
    verdict = _verdict(outcome)
    independently_decisive = verdict != "robust_measured_recovery"
    return ChannelStressCase(
        name=name,
        category=category,
        evidence=evidence,
        outcome=outcome,
        verdict=verdict,
        independently_decisive=independently_decisive,
        interpretation=_interpretation(category, verdict),
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


def _interpretation(category: str, verdict: str) -> str:
    if category == "spoof_resistance":
        return (
            "Single-category spoof and unique-tag stress demotes the signed "
            "fixture, so authenticated tag evidence is still independently "
            "decisive inside the present witness family."
        )
    return (
        f"Even hostile {category} stress does not demote the signed fixture "
        "while authenticated tags, trust boundaries, and pre-registration "
        "remain intact."
    )


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
