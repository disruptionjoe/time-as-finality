"""Tests for T448: E2 chain residual factorization."""

from __future__ import annotations

import json

from models import e2_chain_residual_factorization as t448


def artifact():
    return t448.run()


def screen_item(item_id):
    return next(item for item in artifact()["absorber_screen"] if item["id"] == item_id)


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t448.ARTIFACT
    assert result["sources"]["d2_open_problem"].endswith("computational-finality-arrow.md")
    assert result["sources"]["t417"].endswith("T417-computational-finality-boundary-v0.1-results.md")
    assert result["sources"]["t446"].endswith("T446-e2-family-open-regime-big-swing-v0.1-results.md")
    assert "Recorded-tier residual audit only" in result["honest_ceiling"]


def test_full_chain_inversion_recovers_t446_states():
    audit = artifact()["factorization_audit"]

    assert audit["expected_states_forward_order"] == [4, 256, 32410249]
    assert audit["inversion"]["states_forward_order"] == audit["expected_states_forward_order"]
    assert audit["recovered_expected_states"] is True
    assert audit["new_global_oracle_needed"] is False


def test_chain_inversion_uses_one_step_oracle_per_transition():
    audit = artifact()["factorization_audit"]

    assert audit["transition_count"] == 2
    assert audit["inversion"]["step_oracle_call_count"] == 2
    assert audit["oracle_call_count_equals_transition_count"] is True
    assert audit["oracle_moduli_reverse_order"] == [8549, 77]


def test_public_unwraps_expose_rabin_images():
    inversion = artifact()["factorization_audit"]["inversion"]
    unwraps = inversion["public_unwraps"]
    calls = inversion["step_oracle_calls"]

    assert len(unwraps) == len(calls)
    assert all(item["exact_square"] for item in unwraps)
    assert [item["public_integer_sqrt"] for item in unwraps] == [
        item["rabin_image"] for item in calls
    ]


def test_length_one_embedding_is_rabin_inversion_problem():
    audit = artifact()["length_one_embedding_audit"]

    assert audit["challenge_predecessor"] == 4
    assert audit["rabin_image"] == 16
    assert audit["embedded_final_state"] == 256
    assert audit["recovered_predecessor"] == 4
    assert audit["recovers_rabin_predecessor"] is True


def test_next_domain_control_detects_no_coupling():
    control = artifact()["no_coupling_control"]

    assert control["alternate_next_has_lift_room"] is True
    assert control["lift_state_identical"] is True
    assert control["default_recovered_predecessor"] == 4
    assert control["alternate_recovered_predecessor"] == 4
    assert control["next_domain_changes_predecessor"] is False


def test_missing_step_oracle_rows_record_product_dependency():
    rows = artifact()["missing_step_dependency_audit"]
    missing_rows = [row for row in rows if row["omitted_modulus_n"] is not None]
    complete_rows = [row for row in rows if row["omitted_modulus_n"] is None]

    assert {row["omitted_modulus_n"] for row in missing_rows} == {77, 8549}
    assert all(row["product_decomposition_can_run"] is False for row in missing_rows)
    assert complete_rows == [
        {
            "omitted_modulus_n": None,
            "omitted_modulus_label": None,
            "available_step_oracle_moduli": [77, 8549],
            "product_decomposition_can_run": True,
            "recovered_expected_states": True,
        }
    ]


def test_growth_debt_is_recorded_not_used_as_lock():
    growth = artifact()["growth_debt_audit"]

    assert growth["states_forward_order"] == [4, 256, 32410249]
    assert growth["state_bits_non_decreasing"] is True
    assert growth["domain_bits_increase"] is True
    assert "does not treat growth as the lock" in growth["reading"]


def test_absorber_screen_kills_current_t446_residual_without_d2_decision():
    result = artifact()
    screen = {item["id"]: item for item in result["absorber_screen"]}

    assert all(item["passed"] for item in screen.values())
    assert screen["full_chain_inversion_factors_through_step_oracles"]["status"] == (
        "residual_killed_for_current_packet"
    )
    assert screen["length_one_embedding_is_rabin_step_problem"]["status"] == (
        "no_new_chain_problem"
    )
    assert screen["next_domain_coupling_control"]["status"] == "no_coupling_detected"
    assert result["overall_verdict"]["verdict"] == t448.VERDICT
    assert result["overall_verdict"]["d2_decision"].startswith("none")


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
