"""Tests for T405: Physical-latch finality-lock screen."""

import json

import pytest

from models.physical_latch_finality_lock_screen import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_physical_latch_finality_lock_screen,
)


@pytest.fixture(scope="module")
def res():
    return run_physical_latch_finality_lock_screen()


def _pair(res, pair_id):
    for item in res["pair_audits"]:
        if item["pair_id"] == pair_id:
            return item
    raise AssertionError(f"missing pair {pair_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["source_artifact"] == "T403-same-domain-finality-lock-screen-v0.1"
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["residue_label"] == "physical_latch_substrate_split_absorbed"


def test_imported_t403_causal_signature_is_preserved(res):
    geometry = res["causal_domain_signature"]
    assert geometry["source_artifact"] == "T402-causal-domain-boundary-forcing-screen-v0.1"
    assert geometry["R_and_B_are_spacelike"] is True
    assert geometry["verdict_in_common_future"] is True
    assert geometry["RB_joint_domain_contains_verdict"] is True


def test_main_pair_matches_fixed_projection_but_splits_revision_capability(res):
    main = _pair(res, "physical_latch_finality_lock_pair")
    assert main["visible_causal_payload_equal"] is True
    assert main["fixed_accounting_projection_equal"] is True
    assert main["same_joint_payload"] is True
    assert main["same_verdict_payload"] is True
    assert main["same_revision_budget"] is True
    assert main["same_operation_menu"] is True
    assert main["same_latch_support_without_topology"] is True
    assert main["absorber_mismatch_fields"] == []
    assert main["derived_lock_states"] == {
        "left": "physically_rewritable",
        "right": "physically_sealed",
    }
    assert main["capability"]["differs"] is True
    assert main["capability"]["differing_fields"] == ["can_revise_final_verdict"]
    assert main["capability"]["left"]["can_revise_final_verdict"] is True
    assert main["capability"]["right"]["can_revise_final_verdict"] is False
    assert main["residue_label"] == "absorbed_by_physical_latch_substrate_completion"


def test_latch_substrate_completion_restores_factorization(res):
    main = _pair(res, "physical_latch_finality_lock_pair")
    completion = main["latch_substrate_completion"]
    assert completion["restores_factorization"] is True
    assert completion["differing_fields"] == [
        "physical_latch",
        "derived_lock_state",
    ]
    assert (
        completion["left"]["physical_latch"]["material_topology"]
        == "rewritable_gate"
    )
    assert completion["right"]["physical_latch"]["material_topology"] == "fused_gate"


def test_controls_separate_absorber_classes(res):
    matched = _pair(res, "matched_latch_control")
    assert matched["fixed_accounting_projection_equal"] is True
    assert matched["capability"]["differs"] is False
    assert matched["residue_label"] == "no_capability_split"

    resource = _pair(res, "resource_accounting_control")
    assert resource["fixed_accounting_projection_equal"] is False
    assert {"erased_bits", "beta_work_floor", "blank_capacity_delta"} <= set(
        resource["absorber_mismatch_fields"]
    )
    assert resource["residue_label"] == "absorbed_by_resource_accounting"

    provenance = _pair(res, "provenance_completion_control")
    assert provenance["absorber_mismatch_fields"] == ["provenance_state"]
    assert provenance["residue_label"] == "absorbed_by_provenance_completion"

    control = _pair(res, "control_completion_control")
    assert control["absorber_mismatch_fields"] == ["reversible_control"]
    assert control["residue_label"] == "absorbed_by_control_completion"

    boundary = _pair(res, "boundary_completion_control")
    assert boundary["absorber_mismatch_fields"] == ["boundary_access"]
    assert boundary["residue_label"] == "absorbed_by_boundary_completion"


def test_shortcuts_do_not_count(res):
    hidden = _pair(res, "hidden_label_shortcut_control")
    assert hidden["fixed_accounting_projection_equal"] is True
    assert hidden["hidden_label_shortcut_attempt"] is True
    assert hidden["residue_label"] == "blocked_hidden_label_shortcut"

    stipulated = _pair(res, "stipulated_finality_label_control")
    assert stipulated["fixed_accounting_projection_equal"] is True
    assert stipulated["stipulated_finality_label_attempt"] is True
    assert stipulated["capability"]["differs"] is False
    assert stipulated["residue_label"] == "blocked_stipulated_finality_label"


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["causal_reachability_and_domain_of_dependence"]["status"] == "matched_not_explanatory"
    assert absorber["ordinary_joint_input_completion"]["status"] == "matched_not_explanatory"
    assert absorber["stipulated_finality_state"]["status"] == "blocked"
    assert (
        absorber["fixed_accounting_resource_provenance_control_boundary"]["status"]
        == "matched_not_explanatory_for_main_pair"
    )
    assert absorber["physical_latch_substrate_completion"]["status"] == "absorbs"
    assert absorber["hidden_label_or_class_marker"]["status"] == "blocked"
    assert absorber["claim_promotion"]["status"] == "blocked"


def test_summary_names_only_main_pair_as_same_fixed_accounting_split(res):
    summary = res["summary"]
    assert summary["same_fixed_accounting_split_cases"] == [
        "physical_latch_finality_lock_pair"
    ]
    assert (
        summary["absorbed_cases"]["physical_latch_finality_lock_pair"]
        == "absorbed_by_physical_latch_substrate_completion"
    )
    assert res["main_pair_summary"]["absorber_mismatch_fields"] == []


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("claim promotion follows", "theorem proved", "new law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)
    assert "new physics" in res["falsification_condition"]


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
