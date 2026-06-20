"""T72: physical provenance protocol model.

T70 replaced T68's ideal intervention-sensitive provenance rule with Boolean
degradation flags. T72 replaces those flags with interval/probability-valued
protocol parameters: clock uncertainty, authentication failure, archive
batching, trust boundaries, perturbation back-action, and partial DAG
observability.

The model is not a detector simulation. It is a finite protocol audit: under
which declared physical reliability assumptions can provenance evidence fix
the D1 independence partition before D1 finality is scored?
"""

from __future__ import annotations

from dataclasses import dataclass


RECONSTRUCTION_THRESHOLD = 2
PASSIVE_AGREEMENT = 0.92
PASSIVE_PHI = 0.84


@dataclass(frozen=True)
class Interval:
    low: float
    high: float

    def overlaps(self, other: "Interval") -> bool:
        return self.low <= other.high and other.low <= self.high

    def below(self, other: "Interval") -> bool:
        return self.high < other.low


@dataclass(frozen=True)
class PhysicalWitness:
    name: str
    actual_same_class: bool
    local_time: float
    archive_time: float
    information_bits: tuple[float, float] = (0.95, 0.95)


@dataclass(frozen=True)
class ClockProtocol:
    local_sigma: float
    archive_sigma: float
    batching_window: float
    copy_latency_interval: Interval


@dataclass(frozen=True)
class SignatureProtocol:
    tag_retention_prob: float
    verification_prob: float
    forgery_prob: float
    spoof_independent_prob: float
    independent_unique_tag_prob: float


@dataclass(frozen=True)
class TrustBoundary:
    detector_trust: float
    archive_trust: float
    transport_trust: float

    def multiplier(self) -> float:
        return min(self.detector_trust, self.archive_trust, self.transport_trust)


@dataclass(frozen=True)
class PerturbationProtocol:
    p_change_if_dependent: float
    p_change_if_independent: float
    back_action_prob: float


@dataclass(frozen=True)
class DagProtocol:
    observability: float
    signed_edge_prob: float
    truncation_prob: float
    false_shared_edge_prob: float


@dataclass(frozen=True)
class PhysicalProtocolRegime:
    name: str
    clock: ClockProtocol
    signature: SignatureProtocol
    trust: TrustBoundary
    perturbation: PerturbationProtocol
    dag: DagProtocol
    confidence_floor: float
    max_false_risk: float
    threshold_source: str
    purpose: str


@dataclass(frozen=True)
class ChannelEvidence:
    channel: str
    supports: str
    confidence: float
    false_risk: float
    accepted: bool
    interpretation: str


@dataclass(frozen=True)
class PartitionDecision:
    status: str
    inferred_same_class: bool | None
    inferred_classes: tuple[tuple[str, str], ...]
    accepted_channels: tuple[str, ...]
    max_dependence_confidence: float
    max_independence_confidence: float
    max_false_risk: float
    threshold_source: str
    pre_registered: bool
    depends_on_d1_outcome: bool
    interpretation: str


@dataclass(frozen=True)
class D1Profile:
    accessible_support: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.holder_redundancy,
            self.branch_support,
            self.reversal_cost,
        )


@dataclass(frozen=True)
class WitnessAnalysis:
    witness: PhysicalWitness
    regime: PhysicalProtocolRegime
    evidence: tuple[ChannelEvidence, ...]
    partition: PartitionDecision
    d1_profile: D1Profile | None
    observer_finalized: bool | None
    correctly_classified: bool | None


@dataclass(frozen=True)
class RegimeSummary:
    name: str
    verdict: str
    copied_status: str
    independent_status: str
    computable_d1: bool
    copied_d1: tuple[int, int, int, int] | None
    independent_d1: tuple[int, int, int, int] | None
    threshold_source: str
    interpretation: str


@dataclass(frozen=True)
class T72Result:
    analyses: tuple[WitnessAnalysis, ...]
    regime_table: tuple[RegimeSummary, ...]
    strongest_claim: str
    weakened_claim: str
    minimal_physical_conditions: str
    q1_recommendation: str
    falsification_condition: str
    recommended_next: str


