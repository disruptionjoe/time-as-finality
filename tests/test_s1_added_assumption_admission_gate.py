"""Tests for T464: S1 added-assumption admission gate."""

from models.s1_added_assumption_admission_gate import (
    S1AssumptionProposal,
    evaluate_proposal,
    requirement_audit,
    run,
)


def _by_id(result: dict, proposal_id: str) -> dict:
    return {
        item["proposal_id"]: item for item in result["proposal_evaluations"]
    }[proposal_id]


def test_overall_verdict_keeps_s1_and_t223_unchanged() -> None:
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["verdict"] == "S1_ADDED_ASSUMPTION_ADMISSION_GATE_BUILT_NO_S1_PROMOTION"
    assert verdict["all_s1_promoted_flags_false"] is True
    assert verdict["all_t223_reversed_flags_false"] is True
    assert verdict["s1_promotion"] == "none; T464 is an admission gate only"
    assert "T223 finite no-go remains" in verdict["t223_status"]
    assert result["claim_ledger_update"] == "none; no claim promotion or demotion"


def test_finite_enumeration_and_selected_survivors_do_not_reopen_s1() -> None:
    result = run()
    enumeration = _by_id(result, "more_uniform_ordinal_enumeration")
    selected = _by_id(result, "selected_nine_event_survivor_shortcut")

    assert enumeration["gate_action"] == "reject"
    assert enumeration["gate_label"] == "REJECTED_CLOSED_BY_T223_FINITE_ENSEMBLE_NO_GO"
    assert selected["gate_action"] == "reject"
    assert selected["gate_label"] == "REJECTED_SELECTED_SURVIVOR_NO_CONCENTRATION"
    assert enumeration["t223_reversed"] is False
    assert selected["s1_promoted"] is False


def test_screen_drift_and_t223_reversal_are_rejected() -> None:
    result = run()
    drift = _by_id(result, "screen_redefinition_after_tail")

    assert drift["gate_label"] == "REJECTED_SCREEN_DRIFT_AFTER_T223"
    assert "no_screen_drift_after_t223" in drift["missing_requirements"]

    reversal = evaluate_proposal(
        S1AssumptionProposal(
            proposal_id="direct_reversal",
            description="Reverse T223 without an added-assumption packet.",
            source="results/t54-ordinal-scaling-decisive-v0.1-results.md",
            requests_t223_reversal=True,
        )
    )
    assert reversal["gate_label"] == "REJECTED_T223_REVERSAL_REQUEST"
    assert reversal["t223_reversed"] is False


def test_added_assumption_must_be_declared_before_scoring() -> None:
    result = run()
    no_assumption = _by_id(result, "no_added_assumption_packet")
    post_hoc = _by_id(result, "post_hoc_selection_rule")

    assert no_assumption["gate_label"] == "REJECTED_NO_ADDED_ASSUMPTION"
    assert "added_assumption_type_supported" in no_assumption["missing_requirements"]
    assert post_hoc["gate_label"] == "REJECTED_POST_HOC_ASSUMPTION"
    assert "predeclared_before_scoring" in post_hoc["missing_requirements"]


def test_natural_measure_must_not_be_tail_tuned() -> None:
    result = run()
    tuned = _by_id(result, "tail_tuned_non_uniform_measure")

    assert tuned["gate_label"] == "REJECTED_CIRCULAR_TAIL_TUNING"
    assert "noncircular_not_tail_tuned" in tuned["missing_requirements"]


def test_added_assumption_needs_finite_audit_and_size_or_limit_evidence() -> None:
    result = run()
    no_audit = _by_id(result, "measure_without_finite_audit")
    single_size = _by_id(result, "single_size_positive_measure")

    assert no_audit["gate_label"] == "REJECTED_NO_FINITE_AUDIT_HANDLE"
    assert "finite_audit_on_existing_screens" in no_audit["missing_requirements"]
    assert single_size["gate_label"] == "REJECTED_NO_SIZE_OR_LIMIT_TEST"
    assert "tested_across_multiple_sizes_or_limit" in single_size["missing_requirements"]


def test_sprinkling_or_bridge_packets_must_name_lorentzian_constraints() -> None:
    result = run()
    sprinkling = _by_id(result, "sprinkling_law_without_lorentz_targets")

    assert sprinkling["gate_label"] == "REJECTED_NO_LORENTZIAN_CONSTRAINT_TARGETS"
    assert "lorentzian_constraints_named" in sprinkling["missing_requirements"]


def test_overclaim_promotion_and_external_actions_block() -> None:
    result = run()
    overclaim = _by_id(result, "continuum_bridge_overclaim")
    promotion = _by_id(result, "claim_promotion_shortcut")
    external = _by_id(result, "external_publication_shortcut")

    assert overclaim["gate_action"] == "stop"
    assert overclaim["gate_label"] == "BLOCKED_SPACETIME_OVERCLAIM"
    assert promotion["gate_action"] == "stop"
    assert promotion["gate_label"] == "BLOCKED_CLAIM_PROMOTION_REQUEST"
    assert external["gate_action"] == "stop"
    assert external["gate_label"] == "BLOCKED_EXTERNAL_ACTION_REQUIRED"


def test_synthetic_future_targets_are_admitted_for_review_only() -> None:
    result = run()
    verdict = result["overall_verdict"]

    assert verdict["admitted_future_target_ids"] == [
        "synthetic_natural_measure_review_target",
        "synthetic_continuum_bridge_review_target",
    ]
    assert verdict["admitted_targets_are_synthetic_only"] is True

    for proposal_id in verdict["admitted_future_target_ids"]:
        item = _by_id(result, proposal_id)
        assert item["gate_action"] == "admit_future_s1_review_target"
        assert item["gate_label"] == "ADMITTED_ADDED_ASSUMPTION_REVIEW_TARGET_NO_PROMOTION"
        assert item["admitted_future_target"] is True
        assert item["s1_promoted"] is False
        assert item["t223_reversed"] is False
        assert item["missing_requirements"] == []


def test_requirement_audit_allows_supported_types_only() -> None:
    good = S1AssumptionProposal(
        proposal_id="good",
        description="Supported type",
        source="synthetic",
        assumption_type="selection_rule",
        added_assumption_declared=True,
    )
    bad = S1AssumptionProposal(
        proposal_id="bad",
        description="Unsupported type",
        source="synthetic",
        assumption_type="geometry_slogan",
        added_assumption_declared=True,
    )

    assert requirement_audit(good)["added_assumption_type_supported"] is True
    assert requirement_audit(bad)["added_assumption_type_supported"] is False
