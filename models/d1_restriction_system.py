"""T26: finite graph-indexed D1 restriction systems.

T26 formalizes the smallest object selected by T25. It is intentionally finite:
local D1 profiles live on observer sites, transport edges carry trusted
reachability, optional patches carry local-to-global constraints, and morphisms
must preserve declared local and global structure.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from typing import Any, Callable

from models.multiscale_observer_field import (
    D1FieldScenario,
    D1Profile,
    FieldPatch,
    ObserverProfile,
    ObserverSite,
    PatchConstraint,
    connected_transport_scenario,
    contextual_gluing_scenario,
    partitioned_transport_scenario,
    stratified_access_scenario,
    uniform_broadcast_scenario,
)


D1_DIMENSIONS = (
    "accessible_support",
    "holder_redundancy",
    "branch_support",
    "reversal_cost",
)

HYPOTHESES = (
    "H0: informal graph metadata is sufficient",
    "H1: finite graph-indexed D1 restriction system is sufficient",
    "H2: presheaf or sheaf structure is already required",
    "H3: categorical morphism structure is already required for IPT",
    "H4: no canonical formalization is currently justified",
)


@dataclass(frozen=True)
class LocalD1Value:
    site: ObserverSite
    proposition_value: str
    profile: D1Profile


@dataclass(frozen=True)
class TransportEdge:
    source: str
    target: str
    relation: str
    trust_preserving: bool = True


@dataclass(frozen=True)
class OverlapTest:
    left_site: str
    right_site: str
    dimension: str
    relation: str


@dataclass(frozen=True)
class RestrictionPatch:
    patch_id: str
    site_ids: tuple[str, ...]
    variables: tuple[str, ...]
    constraints: tuple[PatchConstraint, ...]


@dataclass(frozen=True)
class D1RestrictionSystem:
    name: str
    proposition: str
    local_values: tuple[LocalD1Value, ...]
    transport_edges: tuple[TransportEdge, ...]
    source_site: str
    target_site: str
    patches: tuple[RestrictionPatch, ...] = ()
    overlap_tests: tuple[OverlapTest, ...] = ()

    def site_ids(self) -> tuple[str, ...]:
        return tuple(value.site.observer_id for value in self.local_values)

    def profile_by_site(self) -> dict[str, D1Profile]:
        return {value.site.observer_id: value.profile for value in self.local_values}

    def value_by_site(self) -> dict[str, LocalD1Value]:
        return {value.site.observer_id: value for value in self.local_values}


@dataclass(frozen=True)
class ValidationResult:
    system: str
    valid: bool
    axiom_checks: dict[str, bool]
    errors: tuple[str, ...]


@dataclass(frozen=True)
class ScalarProjection:
    rule: str
    profile: D1Profile
    recovered_without_loss: bool
    information_lost: tuple[str, ...]
    assumptions: tuple[str, ...]


@dataclass(frozen=True)
class VectorProjection:
    distinct_profile_count: int
    vector_required: bool
    faithful_without_graph: bool
    information_lost: tuple[str, ...]
    vector: tuple[tuple[str, tuple[int, int, int, int]], ...]


@dataclass(frozen=True)
class TransportSummary:
    graph_connected: bool
    trust_path_exists: bool
    non_trust_edges: tuple[tuple[str, str], ...]
    graph_data_required: bool
    reason: str


@dataclass(frozen=True)
class CompatibilityResult:
    local_patches_satisfiable: bool
    overlap_tests_pass: bool
    compatible: bool
    failed_overlap_tests: tuple[OverlapTest, ...]


@dataclass(frozen=True)
class GlobalSectionResult:
    local_patches_satisfiable: bool
    global_assignment_exists: bool
    obstruction_detected: bool
    local_witness_count: int
    global_witness_count: int
    obstruction_kind: str


@dataclass(frozen=True)
class SystemComparison:
    left: str
    right: str
    same_vector: bool
    same_trusted_reachability: bool
    graph_information_lost_by_vector: bool
    reason: str


@dataclass(frozen=True)
class SiteMap:
    source_site: str
    target_site: str


@dataclass(frozen=True)
class D1RestrictionMorphism:
    name: str
    source: D1RestrictionSystem
    target: D1RestrictionSystem
    site_map: tuple[SiteMap, ...]
    preserved_dimensions: tuple[str, ...] = D1_DIMENSIONS
    require_trust_path_preservation: bool = True
    require_obstruction_preservation: bool = True


@dataclass(frozen=True)
class MorphismAnalysis:
    name: str
    site_map_total: bool
    local_profiles_preserved: bool
    trust_path_preserved: bool
    obstruction_status_preserved: bool
    reached: bool
    obstruction: str
    interpretation: str


@dataclass(frozen=True)
class TheoremAttempt:
    name: str
    reached: bool
    level: str
    statement: str
    evidence: tuple[str, ...]
    boundary: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class NegativeResult:
    attempted_claim: str
    what_failed: str
    why_it_failed: str
    reflects: str
    boundary: str


@dataclass(frozen=True)
class IPTReadinessAudit:
    reached: bool
    ready_for_full_representation: bool
    missing_requirements: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T26Result:
    axioms: tuple[str, ...]
    validations: tuple[ValidationResult, ...]
    theorem_ladder: tuple[TheoremAttempt, ...]
    morphism_analyses: tuple[MorphismAnalysis, ...]
    ipt_readiness: IPTReadinessAudit
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    negative_results: tuple[NegativeResult, ...]
    best_supported_hypothesis: str
    recommendation: str


def axioms() -> tuple[str, ...]:
    return (
        "A1 finite unique observer sites",
        "A2 one local D1 profile and proposition value per site",
        "A3 transport edges reference known sites",
        "A4 patches reference known sites and closed finite variables",
        "A5 D1 dimensions are nonnegative integers",
        "A6 compatibility is checked locally before global-section claims",
        "A7 morphisms preserve declared local dimensions and selected global obstructions",
    )


def system_from_scenario(scenario: D1FieldScenario) -> D1RestrictionSystem:
    return D1RestrictionSystem(
        name=scenario.name,
        proposition=scenario.proposition,
        local_values=tuple(
            LocalD1Value(observer.site, observer.proposition_value, observer.profile)
            for observer in scenario.observer_profiles
        ),
        transport_edges=tuple(
            TransportEdge(edge.source, edge.target, edge.relation, edge.trust_preserving)
            for edge in scenario.edges
        ),
        source_site=scenario.source_observer,
        target_site=scenario.target_observer,
        patches=tuple(_patch_from_field_patch(patch) for patch in scenario.patches),
    )


def vector_sufficient_system() -> D1RestrictionSystem:
    profiles = (
        _local_value("individual", "individual", "person", 1, "trusted", "true", D1Profile(1, 1, 1, 1)),
        _local_value("lab", "laboratory", "lab", 1, "trusted", "true", D1Profile(3, 2, 1, 2)),
        _local_value("archive", "institution", "institution", 1, "trusted", "true", D1Profile(5, 3, 2, 3)),
    )
    return D1RestrictionSystem(
        name="vector_sufficient_trusted_chain",
        proposition="record_R",
        local_values=profiles,
        transport_edges=(
            TransportEdge("individual", "lab", "trusted_report"),
            TransportEdge("lab", "archive", "trusted_archive"),
        ),
        source_site="individual",
        target_site="archive",
    )


def relabeled_transport_system(system: D1RestrictionSystem, prefix: str) -> D1RestrictionSystem:
    mapping = {site_id: f"{prefix}_{site_id}" for site_id in system.site_ids()}
    return D1RestrictionSystem(
        name=f"{prefix}_{system.name}",
        proposition=system.proposition,
        local_values=tuple(_rename_local_value(value, mapping[value.site.observer_id]) for value in system.local_values),
        transport_edges=tuple(
            TransportEdge(mapping[edge.source], mapping[edge.target], edge.relation, edge.trust_preserving)
            for edge in system.transport_edges
        ),
        source_site=mapping[system.source_site],
        target_site=mapping[system.target_site],
        patches=tuple(_rename_patch(patch, mapping) for patch in system.patches),
        overlap_tests=tuple(
            OverlapTest(mapping[test.left_site], mapping[test.right_site], test.dimension, test.relation)
            for test in system.overlap_tests
        ),
    )


def validate_system(system: D1RestrictionSystem) -> ValidationResult:
    site_ids = system.site_ids()
    site_set = set(site_ids)
    patch_site_refs = {
        site_id
        for patch in system.patches
        for site_id in patch.site_ids
    }
    patch_constraint_closed = all(
        {constraint.left, constraint.right} <= set(patch.variables)
        for patch in system.patches
        for constraint in patch.constraints
    )
    checks = {
        "finite_unique_sites": len(site_ids) == len(site_set) and len(site_ids) > 0,
        "total_local_profile_assignment": len(system.local_values) == len(site_ids),
        "edge_endpoints_are_sites": all(
            edge.source in site_set and edge.target in site_set
            for edge in system.transport_edges
        ),
        "source_target_are_sites": system.source_site in site_set and system.target_site in site_set,
        "patch_sites_are_sites": patch_site_refs <= site_set,
        "patch_constraints_closed": patch_constraint_closed,
        "nonnegative_d1_dimensions": all(
            all(part >= 0 for part in value.profile.as_tuple())
            for value in system.local_values
        ),
        "overlap_tests_reference_sites": all(
            test.left_site in site_set and test.right_site in site_set
            for test in system.overlap_tests
        ),
    }
    errors = tuple(name for name, passed in checks.items() if not passed)
    return ValidationResult(system.name, all(checks.values()), checks, errors)


def scalar_projection(
    system: D1RestrictionSystem,
    rule: str,
    chosen_site: str | None = None,
) -> ScalarProjection:
    profiles = system.profile_by_site()
    if rule == "chosen_site":
        if chosen_site is None:
            raise ValueError("chosen_site is required for chosen_site projection")
        profile = profiles[chosen_site]
        return ScalarProjection(
            rule=rule,
            profile=profile,
            recovered_without_loss=False,
            information_lost=(
                "other local profiles",
                "transport graph",
                "patch and overlap constraints",
            ),
            assumptions=(f"site fixed explicitly: {chosen_site}",),
        )
    if rule == "componentwise_min":
        profile = _componentwise(profiles.values(), min)
        assumptions = ("aggregate by componentwise minimum across local profiles",)
    elif rule == "componentwise_max":
        profile = _componentwise(profiles.values(), max)
        assumptions = ("aggregate by componentwise maximum across local profiles",)
    else:
        raise ValueError(f"unknown scalar projection rule: {rule}")

    information_lost: list[str] = []
    if len({profile.as_tuple() for profile in profiles.values()}) > 1:
        information_lost.append("observer profile distribution")
    transport = analyze_transport(system)
    if transport.graph_data_required:
        information_lost.append("trusted transport graph")
    if system.patches:
        information_lost.append("local-to-global patch constraints")
    if system.overlap_tests:
        information_lost.append("overlap tests")
    if system.transport_edges and not transport.graph_data_required:
        assumptions = assumptions + ("trusted transport path preserves reachability",)
    return ScalarProjection(
        rule=rule,
        profile=profile,
        recovered_without_loss=not information_lost,
        information_lost=tuple(information_lost),
        assumptions=assumptions,
    )


def vector_projection(system: D1RestrictionSystem) -> VectorProjection:
    vector = tuple(
        (site_id, system.profile_by_site()[site_id].as_tuple())
        for site_id in sorted(system.site_ids())
    )
    distinct_profile_count = len({profile for _, profile in vector})
    information_lost: list[str] = []
    if analyze_transport(system).graph_data_required:
        information_lost.append("trusted transport graph")
    if system.patches:
        information_lost.append("local-to-global patch constraints")
    if system.overlap_tests:
        information_lost.append("overlap tests")
    return VectorProjection(
        distinct_profile_count=distinct_profile_count,
        vector_required=distinct_profile_count > 1,
        faithful_without_graph=not information_lost,
        information_lost=tuple(information_lost),
        vector=vector,
    )


def analyze_transport(system: D1RestrictionSystem) -> TransportSummary:
    site_set = set(system.site_ids())
    graph_connected = _is_connected(site_set, system.transport_edges, trust_only=False)
    trust_path_exists = _path_exists(
        system.source_site,
        system.target_site,
        system.transport_edges,
        trust_only=True,
    )
    non_trust_edges = tuple(
        (edge.source, edge.target)
        for edge in system.transport_edges
        if not edge.trust_preserving
    )
    graph_data_required = bool(system.transport_edges) and (
        not graph_connected
        or not trust_path_exists
        or bool(non_trust_edges)
    )
    reason = (
        "trusted reachability depends on explicit graph data"
        if graph_data_required
        else "trusted transport is connected for the distinguished endpoints"
    )
    return TransportSummary(
        graph_connected=graph_connected,
        trust_path_exists=trust_path_exists,
        non_trust_edges=non_trust_edges,
        graph_data_required=graph_data_required,
        reason=reason,
    )


def analyze_compatibility(system: D1RestrictionSystem) -> CompatibilityResult:
    gluing = global_section(system)
    failed_tests = tuple(
        test for test in system.overlap_tests if not _overlap_test_passes(system, test)
    )
    overlap_tests_pass = not failed_tests
    return CompatibilityResult(
        local_patches_satisfiable=gluing.local_patches_satisfiable,
        overlap_tests_pass=overlap_tests_pass,
        compatible=gluing.local_patches_satisfiable and overlap_tests_pass,
        failed_overlap_tests=failed_tests,
    )


def global_section(system: D1RestrictionSystem) -> GlobalSectionResult:
    if not system.patches:
        return GlobalSectionResult(True, True, False, 0, 0, "none")
    local_witness_count = sum(
        1 for patch in system.patches if _patch_is_satisfiable(patch)
    )
    all_constraints = tuple(
        constraint
        for patch in system.patches
        for constraint in patch.constraints
    )
    variables = tuple(sorted({variable for patch in system.patches for variable in patch.variables}))
    global_witness_count = _count_assignments_satisfying(variables, all_constraints)
    local_satisfiable = local_witness_count == len(system.patches)
    global_exists = global_witness_count > 0
    obstruction = local_satisfiable and not global_exists
    return GlobalSectionResult(
        local_patches_satisfiable=local_satisfiable,
        global_assignment_exists=global_exists,
        obstruction_detected=obstruction,
        local_witness_count=local_witness_count,
        global_witness_count=global_witness_count,
        obstruction_kind="finite_gluing_obstruction" if obstruction else "none",
    )


def compare_systems(left: D1RestrictionSystem, right: D1RestrictionSystem) -> SystemComparison:
    left_vector = vector_projection(left).vector
    right_vector = vector_projection(right).vector
    left_transport = analyze_transport(left)
    right_transport = analyze_transport(right)
    same_vector = left_vector == right_vector
    same_reachability = left_transport.trust_path_exists == right_transport.trust_path_exists
    graph_loss = same_vector and not same_reachability
    return SystemComparison(
        left=left.name,
        right=right.name,
        same_vector=same_vector,
        same_trusted_reachability=same_reachability,
        graph_information_lost_by_vector=graph_loss,
        reason=(
            "same vector has different trusted reachability"
            if graph_loss
            else "vector comparison preserves the tested reachability distinction"
        ),
    )


def analyze_morphism(morphism: D1RestrictionMorphism) -> MorphismAnalysis:
    mapping = {item.source_site: item.target_site for item in morphism.site_map}
    source_sites = set(morphism.source.site_ids())
    target_profiles = morphism.target.profile_by_site()
    source_profiles = morphism.source.profile_by_site()
    site_map_total = source_sites <= set(mapping) and all(
        target_site in target_profiles for target_site in mapping.values()
    )
    local_profiles_preserved = site_map_total and all(
        _profile_dimensions(source_profiles[source_site], target_profiles[mapping[source_site]], morphism.preserved_dimensions)
        for source_site in source_sites
    )
    if morphism.require_trust_path_preservation and site_map_total:
        source_transport = analyze_transport(morphism.source)
        target_trust_path = _path_exists(
            mapping[morphism.source.source_site],
            mapping[morphism.source.target_site],
            morphism.target.transport_edges,
            trust_only=True,
        )
        trust_path_preserved = source_transport.trust_path_exists == target_trust_path
    else:
        trust_path_preserved = True
    if morphism.require_obstruction_preservation:
        obstruction_status_preserved = (
            global_section(morphism.source).obstruction_detected
            == global_section(morphism.target).obstruction_detected
        )
    else:
        obstruction_status_preserved = True
    reached = (
        site_map_total
        and local_profiles_preserved
        and trust_path_preserved
        and obstruction_status_preserved
    )
    obstruction = _morphism_obstruction(
        site_map_total,
        local_profiles_preserved,
        trust_path_preserved,
        obstruction_status_preserved,
    )
    return MorphismAnalysis(
        name=morphism.name,
        site_map_total=site_map_total,
        local_profiles_preserved=local_profiles_preserved,
        trust_path_preserved=trust_path_preserved,
        obstruction_status_preserved=obstruction_status_preserved,
        reached=reached,
        obstruction=obstruction,
        interpretation=(
            "declared local and global D1 restriction data are preserved"
            if reached
            else "morphism is blocked by an explicit preservation failure"
        ),
    )


def positive_relabel_morphism() -> D1RestrictionMorphism:
    source = system_from_scenario(connected_transport_scenario())
    target = relabeled_transport_system(source, "copy")
    return D1RestrictionMorphism(
        name="trusted_transport_relabeling",
        source=source,
        target=target,
        site_map=tuple(
            SiteMap(site_id, f"copy_{site_id}")
            for site_id in source.site_ids()
        ),
    )


def failed_transport_morphism() -> D1RestrictionMorphism:
    source = system_from_scenario(connected_transport_scenario())
    target = system_from_scenario(partitioned_transport_scenario())
    return D1RestrictionMorphism(
        name="connected_to_partitioned_transport",
        source=source,
        target=target,
        site_map=tuple(SiteMap(site_id, site_id) for site_id in source.site_ids()),
    )


def run_t26_lab() -> T26Result:
    uniform = system_from_scenario(uniform_broadcast_scenario())
    vector_case = vector_sufficient_system()
    stratified = system_from_scenario(stratified_access_scenario())
    connected = system_from_scenario(connected_transport_scenario())
    partitioned = system_from_scenario(partitioned_transport_scenario())
    contextual = system_from_scenario(contextual_gluing_scenario())
    systems = (uniform, vector_case, stratified, connected, partitioned, contextual)
    validations = tuple(validate_system(system) for system in systems)
    morphisms = (
        analyze_morphism(positive_relabel_morphism()),
        analyze_morphism(failed_transport_morphism()),
    )
    ipt_readiness = IPTReadinessAudit(
        reached=False,
        ready_for_full_representation=False,
        missing_requirements=(
            "site maps on current IPT objects",
            "restriction-map commutation checks",
            "obstruction preservation across composed IPTs",
            "domain-independent morphism typing",
        ),
        verdict=(
            "T26 defines D1 restriction morphisms, but this is only a readiness "
            "step for IPT representation."
        ),
    )
    theorem_ladder = _theorem_ladder(
        validations,
        uniform,
        vector_case,
        connected,
        partitioned,
        contextual,
        morphisms,
    )
    return T26Result(
        axioms=axioms(),
        validations=validations,
        theorem_ladder=theorem_ladder,
        morphism_analyses=morphisms,
        ipt_readiness=ipt_readiness,
        hypothesis_evaluations=_hypothesis_evaluations(),
        negative_results=_negative_results(stratified, connected, partitioned, contextual),
        best_supported_hypothesis="H1",
        recommendation=(
            "Adopt D1RestrictionSystem as the repo's next formal D1 extension. "
            "Keep scalar D1 as the fixed-site or uniform projection, keep vector "
            "D1 as the observer-distribution projection, use graph and patch "
            "data for transport and gluing claims, and defer full sheaf and "
            "full IPT representation claims until morphism composition is "
            "tested more broadly."
        ),
    )


def run_t26_analysis() -> dict[str, Any]:
    result = run_t26_lab()
    return {
        "axioms": list(result.axioms),
        "validations": [asdict(validation) for validation in result.validations],
        "theorem_ladder": [asdict(attempt) for attempt in result.theorem_ladder],
        "morphism_analyses": [asdict(analysis) for analysis in result.morphism_analyses],
        "ipt_readiness": asdict(result.ipt_readiness),
        "hypotheses": list(HYPOTHESES),
        "hypothesis_evaluations": [asdict(item) for item in result.hypothesis_evaluations],
        "negative_results": [asdict(item) for item in result.negative_results],
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "recommendation": result.recommendation,
        "system_summaries": [_system_summary(system) for system in _t26_systems()],
    }


def _theorem_ladder(
    validations: tuple[ValidationResult, ...],
    uniform: D1RestrictionSystem,
    vector_case: D1RestrictionSystem,
    connected: D1RestrictionSystem,
    partitioned: D1RestrictionSystem,
    contextual: D1RestrictionSystem,
    morphisms: tuple[MorphismAnalysis, ...],
) -> tuple[TheoremAttempt, ...]:
    vector = vector_projection(vector_case)
    connected_partitioned = compare_systems(connected, partitioned)
    contextual_section = global_section(contextual)
    return (
        TheoremAttempt(
            name="Minimal Axiom Sufficiency Theorem",
            reached=all(validation.valid for validation in validations),
            level="axiom",
            statement="The finite axioms validate every T25 scenario used by T26.",
            evidence=tuple(validation.system for validation in validations),
            boundary="finite validation only; no continuous or Lorentz-covariant semantics claimed",
        ),
        TheoremAttempt(
            name="Scalar Recovery Theorem",
            reached=scalar_projection(uniform, "componentwise_min").recovered_without_loss,
            level="projection",
            statement="Scalar D1 is recovered when local profiles are uniform and no transport or gluing data is lost.",
            evidence=(uniform.name,),
            boundary="fails for divergent local profiles or nontrivial patch data",
        ),
        TheoremAttempt(
            name="Vector Recovery Theorem",
            reached=vector.vector_required and vector.faithful_without_graph,
            level="projection",
            statement="Vector D1 is faithful when observer profiles diverge but graph and gluing data add no distinction.",
            evidence=(vector_case.name,),
            boundary="fails when reachability or patch compatibility matters",
        ),
        TheoremAttempt(
            name="Graph Necessity Theorem",
            reached=connected_partitioned.graph_information_lost_by_vector,
            level="transport",
            statement="Graph transport data is necessary when identical vectors have different trusted reachability.",
            evidence=(connected.name, partitioned.name),
            boundary="does not require sheaf language by itself",
        ),
        TheoremAttempt(
            name="Gluing Obstruction Theorem",
            reached=contextual_section.obstruction_detected,
            level="local_to_global",
            statement="Locally satisfiable D1 patches need not admit a global assignment.",
            evidence=(contextual.name,),
            boundary="finite obstruction only; cohomological semantics remain optional",
        ),
        TheoremAttempt(
            name="Restriction Morphism Theorem",
            reached=morphisms[0].reached and not morphisms[1].reached,
            level="morphism",
            statement="A D1 restriction morphism is executable and can distinguish preserved transport from failed transport.",
            evidence=(morphisms[0].name, morphisms[1].name),
            boundary="composition laws and IPT representation are not proved here",
        ),
        TheoremAttempt(
            name="IPT Representation Theorem",
            reached=False,
            level="representation",
            statement="Full IPT representation requires IPTs to carry site maps and restriction-map commutation data.",
            evidence=("T26 morphisms are ready, but current T23 IPT objects are not",),
            boundary="deferred rather than rejected",
        ),
    )


def _hypothesis_evaluations() -> tuple[HypothesisEvaluation, ...]:
    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            claim="Informal graph metadata is sufficient.",
            status="rejected",
            evidence_for=("T25 could name the structure informally",),
            evidence_against=(
                "scalar/vector/transport/gluing checks need typed fields",
                "morphism failure is only visible with explicit site maps",
            ),
            verdict="too weak for the theorem ladder",
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            claim="Finite graph-indexed D1 restriction system is sufficient.",
            status="best_supported",
            evidence_for=(
                "all T25 scenarios validate",
                "scalar and vector projections are executable",
                "transport and gluing failures are detected",
                "positive and failed morphisms are distinguished",
            ),
            evidence_against=("not yet tested on continuous or covariant domains",),
            verdict="best current formal object",
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            claim="Presheaf or sheaf structure is already required.",
            status="not_required_by_current_evidence",
            evidence_for=("gluing obstruction remains sheaf-compatible",),
            evidence_against=("finite patch constraints reproduce the tested obstruction",),
            verdict="defer full sheaf semantics until the finite object fails",
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            claim="Categorical morphism structure is already required for IPT.",
            status="partially_supported_but_deferred",
            evidence_for=("T26 defines executable restriction morphisms",),
            evidence_against=("current IPT objects lack site maps and restriction-map commutation data",),
            verdict="prepare IPT representation work, but do not claim it",
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            claim="No canonical formalization is currently justified.",
            status="not_best_supported",
            evidence_for=("full sheaf and full IPT claims remain unearned",),
            evidence_against=("one finite object reproduces the T25 theorem ladder",),
            verdict="too pessimistic for current finite evidence",
        ),
    )


def _negative_results(
    stratified: D1RestrictionSystem,
    connected: D1RestrictionSystem,
    partitioned: D1RestrictionSystem,
    contextual: D1RestrictionSystem,
) -> tuple[NegativeResult, ...]:
    del stratified
    return (
        NegativeResult(
            attempted_claim="scalar projection is generally faithful",
            what_failed="scalar projection loses observer distribution, graph data, or patch data outside uniform cases",
            why_it_failed="componentwise scalar aggregation has no place to store site-indexed distinctions",
            reflects="mathematical limit of scalar D1 as a global object",
            boundary="scalar D1 remains valid as a local or recovered projection",
        ),
        NegativeResult(
            attempted_claim="vector projection is generally faithful",
            what_failed="identical vectors can differ in trusted reachability",
            why_it_failed=f"{connected.name} and {partitioned.name} have the same vector but different transport",
            reflects="mathematical limit of vector-only D1",
            boundary="vector D1 remains valid for observer-distribution snapshots",
        ),
        NegativeResult(
            attempted_claim="local compatibility implies global section",
            what_failed="local patch witnesses do not globalize",
            why_it_failed=f"{contextual.name} has local witnesses and zero global witnesses",
            reflects="finite local-to-global obstruction",
            boundary="full sheaf language remains optional, not disproved",
        ),
        NegativeResult(
            attempted_claim="current IPT formalism already has full D1 restriction representation",
            what_failed="T23 IPT objects lack site maps and restriction commutation data",
            why_it_failed="T23 was designed for typed invariant transport, not local-to-global morphisms",
            reflects="framework boundary",
            boundary="T26 supplies a target morphism notion for a later IPT upgrade",
        ),
    )


def _t26_systems() -> tuple[D1RestrictionSystem, ...]:
    return (
        system_from_scenario(uniform_broadcast_scenario()),
        vector_sufficient_system(),
        system_from_scenario(stratified_access_scenario()),
        system_from_scenario(connected_transport_scenario()),
        system_from_scenario(partitioned_transport_scenario()),
        system_from_scenario(contextual_gluing_scenario()),
    )


def _system_summary(system: D1RestrictionSystem) -> dict[str, Any]:
    return {
        "name": system.name,
        "site_count": len(system.site_ids()),
        "edge_count": len(system.transport_edges),
        "patch_count": len(system.patches),
        "scalar_min_recovered": scalar_projection(system, "componentwise_min").recovered_without_loss,
        "vector_faithful_without_graph": vector_projection(system).faithful_without_graph,
        "trust_path_exists": analyze_transport(system).trust_path_exists,
        "global_section_exists": global_section(system).global_assignment_exists,
        "obstruction_detected": global_section(system).obstruction_detected,
    }


def _patch_from_field_patch(patch: FieldPatch) -> RestrictionPatch:
    return RestrictionPatch(
        patch_id=patch.patch_id,
        site_ids=patch.observer_ids,
        variables=patch.variables,
        constraints=patch.constraints,
    )


def _local_value(
    observer_id: str,
    population: str,
    scale: str,
    time_step: int,
    trust_domain: str,
    proposition_value: str,
    profile: D1Profile,
) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(observer_id, population, scale, time_step, trust_domain),
        proposition_value=proposition_value,
        profile=profile,
    )


def _rename_local_value(value: LocalD1Value, observer_id: str) -> LocalD1Value:
    site = value.site
    return LocalD1Value(
        site=ObserverSite(observer_id, site.population, site.scale, site.time_step, site.trust_domain),
        proposition_value=value.proposition_value,
        profile=value.profile,
    )


def _rename_patch(patch: RestrictionPatch, mapping: dict[str, str]) -> RestrictionPatch:
    return RestrictionPatch(
        patch_id=patch.patch_id,
        site_ids=tuple(mapping[site_id] for site_id in patch.site_ids),
        variables=patch.variables,
        constraints=patch.constraints,
    )


def _componentwise(values: Any, fn: Callable[[tuple[int, ...]], int]) -> D1Profile:
    tuples = tuple(profile.as_tuple() for profile in values)
    return D1Profile(*(fn(parts) for parts in zip(*tuples)))


def _is_connected(
    site_ids: set[str],
    edges: tuple[TransportEdge, ...],
    trust_only: bool,
) -> bool:
    if not site_ids:
        return True
    start = sorted(site_ids)[0]
    return site_ids <= _reachable(start, edges, trust_only)


def _path_exists(
    source: str,
    target: str,
    edges: tuple[TransportEdge, ...],
    trust_only: bool,
) -> bool:
    return target in _reachable(source, edges, trust_only)


def _reachable(
    source: str,
    edges: tuple[TransportEdge, ...],
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


def _patch_is_satisfiable(patch: RestrictionPatch) -> bool:
    return _count_assignments_satisfying(patch.variables, patch.constraints) > 0


def _count_assignments_satisfying(
    variables: tuple[str, ...],
    constraints: tuple[PatchConstraint, ...],
) -> int:
    unique_variables = tuple(sorted(set(variables)))
    count = 0
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


def _overlap_test_passes(system: D1RestrictionSystem, test: OverlapTest) -> bool:
    values = system.value_by_site()
    left = values[test.left_site]
    right = values[test.right_site]
    if test.dimension == "proposition_value":
        left_value: Any = left.proposition_value
        right_value: Any = right.proposition_value
    elif test.dimension == "profile":
        left_value = left.profile.as_tuple()
        right_value = right.profile.as_tuple()
    elif test.dimension in D1_DIMENSIONS:
        left_value = getattr(left.profile, test.dimension)
        right_value = getattr(right.profile, test.dimension)
    else:
        raise ValueError(f"unknown overlap dimension: {test.dimension}")
    if test.relation == "same":
        return left_value == right_value
    if test.relation == "different":
        return left_value != right_value
    if test.relation == "left_leq_right":
        return left_value <= right_value
    if test.relation == "left_geq_right":
        return left_value >= right_value
    raise ValueError(f"unknown overlap relation: {test.relation}")


def _profile_dimensions(
    source: D1Profile,
    target: D1Profile,
    dimensions: tuple[str, ...],
) -> bool:
    return all(getattr(source, dimension) == getattr(target, dimension) for dimension in dimensions)


def _morphism_obstruction(
    site_map_total: bool,
    local_profiles_preserved: bool,
    trust_path_preserved: bool,
    obstruction_status_preserved: bool,
) -> str:
    if not site_map_total:
        return "site_map_incomplete"
    if not local_profiles_preserved:
        return "local_profile_mismatch"
    if not trust_path_preserved:
        return "trust_path_not_preserved"
    if not obstruction_status_preserved:
        return "global_obstruction_not_preserved"
    return "none"


def _observer_profile(value: LocalD1Value) -> ObserverProfile:
    return ObserverProfile(value.site, value.proposition_value, value.profile)
