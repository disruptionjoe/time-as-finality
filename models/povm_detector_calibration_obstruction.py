"""T66: POVM detector calibration obstruction.

T64 left a specific open problem: replace declared detector reliabilities with
calibrated detector physics before evaluating observer-relative D1 finality.
This module makes the smallest next move.  It replaces scalar reliability
inputs with explicit two-outcome POVM response matrices for a binary
Stern-Gerlach readout, then asks whether that calibration is sufficient to fix
the D1 verdict.

The result is deliberately mostly negative.  A calibrated POVM response is
enough to compute fragment mutual information and redundancy.  It is not
enough to choose the information threshold or the independence/provenance
partition.  The same calibrated response data can produce different D1
finality verdicts when the archive channel is treated as an independent
detector record versus a copied local log.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, log2, pi


DEFAULT_INFORMATION_THRESHOLD_BITS = 0.75
HIGH_INFORMATION_THRESHOLD_BITS = 0.9
DEFAULT_RECONSTRUCTION_THRESHOLD = 3
DEFAULT_COHERENCE_THRESHOLD = 0.01
INITIAL_POINTER_COHERENCE = 0.5

LOCAL_SETTINGS = {"local_z": 0.0, "local_x": pi / 2.0}
REMOTE_SETTINGS = {"remote_z": 0.0, "remote_x": pi / 2.0, "remote_diag": pi / 4.0}


@dataclass(frozen=True)
class POVMFragment:
    name: str
    holder: str
    p_readout_up_given_spin_up: float
    p_readout_up_given_spin_down: float
    decoherence_factor: float
    independence_class: str
    branch_id: str
    available_from: float
    available_until: float
    physical_role: str
    provenance: str


@dataclass(frozen=True)
class POVMScenario:
    name: str
    fragments: tuple[POVMFragment, ...]
    observer_holders: frozenset[str]
    observer_time: float
    reconstruction_threshold: int = DEFAULT_RECONSTRUCTION_THRESHOLD
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
    povm_redundant_total: bool
    observer_finalized: bool
    redundant_but_inaccessible: bool
    raw_redundancy_overcounts_independence: bool


@dataclass(frozen=True)
class ScenarioAnalysis:
    scenario: POVMScenario
    pointer_coherence_abs: float
    started_fragments: tuple[str, ...]
    available_fragments: tuple[str, ...]
    fragment_information_bits: tuple[tuple[str, float], ...]
    total_r_delta_raw: int
    accessible_r_delta_raw: int
    accessible_r_delta_independent: int
    d1_profile: D1Profile
    predicates: ScenarioPredicates
    classification: str
    interpretation: str


@dataclass(frozen=True)
class ThresholdObstruction:
    low_threshold_bits: float
    high_threshold_bits: float
    same_povm_response: bool
    low_threshold_finalized: bool
    high_threshold_finalized: bool
    verdict_flips: bool
    interpretation: str


@dataclass(frozen=True)
class IndependenceObstruction:
    same_povm_response: bool
    same_access_window: bool
    copy_partition_finalized: bool
    independent_partition_finalized: bool
    verdict_flips: bool
    interpretation: str


@dataclass(frozen=True)
class NoSignallingAudit:
    local_setting: str
    fragment_name: str
    readout_up_probability_by_remote_setting: tuple[tuple[str, float], ...]
    max_delta: float
    passed: bool
    interpretation: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    status: str
    claim: str
    evidence: str


@dataclass(frozen=True)
class T66Result:
    scenarios: tuple[ScenarioAnalysis, ...]
    threshold_obstruction: ThresholdObstruction
    independence_obstruction: IndependenceObstruction
    no_signalling_audits: tuple[NoSignallingAudit, ...]
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    recommended_next: str


def canonical_povm_fragments(
    *, archive_independence_class: str = "local_log"
) -> tuple[POVMFragment, ...]:
    """Return a finite calibrated-response Stern-Gerlach detector proxy."""

    return (
        POVMFragment(
            name="screen_spot",
            holder="local_screen",
            p_readout_up_given_spin_up=0.995,
            p_readout_up_given_spin_down=0.015,
            decoherence_factor=0.08,
            independence_class="screen_grain",
            branch_id="sg_z_pointer",
            available_from=1.0,
            available_until=3.0,
            physical_role="transient detector spot",
            provenance="direct_detector_response",
        ),
        POVMFragment(
            name="photodiode_pulse",
            holder="photodiode",
            p_readout_up_given_spin_up=0.985,
            p_readout_up_given_spin_down=0.035,
            decoherence_factor=0.12,
            independence_class="electronics",
            branch_id="sg_z_pointer",
            available_from=1.5,
            available_until=5.0,
            physical_role="amplified electronics pulse",
            provenance="direct_detector_response",
        ),
        POVMFragment(
            name="local_log",
            holder="local_logger",
            p_readout_up_given_spin_up=0.995,
            p_readout_up_given_spin_down=0.005,
            decoherence_factor=0.2,
            independence_class="local_log",
            branch_id="sg_z_pointer",
            available_from=2.0,
            available_until=10.0,
            physical_role="timestamped local detector log",
            provenance="logged_detector_response",
        ),
        POVMFragment(
            name="network_archive",
            holder="archive_mirror",
            p_readout_up_given_spin_up=0.995,
            p_readout_up_given_spin_down=0.005,
            decoherence_factor=0.5,
            independence_class=archive_independence_class,
            branch_id="sg_z_pointer",
            available_from=4.0,
            available_until=20.0,
            physical_role="network mirror of the local detector log",
            provenance="copied_or_independent_archive",
        ),
        POVMFragment(
            name="thermal_bath_trace",
            holder="cryostat_bath",
            p_readout_up_given_spin_up=0.62,
            p_readout_up_given_spin_down=0.50,
            decoherence_factor=0.3,
            independence_class="thermal_bath",
            branch_id="bath_scattering",
            available_from=0.5,
            available_until=20.0,
            physical_role="weak bath response below record threshold",
            provenance="uncontrolled_environmental_trace",
        ),
    )


def canonical_scenarios() -> tuple[POVMScenario, ...]:
    copy_fragments = canonical_povm_fragments(
        archive_independence_class="local_log"
    )
    independent_archive_fragments = canonical_povm_fragments(
        archive_independence_class="archive_storage"
    )
    local_holders = frozenset({"local_screen", "photodiode", "local_logger"})
    all_holders = frozenset(
        {"local_screen", "photodiode", "local_logger", "archive_mirror"}
    )

    return (
        POVMScenario(
            name="povm_local_lab_after_readout",
            fragments=copy_fragments,
            observer_holders=local_holders,
            observer_time=2.5,
            purpose=(
                "Positive control: calibrated POVM responses make three "
                "independent local detector records available above threshold."
            ),
        ),
        POVMScenario(
            name="same_povm_high_threshold",
            fragments=copy_fragments,
            observer_holders=local_holders,
            observer_time=2.5,
            information_threshold_bits=HIGH_INFORMATION_THRESHOLD_BITS,
            purpose=(
                "Same calibrated detector responses as the positive control, "
                "but with a higher information threshold."
            ),
        ),
        POVMScenario(
            name="povm_redundant_but_inaccessible",
            fragments=copy_fragments,
            observer_holders=frozenset(),
            observer_time=2.5,
            purpose=(
                "The calibrated detector carries redundant above-threshold "
                "records, but this observer has no access window."
            ),
        ),
        POVMScenario(
            name="archive_copy_partition",
            fragments=copy_fragments,
            observer_holders=all_holders,
            observer_time=4.5,
            purpose=(
                "The archive has the same calibrated response as the local log "
                "and is treated as the same provenance class."
            ),
        ),
        POVMScenario(
            name="archive_independent_partition",
            fragments=independent_archive_fragments,
            observer_holders=all_holders,
            observer_time=4.5,
            purpose=(
                "The archive has the same calibrated response data and access "
                "window but is treated as an independent provenance class."
            ),
        ),
    )


def analyze_scenario(scenario: POVMScenario) -> ScenarioAnalysis:
    _validate_scenario(scenario)

    information = tuple(
        (
            fragment.name,
            round(
                povm_mutual_information_bits(
                    fragment.p_readout_up_given_spin_up,
                    fragment.p_readout_up_given_spin_down,
                ),
                12,
            ),
        )
        for fragment in scenario.fragments
    )
    information_by_name = dict(information)
    started_fragments = tuple(
        fragment for fragment in scenario.fragments if _has_started(fragment, scenario)
    )
    available_fragments = tuple(
        fragment for fragment in scenario.fragments if _is_available(fragment, scenario)
    )
    informative_available = tuple(
        fragment
        for fragment in available_fragments
        if information_by_name[fragment.name] >= scenario.information_threshold_bits
    )
    accessible_informative = tuple(
        fragment
        for fragment in informative_available
        if fragment.holder in scenario.observer_holders
    )
    independent_classes = {
        fragment.independence_class for fragment in accessible_informative
    }
    branch_ids = {fragment.branch_id for fragment in accessible_informative}
    pointer_coherence = round(_pointer_coherence_abs(started_fragments), 12)
    profile = D1Profile(
        accessible_support=len(accessible_informative),
        holder_redundancy=len(independent_classes),
        branch_support=len(branch_ids),
        reversal_cost=_independent_erasure_cost_below_threshold(
            len(independent_classes), scenario.reconstruction_threshold
        ),
    )
    predicates = _predicates(
        scenario=scenario,
        pointer_coherence_abs=pointer_coherence,
        total_r_delta_raw=len(informative_available),
        accessible_r_delta_raw=len(accessible_informative),
        accessible_r_delta_independent=profile.holder_redundancy,
    )
    classification, interpretation = _classify(predicates)
    return ScenarioAnalysis(
        scenario=scenario,
        pointer_coherence_abs=pointer_coherence,
        started_fragments=tuple(fragment.name for fragment in started_fragments),
        available_fragments=tuple(fragment.name for fragment in available_fragments),
        fragment_information_bits=information,
        total_r_delta_raw=len(informative_available),
        accessible_r_delta_raw=len(accessible_informative),
        accessible_r_delta_independent=profile.holder_redundancy,
        d1_profile=profile,
        predicates=predicates,
        classification=classification,
        interpretation=interpretation,
    )


def run_t66_analysis() -> T66Result:
    analyses = tuple(analyze_scenario(scenario) for scenario in canonical_scenarios())
    by_name = {analysis.scenario.name: analysis for analysis in analyses}
    threshold_obstruction = _threshold_obstruction(
        by_name["povm_local_lab_after_readout"],
        by_name["same_povm_high_threshold"],
    )
    independence_obstruction = _independence_obstruction(
        by_name["archive_copy_partition"],
        by_name["archive_independent_partition"],
    )
    no_signalling_audits = run_no_signalling_audits()

    return T66Result(
        scenarios=analyses,
        threshold_obstruction=threshold_obstruction,
        independence_obstruction=independence_obstruction,
        no_signalling_audits=no_signalling_audits,
        hypothesis_evaluations=(
            HypothesisEvaluation(
                hypothesis_id="H1",
                status="supported",
                claim=(
                    "Declared scalar reliabilities can be replaced by explicit "
                    "binary POVM response matrices for this detector proxy."
                ),
                evidence=(
                    "Fragment information is computed from P(readout=+|spin=+) "
                    "and P(readout=+|spin=-), not assigned as a reliability."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H2",
                status="weakened",
                claim=(
                    "A calibrated POVM response does not by itself determine "
                    "observer-relative D1 finality."
                ),
                evidence=(
                    "The archive-copy and archive-independent scenarios have "
                    "the same response data and access window but opposite D1 "
                    "finalization verdicts."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H3",
                status="weakened",
                claim=(
                    "The information threshold remains an external input unless "
                    "a physical calibration rule fixes it before evaluation."
                ),
                evidence=(
                    "The same local detector response finalizes at threshold "
                    "0.75 and does not finalize at threshold 0.9."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H4",
                status="supported_guardrail",
                claim=(
                    "The calibrated-response predicate preserves no-signalling "
                    "in the finite singlet audit."
                ),
                evidence=(
                    "All local POVM readout marginals are invariant under the "
                    "tested remote settings."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H5",
                status="open",
                claim=(
                    "Q1 needs a detector provenance rule and threshold rule "
                    "that are specified before the D1 predicate is evaluated."
                ),
                evidence=(
                    "Without those rules, D1 can be changed while leaving the "
                    "calibrated POVM response matrices unchanged."
                ),
            ),
        ),
        strongest_claim=(
            "A calibrated binary POVM response lets TaF compute detector "
            "fragment information and re-run the access-window discriminator, "
            "but it does not determine finality without independent threshold "
            "and provenance assumptions."
        ),
        weakened_claim=(
            "Q1 cannot claim a calibration-free Stern-Gerlach prediction from "
            "POVM data alone.  The same calibrated response can support "
            "different D1 verdicts under different threshold or independence "
            "rules."
        ),
        falsification_condition=(
            "If detector physics cannot non-arbitrarily fix the information "
            "threshold and provenance/independence partition before D1 is "
            "evaluated, Q1 reduces to post hoc bookkeeping.  If those rules "
            "are fixed and D1 always equals standard R_delta, Q1 adds no "
            "independent measurement content."
        ),
        recommended_next=(
            "Derive the independence partition from a detector provenance graph "
            "or measured channel-correlation matrix, then pre-register the "
            "information threshold before comparing D1 with standard R_delta."
        ),
    )


def povm_mutual_information_bits(
    p_readout_up_given_spin_up: float,
    p_readout_up_given_spin_down: float,
) -> float:
    """Mutual information I(S;R) for a uniform binary spin source."""

    _validate_probability(p_readout_up_given_spin_up)
    _validate_probability(p_readout_up_given_spin_down)
    p_readout_up = 0.5 * (
        p_readout_up_given_spin_up + p_readout_up_given_spin_down
    )
    return _binary_entropy_bits(p_readout_up) - 0.5 * (
        _binary_entropy_bits(p_readout_up_given_spin_up)
        + _binary_entropy_bits(p_readout_up_given_spin_down)
    )


def local_povm_readout_up_probability(
    *,
    local_angle: float,
    remote_angle: float,
    fragment: POVMFragment,
) -> float:
    """Return the local readout-up marginal for a singlet pair."""

    probability = 0.0
    for local_outcome in (-1, 1):
        for remote_outcome in (-1, 1):
            joint_probability = singlet_joint_probability(
                local_outcome=local_outcome,
                remote_outcome=remote_outcome,
                local_angle=local_angle,
                remote_angle=remote_angle,
            )
            readout_up_given_outcome = (
                fragment.p_readout_up_given_spin_up
                if local_outcome == 1
                else fragment.p_readout_up_given_spin_down
            )
            probability += joint_probability * readout_up_given_outcome
    return probability


def singlet_joint_probability(
    *,
    local_outcome: int,
    remote_outcome: int,
    local_angle: float,
    remote_angle: float,
) -> float:
    if local_outcome not in {-1, 1} or remote_outcome not in {-1, 1}:
        raise ValueError("outcomes must be -1 or 1")
    return 0.25 * (
        1.0 - local_outcome * remote_outcome * cos(local_angle - remote_angle)
    )


def run_no_signalling_audits() -> tuple[NoSignallingAudit, ...]:
    screen_fragment = canonical_povm_fragments()[0]
    audits: list[NoSignallingAudit] = []
    for local_setting, local_angle in LOCAL_SETTINGS.items():
        marginals = tuple(
            (
                remote_setting,
                round(
                    local_povm_readout_up_probability(
                        local_angle=local_angle,
                        remote_angle=remote_angle,
                        fragment=screen_fragment,
                    ),
                    12,
                ),
            )
            for remote_setting, remote_angle in REMOTE_SETTINGS.items()
        )
        values = tuple(value for _, value in marginals)
        max_delta = round(max(values) - min(values), 12)
        audits.append(
            NoSignallingAudit(
                local_setting=local_setting,
                fragment_name=screen_fragment.name,
                readout_up_probability_by_remote_setting=marginals,
                max_delta=max_delta,
                passed=max_delta <= 1e-12,
                interpretation=(
                    "Remote settings alter joint correlations but not the "
                    "local POVM readout marginal."
                ),
            )
        )
    return tuple(audits)


def t66_result_to_dict(result: T66Result) -> dict[str, object]:
    return {
        "scenarios": [_analysis_to_dict(analysis) for analysis in result.scenarios],
        "threshold_obstruction": {
            "low_threshold_bits": result.threshold_obstruction.low_threshold_bits,
            "high_threshold_bits": result.threshold_obstruction.high_threshold_bits,
            "same_povm_response": result.threshold_obstruction.same_povm_response,
            "low_threshold_finalized": (
                result.threshold_obstruction.low_threshold_finalized
            ),
            "high_threshold_finalized": (
                result.threshold_obstruction.high_threshold_finalized
            ),
            "verdict_flips": result.threshold_obstruction.verdict_flips,
            "interpretation": result.threshold_obstruction.interpretation,
        },
        "independence_obstruction": {
            "same_povm_response": result.independence_obstruction.same_povm_response,
            "same_access_window": result.independence_obstruction.same_access_window,
            "copy_partition_finalized": (
                result.independence_obstruction.copy_partition_finalized
            ),
            "independent_partition_finalized": (
                result.independence_obstruction.independent_partition_finalized
            ),
            "verdict_flips": result.independence_obstruction.verdict_flips,
            "interpretation": result.independence_obstruction.interpretation,
        },
        "no_signalling_audits": [
            {
                "local_setting": audit.local_setting,
                "fragment_name": audit.fragment_name,
                "readout_up_probability_by_remote_setting": list(
                    audit.readout_up_probability_by_remote_setting
                ),
                "max_delta": audit.max_delta,
                "passed": audit.passed,
                "interpretation": audit.interpretation,
            }
            for audit in result.no_signalling_audits
        ],
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


def _threshold_obstruction(
    low_threshold: ScenarioAnalysis, high_threshold: ScenarioAnalysis
) -> ThresholdObstruction:
    return ThresholdObstruction(
        low_threshold_bits=low_threshold.scenario.information_threshold_bits,
        high_threshold_bits=high_threshold.scenario.information_threshold_bits,
        same_povm_response=(
            _povm_response_signature(low_threshold.scenario)
            == _povm_response_signature(high_threshold.scenario)
        ),
        low_threshold_finalized=low_threshold.predicates.observer_finalized,
        high_threshold_finalized=high_threshold.predicates.observer_finalized,
        verdict_flips=(
            low_threshold.predicates.observer_finalized
            != high_threshold.predicates.observer_finalized
        ),
        interpretation=(
            "POVM calibration supplies response probabilities, but does not "
            "select the information threshold that turns response into finality."
        ),
    )


def _independence_obstruction(
    copy_partition: ScenarioAnalysis, independent_partition: ScenarioAnalysis
) -> IndependenceObstruction:
    return IndependenceObstruction(
        same_povm_response=(
            _povm_response_signature(copy_partition.scenario)
            == _povm_response_signature(independent_partition.scenario)
        ),
        same_access_window=(
            _access_signature(copy_partition.scenario)
            == _access_signature(independent_partition.scenario)
        ),
        copy_partition_finalized=copy_partition.predicates.observer_finalized,
        independent_partition_finalized=(
            independent_partition.predicates.observer_finalized
        ),
        verdict_flips=(
            copy_partition.predicates.observer_finalized
            != independent_partition.predicates.observer_finalized
        ),
        interpretation=(
            "The archive copy and independent archive have identical calibrated "
            "response data.  The D1 verdict changes only because the provenance "
            "partition changes."
        ),
    )


def _predicates(
    *,
    scenario: POVMScenario,
    pointer_coherence_abs: float,
    total_r_delta_raw: int,
    accessible_r_delta_raw: int,
    accessible_r_delta_independent: int,
) -> ScenarioPredicates:
    decohered = pointer_coherence_abs <= scenario.coherence_threshold
    redundant = total_r_delta_raw >= scenario.reconstruction_threshold
    observer_finalized = (
        accessible_r_delta_independent >= scenario.reconstruction_threshold
    )
    return ScenarioPredicates(
        decohered_pointer=decohered,
        povm_redundant_total=redundant,
        observer_finalized=observer_finalized,
        redundant_but_inaccessible=(
            decohered
            and redundant
            and accessible_r_delta_raw == 0
            and not observer_finalized
        ),
        raw_redundancy_overcounts_independence=(
            accessible_r_delta_raw >= scenario.reconstruction_threshold
            and accessible_r_delta_independent < scenario.reconstruction_threshold
        ),
    )


def _classify(predicates: ScenarioPredicates) -> tuple[str, str]:
    if predicates.raw_redundancy_overcounts_independence:
        return (
            "povm_independence_obstruction",
            (
                "Calibrated response data give enough raw accessible records, "
                "but provenance says too few are independent for D1 finality."
            ),
        )
    if predicates.redundant_but_inaccessible:
        return (
            "povm_redundant_but_inaccessible",
            (
                "The calibrated detector has redundant above-threshold records, "
                "but this observer has no access window onto them."
            ),
        )
    if predicates.decohered_pointer and predicates.povm_redundant_total:
        if predicates.observer_finalized:
            return (
                "povm_record_finalized",
                (
                    "Calibrated fragment information, observer access, and "
                    "independent holder redundancy all cross threshold."
                ),
            )
        return (
            "povm_underfinalized",
            (
                "The calibrated detector is redundant in total but not final "
                "for this observer under the declared D1 inputs."
            ),
        )
    return (
        "povm_below_redundancy_threshold",
        (
            "The calibrated detector responses do not supply enough "
            "above-threshold fragments under the declared threshold."
        ),
    )


def _has_started(fragment: POVMFragment, scenario: POVMScenario) -> bool:
    return fragment.available_from <= scenario.observer_time


def _is_available(fragment: POVMFragment, scenario: POVMScenario) -> bool:
    return fragment.available_from <= scenario.observer_time <= fragment.available_until


def _pointer_coherence_abs(started_fragments: tuple[POVMFragment, ...]) -> float:
    coherence = INITIAL_POINTER_COHERENCE
    for fragment in started_fragments:
        coherence *= fragment.decoherence_factor
    return coherence


def _independent_erasure_cost_below_threshold(
    independent_support_count: int, reconstruction_threshold: int
) -> int:
    if independent_support_count < reconstruction_threshold:
        return 0
    return independent_support_count - reconstruction_threshold + 1


def _binary_entropy_bits(probability_one: float) -> float:
    _validate_probability(probability_one)
    if probability_one <= 0.0 or probability_one >= 1.0:
        return 0.0
    probability_zero = 1.0 - probability_one
    return -(
        probability_zero * log2(probability_zero)
        + probability_one * log2(probability_one)
    )


def _povm_response_signature(scenario: POVMScenario) -> tuple[tuple[object, ...], ...]:
    return tuple(
        (
            fragment.name,
            fragment.holder,
            fragment.p_readout_up_given_spin_up,
            fragment.p_readout_up_given_spin_down,
            fragment.available_from,
            fragment.available_until,
        )
        for fragment in scenario.fragments
    )


def _access_signature(scenario: POVMScenario) -> tuple[object, ...]:
    return (
        tuple(sorted(scenario.observer_holders)),
        scenario.observer_time,
        scenario.reconstruction_threshold,
        scenario.information_threshold_bits,
    )


def _validate_probability(value: float) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError("probability must be in [0.0, 1.0]")


def _validate_scenario(scenario: POVMScenario) -> None:
    if scenario.reconstruction_threshold < 1:
        raise ValueError("reconstruction_threshold must be positive")
    if scenario.observer_time < 0:
        raise ValueError("observer_time must be non-negative")
    holders = {fragment.holder for fragment in scenario.fragments}
    unknown_holders = scenario.observer_holders - holders
    if unknown_holders:
        raise ValueError(f"observer_holders contains unknown holders: {unknown_holders}")
    for fragment in scenario.fragments:
        _validate_probability(fragment.p_readout_up_given_spin_up)
        _validate_probability(fragment.p_readout_up_given_spin_down)
        if not 0.0 <= fragment.decoherence_factor <= 1.0:
            raise ValueError("decoherence_factor must be in [0.0, 1.0]")
        if fragment.available_until < fragment.available_from:
            raise ValueError("fragment availability interval is inverted")


def _analysis_to_dict(analysis: ScenarioAnalysis) -> dict[str, object]:
    scenario = analysis.scenario
    return {
        "name": scenario.name,
        "purpose": scenario.purpose,
        "observer_holders": sorted(scenario.observer_holders),
        "observer_time": scenario.observer_time,
        "reconstruction_threshold": scenario.reconstruction_threshold,
        "information_threshold_bits": scenario.information_threshold_bits,
        "coherence_threshold": scenario.coherence_threshold,
        "fragments": [
            {
                "name": fragment.name,
                "holder": fragment.holder,
                "p_readout_up_given_spin_up": (
                    fragment.p_readout_up_given_spin_up
                ),
                "p_readout_up_given_spin_down": (
                    fragment.p_readout_up_given_spin_down
                ),
                "information_bits": round(
                    povm_mutual_information_bits(
                        fragment.p_readout_up_given_spin_up,
                        fragment.p_readout_up_given_spin_down,
                    ),
                    12,
                ),
                "decoherence_factor": fragment.decoherence_factor,
                "independence_class": fragment.independence_class,
                "branch_id": fragment.branch_id,
                "available_from": fragment.available_from,
                "available_until": fragment.available_until,
                "physical_role": fragment.physical_role,
                "provenance": fragment.provenance,
            }
            for fragment in scenario.fragments
        ],
        "pointer_coherence_abs": analysis.pointer_coherence_abs,
        "started_fragments": list(analysis.started_fragments),
        "available_fragments": list(analysis.available_fragments),
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
            "povm_redundant_total": analysis.predicates.povm_redundant_total,
            "observer_finalized": analysis.predicates.observer_finalized,
            "redundant_but_inaccessible": (
                analysis.predicates.redundant_but_inaccessible
            ),
            "raw_redundancy_overcounts_independence": (
                analysis.predicates.raw_redundancy_overcounts_independence
            ),
        },
        "classification": analysis.classification,
        "interpretation": analysis.interpretation,
    }
