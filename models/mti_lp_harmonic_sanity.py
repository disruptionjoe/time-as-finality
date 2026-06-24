from __future__ import annotations

from collections import Counter
from math import log
from typing import Iterable, Sequence


def harmonic_mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    if any(value <= 0 for value in values):
        raise ValueError("values must be positive")
    return len(values) / sum(1 / value for value in values)


def beta_from_proxy(proxy_value: float, n: int) -> float:
    if proxy_value <= 0:
        raise ValueError("proxy_value must be positive")
    if n <= 1:
        raise ValueError("n must be greater than 1")
    return 1 - log(proxy_value) / log(n)


def pure_lp_optimum(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    return min(values)


def lower_bound_lp_optimum(values: Sequence[float], d: float) -> tuple[tuple[float, ...], float]:
    if not values:
        raise ValueError("values must be non-empty")
    k = len(values)
    if d < 0 or d > 1 / k:
        raise ValueError("d must satisfy 0 <= d <= 1/k")

    shortest_index = min(range(k), key=lambda index: values[index])
    weights = [d] * k
    weights[shortest_index] = 1 - (k - 1) * d
    objective = sum(weight * value for weight, value in zip(weights, values))
    return tuple(weights), objective


def inverse_time_weights(values: Sequence[float]) -> tuple[float, ...]:
    denominator = sum(1 / value for value in values)
    return tuple((1 / value) / denominator for value in values)


def path_edge_loads(paths: Iterable[Sequence[str]]) -> Counter[str]:
    loads: Counter[str] = Counter()
    for path in paths:
        loads.update(path)
    return loads


def has_shared_edges(paths: Iterable[Sequence[str]]) -> bool:
    return any(load > 1 for load in path_edge_loads(paths).values())
