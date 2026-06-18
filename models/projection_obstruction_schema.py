"""T29: Projection-Obstruction Schema formalization.

This module turns the T27 stretch result into a reusable finite schema over
D1RestrictionSystem pairs. It does not model the underlying physics of any
source theorem. It only checks finite projection, forgotten structure,
local-to-global obstruction, and definability.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    MorphismAnalysis,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    ValidationResult,
    analyze_morphism,
    global_section,
    validate_system,
)
from models.gu_class_relative_bridge import (
    BridgeCase,
    distler_garibaldi_bridge_case,
    nielsen_ninomiya_bridge_case,
    witten_bridge_case,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint


SCHEMA_OUTCOMES = (
    "faithful_projection_obstruction",
    "lossy_projection_no_new_obstruction",
    "shared_obstruction_not_projection_created",
    "non_definable_projection",
)


@dataclass(frozen=True)
class ProjectionCase:
    name: str
    source: str
    richer_system: D1RestrictionSystem
    restricted_system: D1RestrictionSystem
    morphism: D1RestrictionMorphism
    forgotten_structure: tuple[str, ...]
    preserved_structure: tuple[str, ...]
    intended_reading: str


@dataclass(frozen=True)
class ProjectionObstructionSchema:
    name: str
    projection_definable: bool
    richer_obstructed: bool
    restricted_obstructed: bool
    obstruction_created_by_projection: bool
    projection_loses_structure: bool
    morphism_reaches_target: bool
    outcome: str
    schema_instance: bool
    boundary: str


@dataclass(frozen=True)
class ProjectionCaseAnalysis:
    case: ProjectionCase
    richer_validation: ValidationResult
    restricted_validation: ValidationResult
    morphism_analysis: MorphismAnalysis
    schema: ProjectionObstructionSchema
    verdict: str


@dataclass(frozen=True)
class SchemaTheoremAttempt:
    name: str
    reached: bool
    statement: str
    evidence: tuple[str, ...]
    boundary: str


@dataclass(frozen=True)
class NamedClaimDecision:
    create_named_claim: bool
    proposed_id: str
    status: str
    reason: str
    non_claims: tuple[str, ...]


@dataclass(frozen=True)
class T29Result:
    analyses: tuple[ProjectionCaseAnalysis, ...]
    theorem_attempts: tuple[SchemaTheoremAttempt, ...]
    named_claim_decision: NamedClaimDecision
    recommendation: str


def projection_case_from_bridge_case(case: BridgeCase) -> ProjectionCase:
    return ProjectionCase(
        name=case.name,
        source="T27",
        richer_system=case.richer_system,
        restricted_system=case.restricted_system,
        morphism=case.morphism,
        forgotten_structure=case.forgotten_structure,
        preserved_structure=case.preserved_structure,
        intended_reading=case.bridge_verdict,
    )


def synthetic_lossy_no_obstruction_case() -> ProjectionCase:
    richer = D1RestrictionSystem(
        name="synthetic_rich_extra_witness",
        proposition="record_R",
        local_values=(
            _local("rich_A", "rich", "true", D1Profile(2, 2, 1, 1)),
            _local("rich_B", "rich", "true", D1Profile(3, 2, 1, 1)),
        ),
        transport_edges=(TransportEdge("rich_A", "rich_B", "trusted_projection"),),
        source_site="rich_A",
        target_site="rich_B",
        patches=(
            RestrictionPatch(
                "rich_consistency",
                ("rich_A", "rich_B"),
                ("x", "y"),
                (PatchConstraint("x", "y", "same"),),
            ),
        ),
    )
    restricted = D1RestrictionSystem(
        name="synthetic_projected_no_obstruction",
        proposition="record_R",
        local_values=(
            _local("restricted_A", "restricted", "true", D1Profile(1, 1, 0, 1)),
            _local("restricted_B", "restricted", "true", D1Profile(1, 1, 0, 1)),
        ),
        transport_edges=(TransportEdge("restricted_A", "restricted_B", "trusted_projection"),),
        source_site="restricted_A",
        target_site="restricted_B",
        patches=(
            RestrictionPatch(
                "restricted_consistency",
                ("restricted_A", "restricted_B"),
                ("x", "y"),
                (PatchConstraint("x", "y", "same"),),
            ),
        ),
    )
    morphism = D1RestrictionMorphism(
        name="synthetic_forget_extra_witness",
        source=richer,
        target=restricted,
        site_map=(SiteMap("rich_A", "restricted_A"), SiteMap("rich_B", "restricted_B")),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )
    return ProjectionCase(
        name="synthetic_lossy_no_obstruction",
        source="synthetic",
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=(
            "extra accessible support",
            "extra holder redundancy",
            "branch witness not represented in restricted class",
        ),
        preserved_structure=("reversal_cost", "trusted path", "global satisfiability"),
        intended_reading=(
            "Projection exists and loses structure, but no obstruction appears. "
            "This is not a Projection-Obstruction Schema instance."
        ),
    )


def synthetic_shared_obstruction_case() -> ProjectionCase:
    richer = _three_patch_obstructed_system("rich_shared", D1Profile(2, 2, 1, 1))
    restricted = _three_patch_obstructed_system("restricted_shared", D1Profile(1, 1, 0, 1))
    morphism = D1RestrictionMorphism(
        name="synthetic_obstruction_preserving_projection",
        source=richer,
        target=restricted,
        site_map=(
            SiteMap("rich_shared_A", "restricted_shared_A"),
            SiteMap("rich_shared_B", "restricted_shared_B"),
            SiteMap("rich_shared_C", "restricted_shared_C"),
        ),
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=True,
        require_obstruction_preservation=True,
    )
    return ProjectionCase(
        name="synthetic_shared_obstruction",
        source="synthetic",
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=("support and branch detail",),
        preserved_structure=("obstruction status", "trusted path", "reversal_cost"),
        intended_reading=(
            "Projection exists, but the obstruction is already present in the "
            "richer system. Projection does not create the obstruction."
        ),
    )


def analyze_projection_case(case: ProjectionCase) -> ProjectionCaseAnalysis:
    richer_validation = validate_system(case.richer_system)
    restricted_validation = validate_system(case.restricted_system)
    morphism_analysis = analyze_morphism(case.morphism)
    richer_section = global_section(case.richer_system)
    restricted_section = global_section(case.restricted_system)
    projection_definable = morphism_analysis.site_map_total
    obstruction_created = (
        projection_definable
        and not richer_section.obstruction_detected
        and restricted_section.obstruction_detected
    )
    projection_loses_structure = bool(case.forgotten_structure) or not morphism_analysis.local_profiles_preserved
    if not projection_definable:
        outcome = "non_definable_projection"
        boundary = "site map incomplete or category change"
    elif obstruction_created:
        outcome = "faithful_projection_obstruction"
        boundary = "positive finite schema instance"
    elif not richer_section.obstruction_detected and not restricted_section.obstruction_detected:
        outcome = "lossy_projection_no_new_obstruction"
        boundary = "projection may be lossy without producing a no-go obstruction"
    elif richer_section.obstruction_detected and restricted_section.obstruction_detected:
        outcome = "shared_obstruction_not_projection_created"
        boundary = "obstruction is inherited rather than created by projection"
    else:
        outcome = "lossy_projection_no_new_obstruction"
        boundary = "mixed case outside the positive schema"
    schema = ProjectionObstructionSchema(
        name=f"{case.name}_schema",
        projection_definable=projection_definable,
        richer_obstructed=richer_section.obstruction_detected,
        restricted_obstructed=restricted_section.obstruction_detected,
        obstruction_created_by_projection=obstruction_created,
        projection_loses_structure=projection_loses_structure,
        morphism_reaches_target=morphism_analysis.reached,
        outcome=outcome,
        schema_instance=outcome == "faithful_projection_obstruction",
        boundary=boundary,
    )
    return ProjectionCaseAnalysis(
        case=case,
        richer_validation=richer_validation,
        restricted_validation=restricted_validation,
        morphism_analysis=morphism_analysis,
        schema=schema,
        verdict=_verdict_for_schema(case.name, schema),
    )


def run_t29_schema_lab() -> T29Result:
    cases = (
        projection_case_from_bridge_case(witten_bridge_case()),
        projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()),
        projection_case_from_bridge_case(distler_garibaldi_bridge_case()),
        synthetic_lossy_no_obstruction_case(),
        synthetic_shared_obstruction_case(),
    )
    analyses = tuple(analyze_projection_case(case) for case in cases)
    theorem_attempts = _theorem_attempts(analyses)
    named_claim_decision = NamedClaimDecision(
        create_named_claim=True,
        proposed_id="PO1",
        status="partially_supported",
        reason=(
            "T29 supplies a finite object, two positive inherited examples, "
            "one non-definable inherited boundary, and two synthetic boundary "
            "tests. The claim is narrow enough to track without implying a "
            "physics theorem."
        ),
        non_claims=(
            "PO1 does not prove any original physics no-go theorem.",
            "PO1 does not show that Time as Finality proves GU or that GU proves Time as Finality.",
            "PO1 does not replace the source mathematical proofs.",
            "PO1 is finite and class-relative, not a continuous or category-level theorem.",
        ),
    )
    return T29Result(
        analyses=analyses,
        theorem_attempts=theorem_attempts,
        named_claim_decision=named_claim_decision,
        recommendation=(
            "Promote Projection-Obstruction to a named formal schema claim "
            "PO1 with partially_supported status. The supported theorem is "
            "finite and class-relative: when a definable projection forgets "
            "obstruction-resolving data and maps a globally satisfiable richer "
            "system to an obstructed restricted system, the restricted no-go "
            "is faithfully represented as a projection-created gluing "
            "obstruction. Non-definable projections and inherited obstructions "
            "are explicit boundary cases."
        ),
    )


def run_t29_analysis() -> dict[str, Any]:
    result = run_t29_schema_lab()
    return {
        "outcomes": list(SCHEMA_OUTCOMES),
        "analyses": [_analysis_to_dict(analysis) for analysis in result.analyses],
        "theorem_attempts": [asdict(attempt) for attempt in result.theorem_attempts],
        "named_claim_decision": asdict(result.named_claim_decision),
        "recommendation": result.recommendation,
    }


def _theorem_attempts(
    analyses: tuple[ProjectionCaseAnalysis, ...],
) -> tuple[SchemaTheoremAttempt, ...]:
    by_name = {analysis.case.name: analysis for analysis in analyses}
    positive = tuple(
        analysis.case.name
        for analysis in analyses
        if analysis.schema.schema_instance
    )
    non_definable = tuple(
        analysis.case.name
        for analysis in analyses
        if analysis.schema.outcome == "non_definable_projection"
    )
    no_obstruction = by_name["synthetic_lossy_no_obstruction"]
    shared = by_name["synthetic_shared_obstruction"]
    return (
        SchemaTheoremAttempt(
            name="Positive Projection-Obstruction Schema",
            reached=set(positive) >= {"witten_1981", "nielsen_ninomiya"},
            statement=(
                "A site-map-complete projection from a globally satisfiable "
                "richer system to an obstructed restricted system is a finite "
                "Projection-Obstruction instance when the projection loses "
                "obstruction-resolving structure."
            ),
            evidence=positive,
            boundary="finite abstraction only; no source physics theorem is reproved",
        ),
        SchemaTheoremAttempt(
            name="Non-Definable Projection Boundary",
            reached="distler_garibaldi" in non_definable,
            statement=(
                "If the site map is incomplete, the bridge is not a lossy "
                "projection but a category-change boundary for T26."
            ),
            evidence=non_definable,
            boundary="may require presheaf, sheaf, or category-level morphisms",
        ),
        SchemaTheoremAttempt(
            name="Loss Without Obstruction Counterexample",
            reached=no_obstruction.schema.outcome == "lossy_projection_no_new_obstruction",
            statement=(
                "A projection can forget structure without creating a gluing "
                "obstruction."
            ),
            evidence=(no_obstruction.case.name,),
            boundary="loss alone is insufficient for the positive schema",
        ),
        SchemaTheoremAttempt(
            name="Inherited Obstruction Counterexample",
            reached=shared.schema.outcome == "shared_obstruction_not_projection_created",
            statement=(
                "A restricted obstruction is not projection-created when the "
                "richer system is already obstructed."
            ),
            evidence=(shared.case.name,),
            boundary="shared obstruction does not support class-relative projection explanation",
        ),
    )


def _local(site_id: str, population: str, value: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(site_id, population, "finite_site", 0, "schema"),
        proposition_value=value,
        profile=profile,
    )


def _three_patch_obstructed_system(prefix: str, profile: D1Profile) -> D1RestrictionSystem:
    return D1RestrictionSystem(
        name=f"{prefix}_obstructed",
        proposition="record_R",
        local_values=(
            _local(f"{prefix}_A", prefix, "restricted", profile),
            _local(f"{prefix}_B", prefix, "restricted", profile),
            _local(f"{prefix}_C", prefix, "restricted", profile),
        ),
        transport_edges=(
            TransportEdge(f"{prefix}_A", f"{prefix}_B", "edge_ab"),
            TransportEdge(f"{prefix}_B", f"{prefix}_C", "edge_bc"),
        ),
        source_site=f"{prefix}_A",
        target_site=f"{prefix}_C",
        patches=(
            RestrictionPatch(
                "same_ab",
                (f"{prefix}_A", f"{prefix}_B"),
                ("a", "b"),
                (PatchConstraint("a", "b", "same"),),
            ),
            RestrictionPatch(
                "same_bc",
                (f"{prefix}_B", f"{prefix}_C"),
                ("b", "c"),
                (PatchConstraint("b", "c", "same"),),
            ),
            RestrictionPatch(
                "different_ac",
                (f"{prefix}_A", f"{prefix}_C"),
                ("a", "c"),
                (PatchConstraint("a", "c", "different"),),
            ),
        ),
    )


def _verdict_for_schema(name: str, schema: ProjectionObstructionSchema) -> str:
    if schema.outcome == "faithful_projection_obstruction":
        return f"{name}: positive finite Projection-Obstruction instance"
    if schema.outcome == "non_definable_projection":
        return f"{name}: projection not definable inside T26"
    if schema.outcome == "lossy_projection_no_new_obstruction":
        return f"{name}: lossy projection, but no obstruction is created"
    return f"{name}: obstruction is inherited, not projection-created"


def _analysis_to_dict(analysis: ProjectionCaseAnalysis) -> dict[str, Any]:
    case = analysis.case
    richer_section = global_section(case.richer_system)
    restricted_section = global_section(case.restricted_system)
    return {
        "name": case.name,
        "source": case.source,
        "intended_reading": case.intended_reading,
        "richer_system": _system_summary(case.richer_system, analysis.richer_validation),
        "restricted_system": _system_summary(case.restricted_system, analysis.restricted_validation),
        "richer_global_section": asdict(richer_section),
        "restricted_global_section": asdict(restricted_section),
        "morphism": asdict(analysis.morphism_analysis),
        "forgotten_structure": list(case.forgotten_structure),
        "preserved_structure": list(case.preserved_structure),
        "schema": asdict(analysis.schema),
        "verdict": analysis.verdict,
    }


def _system_summary(system: D1RestrictionSystem, validation: ValidationResult) -> dict[str, Any]:
    return {
        "name": system.name,
        "site_count": len(system.site_ids()),
        "patch_count": len(system.patches),
        "edge_count": len(system.transport_edges),
        "validation_valid": validation.valid,
    }
