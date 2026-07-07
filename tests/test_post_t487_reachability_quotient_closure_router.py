"""Tests for T488: post-T487 reachability-quotient closure router."""

from __future__ import annotations

from models.post_t487_reachability_quotient_closure_router import (
    T488Result,
    run,
    run_t488_analysis,
    t488_result_to_dict,
)


def _decision(result: T488Result, proposal_id: str):
    return next(
        decision
        for decision in result.decisions
        if decision.proposal_id == proposal_id
    )


def test_run_returns_t488_result_and_serializable_payload():
    result = run_t488_analysis()
    payload = run()

    assert isinstance(result, T488Result)
    assert payload == t488_result_to_dict(result)
    assert payload["artifact_id"] == (
        "T488-post-t487-reachability-quotient-closure-router-v0.1"
    )


def test_verdict_closes_current_thread_without_promotion():
    result = run_t488_analysis()

    assert result.verdict == (
        "POST_T487_REACHABILITY_QUOTIENT_THREAD_CLOSED_NEW_EVIDENCE_ONLY"
    )
    assert result.claim_ledger_update == "none"
    assert result.current_thread_closed is True
    assert "claim-ledger movement" in result.not_earned
    assert "scale-genesis theorem" in result.not_earned
    assert "record-finality change" in result.not_earned
    assert "cross-repo truth movement" in result.not_earned


def test_t487_anchor_guardrails_are_preserved():
    result = run_t488_analysis()
    anchor = result.t487_anchor

    assert anchor["artifact_id"] == (
        "T487-reachability-quotient-capability-spread-gate-v0.1"
    )
    assert anchor["anchor_ok"] is True
    assert anchor["gate_passed"] is True
    assert anchor["admitted_candidate_ids"] == [
        "source_target_reachability_task",
        "quotient_role_profile_task",
    ]
    assert anchor["reachability_task_sufficient"] is True
    assert anchor["role_profile_task_sufficient"] is True
    assert anchor["path_latency_underdetermined"] is True
    assert anchor["relay_budget_underdetermined"] is True
    assert anchor["component_size_underdetermined"] is True
    assert anchor["record_finality_change_earned"] is False
    assert anchor["scale_genesis_theorem_earned"] is False
    assert anchor["physics_claim_earned"] is False


def test_reachability_and_role_profile_upgrade_restarts_are_rejected():
    result = run_t488_analysis()

    reachability = _decision(result, "repeat_reachability_quotient_upgrade")
    assert reachability.admitted is False
    assert reachability.route_label == "reject_reachability_upgrade_shortcut"
    assert reachability.closes_current_thread is True
    assert "direct_record_finality_or_scale_bridge_theorem" in (
        reachability.missing_requirements
    )

    role_profile = _decision(result, "role_profile_internal_scale_restart")
    assert role_profile.admitted is False
    assert role_profile.route_label == "reject_role_profile_scale_shortcut"
    assert role_profile.closes_current_thread is True


def test_t487_underdetermined_capability_restarts_are_rejected():
    result = run_t488_analysis()

    path_latency = _decision(result, "path_latency_relabel_restart")
    relay_budget = _decision(result, "relay_budget_clock_restart")
    component_size = _decision(result, "component_size_capacity_restart")

    assert path_latency.admitted is False
    assert path_latency.route_label == (
        "reject_t487_underdetermined_capability_restart"
    )
    assert path_latency.classification == "underdetermined_capability_rejection"

    assert relay_budget.admitted is False
    assert relay_budget.route_label == (
        "reject_t487_underdetermined_capability_restart"
    )

    assert component_size.admitted is False
    assert component_size.route_label == (
        "reject_t487_underdetermined_capability_restart"
    )


def test_finality_rg_and_governance_shortcuts_are_blocked():
    result = run_t488_analysis()

    finality = _decision(result, "record_finality_bridge_shortcut")
    rg = _decision(result, "rg_conformal_import_restart")
    posture = _decision(result, "claim_public_posture_shortcut")

    assert finality.admitted is False
    assert finality.route_label == "reject_reachability_upgrade_shortcut"
    assert "direct_record_finality_or_scale_bridge_theorem" in (
        finality.missing_requirements
    )

    assert rg.admitted is False
    assert rg.route_label == "reject_rg_or_conformal_import_restart"
    assert "capability_spread_computed" in rg.missing_requirements
    assert "hostile_overread_controls" in rg.missing_requirements

    assert posture.admitted is False
    assert posture.route_label == "block_governance_or_public_posture_shortcut"
    assert posture.classification == "governance_boundary_block"


def test_undercontrolled_future_packet_is_rejected():
    result = run_t488_analysis()
    decision = _decision(result, "independent_capability_missing_controls")

    assert decision.admitted is False
    assert decision.route_label == "reject_missing_reopen_requirements"
    assert "hostile_overread_controls" in decision.missing_requirements
    assert decision.closes_current_thread is False


def test_future_reopen_targets_are_admitted_for_review_only():
    result = run_t488_analysis()

    independent = _decision(result, "future_independent_capability_object_packet")
    morphism = _decision(result, "future_domain_native_morphism_class_packet")
    finality = _decision(result, "future_direct_record_finality_bridge_packet")

    assert independent.admitted is True
    assert independent.route_label == (
        "admit_future_independent_capability_review_target"
    )
    assert independent.admitted_as_future_review_target is True
    assert independent.counts_as_thread_evidence is False

    assert morphism.admitted is True
    assert morphism.route_label == (
        "admit_future_domain_native_morphism_review_target"
    )
    assert morphism.counts_as_thread_evidence is False

    assert finality.admitted is True
    assert finality.route_label == (
        "admit_future_record_finality_bridge_review_target"
    )
    assert finality.counts_as_thread_evidence is False


def test_only_future_targets_are_admitted():
    result = run_t488_analysis()

    assert result.admitted_future_targets == (
        "future_independent_capability_object_packet",
        "future_domain_native_morphism_class_packet",
        "future_direct_record_finality_bridge_packet",
    )
    assert "repeat_reachability_quotient_upgrade" in result.rejected_restart_packets
    assert "claim_public_posture_shortcut" in result.rejected_restart_packets


def test_future_reopen_minimum_preserves_t487_closure():
    result = run_t488_analysis()

    assert (
        "compute capability spread over the declared visible fibers"
        in result.future_reopen_minimum
    )
    assert (
        "supply evidence independent of the T485/T487 quotient when claiming a new generator"
        in result.future_reopen_minimum
    )
    assert "record clock" in result.not_earned
    assert "RG/TaF equivalence theorem" in result.not_earned
