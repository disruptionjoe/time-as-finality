"""Tests for T451: D2 temporal route demotion packet."""

from __future__ import annotations

import json

from models import d2_temporal_route_demotion_packet as t451


def artifact():
    return t451.run()


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t451.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t417_static_boundary"].endswith(
        "T417-computational-finality-boundary-v0.1-results.md"
    )
    assert result["sources"]["t450"].endswith(
        "T450-e2-period-oracle-trapdoor-equivalence-v0.1-results.md"
    )
    assert "Route-demotion packet only" in result["honest_ceiling"]


def test_imported_evidence_uses_current_d2_gate_verdicts():
    evidence = artifact()["imported_evidence"]

    assert evidence["t438"]["verdict"] == (
        "E2_PERIOD_HARDNESS_ADMISSION_GATE_BUILT_NO_D2_DECISION"
    )
    assert evidence["t444"]["verdict"] == (
        "E2_CHANGED_TRANSITION_REGIME_GATE_BUILT_NO_D2_DECISION"
    )
    assert evidence["t448"]["verdict"] == (
        "T446_CHAIN_RESIDUAL_FACTORS_THROUGH_PER_STEP_RABIN_NO_NEW_D2_THEOREM"
    )
    assert evidence["t449"]["verdict"] == (
        "E2_PERIOD_HARDNESS_PACKET_SHARPENED_TO_HIDDEN_ORDER_THEOREM_TARGET_NO_D2_DECISION"
    )
    assert evidence["t450"]["verdict"] == (
        "PERIOD_ORACLE_COLLAPSES_TO_RABIN_TRAPDOOR_NO_INDEPENDENT_D2_ROUTE"
    )


def test_route_matrix_closes_current_routes_and_preserves_future_exceptions():
    rows = {row["route"]: row for row in artifact()["route_matrix"]}

    assert rows["finite_public_cycle_or_bounded_nonrecovery"]["status"] == "absorbed"
    assert rows["open_rabin_lift_chain"]["status"] == "absorbed"
    assert rows["closed_public_squaring_period_oracle"]["status"] == "absorbed"
    assert rows["changed_transition_or_open_nonpermutation"]["status"] == (
        "future_exception_only"
    )
    assert rows["nonstandard_period_assumption"]["status"] == "future_exception_only"
    assert "T417/Rabin" in rows["open_rabin_lift_chain"]["decision_effect"]


def test_decision_screen_demotes_current_route_without_claim_status_move():
    result = artifact()
    screen = {item["id"]: item for item in result["decision_screen"]}

    assert all(item["passed"] for item in screen.values())
    assert screen["finite_cycle_route_closed"]["status"] == "closed_by_t420_t438"
    assert screen["open_chain_route_closed"]["status"] == "closed_by_t448"
    assert screen["closed_period_route_closed"]["status"] == "closed_by_t450"
    assert screen["future_exception_preserved"]["status"] == (
        "future_changed_assumption_only"
    )
    assert screen["protected_surfaces_unchanged"]["status"] == (
        "no_claim_or_public_posture_move"
    )


def test_overall_verdict_is_route_demotion_to_t417_static_boundary():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t451.VERDICT
    assert verdict["screen_passed"] is True
    assert verdict["current_route_decision"] == (
        "demote current temporal D2 route to T417 static E2 boundary"
    )
    assert verdict["claim_ledger_update"] == "none; no claim status change"
    assert verdict["public_posture_update"] == "none"
    assert "current D2 temporal computational-arrow route" in verdict["reading"]


def test_recommended_next_stops_rebuilding_absorbed_route():
    next_steps = artifact()["recommended_next"]

    assert next_steps[0] == "Stop rebuilding the current public-squaring temporal D2 route."
    assert "T417" in next_steps[1]
    assert "T448/T450 absorbers" in next_steps[2]


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "claim promotion follows",
        "crypto theorem proved",
        "physics claim proved",
        "public posture authorized",
        "North Star movement follows",
    )
    assert all(term not in combined for term in banned)
