"""Tests for T463: post-T462 H7/E1 restart router."""

import json

from models import post_t462_h7_e1_restart_router as t463


def artifact():
    return t463.run()


def evaluation(proposal_id):
    return next(
        item
        for item in artifact()["proposal_evaluations"]
        if item["proposal_id"] == proposal_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t463.ARTIFACT
    assert result["sources"]["h7_handoff"].endswith(
        "h7-physical-deletion-substrate-handoff.md"
    )
    assert result["sources"]["t462_h7_absorber"].endswith(
        "T462-h7-physical-deletion-overread-absorber-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == (
        "none; no claim promotion or demotion"
    )
    assert "Routing/admission gate only" in result["honest_ceiling"]


def test_t462_import_keeps_h7_closed_and_synthetic_only():
    result = artifact()
    imported = result["t462_import_summary"]

    assert imported["verdict"] == t463.t462.VERDICT
    assert imported["all_h7_reopened_flags_false"] is True
    assert imported["synthetic_positive_controls_only"] is True
    assert imported["h7_promotion"].startswith("none")
    assert imported["physical_deletion_evidence"].startswith("none")
    assert result["overall_verdict"]["all_h7_reopened_flags_false"] is True


def test_restart_requirements_name_the_full_h7_burden():
    requirements = artifact()["restart_requirements"]

    assert "reverse edge typed as physical_record_deletion" in requirements
    assert "named physical substrate" in requirements
    assert "full T462 H7 object frozen before scoring" in requirements
    assert "T462 absorber cleared" in requirements
    assert "real substrate evidence before evidential reading" in requirements
    assert "no current T461/T462 minor variation" in requirements


def test_t461_and_t462_variations_do_not_reopen_h7():
    local = evaluation("t461_locality_depth_reopen_attempt")
    synthetic = evaluation("t462_full_burden_without_real_substrate")

    assert local["gate_label"] == "CLOSED_T461_T462_VARIATION_DO_NOT_REOPEN_H7"
    assert local["router_action"] == "do_not_reopen"
    assert local["admitted_future_target"] is False
    assert local["h7_reopened"] is False

    assert synthetic["gate_label"] == "CLOSED_T461_T462_VARIATION_DO_NOT_REOPEN_H7"
    assert synthetic["router_action"] == "do_not_reopen"
    assert synthetic["admitted_future_target"] is False
    assert synthetic["h7_reopened"] is False


def test_adjacent_mode_candidates_route_to_existing_gates():
    e1 = evaluation("new_e1_family_limit_candidate")
    e2 = evaluation("new_e2_hardness_candidate")
    e3 = evaluation("new_e3_exact_no_go_candidate")
    finite = evaluation("finite_time_catalytic_candidate")
    ideal = evaluation("ideal_sector_lock_candidate")

    assert e1["gate_label"] == "ROUTE_TO_T441_E1_FAMILY_LIMIT_GATE"
    assert e1["router_action"] == "route_to_T441"

    assert e2["gate_label"] == "ROUTE_TO_T438_T444_T451_E2_GATES"
    assert e2["router_action"] == "route_to_T438_T444_T451"

    assert e3["gate_label"] == "ROUTE_TO_T440_T436_T447_E3_RESOURCE_LIFT_GATES"
    assert e3["router_action"] == "route_to_T440_T436_T447"

    assert finite["gate_label"] == "ROUTE_TO_T439_FINITE_TIME_CATALYTIC_GATE"
    assert finite["router_action"] == "route_to_T439"

    assert ideal["gate_label"] == "ROUTE_TO_T440_T168_IDEAL_OR_SECTOR_ABSORBER"
    assert ideal["router_action"] == "route_to_T440_T168"

    assert all(
        item["admitted_future_target"] is False
        for item in (e1, e2, e3, finite, ideal)
    )


def test_h7_substrate_shape_failures_do_not_admit():
    access = evaluation("access_revocation_reopen_attempt")
    name_only = evaluation("substrate_name_only_packet")
    uncleared = evaluation("full_object_not_absorber_cleared")
    missing_controls = evaluation("full_object_missing_negative_controls")

    assert access["gate_label"] == "REJECTED_NOT_PHYSICAL_RECORD_DELETION"
    assert "reverse_edge_typed_physical_record_deletion" in access[
        "missing_requirements"
    ]

    assert name_only["gate_label"] == "ROUTE_TO_T462_FULL_OBJECT_CHECK"
    assert "full_h7_object_frozen" in name_only["missing_requirements"]

    assert uncleared["gate_label"] == "ROUTE_TO_T462_ABSORBER_BEFORE_RESTART"
    assert "clears_t462_absorber" in uncleared["missing_requirements"]

    assert missing_controls["gate_label"] == "REJECTED_NO_NEGATIVE_CONTROLS"
    assert "negative_controls_declared" in missing_controls["missing_requirements"]

    assert all(
        item["admitted_future_target"] is False
        for item in (access, name_only, uncleared, missing_controls)
    )


def test_cross_repo_external_and_promotion_shortcuts_block():
    cross_repo = evaluation("cross_repo_support_shortcut")
    external = evaluation("external_substrate_investigation_shortcut")
    promotion = evaluation("claim_promotion_shortcut")

    assert cross_repo["gate_label"] == "BLOCKED_CROSS_REPO_TRUTH_REQUEST"
    assert external["gate_label"] == "BLOCKED_EXTERNAL_ACTION_REQUIRED"
    assert promotion["gate_label"] == "BLOCKED_CLAIM_PROMOTION_REQUEST"

    assert all(
        item["router_action"] == "stop"
        for item in (cross_repo, external, promotion)
    )


def test_only_full_burden_targets_are_admitted_without_h7_reopening():
    synthetic = evaluation("synthetic_full_burden_restart_target")
    future = evaluation("future_named_substrate_review_packet")
    verdict = artifact()["overall_verdict"]

    assert synthetic["gate_label"] == (
        "ADMITTED_SYNTHETIC_FULL_BURDEN_TARGET_NO_REOPENING"
    )
    assert synthetic["router_action"] == "record_synthetic_future_target"
    assert synthetic["admitted_future_target"] is True
    assert synthetic["h7_reopened"] is False

    assert future["gate_label"] == (
        "ADMITTED_NAMED_SUBSTRATE_REVIEW_TARGET_NO_PROMOTION"
    )
    assert future["router_action"] == "admit_future_h7_review_target"
    assert future["admitted_future_target"] is True
    assert future["h7_reopened"] is False

    assert verdict["admitted_future_target_ids"] == [
        "synthetic_full_burden_restart_target",
        "future_named_substrate_review_packet",
    ]
    assert verdict["actual_substrate_packets_admitted_now"] == []
    assert verdict["admitted_targets_are_synthetic_or_future_only"] is True


def test_overall_verdict_records_no_claim_or_evidence_movement():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t463.VERDICT
    assert verdict["h7_promotion"] == "none; T463 is a router only"
    assert verdict["physical_deletion_evidence"].startswith("none in this run")
    assert verdict["claim_ledger_update"] == "none; no claim promotion or demotion"
    assert verdict["all_h7_reopened_flags_false"] is True


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "physical deletion proved",
        "thermodynamic arrow proved",
        "E1 theorem proved",
        "E2 theorem proved",
        "E3 theorem proved",
        "public posture authorized",
        "claim promotion follows",
        "cross-repo support proved",
    )
    assert all(term not in combined for term in banned)
