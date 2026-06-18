"""T32: derivation audit for PO1 admissibility conditions.

T31 identified seven admissibility conditions for PO1. T32 asks whether those
conditions are independent empirical rules or consequences of the finite
restriction-system mathematics.

The executable result is intentionally narrow:

* AC4 is derived from AC6 because `global_section().obstruction_detected`
  already includes local patch satisfiability.
* AC1 and AC2 are type obligations for a pair of D1RestrictionSystems.
* AC3 is the definability obligation for a finite site projection.
* AC6 and AC7 are independent gluing polarity requirements.
* AC5 is not intrinsic to D1RestrictionSystem alone. It depends on
  ProjectionCase metadata naming forgotten structure plus measurable profile
  loss under the morphism.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from itertools import product
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import (
    ADMISSIBILITY_CONDITIONS,
    AdmissibilityCheck,
    check_admissibility,
)
from models.projection_obstruction_schema import ProjectionCase


AC_IDS = tuple(condition[0] for condition in ADMISSIBILITY_CONDITIONS)


@dataclass(frozen=True)
class DependencyEdge:
    source: str
    target: str
    relation: str
    reason: str


@dataclass(frozen=True)
class StructuralPrinciple:
    principle_id: str
    name: str
    statement: str
    generates_conditions: tuple[str, ...]
    status: str
    boundary: str


@dataclass(frozen=True)
class ConditionDerivation:
    condition_id: str
    derivation_status: str
    derived_from: tuple[str, ...]
    proof: str
    independence_witness: str


@dataclass(frozen=True)
class RemovalAudit:
    removed_condition: str
    newly_admitted_false_positives: tuple[str, ...]
    newly_rejected_true_positives: tuple[str, ...]
    failure_class: str
    conclusion: str


@dataclass(frozen=True)
class GeneratedSubset:
    subset_id: str
    feasible: bool
    target_conditions: dict[str, bool]
    actual_conditions: dict[str, bool]
    case_name: str
    verdict: str
    note: str


@dataclass(frozen=True)
class T32Result:
    dependency_edges: tuple[DependencyEdge, ...]
    structural_principles: tuple[StructuralPrinciple, ...]
    condition_derivations: tuple[ConditionDerivation, ...]
    minimal_condition_basis: tuple[str, ...]
    compressed_principle_basis: tuple[str, ...]
    removal_audits: tuple[RemovalAudit, ...]
    generated_subsets: tuple[GeneratedSubset, ...]
    impossible_subsets: tuple[GeneratedSubset, ...]
    best_supported_hypothesis: str
    theorem_verdict: str
    recommendation: str


def dependency_graph() -> tuple[DependencyEdge, ...]:
    return (
        DependencyEdge(
            "P1_typed_pair",
            "AC1",
            "generates",
            "A PO1 candidate must first have a well-formed richer D1RestrictionSystem.",
        ),
        DependencyEdge(
            "P1_typed_pair",
            "AC2",
            "generates",
            "A PO1 candidate must also have a well-formed restricted D1RestrictionSystem.",
        ),
        DependencyEdge(
            "P2_definable_projection",
            "AC3",
            "generates",
            "Projection is finite and definable exactly when the site map is total.",
        ),
        DependencyEdge(
            "P3_projection_created_obstruction",
            "AC6",
            "generates",
            "The restricted target must have a finite gluing obstruction.",
        ),
        DependencyEdge(
            "AC6",
            "AC4",
            "implies",
            "In T26, obstruction_detected means local patches are satisfiable and no global assignment exists.",
        ),
        DependencyEdge(
            "P3_projection_created_obstruction",
            "AC7",
            "generates",
            "The richer source must have a global section, so the obstruction is not inherited.",
        ),
        DependencyEdge(
            "P4_informative_forgetting",
            "AC5",
            "generates_with_extra_metadata",
            "Forgotten named structure is stored on ProjectionCase, not inside D1RestrictionSystem alone.",
        ),
    )


def structural_principles() -> tuple[StructuralPrinciple, ...]:
    return (
        StructuralPrinciple(
            "P1_typed_pair",
            "Typed restriction-system pair",
            "Both source and target must satisfy the T26 finite restriction-system axioms.",
            ("AC1", "AC2"),
            "intrinsic_to_D1RestrictionSystem",
            "This is a typing obligation, not a discovered empirical rule.",
        ),
        StructuralPrinciple(
            "P2_definable_projection",
            "Definable finite projection",
            "A projection must have a total site map into the restricted system.",
            ("AC3",),
            "intrinsic_to_D1RestrictionMorphism",
            "Category-change cases fail here rather than becoming negative PO1 examples.",
        ),
        StructuralPrinciple(
            "P3_projection_created_obstruction",
            "Projection-created nontrivial obstruction",
            "The restricted system is obstructed and the richer system is not.",
            ("AC4", "AC6", "AC7"),
            "intrinsic_to_global_section_polarity",
            "AC4 is redundant once AC6 uses T26 obstruction_detected.",
        ),
        StructuralPrinciple(
            "P4_informative_forgetting",
            "Informative forgotten structure",
            "The projection must forget named structure and measurably lose profile data.",
            ("AC5",),
            "not_intrinsic_to_D1RestrictionSystem_alone",
            "The named-forgotten-structure half lives on ProjectionCase metadata.",
        ),
    )


def condition_derivations() -> tuple[ConditionDerivation, ...]:
    witnesses = _removal_witnesses()
    return (
        ConditionDerivation(
            "AC1",
            "derived_from_type_principle_but_independent_as_a_check",
            ("P1_typed_pair",),
            "If PO1 is stated over D1RestrictionSystem pairs, richer validity is part of the domain of discourse.",
            witnesses["AC1"].name,
        ),
        ConditionDerivation(
            "AC2",
            "derived_from_type_principle_but_independent_as_a_check",
            ("P1_typed_pair",),
            "If PO1 is stated over D1RestrictionSystem pairs, restricted validity is part of the domain of discourse.",
            witnesses["AC2"].name,
        ),
        ConditionDerivation(
            "AC3",
            "derived_from_projection_definability",
            ("P2_definable_projection",),
            "A finite projection cannot be evaluated unless every source site has a target site.",
            witnesses["AC3"].name,
        ),
        ConditionDerivation(
            "AC4",
            "derived_from_AC6",
            ("AC6", "global_section.obstruction_detected"),
            "T26 defines obstruction_detected as local_satisfiable and not global_exists, so AC6 entails AC4.",
            "no feasible D1RestrictionSystem case with AC6=True and AC4=False",
        ),
        ConditionDerivation(
            "AC5",
            "not_derived_from_D1RestrictionSystem_alone",
            ("P4_informative_forgetting",),
            "A restriction system can show profile loss, but named forgotten structure is external ProjectionCase evidence.",
            witnesses["AC5"].name,
        ),
        ConditionDerivation(
            "AC6",
            "independent_gluing_requirement",
            ("P3_projection_created_obstruction",),
            "The other conditions can hold while the restricted system has a global section.",
            witnesses["AC6"].name,
        ),
        ConditionDerivation(
            "AC7",
            "independent_resolution_requirement",
            ("P3_projection_created_obstruction",),
            "The other conditions can hold while the richer system is already obstructed.",
            witnesses["AC7"].name,
        ),
    )


def removal_audits() -> tuple[RemovalAudit, ...]:
    witnesses = _removal_witnesses()
    audits: list[RemovalAudit] = []
    for ac_id in AC_IDS:
        if ac_id == "AC4":
            audits.append(
                RemovalAudit(
                    removed_condition=ac_id,
                    newly_admitted_false_positives=(),
                    newly_rejected_true_positives=(),
                    failure_class="none_under_current_T26_semantics",
                    conclusion=(
                        "Removing AC4 changes no classification because AC6 already implies local "
                        "satisfiability in the executable definition."
                    ),
                )
            )
            continue
        witness = witnesses[ac_id]
        check = check_admissibility(witness)
        audits.append(
            RemovalAudit(
                removed_condition=ac_id,
                newly_admitted_false_positives=(witness.name,),
                newly_rejected_true_positives=(),
                failure_class=check.verdict,
                conclusion=_removal_conclusion(ac_id, witness.name, check),
            )
        )
    return tuple(audits)


def generate_condition_subsets() -> tuple[tuple[GeneratedSubset, ...], tuple[GeneratedSubset, ...]]:
    generated: list[GeneratedSubset] = []
    impossible: list[GeneratedSubset] = []
    for index, values in enumerate(product((False, True), repeat=len(AC_IDS))):
        target = dict(zip(AC_IDS, values))
        subset_id = _subset_id(index, target)
        if target["AC6"] and not target["AC4"]:
            impossible.append(
                GeneratedSubset(
                    subset_id=subset_id,
                    feasible=False,
                    target_conditions=target,
                    actual_conditions={},
                    case_name="none",
                    verdict="impossible",
                    note="AC6 implies AC4 under T26 obstruction_detected semantics.",
                )
            )
            continue
        case = projection_case_for_conditions(target, f"subset_{index:03d}")
        check = check_admissibility(case)
        actual = _conditions_from_check(check)
        generated.append(
            GeneratedSubset(
                subset_id=subset_id,
                feasible=actual == target,
                target_conditions=target,
                actual_conditions=actual,
                case_name=case.name,
                verdict=check.verdict,
                note=(
                    "generated exact finite ProjectionCase"
                    if actual == target
                    else "generator did not hit target condition vector"
                ),
            )
        )
    return tuple(generated), tuple(impossible)


def projection_case_for_conditions(target: dict[str, bool], name: str) -> ProjectionCase:
    if target["AC6"] and not target["AC4"]:
        raise ValueError("AC6=True and AC4=False is impossible in current T26 semantics")

    same_profiles = not target["AC5"] or not target["AC3"]
    rich_profile = D1Profile(2, 2, 1, 2)
    restricted_profile = rich_profile if same_profiles else D1Profile(1, 1, 0, 1)

    rich = _system(
        f"{name}_rich",
        profile=rich_profile,
        obstructed=not target["AC7"],
        locally_inconsistent=False,
        invalid=not target["AC1"],
    )
    restricted = _system(
        f"{name}_restricted",
        profile=restricted_profile,
        obstructed=target["AC6"],
        locally_inconsistent=(not target["AC4"] and not target["AC6"]),
        invalid=not target["AC2"],
    )

    site_map = (
        SiteMap(f"{name}_rich_A", f"{name}_restricted_A"),
        SiteMap(f"{name}_rich_B", f"{name}_restricted_B"),
    )
    if target["AC3"]:
        site_map = site_map + (SiteMap(f"{name}_rich_C", f"{name}_restricted_C"),)

    forgotten_structure = (
        ("obstruction-resolving structure", "measurable profile detail")
        if target["AC5"]
        else ()
    )

    return ProjectionCase(
        name=f"{name}_case",
        source="T32-generated",
        richer_system=rich,
        restricted_system=restricted,
        morphism=D1RestrictionMorphism(
            name=f"{name}_projection",
            source=rich,
            target=restricted,
            site_map=site_map,
            require_trust_path_preservation=True,
            require_obstruction_preservation=False,
        ),
        forgotten_structure=forgotten_structure,
        preserved_structure=("finite sites", "trusted path"),
        intended_reading="generated condition-vector witness for T32",
    )


def run_t32_derivation_audit() -> T32Result:
    generated, impossible = generate_condition_subsets()
    return T32Result(
        dependency_edges=dependency_graph(),
        structural_principles=structural_principles(),
        condition_derivations=condition_derivations(),
        minimal_condition_basis=("AC1", "AC2", "AC3", "AC5", "AC6", "AC7"),
        compressed_principle_basis=(
            "P1_typed_pair",
            "P2_definable_projection",
            "P3_projection_created_obstruction",
            "P4_informative_forgetting",
        ),
        removal_audits=removal_audits(),
        generated_subsets=generated,
        impossible_subsets=impossible,
        best_supported_hypothesis="H2 with H4 boundary",
        theorem_verdict=(
            "AC1-AC7 are not seven independent empirical rules. AC4 derives "
            "from AC6; AC1 and AC2 are type obligations; AC3, AC6, and AC7 "
            "are structural projection/gluing obligations. AC5 remains an "
            "extra informative-loss condition not derivable from "
            "D1RestrictionSystem alone."
        ),
        recommendation=(
            "Replace the independent seven-condition posture with a four-principle "
            "basis: typed pair, definable projection, projection-created "
            "nontrivial obstruction, and informative forgotten structure. Keep "
            "the AC1-AC7 checklist as an expanded audit surface, but fold AC4 "
            "into AC6 in formal statements. Retain AC5 as an explicit "
            "non-intrinsic admissibility guard until forgotten structure is "
            "made first-class inside the formal object."
        ),
    )


def run_t32_analysis() -> dict[str, Any]:
    result = run_t32_derivation_audit()
    feasible_count = sum(1 for item in result.generated_subsets if item.feasible)
    return {
        "dependency_edges": [asdict(edge) for edge in result.dependency_edges],
        "structural_principles": [asdict(principle) for principle in result.structural_principles],
        "condition_derivations": [asdict(derivation) for derivation in result.condition_derivations],
        "minimal_condition_basis": list(result.minimal_condition_basis),
        "compressed_principle_basis": list(result.compressed_principle_basis),
        "removal_audits": [asdict(audit) for audit in result.removal_audits],
        "subset_generation": {
            "total_condition_vectors": 2 ** len(AC_IDS),
            "generated_feasible_vectors": feasible_count,
            "impossible_vectors": len(result.impossible_subsets),
            "impossibility_rule": "AC6 implies AC4",
            "generated_vectors": [asdict(item) for item in result.generated_subsets],
            "impossible_vectors_detail": [asdict(item) for item in result.impossible_subsets],
            "generated_examples": [asdict(item) for item in result.generated_subsets[:12]],
            "impossible_examples": [asdict(item) for item in result.impossible_subsets[:12]],
        },
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "theorem_verdict": result.theorem_verdict,
        "recommendation": result.recommendation,
    }


def _removal_witnesses() -> dict[str, ProjectionCase]:
    all_true = {ac_id: True for ac_id in AC_IDS}
    return {
        "AC1": projection_case_for_conditions({**all_true, "AC1": False}, "remove_ac1"),
        "AC2": projection_case_for_conditions({**all_true, "AC2": False}, "remove_ac2"),
        "AC3": projection_case_for_conditions({**all_true, "AC3": False}, "remove_ac3"),
        "AC5": projection_case_for_conditions({**all_true, "AC5": False}, "remove_ac5"),
        "AC6": projection_case_for_conditions({**all_true, "AC6": False}, "remove_ac6"),
        "AC7": projection_case_for_conditions({**all_true, "AC7": False}, "remove_ac7"),
    }


def _system(
    prefix: str,
    profile: D1Profile,
    obstructed: bool,
    locally_inconsistent: bool,
    invalid: bool,
) -> D1RestrictionSystem:
    if obstructed:
        patches = _obstructed_patches(prefix)
    elif locally_inconsistent:
        patches = _locally_inconsistent_patches(prefix)
    else:
        patches = ()

    edges = (
        TransportEdge(f"{prefix}_A", f"{prefix}_B", "trusted_ab"),
        TransportEdge(f"{prefix}_B", f"{prefix}_C", "trusted_bc"),
    )
    if invalid:
        edges = edges + (TransportEdge(f"{prefix}_A", f"{prefix}_ghost", "invalid_edge"),)

    return D1RestrictionSystem(
        name=prefix,
        proposition="record_R",
        local_values=(
            _local(f"{prefix}_A", profile),
            _local(f"{prefix}_B", profile),
            _local(f"{prefix}_C", profile),
        ),
        transport_edges=edges,
        source_site=f"{prefix}_A",
        target_site=f"{prefix}_C",
        patches=patches,
    )


def _obstructed_patches(prefix: str) -> tuple[RestrictionPatch, ...]:
    return (
        RestrictionPatch(
            f"{prefix}_same_ab",
            (f"{prefix}_A", f"{prefix}_B"),
            ("a", "b"),
            (PatchConstraint("a", "b", "same"),),
        ),
        RestrictionPatch(
            f"{prefix}_same_bc",
            (f"{prefix}_B", f"{prefix}_C"),
            ("b", "c"),
            (PatchConstraint("b", "c", "same"),),
        ),
        RestrictionPatch(
            f"{prefix}_different_ac",
            (f"{prefix}_A", f"{prefix}_C"),
            ("a", "c"),
            (PatchConstraint("a", "c", "different"),),
        ),
    )


def _locally_inconsistent_patches(prefix: str) -> tuple[RestrictionPatch, ...]:
    return (
        RestrictionPatch(
            f"{prefix}_inconsistent_local",
            (f"{prefix}_A", f"{prefix}_B"),
            ("a", "b"),
            (
                PatchConstraint("a", "b", "same"),
                PatchConstraint("a", "b", "different"),
            ),
        ),
    )


def _local(site_id: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(
        site=ObserverSite(site_id, "T32", "finite_site", 0, "derivation"),
        proposition_value="true",
        profile=profile,
    )


def _conditions_from_check(check: AdmissibilityCheck) -> dict[str, bool]:
    return {
        "AC1": check.ac1_richer_valid,
        "AC2": check.ac2_restricted_valid,
        "AC3": check.ac3_projection_definable,
        "AC4": check.ac4_local_compat,
        "AC5": check.ac5_structure_forgotten,
        "AC6": check.ac6_restricted_obstructed,
        "AC7": check.ac7_richer_unobstructed,
    }


def _removal_conclusion(ac_id: str, case_name: str, check: AdmissibilityCheck) -> str:
    if ac_id in {"AC1", "AC2"}:
        return f"Without {ac_id}, {case_name} admits an invalid typed object as PO1 evidence."
    if ac_id == "AC3":
        return f"Without AC3, {case_name} admits a category-change boundary as a projection."
    if ac_id == "AC5":
        return f"Without AC5, {case_name} admits a lossless or unnamed projection as PO1 evidence."
    if ac_id == "AC6":
        return f"Without AC6, {case_name} admits a projection where the restricted system is not obstructed."
    if ac_id == "AC7":
        return f"Without AC7, {case_name} admits a shared obstruction as projection-created."
    return f"{case_name}: {check.verdict}"


def _subset_id(index: int, target: dict[str, bool]) -> str:
    bits = "".join("1" if target[ac_id] else "0" for ac_id in AC_IDS)
    return f"subset_{index:03d}_{bits}"


def ac6_implies_ac4_for_system(system: D1RestrictionSystem) -> bool:
    section = global_section(system)
    if not section.obstruction_detected:
        return True
    return section.local_patches_satisfiable
