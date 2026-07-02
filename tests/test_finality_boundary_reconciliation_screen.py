"""Tests for T401: Finality-boundary reconciliation screen."""

import json

import pytest

from models.finality_boundary_reconciliation_screen import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_finality_boundary_reconciliation_screen,
)


@pytest.fixture(scope="module")
def res():
    return run_finality_boundary_reconciliation_screen()


def _case(res, case_id):
    for item in res["forced_task_audits"]:
        if item["candidate"]["case_id"] == case_id:
            return item
    raise AssertionError(f"missing case {case_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert (
        res["residue_label"]
        == "candidate_finality_native_forced_task_absorbed_as_joint_record_access"
    )


def test_region_and_boundary_views_are_identical(res):
    audit = res["main_pair_audit"]
    assert audit["pair"] == ["aligned", "anti_aligned"]
    assert audit["region_marginals"]["aligned"] == [0.5, 0.5]
    assert audit["region_marginals"]["anti_aligned"] == [0.5, 0.5]
    assert audit["boundary_marginals"]["aligned"] == [0.5, 0.5]
    assert audit["boundary_marginals"]["anti_aligned"] == [0.5, 0.5]
    assert audit["all_R_supported_statistic_bound"] == 0.0
    assert audit["all_boundary_local_statistic_bound"] == 0.0
    assert audit["region_only_binary_success"] == 0.5
    assert audit["boundary_local_binary_success"] == 0.5


def test_region_supported_intervention_menu_has_no_separator(res):
    menu = res["main_pair_audit"]["finite_region_intervention_menu"]
    assert menu["maps"] == ["identity", "flip", "erase_to_0", "erase_to_1"]
    assert menu["n_statistics"] == 4
    assert menu["max_diff"] == 0.0
    assert menu["aligned"] == menu["anti_aligned"]
    assert menu["aligned"]["erase_to_0"] == [1.0, 0.0]
    assert menu["aligned"]["erase_to_1"] == [0.0, 1.0]


def test_boundary_reconciliation_relation_separates(res):
    audit = res["main_pair_audit"]
    relation = audit["boundary_crossing_menu"]["record_reconciliation_relation"]
    assert audit["full_joint_total_variation"] == 1.0
    assert audit["joint_record_binary_success"] == 1.0
    assert relation["aligned"] == {"same": 1.0, "different": 0.0}
    assert relation["anti_aligned"] == {"same": 0.0, "different": 1.0}
    assert relation["separates_pair"] is True
    assert relation["binary_success"] == 1.0


def test_finality_record_reconciliation_clears_task_gate(res):
    item = _case(res, "finality_record_reconciliation_task")
    assert item["formal_forced_task_gate"] == "pass"
    assert item["failure_label"] is None
    assert item["domain_native_burden_cleared"] is True
    assert item["residue_label"] == "candidate_finality_native_forced_task_absorbed"
    assert item["measurement_gate"]["boundary_crossing_advantage"] == 0.5
    assert item["measurement_gate"]["region_enlargement_restores_capability"] is True


def test_optional_access_and_shortcuts_are_blocked(res):
    expected = {
        "optional_joint_state_label": (
            "optional_boundary_menu_only",
            "absorbed_optional_enlarged_access",
        ),
        "hidden_datum_in_R_shortcut": (
            "hidden_datum_smuggled_into_region",
            "blocked_hidden_datum_smuggling",
        ),
        "closure_key_shortcut": (
            "absorbed_by_closure_key",
            "absorbed_closure_key_bookkeeping",
        ),
        "class_marker_shortcut": (
            "absorbed_by_class_marker_signature",
            "absorbed_class_marker_signature",
        ),
    }
    for case_id, (failure, residue) in expected.items():
        item = _case(res, case_id)
        assert item["formal_forced_task_gate"] == "fail"
        assert item["failure_label"] == failure
        assert item["residue_label"] == residue


def test_controls_have_teeth_and_null_case(res):
    controls = res["controls"]
    assert controls["region_visible_control"]["region_total_variation"] == 1.0
    assert controls["region_visible_control"]["region_only_binary_success"] == 1.0
    null_relation = controls["uncorrelated_boundary_control"][
        "record_reconciliation_relation"
    ]
    assert null_relation == {"same": 0.5, "different": 0.5}
    assert controls["uncorrelated_boundary_control"][
        "binary_success_against_aligned_or_anti"
    ] == 0.5


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["ordinary_joint_record_completion"]["status"] == "absorbs"
    assert absorber["R_supported_intervention_underdescription"]["status"] == "certified_no_separator"
    assert absorber["closure_key_or_SBS_shortcut"]["status"] == "blocked_not_invoked"
    assert absorber["class_marker_signature"]["status"] == "blocked"
    assert absorber["claim_promotion"]["status"] == "blocked"


def test_summary_names_only_reconciliation_as_domain_native_pass(res):
    summary = res["summary"]
    assert summary["formal_pass_cases"] == ["finality_record_reconciliation_task"]
    assert summary["domain_native_pass_cases"] == [
        "finality_record_reconciliation_task"
    ]
    assert summary["blocked_cases"]["optional_joint_state_label"] == "optional_boundary_menu_only"


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("new physics", "claim promotion", "theorem proved", "law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
