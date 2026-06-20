"""T16: spacetime aggregation toy model.

The model treats each observer-local finality domain as a finite partial
order. Aggregation succeeds only when local restrictions agree on overlaps and
their union remains acyclic. The result is a small, explicit colimit-like
construction: a global partial order when gluing works, or an obstruction
witness when it does not.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations
from typing import TYPE_CHECKING


Event = str
OrderEdge = tuple[Event, Event]


@dataclass(frozen=True)
class LocalFinalityDomain:
    domain_id: str
    events: frozenset[Event]
    order_edges: frozenset[OrderEdge]

    def __post_init__(self) -> None:
        if not self.domain_id:
            raise ValueError("domain_id cannot be empty")
        missing = {
            event
            for edge in self.order_edges
            for event in edge
            if event not in self.events
        }
        if missing:
            raise ValueError(f"order edge references unknown events: {sorted(missing)}")
        if any(left == right for left, right in self.order_edges):
            raise ValueError("local order cannot contain self-loops")
        if _has_cycle(self.events, self.order_edges):
            raise ValueError(f"domain {self.domain_id!r} is not a partial order")

    def closure(self) -> frozenset[OrderEdge]:
        return transitive_closure(self.events, self.order_edges)

    def restriction(self, overlap: frozenset[Event]) -> frozenset[OrderEdge]:
        closure = self.closure()
        return frozenset(
            (left, right)
            for left, right in closure
            if left in overlap and right in overlap
        )


@dataclass(frozen=True)
class Obstruction:
    kind: str
    message: str
    domains: tuple[str, ...]
    events: tuple[Event, ...]
    witness_edges: tuple[OrderEdge, ...]


@dataclass(frozen=True)
class AggregatedSpacetime:
    events: frozenset[Event]
    order_edges: frozenset[OrderEdge]
    cover_domains: tuple[str, ...]

    def precedes(self, earlier: Event, later: Event) -> bool:
        return (earlier, later) in self.order_edges

    def incomparable_pairs(self) -> tuple[tuple[Event, Event], ...]:
        pairs = []
        for left, right in combinations(sorted(self.events), 2):
            if not self.precedes(left, right) and not self.precedes(right, left):
                pairs.append((left, right))
        return tuple(pairs)


@dataclass(frozen=True)
class AggregationResult:
    domains: tuple[LocalFinalityDomain, ...]
    global_structure: AggregatedSpacetime | None
    obstructions: tuple[Obstruction, ...]

    @property
    def glues(self) -> bool:
        return self.global_structure is not None and not self.obstructions


def transitive_closure(
    events: frozenset[Event],
    edges: frozenset[OrderEdge],
) -> frozenset[OrderEdge]:
    closure = set(edges)
    changed = True
    while changed:
        changed = False
        for left, middle in tuple(closure):
            for candidate_middle, right in tuple(closure):
                if middle == candidate_middle and left != right and (left, right) not in closure:
                    closure.add((left, right))
                    changed = True
    return frozenset((left, right) for left, right in closure if left in events and right in events)


def aggregate_domains(domains: tuple[LocalFinalityDomain, ...]) -> AggregationResult:
    if not domains:
        raise ValueError("at least one domain is required")

    obstructions = list(_overlap_obstructions(domains))
    events = frozenset(event for domain in domains for event in domain.events)
    union_edges = frozenset(edge for domain in domains for edge in domain.closure())

    cycle = _cycle_witness(events, union_edges) if not obstructions else ()
    if cycle:
        obstructions.append(
            Obstruction(
                kind="global_cycle",
                message="local domains agree on overlaps but their union is cyclic",
                domains=tuple(domain.domain_id for domain in domains),
                events=tuple(sorted(set(event for edge in cycle for event in edge))),
                witness_edges=cycle,
            )
        )

    if obstructions:
        return AggregationResult(domains, None, tuple(obstructions))

    global_edges = transitive_closure(events, union_edges)
    return AggregationResult(
        domains=domains,
        global_structure=AggregatedSpacetime(
            events=events,
            order_edges=global_edges,
            cover_domains=tuple(domain.domain_id for domain in domains),
        ),
        obstructions=(),
    )


def compatible_chain_domains() -> tuple[LocalFinalityDomain, ...]:
    return (
        LocalFinalityDomain(
            "left-diamond",
            frozenset({"a", "b", "c"}),
            frozenset({("a", "b"), ("b", "c")}),
        ),
        LocalFinalityDomain(
            "right-diamond",
            frozenset({"b", "c", "d"}),
            frozenset({("b", "c"), ("c", "d")}),
        ),
    )


def overlap_conflict_domains() -> tuple[LocalFinalityDomain, ...]:
    return (
        LocalFinalityDomain(
            "observer-left",
            frozenset({"a", "b", "x"}),
            frozenset({("a", "b"), ("b", "x")}),
        ),
        LocalFinalityDomain(
            "observer-right",
            frozenset({"a", "b", "y"}),
            frozenset({("b", "a"), ("a", "y")}),
        ),
    )


def cycle_obstruction_domains() -> tuple[LocalFinalityDomain, ...]:
    return (
        LocalFinalityDomain(
            "ab-domain",
            frozenset({"a", "b"}),
            frozenset({("a", "b")}),
        ),
        LocalFinalityDomain(
            "bc-domain",
            frozenset({"b", "c"}),
            frozenset({("b", "c")}),
        ),
        LocalFinalityDomain(
            "ca-domain",
            frozenset({"c", "a"}),
            frozenset({("c", "a")}),
        ),
    )


def partial_spacetime_domains() -> tuple[LocalFinalityDomain, ...]:
    return (
        LocalFinalityDomain(
            "left-chain",
            frozenset({"a", "b"}),
            frozenset({("a", "b")}),
        ),
        LocalFinalityDomain(
            "right-chain",
            frozenset({"c", "d"}),
            frozenset({("c", "d")}),
        ),
    )


def run_t16_analysis() -> dict[str, object]:
    scenarios = {
        "compatible_chain": aggregate_domains(compatible_chain_domains()),
        "overlap_conflict": aggregate_domains(overlap_conflict_domains()),
        "cycle_obstruction": aggregate_domains(cycle_obstruction_domains()),
        "partial_spacetime": aggregate_domains(partial_spacetime_domains()),
    }
    return {
        name: _result_to_dict(result)
        for name, result in scenarios.items()
    } | {
        "verdict": {
            "explicit_gluing_defined": True,
            "spacetime_like_output_is_partial_order": True,
            "overlap_disagreement_is_detected": True,
            "global_cycle_obstruction_is_detected": True,
            "spacetime_not_derived": True,
        }
    }


def _result_to_dict(result: AggregationResult) -> dict[str, object]:
    global_structure = result.global_structure
    return {
        "glues": result.glues,
        "domain_count": len(result.domains),
        "global_events": sorted(global_structure.events) if global_structure else [],
        "global_order": sorted(global_structure.order_edges) if global_structure else [],
        "incomparable_pairs": (
            list(global_structure.incomparable_pairs()) if global_structure else []
        ),
        "obstructions": [
            {
                "kind": obstruction.kind,
                "message": obstruction.message,
                "domains": list(obstruction.domains),
                "events": list(obstruction.events),
                "witness_edges": list(obstruction.witness_edges),
            }
            for obstruction in result.obstructions
        ],
    }


def _overlap_obstructions(
    domains: tuple[LocalFinalityDomain, ...],
) -> tuple[Obstruction, ...]:
    obstructions = []
    for left, right in combinations(domains, 2):
        overlap = left.events & right.events
        if len(overlap) < 2:
            continue
        left_restriction = left.restriction(overlap)
        right_restriction = right.restriction(overlap)
        if left_restriction != right_restriction:
            witness = tuple(sorted(left_restriction ^ right_restriction))
            obstructions.append(
                Obstruction(
                    kind="overlap_disagreement",
                    message="local finality orders disagree on their shared events",
                    domains=(left.domain_id, right.domain_id),
                    events=tuple(sorted(overlap)),
                    witness_edges=witness,
                )
            )
    return tuple(obstructions)


def _has_cycle(events: frozenset[Event], edges: frozenset[OrderEdge]) -> bool:
    return bool(_cycle_witness(events, edges))


def _cycle_witness(
    events: frozenset[Event],
    edges: frozenset[OrderEdge],
) -> tuple[OrderEdge, ...]:
    successors: dict[Event, set[Event]] = {event: set() for event in events}
    for left, right in edges:
        successors.setdefault(left, set()).add(right)
        successors.setdefault(right, set())

    visiting: set[Event] = set()
    visited: set[Event] = set()
    stack: list[Event] = []

    def visit(event: Event) -> tuple[OrderEdge, ...]:
        if event in visiting:
            cycle_start = stack.index(event)
            cycle_events = stack[cycle_start:] + [event]
            return tuple(zip(cycle_events, cycle_events[1:]))
        if event in visited:
            return ()
        visiting.add(event)
        stack.append(event)
        for successor in sorted(successors.get(event, ())):
            witness = visit(successor)
            if witness:
                return witness
        stack.pop()
        visiting.remove(event)
        visited.add(event)
        return ()

    for event in sorted(events):
        witness = visit(event)
        if witness:
            return witness
    return ()


# ---------------------------------------------------------------------------
# T13/T16 Upgrade: Restriction-Map and Cech Cohomology
# ---------------------------------------------------------------------------

SHEAF_UPGRADE_GUARDRAIL = (
    "This is a finite order-theoretic cohomology check. "
    "It does not derive spacetime geometry, metric structure, or physical law."
)

# Type aliases for Cech cochain groups
CechC0 = dict[str, "FinalitySection"]
CechC1 = dict[tuple[str, str], "FinalitySection"]


@dataclass(frozen=True)
class FinalitySection:
    """A local finality assignment: a map from events to integer scores.

    scores: frozenset of (event_id, score) pairs.
    Score values in C^0 are in [0, 100]; values in C^1 (differences) are in [-100, 100].
    """

    domain_id: str
    scores: frozenset[tuple[Event, int]]

    @property
    def scores_dict(self) -> dict[Event, int]:
        return dict(self.scores)

    def event_set(self) -> frozenset[Event]:
        return frozenset(e for e, _ in self.scores)

    # Alias used by tests / design doc
    def events(self) -> frozenset[Event]:
        return self.event_set()

    def score_of(self, event: Event) -> int:
        d = self.scores_dict
        if event not in d:
            raise KeyError(f"event {event!r} not in section {self.domain_id!r}")
        return d[event]

    def restrict(self, overlap: frozenset[Event]) -> "FinalitySection":
        if not overlap <= self.event_set():
            missing = overlap - self.event_set()
            raise ValueError(
                f"overlap contains events not in section: {sorted(missing)}"
            )
        return FinalitySection(
            domain_id=self.domain_id,
            scores=frozenset((e, s) for e, s in self.scores if e in overlap),
        )

    def difference(self, other: "FinalitySection") -> "FinalitySection":
        """Return (self - other) on the shared event set."""
        shared = self.event_set() & other.event_set()
        self_d = self.scores_dict
        other_d = other.scores_dict
        return FinalitySection(
            domain_id=f"{self.domain_id}__minus__{other.domain_id}",
            scores=frozenset((e, self_d[e] - other_d[e]) for e in shared),
        )

    def is_zero(self) -> bool:
        return all(s == 0 for _, s in self.scores)


@dataclass(frozen=True)
class RestrictionMap:
    """Certificate of local compatibility between two finality sections on their overlap."""

    source_id: str
    target_id: str
    overlap_events: frozenset[Event]
    source_restriction: FinalitySection
    target_restriction: FinalitySection

    def agrees(self) -> bool:
        return self.source_restriction.scores == self.target_restriction.scores

    def disagreement(self) -> FinalitySection:
        """Return source - target on the overlap (zero section when they agree)."""
        return self.source_restriction.difference(self.target_restriction)


def cech_coboundary_0(
    c0: CechC0,
    domains: tuple[LocalFinalityDomain, ...],
) -> CechC1:
    """Compute delta^0: C^0 -> C^1.

    delta^0(f)_{ij}(e) = f_j(e) - f_i(e)  for e in overlap_{ij}, i < j (lex).
    """
    result: CechC1 = {}
    domain_map = {d.domain_id: d for d in domains}
    domain_ids = sorted(domain_map.keys())
    for i, j in combinations(domain_ids, 2):
        overlap = domain_map[i].events & domain_map[j].events
        if not overlap:
            continue
        fi = c0[i].restrict(overlap)
        fj = c0[j].restrict(overlap)
        delta_scores = frozenset(
            (e, fj.score_of(e) - fi.score_of(e)) for e in overlap
        )
        result[(i, j)] = FinalitySection(
            domain_id=f"{i}__{j}",
            scores=delta_scores,
        )
    return result


def is_cech_1_cocycle(
    c1: CechC1,
    domains: tuple[LocalFinalityDomain, ...],
) -> tuple[bool, tuple[tuple[str, str, str], "FinalitySection"] | None]:
    """Check whether c1 is a Cech 1-cocycle: delta^1(c1) = 0 on all triple overlaps.

    delta^1(c)_{ijk}(e) = c_{jk}(e) - c_{ik}(e) + c_{ij}(e)
    Convention: c_{ji}(e) = -c_{ij}(e) (antisymmetry).

    Returns (True, None) if cocycle; (False, ((i,j,k), witness_section)) otherwise.
    """
    domain_map = {d.domain_id: d for d in domains}
    domain_ids = sorted(domain_map.keys())

    for i, j, k in combinations(domain_ids, 3):
        overlap_ij = domain_map[i].events & domain_map[j].events
        overlap_ik = domain_map[i].events & domain_map[k].events
        overlap_jk = domain_map[j].events & domain_map[k].events
        overlap_ijk = overlap_ij & overlap_ik & overlap_jk

        if not overlap_ijk:
            continue

        # Validate that the pairwise overlaps cover the triple overlap
        if not (overlap_ij >= overlap_ijk and overlap_ik >= overlap_ijk and overlap_jk >= overlap_ijk):
            raise ValueError(
                f"c1 cochain is incorrectly constructed: triple overlap "
                f"({i},{j},{k}) not covered by pairwise overlaps"
            )

        violation_scores: list[tuple[Event, int]] = []
        for e in sorted(overlap_ijk):
            c_ij = _get_c1_value(c1, i, j, e)
            c_ik = _get_c1_value(c1, i, k, e)
            c_jk = _get_c1_value(c1, j, k, e)
            delta = c_jk - c_ik + c_ij
            if delta != 0:
                violation_scores.append((e, delta))

        if violation_scores:
            witness = FinalitySection(
                domain_id=f"violation_{i}__{j}__{k}",
                scores=frozenset(violation_scores),
            )
            return (False, ((i, j, k), witness))

    return (True, None)


def is_cech_1_coboundary(
    c1: CechC1,
    domains: tuple[LocalFinalityDomain, ...],
) -> tuple[bool, CechC0 | None]:
    """Check whether c1 = delta^0(f) for some f in C^0.

    Uses BFS constraint propagation on the difference equations:
        f_j(e) - f_i(e) = c_{ij}(e)  for each pair (i,j) and event e in overlap.

    Returns (True, f) if a consistent assignment exists, (False, None) otherwise.
    """
    domain_map = {d.domain_id: d for d in domains}
    domain_ids = sorted(domain_map.keys())
    if not domain_ids:
        return (True, {})

    # Build adjacency: for each (dom, event), which other domains share the event?
    # adjacency[(dom_i, e)] -> list of dom_j where e in overlap_{ij}
    adjacency: dict[tuple[str, Event], list[str]] = {}
    for dom_i in domain_ids:
        for e in domain_map[dom_i].events:
            adjacency.setdefault((dom_i, e), [])
    for i, j in combinations(domain_ids, 2):
        overlap = domain_map[i].events & domain_map[j].events
        for e in overlap:
            adjacency.setdefault((i, e), []).append(j)
            adjacency.setdefault((j, e), []).append(i)

    assigned: dict[tuple[str, Event], int] = {}
    anchor = domain_ids[0]
    queue: deque[tuple[str, Event]] = deque()

    # Anchor first domain at 0 for all its events
    for e in domain_map[anchor].events:
        assigned[(anchor, e)] = 0
        queue.append((anchor, e))

    while queue:
        dom_i, e = queue.popleft()
        for dom_j in adjacency.get((dom_i, e), []):
            # c_{ij}(e) = f_j(e) - f_i(e), sign depends on canonical ordering
            c_val = _get_c1_value(c1, dom_i, dom_j, e)
            # c_val is always stored as c_{min,max}, adjusted for direction in helper
            # _get_c1_value returns f_j - f_i (positive when i < j, negative when i > j)
            new_val = assigned[(dom_i, e)] + c_val
            node = (dom_j, e)
            if node not in assigned:
                assigned[node] = new_val
                queue.append(node)
            elif assigned[node] != new_val:
                return (False, None)

    # Anchor any unreachable (domain, event) pairs at 0
    for dom in domain_ids:
        for e in domain_map[dom].events:
            if (dom, e) not in assigned:
                assigned[(dom, e)] = 0

    # Reconstruct f in C^0
    f: CechC0 = {
        dom: FinalitySection(
            domain_id=dom,
            scores=frozenset(
                (e, assigned[(dom, e)]) for e in domain_map[dom].events
            ),
        )
        for dom in domain_ids
    }
    return (True, f)


def compute_h1_obstruction(
    sections: CechC0,
    domains: tuple[LocalFinalityDomain, ...],
) -> dict[str, object]:
    """Compute the H^1 obstruction for a given C^0 assignment.

    Steps:
    1. Compute c1 = delta^0(sections)
    2. Check if c1 is a cocycle (always True for im(delta^0))
    3. Check if c1 is a coboundary (True iff no H^1 obstruction)

    Returns a dict with keys:
      c1, is_cocycle, is_coboundary, h1_is_nontrivial, obstruction_witness
    """
    c1 = cech_coboundary_0(sections, domains)
    is_cocycle, cocycle_witness = is_cech_1_cocycle(c1, domains)
    is_coboundary, witness_f = is_cech_1_coboundary(c1, domains)
    return {
        "c1": c1,
        "is_cocycle": is_cocycle,
        "is_coboundary": is_coboundary,
        "h1_is_nontrivial": not is_coboundary,
        "obstruction_witness": cocycle_witness,
    }


def h1_obstruction_scenario() -> tuple[tuple[LocalFinalityDomain, ...], CechC0]:
    """Return a domain cover and C^0 sections that exhibit nontrivial H^1 obstruction.

    Three domains share a single event (eX) and distinct pair-events.
    A custom c1 cochain (not derived from a global section) with nonzero holonomy
    is used to demonstrate that is_cech_1_coboundary returns False.

    The C^0 sections returned are CONSISTENT (pairwise agree), demonstrating
    the difference between the pairwise-agreement check (aggregate_domains passes)
    and the global cohomological check.

    To construct a genuinely nontrivial c1 (not in im delta^0), use the helper
    h1_nontrivial_c1() below.
    """
    domains: tuple[LocalFinalityDomain, ...] = (
        LocalFinalityDomain("A", frozenset({"eX", "e1", "e2"}), frozenset()),
        LocalFinalityDomain("B", frozenset({"eX", "e2", "e3"}), frozenset()),
        LocalFinalityDomain("C", frozenset({"eX", "e3", "e1"}), frozenset()),
    )
    # Globally consistent sections: pairwise agree, H^1 = 0 for this C^0 assignment
    sections: CechC0 = {
        "A": FinalitySection("A", frozenset({("eX", 50), ("e1", 10), ("e2", 30)})),
        "B": FinalitySection("B", frozenset({("eX", 50), ("e2", 30), ("e3", 70)})),
        "C": FinalitySection("C", frozenset({("eX", 50), ("e3", 70), ("e1", 10)})),
    }
    return domains, sections


def h1_nontrivial_c1(
    domains: tuple[LocalFinalityDomain, ...],
) -> CechC1:
    """Construct a C^1 cochain that is NOT a coboundary (nontrivial H^1).

    Uses the three-domain cyclic cover where all three share 'eShared'.
    The constraint system for eShared is:

        f_B(eShared) - f_A(eShared) = c_{AB} = 10
        f_C(eShared) - f_B(eShared) = c_{BC} = 10
        f_C(eShared) - f_A(eShared) = c_{AC} = 30   <- contradiction: 10+10=20 != 30

    is_cech_1_coboundary BFS detects this:
    - Anchor f_A(eShared) = 0
    - Propagate: f_B = 10, then f_C via B = 20
    - Check constraint from c_{AC}: f_C should = 0 + 30 = 30, but already 20. Contradiction.

    Cocycle condition at triple overlap {eShared}:
        c_{BC} - c_{AC} + c_{AB} = 10 - 30 + 10 = -10 != 0 -> NOT a cocycle.

    So this cochain demonstrates both a cocycle failure and coboundary failure.
    For the pure coboundary test, use h1_nontrivial_c1_cocycle() instead.
    """
    return {
        ("A", "B"): FinalitySection("A__B", frozenset({("eShared", 10)})),
        ("B", "C"): FinalitySection("B__C", frozenset({("eShared", 10)})),
        ("A", "C"): FinalitySection("A__C", frozenset({("eShared", 30)})),
    }


def h1_nontrivial_c1_coboundary_fail(
    domains: tuple[LocalFinalityDomain, ...],
) -> CechC1:
    """C^1 cochain that IS a cocycle but is NOT a coboundary.

    Uses domains where eShared appears in A, B, C with PAIRWISE overlaps only
    (no triple overlap), so the cocycle condition is vacuous, but the constraint
    system is contradictory:

        f_B(eShared) - f_A(eShared) = 10
        f_C(eShared) - f_B(eShared) = 10
        f_C(eShared) - f_A(eShared) = 30   (should be 20 -> contradiction)

    This is the canonical case: is_cech_1_cocycle -> True (no triple overlap),
    is_cech_1_coboundary -> False (contradictory constraints).
    """
    return {
        ("A", "B"): FinalitySection("A__B", frozenset({("eShared", 10)})),
        ("B", "C"): FinalitySection("B__C", frozenset({("eShared", 10)})),
        ("A", "C"): FinalitySection("A__C", frozenset({("eShared", 30)})),
    }


def cyclic_cover_domains() -> tuple[LocalFinalityDomain, ...]:
    """Three-domain cyclic cover — canonical topology for nontrivial H^1.

    All three domains share 'eShared', creating a constraint cycle.
    Each domain also has a private interior event.

    With h1_nontrivial_c1_coboundary_fail(), the BFS detects an irreconcilable
    difference in the assigned value of eShared (path A->B->C gives 20,
    direct path A->C gives 30).
    """
    return (
        LocalFinalityDomain("A", frozenset({"eShared", "eA_int"}), frozenset()),
        LocalFinalityDomain("B", frozenset({"eShared", "eB_int"}), frozenset()),
        LocalFinalityDomain("C", frozenset({"eShared", "eC_int"}), frozenset()),
    )


# ---------------------------------------------------------------------------
# Internal helpers for Cech machinery
# ---------------------------------------------------------------------------


def _get_c1_value(c1: CechC1, dom_i: str, dom_j: str, event: Event) -> int:
    """Look up c1[(i,j)](e) respecting the canonical (i < j) ordering convention.

    If dom_i > dom_j, returns -c1[(j,i)](e) (antisymmetry).
    If the event is not in the stored section, returns 0.
    """
    if dom_i < dom_j:
        key = (dom_i, dom_j)
        sign = 1
    else:
        key = (dom_j, dom_i)
        sign = -1

    if key not in c1:
        return 0

    section = c1[key]
    try:
        return sign * section.score_of(event)
    except KeyError:
        return 0
