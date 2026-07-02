"""Tests for T403: Same-domain finality-lock screen."""

import json

import pytest

from models.same_domain_finality_lock_screen import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_same_domain_finality_lock_screen,
)


@pytest.fixture(scope="module")
def res():
    return run_same_domain_finality_lock_screen()


def _pair(res, pair_id):
    for item in res["pair_audits"]:
        if item["pair_id"] == pair_id:
            return item
    raise AssertionError(f"missing pair {pair_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["residue_label"] == "same_domain_finality_state_split_absorbed"
    assert res["source_artifact"] == "T402-causal-domain-boundary-forcing-screen-v0.1"


def test_imported_causal_domain_signature_matches_t402_shape(res):
    geometry = res["causal_domain_signature"]
    assert geometry["source_artifact"] == "T402-causal-domain-boundary-forcing-screen-v0.1"
    assert geometry["R_and_B_are_spacelike"] is True
    assert geometry["verdict_in_common_future"] is True
    assert geometry["R_only_domain_contains_verdict"] is False
    assert geometry["B_only_domain_contains_verdict"] is False
    assert geometry["RB_joint_domain_contains_verdict"] is True


def test_main_pair_matches_causal_and_joint_data_but_splits_finality_capability(res):
    main = _pair(res, "same_domain_finality_lock_pair")
    assert main["visible_projection_equal"] is True
    assert main["same_causal_domain_data"] is True
    assert main["same_joint_payload"] is True
    assert main["same_verdict_payload"] is True
    assert main["same_revision_budget"] is True
    assert main["same_operation_menu"] is True
    assert main["capability"]["differs"] is True
    assert main["capability"]["differing_fields"] == ["can_revise_final_verdict"]
    assert main["capability"]["left"]["can_revise_final_verdict"] is True
    assert main["capability"]["right"]["can_revise_final_verdict"] is False
    assert main["residue_label"] == "absorbed_by_finality_state_completion"


def test_finality_state_completion_restores_factorization(res):
    main = _pair(res, "same_domain_finality_lock_pair")
    completion = main["state_completion"]
    assert completion["restores_factorization"] is True
    assert completion["differing_fields"] == ["finality_state"]
    assert completion["left"]["finality_state"] == "provisional"
    assert completion["right"]["finality_state"] == "sealed"


def test_controls_separate_the_absorbers(res):
    matched = _pair(res, "matched_finality_control")
    assert matched["visible_projection_equal"] is True
    assert matched["capability"]["differs"] is False
    assert matched["residue_label"] == "no_capability_split"

    joint = _pair(res, "joint_input_completion_control")
    assert joint["same_causal_domain_data"] is True
    assert joint["same_joint_payload"] is False
    assert joint["capability"]["differing_fields"] == ["verdict_payload"]
    assert joint["residue_label"] == "absorbed_by_causal_or_joint_input_completion"

    menu = _pair(res, "operation_menu_completion_control")
    assert menu["same_joint_payload"] is True
    assert menu["same_operation_menu"] is False
    assert menu["capability"]["differing_fields"] == ["can_revise_final_verdict"]
    assert menu["residue_label"] == "absorbed_by_operation_menu_completion"

    hidden = _pair(res, "hidden_label_shortcut_control")
    assert hidden["visible_projection_equal"] is True
    assert hidden["hidden_label_shortcut_attempt"] is True
    assert hidden["residue_label"] == "blocked_hidden_label_shortcut"


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["causal_reachability_and_domain_of_dependence"]["status"] == "matched_not_explanatory"
    assert absorber["ordinary_joint_input_completion"]["status"] == "matched_not_explanatory"
    assert absorber["operation_menu_completion"]["status"] == "matched_not_explanatory_for_main_pair"
    assert absorber["finality_state_completion"]["status"] == "absorbs"
    assert absorber["hidden_label_or_class_marker"]["status"] == "blocked"
    assert absorber["claim_promotion"]["status"] == "blocked"


def test_summary_names_only_main_pair_as_same_domain_split(res):
    summary = res["summary"]
    assert summary["same_domain_split_cases"] == ["same_domain_finality_lock_pair"]
    assert (
        summary["absorbed_cases"]["same_domain_finality_lock_pair"]
        == "absorbed_by_finality_state_completion"
    )
    assert (
        res["main_pair_summary"]["differing_capability_fields"]
        == ["can_revise_final_verdict"]
    )


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("new physics", "claim promotion", "theorem proved", "law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
