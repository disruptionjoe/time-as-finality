"""Tests for T402: Causal-domain boundary-forcing screen."""

import json

import pytest

from models.causal_domain_boundary_forcing_screen import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_causal_domain_boundary_forcing_screen,
)


@pytest.fixture(scope="module")
def res():
    return run_causal_domain_boundary_forcing_screen()


def _case(res, case_id):
    for item in res["causal_domain_task_audits"]:
        if item["candidate"]["case_id"] == case_id:
            return item
    raise AssertionError(f"missing case {case_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert (
        res["residue_label"]
        == "candidate_physical_forced_task_absorbed_by_causal_domain_completion"
    )


def test_causal_geometry_forces_boundary_crossing(res):
    geometry = res["causal_geometry"]
    assert geometry["R_and_B_are_spacelike"] is True
    assert geometry["verdict_in_common_future"] is True
    assert geometry["R_only_domain_contains_verdict"] is False
    assert geometry["B_only_domain_contains_verdict"] is False
    assert geometry["RB_joint_domain_contains_verdict"] is True
    assert geometry["boundary_crossing_forced_by_domain"] is True


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


def test_common_future_verdict_separates(res):
    audit = res["main_pair_audit"]
    relation = audit["common_future_verdict_relation"]
    assert audit["full_joint_total_variation"] == 1.0
    assert audit["common_future_verdict_success"] == 1.0
    assert relation["aligned"] == {"same": 1.0, "different": 0.0}
    assert relation["anti_aligned"] == {"same": 0.0, "different": 1.0}
    assert relation["separates_pair"] is True
    assert relation["binary_success"] == 1.0


def test_causal_common_future_task_clears_substrate_gate(res):
    item = _case(res, "causal_common_future_verdict_task")
    assert item["causal_domain_task_gate"] == "pass"
    assert item["failure_label"] is None
    assert item["physical_substrate_burden_cleared"] is True
    assert (
        item["residue_label"]
        == "candidate_physical_forced_task_absorbed_by_causal_domain"
    )
    assert item["measurement_gate"]["common_future_verdict_advantage"] == 0.5
    assert item["measurement_gate"]["joint_domain_restores_capability"] is True


def test_optional_access_and_shortcuts_are_blocked(res):
    expected = {
        "optional_joint_state_label": (
            "optional_boundary_menu_only",
            "absorbed_optional_enlarged_access",
        ),
        "region_hidden_source_bit": (
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
        assert item["causal_domain_task_gate"] == "fail"
        assert item["failure_label"] == failure
        assert item["residue_label"] == residue


def test_controls_have_teeth_and_domain_null(res):
    controls = res["controls"]
    assert controls["region_visible_control"]["region_total_variation"] == 1.0
    assert controls["region_visible_control"]["region_only_binary_success"] == 1.0
    assert (
        controls["causal_domain_negative_control"]["RB_joint_domain_contains_event"]
        is False
    )


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["lorentzian_causal_domain_completion"]["status"] == "absorbs"
    assert (
        absorber["ordinary_joint_input_completion"]["status"]
        == "absorbs_after_domain_access"
    )
    assert absorber["R_supported_intervention_underdescription"]["status"] == "certified_no_separator"
    assert absorber["claim_promotion"]["status"] == "blocked"


def test_summary_names_only_causal_task_as_physical_pass(res):
    summary = res["summary"]
    assert summary["pass_cases"] == ["causal_common_future_verdict_task"]
    assert summary["physical_substrate_pass_cases"] == [
        "causal_common_future_verdict_task"
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
