"""T82: persistent reconciler cost boundary for H7.

T80 showed that raw trace profiles in a reversible CA need not be monotone.
This audit tests the next repair candidate: make the observer a persistent
reconciler subsystem rather than an external terminal window.

The result is a boundary, not a support theorem.  In this finite model,
monotone retained records require either a non-injective OR-style update or an
append-only reversible ledger that consumes fresh blank slots.  A bounded
fixed-size reversible update can stay injective, but it does not preserve
monotone retained support.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import log
from typing import Callable, Iterable

from models.emergence_lab import BOLTZMANN_J_PER_K, shannon_entropy
from models.reversible_finality_nonmonotonicity import canonical_rule30_witness


BitMask = tuple[int, ...]
LogState = tuple[BitMask, ...]


@dataclass(frozen=True)
class FiniteMapAnalysis:
    input_count: int
    image_count: int
    injective: bool
    maximum_preimages: int
    lost_bits: float
    landauer_minimum_joules: float
    preimage_histogram: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class PolicyTrajectory:
    name: str
    memory_states: tuple[object, ...]
    support_sequence: tuple[int, ...]
    novelty_sequence: tuple[int, ...]
    monotone_support: bool
    transition_map: FiniteMapAnalysis
    resource_boundary: str
    verdict: str


@dataclass(frozen=True)
class T82Result:
    observations: tuple[BitMask, ...]
    raw_support_sequence: tuple[int, ...]
    raw_support_monotone: bool
    irreversible_or_policy: PolicyTrajectory
    reversible_xor_policy: PolicyTrajectory
    reversible_append_policy: PolicyTrajectory
    short_append_policy: PolicyTrajectory
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    h7_update: str
    blocker: str
    recommended_next: str


def bitstrings(width: int) -> tuple[BitMask, ...]:
    if width < 1:
        raise ValueError("width must be positive")
    return tuple(product((0, 1), repeat=width))


def analyze_finite_map(
    inputs: Iterable[object],
    update: Callable[[object], object],
    temperature_kelvin: float = 300.0,
) -> FiniteMapAnalysis:
    if temperature_kelvin <= 0:
        raise ValueError("temperature must be positive")
    input_states = tuple(inputs)
    if not input_states:
        raise ValueError("finite map analysis requires at least one input")
    output_counts = Counter(update(state) for state in input_states)
    probabilities = tuple(count / len(input_states) for count in output_counts.values())
    raw_lost_bits = _log2(len(input_states)) - shannon_entropy(probabilities)
    lost_bits = 0.0 if abs(raw_lost_bits) < 1e-12 else raw_lost_bits
    histogram = Counter(output_counts.values())
    return FiniteMapAnalysis(
        input_count=len(input_states),
        image_count=len(output_counts),
        injective=(
            len(output_counts) == len(input_states)
            and all(count == 1 for count in output_counts.values())
        ),
        maximum_preimages=max(output_counts.values()),
        lost_bits=lost_bits,
        landauer_minimum_joules=(
            BOLTZMANN_J_PER_K * temperature_kelvin * log(2) * lost_bits
        ),
        preimage_histogram=tuple(sorted(histogram.items())),
    )


def canonical_observation_sequence(layers: int = 5) -> tuple[BitMask, ...]:
    witness = canonical_rule30_witness(layers=layers)
    return tuple(
        tuple(profile.trace_mask[index] for index in profile.observer_window)
        for profile in witness.layer_profiles
    )


def raw_support_sequence(observations: tuple[BitMask, ...]) -> tuple[int, ...]:
    return tuple(sum(observation) for observation in observations)


def is_monotone(values: tuple[int, ...]) -> bool:
    return all(after >= before for before, after in zip(values, values[1:]))


def irreversible_or_policy(observations: tuple[BitMask, ...]) -> PolicyTrajectory:
    width = _observation_width(observations)
    memory = _blank_mask(width)
    states: list[BitMask] = []
    support: list[int] = []
    novelty: list[int] = []
    for observation in observations:
        novelty.append(sum(bit and not old for old, bit in zip(memory, observation)))
        memory = _or_mask(memory, observation)
        states.append(memory)
        support.append(sum(memory))
    return PolicyTrajectory(
        name="bounded_irreversible_or_memory",
        memory_states=tuple(states),
        support_sequence=tuple(support),
        novelty_sequence=tuple(novelty),
        monotone_support=is_monotone(tuple(support)),
        transition_map=analyze_or_update(width),
        resource_boundary=(
            "Fixed-width memory; monotone because OR coalesces old and new "
            "support states."
        ),
        verdict=(
            "Monotone retained support is bought by a non-injective update, so "
            "this repair reduces H7 to irreversible coarse-graining."
        ),
    )


def reversible_xor_policy(observations: tuple[BitMask, ...]) -> PolicyTrajectory:
    width = _observation_width(observations)
    memory = _blank_mask(width)
    states: list[BitMask] = []
    support: list[int] = []
    novelty: list[int] = []
    for observation in observations:
        novelty.append(sum(bit and not old for old, bit in zip(memory, observation)))
        memory = _xor_mask(memory, observation)
        states.append(memory)
        support.append(sum(memory))
    return PolicyTrajectory(
        name="bounded_reversible_xor_memory",
        memory_states=tuple(states),
        support_sequence=tuple(support),
        novelty_sequence=tuple(novelty),
        monotone_support=is_monotone(tuple(support)),
        transition_map=analyze_xor_update(width),
        resource_boundary=(
            "Fixed-width memory; injective because observation is preserved in "
            "the one-step map."
        ),
        verdict=(
            "Reversibility is preserved, but retained support can decrease; "
            "fixed reversible memory does not recover T18 monotonicity."
        ),
    )


def reversible_append_policy(
    observations: tuple[BitMask, ...],
    horizon: int | None = None,
) -> PolicyTrajectory:
    width = _observation_width(observations)
    resolved_horizon = len(observations) if horizon is None else horizon
    if resolved_horizon < 1:
        raise ValueError("horizon must be positive")
    blank = _blank_mask(width)
    log_state: LogState = tuple(blank for _ in range(resolved_horizon))
    cursor = 0
    states: list[LogState] = []
    support: list[int] = []
    novelty: list[int] = []
    union = blank
    exhausted_at: int | None = None
    for layer, observation in enumerate(observations):
        if cursor >= resolved_horizon:
            exhausted_at = layer
            break
        novelty.append(sum(bit and not old for old, bit in zip(union, observation)))
        mutable = list(log_state)
        mutable[cursor] = observation
        log_state = tuple(mutable)
        cursor += 1
        union = _or_mask(union, observation)
        states.append(log_state)
        support.append(sum(sum(slot) for slot in log_state))
    if exhausted_at is None:
        resource_boundary = (
            f"Injective only on the blank-slot subspace; consumes "
            f"{resolved_horizon * width} blank memory bits for "
            f"{resolved_horizon} observation slots."
        )
    else:
        resource_boundary = (
            f"Exhausted at observation layer {exhausted_at}; continuing would "
            "require either more blank slots or an erasing/recycling rule."
        )
    return PolicyTrajectory(
        name=f"reversible_append_only_ledger_h{resolved_horizon}",
        memory_states=tuple(states),
        support_sequence=tuple(support),
        novelty_sequence=tuple(novelty),
        monotone_support=is_monotone(tuple(support)),
        transition_map=analyze_append_update(resolved_horizon, width),
        resource_boundary=resource_boundary,
        verdict=(
            "Monotone and injective for the checked horizon, but only by "
            "turning elapsed observations into growing ledger state."
        ),
    )


def analyze_or_update(width: int) -> FiniteMapAnalysis:
    states = bitstrings(width)
    inputs = tuple((memory, observation) for memory in states for observation in states)
    return analyze_finite_map(
        inputs,
        lambda state: (_or_mask(state[0], state[1]), state[1]),
    )


def analyze_xor_update(width: int) -> FiniteMapAnalysis:
    states = bitstrings(width)
    inputs = tuple((memory, observation) for memory in states for observation in states)
    return analyze_finite_map(
        inputs,
        lambda state: (_xor_mask(state[0], state[1]), state[1]),
    )


def analyze_append_update(horizon: int, width: int) -> FiniteMapAnalysis:
    blank = _blank_mask(width)
    bit_states = bitstrings(width)
    inputs = []
    for cursor in range(horizon):
        for prefix in product(bit_states, repeat=cursor):
            log_state = tuple(prefix) + tuple(blank for _ in range(horizon - cursor))
            for observation in bit_states:
                inputs.append((log_state, cursor, observation))
    return analyze_finite_map(inputs, _append_step)


def run_t82_analysis(layers: int = 5) -> T82Result:
    observations = canonical_observation_sequence(layers=layers)
    raw = raw_support_sequence(observations)
    return T82Result(
        observations=observations,
        raw_support_sequence=raw,
        raw_support_monotone=is_monotone(raw),
        irreversible_or_policy=irreversible_or_policy(observations),
        reversible_xor_policy=reversible_xor_policy(observations),
        reversible_append_policy=reversible_append_policy(observations),
        short_append_policy=reversible_append_policy(observations, horizon=3),
        strongest_claim=(
            "In the T80 reversible trace witness, an endogenous finite "
            "reconciler gets monotone retained records only by using a "
            "non-injective coarse-graining update or by consuming append-only "
            "blank ledger state."
        ),
        weakened_claim=(
            "H7 is not rescued by adding persistent memory unless the memory "
            "resource or erasure rule is physically accounted for."
        ),
        falsification_condition=(
            "T82 fails if a fixed-size finite reversible reconciler implements "
            "componentwise monotone retained support for the T80 observation "
            "sequence without preserving old memory as garbage, consuming blank "
            "slots, or using a non-injective update."
        ),
        h7_update=(
            "H7 should remain partially supported only as a conditional "
            "constructor theorem. T82 adds that persistent reconciliation must "
            "be resource-accounted: bounded OR memory is irreversible, bounded "
            "XOR memory is reversible but nonmonotone, and append-only reversible "
            "memory shifts the arrow into blank ledger capacity."
        ),
        blocker=(
            "No physically autonomous reconciler has yet been shown to refresh "
            "or compress records indefinitely while preserving D1 monotonicity "
            "without ordinary thermodynamic irreversibility."
        ),
        recommended_next=(
            "Model a cyclic reversible reconciler with explicit garbage export "
            "or heat bath coupling, then test whether the H7 direction differs "
            "from entropy export rather than merely tracking it."
        ),
    )


def t82_result_to_dict(result: T82Result) -> dict[str, object]:
    return {
        "observations": _jsonify(result.observations),
        "raw_support_sequence": list(result.raw_support_sequence),
        "raw_support_monotone": result.raw_support_monotone,
        "policies": {
            "irreversible_or": _policy_to_dict(result.irreversible_or_policy),
            "reversible_xor": _policy_to_dict(result.reversible_xor_policy),
            "reversible_append": _policy_to_dict(result.reversible_append_policy),
            "short_append": _policy_to_dict(result.short_append_policy),
        },
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _policy_to_dict(policy: PolicyTrajectory) -> dict[str, object]:
    transition = policy.transition_map
    return {
        "name": policy.name,
        "memory_states": _jsonify(policy.memory_states),
        "support_sequence": list(policy.support_sequence),
        "novelty_sequence": list(policy.novelty_sequence),
        "monotone_support": policy.monotone_support,
        "transition_map": {
            "input_count": transition.input_count,
            "image_count": transition.image_count,
            "injective": transition.injective,
            "maximum_preimages": transition.maximum_preimages,
            "lost_bits": transition.lost_bits,
            "landauer_minimum_joules": transition.landauer_minimum_joules,
            "preimage_histogram": _jsonify(transition.preimage_histogram),
        },
        "resource_boundary": policy.resource_boundary,
        "verdict": policy.verdict,
    }


def _append_step(state: object) -> object:
    log_state, cursor, observation = state
    mutable = list(log_state)
    mutable[cursor] = observation
    return tuple(mutable), cursor + 1


def _blank_mask(width: int) -> BitMask:
    return tuple(0 for _ in range(width))


def _observation_width(observations: tuple[BitMask, ...]) -> int:
    if not observations:
        raise ValueError("at least one observation is required")
    width = len(observations[0])
    if width < 1 or any(len(observation) != width for observation in observations):
        raise ValueError("observations must be nonempty equal-width masks")
    return width


def _or_mask(left: BitMask, right: BitMask) -> BitMask:
    return tuple(a | b for a, b in zip(left, right))


def _xor_mask(left: BitMask, right: BitMask) -> BitMask:
    return tuple(a ^ b for a, b in zip(left, right))


def _log2(value: int) -> float:
    return log(value) / log(2)


def _jsonify(value: object) -> object:
    if isinstance(value, tuple):
        return [_jsonify(item) for item in value]
    return value
