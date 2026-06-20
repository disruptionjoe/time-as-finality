"""T70: detector provenance robustness stress test.

T68 gave a conditional positive result: intervention-sensitive provenance
metadata can separate a copied archive from an independent readout even when
passive detector statistics are identical. T70 asks whether that rule survives
realistic degradation: clock uncertainty, tag loss or forgery, archive latency,
perturbation back-action, and incomplete provenance DAGs.

The model is intentionally conservative. If degraded metadata no longer fixes
the independence partition before D1 scoring, the rule abstains and D1 finality
is unavailable. That makes the failure mode explicit instead of silently
falling back to passive correlations, thresholds, or semantic labels.
"""

from __future__ import annotations

from dataclasses import dataclass


RECONSTRUCTION_THRESHOLD = 2
PASSIVE_AGREEMENT = 0.92
PASSIVE_PHI = 0.84


@dataclass(frozen=True)
class T68Witness:
    name: str
    actual_same_class: bool
    local_time: float
    archive_time: float
    baseline_tags_equal: bool
    baseline_perturbation_changes_other: bool
    baseline_shared_noncommon_ancestry: bool
    information_bits: tuple[float, float] = (0.95, 0.95)


@dataclass(frozen=True)
class DegradationRegime:
    name: str
    clock_uncertainty: float
    tags_present: bool
    tags_authenticated: bool
    copied_tag_spoofed_independent: bool
    archive_latency_hidden: bool
    perturbation_back_action: bool
    dag_completeness: float
    accepts_partial_dag_threshold: bool
    purpose: str


@dataclass(frozen=True)
class EvidenceVector:
    timing_dependence: bool
    duplicate_tag_dependence: bool
    distinct_tag_independence: bool
    perturbation_dependence: bool
    perturbation_independence: bool
    dag_dependence: bool
    dag_independence: bool
    ambiguous_channels: tuple[str, ...]
    threshold_or_label_dependent: bool

    def dependence_evidence(self) -> bool:
        return (
            self.timing_dependence
            or self.duplicate_tag_dependence
            or self.perturbation_dependence
            or self.dag_dependence
        )

    def independence_evidence(self) -> bool:
        return (
            self.distinct_tag_independence
            or self.perturbation_independence
            or self.dag_independence
        )


@dataclass(frozen=True)
class PartitionDecision:
    status: str
    inferred_same_class: bool | None
    inferred_classes: tuple[tuple[str, str], ...]
    reason: str
    pre_registered: bool
    depends_on_d1_outcome: bool
    threshold_or_label_dependent: bool


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
    witness: T68Witness
    regime: DegradationRegime
    evidence: EvidenceVector
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
    preserves_partition: bool
    clean_failure: bool
    threshold_or_label_dependent: bool
    minimal_metadata_used: tuple[str, ...]
    interpretation: str


@dataclass(frozen=True)
class T70Result:
    witness_analyses: tuple[WitnessAnalysis, ...]
    robustness_table: tuple[RegimeSummary, ...]
    minimal_metadata_requirement: str
    strongest_claim: str
    weakened_claim: str
    q1_recommendation: str
    falsification_condition: str
    recommended_next: str


def canonical_witnesses() -> tuple[T68Witness, T68Witness]:
    return (
        T68Witness(
            name="dependent_copied_archive",
            actual_same_class=True,
            local_time=2.0,
            archive_time=4.0,
            baseline_tags_equal=True,
            baseline_perturbation_changes_other=True,
            baseline_shared_noncommon_ancestry=True,
        ),
        T68Witness(
            name="independent_overlapping_readout",
            actual_same_class=False,
            local_time=2.0,
            archive_time=2.0,
            baseline_tags_equal=False,
            baseline_perturbation_changes_other=False,
            baseline_shared_noncommon_ancestry=False,
        ),
    )


