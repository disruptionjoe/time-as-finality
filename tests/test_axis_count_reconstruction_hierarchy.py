"""Tests for T394: Axis-Count Reconstruction Hierarchy.

Each theorem in tests/T394-axis-count-reconstruction-hierarchy.md gets
direct assertions:

  Theorem 1 (Reconstruction): minimal axis count == order dimension by
    exhaustive linear-extension search for every poset up to n = 6 (up to
    isomorphism), realizer rank magnitudes re-verified pairwise, and the
    tie-collapse loophole closed exhaustively (n <= 5 at d <= 2; n = 6 at
    d = 2 for every dimension-3 class) with the constructive lexicographic
    linearization verified on every first-found preorder witness.

  Theorem 2 (Anti-Scalar as d = 1): dim(P) = 1 iff chain over all classes;
    T49's 3-event witness regression -- its 2-axis success falls out as
    dim = 2, both for the abstract shape and for the actual T49 model's
    record order.

  Theorem 3 (Axis-Count Obstruction): dim(S_3) = 3 and dim(S_4) = 4 by
    exhaustive search; dim(S_5) = 5 by machine-checked certificate plus a
    verified explicit 5-realizer; the certificate is cross-validated
    against brute force on S_3 and S_4.

  Theorem 4 (Realizability): principal-downset record bases under T48's
    non-empty-subset containment rule reproduce every poset up to n = 6;
    the strict-downset variant fails outside antichains (the honest
    edge-case for the non-empty clause).

  House spotlight: S_3 as six PO1-admissible FinaliEvents; record order
    computed with T48's own `_compute_order` equals S_3; AM (T50) holds
    with 3 realizer-rank axes and fails for every proper axis subset.

Labeling convention: events 0..n-1; pairs (i, j) mean i <_P j; pair lists
index-sorted (lexicographic). See the model docstring.
"""

from __future__ import annotations

import pytest

from models.axis_count_reconstruction_hierarchy import (
    N_MAX_ISO_SWEEP,
    explicit_standard_realizer,
    find_axis_realizer,
    incomparable_pairs,
    is_chain,
    linear_extensions,
    magnitudes_from_realizer,
    minimal_axis_count,
    pairs_of_extension,
    record_bases,
    run_analysis,
    standard_example,
    t48_record_dependency_closure,
    verify_reconstruction,
)


@pytest.fixture(scope="module")
def res():
    return run_analysis()


# --------------------------------------------------------------------------- #
# Enumeration self-consistency
# --------------------------------------------------------------------------- #


def test_enumeration_iso_class_counts(res):
    # Counts computed here; they also match the remembered OEIS A000112
    # values (candidate prior art, from memory, unverified -- flagged in
    # the spec), but the assertion is against this run's own enumeration.
    assert res.enumeration["iso_class_counts"] == {
        1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318
    }


def test_enumeration_internal_identities_hold(res):
    # natural-labeled count == sum over classes of e(P) / |Aut(P)|, and
    # labeled counts == sum of n! / |Aut(P)| -- three independent
    # computations (subset enumeration, extension enumeration,
    # automorphism counting) agreeing.
    assert res.enumeration["natural_count_identity_holds"]
    assert res.enumeration["labeled_counts"] == {
        1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023
    }


def test_labeled_counts_match_prior_direction_a_report(res):
    # technical-reports/TECHNICAL-REPORT-direction-a-finite-anti-scalar-
    # generalization-v0.1.md computed 19 (n=3) and 219 (n=4) independently.
    assert res.enumeration["labeled_counts_match_prior_report"]


# --------------------------------------------------------------------------- #
# Theorem 1: Reconstruction iff dim <= d
# --------------------------------------------------------------------------- #


def test_theorem1_realizer_magnitudes_reconstruct_for_all_classes(res):
    assert res.theorem1["classes_checked"] == 405
    assert res.theorem1["realizer_rank_magnitudes_reconstruct_all"]


def test_theorem1_dimension_census(res):
    # Regression pin of the earned census: at n = 6 exactly one chain class,
    # 314 dimension-2 classes, and 3 dimension-3 classes.
    assert res.theorem1["dimension_census"][6] == {1: 1, 2: 314, 3: 3}
    for n in range(1, 6):
        assert set(res.theorem1["dimension_census"][n]) <= {1, 2}


def test_theorem1_tie_collapse_preorders_add_nothing(res):
    for n, tc in res.theorem1["tie_collapse"].items():
        assert tc["achieved_equals_dim_le_2"], f"n={n}"
        assert tc["achieved_equals_dim_le_1_at_d1"], f"n={n}"
    # weak-order counts are the Fubini numbers as enumerated this run
    assert res.theorem1["tie_collapse"][5]["weak_order_count"] == 541
    # at n <= 5 every poset has dim <= 2, so d=2 preorder pairs achieve ALL
    # labeled posets -- independently reproducing the labeled counts
    assert res.theorem1["tie_collapse"][5]["achieved_labeled_posets_d2"] == 4231


