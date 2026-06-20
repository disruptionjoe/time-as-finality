"""T67: correlation-threshold provenance obstruction.

T66 proposed a natural repair: derive the detector independence partition from
measured channel-correlation data instead of declaring provenance classes by
hand.  T67 tests the weakest useful version of that repair.

The core obstruction is simple.  Two detector records can be strongly
correlated for opposite reasons:

1. dependent provenance: one record is a copied descendant of the other;
2. independent provenance: both records are separate readouts of the same
   latent spin variable.

If those two mechanisms can yield the same observed pairwise agreement or the
same binary phi correlation, then a correlation-threshold rule cannot recover
the D1 independence partition.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class ProvenanceScenario:
    name: str
    provenance_class: str
    local_error: float
    archive_parameter: float
    purpose: str


@dataclass(frozen=True)
class ScenarioAnalysis:
    scenario: ProvenanceScenario
    archive_error: float
    agreement_probability: float
    phi_correlation: float
    local_accuracy: float
    archive_accuracy: float
    interpretation: str


@dataclass(frozen=True)
class ThresholdAudit:
    score_name: str
    orientation: str
    threshold: float
    misclassified: tuple[str, ...]
    error_count: int
    interpretation: str


@dataclass(frozen=True)
class OverlapWitness:
    dependent_scenario: str
    independent_scenario: str
    agreement_gap: float
    phi_gap: float
    interpretation: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    claim: str
    evidence: str


@dataclass(frozen=True)
class T67Result:
    analyses: tuple[ScenarioAnalysis, ...]
    overlap_witness: OverlapWitness
    best_agreement_threshold_audit: ThresholdAudit
    best_phi_threshold_audit: ThresholdAudit
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    recommended_next: str


EXACT_OVERLAP_ERROR = (1.0 - sqrt(0.84)) / 2.0


def canonical_scenarios() -> tuple[ProvenanceScenario, ...]:
    return (
        ProvenanceScenario(
            name="dependent_clean_copy",
            provenance_class="dependent_copy",
            local_error=0.02,
            archive_parameter=0.0,
            purpose="Positive control: exact archive copy of the local log.",
        ),
        ProvenanceScenario(
            name="dependent_transport_noisy",
            provenance_class="dependent_copy",
            local_error=0.02,
            archive_parameter=0.08,
            purpose=(
                "Copy provenance with transport noise. The archive descends "
                "from the local log but is not perfectly correlated with it."
            ),
        ),
        ProvenanceScenario(
            name="dependent_transport_very_noisy",
            provenance_class="dependent_copy",
            local_error=0.02,
            archive_parameter=0.18,
            purpose=(
                "More degraded copied archive. Provenance remains dependent "
                "even though agreement drops substantially."
            ),
        ),
        ProvenanceScenario(
            name="independent_high_fidelity",
            provenance_class="independent_readout",
            local_error=0.02,
            archive_parameter=0.02,
            purpose=(
                "Independent detector chain with high agreement because both "
                "channels measure the same latent spin accurately."
            ),
        ),
        ProvenanceScenario(
            name="independent_exact_overlap",
            provenance_class="independent_readout",
            local_error=EXACT_OVERLAP_ERROR,
            archive_parameter=EXACT_OVERLAP_ERROR,
            purpose=(
                "Independent detector chain chosen so that its observed "
                "agreement exactly matches the noisy copied-archive case."
            ),
        ),
        ProvenanceScenario(
            name="independent_medium_fidelity",
            provenance_class="independent_readout",
            local_error=0.1,
            archive_parameter=0.1,
            purpose=(
                "Independent detector chain with lower accuracy and lower "
                "agreement. This overlaps the more degraded copy case."
            ),
        ),
    )


def analyze_scenario(scenario: ProvenanceScenario) -> ScenarioAnalysis:
    _validate_probability(scenario.local_error)
    _validate_probability(scenario.archive_parameter)

    if scenario.provenance_class == "dependent_copy":
        archive_error = _dependent_archive_error(
            local_error=scenario.local_error,
            transport_error=scenario.archive_parameter,
        )
        agreement_probability = 1.0 - scenario.archive_parameter
        interpretation = (
            "The archive is downstream of the local log. Agreement is set by "
            "copy transport fidelity, not by provenance independence."
        )
    elif scenario.provenance_class == "independent_readout":
        archive_error = scenario.archive_parameter
        agreement_probability = _independent_agreement_probability(
            local_error=scenario.local_error,
            archive_error=archive_error,
        )
        interpretation = (
            "The archive is an independent detector chain. Agreement comes "
            "from a shared latent spin, not from copying."
        )
    else:
        raise ValueError(f"unknown provenance_class: {scenario.provenance_class}")

    return ScenarioAnalysis(
        scenario=scenario,
        archive_error=round(archive_error, 12),
        agreement_probability=round(agreement_probability, 12),
        phi_correlation=round(2.0 * agreement_probability - 1.0, 12),
        local_accuracy=round(1.0 - scenario.local_error, 12),
        archive_accuracy=round(1.0 - archive_error, 12),
        interpretation=interpretation,
    )


def run_t67_analysis() -> T67Result:
    analyses = tuple(analyze_scenario(scenario) for scenario in canonical_scenarios())
    overlap_witness = _build_overlap_witness(analyses)
    best_agreement_threshold_audit = best_threshold_audit(
        analyses=analyses,
        score_name="agreement_probability",
    )
    best_phi_threshold_audit = best_threshold_audit(
        analyses=analyses,
        score_name="phi_correlation",
    )

    return T67Result(
        analyses=analyses,
        overlap_witness=overlap_witness,
        best_agreement_threshold_audit=best_agreement_threshold_audit,
        best_phi_threshold_audit=best_phi_threshold_audit,
        hypothesis_evaluations=(
            HypothesisEvaluation(
                hypothesis_id="H1",
                status="refuted",
                claim=(
                    "A pairwise agreement threshold can recover the detector "
                    "independence partition."
                ),
                evidence=(
                    "The dependent noisy-copy witness and the independent "
                    "exact-overlap witness both have agreement 0.92."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H2",
                status="refuted",
                claim=(
                    "Binary phi correlation fixes provenance class."
                ),
                evidence=(
                    "Phi is an affine transform of agreement for these "
                    "unbiased binary records, so the same exact-overlap "
                    "counterexample applies."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H3",
                status="supported",
                claim=(
                    "Measured correlation can rank record similarity, but not "
                    "infer provenance dependence on its own."
                ),
                evidence=(
                    "The best agreement-threshold rule still misclassifies at "
                    "least two of the six canonical witnesses."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H4",
                status="supported",
                claim=(
                    "Q1 needs intervention, timing, or signed-provenance data "
                    "in addition to detector correlations."
                ),
                evidence=(
                    "Correlation overlaps between copied and independent "
                    "channels persist even after explicit finite calibration."
                ),
            ),
        ),
        strongest_claim=(
            "Pairwise detector correlation can audit similarity of records, "
            "but it cannot by itself determine whether two records belong to "
            "the same D1 independence class."
        ),
        weakened_claim=(
            "The T66 repair path 'derive provenance from measured "
            "channel-correlation alone' is too weak. Copied archives and "
            "independent readout chains can be observationally correlation-"
            "equivalent."
        ),
        falsification_condition=(
            "If a pre-registered provenance-inference rule based only on "
            "passive detector correlation statistics classifies copied versus "
            "independent channels correctly across hostile witness families, "
            "T67 is false. Otherwise Q1 still lacks an operational rule for "
            "the independence partition."
        ),
        recommended_next=(
            "Add intervention metadata: delayed-copy tests, write-once tags, "
            "or signed detector provenance graphs. Then test whether those "
            "extra observables fix the independence partition before D1 is "
            "evaluated."
        ),
    )


def best_threshold_audit(
    *,
    analyses: tuple[ScenarioAnalysis, ...],
    score_name: str,
) -> ThresholdAudit:
    scores = [getattr(analysis, score_name) for analysis in analyses]
    candidates = sorted({0.0, 1.0, *scores})
    best: ThresholdAudit | None = None
    for orientation in ("dependent_if_score_ge_threshold", "dependent_if_score_le_threshold"):
        for threshold in candidates:
            misclassified: list[str] = []
            for analysis in analyses:
                predicted = _predict_dependent(
                    score=getattr(analysis, score_name),
                    threshold=threshold,
                    orientation=orientation,
                )
                actual = analysis.scenario.provenance_class == "dependent_copy"
                if predicted != actual:
                    misclassified.append(analysis.scenario.name)
            candidate = ThresholdAudit(
                score_name=score_name,
                orientation=orientation,
                threshold=round(threshold, 12),
                misclassified=tuple(misclassified),
                error_count=len(misclassified),
                interpretation=(
                    "Threshold search over the canonical witness family for a "
                    "single scalar correlation statistic."
                ),
            )
            if best is None or candidate.error_count < best.error_count:
                best = candidate
    assert best is not None
    return best


def t67_result_to_dict(result: T67Result) -> dict[str, object]:
    return {
        "scenarios": [
            {
                "name": analysis.scenario.name,
                "provenance_class": analysis.scenario.provenance_class,
                "purpose": analysis.scenario.purpose,
                "local_error": analysis.scenario.local_error,
                "archive_parameter": analysis.scenario.archive_parameter,
                "local_accuracy": analysis.local_accuracy,
                "archive_error": analysis.archive_error,
                "archive_accuracy": analysis.archive_accuracy,
                "agreement_probability": analysis.agreement_probability,
                "phi_correlation": analysis.phi_correlation,
                "interpretation": analysis.interpretation,
            }
            for analysis in result.analyses
        ],
        "overlap_witness": {
            "dependent_scenario": result.overlap_witness.dependent_scenario,
            "independent_scenario": result.overlap_witness.independent_scenario,
            "agreement_gap": result.overlap_witness.agreement_gap,
            "phi_gap": result.overlap_witness.phi_gap,
            "interpretation": result.overlap_witness.interpretation,
        },
        "best_agreement_threshold_audit": _audit_to_dict(
            result.best_agreement_threshold_audit
        ),
        "best_phi_threshold_audit": _audit_to_dict(
            result.best_phi_threshold_audit
        ),
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


def _audit_to_dict(audit: ThresholdAudit) -> dict[str, object]:
    return {
        "score_name": audit.score_name,
        "orientation": audit.orientation,
        "threshold": audit.threshold,
        "misclassified": list(audit.misclassified),
        "error_count": audit.error_count,
        "interpretation": audit.interpretation,
    }


def _build_overlap_witness(
    analyses: tuple[ScenarioAnalysis, ...]
) -> OverlapWitness:
    by_name = {analysis.scenario.name: analysis for analysis in analyses}
    dependent = by_name["dependent_transport_noisy"]
    independent = by_name["independent_exact_overlap"]
    return OverlapWitness(
        dependent_scenario=dependent.scenario.name,
        independent_scenario=independent.scenario.name,
        agreement_gap=round(
            abs(
                dependent.agreement_probability
                - independent.agreement_probability
            ),
            12,
        ),
        phi_gap=round(
            abs(dependent.phi_correlation - independent.phi_correlation),
            12,
        ),
        interpretation=(
            "A noisy copied archive and an independent readout pair have the "
            "same pairwise correlation statistics in the finite witness family."
        ),
    )


def _predict_dependent(*, score: float, threshold: float, orientation: str) -> bool:
    if orientation == "dependent_if_score_ge_threshold":
        return score >= threshold
    if orientation == "dependent_if_score_le_threshold":
        return score <= threshold
    raise ValueError(f"unknown orientation: {orientation}")


def _dependent_archive_error(*, local_error: float, transport_error: float) -> float:
    return local_error + transport_error - 2.0 * local_error * transport_error


def _independent_agreement_probability(
    *,
    local_error: float,
    archive_error: float,
) -> float:
    return (
        (1.0 - local_error) * (1.0 - archive_error)
        + local_error * archive_error
    )


def _validate_probability(value: float) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError("probability must be in [0.0, 1.0]")
