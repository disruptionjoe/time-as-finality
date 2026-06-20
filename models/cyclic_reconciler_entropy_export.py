"""T84: cyclic reconciler entropy-export boundary for H7.

T82 showed that append-only reversible reconciliation gets monotone retained
records by consuming fresh blank ledger slots.  This audit closes the next
loophole: recycle a fixed-size ledger cyclically.

In the finite witness below, cyclic local memory is not monotone.  Monotone
support reappears only when overwritten records are counted in an exported
history channel, or when the overwrite is treated as erasure with positive
logical information loss.  The result weakens H7: the cyclic repair has not
separated finality direction from entropy/history export.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import log
from typing import Callable, Iterable

from models.emergence_lab import BOLTZMANN_J_PER_K, shannon_entropy
from models.persistent_reconciler_cost_boundary import (
    BitMask,
    canonical_observation_sequence,
    is_monotone,
    raw_support_sequence,
)


RingState = tuple[BitMask, ...]


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
class CyclicTrajectory:
    name: str
    capacity: int
    ring_states: tuple[RingState, ...]
    exported_slots: tuple[BitMask, ...]
    local_support_sequence: tuple[int, ...]
    export_support_sequence: tuple[int, ...]
    accounted_support_sequence: tuple[int, ...]
    local_monotone: bool
    accounted_monotone: bool
    transition_map: FiniteMapAnalysis
    recycled_steps: int
    generic_recycle_lost_bits: float
    resource_boundary: str
    verdict: str


@dataclass(frozen=True)
class T84Result:
    observations: tuple[BitMask, ...]
    raw_support_sequence: tuple[int, ...]
    raw_support_monotone: bool
    reversible_export_policy: CyclicTrajectory
    erasing_heat_bath_policy: CyclicTrajectory
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
    rounded_lost_bits = round(raw_lost_bits)
    if abs(raw_lost_bits) < 1e-12:
        lost_bits = 0.0
    elif abs(raw_lost_bits - rounded_lost_bits) < 1e-12:
        lost_bits = float(rounded_lost_bits)
    else:
        lost_bits = raw_lost_bits
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


def cyclic_reversible_export_policy(
    observations: tuple[BitMask, ...],
    capacity: int = 3,
) -> CyclicTrajectory:
    width = _observation_width(observations)
    if capacity < 1:
        raise ValueError("capacity must be positive")

    ring: RingState = tuple(_blank_mask(width) for _ in range(capacity))
    exported: list[BitMask] = []
    ring_states: list[RingState] = []
    local_support: list[int] = []
    export_support: list[int] = []
    accounted_support: list[int] = []

    for layer, observation in enumerate(observations):
        cursor = layer % capacity
        old_slot = ring[cursor]
        mutable = list(ring)
        mutable[cursor] = observation
        ring = tuple(mutable)
        exported.append(old_slot)
        ring_states.append(ring)
        local = _ring_support(ring)
        exported_total = sum(sum(slot) for slot in exported)
        local_support.append(local)
        export_support.append(exported_total)
        accounted_support.append(local + exported_total)

    transition = analyze_cyclic_export_update(capacity, width)
    recycled_steps = max(0, len(observations) - capacity)
    return CyclicTrajectory(
        name="cyclic_reversible_export",
        capacity=capacity,
        ring_states=tuple(ring_states),
        exported_slots=tuple(exported),
        local_support_sequence=tuple(local_support),
        export_support_sequence=tuple(export_support),
        accounted_support_sequence=tuple(accounted_support),
        local_monotone=is_monotone(tuple(local_support)),
        accounted_monotone=is_monotone(tuple(accounted_support)),
        transition_map=transition,
        recycled_steps=recycled_steps,
        generic_recycle_lost_bits=0.0,
        resource_boundary=(
            "The fixed ring is reversible only because each overwritten slot is "
            "exported as external history; local ring support itself is not "
            "monotone."
        ),
        verdict=(
            "H7 monotonicity is recovered only if exported garbage/history is "
            "counted as retained finality."
        ),
    )


def cyclic_erasing_heat_bath_policy(
    observations: tuple[BitMask, ...],
    capacity: int = 3,
) -> CyclicTrajectory:
    width = _observation_width(observations)
    if capacity < 1:
        raise ValueError("capacity must be positive")

    ring: RingState = tuple(_blank_mask(width) for _ in range(capacity))
    erased: list[BitMask] = []
    ring_states: list[RingState] = []
    local_support: list[int] = []
    erased_support: list[int] = []
    accounted_support: list[int] = []

    for layer, observation in enumerate(observations):
        cursor = layer % capacity
        old_slot = ring[cursor]
        mutable = list(ring)
        mutable[cursor] = observation
        ring = tuple(mutable)
        erased.append(old_slot)
        ring_states.append(ring)
        local = _ring_support(ring)
        erased_total = sum(sum(slot) for slot in erased)
        local_support.append(local)
        erased_support.append(erased_total)
        accounted_support.append(local + erased_total)

    transition = analyze_cyclic_erasing_update(capacity, width)
    recycled_steps = max(0, len(observations) - capacity)
    return CyclicTrajectory(
        name="cyclic_erasing_heat_bath",
        capacity=capacity,
        ring_states=tuple(ring_states),
        exported_slots=tuple(erased),
        local_support_sequence=tuple(local_support),
        export_support_sequence=tuple(erased_support),
        accounted_support_sequence=tuple(accounted_support),
        local_monotone=is_monotone(tuple(local_support)),
        accounted_monotone=is_monotone(tuple(accounted_support)),
        transition_map=transition,
        recycled_steps=recycled_steps,
        generic_recycle_lost_bits=transition.lost_bits * recycled_steps,
        resource_boundary=(
            "The fixed ring can be recycled only by discarding the overwritten "
            "slot; the generic finite update loses the overwritten slot bits."
        ),
        verdict=(
            "Counting erased support restores the same monotone accounting "
            "curve, but no longer as accessible record memory; it is ordinary "
            "erasure/heat-bath bookkeeping."
        ),
    )


def analyze_cyclic_export_update(capacity: int, width: int) -> FiniteMapAnalysis:
    inputs = _cyclic_inputs(capacity, width)
    return analyze_finite_map(inputs, _export_step)


def analyze_cyclic_erasing_update(capacity: int, width: int) -> FiniteMapAnalysis:
    inputs = _cyclic_inputs(capacity, width)
    return analyze_finite_map(inputs, _erasing_step)


def run_t84_analysis(capacity: int = 3, layers: int = 5) -> T84Result:
    observations = canonical_observation_sequence(layers=layers)
    raw = raw_support_sequence(observations)
    export_policy = cyclic_reversible_export_policy(observations, capacity)
    erasing_policy = cyclic_erasing_heat_bath_policy(observations, capacity)
    return T84Result(
        observations=observations,
        raw_support_sequence=raw,
        raw_support_monotone=is_monotone(raw),
        reversible_export_policy=export_policy,
        erasing_heat_bath_policy=erasing_policy,
        strongest_claim=(
            "In the T80 observation witness, a fixed-size cyclic reconciler "
            "does not produce monotone local retained records. Monotonicity "
            "returns only when overwritten slots are exported as history or "
            "discarded through an erasing heat-bath channel."
        ),
        weakened_claim=(
            "H7's physical-arrow reading is weakened: cyclic persistence has "
            "not been separated from ordinary entropy/history export."
        ),
        falsification_condition=(
            "T84 fails if a fixed-capacity cyclic reconciler gives monotone "
            "local retained-record support for the T80 sequence while remaining "
            "injective and without exporting overwritten slots, erasing them, "
            "or hiding them in inaccessible garbage."
        ),
        h7_update=(
            "H7 should remain partially supported only as a conditional "
            "constructor theorem. T84 adds that cyclic reconciliation restores "
            "monotonicity only by moving old records into an exported history "
            "channel or by paying erasure cost; the autonomous local memory "
            "does not supply an independent arrow."
        ),
        blocker=(
            "No cyclic finite observer has yet produced D1-monotone local "
            "records under reversible dynamics without an explicit export, "
            "garbage, or heat-bath account."
        ),
        recommended_next=(
            "Try a logically reversible compression/export model with a "
            "bounded entropy sink and ask whether any nontrivial D1 monotone "
            "survives after the sink is included in the state space."
        ),
    )


def t84_result_to_dict(result: T84Result) -> dict[str, object]:
    return {
        "observations": _jsonify(result.observations),
        "raw_support_sequence": list(result.raw_support_sequence),
        "raw_support_monotone": result.raw_support_monotone,
        "policies": {
            "reversible_export": _trajectory_to_dict(
                result.reversible_export_policy
            ),
            "erasing_heat_bath": _trajectory_to_dict(
                result.erasing_heat_bath_policy
            ),
        },
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _trajectory_to_dict(trajectory: CyclicTrajectory) -> dict[str, object]:
    transition = trajectory.transition_map
    return {
        "name": trajectory.name,
        "capacity": trajectory.capacity,
        "ring_states": _jsonify(trajectory.ring_states),
        "exported_slots": _jsonify(trajectory.exported_slots),
        "local_support_sequence": list(trajectory.local_support_sequence),
        "export_support_sequence": list(trajectory.export_support_sequence),
        "accounted_support_sequence": list(trajectory.accounted_support_sequence),
        "local_monotone": trajectory.local_monotone,
        "accounted_monotone": trajectory.accounted_monotone,
        "transition_map": {
            "input_count": transition.input_count,
            "image_count": transition.image_count,
            "injective": transition.injective,
            "maximum_preimages": transition.maximum_preimages,
            "lost_bits": transition.lost_bits,
            "landauer_minimum_joules": transition.landauer_minimum_joules,
            "preimage_histogram": _jsonify(transition.preimage_histogram),
        },
        "recycled_steps": trajectory.recycled_steps,
        "generic_recycle_lost_bits": trajectory.generic_recycle_lost_bits,
        "resource_boundary": trajectory.resource_boundary,
        "verdict": trajectory.verdict,
    }


def _cyclic_inputs(capacity: int, width: int) -> tuple[object, ...]:
    if capacity < 1:
        raise ValueError("capacity must be positive")
    states = bitstrings(width)
    rings = product(states, repeat=capacity)
    return tuple(
        (tuple(ring), cursor, observation)
        for ring in rings
        for cursor in range(capacity)
        for observation in states
    )


def _export_step(state: object) -> object:
    ring, cursor, observation = state
    old_slot = ring[cursor]
    mutable = list(ring)
    mutable[cursor] = observation
    return tuple(mutable), (cursor + 1) % len(ring), observation, old_slot


def _erasing_step(state: object) -> object:
    ring, cursor, observation = state
    mutable = list(ring)
    mutable[cursor] = observation
    return tuple(mutable), (cursor + 1) % len(ring), observation


def _ring_support(ring: RingState) -> int:
    return sum(sum(slot) for slot in ring)


def _blank_mask(width: int) -> BitMask:
    return tuple(0 for _ in range(width))


def _observation_width(observations: tuple[BitMask, ...]) -> int:
    if not observations:
        raise ValueError("at least one observation is required")
    width = len(observations[0])
    if width < 1 or any(len(observation) != width for observation in observations):
        raise ValueError("observations must be nonempty equal-width masks")
    return width


def _log2(value: int) -> float:
    return log(value) / log(2)


def _jsonify(value: object) -> object:
    if isinstance(value, tuple):
        return [_jsonify(item) for item in value]
    return value
