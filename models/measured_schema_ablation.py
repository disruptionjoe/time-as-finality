"""T81: single-category ablation audit for the measured detector schema.

T76 introduced a large measured evidence schema for detector-provenance audits.
T81 asks a stricter question: which evidence categories are actually
load-bearing in the current executable model, and which are presently
non-discriminating under single-category ablations?
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import random

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
    incomplete_preregistration_control_fixture,
    unsigned_timing_only_control_fixture,
)
from models.provenance_protocol_monte_carlo import FamilyOutcome, sample_family


SAMPLE_COUNT = 400
SEED = 81023


@dataclass(frozen=True)
class AblationCase:
    name: str
    category: str
    evidence: DeploymentEvidence
    outcome: FamilyOutcome
    verdict: str
    load_bearing: bool
    interpretation: str


@dataclass(frozen=True)
class T81Result:
    sample_count: int
    seed: int
    signed_outcome: FamilyOutcome
    signed_verdict: str
    ablations: tuple[AblationCase, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def run_t81_analysis() -> T81Result:
    rng = random.Random(SEED)
    policy = AuditPolicy()
    signed = calibrated_signed_deployment_fixture()
    signed_outcome = sample_family(evidence_to_prior_family(signed, policy), rng, SAMPLE_COUNT)
    signed_verdict = _verdict(signed_outcome)

    ablations = tuple(
        _audit_ablation(name, category, evidence, policy, rng)
        for name, category, evidence in single_category_ablations()
    )
    load_bearing = tuple(case.category for case in ablations if case.load_bearing)
    non_load_bearing = tuple(case.category for case in ablations if not case.load_bearing)

    strongest_claim = (
        "The current measured detector-provenance audit does not justify "
        "treating every T76 evidence field as equally load-bearing. Under "
        "single-category ablations, only trust-boundary evidence fully "
        "collapses the signed fixture, while incomplete pre-registration "
        "demotes it to a threshold-dependent result."
    )
    weakened_claim = (
        "In the current witness family, timing, retention/signature pass "
        "rates, spoof-resistance counts, perturbation counts, and DAG-summary "
        "counts are not independently decisive under single-category "
        "ablation. The executable detector branch is therefore narrower than "
        "the full T76 evidence schema suggests."
    )
    falsification_condition = (
        "T81 fails if every declared T76 evidence category independently "
        "changes the signed fixture's verdict under a single-category "
        "ablation, or if trust-boundary and pre-registration ablations no "
        "longer change the verdict."
    )
    q1_update = (
        "Keep Q1 partially supported only as a measured detector-provenance "
        "audit, but narrow the current executable content: in this model the "
        "detector branch presently behaves mainly as a trust-boundary plus "
        "pre-registration gate, not as a fully identified use of all T76 "
        "evidence channels."
    )
    blocker = (
        "The canonical witness family does not yet make spoof, perturbation, "
        "or DAG evidence independently decisive. Those channels are argued for "
        "in prose, but not individually load-bearing in the current audit."
    )
    recommended_next = (
        "Either compress the measured schema to the categories actually used "
        "by the executable audit, or extend the witness family and classifier "
        "so spoof, perturbation, and DAG evidence each control at least one "
        "false-independence or false-dependence boundary."
    )

    if len(load_bearing) == 0 or len(non_load_bearing) == 0:
        strongest_claim = (
            "The ablation frontier is degenerate and needs reinspection "
            "before being used to refine Q1."
        )

    return T81Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        signed_outcome=signed_outcome,
        signed_verdict=signed_verdict,
        ablations=ablations,
        strongest_claim=strongest_claim,
        weakened_claim=weakened_claim,
        falsification_condition=falsification_condition,
        q1_update=q1_update,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def single_category_ablations() -> tuple[tuple[str, str, DeploymentEvidence], ...]:
    signed = calibrated_signed_deployment_fixture()
    unsigned = unsigned_timing_only_control_fixture()
    incomplete = incomplete_preregistration_control_fixture()

    return (
        (
            "timing_ablation",
            "timing",
            replace(
                signed,
                local_sigma=unsigned.local_sigma,
                archive_sigma=unsigned.archive_sigma,
                batching_window=unsigned.batching_window,
                purpose="Signed fixture with timing fields replaced by unsigned-control timing.",
            ),
        ),
        (
            "retention_signature_ablation",
            "retention_signature",
            replace(
                signed,
                tag_retention=unsigned.tag_retention,
                signature_verification=unsigned.signature_verification,
                purpose=(
                    "Signed fixture with retention and signature-pass rates "
                    "replaced by unsigned-control values."
                ),
            ),
        ),
        (
            "spoof_resistance_ablation",
            "spoof_resistance",
            replace(
                signed,
                accepted_forged_tags=unsigned.accepted_forged_tags,
                accepted_spoofed_independent_tags=unsigned.accepted_spoofed_independent_tags,
                independent_unique_tags=unsigned.independent_unique_tags,
                purpose=(
                    "Signed fixture with spoof and unique-tag evidence "
                    "replaced by unsigned-control values."
                ),
            ),
        ),
        (
            "trust_boundary_ablation",
            "trust_boundaries",
            replace(
                signed,
                archive_boundary_integrity=unsigned.archive_boundary_integrity,
                transport_boundary_integrity=unsigned.transport_boundary_integrity,
                purpose=(
                    "Signed fixture with archive and transport trust "
                    "boundaries replaced by unsigned-control values."
                ),
            ),
        ),
        (
            "perturbation_ablation",
            "perturbation",
            replace(
                signed,
                independent_perturbation_false_changes=unsigned.independent_perturbation_false_changes,
                perturbation_back_action_events=unsigned.perturbation_back_action_events,
                purpose=(
                    "Signed fixture with perturbation-separation evidence "
                    "replaced by unsigned-control values."
                ),
            ),
        ),
        (
            "dag_ablation",
            "dag_observability",
            replace(
                signed,
                dag_observability=unsigned.dag_observability,
                signed_dag_edges=unsigned.signed_dag_edges,
                dag_truncation_events=unsigned.dag_truncation_events,
                false_shared_dag_edges=unsigned.false_shared_dag_edges,
                purpose=(
                    "Signed fixture with DAG observability and signed-edge "
                    "fields replaced by unsigned-control values."
                ),
            ),
        ),
        (
            "preregistration_ablation",
            "preregistration",
            replace(
                signed,
                pre_registered_threshold_coverage=incomplete.pre_registered_threshold_coverage,
                purpose=(
                    "Signed fixture with incomplete pre-registration of "
                    "threshold fields."
                ),
            ),
        ),
    )


def t81_result_to_dict(result: T81Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "signed": {
            "verdict": result.signed_verdict,
            "outcome": _outcome_to_dict(result.signed_outcome),
        },
        "ablations": [
            {
                "name": case.name,
                "category": case.category,
                "verdict": case.verdict,
                "load_bearing": case.load_bearing,
                "interpretation": case.interpretation,
                "outcome": _outcome_to_dict(case.outcome),
            }
            for case in result.ablations
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _audit_ablation(
    name: str,
    category: str,
    evidence: DeploymentEvidence,
    policy: AuditPolicy,
    rng: random.Random,
) -> AblationCase:
    outcome = sample_family(evidence_to_prior_family(evidence, policy), rng, SAMPLE_COUNT)
    verdict = _verdict(outcome)
    load_bearing = verdict != "robust_measured_recovery"
    return AblationCase(
        name=name,
        category=category,
        evidence=evidence,
        outcome=outcome,
        verdict=verdict,
        load_bearing=load_bearing,
        interpretation=_interpretation(verdict, category),
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


def _interpretation(verdict: str, category: str) -> str:
    if verdict == "robust_measured_recovery":
        return (
            f"Replacing only the {category} category does not change the signed "
            "fixture's robust verdict in the current executable audit."
        )
    if verdict == "threshold_dependent_failure":
        return (
            f"Replacing only the {category} category makes the signed fixture "
            "policy-threshold dependent."
        )
    return (
        f"Replacing only the {category} category removes robust recovery from "
        "the signed fixture."
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
