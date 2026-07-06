"""Tests for T471: coarse-graining multivalued fixture gate."""

from __future__ import annotations

from dataclasses import replace

from models.coarse_graining_multivalued_fixture_gate import (
    VERDICT,
    compare_positive_controls,
    default_budget,
    finite_record_states,
    packet_candidates,
    packet_shape,
    run,
)
from models.coarse_graining_task_naturalness_gate import (
    evaluate_naturalness_candidate,
    evaluate_packet,
)


def _evaluations_by_id():
    result = run()
    return {row["candidate_id"]: row for row in result["candidate_evaluations"]}


def _packets_by_id():
    result = run()
    return {row["packet_id"]: row for row in result["packet_evaluations"]}


def test_overall_verdict_is_alphabet_stress_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_ternary_packet_is_admitted_with_independent_positives():
    packets = _packets_by_id()
    packet = packets["ternary_three_holder_packet"]

    assert packet["admitted"] is True
    assert packet["route_label"] == "REPAIRED_TASK_NATURALNESS_PACKET_ADMITTED"
    assert packet["positive_controls_independent"] is True
    assert packet["hostile_controls_blocked"] is True


def test_binary_reference_packet_still_clears():
    packets = _packets_by_id()
    packet = packets["binary_three_holder_packet"]

    assert packet["admitted"] is True
    assert packet["positive_controls_independent"] is True
    assert packet["hostile_controls_blocked"] is True


def test_ternary_positive_controls_are_not_the_same_partition():
    comparison = compare_positive_controls(alphabet_size=3)

    assert comparison["holder_width"] == 3
    assert comparison["state_count"] == 27
    assert comparison["finality_band_class_count"] == 4
    assert comparison["support_count_class_count"] == 4
    assert comparison["partitions_identical"] is False


def test_ternary_positive_controls_clear_task_naturalness():
    evaluations = _evaluations_by_id()

    for candidate_id in (
        "ternary_finality_band",
        "ternary_support_count",
    ):
        row = evaluations[candidate_id]
        assert row["admitted"] is True
        assert row["route_label"] == "TASK_NATURALNESS_PACKET_CLEARED"
        assert row["base_route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"
        assert row["blockers"] == []


def test_ternary_mod_sum_passes_base_gate_but_fails_t470():
    evaluations = _evaluations_by_id()
    row = evaluations["ternary_mod_sum_with_task_label"]

    assert row["base_admitted"] is True
    assert row["base_route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"
    assert row["admitted"] is False
    assert row["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "certified_record_object_not_named" in row["blockers"]
    assert "record_value_or_support_not_preserved" in row["blockers"]
    assert "task_semantics_restates_label" in row["blockers"]


def test_ternary_label_hidden_microstate_and_overread_controls_block():
    evaluations = _evaluations_by_id()

    label_row = evaluations["ternary_label_restatement_lookup"]
    assert label_row["admitted"] is False
    assert label_row["route_label"] == "TASK_NATURALNESS_NOT_MET"
    assert "task_semantics_restates_label" in label_row["blockers"]

    hidden_row = evaluations["ternary_hidden_fourth_field_task"]
    assert hidden_row["admitted"] is False
    assert hidden_row["route_label"] == "BASE_CERTIFICATION_GATE_NOT_MET"
    assert "base_gate:INACCESSIBLE_RECORD_FIELD" in hidden_row["blockers"]

    microstate_row = evaluations["ternary_microstate_identity"]
    assert microstate_row["admitted"] is False
    assert microstate_row["route_label"] == "BASE_CERTIFICATION_GATE_NOT_MET"
    assert "base_gate:TOO_FINE_MICROSTATE_TRACKING" in microstate_row["blockers"]

    overread_row = evaluations["ternary_observer_creates_truth_overread"]
    assert overread_row["admitted"] is False
    assert overread_row["decision"] == "blocked"
    assert overread_row["route_label"] == "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"


def test_packet_with_mod_sum_admitted_would_fail():
    states = finite_record_states(width=4, alphabet_size=3)
    candidates = {
        candidate.base.candidate_id: candidate
        for candidate in packet_candidates(alphabet_size=3)
    }
    budget = default_budget()
    evaluations = {
        candidate_id: evaluate_naturalness_candidate(candidate, budget, states)
        for candidate_id, candidate in candidates.items()
    }
    evaluations["ternary_mod_sum_with_task_label"] = replace(
        evaluations["ternary_mod_sum_with_task_label"],
        admitted=True,
    )
    shape = packet_shape(alphabet_size=3)

    packet = evaluate_packet(
        packet_id="bad_ternary_packet",
        candidate_ids=shape.candidate_ids,
        positive_control_ids=shape.positive_control_ids,
        hostile_control_ids=shape.hostile_control_ids,
        candidates=candidates,
        evaluations=evaluations,
        states=states,
    )

    assert packet.admitted is False
    assert packet.route_label == "HOSTILE_CONTROL_NOT_BLOCKED"
    assert "hostile_control_admitted" in packet.blockers


def test_future_packet_minimum_preserves_nonbinary_burden():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert "stress constructive packets across at least one non-binary alphabet" in minimum
    assert "include cheap accessible arithmetic partitions as hostile controls" in minimum
    assert "keep certified-record and observer-creates-truth guardrails active" in minimum
