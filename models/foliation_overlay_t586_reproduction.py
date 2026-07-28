"""Foliation overlay against the T586 record-capability order: in-repo reproduction.

Re-derives, from scratch and inside repository conventions, the swing-2 result
computed out-of-repo on 2026-07-27 and reported in the system-runtime mailbox
note `mailboxes/time-as-finality/
20260727-swing2-result-foliation-against-t586-order.md`. That note explicitly
requested in-repo reproduction before grading; this script is that
reproduction.

Framing constraints honored:

- T587's closing stop controls: "Do not continue producing T-number scaffolds
  from T586 alone." A foliation overlay -- an injective global time
  assignment, hence a total-order comparator -- is exactly the comparator
  class T587 found absorbed. This artifact is therefore
  reproduction-and-corroboration context for the T587 downgrade
  (`T586_DOWNGRADED_TO_TYPED_RECORD_PREREQUISITE_FILTER_REVIEW_ONLY`), not a
  new T-number and not a new claim.
- Everything is recomputed against the T586 module's own machinery: the
  `_landauer_record_events` fixture (reused unchanged, not copied) and the
  `build_order_report`, `causal_relation`, `transitive_closure`, and
  `clock_label_relation` helpers.

The script is pure stdlib and deterministic. It prints a JSON summary with a
per-quantity expected/actual/match table, where every expected value is the
number reported in the mailbox note, and exits 0 only if all of them match.
A mismatch is the important outcome and must be reported, not smoothed.
"""

from __future__ import annotations

import json
from dataclasses import replace
from itertools import permutations

from models import t586_record_capability_order_gate as t586

PREPARE = "prepare_biased_reference"

Relation = frozenset


def foliation_respects(order: tuple[str, ...], relation: Relation) -> bool:
    """A foliation respects a relation iff it is a linear extension of it."""
    position = {event_id: index for index, event_id in enumerate(order)}
    return all(position[a] < position[b] for a, b in relation)


def foliation_comparabilities(order: tuple[str, ...]) -> Relation:
    """All directed pairs the injective global time assignment makes comparable."""
    return frozenset(
        (order[i], order[j])
        for i in range(len(order))
        for j in range(i + 1, len(order))
    )


def main() -> int:
    events = t586._landauer_record_events()
    event_ids = tuple(event.event_id for event in events)

    # (a) Baseline: the record-order closure from the module's own gate.
    baseline = t586.build_order_report(events)
    record = frozenset(baseline.closure)
    unordered_pairs = [
        (event_ids[i], event_ids[j])
        for i in range(len(event_ids))
        for j in range(i + 1, len(event_ids))
    ]
    incomparable = [
        pair
        for pair in unordered_pairs
        if pair not in record and (pair[1], pair[0]) not in record
    ]
    causal = t586.causal_relation(events)

    # (b) All candidate foliations: the 5! injective global time assignments.
    foliations = list(permutations(event_ids))
    record_admissible = [f for f in foliations if foliation_respects(f, record)]
    causal_admissible = [f for f in foliations if foliation_respects(f, causal)]
    record_not_causal = [f for f in record_admissible if f not in causal_admissible]
    both_admissible = [f for f in record_admissible if f in causal_admissible]

    # (c) What one record-admissible foliation adds beyond the record order.
    # Deterministic choice: first record-admissible foliation in permutation
    # order over the fixture's own event order.
    chosen = record_admissible[0]
    chosen_successive = frozenset(
        (chosen[i], chosen[i + 1]) for i in range(len(chosen) - 1)
    )
    chosen_total = t586.transitive_closure(event_ids, chosen_successive)
    added = sorted(chosen_total - record)
    added_without_record_basis = [
        pair
        for pair in added
        if pair not in record and (pair[1], pair[0]) not in record
    ]

    # (d) T586's clock-label control, re-exercised with an actual foliation
    # label present: assign every event its chosen-foliation position as the
    # clock label and recompute the record order.
    position = {event_id: index for index, event_id in enumerate(chosen)}
    foliated_events = tuple(
        replace(event, clock_label=position[event.event_id]) for event in events
    )
    foliated = t586.build_order_report(foliated_events)
    foliated_record = frozenset(foliated.closure)
    foliated_clock_relation = t586.clock_label_relation(foliated_events)

    checks = [
        ("baseline_strict_partial_order", True, baseline.strict_partial_order),
        ("record_closure_ordered_pairs", 6, len(record)),
        ("record_incomparable_unordered_pairs", 4, len(incomparable)),
        (
            "incomparable_pairs_all_involve_prepare_biased_reference",
            True,
            all(PREPARE in pair for pair in incomparable),
        ),
        ("causal_closure_ordered_pairs", 8, len(causal)),
        ("record_closure_strict_subset_of_causal_closure", True, record < causal),
        ("candidate_foliations", 120, len(foliations)),
        ("foliations_respecting_record_order", 5, len(record_admissible)),
        ("foliations_respecting_causal_order", 3, len(causal_admissible)),
        ("record_admissible_but_causally_inadmissible", 2, len(record_not_causal)),
        ("foliations_respecting_both_orders", 3, len(both_admissible)),
        (
            "transitive_closure_of_successive_pairs_is_the_total_order",
            True,
            chosen_total == foliation_comparabilities(chosen),
        ),
        ("chosen_foliation_total_comparabilities", 10, len(chosen_total)),
        ("chosen_foliation_added_comparabilities", 4, len(added)),
        ("added_comparabilities_without_record_basis", 4, len(added_without_record_basis)),
        (
            "record_order_with_foliation_label_identical_to_baseline",
            True,
            foliated_record == record and foliated.strict_partial_order,
        ),
        (
            "foliation_clock_label_total_order_differs_from_record_order",
            True,
            foliated_clock_relation == chosen_total
            and foliated_clock_relation != record,
        ),
    ]

    summary = {
        "artifact": "foliation-overlay-t586-reproduction-2026-07-27",
        "reproduces": (
            "system-runtime mailboxes/time-as-finality/"
            "20260727-swing2-result-foliation-against-t586-order.md"
        ),
        "framing": (
            "reproduction-and-corroboration for the T587 downgrade context; "
            "not a new T-number; not a new claim"
        ),
        "event_ids": list(event_ids),
        "record_closure": [list(pair) for pair in sorted(record)],
        "record_incomparable_pairs": [list(pair) for pair in incomparable],
        "causal_closure": [list(pair) for pair in sorted(causal)],
        "record_admissible_foliations": [list(f) for f in record_admissible],
        "causal_admissible_foliations": [list(f) for f in causal_admissible],
        "record_admissible_causally_inadmissible_foliations": [
            list(f) for f in record_not_causal
        ],
        "chosen_record_admissible_foliation": list(chosen),
        "chosen_foliation_added_comparabilities": [list(pair) for pair in added],
        "checks": [
            {
                "check_id": check_id,
                "expected": expected,
                "actual": actual,
                "match": expected == actual,
            }
            for check_id, expected, actual in checks
        ],
        "all_match": all(expected == actual for _, expected, actual in checks),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["all_match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
