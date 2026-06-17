"""T16: dynamically generated phase-bearing record traces.

T13-T15 assign signed readout weights by hand.  T16 derives signed weights
from local dynamics: a generated trace cell receives +1 when a seed
perturbation changes a terminal bit from 0 to 1, and -1 when it changes a
terminal bit from 1 to 0.  The finality profile remains phase-blind.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from models.emergence_lab import ElementaryCA, State, int_to_bits, periodic_components
from models.t1_record_graph import Observer, Record
from models.t13_signed_readout import ReadoutRecordGraph


@dataclass(frozen=True)
class SignedTraceRecord:
    index: int
    baseline_bit: int
    counterfactual_bit: int
    weight: int


@dataclass(frozen=True)
class DynamicPhaseWitness:
    rule: int
    width: int
    layers: int
    initial: State
    seed_index: int
    records: tuple[SignedTraceRecord, ...]
    profile: tuple[int, int, int, int]
    readout: float

    @property
    def weights(self) -> tuple[int, ...]:
        return tuple(record.weight for record in self.records)


@dataclass(frozen=True)
class ProfileSeparationWitness:
    left: DynamicPhaseWitness
    right: DynamicPhaseWitness


@dataclass(frozen=True)
class DynamicTrajectoryWitness:
    rule: int
    width: int
    initial: State
    seed_index: int
    layers: tuple[int, ...]
    profiles: tuple[tuple[int, int, int, int], ...]
    readouts: tuple[float, ...]
    weights_by_layer: tuple[tuple[int, ...], ...]


def signed_trace_records(
    ca: ElementaryCA,
    initial: State,
    seed_index: int,
    layers: int,
    observer_indices: tuple[int, ...] | None = None,
) -> tuple[SignedTraceRecord, ...]:
    baseline = ca.run(initial, layers)[-1]
    changed = list(initial)
    changed[seed_index] ^= 1
    counterfactual = ca.run(tuple(changed), layers)[-1]
    indices = tuple(range(ca.width)) if observer_indices is None else observer_indices
    records = []
    for index in indices:
        if baseline[index] == counterfactual[index]:
            continue
        weight = 1 if baseline[index] == 0 and counterfactual[index] == 1 else -1
        records.append(
            SignedTraceRecord(
                index=index,
                baseline_bit=baseline[index],
                counterfactual_bit=counterfactual[index],
                weight=weight,
            )
        )
    return tuple(records)


def _profile(records: tuple[SignedTraceRecord, ...], width: int) -> tuple[int, int, int, int]:
    support = len(records)
    indices = tuple(record.index for record in records)
    return (
        support,
        support,
        periodic_components(indices, width),
        support,
    )


def _readout(records: tuple[SignedTraceRecord, ...]) -> float:
    return float(abs(sum(record.weight for record in records)) ** 2)


def build_readout_graph(
    witness: DynamicPhaseWitness,
) -> tuple[ReadoutRecordGraph, Observer]:
    graph = ReadoutRecordGraph()
    for event in ("trace", "observe"):
        graph.add_event(event)
    graph.add_causal_edge("trace", "observe")
    for position, record in enumerate(witness.records):
        graph.add_weighted_record(
            Record(
                f"r{position}",
                "X",
                "true",
                "trace",
                f"h{record.index}",
                1.0,
            ),
            record.weight,
        )
    observer = Observer(
        "O_dynamic",
        "observe",
        frozenset(f"h{record.index}" for record in witness.records),
    )
    return graph, observer


def make_witness(
    rule: int,
    width: int,
    initial: State,
    seed_index: int,
    layers: int,
) -> DynamicPhaseWitness | None:
    ca = ElementaryCA(rule, width)
    records = signed_trace_records(ca, initial, seed_index, layers)
    if not records:
        return None
    return DynamicPhaseWitness(
        rule=rule,
        width=width,
        layers=layers,
        initial=initial,
        seed_index=seed_index,
        records=records,
        profile=_profile(records, width),
        readout=_readout(records),
    )


def find_profile_separation_witness(
    *,
    width: int = 4,
    max_layers: int = 3,
) -> ProfileSeparationWitness:
    by_profile: dict[tuple[int, int, int, int], list[DynamicPhaseWitness]] = {}
    for rule in range(256):
        for layers in range(1, max_layers + 1):
            for initial_value in range(2**width):
                initial = int_to_bits(initial_value, width)
                for seed_index in range(width):
                    witness = make_witness(rule, width, initial, seed_index, layers)
                    if witness is None:
                        continue
                    bucket = by_profile.setdefault(witness.profile, [])
                    for existing in bucket:
                        if existing.readout != witness.readout:
                            return ProfileSeparationWitness(existing, witness)
                    bucket.append(witness)
    raise AssertionError("no profile/readout separation witness found")


def find_cancellation_trajectory(
    *,
    width: int = 4,
    max_layers: int = 6,
) -> DynamicTrajectoryWitness:
    for rule in range(256):
        ca = ElementaryCA(rule, width)
        for initial_value in range(2**width):
            initial = int_to_bits(initial_value, width)
            for seed_index in range(width):
                profiles = []
                readouts = []
                weights_by_layer = []
                valid_layers = []
                for layers in range(1, max_layers + 1):
                    records = signed_trace_records(ca, initial, seed_index, layers)
                    if not records:
                        continue
                    valid_layers.append(layers)
                    profiles.append(_profile(records, width))
                    readouts.append(_readout(records))
                    weights_by_layer.append(tuple(record.weight for record in records))
                if len(readouts) < 3:
                    continue
                for i, j, k in combinations(range(len(readouts)), 3):
                    if readouts[i] > 0.0 and readouts[j] == 0.0 and readouts[k] > 0.0:
                        return DynamicTrajectoryWitness(
                            rule=rule,
                            width=width,
                            initial=initial,
                            seed_index=seed_index,
                            layers=tuple(valid_layers),
                            profiles=tuple(profiles),
                            readouts=tuple(readouts),
                            weights_by_layer=tuple(weights_by_layer),
                        )
    raise AssertionError("no cancellation trajectory found")


def sweep_dynamic_phase_records(
    *,
    width: int = 4,
    max_layers: int = 3,
) -> dict[str, object]:
    total = 0
    nonempty = 0
    mixed_sign = 0
    cancellation = 0
    profile_readout_pairs: dict[tuple[int, int, int, int], set[float]] = {}
    for rule in range(256):
        ca = ElementaryCA(rule, width)
        for layers in range(1, max_layers + 1):
            for initial_value in range(2**width):
                initial = int_to_bits(initial_value, width)
                for seed_index in range(width):
                    total += 1
                    records = signed_trace_records(ca, initial, seed_index, layers)
                    if not records:
                        continue
                    nonempty += 1
                    weights = tuple(record.weight for record in records)
                    mixed_sign += any(weight > 0 for weight in weights) and any(
                        weight < 0 for weight in weights
                    )
                    cancellation += sum(weights) == 0
                    profile_readout_pairs.setdefault(_profile(records, width), set()).add(
                        _readout(records)
                    )
    separating_profiles = {
        profile: readouts
        for profile, readouts in profile_readout_pairs.items()
        if len(readouts) > 1
    }
    return {
        "width": width,
        "max_layers": max_layers,
        "cases": total,
        "nonempty_trace_cases": nonempty,
        "mixed_sign_fraction": mixed_sign / nonempty,
        "zero_readout_fraction": cancellation / nonempty,
        "profile_count": len(profile_readout_pairs),
        "separating_profile_count": len(separating_profiles),
        "profiles_with_multiple_readouts_fraction": len(separating_profiles)
        / len(profile_readout_pairs),
    }


def _witness_summary(witness: DynamicPhaseWitness) -> dict[str, object]:
    return {
        "rule": witness.rule,
        "width": witness.width,
        "layers": witness.layers,
        "initial": "".join(str(bit) for bit in witness.initial),
        "seed_index": witness.seed_index,
        "weights": witness.weights,
        "profile": witness.profile,
        "readout": witness.readout,
    }


def run_t16_analysis() -> dict[str, object]:
    separation = find_profile_separation_witness()
    trajectory = find_cancellation_trajectory()
    return {
        "derivation_rule": "weight is +1 for terminal 0->1 trace cells and -1 for terminal 1->0 trace cells",
        "sweep": sweep_dynamic_phase_records(),
        "profile_separation_witness": {
            "left": _witness_summary(separation.left),
            "right": _witness_summary(separation.right),
        },
        "cancellation_trajectory": {
            "rule": trajectory.rule,
            "width": trajectory.width,
            "initial": "".join(str(bit) for bit in trajectory.initial),
            "seed_index": trajectory.seed_index,
            "layers": trajectory.layers,
            "profiles": trajectory.profiles,
            "readouts": trajectory.readouts,
            "weights_by_layer": trajectory.weights_by_layer,
        },
        "verdict": {
            "phase_weights_are_dynamically_derived": True,
            "finality_profile_remains_phase_blind": True,
            "profile_does_not_determine_dynamical_signed_readout": True,
            "zero_readout_can_arise_from_generated_cancellation": True,
            "does_not_derive_quantum_mechanics": True,
        },
    }
