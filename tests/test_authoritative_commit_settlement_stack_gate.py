"""Tests for T498 authoritative commit / settlement composite stack gate."""

from __future__ import annotations

import json

from models import authoritative_commit_settlement_stack_gate as t498


def _row(payload, projection, capability):
    return next(
        item
        for item in payload["projection_evaluations"]
        if item["projection_label"] == projection and item["capability_label"] == capability
    )


def _decision(payload, reading_id):
    return next(item for item in payload["reading_decisions"] if item["reading_id"] == reading_id)


def test_artifact_identity_and_scope():
    payload = t498.run()

    assert payload["artifact"] == t498.ARTIFACT
    assert payload["verdict"] == t498.VERDICT
    assert payload["source_t496"] == t498.SOURCE_T496
    assert payload["source_t497"] == t498.SOURCE_T497
    assert payload["source_progress_lanes"] == t498.SOURCE_PROGRESS_LANES
    assert payload["overall"]["review_target_only"] is True
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert "does not prove Time as Finality" in payload["honest_ceiling"]


def test_same_local_marker_has_settlement_capability_spread():
    payload = t498.run()
    row = _row(payload, "local_visible", "authoritative_settlement")

    assert row["factorizes"] is False
    assert row["projection_class_count"] == 1
    assert row["capability_class_count"] == 4
    assert row["max_capability_spread"] == 4
    assert row["label"] == "EXPECTED_SETTLEMENT_STACK_BEHAVIOR"


def test_local_marker_still_factors_native_display_task():
    payload = t498.run()
    row = _row(payload, "local_visible", "local_display")

    assert row["factorizes"] is True
    assert row["max_capability_spread"] == 1
    assert row["label"] == "EXPECTED_SETTLEMENT_STACK_BEHAVIOR"


def test_untrusted_client_claim_does_not_restore_settlement_factorization():
    payload = t498.run()
    row = _row(payload, "client_claim_only", "authoritative_settlement")

    assert row["factorizes"] is False
    assert row["projection_class_count"] == 1
    assert row["max_capability_spread"] == 4


def test_authority_completion_restores_settlement_factorization():
    payload = t498.run()
    ledger = _row(payload, "ledger_server_completion", "authoritative_settlement")
    full = _row(payload, "full_authority_completion", "authoritative_settlement")

    for row in (ledger, full):
        assert row["factorizes"] is True
        assert row["max_capability_spread"] == 1
        assert row["label"] == "EXPECTED_SETTLEMENT_STACK_BEHAVIOR"


def test_absorber_stack_names_completion_rights_and_authority_state():
    payload = t498.run()
    absorber_ids = {absorber["absorber_id"] for absorber in payload["absorber_stack"]}

    assert "server_verdict_completion" in absorber_ids
    assert "ledger_log_completion" in absorber_ids
    assert "rollback_reconciliation_rule" in absorber_ids
    assert "explicit_completion_rights" in absorber_ids
    assert payload["overall"]["all_projection_checks_expected"] is True


def test_only_composite_explanation_reading_is_admitted():
    payload = t498.run()

    admitted = _decision(payload, "authoritative_commit_composite_explanation")
    local_residue = _decision(payload, "local_marker_as_finality_residual")
    metaphor = _decision(payload, "distributed_systems_metaphor_proves_taf")
    claim = _decision(payload, "claim_or_public_posture_shortcut")
    external = _decision(payload, "external_or_cross_repo_shortcut")

    assert admitted["admitted"] is True
    assert admitted["label"] == "ADMITTED_COMPOSITE_ABSORBER_EXPLANATION"
    assert local_residue["label"] == "REJECTED_UNDERDESCRIBED_LOCAL_PROJECTION"
    assert metaphor["label"] == "REJECTED_DISTRIBUTED_SYSTEMS_METAPHOR"
    assert claim["label"] == "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT"
    assert external["label"] == "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT"


def test_payload_json_and_forbidden_overreads_absent():
    payload = t498.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t498.VERDICT in dumped
    forbidden = (
        "claim promotion follows",
        "public posture authorized",
        "cross-repo truth proved",
        "Time as Finality proved",
        "physics mechanism earned",
    )
    for term in forbidden:
        assert term not in dumped
