"""T561: domain-native sheaf transport generalization-boundary gate.

T559 and T560 are two bounded domain-native survivors under the frozen
sheaf-obstruction transport contract. T561 maps the current generalization
boundary with one third predeclared fixture before any source-law reading.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t558_sheaf_obstruction_transport_source_law_packet as t558
from models import t559_domain_native_sheaf_transport_packet_burden_gate as t559
from models import t560_domain_native_sheaf_transport_independent_transfer_gate as t560


ARTIFACT = "T561-domain-native-sheaf-transport-generalization-boundary-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_generalization_boundary_mapped_review_only"
GENERALIZATION_STATUS = "TAF11_GENERALIZATION_BOUNDARY_MAPPED_NO_SOURCE_LAW"
NEXT_PACKET = "t562_domain_native_sheaf_transport_minimality_gate"

NOT_CLAIMED = (
    "T561 does not establish a source law, validate sheaf obstruction "
    "transport as a source family, prove shadow protection, derive spacetime, "
    "prove manifoldlikeness, repair T528, reverse T223, unpause S1, promote "
    "S1, change claim status, change Canon Index tiers, change canon verdicts, "
    "change public posture, change the North Star, authorize external "
    "publication, move TAF4, execute TAF8, or move cross-repo truth. It maps "
    "the bounded generalization boundary for the current TAF11 sheaf transport "
    "route only."
)


@dataclass(frozen=True)
class BoundaryCase:
    case_id: str
    description: str
    expected_status: str
    source_variables: tuple[str, ...]
    record_ids: tuple[str, ...]
    phases: tuple[str, ...]
    partition_shape: tuple[str, ...]
    prior_survivor: bool
    domain_native_payload: bool
    bounded_fixture: bool
    target_blind: bool
    independent_from_prior_survivors: bool
    reuses_t559_payload_shape: bool
    reuses_t560_transfer_shape: bool
    noncommuting_transport_square: bool
    all_obstructions_glue: bool
    transport_square_commutes_after_absorbers: bool
    same_variables_relabel_target: bool
    hidden_target_or_cross_repo_required: bool
    observerse_replay: bool
    aprd_replay: bool
    cross_domain_packet: bool
    imports_lorentzian_target: bool
    asserts_source_law: bool
    moves_taf4: bool
    executes_taf8: bool
    survives_ordinary_sheaf_gluing: bool
    survives_resource_transport_monotone: bool
    survives_consensus_state_machine: bool
    survives_record_provenance_completion: bool
    operation_menu_derived_from_finality: bool
    provenance_complete: bool
    refinement_stable: bool


@dataclass(frozen=True)
class BoundaryOutcome:
    case_id: str
    expected_status: str
    actual_status: str
    matched: bool
    in_generalization_class: bool
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
class T561Result:
    artifact: str
    source_t559_verdict: str
    source_t560_verdict: str
    source_t560_selected_next_packet: str
    generalization_status: str
    frozen_source_variables: tuple[str, ...]
    frozen_mature_absorbers: tuple[str, ...]
    frozen_falsifiers: tuple[str, ...]
    source_t559_admitted_packets: tuple[str, ...]
    source_t560_independent_transfer_packets: tuple[str, ...]
    boundary_outcomes: tuple[BoundaryOutcome, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    bounded_survivor_class: tuple[str, ...]
    selected_next_packet: str
    verdict: str
    source_law_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t561_analysis() -> T561Result:
    t559_result = t559.run_t559_analysis()
    t560_result = t560.run_t560_analysis()
    cases = _boundary_cases(t559_result, t560_result)
    outcomes = tuple(_evaluate_case(case, t560_result) for case in cases)
    gates = _gate_decisions(t559_result, t560_result, cases, outcomes)
    bounded_class = tuple(
        outcome.case_id for outcome in outcomes if outcome.in_generalization_class
    )
    selected_next_packet = NEXT_PACKET if all(gate.passed for gate in gates) else "none"
    verdict = (
        VERDICT
        if t559_result.verdict == t559.VERDICT
        and t560_result.verdict == t560.VERDICT
        and t560_result.selected_next_packet == t560.NEXT_PACKET
        and bounded_class
        == (
            "t559_record_finality_transport_square_survivor",
            "t560_handoff_rotation_repair_transfer_survivor",
            "third_multicover_seal_handoff_fixture",
        )
        and all(outcome.matched for outcome in outcomes)
        and selected_next_packet == NEXT_PACKET
        else "domain_native_sheaf_transport_generalization_boundary_unexpected_status"
    )

    return T561Result(
        artifact=ARTIFACT,
        source_t559_verdict=t559_result.verdict,
        source_t560_verdict=t560_result.verdict,
        source_t560_selected_next_packet=t560_result.selected_next_packet,
        generalization_status=GENERALIZATION_STATUS,
        frozen_source_variables=t560_result.frozen_source_variables,
        frozen_mature_absorbers=t560_result.frozen_mature_absorbers,
        frozen_falsifiers=t560_result.frozen_falsifiers,
        source_t559_admitted_packets=t559_result.admitted_domain_native_packets,
        source_t560_independent_transfer_packets=t560_result.independent_transfer_packets,
        boundary_outcomes=outcomes,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        bounded_survivor_class=bounded_class,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "The route now has a mapped bounded class with three "
            "domain-native fixture shapes and explicit rejection boundaries. "
            "That is stronger route control, not source-law status."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. It should test whether every frozen source "
            "variable and boundary condition is minimal across the admitted "
            "bounded class before any source-law, TAF4, TAF8, claim-ledger, or "
            "public-posture movement."
        ),
        taf11_update=(
            "TAF11 remains active and narrowed. T561 maps the current sheaf "
            "transport generalization class as bounded, domain-native, "
            "target-blind, noncommuting, provenance-complete fixtures under "
            "the frozen absorber and falsifier screen."
        ),
        taf4_update=(
            "TAF4 remains blocked. A bounded finite generalization boundary is "
            "not a finite-to-continuum bridge, causal-set descent, Lorentzian "
            "target import, or manifoldlikeness result."
        ),
        taf8_update=(
            "TAF8 remains waiting. T561 is internal TAF11 boundary mapping, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(outcomes),
        claim_ledger_update=(
            "No claim-ledger update is earned. T561 is a boundary map and "
            "next-minimality-gate selector; it leaves claim rows, Canon Index "
            "tiers, canon verdicts, and public posture unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t561_result_to_dict(result: T561Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t559_verdict": result.source_t559_verdict,
        "source_t560_verdict": result.source_t560_verdict,
        "source_t560_selected_next_packet": result.source_t560_selected_next_packet,
        "generalization_status": result.generalization_status,
        "frozen_source_variables": list(result.frozen_source_variables),
        "frozen_mature_absorbers": list(result.frozen_mature_absorbers),
        "frozen_falsifiers": list(result.frozen_falsifiers),
        "source_t559_admitted_packets": list(result.source_t559_admitted_packets),
        "source_t560_independent_transfer_packets": list(
            result.source_t560_independent_transfer_packets
        ),
        "boundary_outcomes": [
            {
                "case_id": outcome.case_id,
                "expected_status": outcome.expected_status,
                "actual_status": outcome.actual_status,
                "matched": outcome.matched,
                "in_generalization_class": outcome.in_generalization_class,
                "absorber": outcome.absorber,
                "triggered_falsifiers": list(outcome.triggered_falsifiers),
                "reason": outcome.reason,
            }
            for outcome in result.boundary_outcomes
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
        "bounded_survivor_class": list(result.bounded_survivor_class),
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
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


def _boundary_cases(
    t559_result: t559.T559Result,
    t560_result: t560.T560Result,
) -> tuple[BoundaryCase, ...]:
    variables = t560_result.frozen_source_variables
    return (
        BoundaryCase(
            case_id="t559_record_finality_transport_square_survivor",
            description="The original T559 domain-native transport-square survivor.",
            expected_status="inside_bounded_domain_native_class",
            source_variables=variables,
            record_ids=("t559-cover-A", "t559-cover-B", "t559-joint"),
            phases=("local_settlement", "joint_refinement"),
            partition_shape=("left", "right", "joint"),
            prior_survivor=True,
            domain_native_payload=t559_result.admitted_domain_native_packets
            == ("record_finality_transport_square_payload",),
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=False,
            reuses_t559_payload_shape=True,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="t560_handoff_rotation_repair_transfer_survivor",
            description="The T560 independent handoff/rotation/repair survivor.",
            expected_status="inside_bounded_domain_native_class",
            source_variables=variables,
            record_ids=("hr0", "hr1", "hr2", "hr3", "hr4", "hr5"),
            phases=("handoff", "rotation", "contradiction_repair", "seal"),
            partition_shape=("source_pair", "relay_pair", "sink_pair", "sealed_joint"),
            prior_survivor=True,
            domain_native_payload=t560_result.independent_transfer_packets
            == ("handoff_rotation_repair_transfer_payload",),
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=False,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="third_multicover_seal_handoff_fixture",
            description=(
                "A third bounded finality-native fixture with a three-cover "
                "handoff, delayed seal, and disjoint record ids."
            ),
            expected_status="inside_bounded_domain_native_class",
            source_variables=variables,
            record_ids=("mc0", "mc1", "mc2", "mc3", "mc4", "mc5", "mc6"),
            phases=("tri_cover_handoff", "witness_exchange", "seal_delay", "joint_lock"),
            partition_shape=("cover_alpha", "cover_beta", "cover_gamma", "delayed_joint"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="t559_payload_replay_as_new_fixture",
            description="The T559 payload is replayed as if it were a new boundary member.",
            expected_status="rejected_t559_payload_replay",
            source_variables=variables,
            record_ids=("t559-replay-A", "t559-replay-B", "t559-replay-joint"),
            phases=("local_settlement", "joint_refinement"),
            partition_shape=("left", "right", "joint"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=False,
            reuses_t559_payload_shape=True,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="t560_transfer_replay_as_new_fixture",
            description="The T560 transfer shape is replayed as if it were a third fixture.",
            expected_status="rejected_t560_transfer_replay",
            source_variables=variables,
            record_ids=("hr-replay-0", "hr-replay-1", "hr-replay-2", "hr-replay-3"),
            phases=("handoff", "rotation", "contradiction_repair", "seal"),
            partition_shape=("source_pair", "relay_pair", "sink_pair", "sealed_joint"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=False,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=True,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="ordinary_gluing_boundary_control",
            description="A candidate boundary where the local sections glue normally.",
            expected_status="absorbed_ordinary_sheaf_glue",
            source_variables=variables,
            record_ids=("g0", "g1", "g2", "g3"),
            phases=("handoff", "glue"),
            partition_shape=("source", "bridge", "sink"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=False,
            all_obstructions_glue=True,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=False,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="resource_budget_boundary_control",
            description="The boundary gap factors through a normal resource monotone.",
            expected_status="absorbed_resource_transport_monotone",
            source_variables=variables,
            record_ids=("r0", "r1", "r2", "r3"),
            phases=("handoff", "budget_repair"),
            partition_shape=("source", "relay", "sink"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=False,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="consensus_state_machine_boundary_control",
            description="The boundary split is ordinary consensus/state-machine divergence.",
            expected_status="absorbed_consensus_state_machine",
            source_variables=variables,
            record_ids=("c0", "c1", "c2", "c3"),
            phases=("handoff", "quorum_repair"),
            partition_shape=("source", "relay", "sink"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=False,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="record_provenance_boundary_control",
            description="Completing provenance makes the boundary commute.",
            expected_status="absorbed_record_provenance_completion",
            source_variables=variables,
            record_ids=("p0", "p1", "p2", "p3"),
            phases=("handoff", "witness_repair"),
            partition_shape=("source", "bridge", "sink"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=True,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=False,
            operation_menu_derived_from_finality=True,
            provenance_complete=False,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="same_variables_relabel_target_boundary",
            description="The same variables realize the boundary only by relabeling.",
            expected_status="rejected_relabeling_falsifier",
            source_variables=variables,
            record_ids=("x0", "x1", "x2", "x3"),
            phases=("handoff", "rename"),
            partition_shape=("source", "bridge", "sink"),
            prior_survivor=False,
            domain_native_payload=False,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=True,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="hidden_target_import_boundary",
            description="The boundary requires target labels or cross-repo truth.",
            expected_status="rejected_hidden_target_or_cross_repo_import",
            source_variables=variables,
            record_ids=("h0", "h1", "h2", "h3"),
            phases=("handoff", "import"),
            partition_shape=("source", "bridge", "sink"),
            prior_survivor=False,
            domain_native_payload=False,
            bounded_fixture=True,
            target_blind=False,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=True,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="observerse_replay_boundary",
            description="The absorbed Observerse route is replayed.",
            expected_status="rejected_observerse_replay",
            source_variables=variables,
            record_ids=("o0", "o1", "o2", "o3"),
            phases=("issuance", "consensus", "governance"),
            partition_shape=("observerse_stack",),
            prior_survivor=False,
            domain_native_payload=False,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=True,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="aprd_replay_boundary",
            description="The narrowed APRD route is replayed.",
            expected_status="rejected_aprd_replay",
            source_variables=variables,
            record_ids=("a0", "a1", "a2", "a3"),
            phases=("aprd_debt", "aprd_repair"),
            partition_shape=("aprd_stack",),
            prior_survivor=False,
            domain_native_payload=False,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=True,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="taf8_cross_domain_boundary",
            description="A cross-domain shadow-protection packet is imported into TAF11.",
            expected_status="out_of_scope_taf8_cross_domain",
            source_variables=variables,
            record_ids=("d0", "d1", "d2", "d3"),
            phases=("domain_a", "domain_b"),
            partition_shape=("cross_domain",),
            prior_survivor=False,
            domain_native_payload=False,
            bounded_fixture=False,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=True,
            imports_lorentzian_target=False,
            asserts_source_law=False,
            moves_taf4=False,
            executes_taf8=True,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=False,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="taf4_lorentzian_target_import_boundary",
            description="A Lorentzian or causal-set target is imported as success.",
            expected_status="blocked_taf4_target_import",
            source_variables=variables,
            record_ids=("l0", "l1", "l2", "l3"),
            phases=("handoff", "target_fit"),
            partition_shape=("source", "target"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=False,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=True,
            asserts_source_law=False,
            moves_taf4=True,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
        BoundaryCase(
            case_id="source_law_overread_boundary",
            description="Three bounded survivors are asserted as source-law proof.",
            expected_status="blocked_source_law_overread",
            source_variables=variables,
            record_ids=("s0", "s1", "s2", "s3"),
            phases=("handoff", "seal"),
            partition_shape=("source", "bridge", "sink"),
            prior_survivor=False,
            domain_native_payload=True,
            bounded_fixture=True,
            target_blind=True,
            independent_from_prior_survivors=True,
            reuses_t559_payload_shape=False,
            reuses_t560_transfer_shape=False,
            noncommuting_transport_square=True,
            all_obstructions_glue=False,
            transport_square_commutes_after_absorbers=False,
            same_variables_relabel_target=False,
            hidden_target_or_cross_repo_required=False,
            observerse_replay=False,
            aprd_replay=False,
            cross_domain_packet=False,
            imports_lorentzian_target=False,
            asserts_source_law=True,
            moves_taf4=False,
            executes_taf8=False,
            survives_ordinary_sheaf_gluing=True,
            survives_resource_transport_monotone=True,
            survives_consensus_state_machine=True,
            survives_record_provenance_completion=True,
            operation_menu_derived_from_finality=True,
            provenance_complete=True,
            refinement_stable=True,
        ),
    )


def _evaluate_case(case: BoundaryCase, t560_result: t560.T560Result) -> BoundaryOutcome:
    actual_status, absorber = _classify_case(case, t560_result)
    in_generalization_class = actual_status == "inside_bounded_domain_native_class"
    falsifiers = _triggered_falsifiers(case, t560_result)
    return BoundaryOutcome(
        case_id=case.case_id,
        expected_status=case.expected_status,
        actual_status=actual_status,
        matched=actual_status == case.expected_status,
        in_generalization_class=in_generalization_class,
        absorber=absorber,
        triggered_falsifiers=falsifiers,
        reason=_case_reason(actual_status),
    )


def _classify_case(
    case: BoundaryCase,
    t560_result: t560.T560Result,
) -> tuple[str, str]:
    missing = tuple(
        variable
        for variable in t560_result.frozen_source_variables
        if variable not in case.source_variables
    )
    if missing:
        return "rejected_underdeclared_source_variables", "none"
    if case.asserts_source_law:
        return "blocked_source_law_overread", "none"
    if case.cross_domain_packet or case.executes_taf8:
        return "out_of_scope_taf8_cross_domain", "none"
    if case.imports_lorentzian_target or case.moves_taf4:
        return "blocked_taf4_target_import", "none"
    if case.hidden_target_or_cross_repo_required:
        return "rejected_hidden_target_or_cross_repo_import", "none"
    if case.observerse_replay:
        return "rejected_observerse_replay", "none"
    if case.aprd_replay:
        return "rejected_aprd_replay", "none"
    if case.same_variables_relabel_target:
        return "rejected_relabeling_falsifier", "none"
    if case.reuses_t559_payload_shape and not case.prior_survivor:
        return "rejected_t559_payload_replay", "none"
    if case.reuses_t560_transfer_shape and not case.prior_survivor:
        return "rejected_t560_transfer_replay", "none"
    if not case.domain_native_payload:
        return "rejected_no_domain_native_payload", "none"
    if not case.target_blind:
        return "blocked_taf4_target_import", "none"
    if case.all_obstructions_glue or not case.survives_ordinary_sheaf_gluing:
        return "absorbed_ordinary_sheaf_glue", "ordinary_sheaf_gluing_completion"
    if not case.survives_resource_transport_monotone:
        return "absorbed_resource_transport_monotone", "resource_transport_monotone_absorber"
    if not case.survives_consensus_state_machine:
        return "absorbed_consensus_state_machine", "consensus_state_machine_absorber"
    if not case.survives_record_provenance_completion or not case.provenance_complete:
        return "absorbed_record_provenance_completion", "record_provenance_completion_absorber"
    if case.transport_square_commutes_after_absorbers or not case.noncommuting_transport_square:
        return "rejected_commuting_after_absorbers", "none"
    if not case.operation_menu_derived_from_finality or not case.refinement_stable:
        return "rejected_not_finality_native", "none"
    if not case.bounded_fixture:
        return "outside_current_bounded_class", "none"
    if not case.prior_survivor and not case.independent_from_prior_survivors:
        return "rejected_prior_survivor_replay", "none"
    return "inside_bounded_domain_native_class", "none"


def _triggered_falsifiers(
    case: BoundaryCase,
    t560_result: t560.T560Result,
) -> tuple[str, ...]:
    falsifiers: list[str] = []
    declared = set(t560_result.frozen_falsifiers)
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


def _case_reason(status: str) -> str:
    reasons = {
        "inside_bounded_domain_native_class": (
            "The case is bounded, finality-native, target-blind, "
            "provenance-complete, noncommuting, and survives the mature absorbers."
        ),
        "rejected_t559_payload_replay": "A prior T559 survivor cannot count as a new generalization member.",
        "rejected_t560_transfer_replay": "A prior T560 survivor cannot count as a third fixture.",
        "absorbed_ordinary_sheaf_glue": "Ordinary sheaf gluing receives normal state and comparison rights.",
        "absorbed_resource_transport_monotone": "The apparent boundary factors through a native resource monotone.",
        "absorbed_consensus_state_machine": "Ordinary consensus or state-machine completion absorbs the split.",
        "absorbed_record_provenance_completion": "Completing normal provenance fields absorbs the boundary pressure.",
        "rejected_relabeling_falsifier": "The same source variables realize the target by relabeling only.",
        "rejected_hidden_target_or_cross_repo_import": "The case depends on target labels or cross-repo truth.",
        "rejected_observerse_replay": "T556 parked the Observerse route as audit residue only.",
        "rejected_aprd_replay": "APRD remains family-local feeder evidence, not this boundary.",
        "out_of_scope_taf8_cross_domain": "TAF8 cross-domain packets require their own domain-native spine.",
        "blocked_taf4_target_import": "TAF4 or Lorentzian target import cannot define sheaf transport success.",
        "blocked_source_law_overread": "Bounded survivors do not establish source-law status.",
        "rejected_no_domain_native_payload": "The case has formal shape but no finality-native payload.",
        "rejected_commuting_after_absorbers": "The transport square commutes after mature absorbers.",
        "rejected_not_finality_native": "The operation menu is not derived from finality sections and refinements.",
        "outside_current_bounded_class": "The case lacks the bounded fixture shape.",
        "rejected_prior_survivor_replay": "The case is not independent from prior survivors.",
        "rejected_underdeclared_source_variables": "The case does not carry every frozen source variable.",
    }
    return reasons[status]


def _gate_decisions(
    t559_result: t559.T559Result,
    t560_result: t560.T560Result,
    cases: tuple[BoundaryCase, ...],
    outcomes: tuple[BoundaryOutcome, ...],
) -> tuple[GateDecision, ...]:
    outcome_by_id = {outcome.case_id: outcome for outcome in outcomes}
    case_by_id = {case.case_id: case for case in cases}
    bounded_class = tuple(
        outcome.case_id for outcome in outcomes if outcome.in_generalization_class
    )
    absorber_outcomes = {
        outcome.absorber: outcome.actual_status
        for outcome in outcomes
        if outcome.absorber != "none"
    }
    triggered_falsifiers = {
        falsifier
        for outcome in outcomes
        for falsifier in outcome.triggered_falsifiers
    }
    prior_records = (
        set(case_by_id["t559_record_finality_transport_square_survivor"].record_ids),
        set(case_by_id["t560_handoff_rotation_repair_transfer_survivor"].record_ids),
        set(case_by_id["third_multicover_seal_handoff_fixture"].record_ids),
    )
    record_disjoint = all(
        left.isdisjoint(right)
        for index, left in enumerate(prior_records)
        for right in prior_records[index + 1 :]
    )
    third = case_by_id["third_multicover_seal_handoff_fixture"]

    gates = (
        (
            "t559_t560_authority",
            t559_result.verdict == t559.VERDICT
            and t560_result.verdict == t560.VERDICT
            and t560_result.selected_next_packet == t560.NEXT_PACKET,
            "T559 and T560 are completed bounded survivors and T560 selected T561.",
            "The required T559/T560 source state is not present.",
        ),
        (
            "family_contract_frozen",
            tuple(t560_result.frozen_source_variables) == t558.EXPECTED_SOURCE_VARIABLES
            and tuple(t560_result.frozen_mature_absorbers)
            == t558.EXPECTED_MATURE_ABSORBERS
            and tuple(t560_result.frozen_falsifiers) == t558.EXPECTED_FALSIFIERS,
            "The T557-T560 variables, absorbers, and falsifiers are unchanged.",
            "The sheaf transport contract drifted.",
        ),
        (
            "source_survivors_preserved",
            t559_result.admitted_domain_native_packets
            == ("record_finality_transport_square_payload",)
            and t560_result.independent_transfer_packets
            == ("handoff_rotation_repair_transfer_payload",),
            "The T559 and T560 survivors are preserved as source state.",
            "A prior survivor is missing or altered.",
        ),
        (
            "third_fixture_independent",
            outcome_by_id["third_multicover_seal_handoff_fixture"].in_generalization_class
            and third.independent_from_prior_survivors
            and not third.reuses_t559_payload_shape
            and not third.reuses_t560_transfer_shape
            and record_disjoint
            and len(third.phases) >= 4
            and len(third.partition_shape) >= 4,
            "The third fixture is record-disjoint, multi-phase, differently partitioned, and independent.",
            "The third fixture is not independent enough from prior survivors.",
        ),
        (
            "bounded_class_has_three_members",
            bounded_class
            == (
                "t559_record_finality_transport_square_survivor",
                "t560_handoff_rotation_repair_transfer_survivor",
                "third_multicover_seal_handoff_fixture",
            ),
            "The bounded class contains exactly the two prior survivors plus the third fixture.",
            "The bounded class has the wrong membership.",
        ),
        (
            "all_mature_absorbers_exercised",
            all(
                absorber in absorber_outcomes
                and absorber_outcomes[absorber].startswith("absorbed_")
                for absorber in t560_result.frozen_mature_absorbers
            ),
            "Every mature absorber receives a boundary control case.",
            "One or more mature absorbers were not exercised.",
        ),
        (
            "all_declared_falsifiers_exercised",
            set(t560_result.frozen_falsifiers) <= triggered_falsifiers,
            "Every declared falsifier is triggered by at least one control case.",
            "One or more frozen falsifiers were not tested.",
        ),
        (
            "replay_and_spent_routes_rejected",
            outcome_by_id["t559_payload_replay_as_new_fixture"].actual_status
            == "rejected_t559_payload_replay"
            and outcome_by_id["t560_transfer_replay_as_new_fixture"].actual_status
            == "rejected_t560_transfer_replay"
            and outcome_by_id["observerse_replay_boundary"].actual_status
            == "rejected_observerse_replay"
            and outcome_by_id["aprd_replay_boundary"].actual_status
            == "rejected_aprd_replay",
            "T559 replay, T560 replay, Observerse replay, and APRD replay are rejected.",
            "A replay or retired route was allowed.",
        ),
        (
            "taf4_taf8_and_source_law_boundaries_detected",
            outcome_by_id["taf8_cross_domain_boundary"].actual_status
            == "out_of_scope_taf8_cross_domain"
            and outcome_by_id["taf4_lorentzian_target_import_boundary"].actual_status
            == "blocked_taf4_target_import"
            and outcome_by_id["source_law_overread_boundary"].actual_status
            == "blocked_source_law_overread",
            "TAF8, TAF4, and source-law overread shortcuts are rejected.",
            "A target, cross-domain, or source-law shortcut was admitted.",
        ),
        (
            "all_boundary_predictions_match",
            all(outcome.matched for outcome in outcomes),
            "Every boundary case matched the predeclared status.",
            "At least one boundary case missed its predeclared status.",
        ),
        (
            "next_packet_specific",
            NEXT_PACKET == "t562_domain_native_sheaf_transport_minimality_gate",
            "A single minimality gate is named as the next packet.",
            "No specific next packet is named.",
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
            control_id="source_law_overread_control",
            blocks="Treating three bounded domain-native survivors as source-law proof.",
            reason="T561 maps a bounded class boundary; it does not promote the class.",
        ),
        HostileControl(
            control_id="prior_survivor_replay_control",
            blocks="Counting T559 or T560 shape replay as new generalization.",
            reason="The third fixture must be record-disjoint and differently partitioned.",
        ),
        HostileControl(
            control_id="absorber_screen_control",
            blocks="Reading ordinary gluing, resource, consensus, or provenance completion as residue.",
            reason="The same four mature absorbers receive boundary controls.",
        ),
        HostileControl(
            control_id="taf4_target_import_control",
            blocks="Using Lorentzian, causal-set, or finite-to-continuum targets as success criteria.",
            reason="T561 is internal TAF11 route control, not TAF4 bridge evidence.",
        ),
        HostileControl(
            control_id="taf8_cross_domain_control",
            blocks="Executing TAF8 or importing a cross-domain transfer packet.",
            reason="TAF8 still needs a real domain-native packet under its own spine.",
        ),
        HostileControl(
            control_id="spent_route_control",
            blocks="Replaying Observerse or APRD as the generalization route.",
            reason="Observerse is parked after T556 and APRD narrowed after T548.",
        ),
    )


def _claim_labels(outcomes: tuple[BoundaryOutcome, ...]) -> tuple[ClaimLabel, ...]:
    inside_ids = tuple(
        outcome.case_id for outcome in outcomes if outcome.in_generalization_class
    )
    blocked_ids = tuple(
        outcome.case_id for outcome in outcomes if not outcome.in_generalization_class
    )
    absorber_count = sum(1 for outcome in outcomes if outcome.absorber != "none")
    falsifier_count = len(
        {
            falsifier
            for outcome in outcomes
            for falsifier in outcome.triggered_falsifiers
        }
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The bounded domain-native class currently includes: "
                + ", ".join(inside_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "The gate blocks or absorbs these overreach cases: "
                + ", ".join(blocked_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                f"{absorber_count} mature absorber controls and {falsifier_count} "
                "declared falsifiers remain active at the boundary."
            ),
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text=(
                "The next useful test is minimality across the admitted bounded "
                "class, not source-law, TAF4, TAF8, or public-posture movement."
            ),
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T561 Results: Domain-Native Sheaf Transport Generalization-Boundary Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Generalization status: `{payload['generalization_status']}`",
        f"- Source T559 verdict: `{payload['source_t559_verdict']}`",
        f"- Source T560 verdict: `{payload['source_t560_verdict']}`",
        f"- Source T560 selected next packet: `{payload['source_t560_selected_next_packet']}`",
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
    lines.extend(["", "Bounded survivor class:"])
    lines.extend(f"- `{item}`" for item in payload["bounded_survivor_class"])
    lines.extend(
        [
            "",
            "## Boundary Outcomes",
            "",
            "| case | expected | actual | matched? | in class? | absorber | falsifiers | reason |",
            "| --- | --- | --- | :---: | :---: | --- | --- | --- |",
        ]
    )
    for outcome in payload["boundary_outcomes"]:
        falsifiers = ", ".join(outcome["triggered_falsifiers"]) or "none"
        lines.append(
            "| "
            f"`{outcome['case_id']}` | "
            f"`{outcome['expected_status']}` | "
            f"`{outcome['actual_status']}` | "
            f"{outcome['matched']} | "
            f"{outcome['in_generalization_class']} | "
            f"`{outcome['absorber']}` | "
            f"{falsifiers} | "
            f"{outcome['reason']} |"
        )
    lines.extend(["", "## Gate Decisions", "", "| gate | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
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
        ("Source-Law Reading", "source_law_reading"),
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


def write_results(result: T561Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t561_result_to_dict(result)
    json_path = (
        results_dir
        / "T561-domain-native-sheaf-transport-generalization-boundary-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T561-domain-native-sheaf-transport-generalization-boundary-gate-v0.1-results.md"
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

    result = run_t561_analysis()
    payload = t561_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
