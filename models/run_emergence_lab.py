"""Run the first Emergence Laboratory comparison."""

from __future__ import annotations

from dataclasses import asdict
import json

from models.emergence_lab import (
    ElementaryCA,
    SecondOrderCA,
    analyze_eca_trace,
    analyze_rule_suite,
    analyze_transition_map,
    eca_sensitivity_edges,
    exhaustive_preimage_search,
    find_eca_trace_witness,
    find_irreversible_inaccessible_counterexample,
    find_minimal_counterexamples,
    find_observer_divergence,
    find_reversible_record_counterexample,
    int_to_bits,
    profile_dimensions_collapsed,
    second_order_sensitivity_edges,
    sweep_elementary_rules,
)


def serialize(value: object) -> object:
    if hasattr(value, "__dataclass_fields__"):
        return {key: serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): serialize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialize(item) for item in value]
    return value


def main() -> None:
    width = 5
    layers = 6
    initial = int_to_bits(0b00100, width)
    rule = 110
    eca = ElementaryCA(rule, width)
    reversible = SecondOrderCA(eca)

    irreversible_map = analyze_transition_map(eca)
    reversible_map = analyze_transition_map(reversible)
    trace_witness = find_eca_trace_witness(eca, layers=1, window_width=2)
    if trace_witness is None:
        raise RuntimeError("no Rule 110 trace witness found")
    witness_initial, witness_seed, irreversible_trace = trace_witness
    reversible_trace = find_reversible_record_counterexample(reversible, layers)
    inaccessible = find_irreversible_inaccessible_counterexample(
        eca, layers=1, window_width=1
    )
    divergence = find_observer_divergence(irreversible_trace, window_width=2)
    history = eca.run(initial, layers)
    reversible_initial = (initial, initial)
    reversible_history = reversible.run(reversible_initial, layers)
    irreversible_target = eca.step(initial)
    reversible_target = reversible.step(reversible_initial)

    output = {
        "configuration": {
            "rule": rule,
            "width": width,
            "causal_layers": layers,
            "temperature_kelvin": 300.0,
        },
        "irreversible_transition_map": irreversible_map,
        "reversible_transition_map": reversible_map,
        "trace_witness": {
            "initial": witness_initial,
            "seed_index": witness_seed,
        },
        "irreversible_seed_trace": irreversible_trace,
        "actual_sensitivity_edge_count": len(eca_sensitivity_edges(eca, history)),
        "reversible_sensitivity_edge_count": len(
            second_order_sensitivity_edges(reversible, reversible_history)
        ),
        "computational_reversal": {
            "irreversible_exhaustive": exhaustive_preimage_search(
                eca, irreversible_target
            ),
            "reversible_exhaustive": exhaustive_preimage_search(
                reversible, reversible_target
            ),
            "reversible_direct_inverse_evaluations": 1,
            "reversible_direct_inverse_correct": reversible.inverse_step(
                reversible_target
            )
            == reversible_initial,
        },
        "equal_window_observer_divergence": divergence,
        "profile_dimension_collapse": profile_dimensions_collapsed(
            irreversible_trace.profile
        ),
        "reversible_record_zero_information_loss": reversible_trace,
        "irreversible_information_loss_inaccessible_record": inaccessible,
        "rule_suite": analyze_rule_suite(
            (0, 30, 90, 110, 150),
            width=width,
            initial=initial,
            seed_index=2,
            layers=layers,
        ),
        "all_rule_sweep": sweep_elementary_rules(
            width=width,
            layers=3,
            observer_window_width=2,
            verify_reversible_lifts=True,
        ),
        "minimal_counterexamples": find_minimal_counterexamples(max_width=5),
    }
    print(json.dumps(serialize(output), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
