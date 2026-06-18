"""T24: multiscale observer-field audit for D1.

T24 asks whether D1 should be represented only as one selected
observer-indexed profile, as a vector over observer populations, or as a field
over observer sites and communication/gluing structure.

The model keeps the existing D1 profile as the local value. The richer object
is a finite assignment:

    observer/scale/time site -> D1Profile

plus transport edges and optional local constraint patches.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from typing import Any


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
class ObserverSite:
    observer_id: str
    population: str
    scale: str
    time_step: int
    trust_domain: str


@dataclass(frozen=True)
class ObserverProfile:
    site: ObserverSite
    proposition_value: str
    profile: D1Profile


@dataclass(frozen=True)
class FieldEdge:
    source: str
    target: str
    relation: str
    trust_preserving: bool = True


@dataclass(frozen=True)
class PatchConstraint:
    left: str
    right: str
    relation: str


@dataclass(frozen=True)
class FieldPatch:
    patch_id: str
    observer_ids: tuple[str, ...]
    variables: tuple[str, ...]
    constraints: tuple[PatchConstraint, ...]


@dataclass(frozen=True)
class D1FieldScenario:
    name: str
    proposition: str
    observer_profiles: tuple[ObserverProfile, ...]
    edges: tuple[FieldEdge, ...]
    source_observer: str
    target_observer: str
    patches: tuple[FieldPatch, ...] = ()


@dataclass(frozen=True)
class ScalarReduction:
    rule: str
    profile: D1Profile
    recovered_without_loss: bool
    information_lost: tuple[str, ...]
    assumptions: tuple[str, ...]


@dataclass(frozen=True)
class VectorAnalysis:
    distinct_profile_count: int
    vector_required: bool
    reason: str
    vector: tuple[tuple[str, tuple[int, int, int, int]], ...]


@dataclass(frozen=True)
class FieldTransportAnalysis:
    graph_connected: bool
    trust_path_exists: bool
    source_observer: str
    target_observer: str
    field_required: bool
    reason: str


@dataclass(frozen=True)
class GluingAnalysis:
    local_patches_satisfiable: bool
    global_assignment_exists: bool
    obstruction_detected: bool
    obstruction_kind: str
    local_witness_count: int
    global_witness_count: int


@dataclass(frozen=True)
class VectorFieldComparison:
    left: str
    right: str
    same_vector: bool
    same_transport_result: bool
    field_information_lost_by_vector: bool
    reason: str


@dataclass(frozen=True)
class ScenarioAnalysis:
    scenario: D1FieldScenario
    scalar_min: ScalarReduction
    scalar_max: ScalarReduction
    vector: VectorAnalysis
    transport: FieldTransportAnalysis
    gluing: GluingAnalysis
    representation_needed: str


@dataclass(frozen=True)
class T24Result:
    analyses: tuple[ScenarioAnalysis, ...]
    vector_field_comparison: VectorFieldComparison
    reduction_tests: dict[str, bool | str]
    verdict: dict[str, bool | str]
    recommendation: str


def uniform_broadcast_scenario() -> D1FieldScenario:
    profiles = tuple(
        _observer_profile(
            observer_id,
            population,
            scale,
            time_step=3,
            trust_domain="broadcast",
            proposition_value="true",
            profile=D1Profile(4, 4, 2, 3),
        )
        for observer_id, population, scale in (
            ("individual", "individual", "person"),
            ("family", "family", "household"),
            ("lab", "laboratory", "lab"),
            ("science", "scientific_community", "community"),
            ("institution", "institution", "institution"),
            ("civilization", "civilization", "civilization"),
        )
    )
    return D1FieldScenario(
        name="uniform_broadcast",
        proposition="record_R",
        observer_profiles=profiles,
        edges=_chain_edges("individual", "family", "lab", "science", "institution", "civilization"),
        source_observer="individual",
        target_observer="civilization",
    )


def stratified_access_scenario() -> D1FieldScenario:
    profiles = (
        _observer_profile("individual", "individual", "person", 1, "private", "true", D1Profile(1, 1, 1, 1)),
        _observer_profile("family", "family", "household", 1, "private", "true", D1Profile(2, 2, 1, 1)),
        _observer_profile("lab", "laboratory", "lab", 2, "research", "true", D1Profile(4, 3, 2, 2)),
        _observer_profile("science", "scientific_community", "community", 3, "research", "true", D1Profile(2, 2, 1, 1)),
        _observer_profile("institution", "institution", "institution", 3, "institutional", "unsettled", D1Profile(0, 0, 0, 0)),
        _observer_profile("civilization", "civilization", "civilization", 4, "public", "unsettled", D1Profile(0, 0, 0, 0)),
    )
    edges = (
        FieldEdge("individual", "family", "shared_memory"),
        FieldEdge("family", "lab", "sample_handoff"),
        FieldEdge("lab", "science", "publication"),
        FieldEdge("science", "institution", "policy_review", trust_preserving=False),
        FieldEdge("institution", "civilization", "archive", trust_preserving=False),
    )
    return D1FieldScenario(
        name="stratified_access_delay",
        proposition="record_R",
        observer_profiles=profiles,
        edges=edges,
        source_observer="individual",
        target_observer="civilization",
    )


def connected_transport_scenario() -> D1FieldScenario:
    profiles = _same_profile_transport_sites()
    return D1FieldScenario(
        name="connected_same_vector",
        proposition="record_R",
        observer_profiles=profiles,
        edges=_chain_edges("individual", "family", "lab", "institution"),
        source_observer="individual",
        target_observer="institution",
    )


def partitioned_transport_scenario() -> D1FieldScenario:
    profiles = _same_profile_transport_sites()
    return D1FieldScenario(
        name="partitioned_same_vector",
        proposition="record_R",
        observer_profiles=profiles,
        edges=(
            FieldEdge("individual", "family", "private_channel"),
            FieldEdge("lab", "institution", "institutional_channel"),
        ),
        source_observer="individual",
        target_observer="institution",
    )


def contextual_gluing_scenario() -> D1FieldScenario:
    profiles = (
        _observer_profile("context_a0b0", "lab_context", "lab", 1, "chsh", "same", D1Profile(2, 2, 1, 1)),
        _observer_profile("context_a0b1", "lab_context", "lab", 1, "chsh", "same", D1Profile(2, 2, 1, 1)),
        _observer_profile("context_a1b0", "lab_context", "lab", 1, "chsh", "same", D1Profile(2, 2, 1, 1)),
        _observer_profile("context_a1b1", "lab_context", "lab", 1, "chsh", "different", D1Profile(2, 2, 1, 1)),
    )
    patches = (
        _constraint_patch("A0B0", "context_a0b0", "A0", "B0", "same"),
        _constraint_patch("A0B1", "context_a0b1", "A0", "B1", "same"),
        _constraint_patch("A1B0", "context_a1b0", "A1", "B0", "same"),
        _constraint_patch("A1B1", "context_a1b1", "A1", "B1", "different"),
    )
    return D1FieldScenario(
        name="contextual_gluing_obstruction",
        proposition="record_R",
        observer_profiles=profiles,
        edges=(
            FieldEdge("context_a0b0", "context_a0b1", "shared_setting_A0"),
            FieldEdge("context_a0b0", "context_a1b0", "shared_setting_B0"),
            FieldEdge("context_a0b1", "context_a1b1", "shared_setting_B1"),
            FieldEdge("context_a1b0", "context_a1b1", "shared_setting_A1"),
        ),
        source_observer="context_a0b0",
        target_observer="context_a1b1",
        patches=patches,
    )


def analyze_scenario(scenario: D1FieldScenario) -> ScenarioAnalysis:
    scalar_min = reduce_to_scalar(scenario, "componentwise_min")
    scalar_max = reduce_to_scalar(scenario, "componentwise_max")
    vector = analyze_vector(scenario)
    transport = analyze_transport(scenario)
    gluing = analyze_gluing(scenario)
    representation_needed = _representation_needed(vector, transport, gluing)
    return ScenarioAnalysis(
        scenario=scenario,
        scalar_min=scalar_min,
        scalar_max=scalar_max,
        vector=vector,
        transport=transport,
        gluing=gluing,
        representation_needed=representation_needed,
    )


def reduce_to_scalar(
    scenario: D1FieldScenario,
    rule: str,
    chosen_observer: str | None = None,
) -> ScalarReduction:
    profiles = _profiles(scenario)
    distinct_count = len({profile.as_tuple() for profile in profiles.values()})
    if rule == "chosen_observer":
        if chosen_observer is None:
            raise ValueError("chosen_observer is required for chosen_observer rule")
        profile = profiles[chosen_observer]
        assumptions = (f"observer fixed explicitly: {chosen_observer}",)
        lost = (
            "all other observer profiles",
            "communication topology",
            "gluing constraints",
        )
        return ScalarReduction(rule, profile, False, lost, assumptions)
    if rule == "componentwise_min":
        profile = _componentwise(profiles.values(), min)
        assumptions = ("aggregate by componentwise minimum across observer vector",)
    elif rule == "componentwise_max":
        profile = _componentwise(profiles.values(), max)
        assumptions = ("aggregate by componentwise maximum across observer vector",)
    else:
        raise ValueError(f"unknown scalar reduction rule: {rule}")
    information_lost = []
    if distinct_count > 1:
        information_lost.append("observer profile distribution")
    if scenario.edges and analyze_transport(scenario).field_required:
        information_lost.append("communication and trust graph")
    if scenario.patches:
        information_lost.append("local-to-global gluing data")
    if scenario.edges and not analyze_transport(scenario).field_required:
        assumptions = assumptions + (
            "transport graph is connected by trust-preserving paths",
        )
    return ScalarReduction(
        rule=rule,
        profile=profile,
        recovered_without_loss=not information_lost,
        information_lost=tuple(information_lost),
        assumptions=assumptions,
    )


def analyze_vector(scenario: D1FieldScenario) -> VectorAnalysis:
    vector = tuple(
        (observer.site.observer_id, observer.profile.as_tuple())
        for observer in sorted(
            scenario.observer_profiles, key=lambda item: item.site.observer_id
        )
    )
    distinct_count = len({profile for _, profile in vector})
    vector_required = distinct_count > 1
    reason = (
        "multiple observer populations have different D1 profiles"
        if vector_required
        else "all observer populations share one D1 profile"
    )
    return VectorAnalysis(distinct_count, vector_required, reason, vector)


def analyze_transport(scenario: D1FieldScenario) -> FieldTransportAnalysis:
    graph_connected = _is_connected(
        {profile.site.observer_id for profile in scenario.observer_profiles},
        scenario.edges,
        trust_only=False,
    )
    trust_path_exists = _path_exists(
        scenario.source_observer,
        scenario.target_observer,
        scenario.edges,
        trust_only=True,
    )
    field_required = bool(scenario.edges) and (
        not graph_connected
        or not trust_path_exists
        or any(not edge.trust_preserving for edge in scenario.edges)
    )
    reason = (
        "transport depends on graph connectivity or trust-preserving paths"
        if field_required
        else "the observer vector is connected by trust-preserving transport"
    )
    return FieldTransportAnalysis(
        graph_connected=graph_connected,
        trust_path_exists=trust_path_exists,
        source_observer=scenario.source_observer,
        target_observer=scenario.target_observer,
        field_required=field_required,
        reason=reason,
    )


def analyze_gluing(scenario: D1FieldScenario) -> GluingAnalysis:
    if not scenario.patches:
        return GluingAnalysis(
            local_patches_satisfiable=True,
            global_assignment_exists=True,
            obstruction_detected=False,
            obstruction_kind="none",
            local_witness_count=0,
            global_witness_count=0,
        )
    local_witnesses = sum(
        1 for patch in scenario.patches if _patch_is_satisfiable(patch)
    )
    variables = tuple(sorted({var for patch in scenario.patches for var in patch.variables}))
    global_witness_count = _count_assignments_satisfying(
        variables,
        tuple(
            constraint
            for patch in scenario.patches
            for constraint in patch.constraints
        ),
    )
    all_local = local_witnesses == len(scenario.patches)
    global_exists = global_witness_count > 0
    obstruction = all_local and not global_exists
    return GluingAnalysis(
        local_patches_satisfiable=all_local,
        global_assignment_exists=global_exists,
        obstruction_detected=obstruction,
        obstruction_kind="contextual_finality_obstruction" if obstruction else "none",
        local_witness_count=local_witnesses,
        global_witness_count=global_witness_count,
    )


def compare_vector_to_field(
    left: D1FieldScenario,
    right: D1FieldScenario,
) -> VectorFieldComparison:
    same_vector = analyze_vector(left).vector == analyze_vector(right).vector
    left_transport = analyze_transport(left)
    right_transport = analyze_transport(right)
    same_transport = left_transport.trust_path_exists == right_transport.trust_path_exists
    field_loss = same_vector and not same_transport
    return VectorFieldComparison(
        left=left.name,
        right=right.name,
        same_vector=same_vector,
        same_transport_result=same_transport,
        field_information_lost_by_vector=field_loss,
        reason=(
            "same observer-profile vector has different transport behavior"
            if field_loss
            else "observer vector captures the tested transport distinction"
        ),
    )


def run_t24_lab() -> T24Result:
    scenarios = (
        uniform_broadcast_scenario(),
        stratified_access_scenario(),
        connected_transport_scenario(),
        partitioned_transport_scenario(),
        contextual_gluing_scenario(),
    )
    analyses = tuple(analyze_scenario(scenario) for scenario in scenarios)
    comparison = compare_vector_to_field(
        connected_transport_scenario(),
        partitioned_transport_scenario(),
    )
    uniform = analyses[0]
    stratified = analyses[1]
    contextual = analyses[-1]
    reduction_tests = {
        "scalar_recovered_when_field_uniform": uniform.scalar_min.recovered_without_loss,
        "scalar_loses_observer_distribution_when_profiles_diverge": bool(stratified.scalar_min.information_lost),
        "vector_loses_transport_when_same_vector_has_different_graph": comparison.field_information_lost_by_vector,
        "local_patches_need_not_glue_globally": contextual.gluing.obstruction_detected,
        "current_d1_survives_as_local_stalk": True,
    }
    verdict = {
        "single_global_scalar_sufficient": False,
        "vector_d1_required_for_multiscale_snapshots": True,
        "field_d1_required_for_transport_and_gluing_claims": True,
        "scalar_d1_recoverable_as_special_case": True,
        "replace_existing_d1": False,
        "recommendation_class": "introduce_field_extension",
    }
    return T24Result(
        analyses=analyses,
        vector_field_comparison=comparison,
        reduction_tests=reduction_tests,
        verdict=verdict,
        recommendation=(
            "Retain the existing observer-indexed D1 profile as the local "
            "stalk value. Introduce a field-valued D1 extension for claims "
            "about observer populations, communication transport, scale, time, "
            "and local-to-global gluing. A single scalar is only justified when "
            "an observer is fixed explicitly or the field is uniform."
        ),
    )


def run_t24_analysis() -> dict[str, Any]:
    result = run_t24_lab()
    return {
        "analyses": [_scenario_analysis_to_dict(analysis) for analysis in result.analyses],
        "vector_field_comparison": asdict(result.vector_field_comparison),
        "reduction_tests": result.reduction_tests,
        "verdict": result.verdict,
        "recommendation": result.recommendation,
    }


def _observer_profile(
    observer_id: str,
    population: str,
    scale: str,
    time_step: int,
    trust_domain: str,
    proposition_value: str,
    profile: D1Profile,
) -> ObserverProfile:
    return ObserverProfile(
        site=ObserverSite(observer_id, population, scale, time_step, trust_domain),
        proposition_value=proposition_value,
        profile=profile,
    )


def _chain_edges(*observer_ids: str) -> tuple[FieldEdge, ...]:
    return tuple(
        FieldEdge(left, right, "trusted_transport")
        for left, right in zip(observer_ids, observer_ids[1:])
    )


def _same_profile_transport_sites() -> tuple[ObserverProfile, ...]:
    return tuple(
        _observer_profile(
            observer_id,
            population,
            scale,
            time_step=1,
            trust_domain="transport",
            proposition_value="true",
            profile=D1Profile(2, 2, 1, 1),
        )
        for observer_id, population, scale in (
            ("individual", "individual", "person"),
            ("family", "family", "household"),
            ("lab", "laboratory", "lab"),
            ("institution", "institution", "institution"),
        )
    )


def _constraint_patch(
    patch_id: str,
    observer_id: str,
    left: str,
    right: str,
    relation: str,
) -> FieldPatch:
    return FieldPatch(
        patch_id=patch_id,
        observer_ids=(observer_id,),
        variables=(left, right),
        constraints=(PatchConstraint(left, right, relation),),
    )


def _profiles(scenario: D1FieldScenario) -> dict[str, D1Profile]:
    return {
        observer.site.observer_id: observer.profile
        for observer in scenario.observer_profiles
    }


def _componentwise(values: Any, fn: Any) -> D1Profile:
    tuples = tuple(profile.as_tuple() for profile in values)
    return D1Profile(*(fn(parts) for parts in zip(*tuples)))


def _representation_needed(
    vector: VectorAnalysis,
    transport: FieldTransportAnalysis,
    gluing: GluingAnalysis,
) -> str:
    if gluing.obstruction_detected or transport.field_required:
        return "field"
    if vector.vector_required:
        return "vector"
    return "scalar"


def _is_connected(
    observer_ids: set[str],
    edges: tuple[FieldEdge, ...],
    trust_only: bool,
) -> bool:
    if not observer_ids:
        return True
    start = sorted(observer_ids)[0]
    seen = _reachable(start, edges, trust_only)
    return observer_ids <= seen


def _path_exists(
    source: str,
    target: str,
    edges: tuple[FieldEdge, ...],
    trust_only: bool,
) -> bool:
    return target in _reachable(source, edges, trust_only)


def _reachable(
    source: str,
    edges: tuple[FieldEdge, ...],
    trust_only: bool,
) -> set[str]:
    neighbors: dict[str, set[str]] = {}
    for edge in edges:
        if trust_only and not edge.trust_preserving:
            continue
        neighbors.setdefault(edge.source, set()).add(edge.target)
        neighbors.setdefault(edge.target, set()).add(edge.source)
    seen = {source}
    pending = [source]
    while pending:
        current = pending.pop()
        for neighbor in neighbors.get(current, set()):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append(neighbor)
    return seen


def _patch_is_satisfiable(patch: FieldPatch) -> bool:
    return _count_assignments_satisfying(patch.variables, patch.constraints) > 0


def _count_assignments_satisfying(
    variables: tuple[str, ...],
    constraints: tuple[PatchConstraint, ...],
) -> int:
    count = 0
    unique_variables = tuple(sorted(set(variables)))
    for bits in product((-1, 1), repeat=len(unique_variables)):
        assignment = dict(zip(unique_variables, bits))
        if all(_constraint_satisfied(assignment, constraint) for constraint in constraints):
            count += 1
    return count


def _constraint_satisfied(
    assignment: dict[str, int],
    constraint: PatchConstraint,
) -> bool:
    left = assignment[constraint.left]
    right = assignment[constraint.right]
    if constraint.relation == "same":
        return left == right
    if constraint.relation == "different":
        return left != right
    raise ValueError(f"unknown constraint relation: {constraint.relation}")


def _scenario_analysis_to_dict(analysis: ScenarioAnalysis) -> dict[str, Any]:
    scenario = analysis.scenario
    return {
        "scenario": {
            "name": scenario.name,
            "proposition": scenario.proposition,
            "source_observer": scenario.source_observer,
            "target_observer": scenario.target_observer,
            "observer_profiles": [
                {
                    "site": asdict(observer.site),
                    "proposition_value": observer.proposition_value,
                    "profile": asdict(observer.profile) | {"profile_tuple": list(observer.profile.as_tuple())},
                }
                for observer in scenario.observer_profiles
            ],
            "edges": [asdict(edge) for edge in scenario.edges],
            "patches": [asdict(patch) for patch in scenario.patches],
        },
        "scalar_min": _scalar_to_dict(analysis.scalar_min),
        "scalar_max": _scalar_to_dict(analysis.scalar_max),
        "vector": asdict(analysis.vector),
        "transport": asdict(analysis.transport),
        "gluing": asdict(analysis.gluing),
        "representation_needed": analysis.representation_needed,
    }


def _scalar_to_dict(scalar: ScalarReduction) -> dict[str, Any]:
    return {
        "rule": scalar.rule,
        "profile": asdict(scalar.profile) | {"profile_tuple": list(scalar.profile.as_tuple())},
        "recovered_without_loss": scalar.recovered_without_loss,
        "information_lost": list(scalar.information_lost),
        "assumptions": list(scalar.assumptions),
    }
