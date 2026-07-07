"""Tests for T484: transport-topology refinement naturalness gate."""

from __future__ import annotations

from models.transport_topology_refinement_naturalness_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_reachability_bookkeeping_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["reachability_packet_admitted"] is True
    assert verdict["component_size_scale_blocked"] is True
    assert verdict["path_length_scale_blocked"] is True
    assert verdict["internal_scale_structure_earned"] is False
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False
    assert verdict["record_finality_change_earned"] is False


def test_t483_anchor_checks_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t483_gate_passed"] is True
    assert anchors["t483_transport_topology_review_target_admitted"] is True
    assert anchors["t483_fixed_d1_control_passed"] is True
    assert anchors["t483_no_internal_scale_structure_earned"] is True
    assert anchors["t483_no_clock_or_duration_earned"] is True
    assert anchors["t483_future_packet_requires_fixed_d1_control"] is True


def test_refinement_controls_narrow_topology_to_reachability():
    result = run()
    controls = result["refinement_probe"]["controls"]

    assert controls["original_d1_vectors_fixed"] is True
    assert controls["reachability_separates_fixed_d1_pair"] is True
    assert controls["connected_refinement_preserves_original_roles"] is True
    assert controls["partitioned_refinement_preserves_original_roles"] is True
    assert controls["reachability_relabel_invariant"] is True
    assert controls["component_size_changes_under_refinement"] is True
    assert controls["path_length_changes_under_refinement"] is True
    assert controls["partitioned_source_target_remain_unreachable"] is True
    assert controls["uses_clock_duration_or_finality_status"] is False
    assert controls["imports_rg_or_conformal_mechanism"] is False


def test_reachability_assignments_are_refinement_stable():
    result = run()
    probe = result["refinement_probe"]

    assert probe["connected_signature"] == {"source_target_component": 4}
    assert probe["connected_refined_signature"] == {"source_target_component": 4}
    assert probe["partitioned_signature"] == {
        "source_side_component": 2,
        "target_side_component": 2,
    }
    assert probe["partitioned_refined_signature"] == {
        "source_side_component": 2,
        "target_side_component": 2,
    }
    assert all(
        row["profile_tuple"] == [2, 2, 1, 1]
        for row in probe["connected_original_assignments"]
        + probe["connected_refined_original_assignments"]
        + probe["partitioned_original_assignments"]
        + probe["partitioned_refined_original_assignments"]
    )


def test_component_size_and_path_length_change_under_benign_refinement():
    result = run()
    probe = result["refinement_probe"]

    assert probe["connected_component_sizes"] == {
        "family": 4,
        "individual": 4,
        "institution": 4,
        "lab": 4,
    }
    assert probe["connected_refined_component_sizes"] == {
        "family": 7,
        "individual": 7,
        "institution": 7,
        "lab": 7,
    }
    assert probe["connected_source_target_path_length"] == 3
    assert probe["connected_refined_source_target_path_length"] == 6
    assert probe["partitioned_source_target_path_length"] is None


def test_reachability_packet_is_admitted_only_as_bookkeeping():
    result = run()
    packet = _candidate(result, "source_target_reachability_packet")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_reachability_bookkeeping_no_scale_structure"
    assert (
        packet["route_label"]
        == "REACHABILITY_BOOKKEEPING_ADMITTED_NO_SCALE_STRUCTURE"
    )
    assert packet["uses_reachability_relation"] is True
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["source_target_reachability_packet"]


def test_refinement_variant_scale_readings_are_blocked():
    result = run()
    component_size = _candidate(result, "component_size_as_scale")
    path_length = _candidate(result, "shortest_path_length_as_scale")

    assert component_size["admitted"] is False
    assert component_size["decision"] == "reject_refinement_variant"
    assert "component_size_refinement_variant" in component_size["blockers"]

    assert path_length["admitted"] is False
    assert path_length["decision"] == "reject_refinement_variant"
    assert "path_length_refinement_variant" in path_length["blockers"]


def test_label_time_finality_rg_and_promotion_overreads_are_blocked():
    result = run()
    label_only = _candidate(result, "label_word_topology_scale")
    observer_order = _candidate(result, "observer_id_component_order")
    relay_clock = _candidate(result, "relay_count_as_clock")
    finality = _candidate(result, "record_finality_by_reachability")
    rg = _candidate(result, "rg_fixed_point_topology_source")
    promotion = _candidate(result, "promotion_shortcut_topology")

    assert label_only["admitted"] is False
    assert "generator_not_predeclared" in label_only["blockers"]
    assert "label_word_without_generator" in label_only["blockers"]

    assert observer_order["admitted"] is False
    assert "observer_label_order_not_relabel_invariant" in observer_order["blockers"]

    assert relay_clock["admitted"] is False
    assert "hidden_calendar_or_time_order" in relay_clock["blockers"]
    assert "clock_duration_or_arrow_overread" in relay_clock["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_change_overread" in finality["blockers"]

    assert rg["admitted"] is False
    assert "rg_or_conformal_mechanism_imported" in rg["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in rg["blockers"]
    assert "no_local_taf_anchor" in rg["blockers"]

    assert promotion["admitted"] is False
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]


def test_future_packet_minimum_preserves_refinement_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "include transport-refinement controls before using topology as a generator"
        in result["future_packet_minimum"]
    )
    assert (
        "reject component-size and path-length scale readings unless an invariant morphism class is declared"
        in result["future_packet_minimum"]
    )
    assert "independent internal scale structure" in result["not_earned"]
    assert "record clock" in result["not_earned"]
    assert "record-finality change" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
