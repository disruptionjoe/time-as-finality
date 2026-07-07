"""Tests for T491: post-T490 S1 finite-colimit closure router."""

from __future__ import annotations

from models.post_t490_s1_finite_colimit_closure_router import (
    T491Result,
    run,
    run_t491_analysis,
    t491_result_to_dict,
)


def _decision(result: T491Result, proposal_id: str):
    return next(
        decision
        for decision in result.decisions
        if decision.proposal_id == proposal_id
    )


def test_run_returns_t491_result_and_serializable_payload():
    result = run_t491_analysis()
    payload = run()

    assert isinstance(result, T491Result)
    assert payload == t491_result_to_dict(result)
    assert payload["artifact_id"] == (
        "T491-post-t490-s1-finite-colimit-closure-router-v0.1"
    )


def test_verdict_closes_finite_route_without_promotion():
    result = run_t491_analysis()

    assert result.verdict == (
        "POST_T490_S1_FINITE_COLIMIT_ROUTE_CLOSED_NEW_EVIDENCE_ONLY"
    )
    assert result.claim_ledger_update == "none"
    assert result.current_finite_route_closed is True
    assert "S1 promotion" in result.not_earned
    assert "T223 reversal" in result.not_earned
    assert "spacetime derivation" in result.not_earned
    assert "cross-repo truth movement" in result.not_earned


def test_t490_anchor_guardrails_are_preserved():
    result = run_t491_analysis()
    anchor = result.t490_anchor

    assert anchor["artifact_id"] == (
        "T490-s1-nonuniform-measure-persistence-gate-v0.1"
    )
    assert anchor["anchor_ok"] is True
    assert anchor["all_admitted_targets_are_synthetic_only"] is True
    assert anchor["s1_promoted"] is False
    assert anchor["t223_reversed"] is False
    assert anchor["uniform_baseline_rejected"] is True
    assert anchor["tail_indicator_rejected"] is True
    assert anchor["guardrail_conditioning_rejected"] is True
    assert anchor["single_size_positive_rejected"] is True


def test_uniform_tail_guardrail_and_screen_restarts_are_rejected():
    result = run_t491_analysis()

    uniform = _decision(result, "uniform_finite_colimit_rerun")
    tail = _decision(result, "survivor_tail_measure_restart")
    screen = _decision(result, "screen_conditioned_measure_restart")
    drift = _decision(result, "post_t223_screen_drift_restart")

    assert uniform.admitted is False
    assert uniform.route_label == "reject_uniform_finite_colimit_rerun"
    assert uniform.closes_current_finite_route is True
    assert "nonvanishing_mass_target" in uniform.missing_requirements

    assert tail.admitted is False
    assert tail.route_label == "reject_tail_tuned_measure_restart"
    assert "measure_law_or_bridge_predeclared" in tail.missing_requirements

    assert screen.admitted is False
    assert screen.route_label == "reject_guardrail_screen_conditioning_restart"
    assert "later_lorentzian_constraints_named" in screen.missing_requirements

    assert drift.admitted is False
    assert drift.route_label == "reject_post_t223_screen_drift_restart"
    assert "finite_screens_fixed" in drift.missing_requirements
    assert "hostile_overread_controls" in drift.missing_requirements


def test_single_size_and_t490_evidence_shortcuts_are_rejected():
    result = run_t491_analysis()

    single = _decision(result, "single_size_positive_restart")
    evidence = _decision(result, "t490_admission_as_s1_evidence_shortcut")

    assert single.admitted is False
    assert single.route_label == "reject_single_size_positive_restart"
    assert "multi_size_or_limit_audit" in single.missing_requirements

    assert evidence.admitted is False
    assert evidence.route_label == "block_s1_spacetime_or_lorentzian_overclaim"
    assert evidence.classification == "overclaim_boundary_block"


def test_overclaim_governance_and_external_shortcuts_are_blocked():
    result = run_t491_analysis()

    overclaim = _decision(result, "spacetime_derivation_overclaim")
    posture = _decision(result, "claim_public_posture_shortcut")
    external = _decision(result, "external_publication_shortcut")

    assert overclaim.admitted is False
    assert overclaim.route_label == "block_s1_spacetime_or_lorentzian_overclaim"
    assert overclaim.counts_as_s1_evidence is False

    assert posture.admitted is False
    assert posture.route_label == "block_governance_or_public_posture_shortcut"
    assert posture.classification == "governance_boundary_block"

    assert external.admitted is False
    assert external.route_label == "block_external_action_shortcut"
    assert external.classification == "external_action_block"


def test_undercontrolled_future_packet_is_rejected():
    result = run_t491_analysis()
    decision = _decision(result, "independent_measure_missing_hostile_controls")

    assert decision.admitted is False
    assert decision.route_label == "reject_missing_reopen_requirements"
    assert "hostile_overread_controls" in decision.missing_requirements
    assert decision.closes_current_finite_route is False


def test_future_reopen_targets_are_admitted_for_review_only():
    result = run_t491_analysis()

    measure = _decision(result, "future_independent_measure_law_packet")
    continuum = _decision(result, "future_continuum_bridge_packet")
    separate = _decision(result, "future_separate_formal_entry_point_packet")

    assert measure.admitted is True
    assert measure.route_label == "admit_future_independent_measure_law_review_target"
    assert measure.admitted_as_future_review_target is True
    assert measure.counts_as_s1_evidence is False

    assert continuum.admitted is True
    assert continuum.route_label == "admit_future_continuum_bridge_review_target"
    assert continuum.counts_as_s1_evidence is False

    assert separate.admitted is True
    assert separate.route_label == (
        "admit_future_separate_formal_entry_point_review_target"
    )
    assert separate.counts_as_s1_evidence is False


def test_only_future_targets_are_admitted():
    result = run_t491_analysis()

    assert result.admitted_future_targets == (
        "future_independent_measure_law_packet",
        "future_continuum_bridge_packet",
        "future_separate_formal_entry_point_packet",
    )
    assert "uniform_finite_colimit_rerun" in result.rejected_restart_packets
    assert "spacetime_derivation_overclaim" in result.rejected_restart_packets


def test_future_reopen_minimum_preserves_t490_closure():
    result = run_t491_analysis()

    assert (
        "predeclare the nonuniform measure law, selection law, sprinkling law, continuum bridge, or separate formal entry point before scoring"
        in result.future_reopen_minimum
    )
    assert (
        "do not condition directly on survivor success or guardrail-screen pass predicates"
        in result.future_reopen_minimum
    )
    assert "continuum theorem" in result.not_earned
    assert "non-GitHub external action" in result.not_earned
