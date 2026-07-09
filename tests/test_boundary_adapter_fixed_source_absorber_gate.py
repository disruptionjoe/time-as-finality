"""Tests for T512 boundary-adapter fixed-source absorber gate."""

from __future__ import annotations

import json

from models import boundary_adapter_fixed_source_absorber_gate as t512


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t512.run()

    assert payload["artifact_id"] == t512.ARTIFACT_ID
    assert payload["verdict"] == t512.VERDICT
    overall = payload["overall"]
    assert overall["claim_movement"] is False
    assert overall["public_posture_movement"] is False
    assert overall["external_publication"] is False
    assert overall["cross_repo_truth_movement"] is False
    assert overall["real_adapter_claim_earned"] is False
    assert overall["source_crossing_claim_earned"] is False
    assert overall["physics_claim_earned"] is False


def test_predeclared_nonfixed_source_packet_is_review_only():
    payload = t512.run()
    decision = _decision(payload, "predeclared_nonfixed_source_review_target")

    assert decision["admitted"] is True
    assert decision["label"] == "ADMITTED_NONFIXED_SOURCE_REVIEW_TARGET"
    assert decision["review_target_only"] is True
    assert decision["fixed_source_absorber_tested"] is True
    assert decision["fixed_source_absorbs"] is False
    assert decision["undo_handle_admissible"] is False
    assert decision["ledger_conserved"] is True
    assert decision["missing_requirements"] == []
    assert payload["overall"]["review_target_admitted"] is True


def test_fixed_source_containment_and_generation_are_absorbers():
    payload = t512.run()
    disclosure = _decision(payload, "fixed_source_disclosure_control")
    generation = _decision(payload, "fixed_source_generation_control")

    assert disclosure["label"] == "ABSORBED_BY_FIXED_SOURCE_DISCLOSURE"
    assert disclosure["fixed_source_absorbs"] is True
    assert payload["overall"]["fixed_source_disclosure_absorbed"] is True
    assert generation["label"] == "ABSORBED_BY_FIXED_SOURCE_GENERATION"
    assert generation["fixed_source_absorbs"] is True
    assert payload["overall"]["fixed_source_generation_absorbed"] is True


def test_posthoc_and_missing_source_inventory_are_rejected():
    payload = t512.run()
    posthoc = _decision(payload, "posthoc_source_inventory_shortcut")
    missing = _decision(payload, "missing_source_inventory_shortcut")

    assert posthoc["label"] == "REJECTED_POSTHOC_SOURCE_COMPLETION"
    assert posthoc["posthoc_source_completion"] is True
    assert "predeclared fixed source inventory" in posthoc["missing_requirements"]
    assert payload["overall"]["posthoc_source_completion_rejected"] is True
    assert missing["label"] == "REJECTED_MISSING_FIXED_SOURCE_ABSORBER"
    assert missing["fixed_source_absorber_tested"] is False
    assert "fixed richer source inventory" in missing["missing_requirements"]
    assert payload["overall"]["missing_source_inventory_rejected"] is True


def test_admissible_undo_handle_and_source_crossing_language_are_rejected():
    payload = t512.run()
    undo = _decision(payload, "admissible_undo_handle_control")
    source = _decision(payload, "source_crossing_language_shortcut")

    assert undo["label"] == "REJECTED_HANDLE_ADMISSIBLE_NOT_FINAL"
    assert undo["undo_handle_admissible"] is True
    assert payload["overall"]["admissible_handle_rejected"] is True
    assert source["label"] == "REJECTED_SOURCE_CROSSING_NOT_ABSORBER_TEST"
    assert source["source_crossing_claim_blocked"] is True
    assert "fixed richer source inventory" in source["missing_requirements"]
    assert "undo or readout handle" in source["missing_requirements"]
    assert payload["overall"]["source_crossing_language_blocked"] is True


def test_cross_repo_identity_shortcut_is_blocked():
    payload = t512.run()
    decision = _decision(payload, "cross_repo_identity_shortcut")

    assert decision["label"] == "BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT"
    assert decision["action"] == "stop"
    assert "claim_movement" in decision["blocked_shortcuts"]
    assert "cross_repo_truth_movement" in decision["blocked_shortcuts"]
    assert payload["overall"]["cross_repo_shortcut_blocked"] is True


def test_future_minimum_and_not_earned_are_explicit():
    payload = t512.run()
    minimum = set(payload["future_packet_minimum"])
    blocked = set(payload["not_earned"])

    assert "predeclare the fixed richer source inventory before choosing the witness" in minimum
    assert "state whether predeclared source generators can form the candidate record" in minimum
    assert "block post-hoc source completion and cross-repo identity shortcuts" in minimum
    assert "source crossing" in blocked
    assert "real GU/TaF/TI boundary adapter" in blocked
    assert "cross-repo truth movement" in blocked


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t512.run()
    rendered = json.dumps(payload, sort_keys=True)

    assert t512.VERDICT in rendered
    forbidden = (
        "source crossing established",
        "GU support established",
        "claim promotion follows",
        "public posture authorized",
        "cross-repo truth established",
    )
    for phrase in forbidden:
        assert phrase not in rendered
