"""Tests for T477: coarse-graining budget-index gate."""

from __future__ import annotations

from models.coarse_graining_budget_index_gate import VERDICT, run


def _evaluations_for_budget(budget_id: str):
    result = run()
    budget = next(
        row for row in result["budget_results"] if row["budget_id"] == budget_id
    )
    return {row["candidate_id"]: row for row in budget["candidate_evaluations"]}


def _packet_for_budget(budget_id: str):
    result = run()
    budget = next(
        row for row in result["budget_results"] if row["budget_id"] == budget_id
    )
    return budget["packet_evaluation"]


def test_overall_verdict_is_budget_index_guardrail_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_three_holder_positives_persist_under_expanded_budget():
    three = _evaluations_for_budget("three_holder_budget")
    four = _evaluations_for_budget("four_holder_budget")

    for candidate_id in (
        "three_holder_finality_band",
        "three_holder_support_count",
    ):
        assert three[candidate_id]["admitted"] is True
        assert four[candidate_id]["admitted"] is True
        assert three[candidate_id]["route_label"] == "TASK_NATURALNESS_PACKET_CLEARED"
        assert four[candidate_id]["route_label"] == "TASK_NATURALNESS_PACKET_CLEARED"


def test_boundary_pair_is_admitted_only_when_budget_includes_fourth_holder():
    three = _evaluations_for_budget("three_holder_budget")
    four = _evaluations_for_budget("four_holder_budget")

    assert three["boundary_pair_status"]["admitted"] is False
    assert three["boundary_pair_status"]["base_route_label"] == "INACCESSIBLE_RECORD_FIELD"
    assert "base_gate:INACCESSIBLE_RECORD_FIELD" in three["boundary_pair_status"]["blockers"]

    assert four["boundary_pair_status"]["admitted"] is True
    assert four["boundary_pair_status"]["route_label"] == "TASK_NATURALNESS_PACKET_CLEARED"
    assert four["boundary_pair_status"]["blockers"] == []


def test_hostile_controls_remain_blocked_under_expanded_budget():
    four = _evaluations_for_budget("four_holder_budget")

    parity = four["cheap_accessible_parity_with_task_label"]
    assert parity["admitted"] is False
    assert parity["base_admitted"] is True
    assert parity["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "certified_record_object_not_named" in parity["blockers"]
    assert "task_semantics_restates_label" in parity["blockers"]

    lookup = four["label_restatement_lookup"]
    assert lookup["admitted"] is False
    assert lookup["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "task_semantics_restates_label" in lookup["blockers"]

    overread = four["observer_creates_truth_overread"]
    assert overread["admitted"] is False
    assert overread["route_label"] == "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"


def test_microstate_identity_stays_blocked_even_with_full_access():
    four = _evaluations_for_budget("four_holder_budget")
    microstate = four["microstate_identity"]

    assert microstate["admitted"] is False
    assert microstate["base_route_label"] == "TOO_FINE_MICROSTATE_TRACKING"
    assert microstate["route_label"] == "BASE_CERTIFICATION_GATE_NOT_MET"
    assert "base_gate:TOO_FINE_MICROSTATE_TRACKING" in microstate["blockers"]


def test_both_budget_packets_are_admitted_for_review():
    three_packet = _packet_for_budget("three_holder_budget")
    four_packet = _packet_for_budget("four_holder_budget")

    assert three_packet["admitted"] is True
    assert four_packet["admitted"] is True
    assert three_packet["hostile_controls_blocked"] is True
    assert four_packet["hostile_controls_blocked"] is True
    assert four_packet["positive_control_ids"] == [
        "three_holder_finality_band",
        "three_holder_support_count",
        "boundary_pair_status",
    ]


def test_transition_table_marks_budget_indexing():
    result = run()
    transitions = {
        row["candidate_id"]: row["transition"]
        for row in result["budget_transition_rows"]
    }

    assert transitions["three_holder_finality_band"] == "persists_admitted"
    assert transitions["three_holder_support_count"] == "persists_admitted"
    assert (
        transitions["boundary_pair_status"]
        == "observer_budget_reveals_new_admission"
    )
    assert transitions["cheap_accessible_parity_with_task_label"] == "stays_blocked"
    assert transitions["microstate_identity"] == "stays_blocked"


def test_future_packet_minimum_names_budget_transition_burden():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert "declare the observer budget before selecting the relation" in minimum
    assert "report budget transitions for every candidate relation" in minimum
    assert (
        "treat newly accessible record tasks as observer-indexed admissions, not global criteria"
        in minimum
    )
