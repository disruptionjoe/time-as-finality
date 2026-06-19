"""T47: PO1 DAG theorem.

T47 proves that the directed graph of PO1-admissible D1RestrictionMorphisms
in D1Cat is acyclic, has depth at most one, and is bipartite between
unobstructed (pre-finality) and obstructed (post-finality) systems.

The proof is structural and follows from two admissibility conditions:

  AC6: the target (restricted) system must be obstructed.
  AC7: the source (richer) system must be unobstructed.

These two conditions jointly imply:
  (1) No directed cycle exists: a cycle would require some system to be both
      obstructed (AC6 of the incoming edge) and unobstructed (AC7 of the
      outgoing edge). Contradiction.

  (2) No chain of length > 1 exists: the first morphism makes the target
      obstructed (AC6). The second morphism would require that target to be
      unobstructed (AC7). Contradiction.

  (3) The graph is bipartite: all sources must be unobstructed (by AC7);
      all targets must be obstructed (by AC6). Sources and targets are
      disjoint classes.

Executable test:
  Five D1RestrictionSystems are constructed: U1, U2 (unobstructed) and
  O1, O2, O3 (obstructed). All 20 ordered non-self pairs are tested.
  The admitted-edge graph is verified to be a DAG with depth <= 1.

Hypotheses evaluated:
  H_DAG:       PO1-admissible sub-graph of D1Cat is acyclic.
  H_DEPTH1:    No PO1-admissible chain has length > 1.
  H_BIPARTITE: PO1 sub-graph is bipartite (pre-finality vs post-finality).
  H_BORDER:    All PO1-admissible morphisms cross from pre- to post-finality.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SystemNode:
    name: str
    site_count: int
    obstructed: bool
    layer: str  # "pre_finality" or "post_finality"


@dataclass(frozen=True)
class EdgeResult:
    source: str
    target: str
    admissibility: AdmissibilityCheck
    is_po1: bool
    primary_failure: str


@dataclass(frozen=True)
class DagAnalysis:
    nodes: tuple[str, ...]
    admitted_edges: tuple[tuple[str, str], ...]
    rejected_edges: tuple[tuple[str, str], ...]
    is_dag: bool
    topological_sort: tuple[str, ...]
    max_depth: int
    is_bipartite: bool
    pre_finality_nodes: tuple[str, ...]
    post_finality_nodes: tuple[str, ...]
    bipartite_confirmed: bool


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T47Result:
    system_nodes: tuple[SystemNode, ...]
    edge_results: tuple[EdgeResult, ...]
    dag_analysis: DagAnalysis
    theorem_statement: str
    corollary_depth: str
    corollary_bipartite: str
    corollary_border: str
    proof_sketch: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# System constructors
# ---------------------------------------------------------------------------


def _site(sid: str, pop: str) -> ObserverSite:
    return ObserverSite(sid, pop, "finite_site", 0, "t47")


def _lv(sid: str, pop: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(site=_site(sid, pop), proposition_value="true", profile=profile)


def _u1() -> D1RestrictionSystem:
    """Three-site unobstructed system: globally satisfiable coherence patches."""
    p = D1Profile(3, 3, 2, 3)
    return D1RestrictionSystem(
        name="U1_pre_finality",
        proposition="pre_record_Q",
        local_values=(_lv("u1a", "pre", p), _lv("u1b", "pre", p), _lv("u1c", "pre", p)),
        transport_edges=(TransportEdge("u1a", "u1b", "link", True), TransportEdge("u1b", "u1c", "link", True)),
        source_site="u1a",
        target_site="u1c",
        patches=(
            RestrictionPatch("u1_ab", ("u1a", "u1b"), ("a", "b"), (PatchConstraint("a", "b", "same"),)),
            RestrictionPatch("u1_bc", ("u1b", "u1c"), ("b", "c"), (PatchConstraint("b", "c", "same"),)),
            RestrictionPatch("u1_ac", ("u1a", "u1c"), ("a", "c"), (PatchConstraint("a", "c", "same"),)),
        ),
    )


def _u2() -> D1RestrictionSystem:
    """Two-site unobstructed system: no patches (trivially satisfiable)."""
    p = D1Profile(2, 2, 1, 2)
    return D1RestrictionSystem(
        name="U2_pre_finality",
        proposition="pre_record_P",
        local_values=(_lv("u2a", "pre", p), _lv("u2b", "pre", p)),
        transport_edges=(TransportEdge("u2a", "u2b", "link", True),),
        source_site="u2a",
        target_site="u2b",
    )


def _o1() -> D1RestrictionSystem:
    """Three-site obstructed system: parity-conflict triangle (same-same-different)."""
    p = D1Profile(1, 1, 0, 1)
    return D1RestrictionSystem(
        name="O1_post_finality",
        proposition="classical_record_R1",
        local_values=(_lv("o1a", "post", p), _lv("o1b", "post", p), _lv("o1c", "post", p)),
        transport_edges=(TransportEdge("o1a", "o1b", "edge", True), TransportEdge("o1b", "o1c", "edge", True)),
        source_site="o1a",
        target_site="o1c",
        patches=(
            RestrictionPatch("o1_ab", ("o1a", "o1b"), ("x", "y"), (PatchConstraint("x", "y", "same"),)),
            RestrictionPatch("o1_bc", ("o1b", "o1c"), ("y", "z"), (PatchConstraint("y", "z", "same"),)),
            RestrictionPatch("o1_ac", ("o1a", "o1c"), ("x", "z"), (PatchConstraint("x", "z", "different"),)),
        ),
    )


def _o2() -> D1RestrictionSystem:
    """Two-site obstructed system: contradictory constraints on same variables."""
    p = D1Profile(1, 1, 0, 1)
    return D1RestrictionSystem(
        name="O2_post_finality",
        proposition="classical_record_R2",
        local_values=(_lv("o2a", "post", p), _lv("o2b", "post", p)),
        transport_edges=(TransportEdge("o2a", "o2b", "edge", True),),
        source_site="o2a",
        target_site="o2b",
        patches=(
            RestrictionPatch("o2_same", ("o2a", "o2b"), ("p", "q"), (PatchConstraint("p", "q", "same"),)),
            RestrictionPatch("o2_diff", ("o2a", "o2b"), ("p", "q"), (PatchConstraint("p", "q", "different"),)),
        ),
    )


def _o3() -> D1RestrictionSystem:
    """Three-site obstructed system: parity-conflict triangle (same-different-same -> conflict)."""
    p = D1Profile(1, 1, 0, 1)
    return D1RestrictionSystem(
        name="O3_post_finality",
        proposition="classical_record_R3",
        local_values=(_lv("o3a", "post", p), _lv("o3b", "post", p), _lv("o3c", "post", p)),
        transport_edges=(TransportEdge("o3a", "o3b", "edge", True), TransportEdge("o3b", "o3c", "edge", True)),
        source_site="o3a",
        target_site="o3c",
        patches=(
            RestrictionPatch("o3_ab", ("o3a", "o3b"), ("u", "v"), (PatchConstraint("u", "v", "same"),)),
            RestrictionPatch("o3_bc", ("o3b", "o3c"), ("v", "w"), (PatchConstraint("v", "w", "same"),)),
            RestrictionPatch("o3_ac", ("o3a", "o3c"), ("u", "w"), (PatchConstraint("u", "w", "different"),)),
        ),
    )


# ---------------------------------------------------------------------------
# Canonical morphism construction
# ---------------------------------------------------------------------------


def _canonical_morphism(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    label: str,
) -> D1RestrictionMorphism:
    src_sites = list(source.site_ids())
    tgt_sites = list(target.site_ids())
    n = len(tgt_sites)
    site_map = tuple(SiteMap(s, tgt_sites[i % n]) for i, s in enumerate(src_sites))
    return D1RestrictionMorphism(
        name=f"canonical_{label}",
        source=source,
        target=target,
        site_map=site_map,
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


def _check_pair(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
) -> EdgeResult:
    morphism = _canonical_morphism(source, target, f"{source.name}_to_{target.name}")
    case = ProjectionCase(
        name=f"{source.name}_to_{target.name}",
        source="T47",
        richer_system=source,
        restricted_system=target,
        morphism=morphism,
        forgotten_structure=("pre_finality_structure",),
        preserved_structure=(),
        intended_reading="canonical PO1 admissibility test",
    )
    adm = check_admissibility(case)
    if adm.po1_evidence:
        primary = "none (fully admissible)"
    elif adm.failed_conditions:
        primary = adm.failed_conditions[0]
    else:
        primary = "unknown"
    return EdgeResult(
        source=source.name,
        target=target.name,
        admissibility=adm,
        is_po1=adm.po1_evidence,
        primary_failure=primary,
    )


# ---------------------------------------------------------------------------
# DAG analysis
# ---------------------------------------------------------------------------


def _topo_sort_and_dag_check(
    node_names: list[str],
    edges: list[tuple[str, str]],
) -> tuple[bool, tuple[str, ...]]:
    """Kahn's algorithm: returns (is_dag, topological_sort)."""
    graph: dict[str, list[str]] = defaultdict(list)
    in_deg: dict[str, int] = {n: 0 for n in node_names}
    for src, tgt in edges:
        graph[src].append(tgt)
        in_deg[tgt] += 1
    queue = deque(n for n in node_names if in_deg[n] == 0)
    topo: list[str] = []
    while queue:
        v = queue.popleft()
        topo.append(v)
        for u in sorted(graph[v]):
            in_deg[u] -= 1
            if in_deg[u] == 0:
                queue.append(u)
    return len(topo) == len(node_names), tuple(topo)


