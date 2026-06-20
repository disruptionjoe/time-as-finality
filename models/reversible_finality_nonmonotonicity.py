"""T80: reversible local dynamics can violate raw D1 monotonicity.

The audit connects T9's reversible second-order cellular automata with T18's
constructor-style finality direction theorem.  It tests whether the T18
monotone-admissibility rule is automatically grounded by reversible local
dynamics.  The answer is no for raw observer-window trace profiles.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.emergence_lab import (
    ElementaryCA,
    EmergentFinalityProfile,
    SecondOrderCA,
    State,
    TransitionMapAnalysis,
    analyze_second_order_trace,
    analyze_transition_map,
    int_to_bits,
    observer_windows,
)
from models.finality_direction_theorem import (
    FinalityState,
    FinalityVector,
    Transformation,
    classify_transformation,
)


SecondOrderInitial = tuple[State, State]


@dataclass(frozen=True)
class LayerTraceProfile:
    layer: int
    trace_mask: State
    observer_window: tuple[int, ...]
    profile: EmergentFinalityProfile


@dataclass(frozen=True)
class NonmonotoneStep:
    before: LayerTraceProfile
    after: LayerTraceProfile
    decreased_dimensions: tuple[str, ...]
    t18_classification: Transformation


@dataclass(frozen=True)
class ReversibleFinalityWitness:
    rule: int
    width: int
    initial: SecondOrderInitial
    seed_index: int
    observer_window: tuple[int, ...]
    transition: TransitionMapAnalysis
    layer_profiles: tuple[LayerTraceProfile, ...]
    first_nonmonotone_step: NonmonotoneStep
    direct_inverse_checked: bool
    persistent_memory_support: tuple[int, ...]
    persistent_memory_support_monotone: bool
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    h7_update: str
    blocker: str
    recommended_next: str


DIMENSION_NAMES = (
    "accessible_support",
    "spatial_redundancy",
    "independent_terminal_branches",
    "terminal_intervention_cost",
)


def layer_profile_sequence(
    ca: SecondOrderCA,
    initial: SecondOrderInitial,
    seed_index: int,
    observer_window: tuple[int, ...],
    layers: int,
) -> tuple[LayerTraceProfile, ...]:
    return tuple(
        LayerTraceProfile(
            layer=layer,
            trace_mask=trace.trace_mask,
            observer_window=observer_window,
            profile=trace.profile,
        )
        for layer in range(layers + 1)
        for trace in (
            analyze_second_order_trace(
                ca,
                initial,
                seed_index=seed_index,
                layers=layer,
                observer_indices=observer_window,
            ),
        )
    )


def classify_profile_step(
    before: LayerTraceProfile,
    after: LayerTraceProfile,
) -> Transformation:
    before_state = FinalityState(
        name=f"layer_{before.layer}",
        d1=_to_finality_vector(before.profile),
        thermodynamic_cost_proxy=0,
    )
    after_state = FinalityState(
        name=f"layer_{after.layer}",
        d1=_to_finality_vector(after.profile),
        thermodynamic_cost_proxy=0,
    )
    return classify_transformation(before_state, after_state)


def find_first_nonmonotone_step(
    profiles: tuple[LayerTraceProfile, ...],
) -> NonmonotoneStep | None:
    for before, after in zip(profiles, profiles[1:]):
        decreased = tuple(
            name
            for name, before_value, after_value in zip(
                DIMENSION_NAMES,
                before.profile.as_tuple(),
                after.profile.as_tuple(),
            )
            if after_value < before_value
        )
        if decreased:
            return NonmonotoneStep(
                before=before,
                after=after,
                decreased_dimensions=decreased,
                t18_classification=classify_profile_step(before, after),
            )
    return None


def persistent_memory_support_sequence(
    profiles: tuple[LayerTraceProfile, ...],
) -> tuple[int, ...]:
    """Count observed trace events retained by a minimal external memory.

    This is not a repair theorem for D1.  It is only a control showing why T9's
    requested dynamical observer-memory step matters: raw terminal traces can
    disappear, while retained observations are monotone by construction.
    """
    retained = 0
    sequence = []
    for profile in profiles:
        retained += profile.profile.accessible_support
        sequence.append(retained)
    return tuple(sequence)


def is_monotone(values: tuple[int, ...]) -> bool:
    return all(after >= before for before, after in zip(values, values[1:]))


def canonical_rule30_witness(layers: int = 5) -> ReversibleFinalityWitness:
    width = 3
    rule = 30
    base = ElementaryCA(rule, width)
    ca = SecondOrderCA(base)
    zero = int_to_bits(0, width)
    initial = (zero, zero)
    seed_index = 0
    observer_window = (0, 1)
    profiles = layer_profile_sequence(
        ca,
        initial,
        seed_index=seed_index,
        observer_window=observer_window,
        layers=layers,
    )
    nonmonotone = find_first_nonmonotone_step(profiles)
    if nonmonotone is None:
        raise RuntimeError("canonical witness unexpectedly became monotone")
    transition = analyze_transition_map(ca)
    memory_support = persistent_memory_support_sequence(profiles)
    return ReversibleFinalityWitness(
        rule=rule,
        width=width,
        initial=initial,
        seed_index=seed_index,
        observer_window=observer_window,
        transition=transition,
        layer_profiles=profiles,
        first_nonmonotone_step=nonmonotone,
        direct_inverse_checked=all(ca.inverse_step(ca.step(state)) == state for state in ca.states()),
        persistent_memory_support=memory_support,
        persistent_memory_support_monotone=is_monotone(memory_support),
        strongest_claim=(
            "Raw observer-window D1 trace profiles are not monotone under "
            "reversible local dynamics, even when the global transition map is "
            "injective and has zero logical information-loss bound."
        ),
        weakened_claim=(
            "T18's finality arrow remains only a conditional constructor theorem; "
            "its admissible transformations cannot be identified with arbitrary "
            "physical time steps in reversible substrates."
        ),
        falsification_condition=(
            "T80 fails if every reversible second-order CA trajectory with a "
            "nonzero observer-window trace has componentwise nondecreasing raw "
            "D1 trace profiles across physical steps."
        ),
        h7_update=(
            "H7 should be weakened: finality-induced direction is not grounded by "
            "raw reversible trace dynamics alone. It requires an added "
            "persistence, coarse-graining, or constructor-impossibility condition."
        ),
        blocker=(
            "No internal dynamical record-bearing observer has yet been shown to "
            "retain traces while preserving the intended D1 dimensions."
        ),
        recommended_next=(
            "Build the T9 requested persistent reconciler subsystem and test "
            "whether its retained-record D1 profile is monotone without reducing "
            "the claim to thermodynamic erasure."
        ),
    )


def search_reversible_nonmonotone_witness(
    max_width: int = 4,
    max_layers: int = 6,
) -> ReversibleFinalityWitness | None:
    for width in range(1, max_width + 1):
        for rule in range(256):
            ca = SecondOrderCA(ElementaryCA(rule, width))
            transition = analyze_transition_map(ca)
            if not transition.injective or abs(transition.lost_bits) > 1e-12:
                continue
            for initial in ca.states():
                for seed_index in range(width):
                    for window_width in range(1, width + 1):
                        for observer_window in observer_windows(width, window_width):
                            profiles = layer_profile_sequence(
                                ca,
                                initial,
                                seed_index,
                                observer_window,
                                max_layers,
                            )
                            nonmonotone = find_first_nonmonotone_step(profiles)
                            if nonmonotone is None:
                                continue
                            memory_support = persistent_memory_support_sequence(profiles)
                            return ReversibleFinalityWitness(
                                rule=rule,
                                width=width,
                                initial=initial,
                                seed_index=seed_index,
                                observer_window=observer_window,
                                transition=transition,
                                layer_profiles=profiles,
                                first_nonmonotone_step=nonmonotone,
                                direct_inverse_checked=all(
                                    ca.inverse_step(ca.step(state)) == state
                                    for state in ca.states()
                                ),
                                persistent_memory_support=memory_support,
                                persistent_memory_support_monotone=is_monotone(memory_support),
                                strongest_claim=(
                                    "A reversible local-dynamics witness violates raw D1 "
                                    "monotonicity."
                                ),
                                weakened_claim=(
                                    "T18 is conditional and does not follow from reversible "
                                    "dynamics alone."
                                ),
                                falsification_condition=(
                                    "No reversible second-order CA witness with decreasing raw "
                                    "D1 trace profile exists within the declared search bounds."
                                ),
                                h7_update=(
                                    "Require persistence, coarse-graining, or constructor "
                                    "impossibility before using H7 as a physical arrow."
                                ),
                                blocker=(
                                    "The witness uses an externally selected observer window, "
                                    "not an endogenous observer."
                                ),
                                recommended_next=(
                                    "Replace the external window with a persistent reconciler "
                                    "subsystem."
                                ),
                            )
    return None


def run_t80_analysis() -> ReversibleFinalityWitness:
    return canonical_rule30_witness()


def t80_result_to_dict(result: ReversibleFinalityWitness) -> dict[str, object]:
    return {
        "configuration": {
            "rule": result.rule,
            "width": result.width,
            "initial_previous": list(result.initial[0]),
            "initial_current": list(result.initial[1]),
            "seed_index": result.seed_index,
            "observer_window": list(result.observer_window),
        },
        "transition_map": {
            "state_count": result.transition.state_count,
            "image_count": result.transition.image_count,
            "injective": result.transition.injective,
            "lost_bits": result.transition.lost_bits,
            "landauer_minimum_joules": result.transition.landauer_minimum_joules,
            "direct_inverse_checked": result.direct_inverse_checked,
        },
        "layer_profiles": [
            {
                "layer": profile.layer,
                "trace_mask": list(profile.trace_mask),
                "observer_window": list(profile.observer_window),
                "d1_trace_profile": profile.profile.as_tuple(),
            }
            for profile in result.layer_profiles
        ],
        "first_nonmonotone_step": {
            "before_layer": result.first_nonmonotone_step.before.layer,
            "after_layer": result.first_nonmonotone_step.after.layer,
            "before_profile": result.first_nonmonotone_step.before.profile.as_tuple(),
            "after_profile": result.first_nonmonotone_step.after.profile.as_tuple(),
            "decreased_dimensions": list(
                result.first_nonmonotone_step.decreased_dimensions
            ),
            "t18_kind": result.first_nonmonotone_step.t18_classification.kind,
            "t18_possible": result.first_nonmonotone_step.t18_classification.possible,
        },
        "persistent_memory_control": {
            "support_sequence": list(result.persistent_memory_support),
            "monotone": result.persistent_memory_support_monotone,
            "interpretation": (
                "A retained external memory is monotone by construction; raw "
                "terminal traces are not. The next question is whether such "
                "memory can be made endogenous and physically grounded."
            ),
        },
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "blocker": result.blocker,
        "recommended_next": result.recommended_next,
    }


def _to_finality_vector(profile: EmergentFinalityProfile) -> FinalityVector:
    return FinalityVector(
        accessible_support=profile.accessible_support,
        holder_redundancy=profile.spatial_redundancy,
        branch_support=profile.independent_terminal_branches,
        reversal_cost=profile.terminal_intervention_cost,
    )
