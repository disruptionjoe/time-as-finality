"""Tests for T495 bounded-record retrieval bottleneck gate."""

from __future__ import annotations

import json

from models import bounded_record_retrieval_bottleneck_gate as t495


def _scenario(payload, scenario_id):
    return next(
        item
        for item in payload["scenario_evaluations"]
        if item["scenario_id"] == scenario_id
    )


def _reading(payload, reading_id):
    return next(
        item
        for item in payload["reading_evaluations"]
        if item["reading_id"] == reading_id
    )


def test_artifact_identity_and_scope():
    payload = t495.run()

    assert payload["artifact"] == t495.ARTIFACT
    assert payload["overall_verdict"]["verdict"] == t495.VERDICT
    assert payload["stream_space"]["stream_count"] == 32
    assert payload["overall_verdict"]["all_scenarios_matched_expected"] is True
    assert payload["overall_verdict"]["retention_axis_only"] is True
    assert "Finite capability-audit toy only" in payload["honest_ceiling"]


def test_full_history_factors_arbitrary_retrieval():
    payload = t495.run()
    full = _scenario(payload, "full_history_arbitrary_retrieval_control")

    assert full["factorizes"] is True
    assert full["label"] == "PRESERVATION_CONTROL_PASSED"
    assert full["projection_class_count"] == 32
    assert full["capability_class_count"] == 32
    assert full["max_capability_spread"] == 1
    assert full["example_collision"] is None


def test_last2_state_detects_arbitrary_retrieval_bottleneck():
    payload = t495.run()
    last2 = _scenario(payload, "last2_state_arbitrary_retrieval_bottleneck")

    assert last2["factorizes"] is False
    assert last2["label"] == "BOTTLENECK_DETECTED_AS_EXPECTED"
    assert last2["projection_class_count"] == 4
    assert last2["capability_class_count"] == 32
    assert last2["max_capability_spread"] == 8
    assert last2["non_singleton_fiber_count"] == 4
    assert last2["example_collision"] is not None


def test_bounded_summaries_pass_their_native_tasks():
    payload = t495.run()
    suffix = _scenario(payload, "last2_state_suffix_retrieval_control")
    parity = _scenario(payload, "parity_state_parity_task_control")

    assert suffix["factorizes"] is True
    assert suffix["max_capability_spread"] == 1
    assert parity["factorizes"] is True
    assert parity["projection_class_count"] == 2
    assert parity["capability_class_count"] == 2


def test_parity_summary_is_not_arbitrary_retrieval():
    payload = t495.run()
    parity = _scenario(payload, "parity_state_arbitrary_retrieval_bottleneck")

    assert parity["factorizes"] is False
    assert parity["label"] == "BOTTLENECK_DETECTED_AS_EXPECTED"
    assert parity["projection_class_count"] == 2
    assert parity["capability_class_count"] == 32
    assert parity["max_capability_spread"] == 16


def test_only_retention_axis_reading_is_admitted():
    payload = t495.run()
    retention = _reading(payload, "retention_axis_capability_probe")
    copyability = _reading(payload, "naive_attention_quantum_copyability_mapping")
    physics = _reading(payload, "physics_mechanism_import")
    theorem = _reading(payload, "complexity_theorem_shortcut")
    public = _reading(payload, "public_or_cross_repo_update_shortcut")

    assert retention["admitted"] is True
    assert retention["label"] == "ADMITTED_RETENTION_AXIS_CAPABILITY_PROBE"
    assert copyability["admitted"] is False
    assert copyability["label"] == "REJECTED_NAIVE_COPYABILITY_MAPPING"
    assert physics["label"] == "REJECTED_PHYSICS_MECHANISM_IMPORT"
    assert theorem["label"] == "REJECTED_COMPLEXITY_THEOREM_SHORTCUT"
    assert public["label"] == "BLOCKED_PUBLIC_OR_CROSS_REPO_UPDATE"


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t495.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t495.VERDICT in dumped
    forbidden = (
        "physics is literally a Transformer proved",
        "unknown quantum states are copyable",
        "Standard Model derived",
        "claim promotion follows",
        "public posture authorized",
        "cross-repo support proved",
    )
    for term in forbidden:
        assert term not in dumped
