"""Tests for T479: RG-flow multiscale calibration gate."""

from __future__ import annotations

from models.rg_flow_multiscale_calibration_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_analogy_only_without_promotion():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["observer_theory_or_rg_equivalence_earned"] is False


def test_local_t24_and_t38_anchors_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t24_vector_d1_required_for_multiscale_snapshots"] is True
    assert anchors["t24_field_d1_required_for_transport_and_gluing_claims"] is True
    assert anchors["t24_scalar_recoverable_only_as_special_case"] is True
    assert anchors["t38_h1_plus_is_best_supported"] is True
    assert anchors["t38_compression_record_present"] is True
    assert anchors["t38_emergence_record_present"] is True
    assert anchors["t38_h2_required"] is False
    assert anchors["t38_h3_required"] is False


def test_positive_packet_names_all_three_rg_analogues():
    result = run()
    packet = _candidate(result, "taf_d1_h1_plus_scale_calibration")

    assert packet["admitted"] is True
    assert packet["route_label"] == "ANALOGY_CALIBRATION_ADMITTED_NO_PROMOTION"
    assert "field-valued D1 profile" in packet["transported_structure"]
    assert "TypedTransportNetwork" in packet["transport_law"]
    assert "no intrinsic" in packet["fixed_point_analogue"]
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["taf_d1_h1_plus_scale_calibration"]


def test_coupling_flow_and_action_imports_are_blocked():
    result = run()
    coupling = _candidate(result, "coupling_flow_import")
    action = _candidate(result, "lagrangian_record_action")

    assert coupling["admitted"] is False
    assert "coupling_flow_imported_as_record_flow" in coupling["blockers"]
    assert "no_local_taf_transport_anchor" in coupling["blockers"]

    assert action["admitted"] is False
    assert "lagrangian_action_imported_onto_records" in action["blockers"]


def test_fixed_point_and_record_finality_overreads_are_blocked():
    result = run()
    clocked = _candidate(result, "clocked_fixed_point_overread")
    overread = _candidate(result, "record_finality_from_rg_claim")

    assert clocked["admitted"] is False
    assert "fixed_point_carries_intrinsic_scale_or_clock" in clocked["blockers"]

    assert overread["admitted"] is False
    assert "record_finality_derived_from_rg_overread" in overread["blockers"]
    assert "physics_or_public_posture_overread" in overread["blockers"]


def test_incomplete_and_phenomenology_controls_are_blocked():
    result = run()
    incomplete = _candidate(result, "fixed_point_only_no_transport")
    phenomenology = _candidate(result, "conformal_phenomenology_support")

    assert incomplete["admitted"] is False
    assert "transported_structure_not_named" in incomplete["blockers"]
    assert "transport_law_not_named" in incomplete["blockers"]
    assert "no_local_taf_transport_anchor" in incomplete["blockers"]

    assert phenomenology["admitted"] is False
    assert "conformal_phenomenology_used_as_support" in phenomenology["blockers"]


def test_future_packet_minimum_preserves_guardrails():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "keep external RG and conformal-gravity sources at analogy-ledger grade until primary sources are checked"
        in result["future_packet_minimum"]
    )
    assert "RG/TaF equivalence theorem" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