def canonical_witnesses() -> tuple[PhysicalWitness, PhysicalWitness]:
    return (
        PhysicalWitness(
            name="dependent_copied_archive",
            actual_same_class=True,
            local_time=2.0,
            archive_time=4.0,
        ),
        PhysicalWitness(
            name="independent_overlapping_readout",
            actual_same_class=False,
            local_time=2.0,
            archive_time=2.0,
        ),
    )


def canonical_regimes() -> tuple[PhysicalProtocolRegime, ...]:
    copy_latency = Interval(1.0, 3.0)
    return (
        PhysicalProtocolRegime(
            name="robust_recovery_protocol",
            clock=ClockProtocol(0.05, 0.05, 0.05, copy_latency),
            signature=SignatureProtocol(0.99, 0.995, 0.001, 0.001, 0.995),
            trust=TrustBoundary(0.98, 0.98, 0.98),
            perturbation=PerturbationProtocol(0.98, 0.02, 0.02),
            dag=DagProtocol(0.98, 0.995, 0.01, 0.01),
            confidence_floor=0.80,
            max_false_risk=0.20,
            threshold_source="declared_physical_protocol",
            purpose="All provenance instruments are reliable.",
        ),
        PhysicalProtocolRegime(
            name="batched_clock_crypto_dag_recovery",
            clock=ClockProtocol(0.55, 0.55, 0.80, copy_latency),
            signature=SignatureProtocol(0.97, 0.99, 0.002, 0.002, 0.99),
            trust=TrustBoundary(0.96, 0.96, 0.96),
            perturbation=PerturbationProtocol(0.95, 0.05, 0.05),
            dag=DagProtocol(0.97, 0.99, 0.02, 0.01),
            confidence_floor=0.80,
            max_false_risk=0.20,
            threshold_source="declared_physical_protocol",
            purpose="Timing is ambiguous because archives batch writes, but signatures and DAG are reliable.",
        ),
        PhysicalProtocolRegime(
            name="lossy_tags_clean_intervention_recovery",
            clock=ClockProtocol(0.15, 0.15, 0.10, copy_latency),
            signature=SignatureProtocol(0.25, 0.50, 0.01, 0.01, 0.60),
            trust=TrustBoundary(0.94, 0.94, 0.94),
            perturbation=PerturbationProtocol(0.98, 0.02, 0.03),
            dag=DagProtocol(0.94, 0.98, 0.04, 0.02),
            confidence_floor=0.80,
            max_false_risk=0.20,
            threshold_source="declared_physical_protocol",
            purpose="Tags are usually missing, but clean interventions and signed ancestry remain.",
        ),
        PhysicalProtocolRegime(
            name="ambiguous_withhold_low_trust",
            clock=ClockProtocol(0.70, 0.70, 0.80, copy_latency),
            signature=SignatureProtocol(0.50, 0.55, 0.15, 0.20, 0.55),
            trust=TrustBoundary(0.55, 0.45, 0.50),
            perturbation=PerturbationProtocol(0.70, 0.30, 0.35),
            dag=DagProtocol(0.55, 0.70, 0.35, 0.20),
            confidence_floor=0.80,
            max_false_risk=0.20,
            threshold_source="declared_physical_protocol",
            purpose="No channel has enough trusted reliability to fix provenance.",
        ),
        PhysicalProtocolRegime(
            name="partial_dag_ad_hoc_threshold",
            clock=ClockProtocol(0.80, 0.80, 0.90, copy_latency),
            signature=SignatureProtocol(0.20, 0.40, 0.20, 0.20, 0.50),
            trust=TrustBoundary(0.70, 0.70, 0.70),
            perturbation=PerturbationProtocol(0.60, 0.40, 0.40),
            dag=DagProtocol(0.62, 0.75, 0.30, 0.20),
            confidence_floor=0.55,
            max_false_risk=0.35,
            threshold_source="ad_hoc_partial_dag_threshold",
            purpose="Only a partial-DAG score remains; the acceptance floor is not physically justified.",
        ),
        PhysicalProtocolRegime(
            name="forged_tags_false_independence_risk",
            clock=ClockProtocol(0.90, 0.90, 1.00, copy_latency),
            signature=SignatureProtocol(0.95, 0.95, 0.45, 0.95, 0.98),
            trust=TrustBoundary(0.92, 0.92, 0.92),
            perturbation=PerturbationProtocol(0.35, 0.10, 0.25),
            dag=DagProtocol(0.25, 0.50, 0.70, 0.10),
            confidence_floor=0.80,
            max_false_risk=0.97,
            threshold_source="declared_physical_protocol",
            purpose="Forgery makes a copied archive look like a distinct signed origin.",
        ),
        PhysicalProtocolRegime(
            name="backaction_false_dependence_risk",
            clock=ClockProtocol(0.80, 0.80, 0.90, copy_latency),
            signature=SignatureProtocol(0.35, 0.55, 0.15, 0.10, 0.50),
            trust=TrustBoundary(0.90, 0.90, 0.90),
            perturbation=PerturbationProtocol(0.95, 0.92, 0.02),
            dag=DagProtocol(0.30, 0.50, 0.65, 0.15),
            confidence_floor=0.80,
            max_false_risk=0.95,
            threshold_source="declared_physical_protocol",
            purpose="The intervention itself strongly couples readout chains.",
        ),
    )


