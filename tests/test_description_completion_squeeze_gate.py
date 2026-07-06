"""Tests for T457: description-completion squeeze gate."""

import json

from models import description_completion_squeeze_gate as t457


def artifact():
    return t457.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t457.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t456"].endswith(
        "T456-policy-invariant-region-theorem-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Admission/guardrail gate only" in result["honest_ceiling"]


def test_imported_t456_summary_keeps_current_blockers():
    summary = artifact()["t456_import_summary"]

    assert summary["verdict"] == t457.t456.VERDICT
    assert summary["current_t454_t455_label"] == (
        "NOT_ADMITTED_DESCRIPTION_POLICY_THEOREM_BLOCKS"
    )
    assert summary["current_t454_t455_missing_requirements"] == [
        "description_nonfactorization",
        "reference_policy_invariance",
        "policy_independent_region_theorem",
    ]
    assert summary["admitted_candidates_are_synthetic_only"] is True


def test_current_t454_class_factors_through_description():
    current = evaluation("current_t454_boundary_resource_description")

    assert current["admitted_future_target"] is False
    assert current["gate_label"] == "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
    assert current["factorization_audit"][
        "capability_factors_through_description"
    ] is True
    assert current["factorization_audit"][
        "description_nonfactorization_witnessed"
    ] is False
    assert current["factorization_audit"]["omitted_capability_deciding_fields"] == []


def test_omitting_boundary_resource_is_underdescription_without_theorem():
    omitted = evaluation("omitted_boundary_resource_control")

    assert omitted["admitted_future_target"] is False
    assert omitted["gate_label"] == "NOT_ADMITTED_UNDERDESCRIBED_BOUNDARY_RESOURCE"
    assert omitted["factorization_audit"]["description_nonfactorization_witnessed"] is True
    assert "boundary_charge_available" in omitted["factorization_audit"][
        "omitted_capability_deciding_fields"
    ]
    assert "omitted_deciding_fields_theorem_supported" in omitted[
        "missing_requirements"
    ]


def test_only_synthetic_non_descriptive_theorem_target_is_admitted():
    result = artifact()
    target = evaluation("synthetic_non_descriptive_theorem_target")
    complete = evaluation("description_complete_synthetic_control")

    assert target["admitted_future_target"] is True
    assert target["gate_label"] == "ADMITTED_NON_DESCRIPTIVE_THEOREM_TARGET_NO_PROMOTION"
    assert target["missing_requirements"] == []

    assert complete["admitted_future_target"] is False
    assert complete["gate_label"] == "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"

    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_non_descriptive_theorem_target"
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True
    assert result["overall_verdict"]["current_artifacts_admitted_for_stronger_posture"] is False


def test_policy_fragility_hidden_label_and_controls_are_rejected():
    no_policy = evaluation("synthetic_no_policy_independence")
    fragile = evaluation("synthetic_reference_policy_fragile")
    hidden = evaluation("hidden_label_shortcut_control")
    no_negative = evaluation("synthetic_missing_negative_control")

    assert no_policy["gate_label"] == "NOT_ADMITTED_NO_POLICY_INDEPENDENT_THEOREM"
    assert "theorem_policy_independent" in no_policy["missing_requirements"]

    assert fragile["gate_label"] == "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
    assert "reference_policy_invariant_or_precluded" in fragile[
        "missing_requirements"
    ]

    assert hidden["gate_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
    assert no_negative["gate_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "region-indexed discriminator success proved",
        "real substrate law proved",
        "WAY theorem proved",
        "quantum physics theorem proved",
        "GU adapter revived",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
