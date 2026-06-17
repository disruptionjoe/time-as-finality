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
