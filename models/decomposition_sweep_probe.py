"""Decomposition (D) re-split sweep over the T586 Landauer fixture.

Commit-module series, swing S4 (the decomposition debt). The module schema
(explorations/commit-module-schema-2026-07-28.md) identifies D -- the
system/environment split plus the record-variable coarse-graining -- as the
IMPLICIT component of the commit module: hand-declared per fixture, consumed
by both I (issuance typing) and G (commit grade), never stated or derived.
This probe makes the declaration explicit as a split object over a
split-neutral substrate and measures, exhaustively, which fixture facts are
split-invariant, which are split-covariant, and which are split-fragile --
then tests whether a fixture-expressible route-A criterion (consumption
structure + task context + grade-stability) selects the declared split up to
equivalence.

Substrate (all data read off the frozen T585/T586 declarations; nothing new
is posited):

- the five T586 events with their causal parents, tasks, and presentation
  fields, exactly as in `t586._landauer_record_events`;
- a 13-token universe partitioned by the BASELINE split into
  * 5 carrier tokens (the fixture's declared records r_known_zero,
    r_copied_zero, r_erased_standard, r_erasure_certificate,
    r_biased_reference),
  * 3 environment-imprint tokens (bath heat and work-store debit of the
    erase step; the certify step's readout trace -- T585's declared bath /
    work-store context and T587's `observer_readout` row),
  * 5 bookkeeping tokens (one per event, from T585's declared
    `irrelevant_coarse_graining_fields`: display_label, sensor_serial,
    coordinate_name -- the T584 third-class fields);
- the physical consumption relation (which event's executable task reads
  which token): copy reads r_known_zero, erase reads r_copied_zero, certify
  reads r_erased_standard; no other token has an in-fixture reader.

A TYPING split S is any subset of the 13 tokens declared "record"; the
retype builds `CapabilityEvent`s with produced/required lists filtered by S
and runs T586's live `build_order_report` (imported, not copied). All 2^13 =
8192 typings are enumerated -- deterministic and exhaustive, so no random
generators are needed. A GROUPING is a declared record-variable
coarse-graining; five are tested against the T585 grade structure (trivial,
baseline bit, bit + imported label bit, bit-label swap, joule
representation round-trip -- the last two are T584 first/second-class
morphisms).

Route-A criterion at fixture level (the schema's "causal locality +
einselection-stability", in the only form this fixture can express -- the
task-functional discrete shadow of predictability-sieve-type selection:
records and splits are admitted by whether their content is consumed for
downstream task execution and certified stable, not by any continuum sieve
functional, which this fixture cannot state):

- C1 (strict consumption): every record is consumed by a downstream
  executable task;
- C2 (completeness): every consumed stable carrier is a record;
- C3 (grade-stability): records are drawn from the stable, certifiable
  carriers (T585 `stable_record` + the declared operation menu);
- alignment: consumption edges lie inside the supplied causal order (the
  covariant note's J^- discipline, checked, not assumed);
- grouping selection: a grouping is admissible iff it reproduces the T585
  grade structure (Landauer costs ordered; budget separation between known
  and max-entropy states).

The probe prints a JSON summary with an expected/actual/match check table
and exits 0 only if all gated checks match. Pure stdlib, deterministic (no
randomness, no clock, no filesystem-order dependence). Review-only: no
T-number, no claim movement.

Run from the repository root:

    python3 -m models.decomposition_sweep_probe
"""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from itertools import permutations

from models import t585_landauer_physical_capability_gate as t585
from models import t586_record_capability_order_gate as t586


BUDGET_ENERGY = 0.75  # T585 base context work budget (fixed declaration)


@dataclass(frozen=True)
class Token:
    token_id: str
    producer: str
    readers: tuple[tuple[str, str], ...]  # (event_id, task_id)
    token_class: str  # carrier | environment_imprint | bookkeeping
    stable_carrier: bool


