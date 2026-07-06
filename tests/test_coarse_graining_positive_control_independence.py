"""Tests for T468: positive-control independence audit."""

from __future__ import annotations

from models.coarse_graining_positive_control_independence import (
    VERDICT,
    compare_positive_controls,
    minimum_width_for_positive_independence,
    run,
    task_semantics_probe,
)


def test_overall_verdict_is_audit_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["d1_promotion_earned"] is False
    assert verdict["t10_promotion_earned"] is False
    assert verdict["t29_promotion_earned"] is False
    assert verdict["observer_theory_identification_earned"] is False
    assert verdict["physics_claim_earned"] is False


def test_t467_two_holder_positive_controls_are_extensional_duplicates():
    comparison = compare_positive_controls(width=2)

    assert comparison["state_count"] == 4
    assert comparison["partitions_identical"] is True
    assert comparison["finality_band_class_count"] == 3
    assert comparison["local_count_class_count"] == 3


def test_three_holders_are_minimum_binary_width_for_independence():
    comparison = compare_positive_controls(width=3)

    assert comparison["state_count"] == 8
    assert comparison["partitions_identical"] is False
    assert comparison["finality_band_class_count"] == 3
    assert comparison["local_count_class_count"] == 4
    assert minimum_width_for_positive_independence() == 3


def test_finality_task_semantics_is_load_bearing():
    probe = task_semantics_probe()
    without_task = probe["without_finality_task"]
    with_task = probe["with_finality_task_label"]

    assert probe["task_semantics_load_bearing"] is True
    assert without_task["admitted"] is False
    assert without_task["route_label"] == "NO_FINALIZED_RECORD_TASK"
    assert "no_finalized_record_task" in without_task["blockers"]
    assert with_task["admitted"] is True
    assert with_task["route_label"] == "BOUNDED_OBSERVER_CERTIFIABLE"


def test_future_packet_minimum_requires_independent_controls_and_hostile_xor():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert (
        "use at least three binary holders or a multi-valued fixture when claiming independent positive controls"
        in minimum
    )
    assert (
        "include a cheap accessible non-finality partition as a hostile control"
        in minimum
    )
    assert (
        "supply a predeclared task-naturalness account rather than only a boolean finality-task flag"
        in minimum
    )
