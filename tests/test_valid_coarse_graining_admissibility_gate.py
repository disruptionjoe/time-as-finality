"""Tests for T467: valid coarse-graining admissibility gate."""

from __future__ import annotations

from models.valid_coarse_graining_admissibility_gate import (
    VERDICT,
    CertificationBudget,
    CoarseGrainingCandidate,
    evaluate_candidate,
    finite_record_states,
    run,
)


def _evaluations_by_id():
    result = run()
    return {row["candidate_id"]: row for row in result["evaluations"]}


def test_overall_verdict_is_no_promotion_admission_gate():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_filter_matches_predeclared_valid_set_in_fixture():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["filter_matches_predeclared_valid_set"] is True
    assert verdict["admitted_candidate_ids"] == [
        "two_holder_finality_band",
        "bounded_local_count",
    ]


def test_positive_controls_are_bounded_observer_certifiable():
    rows = _evaluations_by_id()

    for candidate_id in ("two_holder_finality_band", "bounded_local_count"):
        row = rows[candidate_id]
        assert row["admitted"] is True
        assert row["decision"] == "admitted_for_review"
        assert row["route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"
        assert row["blockers"] == []


def test_too_fine_and_too_coarse_controls_fail():
    rows = _evaluations_by_id()

    identity = rows["microstate_identity"]
    assert identity["admitted"] is False
    assert identity["route_label"] == "TOO_FINE_MICROSTATE_TRACKING"
    assert "too_fine_microstate_identity" in identity["blockers"]
    assert identity["class_count"] == 16

    constant = rows["constant_all_states"]
    assert constant["admitted"] is False
    assert constant["route_label"] == "TOO_COARSE_NO_TASK_SEPARATION"
    assert "too_coarse_no_task_separation" in constant["blockers"]
    assert constant["class_count"] == 1


def test_inaccessible_and_ornate_relations_fail_before_review():
    rows = _evaluations_by_id()

    hidden = rows["hidden_fourth_field"]
    assert hidden["admitted"] is False
    assert hidden["route_label"] == "INACCESSIBLE_RECORD_FIELD"
    assert "uses_inaccessible_record_fields" in hidden["blockers"]

    ornate = rows["ornate_table_lookup"]
    assert ornate["admitted"] is False
    assert ornate["route_label"] == "COMPUTATION_COST_ORNATE_OR_OVER_BUDGET"
    assert "predicate_cost_ornate" in ornate["blockers"]


def test_posthoc_projection_only_and_single_holder_routes_are_blocked():
    rows = _evaluations_by_id()

    assert rows["posthoc_exception_partition"]["route_label"] == (
        "POSTHOC_EQUIVALENCE_NOT_VALID"
    )
    assert rows["projection_only_shadow"]["route_label"] == "PROJECTION_IS_NOT_FINALITY"
    assert rows["single_holder_dashboard"]["route_label"] == (
        "D1_CERTIFICATION_BUDGET_NOT_MET"
    )


def test_observer_creates_truth_overread_is_forbidden():
    rows = _evaluations_by_id()
    row = rows["observer_creates_truth_overread"]

    assert row["admitted"] is False
    assert row["decision"] == "blocked"
    assert row["route_label"] == "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"
    assert "observer_creates_truth_overread" in row["blockers"]


def test_budget_tightening_rejects_otherwise_valid_control():
    states = finite_record_states()
    tight_budget = CertificationBudget(max_fields_read=1)
    candidate = CoarseGrainingCandidate(
        candidate_id="two_field_control",
        description="Would pass under the default budget.",
        fields_read=(0, 1),
        predicate_cost=2,
        holder_redundancy=2,
        reversal_cost=1,
        declared_before_use=True,
        certified_record_available=True,
        finality_native_task=True,
        expected_valid=True,
        labeler=lambda state: f"{state[0]}_{state[1]}",
    )

    evaluation = evaluate_candidate(candidate, tight_budget, states)

    assert evaluation.admitted is False
    assert evaluation.route_label == "COMPUTATION_COST_ORNATE_OR_OVER_BUDGET"
    assert "field_budget_exceeded" in evaluation.blockers


def test_future_packet_minimum_names_projection_and_creation_guardrails():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert "certified record available, not projection alone" in minimum
    assert (
        "finality-native task declared without observer-creates-truth overread"
        in minimum
    )
    assert (
        "nontrivial coarse-graining: neither all states nor microstate identity"
        in minimum
    )
