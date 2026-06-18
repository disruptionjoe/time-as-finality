"""T23: invariant-preserving transformations kernel.

An invariant-preserving transformation (IPT) is modeled here as a typed map
between finite structures:

    IPT = (source, target, transformation map, preserved invariants,
           allowed losses, obstruction conditions)

The point of T23 is not to claim that all domains are equivalent. It tests
whether the same finite interface can express observer access restriction,
consensus-record theorem transfer, and quantum measurement redundancy
extraction without flattening their differences.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.consensus_record_theorem_transfer import (
    analyze_certificate_system,
    transfer_quorum_intersection_theorem,
    weak_quorum_boundary_system,
)
from models.quantum_measurement_finality import run_measurement_finality_lab


RELATIONSHIP_LEVELS = ("analogy", "homology", "reduction", "equivalence")
INDEPENDENCE_LEVELS = (
    "not independent",
    "proto-independent",
    "repo-ready",
    "publishable-kernel",
)


@dataclass(frozen=True)
class TypedInvariant:
    name: str
    value: Any
    value_type: str
    description: str


@dataclass(frozen=True)
class StructuredObject:
    name: str
    domain: str
    structure_type: str
    invariants: tuple[TypedInvariant, ...]

    def invariant_value(self, name: str) -> Any:
        for invariant in self.invariants:
            if invariant.name == name:
                return invariant.value
        raise KeyError(f"{self.name} has no invariant named {name}")

    def invariant_names(self) -> frozenset[str]:
        return frozenset(invariant.name for invariant in self.invariants)


@dataclass(frozen=True)
class ObstructionCondition:
    name: str
    invariant: str
    triggered: bool
    reason: str


@dataclass(frozen=True)
class InvariantCheck:
    invariant: str
    source_value: Any
    target_value: Any
    preserved: bool
    reason: str


@dataclass(frozen=True)
class InvariantPreservingTransformation:
    name: str
    source: StructuredObject
    target: StructuredObject
    transformation_map: str
    relationship_class: str
    preserved_invariants: tuple[str, ...]
    allowed_losses: tuple[str, ...]
    obstruction_conditions: tuple[ObstructionCondition, ...]


@dataclass(frozen=True)
class IPTAnalysis:
    transformation: InvariantPreservingTransformation
    invariant_checks: tuple[InvariantCheck, ...]
    all_declared_invariants_preserved: bool
    triggered_obstructions: tuple[ObstructionCondition, ...]


@dataclass(frozen=True)
class CompositionResult:
    first: str
    second: str
    source: str
    intermediate: str
    target: str
    requested_invariants: tuple[str, ...]
    source_target_match: bool
    triggered_obstructions: tuple[ObstructionCondition, ...]
    invariant_checks: tuple[InvariantCheck, ...]
    composition_preserves_requested_invariants: bool
    theorem_status: str


@dataclass(frozen=True)
class T23Result:
    taxonomy: dict[str, str]
    transformations: tuple[IPTAnalysis, ...]
    composition_results: tuple[CompositionResult, ...]
    verdict: dict[str, bool | str]
    recommendation: str


def relationship_taxonomy() -> dict[str, str]:
    return {
        "analogy": "Surface similarity. It suggests a comparison but carries no proof obligation.",
        "homology": "Shared formal structure or proof pattern under typed assumptions.",
        "reduction": "The target structure is obtained from the source by an explicit map that preserves named invariants and loses declared quantities.",
        "equivalence": "Two structures preserve each other's named invariants under inverse maps. T23 does not establish any equivalence case.",
    }


def observer_access_transformation() -> InvariantPreservingTransformation:
    result = run_measurement_finality_lab()
    final_stage = result.stages[-1]
    local_lab = _observer_analysis(final_stage, "local_lab_observer")
    source = StructuredObject(
        name="t2_final_global_measurement_state",
        domain="quantum_measurement",
        structure_type="global_entangled_record_state",
        invariants=(
            _inv("pointer_basis", result.pointer_basis, "str", "Declared pointer basis."),
            _inv(
                "system_record_correlation",
                "perfect_z_correlation",
                "str",
                "All record qubits are perfectly Z-correlated with S.",
            ),
            _inv(
                "decohered_pointer",
                final_stage.pointer_coherence_abs == 0.0,
                "bool",
                "Reduced S-A pointer coherence is zero.",
            ),
            _inv(
                "environment_r_delta_total",
                final_stage.environment_r_delta_total,
                "int",
                "Total informative environment fragments.",
            ),
        ),
    )
    target = StructuredObject(
        name="t2_local_lab_d1_view",
        domain="observer_access",
        structure_type="observer_indexed_d1_profile",
        invariants=(
            _inv("pointer_basis", result.pointer_basis, "str", "Pointer basis survives access restriction."),
            _inv(
                "system_record_correlation",
                "perfect_z_correlation",
                "str",
                "Accessible records still carry the same Z-correlation type.",
            ),
            _inv("accessible_support", local_lab.d1_profile.accessible_support, "int", "Accessible supporting records."),
            _inv("holder_redundancy", local_lab.d1_profile.holder_redundancy, "int", "Distinct accessible holders."),
            _inv("branch_support", local_lab.d1_profile.branch_support, "int", "Distinct accessible branch roots."),
            _inv(
                "accessible_environment_r_delta",
                local_lab.accessible_environment_r_delta,
                "int",
                "Informative environment fragments inside local access.",
            ),
        ),
    )
    return InvariantPreservingTransformation(
        name="observer_access_restriction",
        source=source,
        target=target,
        transformation_map="restrict global measurement records to local_lab_observer access window",
        relationship_class="reduction",
        preserved_invariants=("pointer_basis", "system_record_correlation"),
        allowed_losses=("environment_r_delta_total", "inaccessible_records", "global_state_amplitudes"),
        obstruction_conditions=(
            ObstructionCondition(
                "empty_access_window",
                "system_record_correlation",
                False,
                "The local_lab_observer has apparatus and E1 access.",
            ),
        ),
    )


def consensus_record_theorem_transfer_ipt() -> InvariantPreservingTransformation:
    transfer = transfer_quorum_intersection_theorem()
    consensus = transfer.consensus_analysis
    record = transfer.record_analysis
    source = _certificate_analysis_structure(
        "consensus_majority_safety_structure",
        "distributed_consensus",
        "quorum_certificate_system",
        consensus,
    )
    target = _certificate_analysis_structure(
        "record_majority_safety_structure",
        "physical_record_finality",
        "record_certificate_system",
        record,
    )
    return InvariantPreservingTransformation(
        name="consensus_record_quorum_safety_transfer",
        source=source,
        target=target,
        transformation_map="typed theorem transfer from quorum certificates to record certificates",
        relationship_class="homology",
        preserved_invariants=(
            "holder_count",
            "quorum_threshold",
            "quorum_intersection_safety",
            "conflict_exclusion",
        ),
        allowed_losses=("protocol_rounds", "engineered_messages", "byzantine_intent"),
        obstruction_conditions=(
            ObstructionCondition(
                "weak_quorum",
                "quorum_intersection_safety",
                False,
                "The positive transfer has n=5 and q=3, so 2q > n.",
            ),
        ),
    )


def quantum_redundancy_reduction_ipt() -> InvariantPreservingTransformation:
    result = run_measurement_finality_lab()
    final_stage = result.stages[-1]
    local_lab = _observer_analysis(final_stage, "local_lab_observer")
    source = StructuredObject(
        name="t2_local_lab_d1_view",
        domain="observer_access",
        structure_type="observer_indexed_d1_profile",
        invariants=(
            _inv("pointer_basis", result.pointer_basis, "str", "Pointer basis inherited from T2."),
            _inv("holder_redundancy", local_lab.d1_profile.holder_redundancy, "int", "Dynamically generated accessible holders."),
            _inv("accessible_support", local_lab.d1_profile.accessible_support, "int", "Dynamically generated accessible support."),
            _inv("branch_support", local_lab.d1_profile.branch_support, "int", "One pointer-measurement root."),
            _inv("observer_access_indexed", True, "bool", "The profile is observer-window indexed."),
        ),
    )
    target = StructuredObject(
        name="t22_reduction_schema_view",
        domain="d1_physical_reduction_map",
        structure_type="observable_reduction_schema",
        invariants=(
            _inv("pointer_basis", result.pointer_basis, "str", "Pointer basis required by the redundancy observable."),
            _inv("holder_redundancy", 2, "int", "Observable holder redundancy for local access."),
            _inv("accessible_support", 2, "int", "Accessible support under the same local window."),
            _inv("observer_access_indexed", True, "bool", "T22 observables are evaluated per observer access boundary."),
        ),
    )
    return InvariantPreservingTransformation(
        name="quantum_measurement_to_reduction_schema",
        source=source,
        target=target,
        transformation_map="extract T22 observable schema from T2 local_lab D1 profile",
        relationship_class="reduction",
        preserved_invariants=(
            "pointer_basis",
            "holder_redundancy",
            "accessible_support",
            "observer_access_indexed",
        ),
        allowed_losses=("unitary_history", "global_amplitudes", "decoherence_timeline", "branch_support_detail"),
        obstruction_conditions=(
            ObstructionCondition(
                "no_fragment_partition",
                "holder_redundancy",
                False,
                "The T2 local lab access window names apparatus and env_left holders.",
            ),
        ),
    )


def weak_quorum_obstruction_ipt() -> InvariantPreservingTransformation:
    weak = analyze_certificate_system(weak_quorum_boundary_system())
    source = _certificate_analysis_structure(
        "record_majority_safety_structure",
        "physical_record_finality",
        "record_certificate_system",
        transfer_quorum_intersection_theorem().record_analysis,
    )
    target = _certificate_analysis_structure(
        "weak_quorum_record_boundary",
        "physical_record_finality",
        "record_certificate_system",
        weak,
    )
    return InvariantPreservingTransformation(
        name="record_safety_to_weak_quorum_boundary",
        source=source,
        target=target,
        transformation_map="weaken record quorum threshold until disjoint conflicts become possible",
        relationship_class="analogy",
        preserved_invariants=("holder_count", "quorum_intersection_safety"),
        allowed_losses=("conflict_exclusion", "theorem_applicability"),
        obstruction_conditions=(
            ObstructionCondition(
                "weak_quorum",
                "quorum_intersection_safety",
                True,
                "The boundary has n=4 and q=2, so 2q > n is false.",
            ),
        ),
    )


def analyze_ipt(
    transformation: InvariantPreservingTransformation,
) -> IPTAnalysis:
    checks = tuple(
        _check_invariant(transformation.source, transformation.target, name)
        for name in transformation.preserved_invariants
    )
    triggered = tuple(
        condition
        for condition in transformation.obstruction_conditions
        if condition.triggered
    )
    return IPTAnalysis(
        transformation=transformation,
        invariant_checks=checks,
        all_declared_invariants_preserved=all(check.preserved for check in checks)
        and not triggered,
        triggered_obstructions=triggered,
    )


def compose_ipts(
    first: InvariantPreservingTransformation,
    second: InvariantPreservingTransformation,
    requested_invariants: tuple[str, ...],
) -> CompositionResult:
    source_target_match = first.target.name == second.source.name
    triggered = tuple(
        condition
        for condition in first.obstruction_conditions + second.obstruction_conditions
        if condition.triggered
    )
    checks = tuple(
        _composition_check(first, second, invariant)
        for invariant in requested_invariants
    )
    preserves = (
        source_target_match
        and not triggered
        and all(check.preserved for check in checks)
    )
    theorem_status = (
        "composition_preserves_requested_invariants"
        if preserves
        else "composition_blocked_by_obstruction"
        if triggered
        else "composition_not_applicable"
    )
    return CompositionResult(
        first=first.name,
        second=second.name,
        source=first.source.name,
        intermediate=first.target.name,
        target=second.target.name,
        requested_invariants=requested_invariants,
        source_target_match=source_target_match,
        triggered_obstructions=triggered,
        invariant_checks=checks,
        composition_preserves_requested_invariants=preserves,
        theorem_status=theorem_status,
    )


def run_t23_lab() -> T23Result:
    transformations = (
        observer_access_transformation(),
        consensus_record_theorem_transfer_ipt(),
        quantum_redundancy_reduction_ipt(),
        weak_quorum_obstruction_ipt(),
    )
    analyses = tuple(analyze_ipt(transformation) for transformation in transformations)
    composition_success = compose_ipts(
        transformations[0],
        transformations[2],
        ("pointer_basis",),
    )
    composition_obstruction = compose_ipts(
        transformations[1],
        transformations[3],
        ("quorum_intersection_safety",),
    )
    positive_case_count = sum(
        1 for analysis in analyses if analysis.all_declared_invariants_preserved
    )
    same_interface_three_domains = positive_case_count >= 3
    composition_law_executable = (
        composition_success.composition_preserves_requested_invariants
        and composition_obstruction.theorem_status == "composition_blocked_by_obstruction"
    )
    equivalence_claimed = any(
        analysis.transformation.relationship_class == "equivalence"
        for analysis in analyses
    )
    return T23Result(
        taxonomy=relationship_taxonomy(),
        transformations=analyses,
        composition_results=(composition_success, composition_obstruction),
        verdict={
            "typed_ipt_definition_exists": True,
            "same_interface_expresses_three_domains": same_interface_three_domains,
            "composition_law_executable": composition_law_executable,
            "obstruction_condition_executable": bool(composition_obstruction.triggered_obstructions),
            "taxonomy_includes_all_four_levels": set(relationship_taxonomy()) == set(RELATIONSHIP_LEVELS),
            "no_equivalence_claimed": not equivalence_claimed,
            "mathematical_independence": "proto-independent",
        },
        recommendation=(
            "IPT is proto-independent: the same typed interface expresses "
            "observer access restriction, consensus-record theorem transfer, "
            "and quantum redundancy extraction, and a finite composition "
            "theorem is executable. Keep incubating inside Time as Finality "
            "until IPT has a stronger representation theorem and at least one "
            "domain not inherited from the TaF test suite."
        ),
    )


def run_t23_analysis() -> dict[str, Any]:
    result = run_t23_lab()
    return {
        "taxonomy": result.taxonomy,
        "transformations": [
            _analysis_to_dict(analysis) for analysis in result.transformations
        ],
        "composition_results": [
            _composition_to_dict(composition)
            for composition in result.composition_results
        ],
        "verdict": result.verdict,
        "recommendation": result.recommendation,
    }


def _certificate_analysis_structure(
    name: str,
    domain: str,
    structure_type: str,
    analysis: Any,
) -> StructuredObject:
    return StructuredObject(
        name=name,
        domain=domain,
        structure_type=structure_type,
        invariants=(
            _inv("holder_count", len(analysis.system.holders), "int", "Finite holder set cardinality."),
            _inv("quorum_threshold", analysis.system.quorum_threshold, "int", "Certificate threshold."),
            _inv(
                "quorum_intersection_safety",
                analysis.quorum_intersection_assumption,
                "bool",
                "The condition 2q > n holds.",
            ),
            _inv(
                "conflict_exclusion",
                analysis.theorem_blocks_all_conflicts,
                "bool",
                "Typed incompatible certificates are blocked.",
            ),
        ),
    )


def _observer_analysis(stage: Any, name: str) -> Any:
    for observer in stage.observers:
        if observer.observer.name == name:
            return observer
    raise ValueError(f"unknown observer: {name}")


def _inv(name: str, value: Any, value_type: str, description: str) -> TypedInvariant:
    return TypedInvariant(name, value, value_type, description)


def _check_invariant(
    source: StructuredObject, target: StructuredObject, name: str
) -> InvariantCheck:
    try:
        source_value = source.invariant_value(name)
        target_value = target.invariant_value(name)
    except KeyError as error:
        return InvariantCheck(
            name,
            "missing",
            "missing",
            False,
            str(error),
        )
    preserved = source_value == target_value
    return InvariantCheck(
        name,
        source_value,
        target_value,
        preserved,
        "source and target values match" if preserved else "source and target values diverge",
    )


def _composition_check(
    first: InvariantPreservingTransformation,
    second: InvariantPreservingTransformation,
    invariant: str,
) -> InvariantCheck:
    if invariant not in first.preserved_invariants or invariant not in second.preserved_invariants:
        return InvariantCheck(
            invariant,
            "not declared",
            "not declared",
            False,
            "requested invariant is not preserved by both component IPTs",
        )
    try:
        source_value = first.source.invariant_value(invariant)
        target_value = second.target.invariant_value(invariant)
    except KeyError as error:
        return InvariantCheck(
            invariant,
            "missing",
            "missing",
            False,
            str(error),
        )
    preserved = source_value == target_value
    return InvariantCheck(
        invariant,
        source_value,
        target_value,
        preserved,
        "composite source and target values match" if preserved else "composite endpoints diverge",
    )


def _analysis_to_dict(analysis: IPTAnalysis) -> dict[str, Any]:
    transformation = analysis.transformation
    return {
        "name": transformation.name,
        "relationship_class": transformation.relationship_class,
        "transformation_map": transformation.transformation_map,
        "source": _structure_to_dict(transformation.source),
        "target": _structure_to_dict(transformation.target),
        "preserved_invariants": list(transformation.preserved_invariants),
        "allowed_losses": list(transformation.allowed_losses),
        "invariant_checks": [asdict(check) for check in analysis.invariant_checks],
        "obstruction_conditions": [
            asdict(condition) for condition in transformation.obstruction_conditions
        ],
        "triggered_obstructions": [
            asdict(condition) for condition in analysis.triggered_obstructions
        ],
        "all_declared_invariants_preserved": analysis.all_declared_invariants_preserved,
    }


def _structure_to_dict(structure: StructuredObject) -> dict[str, Any]:
    return {
        "name": structure.name,
        "domain": structure.domain,
        "structure_type": structure.structure_type,
        "invariants": [asdict(invariant) for invariant in structure.invariants],
    }


def _composition_to_dict(composition: CompositionResult) -> dict[str, Any]:
    return {
        "first": composition.first,
        "second": composition.second,
        "source": composition.source,
        "intermediate": composition.intermediate,
        "target": composition.target,
        "requested_invariants": list(composition.requested_invariants),
        "source_target_match": composition.source_target_match,
        "triggered_obstructions": [
            asdict(condition) for condition in composition.triggered_obstructions
        ],
        "invariant_checks": [asdict(check) for check in composition.invariant_checks],
        "composition_preserves_requested_invariants": composition.composition_preserves_requested_invariants,
        "theorem_status": composition.theorem_status,
    }
