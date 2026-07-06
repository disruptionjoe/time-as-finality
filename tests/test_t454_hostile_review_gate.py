"""Tests for T455: T454 hostile-review gate."""

import json

from models import t454_hostile_review_gate as t455


def artifact():
    return t455.run()


def survival_check(check_id):
    return next(
        item for item in artifact()["survival_checks"] if item["check_id"] == check_id
    )


def hostile_objection(check_id):
    return next(
        item
        for item in artifact()["hostile_objections"]
        if item["check_id"] == check_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t455.ARTIFACT
    assert result["sources"]["open_problem"].endswith(
        "region-indexed-capability-discriminator.md"
    )
    assert result["sources"]["t454"].endswith(
        "T454-integrated-e3-region-packet-swing-v0.1-results.md"
    )
    assert result["claim_ledger_update"] == "none; no claim promotion"
    assert "Hostile-review gate only" in result["honest_ceiling"]


def test_t454_mechanical_survival_checks_pass():
    region = survival_check("region_packet_mechanical_correctness")
    exact = survival_check("exact_witness_tied_to_named_completion")
    controls = survival_check("negative_controls_keep_scope_narrow")

    assert region["status"] == "PASS"
    assert region["passed"] is True
    assert "boundary menu splits" in " ".join(region["evidence"])

    assert exact["status"] == "PASS"
    assert exact["passed"] is True
    assert "T447 nilpotent-shift certificate" in " ".join(exact["evidence"])

    assert controls["status"] == "PASS"
    assert controls["passed"] is True
    assert "Only the main integrated packet" in " ".join(controls["evidence"])


def test_description_and_reference_policy_objections_fire():
    description = hostile_objection("law_sector_description_absorber_still_fires")
    policy = hostile_objection("reference_policy_fragility_still_fires")

    assert description["status"] == "FIRES"
    assert description["passed"] is False
    assert "description" in description["residual_risk"]

    assert policy["status"] == "FIRES"
    assert policy["passed"] is False
    assert "Cyclic reference control restores completion." in policy["evidence"]
    assert "policy-relative" in policy["residual_risk"]


def test_no_new_theorem_and_posture_blocks_fire():
    theorem = hostile_objection("no_new_region_theorem_beyond_integration")
    posture = hostile_objection("stronger_direction_a_posture_blocked")

    assert theorem["status"] == "FIRES"
    assert theorem["passed"] is False
    assert "No minimality" in " ".join(theorem["evidence"])

    assert posture["status"] == "BLOCKED"
    assert posture["passed"] is False
    assert "does not authorize" not in posture["residual_risk"]
    assert "future promotion requires" in posture["residual_risk"]


def test_overall_verdict_keeps_t454_recorded_tier():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t455.VERDICT
    assert verdict["t454_survives_as_review_target"] is True
    assert verdict["stronger_direction_a_posture_earned"] is False
    assert verdict["region_discriminator_success"] is False
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert verdict["fired_objection_ids"] == [
        "law_sector_description_absorber_still_fires",
        "reference_policy_fragility_still_fires",
        "no_new_region_theorem_beyond_integration",
        "stronger_direction_a_posture_blocked",
    ]


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
