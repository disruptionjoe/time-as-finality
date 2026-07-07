"""Tests for T482: internal scale-generator invariance probe."""

from __future__ import annotations

from models.internal_scale_generator_invariance_probe import VERDICT, run


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
    assert verdict["support_gradient_review_packet_admitted"] is True
    assert verdict["factors_through_existing_d1_profile"] is True
    assert verdict["internal_scale_structure_earned"] is False
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False
    assert verdict["record_finality_change_earned"] is False


def test_t481_anchor_checks_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t481_gate_passed"] is True
    assert anchors["t481_synthetic_review_target_admitted"] is True
    assert anchors["t481_external_bookkeeping_still_admitted"] is True
    assert anchors["t481_no_internal_scale_structure_earned"] is True
    assert anchors["t481_no_clock_or_duration_earned"] is True
    assert anchors["t481_future_packet_requires_relabel_invariance"] is True


def test_support_gradient_controls_pass_but_factor_through_d1():
    result = run()
    controls = result["support_gradient_probe"]["controls"]

    assert controls["stratified_packet_nontrivial"] is True
    assert controls["uniform_packet_collapses_to_single_band"] is True
    assert controls["support_gradient_relabel_invariant"] is True
    assert controls["comparison_domain_predeclared_as_transport_edges"] is True
    assert controls["generator_factors_through_d1_profile"] is True
    assert controls["uses_clock_duration_or_finality_status"] is False
    assert controls["imports_rg_or_conformal_mechanism"] is False


def test_d1_support_gradient_packet_is_admitted_only_as_review_bookkeeping():
    result = run()
    packet = _candidate(result, "d1_support_gradient_review_packet")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_review_packet_no_scale_structure"
    assert packet["route_label"] == "D1_SUPPORT_GRADIENT_REVIEW_ADMITTED_BOOKKEEPING_ONLY"
    assert packet["factors_through_d1_profile"] is True
    assert "support_depth" in packet["generator_rule"]
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["d1_support_gradient_review_packet"]


def test_stratified_assignments_have_predeclared_bands():
    result = run()
    assignments = {
        row["observer_id"]: row
        for row in result["support_gradient_probe"]["stratified_assignments"]
    }

    assert assignments["individual"]["support_depth"] == 4
    assert assignments["individual"]["support_band"] == "low_support"
    assert assignments["family"]["support_depth"] == 6
    assert assignments["family"]["support_band"] == "middle_support"
    assert assignments["lab"]["support_depth"] == 11
    assert assignments["lab"]["support_band"] == "high_support"
    assert result["support_gradient_probe"]["class_counts"] == {
        "high_support": 1,
        "low_support": 3,
        "middle_support": 2,
    }


def test_label_posthoc_and_observer_order_shortcuts_are_blocked():
    result = run()
    label_only = _candidate(result, "label_word_internal_scale")
    posthoc = _candidate(result, "posthoc_support_thresholds")
    observer_order = _candidate(result, "observer_id_rank_generator")

    assert label_only["admitted"] is False
    assert "generator_not_predeclared" in label_only["blockers"]
    assert "label_word_without_generator" in label_only["blockers"]

    assert posthoc["admitted"] is False
    assert "posthoc_thresholds" in posthoc["blockers"]
    assert "comparison_domain_not_predeclared" in posthoc["blockers"]

    assert observer_order["admitted"] is False
    assert "observer_label_order_not_relabel_invariant" in observer_order["blockers"]


def test_time_finality_rg_and_promotion_overreads_are_blocked():
    result = run()
    time_order = _candidate(result, "hidden_time_step_generator")
    finality = _candidate(result, "finality_by_support_band")
    rg = _candidate(result, "rg_fixed_point_scale_generator")
    promotion = _candidate(result, "promotion_shortcut_generator")

    assert time_order["admitted"] is False
    assert "hidden_calendar_or_time_order" in time_order["blockers"]
    assert "clock_duration_or_arrow_overread" in time_order["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_change_overread" in finality["blockers"]

    assert rg["admitted"] is False
    assert "rg_or_conformal_mechanism_imported" in rg["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in rg["blockers"]

    assert promotion["admitted"] is False
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]


def test_future_packet_minimum_preserves_no_overread_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "keep support-gradient packets labeled as D1 bookkeeping unless an independent generator is supplied"
        in result["future_packet_minimum"]
    )
    assert "independent internal scale structure" in result["not_earned"]
    assert "record clock" in result["not_earned"]
    assert "record-finality change" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
