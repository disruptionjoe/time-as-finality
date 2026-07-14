"""T557: TAF11 fresh source-law family preflight gate.

T556 parked the absorbed Observerse protocol-stack route as audit translation
residue and required any renewed TAF11 attempt to begin from a fresh family
with source variables, mature absorbers, and falsifiers declared before target
outcomes are read. T557 performs that preflight only. It does not test the
family as a source law.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t556_observerse_protocol_stack_post_absorber_route_reset_gate as t556


ARTIFACT = "T557-taf11-fresh-source-law-family-preflight-gate-v0.1"
VERDICT = "fresh_source_law_family_preflight_selects_sheaf_obstruction_transport"
PREFLIGHT_STATUS = "TAF11_FRESH_FAMILY_DECLARED_PREFLIGHT_ONLY"
SELECTED_FAMILY_ID = "sheaf_obstruction_transport_family"
NEXT_PACKET = "t558_sheaf_obstruction_transport_source_law_packet"

NOT_CLAIMED = (
    "T557 does not establish a source law, validate the selected family, prove "
    "shadow protection, derive spacetime, prove manifoldlikeness, repair T528, "
    "reverse T223, unpause S1, promote S1, change claim status, change Canon "
    "Index tiers, change canon verdicts, change public posture, change the "
    "North Star, authorize external publication, move TAF4, execute TAF8, or "
    "move cross-repo truth. It only declares a fresh TAF11 family contract and "
    "the next executable packet that must test it."
)


@dataclass(frozen=True)
class FamilyCandidate:
    candidate_id: str
    description: str
    source_variables: tuple[str, ...]
    mature_absorbers: tuple[str, ...]
    falsifiers: tuple[str, ...]
    reuses_observerse_protocol_stack: bool
    replays_aprd_family: bool
    imports_target_or_cross_repo_truth: bool
    computable_before_target_reading: bool
    blocks_taf4_movement: bool
    blocks_taf8_execution: bool
    no_claim_canon_public_external_movement: bool
    next_packet: str


@dataclass(frozen=True)
class FamilyDecision:
    candidate_id: str
    outcome: str
    selected: bool
    role: str
    missing_requirements: tuple[str, ...]
    reason: str
    next_packet: str


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks: str
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T557Result:
    artifact: str
    source_t556_verdict: str
    source_t556_selected_next_packet: str
    preflight_status: str
    family_decisions: tuple[FamilyDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    selected_family_id: str
    selected_source_variables: tuple[str, ...]
    selected_mature_absorbers: tuple[str, ...]
    selected_falsifiers: tuple[str, ...]
    selected_next_packet: str
    verdict: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t557_analysis() -> T557Result:
    t556_result = t556.run_t556_analysis()
    decisions = tuple(_evaluate_candidate(candidate) for candidate in _family_candidates())
    selected = tuple(decision for decision in decisions if decision.selected)
    gates = _gate_decisions(t556_result, decisions, selected)
    selected_candidate = _candidate_by_id(SELECTED_FAMILY_ID)
    selected_family_id = selected[0].candidate_id if len(selected) == 1 else "none"
    selected_next_packet = selected[0].next_packet if len(selected) == 1 else "none"
    verdict = (
        VERDICT
        if t556_result.verdict == t556.VERDICT
        and t556_result.selected_next_packet == t556.NEXT_PACKET
        and selected_family_id == SELECTED_FAMILY_ID
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gates)
        else "fresh_source_law_family_preflight_unexpected_status"
    )

    return T557Result(
        artifact=ARTIFACT,
        source_t556_verdict=t556_result.verdict,
        source_t556_selected_next_packet=t556_result.selected_next_packet,
        preflight_status=PREFLIGHT_STATUS,
        family_decisions=decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        selected_family_id=selected_family_id,
        selected_source_variables=selected_candidate.source_variables,
        selected_mature_absorbers=selected_candidate.mature_absorbers,
        selected_falsifiers=selected_candidate.falsifiers,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        recommended_next=(
            f"Run {NEXT_PACKET} as the first test of the selected family. Keep "
            "the family contract frozen, test the declared sheaf obstruction "
            "transport variables against the mature absorbers and falsifiers, "
            "and reject if target labels, cross-repo truth, Observerse replay, "
            "or APRD replay enter the result."
        ),
        taf11_update=(
            "TAF11 remains the active high-value route. T557 selects the fresh "
            "sheaf obstruction transport family as a preflight contract only; "
            "source-law status waits for the next executable packet."
        ),
        taf4_update=(
            "TAF4 remains blocked. A fresh TAF11 family preflight is not a "
            "finite-to-continuum bridge, causal-set descent, or Lorentzian "
            "target import."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T557 is internal TAF11 family selection, not TAF8 execution."
        ),
        claim_labels=_claim_labels(t556_result, decisions, selected_candidate),
        claim_ledger_update=(
            "No claim-ledger update is earned. T557 declares a test family and "
            "next packet only; it leaves claim rows, Canon Index tiers, canon "
            "verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t557_result_to_dict(result: T557Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t556_verdict": result.source_t556_verdict,
        "source_t556_selected_next_packet": result.source_t556_selected_next_packet,
        "preflight_status": result.preflight_status,
        "family_decisions": [
            {
                "candidate_id": decision.candidate_id,
                "outcome": decision.outcome,
                "selected": decision.selected,
                "role": decision.role,
                "missing_requirements": list(decision.missing_requirements),
                "reason": decision.reason,
                "next_packet": decision.next_packet,
            }
            for decision in result.family_decisions
        ],
        "gate_decisions": [
            {
                "gate_id": gate.gate_id,
                "outcome": gate.outcome,
                "passed": gate.passed,
                "reason": gate.reason,
            }
            for gate in result.gate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks": control.blocks,
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "selected_family_id": result.selected_family_id,
        "selected_source_variables": list(result.selected_source_variables),
        "selected_mature_absorbers": list(result.selected_mature_absorbers),
        "selected_falsifiers": list(result.selected_falsifiers),
        "selected_next_packet": result.selected_next_packet,
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


def _family_candidates() -> tuple[FamilyCandidate, ...]:
    return (
        FamilyCandidate(
            candidate_id=SELECTED_FAMILY_ID,
            description=(
                "A finality-native sheaf obstruction transport family over "
                "finite event covers, local finality sections, restriction "
                "morphisms, and obstruction witnesses."
            ),
            source_variables=(
                "finite_event_cover",
                "local_finality_sections",
                "restriction_morphisms",
                "settlement_obstruction_witness",
                "transport_consistency_square",
                "allowed_refinement_steps",
            ),
            mature_absorbers=(
                "ordinary_sheaf_gluing_completion",
                "resource_transport_monotone_absorber",
                "consensus_state_machine_absorber",
                "record_provenance_completion_absorber",
            ),
            falsifiers=(
                "all_obstructions_glue_under_declared_restrictions",
                "transport_square_commutes_after_mature_absorbers",
                "same_source_variables_realize_target_by_relabeling",
                "hidden_target_label_or_cross_repo_rule_required",
            ),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet=NEXT_PACKET,
        ),
        FamilyCandidate(
            candidate_id="observerse_protocol_stack_replay",
            description="Reuse the absorbed Observerse protocol-stack route.",
            source_variables=(),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=True,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="aprd_replay_as_fresh_family",
            description="Replay APRD after its cross-family narrowing.",
            source_variables=("accessible_provenance_reconstruction_debt",),
            mature_absorbers=("aprd_family_local_completion",),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=True,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="target_or_cross_repo_import_family",
            description="Select a family by reading target labels or another repo.",
            source_variables=("target_label",),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=True,
            computable_before_target_reading=False,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="pause_no_fresh_family_declared",
            description="Do not name a family in this packet.",
            source_variables=(),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="taf4_from_fresh_family_preflight",
            description="Move TAF4 from family selection alone.",
            source_variables=("finite_event_cover",),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=True,
            computable_before_target_reading=False,
            blocks_taf4_movement=False,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="taf8_from_fresh_family_preflight",
            description="Execute TAF8 from internal TAF11 family selection.",
            source_variables=("finite_event_cover",),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=False,
            no_claim_canon_public_external_movement=True,
            next_packet="none",
        ),
        FamilyCandidate(
            candidate_id="claim_canon_public_posture_shortcut",
            description="Move claim, canon, public posture, or external state.",
            source_variables=("finite_event_cover",),
            mature_absorbers=(),
            falsifiers=(),
            reuses_observerse_protocol_stack=False,
            replays_aprd_family=False,
            imports_target_or_cross_repo_truth=False,
            computable_before_target_reading=True,
            blocks_taf4_movement=True,
            blocks_taf8_execution=True,
            no_claim_canon_public_external_movement=False,
            next_packet="none",
        ),
    )


def _candidate_by_id(candidate_id: str) -> FamilyCandidate:
    for candidate in _family_candidates():
        if candidate.candidate_id == candidate_id:
            return candidate
    raise KeyError(candidate_id)


def _evaluate_candidate(candidate: FamilyCandidate) -> FamilyDecision:
    missing = _missing_requirements(candidate)
    if not candidate.no_claim_canon_public_external_movement:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            role="forbidden",
            missing_requirements=missing,
            reason="Family preflight cannot move claims, canon, public posture, or external state.",
            next_packet="none",
        )
    if not candidate.blocks_taf4_movement:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            role="blocked",
            missing_requirements=missing,
            reason="A preflight family declaration is not a finite-to-continuum bridge.",
            next_packet="none",
        )
    if not candidate.blocks_taf8_execution:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            role="blocked",
            missing_requirements=missing,
            reason="Internal TAF11 family selection is not a domain-native TAF8 packet.",
            next_packet="none",
        )
    if candidate.reuses_observerse_protocol_stack:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="REJECTED_OBSERVERSE_REPLAY",
            selected=False,
            role="retired_route",
            missing_requirements=missing,
            reason="T556 parked the absorbed Observerse route as audit residue only.",
            next_packet="none",
        )
    if candidate.replays_aprd_family:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="REJECTED_APRD_REPLAY",
            selected=False,
            role="narrowed_route",
            missing_requirements=missing,
            reason="T548 narrowed APRD to family-local feeder evidence, not a fresh family.",
            next_packet="none",
        )
    if candidate.imports_target_or_cross_repo_truth:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="BLOCKED_TARGET_OR_CROSS_REPO_IMPORT",
            selected=False,
            role="forbidden_import",
            missing_requirements=missing,
            reason="Fresh-family preflight must be declared before target labels or cross-repo truth enter.",
            next_packet="none",
        )
    if candidate.candidate_id == "pause_no_fresh_family_declared":
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="REJECTED_NO_FAMILY_DECLARED",
            selected=False,
            role="underdeclared",
            missing_requirements=missing,
            reason="T556 specifically requires this packet to declare a fresh family contract.",
            next_packet="none",
        )
    if candidate.candidate_id == SELECTED_FAMILY_ID and not missing:
        return FamilyDecision(
            candidate_id=candidate.candidate_id,
            outcome="SELECTED_FRESH_FAMILY_PREFLIGHT",
            selected=True,
            role="taf11_fresh_family_contract",
            missing_requirements=(),
            reason="The family declares variables, mature absorbers, falsifiers, and a next packet before target reading.",
            next_packet=candidate.next_packet,
        )
    return FamilyDecision(
        candidate_id=candidate.candidate_id,
        outcome="REVIEW_ONLY_UNDERDECLARED",
        selected=False,
        role="underdeclared",
        missing_requirements=missing,
        reason="The candidate lacks one or more fresh-family preflight requirements.",
        next_packet="none",
    )


def _missing_requirements(candidate: FamilyCandidate) -> tuple[str, ...]:
    missing: list[str] = []
    if not candidate.source_variables:
        missing.append("source_variables_declared")
    if not candidate.mature_absorbers:
        missing.append("mature_absorbers_predeclared")
    if not candidate.falsifiers:
        missing.append("falsifiers_predeclared")
    if candidate.reuses_observerse_protocol_stack:
        missing.append("does_not_reuse_absorbed_observerse_stack")
    if candidate.replays_aprd_family:
        missing.append("does_not_replay_narrowed_aprd_family")
    if candidate.imports_target_or_cross_repo_truth:
        missing.append("no_target_or_cross_repo_import")
    if not candidate.computable_before_target_reading:
        missing.append("computable_before_target_reading")
    if not candidate.blocks_taf4_movement:
        missing.append("blocks_taf4_movement")
    if not candidate.blocks_taf8_execution:
        missing.append("blocks_taf8_execution")
    if not candidate.no_claim_canon_public_external_movement:
        missing.append("no_claim_canon_public_external_movement")
    if candidate.next_packet == "none":
        missing.append("next_packet_declared")
    return tuple(missing)


def _gate_decisions(
    t556_result: t556.T556Result,
    decisions: tuple[FamilyDecision, ...],
    selected: tuple[FamilyDecision, ...],
) -> tuple[GateDecision, ...]:
    decision_by_id = {decision.candidate_id: decision for decision in decisions}
    selected_candidate = _candidate_by_id(SELECTED_FAMILY_ID)
    gates = (
        (
            "t556_route_reset_authority",
            t556_result.verdict == t556.VERDICT
            and t556_result.selected_next_packet == t556.NEXT_PACKET,
            "T556 selected the fresh-family preflight as the next TAF11 burden.",
            "T556 did not provide the expected route-reset authority.",
        ),
        (
            "exactly_one_fresh_family_selected",
            len(selected) == 1
            and selected[0].candidate_id == SELECTED_FAMILY_ID
            and selected[0].next_packet == NEXT_PACKET,
            "Exactly one fresh family and next packet are selected.",
            "The preflight did not select exactly one fresh family.",
        ),
        (
            "source_variables_absorbers_and_falsifiers_declared",
            bool(selected_candidate.source_variables)
            and bool(selected_candidate.mature_absorbers)
            and bool(selected_candidate.falsifiers),
            "The selected family declares source variables, mature absorbers, and falsifiers.",
            "The selected family is underdeclared.",
        ),
        (
            "observerse_and_aprd_replays_rejected",
            decision_by_id["observerse_protocol_stack_replay"].outcome
            == "REJECTED_OBSERVERSE_REPLAY"
            and decision_by_id["aprd_replay_as_fresh_family"].outcome
            == "REJECTED_APRD_REPLAY",
            "Observerse and APRD replay routes are rejected.",
            "A spent route was allowed to masquerade as a fresh family.",
        ),
        (
            "target_and_cross_repo_imports_blocked",
            decision_by_id["target_or_cross_repo_import_family"].outcome
            == "BLOCKED_TARGET_OR_CROSS_REPO_IMPORT",
            "Target-label and cross-repo imports are blocked.",
            "The family depended on target labels or cross-repo truth.",
        ),
        (
            "taf4_taf8_boundaries_preserved",
            decision_by_id["taf4_from_fresh_family_preflight"].outcome
            == "BLOCKED_TAF4_OVERREAD"
            and decision_by_id["taf8_from_fresh_family_preflight"].outcome
            == "BLOCKED_TAF8_OVERREAD",
            "TAF4 and TAF8 shortcuts are blocked.",
            "TAF4 or TAF8 moved from family selection alone.",
        ),
        (
            "governance_boundaries_preserved",
            decision_by_id["claim_canon_public_posture_shortcut"].outcome
            == "BLOCKED_GOVERNANCE",
            "No claim, canon, public-posture, external, or cross-repo movement is attempted.",
            "A forbidden governance movement was allowed.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in gates
    )


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="observerse_absorber_replay_control",
            blocks="Reusing the absorbed T550-T556 Observerse protocol-stack route.",
            reason="T556 parked that route as audit translation residue only.",
        ),
        HostileControl(
            control_id="aprd_narrowing_control",
            blocks="Replaying APRD as if T548 did not narrow it.",
            reason="APRD remains useful feeder evidence but not the fresh source-law family.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Selecting the family from target labels or cross-repo truth.",
            reason="The family contract must be declared before target reading.",
        ),
        HostileControl(
            control_id="absorber_and_falsifier_control",
            blocks="Testing a family without mature absorbers and falsifiers.",
            reason="T556 required absorbers and falsifiers before renewed TAF11 source-law attempts.",
        ),
        HostileControl(
            control_id="taf4_taf8_shortcut_control",
            blocks="Moving TAF4 or executing TAF8 from preflight selection.",
            reason="A family contract is not a continuum bridge or cross-domain theorem.",
        ),
        HostileControl(
            control_id="public_posture_control",
            blocks="Changing claim rows, Canon Index tiers, canon verdicts, public posture, or publication state.",
            reason="The packet has no governance movement authority.",
        ),
    )


def _claim_labels(
    t556_result: t556.T556Result,
    decisions: tuple[FamilyDecision, ...],
    selected_candidate: FamilyCandidate,
) -> tuple[ClaimLabel, ...]:
    selected = next(decision for decision in decisions if decision.selected)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T556 is consumed as route-reset authority: "
                f"{t556_result.verdict}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The selected fresh family is "
                f"{selected.candidate_id} with next packet {selected.next_packet}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The selected family declares "
                f"{len(selected_candidate.source_variables)} source variables, "
                f"{len(selected_candidate.mature_absorbers)} mature absorbers, "
                f"and {len(selected_candidate.falsifiers)} falsifiers."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "Sheaf obstruction transport is the next honest TAF11 family "
                "because it is fresh relative to Observerse and APRD while "
                "remaining finality-native and falsifiable before target import."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T557 Results: TAF11 Fresh Source-Law Family Preflight Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Preflight status: `{payload['preflight_status']}`",
        f"- Source T556 verdict: `{payload['source_t556_verdict']}`",
        f"- Source T556 selected next packet: `{payload['source_t556_selected_next_packet']}`",
        f"- Selected family: `{payload['selected_family_id']}`",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Selected Family Contract",
        "",
        "Source variables:",
    ]
    lines.extend(f"- `{item}`" for item in payload["selected_source_variables"])
    lines.extend(["", "Mature absorbers:"])
    lines.extend(f"- `{item}`" for item in payload["selected_mature_absorbers"])
    lines.extend(["", "Falsifiers:"])
    lines.extend(f"- `{item}`" for item in payload["selected_falsifiers"])
    lines.extend(
        [
            "",
            "## Family Decisions",
            "",
            "| candidate | outcome | selected? | role | missing requirements | next packet | reason |",
            "| --- | --- | :---: | --- | --- | --- | --- |",
        ]
    )
    for decision in payload["family_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['candidate_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
            f"`{decision['role']}` | "
            f"{missing} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Gate Decisions",
            "",
            "| gate | outcome | passed? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(["", "## Hostile Controls", "", "| control | blocks | reason |", "| --- | --- | --- |"])
    for control in payload["hostile_controls"]:
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{control['blocks']} | "
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


def write_results(result: T557Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t557_result_to_dict(result)
    json_path = results_dir / "T557-taf11-fresh-source-law-family-preflight-gate-v0.1.json"
    md_path = (
        results_dir
        / "T557-taf11-fresh-source-law-family-preflight-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t557_analysis()
    payload = t557_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
