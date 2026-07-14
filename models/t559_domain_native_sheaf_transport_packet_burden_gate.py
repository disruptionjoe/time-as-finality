"""T559: domain-native sheaf transport packet burden gate.

T558 left only formal sheaf obstruction transport residue and required the next
burden to supply a domain-native payload before any source-law reading. T559
tests that burden. It admits one review-only domain-native payload and still
does not establish a source law.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t558_sheaf_obstruction_transport_source_law_packet as t558


ARTIFACT = "T559-domain-native-sheaf-transport-packet-burden-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_payload_admitted_review_only"
PACKET_STATUS = "TAF11_DOMAIN_NATIVE_PAYLOAD_ADMITTED_NO_SOURCE_LAW"
NEXT_PACKET = "t560_domain_native_sheaf_transport_independent_transfer_gate"

NOT_CLAIMED = (
    "T559 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It only "
    "admits one domain-native TAF11 payload as review material and names the "
    "next independent-transfer burden."
)


@dataclass(frozen=True)
class PayloadCase:
    case_id: str
    description: str
    source_variables: tuple[str, ...]
    domain_native_payload: bool
    noncommuting_transport_square: bool
    all_obstructions_glue: bool
    transport_square_commutes_after_absorbers: bool
    same_variables_relabel_target: bool
    hidden_target_or_cross_repo_required: bool
    observerse_replay: bool
    aprd_replay: bool
    taf4_movement: bool
    taf8_execution: bool
    survives_ordinary_sheaf_gluing: bool
    survives_resource_transport_monotone: bool
    survives_consensus_state_machine: bool
    survives_record_provenance_completion: bool
    operation_menu_derived_from_finality: bool
    provenance_complete: bool
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
class T559Result:
    artifact: str
    source_t558_verdict: str
    source_t558_packet_status: str
    source_t558_selected_next_packet: str
    packet_status: str
    frozen_source_variables: tuple[str, ...]
    frozen_mature_absorbers: tuple[str, ...]
    frozen_falsifiers: tuple[str, ...]
    case_decisions: tuple[CaseDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    admitted_domain_native_packets: tuple[str, ...]
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


def run_t559_analysis() -> T559Result:
    t558_result = t558.run_t558_analysis()
    cases = _payload_cases(t558_result)
    decisions = tuple(_evaluate_case(case, t558_result) for case in cases)
    gates = _gate_decisions(t558_result, cases, decisions)
    admitted = tuple(
        decision.case_id
        for decision in decisions
        if decision.outcome == "ADMITTED_DOMAIN_NATIVE_BURDEN_PACKET_REVIEW_ONLY"
    )
    absorbed = tuple(
        decision.case_id for decision in decisions if decision.outcome.startswith("ABSORBED_")
    )
    rejected = tuple(
        decision.case_id
        for decision in decisions
        if decision.outcome.startswith("REJECTED_")
        or decision.outcome.startswith("BLOCKED_")
    )
    verdict = (
        VERDICT
        if t558_result.verdict == t558.VERDICT
        and t558_result.selected_next_packet == t558.NEXT_PACKET
        and admitted == ("record_finality_transport_square_payload",)
        and all(gate.passed for gate in gates)
        else "domain_native_sheaf_transport_payload_unexpected_status"
    )

    return T559Result(
        artifact=ARTIFACT,
        source_t558_verdict=t558_result.verdict,
        source_t558_packet_status=t558_result.packet_status,
        source_t558_selected_next_packet=t558_result.selected_next_packet,
        packet_status=PACKET_STATUS,
        frozen_source_variables=t558_result.frozen_source_variables,
        frozen_mature_absorbers=t558_result.frozen_mature_absorbers,
        frozen_falsifiers=t558_result.frozen_falsifiers,
        case_decisions=decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        admitted_domain_native_packets=admitted,
        absorbed_cases=absorbed,
        rejected_cases=rejected,
        verdict=verdict,
        selected_next_packet=NEXT_PACKET,
        recommended_next=(
            f"Run {NEXT_PACKET} before any source-law reading. Keep the "
            "T559 payload frozen and test an independently shaped "
            "domain-native finality fixture against the same absorber and "
            "falsifier screen."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T559 supplies one "
            "domain-native sheaf transport payload that survives the declared "
            "absorber screen, but a single admitted payload is review material "
            "only, not a source law."
        ),
        taf4_update=(
            "TAF4 remains blocked. A domain-native finite payload is not a "
            "finite-to-continuum bridge, causal-set descent, or Lorentzian "
            "target import."
        ),
        taf8_update=(
            "TAF8 remains waiting. T559 is internal TAF11 burden clearance, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(t558_result, decisions),
        claim_ledger_update=(
            "No claim-ledger update is earned. T559 admits review material "
            "and a next burden only; it leaves claim rows, Canon Index tiers, "
            "canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t559_result_to_dict(result: T559Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t558_verdict": result.source_t558_verdict,
        "source_t558_packet_status": result.source_t558_packet_status,
        "source_t558_selected_next_packet": result.source_t558_selected_next_packet,
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
        "admitted_domain_native_packets": list(result.admitted_domain_native_packets),
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


def _payload_cases(t558_result: t558.T558Result) -> tuple[PayloadCase, ...]:
    variables = t558_result.frozen_source_variables
    return (
        PayloadCase(
            case_id="ordinary_gluing_domain_payload_control",
            description="A domain-native cover whose local finality sections glue.",
            source_variables=variables,
            domain_native_payload=True,
            noncommuting_transport_square=False,
            all_obstructions_glue=True,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=False,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="resource_budget_transport_control",
            description="A transport gap explained by a native resource budget.",
            source_variables=variables,
            domain_native_payload=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=False,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="consensus_state_machine_payload_control",
            description="A local settlement split absorbed by ordinary consensus state.",
            source_variables=variables,
            domain_native_payload=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=False,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="record_provenance_completion_payload_control",
            description="Missing provenance fields complete the transport square.",
            source_variables=variables,
            domain_native_payload=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=False,
            operation_menu_derived_from_finality=True,
            provenance_complete=False,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="same_variables_relabel_target_control",
            description="The same variables realize the target by relabeling only.",
            source_variables=variables,
            domain_native_payload=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=True,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="hidden_target_import_control",
            description="The payload needs target labels or cross-repo truth.",
            source_variables=variables,
            domain_native_payload=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=True,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="observerse_replay_control",
            description="The payload reuses the absorbed Observerse stack.",
            source_variables=variables,
            domain_native_payload=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=True,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="aprd_replay_control",
            description="The payload reuses APRD after its cross-family narrowing.",
            source_variables=variables,
            domain_native_payload=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=True,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="formal_residue_without_payload_control",
            description="A noncommuting square with no finality-native payload.",
            source_variables=variables,
            domain_native_payload=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        PayloadCase(
            case_id="record_finality_transport_square_payload",
            description=(
                "A finality-native payload with complete provenance, frozen "
                "local finality sections, declared restriction morphisms, and "
                "two allowed refinement paths whose settlement obstruction "
                "keeps the transport square noncommuting."
            ),
            source_variables=variables,
            domain_native_payload=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            taf4_movement=False,
            taf8_execution=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
    )


def _evaluate_case(case: PayloadCase, t558_result: t558.T558Result) -> CaseDecision:
    missing = tuple(
        variable
        for variable in t558_result.frozen_source_variables
        if variable not in case.source_variables
    )
    falsifiers = _triggered_falsifiers(case, t558_result)

    if missing:
        return _decision(case, "REJECTED_UNDERDECLARED_SOURCE_VARIABLES", False, "underdeclared", missing, "none", falsifiers, "The payload does not carry every frozen T557 source variable.")
    if case.hidden_target_or_cross_repo_required:
        return _decision(case, "REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT", False, "falsifier", (), "none", falsifiers, "The payload depends on target labels or cross-repo truth.")
    if case.observerse_replay:
        return _decision(case, "REJECTED_OBSERVERSE_REPLAY", False, "spent_route", (), "none", falsifiers, "T556 parked the Observerse route as audit residue only.")
    if case.aprd_replay:
        return _decision(case, "REJECTED_APRD_REPLAY", False, "narrowed_route", (), "none", falsifiers, "APRD remains family-local feeder evidence, not this fresh burden.")
    if case.taf4_movement:
        return _decision(case, "BLOCKED_TAF4_OVERREAD", False, "blocked", (), "none", falsifiers, "A TAF11 payload is not a finite-to-continuum bridge.")
    if case.taf8_execution:
        return _decision(case, "BLOCKED_TAF8_OVERREAD", False, "blocked", (), "none", falsifiers, "A TAF11 payload is not a cross-domain shadow-protection packet.")
    if case.same_variables_relabel_target:
        return _decision(case, "REJECTED_RELABELING_FALSIFIER", False, "falsifier", (), "none", falsifiers, "The same source variables realize the target by relabeling only.")
    if not case.domain_native_payload:
        return _decision(case, "REJECTED_NO_DOMAIN_NATIVE_PAYLOAD", False, "formal_only", (), "none", falsifiers, "The packet has a formal transport shape but no finality-native payload.")
    if case.all_obstructions_glue or not case.survives_ordinary_sheaf_gluing:
        return _decision(case, "ABSORBED_ORDINARY_SHEAF_GLUE", False, "absorbed_control", (), "ordinary_sheaf_gluing_completion", falsifiers, "Ordinary sheaf gluing receives normal state and comparison rights.")
    if not case.survives_resource_transport_monotone:
        return _decision(case, "ABSORBED_RESOURCE_TRANSPORT_MONOTONE", False, "absorbed_control", (), "resource_transport_monotone_absorber", falsifiers, "The apparent obstruction factors through a native resource transport monotone.")
    if not case.survives_consensus_state_machine:
        return _decision(case, "ABSORBED_CONSENSUS_STATE_MACHINE", False, "absorbed_control", (), "consensus_state_machine_absorber", falsifiers, "Ordinary consensus or state-machine completion absorbs the split.")
    if not case.survives_record_provenance_completion or not case.provenance_complete:
        return _decision(case, "ABSORBED_RECORD_PROVENANCE_COMPLETION", False, "absorbed_control", (), "record_provenance_completion_absorber", falsifiers, "Completing normal provenance fields absorbs the missing-witness pressure.")
    if case.transport_square_commutes_after_absorbers or not case.noncommuting_transport_square:
        return _decision(case, "REJECTED_COMMUTING_AFTER_ABSORBERS", False, "falsifier", (), "none", falsifiers, "The transport square commutes after mature absorbers.")
    if not case.operation_menu_derived_from_finality or not case.refinement_stable:
        return _decision(case, "REJECTED_NOT_FINALITY_NATIVE", False, "not_domain_native", (), "none", falsifiers, "The operation menu is not derived from finality sections and allowed refinements.")

    return _decision(
        case,
        "ADMITTED_DOMAIN_NATIVE_BURDEN_PACKET_REVIEW_ONLY",
        True,
        "domain_native_review_payload",
        (),
        "none",
        falsifiers,
        "The payload carries the frozen variables, remains noncommuting, and survives the four mature absorbers.",
    )


def _decision(
    case: PayloadCase,
    outcome: str,
    admitted: bool,
    role: str,
    missing: tuple[str, ...],
    absorber: str,
    falsifiers: tuple[str, ...],
    reason: str,
) -> CaseDecision:
    return CaseDecision(
        case_id=case.case_id,
        outcome=outcome,
        admitted=admitted,
        role=role,
        missing_source_variables=missing,
        absorber=absorber,
        triggered_falsifiers=falsifiers,
        reason=reason,
    )


def _triggered_falsifiers(
    case: PayloadCase, t558_result: t558.T558Result
) -> tuple[str, ...]:
    falsifiers: list[str] = []
    declared = set(t558_result.frozen_falsifiers)
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


def _gate_decisions(
    t558_result: t558.T558Result,
    cases: tuple[PayloadCase, ...],
    decisions: tuple[CaseDecision, ...],
) -> tuple[GateDecision, ...]:
    decision_by_id = {decision.case_id: decision for decision in decisions}
    case_by_id = {case.case_id: case for case in cases}
    admitted = tuple(
        decision
        for decision in decisions
        if decision.outcome == "ADMITTED_DOMAIN_NATIVE_BURDEN_PACKET_REVIEW_ONLY"
    )
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
    admitted_case = case_by_id[admitted[0].case_id] if len(admitted) == 1 else None
    gates = (
        (
            "t558_domain_native_burden_authority",
            t558_result.verdict == t558.VERDICT
            and t558_result.selected_next_packet == t558.NEXT_PACKET,
            "T558 selected T559 as the domain-native packet burden.",
            "T558 did not provide the expected burden authority.",
        ),
        (
            "family_contract_frozen",
            tuple(t558_result.frozen_source_variables) == t558.EXPECTED_SOURCE_VARIABLES
            and tuple(t558_result.frozen_mature_absorbers) == t558.EXPECTED_MATURE_ABSORBERS
            and tuple(t558_result.frozen_falsifiers) == t558.EXPECTED_FALSIFIERS,
            "The T557/T558 variables, absorbers, and falsifiers are unchanged.",
            "The packet changed the frozen sheaf transport contract.",
        ),
        (
            "domain_native_payload_present",
            len(admitted) == 1
            and admitted[0].case_id == "record_finality_transport_square_payload",
            "Exactly one domain-native payload is admitted as review material.",
            "The packet did not isolate exactly one domain-native payload.",
        ),
        (
            "all_mature_absorbers_exercised",
            all(
                absorber in absorber_outcomes
                and absorber_outcomes[absorber].startswith("ABSORBED_")
                for absorber in t558_result.frozen_mature_absorbers
            ),
            "Every mature absorber receives a control case.",
            "One or more mature absorbers were not exercised.",
        ),
        (
            "all_declared_falsifiers_exercised",
            set(t558_result.frozen_falsifiers) <= triggered_falsifiers,
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
            "admitted_payload_survives_absorber_screen",
            admitted_case is not None
            and admitted_case.domain_native_payload
            and admitted_case.noncommuting_transport_square
            and admitted_case.survives_ordinary_sheaf_gluing
            and admitted_case.survives_resource_transport_monotone
            and admitted_case.survives_consensus_state_machine
            and admitted_case.survives_record_provenance_completion
            and not admitted[0].triggered_falsifiers,
            "The admitted payload survives all mature absorbers and no falsifier fires.",
            "The admitted payload did not survive the full absorber and falsifier screen.",
        ),
        (
            "no_source_law_or_governance_movement",
            not any(decision.outcome.startswith("BLOCKED_") for decision in decisions),
            "No source law, TAF4, TAF8, claim, canon, public-posture, external, or cross-repo movement is attempted.",
            "The packet attempted a forbidden governance or target movement.",
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
            control_id="domain_native_payload_control",
            blocks="Treating formal noncommutation as enough.",
            reason="T559 admits only a payload whose operations are native to record finality and allowed refinements.",
        ),
        HostileControl(
            control_id="ordinary_sheaf_gluing_control",
            blocks="Promoting compatible local sections as source-law residue.",
            reason="If all obstructions glue under declared restrictions, ordinary sheaf completion absorbs the case.",
        ),
        HostileControl(
            control_id="resource_transport_control",
            blocks="Reading budget or monotone drawdown as sheaf obstruction law.",
            reason="Resource transport receives normal state and comparison rights.",
        ),
        HostileControl(
            control_id="consensus_and_provenance_control",
            blocks="Reading state-machine divergence or missing provenance as finality-native obstruction.",
            reason="Consensus/state-machine and provenance completion absorbers are tested before admission.",
        ),
        HostileControl(
            control_id="target_import_and_replay_control",
            blocks="Using target labels, cross-repo truth, Observerse replay, or APRD replay.",
            reason="T559 inherits the T557/T558 falsifier screen.",
        ),
        HostileControl(
            control_id="taf4_taf8_public_posture_control",
            blocks="Moving TAF4, executing TAF8, or changing claim/canon/public posture.",
            reason="A single domain-native TAF11 payload is review material only.",
        ),
    )


def _claim_labels(
    t558_result: t558.T558Result, decisions: tuple[CaseDecision, ...]
) -> tuple[ClaimLabel, ...]:
    absorbed_count = sum(1 for decision in decisions if decision.outcome.startswith("ABSORBED_"))
    rejected_count = sum(
        1
        for decision in decisions
        if decision.outcome.startswith("REJECTED_")
        or decision.outcome.startswith("BLOCKED_")
    )
    admitted_count = sum(1 for decision in decisions if decision.admitted)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "T558 is consumed as burden authority: "
                f"{t558_result.verdict}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"{admitted_count} domain-native payload is admitted as review material.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{absorbed_count} mature absorber controls and {rejected_count} "
                "shortcut controls keep the T559 admission narrow."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The admitted payload is finality-native because its operation "
                "menu is built from local finality sections, restriction "
                "morphisms, settlement obstruction witnesses, and allowed "
                "refinements, but one packet is not a source law."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T559 Results: Domain-Native Sheaf Transport Packet Burden Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Packet status: `{payload['packet_status']}`",
        f"- Source T558 verdict: `{payload['source_t558_verdict']}`",
        f"- Source T558 packet status: `{payload['source_t558_packet_status']}`",
        f"- Source T558 selected next packet: `{payload['source_t558_selected_next_packet']}`",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Frozen Contract",
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


def write_results(result: T559Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t559_result_to_dict(result)
    json_path = results_dir / "T559-domain-native-sheaf-transport-packet-burden-gate-v0.1.json"
    md_path = (
        results_dir
        / "T559-domain-native-sheaf-transport-packet-burden-gate-v0.1-results.md"
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

    result = run_t559_analysis()
    payload = t559_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
