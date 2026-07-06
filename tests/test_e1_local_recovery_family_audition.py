"""Tests for T461: E1 local-recovery family audition."""

import json

from models import e1_local_recovery_family_audition as t461


def artifact():
    return t461.run()


def classification(family_id):
    return next(
        item
        for item in artifact()["classifications"]
        if item["family"]["family_id"] == family_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t461.ARTIFACT
    assert result["sources"]["t441_e1_family_gate"].endswith(
        "T441-e1-family-limit-packet-gate-v0.1-results.md"
    )
    assert result["sources"]["h7_handoff"].endswith(
        "h7-physical-deletion-substrate-handoff.md"
    )
    assert "E1 calibration only" in result["honest_ceiling"]


def test_main_nearest_neighbor_family_has_diverging_depth_and_passes_t441():
    item = classification("nearest_neighbor_endpoint_recovery_chain")

    assert item["recovery_depth_sequence"] == [2, 4, 8, 16]
    assert item["strictly_increasing_depth"] is True
    assert item["has_diverging_locality_witness"] is True
    assert item["t441_admitted_for_future_e1_review"] is True
    assert item["t441_label"] == "ADMITTED_E1_FAMILY_LIMIT_REVIEW_NO_PROMOTION"
    assert item["label"] == "E1_LOCALITY_CONTROL_ADMITTED_NO_H7_REOPENING"
    assert item["route"] == "admitted_as_e1_locality_control"
    assert item["h7_reopened"] is False


def test_finite_profiles_record_fixed_depth_recovery_boundary():
    item = classification("nearest_neighbor_endpoint_recovery_chain")
    profiles = item["finite_profiles"]

    assert [profile["scale"] for profile in profiles] == [2, 4, 8, 16]
    assert profiles[0]["recoverable_with_fixed_depth_budget"] is True
    assert all(
        profile["recoverable_with_fixed_depth_budget"] is False
        for profile in profiles[1:]
    )
    assert all(profile["operation_radius"] == 1 for profile in profiles)
    assert all(
        profile["region_shadow"] == "same observer endpoint and local radius"
        for profile in profiles
    )


def test_controls_fail_or_route_under_t441():
    expected = {
        "single_window_endpoint_recovery": "REJECTED_NO_FINITE_APPROXIMANT_MAP",
        "finite_barrier_metastable_recovery": "ABSORBED_BY_FINITE_KINETICS",
        "post_hoc_distance_selector": "REJECTED_POST_HOC_LIMIT_SELECTOR",
        "drifting_task_operation_family": (
            "REJECTED_UNSTABLE_TASK_OPERATION_OR_ACCOUNTING"
        ),
        "hidden_relay_resource_family": "REJECTED_CHANGED_RESOURCE_OR_BOUNDARY",
        "e2_hardness_labeled_recovery": "ROUTE_TO_E2_HARDNESS_GATE",
    }

    for family_id, t441_label in expected.items():
        item = classification(family_id)
        assert item["t441_label"] == t441_label
        assert item["route"] == "reject_or_route_by_t441"
        assert item["h7_reopened"] is False


def test_physical_deletion_overread_is_not_h7_reopening():
    item = classification("locality_family_claimed_as_deletion")

    assert item["t441_admitted_for_future_e1_review"] is True
    assert item["label"] == "E1_ADMITTED_BUT_H7_REQUIRES_DELETION_ABSORBER_AUDIT"
    assert item["route"] == "separate_h7_physical_deletion_review_required"
    assert item["h7_reopened"] is False
    assert "absorber stack" in item["reason"]


def test_overall_verdict_records_locality_control_without_claim_movement():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t461.VERDICT
    assert verdict["admitted_locality_control_ids"] == [
        "nearest_neighbor_endpoint_recovery_chain"
    ]
    assert verdict["deletion_overread_ids"] == ["locality_family_claimed_as_deletion"]
    assert verdict["all_h7_reopened_flags_false"] is True
    assert verdict["e1_theorem"].startswith("none")
    assert verdict["h7_promotion"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion or demotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "E1 theorem proved",
        "thermodynamic arrow proved",
        "physical deletion proved",
        "public posture authorized",
        "claim promotion follows",
    )
    assert all(term not in combined for term in banned)
