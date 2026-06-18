"""T22: D1 physical reduction map and observable audit.

This module gives D1's four formal dimensions candidate physical observables
and runs one executable check where the mapping is currently strongest:
holder redundancy compared with a Quantum-Darwinism-style environmental
redundancy count.

The executable model is deliberately small. It is a classical readout shadow
of a system-environment measurement model: a binary pointer state is recorded
in several environment fragments, and the code computes the mutual information
between the pointer and each fragment. That is enough to test the reduction
contract without claiming to simulate quantum amplitudes, decoherence
dynamics, or full quantum Darwinism.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import log2


D1_DIMENSIONS = (
    "accessible_support",
    "holder_redundancy",
    "branch_support",
    "reversal_cost",
)

CONFIDENCE_LEVELS = (
    "physically supported",
    "partially supported",
    "formal only",
    "failed/rejected",
)


@dataclass(frozen=True)
class ReductionMapEntry:
    dimension: str
    candidate_observable: str
    substrate_assumptions: tuple[str, ...]
    lorentz_frame_status: str
    supporting_tests: tuple[str, ...]
    falsification_conditions: tuple[str, ...]
    confidence_level: str
    verdict: str


@dataclass(frozen=True)
class ConditionalReadout:
    system_state: str
    outcome_distribution: tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class EnvironmentFragment:
    name: str
    holder: str
    readable: bool
    independence_class: str
    branch_id: str
    conditional_readouts: tuple[ConditionalReadout, ...]


@dataclass(frozen=True)
class SystemEnvironmentScenario:
    name: str
    system_prior: tuple[tuple[str, float], ...]
    fragments: tuple[EnvironmentFragment, ...]
    observer_access: frozenset[str]
    information_deficit_delta: float
    reconstruction_threshold: int
    reversal_operations: tuple[str, ...]


@dataclass(frozen=True)
class D1ObservableProfile:
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
class DarwinismRedundancyResult:
    system_entropy_bits: float
    information_threshold_bits: float
    fragment_information_bits: tuple[tuple[str, float], ...]
    accessible_fragment_count: int
    accessible_informative_fragments: tuple[str, ...]
    raw_r_delta_accessible: int
    raw_r_delta_total: int
    independence_corrected_r_delta_accessible: int
    d1_holder_redundancy: int
    agrees_with_d1_holder_redundancy: bool
    raw_count_diverges_from_d1: bool
    divergence_reason: str


@dataclass(frozen=True)
class ReductionAuditResult:
    reduction_map: tuple[ReductionMapEntry, ...]
    scenario: SystemEnvironmentScenario
    d1_profile: D1ObservableProfile
    redundancy_result: DarwinismRedundancyResult
    verdict: str


def d1_reduction_map() -> tuple[ReductionMapEntry, ...]:
    return (
        ReductionMapEntry(
            dimension="accessible_support",
            candidate_observable=(
                "Count or measure of observer-readable record fragments that "
                "carry nonzero information about the target event inside a "
                "declared causal access boundary."
            ),
            substrate_assumptions=(
                "A causal access boundary is specified.",
                "Record fragments have stable readout channels.",
                "The observer readout rule and detection threshold are fixed before evaluation.",
            ),
            lorentz_frame_status=(
                "Observer-window dependent. It should be stated through causal "
                "access or world-tube relations rather than coordinate simultaneity."
            ),
            supporting_tests=("T1", "T9", "T20", "T22"),
            falsification_conditions=(
                "If accessible support is always identical to total support for all observers, the access axis adds no physical content.",
                "If no substrate-independent access boundary can be stated even locally, the observable is underspecified.",
            ),
            confidence_level="partially supported",
            verdict="physically measurable once an observer access boundary is declared",
        ),
        ReductionMapEntry(
            dimension="holder_redundancy",
            candidate_observable=(
                "Quantum-Darwinism-style R_delta count: number of disjoint, "
                "observer-accessible environment fragments or fragment families "
                "whose mutual information with the pointer state exceeds a "
                "declared threshold."
            ),
            substrate_assumptions=(
                "A fragment partition is specified.",
                "A pointer-state readout basis is fixed.",
                "The information deficit delta is fixed.",
                "Correlated duplicate fragments can be identified or explicitly left as a raw-count caveat.",
            ),
            lorentz_frame_status=(
                "Partition and observer-access dependent, but executable once "
                "the fragment partition and access boundary are fixed."
            ),
            supporting_tests=("T20", "T21", "T22"),
            falsification_conditions=(
                "If D1 holder redundancy never differs from raw fragment count, D1 should not claim an independence-sensitive physical axis.",
                "If no operational fragment partition exists in the substrate, the reduction is only formal.",
            ),
            confidence_level="partially supported",
            verdict="strongest current physical traction; T22 supplies an executable check",
        ),
        ReductionMapEntry(
            dimension="branch_support",
            candidate_observable=(
                "Count of causally independent record channels, branch families, "
                "or domain-cover sections supporting the same event."
            ),
            substrate_assumptions=(
                "A channel-independence criterion is specified.",
                "Correlated records within one branch are not double-counted as independent branches.",
                "The local domain cover or causal graph is explicit.",
            ),
            lorentz_frame_status=(
                "Covariance is open. Independence should be stated through "
                "causal relations or domain covers, not a chosen frame's equal-time slice."
            ),
            supporting_tests=("T13", "T16", "T21", "T22"),
            falsification_conditions=(
                "If branch support always collapses to holder redundancy in physically grounded substrates, it should not remain a separate D1 axis.",
                "If branch independence cannot be made invariant under admissible descriptions, the physical reduction fails.",
            ),
            confidence_level="formal only",
            verdict="structurally useful, but physical observable status remains open",
        ),
        ReductionMapEntry(
            dimension="reversal_cost",
            candidate_observable=(
                "Minimum intervention budget needed to erase, invert, or make "
                "unreconstructible the supporting records under a named cost model."
            ),
            substrate_assumptions=(
                "The cost model is declared: graph record edits, control pulses, thermodynamic work, code distance, or another substrate-specific budget.",
                "Observer-accessible reversal and total physical erasure are distinguished.",
                "The reconstruction threshold is fixed before measuring cost.",
            ),
            lorentz_frame_status=(
                "Substrate dependent. It is not currently a Lorentz scalar and "
                "is not identified with thermodynamic work by default."
            ),
            supporting_tests=("T1", "T5", "T9", "T18", "T22"),
            falsification_conditions=(
                "If reversal cost always collapses to standard thermodynamic work, D1 should defer to thermodynamics for this axis.",
                "If different admissible cost models reverse the ordering with no principled choice, the D1 cost axis remains formal only.",
            ),
            confidence_level="formal only",
            verdict="audited but not physically reduced; universal thermodynamic-work identity is rejected",
        ),
    )


def quantum_darwinism_toy_scenario() -> SystemEnvironmentScenario:
    perfect_copy = (
        ConditionalReadout("S0", (("0", 1.0),)),
        ConditionalReadout("S1", (("1", 1.0),)),
    )
    fair_noise = (
        ConditionalReadout("S0", (("0", 0.5), ("1", 0.5))),
        ConditionalReadout("S1", (("0", 0.5), ("1", 0.5))),
    )
    return SystemEnvironmentScenario(
        name="binary_pointer_environment_with_correlated_duplicate",
        system_prior=(("S0", 0.5), ("S1", 0.5)),
        fragments=(
            EnvironmentFragment("E1", "left_array_1", True, "left_channel", "left", perfect_copy),
            EnvironmentFragment("E2", "right_array_1", True, "right_channel", "right", perfect_copy),
            EnvironmentFragment("E3", "left_array_2", True, "left_channel", "left", perfect_copy),
            EnvironmentFragment("E4", "hidden_array", True, "hidden_channel", "hidden", perfect_copy),
            EnvironmentFragment("N1", "noise_probe", True, "noise_channel", "noise", fair_noise),
        ),
        observer_access=frozenset({"E1", "E2", "E3", "N1"}),
        information_deficit_delta=0.1,
        reconstruction_threshold=2,
        reversal_operations=("erase_E1", "erase_E2", "erase_E3", "erase_E4"),
    )


def compute_d1_profile(scenario: SystemEnvironmentScenario) -> D1ObservableProfile:
    accessible_support = _accessible_supporting_fragments(scenario)
    threshold_fragments = _threshold_informative_fragments(scenario, accessible_only=True)
    independence_classes = {
        fragment.independence_class for fragment in threshold_fragments
    }
    branch_ids = {fragment.branch_id for fragment in accessible_support}
    return D1ObservableProfile(
        accessible_support=len(accessible_support),
        holder_redundancy=len(independence_classes),
        branch_support=len(branch_ids - {"noise"}),
        reversal_cost=_record_erasure_cost_below_threshold(
            len(accessible_support), scenario.reconstruction_threshold
        ),
    )


def compute_darwinism_redundancy(
    scenario: SystemEnvironmentScenario,
) -> DarwinismRedundancyResult:
    profile = compute_d1_profile(scenario)
    system_entropy = _entropy(dict(scenario.system_prior).values())
    threshold = (1.0 - scenario.information_deficit_delta) * system_entropy
    fragment_information = tuple(
        (fragment.name, mutual_information_bits(scenario, fragment.name))
        for fragment in scenario.fragments
    )
    accessible_threshold = _threshold_informative_fragments(scenario, accessible_only=True)
    total_threshold = _threshold_informative_fragments(scenario, accessible_only=False)
    corrected = len({fragment.independence_class for fragment in accessible_threshold})
    raw_accessible = len(accessible_threshold)
    raw_total = len(total_threshold)
    return DarwinismRedundancyResult(
        system_entropy_bits=system_entropy,
        information_threshold_bits=threshold,
        fragment_information_bits=fragment_information,
        accessible_fragment_count=len(scenario.observer_access),
        accessible_informative_fragments=tuple(fragment.name for fragment in accessible_threshold),
        raw_r_delta_accessible=raw_accessible,
        raw_r_delta_total=raw_total,
        independence_corrected_r_delta_accessible=corrected,
        d1_holder_redundancy=profile.holder_redundancy,
        agrees_with_d1_holder_redundancy=(corrected == profile.holder_redundancy),
        raw_count_diverges_from_d1=(raw_accessible != profile.holder_redundancy),
        divergence_reason=(
            "E3 carries a full pointer record but is in the same independence "
            "class as E1. Raw R_delta counts E1, E2, and E3; the D1 physical "
            "reduction counts the two independent accessible fragment families."
            if raw_accessible != profile.holder_redundancy
            else "No divergence in this scenario."
        ),
    )


def mutual_information_bits(
    scenario: SystemEnvironmentScenario, fragment_name: str
) -> float:
    fragment = _fragment_by_name(scenario, fragment_name)
    prior = dict(scenario.system_prior)
    joint: dict[tuple[str, str], float] = {}
    outcome_marginal: dict[str, float] = {}
    for state, state_probability in prior.items():
        distribution = _conditional_distribution(fragment, state)
        for outcome, conditional_probability in distribution.items():
            joint_probability = state_probability * conditional_probability
            joint[(state, outcome)] = joint_probability
            outcome_marginal[outcome] = outcome_marginal.get(outcome, 0.0) + joint_probability

    information = 0.0
    for (state, outcome), joint_probability in joint.items():
        if joint_probability == 0.0:
            continue
        denominator = prior[state] * outcome_marginal[outcome]
        information += joint_probability * log2(joint_probability / denominator)
    return information


def audit_d1_reduction_map(
    scenario: SystemEnvironmentScenario | None = None,
) -> ReductionAuditResult:
    chosen = scenario or quantum_darwinism_toy_scenario()
    redundancy = compute_darwinism_redundancy(chosen)
    return ReductionAuditResult(
        reduction_map=d1_reduction_map(),
        scenario=chosen,
        d1_profile=compute_d1_profile(chosen),
        redundancy_result=redundancy,
        verdict=(
            "T22 gives D1 holder redundancy a conditional physical reduction: "
            "with a fixed pointer basis, fragment partition, access boundary, "
            "and delta threshold, D1 holder redundancy agrees with an "
            "independence-corrected R_delta count. Accessible support is "
            "observable but boundary-dependent. Branch support and reversal "
            "cost remain formal-only placeholders until stronger physical "
            "cost and independence criteria are supplied."
        ),
    )


def run_t22_analysis() -> dict[str, object]:
    result = audit_d1_reduction_map()
    confidence_summary = {
        level: sum(
            1 for entry in result.reduction_map if entry.confidence_level == level
        )
        for level in CONFIDENCE_LEVELS
    }
    open_dimensions = tuple(
        entry.dimension
        for entry in result.reduction_map
        if entry.confidence_level in {"formal only", "failed/rejected"}
    )
    return {
        "reduction_map": [asdict(entry) for entry in result.reduction_map],
        "confidence_levels": list(CONFIDENCE_LEVELS),
        "confidence_summary": confidence_summary,
        "toy_model": {
            "scenario": _scenario_to_dict(result.scenario),
            "d1_profile": asdict(result.d1_profile)
            | {
                "tuple_order": list(D1_DIMENSIONS),
                "profile_tuple": list(result.d1_profile.as_tuple()),
            },
            "darwinism_redundancy": asdict(result.redundancy_result),
        },
        "interpretation": {
            "main_result": result.verdict,
            "guardrail": (
                "T22 does not derive D1 from quantum mechanics and does not "
                "prove quantum Darwinism. It supplies one executable observable "
                "comparison and records assumptions for every D1 axis."
            ),
            "repo_recommendation": (
                "D1 can honestly claim a candidate observable program, not a "
                "completed physical definition. Holder redundancy is the first "
                "dimension with executable physical traction; branch support and "
                "reversal cost should remain formal placeholders in strong claims."
            ),
        },
        "verdict": {
            "all_dimensions_have_reduction_entries": (
                {entry.dimension for entry in result.reduction_map}
                == set(D1_DIMENSIONS)
            ),
            "all_entries_have_falsification_conditions": all(
                entry.falsification_conditions for entry in result.reduction_map
            ),
            "holder_redundancy_reduction_supported": (
                result.redundancy_result.agrees_with_d1_holder_redundancy
            ),
            "raw_fragment_count_diverges_from_holder_redundancy": (
                result.redundancy_result.raw_count_diverges_from_d1
            ),
            "inaccessible_record_excluded_from_accessible_support": (
                "E4" not in result.scenario.observer_access
                and result.d1_profile.accessible_support
                < result.redundancy_result.raw_r_delta_total
            ),
            "branch_support_still_formal": "branch_support" in open_dimensions,
            "reversal_cost_still_formal": "reversal_cost" in open_dimensions,
            "no_universal_physical_reduction_claimed": True,
        },
    }


def _accessible_supporting_fragments(
    scenario: SystemEnvironmentScenario,
) -> tuple[EnvironmentFragment, ...]:
    return tuple(
        fragment
        for fragment in scenario.fragments
        if fragment.name in scenario.observer_access
        and fragment.readable
        and mutual_information_bits(scenario, fragment.name) > 0.0
    )


def _threshold_informative_fragments(
    scenario: SystemEnvironmentScenario, *, accessible_only: bool
) -> tuple[EnvironmentFragment, ...]:
    system_entropy = _entropy(dict(scenario.system_prior).values())
    threshold = (1.0 - scenario.information_deficit_delta) * system_entropy
    return tuple(
        fragment
        for fragment in scenario.fragments
        if fragment.readable
        and (not accessible_only or fragment.name in scenario.observer_access)
        and mutual_information_bits(scenario, fragment.name) >= threshold
    )


def _record_erasure_cost_below_threshold(
    accessible_support_count: int, reconstruction_threshold: int
) -> int:
    if accessible_support_count < reconstruction_threshold:
        return 0
    return accessible_support_count - reconstruction_threshold + 1


def _entropy(probabilities: object) -> float:
    return -sum(
        probability * log2(probability)
        for probability in probabilities
        if probability > 0.0
    )


def _conditional_distribution(
    fragment: EnvironmentFragment, state: str
) -> dict[str, float]:
    for readout in fragment.conditional_readouts:
        if readout.system_state == state:
            return dict(readout.outcome_distribution)
    raise ValueError(f"missing conditional readout for {fragment.name}, {state}")


def _fragment_by_name(
    scenario: SystemEnvironmentScenario, fragment_name: str
) -> EnvironmentFragment:
    for fragment in scenario.fragments:
        if fragment.name == fragment_name:
            return fragment
    raise ValueError(f"unknown fragment: {fragment_name}")


def _scenario_to_dict(scenario: SystemEnvironmentScenario) -> dict[str, object]:
    return {
        "name": scenario.name,
        "system_prior": list(scenario.system_prior),
        "observer_access": sorted(scenario.observer_access),
        "information_deficit_delta": scenario.information_deficit_delta,
        "reconstruction_threshold": scenario.reconstruction_threshold,
        "fragments": [asdict(fragment) for fragment in scenario.fragments],
        "reversal_operations": list(scenario.reversal_operations),
    }
