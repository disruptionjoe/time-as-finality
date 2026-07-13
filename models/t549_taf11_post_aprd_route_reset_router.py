"""T549: TAF11 post-APRD route reset router.

T548 narrowed APRD to a family-local feeder: its frozen predictor still works
on known record-transport fixtures, but it does not cross families without a
new native rule. T549 resets the TAF11 route after that narrowing. It chooses
the next executable packet without retuning APRD, moving TAF4, pausing behind
TAF8 without a domain-native packet, or changing governance posture.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t548_aprd_cross_family_prediction_stress_packet as t548


ARTIFACT = "T549-taf11-post-aprd-route-reset-router-v0.1"
VERDICT = "taf11_post_aprd_router_selected_protocol_stack_ablation_preflight"
POST_APRD_STATUS = "APRD_ROUTE_NARROWED_RESET_REQUIRED"
SELECTED_ROUTE = "observerse_protocol_stack_ablation_preflight"
NEXT_PACKET = "t550_observerse_protocol_stack_ablation_preflight_packet"

NOT_CLAIMED = (
    "T549 does not establish a source law, prove a shadow-protection theorem, "
    "derive spacetime, prove manifoldlikeness, repair T528, reverse T223, "
    "unpause S1, promote S1, change claim status, change Canon Index tiers, "
    "change canon verdicts, change public posture, change the North Star, "
    "authorize external publication, move TAF4 from APRD, or move cross-repo "
    "truth. It is a post-APRD TAF11 route-selection router only."
)


@dataclass(frozen=True)
class ResetCandidate:
    candidate_id: str
    description: str
    source_variables: tuple[str, ...]
    predeclared_falsifier: str
    next_packet: str
    finality_native: bool
    new_after_aprd_narrowing: bool
    no_aprd_retune_or_replay: bool
    source_variables_declared: bool
    protocol_stack_layers_declared: bool
    ablation_collapse_modes_predeclared: bool
    computable_without_target_import: bool
    executable_next_packet_specific: bool
    hostile_controls_named: bool
    bridge_to_taf11_burdens: bool
    respects_taf8_wait_state: bool
    blocks_taf4_movement: bool
    no_cross_repo_truth_import: bool
    repeats_aprd_route: bool = False
    requests_taf4_movement: bool = False
    requires_domain_native_taf8_packet: bool = False
    domain_native_taf8_packet_in_hand: bool = False
    depends_on_real_data_packet: bool = False
    replaces_track_1_with_track_2: bool = False
    secondary_lane_only: bool = False
    requests_claim_canon_public_or_external_movement: bool = False


@dataclass(frozen=True)
class CandidateDecision:
    candidate_id: str
    outcome: str
    selected_for_next_execution: bool
    track_role: str
    missing_requirements: tuple[str, ...]
    reason: str
    next_packet: str
    source_variables: tuple[str, ...]
    predeclared_falsifier: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks_candidate_ids: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T549Result:
    artifact: str
    source_t548_verdict: str
    source_t548_status: str
    source_t548_cross_family_survivors: tuple[str, ...]
    source_t548_narrowed_cases: tuple[str, ...]
    post_aprd_status: str
    candidate_decisions: tuple[CandidateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_route_ids: tuple[str, ...]
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t549_analysis() -> T549Result:
    t548_result = t548.run_t548_analysis()
    decisions = tuple(_evaluate_candidate(candidate) for candidate in _candidates())
    selected = tuple(
        decision.candidate_id
        for decision in decisions
        if decision.selected_for_next_execution
    )
    verdict = (
        VERDICT
        if t548_result.verdict == t548.VERDICT
        and t548_result.aprd_cross_family_status == t548.APRD_CROSS_FAMILY_STATUS
        and t548_result.cross_family_survivors == ()
        and selected == (SELECTED_ROUTE,)
        else "taf11_post_aprd_router_unexpected_status"
    )

    return T549Result(
        artifact=ARTIFACT,
        source_t548_verdict=t548_result.verdict,
        source_t548_status=t548_result.aprd_cross_family_status,
        source_t548_cross_family_survivors=t548_result.cross_family_survivors,
        source_t548_narrowed_cases=t548_result.narrowed_cases,
        post_aprd_status=POST_APRD_STATUS,
        candidate_decisions=decisions,
        hostile_controls=_hostile_controls(),
        selected_route_ids=selected,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET}. It should predeclare a minimal protocol stack, "
            "predict each ablation's collapse mode before reading outcomes, and "
            "reject if the stack is post-hoc, imports cross-repo truth, retunes "
            "APRD, or tries to move TAF4/source-law status directly."
        ),
        taf11_update=(
            "TAF11 remains the active Track-1 source-law route, but APRD is no "
            "longer the route to deepen. The next executable swing is an "
            "observerse protocol-stack ablation preflight with native layers and "
            "collapse-mode falsifiers."
        ),
        taf4_update=(
            "TAF4 remains blocked. T549 consumes T548 as a negative control "
            "against finite-to-continuum movement from APRD."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T549 does not pause TAF11 behind TAF8 because no such packet is in hand."
        ),
        claim_labels=_claim_labels(decisions, t548_result),
        claim_ledger_update=(
            "No claim-ledger update is earned. T549 is route selection and "
            "preflight scoping only; it leaves claim rows, Canon Index tiers, "
            "and canon verdicts unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t549_result_to_dict(result: T549Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t548_verdict": result.source_t548_verdict,
        "source_t548_status": result.source_t548_status,
        "source_t548_cross_family_survivors": list(
            result.source_t548_cross_family_survivors
        ),
        "source_t548_narrowed_cases": list(result.source_t548_narrowed_cases),
        "post_aprd_status": result.post_aprd_status,
        "candidate_decisions": [
            {
                "candidate_id": decision.candidate_id,
                "outcome": decision.outcome,
                "selected_for_next_execution": decision.selected_for_next_execution,
                "track_role": decision.track_role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
                "source_variables": list(decision.source_variables),
                "predeclared_falsifier": decision.predeclared_falsifier,
            }
            for decision in result.candidate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks_candidate_ids": list(control.blocks_candidate_ids),
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_route_ids": list(result.selected_route_ids),
        "verdict": result.verdict,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _candidates() -> tuple[ResetCandidate, ...]:
    return (
        ResetCandidate(
            candidate_id=SELECTED_ROUTE,
            description=(
                "Predeclare a minimal observerse protocol stack and ablate each "
                "layer to test whether finality-native ordering needs a stack "
                "object rather than an isolated APRD family rule."
            ),
            source_variables=(
                "issuance_layer",
                "access_control_layer",
                "admissibility_layer",
                "provenance_layer",
                "record_finality_layer",
                "collapse_mode_prediction",
            ),
            predeclared_falsifier=(
                "Reject if layers are chosen post-hoc after outcomes, if ablations "
                "do not have predicted collapse modes, if the stack merely patches "
                "APRD, if cross-repo truth is imported, or if the packet tries to "
                "move TAF4/source-law status without a later survivor."
            ),
            next_packet=NEXT_PACKET,
            finality_native=True,
            new_after_aprd_narrowing=True,
            no_aprd_retune_or_replay=True,
            source_variables_declared=True,
            protocol_stack_layers_declared=True,
            ablation_collapse_modes_predeclared=True,
            computable_without_target_import=True,
            executable_next_packet_specific=True,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=True,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
        ),
        ResetCandidate(
            candidate_id="fresh_source_law_family_menu",
            description=(
                "Search broadly for a new source-law family after APRD narrowing."
            ),
            source_variables=("future_family_variables",),
            predeclared_falsifier=(
                "Reject if the family is selected from target fit or repeats APRD."
            ),
            next_packet="none",
            finality_native=True,
            new_after_aprd_narrowing=True,
            no_aprd_retune_or_replay=True,
            source_variables_declared=False,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=True,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
        ),
        ResetCandidate(
            candidate_id="taf8_pause_until_domain_native_packet",
            description=(
                "Pause TAF11 and wait behind TAF8 until a cross-domain packet appears."
            ),
            source_variables=("future_domain_native_packet",),
            predeclared_falsifier=(
                "Reject unless a real domain-native packet exists under the T541 gate."
            ),
            next_packet="none",
            finality_native=False,
            new_after_aprd_narrowing=True,
            no_aprd_retune_or_replay=True,
            source_variables_declared=False,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=False,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
            requires_domain_native_taf8_packet=True,
            domain_native_taf8_packet_in_hand=False,
        ),
        ResetCandidate(
            candidate_id="deepen_or_retune_aprd_family",
            description=(
                "Patch APRD with a new family-specific rule after T548 narrowed it."
            ),
            source_variables=("aprd_family_rule",),
            predeclared_falsifier="Already rejected by T548 cross-family stress.",
            next_packet="none",
            finality_native=True,
            new_after_aprd_narrowing=False,
            no_aprd_retune_or_replay=False,
            source_variables_declared=True,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
            repeats_aprd_route=True,
        ),
        ResetCandidate(
            candidate_id="taf4_from_aprd_continuum_bridge",
            description=(
                "Move toward finite-to-continuum or Lorentzian reading from APRD."
            ),
            source_variables=("aprd_debt_set", "continuum_target"),
            predeclared_falsifier="Blocked because T548 found no cross-family survivor.",
            next_packet="none",
            finality_native=False,
            new_after_aprd_narrowing=False,
            no_aprd_retune_or_replay=False,
            source_variables_declared=True,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=False,
            no_cross_repo_truth_import=True,
            requests_taf4_movement=True,
        ),
        ResetCandidate(
            candidate_id="quantum_access_structure_immediate_theorem",
            description=(
                "Turn the T548 quantum access-structure miss directly into a TAF11 theorem."
            ),
            source_variables=("access_structure_definition", "shareability_witness"),
            predeclared_falsifier=(
                "Reject if this bypasses the existing TAF6 lane or lacks a native "
                "shareability law."
            ),
            next_packet="none",
            finality_native=False,
            new_after_aprd_narrowing=True,
            no_aprd_retune_or_replay=True,
            source_variables_declared=True,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=True,
            executable_next_packet_specific=False,
            hostile_controls_named=True,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
            secondary_lane_only=True,
        ),
        ResetCandidate(
            candidate_id="taf12_data_packet_wait",
            description=(
                "Wait for a real data-bearing C(R) packet to replace Track 1."
            ),
            source_variables=("future_full_stack_profile", "future_noncompletion_witness"),
            predeclared_falsifier=(
                "Reject as a Track-1 replacement unless a real TAF10/TAF12 packet exists."
            ),
            next_packet="none",
            finality_native=False,
            new_after_aprd_narrowing=True,
            no_aprd_retune_or_replay=True,
            source_variables_declared=False,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=False,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=True,
            blocks_taf4_movement=True,
            no_cross_repo_truth_import=True,
            depends_on_real_data_packet=True,
            replaces_track_1_with_track_2=True,
        ),
        ResetCandidate(
            candidate_id="s1_claim_or_public_posture_shortcut",
            description=(
                "Treat T548 narrowing or T549 routing as reason to move S1, claims, "
                "canon, or public posture."
            ),
            source_variables=(),
            predeclared_falsifier="Blocked by governance.",
            next_packet="none",
            finality_native=False,
            new_after_aprd_narrowing=False,
            no_aprd_retune_or_replay=False,
            source_variables_declared=False,
            protocol_stack_layers_declared=False,
            ablation_collapse_modes_predeclared=False,
            computable_without_target_import=False,
            executable_next_packet_specific=False,
            hostile_controls_named=False,
            bridge_to_taf11_burdens=False,
            respects_taf8_wait_state=False,
            blocks_taf4_movement=False,
            no_cross_repo_truth_import=False,
            requests_claim_canon_public_or_external_movement=True,
        ),
    )


def _evaluate_candidate(candidate: ResetCandidate) -> CandidateDecision:
    missing = _missing_requirements(candidate)
    if candidate.requests_claim_canon_public_or_external_movement:
        outcome = "BLOCKED_GOVERNANCE"
        selected = False
        role = "forbidden"
        reason = "A router cannot move claims, canon, public posture, or external state."
        next_packet = "none"
    elif candidate.requests_taf4_movement:
        outcome = "BLOCKED_TAF4_OVERREAD"
        selected = False
        role = "blocked"
        reason = "T548 narrowed APRD before any finite-to-continuum movement."
        next_packet = "none"
    elif candidate.repeats_aprd_route:
        outcome = "REJECTED_APRD_REPLAY"
        selected = False
        role = "retired_or_narrowed"
        reason = "T548 already rejected cross-family APRD retuning or replay."
        next_packet = "none"
    elif candidate.requires_domain_native_taf8_packet and not candidate.domain_native_taf8_packet_in_hand:
        outcome = "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET"
        selected = False
        role = "taf8_waiting"
        reason = "T541's gate needs a real domain-native packet, and none is in hand."
        next_packet = "none"
    elif candidate.depends_on_real_data_packet and candidate.replaces_track_1_with_track_2:
        outcome = "PAUSED_TRACK_2"
        selected = False
        role = "track_2_waiting"
        reason = "No real data-bearing packet is in hand, and Track 2 cannot replace Track 1."
        next_packet = "none"
    elif candidate.secondary_lane_only:
        outcome = "REVIEW_ONLY_SECONDARY_LANE"
        selected = False
        role = "secondary_lane"
        reason = "The candidate belongs to another lane and is not the TAF11 route reset."
        next_packet = "none"
    elif missing:
        outcome = "REVIEW_ONLY_UNDERDECLARED"
        selected = False
        role = "underdeclared_or_feeder"
        reason = "The candidate lacks one or more post-APRD reset execution requirements."
        next_packet = "none"
    else:
        outcome = "SELECTED_FOR_EXECUTION"
        selected = True
        role = "track_1_next_packet"
        reason = (
            "The candidate is finality-native, new after APRD narrowing, "
            "specific enough to execute, and has layer-ablation falsifiers."
        )
        next_packet = candidate.next_packet

    return CandidateDecision(
        candidate_id=candidate.candidate_id,
        outcome=outcome,
        selected_for_next_execution=selected,
        track_role=role,
        missing_requirements=missing,
        reason=reason,
        next_packet=next_packet,
        source_variables=candidate.source_variables,
        predeclared_falsifier=candidate.predeclared_falsifier,
    )


def _missing_requirements(candidate: ResetCandidate) -> tuple[str, ...]:
    missing: list[str] = []
    if not candidate.finality_native:
        missing.append("finality_native")
    if not candidate.new_after_aprd_narrowing:
        missing.append("new_after_aprd_narrowing")
    if not candidate.no_aprd_retune_or_replay:
        missing.append("no_aprd_retune_or_replay")
    if not candidate.source_variables_declared:
        missing.append("source_variables_declared")
    if not candidate.protocol_stack_layers_declared:
        missing.append("protocol_stack_layers_declared")
    if not candidate.ablation_collapse_modes_predeclared:
        missing.append("ablation_collapse_modes_predeclared")
    if not candidate.computable_without_target_import:
        missing.append("computable_without_target_import")
    if not candidate.executable_next_packet_specific:
        missing.append("executable_next_packet_specific")
    if not candidate.hostile_controls_named:
        missing.append("hostile_controls_named")
    if not candidate.bridge_to_taf11_burdens:
        missing.append("bridge_to_taf11_burdens")
    if not candidate.respects_taf8_wait_state:
        missing.append("respects_taf8_wait_state")
    if not candidate.blocks_taf4_movement:
        missing.append("blocks_taf4_movement")
    if not candidate.no_cross_repo_truth_import:
        missing.append("no_cross_repo_truth_import")
    if candidate.repeats_aprd_route:
        missing.append("no_aprd_route_replay")
    if candidate.requests_taf4_movement:
        missing.append("no_taf4_movement_from_aprd")
    if candidate.requires_domain_native_taf8_packet and not candidate.domain_native_taf8_packet_in_hand:
        missing.append("domain_native_taf8_packet_in_hand")
    if candidate.depends_on_real_data_packet:
        missing.append("not_blocked_on_real_data_packet")
    if candidate.replaces_track_1_with_track_2:
        missing.append("track_2_does_not_replace_track_1")
    if candidate.secondary_lane_only:
        missing.append("not_secondary_lane_only")
    if candidate.requests_claim_canon_public_or_external_movement:
        missing.append("no_claim_canon_public_or_external_movement")
    return tuple(missing)


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="t548_aprd_narrowing_control",
            blocks_candidate_ids=("deepen_or_retune_aprd_family",),
            reason="T548 found no cross-family APRD survivor without retuning.",
        ),
        HostileControl(
            control_id="taf4_movement_control",
            blocks_candidate_ids=("taf4_from_aprd_continuum_bridge",),
            reason="APRD cannot feed finite-to-continuum movement after T548.",
        ),
        HostileControl(
            control_id="taf8_wait_state_control",
            blocks_candidate_ids=("taf8_pause_until_domain_native_packet",),
            reason="T541's TAF8 gate is usable only when a real domain-native packet exists.",
        ),
        HostileControl(
            control_id="track_2_replacement_control",
            blocks_candidate_ids=("taf12_data_packet_wait",),
            reason="A future C(R) packet may help, but it cannot replace Track 1 now.",
        ),
        HostileControl(
            control_id="secondary_lane_control",
            blocks_candidate_ids=("quantum_access_structure_immediate_theorem",),
            reason="The quantum access miss belongs to TAF6 until a TAF11 law is declared.",
        ),
        HostileControl(
            control_id="governance_posture_control",
            blocks_candidate_ids=("s1_claim_or_public_posture_shortcut",),
            reason="Routers do not move claims, canon, public posture, or external state.",
        ),
    )


def _claim_labels(
    decisions: tuple[CandidateDecision, ...],
    t548_result: t548.T548Result,
) -> tuple[ClaimLabel, ...]:
    selected = tuple(decision for decision in decisions if decision.selected_for_next_execution)
    blocked = tuple(
        decision.candidate_id
        for decision in decisions
        if decision.outcome
        in {
            "BLOCKED_GOVERNANCE",
            "BLOCKED_TAF4_OVERREAD",
            "REJECTED_APRD_REPLAY",
            "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET",
            "PAUSED_TRACK_2",
            "REVIEW_ONLY_SECONDARY_LANE",
        }
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T548 is consumed as APRD narrowing with no cross-family "
                "survivors: "
                + ", ".join(t548_result.narrowed_cases)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"Exactly one post-APRD route is selected: {selected[0].candidate_id}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "APRD replay, TAF4 overread, premature TAF8 pause, Track-2 "
                "replacement, secondary-lane shortcut, and governance shortcuts "
                "are blocked or paused: "
                + ", ".join(blocked)
                + "."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "A protocol-stack ablation preflight is the next honest TAF11 "
                "swing because it asks whether a layered finality object, not a "
                "family-local APRD patch, is needed."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T549 Results: TAF11 Post-APRD Route Reset Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Post-APRD status: `{payload['post_aprd_status']}`",
        f"- Source T548 verdict: `{payload['source_t548_verdict']}`",
        f"- Source T548 status: `{payload['source_t548_status']}`",
        "- Source T548 narrowed cases: "
        + ", ".join(f"`{item}`" for item in payload["source_t548_narrowed_cases"]),
        "- Source T548 cross-family survivors: "
        + (
            ", ".join(
                f"`{item}`" for item in payload["source_t548_cross_family_survivors"]
            )
            or "none"
        ),
        "- Selected route ids: "
        + (", ".join(f"`{item}`" for item in payload["selected_route_ids"]) or "none"),
        "",
        "## Candidate Decisions",
        "",
        "| candidate | outcome | selected? | role | missing requirements | next packet | reason |",
        "| --- | --- | :---: | --- | --- | --- | --- |",
    ]
    for decision in payload["candidate_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['candidate_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected_for_next_execution']} | "
            f"`{decision['track_role']}` | "
            f"{missing} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    selected = next(
        decision
        for decision in payload["candidate_decisions"]
        if decision["selected_for_next_execution"]
    )
    lines.extend(
        [
            "",
            "## Selected Route Contract",
            "",
            f"- Route: `{selected['candidate_id']}`",
            f"- Next packet: `{selected['next_packet']}`",
            "- Source variables: "
            + ", ".join(f"`{item}`" for item in selected["source_variables"]),
            f"- Predeclared falsifier: {selected['predeclared_falsifier']}",
            "",
            "## Hostile Controls",
            "",
            "| control | blocks candidates | reason |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["hostile_controls"]:
        blocked = ", ".join(f"`{item}`" for item in control["blocks_candidate_ids"]) or "none"
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{blocked} | "
            f"{control['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF4 Update", "taf4_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T549Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t549_result_to_dict(result)
    json_path = results_dir / "T549-taf11-post-aprd-route-reset-router-v0.1.json"
    md_path = results_dir / "T549-taf11-post-aprd-route-reset-router-v0.1-results.md"
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t549_analysis()
    payload = t549_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
