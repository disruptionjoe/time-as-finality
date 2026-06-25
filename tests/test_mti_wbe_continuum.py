"""Real checks for T227 MTI WBE-continuum screen.

These are assertions over models/mti_wbe_continuum.py, not placeholders.
Run: python -m pytest tests/test_mti_wbe_continuum.py
  or: python tests/test_mti_wbe_continuum.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow running this file directly (python tests/test_mti_wbe_continuum.py)
# by putting the repo root on the import path.
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from models.mti_wbe_continuum import (
    alpha_network,
    beta_network,
    run_wbe_screen,
    solve_total_cost,
)
from models.mti_cflow_solver import edge_loads, path_latency, solve_minimax_cflow


def _lats(net, flows):
    loads = edge_loads(net, flows)
    return [path_latency(net, p, loads) for p in net.paths]


def test_proxies_separate_and_agree_direction():
    r = run_wbe_screen(step=0.011)
    # Both post-hoc proxies put Beta above Alpha.
    assert r.beta_cv[1] > r.beta_cv[0]
    assert r.beta_hm[1] > r.beta_hm[0]
    assert r.proxy_direction_ok()


def test_total_cost_objective_preserves_separation():
    # The physical WEST total-cost optimization separates Alpha/Beta in the
    # SAME direction as the proxies: Beta is faster (smaller delivery cost),
    # hence higher beta.
    a = solve_total_cost(alpha_network(), step=0.011)
    b = solve_total_cost(beta_network(), step=0.011)
    assert b < a, "total-cost objective must rank Beta faster than Alpha"
    r = run_wbe_screen(step=0.011)
    assert r.total_direction_ok()
    assert r.beta_total[1] > r.beta_total[0]


def test_total_cost_routes_flow_through_secondary_branch():
    # The separation is real because the optimizer USES the slow/fast secondary
    # branch (p1): Beta routes strictly more flow through its faster branch.
    def opt_p1_flow(net):
        from models.mti_wbe_continuum import _total_cost, _grid_flows

        best = None
        bf = None
        for fl in _grid_flows(net, 0.0033):
            v = _total_cost(net, fl)
            if best is None or v < best:
                best = v
                bf = fl
        return bf[0]

    a_p1 = opt_p1_flow(alpha_network())
    b_p1 = opt_p1_flow(beta_network())
    assert a_p1 > 0.0 and b_p1 > 0.0, "secondary branch must carry flow"
    assert b_p1 > a_p1, "Beta exploits its faster secondary branch more than Alpha"


def test_minimax_equal_load_objective_DESTROYS_separation():
    # The minimax/equal-load objective (T201's only premise for the harmonic
    # mean) puts ZERO flow on the slow secondary branch in BOTH systems, so the
    # binding (equalized) latency is IDENTICAL and the separation vanishes.
    a_sol = solve_minimax_cflow(alpha_network(), step=0.001)
    b_sol = solve_minimax_cflow(beta_network(), step=0.001)
    assert abs(a_sol.value - b_sol.value) < 1e-6, (
        "minimax objective must NOT separate Alpha from Beta"
    )
    # Confirm the slow branch (p1) is abandoned in both.
    assert a_sol.flows[0] == 0.0
    assert b_sol.flows[0] == 0.0


def test_separation_is_objective_dependent():
    # The load-bearing finding: whether MTI's separation survives the WBE
    # optimization depends on WHICH WBE-faithful objective is chosen.
    r = run_wbe_screen(step=0.011)
    assert r.total_direction_ok() is True
    assert r.minimax_direction_ok() is False


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"PASS {name}")
    print("all checks passed")
