"""T106: bounded-sink reversible-compression obstruction for H7.

T84 left a narrow loophole: perhaps a cyclic reconciler could use reversible
compression plus a bounded entropy sink to keep monotone finality without
unbounded history or erasure.  This audit closes that loophole in the finite
T80/T84 witness family.

The result is negative for H7's physical-arrow reading.  Orderless compression
of overwritten slots is non-injective.  Ordered lossless export is reversible
only by consuming sink capacity.  If the bounded sink is included in the state
space and the cycle is closed by reversible unwinding, the apparent monotone
decreases on the return path.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import log
from typing import Callable, Iterable

from models.cyclic_reconciler_entropy_export import cyclic_reversible_export_policy
from models.emergence_lab import BOLTZMANN_J_PER_K, shannon_entropy
from models.persistent_reconciler_cost_boundary import (
    BitMask,
    canonical_observation_sequence,
    is_monotone,
)


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
class RLEBlock:
    slot: BitMask
    count: int


@dataclass(frozen=True)
class RLECapacityAudit:
    capacity_blocks: int
    final_blocks: tuple[RLEBlock, ...]
    required_blocks: int
    block_count_sequence: tuple[int, ...]
    reconstructed_support_sequence: tuple[int, ...]
    admissible_for_sequence: bool
    first_exhausted_export_index: int | None
    verdict: str


@dataclass(frozen=True)
class CompressionMapAudit:
    ordered_stack_map: FiniteMapAnalysis
    orderless_counter_map: FiniteMapAnalysis
    verdict: str


@dataclass(frozen=True)
class ClosedCycleAudit:
    forward_accounted_support: tuple[int, ...]
    full_cycle_accounted_support: tuple[int, ...]
    forward_rle_block_count: tuple[int, ...]
    full_cycle_rle_block_count: tuple[int, ...]
    forward_accounted_monotone: bool
    full_cycle_accounted_monotone: bool
    forward_block_count_monotone: bool
    full_cycle_block_count_monotone: bool
    strict_cycle_monotone_possible: bool
    verdict: str


@dataclass(frozen=True)
class T106Result:
    observations: tuple[BitMask, ...]
    exported_slots: tuple[BitMask, ...]
    local_ring_support: tuple[int, ...]
    exported_support: tuple[int, ...]
    accounted_support: tuple[int, ...]
    bounded_rle_capacity_audit: RLECapacityAudit
    exact_rle_capacity_audit: RLECapacityAudit
    compression_map_audit: CompressionMapAudit
    closed_cycle_audit: ClosedCycleAudit
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
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


def run_length_encode(slots: tuple[BitMask, ...]) -> tuple[RLEBlock, ...]:
    blocks: list[RLEBlock] = []
    for slot in slots:
        if blocks and blocks[-1].slot == slot:
            last = blocks[-1]
            blocks[-1] = RLEBlock(slot=last.slot, count=last.count + 1)
        else:
            blocks.append(RLEBlock(slot=slot, count=1))
    return tuple(blocks)


def rle_block_count_sequence(slots: tuple[BitMask, ...]) -> tuple[int, ...]:
    return tuple(len(run_length_encode(slots[: index + 1])) for index in range(len(slots)))


def reconstructed_export_support_sequence(slots: tuple[BitMask, ...]) -> tuple[int, ...]:
    total = 0
    sequence: list[int] = []
    for slot in slots:
        total += sum(slot)
        sequence.append(total)
    return tuple(sequence)


def rle_capacity_audit(
    exported_slots: tuple[BitMask, ...],
    capacity_blocks: int,
) -> RLECapacityAudit:
    if capacity_blocks < 1:
        raise ValueError("capacity_blocks must be positive")

    final_blocks = run_length_encode(exported_slots)
    block_counts = rle_block_count_sequence(exported_slots)
    first_exhausted = next(
        (index for index, count in enumerate(block_counts) if count > capacity_blocks),
        None,
    )
    admissible = first_exhausted is None
    if admissible:
        verdict = (
            "The RLE sink can encode this finite export history, but only as a "
            "bounded finite resource sized for the sequence."
        )
    else:
        verdict = (
            "The RLE sink exhausts before the finite export history is fully "
            "encoded; compression does not supply an autonomous arrow."
        )
    return RLECapacityAudit(
        capacity_blocks=capacity_blocks,
        final_blocks=final_blocks,
        required_blocks=len(final_blocks),
        block_count_sequence=block_counts,
        reconstructed_support_sequence=reconstructed_export_support_sequence(exported_slots),
        admissible_for_sequence=admissible,
        first_exhausted_export_index=first_exhausted,
        verdict=verdict,
    )


def analyze_ordered_stack_export(horizon: int, width: int) -> FiniteMapAnalysis:
    if horizon < 1:
        raise ValueError("horizon must be positive")
    symbols = bitstrings(width)
    blank = _blank_mask(width)
    inputs = []
    for cursor in range(horizon):
        for prefix in product(symbols, repeat=cursor):
            sink = tuple(prefix) + tuple(blank for _ in range(horizon - cursor))
            for old_slot in symbols:
                inputs.append((sink, cursor, old_slot))
    return analyze_finite_map(inputs, _ordered_stack_step)


def analyze_orderless_counter_compression(
    max_total_count: int,
    width: int,
) -> FiniteMapAnalysis:
    if max_total_count < 1:
        raise ValueError("max_total_count must be positive")
    symbols = bitstrings(width)
    counts = _bounded_count_states(len(symbols), max_total_count)
    inputs = tuple(
        (count_state, symbol_index)
        for count_state in counts
        if sum(count_state) < max_total_count
        for symbol_index in range(len(symbols))
    )
    return analyze_finite_map(inputs, _orderless_counter_step)


def compression_map_audit(horizon: int, width: int) -> CompressionMapAudit:
    ordered = analyze_ordered_stack_export(horizon, width)
    orderless = analyze_orderless_counter_compression(max_total_count=horizon, width=width)
    return CompressionMapAudit(
        ordered_stack_map=ordered,
        orderless_counter_map=orderless,
        verdict=(
            "Ordered lossless export is injective because it stores the "
            "overwritten slot in a blank sink position. Orderless count "
            "compression is non-injective; it merges distinct histories unless "
            "extra side information is retained, which recreates an ordered "
            "history resource."
        ),
    )


def closed_cycle_audit(
    accounted_support: tuple[int, ...],
    block_count_sequence: tuple[int, ...],
) -> ClosedCycleAudit:
    forward_accounted = (0,) + accounted_support
    full_accounted = forward_accounted + tuple(reversed(forward_accounted[:-1]))
    forward_blocks = (0,) + block_count_sequence
    full_blocks = forward_blocks + tuple(reversed(forward_blocks[:-1]))
    strict_cycle_possible = not (
        full_accounted[0] == full_accounted[-1]
        and max(full_accounted) > full_accounted[0]
    )
    return ClosedCycleAudit(
        forward_accounted_support=forward_accounted,
        full_cycle_accounted_support=full_accounted,
        forward_rle_block_count=forward_blocks,
        full_cycle_rle_block_count=full_blocks,
        forward_accounted_monotone=is_monotone(forward_accounted),
        full_cycle_accounted_monotone=is_monotone(full_accounted),
        forward_block_count_monotone=is_monotone(forward_blocks),
        full_cycle_block_count_monotone=is_monotone(full_blocks),
        strict_cycle_monotone_possible=strict_cycle_possible,
        verdict=(
            "The forward branch has monotone accounting, but the closed "
            "bounded reversible cycle does not. On a finite cycle, any scalar "
            "that is nondecreasing on every reversible edge must be constant "
            "around the cycle, so a strict finality arrow cannot live in the "
            "closed bounded state space."
        ),
    )


def run_t106_analysis(
    layers: int = 5,
    ring_capacity: int = 3,
    undersized_rle_blocks: int = 3,
) -> T106Result:
    observations = canonical_observation_sequence(layers=layers)
    trajectory = cyclic_reversible_export_policy(observations, capacity=ring_capacity)
    exported_slots = trajectory.exported_slots
    width = _observation_width(observations)

    bounded_rle = rle_capacity_audit(exported_slots, capacity_blocks=undersized_rle_blocks)
    exact_rle = rle_capacity_audit(
        exported_slots,
        capacity_blocks=bounded_rle.required_blocks,
    )
    maps = compression_map_audit(horizon=len(exported_slots), width=width)
    cycle = closed_cycle_audit(
        accounted_support=trajectory.accounted_support_sequence,
        block_count_sequence=bounded_rle.block_count_sequence,
    )
    return T106Result(
        observations=observations,
        exported_slots=exported_slots,
        local_ring_support=trajectory.local_support_sequence,
        exported_support=trajectory.export_support_sequence,
        accounted_support=trajectory.accounted_support_sequence,
        bounded_rle_capacity_audit=bounded_rle,
        exact_rle_capacity_audit=exact_rle,
        compression_map_audit=maps,
        closed_cycle_audit=cycle,
        strongest_claim=(
            "For the T80/T84 witness, reversible compression with a bounded "
            "sink does not rescue H7. Orderless compression is non-injective; "
            "ordered lossless export is reversible only while consuming blank "
            "sink capacity; and when the bounded sink is included and the "
            "cycle is closed, the apparent monotone decreases on the reversible "
            "return path."
        ),
        improved=(
            "T106 converts the T84 next-step loophole into a finite obstruction: "
            "the relevant distinction is not raw versus compressed storage, but "
            "whether the overwritten records remain reconstructable in the "
            "state space, are erased, or are hidden in an excluded environment."
        ),
        weakened=(
            "This further weakens H7 as a physical-arrow claim. The tested "
            "bounded reversible sink supplies at most a forward-branch "
            "resource accounting curve, not an autonomous finality direction "
            "after all degrees of freedom are included."
        ),
        falsification_condition=(
            "T106 fails if a finite bounded reversible compressor over the same "
            "T80 exported-slot family gives a strict D1-relevant monotone on "
            "the closed full state space without erasure, excluded history, "
            "fresh blank capacity, or a hidden side channel."
        ),
        h7_update=(
            "H7 should remain only a conditional constructor theorem. T106 adds "
            "that bounded reversible compression/export does not separate the "
            "finality direction from resource accounting: a strict monotone "
            "appears only on an open forward branch or after excluding the sink "
            "return path from the state."
        ),
        claim_ledger_update=(
            "Add T106 to H7: bounded reversible compression does not rescue the "
            "physical-arrow reading. Orderless compression is non-injective, "
            "ordered export consumes sink capacity, and the closed bounded "
            "cycle has no nontrivial strict monotone once the sink is included."
        ),
        open_blocker=(
            "No finite closed reversible observer model has produced a strict "
            "D1-relevant monotone after including the memory, compression sink, "
            "and return/unwind degrees of freedom."
        ),
        recommended_next=(
            "Either formalize this as a general finite-permutation obstruction "
            "for H7, or look for an open-system thermodynamic model where H7's "
            "remaining content is explicitly the observer-indexed coarse "
            "graining rather than a new arrow of time."
        ),
    )


def t106_result_to_dict(result: T106Result) -> dict[str, object]:
    return {
        "observations": _jsonify(result.observations),
        "exported_slots": _jsonify(result.exported_slots),
        "local_ring_support": list(result.local_ring_support),
        "exported_support": list(result.exported_support),
        "accounted_support": list(result.accounted_support),
        "bounded_rle_capacity_audit": _rle_audit_to_dict(
            result.bounded_rle_capacity_audit
        ),
        "exact_rle_capacity_audit": _rle_audit_to_dict(
            result.exact_rle_capacity_audit
        ),
        "compression_map_audit": {
            "ordered_stack_map": _finite_map_to_dict(
                result.compression_map_audit.ordered_stack_map
            ),
            "orderless_counter_map": _finite_map_to_dict(
                result.compression_map_audit.orderless_counter_map
            ),
            "verdict": result.compression_map_audit.verdict,
        },
        "closed_cycle_audit": {
            "forward_accounted_support": list(
                result.closed_cycle_audit.forward_accounted_support
            ),
            "full_cycle_accounted_support": list(
                result.closed_cycle_audit.full_cycle_accounted_support
            ),
            "forward_rle_block_count": list(
                result.closed_cycle_audit.forward_rle_block_count
            ),
            "full_cycle_rle_block_count": list(
                result.closed_cycle_audit.full_cycle_rle_block_count
            ),
            "forward_accounted_monotone": (
                result.closed_cycle_audit.forward_accounted_monotone
            ),
            "full_cycle_accounted_monotone": (
                result.closed_cycle_audit.full_cycle_accounted_monotone
            ),
            "forward_block_count_monotone": (
                result.closed_cycle_audit.forward_block_count_monotone
            ),
            "full_cycle_block_count_monotone": (
                result.closed_cycle_audit.full_cycle_block_count_monotone
            ),
            "strict_cycle_monotone_possible": (
                result.closed_cycle_audit.strict_cycle_monotone_possible
            ),
            "verdict": result.closed_cycle_audit.verdict,
        },
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _ordered_stack_step(state: object) -> object:
    sink, cursor, old_slot = state
    mutable = list(sink)
    mutable[cursor] = old_slot
    return tuple(mutable), cursor + 1


def _orderless_counter_step(state: object) -> object:
    counts, symbol_index = state
    mutable = list(counts)
    mutable[symbol_index] += 1
    return tuple(mutable)


def _bounded_count_states(
    symbol_count: int,
    max_total_count: int,
) -> tuple[tuple[int, ...], ...]:
    states: list[tuple[int, ...]] = []

    def visit(prefix: tuple[int, ...], remaining_symbols: int, remaining_total: int) -> None:
        if remaining_symbols == 0:
            states.append(prefix)
            return
        for count in range(remaining_total + 1):
            visit(prefix + (count,), remaining_symbols - 1, remaining_total - count)

    visit((), symbol_count, max_total_count)
    return tuple(states)


def _rle_audit_to_dict(audit: RLECapacityAudit) -> dict[str, object]:
    return {
        "capacity_blocks": audit.capacity_blocks,
        "final_blocks": [
            {"slot": list(block.slot), "count": block.count}
            for block in audit.final_blocks
        ],
        "required_blocks": audit.required_blocks,
        "block_count_sequence": list(audit.block_count_sequence),
        "reconstructed_support_sequence": list(audit.reconstructed_support_sequence),
        "admissible_for_sequence": audit.admissible_for_sequence,
        "first_exhausted_export_index": audit.first_exhausted_export_index,
        "verdict": audit.verdict,
    }


def _finite_map_to_dict(analysis: FiniteMapAnalysis) -> dict[str, object]:
    return {
        "input_count": analysis.input_count,
        "image_count": analysis.image_count,
        "injective": analysis.injective,
        "maximum_preimages": analysis.maximum_preimages,
        "lost_bits": analysis.lost_bits,
        "landauer_minimum_joules": analysis.landauer_minimum_joules,
        "preimage_histogram": _jsonify(analysis.preimage_histogram),
    }


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
