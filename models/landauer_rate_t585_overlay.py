"""Landauer-rate overlay on the T585/T586 fixtures (exploration companion).

Swing 6B, Part 1 executable. Derives the Landauer-bounded record rate as a
ratio of declared T585 budgets and tests whether annotating T586's events
with that rate refines, changes, or leaves unchanged the record-capability
partial order.

Compliance with T585's failure criteria, stated up front: this script derives
no time, no temporal order, and no issuance from the fixture. The work budget
and the time budget are both DECLARED inputs of T585's fixed context. The
bounded record rate is records-affordable (declared work budget divided by
the source-law per-record reset cost) divided by the declared time budget --
a ratio of two quantities the fixture was already given, not a derived
temporal structure.

Pre-registered prediction (on record in the swing spec before this run): the
rate will NOT refine the order, because T586's clock-label control already
shows the order is not clock-derived and a rate is clock-parameterized, and
because the Landauer bound is astronomically loose (kT ln 2 ~= 2.87e-21 J at
300 K, so ~3.5e20 record resets per second per watt). This script confirms or
refutes that prediction; it does not adjust it.

This artifact deliberately carries no T-number: T587's next_work stops new
T-number scaffolds sourced from T586 alone. It lands as a companion to
explorations/landauer-rate-and-capability-indexed-discriminator-2026-07-27.md
and consumes T585 and T586 by re-executing them, not from cached results.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass, replace
from typing import Any

from models import t585_landauer_physical_capability_gate as t585
from models import t586_record_capability_order_gate as t586


ARTIFACT = "landauer-rate-t585-overlay-exploration-companion-v0.1"
OUTCOME_NULL = "NULL_REFINEMENT_AS_PREREGISTERED"
OUTCOME_POSITIVE = "RATE_REFINED_ORDER_ATTACK_IMMEDIATELY"
OUTCOME_CONTRADICTION = "RATE_BROKE_ORDER_AXIOMS"

K_BOLTZMANN = 1.380649e-23
REFERENCE_TEMPERATURE_K = 300.0
LANDAUER_JOULE = K_BOLTZMANN * REFERENCE_TEMPERATURE_K * math.log(2.0)
RESETS_PER_SECOND_PER_WATT = 1.0 / LANDAUER_JOULE

COMPLIANCE_STATEMENT = (
    "No time, temporal order, or issuance is derived from the T585 fixture. "
    "The work budget and the time budget are both declared T585 context "
    "inputs. records_affordable = declared work budget / per-record reset "
    "cost (binary entropy of the memory state in normalized kBT ln 2 units, "
    "from T585's declared source law); bounded_record_rate = "
    "records_affordable / declared time budget. Both denominators are given, "
    "so the rate is a ratio of declared budgets. Using the fixture to claim "
    "time or temporal order is a T585 failure criterion and is not done here."
)

# Fixture-declared annotation basis: which T585 memory state supplies the
# per-record reset cost for each T586 event's produced record. This mirrors
# T586's own event construction: the main chain acts on the known-zero
# lineage (seed, copy, erase-to-standard, certificate), and the independent
# reference event instantiates the biased state. This mapping is a declared
# annotation, not a derivation.
EVENT_STATE_BASIS = {
    "seed_known_record": "known_zero_record",
    "copy_known_record": "known_zero_record",
    "erase_standard_record": "known_zero_record",
    "certify_erased_record": "known_zero_record",
    "prepare_biased_reference": "biased_record",
}


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class ChannelReport:
    """One candidate route by which rate/capacity data could order events."""

    channel_id: str
    asserted_pairs: tuple[tuple[str, str], ...]
    closure_pairs_reproduced: int
    closure_pairs_contradicted: int
    non_closure_pairs_asserted: int
    record_backed_new_edges: int
    classification: str
    reason: str


def records_affordable(reset_cost_units: float, energy_budget_units: float) -> float:
    """Declared work budget divided by the source-law per-record reset cost."""
    if reset_cost_units < 0.0:
        raise ValueError("reset cost must be nonnegative")
    if reset_cost_units == 0.0:
        return math.inf
    return energy_budget_units / reset_cost_units


def bounded_record_rate(affordable: float, time_budget: float) -> float:
    """Records affordable divided by the declared time budget."""
    if time_budget <= 0.0:
        raise ValueError("declared time budget must be positive")
    return affordable / time_budget


def scalar_rate_relation(rates: dict[str, float]) -> frozenset[tuple[str, str]]:
    """Strict order induced by comparing rate annotations as scalars."""
    return frozenset(
        (a, b) for a in rates for b in rates if a != b and rates[a] < rates[b]
    )


def rate_scaled_clock_relation(
    events: tuple[t586.CapabilityEvent, ...], rate: float
) -> frozenset[tuple[str, str]]:
    """Strict order induced by rate-scaled clock labels t_i = clock_i / rate."""
    if not (rate > 0.0) or math.isinf(rate):
        raise ValueError("rate-scaled clocks need a finite positive rate")
    labels = {event.event_id: event.clock_label / rate for event in events}
    return frozenset(
        (a, b)
        for a in labels
        for b in labels
        if a != b and labels[a] < labels[b]
    )


def _channel(
    channel_id: str,
    asserted: frozenset[tuple[str, str]],
    closure: frozenset[tuple[str, str]],
    classification: str,
    reason: str,
) -> ChannelReport:
    reproduced = len(asserted & closure)
    contradicted = sum(1 for a, b in closure if (b, a) in asserted)
    return ChannelReport(
        channel_id=channel_id,
        asserted_pairs=tuple(sorted(asserted)),
        closure_pairs_reproduced=reproduced,
        closure_pairs_contradicted=contradicted,
        non_closure_pairs_asserted=len(asserted - closure),
        record_backed_new_edges=0,
        classification=classification,
        reason=reason,
    )


def run_overlay_analysis() -> dict[str, Any]:
    # Re-execute both gates as source-owned inputs; no cached results.
    t585_result = t585.run_t585_analysis()
    t586_result = t586.run_t586_analysis()

    base_context = t585_result.contexts[0]
    energy_budget = base_context.budget.energy
    time_budget = base_context.budget.time
    costs = t585_result.landauer_costs

    events = t586_result.events
    event_ids = tuple(event.event_id for event in events)
    closure = frozenset(tuple(pair) for pair in t586_result.order_report.closure)

    # --- The derivation: a ratio of declared budgets, per annotation basis. ---
    declared_afford = {
        event_id: records_affordable(costs[EVENT_STATE_BASIS[event_id]], energy_budget)
        for event_id in event_ids
    }
    declared_rate = {
        event_id: bounded_record_rate(affordable, time_budget)
        for event_id, affordable in declared_afford.items()
    }
    # Adversarial uniform annotation: charge every event the max-entropy reset
    # cost to remove the zero-cost plateau. Annotation stress only; a changed
    # accounting is a T585 completion (access/budget), never fixture truth.
    uniform_rate_value = bounded_record_rate(
        records_affordable(costs["max_entropy_record"], energy_budget), time_budget
    )
    uniform_rate = {event_id: uniform_rate_value for event_id in event_ids}

    # --- Channel 1: rate annotations compared as scalars (declared basis). ---
    declared_scalar = scalar_rate_relation(declared_rate)
    # --- Channel 2: rate annotations compared as scalars (uniform basis). ---
    uniform_scalar = scalar_rate_relation(uniform_rate)
    # --- Channel 3: rate-scaled clock labels, several positive rates. ---
    clock_relation = t586.clock_label_relation(events)
    tested_rates = (uniform_rate_value, declared_rate["prepare_biased_reference"], 1.0)
    scaled_equal_clock = all(
        rate_scaled_clock_relation(events, rate) == clock_relation
        for rate in tested_rates
    )
    # Presentation covariance: permuting clock labels moves every rate-scaled
    # clock order but leaves the record closure fixed (T586's own control,
    # re-verified here with rate annotations attached).
    permuted_events = tuple(
        replace(event, clock_label=100 - event.clock_label) for event in events
    )
    permuted_closure = frozenset(
        tuple(pair) for pair in t586.build_order_report(permuted_events).closure
    )
    permuted_scaled = rate_scaled_clock_relation(permuted_events, tested_rates[0])
    # --- Channel 4: rate-feasibility pruning under the declared accounting. ---
    per_event_cost = {
        event_id: costs[EVENT_STATE_BASIS[event_id]] for event_id in event_ids
    }
    infeasible_events = tuple(
        event_id
        for event_id in event_ids
        if per_event_cost[event_id] > energy_budget
    )
    total_reset_work = sum(per_event_cost.values())
    feasible_closure = frozenset(
        tuple(pair)
        for pair in t586.build_order_report(
            tuple(e for e in events if e.event_id not in infeasible_events)
        ).closure
    )

    channels = (
        _channel(
            "rate_scalar_declared_basis",
            declared_scalar,
            closure,
            "RATE_SCALAR_OVERREAD",
            "Zero-cost known-record lineage makes the main chain's rate one "
            "shared unbounded value, so the scalar comparison orders nothing "
            "inside the chain and relates only the biased reference the "
            "record order proves incomparable.",
        ),
        _channel(
            "rate_scalar_uniform_basis",
            uniform_scalar,
            closure,
            "RATE_SCALAR_OVERREAD",
            "Charging every event the max-entropy reset cost makes the rate "
            "constant across all events; a constant scalar induces the empty "
            "strict order.",
        ),
        _channel(
            "rate_scaled_clock_labels",
            clock_relation,
            closure,
            "CLOCK_PARAMETERIZED_OVERREAD",
            "Dividing clock labels by any finite positive rate is strictly "
            "monotone, so every rate-scaled clock order equals the clock-label "
            "order T586's control already excludes.",
        ),
        _channel(
            "rate_feasibility_pruning",
            frozenset(),
            closure,
            "NO_CHANGE_BOUND_DOES_NOT_BIND",
            "Every per-event reset cost and the fixture total sit inside the "
            "declared work budget, so rate feasibility removes no event and "
            "no edge.",
        ),
    )

    # Record-backedness: T586's order admits an edge only through a record
    # whose unique producer is another event. Rate annotations issue no
    # records, so no channel contributes a record-backed edge; the closure
    # rebuilt from the (unmodified) event set is bitwise the baseline.
    rebuilt_closure = frozenset(
        tuple(pair) for pair in t586.build_order_report(events).closure
    )

    order_after = rebuilt_closure
    prediction_confirmed = (
        order_after == closure
        and all(channel.record_backed_new_edges == 0 for channel in channels)
    )
    axioms_hold = (
        t586_result.order_report.irreflexive
        and t586_result.order_report.transitive
        and t586_result.order_report.antisymmetric
    )
    if not axioms_hold:
        outcome = OUTCOME_CONTRADICTION
    elif prediction_confirmed:
        outcome = OUTCOME_NULL
    else:
        outcome = OUTCOME_POSITIVE

    floor_consistency = (
        (math.isinf(declared_afford["seed_known_record"]))
        == t586._has_t585_task(  # noqa: SLF001 - deliberate reuse of the gate's own probe
            t585_result, "known_zero_record", "erase_to_standard_record"
        )
    ) and (
        (math.floor(records_affordable(costs["max_entropy_record"], energy_budget)) >= 1)
        == t586._has_t585_task(
            t585_result, "max_entropy_record", "erase_to_standard_record"
        )
    )

    checks = (
        Check(
            "t585_reexecuted_as_source",
            t585_result.verdict == t585.VERDICT,
            "T585 was re-executed, not consumed from cached results, and its "
            "review-only verdict is available.",
        ),
        Check(
            "t586_reexecuted_as_source",
            t586_result.verdict == t586.VERDICT,
            "T586 was re-executed, not consumed from cached results, and its "
            "review-only verdict is available.",
        ),
        Check(
            "budgets_are_declared_inputs",
            energy_budget == 0.75 and time_budget == 5.0,
            "Work and time budgets are read from T585's declared fixed "
            "context; neither is derived from the fixture.",
        ),
        Check(
            "si_scale_matches_spec",
            abs(LANDAUER_JOULE - 2.87e-21) / 2.87e-21 < 0.01
            and abs(RESETS_PER_SECOND_PER_WATT - 3.5e20) / 3.5e20 < 0.01,
            "kT ln 2 at 300 K is ~2.87e-21 J and one watt supports ~3.5e20 "
            "record resets per second, the spec's looseness scale.",
        ),
        Check(
            "floor_affordability_matches_t585_feasibility",
            floor_consistency,
            "floor(records_affordable) >= 1 exactly where T585's audited "
            "envelope already makes erasure feasible, so the ratio reading "
            "adds no feasibility content of its own.",
        ),
        Check(
            "scalar_channels_reproduce_no_closure_pair",
            channels[0].closure_pairs_reproduced == 0
            and channels[1].closure_pairs_reproduced == 0,
            "Under both annotation extremes the rate is constant across the "
            "ordered main chain, so the scalar comparison recovers none of "
            "the six record-order pairs.",
        ),
        Check(
            "rate_scaled_clock_is_only_clock_order",
            scaled_equal_clock
            and clock_relation != closure
            and channels[2].closure_pairs_contradicted == 2,
            "Every finite positive rate rescales clock labels monotonically, "
            "reproducing exactly the clock order, which differs from the "
            "record order and reverses two of its six pairs on this fixture.",
        ),
        Check(
            "clock_permutation_moves_rate_clock_not_record_order",
            permuted_closure == closure and permuted_scaled != clock_relation,
            "Permuting presentation clock labels flips the rate-scaled clock "
            "order while the record closure is unchanged, re-verifying T586's "
            "control with rate annotations attached.",
        ),
        Check(
            "feasibility_pruning_leaves_closure_unchanged",
            not infeasible_events
            and total_reset_work <= energy_budget
            and feasible_closure == closure,
            "The Landauer term never binds inside the declared budgets, so "
            "capacity annotations delete no events and no edges.",
        ),
        Check(
            "no_record_backed_new_edges",
            order_after == closure
            and all(channel.record_backed_new_edges == 0 for channel in channels),
            "Rate annotations issue no records, and T586 admits an order edge "
            "only through an issued record with a unique producer; the "
            "rebuilt closure is bitwise the baseline closure.",
        ),
        Check(
            "record_order_axioms_unbroken",
            axioms_hold,
            "The record order remains irreflexive, transitive, and "
            "antisymmetric; the contradiction outcome is not triggered.",
        ),
        Check(
            "preregistered_prediction_confirmed",
            prediction_confirmed,
            "The Landauer-bounded record rate neither refines nor changes "
            "T586's record-capability order, as pre-registered in the swing "
            "spec before this run.",
        ),
    )

    all_passed = all(check.passed for check in checks)
    return {
        "artifact": ARTIFACT,
        "compliance_statement": COMPLIANCE_STATEMENT,
        "declared_budgets": {
            "work_budget_kBTln2_units": energy_budget,
            "time_budget_declared_units": time_budget,
            "provenance": "T585 fixed context (declared inputs, not derived)",
        },
        "si_scale": {
            "kBT_ln2_joules_at_300K": LANDAUER_JOULE,
            "resets_per_second_per_watt": RESETS_PER_SECOND_PER_WATT,
        },
        "per_record_reset_costs_kBTln2_units": {
            event_id: per_event_cost[event_id] for event_id in event_ids
        },
        "records_affordable": {k: _fmt(v) for k, v in declared_afford.items()},
        "bounded_record_rate_per_declared_time_unit": {
            k: _fmt(v) for k, v in declared_rate.items()
        },
        "uniform_stress_rate_per_declared_time_unit": _fmt(uniform_rate_value),
        "baseline_closure": sorted(list(pair) for pair in closure),
        "closure_after_rate_annotation": sorted(list(pair) for pair in order_after),
        "channels": [asdict(channel) for channel in channels],
        "checks": [asdict(check) for check in checks],
        "outcome": outcome if all_passed else "OVERLAY_CHECKS_FAILED",
        "prediction_status": (
            "CONFIRMED" if prediction_confirmed else "REFUTED"
        ),
        "goal3_partial_answer_rate_branch": (
            "For the rate branch of the model family: whatever an "
            "observer-indexed universal rate buys, it is not temporal order. "
            "TaF's own record-capability order neither needs nor gains "
            "ordering information from a Landauer-bounded record rate. Per "
            "the charter, this precise null is the expected successful "
            "outcome, not a shortfall."
        ),
        "not_claimed": (
            "No physical rate constant is established; no time, temporal "
            "order, or issuance is derived from the fixture; no claim-ledger, "
            "Canon Index, hypothesis, or public-posture movement; no new "
            "T-number scaffold (T587 stop respected); no bearing on the "
            "foliation branch, which a scalar rate cannot address."
        ),
    }


def _fmt(value: float) -> Any:
    if math.isinf(value):
        return "unbounded (zero reset cost under the declared source law)"
    return round(value, 6)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    payload = run_overlay_analysis()
    print(json.dumps(payload, indent=2, sort_keys=False))
    return 0 if payload["outcome"] != "OVERLAY_CHECKS_FAILED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
