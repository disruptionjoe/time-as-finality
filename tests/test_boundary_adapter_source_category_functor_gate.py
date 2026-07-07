"""Tests for T504 boundary-adapter source-category functor gate."""

from __future__ import annotations

import json

from models import boundary_adapter_source_category_functor_gate as t504


def _decision(payload, packet_id):
    return next(item for item in payload["decisions"] if item["packet_id"] == packet_id)


def test_artifact_identity_and_scope():
    payload = t504.run()

    assert payload["artifact_id"] == t504.ARTIFACT_ID
    assert payload["verdict"] == t504.VERDICT
    assert payload["source_open_problem"] == t504.SOURCE_OPEN_PROBLEM
    assert payload["target_category_anchor"]["forms_proper_category"] is True
    assert payload["target_category_anchor"]["all_category_laws_hold"] is True
    assert payload["target_category_anchor"]["po1_is_functor_to_bool"] is False
    assert payload["overall"]["claim_movement"] is False
    assert payload["overall"]["public_posture_movement"] is False
    assert payload["overall"]["external_publication"] is False
    assert payload["overall"]["cross_repo_truth_movement"] is False
    assert payload["overall"]["sibling_repo_inspection"] is False


def test_source_category_fixture_has_category_laws():
    report = t504.evaluate_source_category(t504.source_category_fixture())

    assert report.identities_exist is True
    assert report.composition_closed is True
    assert report.associativity_holds is True
    assert report.left_units_hold is True
    assert report.right_units_hold is True
    assert report.forms_category is True
    assert report.object_count == 3
    assert report.morphism_count == 6
    assert report.composable_pair_count == 10


def test_valid_synthetic_functor_is_admitted_as_review_target_only():
    payload = t504.run()
    decision = _decision(payload, "synthetic_sector_restriction_functor")

    assert decision["admitted"] is True
    assert decision["label"] == "ADMITTED_SOURCE_CATEGORY_FUNCTOR_REVIEW_TARGET"
    assert decision["review_target_only"] is True
    assert decision["missing_requirements"] == []
    assert decision["functor_report"]["functor_laws_hold"] is True
    assert decision["functor_report"]["nonconstant_functor"] is True
    assert decision["functor_report"]["w_minus_maps_to_collective_complement"] is True


def test_object_only_and_missing_source_category_are_rejected():
    payload = t504.run()
    object_only = _decision(payload, "object_only_mirror_bridge")
    missing_source = _decision(payload, "missing_source_morphisms")

    assert object_only["admitted"] is False
    assert object_only["label"] == "REJECTED_OBJECT_ONLY_NOT_A_FUNCTOR"
    assert object_only["missing_requirements"] == ["morphism_map"]
    assert missing_source["admitted"] is False
    assert missing_source["label"] == "REJECTED_SOURCE_CATEGORY_NOT_BUILT"
    assert missing_source["missing_requirements"] == ["source_category"]


def test_constant_functor_control_is_rejected_even_when_functorial():
    payload = t504.run()
    decision = _decision(payload, "constant_functor_control")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_CONSTANT_FUNCTOR_CONTROL"
    assert "nonconstant_functor" in decision["missing_requirements"]
    assert decision["functor_report"]["functor_laws_hold"] is True
    assert decision["functor_report"]["nonconstant_functor"] is False


def test_bad_composite_map_fails_functor_law():
    payload = t504.run()
    decision = _decision(payload, "bad_composite_morphism_map")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_FUNCTOR_LAW_FAILURE"
    assert "functor_laws" in decision["missing_requirements"]
    assert decision["functor_report"]["composition_laws_hold"] is False
    assert decision["functor_report"]["failed_composition_checks"] == [
        "composition:restrict_to_mirror;restrict_to_wall"
    ]


def test_wrong_w_minus_target_is_rejected_after_functor_laws_pass():
    payload = t504.run()
    decision = _decision(payload, "w_minus_wrong_target")

    assert decision["admitted"] is False
    assert decision["label"] == "REJECTED_WRONG_W_MINUS_TARGET"
    assert "w_minus_collective_complement_target" in decision["missing_requirements"]
    assert decision["functor_report"]["functor_laws_hold"] is True
    assert decision["functor_report"]["w_minus_maps_to_collective_complement"] is False


def test_cross_repo_truth_shortcut_blocks_before_review_admission():
    payload = t504.run()
    decision = _decision(payload, "sibling_truth_shortcut")

    assert decision["admitted"] is False
    assert decision["label"] == "BLOCKED_CROSS_REPO_OR_GOVERNANCE_SHORTCUT"
    assert decision["action"] == "stop"
    assert "cross_repo_truth_movement" in decision["blocked_shortcuts"]
    assert "sibling_repo_truth_dependency" in decision["blocked_shortcuts"]


def test_future_packet_minimum_preserves_ct1_burdens():
    payload = t504.run()
    minimum = set(payload["future_packet_minimum"])

    assert "declare source morphisms that compose and have identities" in minimum
    assert "map every source morphism to a D1RestrictionMorphism" in minimum
    assert (
        "prove F(id) = id and F(g;f) = F(g);F(f) on the finite fixture"
        in minimum
    )
    assert (
        "keep admission review-only until sibling repo source-category truth is supplied by that repo"
        in minimum
    )


def test_json_serializable_and_forbidden_overreads_absent():
    payload = t504.run()
    rendered = json.dumps(payload, sort_keys=True)

    assert t504.VERDICT in rendered
    forbidden = (
        "mirror boundary proven",
        "GU/TaF adapter established",
        "claim promotion follows",
        "public posture authorized",
        "cross-repo truth established",
    )
    for phrase in forbidden:
        assert phrase not in rendered
