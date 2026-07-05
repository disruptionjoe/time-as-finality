"""Tests for T452: law-sector nonadmissibility gate."""

import json

from models import law_sector_nonadmissibility_gate as t452


def artifact():
    return t452.run()


def evaluation(packet_id):
    return next(
        item for item in artifact()["packet_evaluations"] if item["packet_id"] == packet_id
    )


def test_artifact_identity_and_recorded_scope():
    result = artifact()

    assert result["artifact"] == t452.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Recorded-tier admission gate only" in result["honest_ceiling"]
    assert "not claim-ledger movement" in result["honest_ceiling"]


def test_current_t445_packet_is_not_admitted():
    current = evaluation("current_t445_z2_law_packet")

    assert current["admitted"] is False
    assert current["residue_label"] == "NOT_ADMITTED_COMPLETION_MERELY_OUTSIDE_R"
    assert current["packet"]["clears_t434_law_admission"] is True
    assert current["packet"]["r_statistics_and_interventions_matched"] is True
    assert current["packet"]["boundary_menu_splits_capability"] is True
    assert current["packet"]["completion_merely_hidden_from_r"] is True
    assert "T445 absorber" in current["reason"]


def test_reference_resource_completion_absorbs_the_split():
    reference = evaluation("t445_reference_resource_lift_control")

    assert reference["admitted"] is False
    assert reference["residue_label"] == "RESOURCE_LIFT_ABSORBS_LAW_SECTOR_SPLIT"
    assert reference["packet"]["a2_reference_restores_completion"] is True


def test_t434_failure_modes_remain_rejected():
    restatement = evaluation("transition_table_restatement_control")
    post_hoc = evaluation("post_hoc_completion_policy_control")
    hidden = evaluation("hidden_label_completion_policy_control")

    assert restatement["admitted"] is False
    assert restatement["residue_label"] == "NOT_ADMITTED_TRANSITION_TABLE_RESTATEMENT"

    assert post_hoc["admitted"] is False
    assert post_hoc["residue_label"] == "NOT_ADMITTED_POST_HOC_NONADMISSIBILITY_POLICY"

    assert hidden["admitted"] is False
    assert hidden["residue_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"


def test_cost_only_and_missing_a2_do_not_pass():
    cost = evaluation("family_cost_only_packet")
    missing_a2 = evaluation("missing_a2_resource_lift_audit")

    assert cost["admitted"] is False
    assert cost["residue_label"] == "ROUTES_TO_E1_E2_NOT_SINGLE_PACKET_NONADMISSIBILITY"

    assert missing_a2["admitted"] is False
    assert missing_a2["residue_label"] == "NOT_ADMITTED_A2_RESOURCE_LIFT_UNTESTED"


def test_exact_witness_and_negative_control_are_required():
    no_witness = evaluation("no_exact_nonadmissibility_witness")
    no_control = evaluation("synthetic_missing_negative_control")

    assert no_witness["admitted"] is False
    assert no_witness["residue_label"] == "NOT_ADMITTED_NO_EXACT_NONADMISSIBILITY_WITNESS"

    assert no_control["admitted"] is False
    assert no_control["residue_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"


def test_only_synthetic_full_packet_is_admitted_as_future_target():
    result = artifact()
    synthetic = evaluation("synthetic_exact_nonadmissibility_packet")

    assert synthetic["admitted"] is True
    assert (
        synthetic["residue_label"]
        == "ADMITTED_LAW_SECTOR_NONADMISSIBILITY_REVIEW_TARGET_NO_PROMOTION"
    )
    assert synthetic["packet"]["synthetic_control_only"] is True
    assert result["overall_verdict"]["admitted_packet_ids"] == [
        "synthetic_exact_nonadmissibility_packet"
    ]
    assert result["overall_verdict"]["admitted_packets_are_synthetic_only"] is True


def test_overall_verdict_is_conservative():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t452.VERDICT
    assert verdict["current_t445_admitted"] is False
    assert verdict["current_t445_label"] == "NOT_ADMITTED_COMPLETION_MERELY_OUTSIDE_R"
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "current T445 packet does not pass" in verdict["reading"]


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
