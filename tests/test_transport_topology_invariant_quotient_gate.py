"""Tests for T485: transport-topology invariant quotient gate."""

from __future__ import annotations

from models.transport_topology_invariant_quotient_gate import VERDICT, run


def _candidate(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_evaluations"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_reachability_quotient_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["reachability_quotient_admitted"] is True
    assert verdict["component_count_absorbed"] is True
    assert verdict["component_size_scale_blocked"] is True
    assert verdict["path_length_scale_blocked"] is True
    assert verdict["hop_band_scale_blocked"] is True
    assert verdict["internal_scale_structure_earned"] is False
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["north_star_update"] == "none"
    assert verdict["roadmap_update"] == "none"
    assert verdict["public_posture_update"] == "none"
    assert verdict["physics_claim_earned"] is False
    assert verdict["scale_genesis_theorem_earned"] is False
    assert verdict["record_clock_or_duration_earned"] is False
    assert verdict["record_finality_change_earned"] is False


def test_t484_anchor_checks_are_present():
    result = run()
    anchors = result["local_anchor_checks"]

    assert anchors["t484_gate_passed"] is True
    assert anchors["t484_reachability_bookkeeping_only"] is True
    assert anchors["t484_component_size_blocked"] is True
    assert anchors["t484_path_length_blocked"] is True
    assert anchors["t484_no_internal_scale_structure_earned"] is True
    assert anchors["t484_future_packet_requires_refinement_controls"] is True


def test_quotient_controls_pass_and_separate_fixed_d1_pair():
    result = run()
    controls = result["quotient_probe"]["controls"]

    assert controls["original_d1_vectors_fixed"] is True
    assert controls["reachability_quotient_separates_fixed_d1_pair"] is True
    assert controls["connected_quotient_stable_under_refinement"] is True
    assert controls["partitioned_quotient_stable_under_refinement"] is True
    assert controls["quotient_relabel_invariant"] is True
    assert controls["component_count_is_quotient_summary"] is True
    assert controls["uses_clock_duration_or_finality_status"] is False
    assert controls["imports_rg_or_conformal_mechanism"] is False


def test_reachability_quotient_is_stable_under_subdivision_and_relabeling():
    result = run()
    fixtures = result["quotient_probe"]["fixture_summaries"]

    connected = fixtures["connected_original"]["quotient_signature"]
    assert connected == (("source_target_component", 4),)
    assert fixtures["connected_subdivided_once"]["quotient_signature"] == connected
    assert fixtures["connected_subdivided_twice"]["quotient_signature"] == connected
    assert fixtures["connected_relabel"]["quotient_signature"] == connected

    partitioned = fixtures["partitioned_original"]["quotient_signature"]
    assert partitioned == (
        ("source_side_component", 2),
        ("target_side_component", 2),
    )
    assert fixtures["partitioned_subdivided_once"]["quotient_signature"] == partitioned
    assert fixtures["partitioned_subdivided_twice"]["quotient_signature"] == partitioned
    assert connected != partitioned


def test_size_path_and_hop_bands_are_refinement_artifacts():
    result = run()
    fixtures = result["quotient_probe"]["fixture_summaries"]
    controls = result["quotient_probe"]["controls"]

    assert controls["component_size_changes_under_iterated_refinement"] is True
    assert controls["path_length_changes_under_iterated_refinement"] is True
    assert controls["hop_band_changes_under_iterated_refinement"] is True

    assert fixtures["connected_original"]["component_size_signature"] == (
        ("family", 4),
        ("individual", 4),
        ("institution", 4),
        ("lab", 4),
    )
    assert fixtures["connected_subdivided_once"]["component_size_signature"] == (
        ("family", 7),
        ("individual", 7),
        ("institution", 7),
        ("lab", 7),
    )
    assert fixtures["connected_subdivided_twice"]["component_size_signature"] == (
        ("family", 13),
        ("individual", 13),
        ("institution", 13),
        ("lab", 13),
    )
    assert fixtures["connected_original"]["source_target_path_length"] == 3
    assert fixtures["connected_subdivided_once"]["source_target_path_length"] == 6
    assert fixtures["connected_subdivided_twice"]["source_target_path_length"] == 12
    assert fixtures["connected_original"]["source_target_hop_band"] == "short"
    assert fixtures["connected_subdivided_once"]["source_target_hop_band"] == "middle"
    assert fixtures["connected_subdivided_twice"]["source_target_hop_band"] == "long"


def test_reachability_quotient_packet_is_admitted_only_as_bookkeeping():
    result = run()
    packet = _candidate(result, "reachability_quotient_packet")

    assert packet["admitted"] is True
    assert packet["decision"] == "admit_reachability_quotient_no_scale_structure"
    assert (
        packet["route_label"]
        == "REACHABILITY_QUOTIENT_BOOKKEEPING_ADMITTED_NO_SCALE_STRUCTURE"
    )
    assert packet["uses_reachability_quotient"] is True
    assert packet["blockers"] == []
    assert result["admitted_candidate_ids"] == ["reachability_quotient_packet"]


def test_component_count_is_absorbed_as_quotient_summary():
    result = run()
    packet = _candidate(result, "component_count_summary")

    assert packet["admitted"] is False
    assert packet["decision"] == "absorb_quotient_summary_no_independent_generator"
    assert packet["route_label"] == "QUOTIENT_SUMMARY_ABSORBED"
    assert "component_count_derived_from_reachability_quotient" in packet["blockers"]


def test_refinement_variant_scale_readings_are_blocked():
    result = run()
    component_size = _candidate(result, "component_size_invariant_scale")
    path_length = _candidate(result, "shortest_path_invariant_scale")
    hop_band = _candidate(result, "finite_hop_band_scale")
    relay_count = _candidate(result, "relay_count_internal_clock")

    assert component_size["admitted"] is False
    assert component_size["decision"] == "reject_refinement_variant"
    assert "component_size_refinement_variant" in component_size["blockers"]

    assert path_length["admitted"] is False
    assert path_length["decision"] == "reject_refinement_variant"
    assert "path_length_refinement_variant" in path_length["blockers"]

    assert hop_band["admitted"] is False
    assert hop_band["decision"] == "reject_refinement_variant"
    assert "hop_band_refinement_variant" in hop_band["blockers"]

    assert relay_count["admitted"] is False
    assert relay_count["decision"] == "reject_refinement_variant"
    assert "relay_count_is_refinement_artifact" in relay_count["blockers"]
    assert "clock_duration_or_arrow_overread" in relay_count["blockers"]


def test_finality_rg_and_promotion_overreads_are_blocked():
    result = run()
    quotient_scale = _candidate(result, "quotient_as_internal_scale_structure")
    finality = _candidate(result, "reachability_finality_status")
    rg = _candidate(result, "rg_conformal_morphism_class_import")
    promotion = _candidate(result, "promotion_shortcut_quotient")

    assert quotient_scale["admitted"] is False
    assert "reachability_quotient_not_internal_scale_structure" in quotient_scale["blockers"]

    assert finality["admitted"] is False
    assert "record_finality_change_overread" in finality["blockers"]

    assert rg["admitted"] is False
    assert "rg_or_conformal_mechanism_imported" in rg["blockers"]
    assert "scale_genesis_or_physics_claim_overread" in rg["blockers"]
    assert "no_local_taf_anchor" in rg["blockers"]

    assert promotion["admitted"] is False
    assert "claim_or_public_posture_promotion_shortcut" in promotion["blockers"]
    assert "reachability_quotient_not_internal_scale_structure" in promotion["blockers"]


def test_future_packet_minimum_preserves_invariant_quotient_guards():
    result = run()

    assert result["hostile_violations"] == []
    assert (
        "declare the topology morphism or refinement class before using topology as a generator"
        in result["future_packet_minimum"]
    )
    assert (
        "quotient relay/refinement artifacts away from original observer-site reachability"
        in result["future_packet_minimum"]
    )
    assert "independent internal scale structure" in result["not_earned"]
    assert "record clock" in result["not_earned"]
    assert "record-finality change" in result["not_earned"]
    assert "scale-genesis theorem" in result["not_earned"]
