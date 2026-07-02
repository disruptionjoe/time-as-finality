"""Tests for T406: transition-system operation-unavailability gate."""

import json

import pytest

from models.transition_system_operation_unavailability_gate import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_transition_system_operation_unavailability_gate,
)


@pytest.fixture(scope="module")
def res():
    return run_transition_system_operation_unavailability_gate()


def _pair(res, pair_id):
    for item in res["pair_audits"]:
        if item["pair_id"] == pair_id:
            return item
    raise AssertionError(f"missing pair {pair_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["source_artifact"] == "T405-physical-latch-finality-lock-screen-v0.1"
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert (
        res["residue_label"]
        == "operation_unavailability_absorbed_by_transition_system_completion"
    )


def test_main_pair_matches_fixed_projection_but_splits_on_transition_relation(res):
    main = _pair(res, "transition_unavailability_main_pair")
    assert main["fixed_accounting_projection_equal"] is True
    assert main["transition_system_completion_equal"] is False
    assert main["same_operation_menu"] is True
    assert main["same_revision_budget"] is True
    assert main["same_non_dynamic_substrate_support"] is True
    assert main["absorber_mismatch_fields"] == []
    assert main["capability"]["differs"] is True
    assert main["capability"]["differing_fields"] == ["can_revise_final_verdict"]
    assert main["capability"]["left"]["can_revise_final_verdict"] is True
    assert main["capability"]["right"]["can_revise_final_verdict"] is False
    assert main["residue_label"] == "absorbed_by_transition_system_completion"


def test_matched_transition_systems_do_not_split_capability(res):
    matched = _pair(res, "matched_transition_control")
    assert matched["fixed_accounting_projection_equal"] is True
    assert matched["transition_system_completion_equal"] is True
    assert matched["capability"]["differs"] is False
    assert matched["residue_label"] == "no_capability_split"

    factorization = res["factorization_check"]
    assert factorization["checked_pairs"] > 0
    assert factorization["matched_transition_completion_pairs"] > 0
    assert factorization["violations"] == []
    assert factorization["same_transition_system_implies_same_capability"] is True


def test_controls_separate_absorber_classes(res):
    menu = _pair(res, "operation_menu_completion_control")
    assert menu["fixed_accounting_projection_equal"] is False
    assert menu["residue_label"] == "absorbed_by_fixed_accounting_or_menu_completion"

    resource = _pair(res, "resource_accounting_control")
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
    assert hidden["transition_system_completion_equal"] is True
    assert hidden["hidden_label_shortcut_attempt"] is True
    assert hidden["capability"]["differs"] is False
    assert hidden["residue_label"] == "blocked_hidden_label_shortcut"

    latch = _pair(res, "latch_topology_shortcut_control")
    assert latch["fixed_accounting_projection_equal"] is True
    assert latch["transition_system_completion_equal"] is True
    assert latch["latch_topology_shortcut_attempt"] is True
    assert latch["capability"]["differs"] is False
    assert latch["residue_label"] == "blocked_latch_topology_shortcut"


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["causal_reachability_and_domain_of_dependence"]["status"] == "matched_not_explanatory"
    assert absorber["ordinary_joint_input_completion"]["status"] == "matched_not_explanatory"
    assert (
        absorber["operation_menu_completion"]["status"]
        == "matched_not_explanatory_for_main_pair"
    )
    assert (
        absorber["fixed_accounting_resource_provenance_control_boundary"]["status"]
        == "matched_not_explanatory_for_main_pair"
    )
    assert absorber["latch_topology_completion"]["status"] == "blocked_for_main_pair"
    assert absorber["transition_system_completion"]["status"] == "absorbs"
    assert absorber["claim_promotion"]["status"] == "blocked"


def test_summary_names_only_main_pair_as_same_fixed_accounting_split(res):
    summary = res["summary"]
    assert summary["same_fixed_accounting_split_cases"] == [
        "transition_unavailability_main_pair"
    ]
    assert (
        summary["absorbed_cases"]["transition_unavailability_main_pair"]
        == "absorbed_by_transition_system_completion"
    )
    assert res["main_pair_summary"]["absorber_mismatch_fields"] == []


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("claim promotion follows", "theorem proved", "new law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)
    assert "physical-arrow theorem" in res["falsification_condition"]


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