def run_t72_analysis() -> T72Result:
    analyses = tuple(
        analyze_witness(witness, regime)
        for regime in canonical_regimes()
        for witness in canonical_witnesses()
    )
    table = tuple(summarize_regime(regime, analyses) for regime in canonical_regimes())
    return T72Result(
        analyses=analyses,
        regime_table=table,
        strongest_claim=(
            "A physical provenance protocol can fix D1 independence classes "
            "before finality scoring when at least one dependence channel and "
            "one independence channel clear declared reliability bounds from "
            "the protocol rather than ad hoc post hoc thresholds."
        ),
        weakened_claim=(
            "The recovery is protocol-relative. If authentication, DAG "
            "observability, trust boundaries, and perturbation controls do not "
            "clear their declared reliability bounds, D1 must be withheld; in "
            "hostile regimes the protocol can create false independence or "
            "false dependence risk."
        ),
        minimal_physical_conditions=(
            "Non-arbitrary D1 detector finality requires declared clock/error "
            "bounds, authenticated tags or signed ancestry with high "
            "verification probability, trusted subsystem boundaries, bounded "
            "archive batching, and a perturbation channel whose back-action "
            "risk is below the protocol's false-risk ceiling."
        ),
        q1_recommendation=(
            "Keep Q1 partially supported only as a detector-record provenance "
            "accounting framework under explicit physical protocol "
            "assumptions. Do not claim detector-level provenance recovery "
            "without those assumptions."
        ),
        falsification_condition=(
            "The detector branch should be demoted if physically realistic "
            "protocol parameters generically fall into withhold, false "
            "independence, or false dependence regimes, or if the acceptance "
            "floors cannot be justified independently of the desired D1 result."
        ),
        recommended_next=(
            "Replace the finite regime table with calibration data or a Monte "
            "Carlo protocol simulation over clock, signature, batching, DAG, "
            "trust, and back-action distributions."
        ),
    )


def analyze_witness(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
) -> WitnessAnalysis:
    evidence = evidence_for(witness, regime)
    partition = infer_partition(witness, regime, evidence)
    d1_profile = compute_d1_after_partition(witness, partition)
    observer_finalized = (
        d1_profile.holder_redundancy >= RECONSTRUCTION_THRESHOLD
        if d1_profile is not None
        else None
    )
    correctly_classified = (
        partition.inferred_same_class == witness.actual_same_class
        if partition.inferred_same_class is not None
        else None
    )
    return WitnessAnalysis(
        witness=witness,
        regime=regime,
        evidence=evidence,
        partition=partition,
        d1_profile=d1_profile,
        observer_finalized=observer_finalized,
        correctly_classified=correctly_classified,
    )


