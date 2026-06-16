"""Run the T13 witnesses and print an inspectable result."""

from __future__ import annotations

import json

from models.t13_signed_readout import (
    build_observer_consistency_pair,
    build_w1_pair,
    build_w2_chain,
    sorkin_i2,
    sorkin_i3_coefficients,
)

THRESHOLD = 1


def main() -> None:
    constructive, destructive, observer = build_w1_pair()
    w1 = {
        "profile_constructive": constructive.finality_profile(observer, "X", "true", THRESHOLD).as_tuple(),
        "profile_destructive": destructive.finality_profile(observer, "X", "true", THRESHOLD).as_tuple(),
        "readout_constructive": constructive.readout_born(observer, "X", "true"),
        "readout_destructive": destructive.readout_born(observer, "X", "true"),
    }

    chain_graph, chain_observer, chain = build_w2_chain()
    w2 = {
        "evidence_counts": [
            len(chain_graph.accessible_records(chain_observer, "X", "true", e)) for e in chain
        ],
        "profiles": [
            chain_graph.finality_profile(chain_observer, "X", "true", THRESHOLD, e).as_tuple()
            for e in chain
        ],
        "born_readouts": [chain_graph.readout_born(chain_observer, "X", "true", e) for e in chain],
        "signed_counters": [
            chain_graph.signed_counters(chain_observer, "X", "true", e) for e in chain
        ],
    }

    graph, full, partial = build_observer_consistency_pair()
    consistency = {
        "readout_full_access": graph.readout_born(full, "X", "true"),
        "readout_partial_access": graph.readout_born(partial, "X", "true"),
    }

    result = {
        "threshold": THRESHOLD,
        "W1_profile_blindness": w1,
        "W2_anti_monotone_chain": w2,
        "sorkin_I2_constructive": sorkin_i2((1 + 0j,), (1 + 0j,)),
        "sorkin_I2_destructive": sorkin_i2((1 + 0j,), (-1 + 0j,)),
        "sorkin_I3_coefficients": sorkin_i3_coefficients(),
        "sorkin_I3_symbolic_cancellation": all(
            coefficient == 0 for coefficient in sorkin_i3_coefficients().values()
        ),
        "observer_consistency": consistency,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
