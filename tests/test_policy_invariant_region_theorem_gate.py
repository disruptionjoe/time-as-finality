"""Tests for T456: policy-invariant region theorem gate."""

import json

from models import policy_invariant_region_theorem_gate as t456


def artifact():
    return t456.run()


def evaluation(candidate_id):
    return next(
        item
        for item in artifact()["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_sources_and_ceiling():
    result = artifact()

    assert result["artifact"] == t456.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t455"].endswith(
        "T455-t454-hostile-review-gate-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Admission gate only" in result["honest_ceiling"]


def test_imported_t455_summary_matches_hostile_review_state():
    summary = artifact()["t455_import_summary"]

    assert summary["verdict"] == t456.t455.VERDICT
    assert summary["t454_survives_as_review_target"] is True
    assert summary["region_packet_mechanical_correctness"] is True
    assert summary["exact_witness_tied_to_named_completion"] is True
    assert summary["description_objection_fires"] is True
    assert summary["reference_policy_objection_fires"] is True
    assert summary["no_new_theorem_objection_fires"] is True
    assert summary["stronger_posture_earned"] is False


def test_current_t454_t455_is_not_admitted_for_stronger_posture():
    current = evaluation("current_t454_t455_review_target")

    assert current["admitted_future_target"] is False
    assert current["gate_label"] == "NOT_ADMITTED_DESCRIPTION_POLICY_THEOREM_BLOCKS"
    assert current["requirement_audit"]["description_nonfactorization"] is False
    assert current["requirement_audit"]["reference_policy_invariance"] is False
    assert current["requirement_audit"]["policy_independent_region_theorem"] is False
    assert current["missing_requirements"] == [
        "description_nonfactorization",
        "reference_policy_invariance",
        "policy_independent_region_theorem",
    ]


def test_controls_fail_for_the_right_reasons():
    bare = evaluation("bare_t447_exact_no_go_control")
    desc = evaluation("description_completion_control")
    policy = evaluation("reference_policy_variant_control")
    theorem = evaluation("integration_without_region_theorem_control")

    assert bare["gate_label"] == "NOT_ADMITTED_NO_REGION_PACKET"
    assert "region_packet_present" in bare["missing_requirements"]

    assert desc["gate_label"] == "NOT_ADMITTED_DESCRIPTION_COMPLETION_FACTORS"
    assert "description_nonfactorization" in desc["missing_requirements"]

    assert policy["gate_label"] == "NOT_ADMITTED_REFERENCE_POLICY_FRAGILITY"
    assert "reference_policy_invariance" in policy["missing_requirements"]

    assert theorem["gate_label"] == "NOT_ADMITTED_NO_POLICY_INDEPENDENT_REGION_THEOREM"
    assert "policy_independent_region_theorem" in theorem["missing_requirements"]


def test_only_synthetic_future_target_is_admitted():
    result = artifact()
    synthetic = evaluation("synthetic_policy_invariant_region_theorem_packet")
    missing_control = evaluation("synthetic_missing_negative_control")

    assert synthetic["admitted_future_target"] is True
    assert synthetic["gate_label"] == (
        "ADMITTED_POLICY_INVARIANT_REGION_THEOREM_TARGET_NO_PROMOTION"
    )
    assert synthetic["missing_requirements"] == []

    assert missing_control["admitted_future_target"] is False
    assert missing_control["gate_label"] == "NOT_ADMITTED_NO_NEGATIVE_CONTROL"

    assert result["overall_verdict"]["admitted_candidate_ids"] == [
        "synthetic_policy_invariant_region_theorem_packet"
    ]
    assert result["overall_verdict"]["admitted_candidates_are_synthetic_only"] is True
    assert result["overall_verdict"]["current_artifacts_admitted_for_stronger_posture"] is False


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
