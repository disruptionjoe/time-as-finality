"""T31: PO1 admissibility conditions.

T31 refines PO1 from a broad pattern into a constrained theorem schema by
identifying the necessary and sufficient conditions a projection must satisfy
before obstruction behavior counts as a PO1 instance.

Seven admissibility conditions are evaluated per case:

  AC1 richer_valid          richer D1RestrictionSystem satisfies all T26 axioms
  AC2 restricted_valid      restricted D1RestrictionSystem satisfies all T26 axioms
  AC3 projection_definable  site map is total (site_map_total=True)
  AC4 local_compat          restricted system has all patches locally satisfiable
  AC5 structure_forgotten   projection forgets named structure AND loses measurable
                            profile data (forgotten_structure non-empty AND
                            local_profiles_preserved=False)
  AC6 restricted_obstructed restricted system has global_witness_count=0 and
                            local_witness_count = patch_count
  AC7 richer_unobstructed   richer system does NOT have a gluing obstruction
                            (global_witness_count > 0)

A case is a POSITIVE PO1 INSTANCE if and only if all seven conditions hold.

Failure cases are classified in priority order:
  boundary_non_definable            AC3 fails (category change, not enrichment)
  non_admissible_shared_obstruction AC7 fails (richer also obstructed)
  non_admissible_no_new_obstruction AC6 fails (restricted not obstructed)
  non_admissible_trivial_obstruction AC4 fails (restricted locally inconsistent)
  non_admissible_no_forgotten_structure AC5 fails (projection is not informatively lossy)
  non_admissible_system_invalid     AC1 or AC2 fails

The WEAKEST version of PO1 that correctly classifies all tested cases uses
AC1+AC2+AC3+AC6+AC7. Adding AC4 and AC5 guards against future overcounting
without changing the verdict for any currently tested case.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.cap_theorem_bridge import cap_bridge_case
from models.cross_domain_projection_obstruction_validation import (
    access_control_inheritance_case,
    database_expand_contract_case,
    git_semantic_merge_case,
    type_system_macro_boundary_case,
)
from models.d1_restriction_system import (
    analyze_morphism,
    global_section,
    validate_system,
)
from models.gu_class_relative_bridge import (
    distler_garibaldi_bridge_case,
    nielsen_ninomiya_bridge_case,
    witten_bridge_case,
)
from models.projection_obstruction_schema import (
    ProjectionCase,
    ProjectionCaseAnalysis,
    analyze_projection_case,
    projection_case_from_bridge_case,
    synthetic_lossy_no_obstruction_case,
    synthetic_shared_obstruction_case,
)


ADMISSIBILITY_CONDITIONS = (
    ("AC1", "richer_valid", "Richer D1RestrictionSystem satisfies all T26 axioms."),
    ("AC2", "restricted_valid", "Restricted D1RestrictionSystem satisfies all T26 axioms."),
    ("AC3", "projection_definable", "Site map is total (site_map_total=True); projection can be stated."),
    ("AC4", "local_compat", "Restricted system has all patches locally satisfiable (non-trivial obstruction)."),
    ("AC5", "structure_forgotten", "Projection forgets named structure AND loses measurable profile data."),
    ("AC6", "restricted_obstructed", "Restricted system has a gluing obstruction (global_witness_count=0, all patches locally satisfiable)."),
    ("AC7", "richer_unobstructed", "Richer system has a global section (obstruction_detected=False)."),
)

VERDICT_LABELS = {
    "fully_admissible": "positive PO1 instance",
    "boundary_non_definable": "boundary: non-definable projection",
    "non_admissible_shared_obstruction": "non-admissible: shared obstruction",
    "non_admissible_no_new_obstruction": "non-admissible: no new obstruction",
    "non_admissible_trivial_obstruction": "non-admissible: trivial obstruction",
    "non_admissible_no_forgotten_structure": "non-admissible: no forgotten structure",
    "non_admissible_system_invalid": "non-admissible: system invalid",
}


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class AdmissibilityCheck:
    case_name: str
    source: str
    ac1_richer_valid: bool
    ac2_restricted_valid: bool
    ac3_projection_definable: bool
    ac4_local_compat: bool
    ac5_structure_forgotten: bool
    ac6_restricted_obstructed: bool
    ac7_richer_unobstructed: bool
    verdict: str
    failed_conditions: tuple[str, ...]
    po1_evidence: bool


@dataclass(frozen=True)
class T31Result:
    checks: tuple[AdmissibilityCheck, ...]
    positive_cases: tuple[str, ...]
    boundary_cases: tuple[str, ...]
    non_admissible_cases: tuple[str, ...]
    condition_descriptions: tuple[tuple[str, str, str], ...]
    weakest_po1_conditions: tuple[str, ...]
    recommended_po1_conditions: tuple[str, ...]
    po1_status: str
    po1_recommendation: str


# ---------------------------------------------------------------------------
# Admissibility checker
# ---------------------------------------------------------------------------

def check_admissibility(case: ProjectionCase) -> AdmissibilityCheck:
    richer_val = validate_system(case.richer_system)
    restricted_val = validate_system(case.restricted_system)
    morphism_analysis = analyze_morphism(case.morphism)
    richer_gs = global_section(case.richer_system)
    restricted_gs = global_section(case.restricted_system)

    ac1 = richer_val.valid
    ac2 = restricted_val.valid
    ac3 = morphism_analysis.site_map_total

    patch_count = len(case.restricted_system.patches)
    ac4 = (
        patch_count == 0
        or restricted_gs.local_witness_count == patch_count
    )

    ac5 = (
        bool(case.forgotten_structure)
        and not morphism_analysis.local_profiles_preserved
    )

    ac6 = restricted_gs.obstruction_detected

    ac7 = not richer_gs.obstruction_detected

    verdict, failed = _determine_verdict(ac1, ac2, ac3, ac4, ac5, ac6, ac7)

    return AdmissibilityCheck(
        case_name=case.name,
        source=case.source,
        ac1_richer_valid=ac1,
        ac2_restricted_valid=ac2,
        ac3_projection_definable=ac3,
        ac4_local_compat=ac4,
        ac5_structure_forgotten=ac5,
        ac6_restricted_obstructed=ac6,
        ac7_richer_unobstructed=ac7,
        verdict=verdict,
        failed_conditions=failed,
        po1_evidence=(verdict == "fully_admissible"),
    )


def _determine_verdict(
    ac1: bool,
    ac2: bool,
    ac3: bool,
    ac4: bool,
    ac5: bool,
    ac6: bool,
    ac7: bool,
) -> tuple[str, tuple[str, ...]]:
    failed = []
    if not ac1:
        failed.append("AC1")
    if not ac2:
        failed.append("AC2")
    if not ac3:
        failed.append("AC3")
    if not ac4:
        failed.append("AC4")
    if not ac5:
        failed.append("AC5")
    if not ac6:
        failed.append("AC6")
    if not ac7:
        failed.append("AC7")

    if not failed:
        return "fully_admissible", ()
    if not ac1 or not ac2:
        return "non_admissible_system_invalid", tuple(failed)
    if not ac3:
        return "boundary_non_definable", tuple(failed)
    if not ac7:
        return "non_admissible_shared_obstruction", tuple(failed)
    if not ac6:
        return "non_admissible_no_new_obstruction", tuple(failed)
    if not ac4:
        return "non_admissible_trivial_obstruction", tuple(failed)
    if not ac5:
        return "non_admissible_no_forgotten_structure", tuple(failed)
    return "non_admissible_system_invalid", tuple(failed)


# ---------------------------------------------------------------------------
# Case collection
# ---------------------------------------------------------------------------

def _t31_cases() -> tuple[ProjectionCase, ...]:
    """Collect all cases from T27, T28, T29, and T30 for unified reclassification."""
    cap_case = cap_bridge_case()
    cap_proj = ProjectionCase(
        name=cap_case.name,
        source="T28",
        richer_system=cap_case.richer_system,
        restricted_system=cap_case.restricted_system,
        morphism=cap_case.morphism,
        forgotten_structure=cap_case.forgotten_structure,
        preserved_structure=cap_case.preserved_structure,
        intended_reading=cap_case.bridge_verdict,
    )
    git_hostile = git_semantic_merge_case()
    db_hostile = database_expand_contract_case()
    acl_hostile = access_control_inheritance_case()
    ts_hostile = type_system_macro_boundary_case()
    return (
        projection_case_from_bridge_case(witten_bridge_case()),
        projection_case_from_bridge_case(nielsen_ninomiya_bridge_case()),
        projection_case_from_bridge_case(distler_garibaldi_bridge_case()),
        cap_proj,
        synthetic_lossy_no_obstruction_case(),
        synthetic_shared_obstruction_case(),
        git_hostile.case,
        db_hostile.case,
        acl_hostile.case,
        ts_hostile.case,
    )


# ---------------------------------------------------------------------------
# Audit runner
# ---------------------------------------------------------------------------

def run_t31_admissibility_audit() -> T31Result:
    cases = _t31_cases()
    checks = tuple(check_admissibility(case) for case in cases)

    positive = tuple(c.case_name for c in checks if c.po1_evidence)
    boundary = tuple(c.case_name for c in checks if c.verdict == "boundary_non_definable")
    non_admissible = tuple(c.case_name for c in checks if not c.po1_evidence and c.verdict != "boundary_non_definable")

    weakest = (
        "AC1: richer system valid",
        "AC2: restricted system valid",
        "AC3: projection definable",
        "AC6: restricted system obstructed",
        "AC7: richer system unobstructed",
    )
    recommended = weakest + (
        "AC4: restricted obstruction non-trivial (all patches locally satisfiable)",
        "AC5: projection forgets named and measurable structure",
    )

    return T31Result(
        checks=checks,
        positive_cases=positive,
        boundary_cases=boundary,
        non_admissible_cases=non_admissible,
        condition_descriptions=ADMISSIBILITY_CONDITIONS,
        weakest_po1_conditions=weakest,
        recommended_po1_conditions=recommended,
        po1_status="partially_supported_narrowed",
        po1_recommendation=(
            "PO1 is retained as partially_supported and formally narrowed. "
            "T31 identifies seven admissibility conditions (AC1-AC7). All seven "
            "are required for a case to count as positive PO1 evidence. "
            "Four cases satisfy all seven: witten_1981, nielsen_ninomiya, "
            "cap_theorem, and git_semantic_merge. Two cases are non-definable "
            "boundaries (distler_garibaldi, type_system_macro_expansion). "
            "Four cases are non-admissible: two for shared obstruction "
            "(synthetic_shared_obstruction, access_control_inheritance) and "
            "two for no new obstruction "
            "(synthetic_lossy_no_obstruction, database_expand_contract). "
            "The weakest correct PO1 uses five conditions (AC1-AC3, AC6-AC7). "
            "AC4 and AC5 are added as guards against trivial and structure-free "
            "instances; no current case fails them in isolation, but both are "
            "needed to prevent overcounting in future applications. "
            "PO1 does not split into subclaims: the single positive schema "
            "survives all hostile tests. "
            "The schema is: a definable projection from a globally satisfiable "
            "richer system to a non-trivially obstructed restricted system, "
            "where the projection forgets named and measurable structure, is a "
            "faithful finite Projection-Obstruction instance."
        ),
    )


def run_t31_analysis() -> dict[str, Any]:
    result = run_t31_admissibility_audit()
    return {
        "admissibility_conditions": [
            {"id": ac_id, "field": field, "description": desc}
            for ac_id, field, desc in result.condition_descriptions
        ],
        "checks": [_check_to_dict(c) for c in result.checks],
        "positive_cases": list(result.positive_cases),
        "boundary_cases": list(result.boundary_cases),
        "non_admissible_cases": list(result.non_admissible_cases),
        "weakest_po1_conditions": list(result.weakest_po1_conditions),
        "recommended_po1_conditions": list(result.recommended_po1_conditions),
        "po1_status": result.po1_status,
        "po1_recommendation": result.po1_recommendation,
        "case_count": len(result.checks),
        "positive_count": len(result.positive_cases),
        "boundary_count": len(result.boundary_cases),
        "non_admissible_count": len(result.non_admissible_cases),
    }


def _check_to_dict(c: AdmissibilityCheck) -> dict[str, Any]:
    return {
        "case_name": c.case_name,
        "source": c.source,
        "conditions": {
            "AC1": c.ac1_richer_valid,
            "AC2": c.ac2_restricted_valid,
            "AC3": c.ac3_projection_definable,
            "AC4": c.ac4_local_compat,
            "AC5": c.ac5_structure_forgotten,
            "AC6": c.ac6_restricted_obstructed,
            "AC7": c.ac7_richer_unobstructed,
        },
        "verdict": c.verdict,
        "verdict_label": VERDICT_LABELS.get(c.verdict, c.verdict),
        "failed_conditions": list(c.failed_conditions),
        "po1_evidence": c.po1_evidence,
    }
