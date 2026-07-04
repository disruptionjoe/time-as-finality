"""Tests for T449: E2 period-hardness packet audit."""

from __future__ import annotations

import json

from models import e2_period_hardness_packet_audit as t449


def artifact():
    return t449.run()


def screen_item(item_id):
    return next(item for item in artifact()["absorber_screen"] if item["id"] == item_id)


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t449.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t438"].endswith("T438-e2-period-hardness-admission-gate-v0.1-results.md")
    assert result["sources"]["t448"].endswith("T448-e2-chain-residual-factorization-v0.1-results.md")
    assert "Recorded-tier period-hardness packet audit only" in result["honest_ceiling"]


def test_packet_routes_through_t438_as_future_target_only():
    route = artifact()["t438_route"]

    assert route["admitted_for_future_d2_work"] is True
    assert route["route"] == "admitted_as_future_target"
    assert route["label"] == "ADMITTED_E2_PERIOD_HARDNESS_REDESIGN_PACKET_NO_D2_DECISION"
    assert "future E2 redesign target" in route["reason"]


def test_family_audit_uses_expected_moduli_and_periods():
    audit = artifact()["family_period_audit"]
    rows = audit["rows"]

    assert [row["modulus"]["n"] for row in rows] == [77, 209, 713, 8549, 23449]
    assert [row["period_formula"] for row in rows] == [4, 12, 20, 40, 132]
    assert audit["max_periods"] == [4, 12, 20, 40, 132]
    assert audit["all_formula_match_iteration"] is True


def test_period_formula_matches_public_iteration_for_every_row():
    for row in artifact()["family_period_audit"]["rows"]:
        assert row["period_formula"] == row["period_by_public_iteration"]
        assert row["formula_matches_iteration"] is True


def test_known_period_publicly_recovers_predecessor():
    for row in artifact()["family_period_audit"]["rows"]:
        assert row["period_known_reverses_target"] is True
        assert row["predecessor_from_period"] == row["seed"]


def test_qr_group_order_completion_recovers_semiprime_trapdoor():
    for row in artifact()["family_period_audit"]["rows"]:
        modulus = row["modulus"]
        assert row["qr_group_order_recovers_factorization"] is True
        assert row["recovered_factors_from_qr_size"] == [modulus["p"], modulus["q"]]


def test_small_period_seed_controls_are_not_evidence():
    controls = artifact()["small_period_seed_controls"]

    assert len(controls) == 5
    assert all(row["seed"] == 1 for row in controls)
    assert all(row["period_formula"] == 1 for row in controls)
    assert all(row["period_by_public_iteration"] == 1 for row in controls)
    assert all(row["admitted_as_period_hardness_evidence"] is False for row in controls)


def test_absorber_screen_records_theorem_gap_not_promotion():
    result = artifact()
    screen = {item["id"]: item for item in result["absorber_screen"]}

    assert all(item["passed"] for item in screen.values())
    assert screen["t438_admission"]["status"] == "admitted_as_theorem_target"
    assert screen["period_formula_matches_public_cycle"]["status"] == "toy_formula_verified"
    assert screen["known_period_publicly_reverses"]["status"] == "period_is_missing_capability_object"
    assert screen["group_order_completion_absorbs"]["status"] == "trapdoor_completion_recorded"
    assert screen["small_period_seed_controls"]["status"] == "seed_distribution_required"
    assert screen["hardness_theorem_gap"]["status"] == "open_theorem_obligation"


def test_overall_verdict_sharpens_d2_without_deciding_it():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t449.VERDICT
    assert verdict["screen_passed"] is True
    assert verdict["d2_decision"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "hidden-order/cycle-length" in verdict["reading"]


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