def canonical_regimes() -> tuple[DegradationRegime, ...]:
    return (
        DegradationRegime(
            name="ideal_t68_metadata",
            clock_uncertainty=0.05,
            tags_present=True,
            tags_authenticated=True,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=False,
            perturbation_back_action=False,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="Baseline T68 intervention/provenance rule.",
        ),
        DegradationRegime(
            name="clock_uncertainty_only",
            clock_uncertainty=1.25,
            tags_present=True,
            tags_authenticated=True,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=False,
            perturbation_back_action=False,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="Timing is ambiguous, but tags, intervention, and DAG remain usable.",
        ),
        DegradationRegime(
            name="tag_loss_only",
            clock_uncertainty=0.05,
            tags_present=False,
            tags_authenticated=False,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=False,
            perturbation_back_action=False,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="Origin tags are missing, but timing, intervention, and DAG remain usable.",
        ),
        DegradationRegime(
            name="tag_spoofing_caught_by_dag_and_intervention",
            clock_uncertainty=0.05,
            tags_present=True,
            tags_authenticated=False,
            copied_tag_spoofed_independent=True,
            archive_latency_hidden=False,
            perturbation_back_action=False,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="Tags are forgeable, so only intervention and signed ancestry count.",
        ),
        DegradationRegime(
            name="perturbation_back_action_with_authenticated_records",
            clock_uncertainty=0.05,
            tags_present=True,
            tags_authenticated=True,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=False,
            perturbation_back_action=True,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="The active intervention is contaminated, but tags and DAG remain reliable.",
        ),
        DegradationRegime(
            name="archive_latency_hidden_but_signed_dag_remains",
            clock_uncertainty=1.25,
            tags_present=True,
            tags_authenticated=True,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=True,
            perturbation_back_action=False,
            dag_completeness=1.0,
            accepts_partial_dag_threshold=False,
            purpose="Timing and latency are not trustworthy, but provenance metadata remain signed.",
        ),
        DegradationRegime(
            name="dag_incomplete_tags_lost_back_action",
            clock_uncertainty=1.25,
            tags_present=False,
            tags_authenticated=False,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=True,
            perturbation_back_action=True,
            dag_completeness=0.25,
            accepts_partial_dag_threshold=False,
            purpose="All strong channels are missing or contaminated; the rule should abstain.",
        ),
        DegradationRegime(
            name="partial_dag_threshold_only",
            clock_uncertainty=1.25,
            tags_present=False,
            tags_authenticated=False,
            copied_tag_spoofed_independent=False,
            archive_latency_hidden=True,
            perturbation_back_action=True,
            dag_completeness=0.55,
            accepts_partial_dag_threshold=True,
            purpose="Only a partial ancestry score remains; any classification needs a threshold.",
        ),
        DegradationRegime(
            name="forged_tags_hidden_latency_incomplete_dag",
            clock_uncertainty=1.25,
            tags_present=True,
            tags_authenticated=False,
            copied_tag_spoofed_independent=True,
            archive_latency_hidden=True,
            perturbation_back_action=True,
            dag_completeness=0.25,
            accepts_partial_dag_threshold=False,
            purpose="Forgeable tags plus hidden latency and incomplete DAG remove trusted evidence.",
        ),
    )


def run_t70_analysis() -> T70Result:
    analyses = tuple(
        analyze_witness(witness, regime)
        for regime in canonical_regimes()
        for witness in canonical_witnesses()
    )
    table = tuple(summarize_regime(regime, analyses) for regime in canonical_regimes())
    return T70Result(
        witness_analyses=analyses,
        robustness_table=table,
        minimal_metadata_requirement=(
            "D1 detector finality is non-arbitrary only when the provenance "
            "partition is fixed by at least one authenticated dependence "
            "channel for copied records and at least one authenticated "
            "independence channel for independent records. In this witness "
            "family the usable channels are: clean perturbation response, "
            "authenticated origin tags, complete signed ancestry, or timing "
            "only when paired with ancestry and clock bounds. Passive "
            "similarity and partial-DAG thresholds are insufficient."
        ),
        strongest_claim=(
            "T68 survives moderate single-channel degradation when redundant "
            "authenticated provenance channels remain. The D1 partition can "
            "still be fixed before finality scoring without inspecting the "
            "desired D1 verdict."
        ),
        weakened_claim=(
            "The detector branch of Q1 depends on trusted provenance "
            "instrumentation. If clock, tag, intervention, and DAG evidence "
            "are jointly missing, forgeable, thresholded, or back-action "
            "contaminated, D1 must be withheld or else adds no detector-level "
            "content beyond externally supplied classes."
        ),
        q1_recommendation=(
            "Keep Q1 partially supported, but state the detector contribution "
            "as an intervention-sensitive provenance/accounting framework. "
            "Do not claim provenance recovery from detector outcomes alone."
        ),
        falsification_condition=(
            "T70 would fail if degraded copied and independent witnesses with "
            "identical passive statistics can be classified non-arbitrarily "
            "without authenticated provenance channels, or if a physical "
            "implementation shows the required provenance channels cannot be "
            "made independent of the D1 outcome."
        ),
        recommended_next=(
            "Replace the boolean degradation flags with a physical protocol "
            "model: clock distributions, signature failure probabilities, "
            "archive batching, and intervention back-action matrices."
        ),
    )


def analyze_witness(
    witness: T68Witness,
    regime: DegradationRegime,
) -> WitnessAnalysis:
    evidence = evidence_for(witness, regime)
    partition = infer_partition(evidence)
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


