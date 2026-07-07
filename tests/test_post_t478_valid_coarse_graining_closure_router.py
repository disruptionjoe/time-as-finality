"""Tests for T489: post-T478 valid-coarse-graining closure router."""

from __future__ import annotations

from models.post_t478_valid_coarse_graining_closure_router import (
    T489Result,
    run,
    run_t489_analysis,
    t489_result_to_dict,
)


def _decision(result: T489Result, proposal_id: str):
    return next(
        decision
        for decision in result.decisions
        if decision.proposal_id == proposal_id
    )


def test_run_returns_t489_result_and_serializable_payload():
    result = run_t489_analysis()
    payload = run()

    assert isinstance(result, T489Result)
    assert payload == t489_result_to_dict(result)
    assert payload["artifact_id"] == (
        "T489-post-t478-valid-coarse-graining-closure-router-v0.1"
    )


def test_verdict_closes_current_thread_without_promotion():
    result = run_t489_analysis()

    assert result.verdict == (
        "POST_T478_VALID_COARSE_GRAINING_THREAD_CLOSED_NEW_EVIDENCE_ONLY"
    )
    assert result.claim_ledger_update == "none"
    assert result.current_thread_closed is True
    assert "D1 promotion" in result.not_earned
    assert "Observer Theory equivalence theorem" in result.not_earned
    assert "global valid-coarse-graining criterion" in result.not_earned
    assert "cross-repo truth movement" in result.not_earned


def test_t478_anchor_guardrails_are_preserved():
    result = run_t489_analysis()
    anchor = result.t478_anchor

    assert anchor["artifact_id"] == (
        "T478-coarse-graining-budget-lattice-gate-v0.1"
    )
    assert anchor["anchor_ok"] is True
    assert anchor["gate_passed"] is True
    assert anchor["edge_monotonicity_passed"] is True
    assert anchor["join_path_independence_passed"] is True
    assert anchor["top_path_independence_passed"] is True
    assert anchor["hostile_controls_blocked_when_accessible"] is True
    assert anchor["top_budget_positive_controls_independent"] is True
    assert anchor["d1_promotion_earned"] is False
    assert anchor["observer_theory_identification_earned"] is False
    assert anchor["global_valid_coarse_graining_criterion_earned"] is False


def test_binary_and_task_label_restarts_are_rejected():
    result = run_t489_analysis()

    binary = _decision(result, "t467_binary_positive_control_upgrade")
    assert binary.admitted is False
    assert binary.route_label == "reject_t467_binary_positive_control_upgrade"
    assert binary.closes_current_thread is True
    assert "observer_budget_poset_declared" in binary.missing_requirements

    task_label = _decision(result, "task_label_certification_shortcut")
    assert task_label.admitted is False
    assert task_label.route_label == "reject_task_label_certification_shortcut"
    assert "certified_record_capability_declared" in task_label.missing_requirements
    assert "hostile_overread_controls" in task_label.missing_requirements


def test_lattice_and_boundary_overreads_are_rejected():
    result = run_t489_analysis()

    global_upgrade = _decision(result, "budget_lattice_global_criterion_upgrade")
    boundary = _decision(result, "boundary_pair_global_admission_overread")
    path_promotion = _decision(result, "lattice_path_independence_promotion_shortcut")

    assert global_upgrade.admitted is False
    assert global_upgrade.route_label == "reject_global_criterion_shortcut"
    assert "direct_observer_theory_taf_equivalence_theorem" in (
        global_upgrade.missing_requirements
    )

    assert boundary.admitted is False
    assert boundary.route_label == "reject_observer_index_overread"
    assert boundary.classification == "observer_index_overread_rejection"

    assert path_promotion.admitted is False
    assert path_promotion.route_label == (
        "reject_lattice_coherence_promotion_shortcut"
    )


def test_hostile_control_restarts_remain_blocked():
    result = run_t489_analysis()

    arithmetic = _decision(result, "cheap_arithmetic_xor_restart")
    identity = _decision(result, "microstate_label_restatement_restart")
    truth = _decision(result, "observer_creates_truth_restart")

    assert arithmetic.admitted is False
    assert arithmetic.route_label == "reject_cheap_arithmetic_or_xor_restart"
    assert "certified_record_capability_declared" in arithmetic.missing_requirements

    assert identity.admitted is False
    assert identity.route_label == "reject_microstate_or_label_restatement_restart"

    assert truth.admitted is False
    assert truth.route_label == "reject_observer_creates_truth_restart"
    assert truth.classification == "forbidden_posture_rejection"


def test_observer_theory_and_governance_shortcuts_are_blocked():
    result = run_t489_analysis()

    identity = _decision(result, "observer_theory_identity_shortcut")
    posture = _decision(result, "claim_public_posture_shortcut")

    assert identity.admitted is False
    assert identity.route_label == "reject_observer_theory_or_physics_shortcut"
    assert "direct_observer_theory_taf_equivalence_theorem" in (
        identity.missing_requirements
    )

    assert posture.admitted is False
    assert posture.route_label == "block_governance_or_public_posture_shortcut"
    assert posture.classification == "governance_boundary_block"


def test_undercontrolled_future_packet_is_rejected():
    result = run_t489_analysis()
    decision = _decision(result, "independent_capability_missing_hostile_controls")

    assert decision.admitted is False
    assert decision.route_label == "reject_missing_reopen_requirements"
    assert "hostile_overread_controls" in decision.missing_requirements
    assert decision.closes_current_thread is False


def test_future_reopen_targets_are_admitted_for_review_only():
    result = run_t489_analysis()

    capability = _decision(
        result, "future_independent_certified_record_capability_packet"
    )
    cost = _decision(
        result, "future_domain_native_cost_certifiability_theorem_packet"
    )
    equivalence = _decision(
        result, "future_direct_observer_theory_taf_equivalence_packet"
    )

    assert capability.admitted is True
    assert capability.route_label == (
        "admit_future_independent_capability_review_target"
    )
    assert capability.admitted_as_future_review_target is True
    assert capability.counts_as_thread_evidence is False

    assert cost.admitted is True
    assert cost.route_label == "admit_future_cost_certifiability_review_target"
    assert cost.counts_as_thread_evidence is False

    assert equivalence.admitted is True
    assert equivalence.route_label == (
        "admit_future_equivalence_theorem_review_target"
    )
    assert equivalence.counts_as_thread_evidence is False


def test_only_future_targets_are_admitted():
    result = run_t489_analysis()

    assert result.admitted_future_targets == (
        "future_independent_certified_record_capability_packet",
        "future_domain_native_cost_certifiability_theorem_packet",
        "future_direct_observer_theory_taf_equivalence_packet",
    )
    assert "budget_lattice_global_criterion_upgrade" in (
        result.rejected_restart_packets
    )
    assert "claim_public_posture_shortcut" in result.rejected_restart_packets


def test_future_reopen_minimum_preserves_t478_closure():
    result = run_t489_analysis()

    assert (
        "declare the observer-budget poset before relation selection"
        in result.future_reopen_minimum
    )
    assert (
        "preserve hostile cheap arithmetic, xor, label-restatement, microstate, and observer-creates-truth controls"
        in result.future_reopen_minimum
    )
    assert "cost/certifiability theorem" in result.not_earned
    assert "observer-creates-truth claim" in result.not_earned
