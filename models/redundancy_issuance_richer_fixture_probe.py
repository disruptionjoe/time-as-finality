"""Richer-fixture reopener for the commit-module S2 issuance result.

This deterministic review instrument gives the S2 route the structures its
original fixture could not express: multiple consumers, conditional fragment
states, strong independence, and additive copy prices.  It asks one narrow
question: do those additions make the redundancy-to-issuance verdict
independent of the supplied fragment decomposition?

The instrument is fixture-scoped.  It is not a quantum model, a preferred-
frame result, a claim promotion, or an assertion that either decomposition is
physically privileged.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from typing import Callable, Iterable


BIT_VALUES = (0, 1)
MICROCARRIER_COUNT = 3
REDUNDANCY_THRESHOLD = 2
DISTINGUISHABILITY_THRESHOLD = Fraction(3, 4)

FINE_PARTITION = ((0,), (1,), (2,))
MERGED_PARTITION = ((0, 1, 2),)
RELABELED_FINE_PARTITION = ((2,), (0,), (1,))

CONSUMER_ACCESS = {
    "read_e1": frozenset({0}),
    "read_e2": frozenset({1}),
    "read_e3": frozenset({2}),
    "read_all": frozenset({0, 1, 2}),
}
TARGET_ORDER = (
    ("issue_source", "read_e1"),
    ("issue_source", "read_e2"),
    ("issue_source", "read_e3"),
)

# Frozen before result summaries are computed.  Prediction outcomes are data;
# only instrument-validity controls determine the process exit code.
PRE_REGISTRATIONS = {
    "PR1": (
        "The independent-copy law issues under the fine split at additive "
        "budget 3 and reproduces the three source-to-reader edges."
    ),
    "PR2": (
        "The same microstate fails the nontrivial redundancy criterion under "
        "the merged split because only one independently consumable fragment "
        "remains."
    ),
    "PR3": (
        "A shared-noise family with the same one-fragment distinguishability "
        "is rejected by conditional strong independence."
    ),
    "PR4": "Relabeling the fine fragments preserves every verdict-bearing field.",
    "PR5": "A one-copy family is rejected at redundancy threshold 2.",
    "PR6": (
        "No frozen additive budget in {2,3,4} makes issuance both nontrivial "
        "and invariant across the fine and merged splits."
    ),
    "PR7": (
        "A planted high-copy-cost control is rejected at budget 3 even though "
        "its unpriced redundancy structure passes."
    ),
}

Outcome = tuple[int, ...]
ConditionalLaw = dict[int, dict[Outcome, Fraction]]
Partition = tuple[tuple[int, ...], ...]


def independent_copy_law(error: Fraction = Fraction(1, 10)) -> ConditionalLaw:
    """Three conditionally independent noisy copies of a uniform source bit."""
    law: ConditionalLaw = {}
    for source in BIT_VALUES:
        rows: dict[Outcome, Fraction] = {}
        for outcome in product(BIT_VALUES, repeat=MICROCARRIER_COUNT):
            probability = Fraction(1, 1)
            for value in outcome:
                probability *= 1 - error if value == source else error
            rows[outcome] = probability
        law[source] = rows
    return law


def shared_noise_law(error: Fraction = Fraction(1, 10)) -> ConditionalLaw:
    """Three individually informative copies driven by one shared noise bit."""
    law: ConditionalLaw = {}
    for source in BIT_VALUES:
        correct = (source,) * MICROCARRIER_COUNT
        flipped = (1 - source,) * MICROCARRIER_COUNT
        law[source] = {correct: 1 - error, flipped: error}
    return law


def one_copy_law(error: Fraction = Fraction(1, 10)) -> ConditionalLaw:
    """One informative carrier plus two source-independent fair carriers."""
    law: ConditionalLaw = {}
    for source in BIT_VALUES:
        rows: dict[Outcome, Fraction] = {}
        for outcome in product(BIT_VALUES, repeat=MICROCARRIER_COUNT):
            first = 1 - error if outcome[0] == source else error
            rows[outcome] = first * Fraction(1, 2) * Fraction(1, 2)
        law[source] = rows
    return law


def law_is_normalized(law: ConditionalLaw) -> bool:
    return all(
        set(rows).issubset(set(product(BIT_VALUES, repeat=MICROCARRIER_COUNT)))
        and all(value >= 0 for value in rows.values())
        and sum(rows.values(), Fraction(0, 1)) == 1
        for rows in law.values()
    ) and set(law) == set(BIT_VALUES)


def partition_is_valid(partition: Partition) -> bool:
    flattened = [index for group in partition for index in group]
    return sorted(flattened) == list(range(MICROCARRIER_COUNT)) and (
        len(flattened) == len(set(flattened))
    )


def marginal(
    rows: dict[Outcome, Fraction], group: tuple[int, ...]
) -> dict[Outcome, Fraction]:
    projected: dict[Outcome, Fraction] = {}
    for outcome, probability in rows.items():
        key = tuple(outcome[index] for index in group)
        projected[key] = projected.get(key, Fraction(0, 1)) + probability
    return projected


def total_variation(left: dict[Outcome, Fraction], right: dict[Outcome, Fraction]) -> Fraction:
    support = set(left) | set(right)
    return Fraction(1, 2) * sum(
        abs(left.get(key, Fraction(0, 1)) - right.get(key, Fraction(0, 1)))
        for key in support
    )


def fragment_distinguishability(
    law: ConditionalLaw, group: tuple[int, ...]
) -> Fraction:
    return total_variation(marginal(law[0], group), marginal(law[1], group))


def conditionally_factorizes(law: ConditionalLaw, partition: Partition) -> bool:
    """Exact conditional product test over the declared fragment partition."""
    for source in BIT_VALUES:
        group_marginals = [marginal(law[source], group) for group in partition]
        for outcome in product(BIT_VALUES, repeat=MICROCARRIER_COUNT):
            expected = Fraction(1, 1)
            for group, group_rows in zip(partition, group_marginals):
                key = tuple(outcome[index] for index in group)
                expected *= group_rows.get(key, Fraction(0, 1))
            actual = law[source].get(outcome, Fraction(0, 1))
            if actual != expected:
                return False
    return True


def maximum_access_matching(groups: Iterable[tuple[int, ...]]) -> int:
    """Maximum distinct-consumer matching for independently read fragments."""
    declared_groups = tuple(frozenset(group) for group in groups)
    consumers = tuple(sorted(CONSUMER_ACCESS))

    def search(group_index: int, used_consumers: frozenset[str]) -> int:
        if group_index == len(declared_groups):
            return 0
        best = search(group_index + 1, used_consumers)
        group = declared_groups[group_index]
        for consumer in consumers:
            if consumer in used_consumers:
                continue
            if group <= CONSUMER_ACCESS[consumer]:
                best = max(
                    best,
                    1 + search(group_index + 1, used_consumers | {consumer}),
                )
        return best

    return search(0, frozenset())


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {
        "exact": f"{value.numerator}/{value.denominator}",
        "decimal": round(float(value), 9),
    }


def microstate_digest(law: ConditionalLaw, copy_costs: tuple[Fraction, ...]) -> str:
    """Digest the physical fixture inputs while deliberately excluding D."""
    payload = {
        "law": {
            str(source): [
                {
                    "outcome": list(outcome),
                    "probability": f"{probability.numerator}/{probability.denominator}",
                }
                for outcome, probability in sorted(rows.items())
            ]
            for source, rows in sorted(law.items())
        },
        "copy_costs": [f"{value.numerator}/{value.denominator}" for value in copy_costs],
        "consumer_access": {
            consumer: sorted(access) for consumer, access in sorted(CONSUMER_ACCESS.items())
        },
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return f"sha256:{sha256(encoded).hexdigest()}"


def analyze(
    law: ConditionalLaw,
    partition: Partition,
    copy_costs: tuple[Fraction, ...],
    budget: Fraction | None,
) -> dict[str, object]:
    distinguishabilities = [
        fragment_distinguishability(law, group) for group in partition
    ]
    informative_groups = tuple(
        group
        for group, distinguishability in zip(partition, distinguishabilities)
        if distinguishability >= DISTINGUISHABILITY_THRESHOLD
    )
    access_matching = maximum_access_matching(informative_groups)
    strong_independence = conditionally_factorizes(law, partition)
    unpriced_issuance = (
        len(informative_groups) >= REDUNDANCY_THRESHOLD
        and access_matching >= REDUNDANCY_THRESHOLD
        and strong_independence
    )
    total_copy_cost = sum(copy_costs, Fraction(0, 1))
    price_gate = budget is None or total_copy_cost <= budget
    issued = unpriced_issuance and price_gate
    induced_order = list(TARGET_ORDER) if issued else []
    return {
        "partition": [list(group) for group in partition],
        "microstate_digest": microstate_digest(law, copy_costs),
        "fragment_distinguishabilities": [
            fraction_payload(value) for value in distinguishabilities
        ],
        "informative_fragment_count": len(informative_groups),
        "access_matching_size": access_matching,
        "strong_independence": strong_independence,
        "redundancy_threshold": REDUNDANCY_THRESHOLD,
        "distinguishability_threshold": fraction_payload(
            DISTINGUISHABILITY_THRESHOLD
        ),
        "total_copy_cost": fraction_payload(total_copy_cost),
        "budget": None if budget is None else fraction_payload(budget),
        "price_gate": price_gate,
        "unpriced_issuance": unpriced_issuance,
        "issued": issued,
        "induced_order": [list(edge) for edge in induced_order],
        "reproduces_target_order": tuple(induced_order) == TARGET_ORDER,
    }


def prediction_row(
    prediction_id: str, expected: object, actual: object
) -> dict[str, object]:
    return {
        "prediction_id": prediction_id,
        "statement": PRE_REGISTRATIONS[prediction_id],
        "expected": expected,
        "actual": actual,
        "status": "CONFIRMED" if expected == actual else "REFUTED",
    }


def control_row(control_id: str, expected: object, actual: object) -> dict[str, object]:
    return {
        "control_id": control_id,
        "expected": expected,
        "actual": actual,
        "pass": expected == actual,
    }


def verdict(predictions: list[dict[str, object]]) -> str:
    statuses = {row["prediction_id"]: row["status"] for row in predictions}
    if all(value == "CONFIRMED" for value in statuses.values()):
        return "RICHER_FIXTURE_SHARPENS_PARTIAL_DECOMPOSITION_DEPENDENCE"
    if statuses["PR1"] == "CONFIRMED" and statuses["PR2"] == "REFUTED":
        return "RICHER_FIXTURE_REOPENS_S2_TOWARD_SPLIT_ROBUSTNESS"
    return "RICHER_FIXTURE_RESULT_MIXED_REVIEW_ONLY"


def main() -> int:
    independent = independent_copy_law()
    shared = shared_noise_law()
    one_copy = one_copy_law()
    ordinary_costs = (Fraction(1), Fraction(1), Fraction(1))
    high_costs = (Fraction(1), Fraction(1), Fraction(5))

    fine_budget_3 = analyze(independent, FINE_PARTITION, ordinary_costs, Fraction(3))
    merged_budget_3 = analyze(
        independent, MERGED_PARTITION, ordinary_costs, Fraction(3)
    )
    shared_fine = analyze(shared, FINE_PARTITION, ordinary_costs, Fraction(3))
    one_copy_fine = analyze(
        one_copy, FINE_PARTITION, ordinary_costs, Fraction(3)
    )
    relabeled_fine = analyze(
        independent, RELABELED_FINE_PARTITION, ordinary_costs, Fraction(3)
    )
    high_cost_fine = analyze(
        independent, FINE_PARTITION, high_costs, Fraction(3)
    )

    budget_grid = {}
    for budget in (Fraction(2), Fraction(3), Fraction(4)):
        fine = analyze(independent, FINE_PARTITION, ordinary_costs, budget)
        merged = analyze(independent, MERGED_PARTITION, ordinary_costs, budget)
        budget_grid[str(budget)] = {
            "fine_issued": fine["issued"],
            "merged_issued": merged["issued"],
            "invariant_nontrivial": fine["issued"] and merged["issued"],
        }

    predictions = [
        prediction_row(
            "PR1",
            (True, True),
            (
                fine_budget_3["issued"],
                fine_budget_3["reproduces_target_order"],
            ),
        ),
        prediction_row(
            "PR2",
            (True, False, 1),
            (
                fine_budget_3["microstate_digest"]
                == merged_budget_3["microstate_digest"],
                merged_budget_3["issued"],
                merged_budget_3["access_matching_size"],
            ),
        ),
        prediction_row(
            "PR3",
            (3, False, False),
            (
                shared_fine["informative_fragment_count"],
                shared_fine["strong_independence"],
                shared_fine["issued"],
            ),
        ),
        prediction_row(
            "PR4",
            (
                fine_budget_3["issued"],
                fine_budget_3["informative_fragment_count"],
                fine_budget_3["access_matching_size"],
                fine_budget_3["strong_independence"],
            ),
            (
                relabeled_fine["issued"],
                relabeled_fine["informative_fragment_count"],
                relabeled_fine["access_matching_size"],
                relabeled_fine["strong_independence"],
            ),
        ),
        prediction_row(
            "PR5",
            (1, False),
            (
                one_copy_fine["informative_fragment_count"],
                one_copy_fine["issued"],
            ),
        ),
        prediction_row(
            "PR6",
            False,
            any(row["invariant_nontrivial"] for row in budget_grid.values()),
        ),
        prediction_row(
            "PR7",
            (True, False, False),
            (
                high_cost_fine["unpriced_issuance"],
                high_cost_fine["price_gate"],
                high_cost_fine["issued"],
            ),
        ),
    ]

    controls = [
        control_row(
            "C1_all_conditional_laws_normalize",
            True,
            all(law_is_normalized(law) for law in (independent, shared, one_copy)),
        ),
        control_row(
            "C2_declared_partitions_are_disjoint_covers",
            True,
            all(
                partition_is_valid(partition)
                for partition in (
                    FINE_PARTITION,
                    MERGED_PARTITION,
                    RELABELED_FINE_PARTITION,
                )
            ),
        ),
        control_row(
            "C3_same_microstate_across_fine_and_merged",
            fine_budget_3["microstate_digest"],
            merged_budget_3["microstate_digest"],
        ),
        control_row(
            "C4_additive_copy_cost_is_partition_invariant",
            fine_budget_3["total_copy_cost"],
            merged_budget_3["total_copy_cost"],
        ),
        control_row(
            "C5_independent_copy_law_factorizes",
            True,
            fine_budget_3["strong_independence"],
        ),
        control_row(
            "C6_shared_noise_bites_only_after_fragment_screen",
            (3, 3, False),
            (
                shared_fine["informative_fragment_count"],
                shared_fine["access_matching_size"],
                shared_fine["strong_independence"],
            ),
        ),
        control_row(
            "C7_consumer_matching_distinguishes_fine_and_merged",
            (3, 1),
            (
                fine_budget_3["access_matching_size"],
                merged_budget_3["access_matching_size"],
            ),
        ),
    ]

    all_controls_pass = all(row["pass"] for row in controls)
    all_predictions_confirmed = all(
        row["status"] == "CONFIRMED" for row in predictions
    )
    summary = {
        "artifact": "redundancy-issuance-richer-fixture-probe-2026-07-31",
        "scope": (
            "deterministic finite conditional-state fixture; review-only; "
            "no quantum, preferred-frame, claim, canon, or public-posture result"
        ),
        "question": (
            "Does adding multi-consumer conditional states, strong independence, "
            "and additive copy prices remove S2's supplied-decomposition dependence?"
        ),
        "verdict": verdict(predictions),
        "all_predictions_confirmed": all_predictions_confirmed,
        "all_instrument_controls_pass": all_controls_pass,
        "frozen_constants": {
            "redundancy_threshold": REDUNDANCY_THRESHOLD,
            "distinguishability_threshold": fraction_payload(
                DISTINGUISHABILITY_THRESHOLD
            ),
            "ordinary_copy_costs": [
                fraction_payload(value) for value in ordinary_costs
            ],
            "consumer_access": {
                consumer: sorted(access)
                for consumer, access in sorted(CONSUMER_ACCESS.items())
            },
            "target_order": [list(edge) for edge in TARGET_ORDER],
        },
        "primary_comparison": {
            "fine": fine_budget_3,
            "merged": merged_budget_3,
        },
        "negative_controls": {
            "shared_noise_fine": shared_fine,
            "one_copy_fine": one_copy_fine,
            "high_cost_fine": high_cost_fine,
            "relabeled_fine": relabeled_fine,
        },
        "budget_grid": budget_grid,
        "pre_registrations": predictions,
        "instrument_controls": controls,
        "boundary": {
            "earned": (
                "The richer fixture makes nontrivial redundancy and strong "
                "independence executable, but the issuance verdict still flips "
                "when the same microstate is regrouped into one fragment."
            ),
            "not_earned": (
                "No physical privilege for either partition, no derivation of "
                "issuance, and no preferred-frame or new-physics evidence."
            ),
        },
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if all_controls_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