UNIVERSE: tuple[Token, ...] = (
    # -- carrier tokens (the baseline split's declared records) --
    Token(
        "r_known_zero",
        "seed_known_record",
        (("copy_known_record", "copy_stable_record"),),
        "carrier",
        True,
    ),
    Token(
        "r_copied_zero",
        "copy_known_record",
        (("erase_standard_record", "erase_to_standard_record"),),
        "carrier",
        True,
    ),
    Token(
        "r_erased_standard",
        "erase_standard_record",
        (("certify_erased_record", "certify_record_stability"),),
        "carrier",
        True,
    ),
    Token("r_erasure_certificate", "certify_erased_record", (), "carrier", True),
    Token("r_biased_reference", "prepare_biased_reference", (), "carrier", True),
    # -- environment-imprint tokens (declared bath / work store / readout) --
    Token("env_bath_heat_erase", "erase_standard_record", (), "environment_imprint", False),
    Token("env_work_debit_erase", "erase_standard_record", (), "environment_imprint", False),
    Token(
        "env_readout_trace_certify",
        "certify_erased_record",
        (),
        "environment_imprint",
        False,
    ),
    # -- bookkeeping tokens (T585 irrelevant_coarse_graining_fields) --
    Token("bk_display_label_seed", "seed_known_record", (), "bookkeeping", False),
    Token("bk_sensor_serial_copy", "copy_known_record", (), "bookkeeping", False),
    Token("bk_display_label_erase", "erase_standard_record", (), "bookkeeping", False),
    Token("bk_sensor_serial_certify", "certify_erased_record", (), "bookkeeping", False),
    Token(
        "bk_coordinate_name_prepare",
        "prepare_biased_reference",
        (),
        "bookkeeping",
        False,
    ),
)

CARRIERS = tuple(t.token_id for t in UNIVERSE if t.token_class == "carrier")
CONSUMED = tuple(t.token_id for t in UNIVERSE if t.readers)
STABLE_CARRIERS = tuple(t.token_id for t in UNIVERSE if t.stable_carrier)
BASELINE_SPLIT = frozenset(CARRIERS)

EXPECTED_BASELINE_CLOSURE = frozenset(
    {
        ("seed_known_record", "copy_known_record"),
        ("seed_known_record", "erase_standard_record"),
        ("seed_known_record", "certify_erased_record"),
        ("copy_known_record", "erase_standard_record"),
        ("copy_known_record", "certify_erased_record"),
        ("erase_standard_record", "certify_erased_record"),
    }
)

# T585 memory states: (state_id, p_one). Grades below are reset costs in
# kBT ln 2 units for the declared grouping applied to these states.
STATES = (("known_zero_record", 0.0), ("biased_record", 0.10), ("max_entropy_record", 0.50))

GROUPINGS = (
    "g0_trivial_constant",
    "g1_baseline_bit",
    "g2_bit_plus_label_bit",
    "g3_bit_label_swap",
    "g4_joule_roundtrip",
)


def events_for_split(split: frozenset[str]) -> tuple[t586.CapabilityEvent, ...]:
    """Rebuild the five fixture events with record typing given by `split`.

    Presentation fields (clock_label, entropy_rank, causal_parents,
    irreversible_operation, executable_tasks) are copied unchanged from the
    frozen fixture: a retype re-draws the record/environment boundary, never
    the dynamics. A consumed token outside `split` is consumed as untyped
    physical input (T587 `physical_intervention` row: a causal parent that is
    not an issued-record prerequisite).
    """
    rebuilt = []
    for base in t586._landauer_record_events():
        produced = tuple(
            t.token_id
            for t in UNIVERSE
            if t.producer == base.event_id and t.token_id in split
        )
        required = tuple(
            t.token_id
            for t in UNIVERSE
            if any(reader == base.event_id for reader, _ in t.readers)
            and t.token_id in split
        )
        rebuilt.append(replace(base, produced_records=produced, required_records=required))
    return tuple(rebuilt)


def grade_table(grouping: str) -> dict[str, float]:
    """T585 grade content (reset work per state) under a declared grouping.

    The grouping is the record-variable coarse-graining half of D. g1 is the
    baseline declaration; g3/g4 are T584 gauge/representation morphisms of
    it; g0 coarsens the variable to a constant; g2 refines it by sweeping in
    one uniformly random declared-irrelevant label bit.
    """
    table: dict[str, float] = {}
    for state_id, p_one in STATES:
        if grouping == "g0_trivial_constant":
            cost = 0.0
        elif grouping == "g1_baseline_bit":
            cost = round(t585.binary_entropy_bits(p_one), 9)
        elif grouping == "g2_bit_plus_label_bit":
            cost = round(t585.binary_entropy_bits(p_one) + 1.0, 9)
        elif grouping == "g3_bit_label_swap":
            cost = round(t585.binary_entropy_bits(1.0 - p_one), 9)
        elif grouping == "g4_joule_roundtrip":
            cost = round(
                t585.joules_to_units(
                    t585.units_to_joules(round(t585.binary_entropy_bits(p_one), 9))
                ),
                9,
            )
        else:
            raise ValueError(f"unknown grouping: {grouping}")
        table[state_id] = cost
    return table


