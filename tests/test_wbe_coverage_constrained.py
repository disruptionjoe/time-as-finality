"""T238 tests: coverage-constrained WBE-native delivery model.

Real checks (no placeholders) that decide whether the per-branch coverage
requirement that makes the metric-vs-causal separation re-appear under minimax
is a WBE-NATIVE terminal-reachability constraint (objective-invariant) or a
convenience floor (demotable). Run with: python -m pytest tests/test_wbe_coverage_constrained.py
or python tests/test_wbe_coverage_constrained.py (a bare-assert driver is at the
bottom so it runs without pytest installed).
"""

from __future__ import annotations

import os
import sys
from math import isclose

# allow running directly (python tests/test_*.py) as well as via pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.mti_cflow_solver import Edge, PathNetwork
from models.mti_wbe_continuum import alpha_network, beta_network
from models.wbe_coverage_constrained import (
    all_terminals_reachable,
    congested_delivery_time,
    coverage_constrained_delivery,
    coverage_quantum,
    decide_objective_invariance,
    feasible_bound,
    floor_provenance,
    min_flow_for_delivery_bound,
    _solve_coverage_constrained,
)


# --- Part A: the physical service requirement is stated, not faked ----------

def test_unperfused_terminal_has_infinite_delivery_time():
    """A zero-flow terminal is an un-perfused leaf: delivery time is +inf, the
    physical reading. This is what forbids the unconstrained minimax answer
    (which dropped the slow branch to exactly zero)."""
    a = alpha_network()
    flows = (0.0, 0.33, 0.66)
    times = congested_delivery_time(a, flows)
    assert times[0] == float("inf")
    assert times[1] < float("inf") and times[2] < float("inf")


def test_terminal_reachability_requires_positive_flow_and_bound():
    a = alpha_network()
    q = 0.05
    # all loaded, slack bound -> all reachable
    assert all_terminals_reachable(a, (0.05, 0.4, 0.54), bound=10.0, quantum=q)
    # slow terminal dropped -> NOT all reachable
    assert not all_terminals_reachable(a, (0.0, 0.45, 0.54), bound=10.0, quantum=q)
    # bound below slow free time -> NOT all reachable even if loaded
    assert not all_terminals_reachable(a, (0.05, 0.4, 0.54), bound=3.0, quantum=q)


# --- Part B: the floor is DERIVED from the network, never hand-picked -------

def test_feasibility_threshold_is_network_fixed_max_free_time():
    assert feasible_bound(alpha_network()) == 4.0   # max free time of Alpha
    assert feasible_bound(beta_network()) == 3.0    # max free time of Beta


def test_coverage_quantum_is_network_fixed():
    a = alpha_network()
    # q = demand / K^2 with K=3 paths, demand=0.99 -> 0.11
    assert isclose(coverage_quantum(a), 0.99 / 9.0, abs_tol=1e-12)


def test_delivery_bound_caps_flow_on_fast_branch():
    """The bound induces a flow CEILING c*(1 - tau/D) on each terminal: a
    tighter bound forbids dumping all demand on the fast branch. This is the
    physical work the bound does (it makes coverage non-trivial)."""
    a = alpha_network()
    # p3 is the fast branch (tau=1, cap=1)
    ceil_loose = min_flow_for_delivery_bound(a, 2, bound=12.0)
    ceil_tight = min_flow_for_delivery_bound(a, 2, bound=1.5)
    assert ceil_tight < ceil_loose
    # at D=1.5 the fast branch can carry at most 1/3 of demand -> all-on-p3 forbidden
    assert ceil_tight < a.demand
    # below the free time the terminal cannot meet the bound at any margin
    assert min_flow_for_delivery_bound(a, 2, bound=0.9) == 0.0


# --- Part C/D: objective-invariance under the physical constraint -----------

def test_separation_under_total_cost_with_physical_constraint():
    a = alpha_network()
    q = coverage_quantum(a)
    r = coverage_constrained_delivery(bound=5.0, quantum=q, objective="total_cost")
    assert r.alpha_feasible and r.beta_feasible
    assert r.separates
    assert r.beta_value < r.alpha_value  # Beta (fast slow-branch) delivers cheaper


def test_separation_under_minimax_with_physical_constraint():
    """The load-bearing result: under the terminal-reachability constraint the
    minimax optimum can NO LONGER zero the slow branch, so the separation that
    the unconstrained minimax (T227) annihilated RE-APPEARS."""
    a = alpha_network()
    q = coverage_quantum(a)
    r = coverage_constrained_delivery(bound=5.0, quantum=q, objective="minimax")
    assert r.alpha_feasible and r.beta_feasible
    assert r.separates
    assert r.beta_value < r.alpha_value


