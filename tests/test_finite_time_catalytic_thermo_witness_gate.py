"""Tests for T439: finite-time catalytic thermodynamic witness gate."""

import json
from math import log

from models import finite_time_catalytic_thermo_witness_gate as t439


def artifact():
    return t439.run()


def classification(packet_id):
    return next(
        item for item in artifact()["classifications"] if item["packet"]["packet_id"] == packet_id
    )


def test_artifact_identity_and_sources():
    result = artifact()

    assert result["artifact"] == t439.ARTIFACT
    assert result["sources"]["h7_handoff"].endswith("h7-physical-deletion-substrate-handoff.md")
    assert result["sources"]["n8_absorber_map"].endswith("N8-h7-stochastic-thermodynamic-absorbers.md")
    assert result["sources"]["t142"].endswith("thermodynamic-erasure-calibration-v0.1-results.md")
    assert "admission gate only" in result["honest_ceiling"]


def test_imports_t142_landauer_and_uncopy_guardrail():
    guard = artifact()["t142_imported_guardrail"]

    assert guard["one_bit_blind_reset_beta_work_floor"] == log(2.0)
    assert guard["copy_reverses_have_zero_heat_uncopy_mode"] is True
    assert guard["copy_reverses_have_landauer_reset_mode"] is True
    assert guard["h7_upgrade_status"] == "thermodynamic_absorption_not_upgrade"


def test_t142_uncopy_and_blind_reset_are_absorbed():
    uncopy = classification("t142_correlated_uncopy_copy")
    reset = classification("t142_blind_reset_only")

    assert uncopy["label"] == "ABSORBED_BY_REVERSIBLE_UNCOPY"
    assert uncopy["admitted_for_future_h7_work"] is False
    assert reset["label"] == "ABSORBED_BY_LANDAUER_BENNETT_ERASURE"
    assert reset["admitted_for_future_h7_work"] is False


def test_standard_thermodynamic_absorbers_do_not_admit():
    assert classification("finite_barrier_metastable_memory")["label"] == (
        "ABSORBED_BY_KINETICS_NOT_CONSTRUCTOR_IMPOSSIBILITY"
    )
    assert classification("nonequilibrium_current_only")["label"] == (
        "ABSORBED_BY_STOCHASTIC_THERMO_CURRENT"
    )
    assert classification("feedback_demon_missing_memory")["label"] == (
        "BLOCKED_OMITTED_FEEDBACK_MEMORY_LEDGER"
    )
    assert classification("hidden_sink_export_history")["label"] == (
        "BLOCKED_HIDDEN_SINK_OR_EXPORT_HISTORY"
    )
    assert classification("untyped_resource_drawdown")["label"] == (
        "REJECTED_UNTYPED_RESOURCE_UNIT"
    )


def test_ideal_or_sector_lock_routes_to_separate_spec():
    item = classification("ideal_infinite_barrier_or_sector_lock")

    assert item["route"] == "separate_spec_required"
    assert item["label"] == "ROUTE_TO_IDEAL_LIMIT_OR_E3_SPEC"
    assert item["admitted_for_future_h7_work"] is False


def test_catalyst_accounting_must_be_declared_and_returned():
    hidden = classification("hidden_catalyst_packet")
    consumed = classification("consumed_catalyst_packet")

    assert hidden["label"] == "BLOCKED_UNDECLARED_CATALYST_POLICY"
    assert hidden["admitted_for_future_h7_work"] is False
    assert consumed["label"] == "ABSORBED_BY_CHANGED_CATALYST_RESOURCE_BOUNDARY"
    assert consumed["admitted_for_future_h7_work"] is False


def test_matched_ledger_split_must_persist():
    item = classification("ledger_matched_split_vanishes")

    assert item["label"] == "REJECTED_SPLIT_ABSORBED_AFTER_LEDGER_MATCH"
    assert item["admitted_for_future_h7_work"] is False


def test_full_accounting_synthetic_positive_is_future_target_only():
    item = classification("full_accounting_synthetic_positive_control")

    assert item["admitted_for_future_h7_work"] is True
    assert item["route"] == "admitted_as_future_target"
    assert item["label"] == "ADMITTED_THERMO_RESOURCE_WITNESS_TARGET_NO_H7_PROMOTION"
    assert item["packet"]["synthetic_positive_control"] is True
    assert "future review target" in item["reason"]


def test_overall_verdict_keeps_h7_and_claims_gated():
    verdict = artifact()["overall_verdict"]

    assert verdict["verdict"] == t439.VERDICT
    assert verdict["admitted_packet_ids"] == ["full_accounting_synthetic_positive_control"]
    assert verdict["synthetic_positive_controls_only"] is True
    assert verdict["h7_promotion"].startswith("none")
    assert verdict["claim_ledger_update"] == "none; no claim promotion"


def test_json_serializable_and_avoids_forbidden_promotions():
    result = artifact()
    combined = json.dumps(result, sort_keys=True)

    json.dumps(result, sort_keys=True)
    banned = (
        "H7 promoted",
        "thermodynamic arrow proved",
        "physics claim proved",
        "public posture authorized",
        "claim promotion follows",
    )
    assert all(term not in combined for term in banned)
