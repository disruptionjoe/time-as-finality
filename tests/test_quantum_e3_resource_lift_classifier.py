"""Tests for T436: quantum E3 resource-lift classifier."""

import json

from models import quantum_e3_admissible_menu_gate as t435
from models import quantum_e3_resource_lift_classifier as t436


def artifact():
    return t436.run()


def classification(case_id):
    return next(item for item in artifact()["classifications"] if item["case_id"] == case_id)


def test_artifact_identity_and_scope():
    result = artifact()

    assert result["artifact"] == t436.ARTIFACT
    assert result["source_t435"].endswith("T435-quantum-e3-admissible-menu-gate-v0.1-results.md")
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "not a WAY theorem" in result["honest_ceiling"]
    assert "not a GU/TaF adapter" in result["honest_ceiling"]


def test_t435_main_pair_is_relative_not_absolute_after_a2_lift():
    main = classification("t435_phase_pair_lifted_by_a2_reference")

    assert main["t435_a1_e3_admitted"] is True
    assert main["t435_residue_label"] == "E3_STRUCTURAL_SYMMETRY_RELATIVE_TO_A1_NO_REFERENCE"
    assert main["policy"]["a2_reference_resource_considered"] is True
    assert main["policy"]["a2_reference_resource_admits_separator"] is True
    assert main["absolute_e3_after_resource_lift"] is False
    assert main["resource_lift_label"] == "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"


def test_t435_mixed_control_is_also_relative_not_absolute():
    mixed = classification("t435_mixed_pair_lifted_by_a2_reference")

    assert mixed["t435_a1_e3_admitted"] is True
    assert mixed["absolute_e3_after_resource_lift"] is False
    assert mixed["resource_lift_label"] == "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"


def test_synthetic_exact_no_go_control_can_report_absolute_shape():
    control = classification("synthetic_exact_no_go_survives_a2")

    assert control["t435_a1_e3_admitted"] is True
    assert control["policy"]["synthetic_control_only"] is True
    assert control["policy"]["exact_no_go_witness_predeclared"] is True
    assert control["policy"]["a2_reference_resource_admits_separator"] is False
    assert control["absolute_e3_after_resource_lift"] is True
    assert control["resource_lift_label"] == "ABSOLUTE_E3_SHAPE_SURVIVES_A2_SYNTHETIC_CONTROL"
    assert "synthetic calibration only" in control["reason"]


def test_cost_only_and_missing_a2_audit_do_not_pass_as_absolute_e3():
    cost = classification("large_resource_cost_not_single_instance_e3")
    assert cost["absolute_e3_after_resource_lift"] is False
    assert cost["resource_lift_label"] == "NOT_ABSOLUTE_E3_COST_ONLY_E1_E2_CANDIDATE"

    missing = classification("a1_only_no_resource_lift_audit")
    assert missing["absolute_e3_after_resource_lift"] is False
    assert missing["resource_lift_label"] == "A1_RELATIVE_ONLY_RESOURCE_LIFT_UNTESTED"


def test_post_hoc_and_hidden_resource_policies_are_blocked():
    post_hoc = classification("post_hoc_resource_policy_blocked")
    assert post_hoc["absolute_e3_after_resource_lift"] is False
    assert post_hoc["resource_lift_label"] == "NOT_ADMITTED_RESOURCE_POLICY_POST_HOC"

    hidden = classification("hidden_resource_oracle_blocked")
    assert hidden["absolute_e3_after_resource_lift"] is False
    assert hidden["resource_lift_label"] == "BLOCKED_HIDDEN_RESOURCE_OR_LABEL"


def test_non_e3_baseline_controls_stay_rejected():
    visible = classification("a1_visible_charge_control_not_e3")
    assert visible["t435_a1_e3_admitted"] is False
    assert visible["resource_lift_label"] == "NOT_E3_BASELINE_GATE_FAILED"
    assert visible["absolute_e3_after_resource_lift"] is False

    classical = classification("classical_full_code_control_not_quantum_e3")
    assert classical["t435_a1_e3_admitted"] is False
    assert classical["resource_lift_label"] == "NOT_E3_BASELINE_GATE_FAILED"
    assert classical["absolute_e3_after_resource_lift"] is False


def test_t436_preserves_t435_a2_demotion_fact():
    t435_result = t435.run()
    a2 = next(
        item
        for item in t435_result["candidate_audits"]
        if item["candidate_id"] == "z2_phase_pair_a2_reference"
    )

    assert a2["residue_label"] == "E0_DECLARED_RELATIVE_TO_A2_REFERENCE_RESOURCE"
    assert a2["admitted_e3_relative_to_a1"] is False


def test_overall_verdict_blocks_absolute_reading_of_t435():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t436.VERDICT
    assert verdict["t435_main_pair_relative_not_absolute"] is True
    assert verdict["relative_case_ids"] == [
        "t435_phase_pair_lifted_by_a2_reference",
        "t435_mixed_pair_lifted_by_a2_reference",
    ]
    assert verdict["absolute_synthetic_control_ids"] == [
        "synthetic_exact_no_go_survives_a2"
    ]
    assert "blocking the stronger reading" in verdict["reading"]


def test_result_is_json_serializable_and_avoids_promotion_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    combined = json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "WAY theorem proved",
        "GU adapter revived",
        "quantum physics claim proved",
        "T435 is absolute E3",
    )
    assert all(term not in combined for term in banned)
