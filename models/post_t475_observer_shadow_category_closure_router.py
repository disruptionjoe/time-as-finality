"""T476: post-T475 closure router for observer-shadow category work.

T470-T475 built an indexed audit-atlas chain for observer-shadow packets, but
each gate blocked category, fibration, and direct cross-family composition
readings. This router closes the current packet class against minor restarts
while admitting only genuinely new evidence targets for future review.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models.observer_shadow_bridge_review_gate import run_t475_analysis


ARTIFACT_ID = "T476-post-t475-observer-shadow-category-closure-router-v0.1"
VERDICT = "POST_T475_OBSERVER_SHADOW_CATEGORY_THREAD_CLOSED_NEW_EVIDENCE_ONLY"


@dataclass(frozen=True)
class ClosureProposal:
    """A proposed post-T475 restart or future review packet."""

    proposal_id: str
    proposal_kind: str
    repeats_current_t470_t475_packet_class: bool
    preserves_family_boundaries: bool
    supplies_positive_family_controls: bool
    supplies_hostile_bridge_controls: bool
    has_independent_direct_preservation_proof: bool
    declares_formal_category_semantics: bool
    introduces_new_packet_family: bool
    supplies_new_family_index_controls: bool
    uses_t475_review_metadata_as_proof: bool
    uses_semantic_mapping: bool
    uses_absorber_completion: bool
    identifies_family_capability_objects: bool
    claims_category_or_fibration_evidence: bool
    seeks_claim_or_public_posture_movement: bool
    intended_use: str


@dataclass(frozen=True)
class ClosureDecision:
    """Router decision for a post-T475 proposal."""

    proposal_id: str
    admitted: bool
    route_label: str
    classification: str
    admitted_as_future_review_target: bool
    counts_as_category_evidence: bool
    closes_current_thread: bool
    missing_requirements: tuple[str, ...]
    notes: tuple[str, ...]


@dataclass(frozen=True)
class T476Result:
    """Complete T476 closure-router result."""

    proposals: tuple[ClosureProposal, ...]
    decisions: tuple[ClosureDecision, ...]
    verdict: str
    claim_ledger_update: str
    t475_review_metadata_available: bool
    current_thread_closed: bool
    admitted_future_targets: tuple[str, ...]
    rejected_restart_packets: tuple[str, ...]
    direct_cross_family_composition_supported: bool
    global_category_theorem_supported: bool
    strongest_reading: str
    future_reopen_minimum: tuple[str, ...]
    not_earned: tuple[str, ...]


def run_t476_analysis() -> T476Result:
    """Run the post-T475 observer-shadow closure router."""

    t475 = run_t475_analysis()
    t475_review_metadata_available = (
        t475.cross_family_review_supported
        and t475.admitted_review_packets == ("audit_atlas_review_packet",)
        and not t475.direct_cross_family_composition_supported
        and not t475.global_category_theorem_supported
    )
    proposals = _closure_proposals()
    decisions = tuple(
        _evaluate_proposal(proposal, t475_review_metadata_available)
        for proposal in proposals
    )
    admitted_future_targets = tuple(
        decision.proposal_id
        for decision in decisions
        if decision.admitted_as_future_review_target
    )
    rejected_restart_packets = tuple(
        decision.proposal_id for decision in decisions if not decision.admitted
    )
    current_thread_closed = (
        t475_review_metadata_available
        and all(
            decision.closes_current_thread
            for decision in decisions
            if _proposal_by_id(proposals, decision.proposal_id)
            .repeats_current_t470_t475_packet_class
        )
        and not any(decision.counts_as_category_evidence for decision in decisions)
    )

    return T476Result(
        proposals=proposals,
        decisions=decisions,
        verdict=VERDICT,
        claim_ledger_update="none",
        t475_review_metadata_available=t475_review_metadata_available,
        current_thread_closed=current_thread_closed,
        admitted_future_targets=admitted_future_targets,
        rejected_restart_packets=rejected_restart_packets,
        direct_cross_family_composition_supported=False,
        global_category_theorem_supported=False,
        strongest_reading=(
            "T476 closes the current T470-T475 observer-shadow category thread "
            "against minor restarts. T475 supplies review metadata only; it is "
            "not direct preservation, not category evidence, and not a fibration "
            "argument. Future work can reopen the surface only by bringing an "
            "independent direct cross-family preservation proof with formal "
            "semantics, or by introducing a new packet family with its own "
            "index, bridge, review, positive-control, and hostile-control gates."
        ),
        future_reopen_minimum=(
            "cite T470-T475 and state why the current packet class is insufficient",
            "declare source and target packet families before comparison",
            "preserve family-specific shadows and capability objects separately",
            "preserve native comparisons separately",
            "supply positive controls from each family",
            "supply hostile controls for no-bridge, semantic, absorber-completion, and capability-identification shortcuts",
            "for category or fibration language, provide independent direct preservation proof plus formal semantics",
            "for a new family, provide its own index-admission, bridge-admission, and bridge-review controls",
            "keep claim status, public posture, North Star, roadmap, README, and hard policy unchanged unless separately earned and authorized",
        ),
        not_earned=(
            "observer-shadow category theorem",
            "indexed category or fibration theorem",
            "direct typed-transport/LossKernel composition theorem",
            "North Star geometry proof",
            "D1, PO1, TF1, or LossKernel promotion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "hard-policy movement",
            "public-posture movement",
            "cross-repo truth movement",
        ),
    )


def _closure_proposals() -> tuple[ClosureProposal, ...]:
    return (
        ClosureProposal(
            proposal_id="repeat_t475_review_metadata_upgrade",
            proposal_kind="minor_restart",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=True,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=True,
            seeks_claim_or_public_posture_movement=False,
            intended_use="upgrade T475 review metadata into category evidence",
        ),
        ClosureProposal(
            proposal_id="semantic_atlas_rename_restart",
            proposal_kind="semantic_restart",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=False,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=False,
            uses_semantic_mapping=True,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="rename shared route labels as a typed bridge",
        ),
        ClosureProposal(
            proposal_id="fibration_label_shortcut",
            proposal_kind="category_language_shortcut",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=True,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=True,
            seeks_claim_or_public_posture_movement=False,
            intended_use="call the audit-atlas index bookkeeping a fibration",
        ),
        ClosureProposal(
            proposal_id="absorber_completion_restart",
            proposal_kind="absorber_restart",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=False,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=False,
            uses_semantic_mapping=False,
            uses_absorber_completion=True,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="reopen the bridge by completing hidden source state",
        ),
        ClosureProposal(
            proposal_id="capability_identification_restart",
            proposal_kind="capability_identification",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=False,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=False,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=True,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="identify PO1 admissibility and LossKernel obligations",
        ),
        ClosureProposal(
            proposal_id="control_incomplete_minor_variant",
            proposal_kind="incomplete_controls",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=False,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=True,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="reuse positives while dropping hostile bridge controls",
        ),
        ClosureProposal(
            proposal_id="claim_posture_shortcut",
            proposal_kind="governance_shortcut",
            repeats_current_t470_t475_packet_class=True,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=True,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=True,
            seeks_claim_or_public_posture_movement=True,
            intended_use="move public posture or claim status using T475 metadata",
        ),
        ClosureProposal(
            proposal_id="future_direct_preservation_theorem_packet",
            proposal_kind="future_direct_preservation_target",
            repeats_current_t470_t475_packet_class=False,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=True,
            declares_formal_category_semantics=True,
            introduces_new_packet_family=False,
            supplies_new_family_index_controls=False,
            uses_t475_review_metadata_as_proof=False,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="future proof packet that independently proves cross-family preservation",
        ),
        ClosureProposal(
            proposal_id="future_new_family_atlas_extension_packet",
            proposal_kind="future_new_family_target",
            repeats_current_t470_t475_packet_class=False,
            preserves_family_boundaries=True,
            supplies_positive_family_controls=True,
            supplies_hostile_bridge_controls=True,
            has_independent_direct_preservation_proof=False,
            declares_formal_category_semantics=False,
            introduces_new_packet_family=True,
            supplies_new_family_index_controls=True,
            uses_t475_review_metadata_as_proof=False,
            uses_semantic_mapping=False,
            uses_absorber_completion=False,
            identifies_family_capability_objects=False,
            claims_category_or_fibration_evidence=False,
            seeks_claim_or_public_posture_movement=False,
            intended_use="future packet family extension with its own controls",
        ),
    )


def _evaluate_proposal(
    proposal: ClosureProposal,
    t475_review_metadata_available: bool,
) -> ClosureDecision:
    missing = _missing_requirements(proposal, t475_review_metadata_available)
    notes: list[str] = []

    if proposal.seeks_claim_or_public_posture_movement:
        route = "block_governance_or_public_posture_shortcut"
        admitted = False
        notes.append("T476 has no authority to move claim status or public posture")
    elif not t475_review_metadata_available:
        route = "block_missing_t475_review_metadata"
        admitted = False
        notes.append("T475 review metadata is unavailable or not metadata-only")
    elif proposal.uses_semantic_mapping:
        route = "reject_semantic_restart"
        admitted = False
        notes.append("semantic similarity is still not a typed bridge relation")
    elif proposal.uses_absorber_completion:
        route = "reject_absorber_completion_restart"
        admitted = False
        notes.append("absorber completion remains state-completion bookkeeping")
    elif proposal.identifies_family_capability_objects:
        route = "reject_capability_identification_restart"
        admitted = False
        notes.append("family-specific capability objects must remain distinct")
    elif (
        proposal.claims_category_or_fibration_evidence
        and not (
            proposal.has_independent_direct_preservation_proof
            and proposal.declares_formal_category_semantics
        )
    ):
        route = "reject_category_or_fibration_shortcut"
        admitted = False
        notes.append("category/fibration language needs proof beyond review metadata")
    elif missing:
        route = "reject_missing_reopen_requirements"
        admitted = False
        notes.append("proposal lacks mandatory controls or family boundaries")
    elif (
        proposal.repeats_current_t470_t475_packet_class
        and not proposal.has_independent_direct_preservation_proof
        and not proposal.introduces_new_packet_family
    ):
        route = "reject_current_thread_minor_variant"
        admitted = False
        notes.append("current T470-T475 packet class is closed to minor variants")
    elif (
        proposal.has_independent_direct_preservation_proof
        and proposal.declares_formal_category_semantics
    ):
        route = "admit_future_direct_preservation_review_target"
        admitted = True
        notes.append("future packet may be reviewed as new evidence")
        notes.append("admission is not itself category evidence")
    elif proposal.introduces_new_packet_family and proposal.supplies_new_family_index_controls:
        route = "admit_future_new_family_review_target"
        admitted = True
        notes.append("future packet family may extend the audit atlas")
        notes.append("admission is not itself category evidence")
    else:
        route = "reject_underdeclared_restart"
        admitted = False
        notes.append("proposal does not name a legitimate reopen path")

    classification = _classification_for_route(route)
    admitted_as_future_review_target = route in {
        "admit_future_direct_preservation_review_target",
        "admit_future_new_family_review_target",
    }
    closes_current_thread = (
        proposal.repeats_current_t470_t475_packet_class and not admitted
    )

    return ClosureDecision(
        proposal_id=proposal.proposal_id,
        admitted=admitted,
        route_label=route,
        classification=classification,
        admitted_as_future_review_target=admitted_as_future_review_target,
        counts_as_category_evidence=False,
        closes_current_thread=closes_current_thread,
        missing_requirements=missing,
        notes=tuple(notes),
    )


def _missing_requirements(
    proposal: ClosureProposal,
    t475_review_metadata_available: bool,
) -> tuple[str, ...]:
    missing: list[str] = []

    if not t475_review_metadata_available:
        missing.append("t475_review_metadata_available")
    if not proposal.preserves_family_boundaries:
        missing.append("family_specific_boundaries_preserved")
    if not proposal.supplies_positive_family_controls:
        missing.append("positive_family_controls")
    if not proposal.supplies_hostile_bridge_controls:
        missing.append("hostile_bridge_controls")
    if proposal.claims_category_or_fibration_evidence:
        if not proposal.has_independent_direct_preservation_proof:
            missing.append("independent_direct_preservation_proof")
        if not proposal.declares_formal_category_semantics:
            missing.append("formal_category_semantics")
    if proposal.introduces_new_packet_family and not proposal.supplies_new_family_index_controls:
        missing.append("new_family_index_controls")

    return tuple(missing)


def _classification_for_route(route: str) -> str:
    if route == "block_governance_or_public_posture_shortcut":
        return "governance_boundary_block"
    if route == "block_missing_t475_review_metadata":
        return "missing_prior_gate_block"
    if route == "reject_semantic_restart":
        return "semantic_restart_rejection"
    if route == "reject_absorber_completion_restart":
        return "absorber_completion_rejection"
    if route == "reject_capability_identification_restart":
        return "capability_identification_rejection"
    if route == "reject_missing_reopen_requirements":
        return "missing_reopen_requirement_rejection"
    if route == "reject_category_or_fibration_shortcut":
        return "category_language_shortcut_rejection"
    if route == "reject_current_thread_minor_variant":
        return "current_packet_class_closed"
    if route == "admit_future_direct_preservation_review_target":
        return "future_direct_preservation_review_target"
    if route == "admit_future_new_family_review_target":
        return "future_new_family_review_target"
    if route == "reject_underdeclared_restart":
        return "underdeclared_restart_rejection"
    return "unclassified_closure_route"


def _proposal_by_id(
    proposals: tuple[ClosureProposal, ...],
    proposal_id: str,
) -> ClosureProposal:
    for proposal in proposals:
        if proposal.proposal_id == proposal_id:
            return proposal
    raise KeyError(proposal_id)


def t476_result_to_dict(result: T476Result) -> dict[str, Any]:
    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": result.verdict,
        "proposals": [_proposal_to_dict(proposal) for proposal in result.proposals],
        "decisions": [_decision_to_dict(decision) for decision in result.decisions],
        "claim_ledger_update": result.claim_ledger_update,
        "t475_review_metadata_available": result.t475_review_metadata_available,
        "current_thread_closed": result.current_thread_closed,
        "admitted_future_targets": list(result.admitted_future_targets),
        "rejected_restart_packets": list(result.rejected_restart_packets),
        "direct_cross_family_composition_supported": (
            result.direct_cross_family_composition_supported
        ),
        "global_category_theorem_supported": result.global_category_theorem_supported,
        "strongest_reading": result.strongest_reading,
        "future_reopen_minimum": list(result.future_reopen_minimum),
        "not_earned": list(result.not_earned),
    }


def render_markdown(result: T476Result) -> str:
    decision_rows = []
    for decision in result.decisions:
        missing = ", ".join(decision.missing_requirements) or "none"
        notes = "; ".join(decision.notes) or "none"
        decision_rows.append(
            "| {proposal} | {admitted} | {route} | {classification} | "
            "{future} | {category} | {closed} | {missing} | {notes} |".format(
                proposal=decision.proposal_id,
                admitted=decision.admitted,
                route=decision.route_label,
                classification=decision.classification,
                future=decision.admitted_as_future_review_target,
                category=decision.counts_as_category_evidence,
                closed=decision.closes_current_thread,
                missing=missing,
                notes=notes,
            )
        )

    reopen = [f"- {item}" for item in result.future_reopen_minimum]
    not_earned = [f"- {item}" for item in result.not_earned]

    return "\n".join(
        [
            "# T476 - Post-T475 Observer-Shadow Category Closure Router - v0.1 results",
            "",
            "> Closure router only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T476-post-t475-observer-shadow-category-closure-router.md`",
            "- Model: `models/post_t475_observer_shadow_category_closure_router.py`",
            "- Tests: `tests/test_post_t475_observer_shadow_category_closure_router.py`",
            "- Artifact JSON: `results/T476-post-t475-observer-shadow-category-closure-router-v0.1.json`",
            "- Source open problem: `open-problems/observer-shadow-category.md`",
            "- Prior gates: T470, T472, T473, T474, and T475",
            "",
            f"## Overall verdict: {result.verdict}",
            "",
            result.strongest_reading,
            "",
            "## Closure Decisions",
            "",
            "| proposal | admitted? | route | classification | future target? | category evidence? | closes current thread? | missing requirements | notes |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Future Reopen Minimum",
            "",
            *reopen,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _proposal_to_dict(proposal: ClosureProposal) -> dict[str, Any]:
    return {
        "proposal_id": proposal.proposal_id,
        "proposal_kind": proposal.proposal_kind,
        "repeats_current_t470_t475_packet_class": (
            proposal.repeats_current_t470_t475_packet_class
        ),
        "preserves_family_boundaries": proposal.preserves_family_boundaries,
        "supplies_positive_family_controls": proposal.supplies_positive_family_controls,
        "supplies_hostile_bridge_controls": proposal.supplies_hostile_bridge_controls,
        "has_independent_direct_preservation_proof": (
            proposal.has_independent_direct_preservation_proof
        ),
        "declares_formal_category_semantics": (
            proposal.declares_formal_category_semantics
        ),
        "introduces_new_packet_family": proposal.introduces_new_packet_family,
        "supplies_new_family_index_controls": (
            proposal.supplies_new_family_index_controls
        ),
        "uses_t475_review_metadata_as_proof": (
            proposal.uses_t475_review_metadata_as_proof
        ),
        "uses_semantic_mapping": proposal.uses_semantic_mapping,
        "uses_absorber_completion": proposal.uses_absorber_completion,
        "identifies_family_capability_objects": (
            proposal.identifies_family_capability_objects
        ),
        "claims_category_or_fibration_evidence": (
            proposal.claims_category_or_fibration_evidence
        ),
        "seeks_claim_or_public_posture_movement": (
            proposal.seeks_claim_or_public_posture_movement
        ),
        "intended_use": proposal.intended_use,
    }


def _decision_to_dict(decision: ClosureDecision) -> dict[str, Any]:
    return {
        "proposal_id": decision.proposal_id,
        "admitted": decision.admitted,
        "route_label": decision.route_label,
        "classification": decision.classification,
        "admitted_as_future_review_target": decision.admitted_as_future_review_target,
        "counts_as_category_evidence": decision.counts_as_category_evidence,
        "closes_current_thread": decision.closes_current_thread,
        "missing_requirements": list(decision.missing_requirements),
        "notes": list(decision.notes),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run_t476_analysis()
    payload = t476_result_to_dict(result)
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
