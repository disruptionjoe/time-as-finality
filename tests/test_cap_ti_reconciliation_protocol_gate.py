"""Tests for T513 Cap_TI reconciliation protocol gate."""

from __future__ import annotations

import json

from models import cap_ti_reconciliation_protocol_gate as t513


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t513.run()

    assert payload["artifact_id"] == t513.ARTIFACT_ID
    assert payload["verdict"] == t513.VERDICT
    overall = payload["overall"]
    assert overall["claim_movement"] is False
    assert overall["h7_promotion"] is False
    assert overall["temporal_issuance_source_truth"] is False
    assert overall["cross_repo_truth_movement"] is False
    assert overall["external_publication"] is False
    assert overall["public_posture_movement"] is False
    assert overall["north_star_movement"] is False
    assert overall["roadmap_movement"] is False


def test_round_formula_and_capacity_are_discretized():
    assert t513.expected_protocol_rounds(64, 0.75) == 3
    assert t513.expected_protocol_rounds(64, 0.50) == 8
    assert t513.hierarchy_capacity(64, 0.75) == 23
    assert t513.hierarchy_capacity(64, 0.50) == 8


def test_higher_beta_protocol_requires_fewer_rounds_under_matched_freeze():
    payload = t513.run()
    high = _decision(payload, "hierarchical_protocol_high_beta")
    low = _decision(payload, "hierarchical_protocol_low_beta")

    assert high["admitted"] is True
    assert low["admitted"] is True
    assert high["label"] == "ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET"
    assert low["label"] == "ADMITTED_PROTOCOL_GROUNDING_REVIEW_TARGET"
    assert high["measured_rounds"] == high["expected_rounds"]
    assert low["measured_rounds"] == low["expected_rounds"]
    assert high["measured_rounds"] < low["measured_rounds"]
    assert payload["overall"]["high_beta_fewer_rounds"] is True


def test_same_beta_null_controls_match_rounds():
    payload = t513.run()
    a = _decision(payload, "same_beta_null_control_a")
    b = _decision(payload, "same_beta_null_control_b")

    assert a["admitted"] is True
    assert b["admitted"] is True
    assert a["expected_rounds"] == b["expected_rounds"]
    assert a["measured_rounds"] == b["measured_rounds"]
    assert payload["overall"]["same_beta_null_same_rounds"] is True


def test_formula_only_topology_only_posthoc_and_hidden_timing_are_rejected():
    payload = t513.run()
    formula = _decision(payload, "formula_only_shortcut")
    topology = _decision(payload, "topology_only_shortcut")
    posthoc = _decision(payload, "posthoc_beta_shortcut")
    hidden = _decision(payload, "hidden_timing_shortcut")

    assert formula["label"] == "REJECTED_FORMULA_ONLY_NOT_PROTOCOL"
    assert formula["formula_only_rejected"] is True
    assert "finite reconciliation protocol" in formula["missing_requirements"]
    assert topology["label"] == "ABSORBED_BY_TOPOLOGY_ONLY_NO_TIMING_METRIC"
    assert topology["topology_only_absorbed"] is True
    assert "timing metric" in topology["missing_requirements"]
    assert posthoc["label"] == "REJECTED_POSTHOC_BETA"
    assert posthoc["posthoc_beta_rejected"] is True
    assert hidden["label"] == "REJECTED_HIDDEN_TIMING_SHORTCUT"
    assert hidden["hidden_timing_rejected"] is True


def test_round_mismatch_and_governance_shortcuts_are_blocked():
    payload = t513.run()
    mismatch = _decision(payload, "round_mismatch_control")
    blocked = _decision(payload, "promotion_or_cross_repo_shortcut")

    assert mismatch["label"] == "REJECTED_PROTOCOL_ROUND_MISMATCH"
    assert mismatch["measured_rounds"] != mismatch["expected_rounds"]
    assert payload["overall"]["round_mismatch_rejected"] is True
    assert blocked["label"] == "BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT"
    assert blocked["action"] == "stop"
    assert "claim_movement" in blocked["blocked_shortcuts"]
    assert "h7_promotion" in blocked["blocked_shortcuts"]
    assert "temporal_issuance_source_truth" in blocked["blocked_shortcuts"]
    assert "cross_repo_truth_movement" in blocked["blocked_shortcuts"]
    assert payload["overall"]["governance_shortcut_blocked"] is True


def test_future_minimum_and_not_earned_are_explicit():
    payload = t513.run()
    minimum = set(payload["future_packet_minimum"])
    blocked = set(payload["not_earned"])

    assert "predeclare beta and its timing metric before pair selection" in minimum
    assert "declare hierarchy capacity as ceil(n^beta)" in minimum
    assert "include same-beta null controls" in minimum
    assert "Cap_TI promotion" in blocked
    assert "Temporal Issuance source truth" in blocked
    assert "cross-repo truth movement" in blocked


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t513.run()
    rendered = json.dumps(payload, sort_keys=True)

    assert t513.VERDICT in rendered
    forbidden = (
        "Cap_TI promoted",
        "H7 support established",
        "Temporal Issuance source truth established",
        "claim promotion follows",
        "cross-repo truth established",
    )
    for phrase in forbidden:
        assert phrase not in rendered
