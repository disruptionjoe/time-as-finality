"""Run the reference T1 scenarios and print an inspectable result."""

from __future__ import annotations

import json

from models.t1_record_graph import (
    Observer,
    build_reference_scenario,
    minimal_total_order_counterexample,
)


def main() -> None:
    graph, observer = build_reference_scenario()
    propositions = ("A", "B", "C")
    threshold = 2

    profiles = {
        proposition: graph.finality_profile(observer, proposition, "true", threshold).as_tuple()
        for proposition in propositions
    }
    thermodynamic = {
        proposition: graph.thermodynamic_reversal_proxy(observer, proposition, "true", threshold)
        for proposition in propositions
    }
    relation = sorted(graph.reconstructed_relation(observer, propositions, threshold))

    access_limited = Observer(
        observer.observer_id,
        observer.event,
        observer.accessible_holders - {"ha2"},
    )
    access_loss = {
        "global_active_A_records": sum(
            record.active and record.proposition == "A" for record in graph.records.values()
        ),
        "observer_A_support": graph.finality_profile(
            access_limited, "A", "true", threshold
        ).accessible_support,
    }

    graph.erase_record("rb2")
    physical_reversal = {
        "global_active_B_records": sum(
            record.active and record.proposition == "B" for record in graph.records.values()
        ),
        "observer_B_support": graph.finality_profile(
            observer, "B", "true", threshold
        ).accessible_support,
    }

    counterexample_graph, counterexample_observer = minimal_total_order_counterexample()
    counterexample_relation = sorted(
        counterexample_graph.reconstructed_relation(
            counterexample_observer, ("L", "R"), threshold=1
        )
    )

    output = {
        "primitive_time_used": False,
        "profiles_A_R_B_C": profiles,
        "thermodynamic_reversal_proxy": thermodynamic,
        "reconstructed_relation": relation,
        "spacelike_A_B_ordered": ("A", "B") in relation or ("B", "A") in relation,
        "access_loss": access_loss,
        "physical_reversal": physical_reversal,
        "minimal_total_order_counterexample": {
            "events": sorted(counterexample_graph.events),
            "reconstructed_relation": counterexample_relation,
            "result": "total-order claim fails; partial-order reconstruction survives",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
