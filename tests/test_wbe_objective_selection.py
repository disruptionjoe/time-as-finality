"""T233: tests for the WBE objective-selection principle (the sharp MTI blocker).

Real checks (no placeholders) for models/wbe_objective_selection.py:

PART A (Gate 1, the load-bearing negative result):
  - the constrained-dissipation optimum is the AREA-INCREASING ratio n^{-1/3}
    (NOT the area-preserving n^{-1/2}), across several branching ratios n;
  - that optimum yields metabolic exponent a = 1, NOT 3/4;
  - the area-preserving ratio DOES give exactly 3/4 (closed form), confirming
    3/4 needs area-preserving as a SEPARATE input, not as the dissipation min.

PART B (Gate 2): dissipation min induces the total-cost objective, which loads
  every branch; the minimax/equal-load objective abandons the slow branch
  (reproduces T227).

PART C (resolution regime): under a hard coverage floor, minimax both separates
  Alpha/Beta and loads every branch -- the regime where equal-load fairness and
  metric content coexist.

Tags: finite_witness + poly_decider.
"""

from __future__ import annotations

from math import isclose

import pytest

from models.wbe_objective_selection import (
    BranchingTree,
    area_increasing_beta_r,
    area_preserving_beta_r,
    space_filling_gamma,
    check_dissipation_optimum,
    three_quarter_from_optimal_ratios,
    check_branch_loading,
    check_coverage_constrained_minimax,
    run_selection_principle,
)


# --------------------------------------------------------------------------
# PART A: Gate 1 -- dissipation min does NOT recover 3/4.
# --------------------------------------------------------------------------

@pytest.mark.parametrize("n", [4, 8, 16, 27])
def test_dissipation_optimum_is_area_increasing_not_area_preserving(n):
    """The constrained-dissipation minimizer is the area-INCREASING ratio
    n^{-1/3}, NOT the area-preserving ratio n^{-1/2} that gives 3/4."""
    opt = check_dissipation_optimum(n=n)
    assert opt.argmin_is_area_increasing, (
        f"n={n}: dissipation argmin {opt.beta_r_grid_argmin:.4f} "
        f"should equal area-increasing {opt.beta_r_area_increasing:.4f}"
    )
    assert not opt.argmin_is_area_preserving, (
        f"n={n}: dissipation argmin must NOT be the area-preserving ratio"
    )


@pytest.mark.parametrize("n", [4, 8, 16, 27])
def test_dissipation_optimum_gives_exponent_one_not_three_quarter(n):
    """At the dissipation optimum the metabolic exponent is a = 1, not 3/4.
    This is the core Gate-1 FAILURE: the WBE dissipation principle does not by
    itself select the 3/4 regime."""
    opt = check_dissipation_optimum(n=n)
    assert isclose(opt.exponent_at_optimum, 1.0, abs_tol=0.02), (
        f"n={n}: a@dissip-opt={opt.exponent_at_optimum:.4f} should be ~1.0"
    )
    assert not opt.recovers_three_quarter, (
        f"n={n}: dissipation min must NOT recover 3/4"
    )


@pytest.mark.parametrize("n", [4, 8, 16, 27, 64])
def test_area_preserving_ratios_give_exactly_three_quarter(n):
    """Closed-form: the AREA-PRESERVING + space-filling ratios give exactly
    a = 3/4 for every n. So 3/4 is real, but it requires the area-preserving
    impedance-matching condition as a separate physical input."""
    a = three_quarter_from_optimal_ratios(n=n)
    assert isclose(a, 0.75, abs_tol=1e-9), f"n={n}: area-preserving a={a}"