def evidence_for(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
) -> tuple[ChannelEvidence, ...]:
    trust = regime.trust.multiplier()
    return (
        _timing_evidence(witness, regime, trust),
        _tag_dependence_evidence(witness, regime, trust),
        _tag_independence_evidence(witness, regime, trust),
        _perturbation_dependence_evidence(witness, regime, trust),
        _perturbation_independence_evidence(witness, regime, trust),
        _dag_dependence_evidence(witness, regime, trust),
        _dag_independence_evidence(witness, regime, trust),
    )


def infer_partition(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    evidence: tuple[ChannelEvidence, ...],
) -> PartitionDecision:
    if regime.threshold_source != "declared_physical_protocol":
        return PartitionDecision(
            status="withhold_threshold_dependent",
            inferred_same_class=None,
            inferred_classes=(),
            accepted_channels=(),
            max_dependence_confidence=_max_confidence(evidence, "same"),
            max_independence_confidence=_max_confidence(evidence, "distinct"),
            max_false_risk=max(item.false_risk for item in evidence),
            threshold_source=regime.threshold_source,
            pre_registered=True,
            depends_on_d1_outcome=False,
            interpretation=(
                "The available evidence requires a threshold not justified by "
                "the physical protocol; D1 is withheld."
            ),
        )

    accepted_same = tuple(
        item for item in evidence if item.supports == "same" and item.accepted
    )
    accepted_distinct = tuple(
        item for item in evidence if item.supports == "distinct" and item.accepted
    )
    max_false_risk = max(
        (item.false_risk for item in accepted_same + accepted_distinct),
        default=max(item.false_risk for item in evidence),
    )
    if accepted_same and accepted_distinct:
        return PartitionDecision(
            status="withhold_conflicting_evidence",
            inferred_same_class=None,
            inferred_classes=(),
            accepted_channels=tuple(item.channel for item in accepted_same + accepted_distinct),
            max_dependence_confidence=_max_confidence(evidence, "same"),
            max_independence_confidence=_max_confidence(evidence, "distinct"),
            max_false_risk=max_false_risk,
            threshold_source=regime.threshold_source,
            pre_registered=True,
            depends_on_d1_outcome=False,
            interpretation="Accepted provenance channels conflict; D1 is withheld.",
        )
    if accepted_same:
        status = (
            "false_dependence_risk"
            if not witness.actual_same_class
            else "accepted_same_class"
        )
        return PartitionDecision(
            status=status,
            inferred_same_class=True,
            inferred_classes=(("local_log", "P0"), ("archive", "P0")),
            accepted_channels=tuple(item.channel for item in accepted_same),
            max_dependence_confidence=_max_confidence(evidence, "same"),
            max_independence_confidence=_max_confidence(evidence, "distinct"),
            max_false_risk=max_false_risk,
            threshold_source=regime.threshold_source,
            pre_registered=True,
            depends_on_d1_outcome=False,
            interpretation="Protocol-accepted evidence assigns one independence class.",
        )
    if accepted_distinct:
        status = (
            "false_independence_risk"
            if witness.actual_same_class
            else "accepted_distinct_classes"
        )
        return PartitionDecision(
            status=status,
            inferred_same_class=False,
            inferred_classes=(("local_log", "P0"), ("archive", "P1")),
            accepted_channels=tuple(item.channel for item in accepted_distinct),
            max_dependence_confidence=_max_confidence(evidence, "same"),
            max_independence_confidence=_max_confidence(evidence, "distinct"),
            max_false_risk=max_false_risk,
            threshold_source=regime.threshold_source,
            pre_registered=True,
            depends_on_d1_outcome=False,
            interpretation="Protocol-accepted evidence assigns distinct classes.",
        )
    return PartitionDecision(
        status="withhold_ambiguous",
        inferred_same_class=None,
        inferred_classes=(),
        accepted_channels=(),
        max_dependence_confidence=_max_confidence(evidence, "same"),
        max_independence_confidence=_max_confidence(evidence, "distinct"),
        max_false_risk=max(item.false_risk for item in evidence),
        threshold_source=regime.threshold_source,
        pre_registered=True,
        depends_on_d1_outcome=False,
        interpretation="No channel clears the declared protocol bounds; D1 is withheld.",
    )


