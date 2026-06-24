from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import isclose
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class Edge:
    tau: float
    capacity: float

    def delay(self, load: float) -> float:
        if self.tau <= 0:
            raise ValueError("edge tau must be positive")
        if self.capacity <= 0:
            raise ValueError("edge capacity must be positive")
        if load >= self.capacity:
            return float("inf")
        utilization = load / self.capacity
        return self.tau / (1 - utilization)


@dataclass(frozen=True)
class PathNetwork:
    edges: Mapping[str, Edge]
    paths: tuple[tuple[str, ...], ...]
    demand: float = 1.0

    def __post_init__(self) -> None:
        if self.demand <= 0:
            raise ValueError("demand must be positive")
        if not self.paths:
            raise ValueError("network must include at least one path")
        missing = {
            edge_id
            for path in self.paths
            for edge_id in path
            if edge_id not in self.edges
        }
        if missing:
            raise ValueError(f"paths reference unknown edges: {sorted(missing)}")

    def free_path_times(self) -> tuple[float, ...]:
        return tuple(sum(self.edges[edge_id].tau for edge_id in path) for path in self.paths)


@dataclass(frozen=True)
class FlowSolution:
    flows: tuple[float, ...]
    value: float


def harmonic_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    if any(value <= 0 for value in values):
        raise ValueError("values must be positive")
    return len(values) / sum(1 / value for value in values)


def edge_loads(network: PathNetwork, flows: Sequence[float]) -> Counter[str]:
    if len(flows) != len(network.paths):
        raise ValueError("flow count must match path count")
    loads: Counter[str] = Counter()
    for flow, path in zip(flows, network.paths):
        for edge_id in path:
            loads[edge_id] += flow
    return loads


def path_latency(network: PathNetwork, path: Sequence[str], loads: Mapping[str, float]) -> float:
    return sum(network.edges[edge_id].delay(loads.get(edge_id, 0.0)) for edge_id in path)


def max_loaded_path_latency(network: PathNetwork, flows: Sequence[float]) -> float:
    loads = edge_loads(network, flows)
    latencies = [
        path_latency(network, path, loads)
        for flow, path in zip(flows, network.paths)
        if flow > 1e-12
    ]
    if not latencies:
        return float("inf")
    return max(latencies)


def _grid_simplex(total: float, parts: int, step: float) -> Iterable[tuple[float, ...]]:
    if parts == 1:
        yield (total,)
        return

    ticks = round(total / step)
    if not isclose(ticks * step, total, abs_tol=1e-9):
        raise ValueError("step must divide total demand for grid search")

    def rec(remaining_ticks: int, remaining_parts: int) -> Iterable[tuple[int, ...]]:
        if remaining_parts == 1:
            yield (remaining_ticks,)
            return
        for value in range(remaining_ticks + 1):
            for suffix in rec(remaining_ticks - value, remaining_parts - 1):
                yield (value, *suffix)

    for allocation in rec(ticks, parts):
        yield tuple(value * step for value in allocation)


def solve_minimax_cflow(network: PathNetwork, step: float = 0.001) -> FlowSolution:
    best: FlowSolution | None = None
    for flows in _grid_simplex(network.demand, len(network.paths), step):
        value = max_loaded_path_latency(network, flows)
        if best is None or value < best.value:
            best = FlowSolution(flows=flows, value=value)
    if best is None:
        raise RuntimeError("no feasible flow allocation found")
    return best


def has_shared_edges(paths: Iterable[Sequence[str]]) -> bool:
    counts: Counter[str] = Counter()
    for path in paths:
        counts.update(path)
    return any(count > 1 for count in counts.values())


def disjoint_two_path_network() -> PathNetwork:
    return PathNetwork(
        edges={
            "s-a": Edge(tau=1, capacity=2),
            "a-t": Edge(tau=1, capacity=2),
            "s-b": Edge(tau=1, capacity=2),
            "b-t": Edge(tau=1, capacity=2),
        },
        paths=(("s-a", "a-t"), ("s-b", "b-t")),
    )


def shared_prefix_two_path_network() -> PathNetwork:
    return PathNetwork(
        edges={
            "s-u": Edge(tau=1, capacity=2),
            "u-a": Edge(tau=0.5, capacity=2),
            "a-t": Edge(tau=0.5, capacity=2),
            "u-b": Edge(tau=0.5, capacity=2),
            "b-t": Edge(tau=0.5, capacity=2),
        },
        paths=(("s-u", "u-a", "a-t"), ("s-u", "u-b", "b-t")),
    )


@dataclass(frozen=True)
class RecordPolicy:
    name: str
    append_only: bool
    retains_history: bool
    challenge_window: int


def record_reconstructable(policy: RecordPolicy) -> bool:
    return policy.append_only and policy.retains_history and policy.challenge_window > 0


def fixed_network_record_capability(
    network: PathNetwork, policy: RecordPolicy, step: float = 0.001
) -> tuple[float, bool]:
    return solve_minimax_cflow(network, step=step).value, record_reconstructable(policy)
