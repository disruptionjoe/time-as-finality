"""Tests for T399: Boundary-crossing intervention statistics screen."""

import json

import pytest

from models.boundary_crossing_intervention_screen import (
    ARTIFACT,
    FALSIFICATION_CONDITION,
    VERDICT,
    run_boundary_crossing_intervention_screen,
)


@pytest.fixture(scope="module")
def res():
    return run_boundary_crossing_intervention_screen()


def test_artifact_identity_and_restraint(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["residue_label"] == "absorbed_boundary_access_translation"


def test_region_supported_intervention_statistics_are_identical(res):
    audit = res["main_pair_audit"]
    assert audit["region_trace_distance"] == 0.0
    assert audit["all_R_supported_statistic_bound"] == 0.0
    assert audit["region_only_binary_success"] == 0.5
    finite = audit["finite_region_intervention_menu"]
    assert finite["n_statistics"] == 24
    assert finite["max_diff"] == 0.0
    assert finite["sample_phi_plus"] == finite["sample_psi_plus"]


def test_boundary_local_statistics_are_also_identical(res):
    audit = res["main_pair_audit"]
    assert audit["boundary_local_trace_distance"] == 0.0
    assert audit["all_boundary_local_statistic_bound"] == 0.0
    assert audit["boundary_local_binary_success"] == 0.5
    assert audit["boundary_local_statistics"]["max_diff"] == 0.0


def test_boundary_crossing_menu_separates_pair(res):
    audit = res["main_pair_audit"]
    assert audit["full_trace_distance"] == 1.0
    assert audit["full_state_binary_success"] == 1.0
    parity = audit["boundary_crossing_menu"]["joint_Z_parity_readout"]
    assert parity["phi_plus"] == {"even": 1.0, "odd": 0.0}
    assert parity["psi_plus"] == {"even": 0.0, "odd": 1.0}
    assert parity["binary_success"] == 1.0
    bell = audit["boundary_crossing_menu"]["bell_basis_readout"]
    assert bell["phi_plus"]["phi_plus"] == 1.0
    assert bell["psi_plus"]["psi_plus"] == 1.0
    assert bell["binary_success"] == 1.0


def test_region_visible_control_has_teeth(res):
    control = res["controls"]["region_visible_pair"]
    assert control["region_trace_distance"] == 1.0
    assert control["region_only_binary_success"] == 1.0


def test_phase_correlation_control_requires_bell_menu(res):
    control = res["controls"]["phase_correlation_pair"]
    assert control["region_trace_distance"] == 0.0
    assert control["boundary_local_trace_distance"] == 0.0
    assert control["full_trace_distance"] == 1.0
    assert control["joint_Z_parity_max_diff"] == 0.0
    assert control["bell_basis_separates"] is True


def test_absorber_audit_is_conservative(res):
    absorber = res["absorber_audit"]
    assert absorber["ordinary_enlarged_state_completion"]["status"] == "absorbs"
    assert absorber["R_supported_intervention_underdescription"]["status"] == "certified_no_separator"
    assert absorber["boundary_relocation"]["status"] == "absorbs_as_access_boundary"
    assert absorber["SBS_or_closure_key"]["status"] == "not_invoked"


def test_verdict_and_falsification_are_restrained(res):
    assert res["verdict"] == VERDICT
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("new physics", "claim promotion", "theorem proved", "law")
    for text in (res["verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
