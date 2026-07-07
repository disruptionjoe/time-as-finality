"""Tests for T503 Knuth-Bendix-style finality admission gate."""

from __future__ import annotations

import json

from models.knuth_bendix_finality_admission_gate import (
    VERDICT,
    completion_cases,
    run,
)


def _rows_by_id():
    return {row["case_id"]: row for row in run()["evaluations"]}


def test_overall_verdict_is_review_only_no_promotion():
    result = run()
    overall = result["overall"]

    assert result["verdict"] == VERDICT
    assert overall["t489_route"] == "future_domain_native_cost_certifiability_review_target_only"
    assert overall["t489_thread_reopened_as_claim_evidence"] is False
    assert overall["domain_native_theorem_supplied"] is False
    assert overall["claim_ledger_update"] == "none"
    assert overall["d1_t10_t29_promotion_earned"] is False
    assert overall["observer_theory_equivalence_earned"] is False
    assert overall["global_valid_coarse_graining_criterion_earned"] is False
    assert overall["physics_or_wolfram_model_claim_earned"] is False
    assert overall["cross_repo_truth_movement"] is False


def test_t61_anchor_cases_are_admitted_by_d1_and_completion():
    result = run()
    assert result["t61_anchor"]["anchor_ok"] is True
    assert result["overall"]["t61_anchor_cases_remain_admitted_by_both"] is True

    rows = _rows_by_id()
    for case_id in (
        "t61_positive_prediction_completion",
        "t61_conflict_rollback_completion",
    ):
        row = rows[case_id]
        assert row["completion_admitted"] is True
        assert row["d1_admitted"] is True
        assert row["relationship"] == "coincident_admission"
        assert row["counts_as_claim_evidence"] is False


def test_completion_refines_d1_on_branch_and_cost_controls():
    result = run()
    rows = _rows_by_id()
    expected = {
        "accessible_two_normal_forms_no_join",
        "accessible_cycle_no_final_normal_form",
        "accessible_over_budget_completion",
    }

    assert set(result["relationship_index"]["completion_refines_d1"]) == expected
    for case_id in expected:
        row = rows[case_id]
        assert row["d1_admitted"] is True
        assert row["completion_admitted"] is False
        assert row["relationship"] == "completion_refines_d1"

    assert rows["accessible_cycle_no_final_normal_form"]["rewrite_terminates"] is False
    assert (
        rows["accessible_two_normal_forms_no_join"][
            "rewrite_confluent_to_single_normal_form"
        ]
        is False
    )
    assert rows["accessible_over_budget_completion"]["completion_within_budget"] is False


def test_completion_alone_is_not_sufficient_without_d1_access_or_nonidentity():
    result = run()
    rows = _rows_by_id()
    expected = {
        "hidden_authority_completion_shortcut",
        "microstate_identity_completion_shortcut",
    }

    assert set(result["relationship_index"]["completion_not_sufficient"]) == expected
    for case_id in expected:
        row = rows[case_id]
        assert row["completion_admitted"] is True
        assert row["d1_admitted"] is False
        assert row["relationship"] == "completion_not_sufficient"

    assert rows["hidden_authority_completion_shortcut"]["hidden_completion_rule_used"] is True
    assert rows["microstate_identity_completion_shortcut"]["d1_route_label"] == (
        "TOO_FINE_MICROSTATE_TRACKING"
    )


def test_each_case_matches_predeclared_relationship():
    rows = _rows_by_id()
    expected = {case.case_id: case.expected_relationship for case in completion_cases()}

    assert {case_id: row["relationship"] for case_id, row in rows.items()} == expected


def test_future_packet_minimum_names_both_sided_hostile_controls():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert (
        "include D1-admitted but nonconfluent/cyclic/over-budget hostile controls"
        in minimum
    )
    assert (
        "include completion-confluent but D1-inaccessible or too-fine hostile controls"
        in minimum
    )
    assert (
        "keep admission review-only until a domain-native cost/certifiability theorem is supplied"
        in minimum
    )


def test_result_serializes_to_json():
    rendered = json.dumps(run())

    assert "T503-knuth-bendix-finality-admission-gate-v0.1" in rendered
    assert "completion_refines_d1" in rendered
    assert "completion_not_sufficient" in rendered
