"""T64: Stern-Gerlach detector access-window discriminator.

This module turns the T62 noisy-channel audit into a detector-level toy model.
It treats a Stern-Gerlach readout as a family of noisy binary record fragments:
screen spot, electronics pulse, local log, archive mirror, and weak thermal
trace.  The point is not to simulate a magnet or derive collapse.  The point is
to ask whether observer-relative D1 finality adds a testable predicate after a
fragment partition, access window, information threshold, and independence
partition are physically declared.

The model also includes a finite no-signalling audit for an entangled-pair
variant.  Remote setting changes alter correlations but not the local detector
readout marginal.  If a future finality rule changes that marginal, Q1 fails.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, log2, pi


INITIAL_POINTER_COHERENCE = 0.5
DEFAULT_INFORMATION_THRESHOLD_BITS = 0.75
DEFAULT_COHERENCE_THRESHOLD = 0.01
DEFAULT_RECONSTRUCTION_THRESHOLD = 2
THRESHOLD_SWEEP_BITS = (0.6, 0.75, 0.9)
ACCESS_SWEEP_TIMES = (1.25, 2.5, 4.5)
LOCAL_SETTINGS = {"local_z": 0.0, "local_x": pi / 2.0}
REMOTE_SETTINGS = {"remote_z": 0.0, "remote_x": pi / 2.0, "remote_diag": pi / 4.0}


@dataclass(frozen=True)
class DetectorFragment:
    name: str
    holder: str
    readout_reliability: float
    decoherence_factor: float
    independence_class: str
    branch_id: str
    available_from: float
    available_until: float
    physical_role: str


@dataclass(frozen=True)
class SternGerlachScenario:
    name: str
    fragments: tuple[DetectorFragment, ...]
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
    darwinism_redundant_total: bool
    observer_finalized: bool
    redundant_but_inaccessible: bool
    access_window_underfinalized: bool
    raw_redundancy_overcounts_independence: bool


@dataclass(frozen=True)
class ScenarioAnalysis:
    scenario: SternGerlachScenario
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
class ThresholdSweepPoint:
    information_threshold_bits: float
    observer_time: float
    total_r_delta_raw: int
    accessible_r_delta_independent: int
    observer_finalized: bool
    classification: str


@dataclass(frozen=True)
class NoSignallingAudit:
    local_setting: str
    local_detector_reliability: float
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
class T64Result:
    scenarios: tuple[ScenarioAnalysis, ...]
    threshold_sweep: tuple[ThresholdSweepPoint, ...]
    threshold_flip_count: int
    no_signalling_audits: tuple[NoSignallingAudit, ...]
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    recommended_next: str


def canonical_detector_fragments() -> tuple[DetectorFragment, ...]:
    """Return the finite Stern-Gerlach detector-fragment proxy."""

    return (
        DetectorFragment(
            name="screen_spot",
            holder="local_screen",
            readout_reliability=0.985,
            decoherence_factor=0.08,
            independence_class="screen_grain",
            branch_id="sg_z_pointer",
            available_from=1.0,
            available_until=3.0,
            physical_role="transient spatial spot on the detector screen",
        ),
        DetectorFragment(
            name="photodiode_pulse",
            holder="photodiode",
            readout_reliability=0.97,
            decoherence_factor=0.12,
            independence_class="electronics",
            branch_id="sg_z_pointer",
            available_from=1.5,
            available_until=5.0,
            physical_role="amplified local electronics pulse",
        ),
        DetectorFragment(
            name="local_log",
            holder="local_logger",
            readout_reliability=0.99,
            decoherence_factor=0.2,
            independence_class="local_log",
            branch_id="sg_z_pointer",
            available_from=2.0,
            available_until=10.0,
            physical_role="timestamped local detector log",
        ),
        DetectorFragment(
            name="network_archive",
            holder="archive_mirror",
            readout_reliability=0.99,
            decoherence_factor=0.5,
            independence_class="local_log",
            branch_id="sg_z_pointer",
            available_from=4.0,
            available_until=20.0,
            physical_role="network copy of the local log; not independent",
        ),
        DetectorFragment(
            name="thermal_bath_trace",
            holder="cryostat_bath",
            readout_reliability=0.62,
            decoherence_factor=0.3,
            independence_class="thermal_bath",
            branch_id="bath_scattering",
            available_from=0.5,
            available_until=20.0,
            physical_role="weak bath trace below the information threshold",
        ),
    )


def canonical_scenarios() -> tuple[SternGerlachScenario, ...]:
    fragments = canonical_detector_fragments()
    local_holders = frozenset({"local_screen", "photodiode", "local_logger"})
    all_holders = frozenset(
        {"local_screen", "photodiode", "local_logger", "archive_mirror"}
    )

    return (
        SternGerlachScenario(
            name="local_lab_after_readout",
            fragments=fragments,
            observer_holders=local_holders,
            observer_time=2.5,
            purpose=(
                "Positive control: screen, electronics, and local log are all "
                "above threshold and accessible to the local observer."
            ),
        ),
        SternGerlachScenario(
            name="redundant_but_before_access",
            fragments=fragments,
            observer_holders=frozenset(),
            observer_time=2.5,
            purpose=(
                "Detector records exist, but this observer has no access "
                "window onto any holder."
            ),
        ),
        SternGerlachScenario(
            name="single_channel_early_window",
            fragments=fragments,
            observer_holders=frozenset({"local_screen"}),
            observer_time=1.25,
            purpose=(
                "A transient screen spot is accessible before redundant "
                "detector records exist."
            ),
        ),
        SternGerlachScenario(
            name="duplicate_archive_boundary",
            fragments=fragments,
            observer_holders=all_holders,
            observer_time=4.5,
            reconstruction_threshold=3,
            purpose=(
                "The archive mirror creates raw redundancy, but it is a copy "
                "of the local log rather than an independent holder class."
            ),
        ),
        SternGerlachScenario(
            name="high_threshold_fragility",
            fragments=fragments,
            observer_holders=local_holders,
            observer_time=2.5,
            information_threshold_bits=0.9,
            purpose=(
                "High information thresholds erase the apparent finality of "
                "the same detector access window."
            ),
        ),
    )


def analyze_scenario(scenario: SternGerlachScenario) -> ScenarioAnalysis:
    _validate_scenario(scenario)

    information = tuple(
        (fragment.name, round(mutual_information_bits(fragment.readout_reliability), 12))
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


def run_t64_analysis() -> T64Result:
    analyses = tuple(analyze_scenario(scenario) for scenario in canonical_scenarios())
    by_name = {analysis.scenario.name: analysis for analysis in analyses}
    sweep = run_threshold_sweep()
    threshold_flip_count = _threshold_flip_count(sweep)
    no_signalling_audits = run_no_signalling_audits()

    return T64Result(
        scenarios=analyses,
        threshold_sweep=sweep,
        threshold_flip_count=threshold_flip_count,
        no_signalling_audits=no_signalling_audits,
        hypothesis_evaluations=(
            HypothesisEvaluation(
                hypothesis_id="H1",
                status="supported",
                claim=(
                    "A detector-level access window can separate total "
                    "detector redundancy from observer-relative D1 finality."
                ),
                evidence=(
                    f"{by_name['redundant_but_before_access'].scenario.name} has "
                    f"total R_delta={by_name['redundant_but_before_access'].total_r_delta_raw} "
                    "but D1 profile (0, 0, 0, 0)."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H2",
                status="supported",
                claim=(
                    "Raw fragment redundancy can overcount independent "
                    "detector holders."
                ),
                evidence=(
                    f"{by_name['duplicate_archive_boundary'].scenario.name} has "
                    f"accessible raw R_delta={by_name['duplicate_archive_boundary'].accessible_r_delta_raw} "
                    f"but independent R_delta={by_name['duplicate_archive_boundary'].accessible_r_delta_independent}."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H3",
                status="weakened",
                claim=(
                    "The detector-level D1 predicate is threshold-sensitive, "
                    "so Q1 does not yet produce a calibration-free prediction."
                ),
                evidence=(
                    f"The threshold sweep contains {threshold_flip_count} "
                    "observer-time slices whose finalized/not-finalized verdict "
                    "changes across thresholds."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H4",
                status="supported",
                claim=(
                    "The access-window finality rule does not create signalling "
                    "in the finite entangled-pair audit."
                ),
                evidence=(
                    "All local readout marginals are invariant under remote "
                    "setting changes to numerical precision."
                ),
            ),
            HypothesisEvaluation(
                hypothesis_id="H5",
                status="open",
                claim=(
                    "The access windows, thresholds, and independence partition "
                    "still need derivation from real detector physics."
                ),
                evidence=(
                    "T64 declares these inputs rather than deriving them from a "
                    "Hamiltonian, POVM, or measured detector response curve."
                ),
            ),
        ),
        strongest_claim=(
            "In the T64 Stern-Gerlach toy detector, TaF adds at most an "
            "observer-access and independence-filter predicate over already "
            "formed detector records; it does not add collapse or new noisy "
            "measurement dynamics."
        ),
        weakened_claim=(
            "Q1 is weakened because detector finality can flip under plausible "
            "information-threshold choices. Without a physically justified "
            "threshold and independence partition, the D1 verdict is bookkeeping."
        ),
        falsification_condition=(
            "If detector physics fixes admissible access windows and "
            "independence classes such that D1 always equals standard fragment "
            "redundancy R_delta, or if those inputs cannot be physically "
            "specified at all, Q1 adds no independent measurement content."
        ),
        recommended_next=(
            "Replace the declared binary channels with a calibrated detector "
            "model: a POVM or scattering response curve that fixes fragment "
            "reliabilities, access windows, and independence classes before "
            "the D1 predicate is evaluated."
        ),
    )


def run_threshold_sweep() -> tuple[ThresholdSweepPoint, ...]:
    fragments = canonical_detector_fragments()
    observer_holders = frozenset(
        {"local_screen", "photodiode", "local_logger", "archive_mirror"}
    )
    points: list[ThresholdSweepPoint] = []
    for threshold in THRESHOLD_SWEEP_BITS:
        for observer_time in ACCESS_SWEEP_TIMES:
            scenario = SternGerlachScenario(
                name=f"sweep_threshold_{threshold}_time_{observer_time}",
                fragments=fragments,
                observer_holders=observer_holders,
                observer_time=observer_time,
                information_threshold_bits=threshold,
                reconstruction_threshold=DEFAULT_RECONSTRUCTION_THRESHOLD,
            )
            analysis = analyze_scenario(scenario)
            points.append(
                ThresholdSweepPoint(
                    information_threshold_bits=threshold,
                    observer_time=observer_time,
                    total_r_delta_raw=analysis.total_r_delta_raw,
                    accessible_r_delta_independent=(
                        analysis.accessible_r_delta_independent
                    ),
                    observer_finalized=analysis.predicates.observer_finalized,
                    classification=analysis.classification,
                )
            )
    return tuple(points)


def run_no_signalling_audits(
    local_detector_reliability: float = 0.985,
) -> tuple[NoSignallingAudit, ...]:
    audits: list[NoSignallingAudit] = []
    for local_setting, local_angle in LOCAL_SETTINGS.items():
        marginals = tuple(
            (
                remote_setting,
                round(
                    local_readout_up_probability(
                        local_angle=local_angle,
                        remote_angle=remote_angle,
                        detector_reliability=local_detector_reliability,
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
                local_detector_reliability=local_detector_reliability,
                readout_up_probability_by_remote_setting=marginals,
                max_delta=max_delta,
                passed=max_delta <= 1e-12,
                interpretation=(
                    "Remote setting changes alter joint correlations but not "
                    "the local noisy detector marginal."
                ),
            )
        )
    return tuple(audits)


def mutual_information_bits(readout_reliability: float) -> float:
    if not 0.5 <= readout_reliability <= 1.0:
        raise ValueError("readout_reliability must be in [0.5, 1.0]")
    error_probability = 1.0 - readout_reliability
    return 1.0 - _binary_entropy_bits(error_probability)


def local_readout_up_probability(
    *, local_angle: float, remote_angle: float, detector_reliability: float
) -> float:
    if not 0.5 <= detector_reliability <= 1.0:
        raise ValueError("detector_reliability must be in [0.5, 1.0]")

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
                detector_reliability
                if local_outcome == 1
                else 1.0 - detector_reliability
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


def t64_result_to_dict(result: T64Result) -> dict[str, object]:
    return {
        "scenarios": [_analysis_to_dict(analysis) for analysis in result.scenarios],
        "threshold_sweep": [
            {
                "information_threshold_bits": point.information_threshold_bits,
                "observer_time": point.observer_time,
                "total_r_delta_raw": point.total_r_delta_raw,
                "accessible_r_delta_independent": point.accessible_r_delta_independent,
                "observer_finalized": point.observer_finalized,
                "classification": point.classification,
            }
            for point in result.threshold_sweep
        ],
        "threshold_flip_count": result.threshold_flip_count,
        "no_signalling_audits": [
            {
                "local_setting": audit.local_setting,
                "local_detector_reliability": audit.local_detector_reliability,
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


def _predicates(
    *,
    scenario: SternGerlachScenario,
    pointer_coherence_abs: float,
    total_r_delta_raw: int,
    accessible_r_delta_raw: int,
    accessible_r_delta_independent: int,
) -> ScenarioPredicates:
    decohered = pointer_coherence_abs <= scenario.coherence_threshold
    darwinism_redundant = total_r_delta_raw >= scenario.reconstruction_threshold
    observer_finalized = (
        accessible_r_delta_independent >= scenario.reconstruction_threshold
    )
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
        access_window_underfinalized=(
            accessible_r_delta_raw > 0 and not observer_finalized
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
                "The detector has enough raw accessible fragments, but the "
                "declared independence partition gives too few independent "
                "holder classes for D1 finality."
            ),
        )
    if predicates.redundant_but_inaccessible:
        return (
            "redundant_but_inaccessible",
            (
                "The detector has redundant above-threshold records, but this "
                "observer has no access window onto them."
            ),
        )
    if predicates.decohered_pointer and predicates.darwinism_redundant_total:
        if predicates.observer_finalized:
            return (
                "detector_record_finalized",
                (
                    "Decoherence, total detector redundancy, and "
                    "observer-relative D1 finality agree."
                ),
            )
        if predicates.access_window_underfinalized:
            return (
                "access_window_underfinalized",
                (
                    "Some detector records are accessible, but not enough "
                    "independent holder classes cross the D1 threshold."
                ),
            )
    if predicates.access_window_underfinalized:
        return (
            "single_channel_underfinalized",
            (
                "The observer has a local record channel, but not enough "
                "redundant detector records for D1 finality."
            ),
        )
    return (
        "unclassified_boundary",
        "The predicate combination falls outside the intended T64 witness matrix.",
    )


def _has_started(
    fragment: DetectorFragment, scenario: SternGerlachScenario
) -> bool:
    return fragment.available_from <= scenario.observer_time


def _is_available(
    fragment: DetectorFragment, scenario: SternGerlachScenario
) -> bool:
    return fragment.available_from <= scenario.observer_time <= fragment.available_until


def _pointer_coherence_abs(started_fragments: tuple[DetectorFragment, ...]) -> float:
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
    if probability_one <= 0.0 or probability_one >= 1.0:
        return 0.0
    probability_zero = 1.0 - probability_one
    return -(
        probability_zero * log2(probability_zero)
        + probability_one * log2(probability_one)
    )


def _threshold_flip_count(points: tuple[ThresholdSweepPoint, ...]) -> int:
    verdicts_by_time: dict[float, set[bool]] = {}
    for point in points:
        verdicts_by_time.setdefault(point.observer_time, set()).add(
            point.observer_finalized
        )
    return sum(1 for verdicts in verdicts_by_time.values() if len(verdicts) > 1)


def _validate_scenario(scenario: SternGerlachScenario) -> None:
    if scenario.reconstruction_threshold < 1:
        raise ValueError("reconstruction_threshold must be positive")
    if scenario.observer_time < 0:
        raise ValueError("observer_time must be non-negative")
    holders = {fragment.holder for fragment in scenario.fragments}
    unknown_holders = scenario.observer_holders - holders
    if unknown_holders:
        raise ValueError(f"observer_holders contains unknown holders: {unknown_holders}")
    for fragment in scenario.fragments:
        mutual_information_bits(fragment.readout_reliability)
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
                "readout_reliability": fragment.readout_reliability,
                "information_bits": round(
                    mutual_information_bits(fragment.readout_reliability), 12
                ),
                "decoherence_factor": fragment.decoherence_factor,
                "independence_class": fragment.independence_class,
                "branch_id": fragment.branch_id,
                "available_from": fragment.available_from,
                "available_until": fragment.available_until,
                "physical_role": fragment.physical_role,
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
            "darwinism_redundant_total": analysis.predicates.darwinism_redundant_total,
            "observer_finalized": analysis.predicates.observer_finalized,
            "redundant_but_inaccessible": (
                analysis.predicates.redundant_but_inaccessible
            ),
            "access_window_underfinalized": (
                analysis.predicates.access_window_underfinalized
            ),
            "raw_redundancy_overcounts_independence": (
                analysis.predicates.raw_redundancy_overcounts_independence
            ),
        },
        "classification": analysis.classification,
        "interpretation": analysis.interpretation,
    }
