"""Tests for T450: E2 period-oracle trapdoor equivalence."""

from __future__ import annotations

import json

from models import e2_period_oracle_trapdoor_equivalence as t450


def artifact():
    return t450.run()


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t450.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t417"].endswith("T417-computational-finality-boundary-v0.1-results.md")
    assert result["sources"]["t449"].endswith("T449-e2-period-hardness-packet-audit-v0.1-results.md")
    assert "Recorded-tier trapdoor-equivalence audit only" in result["honest_ceiling"]


def test_period_oracle_recovers_predecessors_for_t449_targets():
    rows = artifact()["period_oracle_to_predecessor"]

    assert [row["modulus"]["n"] for row in rows] == [77, 209, 713, 8549, 23449]
    assert [row["period_oracle_value"] for row in rows] == [4, 12, 20, 40, 132]
    assert [row["predecessor"] for row in rows] == [4, 4, 9, 4, 3]
    assert all(row["forward_of_predecessor_matches_target"] for row in rows)


def test_period_oracle_yields_factorization_by_rabin_reduction():
    rows = artifact()["period_oracle_to_factorization"]

    assert [row["modulus"]["n"] for row in rows] == [77, 209, 713, 8549, 23449]
    assert all(row["period_oracle_yields_factor"] for row in rows)
    for row in rows:
        reduction = row["rabin_reduction_exhibited"]
        modulus = row["modulus"]
        assert reduction["nontrivial_factor"] in (modulus["p"], modulus["q"])
        assert reduction["nontrivial_factor"] * reduction["cofactor"] == modulus["n"]


def test_trapdoor_completion_computes_t449_periods():
    rows = artifact()["trapdoor_to_period"]

    assert [row["period_from_group_order"] for row in rows] == [4, 12, 20, 40, 132]
    assert all(row["matches_t449_period"] for row in rows)
    assert all(row["group_order_recovers_factors"] for row in rows)


def test_oracle_scope_classifier_separates_weak_and_trapdoor_strength_scopes():
    rows = {row["scope"]: row for row in artifact()["oracle_scope_classifier"]}

    assert rows["single_seed_period_value"]["can_reverse_arbitrary_target"] is False
    assert rows["single_seed_period_value"]["can_factor_by_rabin_reduction"] is False
    assert rows["challenge_target_period_value"]["status"] == "single_challenge_predecessor_only"
    assert rows["all_qr_targets_period_oracle"]["can_reverse_arbitrary_target"] is True
    assert rows["all_qr_targets_period_oracle"]["can_factor_by_rabin_reduction"] is True
    assert rows["all_qr_targets_period_oracle"]["status"] == "trapdoor_strength"
    assert rows["group_order_or_factorization_completion"]["status"] == (
        "native_trapdoor_completion"
    )


def test_absorber_screen_records_no_independent_d2_residue():
    screen = {item["id"]: item for item in artifact()["absorber_screen"]}

    assert all(item["passed"] for item in screen.values())
    assert screen["period_oracle_gives_predecessor"]["status"] == (
        "temporal_capability_reduced_to_period_value"
    )
    assert screen["predecessor_oracle_factors_n"]["status"] == (
        "rabin_trapdoor_equivalence_exhibited"
    )
    assert screen["trapdoor_completion_computes_periods"]["status"] == (
        "completion_absorbs_period_object"
    )
    assert screen["independent_d2_residue"]["status"] == "not_found_for_current_route"


def test_overall_verdict_keeps_decision_and_claims_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t450.VERDICT
    assert verdict["screen_passed"] is True
    assert verdict["d2_decision"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "all-target period oracle is trapdoor-strength" in verdict["reading"]


def test_recommended_next_routes_to_demotion_or_changed_assumption():
    next_steps = artifact()["recommended_next"]

    assert "absorbed by Rabin/factoring" in next_steps[0]
    assert "nonstandard period assumption" in next_steps[1]
    assert "demote the temporal D2 route" in next_steps[2]


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "D2 redesigned",
        "D2 abandoned",
        "claim promotion follows",
        "crypto theorem proved",
        "physics claim proved",
        "public posture authorized",
    )
    assert all(term not in combined for term in banned)
