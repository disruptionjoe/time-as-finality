"""Tests for T459: policy-independent theorem-supply gate."""

import json

from models import policy_independent_theorem_supply_gate as t459


def artifact():
    return t459.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t459.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t458"].endswith(
        "T458-reference-policy-invariance-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == (
        "none; no claim promotion or claim demotion"
    )
    assert "Admission/demotion gate only" in result["honest_ceiling"]


def test_imported_t457_and_t458_blockers_remain_active():
    result = artifact()
    t457_summary = result["t457_import_summary"]
    t458_summary = result["t458_import_summary"]

    assert t457_summary["verdict"] == t459.t457.VERDICT
    assert t457_summary["current_label"] == (
        "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
    )
    assert t457_summary["capability_factors_through_description"] is True
    assert t457_summary["current_artifacts_admitted_for_stronger_posture"] is False

    assert t458_summary["verdict"] == t459.t458.VERDICT
    assert t458_summary["current_label"] == "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
    assert t458_summary["unhandled_reference_policies"] == [
        "finite_cyclic_reference",
        "consumed_charge_battery",
        "ideal_phase_reference",
    ]
    assert t458_summary["current_artifacts_admitted_for_stronger_posture"] is False


def test_current_route_is_demoted_to_negative_guardrail():
    result = artifact()
    current = evaluation("current_t454_t455_t457_t458_integrated_route")

    assert current["admitted_future_target"] is False
    assert current["gate_label"] == "NOT_ADMITTED_NO_THEOREM_SUPPLIED"
    assert current["missing_requirements"] == [
        "theorem_supplied",
        "theorem_not_packet_integration",
        "theorem_policy_independent",
        "theorem_targets_named_completion",
        "theorem_makes_completion_nonadmissible",
        "description_nonfactorization_supplied",
        "reference_variants_handled_or_precluded",
    ]
    assert result["overall_verdict"]["current_route_demoted_to_negative_guardrail"] is True
    assert result["overall_verdict"]["route_demotion_scope"] == (
        "current integrated E3-region packet class only"
    )


def test_theorem_supply_controls_fail_for_the_right_reasons():
    integration = evaluation("packet_integration_as_theorem_control")
    description = evaluation("description_factorization_control")
    reference = evaluation("reference_policy_relative_theorem_control")
    dependent = evaluation("policy_dependent_theorem_control")
    post_hoc = evaluation("post_hoc_theorem_control")
    untargeted = evaluation("untargeted_theorem_control")
    completion = evaluation("completion_not_precluded_control")

    assert integration["gate_label"] == (
        "NOT_ADMITTED_PACKET_INTEGRATION_IS_NOT_THEOREM"
    )
    assert "theorem_not_packet_integration" in integration["missing_requirements"]

    assert description["gate_label"] == "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
    assert "description_nonfactorization_supplied" in description[
        "missing_requirements"
    ]

    assert reference["gate_label"] == "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
    assert "reference_variants_handled_or_precluded" in reference[
        "missing_requirements"
    ]

    assert dependent["gate_label"] == "NOT_ADMITTED_POLICY_DEPENDENT_THEOREM"
    assert "theorem_policy_independent" in dependent["missing_requirements"]

    assert post_hoc["gate_label"] == "NOT_ADMITTED_POST_HOC_THEOREM"
    assert "theorem_declared_before_pair" in post_hoc["missing_requirements"]

    assert untargeted["gate_label"] == "NOT_ADMITTED_THEOREM_NOT_TIED_TO_COMPLETION"
    assert "theorem_targets_named_completion" in untargeted[
        "missing_requirements"
    ]

    assert completion["gate_label"] == (
        "NOT_ADMITTED_THEOREM_DOES_NOT_PRECLUDE_COMPLETION"
    )
    assert "theorem_makes_completion_nonadmissible" in completion[
        "missing_requirements"
    ]


def test_only_synthetic_future_theorem_target_is_admitted():
    result = artifact()
    synthetic = evaluation("synthetic_policy_independent_theorem_target")
    hidden = evaluation("hidden_label_theorem_control")
    missing_control = evaluation("synthetic_missing_negative_control")

    assert synthetic["admitted_future_target"] is True
    assert synthetic["gate_label"] == (
        "ADMITTED_POLICY_INDEPENDENT_THEOREM_TARGET_NO_PROMOTION"
    )
    assert synthetic["missing_requirements"] == []

    assert hidden["gate_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
    assert missing_control["gate_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"

    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_policy_independent_theorem_target"
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True
    assert result["overall_verdict"][
        "current_artifacts_admitted_for_stronger_posture"
    ] is False


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "claim demotion follows",
        "region-indexed discriminator success proved",
        "real substrate law proved",
        "WAY theorem proved",
        "quantum physics theorem proved",
        "GU adapter revived",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
