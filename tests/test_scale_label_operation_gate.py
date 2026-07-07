"""Tests for T480: scale-label operation gate."""

from __future__ import annotations

from models.scale_label_operation_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_bookkeeping_only_without_promotion():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False


def test_local_t479_t24_and_t38_anchors_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t479_gate_passed"] is True
    assert anchors["t479_scale_label_burden_declared"] is True
    assert anchors["t479_no_record_clock_earned"] is True
    assert anchors["t24_field_d1_required_for_transport_and_gluing_claims"] is True
    assert anchors["t24_scalar_recoverable_only_as_special_case"] is True
    assert anchors["t38_h1_plus_is_best_supported"] is True
    assert anchors["t38_compression_and_emergence_records_present"] is True


def test_positive_packet_admits_declared_scale_label_bookkeeping_only():
    result = run()
    packet = _candidate(result, "declared_scale_section_bookkeeping")

    assert packet["admitted"] is True
    assert packet["route_label"] == "SCALE_LABEL_BOOKKEEPING_ADMITTED_NO_CLOCK_PROMOTION"
    assert "field-valued D1" in packet["transported_structure"]
    assert "T38 H1+" in packet["transport_law"]
    assert "external finite scale label" in packet["scale_label_operation"]
    assert "no clock" in packet["admitted_reading"]
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["declared_scale_section_bookkeeping"]


def test_fixed_point_clock_and_rg_scale_imports_are_blocked():
    result = run()
    fixed_point = _candidate(result, "fixed_point_intrinsic_clock")
    rg_scale = _candidate(result, "rg_scale_parameter_as_clock")

    assert fixed_point["admitted"] is False
    assert "fixed_point_generates_intrinsic_clock" in fixed_point["blockers"]

    assert rg_scale["admitted"] is False
    assert "rg_scale_imported_as_record_clock" in rg_scale["blockers"]
    assert "no_local_taf_anchor" in rg_scale["blockers"]


def test_label_only_and_hidden_calendar_shortcuts_are_blocked():
    result = run()
    label_only = _candidate(result, "label_only_no_operation")
    hidden_calendar = _candidate(result, "hidden_calendar_breaking")

    assert label_only["admitted"] is False
    assert "scale_label_operation_not_declared" in label_only["blockers"]
    assert "label_word_without_operation" in label_only["blockers"]

    assert hidden_calendar["admitted"] is False
    assert "hidden_calendar_or_time_order" in hidden_calendar["blockers"]


def test_duration_arrow_and_finality_relabel_overreads_are_blocked():
    result = run()
    duration = _candidate(result, "duration_from_scale_order")
    finality = _candidate(result, "record_finality_by_relabel")

    assert duration["admitted"] is False
    assert "duration_or_arrow_derived_from_scale_label" in duration["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_changed_by_label" in finality["blockers"]


def test_phenomenology_and_claim_promotion_shortcuts_are_blocked():
    result = run()
    phenomenology = _candidate(result, "conformal_phenomenology_support")
    promotion = _candidate(result, "scale_genesis_claim_promotion")

    assert phenomenology["admitted"] is False
    assert "conformal_phenomenology_used_as_support" in phenomenology["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in phenomenology["blockers"]

    assert promotion["admitted"] is False
    assert "scale_genesis_or_physics_claim_overread" in promotion["blockers"]


def test_future_packet_minimum_preserves_post_t479_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "declare the scale-label operation as an operation, not a label word"
        in result["future_packet_minimum"]
    )
    assert "record clock" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
