"""Comparative local-dynamics laboratory for emergent record finality."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from math import log2, log
from typing import Iterable, Protocol


BOLTZMANN_J_PER_K = 1.380649e-23


State = tuple[int, ...]
SecondOrderState = tuple[State, State]


def int_to_bits(value: int, width: int) -> State:
    return tuple((value >> shift) & 1 for shift in range(width - 1, -1, -1))


def bits_to_int(bits: State) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def xor_states(left: State, right: State) -> State:
    return tuple(a ^ b for a, b in zip(left, right))


def hamming_distance(left: State, right: State) -> int:
    return sum(a != b for a, b in zip(left, right))


def flip_bit(state: State, index: int) -> State:
    changed = list(state)
    changed[index] ^= 1
    return tuple(changed)


@dataclass(frozen=True)
class EmergentFinalityProfile:
    accessible_support: int
    spatial_redundancy: int
    independent_terminal_branches: int
    terminal_intervention_cost: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.spatial_redundancy,
            self.independent_terminal_branches,
            self.terminal_intervention_cost,
        )

    def no_more_final_than(self, other: "EmergentFinalityProfile") -> bool:
        return all(a <= b for a, b in zip(self.as_tuple(), other.as_tuple()))


@dataclass(frozen=True)
class TransitionMapAnalysis:
    state_count: int
    image_count: int
    injective: bool
    mean_preimages_per_image: float
    maximum_preimages: int
    lost_bits: float
    landauer_minimum_joules: float
    preimage_histogram: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class PreimageSearch:
    target: object
    preimages: tuple[object, ...]
    candidates_examined: int
    first_match_at: int | None

    @property
    def unique(self) -> bool:
        return len(self.preimages) == 1


@dataclass(frozen=True)
class TraceAnalysis:
    baseline_terminal: State
    counterfactual_terminal: State
    trace_mask: State
    observer_indices: tuple[int, ...]
    profile: EmergentFinalityProfile


@dataclass(frozen=True)
class RuleSweepResult:
    rule: int
    injective: bool
    lost_bits: float
    trace_survival_fraction: float
    observer_divergence_fraction: float


@dataclass(frozen=True)
class RuleSweepSummary:
    width: int
    layers: int
    rule_count: int
    injective_rule_count: int
    mean_lost_bits: float
    mean_trace_survival_fraction: float
    lost_bits_trace_survival_correlation: float
    same_loss_different_survival: tuple[int, int] | None
    same_survival_different_loss: tuple[int, int] | None
    reversible_lifts_all_injective: bool
    results: tuple[RuleSweepResult, ...]


class FiniteSubstrate(Protocol):
    width: int

    def states(self) -> Iterable[object]:
        ...

    def step(self, state: object) -> object:
        ...


class ElementaryCA:
    def __init__(self, rule: int, width: int) -> None:
        if not 0 <= rule <= 255:
            raise ValueError("elementary CA rule must be in [0, 255]")
        if width < 1:
            raise ValueError("width must be positive")
        self.rule = rule
        self.width = width

    def states(self) -> Iterable[State]:
        for value in range(2**self.width):
            yield int_to_bits(value, self.width)

    def local_update(self, left: int, center: int, right: int) -> int:
        neighborhood = (left << 2) | (center << 1) | right
        return (self.rule >> neighborhood) & 1

    def step(self, state: State) -> State:
        if len(state) != self.width:
            raise ValueError("state width mismatch")
        return tuple(
            self.local_update(
                state[(index - 1) % self.width],
                state[index],
                state[(index + 1) % self.width],
            )
            for index in range(self.width)
        )

    def run(self, initial: State, layers: int) -> tuple[State, ...]:
        history = [initial]
        for _ in range(layers):
            history.append(self.step(history[-1]))
        return tuple(history)

    def actual_parent_offsets(self, state: State, index: int) -> tuple[int, ...]:
        offsets = []
        baseline = self.step(state)[index]
        for offset in (-1, 0, 1):
            changed = flip_bit(state, (index + offset) % self.width)
            if self.step(changed)[index] != baseline:
                offsets.append(offset)
        return tuple(offsets)


class SecondOrderCA:
    """Reversible second-order lift of an elementary CA."""

    def __init__(self, base: ElementaryCA) -> None:
        self.base = base
        self.width = base.width

    def states(self) -> Iterable[SecondOrderState]:
        states = tuple(self.base.states())
        return product(states, repeat=2)

    def step(self, state: SecondOrderState) -> SecondOrderState:
        previous, current = state
        return current, xor_states(self.base.step(current), previous)

    def inverse_step(self, state: SecondOrderState) -> SecondOrderState:
        current, next_state = state
        previous = xor_states(self.base.step(current), next_state)
        return previous, current

    def run(self, initial: SecondOrderState, layers: int) -> tuple[SecondOrderState, ...]:
        history = [initial]
        for _ in range(layers):
            history.append(self.step(history[-1]))
        return tuple(history)


def shannon_entropy(probabilities: Iterable[float]) -> float:
    return -sum(probability * log2(probability) for probability in probabilities if probability)


def analyze_transition_map(
    substrate: FiniteSubstrate,
    temperature_kelvin: float = 300.0,
) -> TransitionMapAnalysis:
    if temperature_kelvin <= 0:
        raise ValueError("temperature must be positive")
    states = tuple(substrate.states())
    preimages: dict[object, list[object]] = defaultdict(list)
    for state in states:
        preimages[substrate.step(state)].append(state)
    counts = Counter(len(items) for items in preimages.values())
    output_probabilities = [len(items) / len(states) for items in preimages.values()]
    input_entropy = log2(len(states))
    output_entropy = shannon_entropy(output_probabilities)
    lost_bits = input_entropy - output_entropy
    return TransitionMapAnalysis(
        state_count=len(states),
        image_count=len(preimages),
        injective=len(preimages) == len(states) and all(len(items) == 1 for items in preimages.values()),
        mean_preimages_per_image=len(states) / len(preimages),
        maximum_preimages=max(len(items) for items in preimages.values()),
        lost_bits=lost_bits,
        landauer_minimum_joules=BOLTZMANN_J_PER_K
        * temperature_kelvin
        * log(2)
        * lost_bits,
        preimage_histogram=tuple(sorted(counts.items())),
    )


def exhaustive_preimage_search(substrate: FiniteSubstrate, target: object) -> PreimageSearch:
    candidates = tuple(substrate.states())
    found = []
    first_match_at = None
    for index, candidate in enumerate(candidates, start=1):
        if substrate.step(candidate) == target:
            found.append(candidate)
            if first_match_at is None:
                first_match_at = index
    return PreimageSearch(target, tuple(found), len(candidates), first_match_at)


def periodic_components(indices: Iterable[int], width: int) -> int:
    selected = set(indices)
    if not selected:
        return 0
    if len(selected) == width:
        return 1
    components = 0
    for index in selected:
        if (index - 1) % width not in selected:
            components += 1
    return components


def observer_windows(width: int, window_width: int) -> tuple[tuple[int, ...], ...]:
    if not 1 <= window_width <= width:
        raise ValueError("observer window width must be in [1, width]")
    return tuple(
        tuple((start + offset) % width for offset in range(window_width))
        for start in range(width)
    )


def analyze_eca_trace(
    ca: ElementaryCA,
    initial: State,
    seed_index: int,
    layers: int,
    observer_indices: Iterable[int] | None = None,
) -> TraceAnalysis:
    baseline = ca.run(initial, layers)[-1]
    counterfactual = ca.run(flip_bit(initial, seed_index), layers)[-1]
    trace = xor_states(baseline, counterfactual)
    indices = tuple(range(ca.width)) if observer_indices is None else tuple(observer_indices)
    accessible_trace_cells = tuple(index for index in indices if trace[index])
    support = len(accessible_trace_cells)
    profile = EmergentFinalityProfile(
        accessible_support=support,
        spatial_redundancy=support,
        independent_terminal_branches=periodic_components(accessible_trace_cells, ca.width),
        terminal_intervention_cost=support,
    )
    return TraceAnalysis(baseline, counterfactual, trace, indices, profile)


def analyze_second_order_trace(
    ca: SecondOrderCA,
    initial: SecondOrderState,
    seed_index: int,
    layers: int,
    observer_indices: Iterable[int] | None = None,
) -> TraceAnalysis:
    previous, current = initial
    baseline = ca.run(initial, layers)[-1][1]
    changed_initial = (previous, flip_bit(current, seed_index))
    counterfactual = ca.run(changed_initial, layers)[-1][1]
    trace = xor_states(baseline, counterfactual)
    indices = tuple(range(ca.width)) if observer_indices is None else tuple(observer_indices)
    accessible_trace_cells = tuple(index for index in indices if trace[index])
    support = len(accessible_trace_cells)
    profile = EmergentFinalityProfile(
        accessible_support=support,
        spatial_redundancy=support,
        independent_terminal_branches=periodic_components(accessible_trace_cells, ca.width),
        terminal_intervention_cost=support,
    )
    return TraceAnalysis(baseline, counterfactual, trace, indices, profile)


def eca_sensitivity_edges(
    ca: ElementaryCA,
    history: tuple[State, ...],
) -> frozenset[tuple[tuple[int, int], tuple[int, int]]]:
    edges: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for layer, state in enumerate(history[:-1]):
        for child_index in range(ca.width):
            for offset in ca.actual_parent_offsets(state, child_index):
                parent_index = (child_index + offset) % ca.width
                edges.add(((layer, parent_index), (layer + 1, child_index)))
    return frozenset(edges)


def second_order_sensitivity_edges(
    ca: SecondOrderCA,
    history: tuple[SecondOrderState, ...],
) -> frozenset[tuple[tuple[int, str, int], tuple[int, str, int]]]:
    """Return actual Boolean-sensitivity edges for both state registers."""
    edges: set[tuple[tuple[int, str, int], tuple[int, str, int]]] = set()
    for layer, (previous, current) in enumerate(history[:-1]):
        baseline_next = ca.step((previous, current))
        for register_name, register in (("previous", previous), ("current", current)):
            for parent_index in range(ca.width):
                if register_name == "previous":
                    changed_input = (flip_bit(previous, parent_index), current)
                else:
                    changed_input = (previous, flip_bit(current, parent_index))
                changed_next = ca.step(changed_input)
                for child_register_name, (baseline_register, changed_register) in (
                    ("previous", (baseline_next[0], changed_next[0])),
                    ("current", (baseline_next[1], changed_next[1])),
                ):
                    for child_index, (baseline_bit, changed_bit) in enumerate(
                        zip(baseline_register, changed_register)
                    ):
                        if baseline_bit != changed_bit:
                            edges.add(
                                (
                                    (layer, register_name, parent_index),
                                    (layer + 1, child_register_name, child_index),
                                )
                            )
    return frozenset(edges)


def find_observer_divergence(
    trace: TraceAnalysis,
    window_width: int,
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    profiles: dict[tuple[int, ...], EmergentFinalityProfile] = {}
    for window in observer_windows(len(trace.trace_mask), window_width):
        cells = tuple(index for index in window if trace.trace_mask[index])
        support = len(cells)
        profiles[window] = EmergentFinalityProfile(
            support,
            support,
            periodic_components(cells, len(trace.trace_mask)),
            support,
        )
    for left, left_profile in profiles.items():
        for right, right_profile in profiles.items():
            if left < right and left_profile != right_profile:
                return left, right
    return None


def find_eca_trace_witness(
    ca: ElementaryCA,
    layers: int,
    window_width: int | None = None,
) -> tuple[State, int, TraceAnalysis] | None:
    for initial in ca.states():
        for seed_index in range(ca.width):
            trace = analyze_eca_trace(ca, initial, seed_index, layers)
            if trace.profile.accessible_support == 0:
                continue
            if window_width is None or find_observer_divergence(trace, window_width):
                return initial, seed_index, trace
    return None


def find_irreversible_inaccessible_counterexample(
    ca: ElementaryCA,
    layers: int,
    window_width: int,
) -> tuple[State, int, tuple[int, ...], TraceAnalysis] | None:
    transition = analyze_transition_map(ca)
    if transition.injective:
        return None
    for initial in ca.states():
        for seed_index in range(ca.width):
            global_trace = analyze_eca_trace(ca, initial, seed_index, layers)
            if global_trace.profile.accessible_support == 0:
                continue
            for window in observer_windows(ca.width, window_width):
                local_trace = analyze_eca_trace(ca, initial, seed_index, layers, window)
                if local_trace.profile.accessible_support == 0:
                    return initial, seed_index, window, global_trace
    return None


def find_reversible_record_counterexample(
    ca: SecondOrderCA,
    layers: int,
) -> tuple[SecondOrderState, int, TraceAnalysis] | None:
    transition = analyze_transition_map(ca)
    if not transition.injective or transition.lost_bits > 1e-12:
        return None
    zero = tuple(0 for _ in range(ca.width))
    candidate_initials = [
        (zero, int_to_bits(value, ca.width))
        for value in range(1, 2**ca.width)
    ]
    for initial in candidate_initials:
        for seed_index in range(ca.width):
            trace = analyze_second_order_trace(ca, initial, seed_index, layers)
            if trace.profile.accessible_support:
                return initial, seed_index, trace
    return None


def find_minimal_counterexamples(max_width: int = 5) -> dict[str, object]:
    reversible_record = None
    irreversible_inaccessible = None
    observer_divergence = None

    for width in range(1, max_width + 1):
        if reversible_record is None:
            for rule in range(256):
                lifted = SecondOrderCA(ElementaryCA(rule, width))
                witness = find_reversible_record_counterexample(lifted, layers=1)
                if witness:
                    initial, seed, trace = witness
                    reversible_record = {
                        "width": width,
                        "rule": rule,
                        "initial": initial,
                        "seed_index": seed,
                        "trace": trace,
                    }
                    break

        if width < 2:
            continue
        for rule in range(256):
            ca = ElementaryCA(rule, width)
            if irreversible_inaccessible is None:
                witness = find_irreversible_inaccessible_counterexample(
                    ca, layers=1, window_width=1
                )
                if witness:
                    initial, seed, window, trace = witness
                    irreversible_inaccessible = {
                        "width": width,
                        "rule": rule,
                        "initial": initial,
                        "seed_index": seed,
                        "observer_window": window,
                        "global_trace": trace,
                        "lost_bits": analyze_transition_map(ca).lost_bits,
                    }
            if observer_divergence is None:
                for initial in ca.states():
                    for seed in range(width):
                        trace = analyze_eca_trace(ca, initial, seed, layers=1)
                        windows = find_observer_divergence(trace, window_width=1)
                        if windows:
                            observer_divergence = {
                                "width": width,
                                "rule": rule,
                                "initial": initial,
                                "seed_index": seed,
                                "trace": trace,
                                "observer_windows": windows,
                            }
                            break
                    if observer_divergence is not None:
                        break
            if irreversible_inaccessible and observer_divergence:
                break
        if reversible_record and irreversible_inaccessible and observer_divergence:
            break

    return {
        "reversible_record_with_zero_information_loss": reversible_record,
        "irreversible_record_inaccessible_to_bounded_observer": irreversible_inaccessible,
        "equal_access_observer_divergence": observer_divergence,
    }


def profile_dimensions_collapsed(profile: EmergentFinalityProfile) -> bool:
    return (
        profile.accessible_support
        == profile.spatial_redundancy
        == profile.terminal_intervention_cost
    )


def pearson_correlation(left: Iterable[float], right: Iterable[float]) -> float:
    xs = tuple(left)
    ys = tuple(right)
    if len(xs) != len(ys) or not xs:
        raise ValueError("correlation requires equal non-empty samples")
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    centered_x = tuple(value - mean_x for value in xs)
    centered_y = tuple(value - mean_y for value in ys)
    numerator = sum(x * y for x, y in zip(centered_x, centered_y))
    denominator_x = sum(value * value for value in centered_x) ** 0.5
    denominator_y = sum(value * value for value in centered_y) ** 0.5
    if denominator_x == 0 or denominator_y == 0:
        return 0.0
    return numerator / (denominator_x * denominator_y)


def sweep_elementary_rules(
    width: int = 5,
    layers: int = 3,
    observer_window_width: int = 2,
    verify_reversible_lifts: bool = True,
) -> RuleSweepSummary:
    results = []
    reversible_lifts_all_injective = True
    for rule in range(256):
        ca = ElementaryCA(rule, width)
        transition = analyze_transition_map(ca)
        interventions = 0
        surviving = 0
        divergent = 0
        for initial in ca.states():
            for seed_index in range(width):
                interventions += 1
                trace = analyze_eca_trace(ca, initial, seed_index, layers)
                if trace.profile.accessible_support:
                    surviving += 1
                if find_observer_divergence(trace, observer_window_width):
                    divergent += 1
        if verify_reversible_lifts:
            reversible_lifts_all_injective &= analyze_transition_map(
                SecondOrderCA(ca)
            ).injective
        results.append(
            RuleSweepResult(
                rule=rule,
                injective=transition.injective,
                lost_bits=transition.lost_bits,
                trace_survival_fraction=surviving / interventions,
                observer_divergence_fraction=divergent / interventions,
            )
        )

    same_loss_different_survival = None
    same_survival_different_loss = None
    for left, right in combinations(results, 2):
        if (
            same_loss_different_survival is None
            and abs(left.lost_bits - right.lost_bits) < 1e-12
            and abs(left.trace_survival_fraction - right.trace_survival_fraction)
            > 0.1
        ):
            same_loss_different_survival = (left.rule, right.rule)
        if (
            same_survival_different_loss is None
            and abs(left.trace_survival_fraction - right.trace_survival_fraction)
            < 1e-12
            and abs(left.lost_bits - right.lost_bits) > 0.1
        ):
            same_survival_different_loss = (left.rule, right.rule)
        if same_loss_different_survival and same_survival_different_loss:
            break

    return RuleSweepSummary(
        width=width,
        layers=layers,
        rule_count=len(results),
        injective_rule_count=sum(result.injective for result in results),
        mean_lost_bits=sum(result.lost_bits for result in results) / len(results),
        mean_trace_survival_fraction=sum(
            result.trace_survival_fraction for result in results
        )
        / len(results),
        lost_bits_trace_survival_correlation=pearson_correlation(
            (result.lost_bits for result in results),
            (result.trace_survival_fraction for result in results),
        ),
        same_loss_different_survival=same_loss_different_survival,
        same_survival_different_loss=same_survival_different_loss,
        reversible_lifts_all_injective=reversible_lifts_all_injective,
        results=tuple(results),
    )


def analyze_rule_suite(
    rules: Iterable[int],
    width: int,
    initial: State,
    seed_index: int,
    layers: int,
    temperature_kelvin: float = 300.0,
) -> tuple[dict[str, object], ...]:
    results = []
    for rule in rules:
        eca = ElementaryCA(rule, width)
        reversible = SecondOrderCA(eca)
        eca_map = analyze_transition_map(eca, temperature_kelvin)
        reversible_map = analyze_transition_map(reversible, temperature_kelvin)
        eca_trace = analyze_eca_trace(eca, initial, seed_index, layers)
        reversible_trace = analyze_second_order_trace(
            reversible,
            (initial, initial),
            seed_index,
            layers,
        )
        results.append(
            {
                "rule": rule,
                "irreversible_map": eca_map,
                "reversible_map": reversible_map,
                "irreversible_trace": eca_trace,
                "reversible_trace": reversible_trace,
            }
        )
    return tuple(results)
