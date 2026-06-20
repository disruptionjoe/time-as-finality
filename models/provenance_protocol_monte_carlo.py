"""T74: Monte Carlo audit of the T72 physical provenance protocol.

The T72 regime table gave hand-picked positive and negative protocol regimes.
T74 asks whether those regimes occupy meaningful parameter volume under simple
stress priors, or whether robust provenance recovery survives only in a narrow
engineered corner of parameter space.
"""

from __future__ import annotations

from dataclasses import dataclass
import random

from models.physical_provenance_protocol import (
    ClockProtocol,
    DagProtocol,
    PhysicalProtocolRegime,
    PerturbationProtocol,
    SignatureProtocol,
    TrustBoundary,
    analyze_witness,
    canonical_witnesses,
)


SAMPLE_COUNT = 400
SEED = 74017


@dataclass(frozen=True)
class Range:
    low: float
    high: float

    def sample(self, rng: random.Random) -> float:
        return rng.uniform(self.low, self.high)


@dataclass(frozen=True)
class PriorFamily:
    name: str
    local_sigma: Range
    archive_sigma: Range
    batching_window: Range
    tag_retention: Range
    verification: Range
    forgery: Range
    spoof_independent: Range
    unique_independent_tag: Range
    detector_trust: Range
    archive_trust: Range
    transport_trust: Range
    p_change_dependent: Range
    p_change_independent: Range
    back_action: Range
    observability: Range
    signed_edge: Range
    truncation: Range
    false_shared_edge: Range
    confidence_floor: Range
    max_false_risk: Range
    declared_threshold_prob: float
    purpose: str


@dataclass(frozen=True)
class FamilyOutcome:
    sample_count: int
    robust_rate: float
    withhold_rate: float
    threshold_dependent_rate: float
    false_independence_rate: float
    false_dependence_rate: float
    computable_d1_rate: float
    robust_count: int
    withhold_count: int
    threshold_dependent_count: int
    false_independence_count: int
    false_dependence_count: int
    computable_d1_count: int


@dataclass(frozen=True)
class T74Result:
    sample_count: int
    seed: int
    family_outcomes: dict[str, FamilyOutcome]
    strongest_claim: str
    weakened_claim: str
    blocker: str
    recommended_next: str


def prior_families() -> tuple[PriorFamily, ...]:
    return (
        PriorFamily(
            name="engineered_lab",
            local_sigma=Range(0.01, 0.12),
            archive_sigma=Range(0.01, 0.12),
            batching_window=Range(0.01, 0.20),
            tag_retention=Range(0.88, 1.00),
            verification=Range(0.92, 1.00),
            forgery=Range(0.00, 0.03),
            spoof_independent=Range(0.00, 0.03),
            unique_independent_tag=Range(0.92, 1.00),
            detector_trust=Range(0.90, 1.00),
            archive_trust=Range(0.90, 1.00),
            transport_trust=Range(0.90, 1.00),
            p_change_dependent=Range(0.90, 1.00),
            p_change_independent=Range(0.00, 0.08),
            back_action=Range(0.00, 0.05),
            observability=Range(0.90, 1.00),
            signed_edge=Range(0.92, 1.00),
            truncation=Range(0.00, 0.08),
            false_shared_edge=Range(0.00, 0.04),
            confidence_floor=Range(0.78, 0.85),
            max_false_risk=Range(0.12, 0.22),
            declared_threshold_prob=1.0,
            purpose="High-control laboratory detector with authenticated provenance.",
        ),
        PriorFamily(
            name="mixed_lab",
            local_sigma=Range(0.05, 0.45),
            archive_sigma=Range(0.05, 0.45),
            batching_window=Range(0.05, 0.65),
            tag_retention=Range(0.45, 0.98),
            verification=Range(0.60, 0.99),
            forgery=Range(0.00, 0.18),
            spoof_independent=Range(0.00, 0.20),
            unique_independent_tag=Range(0.55, 0.98),
            detector_trust=Range(0.65, 0.98),
            archive_trust=Range(0.60, 0.98),
            transport_trust=Range(0.60, 0.98),
            p_change_dependent=Range(0.70, 0.99),
            p_change_independent=Range(0.02, 0.28),
            back_action=Range(0.02, 0.22),
            observability=Range(0.55, 0.98),
            signed_edge=Range(0.65, 0.99),
            truncation=Range(0.02, 0.25),
            false_shared_edge=Range(0.00, 0.18),
            confidence_floor=Range(0.75, 0.88),
            max_false_risk=Range(0.14, 0.28),
            declared_threshold_prob=0.9,
            purpose="Partially instrumented lab detector with moderate trust and metadata loss.",
        ),
        PriorFamily(
            name="field_degraded",
            local_sigma=Range(0.25, 0.95),
            archive_sigma=Range(0.25, 0.95),
            batching_window=Range(0.30, 1.10),
            tag_retention=Range(0.10, 0.80),
            verification=Range(0.35, 0.90),
            forgery=Range(0.05, 0.45),
            spoof_independent=Range(0.05, 0.50),
            unique_independent_tag=Range(0.30, 0.85),
            detector_trust=Range(0.35, 0.90),
            archive_trust=Range(0.30, 0.90),
            transport_trust=Range(0.30, 0.90),
            p_change_dependent=Range(0.45, 0.98),
            p_change_independent=Range(0.10, 0.60),
            back_action=Range(0.08, 0.45),
            observability=Range(0.20, 0.85),
            signed_edge=Range(0.30, 0.90),
            truncation=Range(0.10, 0.60),
            false_shared_edge=Range(0.05, 0.35),
            confidence_floor=Range(0.72, 0.90),
            max_false_risk=Range(0.16, 0.40),
            declared_threshold_prob=0.7,
            purpose="Degraded or distributed instrumentation with partial trust and partial observability.",
        ),
    )


