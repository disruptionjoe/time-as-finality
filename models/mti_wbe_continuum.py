"""T227: MTI exact WBE-continuum derivation screen.

This module attacks the *only* remaining MTI blocker: whether the
metric-vs-causal beta separation found in T186/T187 (post-hoc proxies)
survives an *actual* West-Brown-Enquist-Moses joint energy-time
optimization, rather than a chosen functional form
beta = 0.75*(1 - CV(T))  (T186) or  beta = 1 - log(HM(T))/log(n)  (T187).

It does this WITHOUT inventing new physics. It reuses the physical
congestion-delay model already in models/mti_cflow_solver.py:

    delay(load) = tau / (1 - load/capacity)          (M/M/1-style queue cost)

which is the canonical transport-network delivery-time cost. The WBE
joint optimization is then made concrete as: allocate unit demand across
the available source-to-sink paths to minimize a *physical* delivery-time
objective, and ask whether the optimized objective separates two systems
(Alpha, Beta) that share identical causal order, identical event count,
identical entropy production, and identical free (uncongested) topology
EXCEPT for the metric delivery-time labels on one branch.

Three WBE-faithful objectives are screened, because the WBE continuum
derivation does not by itself privilege one:

  (1) TOTAL  = min_w sum_i w_i * latency_i(w)        (West total-cost form)
  (2) MINIMAX/equal-load = min_w max_i latency_i(w)  (T201 fairness form
      that is the *only* premise under which the harmonic mean appears)
  (3) MEAN free-flow time  = sum_i w_i * tau_i        (causal-blind control)

For each, we report the optimized objective for Alpha and Beta and whether
the sign of the separation matches the T186/T187 proxy direction
(Beta "better"/faster than Alpha => higher beta).

The point is a HONEST screen, not a promotion: we determine which finite
restriction in T186/T187 is load-bearing and whether dropping it (going to
the physical optimization) preserves the separation or dissolves it.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from typing import Sequence

from models.mti_cflow_solver import (
    Edge,
    PathNetwork,
    harmonic_mean,
    solve_minimax_cflow,
)


# ---------------------------------------------------------------------------
# Fixtures: Alpha and Beta as physical transport networks.
#
# Both have identical causal order (e1->{e2,e3}->e5, e4->e5) and identical
# topology of three source-to-sink delivery paths. They differ ONLY in the
# tau (free transit time) of the e4 secondary branch:
#   Alpha: slow secondary branch  -> free path times {4, 2, 1}
#   Beta:  fast secondary branch  -> free path times {3, 2, 1}
# This is exactly the T186/T187 metric difference, re-expressed as a network.
# ---------------------------------------------------------------------------

def _three_path_network(secondary_tau: float, capacity: float = 1.0) -> PathNetwork:
    """Three disjoint delivery paths with free times {secondary_tau, 2, 1}.

    Path P1 (slow primary, e1->e2->e5): free time = secondary_tau.
    Path P2 (e1->e3->e5):               free time = 2.
    Path P3 (e4->e5 secondary):         free time = 1.

    Capacity is shared per edge; paths are edge-disjoint so each path's
    congestion depends only on its own flow. This isolates the delivery-time
    metric as the only varying input, matching T186/T188 (G encodes topology,
    not timing).
    """
    return PathNetwork(
        edges={
            "p1": Edge(tau=secondary_tau, capacity=capacity),
            "p2": Edge(tau=2.0, capacity=capacity),
            "p3": Edge(tau=1.0, capacity=capacity),
        },
        paths=(("p1",), ("p2",), ("p3",)),
        demand=0.99,  # < total capacity 3.0; keeps all delays finite
    )


def alpha_network() -> PathNetwork:
    return _three_path_network(secondary_tau=4.0)


def beta_network() -> PathNetwork:
    return _three_path_network(secondary_tau=3.0)


# ---------------------------------------------------------------------------
# WBE-faithful objectives.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ObjectiveResult:
    name: str
    alpha_value: float
    beta_value: float

    @property
    def separates(self) -> bool:
        return not _isclose(self.alpha_value, self.beta_value)

    @property
    def beta_faster(self) -> bool:
        """True if Beta achieves a *smaller* (better) delivery objective."""
        return self.beta_value < self.alpha_value


def _isclose(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol


def _congested_latencies(network: PathNetwork, flows: Sequence[float]) -> list[float]:
    from models.mti_cflow_solver import edge_loads, path_latency

    loads = edge_loads(network, flows)
    return [path_latency(network, path, loads) for path in network.paths]


def _total_cost(network: PathNetwork, flows: Sequence[float]) -> float:
    lat = _congested_latencies(network, flows)
    return sum(w * l for w, l in zip(flows, lat))


def _grid_flows(network: PathNetwork, step: float):
    from models.mti_cflow_solver import _grid_simplex

    yield from _grid_simplex(network.demand, len(network.paths), step)


def solve_total_cost(network: PathNetwork, step: float = 0.01) -> float:
    """min_w sum_i w_i * congested_latency_i(w) -- West total-cost form."""
    best = None
    for flows in _grid_flows(network, step):
        v = _total_cost(network, flows)
        if best is None or v < best:
            best = v
    assert best is not None
    return best


def solve_minimax(network: PathNetwork, step: float = 0.01) -> float:
    """min_w max_i congested_latency_i(w) -- equal-load / fairness form (T201)."""
    return solve_minimax_cflow(network, step=step).value


def solve_mean_free(network: PathNetwork) -> float:
    """Uniform-flow mean of FREE (uncongested) path times.

    Causal-blind control: depends only on the multiset of free path times,
    i.e. the metric labels. Uniform split = no optimization."""
    tau = network.free_path_times()
    return sum(tau) / len(tau)


# ---------------------------------------------------------------------------
# Beta read-outs, made comparable across the proxy and the optimization.
# ---------------------------------------------------------------------------

def beta_cv_proxy(free_times: Sequence[float], calib: float = 0.75) -> float:
    """T186 proxy: beta = calib * (1 - CV(T))."""
    n = len(free_times)
    mean = sum(free_times) / n
    var = sum((t - mean) ** 2 for t in free_times) / n
    cv = sqrt(var) / mean
    return calib * (1 - cv)


def beta_hm_proxy(free_times: Sequence[float], n_scale: int) -> float:
    """T187 proxy: beta = 1 - log(HM(T)) / log(n_scale)."""
    hm = harmonic_mean(free_times)
    return 1 - log(hm) / log(n_scale)


def beta_from_optimized(objective_value: float, n_scale: int) -> float:
    """Map an optimized delivery objective T* to a beta via the SAME
    scaling relation T187 used (R = n^(1-beta) = T*), but now T* is the
    PHYSICALLY optimized delivery time, not a chosen summary.

    beta = 1 - log(T*) / log(n_scale).
    Lower optimized delivery time T* => higher beta (faster network).
    """
    if objective_value <= 0:
        raise ValueError("objective must be positive to take a log")
    return 1 - log(objective_value) / log(n_scale)


# ---------------------------------------------------------------------------
# Full screen.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class WBEScreenResult:
    objectives: tuple[ObjectiveResult, ...]
    beta_cv: tuple[float, float]          # (alpha, beta)
    beta_hm: tuple[float, float]
    beta_total: tuple[float, float]       # from optimized TOTAL objective
    beta_minimax: tuple[float, float]     # from optimized MINIMAX objective

    def proxy_direction_ok(self) -> bool:
        """Both proxies agree beta(Beta) > beta(Alpha)."""
        return self.beta_cv[1] > self.beta_cv[0] and self.beta_hm[1] > self.beta_hm[0]

    def total_direction_ok(self) -> bool:
        return self.beta_total[1] > self.beta_total[0]

    def minimax_direction_ok(self) -> bool:
        return self.beta_minimax[1] > self.beta_minimax[0]


def run_wbe_screen(step: float = 0.01) -> WBEScreenResult:
    a = alpha_network()
    b = beta_network()
    n_scale = 5  # event count, matches T187 n=5

    total = ObjectiveResult("total_cost", solve_total_cost(a, step), solve_total_cost(b, step))
    minimax = ObjectiveResult("minimax_equal_load", solve_minimax(a, step), solve_minimax(b, step))
    mean_free = ObjectiveResult("mean_free_time", solve_mean_free(a), solve_mean_free(b))

    beta_cv = (beta_cv_proxy(a.free_path_times()), beta_cv_proxy(b.free_path_times()))
    beta_hm = (beta_hm_proxy(a.free_path_times(), n_scale), beta_hm_proxy(b.free_path_times(), n_scale))
    beta_total = (
        beta_from_optimized(total.alpha_value, n_scale),
        beta_from_optimized(total.beta_value, n_scale),
    )
    beta_minimax = (
        beta_from_optimized(minimax.alpha_value, n_scale),
        beta_from_optimized(minimax.beta_value, n_scale),
    )

    return WBEScreenResult(
        objectives=(total, minimax, mean_free),
        beta_cv=beta_cv,
        beta_hm=beta_hm,
        beta_total=beta_total,
        beta_minimax=beta_minimax,
    )


if __name__ == "__main__":
    r = run_wbe_screen()
    print("=== WBE continuum-grounded screen: Alpha vs Beta ===")
    for o in r.objectives:
        print(f"{o.name:20s}  alpha={o.alpha_value:.6f}  beta={o.beta_value:.6f}  "
              f"separates={o.separates}  beta_faster={o.beta_faster}")
    print()
    print(f"beta_cv_proxy   alpha={r.beta_cv[0]:.4f} beta={r.beta_cv[1]:.4f} "
          f"dir_ok={r.beta_cv[1] > r.beta_cv[0]}")
    print(f"beta_hm_proxy   alpha={r.beta_hm[0]:.4f} beta={r.beta_hm[1]:.4f} "
          f"dir_ok={r.beta_hm[1] > r.beta_hm[0]}")
    print(f"beta_TOTAL_opt  alpha={r.beta_total[0]:.4f} beta={r.beta_total[1]:.4f} "
          f"dir_ok={r.total_direction_ok()}")
    print(f"beta_MINIMAX_opt alpha={r.beta_minimax[0]:.4f} beta={r.beta_minimax[1]:.4f} "
          f"dir_ok={r.minimax_direction_ok()}")
    print()
    print(f"proxy_direction_ok   = {r.proxy_direction_ok()}")
    print(f"total_direction_ok   = {r.total_direction_ok()}")
    print(f"minimax_direction_ok = {r.minimax_direction_ok()}")
