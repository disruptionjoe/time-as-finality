"""Tests for T437: repaired taxonomy hostile-review gate."""

import json

from models import repaired_taxonomy_hostile_review_gate as t437


def artifact():
    return t437.run()


def repair_check(check_id):
    return next(item for item in artifact()["repair_checks"] if item["check_id"] == check_id)


def promotion_check(check_id):
    return next(item for item in artifact()["promotion_checks"] if item["check_id"] == check_id)


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t437.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "finite-closed-capability-boundary-scope-theorem.md"
    )
    assert result["sources"]["classical_repair"].endswith(
        "T433-classical-declarability-proof-certificate-v0.1-results.md"
    )
    assert result["sources"]["quantum_a_class_gate"].endswith(
        "T435-quantum-e3-admissible-menu-gate-v0.1-results.md"
    )
    assert result["sources"]["resource_lift_gate"].endswith(
        "T436-quantum-e3-resource-lift-classifier-v0.1-results.md"
    )
    assert "no claim promotion" in result["honest_ceiling"]


def test_repair_packet_survives_as_internal_map_only():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t437.VERDICT
    assert verdict["repair_packet_survives_as_internal_map"] is True
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "internal use as an organizing map" in verdict["reading"]


def test_classical_repair_uses_t433_certificate():
    check = repair_check("classical_single_instance_repair")

    assert check["status"] == "PASS"
    assert check["passed"] is True
    assert any("CLASSICAL_DECLARABILITY_PROOF_CERTIFIED" in item for item in check["evidence"])
    assert "not a universal no-go" in check["residual_risk"]


def test_quantum_a_class_and_resource_lift_repairs_pass():
    q_check = repair_check("quantum_a_class_statement")
    lift_check = repair_check("resource_lift_blocks_absolute_overread")

    assert q_check["status"] == "PASS"
    assert q_check["passed"] is True
    assert any("A1 phase pair" in item for item in q_check["evidence"])
    assert "not a WAY theorem" in q_check["residual_risk"]

    assert lift_check["status"] == "PASS"
    assert lift_check["passed"] is True
    assert any("A1-relative and A2-declared" in item for item in lift_check["evidence"])
    assert "independently typed exact no-go witness" in lift_check["residual_risk"]


def test_prior_art_and_universal_no_go_checks_pass_conservatively():
    prior = repair_check("prior_art_verification_recorded")
    withdrawn = repair_check("universal_no_go_not_revived")

    assert prior["status"] == "PASS"
    assert "LOW" in " ".join(prior["evidence"])
    assert "No new web fetch" in prior["residual_risk"]

    assert withdrawn["status"] == "PASS"
    assert any("internal organizing map" in item for item in withdrawn["evidence"])


def test_promotion_and_external_posture_remain_blocked():
    hard_paper = promotion_check("hard_theorem_publication_blocked")
    absolute = promotion_check("real_absolute_e3_witness_missing")
    d2 = promotion_check("d2_computational_arrow_still_separate")

    assert hard_paper["status"] == "BLOCKED"
    assert hard_paper["passed"] is False
    assert "does not authorize publication" in hard_paper["residual_risk"]

    assert absolute["status"] == "BLOCKED"
    assert absolute["passed"] is False
    assert any("synthetic exact no-go" in item for item in absolute["evidence"])

    assert d2["status"] == "BLOCKED"
    assert d2["passed"] is False
    assert "separate" in d2["residual_risk"]


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "WAY theorem proved",
        "universal no-go revived",
        "public paper authorized",
        "GU adapter revived",
        "D2 decided",
    )
    assert all(term not in combined for term in banned)