def evidence_for(witness: T68Witness, regime: DegradationRegime) -> EvidenceVector:
    ambiguous: list[str] = []

    if regime.archive_latency_hidden:
        ambiguous.append("archive_latency_hidden")
    timing_gap = witness.archive_time - witness.local_time
    timing_reliable = (
        not regime.archive_latency_hidden
        and timing_gap > 2.0 * regime.clock_uncertainty
    )
    if not timing_reliable and witness.actual_same_class:
        ambiguous.append("clock_or_latency_timing")
    timing_dependence = (
        witness.actual_same_class
        and timing_reliable
        and witness.baseline_shared_noncommon_ancestry
        and regime.dag_completeness >= 0.9
    )

    tags_usable = regime.tags_present and regime.tags_authenticated
    if not regime.tags_present:
        ambiguous.append("tag_loss")
    elif not regime.tags_authenticated:
        ambiguous.append("unauthenticated_or_forgeable_tags")
    visible_tags_equal = (
        False
        if regime.copied_tag_spoofed_independent and witness.actual_same_class
        else witness.baseline_tags_equal
    )
    duplicate_tag_dependence = tags_usable and visible_tags_equal
    distinct_tag_independence = tags_usable and not visible_tags_equal

    if regime.perturbation_back_action:
        ambiguous.append("perturbation_back_action")
    perturbation_dependence = (
        witness.baseline_perturbation_changes_other
        and not regime.perturbation_back_action
    )
    perturbation_independence = (
        not witness.baseline_perturbation_changes_other
        and not regime.perturbation_back_action
    )

    dag_complete = regime.dag_completeness >= 0.9
    if not dag_complete:
        ambiguous.append("incomplete_provenance_dag")
    dag_dependence = dag_complete and witness.baseline_shared_noncommon_ancestry
    dag_independence = dag_complete and not witness.baseline_shared_noncommon_ancestry
    threshold_or_label_dependent = regime.accepts_partial_dag_threshold

    return EvidenceVector(
        timing_dependence=timing_dependence,
        duplicate_tag_dependence=duplicate_tag_dependence,
        distinct_tag_independence=distinct_tag_independence,
        perturbation_dependence=perturbation_dependence,
        perturbation_independence=perturbation_independence,
        dag_dependence=dag_dependence,
        dag_independence=dag_independence,
        ambiguous_channels=tuple(sorted(set(ambiguous))),
        threshold_or_label_dependent=threshold_or_label_dependent,
    )


def infer_partition(evidence: EvidenceVector) -> PartitionDecision:
    if evidence.threshold_or_label_dependent:
        return PartitionDecision(
            status="undetermined_threshold_or_label_dependent",
            inferred_same_class=None,
            inferred_classes=(),
            reason=(
                "Only thresholded partial metadata or unaudited labels remain; "
                "D1 must not be evaluated."
            ),
            pre_registered=True,
            depends_on_d1_outcome=False,
            threshold_or_label_dependent=True,
        )
    if evidence.dependence_evidence():
        return PartitionDecision(
            status="determined",
            inferred_same_class=True,
            inferred_classes=(("local_log", "P0"), ("archive", "P0")),
            reason="At least one authenticated dependence channel remains.",
            pre_registered=True,
            depends_on_d1_outcome=False,
            threshold_or_label_dependent=False,
        )
    if evidence.independence_evidence():
        return PartitionDecision(
            status="determined",
            inferred_same_class=False,
            inferred_classes=(("local_log", "P0"), ("archive", "P1")),
            reason="At least one authenticated independence channel remains.",
            pre_registered=True,
            depends_on_d1_outcome=False,
            threshold_or_label_dependent=False,
        )
    return PartitionDecision(
        status="undetermined_clean_abstention",
        inferred_same_class=None,
        inferred_classes=(),
        reason=(
            "No authenticated provenance channel remains; the rule abstains "
            "instead of using passive statistics."
        ),
        pre_registered=True,
        depends_on_d1_outcome=False,
        threshold_or_label_dependent=False,
    )


