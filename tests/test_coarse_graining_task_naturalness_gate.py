"""Tests for T469: coarse-graining task-naturalness gate."""

from __future__ import annotations

from dataclasses import replace

from models.coarse_graining_task_naturalness_gate import (
    VERDICT,
    default_budget,
    evaluate_naturalness_candidate,
    evaluate_packet,
    example_candidates,
    run,
)
from models.valid_coarse_graining_admissibility_gate import finite_record_states


def _evaluations_by_id():
    result = run()
    return {row["candidate_id"]: row for row in result["candidate_evaluations"]}


def _packets_by_id():
    result = run()
    return {row["packet_id"]: row for row in result["packet_evaluations"]}


def test_overall_verdict_is_fixture_repair_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_repaired_three_holder_packet_is_admitted_for_review():
    packets = _packets_by_id()
    packet = packets["repaired_three_holder_packet"]

    assert packet["admitted"] is True
    assert packet["route_label"] == "REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED"
    assert packet["positive_controls_independent"] is True
    assert packet["hostile_controls_blocked"] is True


def test_legacy_two_holder_packet_fails_positive_control_independence():
    packets = _packets_by_id()
    packet = packets["legacy_two_holder_packet"]

    assert packet["admitted"] is False
    assert packet["route_label"] == "POSITIVE_CONTROL_INDEPENDENCE_NOT_MET"
    assert "positive_controls_not_independent" in packet["blockers"]
    assert packet["positive_controls_independent"] is False


def test_three_holder_positive_controls_clear_task_naturalness():
    evaluations = _evaluations_by_id()

    for candidate_id in (
        "three_holder_finality_band",
        "three_holder_support_count",
    ):
        row = evaluations[candidate_id]
        assert row["admitted"] is True
        assert row["route_label"] == "TASK_NATURALNESS_PACKET_CLEARED"
        assert row["base_route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"
        assert row["blockers"] == []


def test_cheap_xor_passes_base_gate_but_fails_t469():
    evaluations = _evaluations_by_id()
    row = evaluations["cheap_accessible_xor_with_task_label"]

    assert row["base_admitted"] is True
    assert row["base_route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"
    assert row["admitted"] is False
    assert row["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "certified_record_object_not_named" in row["blockers"]
    assert "record_value_or_support_not_preserved" in row["blockers"]
    assert "task_semantics_restates_label" in row["blockers"]


def test_label_restatement_and_hidden_field_controls_are_blocked():
    evaluations = _evaluations_by_id()

    label_row = evaluations["label_restatement_lookup"]
    assert label_row["admitted"] is False
    assert label_row["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "task_semantics_restates_label" in label_row["blockers"]

    hidden_row = evaluations["hidden_fourth_field_task"]
    assert hidden_row["admitted"] is False
    assert hidden_row["route_label"] == "BASE_CERTIFICATION_GATE_NOT_MET"
    assert "base_gate:INACCESSIBLE_RECORD_FIELD" in hidden_row["blockers"]


def test_observer_creates_truth_overread_is_forbidden():
    evaluations = _evaluations_by_id()
    row = evaluations["observer_creates_truth_overread"]

    assert row["admitted"] is False
    assert row["decision"] == "blocked"
    assert row["route_label"] == "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"
    assert "observer_creates_truth_overread" in row["blockers"]


def test_packet_with_hostile_control_admitted_would_fail():
    states = finite_record_states(width=4)
    candidates = {candidate.base.candidate_id: candidate for candidate in example_candidates()}
    budget = default_budget()
    evaluations = {
        candidate_id: evaluate_naturalness_candidate(candidate, budget, states)
        for candidate_id, candidate in candidates.items()
    }
    evaluations["cheap_accessible_xor_with_task_label"] = replace(
        evaluations["cheap_accessible_xor_with_task_label"],
        admitted=True,
    )

    packet = evaluate_packet(
        packet_id="bad_packet",
        candidate_ids=(
            "three_holder_finality_band",
            "three_holder_support_count",
            "cheap_accessible_xor_with_task_label",
        ),
        positive_control_ids=(
            "three_holder_finality_band",
            "three_holder_support_count",
        ),
        hostile_control_ids=("cheap_accessible_xor_with_task_label",),
        candidates=candidates,
        evaluations=evaluations,
        states=states,
    )

    assert packet.admitted is False
    assert packet.route_label == "HOSTILE_CONTROL_NOT_BLOCKED"
    assert "hostile_control_admitted" in packet.blockers


def test_future_packet_minimum_names_task_naturalness_burdens():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert "include cheap accessible non-finality hostile controls" in minimum
    assert "name a certified record object before selecting the relation" in minimum
    assert (
        "show the task preserves record value, support, or finality status"
        in minimum
    )
    assert default_budget().max_fields_read == 3
