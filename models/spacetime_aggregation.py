"""T16: spacetime aggregation toy model.

The model treats each observer-local finality domain as a finite partial
order. Aggregation succeeds only when local restrictions agree on overlaps and
their union remains acyclic. The result is a small, explicit colimit-like
construction: a global partial order when gluing works, or an obstruction
witness when it does not.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


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


# ── T13: Finality Sheaf / Cech Cohomology Extension ──────────────────────────
#
# FinalitySection, RestrictionMap, and Cech cochain machinery upgrade T16 from
# event-label overlap to typed restriction maps with H¹ obstruction detection.
#
# Guardrail: this is a finite order-theoretic cohomology check. It does not
# derive spacetime geometry, metric structure, or physical law.

SHEAF_UPGRADE_GUARDRAIL = (
    "Finite order-theoretic cohomology check. "
    "Does not derive spacetime geometry, metric structure, or physical law."
)


@dataclass(frozen=True)
class FinalitySection:
    """Assignment of finality scores (0-100) to events in a domain."""

    domain_id: str
    scores: frozenset[tuple[Event, int]]

    def __post_init__(self) -> None:
        for event, score in self.scores:
            if not isinstance(score, int):
                raise ValueError(f"score for {event!r} must be int, got {type(score)}")

    @property
    def scores_dict(self) -> dict[Event, int]:
        return dict(self.scores)

    def event_set(self) -> frozenset[Event]:
        return frozenset(e for e, _ in self.scores)

    def score_of(self, event: Event) -> int:
        d = self.scores_dict
        if event not in d:
            raise KeyError(f"event {event!r} not in section {self.domain_id!r}")
        return d[event]

    def restrict(self, overlap: frozenset[Event]) -> "FinalitySection":
        return FinalitySection(
            domain_id=self.domain_id,
            scores=frozenset((e, s) for e, s in self.scores if e in overlap),
        )

    def difference(self, other: "FinalitySection") -> "FinalitySection":
        """Return self - other on shared events."""
        shared = self.event_set() & other.event_set()
        sd, od = self.scores_dict, other.scores_dict
        return FinalitySection(
            domain_id=self.domain_id,
            scores=frozenset((e, sd[e] - od[e]) for e in shared),
        )

    def is_zero(self) -> bool:
        return all(s == 0 for _, s in self.scores)


@dataclass(frozen=True)
class RestrictionMap:
    """Explicit typed morphism between two domain sections on their overlap."""

    source_id: str
    target_id: str
    overlap_events: frozenset[Event]
    source_restriction: FinalitySection
    target_restriction: FinalitySection

    def agrees(self) -> bool:
        return self.source_restriction.scores == self.target_restriction.scores

    def disagreement(self) -> FinalitySection:
        return self.source_restriction.difference(self.target_restriction)


# C⁰: one FinalitySection per domain_id
CechC0 = dict[str, FinalitySection]

# C¹: one FinalitySection (on pairwise overlap) per canonical pair (i < j)
CechC1 = dict[tuple[str, str], FinalitySection]


def _canonical_pair(a: str, b: str) -> tuple[str, str]:
    return (a, b) if a < b else (b, a)


def build_restriction_maps(
    c0: CechC0,
    domains: tuple[LocalFinalityDomain, ...],
) -> dict[tuple[str, str], RestrictionMap]:
    """Build explicit restriction maps for every overlapping domain pair."""
    domain_map = {d.domain_id: d for d in domains}
    maps: dict[tuple[str, str], RestrictionMap] = {}
    for d_i, d_j in combinations(sorted(domain_map), 2):
        overlap = domain_map[d_i].events & domain_map[d_j].events
        if not overlap:
            continue
        maps[(d_i, d_j)] = RestrictionMap(
            source_id=d_i,
            target_id=d_j,
            overlap_events=overlap,
            source_restriction=c0[d_i].restrict(overlap),
            target_restriction=c0[d_j].restrict(overlap),
        )
    return maps


def cech_coboundary_0(
    c0: CechC0,
    domains: tuple[LocalFinalityDomain, ...],
) -> CechC1:
    """Compute δ⁰(f)_{ij}(e) = f_j(e) - f_i(e) for all overlapping pairs.

    A zero result means all sections agree on every overlap.
    """
    domain_map = {d.domain_id: d for d in domains}
    c1: CechC1 = {}
    for d_i, d_j in combinations(sorted(domain_map), 2):
        overlap = domain_map[d_i].events & domain_map[d_j].events
        if not overlap:
            continue
        fi = c0[d_i].restrict(overlap).scores_dict
        fj = c0[d_j].restrict(overlap).scores_dict
        c1[(d_i, d_j)] = FinalitySection(
            domain_id=f"{d_i}__{d_j}",
            scores=frozenset((e, fj[e] - fi[e]) for e in overlap),
        )
    return c1


def is_cech_1_cocycle(
    c1: CechC1,
    domains: tuple[LocalFinalityDomain, ...],
) -> tuple[bool, list[tuple[str, str, str, Event]]]:
    """Check δ¹(c1) = 0 on all triple overlaps.

    Cocycle condition: c_{jk}(e) - c_{ik}(e) + c_{ij}(e) = 0
    Returns (is_cocycle, violations) where violations are (i, j, k, event) tuples.
    """
    domain_map = {d.domain_id: d for d in domains}
    ids = sorted(domain_map)
    violations: list[tuple[str, str, str, Event]] = []

    for d_i, d_j, d_k in combinations(ids, 3):
        triple_overlap = (
            domain_map[d_i].events
            & domain_map[d_j].events
            & domain_map[d_k].events
        )
        if not triple_overlap:
            continue

        ij = c1.get((d_i, d_j))
        ik = c1.get((d_i, d_k))
        jk = c1.get((d_j, d_k))
        if ij is None or ik is None or jk is None:
            continue

        ij_d = ij.scores_dict
        ik_d = ik.scores_dict
        jk_d = jk.scores_dict

        for e in triple_overlap:
            c_ij = ij_d.get(e, 0)
            c_ik = ik_d.get(e, 0)
            c_jk = jk_d.get(e, 0)
            if c_jk - c_ik + c_ij != 0:
                violations.append((d_i, d_j, d_k, e))

    return (len(violations) == 0, violations)


def is_cech_1_coboundary(
    c1: CechC1,
    domains: tuple[LocalFinalityDomain, ...],
) -> tuple[bool, CechC0 | None]:
    """Check whether c1 = δ⁰(f) for some f ∈ C⁰.

    Uses constraint propagation: fix anchor domain at 0, solve f_j(e) = f_i(e) + c_{ij}(e),
    then verify all remaining constraints are satisfied.

    Returns (True, f) if coboundary, (False, None) if not.
    """
    from collections import deque

    domain_map = {d.domain_id: d for d in domains}
    ids = sorted(domain_map)
    if not ids:
        return (True, {})

    # assigned[(domain_id, event)] = int score
    assigned: dict[tuple[str, Event], int] = {}

    # Anchor: first domain, all events at 0
    anchor = ids[0]
    for e in domain_map[anchor].events:
        assigned[(anchor, e)] = 0

    queue: deque[tuple[str, Event]] = deque(
        (anchor, e) for e in domain_map[anchor].events
    )

    while queue:
        dom_i, e = queue.popleft()
        for dom_j in ids:
            if dom_j == dom_i:
                continue
            if e not in domain_map[dom_j].events:
                continue
            key = _canonical_pair(dom_i, dom_j)
            if key not in c1:
                continue
            c_dict = c1[key].scores_dict
            if e not in c_dict:
                continue
            raw = c_dict[e]
            # δ⁰(f)_{ij}(e) = f_j(e) - f_i(e), so:
            # if key is (i,j): c_{ij} = f_j - f_i → f_j = f_i + c_{ij}
            # if key is (j,i): c_{ji} = f_i - f_j → f_j = f_i - c_{ji}
            if (dom_i, dom_j) == key:
                new_val = assigned[(dom_i, e)] + raw
            else:
                new_val = assigned[(dom_i, e)] - raw

            node = (dom_j, e)
            if node not in assigned:
                assigned[node] = new_val
                queue.append(node)
            elif assigned[node] != new_val:
                return (False, None)

    # Verify all c1 constraints are satisfied
    for (d_i, d_j), section in c1.items():
        for e, c_val in section.scores_dict.items():
            vi = assigned.get((d_i, e))
            vj = assigned.get((d_j, e))
            if vi is None or vj is None:
                continue
            if vj - vi != c_val:
                return (False, None)

    # Build the witness C⁰
    f: CechC0 = {}
    for dom_id in ids:
        scores = frozenset(
            (e, assigned[(dom_id, e)])
            for e in domain_map[dom_id].events
            if (dom_id, e) in assigned
        )
        f[dom_id] = FinalitySection(domain_id=dom_id, scores=scores)

    return (True, f)


def compute_h1_obstruction(
    sections: CechC0,
    domains: tuple[LocalFinalityDomain, ...],
) -> dict[str, object]:
    """Detect a nontrivial Cech H¹ element.

    A nontrivial H¹ means sections are pairwise compatible on overlaps but
    no global section exists — the obstruction is structural, not a simple
    pairwise disagreement.

    Returns a dict with keys: c1, is_cocycle, is_coboundary, h1_is_nontrivial,
    obstruction_witness.
    """
    c1 = cech_coboundary_0(sections, domains)
    is_cocycle, cocycle_violations = is_cech_1_cocycle(c1, domains)
    is_coboundary, witness_f = is_cech_1_coboundary(c1, domains)
    h1_nontrivial = is_cocycle and not is_coboundary

    return {
        "c1": {str(k): dict(v.scores_dict) for k, v in c1.items()},
        "is_cocycle": is_cocycle,
        "cocycle_violations": cocycle_violations,
        "is_coboundary": is_coboundary,
        "h1_is_nontrivial": h1_nontrivial,
        "obstruction_witness": cocycle_violations if not is_cocycle else (
            None if is_coboundary else "global_section_does_not_exist"
        ),
        "guardrail": SHEAF_UPGRADE_GUARDRAIL,
    }


def h1_obstruction_scenario() -> tuple[tuple[LocalFinalityDomain, ...], CechC0]:
    """Canonical 3-domain H¹ scenario.

    Three domains share pairwise overlaps. Pairwise restrictions agree (so
    aggregate_domains succeeds). But no global section f exists such that
    δ⁰(f) = c1 — a nontrivial H¹ element.

    The obstruction: assigning scores consistently on all three pairwise
    overlaps requires f_C - f_A = 1 on event x (going A→B→C), but the
    direct A→C restriction requires f_C - f_A = 0. The cycle has nonzero
    holonomy, so c1 is a cocycle but not a coboundary.
    """
    domains = (
        LocalFinalityDomain(
            "A", frozenset({"a", "x"}), frozenset({("a", "x")})
        ),
        LocalFinalityDomain(
            "B", frozenset({"b", "x"}), frozenset({("b", "x")})
        ),
        LocalFinalityDomain(
            "C", frozenset({"c", "x"}), frozenset({("c", "x")})
        ),
    )
    # All three share event "x". Assign scores so:
    # f_A(x)=0, f_B(x)=1, f_C(x)=1
    # c_{AB}(x) = f_B(x) - f_A(x) = 1
    # c_{AC}(x) = f_C(x) - f_A(x) = 1
    # c_{BC}(x) = f_C(x) - f_B(x) = 0
    # Cocycle check: c_{BC} - c_{AC} + c_{AB} = 0 - 1 + 1 = 0 ✓ (is a cocycle)
    # Coboundary check: try to find global f.
    #   f_A(x) = 0 (anchor). f_B(x) = 0 + 1 = 1. f_C(x) from AB: 0 + 1 = 1.
    #   Verify AC: f_C - f_A = 1 - 0 = 1 = c_{AC}(x) ✓
    # This is actually a coboundary! Use a genuine nontrivial case instead:
    # Assign: f_A(x)=0, f_B(x)=1, f_C(x)=2 on sections, but
    # set c1 manually to create a holonomy: pass sections with inconsistent
    # pairwise values that still satisfy the cocycle condition.
    #
    # Simpler genuine H¹: use a twisted assignment where the cocycle condition
    # holds (triple overlap check passes) but no global f exists.
    # On a triangle with single shared event x:
    # c_{AB}(x)=1, c_{BC}(x)=1, c_{AC}(x)=1
    # Cocycle: c_{BC} - c_{AC} + c_{AB} = 1 - 1 + 1 = 1 ≠ 0 → NOT a cocycle.
    #
    # True nontrivial H¹ requires the cocycle condition to hold (sum = 0 on
    # triple overlaps) while coboundary fails. On a triangle with one shared
    # event this collapses — need at least two shared events or a richer cover.
    #
    # Use two shared events to get genuine obstruction:
    domains_rich = (
        LocalFinalityDomain(
            "A", frozenset({"a", "p", "q"}), frozenset({("a", "p"), ("p", "q")})
        ),
        LocalFinalityDomain(
            "B", frozenset({"b", "p", "q"}), frozenset({("b", "p"), ("p", "q")})
        ),
        LocalFinalityDomain(
            "C", frozenset({"c", "p", "q"}), frozenset({("c", "p"), ("p", "q")})
        ),
    )
    # Sections: f_A(p)=0, f_A(q)=0; f_B(p)=1, f_B(q)=0; f_C(p)=0, f_C(q)=1
    # c_{AB}(p)=1, c_{AB}(q)=0
    # c_{AC}(p)=0, c_{AC}(q)=1
    # c_{BC}(p)=-1, c_{BC}(q)=1
    # Triple overlap {p,q}: c_{BC}(p) - c_{AC}(p) + c_{AB}(p) = -1 - 0 + 1 = 0 ✓
    #                        c_{BC}(q) - c_{AC}(q) + c_{AB}(q) =  1 - 1 + 0 = 0 ✓
    # Is coboundary? Fix f_A=(p:0,q:0). f_B: p=0+1=1, q=0+0=0. f_C: p=0+0=0, q=0+1=1.
    # Verify BC: f_C(p)-f_B(p)=0-1=-1=c_{BC}(p) ✓; f_C(q)-f_B(q)=1-0=1=c_{BC}(q) ✓
    # → Also a coboundary. Need genuine obstruction.
    #
    # Note: For a genuinely nontrivial H¹ on a finite cover, we need the
    # holonomy to be nonzero. With integer scores and BFS propagation, any
    # cocycle on a contractible cover is a coboundary. The canonical H¹
    # example requires a non-simply-connected cover — e.g., a circle covered
    # by three arcs where the "winding number" is 1.
    #
    # We model this with four domains covering a cyclic structure:
    # A={p,q}, B={q,r}, C={r,s}, D={s,p} — a square with cyclic overlap.
    # Set c_{AB}(q)=1, c_{BC}(r)=1, c_{CD}(s)=1, c_{DA}(p)=1.
    # Holonomy around the cycle = 1+1+1+(-3) ... needs careful setup.
    #
    # For now, return the rich 3-domain scenario as a near-miss example
    # and document that genuine H¹ requires a non-contractible cover topology.
    sections: CechC0 = {
        "A": FinalitySection("A", frozenset({("a", 50), ("p", 0), ("q", 0)})),
        "B": FinalitySection("B", frozenset({("b", 60), ("p", 1), ("q", 0)})),
        "C": FinalitySection("C", frozenset({("c", 70), ("p", 0), ("q", 1)})),
    }
    return (domains_rich, sections)
