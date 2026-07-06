"""Tests for T454: integrated E3-region packet swing."""

import json

from models import integrated_e3_region_packet_swing as t454


def artifact():
    return t454.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def main_packet():
    return evaluation("main_integrated_nonwrapping_e3_region_packet")


def test_artifact_identity_and_recorded_scope():
    result = artifact()

    assert result["artifact"] == t454.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t453"].endswith(
        "T453-e3-to-region-nonadmissibility-adapter-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Recorded-tier finite toy integration only" in result["honest_ceiling"]
    assert "not a WAY theorem" in result["honest_ceiling"]


def test_main_pair_matches_all_r_supported_statistics_and_interventions():
    main = main_packet()
    cert = main["pair_audit"]["region_equality_certificate"]

    assert cert["r_visible_projection_equal"] is True
    assert cert["observational_statistics_equal"] is True
    assert cert["interventional_statistics_equal"] is True
    assert cert["tested_r_interventions"] == list(t454.R_MENU)


def test_main_pair_splits_only_under_boundary_menu():
    main = main_packet()
    r_only = main["pair_audit"]["r_only_capability"]
    boundary = main["pair_audit"]["boundary_capability"]

    assert r_only["differs"] is False
    assert boundary["differs"] is True
    assert boundary["differing_fields"] == [
        "can_revise_final_verdict",
        "revision_blocked_reason",
        "available_boundary_charge",
    ]
    assert boundary["left"]["can_revise_final_verdict"] is True
    assert boundary["right"]["can_revise_final_verdict"] is False


def test_main_completion_is_tied_to_t447_no_go_certificate():
    main = main_packet()
    completion = main["completion_audit"]
    certificate = completion["certificate"]

    assert main["admitted_review_target"] is True
    assert main["integrated_label"] == (
        "ADMITTED_INTEGRATED_E3_REGION_REVIEW_TARGET_NO_PROMOTION"
    )
    assert completion["completion_label"] == (
        "NAMED_COMPLETION_BLOCKED_BY_FINITE_NONWRAPPING_E3_NO_GO"
    )
    assert (
        completion["completion_physically_nonadmissible_under_declared_policy"]
        is True
    )
    assert certificate["reference_model"] == "finite_nonwrapping_charge_ladder"
    assert certificate["has_nonzero_unit_modulus_eigenvector"] is False
    assert "nilpotent" in certificate["proof"]


def test_main_packet_passes_t452_requirements_but_stays_review_target():
    main = main_packet()
    checks = main["t452_requirement_check"]["checks"]

    assert main["t452_requirement_check"]["all_checks_pass"] is True
    assert all(checks.values())
    assert checks["exact_witness_targets_named_completion"] is True
    assert checks["completion_physically_nonadmissible"] is True
    assert artifact()["overall_verdict"]["region_discriminator_success"] is False


def test_reference_and_resource_controls_route_away():
    cyclic = evaluation("cyclic_reference_completion_control")
    consumed = evaluation("consumed_battery_completion_control")
    ideal = evaluation("ideal_reference_completion_control")

    assert cyclic["admitted_review_target"] is False
    assert (
        cyclic["integrated_label"]
        == "COMPLETION_RESTORED_BY_CYCLIC_REFERENCE_CONTROL"
    )
    assert cyclic["completion_audit"]["certificate"]["reference_model"] == (
        "finite_cyclic_charge_reference"
    )
    assert cyclic["completion_audit"]["certificate"][
        "has_nonzero_unit_modulus_eigenvector"
    ] is True

    assert consumed["admitted_review_target"] is False
    assert consumed["integrated_label"] == (
        "RESOURCE_COMPLETION_ROUTES_AWAY_FROM_EXACT_CATALYTIC_E3"
    )

    assert ideal["admitted_review_target"] is False
    assert ideal["integrated_label"] == (
        "IDEAL_REFERENCE_ROUTES_TO_IDEAL_OR_LIMIT_POLICY"
    )


def test_description_only_completion_remains_e0_ceiling():
    description = evaluation("description_only_completion_control")
    ceiling = artifact()["description_factorization_ceiling"]

    assert description["admitted_review_target"] is False
    assert description["integrated_label"] == (
        "E0_DESCRIPTION_COMPLETION_ABSORBS_NO_E3_WITNESS"
    )
    assert ceiling["violations"] == []
    assert (
        ceiling["capability_factors_through_boundary_charge_description"] is True
    )


def test_post_hoc_hidden_missing_and_no_split_controls_are_rejected():
    post_hoc = evaluation("post_hoc_completion_policy_control")
    hidden = evaluation("hidden_label_completion_policy_control")
    missing_region = evaluation("missing_region_pair_control")
    missing_negative = evaluation("missing_negative_control")
    no_split = evaluation("matched_boundary_no_split_control")

    assert post_hoc["integrated_label"] == "BLOCKED_POST_HOC_COMPLETION_POLICY"
    assert hidden["integrated_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
    assert missing_region["integrated_label"] == (
        "NOT_REGION_INDEXED_BASE_PACKET_MISSING"
    )
    assert missing_negative["integrated_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"
    assert no_split["integrated_label"] == (
        "NOT_ADMITTED_NO_BOUNDARY_CAPABILITY_SPLIT"
    )


def test_overall_verdict_is_conservative():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t454.VERDICT
    assert verdict["main_candidate_admitted"] is True
    assert verdict["main_candidate_label"] == (
        "ADMITTED_INTEGRATED_E3_REGION_REVIEW_TARGET_NO_PROMOTION"
    )
    assert verdict["admitted_candidate_ids"] == [
        "main_integrated_nonwrapping_e3_region_packet"
    ]
    assert verdict["region_discriminator_success"] is False
    assert verdict["description_completion_still_explains_boundary_state"] is True
    assert verdict["claim_ledger_update"] == "none; no claim promotion"


def test_result_is_json_serializable_and_avoids_promotion_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    combined = json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "region-indexed discriminator success proved",
        "real physics law proved",
        "WAY theorem proved",
        "quantum physics theorem proved",
        "GU adapter revived",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
