"""T13: signed and interfering readout on the T1 causal record graph.

Typed extension: records carry complex weights. The finality layer (T1
machinery) is weight-blind by construction; readout is computed from weights.
The point of the lab is to prove those two layers mathematically distinct.
No T1/T12 source is modified.
"""

from __future__ import annotations

import cmath
from itertools import combinations

from models.t1_record_graph import CausalRecordGraph, Observer, Record


class ReadoutRecordGraph(CausalRecordGraph):
    """Causal record graph whose records carry complex readout weights."""

    def __init__(self) -> None:
        super().__init__()
        self.weights: dict[str, complex] = {}

    def add_weighted_record(self, record: Record, weight: complex) -> None:
        self.add_record(record)
        self.weights[record.record_id] = complex(weight)

    def amplitude(
        self,
        observer: Observer,
        proposition: str,
        value: str,
        event: str | None = None,
    ) -> complex:
        records = self.accessible_records(observer, proposition, value, event)
        return sum((self.weights[r.record_id] for r in records), 0j)

    def readout_linear(self, observer: Observer, proposition: str, value: str, event: str | None = None) -> float:
        """Phase 1: signed scalar readout (Jordan-decomposable; trivial case)."""
        amp = self.amplitude(observer, proposition, value, event)
        if abs(amp.imag) > 1e-12:
            raise ValueError("linear readout is defined for real signed weights only")
        return amp.real

    def signed_counters(self, observer: Observer, proposition: str, value: str, event: str | None = None) -> tuple[int, int]:
        """Monotone counters (P, N) for +1/-1 weights: the Jordan decomposition."""
        records = self.accessible_records(observer, proposition, value, event)
        plus = sum(1 for r in records if self.weights[r.record_id].real > 0)
        minus = sum(1 for r in records if self.weights[r.record_id].real < 0)
        return plus, minus

    def readout_born(self, observer: Observer, proposition: str, value: str, event: str | None = None) -> float:
        """Phase 2: Born-style readout |sum of amplitudes|^2 (interference-bearing)."""
        return abs(self.amplitude(observer, proposition, value, event)) ** 2


def measure(weights: tuple[complex, ...]) -> float:
    """Sorkin-style measure of a record set: mu(S) = |sum of weights|^2."""
    return abs(sum(weights, 0j)) ** 2


def sorkin_i2(a: tuple[complex, ...], b: tuple[complex, ...]) -> float:
    return measure(a + b) - measure(a) - measure(b)


def sorkin_i3(a: tuple[complex, ...], b: tuple[complex, ...], c: tuple[complex, ...]) -> float:
    return (
        measure(a + b + c)
        - measure(a + b)
        - measure(a + c)
        - measure(b + c)
        + measure(a)
        + measure(b)
        + measure(c)
    )


def sorkin_i3_coefficients() -> dict[str, int]:
    """Coefficient check for the quadratic measure's third-order term.

    For mu(S) = |sum S|^2, every ordered pair contribution w_i * conj(w_j)
    appears with net coefficient zero in I3.  The labels name whether each
    ordered pair is internal to one block or crosses two blocks.
    """

    return {
        "within_a": 1 - 1 - 1 + 1,
        "within_b": 1 - 1 - 1 + 1,
        "within_c": 1 - 1 - 1 + 1,
        "cross_ab": 1 - 1,
        "cross_ac": 1 - 1,
        "cross_bc": 1 - 1,
    }


def build_w1_pair() -> tuple[ReadoutRecordGraph, ReadoutRecordGraph, Observer]:
    """Two graphs, identical topology and records, weights differ by one phase.

    Constructive: weights (1, 1).  Destructive: weights (1, -1).
    Finality profiles are weight-blind and therefore identical.
    """

    def build(second_weight: complex) -> ReadoutRecordGraph:
        graph = ReadoutRecordGraph()
        for event in ("x1", "x2", "observe"):
            graph.add_event(event)
        graph.add_causal_edge("x1", "observe")
        graph.add_causal_edge("x2", "observe")
        graph.add_weighted_record(Record("r1", "X", "true", "x1", "h1", 1.0), 1)
        graph.add_weighted_record(Record("r2", "X", "true", "x2", "h2", 1.0), second_weight)
        return graph

    constructive = build(1)
    destructive = build(-1)
    observer = Observer("O", "observe", frozenset({"h1", "h2"}))
    return constructive, destructive, observer


def build_w2_chain() -> tuple[ReadoutRecordGraph, Observer, tuple[str, ...]]:
    """A causal chain where evidence grows monotonically and readout cancels mid-chain.

    Weights along the chain: +1, -1, +1.  Born readout: 1 -> 0 -> 1.
    """
    graph = ReadoutRecordGraph()
    events = ("e1", "e2", "e3", "observe")
    for event in events:
        graph.add_event(event)
    graph.add_causal_edge("e1", "e2")
    graph.add_causal_edge("e2", "e3")
    graph.add_causal_edge("e3", "observe")
    graph.add_weighted_record(Record("c1", "X", "true", "e1", "h1", 1.0), 1)
    graph.add_weighted_record(Record("c2", "X", "true", "e2", "h2", 1.0), -1)
    graph.add_weighted_record(Record("c3", "X", "true", "e3", "h3", 1.0), 1)
    observer = Observer("O", "observe", frozenset({"h1", "h2", "h3"}))
    return graph, observer, ("e1", "e2", "e3")


def build_observer_consistency_pair() -> tuple[ReadoutRecordGraph, Observer, Observer]:
    """One graph, two observers; the partial observer cannot access the -1 record."""
    graph, _, _ = build_w2_chain()
    full = Observer("O_full", "observe", frozenset({"h1", "h2", "h3"}))
    partial = Observer("O_partial", "observe", frozenset({"h1", "h3"}))
    return graph, full, partial
