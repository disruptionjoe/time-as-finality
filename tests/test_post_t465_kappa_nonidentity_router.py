"""Tests for T466: post-T465 kappa non-identity router."""

from __future__ import annotations

from models.post_t465_kappa_nonidentity_router import (
    VERDICT,
    KappaPacketProposal,
    evaluate_packet,
    run,
)


def _evaluations_by_id():
    result = run()
    return {row["proposal_id"]: row for row in result["evaluations"]}


def test_overall_verdict_blocks_promotion_and_names_future_target_only():
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == VERDICT
    assert verdict["current_catalogue_promoted"] is False
    assert verdict["t224_promotion_earned"] is False
    assert verdict["genre_agnostic_theorem_earned"] is False
    assert verdict["claim_ledger_update"] == "none"
    assert verdict["admitted_future_target_ids"] == [
        "synthetic_future_nonidentity_packet"
    ]
    assert verdict["admitted_targets_are_synthetic_only"] is True


def test_existing_finite_catalogue_is_reencoding_only():
    rows = _evaluations_by_id()
    row = rows["current_t224_t244_catalogue"]

    assert row["admitted_future_target"] is False
    assert row["route_label"] == "FINITE_REENCODING_CATALOGUE_HELD_NO_PROMOTION"
    assert "synthetic_nu_written_from_native_rank" in row["blockers"]


def test_ab_contextuality_routes_to_t465_absorber():
    rows = _evaluations_by_id()
    row = rows["ab_contextuality_after_t465"]

    assert row["admitted_future_target"] is False
    assert row["route_label"] == "T465_ABSORBER_REENCODING_NOT_PREDICTION"
    assert "same_support_global_section_rank_reencoding" in row["blockers"]


def test_shortcuts_are_blocked_before_review():
    rows = _evaluations_by_id()

    assert rows["shared_derivation_cap_shortcut"]["route_label"] == (
        "SHARED_DERIVATION_SHORTCUT"
    )
    assert rows["native_witness_calls_kappa"]["route_label"] == (
        "NATIVE_WITNESS_NOT_INDEPENDENT"
    )
    assert rows["presence_only_packet"]["route_label"] == (
        "NONIDENTITY_BURDEN_NOT_MET"
    )
    assert rows["claim_promotion_shortcut"]["route_label"] == (
        "FORBIDDEN_POSTURE_OR_CLAIM_MOVE"
    )


def test_no_falsifier_or_nonindependent_source_does_not_pass():
    proposal = KappaPacketProposal(
        proposal_id="bad_pair",
        description="No falsifier and source rank chosen after target rank.",
        source_kappa=2,
        native_target_rank=2,
        nu_kappa=2,
        native_witness_kind="bad paired fixture",
        source_rank_independent_of_target_construction=False,
        native_witness_independent_of_compute_kappa=True,
        predeclared_mapping_before_target_measurement=True,
        has_mismatch_or_negative_control=False,
        no_shared_derivation_with_source=True,
        rank_load_bearing=True,
    )

    evaluation = evaluate_packet(proposal)

    assert evaluation.admitted_future_target is False
    assert evaluation.route_label == "NONIDENTITY_BURDEN_NOT_MET"
    assert "source_rank_not_independent_of_target_construction" in evaluation.blockers
    assert "no_mismatch_or_negative_control" in evaluation.blockers


def test_synthetic_future_nonidentity_packet_is_admitted_for_review_only():
    rows = _evaluations_by_id()
    row = rows["synthetic_future_nonidentity_packet"]

    assert row["admitted_future_target"] is True
    assert row["decision"] == "admitted_for_review"
    assert row["route_label"] == "SYNTHETIC_NONIDENTITY_REVIEW_TARGET_ONLY"
    assert row["blockers"] == []
    assert row["allowed_action"] == "future review target only; no claim movement"


def test_future_packet_minimum_keeps_t465_burden_explicit():
    result = run()
    minimum = set(result["future_packet_minimum"])

    assert "source rank fixed independently before target construction" in minimum
    assert "target native witness independent of compute_kappa" in minimum
    assert (
        "target native witness not identical to same support/global-section rank"
        in minimum
    )
    assert "synthetic nu not written from the native rank by construction" in minimum
    assert "review only; no claim movement from packet shape alone" in minimum
