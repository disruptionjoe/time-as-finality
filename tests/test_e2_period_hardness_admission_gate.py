"""Tests for T438: E2 period-hardness admission gate."""

import json

from models import e2_period_hardness_admission_gate as t438


def artifact():
    return t438.run()


def classification(packet_id):
    return next(
        item for item in artifact()["classifications"] if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t438.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t419"].endswith("T419-computational-arrow-of-time-v0.1-results.md")
    assert result["sources"]["t420"].endswith("T420-finite-cycle-anti-relabel-gate-v0.1-results.md")
    assert "admission gate only" in result["honest_ceiling"]


def test_imports_t420_guardrail_for_t419_orbit():
    guard = artifact()["t420_imported_guardrail"]

    assert guard["t419_seed_orbit"] == [4, 16, 25, 9]
    assert guard["public_predecessor_label"] == 9
    assert guard["max_forward_steps_to_predecessor"] == 3
    assert guard["every_predecessor_recovered_within_bound"] is True


def test_t419_finite_public_cycle_is_rejected_by_t420():
    item = classification("t419_qr77_finite_public_cycle")

    assert item["admitted_for_future_d2_work"] is False
    assert item["label"] == "REJECTED_T420_PUBLIC_CYCLE_ABSORBS_ARROW"
    assert "public forward iteration recovers" in item["reason"]


def test_bounded_nonrecovery_is_rejected_without_period_hardness():
    item = classification("long_cycle_bounded_nonrecovery_only")

    assert item["admitted_for_future_d2_work"] is False
    assert item["label"] == "REJECTED_BOUNDED_NONRECOVERY_NOT_EVIDENCE"
    assert "Bounded search failure" in item["reason"]


def test_point_inversion_only_demotes_to_t417_static_boundary():
    item = classification("point_sqrt_hardness_static_relabel")

    assert item["label"] == "REJECTED_STATIC_T417_RELABEL"
    assert "T417" in item["reason"]
    assert item["admitted_for_future_d2_work"] is False


def test_other_absorbers_and_blockers_do_not_admit():
    assert classification("single_instance_hard_theorem_claim")["label"] == (
        "REJECTED_SINGLE_INSTANCE_FINITE_CRACKABLE"
    )
    assert classification("thermodynamic_reversal_cost_packet")["label"] == (
        "NOT_E2_THERMODYNAMIC_OR_ERASURE_E1"
    )
    assert classification("brown_susskind_complexity_growth_packet")["label"] == (
        "NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH"
    )
    assert classification("post_hoc_period_policy_packet")["label"] == (
        "BLOCKED_POST_HOC_OR_HIDDEN_SELECTOR"
    )


def test_changed_transition_and_open_packets_are_routed_not_admitted():
    changed = classification("changed_public_transition_packet")
    open_packet = classification("open_nonpermutation_packet")

    assert changed["route"] == "separate_spec_required"
    assert changed["admitted_for_future_d2_work"] is False
    assert open_packet["route"] == "separate_spec_required"
    assert open_packet["admitted_for_future_d2_work"] is False


def test_predeclared_period_hardness_packet_is_admitted_only_as_future_target():
    item = classification("predeclared_period_hardness_family_packet")

    assert item["admitted_for_future_d2_work"] is True
    assert item["route"] == "admitted_as_future_target"
    assert item["label"] == "ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION"
    assert "future E2 redesign target" in item["reason"]


def test_overall_verdict_keeps_d2_and_claims_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t438.VERDICT
    assert verdict["admitted_packet_ids"] == ["predeclared_period_hardness_family_packet"]
    assert "changed_public_transition_packet" in verdict["routed_packet_ids"]
    assert verdict["d2_decision"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "D2 redesigned",
        "D2 abandoned",
        "claim promotion follows",
        "crypto theorem proved",
        "physics claim proved",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
