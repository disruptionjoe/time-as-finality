"""Tests for T440: ideal-limit / sector-lock routing gate."""

import json

from models import ideal_limit_sector_lock_routing_gate as t440


def artifact():
    return t440.run()


def classification(packet_id):
    return next(
        item for item in artifact()["classifications"] if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t440.ARTIFACT
    assert result["sources"]["t439_routing_obligation"].endswith(
        "T439-finite-time-catalytic-thermo-witness-gate-v0.1-results.md"
    )
    assert result["sources"]["t168_sector_screen"].endswith(
        "h7-sector-restriction-screen-v0.1-results.md"
    )
    assert result["sources"]["n14_sector_gauge_absorber"].endswith(
        "N14-h7-sector-gauge-absorber.md"
    )
    assert result["sources"]["t436_resource_lift_classifier"].endswith(
        "T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
    )
    assert "routing gate only" in result["honest_ceiling"]


def test_infinite_barrier_exact_sector_and_gauge_relabel_are_not_h7_evidence():
    infinite = classification("infinite_barrier_single_instance")
    sector = classification("exact_sector_local_ban")
    relabel = classification("gauge_relabel_lock")

    assert infinite["label"] == "H7_NULL_INFINITE_BARRIER_IDEALIZATION"
    assert sector["label"] == "H7_NULL_EXACT_SECTOR_STIPULATION"
    assert relabel["label"] == "H7_NULL_GAUGE_REPRESENTATIVE_CHANGE"
    assert all(not item["admitted_for_future_review"] for item in (infinite, sector, relabel))


def test_reservoirs_reference_frames_and_finite_controls_absorb_sector_locks():
    reservoir = classification("compensating_reservoir_sector")
    reference = classification("reference_frame_lifted_phase_lock")
    finite_control = classification("finite_symmetry_enforcement")

    assert reservoir["label"] == "E0_DECLARED_BY_RESERVOIR_OR_REFERENCE_COMPLETION"
    assert reference["label"] == "E0_DECLARED_BY_RESERVOIR_OR_REFERENCE_COMPLETION"
    assert reservoir["route"] == "e0_resource_completion"
    assert reference["route"] == "e0_resource_completion"
    assert finite_control["label"] == "ABSORBED_BY_FINITE_CONTROL_OR_KINETICS"
    assert finite_control["route"] == "absorbed"


def test_post_hoc_and_incomplete_e1_packets_are_rejected():
    selector = classification("post_hoc_idealization_selector")
    incomplete = classification("incomplete_e1_limit_packet")
    single = classification("single_instance_e1_overread")

    assert selector["label"] == "REJECTED_POST_HOC_IDEALIZATION_SELECTOR"
    assert incomplete["label"] == "REJECTED_INCOMPLETE_E1_LIMIT_PACKET"
    assert single["label"] == "REJECTED_E1_CANNOT_BE_SINGLE_INSTANCE"
    assert all(not item["admitted_for_future_review"] for item in (selector, incomplete, single))


def test_e1_family_limit_synthetic_control_is_future_review_only():
    item = classification("e1_family_limit_synthetic_control")

    assert item["admitted_for_future_review"] is True
    assert item["route"] == "e1_family_limit_review"
    assert item["label"] == "ADMITTED_E1_IDEAL_LIMIT_REVIEW_NO_PROMOTION"
    assert item["packet"]["synthetic_e1_control"] is True
    assert "future E1 review" in item["reason"]


def test_a2_resource_lift_blocks_overreading_a1_as_e3():
    item = classification("a2_lift_absorbs_sector_lock")

    assert item["route"] == "e0_resource_completion"
    assert item["label"] == "E0_DECLARED_AFTER_A2_RESOURCE_LIFT"
    assert item["admitted_for_future_review"] is False


def test_e3_exact_no_go_synthetic_control_is_future_review_only():
    item = classification("e3_exact_no_go_synthetic_control")

    assert item["admitted_for_future_review"] is True
    assert item["route"] == "e3_exact_no_go_review"
    assert item["label"] == "ADMITTED_E3_EXACT_NO_GO_REVIEW_NO_PROMOTION"
    assert item["packet"]["synthetic_e3_control"] is True
    assert "future E3 review" in item["reason"]


def test_overall_verdict_keeps_h7_claims_and_public_posture_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t440.VERDICT
    assert verdict["admitted_packet_ids"] == [
        "e1_family_limit_synthetic_control",
        "e3_exact_no_go_synthetic_control",
    ]
    assert verdict["synthetic_controls_only"] is True
    assert verdict["h7_promotion"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "E1 theorem proved",
        "E3 theorem proved",
        "WAY proved",
        "public posture authorized",
        "claim promotion follows",
    )
    assert all(term not in combined for term in banned)
