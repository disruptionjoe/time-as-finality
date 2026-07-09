"""Tests for T511 boundary-adapter finality gate."""

from __future__ import annotations

import json

from models import boundary_adapter_finality_gate as t511


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t511.run()

    assert payload["artifact_id"] == t511.ARTIFACT_ID
    assert payload["verdict"] == t511.VERDICT
    assert payload["source_intake"] == t511.SOURCE_INTAKE
    assert payload["source_guardrail"] == t511.SOURCE_GUARDRAIL
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert payload["overall"]["external_publication"] is False
    assert payload["overall"]["cross_repo_truth_movement"] is False
    assert payload["overall"]["sibling_repo_inspection"] is False
    assert payload["overall"]["gu_support_earned"] is False
    assert payload["overall"]["temporal_issuance_support_earned"] is False
    assert payload["overall"]["universal_ledger_claimed"] is False


def test_inadmissible_handle_conserved_ledger_is_review_target_only():
    payload = t511.run()
    decision = _decision(payload, "inadmissible_handle_conserved_ledger")

    assert decision["admitted"] is True
    assert decision["label"] == "ADMITTED_ADAPTER_FINALITY_REVIEW_TARGET"
    assert decision["review_target_only"] is True
    assert decision["undo_handle_admissible"] is False
    assert decision["readout_handle_admissible"] is False
    assert decision["ledger_conserved"] is True
    assert decision["missing_requirements"] == []
    assert payload["overall"]["positive_review_target_admitted"] is True


def test_admissible_undo_handle_blocks_finality():
    payload = t511.run()
    decision = _decision(payload, "admissible_undo_handle_control")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL"
    assert decision["undo_handle_admissible"] is True
    assert decision["ledger_conserved"] is True
    assert payload["overall"]["admissible_handle_rejected"] is True


def test_absent_handle_is_not_inadmissibility():
    payload = t511.run()
    decision = _decision(payload, "absent_handle_prose_shortcut")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_HANDLE_ABSENT_NOT_INADMISSIBLE"
    assert "handle inadmissibility proof" in decision["missing_requirements"]
    assert payload["overall"]["absent_handle_rejected"] is True


def test_ledger_drift_and_missing_fixed_source_absorber_are_rejected():
    payload = t511.run()
    drift = _decision(payload, "ledger_drift_control")
    missing_absorber = _decision(payload, "fixed_source_absorber_missing")

    assert drift["admitted"] is False
    assert drift["label"] == "REJECTED_LEDGER_DRIFT"
    assert drift["ledger_conserved"] is False
    assert "conserved ledger or invariant" in drift["missing_requirements"]
    assert payload["overall"]["drifting_ledger_rejected"] is True

    assert missing_absorber["admitted"] is False
    assert missing_absorber["label"] == "REJECTED_FIXED_SOURCE_ABSORBER_UNTESTED"
    assert "fixed-richer-source absorber" in missing_absorber["missing_requirements"]
    assert payload["overall"]["fixed_source_absorber_required"] is True


def test_boundary_supply_and_source_crossing_are_not_finality_by_themselves():
    payload = t511.run()
    boundary = _decision(payload, "boundary_supply_only")
    source = _decision(payload, "source_crossing_language_only")

    assert boundary["admitted"] is False
    assert boundary["label"] == "REJECTED_BOUNDARY_SUPPLY_NOT_FINALITY"
    assert "undo or readout handle" in boundary["missing_requirements"]
    assert payload["overall"]["boundary_supply_only_rejected"] is True

    assert source["admitted"] is False
    assert source["label"] == "REJECTED_SOURCE_CROSSING_NOT_TAF_FINALITY"
    assert "ledger or invariant" in source["missing_requirements"]
    assert payload["overall"]["source_crossing_only_rejected"] is True


def test_cross_repo_identity_shortcut_is_blocked():
    payload = t511.run()
    decision = _decision(payload, "cross_repo_identity_shortcut")

    assert decision["admitted"] is False
    assert decision["label"] == "BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT"
    assert decision["action"] == "stop"
    assert "claim_movement" in decision["blocked_shortcuts"]
    assert "cross_repo_truth_movement" in decision["blocked_shortcuts"]


def test_future_packet_minimum_and_not_earned_are_explicit():
    payload = t511.run()
    minimum = set(payload["future_packet_minimum"])
    blocked = set(payload["not_earned"])

    assert "declare the admissible operation/readout class before choosing the witness" in minimum
    assert "prove the handle is inadmissible rather than merely absent" in minimum
    assert "include fixed-richer-source disclosure as an absorber" in minimum
    assert "keep cross-repo identity and support claims gated" in minimum
    assert "real GU/TaF/TI boundary adapter" in blocked
    assert "physics-side irreversibility claim" in blocked
    assert "cross-repo truth movement" in blocked


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t511.run()
    rendered = json.dumps(payload, sort_keys=True)

    assert t511.VERDICT in rendered
    forbidden = (
        "GU/TaF/TI identity established",
        "claim promotion follows",
        "public posture authorized",
        "physical irreversibility proven",
        "cross-repo truth established",
    )
    for phrase in forbidden:
        assert phrase not in rendered
