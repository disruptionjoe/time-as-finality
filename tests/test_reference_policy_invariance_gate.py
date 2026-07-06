"""Tests for T458: reference-policy invariance/preclusion gate."""

import json

from models import reference_policy_invariance_gate as t458


def artifact():
    return t458.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t458.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t457"].endswith(
        "T457-description-completion-squeeze-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Admission/guardrail gate only" in result["honest_ceiling"]


def test_imported_t457_summary_keeps_description_blocker_intact():
    summary = artifact()["t457_import_summary"]

    assert summary["verdict"] == t458.t457.VERDICT
    assert summary["current_t454_class_label"] == (
        "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
    )
    assert summary["current_t454_class_factors_through_description"] is True
    assert summary["admitted_candidates_are_synthetic_only"] is True


def test_current_packet_is_reference_policy_relative():
    current = evaluation("current_t454_t455_t457_reference_policy_packet")
    audit = current["reference_policy_audit"]

    assert current["admitted_future_target"] is False
    assert current["gate_label"] == "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
    assert audit["reference_scope_complete"] is True
    assert audit["unhandled_reference_policies"] == [
        "finite_cyclic_reference",
        "consumed_charge_battery",
        "ideal_phase_reference",
    ]
    assert "all_required_reference_policies_handled" in current[
        "missing_requirements"
    ]


def test_finite_policy_only_scope_is_incomplete():
    finite_only = evaluation("finite_policy_only_selection_control")

    assert finite_only["admitted_future_target"] is False
    assert finite_only["gate_label"] == "NOT_ADMITTED_REFERENCE_SCOPE_INCOMPLETE"
    assert finite_only["reference_policy_audit"]["missing_reference_policies"] == [
        "finite_cyclic_reference",
        "consumed_charge_battery",
        "ideal_phase_reference",
    ]
    assert "reference_scope_complete" in finite_only["missing_requirements"]


def test_only_synthetic_invariant_or_precluded_targets_are_admitted():
    result = artifact()
    invariant = evaluation("synthetic_reference_policy_invariant_target")
    precluded = evaluation("synthetic_reference_policy_preclusion_target")

    assert invariant["admitted_future_target"] is True
    assert precluded["admitted_future_target"] is True
    assert invariant["gate_label"] == (
        "ADMITTED_REFERENCE_POLICY_INVARIANT_OR_PRECLUDED_TARGET_NO_PROMOTION"
    )
    assert precluded["gate_label"] == (
        "ADMITTED_REFERENCE_POLICY_INVARIANT_OR_PRECLUDED_TARGET_NO_PROMOTION"
    )
    assert invariant["missing_requirements"] == []
    assert precluded["missing_requirements"] == []
    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_reference_policy_invariant_target",
        "synthetic_reference_policy_preclusion_target",
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True
    assert result["overall_verdict"][
        "current_artifacts_admitted_for_stronger_posture"
    ] is False


def test_policy_dependent_post_hoc_hidden_and_control_failures():
    dependent = evaluation("synthetic_policy_dependent_preclusion_control")
    post_hoc = evaluation("synthetic_post_hoc_preclusion_control")
    hidden = evaluation("hidden_label_policy_control")
    late_scope = evaluation("post_hoc_reference_scope_control")
    no_negative = evaluation("synthetic_missing_negative_control")

    assert dependent["gate_label"] == "NOT_ADMITTED_POLICY_DEPENDENT_PRECLUSION"
    assert "all_preclusions_policy_independent" in dependent["missing_requirements"]

    assert post_hoc["gate_label"] == "NOT_ADMITTED_POST_HOC_POLICY_PRECLUSION"
    assert "all_preclusions_declared_before_pair" in post_hoc[
        "missing_requirements"
    ]

    assert hidden["gate_label"] == "BLOCKED_HIDDEN_LABEL_OR_CASE_ID"
    assert late_scope["gate_label"] == "BLOCKED_POST_HOC_REFERENCE_SCOPE"
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