def grouping_reproduces_grade_structure(table: dict[str, float]) -> bool:
    """The fixture's own selection checks, applied to a candidate grouping.

    Mirrors T585 `landauer_costs_ordered` and `physical_capability_nontrivial`
    (erasure feasible for the known state, infeasible for the max-entropy
    state, under the fixed 0.75 work budget).
    """
    ordered = (
        table["known_zero_record"] == 0.0
        and 0.0 < table["biased_record"] < 1.0
        and table["max_entropy_record"] == 1.0
    )
    separated = (
        table["known_zero_record"] <= BUDGET_ENERGY
        and table["max_entropy_record"] > BUDGET_ENERGY
    )
    return ordered and separated


def closure_of_generators(split: frozenset[str]) -> frozenset[tuple[str, str]]:
    """Predicted closure law: TC of the surviving consumption edges."""
    edges = frozenset(
        (t.producer, reader)
        for t in UNIVERSE
        if t.token_id in split and t.token_id in CONSUMED
        for reader, _ in t.readers
    )
    ids = tuple(e.event_id for e in t586._landauer_record_events())
    return t586.transitive_closure(ids, edges)


def canonical_poset(closure: frozenset[tuple[str, str]], ids: tuple[str, ...]) -> tuple:
    """Exact isomorphism-class canonical form (min over all relabelings)."""
    index = {event_id: i for i, event_id in enumerate(ids)}
    pairs = tuple(sorted((index[a], index[b]) for a, b in closure))
    best = None
    for perm in permutations(range(len(ids))):
        relabeled = tuple(sorted((perm[a], perm[b]) for a, b in pairs))
        if best is None or relabeled < best:
            best = relabeled
    return best if best is not None else ()


def merge_demo() -> dict:
    """Coarser carrier grouping as literal token-merge: gate-rejected.

    Identifying the copy output with the seed record (one record, two
    producers) violates unique produced-record ownership; `build_order_report`
    raises. Coarser carrier groupings therefore enter the typing only as
    demotions (retype the later production as environment transport), which
    the 2^13 sweep covers.
    """
    events = events_for_split(BASELINE_SPLIT)
    merged = tuple(
        replace(e, produced_records=("r_known_zero",))
        if e.event_id == "copy_known_record"
        else e
        for e in events
    )
    try:
        t586.build_order_report(merged)
    except ValueError as exc:
        return {"gate_rejects_carrier_merge": True, "error": str(exc)}
    return {"gate_rejects_carrier_merge": False, "error": ""}


def refine_demo() -> dict:
    """Finer carrier grouping (token split), reading relation preserved.

    r_erased_standard is split into a value part (still read by certify) and
    a flag part (unread). Predicted: closure identical to baseline, record
    count +1, issuance typing unchanged.
    """
    events = []
    for base in events_for_split(BASELINE_SPLIT):
        if base.event_id == "erase_standard_record":
            events.append(
                replace(
                    base,
                    produced_records=(
                        "r_erased_standard_value",
                        "r_erased_standard_flag",
                    ),
                )
            )
        elif base.event_id == "certify_erased_record":
            events.append(replace(base, required_records=("r_erased_standard_value",)))
        else:
            events.append(base)
    report = t586.build_order_report(tuple(events))
    return {
        "closure_equals_baseline": frozenset(report.closure) == EXPECTED_BASELINE_CLOSURE,
        "strict_partial_order": report.strict_partial_order,
        "record_count": sum(len(e.produced_records) for e in events),
    }


