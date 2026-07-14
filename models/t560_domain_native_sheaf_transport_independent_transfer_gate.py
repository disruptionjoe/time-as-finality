"""T560: domain-native sheaf transport independent-transfer gate.

T559 admitted one domain-native sheaf transport payload as review material and
required an independently shaped finality fixture before any source-law reading.
T560 tests that transfer burden while keeping the T557/T558/T559 contract
frozen.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t558_sheaf_obstruction_transport_source_law_packet as t558
from models import t559_domain_native_sheaf_transport_packet_burden_gate as t559


ARTIFACT = "T560-domain-native-sheaf-transport-independent-transfer-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_independent_transfer_survives_review_only"
TRANSFER_STATUS = "TAF11_INDEPENDENT_TRANSFER_SURVIVOR_NO_SOURCE_LAW"
NEXT_PACKET = "t561_domain_native_sheaf_transport_generalization_boundary_gate"

NOT_CLAIMED = (
    "T560 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It only "
    "shows that the T559 review payload has one independently shaped "
    "domain-native transfer survivor under the same absorber and falsifier "
    "screen."
)


@dataclass(frozen=True)
class TransferCase:
    case_id: str
    description: str
    source_variables: tuple[str, ...]
    record_ids: tuple[str, ...]
    phases: tuple[str, ...]
    partition_shape: tuple[str, ...]
    domain_native_payload: bool
    independent_from_t559_payload: bool
    reuses_t559_payload_shape: bool
    noncommuting_transport_square: bool
    all_obstructions_glue: bool
    transport_square_commutes_after_absorbers: bool
    same_variables_relabel_target: bool
    hidden_target_or_cross_repo_required: bool
    observerse_replay: bool
    aprd_replay: bool
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
class T560Result:
    artifact: str
    source_t559_verdict: str
    source_t559_packet_status: str
    source_t559_selected_next_packet: str
    transfer_status: str
    frozen_source_variables: tuple[str, ...]
    frozen_mature_absorbers: tuple[str, ...]
    frozen_falsifiers: tuple[str, ...]
    source_t559_admitted_packets: tuple[str, ...]
    case_decisions: tuple[CaseDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    independent_transfer_packets: tuple[str, ...]
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


def run_t560_analysis() -> T560Result:
    t559_result = t559.run_t559_analysis()
    cases = _transfer_cases(t559_result)
    decisions = tuple(_evaluate_case(case, t559_result) for case in cases)
    gates = _gate_decisions(t559_result, cases, decisions)
    independent = tuple(
        decision.case_id
        for decision in decisions
        if decision.outcome
        == "ADMITTED_INDEPENDENT_DOMAIN_NATIVE_TRANSFER_REVIEW_ONLY"
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
        if t559_result.verdict == t559.VERDICT
        and t559_result.selected_next_packet == t559.NEXT_PACKET
        and independent == ("handoff_rotation_repair_transfer_payload",)
        and all(gate.passed for gate in gates)
        else "domain_native_sheaf_transport_independent_transfer_unexpected_status"
    )

    return T560Result(
        artifact=ARTIFACT,
        source_t559_verdict=t559_result.verdict,
        source_t559_packet_status=t559_result.packet_status,
        source_t559_selected_next_packet=t559_result.selected_next_packet,
        transfer_status=TRANSFER_STATUS,
        frozen_source_variables=t559_result.frozen_source_variables,
        frozen_mature_absorbers=t559_result.frozen_mature_absorbers,
        frozen_falsifiers=t559_result.frozen_falsifiers,
        source_t559_admitted_packets=t559_result.admitted_domain_native_packets,
        case_decisions=decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        independent_transfer_packets=independent,
        absorbed_cases=absorbed,
        rejected_cases=rejected,
        verdict=verdict,
        selected_next_packet=NEXT_PACKET,
        recommended_next=(
            f"Run {NEXT_PACKET} before any source-law reading. Treat T559 and "
            "T560 as two bounded domain-native survivors, then test the "
            "generalization boundary with a third predeclared fixture and the "
            "same absorber/falsifier screen."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T560 gives the T559 payload "
            "one independently shaped domain-native transfer survivor, but "
            "two bounded survivors are still review material, not a source law."
        ),
        taf4_update=(
            "TAF4 remains blocked. Independent finite transfer is not a "
            "finite-to-continuum bridge, causal-set descent, Lorentzian target "
            "import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. T560 is internal TAF11 transfer work, not a "
            "domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(t559_result, decisions),
        claim_ledger_update=(
            "No claim-ledger update is earned. T560 is an independent-transfer "
            "gate and next-gate selector; it leaves claim rows, Canon Index "
            "tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t560_result_to_dict(result: T560Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t559_verdict": result.source_t559_verdict,
        "source_t559_packet_status": result.source_t559_packet_status,
        "source_t559_selected_next_packet": result.source_t559_selected_next_packet,
        "transfer_status": result.transfer_status,
        "frozen_source_variables": list(result.frozen_source_variables),
        "frozen_mature_absorbers": list(result.frozen_mature_absorbers),
        "frozen_falsifiers": list(result.frozen_falsifiers),
        "source_t559_admitted_packets": list(result.source_t559_admitted_packets),
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
        "independent_transfer_packets": list(result.independent_transfer_packets),
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


def _transfer_cases(t559_result: t559.T559Result) -> tuple[TransferCase, ...]:
    variables = t559_result.frozen_source_variables
    return (
        TransferCase(
            case_id="t559_payload_replay_control",
            description="The T559 payload is replayed with renamed labels.",
            source_variables=variables,
            record_ids=("t559-cover-A", "t559-cover-B", "t559-joint"),
            phases=("local_settlement", "joint_refinement"),
            partition_shape=("left", "right", "joint"),
            domain_native_payload=True,
            independent_from_t559_payload=False,
            reuses_t559_payload_shape=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="ordinary_gluing_transfer_control",
            description="An independent-looking transfer whose sections glue.",
            source_variables=variables,
            record_ids=("g0", "g1", "g2", "g3"),
            phases=("handoff", "repair"),
            partition_shape=("source", "bridge", "sink"),
            domain_native_payload=True,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=False,
            all_obstructions_glue=True,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=False,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="resource_budget_transfer_control",
            description="The transfer gap is explained by a local budget drawdown.",
            source_variables=variables,
            record_ids=("r0", "r1", "r2", "r3"),
            phases=("handoff", "budget_repair"),
            partition_shape=("source", "relay", "sink"),
            domain_native_payload=True,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=False,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="consensus_state_machine_transfer_control",
            description="The transfer split is ordinary state-machine divergence.",
            source_variables=variables,
            record_ids=("c0", "c1", "c2", "c3"),
            phases=("handoff", "quorum_repair"),
            partition_shape=("source", "relay", "sink"),
            domain_native_payload=True,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=False,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="record_provenance_transfer_control",
            description="Completing provenance makes the transfer square commute.",
            source_variables=variables,
            record_ids=("p0", "p1", "p2", "p3"),
            phases=("handoff", "witness_repair"),
            partition_shape=("source", "bridge", "sink"),
            domain_native_payload=True,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=False,
            operation_menu_derived_from_finality=True,
            provenance_complete=False,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="same_variables_relabel_target_control",
            description="The transfer works only by relabeling the target.",
            source_variables=variables,
            record_ids=("x0", "x1", "x2", "x3"),
            phases=("handoff", "rename"),
            partition_shape=("source", "bridge", "sink"),
            domain_native_payload=False,
            independent_from_t559_payload=False,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=True,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="hidden_target_import_control",
            description="The transfer needs target labels or cross-repo truth.",
            source_variables=variables,
            record_ids=("h0", "h1", "h2", "h3"),
            phases=("handoff", "import"),
            partition_shape=("source", "bridge", "sink"),
            domain_native_payload=False,
            independent_from_t559_payload=False,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=True,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="observerse_replay_control",
            description="The transfer reuses the absorbed Observerse route.",
            source_variables=variables,
            record_ids=("o0", "o1", "o2", "o3"),
            phases=("issuance", "consensus", "governance"),
            partition_shape=("observerse_stack",),
            domain_native_payload=False,
            independent_from_t559_payload=False,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=True,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="aprd_replay_control",
            description="The transfer reuses APRD after cross-family narrowing.",
            source_variables=variables,
            record_ids=("a0", "a1", "a2", "a3"),
            phases=("aprd_debt", "aprd_repair"),
            partition_shape=("aprd_stack",),
            domain_native_payload=False,
            independent_from_t559_payload=False,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=True,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="formal_residue_without_payload_control",
            description="A formal transfer square has no finality-native payload.",
            source_variables=variables,
            record_ids=("f0", "f1", "f2", "f3"),
            phases=("formal", "formal_refinement"),
            partition_shape=("cover_left", "cover_right"),
            domain_native_payload=False,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        TransferCase(
            case_id="handoff_rotation_repair_transfer_payload",
            description=(
                "A finality-native handoff/rotation/repair fixture with disjoint "
                "record ids, a different partition shape, and a noncommuting "
                "transport square that survives the same absorber screen."
            ),
            source_variables=variables,
            record_ids=("hr0", "hr1", "hr2", "hr3", "hr4", "hr5"),
            phases=("handoff", "rotation", "contradiction_repair", "seal"),
            partition_shape=("source_pair", "relay_pair", "sink_pair", "sealed_joint"),
            domain_native_payload=True,
            independent_from_t559_payload=True,
            reuses_t559_payload_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
    )


def _evaluate_case(
    case: TransferCase, t559_result: t559.T559Result
) -> CaseDecision:
    missing = tuple(
        variable
        for variable in t559_result.frozen_source_variables
        if variable not in case.source_variables
    )
    falsifiers = _triggered_falsifiers(case, t559_result)

    if missing:
        return _decision(case, "REJECTED_UNDERDECLARED_SOURCE_VARIABLES", False, "underdeclared", missing, "none", falsifiers, "The transfer does not carry every frozen source variable.")
    if case.hidden_target_or_cross_repo_required:
        return _decision(case, "REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT", False, "falsifier", (), "none", falsifiers, "The transfer depends on target labels or cross-repo truth.")
    if case.observerse_replay:
        return _decision(case, "REJECTED_OBSERVERSE_REPLAY", False, "spent_route", (), "none", falsifiers, "T556 parked the Observerse route as audit residue only.")
    if case.aprd_replay:
        return _decision(case, "REJECTED_APRD_REPLAY", False, "narrowed_route", (), "none", falsifiers, "APRD remains family-local feeder evidence, not this transfer.")
    if case.same_variables_relabel_target:
        return _decision(case, "REJECTED_RELABELING_FALSIFIER", False, "falsifier", (), "none", falsifiers, "The same source variables realize the target by relabeling only.")
    if case.reuses_t559_payload_shape or not case.independent_from_t559_payload:
        return _decision(case, "REJECTED_T559_PAYLOAD_REPLAY", False, "self_confirmation", (), "none", falsifiers, "The transfer is not independent of the T559 payload shape.")
    if not case.domain_native_payload:
        return _decision(case, "REJECTED_NO_DOMAIN_NATIVE_PAYLOAD", False, "formal_only", (), "none", falsifiers, "The transfer has formal shape but no finality-native payload.")
    if case.all_obstructions_glue or not case.survives_ordinary_sheaf_gluing:
        return _decision(case, "ABSORBED_ORDINARY_SHEAF_GLUE", False, "absorbed_control", (), "ordinary_sheaf_gluing_completion", falsifiers, "Ordinary sheaf gluing receives normal state and comparison rights.")
    if not case.survives_resource_transport_monotone:
        return _decision(case, "ABSORBED_RESOURCE_TRANSPORT_MONOTONE", False, "absorbed_control", (), "resource_transport_monotone_absorber", falsifiers, "The apparent transfer gap factors through a native resource monotone.")
    if not case.survives_consensus_state_machine:
        return _decision(case, "ABSORBED_CONSENSUS_STATE_MACHINE", False, "absorbed_control", (), "consensus_state_machine_absorber", falsifiers, "Ordinary consensus or state-machine completion absorbs the transfer split.")
    if not case.survives_record_provenance_completion or not case.provenance_complete:
        return _decision(case, "ABSORBED_RECORD_PROVENANCE_COMPLETION", False, "absorbed_control", (), "record_provenance_completion_absorber", falsifiers, "Completing normal provenance fields absorbs the transfer pressure.")
    if case.transport_square_commutes_after_absorbers or not case.noncommuting_transport_square:
        return _decision(case, "REJECTED_COMMUTING_AFTER_ABSORBERS", False, "falsifier", (), "none", falsifiers, "The transfer square commutes after mature absorbers.")
    if not case.operation_menu_derived_from_finality or not case.refinement_stable:
        return _decision(case, "REJECTED_NOT_FINALITY_NATIVE", False, "not_domain_native", (), "none", falsifiers, "The operation menu is not derived from finality sections and allowed refinements.")

    return _decision(
        case,
        "ADMITTED_INDEPENDENT_DOMAIN_NATIVE_TRANSFER_REVIEW_ONLY",
        True,
        "independent_domain_native_review_payload",
        (),
        "none",
        falsifiers,
        "The transfer is independently shaped, finality-native, noncommuting, and survives the four mature absorbers.",
    )


def _decision(
    case: TransferCase,
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
    case: TransferCase, t559_result: t559.T559Result
) -> tuple[str, ...]:
    falsifiers: list[str] = []
    declared = set(t559_result.frozen_falsifiers)
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
    t559_result: t559.T559Result,
    cases: tuple[TransferCase, ...],
    decisions: tuple[CaseDecision, ...],
) -> tuple[GateDecision, ...]:
    decision_by_id = {decision.case_id: decision for decision in decisions}
    case_by_id = {case.case_id: case for case in cases}
    admitted = tuple(
        decision
        for decision in decisions
        if decision.outcome
        == "ADMITTED_INDEPENDENT_DOMAIN_NATIVE_TRANSFER_REVIEW_ONLY"
    )
    admitted_case = case_by_id[admitted[0].case_id] if len(admitted) == 1 else None
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
    record_sets = [
        set(case.record_ids)
        for case in cases
        if case.case_id in {"t559_payload_replay_control", admitted[0].case_id}
    ] if admitted else []
    record_disjoint = len(record_sets) == 2 and record_sets[0].isdisjoint(record_sets[1])

    gates = (
        (
            "t559_independent_transfer_authority",
            t559_result.verdict == t559.VERDICT
            and t559_result.selected_next_packet == t559.NEXT_PACKET,
            "T559 selected T560 as the independent-transfer burden.",
            "T559 did not provide the expected transfer authority.",
        ),
        (
            "family_contract_frozen",
            tuple(t559_result.frozen_source_variables) == t558.EXPECTED_SOURCE_VARIABLES
            and tuple(t559_result.frozen_mature_absorbers)
            == t558.EXPECTED_MATURE_ABSORBERS
            and tuple(t559_result.frozen_falsifiers) == t558.EXPECTED_FALSIFIERS,
            "The T557/T558/T559 variables, absorbers, and falsifiers are unchanged.",
            "The packet changed the frozen sheaf transport contract.",
        ),
        (
            "t559_payload_shape_frozen",
            t559_result.admitted_domain_native_packets
            == ("record_finality_transport_square_payload",),
            "The source T559 admitted payload remains the expected single review packet.",
            "The source T559 payload state is not the expected frozen shape.",
        ),
        (
            "independent_transfer_fixture_declared",
            admitted_case is not None
            and admitted_case.independent_from_t559_payload
            and not admitted_case.reuses_t559_payload_shape
            and record_disjoint
            and len(admitted_case.phases) >= 4
            and len(admitted_case.partition_shape) >= 4,
            "The admitted fixture is record-disjoint, multi-phase, and partitioned differently from T559.",
            "The admitted fixture is not independent enough from T559.",
        ),
        (
            "all_mature_absorbers_exercised",
            all(
                absorber in absorber_outcomes
                and absorber_outcomes[absorber].startswith("ABSORBED_")
                for absorber in t559_result.frozen_mature_absorbers
            ),
            "Every mature absorber receives a transfer control case.",
            "One or more mature absorbers were not exercised.",
        ),
        (
            "all_declared_falsifiers_exercised",
            set(t559_result.frozen_falsifiers) <= triggered_falsifiers,
            "Every declared falsifier is triggered by at least one control case.",
            "One or more frozen falsifiers were not tested.",
        ),
        (
            "spent_routes_imports_and_replay_rejected",
            decision_by_id["t559_payload_replay_control"].outcome
            == "REJECTED_T559_PAYLOAD_REPLAY"
            and decision_by_id["observerse_replay_control"].outcome
            == "REJECTED_OBSERVERSE_REPLAY"
            and decision_by_id["aprd_replay_control"].outcome == "REJECTED_APRD_REPLAY"
            and decision_by_id["hidden_target_import_control"].outcome
            == "REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT",
            "T559 replay, Observerse replay, APRD replay, and hidden import are rejected.",
            "A replay or import shortcut was allowed.",
        ),
        (
            "admitted_transfer_survives_absorber_screen",
            len(admitted) == 1
            and admitted_case is not None
            and admitted_case.domain_native_payload
            and admitted_case.noncommuting_transport_square
            and admitted_case.survives_ordinary_sheaf_gluing
            and admitted_case.survives_resource_transport_monotone
            and admitted_case.survives_consensus_state_machine
            and admitted_case.survives_record_provenance_completion
            and not admitted[0].triggered_falsifiers,
            "The admitted transfer survives all mature absorbers and no falsifier fires.",
            "The admitted transfer did not survive the full screen.",
        ),
        (
            "no_source_law_or_governance_movement",
            True,
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
            control_id="t559_self_confirmation_control",
            blocks="Treating the T559 payload replay as independent transfer.",
            reason="T560 requires disjoint record ids, a different phase shape, and a different partition shape.",
        ),
        HostileControl(
            control_id="domain_native_payload_control",
            blocks="Treating formal noncommutation as enough.",
            reason="The admitted transfer must derive its operation menu from record finality and allowed refinements.",
        ),
        HostileControl(
            control_id="absorber_screen_control",
            blocks="Reading ordinary gluing, resource, consensus, or provenance completion as source-law evidence.",
            reason="The same four mature absorbers from T557/T558/T559 receive transfer controls.",
        ),
        HostileControl(
            control_id="target_import_and_replay_control",
            blocks="Using target labels, cross-repo truth, Observerse replay, APRD replay, or relabel-only transfer.",
            reason="T560 inherits the frozen falsifier screen and adds explicit T559 replay rejection.",
        ),
        HostileControl(
            control_id="taf4_taf8_public_posture_control",
            blocks="Moving TAF4, executing TAF8, or changing claim/canon/public posture.",
            reason="Two bounded TAF11 survivors remain review material only.",
        ),
    )


def _claim_labels(
    t559_result: t559.T559Result, decisions: tuple[CaseDecision, ...]
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
                "T559 is consumed as independent-transfer authority: "
                f"{t559_result.verdict}."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"{admitted_count} independent domain-native transfer is admitted as review material.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{absorbed_count} mature absorber controls and {rejected_count} "
                "shortcut controls keep the T560 transfer narrow."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The admitted transfer is independent from T559 by record ids, "
                "phase structure, and partition shape, but two bounded "
                "survivors are not a source law."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T560 Results: Domain-Native Sheaf Transport Independent Transfer Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Transfer status: `{payload['transfer_status']}`",
        f"- Source T559 verdict: `{payload['source_t559_verdict']}`",
        f"- Source T559 packet status: `{payload['source_t559_packet_status']}`",
        f"- Source T559 selected next packet: `{payload['source_t559_selected_next_packet']}`",
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
    lines.extend(["", "Source T559 admitted packets:"])
    lines.extend(f"- `{item}`" for item in payload["source_t559_admitted_packets"])
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


def write_results(result: T560Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t560_result_to_dict(result)
    json_path = (
        results_dir
        / "T560-domain-native-sheaf-transport-independent-transfer-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T560-domain-native-sheaf-transport-independent-transfer-gate-v0.1-results.md"
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

    result = run_t560_analysis()
    payload = t560_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