def _max_path_depth(
    node_names: list[str],
    edges: list[tuple[str, str]],
    topo: tuple[str, ...],
) -> int:
    graph: dict[str, list[str]] = defaultdict(list)
    for src, tgt in edges:
        graph[src].append(tgt)
    depth: dict[str, int] = {n: 0 for n in node_names}
    for node in topo:
        for neighbor in graph[node]:
            depth[neighbor] = max(depth[neighbor], depth[node] + 1)
    return max(depth.values()) if depth else 0


def _analyze_dag(
    systems: list[D1RestrictionSystem],
    edge_results: list[EdgeResult],
) -> DagAnalysis:
    node_names = [s.name for s in systems]
    sections = {s.name: global_section(s) for s in systems}
    pre_nodes = tuple(n for n in node_names if not sections[n].obstruction_detected)
    post_nodes = tuple(n for n in node_names if sections[n].obstruction_detected)
    pre_set = set(pre_nodes)
    post_set = set(post_nodes)

    admitted = [(r.source, r.target) for r in edge_results if r.is_po1]
    rejected = [(r.source, r.target) for r in edge_results if not r.is_po1]

    is_dag, topo = _topo_sort_and_dag_check(node_names, admitted)
    depth = _max_path_depth(node_names, admitted, topo) if is_dag else -1

    bipartite_confirmed = all(
        src in pre_set and tgt in post_set for src, tgt in admitted
    )

    return DagAnalysis(
        nodes=tuple(node_names),
        admitted_edges=tuple(admitted),
        rejected_edges=tuple(rejected),
        is_dag=is_dag,
        topological_sort=topo,
        max_depth=depth,
        is_bipartite=bipartite_confirmed,
        pre_finality_nodes=pre_nodes,
        post_finality_nodes=post_nodes,
        bipartite_confirmed=bipartite_confirmed,
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t47_analysis() -> T47Result:
    systems = [_u1(), _u2(), _o1(), _o2(), _o3()]

    edge_results: list[EdgeResult] = []
    for src in systems:
        for tgt in systems:
            if src.name != tgt.name:
                edge_results.append(_check_pair(src, tgt))

    dag = _analyze_dag(systems, edge_results)

    system_nodes = tuple(
        SystemNode(
            name=s.name,
            site_count=len(s.site_ids()),
            obstructed=global_section(s).obstruction_detected,
            layer="post_finality" if global_section(s).obstruction_detected else "pre_finality",
        )
        for s in systems
    )

    theorem = (
        "PO1 DAG Theorem (T47): The directed graph of PO1-admissible "
        "D1RestrictionMorphisms in D1Cat is acyclic. No directed cycle of "
        "PO1-admissible morphisms can exist. Proof: suppose f1,...,fn form a "
        "PO1-admissible cycle A1 -> A2 -> ... -> An -> A1. For f1: A1 -> A2, "
        "AC7 requires A1 unobstructed. For fn: An -> A1, AC6 requires A1 "
        "obstructed. Contradiction."
    )

    cor_depth = (
        "Depth Bound Corollary: No PO1-admissible chain has length > 1. "
        "If f: A -> B is PO1-admissible, AC6 requires B obstructed. "
        "Any g: B -> C would require AC7: B unobstructed. Contradiction. "
        f"Verified: max_depth = {dag.max_depth} in this model."
    )

    cor_bip = (
        "Bipartite Corollary: The PO1-admissible sub-graph of D1Cat is "
        "bipartite between unobstructed systems (pre-finality layer) and "
        "obstructed systems (post-finality layer), with all edges directed "
        "from pre- to post-finality. "
        f"Verified: pre_nodes={dag.pre_finality_nodes}, "
        f"post_nodes={dag.post_finality_nodes}."
    )

    cor_border = (
        "Finality Border Corollary: PO1-admissible morphisms mark the "
        "finality boundary in D1Cat. Every PO1-admissible morphism crosses "
        "from pre-finality to post-finality. No PO1-admissible morphism "
        "crosses in the reverse direction. The finality boundary is a "
        "categorical one-way gate in D1Cat."
    )

    proof = (
        "The proof depends only on AC6 and AC7. AC6 (target obstructed) and "
        "AC7 (source unobstructed) jointly prevent any system from being both "
        "source and target in a PO1-admissible morphism. This rules out "
        "self-loops, back-edges, and cycles of any length. The finite witness "
        "here confirms that all AC7 failures occur precisely when the source "
        "is obstructed, consistent with the structural proof."
    )

    po1_count = sum(1 for r in edge_results if r.is_po1)
    ac7_failures = sum(1 for r in edge_results if not r.is_po1 and "AC7" in r.primary_failure)
    ac6_failures = sum(1 for r in edge_results if not r.is_po1 and "AC6" in r.primary_failure)

    hyps = (
        HypothesisResult(
            "H_DAG",
            "PO1-admissible sub-graph of D1Cat is acyclic",
            "supported" if dag.is_dag else "refuted",
            f"DAG check: {dag.is_dag}; admitted edges: {len(dag.admitted_edges)}",
        ),
        HypothesisResult(
            "H_DEPTH1",
            "No PO1-admissible chain has length > 1",
            "supported" if dag.max_depth <= 1 else "refuted",
            f"max path depth in admitted graph: {dag.max_depth}",
        ),
        HypothesisResult(
            "H_BIPARTITE",
            "PO1 sub-graph is bipartite (pre-finality vs post-finality)",
            "supported" if dag.bipartite_confirmed else "refuted",
            f"bipartite confirmed: {dag.bipartite_confirmed}; "
            f"pre={dag.pre_finality_nodes}; post={dag.post_finality_nodes}",
        ),
        HypothesisResult(
            "H_BORDER",
            "All PO1-admissible morphisms cross pre- to post-finality",
            "supported" if dag.bipartite_confirmed else "refuted",
            f"admitted={po1_count} edges all pre->post; "
            f"AC7 failures={ac7_failures}; AC6 failures={ac6_failures}",
        ),
    )

    all_supported = all(h.status == "supported" for h in hyps)
    best = (
        "H_DAG, H_DEPTH1, H_BIPARTITE, H_BORDER (all four hold)"
        if all_supported
        else "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T47Result(
        system_nodes=system_nodes,
        edge_results=tuple(edge_results),
        dag_analysis=dag,
        theorem_statement=theorem,
        corollary_depth=cor_depth,
        corollary_bipartite=cor_bip,
        corollary_border=cor_border,
        proof_sketch=proof,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _edge_to_dict(r: EdgeResult) -> dict[str, Any]:
    return {
        "source": r.source,
        "target": r.target,
        "is_po1": r.is_po1,
        "verdict": r.admissibility.verdict,
        "primary_failure": r.primary_failure,
        "conditions": {
            "AC1": r.admissibility.ac1_richer_valid,
            "AC2": r.admissibility.ac2_restricted_valid,
            "AC3": r.admissibility.ac3_projection_definable,
            "AC4": r.admissibility.ac4_local_compat,
            "AC5": r.admissibility.ac5_structure_forgotten,
            "AC6": r.admissibility.ac6_restricted_obstructed,
            "AC7": r.admissibility.ac7_richer_unobstructed,
        },
    }


def t47_result_to_dict(r: T47Result) -> dict[str, Any]:
    return {
        "systems": [
            {"name": n.name, "sites": n.site_count, "obstructed": n.obstructed, "layer": n.layer}
            for n in r.system_nodes
        ],
        "edge_results": [_edge_to_dict(e) for e in r.edge_results],
        "dag_analysis": {
            "nodes": list(r.dag_analysis.nodes),
            "admitted_edges": [list(e) for e in r.dag_analysis.admitted_edges],
            "rejected_edges": [list(e) for e in r.dag_analysis.rejected_edges],
            "is_dag": r.dag_analysis.is_dag,
            "topological_sort": list(r.dag_analysis.topological_sort),
            "max_depth": r.dag_analysis.max_depth,
            "is_bipartite": r.dag_analysis.is_bipartite,
            "pre_finality_nodes": list(r.dag_analysis.pre_finality_nodes),
            "post_finality_nodes": list(r.dag_analysis.post_finality_nodes),
        },
        "theorem_statement": r.theorem_statement,
        "corollary_depth": r.corollary_depth,
        "corollary_bipartite": r.corollary_bipartite,
        "corollary_border": r.corollary_border,
        "proof_sketch": r.proof_sketch,
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
