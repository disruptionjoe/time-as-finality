"""Tests for T447: quantum E3 exact no-go big swing."""

import json

from models import quantum_e3_exact_no_go_big_swing as t447


def artifact():
    return t447.run()


def case(case_id):
    return next(item for item in artifact()["case_audits"] if item["case_id"] == case_id)


def test_artifact_identity_and_scope():
    result = artifact()

    assert result["artifact"] == t447.ARTIFACT
    assert result["source_t436"].endswith(
        "T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "not a WAY theorem" in result["honest_ceiling"]
    assert "not an unrestricted absolute E3 result" in result["honest_ceiling"]


def test_main_packet_survives_declared_finite_catalytic_a2_lift():
    main = case("finite_nonwrapping_exact_catalyst_charge_flip")

    assert main["a1_audit"]["a1_structural_obstruction"] is True
    assert main["a1_audit"]["a1_label"] == (
        "A1_EXACT_STRUCTURAL_OBSTRUCTION_CHARGE_CHANGE_NO_REFERENCE"
    )
    assert main["policy"]["reference_kind"] == "finite_nonwrapping_charge_ladder"
    assert main["policy"]["exact_catalyst_return_required"] is True
    assert main["policy"]["total_charge_conservation_required"] is True
    assert main["certificate"]["has_nonzero_unit_modulus_eigenvector"] is False
    assert main["survives_declared_finite_a2_resource_lift"] is True
    assert main["unrestricted_absolute_e3_earned"] is False
    assert main["resource_lift_label"] == (
        "FINITE_A2_EXACT_CATALYTIC_NO_GO_SURVIVES_TOY_RESOURCE_LIFT"
    )


def test_finite_shift_certificate_is_exact_nilpotent_no_go():
    certificate = t447.finite_nonwrapping_shift_certificate(5)

    assert certificate["nilpotent_power"] == 5
    assert certificate["requires_nonzero_unit_modulus_eigenvector"] is True
    assert certificate["has_nonzero_unit_modulus_eigenvector"] is False
    assert "S^N = 0" in certificate["proof"]
    assert "eta = 0" in certificate["proof"]


def test_cyclic_reference_control_blocks_unrestricted_overclaim():
    cyclic = case("cyclic_reference_control")

    assert cyclic["a1_audit"]["a1_structural_obstruction"] is True
    assert cyclic["certificate"]["reference_model"] == "finite_cyclic_charge_reference"
    assert cyclic["certificate"]["has_nonzero_unit_modulus_eigenvector"] is True
    assert cyclic["survives_declared_finite_a2_resource_lift"] is False
    assert cyclic["resource_lift_label"] == "LIFTED_BY_CYCLIC_REFERENCE_TOY_CONTROL"


def test_consumed_and_ideal_references_route_not_absolute():
    finite_consumed = case("finite_reference_may_be_consumed")
    assert finite_consumed["survives_declared_finite_a2_resource_lift"] is False
    assert finite_consumed["resource_lift_label"] == (
        "RESOURCE_COMPLETION_REFERENCE_MAY_CHANGE_NOT_ABSOLUTE"
    )

    battery = case("consumed_charge_battery_control")
    assert battery["survives_declared_finite_a2_resource_lift"] is False
    assert battery["resource_lift_label"] == (
        "RESOURCE_COMPLETION_CONSUMED_REFERENCE_NOT_ABSOLUTE"
    )

    ideal = case("ideal_phase_reference_control")
    assert ideal["survives_declared_finite_a2_resource_lift"] is False
    assert ideal["resource_lift_label"] == (
        "ROUTES_TO_IDEAL_OR_LIMIT_REFERENCE_NOT_FINITE_EXACT"
    )


def test_missing_a2_post_hoc_hidden_and_cost_only_controls_rejected():
    missing = case("a1_only_missing_a2_audit")
    assert missing["resource_lift_label"] == "A1_RELATIVE_ONLY_A2_RESOURCE_LIFT_UNTESTED"

    post_hoc = case("post_hoc_exact_witness_blocked")
    assert post_hoc["resource_lift_label"] == "BLOCKED_POST_HOC_NO_GO_WITNESS"

    hidden = case("hidden_label_oracle_blocked")
    assert hidden["resource_lift_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"

    cost = case("large_resource_cost_only_control")
    assert cost["resource_lift_label"] == "NOT_EXACT_E3_COST_ONLY_E1_E2_CANDIDATE"


def test_a1_visible_control_does_not_pass_baseline():
    visible = case("a1_visible_task_control")

    assert visible["a1_audit"]["a1_structural_obstruction"] is False
    assert visible["a1_audit"]["a1_label"] == "A1_ALREADY_SEES_OR_CAN_DO_TASK"
    assert visible["resource_lift_label"] == "NOT_E3_A1_BASELINE_FAILED"


def test_t435_phase_pair_remains_relative_control():
    control = case("t435_phase_pair_relative_control")

    assert control["certificate"]["source_case_id"] == "t435_phase_pair_lifted_by_a2_reference"
    assert control["certificate"]["t436_label"] == (
        "A1_RELATIVE_LIFTED_TO_E0_BY_A2_REFERENCE"
    )
    assert control["certificate"]["t436_absolute_after_resource_lift"] is False
    assert control["resource_lift_label"] == "T435_CONTROL_A1_RELATIVE_LIFTED_BY_A2_REFERENCE"


def test_overall_verdict_is_positive_in_toy_but_not_unrestricted():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t447.VERDICT
    assert verdict["main_case_survives_declared_finite_a2"] is True
    assert verdict["finite_a2_survivor_case_ids"] == [
        "finite_nonwrapping_exact_catalyst_charge_flip"
    ]
    assert verdict["unrestricted_absolute_e3_case_ids"] == []
    assert "does not earn an unrestricted absolute E3 result" in verdict["reading"]


def test_result_is_json_serializable_and_avoids_promotion_language():
    result = artifact()

    json.dumps(result, sort_keys=True)
    combined = json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "WAY theorem proved",
        "GU adapter revived",
        "quantum physics claim proved",
        "unrestricted absolute E3 result proved",
    )
    assert all(term not in combined for term in banned)
