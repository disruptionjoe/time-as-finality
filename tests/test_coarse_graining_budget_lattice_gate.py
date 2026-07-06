"""Tests for T478: coarse-graining budget-lattice gate."""

from __future__ import annotations

from models.coarse_graining_budget_lattice_gate import VERDICT, run


def _budget(result, budget_id: str):
    return next(row for row in result["budget_results"] if row["budget_id"] == budget_id)


def _evaluations(result, budget_id: str):
    budget = _budget(result, budget_id)
    return {
        row["candidate_id"]: row
        for row in budget["candidate_evaluations"]
    }


def _transition(result, candidate_id: str):
    return next(
        row
        for row in result["candidate_transition_rows"]
        if row["candidate_id"] == candidate_id
    )


def test_overall_verdict_is_lattice_guardrail_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["gate_passed"] is True
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["global_valid_coarse_graining_criterion_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_no_admitted_candidate_is_lost_on_budget_edges():
    result = run()

    assert result["edge_checks"]
    assert all(row["monotone"] for row in result["edge_checks"])
    assert all(row["lost_admissions"] == [] for row in result["edge_checks"])


def test_join_checks_preserve_prior_admissions_and_explain_new_ones():
    result = run()
    joins = result["join_checks"]

    assert joins
    assert all(row["path_independent_and_explained"] for row in joins)
    assert all(row["no_preexisting_admission_loss"] for row in joins)
    assert all(row["new_admissions_explained_by_join_budget"] for row in joins)

    join_012 = next(
        row
        for row in joins
        if row["left_budget"] == "budget_01"
        and row["right_budget"] == "budget_02"
    )
    assert join_012["join_budget"] == "budget_012"
    assert "three_holder_finality_band" in join_012["newly_admitted_at_join"]
    assert "three_holder_support_count" in join_012["newly_admitted_at_join"]


def test_top_budget_verdict_is_independent_of_expansion_path():
    result = run()

    assert result["path_checks"]
    for row in result["path_checks"]:
        assert row["top_vector_matches_direct_top"] is True


def test_pair_and_boundary_positives_are_observer_budget_indexed():
    result = run()

    pair_01 = _transition(result, "pair_01_finality_band")
    assert pair_01["first_admitted_budgets"] == ["budget_01"]
    assert "budget_012" in pair_01["admitted_budgets"]
    assert "budget_013" in pair_01["admitted_budgets"]
    assert "budget_0123" in pair_01["admitted_budgets"]
    assert "budget_02" not in pair_01["admitted_budgets"]

    pair_02 = _transition(result, "pair_02_finality_band")
    assert pair_02["first_admitted_budgets"] == ["budget_02"]
    assert "budget_012" in pair_02["admitted_budgets"]
    assert "budget_023" in pair_02["admitted_budgets"]

    boundary = _transition(result, "boundary_pair_status")
    assert boundary["first_admitted_budgets"] == ["budget_03"]
    assert "budget_013" in boundary["admitted_budgets"]
    assert "budget_023" in boundary["admitted_budgets"]
    assert "budget_0123" in boundary["admitted_budgets"]


def test_hostile_controls_stay_blocked_when_accessible():
    result = run()

    assert result["hostile_violations"] == []
    budget_0123 = _evaluations(result, "budget_0123")

    pair_parity = budget_0123["cheap_pair01_parity_with_task_label"]
    assert pair_parity["base_admitted"] is True
    assert pair_parity["admitted"] is False
    assert pair_parity["route_label"] == "TASK_NATURALNESS_NOT_MET"

    triple_parity = budget_0123["cheap_triple_parity_with_task_label"]
    assert triple_parity["base_admitted"] is True
    assert triple_parity["admitted"] is False
    assert "certified_record_object_not_named" in triple_parity["blockers"]

    lookup = budget_0123["label_restatement_lookup"]
    assert lookup["base_admitted"] is True
    assert lookup["admitted"] is False
    assert "task_semantics_restates_label" in lookup["blockers"]

    microstate = budget_0123["microstate_identity"]
    assert microstate["base_route_label"] == "TOO_FINE_MICROSTATE_TRACKING"
    assert microstate["admitted"] is False

    overread = budget_0123["observer_creates_truth_overread"]
    assert overread["route_label"] == "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"
    assert overread["admitted"] is False


def test_top_budget_has_independent_positive_controls_without_promotion():
    result = run()

    assert result["top_budget_positives_independent"] is True
    assert set(result["top_budget_admitted_positive_ids"]) == {
        "pair_01_finality_band",
        "pair_02_finality_band",
        "boundary_pair_status",
        "three_holder_finality_band",
        "three_holder_support_count",
    }
    assert (
        "treat budget-indexed admissions as local review targets, not global valid-coarse-graining criteria"
        in result["future_packet_minimum"]
    )
