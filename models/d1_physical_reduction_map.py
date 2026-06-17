"""T22: D1 physical reduction map and observable audit.

This module gives D1's four formal dimensions candidate physical observables
and runs one executable check where the mapping is currently strongest:
distinct holder redundancy compared with a Quantum-Darwinism-style count of
independent informative environment fragments.

The result is an audit, not a claim that all D1 dimensions are now physically
derived. It records assumptions and falsification conditions per dimension.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


D1_DIMENSIONS = (
    "accessible_support",
    "holder_redundancy",
    "branch_support",
    "reversal_cost",
)


@dataclass(frozen=True)
class ReductionMapEntry:
    dimension: str
    candidate_observable: str
    substrate_assumptions: tuple[str, ...]
    frame_status: str
    supporting_tests: tuple[str, ...]
    falsification_condition: str
    confidence: str
    verdict: str


@dataclass(frozen=True)
class EnvironmentFragment:
    name: str
    readable: bool
    encodes_system: bool
    independent_channel: bool
    branch_id: str


@dataclass(frozen=True)
class SystemEnvironmentScenario:
    name: str
    system_states: tuple[str, ...]
    fragments: tuple[EnvironmentFragment, ...]
    observer_access: frozenset[str]
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
    accessible_fragment_count: int
    raw_informative_fragment_count: int
    independent_informative_fragments: int
    redundancy_ratio: float
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
                "Count of observer-readable record fragments that encode the "
                "target system state inside the observer access boundary."
            ),
            substrate_assumptions=(
                "A causal access boundary is specified.",
                "Record fragments have a stable readout channel.",
                "The observer readout rule is fixed before evaluation.",
            ),
            frame_status=(
                "Observer-window dependent; valid only relative to the chosen "
                "causal access boundary."
            ),
            supporting_tests=("T1", "T9", "T20", "T22"),
            falsification_condition=(
                "If accessible support is always identical to total support "
                "regardless of access boundary, this D1 dimension adds no work."
            ),
            confidence="partially_supported",
            verdict="physically plausible but observer-boundary dependent",
        ),
        ReductionMapEntry(
            dimension="holder_redundancy",
            candidate_observable=(
                "Count of independent environment fragments carrying enough "
                "information to infer the system pointer state."
            ),
            substrate_assumptions=(
                "A fragment partition is specified.",
                "Informative fragments can be separated from noise fragments.",
                "Correlated duplicate fragments are not double-counted.",
                "The pointer-state readout basis is fixed.",
            ),
            frame_status=(
                "Partition dependent, but testable once the environment "
                "fragment partition and access boundary are stated."
            ),
            supporting_tests=("T20", "T21", "T22"),
            falsification_condition=(
                "If D1 holder redundancy is always just raw fragment count, or "
                "if no principled independence test exists, the reduction fails."
            ),
            confidence="partially_supported_executable",
            verdict="first executable reduction supplied by T22",
        ),
        ReductionMapEntry(
            dimension="branch_support",
            candidate_observable=(
                "Count of causally independent record channels or branch "
                "families supporting the same event."
            ),
            substrate_assumptions=(
                "A channel-independence criterion is specified.",
                "Correlated records within one branch are not double-counted.",
                "The causal domain cover is explicit.",
            ),
            frame_status=(
                "Covariance open; independence should be stated through causal "
                "relations, not coordinate simultaneity."
            ),
            supporting_tests=("T13", "T16", "T21", "T22"),
            falsification_condition=(
                "If branch support always collapses to holder redundancy in "
                "physical substrates, it should not remain a separate axis."
            ),
            confidence="formal_with_partial_support",
            verdict="separate in toy models; physical reduction still open",
        ),
        ReductionMapEntry(
            dimension="reversal_cost",
            candidate_observable=(
                "Minimum intervention, operation, or work budget needed to "
                "erase or invert all supporting records under a named cost model."
            ),
            substrate_assumptions=(
                "The cost model is declared: graph operations, thermodynamic "
                "work, control pulses, or another substrate-specific budget.",
                "Accessible erasure and total physical erasure are distinguished.",
            ),
            frame_status=(
                "Substrate dependent; not yet a Lorentz scalar or universal "
                "thermodynamic quantity."
            ),
            supporting_tests=("T1", "T5", "T9", "T18", "T22"),
            falsification_condition=(
                "If reversal cost always collapses to standard thermodynamic "
                "cost, D1 should defer to thermodynamics for this axis."
            ),
            confidence="weakest_open",
            verdict="audited but not physically reduced",
        ),
    )


def quantum_darwinism_toy_scenario() -> SystemEnvironmentScenario:
    return SystemEnvironmentScenario(
        name="binary_pointer_environment_with_correlated_duplicate",
        system_states=("S0", "S1"),
        fragments=(
            EnvironmentFragment("E1", True, True, True, "left"),
            EnvironmentFragment("E2", True, True, True, "right"),
            EnvironmentFragment("E3", True, True, False, "left"),
            EnvironmentFragment("E4", False, True, True, "hidden"),
            EnvironmentFragment("N1", True, False, True, "noise"),
        ),
        observer_access=frozenset({"E1", "E2", "E3", "N1"}),
        reversal_operations=("erase_E1", "erase_E2", "erase_E3", "erase_E4"),
    )


def compute_d1_profile(scenario: SystemEnvironmentScenario) -> D1ObservableProfile:
    accessible_informative = _accessible_informative_fragments(scenario)
    independent_accessible = tuple(
        fragment for fragment in accessible_informative if fragment.independent_channel
    )
    branch_ids = {fragment.branch_id for fragment in independent_accessible}
    return D1ObservableProfile(
        accessible_support=len(accessible_informative),
        holder_redundancy=len(independent_accessible),
        branch_support=len(branch_ids),
        reversal_cost=len(scenario.reversal_operations),
    )


def compute_darwinism_redundancy(
    scenario: SystemEnvironmentScenario,
) -> DarwinismRedundancyResult:
    accessible_count = len(scenario.observer_access)
    accessible_informative = _accessible_informative_fragments(scenario)
    independent_informative = tuple(
        fragment for fragment in accessible_informative if fragment.independent_channel
    )
    profile = compute_d1_profile(scenario)
    redundancy_ratio = len(independent_informative) / len(scenario.system_states)
    raw_diverges = len(accessible_informative) != profile.holder_redundancy
    return DarwinismRedundancyResult(
        accessible_fragment_count=accessible_count,
        raw_informative_fragment_count=len(accessible_informative),
        independent_informative_fragments=len(independent_informative),
        redundancy_ratio=redundancy_ratio,
        d1_holder_redundancy=profile.holder_redundancy,
        agrees_with_d1_holder_redundancy=(
            len(independent_informative) == profile.holder_redundancy
        ),
        raw_count_diverges_from_d1=raw_diverges,
        divergence_reason=(
            "E3 carries the pointer record but is correlated with E1, so it "
            "raises accessible support without raising independent holder "
            "redundancy."
            if raw_diverges
            else "No divergence in this scenario."
        ),
    )


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
            "Holder redundancy has a first executable physical reduction in "
            "the toy fragment model; accessible support, branch support, and "
            "reversal cost remain assumption-bearing audit entries."
        ),
    )


def run_t22_analysis() -> dict[str, object]:
    result = audit_d1_reduction_map()
    open_dimensions = tuple(
        entry.dimension
        for entry in result.reduction_map
        if entry.confidence in {"weakest_open", "formal_with_partial_support"}
    )
    return {
        "reduction_map": [asdict(entry) for entry in result.reduction_map],
        "toy_model": {
            "scenario": {
                "name": result.scenario.name,
                "system_states": list(result.scenario.system_states),
                "observer_access": sorted(result.scenario.observer_access),
                "fragments": [asdict(fragment) for fragment in result.scenario.fragments],
                "reversal_operations": list(result.scenario.reversal_operations),
            },
            "d1_profile": asdict(result.d1_profile)
            | {"tuple_order": list(D1_DIMENSIONS), "profile_tuple": list(result.d1_profile.as_tuple())},
            "darwinism_redundancy": asdict(result.redundancy_result),
        },
        "interpretation": {
            "main_result": result.verdict,
            "guardrail": (
                "T22 does not derive D1 from quantum mechanics. It supplies one "
                "toy observable reduction and records assumptions for every D1 axis."
            ),
            "why_it_matters": (
                "The model shows why D1 should count independent informative "
                "holders, not raw environmental copies."
            ),
        },
        "verdict": {
            "all_dimensions_have_reduction_entries": (
                {entry.dimension for entry in result.reduction_map}
                == set(D1_DIMENSIONS)
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
                < sum(1 for fragment in result.scenario.fragments if fragment.encodes_system)
            ),
            "reversal_cost_still_open": "reversal_cost" in open_dimensions,
            "no_universal_physical_reduction_claimed": True,
        },
    }


def _accessible_informative_fragments(
    scenario: SystemEnvironmentScenario,
) -> tuple[EnvironmentFragment, ...]:
    return tuple(
        fragment
        for fragment in scenario.fragments
        if fragment.name in scenario.observer_access
        and fragment.readable
        and fragment.encodes_system
    )
