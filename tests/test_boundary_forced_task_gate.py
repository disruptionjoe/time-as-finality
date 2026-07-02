"""Tests for T400: Boundary-forced task gate."""

import json

import pytest

from models.boundary_forced_task_gate import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_boundary_forced_task_gate,
)


@pytest.fixture(scope="module")
def res():
    return run_boundary_forced_task_gate()


def _case(res, case_id):
    for item in res["audits"]:
        if item["candidate"]["case_id"] == case_id:
            return item
    raise AssertionError(f"missing case {case_id}")


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["residue_label"] == "gate_operationalized_no_claim_promotion"


def test_t399_substrate_is_preserved(res):
    substrate = res["uses_substrate"]
    assert substrate["source_artifact"] == "T399-boundary-crossing-intervention-screen-v0.1"
    assert substrate["pair"] == ["phi_plus", "psi_plus"]
    assert substrate["all_R_supported_statistic_bound"] == 0.0
    assert substrate["finite_region_intervention_menu_max_diff"] == 0.0
    assert substrate["boundary_local_trace_distance"] == 0.0
    assert substrate["region_only_binary_success"] == 0.5
    assert substrate["boundary_crossing_success"] == 1.0


def test_t399_optional_boundary_access_fails_gate(res):
    item = _case(res, "t399_optional_state_label")
    assert item["formal_forced_task_gate"] == "fail"
    assert item["failure_label"] == "optional_boundary_menu_only"
    assert item["residue_label"] == "absorbed_optional_enlarged_access"
    assert item["domain_native_burden_cleared"] is False


def test_synthetic_relational_task_is_control_only(res):
    item = _case(res, "synthetic_RB_parity_task")
    assert item["formal_forced_task_gate"] == "pass"
    assert item["failure_label"] is None
    assert item["residue_label"] == "formal_positive_control_only"
    assert item["domain_native_burden_cleared"] is False
    assert item["measurement_gate"]["boundary_crossing_advantage"] == 0.5
    assert item["measurement_gate"]["region_enlargement_restores_capability"] is True


def test_shortcuts_are_blocked(res):
    expected = {
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


def test_summary_names_only_synthetic_formal_pass(res):
    summary = res["summary"]
    assert summary["formal_pass_cases"] == ["synthetic_RB_parity_task"]
    assert summary["domain_native_pass_cases"] == []
    assert summary["blocked_cases"]["t399_optional_state_label"] == "optional_boundary_menu_only"


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("new physics", "claim promotion", "theorem proved", "law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)

