"""Tests for T496 bridge-functor admission packet gate."""

from __future__ import annotations

import json

from models import bridge_functor_admission_packet_gate as t496


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t496.run()

    assert payload["artifact"] == t496.ARTIFACT
    assert payload["verdict"] == t496.VERDICT
    assert payload["source_synthesis"] == t496.SOURCE_SYNTHESIS
    assert payload["source_packet_report"] == t496.SOURCE_PACKET_REPORT
    assert payload["source_packet_template"] == t496.SOURCE_PACKET_TEMPLATE
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert payload["overall"]["external_publication"] is False
    assert payload["overall"]["cross_repo_truth_movement"] is False
    assert "Admission gate only" in payload["honest_ceiling"]


def test_complete_packets_are_admitted_as_review_targets_only():
    payload = t496.run()
    typed_gap = _decision(payload, "typed_gap_direct_preservation_packet")
    s1 = _decision(payload, "s1_independent_measure_packet")
    retrieval = _decision(payload, "bounded_retrieval_lower_bound_packet")

    for decision in (typed_gap, s1, retrieval):
        assert decision["admitted"] is True
        assert decision["label"] == "ADMITTED_BRIDGE_FUNCTOR_REVIEW_TARGET"
        assert decision["action"] == "review"
        assert decision["review_target_only"] is True
        assert decision["missing_requirements"] == []


def test_analogy_only_packet_is_rejected_without_domain_law_source():
    payload = t496.run()
    decision = _decision(payload, "analogy_only_geometry_restart")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_INCOMPLETE_ADMISSION_PACKET"
    assert "domain_native_law_or_theorem_source" in decision["missing_requirements"]


def test_closed_route_requires_named_new_key():
    payload = t496.run()
    decision = _decision(payload, "closed_route_without_new_key")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_CLOSED_ROUTE_WITHOUT_REQUIRED_NEW_KEY"
    assert "closed_route_new_key" in decision["missing_requirements"]


def test_core_packet_fields_and_absorber_status_are_required():
    payload = t496.run()
    missing_cap = _decision(payload, "missing_native_capability_object")
    absorber_only = _decision(payload, "absorbers_declared_only")
    no_spread = _decision(payload, "no_capability_spread_packet")

    assert missing_cap["admitted"] is False
    assert "native_capability_object" in missing_cap["missing_requirements"]
    assert absorber_only["admitted"] is False
    assert "tested_absorber_checks" in absorber_only["missing_requirements"]
    assert no_spread["admitted"] is False
    assert "capability_spread_evidence" in no_spread["missing_requirements"]


def test_governance_shortcuts_block_before_review_admission():
    payload = t496.run()
    decision = _decision(payload, "public_posture_shortcut_packet")

    assert decision["admitted"] is False
    assert decision["label"] == "BLOCKED_GOVERNANCE_OR_EXTERNAL_SHORTCUT"
    assert decision["action"] == "stop"
    assert "claim_movement" in decision["blocked_shortcuts"]
    assert "public_posture_movement" in decision["blocked_shortcuts"]
    assert "cross_repo_truth_movement" in decision["blocked_shortcuts"]


def test_closed_route_registry_preserves_current_reopen_keys():
    payload = t496.run()
    routes = payload["closed_routes"]

    assert routes["s1_finite_colimit"]["closing_tests"] == ["T490", "T491"]
    assert "independent_measure_law" in routes["s1_finite_colimit"]["required_new_keys"]
    assert routes["rg_reachability_quotient"]["closing_tests"] == ["T487", "T488"]
    assert "domain_native_morphism_class" in routes["rg_reachability_quotient"]["required_new_keys"]
    assert routes["bounded_record_retrieval"]["closing_tests"] == ["T495"]
    assert "source_checked_lower_bound" in routes["bounded_record_retrieval"]["required_new_keys"]


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t496.run()
    dumped = json.dumps(payload, sort_keys=True)

    assert t496.VERDICT in dumped
    forbidden = (
        "claim promotion follows",
        "public posture authorized",
        "cross-repo truth established",
        "theorem proved by admission",
        "physics support earned",
    )
    for term in forbidden:
        assert term not in dumped
