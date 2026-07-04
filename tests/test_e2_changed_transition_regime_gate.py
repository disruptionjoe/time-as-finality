"""Tests for T444: E2 changed-transition regime gate."""

import json

from models import e2_changed_transition_regime_gate as t444


def artifact():
    return t444.run()


def classification(packet_id):
    return next(
        item
        for item in artifact()["classifications"]
        if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t444.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t438"].endswith("T438-e2-period-hardness-admission-gate-v0.1-results.md")
    assert "routing/admission gate only" in result["honest_ceiling"]


def test_imports_t438_separate_spec_guardrail():
    guard = artifact()["imported_t438_guardrail"]

    assert guard["t438_verdict"] == "E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION"
    assert "changed_public_transition_packet" in guard["routed_packet_ids"]
    assert "open_nonpermutation_packet" in guard["routed_packet_ids"]


def test_closed_public_permutation_routes_back_to_t438():
    item = classification("closed_public_permutation_period_packet")

    assert item["admitted_for_separate_spec_review"] is False
    assert item["route"] == "route_back_to_t438"
    assert item["label"] == "ROUTE_BACK_TO_T438_CLOSED_PUBLIC_PERMUTATION"


def test_post_hoc_and_hidden_transition_policies_are_blocked():
    post_hoc = classification("post_hoc_transition_swap_packet")
    hidden = classification("hidden_oracle_transition_packet")

    assert post_hoc["label"] == "BLOCKED_POST_HOC_OR_HIDDEN_TRANSITION_POLICY"
    assert hidden["label"] == "BLOCKED_POST_HOC_OR_HIDDEN_TRANSITION_POLICY"
    assert post_hoc["admitted_for_separate_spec_review"] is False
    assert hidden["admitted_for_separate_spec_review"] is False


def test_e1_and_symmetric_complexity_packets_do_not_admit_as_e2():
    thermo = classification("thermodynamic_transition_cost_packet")
    complexity = classification("brown_susskind_complexity_packet")

    assert thermo["label"] == "NOT_E2_THERMODYNAMIC_OR_ERASURE_E1"
    assert complexity["label"] == "NOT_E2_SYMMETRIC_COMPLEXITY_GROWTH"


def test_unknown_transition_is_not_a_capability_boundary():
    item = classification("pure_unknown_transition_packet")

    assert item["label"] == "REJECTED_EPISTEMIC_IGNORANCE_NOT_CAPABILITY_BOUNDARY"
    assert "Mere ignorance" in item["reason"]


def test_changed_transition_requires_frozen_evidence():
    item = classification("unfrozen_transition_evidence_packet")

    assert item["label"] == "REJECTED_UNFROZEN_TRANSITION_EVIDENCE"
    assert item["admitted_for_separate_spec_review"] is False


def test_predeclared_changed_transition_packet_is_admitted_only_as_separate_spec():
    item = classification("predeclared_changed_transition_packet")

    assert item["admitted_for_separate_spec_review"] is True
    assert item["route"] == "admitted_as_separate_spec_target"
    assert item["label"] == "ADMITTED_CHANGED_TRANSITION_SEPARATE_SPEC_NO_D2_DECISION"
    assert "separate-regime review target" in item["reason"]


def test_open_nonpermutation_requires_a_dynamics_law():
    item = classification("open_nonpermutation_no_law_packet")

    assert item["label"] == "REJECTED_NO_OPEN_DYNAMICS_LAW"
    assert item["admitted_for_separate_spec_review"] is False


def test_resource_completion_absorbs_open_packet():
    item = classification("resource_completion_absorbed_open_packet")

    assert item["label"] == "REJECTED_RESOURCE_OR_ENVIRONMENT_COMPLETION_ABSORBS"
    assert item["admitted_for_separate_spec_review"] is False


def test_predeclared_open_packet_is_admitted_only_as_separate_spec():
    item = classification("predeclared_open_nonpermutation_packet")

    assert item["admitted_for_separate_spec_review"] is True
    assert item["route"] == "admitted_as_separate_spec_target"
    assert item["label"] == "ADMITTED_OPEN_NONPERMUTATION_SEPARATE_SPEC_NO_D2_DECISION"
    assert "separate-regime review target" in item["reason"]


def test_overall_verdict_keeps_d2_and_claims_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t444.VERDICT
    assert verdict["admitted_packet_ids"] == [
        "predeclared_changed_transition_packet",
        "predeclared_open_nonpermutation_packet",
    ]
    assert verdict["routed_back_to_t438_packet_ids"] == [
        "closed_public_permutation_period_packet"
    ]
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