@pytest.mark.parametrize("n", [4, 8, 27])
def test_metabolic_exponent_formula_consistency(n):
    """The metabolic_exponent algebra agrees with the area-increasing /
    area-preserving regime values it is supposed to encode."""
    gamma = space_filling_gamma(n)
    ai = BranchingTree(n=n, beta_r=area_increasing_beta_r(n), gamma=gamma, levels=2)
    ap = BranchingTree(n=n, beta_r=area_preserving_beta_r(n), gamma=gamma, levels=2)
    assert isclose(ai.metabolic_exponent(), 1.0, abs_tol=1e-9)
    assert isclose(ap.metabolic_exponent(), 0.75, abs_tol=1e-9)


def test_impedance_monotone_decreasing_in_radius_no_interior_optimum():
    """Sanity: bare impedance has NO interior optimum (fatter is always less
    dissipative), which is exactly why the constraint (fixed volume) is needed.
    Confirms we did not accidentally smuggle a 3/4-selecting term into Z."""
    n, gamma = 8, space_filling_gamma(8)
    z_small = BranchingTree(n=n, beta_r=0.30, gamma=gamma, levels=10).total_impedance()
    z_mid = BranchingTree(n=n, beta_r=0.55, gamma=gamma, levels=10).total_impedance()
    z_big = BranchingTree(n=n, beta_r=0.90, gamma=gamma, levels=10).total_impedance()
    assert z_small > z_mid > z_big  # strictly decreasing in radius ratio


# --------------------------------------------------------------------------
# PART B: Gate 2 -- induced objective branch-loading.
# --------------------------------------------------------------------------

def test_total_cost_loads_every_branch_both_systems():
    """The objective the dissipation principle induces (total-cost) keeps every
    delivery branch loaded on BOTH Alpha and Beta -> passes Gate 2."""
    loading = check_branch_loading()
    tc = loading["total_cost"]
    assert tc.gate2_pass
    assert tc.alpha_all_loaded and tc.beta_all_loaded


def test_minimax_abandons_slow_branch_reproduces_t227():
    """The minimax/equal-load objective puts ZERO flow on the slow branch in
    both systems -> fails Gate 2, reproducing the T227 annihilation."""
    loading = check_branch_loading()
    mm = loading["minimax_equal_load"]
    assert not mm.gate2_pass
    # slow branch p1 is the first path; minimax zeroes it in both systems
    assert isclose(mm.alpha_flows[0], 0.0, abs_tol=1e-9)
    assert isclose(mm.beta_flows[0], 0.0, abs_tol=1e-9)


# --------------------------------------------------------------------------
# PART C: hard-coverage regime where equal-load and metric content coexist.
# --------------------------------------------------------------------------

@pytest.mark.parametrize("floor", [0.05, 0.10])
def test_coverage_constrained_minimax_separates_and_loads(floor):
    """Under a hard nonzero-flow floor on every branch, even the minimax
    objective separates Alpha from Beta AND loads every branch -- the regime
    where equal-load fairness and metric-temporal content coexist."""
    cc = check_coverage_constrained_minimax(floor=floor)
    assert cc.separates, f"floor={floor}: alpha={cc.alpha_value} beta={cc.beta_value}"
    assert cc.all_loaded
    # direction matches the proxies/total-cost: Beta is faster (smaller minimax)
    assert cc.beta_value < cc.alpha_value


# --------------------------------------------------------------------------
# Combined two-gate verdict.
# --------------------------------------------------------------------------

def test_two_gates_not_jointly_satisfied_by_one_principle():
    """The combined verdict: the SAME principle does not pass both gates.
    Dissipation min passes Gate 2 (loads branches) but FAILS Gate 1 (gives a=1,
    not 3/4). So no single WBE-native principle promotes MTI on these fixtures
    via dissipation minimization."""
    v = run_selection_principle()
    assert v.selected_objective == "total_cost"
    assert v.gate2_selected_loads_all_branches is True     # Gate 2 passes
    assert v.gate1_recovers_three_quarter is False         # Gate 1 fails
    assert v.both_gates_pass is False                      # NOT jointly satisfied
    # the separation does survive the selected (total-cost) objective, so the
    # blocker is purely Gate 1 (calibration), not Gate 2.
    assert v.separation_survives_selected is True
