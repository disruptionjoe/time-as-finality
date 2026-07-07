"""Tests for T487: reachability-quotient capability-spread gate."""

from __future__ import annotations

from models.reachability_quotient_capability_spread_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_task_only_capability_spread_gate():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["reachability_task_sufficient"] is True
    assert verdict["role_profile_task_sufficient"] is True
    assert verdict["path_latency_underdetermined"] is True
    assert verdict["relay_budget_underdetermined"] is True
    assert verdict["component_size_underdetermined"] is True
    assert verdict["internal_scale_structure_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False
    assert verdict["record_finality_change_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["physics_claim_earned"] is False
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"


def test_t485_anchor_is_consumed_without_reopening_promotions():
    result = run()
    anchor = result["t485_anchor"]

    assert anchor["artifact_id"] == "T485-transport-topology-invariant-quotient-gate-v0.1"
    assert anchor["gate_passed"] is True
    assert anchor["reachability_quotient_admitted"] is True
    assert anchor["component_size_scale_blocked"] is True
    assert anchor["hop_band_scale_blocked"] is True
    assert anchor["record_finality_change_earned"] is False


def test_reachability_capability_spreads_are_singleton_by_visible_quotient():
    result = run()
    spreads = result["capability_spreads"]

    assert spreads["source_target_reachable"]["all_visible_classes_singleton"] is True
    assert spreads["quotient_role_profile"]["all_visible_classes_singleton"] is True
    assert spreads["source_target_reachable"]["non_singleton_visible_classes"] == []
    assert spreads["quotient_role_profile"]["non_singleton_visible_classes"] == []


def test_path_relay_and_component_size_spreads_are_non_singleton():
    result = run()
    spreads = result["capability_spreads"]

    assert spreads["source_target_hop_band"]["all_visible_classes_singleton"] is False
    assert spreads["relay_site_count"]["all_visible_classes_singleton"] is False
    assert spreads["max_component_size"]["all_visible_classes_singleton"] is False

    connected_key = "(('source_target_component', 4),)"
    assert connected_key in spreads["source_target_hop_band"]["non_singleton_visible_classes"]
    assert connected_key in spreads["relay_site_count"]["non_singleton_visible_classes"]
    assert connected_key in spreads["max_component_size"]["non_singleton_visible_classes"]


def test_only_declared_reachability_tasks_are_admitted():
    result = run()

    assert result["admitted_candidate_ids"] == [
        "source_target_reachability_task",
        "quotient_role_profile_task",
    ]
    assert result["hostile_violations"] == []

    reachability = _candidate(result, "source_target_reachability_task")
    role_profile = _candidate(result, "quotient_role_profile_task")

    assert reachability["admitted"] is True
    assert reachability["decision"] == "admit_declared_reachability_task_only"
    assert role_profile["admitted"] is True
    assert role_profile["route_label"] == "REACHABILITY_CAPABILITY_SPREAD_SINGLETON"


def test_latency_relay_and_component_size_tasks_are_rejected():
    result = run()
    latency = _candidate(result, "path_latency_band_task")
    relay = _candidate(result, "relay_budget_task")
    component_size = _candidate(result, "component_size_capacity_task")

    assert latency["admitted"] is False
    assert latency["decision"] == "reject_non_singleton_spread"
    assert "path_or_hop_band_refinement_variant" in latency["blockers"]
    assert "non_singleton_capability_spread" in latency["blockers"]

    assert relay["admitted"] is False
    assert "relay_count_refinement_artifact" in relay["blockers"]
    assert "non_singleton_capability_spread" in relay["blockers"]

    assert component_size["admitted"] is False
    assert "component_size_refinement_variant" in component_size["blockers"]
    assert "reachability_quotient_not_internal_scale_structure" in component_size["blockers"]


def test_finality_scale_physics_and_promotion_overreads_are_blocked():
    result = run()
    finality = _candidate(result, "reachability_finality_task")
    promotion = _candidate(result, "quotient_promotion_task")

    assert finality["admitted"] is False
    assert "record_finality_change_overread" in finality["blockers"]
    assert "capability_not_task_natural_under_t485" in finality["blockers"]

    assert promotion["admitted"] is False
    assert "reachability_quotient_not_internal_scale_structure" in promotion["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in promotion["blockers"]
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]


def test_future_packet_minimum_preserves_capability_spread_guard():
    result = run()

    assert (
        "compute capability spread over quotient-visible fibers"
        in result["future_packet_minimum"]
    )
    assert "independent internal scale structure" in result["not_earned"]
    assert "record-finality change" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
