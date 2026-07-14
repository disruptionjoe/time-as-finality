"""T558: sheaf obstruction transport source-law packet.

T557 selected the sheaf obstruction transport family as a fresh TAF11
preflight contract. T558 is the first packet that actually tests the selected
variables against the mature absorbers and falsifiers. It keeps the family
contract frozen and does not establish a source law.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t557_taf11_fresh_source_law_family_preflight_gate as t557


ARTIFACT = "T558-sheaf-obstruction-transport-source-law-packet-v0.1"
VERDICT = "sheaf_obstruction_transport_packet_formal_residue_no_source_law"
PACKET_STATUS = "TAF11_FORMAL_RESIDUE_ONLY_DOMAIN_NATIVE_PACKET_REQUIRED"
NEXT_PACKET = "t559_domain_native_sheaf_transport_packet_burden_gate"
EXPECTED_SOURCE_VARIABLES = (
    "finite_event_cover",
    "local_finality_sections",
    "restriction_morphisms",
    "settlement_obstruction_witness",
    "transport_consistency_square",
    "allowed_refinement_steps",
)
EXPECTED_MATURE_ABSORBERS = (
    "ordinary_sheaf_gluing_completion",
    "resource_transport_monotone_absorber",
    "consensus_state_machine_absorber",
    "record_provenance_completion_absorber",
)
EXPECTED_FALSIFIERS = (
    "all_obstructions_glue_under_declared_restrictions",
    "transport_square_commutes_after_mature_absorbers",
    "same_source_variables_realize_target_by_relabeling",
    "hidden_target_label_or_cross_repo_rule_required",
)

NOT_CLAIMED = (
    "T558 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It only "
    "tests the frozen T557 family contract and names the next domain-native "
    "packet burden."
)


@dataclass(frozen=True)
class PacketCase:
    case_id: str
    description: str
    source_variables: tuple[str, ...]
    absorber: str
    all_obstructions_glue: bool
    transport_square_commutes_after_absorbers: bool
    same_variables_relabel_target: bool
    hidden_target_or_cross_repo_required: bool
    observerse_replay: bool
    aprd_replay: bool
    domain_native_payload: bool
    refinement_stable: bool


@dataclass(frozen=True)
class CaseDecision:
    case_id: str
    outcome: str
    admitted: bool
    role: str
    missing_source_variables: tuple[str, ...]
    absorber: str
    triggered_falsifiers: tuple[str, ...]
    reason: str


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
class T558Result:
    artifact: str
    source_t557_verdict: str
    source_t557_selected_family: str
    source_t557_selected_next_packet: str
    packet_status: str
    frozen_source_variables: tuple[str, ...]
    frozen_mature_absorbers: tuple[str, ...]
    frozen_falsifiers: tuple[str, ...]
    case_decisions: tuple[CaseDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    formal_residue_cases: tuple[str, ...]
    absorbed_cases: tuple[str, ...]
    rejected_cases: tuple[str, ...]
    verdict: str
    selected_next_packet: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t558_analysis() -> T558Result:
    t557_result = t557.run_t557_analysis()
    cases = _packet_cases(t557_result)
    decisions = tuple(_evaluate_case(case, t557_result) for case in cases)
    gates = _gate_decisions(t557_result, decisions)
    formal_residue_cases = tuple(
        decision.case_id
        for decision in decisions
        if decision.outcome == "FORMAL_RESIDUE_ONLY_DOMAIN_NATIVE_BURDEN_REMAINS"
    )
    absorbed_cases = tuple(
        decision.case_id for decision in decisions if decision.outcome.startswith("ABSORBED_")
    )
    rejected_cases = tuple(
        decision.case_id
        for decision in decisions
        if decision.outcome.startswith("REJECTED_")
        or decision.outcome.startswith("BLOCKED_")
    )
    verdict = (
        VERDICT
        if t557_result.verdict == t557.VERDICT
        and t557_result.selected_family_id == t557.SELECTED_FAMILY_ID
        and t557_result.selected_next_packet == t557.NEXT_PACKET
        and formal_residue_cases == ("formal_noncommuting_transport_fixture",)
        and all(gate.passed for gate in gates)
        else "sheaf_obstruction_transport_packet_unexpected_status"
    )

    return T558Result(
        artifact=ARTIFACT,
        source_t557_verdict=t557_result.verdict,
        source_t557_selected_family=t557_result.selected_family_id,
        source_t557_selected_next_packet=t557_result.selected_next_packet,
        packet_status=PACKET_STATUS,
        frozen_source_variables=t557_result.selected_source_variables,
        frozen_mature_absorbers=t557_result.selected_mature_absorbers,
        frozen_falsifiers=t557_result.selected_falsifiers,
        case_decisions=decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        formal_residue_cases=formal_residue_cases,
        absorbed_cases=absorbed_cases,
        rejected_cases=rejected_cases,
        verdict=verdict,
        selected_next_packet=NEXT_PACKET,
        recommended_next=(
            f"Run {NEXT_PACKET} only if a domain-native packet supplies the "
            "same frozen sheaf obstruction transport variables with a "
            "noncommuting transport square that survives the four mature "
            "absorbers and does not rely on target labels, cross-repo truth, "
            "Observerse replay, or APRD replay."
        ),
        taf11_update=(
            "TAF11 remains active but narrowed. T558 leaves one formal "
            "noncommuting transport residue and converts the next burden into "
            "a domain-native packet requirement before any source-law reading."
        ),
        taf4_update=(
            "TAF4 remains blocked. A formal sheaf obstruction transport residue "
            "is not a finite-to-continuum bridge, causal-set descent, or "
            "Lorentzian target import."
        ),
        taf8_update=(
            "TAF8 remains waiting for a real domain-native cross-domain packet. "
            "T558 is still internal TAF11 absorber/falsifier work."
        ),
        claim_labels=_claim_labels(t557_result, decisions),
        claim_ledger_update=(
            "No claim-ledger update is earned. T558 records a formal residue "
            "and next burden only; it leaves claim rows, Canon Index tiers, "
            "canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t558_result_to_dict(result: T558Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t557_verdict": result.source_t557_verdict,
        "source_t557_selected_family": result.source_t557_selected_family,
        "source_t557_selected_next_packet": result.source_t557_selected_next_packet,
        "packet_status": result.packet_status,
        "frozen_source_variables": list(result.frozen_source_variables),
        "frozen_mature_absorbers": list(result.frozen_mature_absorbers),
        "frozen_falsifiers": list(result.frozen_falsifiers),
        "case_decisions": [
            {
                "case_id": decision.case_id,
                "outcome": decision.outcome,
                "admitted": decision.admitted,
                "role": decision.role,
                "missing_source_variables": list(decision.missing_source_variables),
                "absorber": decision.absorber,
                "triggered_falsifiers": list(decision.triggered_falsifiers),
                "reason": decision.reason,
            }
            for decision in result.case_decisions
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
        "formal_residue_cases": list(result.formal_residue_cases),
        "absorbed_cases": list(result.absorbed_cases),
        "rejected_cases": list(result.rejected_cases),
        "verdict": result.verdict,
        "selected_next_packet": result.selected_next_packet,
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


def _packet_cases(t557_result: t557.T557Result) -> tuple[PacketCase, ...]:
    variables = t557_result.selected_source_variables
    return (
        PacketCase(
            case_id="ordinary_gluing_completion_control",
            description="All declared local sections glue under restrictions.",
            source_variables=variables,
            absorber="ordinary_sheaf_gluing_completion",
            all_obstructions_glue=True,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=True,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="resource_transport_monotone_control",
            description="The apparent transport obstruction is a resource drawdown.",
            source_variables=variables,
            absorber="resource_transport_monotone_absorber",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=True,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="consensus_state_machine_control",
            description="The obstruction is ordinary consensus state divergence.",
            source_variables=variables,
            absorber="consensus_state_machine_absorber",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=True,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="record_provenance_completion_control",
            description="Missing provenance fields complete the obstruction witness.",
            source_variables=variables,
            absorber="record_provenance_completion_absorber",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=True,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="same_variables_relabel_target_control",
            description="The same variables realize the target by relabeling only.",
            source_variables=variables,
            absorber="none",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=True,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=False,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="hidden_target_import_control",
            description="The packet needs target labels or cross-repo truth.",
            source_variables=variables,
            absorber="none",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=True,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=False,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="observerse_replay_control",
            description="The packet reuses the absorbed Observerse protocol stack.",
            source_variables=variables,
            absorber="none",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=True,
            aprd_replay=False,
            domain_native_payload=False,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="aprd_replay_control",
            description="The packet reuses APRD after its cross-family narrowing.",
            source_variables=variables,
            absorber="none",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=True,
            domain_native_payload=False,
            refinement_stable=True,
        ),
        PacketCase(
            case_id="formal_noncommuting_transport_fixture",
            description=(
                "A formal finite cover has a noncommuting transport square after "
                "the declared absorber controls, but no domain-native payload."
            ),
            source_variables=variables,
            absorber="none",
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            domain_native_payload=False,
            refinement_stable=True,
        ),
    )


def _evaluate_case(case: PacketCase, t557_result: t557.T557Result) -> CaseDecision:
    missing = tuple(
        variable
        for variable in t557_result.selected_source_variables
        if variable not in case.source_variables
    )
    falsifiers = _triggered_falsifiers(case, t557_result)

    if missing:
        return CaseDecision(
            case_id=case.case_id,
            outcome="REJECTED_UNDERDECLARED_SOURCE_VARIABLES",
            admitted=False,
            role="underdeclared",
            missing_source_variables=missing,
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason="The packet does not carry every frozen T557 source variable.",
        )
    if case.hidden_target_or_cross_repo_required:
        return CaseDecision(
            case_id=case.case_id,
            outcome="REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT",
            admitted=False,
            role="falsifier",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason="The packet depends on target labels or cross-repo truth.",
        )
    if case.observerse_replay:
        return CaseDecision(
            case_id=case.case_id,
            outcome="REJECTED_OBSERVERSE_REPLAY",
            admitted=False,
            role="spent_route",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason="T556 parked the Observerse route as audit residue only.",
        )
    if case.aprd_replay:
        return CaseDecision(
            case_id=case.case_id,
            outcome="REJECTED_APRD_REPLAY",
            admitted=False,
            role="narrowed_route",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason="APRD remains family-local feeder evidence, not this fresh family.",
        )
    if case.same_variables_relabel_target:
        return CaseDecision(
            case_id=case.case_id,
            outcome="REJECTED_RELABELING_FALSIFIER",
            admitted=False,
            role="falsifier",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason="The same source variables realize the target by relabeling only.",
        )
    if case.absorber != "none":
        return CaseDecision(
            case_id=case.case_id,
            outcome=_absorber_outcome(case.absorber),
            admitted=False,
            role="absorbed_control",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason=f"The mature absorber `{case.absorber}` receives normal state and comparison rights.",
        )
    if not case.domain_native_payload:
        return CaseDecision(
            case_id=case.case_id,
            outcome="FORMAL_RESIDUE_ONLY_DOMAIN_NATIVE_BURDEN_REMAINS",
            admitted=True,
            role="formal_residue",
            missing_source_variables=(),
            absorber=case.absorber,
            triggered_falsifiers=falsifiers,
            reason=(
                "The finite formal packet leaves a noncommuting transport shape, "
                "but without a domain-native payload it is not source-law evidence."
            ),
        )
    return CaseDecision(
        case_id=case.case_id,
        outcome="BLOCKED_UNEXPECTED_SOURCE_LAW_SURVIVOR",
        admitted=False,
        role="review_stop",
        missing_source_variables=(),
        absorber=case.absorber,
        triggered_falsifiers=falsifiers,
        reason="A domain-native survivor would require a separate review packet.",
    )


def _triggered_falsifiers(
    case: PacketCase, t557_result: t557.T557Result
) -> tuple[str, ...]:
    falsifiers: list[str] = []
    declared = set(t557_result.selected_falsifiers)
    if (
        "all_obstructions_glue_under_declared_restrictions" in declared
        and case.all_obstructions_glue
    ):
        falsifiers.append("all_obstructions_glue_under_declared_restrictions")
    if (
        "transport_square_commutes_after_mature_absorbers" in declared
        and case.transport_square_commutes_after_absorbers
    ):
        falsifiers.append("transport_square_commutes_after_mature_absorbers")
    if (
        "same_source_variables_realize_target_by_relabeling" in declared
        and case.same_variables_relabel_target
    ):
        falsifiers.append("same_source_variables_realize_target_by_relabeling")
    if (
        "hidden_target_label_or_cross_repo_rule_required" in declared
        and case.hidden_target_or_cross_repo_required
    ):
        falsifiers.append("hidden_target_label_or_cross_repo_rule_required")
    return tuple(falsifiers)


def _absorber_outcome(absorber: str) -> str:
    return {
        "ordinary_sheaf_gluing_completion": "ABSORBED_ORDINARY_SHEAF_GLUE",
        "resource_transport_monotone_absorber": "ABSORBED_RESOURCE_TRANSPORT_MONOTONE",
        "consensus_state_machine_absorber": "ABSORBED_CONSENSUS_STATE_MACHINE",
        "record_provenance_completion_absorber": "ABSORBED_RECORD_PROVENANCE_COMPLETION",
    }[absorber]


def _gate_decisions(
    t557_result: t557.T557Result, decisions: tuple[CaseDecision, ...]
) -> tuple[GateDecision, ...]:
    decision_by_id = {decision.case_id: decision for decision in decisions}
    absorber_outcomes = {
        decision.absorber: decision.outcome
        for decision in decisions
        if decision.absorber != "none"
    }
    triggered_falsifiers = {
        falsifier
        for decision in decisions
        for falsifier in decision.triggered_falsifiers
    }
    formal_residue = [
        decision
        for decision in decisions
        if decision.outcome == "FORMAL_RESIDUE_ONLY_DOMAIN_NATIVE_BURDEN_REMAINS"
    ]
    gates = (
        (
            "t557_preflight_authority",
            t557_result.verdict == t557.VERDICT
            and t557_result.selected_family_id == t557.SELECTED_FAMILY_ID
            and t557_result.selected_next_packet == t557.NEXT_PACKET,
            "T557 supplies the expected fresh-family preflight authority.",
            "T557 did not supply the expected source state.",
        ),
        (
            "family_contract_frozen",
            tuple(t557_result.selected_source_variables) == EXPECTED_SOURCE_VARIABLES
            and tuple(t557_result.selected_mature_absorbers) == EXPECTED_MATURE_ABSORBERS
            and tuple(t557_result.selected_falsifiers) == EXPECTED_FALSIFIERS,
            "The T557 variables, absorbers, and falsifiers are unchanged.",
            "The packet changed the T557 family contract.",
        ),
        (
            "all_mature_absorbers_exercised",
            all(
                absorber in absorber_outcomes
                and absorber_outcomes[absorber].startswith("ABSORBED_")
                for absorber in t557_result.selected_mature_absorbers
            ),
            "Every mature absorber receives a control case.",
            "One or more mature absorbers were not exercised.",
        ),
        (
            "all_declared_falsifiers_exercised",
            set(t557_result.selected_falsifiers) <= triggered_falsifiers,
            "Every declared falsifier is triggered by at least one control case.",
            "One or more T557 falsifiers were not tested.",
        ),
        (
            "spent_routes_and_imports_rejected",
            decision_by_id["observerse_replay_control"].outcome == "REJECTED_OBSERVERSE_REPLAY"
            and decision_by_id["aprd_replay_control"].outcome == "REJECTED_APRD_REPLAY"
            and decision_by_id["hidden_target_import_control"].outcome
            == "REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT",
            "Observerse replay, APRD replay, and hidden target import are rejected.",
            "A spent route or import shortcut was allowed.",
        ),
        (
            "formal_residue_bounded",
            len(formal_residue) == 1
            and formal_residue[0].case_id == "formal_noncommuting_transport_fixture"
            and formal_residue[0].admitted,
            "Exactly one formal residue remains, and it is not source-law evidence.",
            "The formal residue boundary is unclear.",
        ),
        (
            "no_source_law_or_governance_movement",
            not any(
                decision.outcome == "BLOCKED_UNEXPECTED_SOURCE_LAW_SURVIVOR"
                for decision in decisions
            ),
            "No source law, TAF4, TAF8, claim, canon, public-posture, external, or cross-repo movement is attempted.",
            "The packet tried to move a source-law or governance boundary.",
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
            control_id="ordinary_sheaf_gluing_control",
            blocks="Mistaking ordinary compatible local sections for a new source law.",
            reason="If all obstructions glue under declared restrictions, the first T557 falsifier fires.",
        ),
        HostileControl(
            control_id="resource_transport_monotone_control",
            blocks="Reading resource drawdown or transport budget as sheaf obstruction law.",
            reason="Mature resource transport monotones receive normal comparison rights.",
        ),
        HostileControl(
            control_id="consensus_state_machine_control",
            blocks="Reading consensus state divergence as finality-native sheaf law.",
            reason="Ordinary consensus/state-machine completion absorbs that split.",
        ),
        HostileControl(
            control_id="record_provenance_completion_control",
            blocks="Reading missing provenance fields as source-law evidence.",
            reason="Record-provenance completion absorbs missing-witness pressure.",
        ),
        HostileControl(
            control_id="target_import_and_relabeling_control",
            blocks="Target labels, cross-repo rules, or relabel-only target realization.",
            reason="Those are explicit T557 falsifiers, not admissible evidence.",
        ),
        HostileControl(
            control_id="taf4_taf8_public_posture_control",
            blocks="Moving TAF4, executing TAF8, or changing claim/canon/public posture.",
            reason="T558 has only repo-local TAF11 absorber/falsifier authority.",
        ),
    )


def _claim_labels(
    t557_result: t557.T557Result, decisions: tuple[CaseDecision, ...]
) -> tuple[ClaimLabel, ...]:
    absorbed_count = sum(1 for decision in decisions if decision.outcome.startswith("ABSORBED_"))
    rejected_count = sum(
        1
        for decision in decisions
        if decision.outcome.startswith("REJECTED_")
        or decision.outcome.startswith("BLOCKED_")
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T557 is consumed as preflight authority: "
                f"{t557_result.verdict}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{absorbed_count} mature absorber controls absorb or close "
                "ordinary readings of the selected family."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{rejected_count} shortcut or falsifier controls reject spent "
                "routes, imports, and relabel-only readings."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The noncommuting finite transport fixture is a formal residue "
                "only because it has no domain-native payload."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T558 Results: Sheaf Obstruction Transport Source-Law Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Packet status: `{payload['packet_status']}`",
        f"- Source T557 verdict: `{payload['source_t557_verdict']}`",
        f"- Source T557 selected family: `{payload['source_t557_selected_family']}`",
        f"- Source T557 selected next packet: `{payload['source_t557_selected_next_packet']}`",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Frozen T557 Contract",
        "",
        "Source variables:",
    ]
    lines.extend(f"- `{item}`" for item in payload["frozen_source_variables"])
    lines.extend(["", "Mature absorbers:"])
    lines.extend(f"- `{item}`" for item in payload["frozen_mature_absorbers"])
    lines.extend(["", "Falsifiers:"])
    lines.extend(f"- `{item}`" for item in payload["frozen_falsifiers"])
    lines.extend(
        [
            "",
            "## Case Decisions",
            "",
            "| case | outcome | admitted? | role | absorber | falsifiers | reason |",
            "| --- | --- | :---: | --- | --- | --- | --- |",
        ]
    )
    for decision in payload["case_decisions"]:
        falsifiers = ", ".join(decision["triggered_falsifiers"]) or "none"
        lines.append(
            "| "
            f"`{decision['case_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['admitted']} | "
            f"`{decision['role']}` | "
            f"`{decision['absorber']}` | "
            f"{falsifiers} | "
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


def write_results(result: T558Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t558_result_to_dict(result)
    json_path = results_dir / "T558-sheaf-obstruction-transport-source-law-packet-v0.1.json"
    md_path = (
        results_dir
        / "T558-sheaf-obstruction-transport-source-law-packet-v0.1-results.md"
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

    result = run_t558_analysis()
    payload = t558_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