def compute_d1_after_partition(
    witness: PhysicalWitness,
    partition: PartitionDecision,
) -> D1Profile | None:
    if partition.inferred_same_class is None:
        return None
    accessible_support = sum(1 for bits in witness.information_bits if bits >= 0.75)
    holder_redundancy = 1 if partition.inferred_same_class else 2
    reversal_cost = (
        holder_redundancy - RECONSTRUCTION_THRESHOLD + 1
        if holder_redundancy >= RECONSTRUCTION_THRESHOLD
        else 0
    )
    return D1Profile(
        accessible_support=accessible_support,
        holder_redundancy=holder_redundancy,
        branch_support=1,
        reversal_cost=reversal_cost,
    )


def summarize_regime(
    regime: PhysicalProtocolRegime,
    analyses: tuple[WitnessAnalysis, ...],
) -> RegimeSummary:
    copied = _analysis_by_witness(analyses, regime.name, "dependent_copied_archive")
    independent = _analysis_by_witness(
        analyses,
        regime.name,
        "independent_overlapping_readout",
    )
    statuses = {copied.partition.status, independent.partition.status}
    computable = copied.d1_profile is not None and independent.d1_profile is not None
    if copied.correctly_classified is True and independent.correctly_classified is True:
        verdict = "robust_provenance_recovery"
        interpretation = "Both provenance classes are fixed before D1 scoring."
    elif "false_independence_risk" in statuses:
        verdict = "false_independence_risk"
        interpretation = "A copied archive is accepted as independent."
    elif "false_dependence_risk" in statuses:
        verdict = "false_dependence_risk"
        interpretation = "An independent readout is accepted as dependent."
    elif "withhold_threshold_dependent" in statuses:
        verdict = "ambiguous_withhold_threshold_dependent"
        interpretation = "The only recovery route uses an unjustified threshold."
    elif "withhold_conflicting_evidence" in statuses:
        verdict = "ambiguous_withhold_conflicting"
        interpretation = "Accepted protocol evidence conflicts."
    else:
        verdict = "ambiguous_withhold_region"
        interpretation = "Protocol evidence is too weak; D1 is not computed."
    return RegimeSummary(
        name=regime.name,
        verdict=verdict,
        copied_status=copied.partition.status,
        independent_status=independent.partition.status,
        computable_d1=computable,
        copied_d1=copied.d1_profile.as_tuple() if copied.d1_profile else None,
        independent_d1=(
            independent.d1_profile.as_tuple() if independent.d1_profile else None
        ),
        threshold_source=regime.threshold_source,
        interpretation=interpretation,
    )


def t72_result_to_dict(result: T72Result) -> dict[str, object]:
    return {
        "passive_statistics": {
            "agreement_probability": PASSIVE_AGREEMENT,
            "phi_correlation": PASSIVE_PHI,
        },
        "regime_table": [
            {
                "name": summary.name,
                "verdict": summary.verdict,
                "copied_status": summary.copied_status,
                "independent_status": summary.independent_status,
                "computable_d1": summary.computable_d1,
                "copied_d1": list(summary.copied_d1) if summary.copied_d1 else None,
                "independent_d1": (
                    list(summary.independent_d1) if summary.independent_d1 else None
                ),
                "threshold_source": summary.threshold_source,
                "interpretation": summary.interpretation,
            }
            for summary in result.regime_table
        ],
        "analyses": [_analysis_to_dict(analysis) for analysis in result.analyses],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "minimal_physical_conditions": result.minimal_physical_conditions,
        "q1_recommendation": result.q1_recommendation,
        "falsification_condition": result.falsification_condition,
        "recommended_next": result.recommended_next,
    }


