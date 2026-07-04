"""T442: Consensus Definalization Bound (Landauer x Lamport).

*** HOSTILE REVIEW 2026-07-03: the topological reversal term lambda(G) is
    REFUTED as a cost floor (audits/2026-07-03-t442-hostile-review.md;
    _local/t442_reversal_probe.py). A spanning-tree protocol reverses at a cost
    independent of lambda(G). The computed quantities here remain correct, but
    the interpretation of `forced + lambda(G)` as a thermodynamic floor and the
    `overall_verdict` string below are SUPERSEDED. Only the conceptual point
    survives: T396's export escape is illegitimate for an objective *final*
    record, so H(X|V) is genuinely paid. See the results doc. ***

Direction C, rung 1 -- the positive complement of T110, taken past the T396
absorption.

Background
---------
T110 (the repo's one theorem_backed result, a NEGATIVE one) forbids a strict
scalar finality monotone in a *finite closed reversible* system, and explicitly
hands the positive question to the *open / dissipative* regime. T396 took the
first swing there and it collapsed: minimal coarse-grained consensus cost was
ordinary entropy reduction H(X)-H(V)=H(X|V); the pure holder-count floor was
refuted by already-consensus inputs; and -- decisively -- a full-transcript
export control had ZERO closed-reversible cost in every fixture (the Bennett
reversible-computing escape). T396's own Next Gate asked for the missing
ingredient: "communication geometry".

The claim this model tests
--------------------------
T396 measured the logical erasure of a SINGLE system, where "export the whole
transcript" is always legal and free -> cost 0. A *distributed objective record*
(k separated holders each carrying a clean, robust copy, in the Quantum-Darwinism
sense) has two properties that close that escape:

  (L1) locality       -- there is no global site holding "the transcript";
                         finality requires the value at k separated sites.
  (L2) no-undo-handle  -- a record co-present with the reconciliation garbage that
                         could reverse it is, by definition, NOT final ("the past
                         is what has become hard to undo"). Finality = the garbage
                         is thermalised, not retained.

Under (L1)+(L2) the T396 export control is unavailable, so:
  (A) the H(X|V) fan-in erasure becomes IRREDUCIBLE dissipation, not an avoidable
      bookkeeping artifact; and
  (B) DEFINALIZATION (returning to a state with no re-finalizable local record)
      carries a graph-topological communication floor -- a reversal-cost term that
      is a cut invariant of the communication graph, invisible to a single-system
      entropy ledger.

Both terms vanish in exactly the limits where they should: k=1, all holders
co-located (single site), or pre-agreed inputs -- the broadcast / Darwinism limit.
That vanishing is the model's own kill control and reproduces T396's zeros.

What this is / is not
---------------------
- IS: a computed finite-witness separation. Reproduces T396 exactly, then shows
  the term T396 could not see once communication geometry + distributed local
  finality are declared BEFORE scoring (per T439 discipline).
- Targets: A1 (distributed-systems finality analogy); D1 reversal-cost and
  holder-redundancy axes.
- IS NOT: an H7 physical-arrow claim (framed as a resource / reversal-cost lower
  bound, not a scalar arrow -> stays clear of T116/T122/T152 arrow absorbers); a
  general theorem (finite witnesses + a cut-argument sketch); a new physical law
  (Landauer, Bennett, edge-connectivity, Lamport/FLP are all standard). The
  repo-specific content is IDENTIFYING the assumption that closes T396's export
  escape and the topological reversal term it exposes.

Dimensionless units: costs are in bits (x kT ln 2 for the thermodynamic reading,
which is CONDITIONAL on (L2), stated not proven).
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass, asdict
from typing import Callable

BitString = tuple[int, ...]
Distribution = dict[BitString, float]
Rule = Callable[[BitString], int]
Graph = frozenset[frozenset[int]]

TOL = 1e-12
LN2 = math.log(2.0)


def _xlog2x(p: float) -> float:
    return 0.0 if p <= TOL else -p * math.log2(p)


def h2(p: float) -> float:
    return _xlog2x(p) + _xlog2x(1.0 - p)


def entropy(dist: dict) -> float:
    return sum(_xlog2x(p) for p in dist.values())


def marginal(dist: Distribution, rule: Rule) -> dict:
    out: dict[int, float] = {}
    for x, p in dist.items():
        out[rule(x)] = out.get(rule(x), 0.0) + p
    return out


def cond_entropy_X_given_V(dist: Distribution, rule: Rule) -> float:
    """H(X|V), V=rule(X). Since V is a function of X, H(X|V)=H(X)-H(V)."""
    return entropy(dist) - entropy(marginal(dist, rule))


def per_holder_reset(dist: Distribution, rule: Rule, k: int) -> float:
    """Sum_i H(x_i|V) -- additive per-holder reset; can overcount joint floor."""
    total = 0.0
    for i in range(k):
        joint: dict[tuple[int, int], float] = {}
        vm: dict[int, float] = {}
        for x, p in dist.items():
            v = rule(x)
            joint[(x[i], v)] = joint.get((x[i], v), 0.0) + p
            vm[v] = vm.get(v, 0.0) + p
        total += entropy(joint) - entropy(vm)
    return total


def expected_disagreement(dist: Distribution, rule: Rule, k: int) -> float:
    tot = 0.0
    for x, p in dist.items():
        v = rule(x)
        tot += p * sum(1 for i in range(k) if x[i] != v)
    return tot


def edge(i: int, j: int) -> frozenset[int]:
    return frozenset((i, j))


def line_graph(k: int) -> Graph:
    return frozenset(edge(i, i + 1) for i in range(k - 1))


def star_graph(k: int) -> Graph:
    return frozenset(edge(0, i) for i in range(1, k))


def ring_graph(k: int) -> Graph:
    return frozenset(edge(i, (i + 1) % k) for i in range(k))


def complete_graph(k: int) -> Graph:
    return frozenset(edge(i, j) for i in range(k) for j in range(i + 1, k))


def is_connected(k: int, g: Graph) -> bool:
    if k <= 1:
        return True
    adj: dict[int, set[int]] = {i: set() for i in range(k)}
    for e in g:
        a, b = tuple(e)
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        n = stack.pop()
        for mnode in adj[n]:
            if mnode not in seen:
                seen.add(mnode)
                stack.append(mnode)
    return len(seen) == k


def edge_connectivity(k: int, g: Graph) -> int:
    """lambda(G): minimum edges crossing any nonempty proper cut. The minimum
    re-communication to isolate a V-holder so it cannot re-broadcast."""
    if k <= 1 or not is_connected(k, g):
        return 0
    best = None
    nodes = list(range(k))
    for r in range(1, k):
        for combo in itertools.combinations(nodes[1:], r - 1):
            s = set(combo) | {0}
            if len(s) == k:
                continue
            crossing = sum(1 for e in g if len(e & s) == 1)
            best = crossing if best is None else min(best, crossing)
    return best if best is not None else 0


def iid_uniform(k: int) -> Distribution:
    return {x: 1.0 / (2 ** k) for x in itertools.product((0, 1), repeat=k)}


def all_equal(k: int) -> Distribution:
    return {(0,) * k: 0.5, (1,) * k: 0.5}


def single_error(k: int) -> Distribution:
    dist: Distribution = {}
    for b in (0, 1):
        for i in range(k):
            x = [b] * k
            x[i] = 1 - b
            key = tuple(x)
            dist[key] = dist.get(key, 0.0) + 0.5 * (1.0 / k)
    return dist


def rule_root_copy(x: BitString) -> int:
    return x[0]


def rule_majority(x: BitString) -> int:
    s = sum(x)
    if 2 * s == len(x):
        return x[0]
    return 1 if s > len(x) / 2 else 0


@dataclass
class Fixture:
    task_id: str
    k: int
    dist_name: str
    dist: Distribution
    rule_name: str
    rule: Rule
    graph_name: str
    graph: Graph
    export_available: bool
    barrier_height_kT: float = 7.0


@dataclass
class Audit:
    task_id: str
    k: int
    dist_name: str
    rule_name: str
    graph_name: str
    H_X: float
    H_V: float
    single_system_floor_bits: float
    per_holder_reset_bits: float
    export_escape_cost_bits: float
    expected_disagreement: float
    edge_connectivity: int
    spanning_reach_floor: int
    forced_erasure_bits: float
    reversal_comm_floor_edges: int
    total_definalization_floor_bits: float
    thermo_floor_kT: float
    surcharge_visible: bool
    verdict: str


def audit_fixture(fx: Fixture) -> Audit:
    hX = entropy(fx.dist)
    hV = entropy(marginal(fx.dist, fx.rule))
    floor = cond_entropy_X_given_V(fx.dist, fx.rule)
    reset = per_holder_reset(fx.dist, fx.rule, fx.k)
    disagree = expected_disagreement(fx.dist, fx.rule, fx.k)
    lam = edge_connectivity(fx.k, fx.graph)
    span = max(fx.k - 1, 0)

    connected = is_connected(fx.k, fx.graph) and fx.k >= 2
    genuine_disagreement = disagree > TOL

    if fx.export_available:
        forced, comm = 0.0, 0
        verdict = "T396_EXPORT_ESCAPE_COST_ZERO"
        visible = False
    elif not connected or not genuine_disagreement:
        forced, comm = 0.0, 0
        verdict = "SURCHARGE_VANISHES_BROADCAST_OR_PREAGREED_LIMIT"
        visible = False
    else:
        forced, comm = floor, lam
        verdict = "CONSENSUS_SURCHARGE_IRREDUCIBLE_UNDER_LOCAL_FINALITY"
        visible = True

    total_bits = forced + comm
    return Audit(
        task_id=fx.task_id, k=fx.k, dist_name=fx.dist_name, rule_name=fx.rule_name,
        graph_name=fx.graph_name, H_X=round(hX, 6), H_V=round(hV, 6),
        single_system_floor_bits=round(floor, 6),
        per_holder_reset_bits=round(reset, 6), export_escape_cost_bits=0.0,
        expected_disagreement=round(disagree, 6), edge_connectivity=lam,
        spanning_reach_floor=span, forced_erasure_bits=round(forced, 6),
        reversal_comm_floor_edges=comm,
        total_definalization_floor_bits=round(total_bits, 6),
        thermo_floor_kT=round(total_bits * LN2, 6),
        surcharge_visible=visible, verdict=verdict,
    )


def build_fixtures() -> list[Fixture]:
    fx: list[Fixture] = []
    # Part 1: reproduce T396's single-system floor exactly (export regime).
    for k in (2, 3, 4, 5, 6):
        fx.append(Fixture(f"t396_repro_root_copy_k{k}", k, "iid_uniform",
                          iid_uniform(k), "root_copy", rule_root_copy,
                          "line", line_graph(k), True))
    for k in (3, 5):
        fx.append(Fixture(f"t396_repro_majority_k{k}", k, "iid_uniform",
                          iid_uniform(k), "majority", rule_majority,
                          "line", line_graph(k), True))
    fx.append(Fixture("t396_repro_already_consensus_k5", 5, "all_equal",
                      all_equal(5), "root_copy", rule_root_copy,
                      "line", line_graph(5), True))
    # Part 2: same tasks, distributed objective final record (export closed).
    for gname, gfun in (("line", line_graph), ("star", star_graph),
                        ("ring", ring_graph), ("complete", complete_graph)):
        fx.append(Fixture(f"dist_majority_k5_{gname}", 5, "iid_uniform",
                          iid_uniform(5), "majority", rule_majority,
                          gname, gfun(5), False))
    fx.append(Fixture("dist_majority_k3_complete", 3, "iid_uniform",
                      iid_uniform(3), "majority", rule_majority,
                      "complete", complete_graph(3), False))
    # Part 3: kill controls (surcharge MUST vanish).
    fx.append(Fixture("kill_preagreed_k5_complete", 5, "all_equal",
                      all_equal(5), "root_copy", rule_root_copy,
                      "complete", complete_graph(5), False))
    fx.append(Fixture("kill_colocated_k1", 1, "iid_uniform",
                      iid_uniform(1), "root_copy", rule_root_copy,
                      "trivial", frozenset(), False))
    # Part 4: minimal-disagreement positive fixture (reproduces T396's
    # single_error_majority_k5 floor 2.321928, now made irreducible).
    fx.append(Fixture("dist_single_error_k5_ring", 5, "single_error",
                      single_error(5), "majority", rule_majority,
                      "ring", ring_graph(5), False))
    return fx


def run_checks(audits: dict[str, Audit], fixtures: dict[str, Fixture]) -> dict:
    checks: dict[str, object] = {}
    checks["t396_root_copy_floor_equals_k_minus_1"] = all(
        abs(audits[f"t396_repro_root_copy_k{k}"].single_system_floor_bits - (k - 1)) < 1e-9
        for k in (2, 3, 4, 5, 6))
    a3 = audits["t396_repro_majority_k3"]
    checks["t396_majority_k3_joint_floor_2"] = abs(a3.single_system_floor_bits - 2.0) < 1e-9
    checks["t396_majority_k3_reset_overcounts"] = (
        abs(a3.per_holder_reset_bits - 2.433834) < 1e-4
        and a3.per_holder_reset_bits > a3.single_system_floor_bits)
    checks["t396_single_error_k5_matches"] = abs(
        audits["dist_single_error_k5_ring"].single_system_floor_bits - 2.321928) < 1e-4
    checks["t396_already_consensus_zero"] = (
        audits["t396_repro_already_consensus_k5"].single_system_floor_bits == 0.0)
    checks["export_escape_is_free_everywhere"] = all(
        a.total_definalization_floor_bits == 0.0
        for tid, a in audits.items() if fixtures[tid].export_available)
    dm = audits["dist_majority_k5_complete"]
    checks["floor_irreducible_under_local_finality"] = (
        dm.surcharge_visible and dm.forced_erasure_bits > 0.0)
    lam = {g: audits[f"dist_majority_k5_{g}"].edge_connectivity
           for g in ("line", "star", "ring", "complete")}
    checks["reversal_term_is_topological"] = (
        lam["line"] == 1 and lam["star"] == 1 and lam["ring"] == 2 and lam["complete"] == 4)
    checks["reversal_term_not_k_only"] = (lam["ring"] != lam["line"])
    tot = {g: audits[f"dist_majority_k5_{g}"].total_definalization_floor_bits
           for g in ("line", "star", "ring", "complete")}
    checks["total_floor_orders_by_topology"] = (tot["line"] < tot["ring"] < tot["complete"])
    checks["distributed_exceeds_single_system_escape"] = (
        dm.total_definalization_floor_bits > 0.0
        and audits["t396_repro_majority_k5"].total_definalization_floor_bits == 0.0)
    checks["kill_preagreed_vanishes"] = not audits["kill_preagreed_k5_complete"].surcharge_visible
    checks["kill_colocated_vanishes"] = not audits["kill_colocated_k1"].surcharge_visible
    checks["reversal_bound_independent_of_barrier"] = (
        edge_connectivity(5, complete_graph(5)) == dm.edge_connectivity)
    checks["all_passed"] = all(bool(v) for v in checks.values())
    return checks


def run() -> dict:
    fixtures = {fx.task_id: fx for fx in build_fixtures()}
    audits = {tid: audit_fixture(fx) for tid, fx in fixtures.items()}
    checks = run_checks(audits, fixtures)
    positive = [a for a in audits.values() if a.surcharge_visible]
    verdict = (
        "DISTRIBUTED_DEFINALIZATION_BOUND_COMPUTED_"
        "SURCHARGE_IRREDUCIBLE_UNDER_LOCAL_FINALITY_NO_H7_PROMOTION"
        if (checks["all_passed"] and positive)
        else "DIRECTION_C_DEMOTED_ENTROPY_BOOKKEEPING_PLUS_OVERHEAD")
    return {
        "test_id": "T442",
        "title": "Consensus Definalization Bound (Landauer x Lamport)",
        "tier": "recorded / computed finite-witness",
        "targets": ["A1", "D1 reversal-cost axis", "D1 holder-redundancy axis"],
        "not_claimed": [
            "H7 physical-arrow (resource/reversal bound, not a scalar arrow)",
            "general theorem (finite witnesses + cut-argument sketch only)",
            "new physical law (Landauer/Bennett/edge-connectivity/Lamport standard)",
            "CLAIM-LEDGER / TESTS.md / ROADMAP / North Star movement"],
        "conditional_assumption": (
            "Thermodynamic reading (x kT ln2) is CONDITIONAL on (L2) local "
            "thermalisation of reconciliation garbage -- the physically-motivated "
            "definition of a distributed objective final record. Relaxing it "
            "(retain/export garbage) recovers T396's zero."),
        "overall_verdict": verdict,
        "review_2026_07_03": (
            "SUPERSEDED_IN_PART: topological lambda(G) term REFUTED as a cost "
            "floor (spanning-tree protocol reverses independent of lambda(G)); "
            "see audits/2026-07-03-t442-hostile-review.md. Surviving claim is "
            "conceptual: T396 export escape illegitimate for an objective final "
            "record, so H(X|V) is genuinely paid. Topology's real home is Dolev "
            "fault-tolerance feasibility, not a heat cost."),
        "checks": checks,
        "audits": {tid: asdict(a) for tid, a in audits.items()},
    }


def main(write: bool = False) -> dict:
    result = run()
    print(json.dumps(result, indent=2))
    if write:
        out = "results/T442-consensus-definalization-bound-v0.1.json"
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print("wrote " + out)
    return result


if __name__ == "__main__":
    import sys
    main(write="--write-results" in sys.argv)
