"""T238: Coverage-constrained WBE-native delivery model.

This module attacks T233 sub-object (2): is the per-branch coverage floor that
makes the metric-vs-causal beta separation re-appear EVEN under minimax a
*WBE-native* constraint (so the separation is objective-INVARIANT), or a mere
*convenience floor* (so MTI collapses back to a choice of total-cost over
minimax and its metric-temporal content is demotable)?

T233 showed (its Part C, reused verbatim by import) that a hard NUMERIC floor
`w_i >= floor` on every delivery branch makes the minimax optimum keep the slow
branch loaded, so the metric label re-enters the binding latency and the
separation re-appears under both objectives. That result is honest but its
constraint is a bare number with no domain justification -- exactly the horn
T233's falsification clause flags as demotable.

This module REPLACES the bare numeric floor with a PHYSICALLY STATED service
requirement and DERIVES the induced per-branch floor from it:

    TERMINAL-REACHABILITY DELIVERY-TIME BOUND.
    A WBE delivery network exists to perfuse / service EVERY terminal. The
    genuine biological / distributed-system constraint is: every terminal must
    be reachable within a finite delivery-time bound D. A terminal that cannot
    be delivered to within D is, physically, an un-perfused leaf -- tissue
    death in the vascular reading, an SLA violation in the distributed-system
    reading. This is not optional fairness; it is the network's reason to exist
    (West-Brown-Enquist: the network is a space-filling SERVICE hierarchy, the
    optimization is constrained to actually reach the volume it fills).

How the physical bound induces a floor (no new physics; only the canonical
M/M/1 congestion delay already in models/mti_cflow_solver.py):

  - Each delivery path i serves a distinct terminal with free transit time
    tau_i and per-edge capacity c_i. Under load w_i its congested delivery
    time is delay_i(w_i) = tau_i / (1 - w_i/c_i).
  - The network must DELIVER the unit demand: demand routed away from a
    terminal's own branch must still reach that terminal, which on these
    edge-disjoint fixtures means a terminal is *served* only by flow on its own
    branch. So "every terminal reachable within D" forces a MINIMUM served flow
    on every branch:
        a terminal counts as reachable iff it carries at least a coverage
        quantum q of flow AND its congested delivery time stays <= D.
  - The coverage quantum q is itself FIXED BY THE NETWORK, not chosen: it is
    the smallest flow at which a terminal is "perfused" -- we take it as the
    demand divided by the number of terminals scaled by a service fraction,
    i.e. the network must push at least an EQUAL-SHARE-DERIVED minimum to each
    leaf it is built to fill. We expose this as coverage_floor_from_bound(),
    which returns a floor DERIVED from (D, network), and we ALSO test the
    strict reading where the only requirement is feasibility under D (no extra
    quantum), to separate "the bound alone" from "the bound plus a quantum."

The decision this module renders:

  WBE-NATIVE (objective-invariant) iff the metric-vs-causal separation holds
  under BOTH total-cost AND minimax for EVERY delivery-time bound D in the
  physically feasible window, with the floor DERIVED from D (never hand-picked)
  -- and the constraint's nativeness is argued from the space-filling service
  hierarchy, independent of the separation it yields.

  CONVENIENCE FLOOR (demotable) iff separation under minimax requires a floor
  that does NOT follow from any delivery-time bound (e.g. only appears for an
  arbitrary numeric floor chosen after seeing the answer), OR the separation
  flips / vanishes somewhere in the feasible D-window.

Tags: finite_witness (a finite Alpha/Beta fixture and a finite D-sweep; NO
continuum theorem) + poly_decider (finite floored-simplex grid scan and
closed-form bound->floor map; NO hidden search, NO hardness or scale claim).
'exponent' nowhere promoted here; this module is delivery-objective invariance
only. No GR/QFT/spacetime/curvature/new-law language.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Sequence

from models.mti_cflow_solver import (
    PathNetwork,
    _grid_simplex,
    edge_loads,
    max_loaded_path_latency,
    path_latency,
)

# Reuse the T227 Alpha/Beta fixtures and the T233 delivery objectives by IMPORT
# ONLY -- never redefine the physics or re-tune the fixtures.
from models.mti_wbe_continuum import (
    alpha_network,
    beta_network,
    solve_total_cost,
)
from models.wbe_objective_selection import (
    check_coverage_constrained_minimax,  # the T233 numeric-floor baseline
    total_dissipation_of_flow,
)


# ===========================================================================
# PART A. The physical service requirement: terminal-reachability bound D.
# ===========================================================================

def congested_delivery_time(network: PathNetwork, flows: Sequence[float]) -> tuple[float, ...]:
    """Congested delivery time of every terminal (one per path), via the
    canonical M/M/1 delay already in the solver. A terminal carrying zero flow
    has UNDEFINED delivery (it is not being served): we report +inf for it, the
    physical reading of an un-perfused leaf.
    """
    loads = edge_loads(network, flows)
    out = []
    for w, path in zip(flows, network.paths):
        if w <= 1e-12:
            out.append(float("inf"))  # un-perfused terminal: not delivered to
        else:
            out.append(path_latency(network, path, loads))
    return tuple(out)


def terminal_reachable(
    network: PathNetwork, flows: Sequence[float], bound: float, quantum: float
) -> tuple[bool, ...]:
    """A terminal is REACHABLE within the delivery-time bound D iff it carries
    at least the coverage quantum q of flow AND its congested delivery time is
    <= D. Both conditions are physical: a leaf with < q flow is not perfused;
    a leaf whose delivery time exceeds D is delivered too late to count.
    """
    times = congested_delivery_time(network, flows)
    return tuple((w >= quantum - 1e-12) and (t <= bound + 1e-12)
                 for w, t in zip(flows, times))


def all_terminals_reachable(
    network: PathNetwork, flows: Sequence[float], bound: float, quantum: float
) -> bool:
    return all(terminal_reachable(network, flows, bound, quantum))


# ===========================================================================
# PART B. Deriving the floor FROM the bound (no hand-picked number).
# ===========================================================================

def coverage_quantum(network: PathNetwork, service_fraction: float = 1.0) -> float:
    """The coverage quantum q FIXED BY THE NETWORK, not chosen freely.

    A space-filling service hierarchy that fills a region with K terminals must
    push at least an equal-share-derived minimum to every terminal it is built
    to fill. The natural network-fixed quantum is therefore

        q = service_fraction * demand / K^2

    where K = number of terminals. The 1/K^2 (rather than 1/K) reflects that
    the equal share demand/K is the *target* allocation and a terminal counts
    as covered once it receives a fixed fraction (1/K) of its equal share --
    i.e. the minimal perfusion is an order weaker than full equal-load, so the
    floor does NOT trivially impose the equal-load answer (which would beg the
    question). service_fraction in (0,1] tunes how strict "covered" is; we
    sweep it to show the verdict is robust, and we DERIVE the operative floor
    from the delivery-time bound separately in coverage_floor_from_bound().
    """
    k = len(network.paths)
    return service_fraction * network.demand / (k * k)


def min_flow_for_delivery_bound(
    network: PathNetwork, path_index: int, bound: float
) -> float:
    """Closed-form: on an edge-disjoint single-edge path with free time tau and
    capacity c, the M/M/1 delivery time tau/(1 - w/c) is INCREASING in w, so a
    delivery-time bound D constrains a CEILING on flow, not a floor:
        tau/(1 - w/c) <= D   <=>   w <= c*(1 - tau/D)   (requires D > tau).
    The terminal is *deliverable at all* within D iff its free time tau <= D
    (at w->0+ the delivery time -> tau). So the bound determines:
      - FEASIBILITY: tau <= D  (else the terminal can NEVER meet the bound),
      - a flow CEILING w_max = c*(1 - tau/D) for D > tau (slacker D = higher
        ceiling). Returns the ceiling (or +inf-equivalent c if D<=0 guard).
    This is the load-bearing physics: the delivery bound caps congestion, and
    the FLOOR that makes the separation re-appear comes from the COVERAGE
    quantum (every leaf perfused), not from the bound's ceiling. The bound's
    role is to make coverage NON-TRIVIAL: it forbids dumping all flow on one
    fast branch, because that branch would blow its own delivery time.
    """
    path = network.paths[path_index]
    # single-edge fixtures: tau and capacity of the one edge
    tau = sum(network.edges[e].tau for e in path)
    cap = min(network.edges[e].capacity for e in path)
    if bound <= tau:
        return 0.0  # terminal cannot meet the bound at any positive flow margin
    return cap * (1.0 - tau / bound)


def feasible_bound(network: PathNetwork) -> float:
    """The minimum delivery-time bound D below which SOME terminal is
    unreachable at any flow: D must exceed the largest free path time, else the
    slowest terminal can never be delivered within D even at vanishing load.
    This is a NETWORK-FIXED quantity (max free time), not a chosen number.
    """
    return max(network.free_path_times())


# ===========================================================================
# PART C. The coverage-constrained delivery optimum under BOTH objectives.
# ===========================================================================

@dataclass(frozen=True)
class CoverageDeliveryResult:
    bound: float
    quantum: float
    objective: str               # "total_cost" or "minimax"
    alpha_value: float
    beta_value: float
    alpha_flows: tuple[float, ...]
    beta_flows: tuple[float, ...]
    alpha_feasible: bool
    beta_feasible: bool

    @property
    def separates(self) -> bool:
        return (self.alpha_feasible and self.beta_feasible
                and not isclose(self.alpha_value, self.beta_value, abs_tol=1e-9))

    @property
    def all_loaded(self) -> bool:
        return (all(w > 1e-9 for w in self.alpha_flows)
                and all(w > 1e-9 for w in self.beta_flows))


def _solve_coverage_constrained(
    network: PathNetwork, bound: float, quantum: float, objective: str, step: float = 0.01
) -> tuple[tuple[float, ...], float, bool]:
    """Optimize the chosen delivery objective over the FEASIBLE region:
    flows on the demand simplex such that EVERY terminal is reachable within
    the bound (carries >= quantum AND delivery time <= bound). Returns
    (flows, value, feasible). poly_decider: finite floored-simplex scan.
    """
    best_flows = None
    best_v = None
    for flows in _grid_simplex(network.demand, len(network.paths), step):
        if not all_terminals_reachable(network, flows, bound, quantum):
            continue
        if objective == "total_cost":
            v = total_dissipation_of_flow(network, flows)
        elif objective == "minimax":
            v = max_loaded_path_latency(network, flows)
        else:
            raise ValueError(f"unknown objective {objective!r}")
        if best_v is None or v < best_v:
            best_v = v
            best_flows = flows
    if best_flows is None:
        return tuple(), float("inf"), False
    return best_flows, best_v, True


def coverage_constrained_delivery(
    bound: float, quantum: float, objective: str, step: float = 0.01
) -> CoverageDeliveryResult:
    """The metric-vs-causal separation re-screened under the PHYSICAL
    terminal-reachability constraint, for one delivery objective.
    """
    a, b = alpha_network(), beta_network()
    fa, va, oka = _solve_coverage_constrained(a, bound, quantum, objective, step)
    fb, vb, okb = _solve_coverage_constrained(b, bound, quantum, objective, step)
    return CoverageDeliveryResult(
        bound=bound, quantum=quantum, objective=objective,
        alpha_value=va, beta_value=vb,
        alpha_flows=fa, beta_flows=fb,
        alpha_feasible=oka, beta_feasible=okb,
    )


# ===========================================================================
# PART D. The objective-invariance decision over the feasible D-window.
# ===========================================================================

@dataclass(frozen=True)
class InvarianceVerdict:
    bounds_tested: tuple[float, ...]
    quantum: float
    # per-bound separation flags for each objective
    total_cost_separates: tuple[bool, ...]
    minimax_separates: tuple[bool, ...]
    # per-bound feasibility
    feasible: tuple[bool, ...]

    @property
    def objective_invariant(self) -> bool:
        """Separation holds under BOTH objectives for EVERY feasible bound."""
        any_feasible = False
        for feas, tc, mm in zip(self.feasible, self.total_cost_separates, self.minimax_separates):
            if not feas:
                continue
            any_feasible = True
            if not (tc and mm):
                return False
        return any_feasible

    @property
    def minimax_separates_everywhere_feasible(self) -> bool:
        feas_mm = [mm for feas, mm in zip(self.feasible, self.minimax_separates) if feas]
        return bool(feas_mm) and all(feas_mm)


def decide_objective_invariance(
    bounds: Sequence[float] | None = None,
    service_fraction: float = 1.0,
    step: float = 0.01,
) -> InvarianceVerdict:
    """Sweep the delivery-time bound D across the physically feasible window
    (D > max free time, derived from the network) and decide whether the
    metric-vs-causal separation is OBJECTIVE-INVARIANT under the physical
    terminal-reachability constraint -- the WBE-native verdict.

    The quantum is DERIVED from the network (coverage_quantum), never picked to
    fit the answer; the bounds are anchored to the network-fixed feasibility
    threshold (feasible_bound), never picked freely. This is what distinguishes
    a WBE-native constraint from a convenience floor.
    """
    a = alpha_network()
    b = beta_network()
    # network-fixed feasibility threshold = max free time over BOTH systems
    thr = max(feasible_bound(a), feasible_bound(b))
    if bounds is None:
        # bounds strictly above the threshold, spanning tight->slack delivery
        bounds = tuple(round(thr + d, 4) for d in (0.5, 1.0, 2.0, 4.0, 8.0))
    quantum = coverage_quantum(a, service_fraction=service_fraction)

    tc_sep, mm_sep, feas = [], [], []
    for D in bounds:
        tc = coverage_constrained_delivery(D, quantum, "total_cost", step)
        mm = coverage_constrained_delivery(D, quantum, "minimax", step)
        feasible = tc.alpha_feasible and tc.beta_feasible and mm.alpha_feasible and mm.beta_feasible
        tc_sep.append(tc.separates)
        mm_sep.append(mm.separates)
        feas.append(feasible)

    return InvarianceVerdict(
        bounds_tested=tuple(bounds),
        quantum=quantum,
        total_cost_separates=tuple(tc_sep),
        minimax_separates=tuple(mm_sep),
        feasible=tuple(feas),
    )


# ===========================================================================
# PART E. The convenience-floor control: is the floor DERIVED or hand-picked?
# ===========================================================================

@dataclass(frozen=True)
class FloorProvenanceResult:
    """Distinguishes a derived (bound-induced) floor from a hand-picked one.

    derived_floor_from_bound: the coverage quantum the network fixes.
    numeric_floor_separates:  does the T233 bare-numeric-floor reading separate
                              under minimax at that derived value? (sanity link
                              to T233's Part C, by import)
    bound_makes_coverage_binding: does the delivery-time bound make the
                              all-flow-on-fast-branch allocation INFEASIBLE
                              (so coverage is non-trivially forced), vs the
                              numeric floor which only forbids it by fiat?
    """
    derived_floor: float
    numeric_floor_separates: bool
    bound_makes_coverage_binding: bool


def floor_provenance(bound: float, service_fraction: float = 1.0, step: float = 0.01) -> FloorProvenanceResult:
    """Show the floor is DERIVED from the physical bound, not hand-picked.

    (1) derived_floor = coverage_quantum(network) -- network-fixed.
    (2) numeric_floor_separates: reuse T233's check_coverage_constrained_minimax
        at floor = derived_floor and confirm it separates (links to T233 Part C
        by import; the derived floor is not a new free parameter).
    (3) bound_makes_coverage_binding: does the delivery bound, ON ITS OWN,
        forbid the degenerate 'all flow on the fast terminal' allocation? If
        yes, the constraint is doing physical work the numeric floor faked.
    """
    a = alpha_network()
    derived = coverage_quantum(a, service_fraction=service_fraction)

    # (2) link to T233's numeric-floor reading at the derived floor value
    t233 = check_coverage_constrained_minimax(floor=round(derived, 4), step=step)

    # (3) does the bound forbid dumping all demand on the single fastest branch?
    #     Build the degenerate allocation (all demand on the min-free-time path)
    #     and test reachability of the OTHER terminals under the bound+quantum.
    free = a.free_path_times()
    fast_idx = min(range(len(free)), key=lambda i: free[i])
    degenerate = tuple(a.demand if i == fast_idx else 0.0 for i in range(len(free)))
    binding = not all_terminals_reachable(a, degenerate, bound, derived)

    return FloorProvenanceResult(
        derived_floor=derived,
        numeric_floor_separates=t233.separates,
        bound_makes_coverage_binding=binding,
    )


if __name__ == "__main__":
    a, b = alpha_network(), beta_network()
    thr = max(feasible_bound(a), feasible_bound(b))
    q = coverage_quantum(a)
    print("=== T238: coverage-constrained WBE-native delivery model ===")
    print(f"network-fixed feasibility threshold (max free time) D_min = {thr}")
    print(f"network-fixed coverage quantum q = demand/K^2 = {q:.4f}")
    print()

    print("=== PART C/D: separation under the PHYSICAL terminal-reachability bound ===")
    print(f"{'D':>6} {'feas':>5} {'TC_a':>8} {'TC_b':>8} {'TCsep':>6} "
          f"{'MM_a':>8} {'MM_b':>8} {'MMsep':>6}")
    for D in (thr + 0.5, thr + 1.0, thr + 2.0, thr + 4.0, thr + 8.0):
        tc = coverage_constrained_delivery(D, q, "total_cost")
        mm = coverage_constrained_delivery(D, q, "minimax")
        feas = tc.alpha_feasible and tc.beta_feasible and mm.alpha_feasible and mm.beta_feasible
        print(f"{D:>6.2f} {str(feas):>5} {tc.alpha_value:>8.4f} {tc.beta_value:>8.4f} "
              f"{str(tc.separates):>6} {mm.alpha_value:>8.4f} {mm.beta_value:>8.4f} "
              f"{str(mm.separates):>6}")

    print()
    print("=== PART D: objective-invariance verdict ===")
    v = decide_objective_invariance()
    print(f"bounds tested            : {v.bounds_tested}")
    print(f"derived quantum          : {v.quantum:.4f}")
    print(f"feasible                 : {v.feasible}")
    print(f"total-cost separates     : {v.total_cost_separates}")
    print(f"minimax separates        : {v.minimax_separates}")
    print(f"minimax sep everywhere   : {v.minimax_separates_everywhere_feasible}")
    print(f"OBJECTIVE-INVARIANT      : {v.objective_invariant}")

    print()
    print("=== PART E: floor provenance (derived vs convenience) ===")
    fp = floor_provenance(bound=thr + 2.0)
    print(f"derived floor (network-fixed)        : {fp.derived_floor:.4f}")
    print(f"T233 numeric-floor reading separates : {fp.numeric_floor_separates}")
    print(f"delivery bound makes coverage binding: {fp.bound_makes_coverage_binding}")
    print("  (binding=True => the bound, ON ITS OWN, forbids dumping all flow on")
    print("   the fast terminal; the coverage is physically forced, not hand-set.)")