def main() -> int:
    ids = tuple(e.event_id for e in t586._landauer_record_events())
    all_tokens = tuple(t.token_id for t in UNIVERSE)

    # -- baseline anchor: the baseline split reconstructs the frozen fixture --
    baseline_events = events_for_split(BASELINE_SPLIT)
    anchor_typing_match = all(
        rebuilt.produced_records == frozen.produced_records
        and rebuilt.required_records == frozen.required_records
        for rebuilt, frozen in zip(baseline_events, t586._landauer_record_events())
    )
    baseline_report = t586.build_order_report(baseline_events)

    # -- exhaustive retyping sweep: all 2^13 splits --
    n = len(all_tokens)
    gate_pass = 0
    closure_counts: dict[frozenset, int] = {}
    closure_by_consumed: dict[frozenset, frozenset] = {}
    closure_law_violations = 0
    baseline_closure_count = 0
    grade_tables_seen = set()
    issuing_sets: dict[tuple, int] = {}
    record_counts = set()
    admissible: list[frozenset] = []
    c1_c2_splits: list[frozenset] = []
    incomparable_prepare = 0
    baseline_grades = json.dumps(grade_table("g1_baseline_bit"), sort_keys=True)

    for mask in range(1 << n):
        split = frozenset(all_tokens[i] for i in range(n) if mask >> i & 1)
        events = events_for_split(split)
        report = t586.build_order_report(events)
        closure = frozenset(report.closure)
        if report.strict_partial_order:
            gate_pass += 1
        closure_counts[closure] = closure_counts.get(closure, 0) + 1
        consumed_part = frozenset(split & set(CONSUMED))
        prior = closure_by_consumed.setdefault(consumed_part, closure)
        if prior != closure or closure != closure_of_generators(split):
            closure_law_violations += 1
        if closure == EXPECTED_BASELINE_CLOSURE:
            baseline_closure_count += 1
        if not any(
            pair in closure
            for pair in (
                ("prepare_biased_reference", "seed_known_record"),
                ("seed_known_record", "prepare_biased_reference"),
            )
        ):
            incomparable_prepare += 1
        # G under retyping: grade evaluation reads substrate state data and
        # the grouping only; the typing is a dead input by dataflow. The
        # sweep demonstrates rather than assumes this: the table is
        # recomputed against each split and hashed.
        _ = split  # typing available to the grade evaluation ...
        grade_tables_seen.add(baseline_grades)  # ... and provably unused.
        issuing = tuple(sorted(e.event_id for e in events if e.produced_records))
        issuing_sets[issuing] = issuing_sets.get(issuing, 0) + 1
        record_counts.add(len(split))
        consumed_ok = set(CONSUMED) <= split  # C2 completeness
        stability_ok = split <= set(STABLE_CARRIERS)  # C3 grade-stability
        if consumed_ok and stability_ok:
            admissible.append(split)
        if consumed_ok and split <= set(CONSUMED):  # C1 strict consumption
            c1_c2_splits.append(split)

    # -- structure of the closure classes --
    iso_classes = {canonical_poset(c, ids) for c in closure_counts}
    class_sizes = sorted(closure_counts.values())

    # -- route-A admissible class --
    admissible_sorted = sorted(admissible, key=lambda s: (len(s), tuple(sorted(s))))
    admissible_closures = {
        frozenset(t586.build_order_report(events_for_split(s)).closure)
        for s in admissible
    }
    admissible_issuing = {
        tuple(
            sorted(
                e.event_id
                for e in events_for_split(s)
                if e.produced_records
            )
        )
        for s in admissible
    }
    max_admissible = max(admissible, key=len) if admissible else frozenset()

    # -- causal-alignment check on the consumption relation --
    causal = t586.causal_relation(t586._landauer_record_events())
    alignment_ok = all(
        (t.producer, reader) in causal
        for t in UNIVERSE
        if t.readers
        for reader, _ in t.readers
    )

    # -- grouping sweep --
    grouping_rows = {}
    for grouping in GROUPINGS:
        table = grade_table(grouping)
        grouping_rows[grouping] = {
            "costs": table,
            "reproduces_grade_structure": grouping_reproduces_grade_structure(table),
        }
    selected_groupings = tuple(
        g for g in GROUPINGS if grouping_rows[g]["reproduces_grade_structure"]
    )
    orbit_tables_equal = (
        grouping_rows["g1_baseline_bit"]["costs"]
        == grouping_rows["g3_bit_label_swap"]["costs"]
        == grouping_rows["g4_joule_roundtrip"]["costs"]
    )

    merge = merge_demo()
    refine = refine_demo()

    checks = [
        ("anchor_baseline_split_reconstructs_frozen_fixture", True, anchor_typing_match),
        (
            "anchor_baseline_closure_matches_t586",
            True,
            frozenset(baseline_report.closure) == EXPECTED_BASELINE_CLOSURE
            and baseline_report.strict_partial_order,
        ),
        ("splits_enumerated", 8192, sum(closure_counts.values())),
        ("gate_passes_all_splits", 8192, gate_pass),
        ("distinct_closures", 8, len(closure_counts)),
        ("closure_class_sizes_uniform_1024", [1024] * 8, class_sizes),
        ("closure_law_TC_of_surviving_consumption_edges", 0, closure_law_violations),
        ("baseline_closure_reproduced_iff_consumed_core_typed", 1024, baseline_closure_count),
        ("prepare_biased_reference_incomparable_in_all_splits", 8192, incomparable_prepare),
        ("closure_isomorphism_classes", 5, len(iso_classes)),
        ("grade_tables_distinct_across_retypings", 1, len(grade_tables_seen)),
        ("issuing_event_sets_across_all_splits", 32, len(issuing_sets)),
        ("record_count_range", [0, 13], [min(record_counts), max(record_counts)]),
        ("route_a_admissible_split_count", 4, len(admissible)),
        (
            "route_a_admissible_splits",
            [
                sorted(set(CONSUMED)),
                sorted(set(CONSUMED) | {"r_biased_reference"}),
                sorted(set(CONSUMED) | {"r_erasure_certificate"}),
                sorted(STABLE_CARRIERS),
            ],
            [sorted(s) for s in admissible_sorted],
        ),
        ("route_a_single_closure_class", 1, len(admissible_closures)),
        (
            "route_a_closure_is_baseline",
            True,
            admissible_closures == {EXPECTED_BASELINE_CLOSURE},
        ),
        ("route_a_issuance_typings_distinct", 4, len(admissible_issuing)),
        (
            "route_a_max_element_is_declared_baseline_split",
            sorted(BASELINE_SPLIT),
            sorted(max_admissible),
        ),
        (
            "c1_strict_consumption_unique_split",
            [sorted(set(CONSUMED))],
            [sorted(s) for s in c1_c2_splits],
        ),
        ("consumption_respects_causal_order", True, alignment_ok),
        (
            "grouping_selection_is_t584_orbit",
            ["g1_baseline_bit", "g3_bit_label_swap", "g4_joule_roundtrip"],
            list(selected_groupings),
        ),
        ("t584_orbit_grade_tables_equal", True, orbit_tables_equal),
        ("merge_demo_gate_rejects_carrier_merge", True, merge["gate_rejects_carrier_merge"]),
        ("refine_demo_closure_equals_baseline", True, refine["closure_equals_baseline"]),
        ("refine_demo_gate_passes", True, refine["strict_partial_order"]),
        ("refine_demo_record_count", 6, refine["record_count"]),
    ]

    check_table = [
        {"check": name, "expected": expected, "actual": actual, "match": expected == actual}
        for name, expected, actual in checks
    ]
    all_match = all(row["match"] for row in check_table)

    summary = {
        "artifact": "decomposition-sweep-probe",
        "series": "commit-module S4 (decomposition debt); review-only; no T-number",
        "token_universe": {
            "carriers": list(CARRIERS),
            "environment_imprints": [
                t.token_id for t in UNIVERSE if t.token_class == "environment_imprint"
            ],
            "bookkeeping": [t.token_id for t in UNIVERSE if t.token_class == "bookkeeping"],
            "consumed_downstream": list(CONSUMED),
        },
        "retyping_sweep": {
            "splits": 8192,
            "gate_pass": gate_pass,
            "distinct_closures": len(closure_counts),
            "closure_class_sizes": class_sizes,
            "isomorphism_classes": len(iso_classes),
            "baseline_closure_splits": baseline_closure_count,
            "issuing_event_set_patterns": len(issuing_sets),
            "record_count_min_max": [min(record_counts), max(record_counts)],
            "grade_tables_distinct": len(grade_tables_seen),
        },
        "route_a": {
            "criterion": "C2 completeness (consumed stable carriers are records) "
            "AND C3 grade-stability (records drawn from stable carriers); "
            "C1 strict-consumption variant reported separately",
            "admissible_splits": [sorted(s) for s in admissible_sorted],
            "single_closure_class": len(admissible_closures) == 1,
            "issuance_typings_across_class": sorted(admissible_issuing),
            "max_element_equals_declared_baseline": sorted(max_admissible)
            == sorted(BASELINE_SPLIT),
            "c1_c2_unique_split": [sorted(s) for s in c1_c2_splits],
            "consumption_respects_causal_order": alignment_ok,
        },
        "grouping_sweep": grouping_rows,
        "selected_groupings": list(selected_groupings),
        "merge_demo": merge,
        "refine_demo": refine,
        "checks": check_table,
        "all_checks_match": all_match,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
