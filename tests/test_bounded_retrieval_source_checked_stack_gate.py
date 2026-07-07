"""Tests for T497 source-checked bounded retrieval composite stack gate."""

from __future__ import annotations

import json

from models import bounded_retrieval_source_checked_stack_gate as t497


def _length_rows(payload, projection, capability):
    return [
        row
        for row in payload["length_evaluations"]
        if row["projection_label"] == projection and row["capability_label"] == capability
    ]


def _decision(payload, reading_id):
    return next(row for row in payload["reading_decisions"] if row["reading_id"] == reading_id)


def test_artifact_identity_and_scope():
    payload = t497.run()

    assert payload["artifact"] == t497.ARTIFACT
    assert payload["verdict"] == t497.VERDICT
    assert payload["source_t495"] == t497.SOURCE_T495
    assert payload["source_t496"] == t497.SOURCE_T496
    assert payload["source_n18"] == t497.SOURCE_N18
    assert payload["overall"]["review_target_only"] is True
    assert payload["overall"]["claim_movement"] is False
    assert "does not prove an SSM/Transformer theorem" in payload["honest_ceiling"]


def test_primary_sources_support_narrow_retrieval_workload():
    payload = t497.run()

    source_ids = {source["source_id"] for source in payload["source_checks"]}
    assert "jelassi_2024_copying" in source_ids
    assert "gu_dao_2023_mamba" in source_ids
    assert "schlag_2021_fast_weights" in source_ids
    assert payload["overall"]["source_checked_retrieval_workload"] is True
    assert "jelassi_2024_copying" in payload["direct_copying_retrieval_sources"]


def test_full_history_factors_arbitrary_retrieval_for_all_lengths():
    payload = t497.run()
    rows = _length_rows(payload, "full_history", "arbitrary_retrieval")

    assert [row["length"] for row in rows] == list(range(2, 9))
    assert all(row["factorizes"] for row in rows)
    assert all(row["max_capability_spread"] == 1 for row in rows)
    assert all(row["label"] == "EXPECTED_STACK_BEHAVIOR" for row in rows)


def test_last2_arbitrary_retrieval_spread_grows_after_retained_window():
    payload = t497.run()
    rows = _length_rows(payload, "last_2_state", "arbitrary_retrieval")
    by_length = {row["length"]: row for row in rows}

    assert by_length[2]["factorizes"] is True
    for length in range(3, 9):
        row = by_length[length]
        assert row["factorizes"] is False
        assert row["max_capability_spread"] == 2 ** (length - 2)
        assert row["label"] == "EXPECTED_STACK_BEHAVIOR"


def test_last2_native_suffix_task_still_factors_for_all_lengths():
    payload = t497.run()
    rows = _length_rows(payload, "last_2_state", "last_2_suffix_retrieval")

    assert all(row["factorizes"] for row in rows)
    assert all(row["max_capability_spread"] == 1 for row in rows)
    assert all(row["label"] == "EXPECTED_STACK_BEHAVIOR" for row in rows)


def test_only_composite_explanation_reading_is_admitted():
    payload = t497.run()

    admitted = _decision(payload, "bounded_retrieval_composite_explanation")
    theorem = _decision(payload, "complexity_theorem_import")
    physics = _decision(payload, "physics_mechanism_import")
    copyability = _decision(payload, "attention_quantum_copyability_revival")
    public = _decision(payload, "public_or_cross_repo_shortcut")

    assert admitted["admitted"] is True
    assert admitted["label"] == "ADMITTED_COMPOSITE_ABSORBER_EXPLANATION"
    assert theorem["label"] == "REJECTED_THEOREM_IMPORT_SHORTCUT"
    assert physics["label"] == "REJECTED_PHYSICS_MECHANISM_IMPORT"
    assert copyability["label"] == "REJECTED_NAIVE_COPYABILITY_REVIVAL"
    assert public["label"] == "BLOCKED_PUBLIC_OR_CROSS_REPO_SHORTCUT"


def test_payload_json_and_forbidden_overreads_absent():
    payload = t497.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t497.VERDICT in dumped
    forbidden = (
        "Standard Model derived",
        "unknown quantum states are copyable",
        "claim promotion follows",
        "public posture authorized",
        "cross-repo truth proved",
    )
    for term in forbidden:
        assert term not in dumped
