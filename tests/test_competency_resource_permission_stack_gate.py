"""Tests for T500 competency/resource/permission/provenance stack gate."""

from __future__ import annotations

import json

from models import competency_resource_permission_stack_gate as t500


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t500.run()

    assert payload["artifact"] == t500.ARTIFACT
    assert payload["verdict"] == t500.VERDICT
    assert payload["sources"]["progress_lanes"] == t500.SOURCE_PROGRESS_LANES
    assert payload["sources"]["t493"] == t500.SOURCE_T493
    assert payload["stack_layers"] == list(t500.STACK_LAYERS)
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert "does not prove a new C(R) primitive" in payload["honest_ceiling"]


def test_current_c_r_full_stack_is_absorbed_as_composite_profile():
    payload = t500.run()
    row = _decision(payload, "current_t493_t494_c_r_full_stack")

    assert row["admitted"] is True
    assert row["label"] == "ABSORBED_BY_FULL_COMPETENCY_RESOURCE_PERMISSION_PROVENANCE_STACK"
    assert row["full_stack_complete"] is True
    assert row["residual_survives_full_stack"] is False
    assert row["missing_layers"] == ()
    assert payload["overall"]["current_c_r_full_stack_absorbed"] is True
    assert payload["overall"]["current_c_r_residual_survives_full_stack"] is False


def test_weak_single_layer_readings_are_rejected():
    payload = t500.run()
    single = _decision(payload, "single_success_statistic_reading")
    resource = _decision(payload, "resource_preorder_only")
    permission = _decision(payload, "permission_boundary_only")
    provenance = _decision(payload, "provenance_completion_only")

    assert single["label"] == "REJECTED_SINGLE_STATISTIC_NOT_FULL_STACK"
    assert resource["label"] == "REJECTED_INCOMPLETE_ABSORBER_STACK"
    assert permission["label"] == "REJECTED_INCOMPLETE_ABSORBER_STACK"
    assert provenance["label"] == "REJECTED_INCOMPLETE_ABSORBER_STACK"
    assert "full_competency_profile" in resource["missing_layers"]
    assert "resource_preorder" in permission["missing_layers"]
    assert "permission_lattice" in provenance["missing_layers"]


def test_synthetic_full_stack_residual_is_review_only():
    payload = t500.run()
    row = _decision(payload, "synthetic_full_stack_residual_packet")

    assert row["admitted"] is True
    assert row["label"] == "ADMITTED_FUTURE_REVIEW_TARGET_AFTER_FULL_STACK"
    assert row["action"] == "review_only"
    assert row["full_stack_complete"] is True
    assert row["residual_survives_full_stack"] is True
    assert payload["overall"]["synthetic_full_stack_residual_admitted_for_review"] is True
    assert payload["overall"]["review_target_only"] is True


def test_context_controls_and_mechanism_import_are_rejected():
    payload = t500.run()
    context = _decision(payload, "missing_region_menu_task_context")
    mechanism = _decision(payload, "external_mechanism_import")

    assert context["label"] == "REJECTED_UNDECLARED_REGION_MENU_TASK_CONTEXT"
    assert mechanism["label"] == "REJECTED_EXTERNAL_MECHANISM_IMPORT"
    assert context["admitted"] is False
    assert mechanism["admitted"] is False


def test_governance_and_external_shortcuts_are_blocked():
    payload = t500.run()
    posture = _decision(payload, "claim_public_posture_shortcut")
    external = _decision(payload, "external_or_cross_repo_shortcut")

    assert posture["label"] == "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT"
    assert external["label"] == "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT"
    assert posture["admitted"] is False
    assert external["admitted"] is False
    assert payload["overall"]["external_publication"] is False
    assert payload["overall"]["cross_repo_truth_movement"] is False


def test_payload_json_and_forbidden_overreads_absent():
    payload = t500.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t500.VERDICT in dumped
    forbidden = (
        "claim promotion follows",
        "region-indexed discriminator proved",
        "public posture authorized",
        "cross-repo truth proved",
        "Levin mechanism imported",
    )
    for term in forbidden:
        assert term not in dumped