def compute_d1_after_partition(
    witness: T68Witness,
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
    regime: DegradationRegime,
    analyses: tuple[WitnessAnalysis, ...],
) -> RegimeSummary:
    regime_analyses = tuple(
        analysis for analysis in analyses if analysis.regime.name == regime.name
    )
    copied = _analysis_by_witness(regime_analyses, "dependent_copied_archive")
    independent = _analysis_by_witness(
        regime_analyses,
        "independent_overlapping_readout",
    )
    preserves = copied.correctly_classified is True and independent.correctly_classified is True
    threshold_or_label = (
        copied.partition.threshold_or_label_dependent
        or independent.partition.threshold_or_label_dependent
    )
    clean_failure = (
        not preserves
        and not threshold_or_label
        and (
            copied.partition.inferred_same_class is None
            or independent.partition.inferred_same_class is None
        )
    )
    if preserves:
        verdict = "survives"
        interpretation = (
            "The degraded regime still fixes both provenance classes before D1."
        )
    elif threshold_or_label:
        verdict = "fails_threshold_or_label_dependent"
        interpretation = (
            "Classification would require a partial-DAG threshold or unaudited "
            "label; D1 is withheld."
        )
    else:
        verdict = "fails_clean_abstention"
        interpretation = (
            "Trusted provenance evidence is insufficient; the rule abstains "
            "rather than evaluating D1."
        )
    return RegimeSummary(
        name=regime.name,
        verdict=verdict,
        copied_status=copied.partition.status,
        independent_status=independent.partition.status,
        preserves_partition=preserves,
        clean_failure=clean_failure,
        threshold_or_label_dependent=threshold_or_label,
        minimal_metadata_used=_metadata_used(copied.evidence, independent.evidence),
        interpretation=interpretation,
    )


def t70_result_to_dict(result: T70Result) -> dict[str, object]:
    return {
        "passive_statistics": {
            "agreement_probability": PASSIVE_AGREEMENT,
            "phi_correlation": PASSIVE_PHI,
        },
        "robustness_table": [
            {
                "name": summary.name,
                "verdict": summary.verdict,
                "copied_status": summary.copied_status,
                "independent_status": summary.independent_status,
                "preserves_partition": summary.preserves_partition,
                "clean_failure": summary.clean_failure,
                "threshold_or_label_dependent": (
                    summary.threshold_or_label_dependent
                ),
                "minimal_metadata_used": list(summary.minimal_metadata_used),
                "interpretation": summary.interpretation,
            }
            for summary in result.robustness_table
        ],
        "witness_analyses": [
            _analysis_to_dict(analysis) for analysis in result.witness_analyses
        ],
        "minimal_metadata_requirement": result.minimal_metadata_requirement,
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "q1_recommendation": result.q1_recommendation,
        "falsification_condition": result.falsification_condition,
        "recommended_next": result.recommended_next,
    }


def _analysis_by_witness(
    analyses: tuple[WitnessAnalysis, ...],
    witness_name: str,
) -> WitnessAnalysis:
    for analysis in analyses:
        if analysis.witness.name == witness_name:
            return analysis
    raise ValueError(f"missing witness analysis: {witness_name}")


def _metadata_used(
    copied: EvidenceVector,
    independent: EvidenceVector,
) -> tuple[str, ...]:
    used: list[str] = []
    if copied.timing_dependence:
        used.append("timing_plus_ancestry")
    if copied.duplicate_tag_dependence or independent.distinct_tag_independence:
        used.append("authenticated_origin_tags")
    if copied.perturbation_dependence or independent.perturbation_independence:
        used.append("clean_perturbation_response")
    if copied.dag_dependence or independent.dag_independence:
        used.append("complete_signed_dag")
    return tuple(used)


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
        "regime_purpose": analysis.regime.purpose,
        "witness": analysis.witness.name,
        "actual_same_class": analysis.witness.actual_same_class,
        "evidence": {
            "timing_dependence": analysis.evidence.timing_dependence,
            "duplicate_tag_dependence": (
                analysis.evidence.duplicate_tag_dependence
            ),
            "distinct_tag_independence": (
                analysis.evidence.distinct_tag_independence
            ),
            "perturbation_dependence": (
                analysis.evidence.perturbation_dependence
            ),
            "perturbation_independence": (
                analysis.evidence.perturbation_independence
            ),
            "dag_dependence": analysis.evidence.dag_dependence,
            "dag_independence": analysis.evidence.dag_independence,
            "ambiguous_channels": list(analysis.evidence.ambiguous_channels),
            "threshold_or_label_dependent": (
                analysis.evidence.threshold_or_label_dependent
            ),
        },
        "partition": {
            "status": analysis.partition.status,
            "inferred_same_class": analysis.partition.inferred_same_class,
            "inferred_classes": list(analysis.partition.inferred_classes),
            "reason": analysis.partition.reason,
            "pre_registered": analysis.partition.pre_registered,
            "depends_on_d1_outcome": analysis.partition.depends_on_d1_outcome,
            "threshold_or_label_dependent": (
                analysis.partition.threshold_or_label_dependent
            ),
        },
        "d1_profile": d1_profile,
        "observer_finalized": analysis.observer_finalized,
        "correctly_classified": analysis.correctly_classified,
    }


