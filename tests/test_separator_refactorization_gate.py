"""Tests for T412: Separator Refactorization Gate."""

import json

import pytest

from models.separator_refactorization_gate import (
    ARTIFACT,
    VERDICT,
    run_separator_refactorization_gate,
)


@pytest.fixture(scope="module")
def res():
    return run_separator_refactorization_gate()


def test_artifact_identity_and_scope(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["residue_label"] == "factorization_guardrail_required"


def test_declared_factorization_has_global_only_separator(res):
    declared = res["declared_factorization"]
    assert declared["max_proper_subset_trace_distance"] == 0.0
    assert all(v == 0.0 for v in declared["proper_subset_trace_distances"].values())
    assert declared["full_trace_distance"] == 1.0
    parity = declared["full_parity_readout"]
    assert parity["even_state"] == {"even": 1.0, "odd": 0.0}
    assert parity["odd_state"] == {"even": 0.0, "odd": 1.0}
    assert parity["binary_success"] == 1.0


def test_product_structure_preserving_relabels_do_not_localize(res):
    relabels = res["structure_preserving_relabels"]
    assert relabels["n_permutation_flip_relabels"] == 48
    assert relabels["max_proper_subset_trace_distance_after_relabels"] == 0.0
    assert relabels["product_basis_spot_check"]["max_proper_subset_trace_distance"] == 0.0
    assert relabels["product_basis_spot_check"]["full_trace_distance"] == 1.0
    assert relabels["survives"] is True


def test_entangling_refactorization_localizes_parity(res):
    attack = res["entangling_refactorization_attack"]
    assert attack["map"] == "y0 = x0 xor x1 xor x2; y1 = x1; y2 = x2"
    assert attack["localized_factor"] == "0"
    assert attack["proper_subset_trace_distances"]["0"] == 1.0
    assert attack["localized_factor_trace_distance"] == 1.0
    assert attack["localized_factor_even_state"] == [[1.0, 0.0], [0.0, 0.0]]
    assert attack["localized_factor_odd_state"] == [[0.0, 0.0], [0.0, 1.0]]
    assert attack["full_trace_distance_after_refactorization"] == 1.0
    assert attack["collapses_if_admissible"] is True


def test_admissibility_verdict_is_the_result(res):
    verdict = res["admissibility_verdict"]
    assert verdict["product_structure_preserving_relabels"] == "pass"
    assert verdict["arbitrary_entangling_refactorizations"] == "fail"
    assert "operational tensor product" in verdict["rule_needed"]
    assert res["verdict"] == VERDICT
    assert "factorization/coupling-preservation" in res["verdict"]


def test_no_promotion_language(res):
    text = json.dumps(res, sort_keys=True)
    banned = ("new physics", "claim promotion earned", "physical-boundary result")
    assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, sort_keys=True)
