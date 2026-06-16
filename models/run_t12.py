"""Run the T12 coupling-profile experiment and print an inspectable result."""

from __future__ import annotations

import json

from models.t12_coupling import build_t12_scenario, omniscient_relation

PROPS = ("A", "B", "C", "D")
THRESHOLD = 2


def main() -> None:
    graph, population = build_t12_scenario()
    truth = sorted(omniscient_relation(graph, PROPS, THRESHOLD))

    observers = {}
    for observer in population:
        observers[observer.observer_id] = {
            "profile": sorted(observer.profile),
            "accepts_conditional": observer.accepts_conditional,
            "reconstructible": [
                p for p in PROPS if graph.reconstructible(observer, p, THRESHOLD)
            ],
            "relation": sorted(graph.observer_relation(observer, PROPS, THRESHOLD)),
            "constrained_by": [
                p for p in PROPS if graph.constrained(observer, p, THRESHOLD)
            ],
        }

    grades = {
        p: {
            "channel": graph.proposition_channel(p).channel,
            "binding": graph.proposition_channel(p).binding,
            "reach": graph.reach(p, population),
            "hardness": graph.hardness(p, population, THRESHOLD),
        }
        for p in PROPS
    }

    result = {
        "threshold": THRESHOLD,
        "omniscient_relation": truth,
        "observers": observers,
        "record_grades": grades,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
