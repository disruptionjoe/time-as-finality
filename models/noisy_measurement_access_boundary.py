"""T62: noisy measurement access-boundary discriminator.

This module extends the T2/T22 quantum-record thread with a deliberately
limited channel-level audit. It separates three predicates that are easy to
conflate:

* pointer decoherence;
* Quantum-Darwinism-style redundant fragment records;
* observer-relative D1 finality under an access boundary.

The model is not a Hamiltonian simulation and does not claim new quantum
dynamics. It uses binary readout channels as a stress test for whether Q1 adds
anything beyond decoherence and environmental redundancy. The surviving claim
is narrower: TaF adds an explicit observer-access and independence filter over
already-declared record channels.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log2


INITIAL_POINTER_COHERENCE = 0.5
DEFAULT_INFORMATION_THRESHOLD_BITS = 0.75
DEFAULT_COHERENCE_THRESHOLD = 0.01


@dataclass(frozen=True)
class NoisyFragment:
    name: str
    holder: str
    readout_reliability: float
    decoherence_factor: float
    independence_class: str
    branch_id: str


@dataclass(frozen=True)
class NoisyMeasurementScenario:
    name: str
    fragments: tuple[NoisyFragment, ...]
    observer_access: frozenset[str]
    reconstruction_threshold: int
    information_threshold_bits: float = DEFAULT_INFORMATION_THRESHOLD_BITS
    coherence_threshold: float = DEFAULT_COHERENCE_THRESHOLD
    purpose: str = ""


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
class ScenarioPredicates:
    decohered_pointer: bool
    darwinism_redundant_total: bool
    observer_finalized: bool
    redundant_but_inaccessible: bool
    decohered_without_darwinism: bool
    raw_redundancy_overcounts_independence: bool


@dataclass(frozen=True)
class ScenarioAnalysis:
    scenario: NoisyMeasurementScenario
    pointer_coherence_abs: float
    fragment_information_bits: tuple[tuple[str, float], ...]
    total_r_delta_raw: int
    accessible_r_delta_raw: int
    accessible_r_delta_independent: int
    d1_profile: D1Profile
    predicates: ScenarioPredicates
    classification: str
    interpretation: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    claim: str
    evidence: str


@dataclass(frozen=True)
class T62Result:
    scenarios: tuple[ScenarioAnalysis, ...]
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    recommended_next: str


def canonical_noisy_scenarios() -> tuple[NoisyMeasurementScenario, ...]:
    """Return the finite discriminator matrix."""

    informative = (
        NoisyFragment("E1", "left_array", 0.99, 0.1, "left_channel", "z_pointer"),
        NoisyFragment("E2", "right_array", 0.99, 0.1, "right_channel", "z_pointer"),
        NoisyFragment("E3", "remote_array", 0.99, 0.1, "remote_channel", "z_pointer"),
    )
    weak_bath = tuple(
        NoisyFragment(
            name=f"W{index}",
            holder=f"weak_bath_{index}",
            readout_reliability=0.68,
            decoherence_factor=0.45,
            independence_class=f"weak_{index}",
            branch_id="weak_scattering",
        )
        for index in range(1, 9)
    )
    duplicate = (
        NoisyFragment("D1", "left_array_1", 0.99, 0.1, "left_channel", "z_pointer"),
        NoisyFragment("D2", "right_array", 0.99, 0.1, "right_channel", "z_pointer"),
        NoisyFragment("D3", "left_array_2", 0.99, 0.1, "left_channel", "z_pointer"),
    )

    return (
        NoisyMeasurementScenario(
            name="redundant_accessible_control",
            fragments=informative,
            observer_access=frozenset({"E1", "E2", "E3"}),
            reconstruction_threshold=2,
            purpose=(
                "Positive control where decoherence, total redundancy, and "
                "observer-relative finality agree."
            ),
        ),
        NoisyMeasurementScenario(
            name="decohered_not_darwinist",
            fragments=weak_bath,
            observer_access=frozenset(fragment.name for fragment in weak_bath),
            reconstruction_threshold=2,
            purpose=(
                "Pointer coherence is suppressed by many weak scatterers, but "
                "no single fragment crosses the information threshold."
            ),
        ),
        NoisyMeasurementScenario(
            name="redundant_but_inaccessible",
            fragments=informative,
            observer_access=frozenset(),
            reconstruction_threshold=2,
            purpose=(
                "Environmental records exist, but the observer has no access "
                "window onto them."
            ),
        ),
        NoisyMeasurementScenario(
            name="raw_duplicate_boundary",
            fragments=duplicate,
            observer_access=frozenset({"D1", "D2", "D3"}),
            reconstruction_threshold=3,
            purpose=(
                "Raw fragment count crosses threshold, but one record is a "
                "correlated duplicate rather than an independent holder."
            ),
        ),
    )


def analyze_scenario(scenario: NoisyMeasurementScenario) -> ScenarioAnalysis:
    _validate_scenario(scenario)

    information = tuple(
        (fragment.name, round(mutual_information_bits(fragment.readout_reliability), 12))
        for fragment in scenario.fragments
    )
    information_by_name = dict(information)
    informative_fragments = tuple(
        fragment
        for fragment in scenario.fragments
        if information_by_name[fragment.name] >= scenario.information_threshold_bits
    )
    accessible_informative = tuple(
        fragment
        for fragment in informative_fragments
        if fragment.name in scenario.observer_access
    )
    pointer_coherence = round(_pointer_coherence_abs(scenario), 12)
    profile = D1Profile(
        accessible_support=len(accessible_informative),
        holder_redundancy=len(
            {fragment.independence_class for fragment in accessible_informative}
        ),
        branch_support=len({fragment.branch_id for fragment in accessible_informative}),
        reversal_cost=_record_erasure_cost_below_threshold(
            len(accessible_informative),
            scenario.reconstruction_threshold,
        ),
    )
    predicates = _predicates(
        scenario=scenario,
        pointer_coherence_abs=pointer_coherence,
        total_r_delta_raw=len(informative_fragments),
        accessible_r_delta_raw=len(accessible_informative),
        accessible_r_delta_independent=profile.holder_redundancy,
    )
    classification, interpretation = _classify(predicates)
    return ScenarioAnalysis(
        scenario=scenario,
        pointer_coherence_abs=pointer_coherence,
        fragment_information_bits=information,
        total_r_delta_raw=len(informative_fragments),
        accessible_r_delta_raw=len(accessible_informative),
        accessible_r_delta_independent=profile.holder_redundancy,
        d1_profile=profile,
        predicates=predicates,
        classification=classification,
        interpretation=interpretation,
    )


def run_t62_analysis() -> T62Result:
    analyses = tuple(analyze_scenario(scenario) for scenario in canonical_noisy_scenarios())
    by_name = {analysis.scenario.name: analysis for analysis in analyses}

    return T62Result(
        scenarios=analyses,
        hypothesis_evaluations=(
            HypothesisEvaluation(
                hypothesis_id="H1",
                status="supported",
                claim=(
                    "Decoherence, total environmental redundancy, and "
                    "observer-relative finality are distinct predicates."
                ),
                evidence=(
                    "The matrix contains one alignment control plus separate "
                    "decohered-not-Darwinist, redundant-inaccessible, and "
                    "duplicate-overcount witnesses."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H2",
                status="supported",
                claim=(
                    "Q1's strongest surviving content is observer-access "
                    "indexing over classical record availability."
                ),
                evidence=(
                    f"{by_name['redundant_but_inaccessible'].scenario.name} has "
                    "decoherence and total R_delta but D1 profile (0, 0, 0, 0)."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H3",
                status="weakened",
                claim=(
                    "TaF does not earn an independent noisy measurement "
                    "dynamics claim from this audit."
                ),
                evidence=(
                    "The decohered-not-Darwinist case is already natural in "
                    "standard decoherence versus Quantum Darwinism language; "
                    "TaF adds only access-boundary and independence bookkeeping."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H4",
                status="open",
                claim=(
                    "The thresholds and independence classes need detector-level "
                    "or Hamiltonian justification before external physics claims."
                ),
                evidence=(
                    "Changing the information threshold or independence partition "
                    "can flip the D1 predicate without changing the abstract "
                    "channel family."
                ),
            ),
        ),
        strongest_claim=(
            "In the T62 channel-level model, TaF can distinguish 'decohered', "
            "'environmentally redundant', and 'final for this observer' without "
            "adding collapse or hidden variables."
        ),
        weakened_claim=(
            "T62 weakens Q1 away from any claim of new measurement dynamics. "
            "The earned claim is an access-boundary discriminator layered on "
            "top of decoherence and Quantum-Darwinism-style records."
        ),
        falsification_condition=(
            "If physically justified access boundaries and independence classes "
            "cannot be specified in a detector-level model, or if D1 predicates "
            "always reduce to standard R_delta under those specifications, Q1 "
            "adds no independent content for measurement."
        ),
        recommended_next=(
            "Build the detector-level version: a noisy Stern-Gerlach or photon "
            "scattering readout with explicit fragment partition, access window, "
            "threshold sensitivity, and no-signalling checks."
        ),
    )


def mutual_information_bits(readout_reliability: float) -> float:
    if not 0.5 <= readout_reliability <= 1.0:
        raise ValueError("readout_reliability must be in [0.5, 1.0]")
    error_probability = 1.0 - readout_reliability
    return 1.0 - _binary_entropy_bits(error_probability)


def t62_result_to_dict(result: T62Result) -> dict[str, object]:
    return {
        "scenarios": [_analysis_to_dict(analysis) for analysis in result.scenarios],
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


def _predicates(
    *,
    scenario: NoisyMeasurementScenario,
    pointer_coherence_abs: float,
    total_r_delta_raw: int,
    accessible_r_delta_raw: int,
    accessible_r_delta_independent: int,
) -> ScenarioPredicates:
    decohered = pointer_coherence_abs <= scenario.coherence_threshold
    darwinism_redundant = total_r_delta_raw >= scenario.reconstruction_threshold
    observer_finalized = accessible_r_delta_independent >= scenario.reconstruction_threshold
    return ScenarioPredicates(
        decohered_pointer=decohered,
        darwinism_redundant_total=darwinism_redundant,
        observer_finalized=observer_finalized,
        redundant_but_inaccessible=(
            decohered
            and darwinism_redundant
            and accessible_r_delta_raw == 0
            and not observer_finalized
        ),
        decohered_without_darwinism=(
            decohered and not darwinism_redundant and not observer_finalized
        ),
        raw_redundancy_overcounts_independence=(
            accessible_r_delta_raw >= scenario.reconstruction_threshold
            and accessible_r_delta_independent < scenario.reconstruction_threshold
        ),
    )


def _classify(predicates: ScenarioPredicates) -> tuple[str, str]:
    if predicates.raw_redundancy_overcounts_independence:
        return (
            "raw_redundancy_overcounts_independence",
            (
                "Raw fragment redundancy crosses the threshold, but D1 rejects "
                "finalization because the declared independence partition has "
                "too few independent holder classes."
            ),
        )
    if predicates.redundant_but_inaccessible:
        return (
            "redundant_but_inaccessible",
            (
                "The environment carries redundant records, but this observer "
                "has no accessible finalized record."
            ),
        )
    if predicates.decohered_without_darwinism:
        return (
            "decohered_without_redundant_records",
            (
                "The pointer is decohered by weak scattering, but no individual "
                "fragment is an above-threshold redundant record."
            ),
        )
    if (
        predicates.decohered_pointer
        and predicates.darwinism_redundant_total
        and predicates.observer_finalized
    ):
        return (
            "alignment_control",
            (
                "Decoherence, total environmental redundancy, and "
                "observer-relative D1 finality agree."
            ),
        )
    return (
        "unclassified_boundary",
        "The predicate combination falls outside the intended T62 witness matrix.",
    )


def _pointer_coherence_abs(scenario: NoisyMeasurementScenario) -> float:
    coherence = INITIAL_POINTER_COHERENCE
    for fragment in scenario.fragments:
        coherence *= fragment.decoherence_factor
    return coherence


def _record_erasure_cost_below_threshold(
    accessible_support_count: int,
    reconstruction_threshold: int,
) -> int:
    if accessible_support_count < reconstruction_threshold:
        return 0
    return accessible_support_count - reconstruction_threshold + 1


def _binary_entropy_bits(probability_one: float) -> float:
    if probability_one <= 0.0 or probability_one >= 1.0:
        return 0.0
    probability_zero = 1.0 - probability_one
    return -(
        probability_zero * log2(probability_zero)
        + probability_one * log2(probability_one)
    )


def _validate_scenario(scenario: NoisyMeasurementScenario) -> None:
    if scenario.reconstruction_threshold < 1:
        raise ValueError("reconstruction_threshold must be positive")
    names = {fragment.name for fragment in scenario.fragments}
    unknown_access = scenario.observer_access - names
    if unknown_access:
        raise ValueError(f"observer_access contains unknown fragments: {unknown_access}")
    for fragment in scenario.fragments:
        if not 0.0 <= fragment.decoherence_factor <= 1.0:
            raise ValueError("decoherence_factor must be in [0.0, 1.0]")
        mutual_information_bits(fragment.readout_reliability)


def _analysis_to_dict(analysis: ScenarioAnalysis) -> dict[str, object]:
    scenario = analysis.scenario
    return {
        "name": scenario.name,
        "purpose": scenario.purpose,
        "observer_access": sorted(scenario.observer_access),
        "reconstruction_threshold": scenario.reconstruction_threshold,
        "information_threshold_bits": scenario.information_threshold_bits,
        "coherence_threshold": scenario.coherence_threshold,
        "fragments": [
            {
                "name": fragment.name,
                "holder": fragment.holder,
                "readout_reliability": fragment.readout_reliability,
                "decoherence_factor": fragment.decoherence_factor,
                "independence_class": fragment.independence_class,
                "branch_id": fragment.branch_id,
            }
            for fragment in scenario.fragments
        ],
        "pointer_coherence_abs": analysis.pointer_coherence_abs,
        "fragment_information_bits": list(analysis.fragment_information_bits),
        "total_r_delta_raw": analysis.total_r_delta_raw,
        "accessible_r_delta_raw": analysis.accessible_r_delta_raw,
        "accessible_r_delta_independent": analysis.accessible_r_delta_independent,
        "d1_profile": {
            "accessible_support": analysis.d1_profile.accessible_support,
            "holder_redundancy": analysis.d1_profile.holder_redundancy,
            "branch_support": analysis.d1_profile.branch_support,
            "reversal_cost": analysis.d1_profile.reversal_cost,
            "profile_tuple": list(analysis.d1_profile.as_tuple()),
        },
        "predicates": {
            "decohered_pointer": analysis.predicates.decohered_pointer,
            "darwinism_redundant_total": analysis.predicates.darwinism_redundant_total,
            "observer_finalized": analysis.predicates.observer_finalized,
            "redundant_but_inaccessible": analysis.predicates.redundant_but_inaccessible,
            "decohered_without_darwinism": analysis.predicates.decohered_without_darwinism,
            "raw_redundancy_overcounts_independence": (
                analysis.predicates.raw_redundancy_overcounts_independence
            ),
        },
        "classification": analysis.classification,
        "interpretation": analysis.interpretation,
    }