def _timing_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    gap = witness.archive_time - witness.local_time
    uncertainty = (
        2.0 * regime.clock.local_sigma
        + 2.0 * regime.clock.archive_sigma
        + regime.clock.batching_window
    )
    gap_interval = Interval(gap - uncertainty, gap + uncertainty)
    confidence = trust * max(0.0, 1.0 - uncertainty / 4.0)
    if gap_interval.overlaps(regime.clock.copy_latency_interval):
        supports = "same"
        false_risk = 1.0 - confidence
        interpretation = "Observed timing is compatible with declared copy latency."
    elif gap_interval.below(regime.clock.copy_latency_interval):
        supports = "distinct"
        false_risk = 1.0 - confidence
        interpretation = "Observed timing is too fast for declared copy latency."
    else:
        supports = "none"
        false_risk = 1.0
        interpretation = "Clock and batching uncertainty make timing unusable."
    return _channel(
        "clock_latency_interval",
        supports,
        confidence,
        false_risk,
        regime,
        interpretation,
    )


def _tag_dependence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    sig = regime.signature
    confidence = trust * sig.tag_retention_prob * sig.verification_prob * (1.0 - sig.forgery_prob)
    if witness.actual_same_class and sig.spoof_independent_prob < 0.5:
        supports = "same"
    elif not witness.actual_same_class and sig.independent_unique_tag_prob < 0.5:
        supports = "same"
    else:
        supports = "none"
    return _channel(
        "authenticated_duplicate_origin_tag",
        supports,
        confidence,
        sig.forgery_prob + (1.0 - sig.verification_prob),
        regime,
        "Duplicate authenticated origin tags indicate shared provenance.",
    )


def _tag_independence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    sig = regime.signature
    if witness.actual_same_class:
        confidence = trust * sig.spoof_independent_prob * sig.verification_prob
        false_risk = sig.spoof_independent_prob
    else:
        confidence = trust * sig.independent_unique_tag_prob * sig.verification_prob * (1.0 - sig.forgery_prob)
        false_risk = sig.forgery_prob + (1.0 - sig.independent_unique_tag_prob)
    supports = "distinct" if confidence > 0.0 else "none"
    return _channel(
        "authenticated_distinct_origin_tags",
        supports,
        confidence,
        false_risk,
        regime,
        "Distinct authenticated origin tags indicate separate provenance.",
    )


def _perturbation_dependence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    pert = regime.perturbation
    if witness.actual_same_class:
        observed_change = pert.p_change_if_dependent
    else:
        observed_change = min(1.0, pert.p_change_if_independent + pert.back_action_prob)
    confidence = trust * observed_change * (1.0 - pert.back_action_prob)
    false_risk = pert.back_action_prob + (pert.p_change_if_independent if not witness.actual_same_class else 0.0)
    return _channel(
        "perturbation_change_response",
        "same",
        confidence,
        min(1.0, false_risk),
        regime,
        "Changing one channel changes the other under intervention.",
    )


def _perturbation_independence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    pert = regime.perturbation
    if witness.actual_same_class:
        no_change = 1.0 - pert.p_change_if_dependent
    else:
        no_change = max(0.0, 1.0 - pert.p_change_if_independent - pert.back_action_prob)
    confidence = trust * no_change * (1.0 - pert.back_action_prob)
    false_risk = pert.back_action_prob + (1.0 - pert.p_change_if_dependent if witness.actual_same_class else 0.0)
    return _channel(
        "perturbation_no_change_response",
        "distinct",
        confidence,
        min(1.0, false_risk),
        regime,
        "Perturbing one channel does not change the other.",
    )


def _dag_dependence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    dag = regime.dag
    if witness.actual_same_class:
        confidence = trust * dag.observability * dag.signed_edge_prob * (1.0 - dag.truncation_prob)
        false_risk = dag.truncation_prob
    else:
        confidence = trust * dag.false_shared_edge_prob * dag.signed_edge_prob
        false_risk = dag.false_shared_edge_prob
    return _channel(
        "signed_shared_ancestry",
        "same",
        confidence,
        false_risk,
        regime,
        "A signed provenance DAG shows shared non-common ancestry.",
    )


