"""Tests for T483: internal scale-generator independence gate."""

from __future__ import annotations

from models.internal_scale_generator_independence_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_review_target_only_without_promotion():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["transport_topology_review_target_admitted"] is True
    assert verdict["d1_completion_control_blocked"] is True
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False
    assert verdict["record_finality_change_earned"] is False
    assert verdict["internal_scale_structure_earned"] is False


def test_t482_anchor_checks_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t482_gate_passed"] is True
    assert anchors["t482_support_gradient_admitted_as_bookkeeping"] is True
    assert anchors["t482_support_gradient_factors_through_d1"] is True
    assert anchors["t482_no_internal_scale_structure_earned"] is True
    assert anchors["t482_no_clock_or_duration_earned"] is True
    assert anchors["t482_future_packet_requires_independent_generator"] is True


def test_fixed_d1_transport_topology_controls_pass():
    result = run()
    controls = result["fixed_d1_independence_probe"]["controls"]

    assert controls["fixed_d1_vectors_match"] is True
    assert controls["transport_topology_separates"] is True
    assert controls["transport_topology_relabel_invariant"] is True
    assert controls["connected_source_target_reachable"] is True
    assert controls["partitioned_source_target_reachable"] is False
    assert controls["d1_profile_completion_insufficient"] is True
    assert controls["uses_clock_duration_or_finality_status"] is False
    assert controls["imports_rg_or_conformal_mechanism"] is False


def test_transport_topology_assignments_show_fixed_d1_separation():
    result = run()
    probe = result["fixed_d1_independence_probe"]

    assert probe["connected_signature"] == {"source_target_component": 4}
    assert probe["partitioned_signature"] == {
        "source_side_component": 2,
        "target_side_component": 2,
    }
    assert probe["connected_signature"] == probe["relabel_signature"]
    assert all(
        row["profile_tuple"] == [2, 2, 1, 1]
        for row in probe["connected_assignments"] + probe["partitioned_assignments"]
    )


def test_t482_support_gradient_is_rejected_as_d1_completion():
    result = run()
    packet = _candidate(result, "t482_d1_support_gradient")

    assert packet["admitted"] is False
    assert packet["decision"] == "reject_d1_completion_absorbed"
    assert packet["route_label"] == "D1_COMPLETION_ABSORBED_GENERATOR"
    assert "d1_profile_completion_absorbs_generator" in packet["blockers"]


def test_transport_topology_packet_is_admitted_only_as_review_target():
    result = run()
    packet = _candidate(result, "transport_topology_review_target")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_review_target_no_scale_structure"
    assert (
        packet["route_label"]
        == "TRANSPORT_TOPOLOGY_REVIEW_TARGET_ADMITTED_NO_SCALE_STRUCTURE"
    )
    assert packet["uses_transport_topology"] is True
    assert packet["d1_profile_completion_sufficient"] is False
    assert packet["separates_fixed_d1_transport_counterfactual"] is True
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["transport_topology_review_target"]


def test_label_posthoc_and_observer_order_shortcuts_are_blocked():
    result = run()
    label_only = _candidate(result, "label_word_independence")
    posthoc = _candidate(result, "posthoc_counterfactual_selector")
    observer_order = _candidate(result, "observer_id_rank_independence")

    assert label_only["admitted"] is False
    assert "generator_not_predeclared" in label_only["blockers"]
    assert "label_word_without_generator" in label_only["blockers"]

    assert posthoc["admitted"] is False
    assert "posthoc_counterfactual_selection" in posthoc["blockers"]
    assert "comparison_domain_not_predeclared" in posthoc["blockers"]

    assert observer_order["admitted"] is False
    assert "observer_label_order_not_relabel_invariant" in observer_order["blockers"]


def test_time_finality_rg_and_promotion_overreads_are_blocked():
    result = run()
    hidden_time = _candidate(result, "hidden_time_order_independence")
    finality = _candidate(result, "finality_by_transport_component")
    rg = _candidate(result, "rg_fixed_point_independence_source")
    promotion = _candidate(result, "promotion_shortcut_independence")

    assert hidden_time["admitted"] is False
    assert "hidden_calendar_or_time_order" in hidden_time["blockers"]
    assert "clock_duration_or_arrow_overread" in hidden_time["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_change_overread" in finality["blockers"]

    assert rg["admitted"] is False
    assert "rg_or_conformal_mechanism_imported" in rg["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in rg["blockers"]
    assert "no_local_taf_anchor" in rg["blockers"]

    assert promotion["admitted"] is False
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]


def test_future_packet_minimum_preserves_independence_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "prove the generator is not recoverable from the existing D1 profile tuple"
        in result["future_packet_minimum"]
    )
    assert (
        "include a fixed-D1 counterfactual pair before claiming independence"
        in result["future_packet_minimum"]
    )
    assert "independent internal scale structure" in result["not_earned"]
    assert "record clock" in result["not_earned"]
    assert "record-finality change" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
