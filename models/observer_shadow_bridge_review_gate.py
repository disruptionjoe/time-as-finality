"""T475: bridge-review gate for observer-shadow packets.

T474 admits only an audit-atlas bridge between typed-transport and LossKernel
packet families. This follow-up asks whether that bridge can support a concrete
cross-family review packet without becoming direct composition, semantic
relabeling, absorber completion, or category/fibration evidence.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.observer_shadow_bridge_admission_gate import run_t474_analysis


ARTIFACT_ID = "T475-observer-shadow-bridge-review-gate-v0.1"
VERDICT = "BRIDGE_REVIEW_GATE_BUILT_REVIEW_METADATA_ONLY_NO_CATEGORY"


@dataclass(frozen=True)
class BridgeReviewPacket:
    """A concrete cross-family review packet after T474."""

    packet_id: str
    bridge_proposal_id: str
    source_family: str
    target_family: str
    family_specific_shadows_preserved: bool
    family_specific_capability_objects_preserved: bool
    native_comparisons_preserved: bool
    required_review_controls: tuple[str, ...]
    supplied_review_controls: tuple[str, ...]
    uses_semantic_mapping: bool
    uses_absorber_completion: bool
    uses_direct_composition: bool
    identifies_family_capability_objects: bool
    claims_category_evidence: bool
    intended_use: str


@dataclass(frozen=True)
class BridgeReviewDecision:
    """Admission decision for a bridge-review packet."""

    packet_id: str
    bridge_proposal_id: str
    admitted: bool
    route_label: str
    classification: str
    missing_review_controls: tuple[str, ...]
    counts_as_cross_family_review: bool
    counts_as_direct_composition: bool
    counts_as_category_evidence: bool
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T475Result:
    """Complete T475 bridge-review gate result."""

    packets: tuple[BridgeReviewPacket, ...]
    decisions: tuple[BridgeReviewDecision, ...]
    verdict: str
    claim_ledger_update: str
    admitted_review_packets: tuple[str, ...]
    rejected_review_packets: tuple[str, ...]
    t474_admitted_bridge_available: bool
    cross_family_review_supported: bool
    direct_cross_family_composition_supported: bool
    global_category_theorem_supported: bool
    strongest_reading: str
    future_packet_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t475_analysis() -> T475Result:
    """Run the finite observer-shadow bridge-review gate."""

    t474 = run_t474_analysis()
    available_controls = {
        control.control_id for control in t474.controls if control.available
    }
    bridge_admissions = {
        admission.proposal_id: admission for admission in t474.admissions
    }
    packets = _review_packets()
    decisions = tuple(
        _evaluate_packet(packet, bridge_admissions, available_controls)
        for packet in packets
    )
    admitted = tuple(
        decision.packet_id for decision in decisions if decision.admitted
    )
    rejected = tuple(
        decision.packet_id for decision in decisions if not decision.admitted
    )

    return T475Result(
        packets=packets,
        decisions=decisions,
        verdict=VERDICT,
        claim_ledger_update="none",
        admitted_review_packets=admitted,
        rejected_review_packets=rejected,
        t474_admitted_bridge_available=t474.atlas_bridge_available,
        cross_family_review_supported=admitted == ("audit_atlas_review_packet",),
        direct_cross_family_composition_supported=False,
        global_category_theorem_supported=False,
        strongest_reading=(
            "T475 shows that the T474 audit-atlas bridge can support one "
            "concrete cross-family review packet only as verdict/control "
            "metadata. The review must preserve family-specific shadows, "
            "capability objects, and native comparisons. It cannot identify "
            "typed-transport PO1 evidence with LossKernel obligations, cannot "
            "use absorber completion as a bridge, and cannot count as direct "
            "composition or category evidence."
        ),
        future_packet_minimum=(
            "cite an admitted T474 audit-atlas bridge",
            "preserve source and target family shadows separately",
            "preserve source and target capability objects separately",
            "preserve native comparisons separately",
            "supply both positive family controls and hostile bridge controls",
            "state that the packet is review metadata rather than direct composition",
            "block category or fibration language unless direct cross-family preservation is proved",
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


def _review_packets() -> tuple[BridgeReviewPacket, ...]:
    required = (
        "transport_bookkeeping_positive",
        "losskernel_preservation_positive",
        "no_bridge_hostile",
        "upstream_rejection_hostile",
        "absorber_completion_hostile",
    )

    return (
        BridgeReviewPacket(
            packet_id="no_admitted_bridge_review_packet",
            bridge_proposal_id="no_declared_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=False,
            family_specific_capability_objects_preserved=False,
            native_comparisons_preserved=False,
            required_review_controls=required,
            supplied_review_controls=(),
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            uses_direct_composition=True,
            identifies_family_capability_objects=True,
            claims_category_evidence=True,
            intended_use="review by composing unlike packets without an admitted bridge",
        ),
        BridgeReviewPacket(
            packet_id="semantic_review_packet",
            bridge_proposal_id="semantic_keyword_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=False,
            family_specific_capability_objects_preserved=False,
            native_comparisons_preserved=False,
            required_review_controls=required,
            supplied_review_controls=required,
            uses_semantic_mapping=True,
            uses_absorber_completion=False,
            uses_direct_composition=False,
            identifies_family_capability_objects=False,
            claims_category_evidence=False,
            intended_use="review by shared words such as loss or forgetting",
        ),
        BridgeReviewPacket(
            packet_id="absorber_completion_review_packet",
            bridge_proposal_id="absorber_completion_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=False,
            family_specific_capability_objects_preserved=False,
            native_comparisons_preserved=False,
            required_review_controls=required,
            supplied_review_controls=required,
            uses_semantic_mapping=False,
            uses_absorber_completion=True,
            uses_direct_composition=False,
            identifies_family_capability_objects=False,
            claims_category_evidence=False,
            intended_use="review by completing hidden source state first",
        ),
        BridgeReviewPacket(
            packet_id="direct_composition_review_packet",
            bridge_proposal_id="audit_atlas_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=True,
            family_specific_capability_objects_preserved=False,
            native_comparisons_preserved=False,
            required_review_controls=required,
            supplied_review_controls=required,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            uses_direct_composition=True,
            identifies_family_capability_objects=True,
            claims_category_evidence=True,
            intended_use="turn admitted bridge metadata into direct category composition",
        ),
        BridgeReviewPacket(
            packet_id="control_incomplete_review_packet",
            bridge_proposal_id="audit_atlas_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=True,
            family_specific_capability_objects_preserved=True,
            native_comparisons_preserved=True,
            required_review_controls=required,
            supplied_review_controls=(
                "transport_bookkeeping_positive",
                "losskernel_preservation_positive",
            ),
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            uses_direct_composition=False,
            identifies_family_capability_objects=False,
            claims_category_evidence=False,
            intended_use="review using positives but no hostile bridge controls",
        ),
        BridgeReviewPacket(
            packet_id="capability_identification_review_packet",
            bridge_proposal_id="audit_atlas_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=True,
            family_specific_capability_objects_preserved=False,
            native_comparisons_preserved=True,
            required_review_controls=required,
            supplied_review_controls=required,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            uses_direct_composition=False,
            identifies_family_capability_objects=True,
            claims_category_evidence=False,
            intended_use="review by identifying PO1 evidence with witness obligations",
        ),
        BridgeReviewPacket(
            packet_id="audit_atlas_review_packet",
            bridge_proposal_id="audit_atlas_bridge_packet",
            source_family="typed_transport",
            target_family="losskernel",
            family_specific_shadows_preserved=True,
            family_specific_capability_objects_preserved=True,
            native_comparisons_preserved=True,
            required_review_controls=required,
            supplied_review_controls=required,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            uses_direct_composition=False,
            identifies_family_capability_objects=False,
            claims_category_evidence=False,
            intended_use="compare route labels and control status as audit-atlas metadata",
        ),
    )


def _evaluate_packet(
    packet: BridgeReviewPacket,
    bridge_admissions: dict[str, Any],
    available_controls: set[str],
) -> BridgeReviewDecision:
    bridge = bridge_admissions[packet.bridge_proposal_id]
    missing = tuple(
        control
        for control in packet.required_review_controls
        if control not in packet.supplied_review_controls
        or control not in available_controls
    )
    notes: list[str] = []

    if not bridge.admitted:
        route = "reject_upstream_bridge_not_admitted"
        admitted = False
        notes.append("T474 rejected the named bridge proposal")
    elif missing:
        route = "reject_missing_review_controls"
        admitted = False
        notes.append("review packet omits required positive or hostile controls")
    elif packet.uses_semantic_mapping:
        route = "reject_semantic_review_mapping"
        admitted = False
        notes.append("semantic similarity is not a typed cross-family review relation")
    elif packet.uses_absorber_completion:
        route = "reject_absorber_completion_review"
        admitted = False
        notes.append("absorber completion remains state-completion bookkeeping")
    elif packet.uses_direct_composition or packet.claims_category_evidence:
        route = "reject_direct_composition_or_category_review"
        admitted = False
        notes.append("audit-atlas metadata does not supply direct composition")
    elif packet.identifies_family_capability_objects:
        route = "reject_capability_object_identification"
        admitted = False
        notes.append("family-specific capability objects must remain distinct")
    elif (
        not packet.family_specific_shadows_preserved
        or not packet.family_specific_capability_objects_preserved
        or not packet.native_comparisons_preserved
    ):
        route = "reject_underdeclared_family_boundaries"
        admitted = False
        notes.append("review packet does not preserve family-specific boundaries")
    else:
        route = "admit_review_metadata_only"
        admitted = True
        notes.append("packet is admitted only as cross-family review metadata")
        notes.append("shadows, capability objects, and native comparisons stay separate")

    classification = _classification_for_route(route)

    return BridgeReviewDecision(
        packet_id=packet.packet_id,
        bridge_proposal_id=packet.bridge_proposal_id,
        admitted=admitted,
        route_label=route,
        classification=classification,
        missing_review_controls=missing,
        counts_as_cross_family_review=route == "admit_review_metadata_only",
        counts_as_direct_composition=False,
        counts_as_category_evidence=False,
        notes=tuple(notes),
    )


def _classification_for_route(route: str) -> str:
    if route == "admit_review_metadata_only":
        return "review_metadata_admitted_no_category_evidence"
    if route == "reject_upstream_bridge_not_admitted":
        return "upstream_bridge_rejection"
    if route == "reject_missing_review_controls":
        return "control_incomplete_rejection"
    if route == "reject_semantic_review_mapping":
        return "semantic_relabel_rejection"
    if route == "reject_absorber_completion_review":
        return "absorber_completion_rejection"
    if route == "reject_direct_composition_or_category_review":
        return "direct_composition_rejection"
    if route == "reject_capability_object_identification":
        return "capability_identification_rejection"
    if route == "reject_underdeclared_family_boundaries":
        return "underdeclared_family_boundary_rejection"
    return "unclassified_review_route"


def t475_result_to_dict(result: T475Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "packets": [_packet_to_dict(packet) for packet in result.packets],
        "decisions": [_decision_to_dict(decision) for decision in result.decisions],
        "claim_ledger_update": result.claim_ledger_update,
        "admitted_review_packets": list(result.admitted_review_packets),
        "rejected_review_packets": list(result.rejected_review_packets),
        "t474_admitted_bridge_available": result.t474_admitted_bridge_available,
        "cross_family_review_supported": result.cross_family_review_supported,
        "direct_cross_family_composition_supported": (
            result.direct_cross_family_composition_supported
        ),
        "global_category_theorem_supported": result.global_category_theorem_supported,
        "strongest_reading": result.strongest_reading,
        "future_packet_minimum": list(result.future_packet_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T475Result) -> str:
    decision_rows = []
    for decision in result.decisions:
        missing = ", ".join(decision.missing_review_controls) or "none"
        notes = "; ".join(decision.notes) or "none"
        decision_rows.append(
            "| {packet_id} | {bridge} | {admitted} | {route} | {classification} | "
            "{missing} | {review} | {category} | {notes} |".format(
                packet_id=decision.packet_id,
                bridge=decision.bridge_proposal_id,
                admitted=decision.admitted,
                route=decision.route_label,
                classification=decision.classification,
                missing=missing,
                review=decision.counts_as_cross_family_review,
                category=decision.counts_as_category_evidence,
                notes=notes,
            )
        )

    minimum = [f"- {item}" for item in result.future_packet_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T475 - Observer-Shadow Bridge Review Gate - v0.1 results",
            "",
            "> Bridge-review guardrail only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T475-observer-shadow-bridge-review-gate.md`",
            "- Model: `models/observer_shadow_bridge_review_gate.py`",
            "- Tests: `tests/test_observer_shadow_bridge_review_gate.py`",
            "- Artifact JSON: `results/T475-observer-shadow-bridge-review-gate-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Prior gates: T470, T472, T473, and T474",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Review Packet Decisions",
            "",
            "| packet | bridge proposal | admitted? | route | classification | missing controls | counts as review? | category evidence? | notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
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


def _packet_to_dict(packet: BridgeReviewPacket) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "bridge_proposal_id": packet.bridge_proposal_id,
        "source_family": packet.source_family,
        "target_family": packet.target_family,
        "family_specific_shadows_preserved": packet.family_specific_shadows_preserved,
        "family_specific_capability_objects_preserved": (
            packet.family_specific_capability_objects_preserved
        ),
        "native_comparisons_preserved": packet.native_comparisons_preserved,
        "required_review_controls": list(packet.required_review_controls),
        "supplied_review_controls": list(packet.supplied_review_controls),
        "uses_semantic_mapping": packet.uses_semantic_mapping,
        "uses_absorber_completion": packet.uses_absorber_completion,
        "uses_direct_composition": packet.uses_direct_composition,
        "identifies_family_capability_objects": packet.identifies_family_capability_objects,
        "claims_category_evidence": packet.claims_category_evidence,
        "intended_use": packet.intended_use,
    }


def _decision_to_dict(decision: BridgeReviewDecision) -> dict[str, Any]:
    return {
        "packet_id": decision.packet_id,
        "bridge_proposal_id": decision.bridge_proposal_id,
        "admitted": decision.admitted,
        "route_label": decision.route_label,
        "classification": decision.classification,
        "missing_review_controls": list(decision.missing_review_controls),
        "counts_as_cross_family_review": decision.counts_as_cross_family_review,
        "counts_as_direct_composition": decision.counts_as_direct_composition,
        "counts_as_category_evidence": decision.counts_as_category_evidence,
        "notes": list(decision.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t475_analysis()
    payload = t475_result_to_dict(result)
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
