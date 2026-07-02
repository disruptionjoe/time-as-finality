"""Tests for T413: Legitimacy-as-Shapley Finality Probe.

Asserts the predeclared legs of tests/T413-legitimacy-shapley-finality-probe.md
(frozen before the model existed). Exploratory homology probe; no claim
promotion; ledger untouched. Cross-domain material is the object of study, not
evidence.
"""

from fractions import Fraction as F

from models.legitimacy_shapley_finality_probe import (
    run, DIV_A, DIV_B, DIV_C, N, S_R, FOCUS,
    shapley_by_dividends, shapley_by_permutations, v_of,
    joint_record_completion_verdict, restricted_games_agree,
)

R = run()


def test_leg1_shapley_crosscheck_and_efficiency():
    l1 = R["leg1_crosscheck_efficiency"]
    assert l1["dividend_eq_permutation"] is True
    assert l1["efficiency_A"] and l1["efficiency_B"] and l1["efficiency_C"]
    # predeclared closed-form Shapley vectors
    assert l1["phi_A"] == ["2", "2", "2", "0", "0"]
    assert l1["phi_B"] == ["3", "2", "2", "1", "0"]
    assert l1["phi_C"] == ["3", "3", "3", "1", "1"]
    assert l1["v_N"] == {"A": "6", "B": "8", "C": "11"}


def test_leg2_within_R_equality_both_pairs():
    l2 = R["leg2_within_R_equality"]
    assert l2["pair1_within_R_equal"] is True
    assert l2["pair2_within_R_equal"] is True


def test_leg3_shapley_separation_delta_one():
    l3 = R["leg3_shapley_separation"]
    assert l3["pair1_phi0_delta"] == "1"
    assert l3["pair2_phi0_delta"] == "1"


def test_leg4_joint_record_completion_split():
    l4 = R["leg4_joint_record_completion_SPLIT"]
    # Pair 1: ABSORBED via a proper-subset coalition {0,3}, size 2
    assert l4["pair1"]["verdict"] == "ABSORBED"
    assert l4["pair1"]["min_sep_coalition"] == [0, 3]
    assert l4["pair1"]["min_sep_size"] == 2
    assert l4["pair1"]["datum_in_proper_subset"] is True
    # Pair 2: SURVIVES proper-subset completion (R1); datum only in the whole
    assert l4["pair2"]["verdict"] == "SURVIVES-R1"
    assert l4["pair2"]["min_sep_coalition"] == sorted(N)
    assert l4["pair2"]["min_sep_size"] == len(N)
    assert l4["pair2"]["datum_in_proper_subset"] is False


def test_leg4_R1_certificate_all_proper_subsets_identical():
    # Exhaustive: every proper subset S !< N gives identical restricted games
    # for Pair 2 (the R1 certificate).
    for r in range(len(N)):
        from itertools import combinations
        for S in combinations(N, r):
            assert restricted_games_agree(DIV_A, DIV_C, S) is True
    # and the grand coalition is where they differ
    assert v_of(DIV_A, N) != v_of(DIV_C, N)


def test_leg5_relabel_localizes_but_breaks_axioms():
    l5 = R["leg5_relabel_vs_axioms"]
    # the declared boundary-blind re-weighting DOES move phi_0 (tries to localize)
    assert l5["boundary_blind_changes_phi0"] is True
    # but it is illegitimate: violates efficiency and/or symmetry
    assert not (l5["boundary_blind_efficient"] and l5["boundary_blind_symmetric"])
    # Shapley is legitimate: efficient AND symmetric
    assert l5["shapley_efficient"] is True
    assert l5["shapley_symmetric"] is True


def test_leg6_R2_datum_is_declared():
    l6 = R["leg6_R2_declared_honesty"]
    assert l6["datum_is_declared"] is True
    assert l6["boundary_physicality_reduces_to_declaration"] is True


def test_leg7_nash_multiplicity_vs_shapley_uniqueness():
    l7 = R["leg7_nash_multiplicity_vs_shapley_uniqueness"]
    # a positive-dimensional polytope of declared imputations
    assert l7["imputation_set_dimension"] == len(N) - 1 == 4
    assert l7["shapley_unique_point"] is True
    # Aumann-Shapley-flavored trend present for N = 3,4,5
    trend = l7["aumann_shapley_trend"]
    assert [row["N"] for row in trend] == [3, 4, 5]
    # the grand-coalition dividend's grip on a single share falls: 5/n
    assert [row["grand_dividend_contrib_to_phi_0"] for row in trend] == \
        ["5/3", "5/4", "1"]


def test_leg8_no_classical_no_marginal_separator():
    l8 = R["leg8_quantum_residue_negative"]
    assert l8["equal_games_identical_phi"] is True
    assert l8["pair1_phi_diff_has_coalition_witness"] is True
    assert l8["pair2_phi_diff_has_coalition_witness"] is True
    assert l8["no_marginal_separator_possible_classically"] is True


def test_homology_headline_wound_reproduces():
    """The headline: Pair 1 dies to joint-record completion exactly as T411 did
    (proper-subset query), while Pair 2 constructs a classical R1 object (datum
    in the whole) that the proper-subset move cannot absorb - but whose
    physicality is still declared (Leg 6)."""
    l4 = R["leg4_joint_record_completion_SPLIT"]
    assert l4["pair1"]["verdict"] == "ABSORBED"
    assert l4["pair2"]["verdict"] == "SURVIVES-R1"
    assert R["leg6_R2_declared_honesty"]["datum_is_declared"] is True
