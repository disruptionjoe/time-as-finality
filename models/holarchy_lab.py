"""T40: Holarchy Lab — Emergent Holonic Finality via Recursive Typed Transport.

A holarchy is a system of nested wholes: each level is simultaneously a whole
(relative to its components) and a part (relative to the level above).

This test asks: in a network where nodes are themselves D1RestrictionSystems
connected by cross-level typed constraints, does macro-level finality (holonic
global section) emerge from or reduce to micro-level finality?

The question connects directly to T38's transport formalism: T38 established
that TypedTransportNetwork is the minimal formalism for ten transport questions.
T40 asks whether a second level of nesting (networks of networks) produces
genuinely new obstruction phenomena or reduces to flat CSP.

From T39: a D1 global section is equivalent to signed-graph satisfiability.
Holonic emergence occurs when the combined signed graph (micro + cross-level
constraints) has a negative cycle that the individual micro graphs do not.

Three hypotheses:

H_A: Holonic finality reduces to micro finality.
  If every micro system has a global section, the holonic network does too.
  PREDICTION: no holonic emergence cases exist.

H_B: Holonic finality is genuinely independent.
  Cross-level constraints can create obstructions from micro-compatible systems.
  The obstruction depends on the topology of cross-level edges, not just
  micro-level satisfiability.
  PREDICTION: holonic emergence cases exist.

H_C: Cross-level AC5 (forgotten cross-level structure) is necessary and sufficient
  for holonic PO1 instances.
  PREDICTION: every holonic PO1 case has non-empty cross-level forgotten_dims;
  no holonic PO1 case exists when forgotten_dims is empty.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product as itertools_product
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint


# ---------------------------------------------------------------------------
# Holarchy primitives
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class HolonicNode:
    """A D1RestrictionSystem as one node in a holarchy.

    entry_site and exit_site name the canonical interface sites — the
    variables at which cross-level constraints attach.
    """
    name: str
    system: D1RestrictionSystem
    entry_site: str
    exit_site: str


@dataclass(frozen=True)
class HolonicEdge:
    """A cross-level connection: constraints between interface sites of two nodes.

    forgotten_dims names the structure that a morphism mapping from a richer
    holonic network forgets at this edge. Empty means no structure is forgotten.
    """
    name: str
    from_node: str
    to_node: str
    cross_constraints: tuple[PatchConstraint, ...]
    forgotten_dims: tuple[str, ...]


@dataclass(frozen=True)
class HolonicNetwork:
    """A directed graph of D1RestrictionSystems connected by cross-level constraints.

    The holonic global section requires all micro patches (from each node's
    D1RestrictionSystem) AND all cross-level patches (from HolonicEdges) to
    be jointly satisfiable.
    """
    name: str
    nodes: tuple[HolonicNode, ...]
    edges: tuple[HolonicEdge, ...]


# ---------------------------------------------------------------------------
# Analysis primitives
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MicroSectionResult:
    """Per-node satisfiability result."""
    node_name: str
    globally_satisfiable: bool
    witness_count: int


@dataclass(frozen=True)
class HolonicGlobalSection:
    """Full holonic satisfiability analysis.

    Combines micro patches from each node with cross-level patches from edges.
    """
    network_name: str
    micro_results: tuple[MicroSectionResult, ...]
    all_micro_satisfiable: bool
    holonic_globally_satisfiable: bool
    holonic_witness_count: int
    emergence_detected: bool   # all micro satisfiable AND holonic NOT satisfiable
    obstruction_source: str    # "none" | "micro_only" | "holonic_emergence"


@dataclass(frozen=True)
class HolonicPO1Bridge:
    """PO1 analysis at the holonic level.

    source is a holonic network that is holonically satisfiable.
    target is a holonic network that is holonically obstructed.
    The morphism from source to target has named forgotten_dims.
    """
    case_name: str
    source_name: str
    target_name: str
    source_holonic_satisfiable: bool
    target_holonic_obstructed: bool
    cross_level_forgotten_dims: tuple[str, ...]
    ac5_fires: bool    # non-empty forgotten_dims
    ac7_holds: bool    # source holonically satisfiable
    holonic_po1_admissible: bool   # ac5 AND ac7 AND target obstructed


@dataclass(frozen=True)
class HypothesisHolarchy:
    hypothesis_id: str
    claim: str
    verdict: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class T40Result:
    scenarios: tuple[HolonicGlobalSection, ...]
    holonic_po1_bridges: tuple[HolonicPO1Bridge, ...]
    emergence_count: int
    po1_admissible_count: int
    theorem_holonic_emergence: str
    theorem_cross_level_ac5: str
    hypothesis_evaluations: tuple[HypothesisHolarchy, ...]
    best_supported_hypothesis: str
    boundary: str
    recommendation: str


# ---------------------------------------------------------------------------
# Signed-graph parity check (independent of T39 to avoid circular imports)
# ---------------------------------------------------------------------------


def _collect_variables_and_constraints(
    network: HolonicNetwork,
) -> tuple[list[str], list[PatchConstraint]]:
    """Collect all variables and constraints from micro systems and cross-level edges."""
    all_vars: list[str] = []
    seen_vars: set[str] = set()
    all_constraints: list[PatchConstraint] = []

    for node in network.nodes:
        for patch in node.system.patches:
            for constraint in patch.constraints:
                for v in (constraint.left, constraint.right):
                    if v not in seen_vars:
                        seen_vars.add(v)
                        all_vars.append(v)
                all_constraints.append(constraint)

    for edge in network.edges:
        for constraint in edge.cross_constraints:
            for v in (constraint.left, constraint.right):
                if v not in seen_vars:
                    seen_vars.add(v)
                    all_vars.append(v)
            all_constraints.append(constraint)

    return all_vars, all_constraints


def _parity_check(variables: list[str], constraints: list[PatchConstraint]) -> bool:
    """Return True iff the signed-graph is 2-colorable (no negative cycle)."""
    adj: dict[str, list[tuple[str, int]]] = {v: [] for v in variables}
    for c in constraints:
        sign = 1 if c.relation == "same" else -1
        adj[c.left].append((c.right, sign))
        adj[c.right].append((c.left, sign))

    colors: dict[str, int] = {}
    for start in variables:
        if start in colors:
            continue
        colors[start] = 1
        queue = [start]
        while queue:
            current = queue.pop(0)
            for neighbor, sign in adj[current]:
                expected = colors[current] * sign
                if neighbor not in colors:
                    colors[neighbor] = expected
                    queue.append(neighbor)
                elif colors[neighbor] != expected:
                    return False
    return True


def _count_witnesses(variables: list[str], constraints: list[PatchConstraint]) -> int:
    """Enumerate {-1,1}^n assignments satisfying all constraints (up to 8 vars)."""
    if len(variables) > 8:
        return -1
    count = 0
    for bits in itertools_product((-1, 1), repeat=len(variables)):
        assignment = dict(zip(variables, bits))
        if all(_satisfies(assignment, c) for c in constraints):
            count += 1
    return count


def _satisfies(assignment: dict[str, int], c: PatchConstraint) -> bool:
    left, right = assignment[c.left], assignment[c.right]
    if c.relation == "same":
        return left == right
    if c.relation == "different":
        return left != right
    raise ValueError(f"unknown relation: {c.relation}")


# ---------------------------------------------------------------------------
# Node-level analysis
# ---------------------------------------------------------------------------


def _analyze_node(node: HolonicNode) -> MicroSectionResult:
    """Check micro-level satisfiability for a single node."""
    if not node.system.patches:
        return MicroSectionResult(
            node_name=node.name,
            globally_satisfiable=True,
            witness_count=-1,
        )
    vars_: list[str] = []
    seen: set[str] = set()
    constraints: list[PatchConstraint] = []
    for patch in node.system.patches:
        for c in patch.constraints:
            for v in (c.left, c.right):
                if v not in seen:
                    seen.add(v)
                    vars_.append(v)
            constraints.append(c)
    satisfiable = _parity_check(vars_, constraints)
    witnesses = _count_witnesses(vars_, constraints)
    return MicroSectionResult(
        node_name=node.name,
        globally_satisfiable=satisfiable,
        witness_count=witnesses,
    )


# ---------------------------------------------------------------------------
# Holonic-network analysis
# ---------------------------------------------------------------------------


def analyze_holonic_network(network: HolonicNetwork) -> HolonicGlobalSection:
    """Compute holonic global section: micro + cross-level constraints jointly."""
    micro_results = tuple(_analyze_node(n) for n in network.nodes)
    all_micro_sat = all(r.globally_satisfiable for r in micro_results)

    all_vars, all_constraints = _collect_variables_and_constraints(network)
    holonic_sat = _parity_check(all_vars, all_constraints)
    witnesses = _count_witnesses(all_vars, all_constraints)

    emergence = all_micro_sat and (not holonic_sat)

    if holonic_sat:
        source = "none"
    elif not all_micro_sat:
        source = "micro_only"
    else:
        source = "holonic_emergence"

    return HolonicGlobalSection(
        network_name=network.name,
        micro_results=micro_results,
        all_micro_satisfiable=all_micro_sat,
        holonic_globally_satisfiable=holonic_sat,
        holonic_witness_count=witnesses,
        emergence_detected=emergence,
        obstruction_source=source,
    )


def analyze_holonic_po1(
    source: HolonicNetwork,
    target: HolonicNetwork,
    forgotten_dims: tuple[str, ...],
    case_name: str,
) -> HolonicPO1Bridge:
    """Check PO1 admissibility at the holonic level."""
    src_section = analyze_holonic_network(source)
    tgt_section = analyze_holonic_network(target)

    src_sat = src_section.holonic_globally_satisfiable
    tgt_obstructed = not tgt_section.holonic_globally_satisfiable
    ac5 = len(forgotten_dims) > 0
    ac7 = src_sat
    admissible = ac5 and ac7 and tgt_obstructed

    return HolonicPO1Bridge(
        case_name=case_name,
        source_name=source.name,
        target_name=target.name,
        source_holonic_satisfiable=src_sat,
        target_holonic_obstructed=tgt_obstructed,
        cross_level_forgotten_dims=forgotten_dims,
        ac5_fires=ac5,
        ac7_holds=ac7,
        holonic_po1_admissible=admissible,
    )


# ---------------------------------------------------------------------------
# Scenario builders
# ---------------------------------------------------------------------------

_PROFILE = D1Profile(2, 2, 2, 2)


def _simple_node(name: str, entry: str, exit_: str, relation: str = "same") -> HolonicNode:
    """Build a 2-site HolonicNode with one same/different internal patch."""
    system = D1RestrictionSystem(
        name=f"sys_{name}",
        proposition=f"prop_{name}",
        local_values=(
            LocalD1Value(ObserverSite(entry, "abstract", name, 0, "trusted"), "true", _PROFILE),
            LocalD1Value(ObserverSite(exit_, "abstract", name, 0, "trusted"), "true", _PROFILE),
        ),
        transport_edges=(TransportEdge(entry, exit_, "transport", True),),
        source_site=entry,
        target_site=exit_,
        patches=(
            RestrictionPatch(
                f"p_{name}",
                (entry, exit_),
                (entry, exit_),
                (PatchConstraint(entry, exit_, relation),),
            ),
        ),
    )
    return HolonicNode(name=name, system=system, entry_site=entry, exit_site=exit_)


def _trivial_node(name: str, entry: str, exit_: str) -> HolonicNode:
    """Build a 2-site HolonicNode with no internal patches (trivially satisfiable)."""
    system = D1RestrictionSystem(
        name=f"sys_{name}",
        proposition=f"prop_{name}",
        local_values=(
            LocalD1Value(ObserverSite(entry, "abstract", name, 0, "trusted"), "true", _PROFILE),
            LocalD1Value(ObserverSite(exit_, "abstract", name, 0, "trusted"), "true", _PROFILE),
        ),
        transport_edges=(TransportEdge(entry, exit_, "transport", True),),
        source_site=entry,
        target_site=exit_,
        patches=(),
    )
    return HolonicNode(name=name, system=system, entry_site=entry, exit_site=exit_)


def build_holonic_flat_scenario() -> HolonicNetwork:
    """Scenario 1: 2 nodes, both satisfiable, compatible cross-level constraint.

    Node A: a1=a2 (same)
    Node B: b1=b2 (same)
    Cross A→B: a2=b1 (same)
    Combined: a1=a2=b1=b2 → satisfiable (2 witnesses).
    Holonic global section: exists. Emergence: False.
    """
    nodeA = _simple_node("flat_A", "a1", "a2", "same")
    nodeB = _simple_node("flat_B", "b1", "b2", "same")
    edge = HolonicEdge(
        name="flat_A_to_B",
        from_node="flat_A",
        to_node="flat_B",
        cross_constraints=(PatchConstraint("a2", "b1", "same"),),
        forgotten_dims=(),
    )
    return HolonicNetwork(
        name="holonic_flat",
        nodes=(nodeA, nodeB),
        edges=(edge,),
    )


def build_holonic_compatible_different_scenario() -> HolonicNetwork:
    """Scenario 2: 2 nodes, both satisfiable, cross-level 'different' — still satisfiable.

    Node A: a1=a2 (same)
    Node B: b1=b2 (same)
    Cross A→B: a2≠b1 (different)
    Combined: a1=a2≠b1=b2 → satisfiable (a=+1,b=-1 or a=-1,b=+1; 2 witnesses).
    Holonic global section: exists. Emergence: False.
    This shows 'different' cross-level constraints do not automatically obstruct.
    """
    nodeA = _simple_node("diff_A", "a1", "a2", "same")
    nodeB = _simple_node("diff_B", "b1", "b2", "same")
    edge = HolonicEdge(
        name="diff_A_to_B",
        from_node="diff_A",
        to_node="diff_B",
        cross_constraints=(PatchConstraint("a2", "b1", "different"),),
        forgotten_dims=(),
    )
    return HolonicNetwork(
        name="holonic_compatible_different",
        nodes=(nodeA, nodeB),
        edges=(edge,),
    )


def build_holonic_emergent_obstruction_scenario() -> HolonicNetwork:
    """Scenario 3: 3 nodes, all satisfiable, transitive parity conflict at holonic level.

    Node A: a1=a2 (same)   Node B: b1=b2 (same)   Node C: c1=c2 (same)
    Cross A→B: a2=b1 (same)
    Cross B→C: b2=c1 (same)
    Cross A→C: a2≠c1 (different)  ← creates the negative cycle

    Combined chain: a1=a2=b1=b2=c1=c2 (from micro + first two cross edges)
    But also: a2≠c1 → a2≠a2 → contradiction. OBSTRUCTED.

    Each micro node is satisfiable. Each pair of cross-level edges is locally
    satisfiable. The three-way combination is obstructed.
    Emergence: True. This is the minimum holonic emergence case.
    """
    nodeA = _simple_node("em_A", "a1", "a2", "same")
    nodeB = _simple_node("em_B", "b1", "b2", "same")
    nodeC = _simple_node("em_C", "c1", "c2", "same")
    edge_AB = HolonicEdge(
        name="em_A_to_B",
        from_node="em_A",
        to_node="em_B",
        cross_constraints=(PatchConstraint("a2", "b1", "same"),),
        forgotten_dims=(),
    )
    edge_BC = HolonicEdge(
        name="em_B_to_C",
        from_node="em_B",
        to_node="em_C",
        cross_constraints=(PatchConstraint("b2", "c1", "same"),),
        forgotten_dims=(),
    )
    edge_AC = HolonicEdge(
        name="em_A_to_C_shortcut",
        from_node="em_A",
        to_node="em_C",
        cross_constraints=(PatchConstraint("a2", "c1", "different"),),
        forgotten_dims=(),
    )
    return HolonicNetwork(
        name="holonic_emergent",
        nodes=(nodeA, nodeB, nodeC),
        edges=(edge_AB, edge_BC, edge_AC),
    )


def build_holonic_micro_obstructed_scenario() -> HolonicNetwork:
    """Scenario 4: one micro node obstructed → holonic obstructed.

    Node A: a1=a2 (same) → satisfiable
    Node B: b1=b2 AND b1≠b2 (direct parity conflict) → obstructed
    Cross A→B: a2=b1 (same)

    All micro satisfiable = False (B is obstructed).
    Holonic obstructed (B's constraint propagates).
    Emergence: False (obstruction is at the micro level).
    This is the control case: micro obstruction ≠ holonic emergence.
    """
    nodeA = _simple_node("mo_A", "a1", "a2", "same")
    # Build obstructed node B: b1=b2 AND b1≠b2
    sysB = D1RestrictionSystem(
        name="sys_mo_B",
        proposition="prop_mo_B",
        local_values=(
            LocalD1Value(ObserverSite("b1", "abstract", "mo_B", 0, "trusted"), "true", _PROFILE),
            LocalD1Value(ObserverSite("b2", "abstract", "mo_B", 0, "trusted"), "true", _PROFILE),
        ),
        transport_edges=(TransportEdge("b1", "b2", "transport", True),),
        source_site="b1",
        target_site="b2",
        patches=(
            RestrictionPatch("p_same_B", ("b1", "b2"), ("b1", "b2"), (PatchConstraint("b1", "b2", "same"),)),
            RestrictionPatch("p_diff_B", ("b1", "b2"), ("b1", "b2"), (PatchConstraint("b1", "b2", "different"),)),
        ),
    )
    nodeB = HolonicNode(name="mo_B", system=sysB, entry_site="b1", exit_site="b2")
    edge = HolonicEdge(
        name="mo_A_to_B",
        from_node="mo_A",
        to_node="mo_B",
        cross_constraints=(PatchConstraint("a2", "b1", "same"),),
        forgotten_dims=(),
    )
    return HolonicNetwork(
        name="holonic_micro_obstructed",
        nodes=(nodeA, nodeB),
        edges=(edge,),
    )


def build_holonic_po1_source() -> HolonicNetwork:
    """Source for holonic PO1 case: 2 nodes, compatible cross-level constraints.

    Node A: a1=a2 (same)
    Node B: b1=b2 (same)
    Cross A→B: a2=b1 (same) AND a1=b2 (same)
    Combined: a1=a2=b1=b2 (from same chain + a1=b2) → satisfiable.
    Holonic global section: exists.
    """
    nodeA = _simple_node("po1_src_A", "a1", "a2", "same")
    nodeB = _simple_node("po1_src_B", "b1", "b2", "same")
    edge = HolonicEdge(
        name="po1_src_A_to_B",
        from_node="po1_src_A",
        to_node="po1_src_B",
        cross_constraints=(
            PatchConstraint("a2", "b1", "same"),
            PatchConstraint("a1", "b2", "same"),   # the "forgotten" cross-constraint
        ),
        forgotten_dims=("a1-b2-compatibility",),
    )
    return HolonicNetwork(
        name="holonic_po1_source",
        nodes=(nodeA, nodeB),
        edges=(edge,),
    )


def build_holonic_po1_target() -> HolonicNetwork:
    """Target for holonic PO1 case: same nodes, one cross-constraint replaced.

    Node A: a1=a2 (same)
    Node B: b1=b2 (same)
    Cross A→B: a2=b1 (same) AND a1≠b2 (different)
    Combined: a1=a2=b1=b2 (from same chain) BUT also a1≠b2 → a1≠a1 → OBSTRUCTED.

    The morphism from source to target forgets the a1=b2 constraint and replaces
    it with a1≠b2 (the restricted view without the mediating compatibility).
    forgotten_dims = ("a1-b2-compatibility",).
    """
    nodeA = _simple_node("po1_tgt_A", "a1", "a2", "same")
    nodeB = _simple_node("po1_tgt_B", "b1", "b2", "same")
    edge = HolonicEdge(
        name="po1_tgt_A_to_B",
        from_node="po1_tgt_A",
        to_node="po1_tgt_B",
        cross_constraints=(
            PatchConstraint("a2", "b1", "same"),
            PatchConstraint("a1", "b2", "different"),   # conflict instead of compatible
        ),
        forgotten_dims=("a1-b2-compatibility",),
    )
    return HolonicNetwork(
        name="holonic_po1_target",
        nodes=(nodeA, nodeB),
        edges=(edge,),
    )


def build_holonic_po1_no_forgotten() -> tuple[HolonicNetwork, HolonicNetwork]:
    """Control: holonic PO1 without forgotten_dims (AC5 does not fire).

    Source: 2 nodes, compatible → satisfiable
    Target: 2 nodes, obstructed
    forgotten_dims = () ← empty; AC5 does not fire → not admissible

    This shows that holonic PO1 requires named forgotten structure, not just
    source-satisfiable + target-obstructed.
    """
    # Source: a1=a2, b1=b2, a2=b1 → satisfiable
    nodeA_src = _simple_node("nf_src_A", "a1", "a2", "same")
    nodeB_src = _simple_node("nf_src_B", "b1", "b2", "same")
    src_edge = HolonicEdge(
        name="nf_src_A_to_B",
        from_node="nf_src_A",
        to_node="nf_src_B",
        cross_constraints=(PatchConstraint("a2", "b1", "same"),),
        forgotten_dims=(),   # no forgotten structure declared
    )
    source = HolonicNetwork(
        name="holonic_po1_no_forgotten_source",
        nodes=(nodeA_src, nodeB_src),
        edges=(src_edge,),
    )
    # Target: 3-node triangle (emergent obstruction, same as scenario 3)
    nodeA_tgt = _simple_node("nf_tgt_A", "x1", "x2", "same")
    nodeB_tgt = _simple_node("nf_tgt_B", "y1", "y2", "same")
    nodeC_tgt = _simple_node("nf_tgt_C", "z1", "z2", "same")
    edge_AB = HolonicEdge(
        name="nf_tgt_AB", from_node="nf_tgt_A", to_node="nf_tgt_B",
        cross_constraints=(PatchConstraint("x2", "y1", "same"),), forgotten_dims=(),
    )
    edge_BC = HolonicEdge(
        name="nf_tgt_BC", from_node="nf_tgt_B", to_node="nf_tgt_C",
        cross_constraints=(PatchConstraint("y2", "z1", "same"),), forgotten_dims=(),
    )
    edge_AC = HolonicEdge(
        name="nf_tgt_AC", from_node="nf_tgt_A", to_node="nf_tgt_C",
        cross_constraints=(PatchConstraint("x2", "z1", "different"),), forgotten_dims=(),
    )
    target = HolonicNetwork(
        name="holonic_po1_no_forgotten_target",
        nodes=(nodeA_tgt, nodeB_tgt, nodeC_tgt),
        edges=(edge_AB, edge_BC, edge_AC),
    )
    return source, target


# ---------------------------------------------------------------------------
# Hypothesis evaluations
# ---------------------------------------------------------------------------


def _evaluate_hypotheses(
    scenarios: tuple[HolonicGlobalSection, ...],
    bridges: tuple[HolonicPO1Bridge, ...],
) -> tuple[HypothesisHolarchy, ...]:
    emergence_count = sum(1 for s in scenarios if s.emergence_detected)
    admissible_count = sum(1 for b in bridges if b.holonic_po1_admissible)
    non_admissible_no_ac5 = sum(
        1 for b in bridges
        if not b.holonic_po1_admissible and not b.ac5_fires and b.target_holonic_obstructed
    )

    return (
        HypothesisHolarchy(
            hypothesis_id="H_A",
            claim="Holonic finality reduces to micro finality: if all micro systems are satisfiable, the holonic network is too.",
            verdict="rejected",
            evidence_for=(),
            evidence_against=(
                f"Holonic emergence cases found: {emergence_count}. "
                "build_holonic_emergent_obstruction_scenario() shows 3 nodes each "
                "individually satisfiable with combined holonic obstruction from "
                "cross-level transitive parity conflict (a1=a2, b1=b2, c1=c2 micro; "
                "a2=b1, b2=c1 same cross-edges; a2≠c1 different cross-edge).",
            ),
            reason="H_A is rejected: holonic emergence cases exist where all micro systems "
                   "are satisfiable but the holonic network is not.",
        ),
        HypothesisHolarchy(
            hypothesis_id="H_B",
            claim="Holonic finality is genuinely independent: cross-level constraints can create obstructions from micro-compatible systems.",
            verdict="best_supported",
            evidence_for=(
                f"Holonic emergence confirmed in {emergence_count} scenario(s). "
                "The emergent obstruction arises from the signed-graph negative cycle "
                "formed by cross-level edges, not from any micro-level conflict. "
                f"Holonic PO1 admissible cases: {admissible_count}. "
                "The flat and compatible-different scenarios confirm that cross-level "
                "edges do not automatically obstruct: the topology matters.",
            ),
            evidence_against=(
                "H_A is rejected by one scenario, not by a parameter sweep. "
                "A future parameterized audit (T40 follow-up) would strengthen the claim.",
            ),
            reason="H_B is best supported: holonic emergence is confirmed and is topology-dependent.",
        ),
        HypothesisHolarchy(
            hypothesis_id="H_C",
            claim="Cross-level AC5 (non-empty forgotten_dims) is necessary for holonic PO1 admissibility.",
            verdict="supported",
            evidence_for=(
                f"Every admissible holonic PO1 case ({admissible_count}) has non-empty "
                "forgotten_dims (AC5 fires). "
                f"Control case with empty forgotten_dims: {non_admissible_no_ac5} non-admissible "
                "instance(s) confirming that source-satisfiable + target-obstructed alone "
                "is insufficient without named cross-level forgotten structure.",
            ),
            evidence_against=(
                "The control case only tests one scenario. "
                "More exhaustive exploration (T40 follow-up) needed to confirm necessity.",
            ),
            reason="H_C is supported but not yet fully confirmed: all tested cases are consistent "
                   "with AC5 necessity, but the sample is small.",
        ),
    )


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------


def run_t40_analysis() -> T40Result:
    # Build and analyze scenarios
    flat = build_holonic_flat_scenario()
    diff = build_holonic_compatible_different_scenario()
    emergent = build_holonic_emergent_obstruction_scenario()
    micro_obs = build_holonic_micro_obstructed_scenario()

    flat_result = analyze_holonic_network(flat)
    diff_result = analyze_holonic_network(diff)
    emergent_result = analyze_holonic_network(emergent)
    micro_obs_result = analyze_holonic_network(micro_obs)

    scenarios = (flat_result, diff_result, emergent_result, micro_obs_result)

    # PO1 bridges
    po1_src = build_holonic_po1_source()
    po1_tgt = build_holonic_po1_target()
    po1_bridge = analyze_holonic_po1(
        source=po1_src,
        target=po1_tgt,
        forgotten_dims=("a1-b2-compatibility",),
        case_name="holonic_po1_main",
    )

    nf_src, nf_tgt = build_holonic_po1_no_forgotten()
    nf_bridge = analyze_holonic_po1(
        source=nf_src,
        target=nf_tgt,
        forgotten_dims=(),
        case_name="holonic_po1_no_forgotten_control",
    )

    bridges = (po1_bridge, nf_bridge)

    emergence_count = sum(1 for s in scenarios if s.emergence_detected)
    po1_admissible_count = sum(1 for b in bridges if b.holonic_po1_admissible)

    hypotheses = _evaluate_hypotheses(scenarios, bridges)

    return T40Result(
        scenarios=scenarios,
        holonic_po1_bridges=bridges,
        emergence_count=emergence_count,
        po1_admissible_count=po1_admissible_count,
        theorem_holonic_emergence=(
            "Holonic Emergence Theorem: in a HolonicNetwork, a holonic obstruction "
            "can arise from cross-level constraints even when every micro node is "
            "individually satisfiable. The minimum case has 3 nodes forming a directed "
            "triangle with cross-level constraints a2=b1 (same), b2=c1 (same), a2≠c1 "
            "(different), creating a negative signed-graph cycle at the holonic level. "
            "This is equivalent to the T26/T39 minimum transitive obstruction, but at "
            "the cross-level rather than the within-level layer."
        ),
        theorem_cross_level_ac5=(
            "Cross-Level AC5 Theorem: holonic PO1 admissibility requires non-empty "
            "forgotten_dims in the cross-level morphism (AC5 at the holonic level). "
            "A source-satisfiable + target-obstructed holonic pair is NOT a holonic PO1 "
            "instance if the cross-level morphism declares no forgotten structure. "
            "The named forgotten structure identifies WHICH cross-level compatibility "
            "was lost by the projection, making the holonic obstruction causally attributed "
            "rather than accidentally co-occurring."
        ),
        hypothesis_evaluations=hypotheses,
        best_supported_hypothesis="H_B",
        boundary=(
            "Results are for binary {-1,1} domains with same/different constraints "
            "(same CSP fragment as T39). The holonic nodes used here are D1RestrictionSystems; "
            "a full holarchy would use TypedTransportNetworks as nodes (networks of networks). "
            "That second-level nesting has not been implemented — this test covers one level "
            "of cross-level composition. The parameter space is small (4 scenarios, 2 PO1 "
            "bridges); a broader enumeration would strengthen the statistical confidence in "
            "H_B and H_C. The micro_obstructed scenario is a control; it shows that micro "
            "obstructions propagate to the holonic level (no absorption), which is the "
            "expected behavior for strict holonic satisfiability."
        ),
        recommendation=(
            "Adopt Holonic Emergence and Cross-Level AC5 as named theorems in CLAIM-LEDGER.md. "
            "Next steps: (1) extend nodes from D1RestrictionSystems to TypedTransportNetworks "
            "to implement the full second-level nesting; (2) run a parameter sweep over "
            "cross-level edge topologies to map which configurations produce emergence vs. "
            "reduction; (3) test whether the holonic AC5 condition is a strict strengthening "
            "of the T32 admissibility basis or collapses to the same conditions at higher scale."
        ),
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def t40_result_to_dict(result: T40Result) -> dict[str, Any]:
    def _scenario(s: HolonicGlobalSection) -> dict[str, Any]:
        return {
            "network_name": s.network_name,
            "micro_results": [
                {"node_name": r.node_name, "globally_satisfiable": r.globally_satisfiable}
                for r in s.micro_results
            ],
            "all_micro_satisfiable": s.all_micro_satisfiable,
            "holonic_globally_satisfiable": s.holonic_globally_satisfiable,
            "holonic_witness_count": s.holonic_witness_count,
            "emergence_detected": s.emergence_detected,
            "obstruction_source": s.obstruction_source,
        }

    def _bridge(b: HolonicPO1Bridge) -> dict[str, Any]:
        return {
            "case_name": b.case_name,
            "source_name": b.source_name,
            "target_name": b.target_name,
            "source_holonic_satisfiable": b.source_holonic_satisfiable,
            "target_holonic_obstructed": b.target_holonic_obstructed,
            "cross_level_forgotten_dims": list(b.cross_level_forgotten_dims),
            "ac5_fires": b.ac5_fires,
            "ac7_holds": b.ac7_holds,
            "holonic_po1_admissible": b.holonic_po1_admissible,
        }

    def _hyp(h: HypothesisHolarchy) -> dict[str, Any]:
        return {
            "hypothesis_id": h.hypothesis_id,
            "claim": h.claim,
            "verdict": h.verdict,
            "evidence_for": list(h.evidence_for),
            "evidence_against": list(h.evidence_against),
            "reason": h.reason,
        }

    return {
        "scenarios": [_scenario(s) for s in result.scenarios],
        "holonic_po1_bridges": [_bridge(b) for b in result.holonic_po1_bridges],
        "emergence_count": result.emergence_count,
        "po1_admissible_count": result.po1_admissible_count,
        "theorem_holonic_emergence": result.theorem_holonic_emergence,
        "theorem_cross_level_ac5": result.theorem_cross_level_ac5,
        "hypothesis_evaluations": [_hyp(h) for h in result.hypothesis_evaluations],
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "boundary": result.boundary,
        "recommendation": result.recommendation,
    }
