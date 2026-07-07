"""T504: boundary-adapter source-category and functor gate.

The CT-1 open problem says the GU/TaF boundary adapter cannot remain an
object-level analogy. A real adapter needs a named source category, a target
category, a map on objects and morphisms, and functor laws. This module keeps
the work repo-local: it builds a finite abstract boundary-sector fixture and
checks whether candidate packets clear the source-category and non-constant
functor burdens against the already-proven T41 D1Cat target.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.d1_restriction_system import D1RestrictionMorphism, D1RestrictionSystem
from models.transport_network import _compose_morphisms
from models.typed_transport_category import (
    _make_aligned_morphism,
    _make_category_system,
    make_identity,
    morphisms_equal_modulo_name,
    run_t41_analysis,
)


ARTIFACT_ID = "T504-boundary-adapter-source-category-functor-gate-v0.1"
VERDICT = "BOUNDARY_SOURCE_CATEGORY_FUNCTOR_GATE_BUILT_REVIEW_ONLY"
SOURCE_OPEN_PROBLEM = "open-problems/boundary-adapter-as-functor-spec-2026-07-07.md"
TARGET_CATEGORY_ANCHOR = "T41 D1Cat"
W_MINUS_TARGET = "D1_collective_complement_shadow"


@dataclass(frozen=True)
class BoundaryObject:
    object_id: str
    description: str
    sector_kind: str
    ghost_parity: str


@dataclass(frozen=True)
class BoundaryMorphism:
    morphism_id: str
    source: str
    target: str
    operation: str
    preserves_krein_signature: bool
    preserves_ghost_parity: bool
    identity: bool = False


@dataclass(frozen=True)
class SourceCategory:
    objects: tuple[BoundaryObject, ...]
    morphisms: tuple[BoundaryMorphism, ...]
    composition: dict[tuple[str, str], str]


@dataclass(frozen=True)
class SourceCategoryLawReport:
    identities_exist: bool
    composition_closed: bool
    associativity_holds: bool
    left_units_hold: bool
    right_units_hold: bool
    forms_category: bool
    object_count: int
    morphism_count: int
    composable_pair_count: int


@dataclass(frozen=True)
class FunctorLawReport:
    object_map_total: bool
    morphism_map_total: bool
    identity_laws_hold: bool
    composition_laws_hold: bool
    functor_laws_hold: bool
    nonconstant_on_objects: bool
    nonconstant_on_nonidentity_morphisms: bool
    nonconstant_functor: bool
    w_minus_maps_to_collective_complement: bool
    failed_composition_checks: tuple[str, ...]


@dataclass(frozen=True)
class AdapterPacket:
    packet_id: str
    description: str
    source_category: SourceCategory | None
    target_fixture_kind: str
    declares_object_map: bool
    declares_morphism_map: bool
    maps_w_minus_to_collective_complement: bool
    requests_claim_movement: bool = False
    requests_public_posture_movement: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth_movement: bool = False
    depends_on_sibling_repo_truth: bool = False


@dataclass(frozen=True)
class AdapterDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    review_target_only: bool
    missing_requirements: tuple[str, ...]
    blocked_shortcuts: tuple[str, ...]
    source_category_report: SourceCategoryLawReport | None
    functor_report: FunctorLawReport | None
    strongest_allowed_reading: str


def run() -> dict[str, Any]:
    """Run T504 and return a serializable result."""

    t41 = run_t41_analysis()
    packets = fixture_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    admitted = tuple(decision.packet_id for decision in decisions if decision.admitted)
    rejected = tuple(decision.packet_id for decision in decisions if not decision.admitted)

    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": VERDICT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "target_category_anchor": {
            "name": TARGET_CATEGORY_ANCHOR,
            "forms_proper_category": t41.forms_proper_category,
            "all_category_laws_hold": t41.all_category_laws_hold,
            "po1_is_functor_to_bool": t41.po1_is_functor,
        },
        "objective": (
            "Make CT-1's boundary-adapter burden executable: no adapter packet "
            "is admitted until it names a source category, maps objects and "
            "morphisms into D1Cat, satisfies identity and composition laws, and "
            "is non-constant."
        ),
        "packets": [_packet_dict(packet) for packet in packets],
        "decisions": [_decision_dict(decision) for decision in decisions],
        "admitted_packet_ids": list(admitted),
        "rejected_packet_ids": list(rejected),
        "overall": {
            "admitted_count": len(admitted),
            "rejected_count": len(rejected),
            "review_target_only": all(
                decision.review_target_only for decision in decisions if decision.admitted
            ),
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
            "sibling_repo_inspection": False,
            "strongest_reading": (
                "T504 does not build the real GU/TaF adapter. It builds the "
                "TaF-side admission gate for such an adapter. A synthetic finite "
                "boundary-sector category can map non-constantly into D1Cat and "
                "satisfy functor laws, which proves the check is executable. "
                "Object-only bridges, missing source morphisms, constant "
                "functors, bad composition maps, W-minus mis-targeting, and "
                "cross-repo shortcut packets are rejected or blocked."
            ),
        },
        "future_packet_minimum": [
            "declare boundary-sector objects inside a named source category",
            "declare source morphisms that compose and have identities",
            "map every source object to a D1Cat object or declared D1 subcategory object",
            "map every source morphism to a D1RestrictionMorphism",
            "prove F(id) = id and F(g;f) = F(g);F(f) on the finite fixture",
            "show the functor is non-constant on objects or nonidentity morphisms",
            "send the W-minus or mirror-sector object to the declared collective-complement target",
            "include constant-functor, object-only, and bad-composition hostile controls",
            "keep admission review-only until sibling repo source-category truth is supplied by that repo",
        ],
        "not_earned": [
            "real GU source category",
            "real GU/TaF adapter",
            "two-adapter gate",
            "adjunction or equivalence",
            "mirror equals collective-capability boundary",
            "category theorem beyond the finite synthetic fixture",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "hard-policy movement",
            "external publication",
            "cross-repo truth movement",
        ],
    }


def source_category_fixture() -> SourceCategory:
    objects = (
        BoundaryObject(
            "carrier",
            "abstract total boundary carrier; local fixture only",
            "total_boundary_carrier",
            "mixed",
        ),
        BoundaryObject(
            "w_minus_mirror",
            "abstract W-minus mirror sector; local fixture only",
            "mirror_sector",
            "minus",
        ),
        BoundaryObject(
            "collective_wall",
            "abstract collective-complement boundary wall; local fixture only",
            "capability_boundary",
            "minus",
        ),
    )
    morphisms = (
        BoundaryMorphism("id_carrier", "carrier", "carrier", "identity", True, True, True),
        BoundaryMorphism(
            "id_w_minus_mirror",
            "w_minus_mirror",
            "w_minus_mirror",
            "identity",
            True,
            True,
            True,
        ),
        BoundaryMorphism(
            "id_collective_wall",
            "collective_wall",
            "collective_wall",
            "identity",
            True,
            True,
            True,
        ),
        BoundaryMorphism(
            "restrict_to_mirror",
            "carrier",
            "w_minus_mirror",
            "ghost_parity_restriction",
            True,
            True,
        ),
        BoundaryMorphism(
            "restrict_to_wall",
            "w_minus_mirror",
            "collective_wall",
            "sector_to_capability_boundary_restriction",
            True,
            True,
        ),
        BoundaryMorphism(
            "restrict_to_wall_direct",
            "carrier",
            "collective_wall",
            "composite_restriction",
            True,
            True,
        ),
    )
    composition = {
        ("id_carrier", "id_carrier"): "id_carrier",
        ("id_w_minus_mirror", "id_w_minus_mirror"): "id_w_minus_mirror",
        ("id_collective_wall", "id_collective_wall"): "id_collective_wall",
        ("id_carrier", "restrict_to_mirror"): "restrict_to_mirror",
        ("restrict_to_mirror", "id_w_minus_mirror"): "restrict_to_mirror",
        ("id_w_minus_mirror", "restrict_to_wall"): "restrict_to_wall",
        ("restrict_to_wall", "id_collective_wall"): "restrict_to_wall",
        ("id_carrier", "restrict_to_wall_direct"): "restrict_to_wall_direct",
        ("restrict_to_wall_direct", "id_collective_wall"): "restrict_to_wall_direct",
        ("restrict_to_mirror", "restrict_to_wall"): "restrict_to_wall_direct",
    }
    return SourceCategory(objects=objects, morphisms=morphisms, composition=composition)


def fixture_packets() -> tuple[AdapterPacket, ...]:
    category = source_category_fixture()
    return (
        AdapterPacket(
            "synthetic_sector_restriction_functor",
            "Finite synthetic source category with a non-constant functor into D1Cat.",
            category,
            "valid_nonconstant",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=True,
        ),
        AdapterPacket(
            "object_only_mirror_bridge",
            "Names the mirror object and C(R) object but gives no action on morphisms.",
            category,
            "object_only",
            declares_object_map=True,
            declares_morphism_map=False,
            maps_w_minus_to_collective_complement=True,
        ),
        AdapterPacket(
            "missing_source_morphisms",
            "Uses boundary-sector objects without a category of morphisms.",
            None,
            "missing_source",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=True,
        ),
        AdapterPacket(
            "constant_functor_control",
            "Maps every source object and morphism into one D1 object.",
            category,
            "constant",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=False,
        ),
        AdapterPacket(
            "bad_composite_morphism_map",
            "Maps objects and morphisms but violates F(g;f)=F(g);F(f).",
            category,
            "bad_composition",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=True,
        ),
        AdapterPacket(
            "w_minus_wrong_target",
            "A non-constant functor that does not send W-minus to collective complement.",
            category,
            "wrong_w_minus_target",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=False,
        ),
        AdapterPacket(
            "sibling_truth_shortcut",
            "Attempts to treat sibling-repo GU carrier content as already verified here.",
            category,
            "valid_nonconstant",
            declares_object_map=True,
            declares_morphism_map=True,
            maps_w_minus_to_collective_complement=True,
            requests_cross_repo_truth_movement=True,
            depends_on_sibling_repo_truth=True,
        ),
    )


def evaluate_packet(packet: AdapterPacket) -> AdapterDecision:
    blocked = _blocked_shortcuts(packet)
    source_report = (
        evaluate_source_category(packet.source_category)
        if packet.source_category is not None
        else None
    )
    functor_report: FunctorLawReport | None = None
    missing: list[str] = []

    if packet.source_category is None:
        missing.append("source_category")
    elif source_report is not None and not source_report.forms_category:
        missing.append("source_category_laws")

    if not packet.declares_object_map:
        missing.append("object_map")
    if not packet.declares_morphism_map:
        missing.append("morphism_map")

    if (
        packet.source_category is not None
        and source_report is not None
        and source_report.forms_category
        and packet.declares_object_map
        and packet.declares_morphism_map
    ):
        functor_report = evaluate_functor(packet.source_category, packet.target_fixture_kind)
        if not functor_report.functor_laws_hold:
            missing.append("functor_laws")
        if not functor_report.nonconstant_functor:
            missing.append("nonconstant_functor")
        if not packet.maps_w_minus_to_collective_complement:
            missing.append("w_minus_collective_complement_target")
        elif not functor_report.w_minus_maps_to_collective_complement:
            missing.append("w_minus_collective_complement_target")

    if blocked:
        return AdapterDecision(
            packet_id=packet.packet_id,
            admitted=False,
            label="BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT",
            action="stop",
            review_target_only=False,
            missing_requirements=tuple(missing),
            blocked_shortcuts=blocked,
            source_category_report=source_report,
            functor_report=functor_report,
            strongest_allowed_reading=(
                "The packet must be rewritten as repo-local review intake; "
                "sibling-repo truth and cross-repo movement are not executed here."
            ),
        )

    if "source_category" in missing or "source_category_laws" in missing:
        label = "REJECTED_SOURCE_CATEGORY_NOT_BUILT"
    elif "morphism_map" in missing:
        label = "REJECTED_OBJECT_ONLY_NOT_A_FUNCTOR"
    elif "functor_laws" in missing:
        label = "REJECTED_FUNCTOR_LAW_FAILURE"
    elif "nonconstant_functor" in missing:
        label = "REJECTED_CONSTANT_FUNCTOR_CONTROL"
    elif "w_minus_collective_complement_target" in missing:
        label = "REJECTED_WRONG_W_MINUS_TARGET"
    elif missing:
        label = "REJECTED_INCOMPLETE_ADAPTER_PACKET"
    else:
        return AdapterDecision(
            packet_id=packet.packet_id,
            admitted=True,
            label="ADMITTED_SOURCE_CATEGORY_FUNCTOR_REVIEW_TARGET",
            action="review",
            review_target_only=True,
            missing_requirements=(),
            blocked_shortcuts=(),
            source_category_report=source_report,
            functor_report=functor_report,
            strongest_allowed_reading=(
                "Synthetic finite review target only. The packet proves that the "
                "CT-1 check is executable against D1Cat, not that GU has supplied "
                "the real source category or that the tri-repo adapter is true."
            ),
        )

    return AdapterDecision(
        packet_id=packet.packet_id,
        admitted=False,
        label=label,
        action="reject",
        review_target_only=False,
        missing_requirements=tuple(missing),
        blocked_shortcuts=(),
        source_category_report=source_report,
        functor_report=functor_report,
        strongest_allowed_reading="Rejected packet; no adapter review target admitted.",
    )


def evaluate_source_category(category: SourceCategory) -> SourceCategoryLawReport:
    objects = {obj.object_id for obj in category.objects}
    morphisms = {m.morphism_id: m for m in category.morphisms}
    identities = {
        morphism.source: morphism.morphism_id
        for morphism in category.morphisms
        if morphism.identity and morphism.source == morphism.target
    }
    identities_exist = objects == set(identities)
    composable_pairs = tuple(
        (left.morphism_id, right.morphism_id)
        for left in category.morphisms
        for right in category.morphisms
        if left.target == right.source
    )
    composition_closed = all(
        pair in category.composition and category.composition[pair] in morphisms
        for pair in composable_pairs
    )
    left_units_hold = all(
        category.composition.get((identities.get(m.source, ""), m.morphism_id))
        == m.morphism_id
        for m in category.morphisms
    )
    right_units_hold = all(
        category.composition.get((m.morphism_id, identities.get(m.target, "")))
        == m.morphism_id
        for m in category.morphisms
    )
    associativity_holds = _source_associativity_holds(category, composable_pairs)
    forms_category = (
        identities_exist
        and composition_closed
        and associativity_holds
        and left_units_hold
        and right_units_hold
    )
    return SourceCategoryLawReport(
        identities_exist=identities_exist,
        composition_closed=composition_closed,
        associativity_holds=associativity_holds,
        left_units_hold=left_units_hold,
        right_units_hold=right_units_hold,
        forms_category=forms_category,
        object_count=len(objects),
        morphism_count=len(morphisms),
        composable_pair_count=len(composable_pairs),
    )


def evaluate_functor(category: SourceCategory, fixture_kind: str) -> FunctorLawReport:
    object_map, morphism_map = _target_fixture(category, fixture_kind)
    objects = {obj.object_id for obj in category.objects}
    morphisms = {m.morphism_id: m for m in category.morphisms}
    object_map_total = objects <= set(object_map)
    morphism_map_total = set(morphisms) <= set(morphism_map)
    failed: list[str] = []

    identity_laws = []
    for morphism in category.morphisms:
        if not morphism.identity:
            continue
        target_identity = make_identity(object_map[morphism.source])
        mapped = morphism_map[morphism.morphism_id]
        check = morphisms_equal_modulo_name(mapped, target_identity)
        identity_laws.append(check.equal_modulo_name)
        if not check.equal_modulo_name:
            failed.append(f"identity:{morphism.morphism_id}")

    composition_laws = []
    for left in category.morphisms:
        for right in category.morphisms:
            if left.target != right.source:
                continue
            composite_id = category.composition[(left.morphism_id, right.morphism_id)]
            mapped_composite = morphism_map[composite_id]
            composed_mapping = _compose_morphisms(
                morphism_map[left.morphism_id],
                morphism_map[right.morphism_id],
            )
            check = morphisms_equal_modulo_name(mapped_composite, composed_mapping)
            composition_laws.append(check.equal_modulo_name)
            if not check.equal_modulo_name:
                failed.append(f"composition:{left.morphism_id};{right.morphism_id}")

    object_image_names = {obj.name for obj in object_map.values()}
    nonidentity_image_fingerprints = {
        _morphism_fingerprint(morphism_map[m.morphism_id])
        for m in category.morphisms
        if not m.identity
    }
    nonconstant_on_objects = len(object_image_names) > 1
    nonconstant_on_nonidentity_morphisms = len(nonidentity_image_fingerprints) > 1
    w_minus_target = object_map["w_minus_mirror"].name == W_MINUS_TARGET

    return FunctorLawReport(
        object_map_total=object_map_total,
        morphism_map_total=morphism_map_total,
        identity_laws_hold=all(identity_laws),
        composition_laws_hold=all(composition_laws),
        functor_laws_hold=object_map_total
        and morphism_map_total
        and all(identity_laws)
        and all(composition_laws),
        nonconstant_on_objects=nonconstant_on_objects,
        nonconstant_on_nonidentity_morphisms=nonconstant_on_nonidentity_morphisms,
        nonconstant_functor=nonconstant_on_objects or nonconstant_on_nonidentity_morphisms,
        w_minus_maps_to_collective_complement=w_minus_target,
        failed_composition_checks=tuple(failed),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    decision_rows = [
        "| {packet_id} | {admitted} | {label} | {missing} | {blocked} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            missing=", ".join(decision["missing_requirements"]) or "none",
            blocked=", ".join(decision["blocked_shortcuts"]) or "none",
        )
        for decision in payload["decisions"]
    ]
    future = [f"- {item}" for item in payload["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T504 - Boundary-Adapter Source-Category Functor Gate - v0.1 results",
            "",
            "> Admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T504-boundary-adapter-source-category-functor-gate.md`",
            "- Model: `models/boundary_adapter_source_category_functor_gate.py`",
            "- Tests: `tests/test_boundary_adapter_source_category_functor_gate.py`",
            "- Source open problem: `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`",
            "- Target-category anchor: T41 / `models/typed_transport_category.py`",
            "- Artifact JSON: `results/T504-boundary-adapter-source-category-functor-gate-v0.1.json`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["overall"]["strongest_reading"],
            "",
            "## Decisions",
            "",
            "| Packet | Admitted? | Label | Missing requirements | Blocked shortcuts |",
            "| --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Target Category Anchor",
            "",
            f"- T41 forms proper category: `{payload['target_category_anchor']['forms_proper_category']}`",
            f"- T41 category laws hold: `{payload['target_category_anchor']['all_category_laws_hold']}`",
            f"- PO1 is functor to Bool: `{payload['target_category_anchor']['po1_is_functor_to_bool']}`",
            "",
            "## Future Packet Minimum",
            "",
            *future,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _source_associativity_holds(
    category: SourceCategory,
    composable_pairs: tuple[tuple[str, str], ...],
) -> bool:
    morphisms = {m.morphism_id: m for m in category.morphisms}
    pair_set = set(composable_pairs)
    for f in category.morphisms:
        for g in category.morphisms:
            for h in category.morphisms:
                if (f.morphism_id, g.morphism_id) not in pair_set:
                    continue
                if (g.morphism_id, h.morphism_id) not in pair_set:
                    continue
                fg = category.composition[(f.morphism_id, g.morphism_id)]
                gh = category.composition[(g.morphism_id, h.morphism_id)]
                if (fg, h.morphism_id) not in category.composition:
                    return False
                if (f.morphism_id, gh) not in category.composition:
                    return False
                lhs = category.composition[(fg, h.morphism_id)]
                rhs = category.composition[(f.morphism_id, gh)]
                if lhs != rhs:
                    return False
                if morphisms[lhs].source != f.source or morphisms[lhs].target != h.target:
                    return False
    return True


def _target_fixture(
    category: SourceCategory,
    fixture_kind: str,
) -> tuple[dict[str, D1RestrictionSystem], dict[str, D1RestrictionMorphism]]:
    if fixture_kind == "constant":
        const = _make_category_system("D1_constant_boundary_shadow", "t504_const")
        object_map = {obj.object_id: const for obj in category.objects}
        id_const = make_identity(const)
        morphism_map = {m.morphism_id: id_const for m in category.morphisms}
        return object_map, morphism_map

    if fixture_kind == "wrong_w_minus_target":
        carrier = _make_category_system("D1_boundary_carrier_shadow", "t504_carrier")
        wall = _make_category_system("D1_collective_wall_shadow", "t504_wall")
        complement = _make_category_system(W_MINUS_TARGET, "t504_complement")
        object_map = {
            "carrier": carrier,
            "w_minus_mirror": wall,
            "collective_wall": complement,
        }
        return object_map, _morphism_map_for_chain(
            category,
            carrier,
            wall,
            complement,
            bad_composite=False,
        )

    carrier = _make_category_system("D1_boundary_carrier_shadow", "t504_carrier")
    complement = _make_category_system(W_MINUS_TARGET, "t504_complement")
    wall = _make_category_system("D1_collective_wall_shadow", "t504_wall")
    object_map = {
        "carrier": carrier,
        "w_minus_mirror": complement,
        "collective_wall": wall,
    }
    bad = fixture_kind == "bad_composition"
    return object_map, _morphism_map_for_chain(
        category,
        carrier,
        complement,
        wall,
        bad_composite=bad,
    )


def _morphism_map_for_chain(
    category: SourceCategory,
    carrier: D1RestrictionSystem,
    mirror: D1RestrictionSystem,
    wall: D1RestrictionSystem,
    bad_composite: bool,
) -> dict[str, D1RestrictionMorphism]:
    morphism_map: dict[str, D1RestrictionMorphism] = {}
    object_by_id = {
        "carrier": carrier,
        "w_minus_mirror": mirror,
        "collective_wall": wall,
    }
    for morphism in category.morphisms:
        if morphism.identity:
            morphism_map[morphism.morphism_id] = make_identity(object_by_id[morphism.source])
    morphism_map["restrict_to_mirror"] = _make_aligned_morphism(
        "F_restrict_to_mirror",
        carrier,
        mirror,
        ("accessible_support", "holder_redundancy", "branch_support"),
    )
    morphism_map["restrict_to_wall"] = _make_aligned_morphism(
        "F_restrict_to_wall",
        mirror,
        wall,
        ("accessible_support",),
    )
    direct_dims = ("holder_redundancy",) if bad_composite else ("accessible_support",)
    morphism_map["restrict_to_wall_direct"] = _make_aligned_morphism(
        "F_restrict_to_wall_direct",
        carrier,
        wall,
        direct_dims,
    )
    return morphism_map


def _morphism_fingerprint(morphism: D1RestrictionMorphism) -> tuple[Any, ...]:
    return (
        morphism.source.name,
        morphism.target.name,
        tuple(sorted((sm.source_site, sm.target_site) for sm in morphism.site_map)),
        tuple(sorted(morphism.preserved_dimensions)),
    )


def _blocked_shortcuts(packet: AdapterPacket) -> tuple[str, ...]:
    blocked: list[str] = []
    if packet.requests_claim_movement:
        blocked.append("claim_movement")
    if packet.requests_public_posture_movement:
        blocked.append("public_posture_movement")
    if packet.requests_external_publication:
        blocked.append("external_publication")
    if packet.requests_cross_repo_truth_movement:
        blocked.append("cross_repo_truth_movement")
    if packet.depends_on_sibling_repo_truth:
        blocked.append("sibling_repo_truth_dependency")
    return tuple(blocked)


def _packet_dict(packet: AdapterPacket) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "description": packet.description,
        "source_category_declared": packet.source_category is not None,
        "target_fixture_kind": packet.target_fixture_kind,
        "declares_object_map": packet.declares_object_map,
        "declares_morphism_map": packet.declares_morphism_map,
        "maps_w_minus_to_collective_complement": (
            packet.maps_w_minus_to_collective_complement
        ),
        "requests_claim_movement": packet.requests_claim_movement,
        "requests_public_posture_movement": packet.requests_public_posture_movement,
        "requests_external_publication": packet.requests_external_publication,
        "requests_cross_repo_truth_movement": packet.requests_cross_repo_truth_movement,
        "depends_on_sibling_repo_truth": packet.depends_on_sibling_repo_truth,
    }


def _decision_dict(decision: AdapterDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "admitted": decision.admitted,
        "label": decision.label,
        "action": decision.action,
        "review_target_only": decision.review_target_only,
        "missing_requirements": list(decision.missing_requirements),
        "blocked_shortcuts": list(decision.blocked_shortcuts),
        "source_category_report": (
            None
            if decision.source_category_report is None
            else decision.source_category_report.__dict__
        ),
        "functor_report": (
            None
            if decision.functor_report is None
            else {
                **decision.functor_report.__dict__,
                "failed_composition_checks": list(
                    decision.functor_report.failed_composition_checks
                ),
            }
        ),
        "strongest_allowed_reading": decision.strongest_allowed_reading,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
