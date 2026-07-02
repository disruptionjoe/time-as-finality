"""Tests for T416: Coupling-Graph Forcing Gate."""

import json

from models.coupling_graph_forcing_gate import (
    ARTIFACT,
    VERDICT,
    preserves_path_coupling_graph,
    preserves_singleton_operations,
    run_coupling_graph_forcing_gate,
)
from models.admissibility_derivation_probe import ENTANGLING_EQ_PRESERVER, FANIN


R = run_coupling_graph_forcing_gate()


def test_artifact_identity_and_scope():
    assert R["artifact"] == ARTIFACT
    assert R["claim_ledger_update"] == "none; no claim promotion"
    assert R["verdict"] == VERDICT


def test_separator_only_does_not_force_product_structure():
    packet = R["evidence_packets"]["separator_only"]
    assert packet["admissible_count_linear"] == 24
    assert packet["entangling_equality_preservers_admitted"] == 18
    assert packet["admits_entangling_equality_preserver"] is True
    assert packet["status"] == "does_not_force_product_or_coupling_structure"
    assert packet["independent_of_target_separator"] is False


def test_singleton_operation_support_excludes_entangling_equality_preservers():
    packet = R["evidence_packets"]["singleton_operation_support"]
    assert packet["admissible_count_linear"] == 6
    assert packet["admissible_count_with_local_bit_flips_if_affine_extended"] == 48
    assert packet["entangling_equality_preservers_admitted"] == 0
    assert packet["admits_entangling_equality_preserver"] is False
    assert packet["status"] == "forces_product_atoms_up_to_permutation_if_independent"


def test_path_coupling_graph_further_restricts_automorphisms():
    packet = R["evidence_packets"]["path_coupling_graph"]
    assert packet["admissible_count_linear"] == 2
    assert packet["admissible_count_with_local_bit_flips_if_affine_extended"] == 16
    assert packet["entangling_equality_preservers_admitted"] == 0
    assert sorted(packet["automorphism_permutations"]) == [[0, 1, 2], [2, 1, 0]]


def test_named_attacks_classify_correctly():
    ent = R["named_attacks"]["entangling_equality_preserver"]
    assert ent["equality_preserving"] is True
    assert ent["global_parity_preserving"] is True
    assert ent["preserves_singleton_operations"] is False
    assert preserves_singleton_operations(ENTANGLING_EQ_PRESERVER) is False
    assert preserves_path_coupling_graph(ENTANGLING_EQ_PRESERVER) is False

    fanin = R["named_attacks"]["fanin_localizer"]
    assert fanin["equality_preserving"] is False
    assert fanin["preserves_singleton_operations"] is False
    assert preserves_singleton_operations(FANIN) is False


def test_r2_burden_is_independent_operational_evidence():
    rule = R["decision_rule"]
    assert rule["separator_only"] == "insufficient_for_R2"
    assert "independently_measured" in rule["singleton_operations"]
    assert "independently_measured" in rule["coupling_graph"]
    assert "R2 is not discharged" in R["verdict"]
    assert "factorization-relative" in R["demotion_condition"]


def test_result_is_json_serializable():
    json.dumps(R, sort_keys=True)
