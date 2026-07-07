"""Tests for T481: internal scale-structure admission gate."""

from __future__ import annotations

from models.internal_scale_structure_admission_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_review_only_without_promotion():
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
    assert verdict["internal_scale_structure_earned"] is False


def test_t480_anchor_checks_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t480_gate_passed"] is True
    assert anchors["t480_external_or_internal_status_required"] is True
    assert anchors["t480_comparison_edges_required"] is True
    assert anchors["t480_no_clock_or_duration_earned"] is True
    assert anchors["t480_no_scale_genesis_earned"] is True
    assert anchors["t480_positive_packet_bookkeeping_only"] is True


def test_external_bookkeeping_packet_is_admitted_only_as_bookkeeping():
    result = run()
    packet = _candidate(result, "external_scale_label_bookkeeping")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_external_bookkeeping"
    assert packet["route_label"] == "EXTERNAL_SCALE_BOOKKEEPING_ADMITTED_NO_PROMOTION"
    assert packet["declared_status"] == "external_bookkeeping"
    assert "comparison bookkeeping" in packet["admitted_reading"]
    assert "joined by declared T38 transport edges" in packet["comparison_domain"]
    assert packet["blockers"] == []


def test_synthetic_internal_review_target_is_admitted_without_earning_structure():
    result = run()
    packet = _candidate(result, "synthetic_internal_scale_review_target")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_synthetic_review_target"
    assert packet["route_label"] == "INTERNAL_SCALE_REVIEW_TARGET_ADMITTED_NO_PROMOTION"
    assert packet["declared_status"] == "internal_structure_review_target"
    assert "compatibility operator" in packet["internal_generating_rule"]
    assert "predeclared equivalence classes" in packet["comparison_domain"]
    assert "future review target" in packet["admitted_reading"]
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == [
        "external_scale_label_bookkeeping",
        "synthetic_internal_scale_review_target",
    ]


def test_internal_by_assertion_and_label_restatement_are_blocked():
    result = run()
    assertion = _candidate(result, "internal_by_assertion")
    label_only = _candidate(result, "label_restatement_as_structure")

    assert assertion["admitted"] is False
    assert "internal_generating_rule_not_declared" in assertion["blockers"]
    assert "positive_negative_controls_missing" in assertion["blockers"]
    assert "relabel_invariance_check_missing" in assertion["blockers"]

    assert label_only["admitted"] is False
    assert "scale_label_operation_not_declared" in label_only["blockers"]
    assert "label_word_without_operation" in label_only["blockers"]


def test_posthoc_domain_and_hidden_calendar_shortcuts_are_blocked():
    result = run()
    posthoc = _candidate(result, "posthoc_comparison_domain")
    hidden_calendar = _candidate(result, "hidden_calendar_internal_scale")

    assert posthoc["admitted"] is False
    assert "comparison_domain_selected_posthoc" in posthoc["blockers"]

    assert hidden_calendar["admitted"] is False
    assert "hidden_calendar_or_time_order" in hidden_calendar["blockers"]
    assert "positive_negative_controls_missing" in hidden_calendar["blockers"]


def test_duration_arrow_and_finality_overreads_are_blocked():
    result = run()
    duration = _candidate(result, "duration_from_internal_order")
    finality = _candidate(result, "record_finality_from_internal_scale")

    assert duration["admitted"] is False
    assert "duration_or_arrow_derived_from_scale_structure" in duration["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_changed_by_scale_structure" in finality["blockers"]


def test_rg_conformal_and_promotion_shortcuts_are_blocked():
    result = run()
    rg = _candidate(result, "rg_fixed_point_internal_source")
    promotion = _candidate(result, "promotion_shortcut_packet")

    assert rg["admitted"] is False
    assert "rg_or_conformal_mechanism_imported" in rg["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in rg["blockers"]
    assert "no_local_taf_anchor" in rg["blockers"]

    assert promotion["admitted"] is False
    assert "scale_genesis_or_physics_claim_overread" in promotion["blockers"]
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]


def test_future_packet_minimum_preserves_t480_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "state whether the scale label is external bookkeeping or claimed internal structure"
        in result["future_packet_minimum"]
    )
    assert "predeclare the comparison domain before selecting a witness or separator" in (
        result["future_packet_minimum"]
    )
    assert "internal scale structure" in result["not_earned"]
    assert "record clock" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
