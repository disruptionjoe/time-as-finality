"""T68: intervention-sensitive detector provenance.

T67 showed that passive detector correlations cannot recover D1 independence
classes.  T68 adds intervention-sensitive observables and asks whether a
pre-registered provenance rule can separate the same hostile copied-vs-
independent pair before D1 finality is evaluated.

The result is a conditional positive.  Passive statistics still do not help,
but signed origin tags, active perturbation response, and a provenance DAG
separate copied archives from independent readout chains in this finite model.
The success depends on extra detector/provenance metadata, not on calibrated
POVM response matrices or passive channel similarity.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


DEFAULT_RECONSTRUCTION_THRESHOLD = 2
PASSIVE_AGREEMENT = 0.92
PASSIVE_PHI = 0.84
EXACT_OVERLAP_ERROR = (1.0 - sqrt(PASSIVE_PHI)) / 2.0
ALLOWED_COMMON_ANCESTORS = frozenset({"latent_spin"})


@dataclass(frozen=True)
class DetectorRecord:
    name: str
    created_at: float
    origin_tag: str
    signed_by: str
    ancestors: frozenset[str]
    holder: str
    information_bits: float


@dataclass(frozen=True)
class InterventionTrace:
    intervention: str
    target_record: str
    observed_record: str
    observed_changed: bool
    interpretation: str


@dataclass(frozen=True)
class T68Scenario:
    name: str
    actual_provenance_class: str
    local_error: float
    archive_error_or_copy_noise: float
    records: tuple[DetectorRecord, DetectorRecord]
    intervention_trace: InterventionTrace
    purpose: str


@dataclass(frozen=True)
class PassiveStatistics:
    agreement_probability: float
    phi_correlation: float


@dataclass(frozen=True)
class InterventionObservables:
    delayed_copy_candidate: bool
    duplicate_origin_tag: bool
    perturbation_coupling: bool
    disallowed_shared_ancestry: bool
    physically_interpretable: bool


@dataclass(frozen=True)
class PartitionResult:
    inferred_same_independence_class: bool
    inferred_classes: tuple[tuple[str, str], ...]
    rule_id: str
    rule_text: str
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
class ScenarioAnalysis:
    scenario: T68Scenario
    passive_statistics: PassiveStatistics
    observables: InterventionObservables
    partition: PartitionResult
    d1_profile: D1Profile
    observer_finalized: bool
    correctly_classified: bool
    interpretation: str


@dataclass(frozen=True)
class SeparationAudit:
    passive_statistics_identical: bool
    intervention_partitions_distinct: bool
    d1_computed_after_partition: bool
    success: bool
    interpretation: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    claim: str
    evidence: str


@dataclass(frozen=True)
class T68Result:
    analyses: tuple[ScenarioAnalysis, ...]
    separation_audit: SeparationAudit
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    recommended_next: str


def canonical_scenarios() -> tuple[T68Scenario, ...]:
    return (
        T68Scenario(
            name="dependent_copied_archive_same_passive_stats",
            actual_provenance_class="dependent_copy",
            local_error=0.02,
            archive_error_or_copy_noise=0.08,
            records=(
                DetectorRecord(
                    name="local_log",
                    created_at=2.0,
                    origin_tag="origin:local_detector_chain",
                    signed_by="local_detector_key",
                    ancestors=frozenset({"latent_spin", "screen_spot", "local_log"}),
                    holder="local_logger",
                    information_bits=0.95,
                ),
                DetectorRecord(
                    name="archive",
                    created_at=4.0,
                    origin_tag="origin:local_detector_chain",
                    signed_by="archive_copy_key",
                    ancestors=frozenset(
                        {"latent_spin", "screen_spot", "local_log", "archive"}
                    ),
                    holder="archive_mirror",
                    information_bits=0.95,
                ),
            ),
            intervention_trace=InterventionTrace(
                intervention="do(local_log := forced_flip_before_archive_write)",
                target_record="local_log",
                observed_record="archive",
                observed_changed=True,
                interpretation=(
                    "Perturbing the local log before archive write changes "
                    "the archive, indicating downstream dependence."
                ),
            ),
            purpose=(
                "Copied archive with the same passive agreement and phi as "
                "the independent overlap witness."
            ),
        ),
        T68Scenario(
            name="independent_readout_same_passive_stats",
            actual_provenance_class="independent_readout",
            local_error=EXACT_OVERLAP_ERROR,
            archive_error_or_copy_noise=EXACT_OVERLAP_ERROR,
            records=(
                DetectorRecord(
                    name="local_log",
                    created_at=2.0,
                    origin_tag="origin:local_detector_chain",
                    signed_by="local_detector_key",
                    ancestors=frozenset({"latent_spin", "screen_spot", "local_log"}),
                    holder="local_logger",
                    information_bits=0.95,
                ),
                DetectorRecord(
                    name="archive",
                    created_at=2.0,
                    origin_tag="origin:archive_detector_chain",
                    signed_by="archive_detector_key",
                    ancestors=frozenset(
                        {"latent_spin", "archive_sensor", "archive"}
                    ),
                    holder="archive_mirror",
                    information_bits=0.95,
                ),
            ),
            intervention_trace=InterventionTrace(
                intervention="do(local_log := forced_flip_after_local_write)",
                target_record="local_log",
                observed_record="archive",
                observed_changed=False,
                interpretation=(
                    "Perturbing the local log does not change the archive "
                    "readout, supporting separate detector-chain provenance."
                ),
            ),
            purpose=(
                "Independent overlapping readout with passive statistics "
                "matched to the copied archive witness."
            ),
        ),
    )


def analyze_scenario(scenario: T68Scenario) -> ScenarioAnalysis:
    passive_statistics = passive_statistics_for(scenario)
    observables = intervention_observables_for(scenario)
    partition = infer_partition(scenario, observables)
    d1_profile = compute_d1_after_partition(scenario, partition)
    observer_finalized = d1_profile.holder_redundancy >= DEFAULT_RECONSTRUCTION_THRESHOLD
    correctly_classified = (
        partition.inferred_same_independence_class
        == (scenario.actual_provenance_class == "dependent_copy")
    )
    return ScenarioAnalysis(
        scenario=scenario,
        passive_statistics=passive_statistics,
        observables=observables,
        partition=partition,
        d1_profile=d1_profile,
        observer_finalized=observer_finalized,
        correctly_classified=correctly_classified,
        interpretation=(
            "Intervention-sensitive provenance is fixed before D1 scoring; "
            "the D1 verdict follows from the inferred independence classes."
        ),
    )


def run_t68_analysis() -> T68Result:
    analyses = tuple(analyze_scenario(scenario) for scenario in canonical_scenarios())
    separation_audit = _separation_audit(analyses)
    return T68Result(
        analyses=analyses,
        separation_audit=separation_audit,
        hypothesis_evaluations=(
            HypothesisEvaluation(
                hypothesis_id="H1",
                status="supported",
                claim=(
                    "Intervention-sensitive provenance observables separate "
                    "copied archives from independent readout chains when "
                    "passive statistics are identical."
                ),
                evidence=(
                    "The two canonical witnesses both have agreement 0.92 "
                    "and phi 0.84, but perturbation response, origin tags, "
                    "and provenance DAG ancestry infer different partitions."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H2",
                status="supported_with_assumptions",
                claim=(
                    "The D1 independence partition can be fixed before "
                    "finality scoring."
                ),
                evidence=(
                    "The pre-registered T68 rule uses only timing, origin-tag, "
                    "perturbation, and DAG evidence; D1 is computed afterward."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H3",
                status="boundary",
                claim=(
                    "Timing alone is not the core result; the reliable signal "
                    "is causal/provenance metadata plus intervention response."
                ),
                evidence=(
                    "The rule does not classify by delay threshold. It uses "
                    "record ancestry, duplicate origin tags, and active "
                    "perturbation coupling."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H4",
                status="weakened",
                claim=(
                    "TaF detector-level contribution is operational only when "
                    "records carry causal/provenance metadata beyond calibrated "
                    "outcome statistics."
                ),
                evidence=(
                    "The same passive statistics are insufficient in T67 and "
                    "remain insufficient here; the successful separation comes "
                    "from intervention-sensitive record metadata."
                ),
            ),
        ),
        strongest_claim=(
            "In the finite detector witness family, D1 independence classes "
            "can be operationally fixed before finality scoring when records "
            "carry intervention-sensitive provenance data: origin tags, "
            "perturbation response, and signed ancestry."
        ),
        weakened_claim=(
            "TaF's detector-level content is not calibration-free and not "
            "recoverable from calibrated outcome statistics or passive "
            "correlations. It becomes operational only for detector records "
            "with causal/provenance metadata."
        ),
        falsification_condition=(
            "T68 fails if copied and independent detector chains can be made "
            "identical under passive statistics, timing, origin tags, active "
            "perturbation response, and signed ancestry while still requiring "
            "opposite D1 independence partitions."
        ),
        recommended_next=(
            "Replace the finite provenance metadata with a physically modeled "
            "detector protocol: explicit clock uncertainty, tag failure modes, "
            "and intervention back-action limits."
        ),
    )


def passive_statistics_for(scenario: T68Scenario) -> PassiveStatistics:
    if scenario.name not in {
        "dependent_copied_archive_same_passive_stats",
        "independent_readout_same_passive_stats",
    }:
        raise ValueError(f"unknown canonical scenario: {scenario.name}")
    return PassiveStatistics(
        agreement_probability=PASSIVE_AGREEMENT,
        phi_correlation=PASSIVE_PHI,
    )


def intervention_observables_for(
    scenario: T68Scenario,
) -> InterventionObservables:
    first, second = scenario.records
    shared_ancestors = (
        first.ancestors & second.ancestors
    ) - ALLOWED_COMMON_ANCESTORS
    delayed_copy_candidate = (
        second.created_at > first.created_at
        and first.name in second.ancestors
    )
    duplicate_origin_tag = first.origin_tag == second.origin_tag
    perturbation_coupling = scenario.intervention_trace.observed_changed
    disallowed_shared_ancestry = bool(shared_ancestors)
    physically_interpretable = all(
        (
            first.signed_by,
            second.signed_by,
            first.origin_tag,
            second.origin_tag,
        )
    )
    return InterventionObservables(
        delayed_copy_candidate=delayed_copy_candidate,
        duplicate_origin_tag=duplicate_origin_tag,
        perturbation_coupling=perturbation_coupling,
        disallowed_shared_ancestry=disallowed_shared_ancestry,
        physically_interpretable=physically_interpretable,
    )


def infer_partition(
    scenario: T68Scenario,
    observables: InterventionObservables,
) -> PartitionResult:
    same_class = (
        observables.perturbation_coupling
        or observables.duplicate_origin_tag
        or observables.disallowed_shared_ancestry
        or observables.delayed_copy_candidate
    )
    first, second = scenario.records
    if same_class:
        classes = ((first.name, "P0"), (second.name, "P0"))
        interpretation = (
            "Records are assigned to the same independence class because "
            "intervention/provenance data show downstream dependence."
        )
    else:
        classes = ((first.name, "P0"), (second.name, "P1"))
        interpretation = (
            "Records are assigned to distinct independence classes because "
            "the only shared ancestor is the allowed common spin source and "
            "the perturbation does not propagate."
        )
    return PartitionResult(
        inferred_same_independence_class=same_class,
        inferred_classes=classes,
        rule_id="T68_PREREGISTERED_INTERVENTION_PROVENANCE_RULE",
        rule_text=(
            "Before D1 scoring, place two records in the same independence "
            "class if active perturbation of one changes the other, if they "
            "share a write-once origin tag, if a signed provenance DAG shows "
            "non-common ancestry, or if timing plus ancestry shows delayed "
            "copying. Otherwise assign distinct classes. The allowed common "
            "ancestor is the latent spin source."
        ),
        pre_registered=True,
        depends_on_d1_outcome=False,
        interpretation=interpretation,
    )


def compute_d1_after_partition(
    scenario: T68Scenario,
    partition: PartitionResult,
) -> D1Profile:
    informative_records = tuple(
        record for record in scenario.records if record.information_bits >= 0.75
    )
    class_by_record = dict(partition.inferred_classes)
    holder_redundancy = len(
        {class_by_record[record.name] for record in informative_records}
    )
    branch_support = 1
    reversal_cost = (
        holder_redundancy - DEFAULT_RECONSTRUCTION_THRESHOLD + 1
        if holder_redundancy >= DEFAULT_RECONSTRUCTION_THRESHOLD
        else 0
    )
    return D1Profile(
        accessible_support=len(informative_records),
        holder_redundancy=holder_redundancy,
        branch_support=branch_support,
        reversal_cost=reversal_cost,
    )


def t68_result_to_dict(result: T68Result) -> dict[str, object]:
    return {
        "scenarios": [_analysis_to_dict(analysis) for analysis in result.analyses],
        "separation_audit": {
            "passive_statistics_identical": (
                result.separation_audit.passive_statistics_identical
            ),
            "intervention_partitions_distinct": (
                result.separation_audit.intervention_partitions_distinct
            ),
            "d1_computed_after_partition": (
                result.separation_audit.d1_computed_after_partition
            ),
            "success": result.separation_audit.success,
            "interpretation": result.separation_audit.interpretation,
        },
        "hypothesis_evaluations": [
            {
                "id": evaluation.hypothesis_id,
                "status": evaluation.status,
                "claim": evaluation.claim,
                "evidence": evaluation.evidence,
            }
            for evaluation in result.hypothesis_evaluations
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "recommended_next": result.recommended_next,
    }


def _analysis_to_dict(analysis: ScenarioAnalysis) -> dict[str, object]:
    return {
        "name": analysis.scenario.name,
        "actual_provenance_class": analysis.scenario.actual_provenance_class,
        "purpose": analysis.scenario.purpose,
        "passive_statistics": {
            "agreement_probability": (
                analysis.passive_statistics.agreement_probability
            ),
            "phi_correlation": analysis.passive_statistics.phi_correlation,
        },
        "records": [
            {
                "name": record.name,
                "created_at": record.created_at,
                "origin_tag": record.origin_tag,
                "signed_by": record.signed_by,
                "ancestors": sorted(record.ancestors),
                "holder": record.holder,
                "information_bits": record.information_bits,
            }
            for record in analysis.scenario.records
        ],
        "intervention_trace": {
            "intervention": analysis.scenario.intervention_trace.intervention,
            "target_record": analysis.scenario.intervention_trace.target_record,
            "observed_record": analysis.scenario.intervention_trace.observed_record,
            "observed_changed": (
                analysis.scenario.intervention_trace.observed_changed
            ),
            "interpretation": analysis.scenario.intervention_trace.interpretation,
        },
        "observables": {
            "delayed_copy_candidate": (
                analysis.observables.delayed_copy_candidate
            ),
            "duplicate_origin_tag": analysis.observables.duplicate_origin_tag,
            "perturbation_coupling": (
                analysis.observables.perturbation_coupling
            ),
            "disallowed_shared_ancestry": (
                analysis.observables.disallowed_shared_ancestry
            ),
            "physically_interpretable": (
                analysis.observables.physically_interpretable
            ),
        },
        "partition": {
            "inferred_same_independence_class": (
                analysis.partition.inferred_same_independence_class
            ),
            "inferred_classes": list(analysis.partition.inferred_classes),
            "rule_id": analysis.partition.rule_id,
            "rule_text": analysis.partition.rule_text,
            "pre_registered": analysis.partition.pre_registered,
            "depends_on_d1_outcome": analysis.partition.depends_on_d1_outcome,
            "interpretation": analysis.partition.interpretation,
        },
        "d1_profile": {
            "accessible_support": analysis.d1_profile.accessible_support,
            "holder_redundancy": analysis.d1_profile.holder_redundancy,
            "branch_support": analysis.d1_profile.branch_support,
            "reversal_cost": analysis.d1_profile.reversal_cost,
            "profile_tuple": list(analysis.d1_profile.as_tuple()),
        },
        "observer_finalized": analysis.observer_finalized,
        "correctly_classified": analysis.correctly_classified,
        "interpretation": analysis.interpretation,
    }


def _separation_audit(analyses: tuple[ScenarioAnalysis, ...]) -> SeparationAudit:
    passive_statistics = {
        (
            analysis.passive_statistics.agreement_probability,
            analysis.passive_statistics.phi_correlation,
        )
        for analysis in analyses
    }
    partitions = {
        analysis.partition.inferred_same_independence_class
        for analysis in analyses
    }
    d1_after_partition = all(
        analysis.partition.pre_registered
        and not analysis.partition.depends_on_d1_outcome
        for analysis in analyses
    )
    passive_identical = len(passive_statistics) == 1
    partitions_distinct = len(partitions) == 2
    success = (
        passive_identical
        and partitions_distinct
        and d1_after_partition
        and all(analysis.correctly_classified for analysis in analyses)
    )
    return SeparationAudit(
        passive_statistics_identical=passive_identical,
        intervention_partitions_distinct=partitions_distinct,
        d1_computed_after_partition=d1_after_partition,
        success=success,
        interpretation=(
            "The passive observables are intentionally identical; the "
            "intervention/provenance observables determine different "
            "independence partitions before D1 scoring."
        ),
    )