def run_t74_analysis() -> T74Result:
    rng = random.Random(SEED)
    families = prior_families()
    outcomes = {
        family.name: sample_family(family, rng, SAMPLE_COUNT)
        for family in families
    }
    strongest_claim = (
        "Robust detector-provenance recovery is not a generic consequence of "
        "having calibrated detector channels. In this audit it occupies a "
        "high-trust, low-back-action, high-authentication corner of protocol "
        "space and drops sharply under broader stress priors."
    )
    weakened_claim = (
        "Under the mixed and degraded priors, robust recovery disappeared "
        "entirely; the protocol mostly withheld D1 rather than recovering a "
        "partition. Q1's detector branch should therefore be treated as an "
        "engineered protocol claim, not a generic measurement claim."
    )
    blocker = (
        "The priors are stress priors, not calibration posteriors. Without "
        "detector-specific calibration data, T74 quantifies fragility but not "
        "real experimental frequency."
    )
    recommended_next = (
        "Map one concrete detector stack onto T72/T74 parameters and replace "
        "the stress priors with measured posteriors for clocks, "
        "authentication, batching, trust, back-action, and DAG observability."
    )
    return T74Result(
        sample_count=SAMPLE_COUNT,
        seed=SEED,
        family_outcomes=outcomes,
        strongest_claim=strongest_claim,
        weakened_claim=weakened_claim,
        blocker=blocker,
        recommended_next=recommended_next,
    )


def t74_result_to_dict(result: T74Result) -> dict[str, object]:
    return {
        "sample_count": result.sample_count,
        "seed": result.seed,
        "family_outcomes": {
            name: {
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
            for name, outcome in result.family_outcomes.items()
        },
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def sample_family(
    family: PriorFamily,
    rng: random.Random,
    sample_count: int = SAMPLE_COUNT,
) -> FamilyOutcome:
    robust = 0
    withhold = 0
    threshold_dependent = 0
    false_independence = 0
    false_dependence = 0
    computable_d1 = 0

    witnesses = canonical_witnesses()
    for index in range(sample_count):
        regime = _sample_regime(family, rng, index)
        analyses = tuple(analyze_witness(witness, regime) for witness in witnesses)
        copied, independent = analyses
        statuses = {copied.partition.status, independent.partition.status}

        if copied.correctly_classified and independent.correctly_classified:
            robust += 1
        elif "false_independence_risk" in statuses:
            false_independence += 1
        elif "false_dependence_risk" in statuses:
            false_dependence += 1
        elif "withhold_threshold_dependent" in statuses:
            threshold_dependent += 1
        else:
            withhold += 1

        if copied.d1_profile is not None and independent.d1_profile is not None:
            computable_d1 += 1

    return FamilyOutcome(
        sample_count=sample_count,
        robust_rate=round(robust / sample_count, 4),
        withhold_rate=round(withhold / sample_count, 4),
        threshold_dependent_rate=round(threshold_dependent / sample_count, 4),
        false_independence_rate=round(false_independence / sample_count, 4),
        false_dependence_rate=round(false_dependence / sample_count, 4),
        computable_d1_rate=round(computable_d1 / sample_count, 4),
        robust_count=robust,
        withhold_count=withhold,
        threshold_dependent_count=threshold_dependent,
        false_independence_count=false_independence,
        false_dependence_count=false_dependence,
        computable_d1_count=computable_d1,
    )


def _sample_regime(
    family: PriorFamily,
    rng: random.Random,
    index: int,
) -> PhysicalProtocolRegime:
    threshold_source = (
        "declared_physical_protocol"
        if rng.random() <= family.declared_threshold_prob
        else "ad_hoc_partial_dag_threshold"
    )
    return PhysicalProtocolRegime(
        name=f"{family.name}_sample_{index}",
        clock=ClockProtocol(
            local_sigma=family.local_sigma.sample(rng),
            archive_sigma=family.archive_sigma.sample(rng),
            batching_window=family.batching_window.sample(rng),
            copy_latency_interval=_copy_latency_interval(),
        ),
        signature=SignatureProtocol(
            tag_retention_prob=family.tag_retention.sample(rng),
            verification_prob=family.verification.sample(rng),
            forgery_prob=family.forgery.sample(rng),
            spoof_independent_prob=family.spoof_independent.sample(rng),
            independent_unique_tag_prob=family.unique_independent_tag.sample(rng),
        ),
        trust=TrustBoundary(
            detector_trust=family.detector_trust.sample(rng),
            archive_trust=family.archive_trust.sample(rng),
            transport_trust=family.transport_trust.sample(rng),
        ),
        perturbation=PerturbationProtocol(
            p_change_if_dependent=family.p_change_dependent.sample(rng),
            p_change_if_independent=family.p_change_independent.sample(rng),
            back_action_prob=family.back_action.sample(rng),
        ),
        dag=DagProtocol(
            observability=family.observability.sample(rng),
            signed_edge_prob=family.signed_edge.sample(rng),
            truncation_prob=family.truncation.sample(rng),
            false_shared_edge_prob=family.false_shared_edge.sample(rng),
        ),
        confidence_floor=family.confidence_floor.sample(rng),
        max_false_risk=family.max_false_risk.sample(rng),
        threshold_source=threshold_source,
        purpose=family.purpose,
    )


def _copy_latency_interval():
    from models.physical_provenance_protocol import Interval

    return Interval(1.0, 3.0)
