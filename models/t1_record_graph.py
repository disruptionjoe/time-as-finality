"""Finite causal-record-graph model for T1.

The implementation uses only graph reachability and record state. Numeric
timestamps and a global event order are intentionally absent.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations
from typing import Iterable


@dataclass(frozen=True)
class Record:
    record_id: str
    proposition: str
    value: str
    event: str
    holder: str
    erasure_cost: float = 1.0
    active: bool = True


@dataclass(frozen=True)
class Observer:
    observer_id: str
    event: str
    accessible_holders: frozenset[str]
    level: str = "reconciler"


@dataclass(frozen=True)
class FinalityProfile:
    accessible_support: int
    redundancy: int
    branch_robustness: int
    graph_reversal_cost: int

    def no_more_final_than(self, other: "FinalityProfile") -> bool:
        return all(a <= b for a, b in zip(self.as_tuple(), other.as_tuple()))

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.redundancy,
            self.branch_robustness,
            self.graph_reversal_cost,
        )


class CausalRecordGraph:
    def __init__(self) -> None:
        self._successors: dict[str, set[str]] = {}
        self.records: dict[str, Record] = {}

    @property
    def events(self) -> frozenset[str]:
        return frozenset(self._successors)

    def add_event(self, event: str) -> None:
        self._successors.setdefault(event, set())

    def add_causal_edge(self, earlier: str, later: str) -> None:
        self.add_event(earlier)
        self.add_event(later)
        self._successors[earlier].add(later)
        if self.is_ancestor(later, earlier):
            self._successors[earlier].remove(later)
            raise ValueError(f"edge {earlier!r}->{later!r} creates a cycle")

    def add_record(self, record: Record) -> None:
        if record.event not in self._successors:
            raise ValueError(f"unknown record event: {record.event}")
        if record.record_id in self.records:
            raise ValueError(f"duplicate record id: {record.record_id}")
        if record.erasure_cost < 0:
            raise ValueError("erasure cost must be non-negative")
        self.records[record.record_id] = record

    def erase_record(self, record_id: str) -> None:
        self.records[record_id] = replace(self.records[record_id], active=False)

    def is_ancestor(self, earlier: str, later: str) -> bool:
        if earlier == later:
            return True
        if earlier not in self._successors or later not in self._successors:
            return False
        pending = list(self._successors[earlier])
        seen: set[str] = set()
        while pending:
            event = pending.pop()
            if event == later:
                return True
            if event not in seen:
                seen.add(event)
                pending.extend(self._successors[event])
        return False

    def causal_past(self, event: str) -> frozenset[str]:
        return frozenset(candidate for candidate in self.events if self.is_ancestor(candidate, event))

    def topological_orders(self, limit: int | None = None) -> list[tuple[str, ...]]:
        predecessors = {
            event: {candidate for candidate in self.events if candidate != event and self.is_ancestor(candidate, event)}
            for event in self.events
        }
        results: list[tuple[str, ...]] = []

        def visit(prefix: tuple[str, ...], remaining: frozenset[str]) -> None:
            if limit is not None and len(results) >= limit:
                return
            if not remaining:
                results.append(prefix)
                return
            available = sorted(event for event in remaining if not (predecessors[event] & remaining))
            for event in available:
                visit(prefix + (event,), remaining - {event})

        visit((), self.events)
        return results

    def accessible_records(
        self,
        observer: Observer,
        proposition: str,
        value: str,
        event: str | None = None,
    ) -> tuple[Record, ...]:
        evaluation_event = event or observer.event
        if not self.is_ancestor(evaluation_event, observer.event):
            raise ValueError("evaluation event must be in the observer's causal past")
        return tuple(
            record
            for record in self.records.values()
            if record.active
            and record.proposition == proposition
            and record.value == value
            and record.holder in observer.accessible_holders
            and self.is_ancestor(record.event, evaluation_event)
        )

    def _antichain_width(self, events: Iterable[str]) -> int:
        unique_events = tuple(sorted(set(events)))
        for size in range(len(unique_events), 0, -1):
            for subset in combinations(unique_events, size):
                if all(
                    not self.is_ancestor(left, right) and not self.is_ancestor(right, left)
                    for left, right in combinations(subset, 2)
                ):
                    return size
        return 0

    def finality_profile(
        self,
        observer: Observer,
        proposition: str,
        value: str,
        threshold: int,
        event: str | None = None,
    ) -> FinalityProfile:
        if threshold < 1:
            raise ValueError("threshold must be at least one")
        records = self.accessible_records(observer, proposition, value, event)
        support = len(records)
        reversal_count = max(0, support - threshold + 1)
        return FinalityProfile(
            accessible_support=support,
            redundancy=len({record.holder for record in records}),
            branch_robustness=self._antichain_width(record.event for record in records),
            graph_reversal_cost=reversal_count,
        )

    def thermodynamic_reversal_proxy(
        self,
        observer: Observer,
        proposition: str,
        value: str,
        threshold: int,
        event: str | None = None,
    ) -> float:
        records = self.accessible_records(observer, proposition, value, event)
        erase_count = max(0, len(records) - threshold + 1)
        if erase_count == 0:
            return 0.0
        costs = sorted(record.erasure_cost for record in records)
        return sum(costs[:erase_count])

    def reconstruct_value(
        self,
        observer: Observer,
        proposition: str,
        threshold: int,
        event: str | None = None,
    ) -> str | None:
        evaluation_event = event or observer.event
        values = sorted({record.value for record in self.records.values() if record.proposition == proposition})
        winners = [
            value
            for value in values
            if len(self.accessible_records(observer, proposition, value, evaluation_event)) >= threshold
        ]
        return winners[0] if len(winners) == 1 else None

    def stabilization_frontier(
        self,
        observer: Observer,
        proposition: str,
        threshold: int,
    ) -> frozenset[str]:
        past = self.causal_past(observer.event)
        reconstructible = {
            event
            for event in past
            if self.reconstruct_value(observer, proposition, threshold, event) is not None
        }
        minimal = {
            event
            for event in reconstructible
            if not any(
                candidate != event
                and candidate in reconstructible
                and self.is_ancestor(candidate, event)
                for candidate in reconstructible
            )
        }
        return frozenset(minimal)

    def reconstructed_relation(
        self,
        observer: Observer,
        propositions: Iterable[str],
        threshold: int,
    ) -> frozenset[tuple[str, str]]:
        frontiers = {
            proposition: self.stabilization_frontier(observer, proposition, threshold)
            for proposition in propositions
        }
        relation: set[tuple[str, str]] = set()
        for left, right in combinations(sorted(frontiers), 2):
            left_before_right = self._frontier_precedes(frontiers[left], frontiers[right])
            right_before_left = self._frontier_precedes(frontiers[right], frontiers[left])
            if left_before_right and not right_before_left:
                relation.add((left, right))
            elif right_before_left and not left_before_right:
                relation.add((right, left))
        return frozenset(relation)

    def _frontier_precedes(self, left: frozenset[str], right: frozenset[str]) -> bool:
        if not left or not right:
            return False
        return all(any(a != b and self.is_ancestor(a, b) for a in left) for b in right)


def build_reference_scenario() -> tuple[CausalRecordGraph, Observer]:
    graph = CausalRecordGraph()
    for event in ("a", "a_copy", "b", "b_copy", "merge", "c", "c_copy", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("a", "a_copy")
    graph.add_causal_edge("b", "b_copy")
    graph.add_causal_edge("a_copy", "merge")
    graph.add_causal_edge("b_copy", "merge")
    graph.add_causal_edge("merge", "c")
    graph.add_causal_edge("c", "c_copy")
    graph.add_causal_edge("c_copy", "observe")

    records = (
        Record("ra1", "A", "true", "a", "ha1", 1.0),
        Record("ra2", "A", "true", "a_copy", "ha2", 8.0),
        Record("rb1", "B", "true", "b", "hb1", 2.0),
        Record("rb2", "B", "true", "b_copy", "hb2", 2.0),
        Record("rc1", "C", "true", "c", "hc1", 0.5),
        Record("rc2", "C", "true", "c_copy", "hc2", 0.5),
    )
    for record in records:
        graph.add_record(record)
    observer = Observer(
        "O",
        "observe",
        frozenset(record.holder for record in records),
    )
    return graph, observer


def minimal_total_order_counterexample() -> tuple[CausalRecordGraph, Observer]:
    graph = CausalRecordGraph()
    for event in ("left", "right", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("left", "observe")
    graph.add_causal_edge("right", "observe")
    graph.add_record(Record("left-record", "L", "true", "left", "left-holder"))
    graph.add_record(Record("right-record", "R", "true", "right", "right-holder"))
    observer = Observer("O", "observe", frozenset({"left-holder", "right-holder"}))
    return graph, observer
