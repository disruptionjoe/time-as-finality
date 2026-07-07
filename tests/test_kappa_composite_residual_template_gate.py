"""Tests for T499 kappa composite-residual template gate."""

from __future__ import annotations

import json

from models import kappa_composite_residual_template_gate as t499


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t499.run()

    assert payload["artifact"] == t499.ARTIFACT
    assert payload["verdict"] == t499.VERDICT
    assert payload["source_progress_lanes"] == t499.SOURCE_PROGRESS_LANES
    assert payload["source_kappa_open_problem"] == t499.SOURCE_KAPPA_OPEN_PROBLEM
    assert payload["source_t465"] == t499.SOURCE_T465
    assert payload["source_t466"] == t499.SOURCE_T466
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert "does not promote kappa" in payload["honest_ceiling"]


def test_historical_kappa_catalogue_is_method_template_only():
    payload = t499.run()
    row = _decision(payload, "t224_t244_historical_kappa_catalogue")

    assert row["decision"] == "admitted_method_template_only"
    assert row["route_label"] == "STRUCTURAL_TEMPLATE_ONLY_T465_T466_CEILING"
    assert row["core_template_passes"] is True
    assert row["nonidentity_burden_passes"] is False
    assert "target_witness_not_nonidentity" in row["blockers"]
    assert "synthetic_nu_written_from_native_rank" in row["blockers"]
    assert payload["overall"]["historical_kappa_catalogue_admitted_as_method_template"] is True
    assert payload["overall"]["prediction_language_earned"] is False


def test_t466_synthetic_nonidentity_packet_is_review_only():
    payload = t499.run()
    row = _decision(payload, "t466_synthetic_nonidentity_packet")

    assert row["decision"] == "admitted_future_review_target"
    assert row["route_label"] == "NONIDENTITY_REVIEW_TARGET_ONLY"
    assert row["core_template_passes"] is True
    assert row["nonidentity_burden_passes"] is True
    assert row["blockers"] == ()
    assert row["allowed_action"] == "future review target only; no claim movement"
    assert payload["overall"]["synthetic_nonidentity_packet_admitted_for_review"] is True
    assert payload["overall"]["kappa_promotion_earned"] is False


def test_ab_contextuality_same_support_is_not_template_promotion():
    payload = t499.run()
    row = _decision(payload, "t465_ab_contextuality_same_support")

    assert row["decision"] == "not_admitted"
    assert row["route_label"] == "CORE_KAPPA_TEMPLATE_BURDEN_NOT_MET"
    assert "fewer_than_two_absorbers" in row["blockers"]
    assert "same_support_global_section_reencoding" in row["blockers"]


def test_retuning_and_missing_native_witnesses_are_rejected():
    payload = t499.run()
    retuned = _decision(payload, "retuned_per_domain_packet")
    missing = _decision(payload, "native_witness_missing_packet")

    assert retuned["decision"] == "not_admitted"
    assert "same_invariant_not_fixed" in retuned["blockers"]
    assert "per_domain_retuning" in retuned["blockers"]
    assert missing["decision"] == "not_admitted"
    assert "native_witnesses_not_declared" in missing["blockers"]
    assert "native_witnesses_not_independent" in missing["blockers"]
    assert "no_falsifying_control" in missing["blockers"]


def test_claim_promotion_shortcut_is_blocked_even_when_structurally_strong():
    payload = t499.run()
    row = _decision(payload, "claim_promotion_shortcut")

    assert row["decision"] == "blocked"
    assert row["route_label"] == "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT"
    assert row["core_template_passes"] is True
    assert row["nonidentity_burden_passes"] is True
    assert "claim_movement_requested" in row["blockers"]


def test_template_minimum_keeps_method_and_promotion_burdens_separate():
    payload = t499.run()
    minimum = set(payload["template_minimum"])

    assert "same invariant fixed across absorbers" in minimum
    assert "no per-domain retuning" in minimum
    assert "native target witnesses declared" in minimum
    assert "T465/T466 ceiling retained: method template does not equal prediction" in minimum
    assert "review only; no claim movement from packet shape alone" in minimum


def test_payload_json_and_forbidden_overreads_absent():
    payload = t499.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t499.VERDICT in dumped
    forbidden = (
        "kappa promotion earned",
        "T224 theorem proved",
        "genre theorem established",
        "public posture authorized",
        "cross-repo truth proved",
    )
    for term in forbidden:
        assert term not in dumped
