"""Tests for T445: region capability substrate-law big swing."""

import json

from models import region_capability_substrate_law_big_swing as t445


def artifact():
    return t445.run()


def pair(pair_id):
    return next(item for item in artifact()["pair_audits"] if item["pair_id"] == pair_id)


def t434_audit(candidate_id):
    return artifact()["t434_admission_audits"][candidate_id]


def test_artifact_identity_and_recorded_scope():
    result = artifact()

    assert result["artifact"] == t445.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Recorded-tier finite substrate-law pressure test only" in result["honest_ceiling"]
    assert "not a region-indexed discriminator success" in result["honest_ceiling"]


def test_main_pair_matches_all_r_supported_statistics_and_interventions():
    main = pair("main_boundary_compensator_pair")
    cert = main["region_equality_certificate"]

    assert cert["r_visible_projection_equal"] is True
    assert cert["observational_statistics_equal"] is True
    assert cert["interventional_statistics_equal"] is True
    assert cert["tested_r_interventions"] == list(t445.R_MENU)
    assert main["fixed_accounting_projection_equal"] is True


def test_boundary_menu_splits_but_r_only_menu_does_not():
    main = pair("main_boundary_compensator_pair")
    r_only = pair("r_only_no_split_control")

    assert r_only["menu_policy"] == "R_only"
    assert r_only["capability"]["differs"] is False
    assert r_only["transition_system_completion_equal"] is True

    assert main["menu_policy"] == "boundary"
    assert main["capability"]["differs"] is True
    assert main["capability"]["differing_fields"] == [
        "can_revise_final_verdict",
        "revision_blocked_reason",
        "available_compensator_charge",
    ]
    assert main["capability"]["left"]["can_revise_final_verdict"] is True
    assert main["capability"]["right"]["can_revise_final_verdict"] is False
    assert main["transition_system_completion_equal"] is False


def test_t434_admits_main_law_packet_and_rejects_transition_table_shortcut():
    main = t434_audit("main_z2_conservation_packet")
    restatement = t434_audit("transition_table_restatement_control")

    assert main["admitted"] is True
    assert (
        main["residue_label"]
        == "admitted_conservation_law_forced_transition_candidate"
    )
    assert main["law_package"]["reads_transition_relation"] is False
    assert main["law_package"]["declared_before_pair"] is True

    assert restatement["admitted"] is False
    assert restatement["residue_label"] == "not_admitted_transition_table_restatement"
    assert restatement["law_package"]["reads_transition_relation"] is True


def test_post_hoc_and_hidden_law_controls_are_rejected():
    post_hoc = t434_audit("post_hoc_law_control")
    hidden = t434_audit("hidden_label_law_control")

    assert post_hoc["admitted"] is False
    assert post_hoc["residue_label"] == "not_admitted_post_hoc_law"

    assert hidden["admitted"] is False
    assert hidden["residue_label"] == "blocked_hidden_label_law"


def test_reference_resource_lift_removes_the_boundary_split():
    reference = pair("reference_resource_lift_control")

    assert reference["menu_policy"] == "reference_resource"
    assert reference["capability"]["differs"] is False
    assert reference["capability"]["left"]["can_revise_final_verdict"] is True
    assert reference["capability"]["right"]["can_revise_final_verdict"] is True


def test_law_sector_completion_absorbs_the_recorded_result():
    result = artifact()
    absorber = result["absorber_audit"]["ordinary_joint_record_or_law_sector_completion"]
    factorization = absorber["factorization_check"]
    main = pair("main_boundary_compensator_pair")

    assert absorber["status"] == "absorbs_recorded_result"
    assert main["law_sector_completion_equal"] is False
    assert factorization["matched_law_sector_completion_pairs"] > 0
    assert factorization["violations"] == []
    assert factorization["capability_factors_through_law_sector_completion"] is True


def test_visible_region_control_and_hidden_selector_do_not_become_positives():
    visible = pair("r_visible_charge_control")
    hidden = pair("hidden_selector_control")

    assert visible["region_equality_certificate"]["r_visible_projection_equal"] is False
    assert visible["capability"]["differs"] is False

    assert hidden["hidden_selector_shortcut_attempt"] is True
    assert hidden["capability"]["differs"] is False


def test_overall_verdict_is_conservative():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t445.VERDICT
    assert verdict["t434_main_packet_admitted"] is True
    assert verdict["main_pair_r_statistics_equal"] is True
    assert verdict["main_pair_r_interventions_equal"] is True
    assert verdict["r_only_pair_splits"] is False
    assert verdict["boundary_pair_splits"] is True
    assert verdict["reference_resource_pair_splits"] is False
    assert verdict["transition_table_restatement_rejected"] is True
    assert verdict["law_sector_completion_absorbs"] is True
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
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