def _dag_independence_evidence(
    witness: PhysicalWitness,
    regime: PhysicalProtocolRegime,
    trust: float,
) -> ChannelEvidence:
    dag = regime.dag
    if witness.actual_same_class:
        confidence = trust * dag.truncation_prob * dag.signed_edge_prob
        false_risk = dag.truncation_prob
    else:
        confidence = trust * dag.observability * dag.signed_edge_prob * (1.0 - dag.false_shared_edge_prob)
        false_risk = dag.false_shared_edge_prob + (1.0 - dag.observability)
    return _channel(
        "signed_disjoint_ancestry",
        "distinct",
        confidence,
        min(1.0, false_risk),
        regime,
        "A signed provenance DAG shows disjoint ancestry above common source.",
    )


def _channel(
    name: str,
    supports: str,
    confidence: float,
    false_risk: float,
    regime: PhysicalProtocolRegime,
    interpretation: str,
) -> ChannelEvidence:
    accepted = (
        supports in {"same", "distinct"}
        and confidence >= regime.confidence_floor
        and false_risk <= regime.max_false_risk
    )
    return ChannelEvidence(
        channel=name,
        supports=supports,
        confidence=round(confidence, 4),
        false_risk=round(false_risk, 4),
        accepted=accepted,
        interpretation=interpretation,
    )


def _max_confidence(
    evidence: tuple[ChannelEvidence, ...],
    support: str,
) -> float:
    return max(
        (item.confidence for item in evidence if item.supports == support),
        default=0.0,
    )


def _analysis_by_witness(
    analyses: tuple[WitnessAnalysis, ...],
    regime_name: str,
    witness_name: str,
) -> WitnessAnalysis:
    for analysis in analyses:
        if analysis.regime.name == regime_name and analysis.witness.name == witness_name:
            return analysis
    raise ValueError(f"missing analysis: {regime_name}/{witness_name}")


def _analysis_to_dict(analysis: WitnessAnalysis) -> dict[str, object]:
    d1_profile = (
        {
            "accessible_support": analysis.d1_profile.accessible_support,
            "holder_redundancy": analysis.d1_profile.holder_redundancy,
            "branch_support": analysis.d1_profile.branch_support,
            "reversal_cost": analysis.d1_profile.reversal_cost,
            "profile_tuple": list(analysis.d1_profile.as_tuple()),
        }
        if analysis.d1_profile is not None
        else None
    )
    return {
        "regime": analysis.regime.name,
        "witness": analysis.witness.name,
        "actual_same_class": analysis.witness.actual_same_class,
        "evidence": [
            {
                "channel": item.channel,
                "supports": item.supports,
                "confidence": item.confidence,
                "false_risk": item.false_risk,
                "accepted": item.accepted,
                "interpretation": item.interpretation,
            }
            for item in analysis.evidence
        ],
        "partition": {
            "status": analysis.partition.status,
            "inferred_same_class": analysis.partition.inferred_same_class,
            "inferred_classes": list(analysis.partition.inferred_classes),
            "accepted_channels": list(analysis.partition.accepted_channels),
            "max_dependence_confidence": (
                analysis.partition.max_dependence_confidence
            ),
            "max_independence_confidence": (
                analysis.partition.max_independence_confidence
            ),
            "max_false_risk": analysis.partition.max_false_risk,
            "threshold_source": analysis.partition.threshold_source,
            "pre_registered": analysis.partition.pre_registered,
            "depends_on_d1_outcome": analysis.partition.depends_on_d1_outcome,
            "interpretation": analysis.partition.interpretation,
        },
        "d1_profile": d1_profile,
        "observer_finalized": analysis.observer_finalized,
        "correctly_classified": analysis.correctly_classified,
    }
