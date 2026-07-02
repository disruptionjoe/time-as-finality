"""Tests for T398: Resource-Profile Absorber for the T397 C(R) object."""

import json

import pytest

from models.resource_profile_absorber import (
    ABSORBER_VERDICT,
    ARTIFACT,
    FALSIFICATION_CONDITION,
    run_resource_profile_absorber,
)


@pytest.fixture(scope="module")
def res():
    return run_resource_profile_absorber()


def test_artifact_identity_and_source(res):
    assert res["artifact"] == ARTIFACT
    assert res["source_artifact"] == "T397-region-capability-no-go"
    assert res["claim_ledger_update"] == "none; no claim promotion"


def test_resource_quotient_matches_t397_profiles(res):
    objs = res["resource_objects"]
    assert len(objs) == 12
    assert sum(len(obj["configs"]) for obj in objs) == 24
    assert all(obj["id"].startswith("U") and "_R" in obj["id"] for obj in objs)


def test_product_preorder_matches_t397_shape(res):
    rel = res["relations"]
    assert rel["relation_size"] == 48
    assert rel["preorder_size_including_reflexives"] == 60
    assert rel["n_incomparable_pairs"] == 18
    assert len(rel["strict_pairs"]) == 48


def test_two_axes_jointly_classify_and_are_monotone(res):
    audit = res["monotone_audit"]
    assert audit["n_undo_levels"] == 3
    assert audit["n_readout_levels"] == 4
    assert audit["axis_pair_count"] == 12
    assert audit["axes_jointly_classify"] is True
    assert audit["axes_monotone"] is True


def test_scalar_no_go_is_absorbed_as_resource_preorder(res):
    scalar = res["monotone_audit"]["scalar_absorbed"]
    assert scalar["t397_weak_orders_scanned"] == 4683
    assert scalar["t397_reproducing_scalars"] == 0
    assert "absorbed" in scalar["absorber_reading"]


def test_capability_factors_through_admitted_resource_profile(res):
    fact = res["factorization_audit"]
    assert fact["n_configs"] == 24
    assert fact["n_resource_objects"] == 12
    assert fact["same_resource_capability_splits"] == []
    assert fact["capability_factors_through_resource_profile"] is True
    assert fact["capability_test"]["factors_through_resource_profile"] is True


def test_statistics_flat_class_is_underdescribed_resource_shadow(res):
    flat = res["factorization_audit"]["statistics_flat_class"]
    assert flat["size"] == 16
    assert flat["stats_constant"] is True
    assert flat["n_resource_objects_realized"] == 12
    assert flat["spans_all_resource_objects"] is True
    assert res["factorization_audit"]["featured_pair_same_statistics_different_resource"] is True


def test_absorber_challenges_are_conservative(res):
    challenges = res["absorber_challenges"]
    assert challenges["anti_scalar_theorem_shape"]["status"] == "absorbed"
    assert challenges["statistics_flatness"]["status"] == "absorbed_as_incomplete_shadow"
    assert challenges["region_indexing"]["status"] == "absorbed_as_context_parameter"
    assert challenges["physical_realization"]["status"] == "translation_residue"


def test_verdict_and_falsification_are_restrained(res):
    assert res["absorber_verdict"] == ABSORBER_VERDICT
    assert "not a promoted resource-theory residue" in res["absorber_verdict"]
    assert res["falsification_condition"] == FALSIFICATION_CONDITION
    banned = ("theorem proved", "law", "new physics", "claim promotion")
    for text in (res["absorber_verdict"], res["falsification_condition"]):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, default=float, sort_keys=True)
