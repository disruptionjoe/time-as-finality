"""T443: Dolev-style redundancy feasibility gate.

This model follows the surviving topology lead after the T442 hostile review.
It does not assign a thermodynamic surcharge to communication topology.
Instead, it treats topology as an admission condition for robust distributed
finality under Byzantine holder faults.

Gate encoded here, for the classical synchronous point-to-point setting:

    n >= 3f + 1
    vertex_connectivity(G) >= 2f + 1

The code is a finite audit harness, not a proof of the distributed-systems
theorem. It keeps the Time-as-Finality reading narrow: D1 holder redundancy can
inherit a feasibility guard from known consensus theory; no H7 or heat-cost
claim is earned.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import asdict, dataclass

Edge = frozenset[int]
Graph = frozenset[Edge]


def edge(a: int, b: int) -> Edge:
    if a == b:
        raise ValueError("self-loops are not used in this gate")
    return frozenset((a, b))


def line_graph(n: int) -> Graph:
    return frozenset(edge(i, i + 1) for i in range(n - 1))


def star_graph(n: int) -> Graph:
    return frozenset(edge(0, i) for i in range(1, n))


def cycle_graph(n: int) -> Graph:
    if n < 3:
        return line_graph(n)
    return frozenset(edge(i, (i + 1) % n) for i in range(n))


def complete_graph(n: int) -> Graph:
    return frozenset(edge(i, j) for i in range(n) for j in range(i + 1, n))


def complete_bipartite_graph(left: int, right: int) -> tuple[int, Graph]:
    n = left + right
    return n, frozenset(edge(i, left + j) for i in range(left) for j in range(right))


def disconnected_pair_graph() -> tuple[int, Graph]:
    return 4, frozenset((edge(0, 1), edge(2, 3)))


def _neighbors(nodes: set[int], graph: Graph) -> dict[int, set[int]]:
    adj = {node: set() for node in nodes}
    for item in graph:
        a, b = tuple(item)
        if a in nodes and b in nodes:
            adj[a].add(b)
            adj[b].add(a)
    return adj


def is_connected(n: int, graph: Graph, removed: set[int] | None = None) -> bool:
    removed = removed or set()
    nodes = set(range(n)) - removed
    if len(nodes) <= 1:
        return True
    adj = _neighbors(nodes, graph)
    start = next(iter(nodes))
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in adj[node]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen == nodes


def vertex_connectivity(n: int, graph: Graph) -> int:
    """Exact vertex connectivity for small simple undirected graphs."""
    if n <= 1:
        return 0
    if not is_connected(n, graph):
        return 0
    if graph == complete_graph(n):
        return n - 1

    nodes = range(n)
    for r in range(1, n - 1):
        for removed in itertools.combinations(nodes, r):
            if not is_connected(n, graph, set(removed)):
                return r
    return n - 1


@dataclass(frozen=True)
class Fixture:
    fixture_id: str
    graph_name: str
    n: int
    graph: Graph
    faults: int


@dataclass(frozen=True)
class Audit:
    fixture_id: str
    graph_name: str
    n: int
    faults: int
    vertex_connectivity: int
    required_nodes: int
    required_vertex_connectivity: int
    admitted: bool
    blockers: tuple[str, ...]
    cost_claim_made: bool
    verdict: str


def audit_fixture(fx: Fixture) -> Audit:
    kappa = vertex_connectivity(fx.n, fx.graph)
    if fx.faults == 0:
        required_nodes = 1
        required_kappa = 1 if fx.n > 1 else 0
    else:
        required_nodes = 3 * fx.faults + 1
        required_kappa = 2 * fx.faults + 1

    blockers: list[str] = []
    if fx.n < required_nodes:
        blockers.append("node_count_below_3f_plus_1")
    if kappa < required_kappa:
        if fx.faults == 0:
            blockers.append("not_connected")
        else:
            blockers.append("vertex_connectivity_below_2f_plus_1")

    admitted = not blockers
    verdict = (
        "D1_HOLDER_REDUNDANCY_FEASIBILITY_ADMITTED_NO_COST_CLAIM"
        if admitted
        else "D1_HOLDER_REDUNDANCY_FEASIBILITY_BLOCKED_NO_COST_CLAIM"
    )
    return Audit(
        fixture_id=fx.fixture_id,
        graph_name=fx.graph_name,
        n=fx.n,
        faults=fx.faults,
        vertex_connectivity=kappa,
        required_nodes=required_nodes,
        required_vertex_connectivity=required_kappa,
        admitted=admitted,
        blockers=tuple(blockers),
        cost_claim_made=False,
        verdict=verdict,
    )


def build_fixtures() -> list[Fixture]:
    k33_n, k33 = complete_bipartite_graph(3, 3)
    disc_n, disc = disconnected_pair_graph()
    return [
        Fixture("t442_line_k5_f0", "line", 5, line_graph(5), 0),
        Fixture("t442_line_k5_f1", "line", 5, line_graph(5), 1),
        Fixture("t442_star_k5_f1", "star", 5, star_graph(5), 1),
        Fixture("t442_cycle_k5_f1", "cycle", 5, cycle_graph(5), 1),
        Fixture("t442_complete_k5_f1", "complete", 5, complete_graph(5), 1),
        Fixture("complete_k4_f1_minimal_pass", "complete", 4, complete_graph(4), 1),
        Fixture("cycle_k4_f1_connectivity_fail", "cycle", 4, cycle_graph(4), 1),
        Fixture("k33_f1_pass", "complete_bipartite_3_3", k33_n, k33, 1),
        Fixture("complete_k6_f2_node_count_fail", "complete", 6, complete_graph(6), 2),
        Fixture("cycle_k7_f2_connectivity_fail", "cycle", 7, cycle_graph(7), 2),
        Fixture("complete_k7_f2_minimal_pass", "complete", 7, complete_graph(7), 2),
        Fixture("disconnected_f0_fail", "disconnected_pair", disc_n, disc, 0),
    ]


def run_checks(audits: dict[str, Audit]) -> dict[str, bool]:
    checks = {
        "line_star_cycle_complete_kappas": (
            audits["t442_line_k5_f1"].vertex_connectivity == 1
            and audits["t442_star_k5_f1"].vertex_connectivity == 1
            and audits["t442_cycle_k5_f1"].vertex_connectivity == 2
            and audits["t442_complete_k5_f1"].vertex_connectivity == 4
        ),
        "f1_requires_three_vertex_connectivity": (
            audits["complete_k4_f1_minimal_pass"].admitted
            and not audits["cycle_k4_f1_connectivity_fail"].admitted
            and audits["k33_f1_pass"].admitted
        ),
        "f2_requires_seven_nodes_and_five_connectivity": (
            not audits["complete_k6_f2_node_count_fail"].admitted
            and not audits["cycle_k7_f2_connectivity_fail"].admitted
            and audits["complete_k7_f2_minimal_pass"].admitted
        ),
        "t442_graphs_reframed_as_feasibility_not_cost": (
            not audits["t442_line_k5_f1"].admitted
            and not audits["t442_star_k5_f1"].admitted
            and not audits["t442_cycle_k5_f1"].admitted
            and audits["t442_complete_k5_f1"].admitted
        ),
        "f0_reduces_to_plain_connectivity": (
            audits["t442_line_k5_f0"].admitted
            and not audits["disconnected_f0_fail"].admitted
        ),
        "no_thermodynamic_cost_claim_reintroduced": all(
            not audit.cost_claim_made for audit in audits.values()
        ),
    }
    checks["all_passed"] = all(checks.values())
    return checks


def run() -> dict:
    fixtures = build_fixtures()
    audits = {fx.fixture_id: audit_fixture(fx) for fx in fixtures}
    checks = run_checks(audits)
    return {
        "test_id": "T443",
        "title": "Dolev Redundancy Feasibility Gate",
        "tier": "recorded / finite admission gate",
        "theorem_boundary": (
            "Known consensus-theory feasibility condition, encoded here as an "
            "audit gate: n >= 3f + 1 and vertex connectivity >= 2f + 1 in the "
            "synchronous point-to-point Byzantine setting."
        ),
        "targets": ["A1", "D1 holder-redundancy axis"],
        "not_claimed": [
            "thermodynamic surcharge",
            "H7 physical arrow",
            "new distributed-systems theorem",
            "claim-ledger movement",
            "public-posture movement",
        ],
        "overall_verdict": (
            "DOLEV_REDUNDANCY_FEASIBILITY_GATE_BUILT_NO_COST_CLAIM"
            if checks["all_passed"]
            else "DOLEV_REDUNDANCY_FEASIBILITY_GATE_FAILED"
        ),
        "checks": checks,
        "audits": {key: asdict(value) for key, value in audits.items()},
    }


def main(write: bool = False) -> dict:
    result = run()
    print(json.dumps(result, indent=2))
    if write:
        out = "results/T443-dolev-redundancy-feasibility-gate-v0.1.json"
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print("wrote " + out)
    return result


if __name__ == "__main__":
    import sys

    main(write="--write-results" in sys.argv)