def test_theorem1_dim3_classes_have_no_two_preorder_representation(res):
    refutations = res.theorem1["dim3_two_preorder_refutation_n6"]
    assert len(refutations) == 3
    for r in refutations:
        assert not r["two_preorder_representation_found"]
        assert r["pairs_scanned"] == r["extending_weak_orders"] ** 2


def test_theorem1_lexicographic_linearization_verified_on_all_witnesses(res):
    assert res.theorem1["linearization_all_ok"]
    assert res.theorem1["linearization_witnesses_checked"] == 4473


def test_theorem1_holds(res):
    assert res.theorem1["holds"]


# --------------------------------------------------------------------------- #
# Theorem 2: Anti-Scalar as d = 1
# --------------------------------------------------------------------------- #


def test_theorem2_dim1_iff_chain_up_to_n6(res):
    assert res.theorem2["dim1_iff_chain_all_classes"]


def test_theorem2_t49_witness_regression(res):
    # T49's 3-event shape (e1, e2 < e3; e1 || e2): 2-axis success == dim 2.
    assert res.theorem2["t49_shape_dim"] == 2
    assert res.theorem2["t49_shape_incomparable_pairs_index_sorted"] == [(0, 1)]
    assert res.theorem2["t49_shape_realizer_reconstructs"]
    # cross-artifact: the actual T49 model's record order has dim 2 and its
    # own 2-axis comparison is an exact match.
    assert res.theorem2["t49_model_record_order_dim"] == 2
    assert res.theorem2["t49_model_2axis_exact_match"]
    assert res.theorem2["t49_model_relation_matches_shape"]


def test_theorem2_any_incomparable_pair_blocks_single_axis():
    # direct micro-check, independent of the sweep: the T49 shape has no
    # 1-axis realizer, and adding comparability (chain) restores it.
    t49_rel = frozenset({(0, 2), (1, 2)})
    assert find_axis_realizer(3, t49_rel, 1) is None
    chain = frozenset({(0, 1), (0, 2), (1, 2)})
    assert find_axis_realizer(3, chain, 1) is not None


def test_theorem2_holds(res):
    assert res.theorem2["holds"]


# --------------------------------------------------------------------------- #
# Theorem 3: Axis-count obstruction (standard examples)
# --------------------------------------------------------------------------- #


def test_theorem3_s3_needs_exactly_three_axes(res):
    s3 = res.theorem3["S3"]
    assert s3["brute_force_minimal_axis_count"] == 3
    assert s3["extension_count"] == 48 == s3["closed_form_count"]
    assert s3["realizer_intersection_exact"]
    assert s3["realizer_rank_magnitudes_reconstruct"]


def test_theorem3_s3_appears_in_n6_census_as_dim3(res):
    # S_3 has 6 events, so it is one of the 3 dimension-3 classes at n = 6.
    assert res.theorem1["dimension_census"][6][3] == 3
    n, rel = standard_example(3)
    dmin, _ = minimal_axis_count(n, rel)
    assert dmin == 3


def test_theorem3_s4_needs_exactly_four_axes(res):
    s4 = res.theorem3["S4"]
    assert not s4["d2_realizer_found"]
    ref = s4["d3_refutation"]
    assert not ref["realizer_found"]
    assert ref["automorphism_count"] == 24
    assert ref["extension_count"] == 720 == s4["closed_form_count"]
    assert ref["orbit_representatives"] == 30
    assert ref["tuples_scanned"] == 21600
    assert s4["realizer_intersection_exact"]
    assert s4["realizer_rank_magnitudes_reconstruct"]


def test_theorem3_s5_escapes_four_axes(res):
    s5 = res.theorem3["S5"]
    # certificate ingredients, all machine-checked
    assert s5["cross_pairs_all_present"]
    assert s5["diagonal_pairs_incomparable"]
    assert s5["pairwise_reversal_cycle_certificates"]
    assert s5["max_diagonal_reversals_any_extension"] == 1
    assert s5["extension_count"] == 17280 == s5["closed_form_count"]
    # upper bound: explicit verified 5-realizer
    assert s5["realizer_intersection_exact"]
    assert s5["realizer_rank_magnitudes_reconstruct"]
    assert s5["dim_upper_bound"] == 5
    # the d = 4 brute force is honestly not claimed
    assert "not attempted" in s5["d4_brute_force"]


def test_theorem3_certificate_cross_validated_against_brute_force(res):
    # The same certificate machinery holds on S_3 and S_4, where brute-force
    # exhaustive search independently gives the same minimal axis counts.
    for key, dmin in (("S3", 3), ("S4", 4)):
        cert = res.theorem3[key]
        assert cert["lower_bound_certified"]
        assert cert["max_diagonal_reversals_any_extension"] == 1
    assert res.theorem3["S3"]["brute_force_minimal_axis_count"] == 3
    assert not res.theorem3["S4"]["d3_refutation"]["realizer_found"]


