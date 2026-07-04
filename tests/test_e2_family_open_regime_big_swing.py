"""Tests for T446: E2 family/open-regime big swing."""

from __future__ import annotations

import json

from models import e2_family_open_regime_big_swing as t446


def artifact():
    return t446.run()


def screen_item(item_id):
    return next(item for item in artifact()["absorber_screen"] if item["id"] == item_id)


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t446.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t417"].endswith("T417-computational-finality-boundary-v0.1-results.md")
    assert result["sources"]["t438"].endswith("T438-e2-period-hardness-admission-gate-v0.1-results.md")
    assert result["sources"]["t444"].endswith("T444-e2-changed-transition-regime-gate-v0.1-results.md")
    assert "Recorded-tier packet swing only" in result["honest_ceiling"]


def test_schedule_starts_from_t417_and_has_injective_lift_room():
    audit = artifact()["schedule_audit"]
    rows = audit["rows"]

    assert rows[0]["label"] == "N0_T417_T419"
    assert rows[0]["n"] == 77
    assert audit["all_blum_prime_pairs"] is True
    assert audit["all_next_moduli_leave_injective_lift_room"] is True
    assert rows[0]["next_n_gt_n_squared"] is True
    assert rows[1]["next_n_gt_n_squared"] is True


def test_packet_routes_through_t438_and_t444():
    routes = artifact()["gate_routes"]

    assert routes["t438"]["route"] == "separate_spec_required"
    assert routes["t438"]["label"] == "ROUTE_TO_DIFFERENT_REGIME_SPEC"
    assert routes["t444"]["route"] == "admitted_as_separate_spec_target"
    assert routes["t444"]["label"] == "ADMITTED_OPEN_NONPERMUTATION_SEPARATE_SPEC_NO_D2_DECISION"
    assert routes["t444"]["admitted_for_separate_spec_review"] is True


def test_chain_has_two_public_steps_and_trapdoor_reversal():
    trace = artifact()["chain_trace"]

    assert trace["closed_public_permutation_regime"] is False
    assert trace["transition_count"] == 2
    assert trace["domain_moduli"] == [77, 8549, 81162077]
    for step in trace["steps"]:
        assert step["public_lift_inverse_matches_rabin_image"] is True
        assert step["trapdoor_predecessor_matches_x_t"] is True
        assert step["injective_lift_room"] is True
        assert step["x_next_in_next_qr_by_construction"] is True


def test_toy_crackability_is_recorded_not_used_as_hardness_evidence():
    trace = artifact()["chain_trace"]
    finite_cycle = screen_item("finite_cycle_toy_absorber")

    assert finite_cycle["passed"] is True
    assert finite_cycle["status"] == "survives_with_toy_caveat"
    assert finite_cycle["toy_public_cycle_crackable"] is True
    for step in trace["steps"]:
        assert step["brute_force_predecessor_matches_x_t"] is True
        assert step["public_cycle_predecessor_matches_x_t"] is True


def test_rabin_reductions_are_exhibited_for_current_moduli():
    reductions = artifact()["rabin_reductions"]

    assert len(reductions) == 2
    for row in reductions:
        assert row["sqrt_oracle_yields_factor"] is True
        reduction = row["rabin_reduction_exhibited"]
        assert reduction["nontrivial_factor"] in (
            row["modulus"]["p"],
            row["modulus"]["q"],
        )
        assert reduction["nontrivial_factor"] * reduction["cofactor"] == row["modulus"]["n"]


def test_absorber_screen_keeps_only_residuals_not_kills():
    result = artifact()
    screen = {item["id"]: item for item in result["absorber_screen"]}

    assert all(item["passed"] for item in screen.values())
    assert screen["t438_t444_route"]["status"] == "survives"
    assert screen["information_present_reversal_exists"]["status"] == "survives"
    assert screen["pure_ignorance_absorber"]["status"] == "survives"
    assert screen["e1_thermodynamic_cost_absorber"]["status"] == "survives"
    assert screen["named_hardness_reduction"]["status"] == "survives_conditionally"
    assert screen["static_t417_relabel_absorber"]["status"] == "partial_residual"
    assert screen["symmetric_complexity_growth_absorber"]["status"] == "survives_with_growth_debt"


def test_overall_verdict_is_candidate_packet_no_promotion():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t446.VERDICT
    assert verdict["screen_passed"] is True
    assert verdict["residual_absorbers"] == [
        "static_t417_relabel_absorber",
        "symmetric_complexity_growth_absorber",
    ]
    assert verdict["d2_decision"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"
    assert "toy arithmetic is crackable" in verdict["toy_status"]


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
