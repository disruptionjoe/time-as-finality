"""Tests for T460: post-T459 Direction-A restart router."""

import json

from models import post_t459_direction_a_restart_router as t460


def artifact():
    return t460.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t460.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t459"].endswith(
        "T459-policy-independent-theorem-supply-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == (
        "none; no claim promotion or claim demotion"
    )
    assert "Routing/admission gate only" in result["honest_ceiling"]


def test_t459_import_keeps_current_route_closed():
    result = artifact()
    imported = result["t459_import_summary"]

    assert imported["verdict"] == t460.t459.VERDICT
    assert imported["current_route_demoted_to_negative_guardrail"] is True
    assert imported["current_artifacts_admitted_for_stronger_posture"] is False
    assert result["overall_verdict"]["current_route_closed"] is True
    assert result["overall_verdict"]["current_route_action"] == "do_not_reopen"


def test_current_class_and_minor_variation_are_not_reopened():
    current = evaluation("current_t454_t459_integrated_route")
    variation = evaluation("minor_boundary_resource_variation")

    assert current["gate_label"] == (
        "CLOSED_CURRENT_T454_T459_CLASS_NEGATIVE_GUARDRAIL"
    )
    assert current["router_action"] == "do_not_reopen"
    assert current["admitted_future_target"] is False

    assert variation["gate_label"] == "NOT_ADMITTED_NO_NEW_PACKET_CLASS"
    assert "new_packet_class_declared" in variation["missing_requirements"]
    assert "does_not_use_current_t454_t459_class" in variation["missing_requirements"]


def test_restart_controls_fail_for_the_right_reasons():
    no_region = evaluation("theorem_without_region_packet")
    no_theorem = evaluation("new_packet_without_independent_theorem")
    post_hoc = evaluation("post_hoc_new_packet_theorem")
    description = evaluation("new_packet_description_factorizes")
    reference = evaluation("new_packet_reference_policy_fragile")
    untargeted = evaluation("untargeted_independent_theorem_packet")

    assert no_region["gate_label"] == "NOT_ADMITTED_NO_REGION_PACKET"
    assert "region_packet_present" in no_region["missing_requirements"]

    assert no_theorem["gate_label"] == "NOT_ADMITTED_T459_NO_INDEPENDENT_THEOREM"
    assert "independent_theorem_supplied" in no_theorem["missing_requirements"]

    assert post_hoc["gate_label"] == "NOT_ADMITTED_POST_HOC_THEOREM"
    assert "theorem_declared_before_pair" in post_hoc["missing_requirements"]

    assert description["gate_label"] == (
        "NOT_ADMITTED_T457_DESCRIPTION_COMPLETION_BLOCKER"
    )
    assert "clears_description_completion_blocker" in description[
        "missing_requirements"
    ]

    assert reference["gate_label"] == "NOT_ADMITTED_T458_REFERENCE_POLICY_FRAGILITY"
    assert "handles_reference_policy_variants" in reference["missing_requirements"]

    assert untargeted["gate_label"] == "NOT_ADMITTED_THEOREM_NOT_TIED_TO_COMPLETION"
    assert "theorem_targets_named_completion" in untargeted["missing_requirements"]


def test_adjacent_mode_and_cross_repo_candidates_are_routed_or_blocked():
    e1 = evaluation("e1_family_limit_packet")
    e2 = evaluation("e2_changed_transition_packet")
    cross_repo = evaluation("cross_repo_adapter_shortcut")

    assert e1["gate_label"] == "ROUTE_TO_EXISTING_MODE_GATE_NOT_DIRECTION_A_RESTART"
    assert e1["router_action"] == "route_to_T441_E1_family_limit_packet_gate"
    assert e1["admitted_future_target"] is False

    assert e2["gate_label"] == "ROUTE_TO_EXISTING_MODE_GATE_NOT_DIRECTION_A_RESTART"
    assert e2["router_action"] == "route_to_T438_T444_E2_packet_gates"
    assert e2["admitted_future_target"] is False

    assert cross_repo["gate_label"] == "BLOCKED_CROSS_REPO_TRUTH_REQUEST"
    assert cross_repo["router_action"] == "stop"


def test_only_synthetic_new_class_is_admitted():
    result = artifact()
    synthetic = evaluation("synthetic_new_independent_theorem_packet")
    missing_control = evaluation("synthetic_missing_negative_control")

    assert synthetic["admitted_future_target"] is True
    assert synthetic["gate_label"] == (
        "ADMITTED_NEW_DIRECTION_A_RESTART_TARGET_NO_PROMOTION"
    )
    assert synthetic["missing_requirements"] == []

    assert missing_control["gate_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
    assert "negative_control_present" in missing_control["missing_requirements"]

    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_new_independent_theorem_packet"
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True
    assert result["overall_verdict"][
        "current_artifacts_admitted_for_stronger_posture"
    ] is False


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "claim demotion follows",
        "region-indexed discriminator success proved",
        "real substrate law proved",
        "WAY theorem proved",
        "quantum physics theorem proved",
        "GU adapter revived",
        "public posture authorized",
        "cross-repo support proved",
    )
    assert all(term not in combined for term in banned)
