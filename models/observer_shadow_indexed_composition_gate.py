"""T473: indexed-composition gate for observer-shadow packets.

T470 found that observer-shadow comparison needs load-bearing indices. T472
made index admission executable. This follow-up asks whether the admitted
indexed bookkeeping composes in finite controls, while blocking absorber
completion and cross-family bridge shortcuts from becoming category evidence.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.observer_shadow_composition_gate import run_t470_analysis
from models.observer_shadow_index_admission_gate import run_t472_analysis
from models.transport_network import _compose_morphisms, _make_layer, _make_transport
from models.multiscale_observer_field import D1Profile


ARTIFACT_ID = "T473-observer-shadow-indexed-composition-gate-v0.1"
VERDICT = "INDEXED_COMPOSITION_GATE_BUILT_ASSOCIATIVE_BOOKKEEPING_ONLY"


@dataclass(frozen=True)
class TransportCompositionFixture:
    """Finite transport composition associativity check."""

    fixture_id: str
    left_signature: tuple[str, ...]
    right_signature: tuple[str, ...]
    left_forgotten_index: tuple[str, ...]
    right_forgotten_index: tuple[str, ...]
    structurally_associative: bool
    forgotten_index_associative: bool
    classification: str
    category_evidence: bool
    notes: tuple[str, ...]


@dataclass(frozen=True)
class CompositionAtom:
    """Route atom inherited from a T472 packet decision."""

    atom_id: str
    packet_id: str
    family: str
    route_label: str
    admitted: bool
    declared_indices: tuple[str, ...]
    evidence_kind: str


@dataclass(frozen=True)
class CompositionProduct:
    """A product of route atoms under the T473 route algebra."""

    atom_ids: tuple[str, ...]
    families: tuple[str, ...]
    route_label: str
    admitted: bool
    declared_indices: tuple[str, ...]
    evidence_kind: str
    counts_as_preservation_control: bool
    category_evidence: bool
    notes: tuple[str, ...]


@dataclass(frozen=True)
class RouteCompositionCase:
    """Associativity and routing decision for a finite composition case."""

    case_id: str
    atom_ids: tuple[str, ...]
    left_route: str
    right_route: str
    association_invariant: bool
    final_route: str
    admitted: bool
    counts_as_preservation_control: bool
    category_evidence: bool
    classification: str
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T473Result:
    """Complete T473 indexed-composition gate result."""

    transport_fixture: TransportCompositionFixture
    atoms: tuple[CompositionAtom, ...]
    route_cases: tuple[RouteCompositionCase, ...]
    verdict: str
    claim_ledger_update: str
    indexed_bookkeeping_associative_in_fixture: bool
    cross_family_composition_supported: bool
    absorber_completion_category_evidence: bool
    global_category_theorem_supported: bool
    strongest_reading: str
    future_packet_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t473_analysis() -> T473Result:
    """Run the finite indexed-composition gate."""

    transport_fixture = _transport_composition_fixture()
    atoms = _composition_atoms()
    atom_map = {atom.atom_id: atom for atom in atoms}
    route_cases = tuple(
        _route_case(case_id, tuple(atom_map[atom_id] for atom_id in atom_ids))
        for case_id, atom_ids in (
            (
                "transport_indexed_bookkeeping_threefold",
                (
                    "transport_path_indexed",
                    "transport_path_indexed",
                    "transport_path_indexed",
                ),
            ),
            (
                "losskernel_preservation_threefold",
                (
                    "losskernel_neighbor_preservation",
                    "losskernel_neighbor_preservation",
                    "losskernel_neighbor_preservation",
                ),
            ),
            (
                "losskernel_absorber_taints_composition",
                (
                    "losskernel_neighbor_preservation",
                    "losskernel_hidden_source_completed",
                    "losskernel_neighbor_preservation",
                ),
            ),
            (
                "endpoint_rejection_blocks_composition",
                (
                    "transport_endpoint_only",
                    "transport_path_indexed",
                ),
            ),
            (
                "cross_family_bridge_missing",
                (
                    "transport_path_indexed",
                    "losskernel_neighbor_preservation",
                ),
            ),
        )
    )

    return T473Result(
        transport_fixture=transport_fixture,
        atoms=atoms,
        route_cases=route_cases,
        verdict=VERDICT,
        claim_ledger_update="none",
        indexed_bookkeeping_associative_in_fixture=(
            transport_fixture.structurally_associative
            and transport_fixture.forgotten_index_associative
            and _case(route_cases, "transport_indexed_bookkeeping_threefold").association_invariant
        ),
        cross_family_composition_supported=False,
        absorber_completion_category_evidence=False,
        global_category_theorem_supported=False,
        strongest_reading=(
            "T473 finds finite associativity for the current indexed transport "
            "bookkeeping and for repeated LossKernel preservation controls, but "
            "only as a route gate. Absorber completion taints a composition as "
            "state-completion bookkeeping, rejected upstream packets stay "
            "blocked, and cross-family composition has no declared bridge. This "
            "supports an indexed audit-atlas guardrail, not an observer-shadow "
            "category or fibration theorem."
        ),
        future_packet_minimum=(
            "declare source and target family before composing observer-shadow packets",
            "prove or test associativity for the declared indices rather than assuming it",
            "separate finite preservation-control composition from indexed bookkeeping",
            "route any absorber completion outside category evidence",
            "supply an explicit cross-family bridge before composing transport and LossKernel-style packets",
        ),
        not_earned=(
            "observer-shadow category theorem",
            "indexed category or fibration theorem",
            "North Star geometry proof",
            "D1, PO1, TF1, or LossKernel promotion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "roadmap movement",
            "public-posture movement",
        ),
    )


def _transport_composition_fixture() -> TransportCompositionFixture:
    profile_rich = D1Profile(
        accessible_support=3,
        holder_redundancy=2,
        branch_support=2,
        reversal_cost=2,
    )
    profile_restricted = D1Profile(
        accessible_support=1,
        holder_redundancy=2,
        branch_support=2,
        reversal_cost=2,
    )
    layer_a = _make_layer("A", "a", profile_rich, obstructed=False)
    layer_b = _make_layer("B", "b", profile_restricted, obstructed=False)
    layer_c = _make_layer("C", "c", profile_restricted, obstructed=False)
    layer_d = _make_layer("D", "d", profile_restricted, obstructed=True)

    transport_ab = _make_transport(
        "A_to_B",
        layer_a,
        layer_b,
        forgotten=("type_guarantee",),
    )
    transport_bc = _make_transport(
        "B_to_C",
        layer_b,
        layer_c,
        forgotten=("branch_support",),
    )
    transport_cd = _make_transport(
        "C_to_D",
        layer_c,
        layer_d,
        forgotten=("reversal_cost",),
    )

    left = _compose_morphisms(
        _compose_morphisms(transport_ab.morphism, transport_bc.morphism),
        transport_cd.morphism,
    )
    right = _compose_morphisms(
        transport_ab.morphism,
        _compose_morphisms(transport_bc.morphism, transport_cd.morphism),
    )
    left_signature = _morphism_signature(left)
    right_signature = _morphism_signature(right)
    left_forgotten = _ordered_union(
        _ordered_union(transport_ab.forgotten_structure, transport_bc.forgotten_structure),
        transport_cd.forgotten_structure,
    )
    right_forgotten = _ordered_union(
        transport_ab.forgotten_structure,
        _ordered_union(transport_bc.forgotten_structure, transport_cd.forgotten_structure),
    )
    structurally_associative = left_signature == right_signature
    forgotten_index_associative = left_forgotten == right_forgotten

    return TransportCompositionFixture(
        fixture_id="three_step_transport_index_fixture",
        left_signature=left_signature,
        right_signature=right_signature,
        left_forgotten_index=left_forgotten,
        right_forgotten_index=right_forgotten,
        structurally_associative=structurally_associative,
        forgotten_index_associative=forgotten_index_associative,
        classification=(
            "finite_indexed_transport_composition_associative"
            if structurally_associative and forgotten_index_associative
            else "finite_indexed_transport_composition_obstruction"
        ),
        category_evidence=False,
        notes=(
            "checks the current D1 morphism core up to structural fields, not morphism names",
            "forgotten-structure index accumulation is association-invariant in this finite fixture",
            "finite associativity is bookkeeping support only, not a category theorem",
        ),
    )


def _composition_atoms() -> tuple[CompositionAtom, ...]:
    t470 = run_t470_analysis()
    t472 = run_t472_analysis()
    checks = {check.check_id: check for check in t470.checks}
    packets = {packet.packet_id: packet for packet in t472.packets}
    admissions = {admission.packet_id: admission for admission in t472.admissions}

    return (
        _atom(
            "transport_endpoint_only",
            "transport_endpoint_only_packet",
            packets,
            admissions,
            checks,
        ),
        _atom(
            "transport_path_indexed",
            "transport_path_indexed_packet",
            packets,
            admissions,
            checks,
        ),
        _atom(
            "losskernel_neighbor_preservation",
            "losskernel_neighbor_preservation_packet",
            packets,
            admissions,
            checks,
        ),
        _atom(
            "losskernel_hidden_source_completed",
            "losskernel_hidden_source_completed_packet",
            packets,
            admissions,
            checks,
        ),
    )


def _atom(
    atom_id: str,
    packet_id: str,
    packets: dict[str, Any],
    admissions: dict[str, Any],
    checks: dict[str, Any],
) -> CompositionAtom:
    packet = packets[packet_id]
    admission = admissions[packet_id]
    check = checks[packet.check_id]
    if not admission.admitted:
        evidence_kind = "rejected"
    elif admission.route_label == "admitted_preservation_control":
        evidence_kind = "preservation_control"
    elif admission.route_label == "admitted_indexed_completion":
        evidence_kind = "indexed_bookkeeping"
    elif admission.route_label == "absorber_completion_recorded":
        evidence_kind = "absorber_completion"
    else:
        evidence_kind = "unclassified"
    return CompositionAtom(
        atom_id=atom_id,
        packet_id=packet_id,
        family=check.family,
        route_label=admission.route_label,
        admitted=admission.admitted,
        declared_indices=packet.declared_indices,
        evidence_kind=evidence_kind,
    )


def _route_case(case_id: str, atoms: tuple[CompositionAtom, ...]) -> RouteCompositionCase:
    if len(atoms) == 2:
        left = _compose_products(_product_from_atom(atoms[0]), _product_from_atom(atoms[1]))
        right = left
    elif len(atoms) == 3:
        left = _compose_products(
            _compose_products(_product_from_atom(atoms[0]), _product_from_atom(atoms[1])),
            _product_from_atom(atoms[2]),
        )
        right = _compose_products(
            _product_from_atom(atoms[0]),
            _compose_products(_product_from_atom(atoms[1]), _product_from_atom(atoms[2])),
        )
    else:
        raise ValueError("T473 route cases use two or three atoms")

    association_invariant = _product_signature(left) == _product_signature(right)
    final = left
    classification = _classify_product(final, association_invariant)
    notes = final.notes
    if not association_invariant:
        notes = notes + ("left and right association routes differ",)

    return RouteCompositionCase(
        case_id=case_id,
        atom_ids=tuple(atom.atom_id for atom in atoms),
        left_route=left.route_label,
        right_route=right.route_label,
        association_invariant=association_invariant,
        final_route=final.route_label,
        admitted=final.admitted,
        counts_as_preservation_control=final.counts_as_preservation_control,
        category_evidence=final.category_evidence,
        classification=classification,
        notes=notes,
    )


def _compose_products(left: CompositionProduct, right: CompositionProduct) -> CompositionProduct:
    atom_ids = left.atom_ids + right.atom_ids
    families = _ordered_union(left.families, right.families)
    declared_indices = _ordered_union(left.declared_indices, right.declared_indices)
    notes: list[str] = list(left.notes + right.notes)

    if not left.admitted or not right.admitted:
        route = "reject_unadmitted_packet"
        admitted = False
        evidence_kind = "rejected"
        counts_as_preservation_control = False
        notes.append("composition contains a packet rejected by T472")
    elif len(families) > 1:
        route = "reject_no_cross_family_bridge"
        admitted = False
        evidence_kind = "bridge_missing"
        counts_as_preservation_control = False
        notes.append("no cross-family bridge has been declared for this composition")
    elif left.evidence_kind == "absorber_completion" or right.evidence_kind == "absorber_completion":
        route = "absorber_completion_route"
        admitted = True
        evidence_kind = "absorber_completion"
        counts_as_preservation_control = False
        notes.append("absorber completion remains state-completion bookkeeping")
    elif left.evidence_kind == "indexed_bookkeeping" or right.evidence_kind == "indexed_bookkeeping":
        route = "indexed_bookkeeping_route"
        admitted = True
        evidence_kind = "indexed_bookkeeping"
        counts_as_preservation_control = False
        notes.append("declared indices compose as bookkeeping only")
    elif left.evidence_kind == "preservation_control" and right.evidence_kind == "preservation_control":
        route = "preservation_control_route"
        admitted = True
        evidence_kind = "preservation_control"
        counts_as_preservation_control = True
        notes.append("finite preservation controls compose within one family")
    else:
        route = "reject_unclassified_route"
        admitted = False
        evidence_kind = "rejected"
        counts_as_preservation_control = False
        notes.append("composition route is not classified by T473")

    return CompositionProduct(
        atom_ids=atom_ids,
        families=families,
        route_label=route,
        admitted=admitted,
        declared_indices=declared_indices,
        evidence_kind=evidence_kind,
        counts_as_preservation_control=counts_as_preservation_control,
        category_evidence=False,
        notes=tuple(dict.fromkeys(notes)),
    )


def _product_from_atom(atom: CompositionAtom) -> CompositionProduct:
    return CompositionProduct(
        atom_ids=(atom.atom_id,),
        families=(atom.family,),
        route_label=atom.route_label,
        admitted=atom.admitted,
        declared_indices=atom.declared_indices,
        evidence_kind=atom.evidence_kind,
        counts_as_preservation_control=atom.evidence_kind == "preservation_control",
        category_evidence=False,
        notes=(),
    )


def _classify_product(product: CompositionProduct, association_invariant: bool) -> str:
    if not association_invariant:
        return "association_obstruction"
    if product.route_label == "indexed_bookkeeping_route":
        return "associative_indexed_bookkeeping_only"
    if product.route_label == "preservation_control_route":
        return "associative_finite_preservation_control"
    if product.route_label == "absorber_completion_route":
        return "absorber_completion_blocks_category_evidence"
    if product.route_label == "reject_unadmitted_packet":
        return "blocked_by_t472_rejection"
    if product.route_label == "reject_no_cross_family_bridge":
        return "blocked_by_missing_cross_family_bridge"
    return "unclassified"


def _product_signature(product: CompositionProduct) -> tuple[object, ...]:
    return (
        product.families,
        product.route_label,
        product.admitted,
        product.declared_indices,
        product.evidence_kind,
        product.counts_as_preservation_control,
        product.category_evidence,
    )


def _morphism_signature(morphism: Any) -> tuple[str, ...]:
    site_map = tuple(f"{item.source_site}->{item.target_site}" for item in morphism.site_map)
    return (
        f"source:{morphism.source.name}",
        f"target:{morphism.target.name}",
        "site_map:" + ",".join(site_map),
        "preserved:" + ",".join(morphism.preserved_dimensions),
    )


def _ordered_union(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    output: list[str] = []
    for item in left + right:
        if item not in seen:
            seen.add(item)
            output.append(item)
    return tuple(output)


def _case(cases: tuple[RouteCompositionCase, ...], case_id: str) -> RouteCompositionCase:
    return next(case for case in cases if case.case_id == case_id)


def t473_result_to_dict(result: T473Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "transport_fixture": _transport_fixture_to_dict(result.transport_fixture),
        "atoms": [_atom_to_dict(atom) for atom in result.atoms],
        "route_cases": [_route_case_to_dict(case) for case in result.route_cases],
        "claim_ledger_update": result.claim_ledger_update,
        "indexed_bookkeeping_associative_in_fixture": result.indexed_bookkeeping_associative_in_fixture,
        "cross_family_composition_supported": result.cross_family_composition_supported,
        "absorber_completion_category_evidence": result.absorber_completion_category_evidence,
        "global_category_theorem_supported": result.global_category_theorem_supported,
        "strongest_reading": result.strongest_reading,
        "future_packet_minimum": list(result.future_packet_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T473Result) -> str:
    fixture = result.transport_fixture
    route_rows = []
    for case in result.route_cases:
        route_rows.append(
            "| {case_id} | {left_route} | {right_route} | {invariant} | {final_route} | {classification} | {category} |".format(
                case_id=case.case_id,
                left_route=case.left_route,
                right_route=case.right_route,
                invariant=case.association_invariant,
                final_route=case.final_route,
                classification=case.classification,
                category=case.category_evidence,
            )
        )

    minimum = [f"- {item}" for item in result.future_packet_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T473 - Observer-Shadow Indexed Composition Gate - v0.1 results",
            "",
            "> Indexed-composition guardrail only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T473-observer-shadow-indexed-composition-gate.md`",
            "- Model: `models/observer_shadow_indexed_composition_gate.py`",
            "- Tests: `tests/test_observer_shadow_indexed_composition_gate.py`",
            "- Artifact JSON: `results/T473-observer-shadow-indexed-composition-gate-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Prior gates: T470 and T472",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Transport Composition Fixture",
            "",
            f"- fixture: `{fixture.fixture_id}`",
            f"- structurally associative: `{fixture.structurally_associative}`",
            f"- forgotten-index associative: `{fixture.forgotten_index_associative}`",
            f"- classification: `{fixture.classification}`",
            f"- category evidence: `{fixture.category_evidence}`",
            "",
            "## Route Composition Cases",
            "",
            "| case | left route | right route | association invariant? | final route | classification | category evidence? |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *route_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _transport_fixture_to_dict(fixture: TransportCompositionFixture) -> dict[str, Any]:
    return {
        "fixture_id": fixture.fixture_id,
        "left_signature": list(fixture.left_signature),
        "right_signature": list(fixture.right_signature),
        "left_forgotten_index": list(fixture.left_forgotten_index),
        "right_forgotten_index": list(fixture.right_forgotten_index),
        "structurally_associative": fixture.structurally_associative,
        "forgotten_index_associative": fixture.forgotten_index_associative,
        "classification": fixture.classification,
        "category_evidence": fixture.category_evidence,
        "notes": list(fixture.notes),
    }


def _atom_to_dict(atom: CompositionAtom) -> dict[str, Any]:
    return {
        "atom_id": atom.atom_id,
        "packet_id": atom.packet_id,
        "family": atom.family,
        "route_label": atom.route_label,
        "admitted": atom.admitted,
        "declared_indices": list(atom.declared_indices),
        "evidence_kind": atom.evidence_kind,
    }


def _route_case_to_dict(case: RouteCompositionCase) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "atom_ids": list(case.atom_ids),
        "left_route": case.left_route,
        "right_route": case.right_route,
        "association_invariant": case.association_invariant,
        "final_route": case.final_route,
        "admitted": case.admitted,
        "counts_as_preservation_control": case.counts_as_preservation_control,
        "category_evidence": case.category_evidence,
        "classification": case.classification,
        "notes": list(case.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t473_analysis()
    payload = t473_result_to_dict(result)
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
