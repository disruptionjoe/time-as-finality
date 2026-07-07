"""Tests for T494 Levin/Fields primary-source competency absorber gate."""

from __future__ import annotations

import json

from models import levin_fields_primary_source_absorber_gate as t494


def _evaluation(payload, candidate_id):
    return next(
        item
        for item in payload["candidate_evaluations"]
        if item["candidate_id"] == candidate_id
    )


def test_artifact_identity_and_source_check_scope():
    payload = t494.run()

    assert payload["artifact"] == t494.ARTIFACT
    assert payload["overall_verdict"]["verdict"] == t494.VERDICT
    assert payload["source_audit"]["source_count"] == 6
    assert payload["source_audit"]["all_core_sources_checked"] is True
    assert payload["overall_verdict"]["n16_upgraded_for_bounded_scope"] is True
    assert "Primary-source absorber note" in payload["honest_ceiling"]


def test_sources_support_calibration_and_absorber_warning_not_taf_novelty():
    payload = t494.run()
    audit = payload["source_audit"]

    assert "fields_levin_2022_competency" in audit["calibration_ids"]
    assert "levin_2019_computational_boundary" in audit["calibration_ids"]
    assert "bongard_levin_2022_polycomputing" in audit["absorber_risk_ids"]
    assert audit["supports_taf_c_r_novelty_ids"] == []
    assert audit["imports_taf_mechanism_ids"] == []


def test_primary_source_status_and_full_profile_absorber_are_admitted():
    payload = t494.run()
    status = _evaluation(payload, "n16_primary_source_status_upgrade")
    absorber = _evaluation(payload, "competency_as_full_profile_absorber")

    assert status["admitted"] is True
    assert status["label"] == "ADMITTED_PRIMARY_SOURCE_ABSORBER_WARNING_NO_CLAIM"
    assert absorber["admitted"] is True
    assert absorber["action"] == "absorb_or_calibrate"
    assert payload["claim_ledger_update"] == "none; no claim promotion or demotion"


def test_cognitive_light_cone_is_region_calibration_only():
    payload = t494.run()
    light_cone = _evaluation(payload, "cognitive_light_cone_region_indexing_calibration")

    assert light_cone["admitted"] is True
    assert light_cone["label"] == "ADMITTED_REGION_INDEXING_CALIBRATION_NO_CLAIM"
    assert light_cone["action"] == "calibrate"


def test_shortcuts_are_rejected_or_blocked():
    payload = t494.run()

    single = _evaluation(payload, "single_statistic_equals_full_c_r")
    mechanism = _evaluation(payload, "active_inference_mechanism_import")
    novelty = _evaluation(payload, "novelty_over_competency_shortcut")
    polycomputing = _evaluation(payload, "polycomputing_objective_identity_shortcut")
    public = _evaluation(payload, "public_or_cross_repo_update_shortcut")

    assert single["admitted"] is False
    assert single["label"] == "REJECTED_SINGLE_STATISTIC_FULL_PROFILE_COLLAPSE"
    assert mechanism["admitted"] is False
    assert mechanism["label"] == "REJECTED_MECHANISM_IMPORT"
    assert novelty["admitted"] is False
    assert novelty["label"] == "BLOCKED_NOVELTY_OVER_COMPETENCY_SHORTCUT"
    assert polycomputing["admitted"] is False
    assert polycomputing["label"] == "REJECTED_POLYCOMPUTING_OBJECTIVE_IDENTITY"
    assert public["admitted"] is False
    assert public["label"] == "BLOCKED_PUBLIC_OR_CROSS_REPO_UPDATE"


def test_json_serializable_and_forbidden_promotions_absent():
    payload = t494.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t494.VERDICT in dumped
    forbidden = (
        "region-indexed discriminator success proved",
        "claim promotion follows",
        "active inference imported",
        "public posture authorized",
        "cross-repo support proved",
        "novelty over competency proved",
    )
    for term in forbidden:
        assert term not in dumped