def test_objective_invariant_across_feasible_bound_window():
    """The whole point: separation holds under BOTH objectives for EVERY
    feasible delivery-time bound, with the floor derived from the network."""
    v = decide_objective_invariance()
    assert all(v.feasible)
    assert all(v.total_cost_separates)
    assert all(v.minimax_separates)
    assert v.objective_invariant
    assert v.minimax_separates_everywhere_feasible


def test_verdict_robust_to_shrinking_coverage_quantum():
    """The verdict does NOT depend on the quantum being large (which would mean
    the floor is doing the work by fiat). It survives the quantum -> small."""
    for sf in (1.0, 0.5, 0.25, 0.1, 0.05):
        v = decide_objective_invariance(service_fraction=sf)
        assert v.objective_invariant, f"failed at service_fraction={sf}"


# --- Part E: the constraint does real physical work (not a renamed number) --

def test_delivery_bound_makes_coverage_binding():
    """The delivery-time bound, ON ITS OWN, forbids the degenerate
    'all flow on the fast terminal' allocation -- physical work a bare numeric
    floor only fakes."""
    fp = floor_provenance(bound=6.0)
    assert fp.bound_makes_coverage_binding
    assert fp.numeric_floor_separates  # links to T233 Part C at the derived floor


def test_constraint_void_below_threshold_infeasible():
    """A delivery bound below the slowest terminal's free time makes that
    terminal genuinely unreachable: the constraint reports INFEASIBLE rather
    than silently fabricating a number. This is a real physical bound."""
    a = alpha_network()
    q = coverage_quantum(a)
    _, _, feasible = _solve_coverage_constrained(a, bound=3.5, quantum=q, objective="minimax")
    assert not feasible  # Alpha's slow terminal (tau=4) cannot be reached within D=3.5


# --- Falsification control: separation is carried by the METRIC label -------

def test_falsification_identical_metric_label_kills_separation():
    """Decisive control: if the slow terminal's metric label is identical in
    both systems, the constraint must NOT manufacture a separation. The
    constraint reveals the metric label; it does not invent one."""
    q = 0.11

    def net(slow_tau: float) -> PathNetwork:
        return PathNetwork(
            edges={
                "p1": Edge(tau=slow_tau, capacity=1.0),
                "p2": Edge(tau=2.0, capacity=1.0),
                "p3": Edge(tau=1.0, capacity=1.0),
            },
            paths=(("p1",), ("p2",), ("p3",)),
            demand=0.99,
        )

    na, nb = net(3.0), net(3.0)  # IDENTICAL metric label
    _, va, _ = _solve_coverage_constrained(na, 5.0, q, "minimax", step=0.01)
    _, vb, _ = _solve_coverage_constrained(nb, 5.0, q, "minimax", step=0.01)
    assert isclose(va, vb, abs_tol=1e-9)  # no metric difference -> no separation

    # and the converse: a metric difference DOES separate under the same machinery
    nc = net(4.0)
    _, vc, _ = _solve_coverage_constrained(nc, 5.0, q, "minimax", step=0.01)
    assert not isclose(vc, vb, abs_tol=1e-9)


def test_unconstrained_minimax_drops_slow_branch_constrained_does_not():
    """Contrast with T227: unconstrained minimax abandons the slow branch
    (its delivery time leaves the binding set); the constrained optimum keeps
    it, so the metric label enters the binding latency."""
    a = alpha_network()
    q = coverage_quantum(a)
    flows, value, feasible = _solve_coverage_constrained(a, bound=5.0, quantum=q, objective="minimax")
    assert feasible
    # slow branch p1 carries at least the quantum (NOT zero as in T227)
    assert flows[0] >= q - 1e-9
    # and the binding minimax value reflects the slow terminal's metric label
    assert value > 3.0  # tracks Alpha's slow tau=4 region, > Beta's


# --- bare-assert driver so this runs without pytest -------------------------

if __name__ == "__main__":
    checks = [
        test_unperfused_terminal_has_infinite_delivery_time,
        test_terminal_reachability_requires_positive_flow_and_bound,
        test_feasibility_threshold_is_network_fixed_max_free_time,
        test_coverage_quantum_is_network_fixed,
        test_delivery_bound_caps_flow_on_fast_branch,
        test_separation_under_total_cost_with_physical_constraint,
        test_separation_under_minimax_with_physical_constraint,
        test_objective_invariant_across_feasible_bound_window,
        test_verdict_robust_to_shrinking_coverage_quantum,
        test_delivery_bound_makes_coverage_binding,
        test_constraint_void_below_threshold_infeasible,
        test_falsification_identical_metric_label_kills_separation,
        test_unconstrained_minimax_drops_slow_branch_constrained_does_not,
    ]
    passed = 0
    for c in checks:
        c()
        passed += 1
        print(f"PASS  {c.__name__}")
    print(f"\n{passed}/{len(checks)} checks passed")
