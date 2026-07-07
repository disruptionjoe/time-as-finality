"""T502 - post-T501 composite absorber-stack closure router.

T497-T501 made the five preserved composite absorber-stack lanes executable:
bounded retrieval, authoritative settlement, kappa method-template, C(R)
competency/resource/permission/provenance, and typed translation/object
identity.

This router closes that lane set to minor restarts and overreads. It admits
only future review packets that carry the new burden named by the relevant
lane's latest result. Admission is review-only; it does not move claims,
public posture, North Star, hard policy, external publication, or cross-repo
truth.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T502-post-t501-composite-absorber-stack-closure-router-v0.1"
VERDICT = "POST_T501_COMPOSITE_ABSORBER_STACK_CLOSED_NEW_EVIDENCE_ONLY"

LANE_RESULTS = {
    "bounded_retrieval": (
        "T497-bounded-retrieval-source-checked-stack-gate-v0.1",
        "BOUNDED_RETRIEVAL_SOURCE_CHECKED_STACK_BUILT_COMPOSITE_EXPLANATION",
    ),
    "authoritative_settlement": (
        "T498-authoritative-commit-settlement-stack-gate-v0.1",
        "AUTHORITATIVE_COMMIT_SETTLEMENT_STACK_BUILT_COMPOSITE_EXPLANATION",
    ),
    "kappa_template": (
        "T499-kappa-composite-residual-template-gate-v0.1",
        "KAPPA_COMPOSITE_TEMPLATE_GATE_BUILT_METHOD_ONLY_NO_PROMOTION",
    ),
    "competency_resource_permission": (
        "T500-competency-resource-permission-stack-gate-v0.1",
        "COMPETENCY_RESOURCE_PERMISSION_STACK_BUILT_NO_RESIDUAL_AFTER_FULL_STACK",
    ),
    "typed_translation_identity": (
        "T501-typed-translation-object-identity-stack-gate-v0.1",
        "TYPED_TRANSLATION_OBJECT_IDENTITY_STACK_BUILT_SCHEMA_PRESERVATION_ONLY",
    ),
}

LANE_LABELS = {
    "bounded_retrieval": "bounded retrieval source-checked stack",
    "authoritative_settlement": "authoritative commit / settlement stack",
    "kappa_template": "kappa composite residual template",
    "competency_resource_permission": "competency resource permission stack",
    "typed_translation_identity": "typed translation object-identity stack",
}

HONEST_CEILING = (
    "T502 is a closure and admission router only. It closes T497-T501 to "
    "minor restarts and overreads, while preserving named future review paths. "
    "It does not prove a theorem, promote a claim, alter public posture, "
    "change hard policy, publish externally, or move cross-repo truth."
)


@dataclass(frozen=True)
class CompositeProposal:
    packet_id: str
    target_lane: str
    description: str
    cites_completed_lane_anchor: bool
    supplies_named_new_burden: bool
    supplies_native_source_or_theorem: bool
    grants_full_absorber_stack: bool
    shows_controlled_capability_spread: bool
    supplies_positive_controls: bool
    supplies_hostile_controls: bool
    declares_demote_path: bool
    minor_restart: bool = False
    analogy_only: bool = False
    imports_theorem_or_prediction: bool = False
    imports_physics_mechanism: bool = False
    uses_single_layer_reading: bool = False
    asks_object_identity_from_schema: bool = False
    uses_synthetic_control_as_result: bool = False
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class CompositeDecision:
    packet_id: str
    admitted: bool
    route_label: str
    action: str
    target_lane: str
    future_review_target: bool
    closes_completed_lane: bool
    counts_as_claim_evidence: bool
    missing_requirements: tuple[str, ...]
    reason: str


def run() -> dict[str, Any]:
    anchors = _anchor_checks(_load_lane_results())
    proposals = proposal_fixtures()
    decisions = tuple(evaluate_proposal(proposal, anchors) for proposal in proposals)
    admitted_future_targets = tuple(
        decision.packet_id for decision in decisions if decision.future_review_target
    )
    rejected_packets = tuple(
        decision.packet_id for decision in decisions if not decision.admitted
    )
    current_stack_lanes_closed = (
        anchors["all_anchors_ok"]
        and all(
            decision.closes_completed_lane
            for decision in decisions
            if _proposal_by_id(proposals, decision.packet_id).minor_restart
            or _is_completed_lane_overread(_proposal_by_id(proposals, decision.packet_id))
        )
        and not any(decision.counts_as_claim_evidence for decision in decisions)
        and admitted_future_targets
        == (
            "future_bounded_retrieval_lower_bound_packet",
            "future_authoritative_protocol_packet",
            "future_kappa_nonidentity_packet",
            "future_full_stack_cr_residual_packet",
            "future_exact_object_preservation_packet",
        )
    )

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "source_progress_lanes": "open-problems/composite-absorber-stack-progress-lanes.md",
        "honest_ceiling": HONEST_CEILING,
        "anchors": anchors,
        "proposals": [asdict(proposal) for proposal in proposals],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "all_five_lanes_executable": anchors["all_anchors_ok"],
            "current_stack_lanes_closed": current_stack_lanes_closed,
            "admitted_future_targets": list(admitted_future_targets),
            "rejected_packets": list(rejected_packets),
            "review_target_only": True,
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "future_reopen_minimum": future_reopen_minimum(),
        "not_earned": not_earned(),
        "strongest_result": (
            "T497-T501 now form a completed composite absorber-stack screen. "
            "Bounded retrieval, authoritative settlement, kappa, C(R), and "
            "typed-gap/object-identity restarts are closed unless a packet "
            "cites the completed lane, supplies the named new burden, grants "
            "the full absorber stack, shows controlled capability spread, "
            "passes controls, and declares a demotion path. Admitted packets "
            "are future review targets only."
        ),
        "recommended_next": (
            "Use T502 as the routing screen before reopening any composite "
            "absorber-stack lane. Minor restarts should be rejected; packets "
            "with new evidence should be routed to the lane-specific burden."
        ),
    }


def proposal_fixtures() -> tuple[CompositeProposal, ...]:
    return (
        CompositeProposal(
            packet_id="bounded_retrieval_last2_rerun",
            target_lane="bounded_retrieval",
            description="Rerun the last-2 bounded retrieval fixture without theorem assumptions.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=False,
            minor_restart=True,
        ),
        CompositeProposal(
            packet_id="bounded_retrieval_theorem_import_shortcut",
            target_lane="bounded_retrieval",
            description="Treat T497 source checking as an SSM/Transformer theorem import.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            declares_demote_path=False,
            imports_theorem_or_prediction=True,
        ),
        CompositeProposal(
            packet_id="settlement_local_marker_residual_restart",
            target_lane="authoritative_settlement",
            description="Reassert local commit marker finality after T498 without authority completion.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=False,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=False,
            minor_restart=True,
        ),
        CompositeProposal(
            packet_id="kappa_prediction_overread",
            target_lane="kappa_template",
            description="Treat the T224-T244 kappa catalogue as prediction or theorem language.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=False,
            imports_theorem_or_prediction=True,
        ),
        CompositeProposal(
            packet_id="cr_single_statistic_restart",
            target_lane="competency_resource_permission",
            description="Reopen C(R) through one observed success statistic after T500.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=False,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=False,
            supplies_hostile_controls=True,
            declares_demote_path=False,
            uses_single_layer_reading=True,
        ),
        CompositeProposal(
            packet_id="typed_gap_same_schema_identity_overread",
            target_lane="typed_translation_identity",
            description="Treat the shared typed-gap schema as object identity.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=False,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=False,
            asks_object_identity_from_schema=True,
        ),
        CompositeProposal(
            packet_id="analogy_only_composite_packet",
            target_lane="bounded_retrieval",
            description="Use the completed lane set as analogy only.",
            cites_completed_lane_anchor=False,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=False,
            shows_controlled_capability_spread=False,
            supplies_positive_controls=False,
            supplies_hostile_controls=False,
            declares_demote_path=False,
            analogy_only=True,
        ),
        CompositeProposal(
            packet_id="synthetic_control_as_evidence_shortcut",
            target_lane="competency_resource_permission",
            description="Treat a synthetic positive control from T500 as earned C(R) evidence.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=False,
            supplies_native_source_or_theorem=False,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=False,
            declares_demote_path=False,
            uses_synthetic_control_as_result=True,
        ),
        CompositeProposal(
            packet_id="claim_public_posture_shortcut",
            target_lane="kappa_template",
            description="Use the composite lane set to move claim status or public posture.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
            requests_claim_or_public_posture=True,
        ),
        CompositeProposal(
            packet_id="external_cross_repo_shortcut",
            target_lane="typed_translation_identity",
            description="Publish or move cross-repo truth from a composite stack packet.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
        CompositeProposal(
            packet_id="future_bounded_retrieval_lower_bound_packet",
            target_lane="bounded_retrieval",
            description="Future packet restating a checked copying/retrieval lower-bound theorem under exact assumptions.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
        ),
        CompositeProposal(
            packet_id="future_authoritative_protocol_packet",
            target_lane="authoritative_settlement",
            description="Future source-checked commit or consensus protocol packet with exact finality and rollback rules.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
        ),
        CompositeProposal(
            packet_id="future_kappa_nonidentity_packet",
            target_lane="kappa_template",
            description="Future non-identity target witness with independent source rank and predeclared map.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
        ),
        CompositeProposal(
            packet_id="future_full_stack_cr_residual_packet",
            target_lane="competency_resource_permission",
            description="Future C(R) packet showing controlled spread after competency, resource, permission, and provenance completion.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
        ),
        CompositeProposal(
            packet_id="future_exact_object_preservation_packet",
            target_lane="typed_translation_identity",
            description="Future typed-gap packet with same carrier, target, admissibility rule, direct theorem, and invariant obstruction.",
            cites_completed_lane_anchor=True,
            supplies_named_new_burden=True,
            supplies_native_source_or_theorem=True,
            grants_full_absorber_stack=True,
            shows_controlled_capability_spread=True,
            supplies_positive_controls=True,
            supplies_hostile_controls=True,
            declares_demote_path=True,
        ),
    )


def evaluate_proposal(
    proposal: CompositeProposal,
    anchors: dict[str, Any],
) -> CompositeDecision:
    missing = missing_requirements(proposal)
    closes_lane = _is_completed_lane_overread(proposal) or proposal.minor_restart

    if proposal.requests_claim_or_public_posture:
        return _decision(
            proposal,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            False,
            closes_lane,
            missing,
            "Composite closure cannot move claims, roadmap, README, North Star, or public posture.",
        )
    if proposal.requests_external_publication or proposal.requests_cross_repo_truth:
        return _decision(
            proposal,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            False,
            closes_lane,
            missing,
            "External publication and cross-repo truth updates are outside this run.",
        )
    if not anchors["all_anchors_ok"]:
        return _decision(
            proposal,
            False,
            "BLOCKED_MISSING_COMPLETED_STACK_ANCHOR",
            "stop",
            False,
            False,
            missing,
            "One or more T497-T501 anchors is missing or no longer has the expected review-only verdict.",
        )
    if proposal.analogy_only:
        return _decision(
            proposal,
            False,
            "REJECTED_ANALOGY_ONLY_RESTART",
            "reject",
            False,
            closes_lane,
            missing,
            "T496 and T502 require typed packets, not analogy-only restarts.",
        )
    if proposal.uses_synthetic_control_as_result:
        return _decision(
            proposal,
            False,
            "REJECTED_SYNTHETIC_CONTROL_OVERREAD",
            "reject",
            False,
            closes_lane,
            missing,
            "Synthetic controls calibrate the gate; they do not count as earned evidence.",
        )
    if proposal.imports_physics_mechanism:
        return _decision(
            proposal,
            False,
            "REJECTED_PHYSICS_MECHANISM_IMPORT",
            "reject",
            False,
            closes_lane,
            missing,
            "Composite stack screens do not import physics mechanisms.",
        )
    if proposal.imports_theorem_or_prediction:
        return _decision(
            proposal,
            False,
            "REJECTED_THEOREM_OR_PREDICTION_OVERREAD",
            "reject",
            False,
            closes_lane,
            missing,
            "The completed lane does not supply theorem or prediction language without the named new burden.",
        )
    if proposal.uses_single_layer_reading:
        return _decision(
            proposal,
            False,
            "REJECTED_SINGLE_LAYER_STACK_RESTART",
            "reject",
            False,
            closes_lane,
            missing,
            "Single-layer readings do not reopen a lane after the full absorber stack has been granted.",
        )
    if proposal.asks_object_identity_from_schema:
        return _decision(
            proposal,
            False,
            "REJECTED_OBJECT_IDENTITY_FROM_SCHEMA_OVERREAD",
            "reject",
            False,
            closes_lane,
            missing,
            "Shared schema does not imply object identity after T501.",
        )
    if proposal.minor_restart:
        return _decision(
            proposal,
            False,
            "REJECTED_COMPLETED_LANE_MINOR_RESTART",
            "reject",
            False,
            True,
            missing,
            "The lane is complete; a rerun needs the named new burden.",
        )
    if missing:
        return _decision(
            proposal,
            False,
            "REJECTED_MISSING_NEW_EVIDENCE_BURDEN",
            "reject",
            False,
            closes_lane,
            missing,
            "The packet does not satisfy the T502 reopen minimum.",
        )

    route = _future_route_for_lane(proposal.target_lane)
    return _decision(
        proposal,
        True,
        route,
        "review_only",
        True,
        False,
        (),
        f"Future packet may be reviewed under the {LANE_LABELS[proposal.target_lane]} burden.",
    )


def missing_requirements(proposal: CompositeProposal) -> tuple[str, ...]:
    missing: list[str] = []
    if proposal.target_lane not in LANE_RESULTS:
        missing.append("known_completed_lane")
    if not proposal.cites_completed_lane_anchor:
        missing.append("completed_lane_anchor_cited")
    if not proposal.supplies_named_new_burden:
        missing.append("named_new_burden")
    if not proposal.supplies_native_source_or_theorem:
        missing.append("native_source_or_theorem")
    if not proposal.grants_full_absorber_stack:
        missing.append("full_absorber_stack_granted")
    if not proposal.shows_controlled_capability_spread:
        missing.append("controlled_capability_spread")
    if not proposal.supplies_positive_controls:
        missing.append("positive_controls")
    if not proposal.supplies_hostile_controls:
        missing.append("hostile_overread_controls")
    if not proposal.declares_demote_path:
        missing.append("demotion_path")
    return tuple(missing)


def future_reopen_minimum() -> tuple[str, ...]:
    return (
        "cite the completed lane anchor from T497, T498, T499, T500, or T501",
        "state the named new burden from that lane's latest result before scoring",
        "supply a native source, theorem, protocol, non-identity witness, or direct preservation theorem as appropriate to the lane",
        "grant the full declared absorber stack rather than a single-layer projection",
        "show controlled capability spread after the full stack or demote to composite explanation",
        "include native positive controls and hostile overread controls",
        "declare the demotion path if any absorber layer explains the packet",
        "keep admitted packets as review targets until a runnable artifact earns a narrower update",
        "block claim, public-posture, external-publication, and cross-repo shortcuts",
    )


def not_earned() -> tuple[str, ...]:
    return (
        "new C(R) primitive",
        "region-indexed discriminator success",
        "kappa promotion",
        "kappa prediction language",
        "genre-agnostic theorem",
        "SSM or Transformer theorem",
        "authoritative-settlement theorem",
        "same-object typed-gap identity",
        "category theorem",
        "geometry or physics support",
        "claim-ledger movement",
        "roadmap movement",
        "README movement",
        "North Star movement",
        "public-posture movement",
        "hard-policy movement",
        "protected-license movement",
        "external publication",
        "cross-repo truth movement",
    )


def render_markdown(payload: dict[str, Any]) -> str:
    anchor_rows = [
        "| {lane} | {artifact} | {verdict} | {anchor_ok} |".format(
            lane=lane,
            artifact=anchor["artifact"],
            verdict=anchor["verdict"],
            anchor_ok=anchor["anchor_ok"],
        )
        for lane, anchor in payload["anchors"]["lanes"].items()
    ]
    decision_rows = [
        "| {packet_id} | {target_lane} | {admitted} | {route_label} | {future} | {closed} | {claim} | {missing} | {action} |".format(
            packet_id=decision["packet_id"],
            target_lane=decision["target_lane"],
            admitted="yes" if decision["admitted"] else "no",
            route_label=decision["route_label"],
            future="yes" if decision["future_review_target"] else "no",
            closed="yes" if decision["closes_completed_lane"] else "no",
            claim="yes" if decision["counts_as_claim_evidence"] else "no",
            missing=", ".join(decision["missing_requirements"]) or "none",
            action=decision["action"],
        )
        for decision in payload["decisions"]
    ]
    future_minimum = [f"- {item}" for item in payload["future_reopen_minimum"]]
    blocked = [f"- {item}" for item in payload["not_earned"]]

    return "\n".join(
        [
            "# T502 - Post-T501 Composite Absorber-Stack Closure Router - v0.1 results",
            "",
            "> Closure router only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, protected-license, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T502-post-t501-composite-absorber-stack-closure-router.md`",
            "- Model: `models/post_t501_composite_absorber_stack_closure_router.py`",
            "- Tests: `tests/test_post_t501_composite_absorber_stack_closure_router.py`",
            "- Artifact JSON: `results/T502-post-t501-composite-absorber-stack-closure-router-v0.1.json`",
            "- Source progress artifact: `open-problems/composite-absorber-stack-progress-lanes.md`",
            "- Prior gates: T497, T498, T499, T500, T501",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Completed Lane Anchors",
            "",
            "| Lane | Artifact | Verdict | Anchor OK? |",
            "| --- | --- | --- | --- |",
            *anchor_rows,
            "",
            "## Router Decisions",
            "",
            "| Packet | Lane | Admitted? | Route | Future target? | Closes completed lane? | Counts as claim evidence? | Missing requirements | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## Future Reopen Minimum",
            "",
            *future_minimum,
            "",
            "## What This Does Not Earn",
            "",
            *blocked,
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )


def _load_lane_results() -> dict[str, dict[str, Any]]:
    results: dict[str, dict[str, Any]] = {}
    for lane, (artifact, _verdict) in LANE_RESULTS.items():
        path = Path("results") / f"{artifact}.json"
        results[lane] = json.loads(path.read_text(encoding="utf-8"))
    return results


def _anchor_checks(payloads: dict[str, dict[str, Any]]) -> dict[str, Any]:
    lanes = {
        "bounded_retrieval": _bounded_retrieval_anchor(payloads["bounded_retrieval"]),
        "authoritative_settlement": _authoritative_settlement_anchor(
            payloads["authoritative_settlement"]
        ),
        "kappa_template": _kappa_anchor(payloads["kappa_template"]),
        "competency_resource_permission": _cr_anchor(
            payloads["competency_resource_permission"]
        ),
        "typed_translation_identity": _typed_translation_anchor(
            payloads["typed_translation_identity"]
        ),
    }
    return {
        "lanes": lanes,
        "all_anchors_ok": all(anchor["anchor_ok"] for anchor in lanes.values()),
    }


def _bounded_retrieval_anchor(payload: dict[str, Any]) -> dict[str, Any]:
    readings = {item["reading_id"]: item for item in payload["reading_decisions"]}
    ok = (
        payload["artifact"] == LANE_RESULTS["bounded_retrieval"][0]
        and payload["verdict"] == LANE_RESULTS["bounded_retrieval"][1]
        and payload["overall"]["review_target_only"] is True
        and payload["overall"]["claim_movement"] is False
        and payload["overall"]["external_publication"] is False
        and readings["bounded_retrieval_composite_explanation"]["admitted"] is True
        and readings["complexity_theorem_import"]["admitted"] is False
        and readings["attention_quantum_copyability_revival"]["admitted"] is False
    )
    return _anchor_payload(payload, ok)


def _authoritative_settlement_anchor(payload: dict[str, Any]) -> dict[str, Any]:
    readings = {item["reading_id"]: item for item in payload["reading_decisions"]}
    ok = (
        payload["artifact"] == LANE_RESULTS["authoritative_settlement"][0]
        and payload["verdict"] == LANE_RESULTS["authoritative_settlement"][1]
        and payload["overall"]["local_visible_settlement_factorizes"] is False
        and payload["overall"]["full_authority_completion_factorizes"] is True
        and payload["overall"]["review_target_only"] is True
        and payload["overall"]["claim_movement"] is False
        and readings["local_marker_as_finality_residual"]["admitted"] is False
    )
    return _anchor_payload(payload, ok)


def _kappa_anchor(payload: dict[str, Any]) -> dict[str, Any]:
    ok = (
        payload["artifact"] == LANE_RESULTS["kappa_template"][0]
        and payload["verdict"] == LANE_RESULTS["kappa_template"][1]
        and payload["overall"]["historical_kappa_catalogue_admitted_as_method_template"]
        is True
        and payload["overall"]["synthetic_nonidentity_packet_admitted_for_review"]
        is True
        and payload["overall"]["kappa_promotion_earned"] is False
        and payload["overall"]["prediction_language_earned"] is False
        and "non-identity promotion burden requires independent source rank and predeclared map"
        in payload["template_minimum"]
    )
    return _anchor_payload(payload, ok)


def _cr_anchor(payload: dict[str, Any]) -> dict[str, Any]:
    ok = (
        payload["artifact"] == LANE_RESULTS["competency_resource_permission"][0]
        and payload["verdict"] == LANE_RESULTS["competency_resource_permission"][1]
        and payload["overall"]["current_c_r_full_stack_absorbed"] is True
        and payload["overall"]["current_c_r_residual_survives_full_stack"] is False
        and payload["overall"]["synthetic_full_stack_residual_admitted_for_review"]
        is True
        and payload["overall"]["review_target_only"] is True
        and payload["overall"]["claim_movement"] is False
    )
    return _anchor_payload(payload, ok)


def _typed_translation_anchor(payload: dict[str, Any]) -> dict[str, Any]:
    ok = (
        payload["artifact"] == LANE_RESULTS["typed_translation_identity"][0]
        and payload["verdict"] == LANE_RESULTS["typed_translation_identity"][1]
        and payload["overall"]["actual_t92_t113_interface_preserved"] is True
        and payload["overall"]["actual_t92_t113_object_identity_passes"] is False
        and payload["overall"]["synthetic_exact_packet_admitted_for_review"] is True
        and payload["overall"]["review_target_only_for_residuals"] is True
        and payload["overall"]["claim_movement"] is False
    )
    return _anchor_payload(payload, ok)


def _anchor_payload(payload: dict[str, Any], anchor_ok: bool) -> dict[str, Any]:
    return {
        "artifact": payload["artifact"],
        "verdict": payload["verdict"],
        "anchor_ok": anchor_ok,
    }


def _future_route_for_lane(lane: str) -> str:
    routes = {
        "bounded_retrieval": "ADMIT_FUTURE_BOUNDED_RETRIEVAL_THEOREM_REVIEW_TARGET",
        "authoritative_settlement": "ADMIT_FUTURE_AUTHORITATIVE_PROTOCOL_REVIEW_TARGET",
        "kappa_template": "ADMIT_FUTURE_KAPPA_NONIDENTITY_REVIEW_TARGET",
        "competency_resource_permission": "ADMIT_FUTURE_FULL_STACK_CR_RESIDUAL_REVIEW_TARGET",
        "typed_translation_identity": "ADMIT_FUTURE_EXACT_OBJECT_PRESERVATION_REVIEW_TARGET",
    }
    return routes.get(lane, "REJECT_UNKNOWN_LANE")


def _decision(
    proposal: CompositeProposal,
    admitted: bool,
    route_label: str,
    action: str,
    future_review_target: bool,
    closes_completed_lane: bool,
    missing_requirements: tuple[str, ...],
    reason: str,
) -> CompositeDecision:
    return CompositeDecision(
        packet_id=proposal.packet_id,
        admitted=admitted,
        route_label=route_label,
        action=action,
        target_lane=proposal.target_lane,
        future_review_target=future_review_target,
        closes_completed_lane=closes_completed_lane,
        counts_as_claim_evidence=False,
        missing_requirements=missing_requirements,
        reason=reason,
    )


def _is_completed_lane_overread(proposal: CompositeProposal) -> bool:
    return (
        proposal.imports_theorem_or_prediction
        or proposal.imports_physics_mechanism
        or proposal.uses_single_layer_reading
        or proposal.asks_object_identity_from_schema
        or proposal.uses_synthetic_control_as_result
        or proposal.analogy_only
    )


def _proposal_by_id(
    proposals: tuple[CompositeProposal, ...],
    packet_id: str,
) -> CompositeProposal:
    for proposal in proposals:
        if proposal.packet_id == packet_id:
            return proposal
    raise KeyError(packet_id)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT}.json"
        md_path = results_dir / f"{ARTIFACT}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
