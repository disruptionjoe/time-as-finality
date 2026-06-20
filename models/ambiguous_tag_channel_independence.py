"""T86: ambiguous-tag channel-independence audit for detector provenance.

T85 narrowed the measured detector branch to pre-registration, trust, and
authenticated-tag sufficiency in its existing witness family. T86 asks the
next harder question: if timing and authenticated tags are intentionally made
ambiguous, can perturbation response or signed DAG ancestry carry the verdict
on its own inside the same T74/T76 protocol audit?

This is still not detector dynamics. It is a hostile raw-log-count fixture for
already formed detector records.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import random

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
    ProportionEvidence,
    TimingEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
)
from models.provenance_protocol_monte_carlo import FamilyOutcome, sample_family


SAMPLE_COUNT = 400
SEED = 86037


@dataclass(frozen=True)
class AmbiguousTagCase:
    name: str
    channel_under_test: str
    role: str
    evidence: DeploymentEvidence
    outcome: FamilyOutcome
    verdict: str
    rescues_with_ambiguous_tags: bool
    interpretation: str


@dataclass(frozen=True)
class T86Result:
    sample_count: int
    seed: int
    cases: tuple[AmbiguousTagCase, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    blocker: str
    recommended_next: str


def run_t86_analysis() -> T86Result:
    policy = AuditPolicy()
    cases = tuple(
        _audit_case(index, name, channel, role, evidence, policy)
        for index, (name, channel, role, evidence) in enumerate(
            ambiguous_tag_channel_cases(),
            start=1,
        )
    )
    return T86Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        cases=cases,
        strongest_claim=(
            "Inside the current executable protocol, perturbation response "
            "and signed ancestry can be independently decisive when timing "
            "and authenticated tags are deliberately ambiguous. The result "
            "rescues those channels from immediate schema deletion, but only "
            "as pre-registered raw-log isolation tests."
        ),
        weakened_claim=(
            "This does not upgrade Q1 into a detector theory. The same "
            "ambiguous-tag family with perturbation back-action or DAG "
            "truncation withholds D1 completely, so the channel claim is "
            "narrow and control-dependent."
        ),
        falsification_condition=(
            "T86 fails if the all-ambiguous negative control robustly "
            "recovers D1, if the clean perturbation-only or clean DAG-only "
            "families stop recovering both witness classes, or if the "
            "contaminated controls recover despite back-action/truncation."
        ),
        q1_update=(
            "Keep Q1 partially supported only as a detector-record "
            "admissibility protocol. Perturbation and DAG channels may stay "
            "in the core schema only as independently isolated, "
            "pre-registered raw-log tests under ambiguous timing/tag "
            "controls; they are not empirical support until a T78-style real "
            "deployment supplies those logs."
        ),
        blocker=(
            "The positive families are constructed fixture counts, not "
            "measured deployment logs. They also rely on the protocol's "
            "actual-class witness labels when computing whether recovery is "
            "correct, so the next real test must define copied and "
            "independent controls before data collection."
        ),
        recommended_next=(
            "Draft the T78 raw-log table needed for a real ambiguous-tag "
            "deployment: paired copied/independent controls, perturbation "
            "trials, signed ancestry exports, tag ambiguity rates, timing "
            "uncertainty, and pre-registered demotion rules."
        ),
    )


def ambiguous_tag_channel_cases() -> tuple[
    tuple[str, str, str, DeploymentEvidence],
    ...,
]:
    weak = _weak_ambiguous_fixture()
    return (
        (
            "all_channels_ambiguous_negative_control",
            "none",
            "negative_control",
            weak,
        ),
        (
            "clean_perturbation_only_rescue",
            "perturbation_response",
            "positive_test",
            replace(
                weak,
                name="clean_perturbation_only_rescue",
                dependent_perturbation_changes=ProportionEvidence(
                    995,
                    1000,
                    "dependent-copy perturbation responses",
                ),
                independent_perturbation_false_changes=ProportionEvidence(
                    2,
                    1000,
                    "independent-channel perturbation false changes",
                ),
                perturbation_back_action_events=ProportionEvidence(
                    2,
                    1000,
                    "perturbation back-action events",
                ),
                purpose=(
                    "Timing and authenticated tags are ambiguous; clean "
                    "perturbation response is the only reliable separator."
                ),
            ),
        ),
        (
            "backaction_contaminated_perturbation_control",
            "perturbation_response",
            "contamination_control",
            replace(
                weak,
                name="backaction_contaminated_perturbation_control",
                dependent_perturbation_changes=ProportionEvidence(
                    995,
                    1000,
                    "dependent-copy perturbation responses",
                ),
                independent_perturbation_false_changes=ProportionEvidence(
                    350,
                    1000,
                    "independent-channel perturbation false changes",
                ),
                perturbation_back_action_events=ProportionEvidence(
                    350,
                    1000,
                    "perturbation back-action events",
                ),
                purpose=(
                    "Perturbation appears sensitive but is contaminated by "
                    "back-action and independent-channel false changes."
                ),
            ),
        ),
        (
            "clean_dag_only_rescue",
            "signed_ancestry_dag",
            "positive_test",
            replace(
                weak,
                name="clean_dag_only_rescue",
                dag_observability=ProportionEvidence(
                    995,
                    1000,
                    "complete ancestry DAG observations",
                ),
                signed_dag_edges=ProportionEvidence(
                    995,
                    1000,
                    "verified signed DAG edges",
                ),
                dag_truncation_events=ProportionEvidence(
                    2,
                    1000,
                    "DAG truncation events",
                ),
                false_shared_dag_edges=ProportionEvidence(
                    2,
                    1000,
                    "false shared-ancestry edges",
                ),
                purpose=(
                    "Timing and authenticated tags are ambiguous; signed DAG "
                    "ancestry is the only reliable separator."
                ),
            ),
        ),
        (
            "truncated_dag_control",
            "signed_ancestry_dag",
            "contamination_control",
            replace(
                weak,
                name="truncated_dag_control",
                dag_observability=ProportionEvidence(
                    995,
                    1000,
                    "complete ancestry DAG observations",
                ),
                signed_dag_edges=ProportionEvidence(
                    995,
                    1000,
                    "verified signed DAG edges",
                ),
                dag_truncation_events=ProportionEvidence(
                    350,
                    1000,
                    "DAG truncation events",
                ),
                false_shared_dag_edges=ProportionEvidence(
                    350,
                    1000,
                    "false shared-ancestry edges",
                ),
                purpose=(
                    "DAG observability is high, but truncation and false "
                    "shared-edge rates make signed ancestry unsafe."
                ),
            ),
        ),
    )


def t86_result_to_dict(result: T86Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "cases": [
            {
                "name": case.name,
                "channel_under_test": case.channel_under_test,
                "role": case.role,
                "verdict": case.verdict,
                "rescues_with_ambiguous_tags": case.rescues_with_ambiguous_tags,
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


def _weak_ambiguous_fixture() -> DeploymentEvidence:
    signed = calibrated_signed_deployment_fixture()
    return replace(
        signed,
        name="all_channels_ambiguous_negative_control",
        local_sigma=TimingEvidence(0.65, 0.05, "local TDC rms timing"),
        archive_sigma=TimingEvidence(0.65, 0.05, "archive clock rms timing"),
        batching_window=TimingEvidence(
            1.00,
            0.05,
            "event-batch latency window",
        ),
        tag_retention=ProportionEvidence(500, 1000, "retained event tags"),
        signature_verification=ProportionEvidence(500, 1000, "verified signatures"),
        accepted_forged_tags=ProportionEvidence(
            150,
            1000,
            "accepted forged tags",
        ),
        accepted_spoofed_independent_tags=ProportionEvidence(
            500,
            1000,
            "accepted copied records with spoofed independent tags",
        ),
        independent_unique_tags=ProportionEvidence(
            500,
            1000,
            "independent records with unique tags",
        ),
        dependent_perturbation_changes=ProportionEvidence(
            500,
            1000,
            "dependent-copy perturbation responses",
        ),
        independent_perturbation_false_changes=ProportionEvidence(
            500,
            1000,
            "independent-channel perturbation false changes",
        ),
        perturbation_back_action_events=ProportionEvidence(
            400,
            1000,
            "perturbation back-action events",
        ),
        dag_observability=ProportionEvidence(
            500,
            1000,
            "complete ancestry DAG observations",
        ),
        signed_dag_edges=ProportionEvidence(
            500,
            1000,
            "verified signed DAG edges",
        ),
        dag_truncation_events=ProportionEvidence(
            400,
            1000,
            "DAG truncation events",
        ),
        false_shared_dag_edges=ProportionEvidence(
            300,
            1000,
            "false shared-ancestry edges",
        ),
        purpose=(
            "Negative control: timing, authenticated tags, perturbation, and "
            "DAG ancestry are all ambiguous enough that D1 should be withheld."
        ),
    )


def _audit_case(
    index: int,
    name: str,
    channel: str,
    role: str,
    evidence: DeploymentEvidence,
    policy: AuditPolicy,
) -> AmbiguousTagCase:
    outcome = sample_family(
        evidence_to_prior_family(evidence, policy),
        random.Random(SEED + index),
        SAMPLE_COUNT,
    )
    verdict = _verdict(outcome)
    rescues = role == "positive_test" and verdict == "robust_measured_recovery"
    return AmbiguousTagCase(
        name=name,
        channel_under_test=channel,
        role=role,
        evidence=evidence,
        outcome=outcome,
        verdict=verdict,
        rescues_with_ambiguous_tags=rescues,
        interpretation=_interpretation(channel, role, verdict),
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


def _interpretation(channel: str, role: str, verdict: str) -> str:
    if role == "negative_control":
        return (
            "All available timing/tag/provenance channels are ambiguous; the "
            f"protocol verdict is {verdict}."
        )
    if role == "positive_test":
        return (
            f"With timing and tags ambiguous, clean {channel} evidence alone "
            f"yields verdict {verdict}."
        )
    return (
        f"The {channel} channel is present but contaminated; the protocol "
        f"verdict is {verdict}."
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