def test_theorem3_explicit_realizer_reverses_exactly_one_diagonal_each():
    # L_k of the explicit S_d realizer reverses diagonal pair k and no other.
    for d in (3, 4, 5):
        realizer = explicit_standard_realizer(d)
        for k, ext in enumerate(realizer):
            pos = {x: i for i, x in enumerate(ext)}
            reversed_pairs = [i for i in range(d) if pos[d + i] < pos[i]]
            assert reversed_pairs == [k]


def test_theorem3_holds(res):
    assert res.theorem3["holds"]


# --------------------------------------------------------------------------- #
# Theorem 4: Realizability via record bases
# --------------------------------------------------------------------------- #


def test_theorem4_principal_downset_bases_realize_every_poset(res):
    assert res.theorem4["classes_checked"] == 405
    assert res.theorem4["faithful_variant_exact_all"]
    assert res.theorem4["single_basis_variant_exact_all"]
    assert res.theorem4["nonempty_clause_vacuous_for_principal_downsets"]


def test_theorem4_strict_downset_variant_fails_outside_antichains(res):
    # exactly one antichain class per n = 6 successes total (n = 1..6)
    assert res.theorem4["strict_downset_variant_exact_count"] == 6
    assert res.theorem4["strict_variant_succeeds_only_on_antichains"]
    witness = res.theorem4["strict_two_chain_failure_witness"]
    assert witness["fails"]
    assert witness["closure_pairs_index_sorted"] == []


def test_theorem4_two_chain_micro_witness():
    # direct micro-check of the non-empty-clause edge case: strict downsets
    # give the minimal event an empty target basis, so 0 < 1 is lost.
    chain2 = frozenset({(0, 1)})
    src, tgt = record_bases(2, chain2, "strict")
    assert tgt[0] == frozenset()
    assert t48_record_dependency_closure(2, src, tgt) == frozenset()
    src_p, tgt_p = record_bases(2, chain2, "faithful")
    assert all(tgt_p[e] for e in range(2))
    assert t48_record_dependency_closure(2, src_p, tgt_p) == chain2


def test_theorem4_holds(res):
    assert res.theorem4["holds"]


# --------------------------------------------------------------------------- #
# House-object spotlight: S_3 as FinaliEvents
# --------------------------------------------------------------------------- #


def test_house_spotlight_events_are_po1_admissible(res):
    sp = res.house_spotlight
    assert sp["all_po1_admissible"]
    assert set(sp["verdicts"]) == {"fully_admissible"}
    assert sp["event_names"] == [
        "s3_a1", "s3_a2", "s3_a3", "s3_b1", "s3_b2", "s3_b3"
    ]


def test_house_spotlight_record_order_is_s3(res):
    sp = res.house_spotlight
    assert sp["is_partial_order"]
    assert sp["order_matches_s3"]


def test_house_spotlight_am_holds_on_three_axes_and_fails_on_subsets(res):
    sp = res.house_spotlight
    assert sp["am_3axis_exact"]
    assert sp["am_3axis_matching_pairs"] == 36 == sp["am_3axis_total_pairs"]
    assert sp["am_proper_subsets_all_fail"]
    assert set(sp["am_proper_subsets_exact"]) == {
        "causal", "info", "obs_access",
        "causal,info", "causal,obs_access", "info,obs_access",
    }


# --------------------------------------------------------------------------- #
# Primitive sanity + verdict language
# --------------------------------------------------------------------------- #


def test_primitives_sanity_on_small_cases():
    # 2-antichain: dim 2, realizer verified
    rel = frozenset()
    dmin, realizer = minimal_axis_count(2, rel)
    assert dmin == 2
    assert verify_reconstruction(2, rel, realizer)
    # 3-chain: single extension, dim 1
    chain = frozenset({(0, 1), (0, 2), (1, 2)})
    assert is_chain(3, chain)
    assert len(linear_extensions(3, chain)) == 1
    assert incomparable_pairs(3, chain) == ()
    # magnitudes from a realizer are ranks
    mags = magnitudes_from_realizer(2, ((0, 1), (1, 0)))
    assert mags == [(1, 2), (2, 1)]
    assert pairs_of_extension((0, 1, 2)) == frozenset({(0, 1), (0, 2), (1, 2)})


def test_all_theorems_hold_and_verdict_language_is_restrained(res):
    assert res.all_theorems_hold
    v = res.verdict_language.lower()
    assert "no claim promotion" in v
    assert "no physics claim" in v
    assert "open question" in v
    assert res.caps["N_MAX_ISO_SWEEP"] == N_MAX_ISO_SWEEP == 6
