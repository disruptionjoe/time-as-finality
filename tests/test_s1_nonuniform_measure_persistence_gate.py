"""Tests for T490: S1 nonuniform measure persistence gate."""

from __future__ import annotations

from fractions import Fraction

from models.s1_nonuniform_measure_persistence_gate import (
    NONVANISHING_REVIEW_FLOOR,
    MeasurePacket,
    evaluate_packet,
    run,
    survivor_mass_trajectory,
    t223_census,
)


def _decision(result: dict, packet_id: str) -> dict:
    return {item["packet_id"]: item for item in result["decisions"]}[packet_id]


def test_t223_baseline_census_is_fixed() -> None:
    census = t223_census()

    assert [(item.event_count, item.total_cases) for item in census] == [
        (6, 720),
        (7, 5040),
        (8, 40320),
    ]
    assert [item.stable_survivor_count for item in census] == [26, 174, 361]
    assert [item.uniform_survivor_mass for item in census] == [
        Fraction(13, 360),
        Fraction(29, 840),
        Fraction(361, 40320),
    ]
    assert [item.parent_conditioned_survivor_mass for item in census] == [
        Fraction(1, 6),
        Fraction(58, 187),
        Fraction(361, 2057),
    ]
    assert NONVANISHING_REVIEW_FLOOR == Fraction(1, 20)


def test_overall_verdict_keeps_s1_and_t223_unchanged() -> None:
    result = run()

    assert result["verdict"] == (
        "S1_NONUNIFORM_MEASURE_PERSISTENCE_GATE_BUILT_SCREEN_CONDITIONING_NOT_ENOUGH"
    )
    assert result["s1_promoted"] is False
    assert result["t223_reversed"] is False
    assert result["claim_ledger_update"] == "none"
    assert "S1 promotion" in result["not_earned"]
    assert "T223 reversal" in result["not_earned"]
    assert "spacetime derivation" in result["not_earned"]


def test_uniform_baseline_is_rejected_as_t223_closed_route() -> None:
    result = run()
    decision = _decision(result, "uniform_ordinal_baseline")

    assert decision["admitted"] is False
    assert decision["gate_label"] == "REJECTED_UNIFORM_BASELINE_CLOSED_BY_T223"
    assert "not_uniform_t223_baseline" in decision["missing_requirements"]
    assert "nonvanishing_review_floor" in decision["missing_requirements"]


def test_survivor_tail_and_guardrail_conditioning_are_rejected() -> None:
    result = run()
    tail = _decision(result, "known_survivor_tail_indicator")
    parent = _decision(result, "parent_interval_conditioned_measure")
    full_stack = _decision(result, "full_screen_stack_conditioned_measure")

    assert tail["gate_label"] == "REJECTED_TAIL_INDICATOR_OR_SUCCESS_CONDITIONING"
    assert tail["classification"] == "tail_tuned_measure_rejection"
    assert "not_conditioned_on_survivor_success" in tail["missing_requirements"]

    assert parent["gate_label"] == "REJECTED_GUARDRAIL_SCREEN_CONDITIONING"
    assert parent["classification"] == "screen_conditioned_measure_rejection"
    assert "not_guardrail_screen_conditioned" in parent["missing_requirements"]

    assert full_stack["gate_label"] == (
        "REJECTED_TAIL_INDICATOR_OR_SUCCESS_CONDITIONING"
    )
    assert "not_conditioned_on_survivor_success" in full_stack["missing_requirements"]
    assert "not_guardrail_screen_conditioned" in full_stack["missing_requirements"]


def test_screen_drift_and_single_size_positive_fail() -> None:
    result = run()
    drift = _decision(result, "screen_drift_after_t223")
    single = _decision(result, "single_size_n8_positive")

    assert drift["gate_label"] == "REJECTED_SCREEN_DRIFT_AFTER_T223"
    assert "no_screen_drift" in drift["missing_requirements"]

    assert single["gate_label"] == "REJECTED_SINGLE_SIZE_POSITIVE"
    assert "multi_size_or_limit_audit" in single["missing_requirements"]


def test_missing_independent_law_or_lorentzian_targets_fail() -> None:
    result = run()
    no_law = _decision(result, "unjustified_nonuniform_weight")
    no_targets = _decision(result, "nonvanishing_but_no_lorentzian_targets")

    assert no_law["gate_label"] == "REJECTED_NO_INDEPENDENT_GENERATING_LAW"
    assert "independent_generating_law" in no_law["missing_requirements"]

    assert no_targets["gate_label"] == "REJECTED_NO_LORENTZIAN_CONSTRAINT_TARGETS"
    assert "later_lorentzian_constraints_named" in no_targets["missing_requirements"]


def test_promotion_and_external_shortcuts_block() -> None:
    result = run()
    promotion = _decision(result, "claim_promotion_shortcut")
    external = _decision(result, "external_publication_shortcut")

    assert promotion["gate_label"] == "BLOCKED_S1_PROMOTION_REQUEST"
    assert promotion["classification"] == "governance_boundary_block"
    assert promotion["counts_as_s1_evidence"] is False

    assert external["gate_label"] == "BLOCKED_EXTERNAL_ACTION_REQUIRED"
    assert external["classification"] == "external_action_block"
    assert external["counts_as_s1_evidence"] is False


def test_synthetic_future_targets_are_admitted_for_review_only() -> None:
    result = run()

    assert result["admitted_future_targets"] == [
        "synthetic_predeclared_measure_review_target",
        "synthetic_continuum_bridge_weight_target",
    ]
    assert result["all_admitted_targets_are_synthetic_only"] is True

    for packet_id in result["admitted_future_targets"]:
        decision = _decision(result, packet_id)
        assert decision["gate_label"] == (
            "ADMITTED_MEASURE_PERSISTENCE_REVIEW_TARGET_NO_PROMOTION"
        )
        assert decision["admitted"] is True
        assert decision["admitted_as_future_review_target"] is True
        assert decision["counts_as_s1_evidence"] is False
        assert decision["missing_requirements"] == []


def test_low_declared_survivor_mass_fails_review_floor() -> None:
    packet = MeasurePacket(
        packet_id="low_mass",
        description="Predeclared but below the finite review floor.",
        measure_kind="nonuniform_measure",
        declares_t223_context=True,
        predeclared_before_scoring=True,
        has_independent_generating_law=True,
        finite_audit_fixed_screens=True,
        audited_sizes=(6, 7, 8),
        provides_nonvanishing_mass_claim=True,
        names_lorentzian_targets=True,
        declared_survivor_masses=(
            (6, Fraction(1, 10)),
            (7, Fraction(1, 12)),
            (8, Fraction(1, 100)),
        ),
    )

    decision = evaluate_packet(packet)
    assert decision.gate_label == "REJECTED_SURVIVOR_MASS_BELOW_REVIEW_FLOOR"
    assert "nonvanishing_review_floor" in decision.missing_requirements


def test_survivor_mass_trajectory_uses_packet_mass_before_baseline() -> None:
    packet = MeasurePacket(
        packet_id="declared",
        description="Declared masses.",
        measure_kind="nonuniform_measure",
        declares_t223_context=True,
        predeclared_before_scoring=True,
        has_independent_generating_law=True,
        finite_audit_fixed_screens=True,
        audited_sizes=(6, 7, 8),
        provides_nonvanishing_mass_claim=True,
        names_lorentzian_targets=True,
        declared_survivor_masses=((8, Fraction(1, 3)), (6, Fraction(1, 4))),
    )

    assert survivor_mass_trajectory(packet) == (
        (6, Fraction(1, 4)),
        (8, Fraction(1, 3)),
    )
