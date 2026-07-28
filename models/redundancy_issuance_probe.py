"""Redundancy-issuance probe for commit-module swing 2 (Debt L1, repair route 2).

Registered kill under test (commit-module-schema-2026-07-28.md, Debt L1):
"redundancy-issuance must reproduce the T586 record order on causally-aligned
fixtures without consuming D."

The probe operationalizes an SBS/strong-quantum-Darwinism-class redundancy
condition (N10's primary set: Korbicz-Horodecki-Horodecki 2014; Horodecki et
al. 2015; Brandao-Piani-Horodecki 2015; Le & Olaya-Castro 2019; Korbicz 2021)
for the finite classical-abstract T586 fixture class, mechanism-preserving:

    an event issues a record iff a declared discrete outcome variable of the
    event is (a) imprinted in >= R stable carriers outside the source
    (fragment redundancy), (b) independently consumable by distinct
    downstream tasks without mutual disturbance (objectivity), and
    optionally (c) stable under the fixture's admissible operations
    (flagged: grade content -- the I->G edge).

Decomposition inputs (D) are explicit and varied over an admissible class:

  - coarse-graining (which tokens are carriers of one outcome variable):
      token_level  -- each produced record its own variable (finest);
      event_level  -- one variable per producing event, carriers = its tokens;
      provenance_level -- event_level plus copy-task attribution: a token
          produced by a copy-type task (task id starting with "copy",
          exactly one required record) is a carrier of the SOURCE token's
          variable, transitively (SBS reading: a copy proliferates an
          existing pointer variable; it does not originate one).
  - fragment partition (which carriers count as independently accessible
      fragments): finest (one block per carrier), single_block (all carriers
      one fragment), seeded random partitions. R counts nonempty blocks.

It then runs the reproduction test:

  1. class screen -- the eleven T587 boundary-input classes (profiles
     declared from T587's own reason lines) against the redundancy condition;
     coextension with T587's live admitted set at R=1 and R=2;
  2. frozen T586 fixture -- issuance sets and induced record-order closures
     per (grouping, R) cell, plus the certified-stability variant of (c);
  3. fixture family -- the sweep's causally-aligned regimes (i)
     record_equals_causal and (ii) record_strict_subset_causal, reusing
     fixture_family_sweep's generators and seeds verbatim (200 fixtures per
     regime); regime (iii) is excluded by the series' carried scope entry
     (causal alignment binds every reproduction target);
  4. copy-augmented subfamily -- the first 60 regime-(ii) fixtures with a
     record edge get one seeded copy event inserted, so the family exhibits
     the copy/provenance structure the frozen fixture has and the plain
     family lacks;
  5. split-stability probe -- issuance-set and closure stability under the
     admissible D variations, at R=1 and R=2.

Pure stdlib, deterministic: all randomness from random.Random seeded with
the fixed literals below; no clock, date, or filesystem-order dependence.
Prints a JSON summary with an expected/actual/match check table; theorem
confirmations and hand-derivable values are gated; empirical rates are
reported as measurements, not gated. Exits 0 iff all gated checks match.

Run from the repository root:

    python3 -m models.redundancy_issuance_probe
"""

from __future__ import annotations

import json
from dataclasses import replace
from random import Random

from models import fixture_family_sweep as sweep
from models import t586_record_capability_order_gate as t586
from models import t587_t586_causal_collapse_boundary_attack as t587

PARTITION_SEED = 61001
AUGMENT_SEED_BASE = 61002
SEEDED_PARTITION_BASE = 61003
AUGMENT_COUNT = 60
GROUPINGS = ("token_level", "event_level", "provenance_level")
ALIGNED_REGIMES = ("record_equals_causal", "record_strict_subset_causal")


# ---------------------------------------------------------------------------
# Decomposition inputs: coarse-graining (variable map) and fragment partition
# ---------------------------------------------------------------------------


def _producer_map(events):
    producers = {}
    for event in events:
        for record_id in event.produced_records:
            producers[record_id] = event.event_id
    return producers


def _is_copy_event(event):
    return (
        any(task.startswith("copy") for task in event.executable_tasks)
        and len(event.required_records) == 1
        and len(event.produced_records) >= 1
    )


def variable_map(events, grouping):
    """Return {variable_id: {"origin": event_id, "carriers": [record_ids]}}.

    variable_id is the root token (token/provenance level) or the origin
    event id (event level); origin is the event whose outcome the variable
    coarse-grains.
    """
    producers = _producer_map(events)
    if grouping == "token_level":
        return {
            record_id: {"origin": producers[record_id], "carriers": [record_id]}
            for record_id in sorted(producers)
        }
    if grouping == "event_level":
        variables = {}
        for record_id in sorted(producers):
            origin = producers[record_id]
            variables.setdefault(origin, {"origin": origin, "carriers": []})
            variables[origin]["carriers"].append(record_id)
        return variables
    if grouping == "provenance_level":
        root = {record_id: record_id for record_id in producers}
        changed = True
        while changed:
            changed = False
            for event in events:
                if not _is_copy_event(event):
                    continue
                source = event.required_records[0]
                if source not in root:
                    continue
                for record_id in event.produced_records:
                    if root[record_id] != root[source]:
                        root[record_id] = root[source]
                        changed = True
        grouped = {}
        for record_id in sorted(producers):
            root_token = root[record_id]
            key = producers[root_token]
            grouped.setdefault(
                key, {"origin": producers[root_token], "carriers": []}
            )
            grouped[key]["carriers"].append(record_id)
        return grouped
    raise ValueError(f"unknown grouping: {grouping}")


def finest_partition(carriers, rng=None):
    return [[carrier] for carrier in carriers]


def single_block_partition(carriers, rng=None):
    return [list(carriers)]


def seeded_partition(carriers, rng):
    pool = list(carriers)
    rng.shuffle(pool)
    block_count = rng.randint(1, len(pool))
    blocks = [[] for _ in range(block_count)]
    for index, carrier in enumerate(pool):
        blocks[index % block_count].append(carrier)
    return [block for block in blocks if block]


# ---------------------------------------------------------------------------
# The operationalized condition and the induced record order
# ---------------------------------------------------------------------------


def issued_variables(variables, threshold, partition_fn=finest_partition, rng=None):
    issued = set()
    for variable_id in sorted(variables):
        carriers = variables[variable_id]["carriers"]
        blocks = partition_fn(carriers, rng)
        fragments = sum(1 for block in blocks if block)
        if fragments >= threshold:
            issued.add(variable_id)
    return issued


def issued_events(variables, issued):
    return frozenset(variables[variable_id]["origin"] for variable_id in issued)


def consumers_map(events):
    """token -> consumer event ids; the consumer must declare an executable
    task (the T586 task-typing wrinkle: no task, no edge)."""
    consumers = {}
    for event in events:
        if not event.executable_tasks:
            continue
        for record_id in event.required_records:
            consumers.setdefault(record_id, []).append(event.event_id)
    return consumers


def induced_closure(events, variables, issued):
    ids = tuple(event.event_id for event in events)
    consumers = consumers_map(events)
    edges = set()
    for variable_id in issued:
        origin = variables[variable_id]["origin"]
        for carrier in variables[variable_id]["carriers"]:
            for consumer in consumers.get(carrier, ()):
                if consumer != origin:
                    edges.add((origin, consumer))
    return t586.transitive_closure(ids, frozenset(edges))


def producing_events(events):
    return frozenset(
        event.event_id for event in events if event.produced_records
    )


# ---------------------------------------------------------------------------
# Part A: class screen (typing coextension on T587's eleven boundary classes)
# ---------------------------------------------------------------------------

# Profiles are declared from T587's own reason lines (quoted in the results
# note); fields: discrete_outcome -- a frozen discrete outcome variable
# exists; carriers -- stable consumable tokens the event natively imprints
# its outcome into; nondisturbing_multi_access -- carriers are readable by
# distinct downstream tasks without disturbing each other or the source.
CLASS_PROFILES = {
    # "A stable produced record with a unique producer may support a
    # task-prerequisite edge."
    "physical_record_production": (True, 1, True),
    # "Changing who can read a record changes access; it does not issue a
    # new produced record."
    "access_change": (True, 0, False),
    # "A changed envelope is evidence for capability comparison ..."
    "capability_change": (True, 0, False),
    # "Choosing a boundary or section is a metatheoretic selection unless
    # the source model issues a record token."
    "final_boundary_selection": (True, 0, False),
    # "Readout may reveal a record; readout alone is not native record
    # production." (no new carrier; access is observer-private)
    "observer_readout": (True, 0, False),
    # "An intervention can be a causal parent without being an
    # issued-record prerequisite."
    "physical_intervention": (True, 0, False),
    # "Feedback counts only when the model emits a stable record consumed
    # by a later executable task." (bare exemplar: no emitted record)
    "autonomous_feedback": (True, 0, False),
    # "Edge or defect degrees of freedom are source variables until an
    # issuance rule turns them into records." (variable exists, unimprinted)
    "edge_defect_degrees_of_freedom": (True, 0, False),
    # "Continuous flux must be discretized or recorded ... before it can
    # enter the record order." (no frozen discrete packet)
    "continuous_source_flux": (False, 0, False),
    # "Random input is not a record-order source unless the sampled outcome
    # is issued as a stable record." (sample discrete, not imprinted)
    "stochastic_input": (True, 0, False),
    # "A source-owned issuance rule is the explicit bridge from physical
    # input to produced-record prerequisite."
    "native_record_issuance_rule": (True, 1, True),
}


def class_screen(threshold):
    admitted = set()
    for class_id, profile in CLASS_PROFILES.items():
        discrete, carriers, nondisturbing = profile
        if discrete and carriers >= threshold and (carriers == 0 or nondisturbing):
            admitted.add(class_id)
    return admitted


def t587_admitted_classes():
    return {
        item.class_id
        for item in t587._boundary_input_classes()
        if item.counts_as_record_source
    }


# ---------------------------------------------------------------------------
# Part B: frozen T586 fixture
# ---------------------------------------------------------------------------


def certified_tokens(events):
    """Tokens with an in-fixture stability certification: required by an
    event whose executable task is certify_record_stability (T585's
    stability-as-task operationalization of 'stable')."""
    certified = set()
    for event in events:
        if "certify_record_stability" in event.executable_tasks:
            certified.update(event.required_records)
    return certified


def frozen_fixture_cells():
    events = t586._landauer_record_events()
    target = frozenset(t586.build_order_report(events).closure)
    cells = {}
    for grouping in GROUPINGS:
        variables = variable_map(events, grouping)
        for threshold in (1, 2):
            for partition_name, partition_fn in (
                ("finest", finest_partition),
                ("single_block", single_block_partition),
            ):
                issued = issued_variables(variables, threshold, partition_fn)
                closure = induced_closure(events, variables, issued)
                max_carriers = max(
                    (len(variables[v]["carriers"]) for v in issued), default=0
                )
                cells[f"{grouping}|R{threshold}|{partition_name}"] = {
                    "issued_events": sorted(issued_events(variables, issued)),
                    "closure_pairs": len(closure),
                    "reproduces": closure == target,
                    "max_issued_carrier_count": max_carriers,
                }
    variables_token = variable_map(events, "token_level")
    certified = certified_tokens(events)
    issued_cert = {
        variable_id
        for variable_id in issued_variables(variables_token, 1)
        if set(variables_token[variable_id]["carriers"]) & certified
    }
    closure_cert = induced_closure(events, variables_token, issued_cert)
    cells["token_level|R1|certified_stability"] = {
        "issued_events": sorted(issued_events(variables_token, issued_cert)),
        "closure_pairs": len(closure_cert),
        "reproduces": closure_cert == target,
        "max_issued_carrier_count": 1 if issued_cert else 0,
    }
    return events, target, cells


# ---------------------------------------------------------------------------
# Part C: causally-aligned fixture family (sweep generators, verbatim seeds)
# ---------------------------------------------------------------------------


def regime_fixtures(regime):
    rng = Random(sweep.REGIME_SEEDS[regime])
    fixtures = []
    for index in range(sweep.FIXTURES_PER_REGIME):
        n = sweep.EVENT_SIZES[index % len(sweep.EVENT_SIZES)]
        fixture = None
        while fixture is None:
            fixture = sweep.generate_fixture(regime, rng, n)
        fixtures.append(fixture)
    return fixtures


def analyze_family_fixture(fixture, seeded_rng):
    events = sweep.make_events(
        fixture["n"], fixture["causal_edges"], fixture["record_edges"]
    )
    target = frozenset(t586.build_order_report(events).closure)
    producing = producing_events(events)
    row = {"target_empty": not target}
    issued_sets_r1 = {}
    for grouping in GROUPINGS:
        variables = variable_map(events, grouping)
        for threshold in (1, 2):
            issued = issued_variables(variables, threshold)
            closure = induced_closure(events, variables, issued)
            key = f"{grouping}_r{threshold}"
            row[f"{key}_reproduces"] = closure == target
            row[f"{key}_vacuous"] = not target
            if threshold == 2 and target:
                row[f"{key}_coverage"] = len(closure & target) / len(target)
            if threshold == 1:
                issued_sets_r1[grouping] = issued_events(variables, issued)
                row[f"{key}_issued_equals_producing"] = (
                    issued_events(variables, issued) == producing
                )
        # split-stability at the fragment-partition axis (event grouping is
        # where family carrier multiplicity lives)
        if grouping == "event_level":
            issued_f1 = issued_variables(variables, 1, finest_partition)
            issued_s1 = issued_variables(variables, 1, single_block_partition)
            issued_r1_seeded = issued_variables(
                variables, 1, seeded_partition, seeded_rng
            )
            row["r1_partition_invariant"] = issued_f1 == issued_s1 == issued_r1_seeded
            issued_f2 = issued_variables(variables, 2, finest_partition)
            issued_s2 = issued_variables(variables, 2, single_block_partition)
            issued_r2_seeded = issued_variables(
                variables, 2, seeded_partition, seeded_rng
            )
            row["r2_partition_fragile_extremes"] = issued_f2 != issued_s2
            row["r2_partition_fragile_seeded"] = issued_f2 != issued_r2_seeded
            row["r2_nonvacuous_reproduction_survives_single_block"] = (
                bool(target)
                and row["event_level_r2_reproduces"]
                and induced_closure(events, variables, issued_s2) == target
            )
    row["prov_equals_event_issued_r1"] = (
        issued_sets_r1["provenance_level"] == issued_sets_r1["event_level"]
    )
    row["has_multicarrier_event"] = any(
        len(info["carriers"]) >= 2
        for info in variable_map(events, "event_level").values()
    )
    return row


def run_family():
    per_regime = {}
    for regime in ALIGNED_REGIMES:
        fixtures = regime_fixtures(regime)
        rows = []
        for index, fixture in enumerate(fixtures):
            seeded_rng = Random(SEEDED_PARTITION_BASE + index)
            rows.append(analyze_family_fixture(fixture, seeded_rng))
        per_regime[regime] = rows
    return per_regime


def summarize_family(rows):
    count = len(rows)
    summary = {"fixtures": count, "empty_record_closure": sum(r["target_empty"] for r in rows)}
    for grouping in GROUPINGS:
        for threshold in (1, 2):
            key = f"{grouping}_r{threshold}"
            summary[f"{key}_reproduces"] = sum(r[f"{key}_reproduces"] for r in rows)
            if threshold == 2:
                summary[f"{key}_reproduces_nonvacuous"] = sum(
                    r[f"{key}_reproduces"] and not r["target_empty"] for r in rows
                )
                coverages = sorted(
                    r[f"{key}_coverage"] for r in rows if f"{key}_coverage" in r
                )
                if coverages:
                    mid = len(coverages) // 2
                    median = (
                        coverages[mid]
                        if len(coverages) % 2
                        else (coverages[mid - 1] + coverages[mid]) / 2
                    )
                    summary[f"{key}_coverage_min_median_max"] = [
                        round(coverages[0], 4),
                        round(median, 4),
                        round(coverages[-1], 4),
                    ]
    summary["token_r1_issued_equals_producing"] = sum(
        r["token_level_r1_issued_equals_producing"] for r in rows
    )
    summary["event_r1_issued_equals_producing"] = sum(
        r["event_level_r1_issued_equals_producing"] for r in rows
    )
    summary["prov_equals_event_issued_r1"] = sum(
        r["prov_equals_event_issued_r1"] for r in rows
    )
    summary["r1_partition_invariant"] = sum(r["r1_partition_invariant"] for r in rows)
    summary["has_multicarrier_event"] = sum(r["has_multicarrier_event"] for r in rows)
    summary["r2_partition_fragile_extremes"] = sum(
        r["r2_partition_fragile_extremes"] for r in rows
    )
    summary["r2_partition_fragile_seeded"] = sum(
        r["r2_partition_fragile_seeded"] for r in rows
    )
    summary["r2_nonvacuous_reproduction_survives_single_block"] = sum(
        r["r2_nonvacuous_reproduction_survives_single_block"] for r in rows
    )
    return summary


# ---------------------------------------------------------------------------
# Part D: copy-augmented subfamily (regime ii + one seeded copy event each)
# ---------------------------------------------------------------------------


def augment_with_copy(fixture, index):
    if not fixture["record_edges"]:
        return None
    rng = Random(AUGMENT_SEED_BASE + index)
    events = list(
        sweep.make_events(
            fixture["n"], fixture["causal_edges"], fixture["record_edges"]
        )
    )
    a, b = fixture["record_edges"][rng.randrange(len(fixture["record_edges"]))]
    source_token = f"r_{a}_{b}"
    copy_token = f"r_copy_{a}_{b}"
    copy_id = f"ev_copy_{a}_{b}"
    consumer_index = next(
        i for i, event in enumerate(events) if event.event_id == f"ev{b}"
    )
    consumer = events[consumer_index]
    events[consumer_index] = replace(
        consumer,
        required_records=tuple(
            copy_token if record_id == source_token else record_id
            for record_id in consumer.required_records
        ),
        causal_parents=consumer.causal_parents + (copy_id,),
    )
    events.append(
        t586.CapabilityEvent(
            event_id=copy_id,
            produced_records=(copy_token,),
            required_records=(source_token,),
            executable_tasks=("copy_stable_record",),
            clock_label=100,
            entropy_rank=9.9,
            causal_parents=(f"ev{a}",),
            irreversible_operation=False,
        )
    )
    return tuple(events), copy_id, f"ev{a}"


def run_augmented(regime_ii_fixtures):
    rows = []
    index = 0
    for fixture in regime_ii_fixtures:
        if len(rows) >= AUGMENT_COUNT:
            break
        augmented = augment_with_copy(fixture, index)
        index += 1
        if augmented is None:
            continue
        events, copy_id, origin_id = augmented
        target = frozenset(t586.build_order_report(events).closure)
        strict = t586.build_order_report(events).strict_partial_order
        variables_token = variable_map(events, "token_level")
        variables_prov = variable_map(events, "provenance_level")
        issued_token_r1 = issued_variables(variables_token, 1)
        issued_prov_r1 = issued_variables(variables_prov, 1)
        closure_token_r1 = induced_closure(events, variables_token, issued_token_r1)
        closure_prov_r1 = induced_closure(events, variables_prov, issued_prov_r1)
        issued_prov_r2_finest = issued_variables(variables_prov, 2, finest_partition)
        issued_prov_r2_single = issued_variables(
            variables_prov, 2, single_block_partition
        )
        origin_variable_multicarrier = any(
            len(variables_prov[v]["carriers"]) >= 2
            and variables_prov[v]["origin"] == origin_id
            for v in variables_prov
        )
        rows.append(
            {
                "strict_partial_order": strict,
                "token_r1_reproduces": closure_token_r1 == target,
                "copy_event_issues_token_r1": copy_id
                in issued_events(variables_token, issued_token_r1),
                "copy_event_issues_prov_r1": copy_id
                in issued_events(variables_prov, issued_prov_r1),
                "prov_r1_reproduces": closure_prov_r1 == target,
                "prov_r1_issued_set_differs_from_token": issued_events(
                    variables_prov, issued_prov_r1
                )
                != issued_events(variables_token, issued_token_r1),
                "origin_variable_multicarrier": origin_variable_multicarrier,
                "prov_r2_partition_flip": issued_prov_r2_finest
                != issued_prov_r2_single,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Hand demo: three-event partition-flip witness
# ---------------------------------------------------------------------------


def partition_flip_demo():
    events = sweep.make_events(3, ((0, 1), (0, 2)), ((0, 1), (0, 2)))
    target = frozenset(t586.build_order_report(events).closure)
    variables = variable_map(events, "event_level")
    issued_finest = issued_variables(variables, 2, finest_partition)
    issued_single = issued_variables(variables, 2, single_block_partition)
    closure_finest = induced_closure(events, variables, issued_finest)
    closure_single = induced_closure(events, variables, issued_single)
    return {
        "target_pairs": len(target),
        "finest_reproduces": closure_finest == target,
        "single_block_reproduces": closure_single == target,
        "issued_finest": sorted(issued_events(variables, issued_finest)),
        "issued_single": sorted(issued_events(variables, issued_single)),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    admitted_r1 = class_screen(1)
    admitted_r2 = class_screen(2)
    t587_admitted = t587_admitted_classes()

    frozen_events, frozen_target, cells = frozen_fixture_cells()
    reproducing_cells = sorted(
        cell_id for cell_id, cell in cells.items() if cell["reproduces"]
    )
    nondegenerate_reproducing_cells = sorted(
        cell_id
        for cell_id, cell in cells.items()
        if cell["reproduces"] and cell["max_issued_carrier_count"] >= 2
    )
    token_r1 = cells["token_level|R1|finest"]
    biased_incomparable = (
        ("prepare_biased_reference", "seed_known_record") not in frozen_target
        and ("seed_known_record", "prepare_biased_reference") not in frozen_target
    )

    per_regime_rows = run_family()
    family = {
        regime: summarize_family(rows) for regime, rows in per_regime_rows.items()
    }
    regime_ii_fixtures = regime_fixtures("record_strict_subset_causal")
    augmented_rows = run_augmented(regime_ii_fixtures)
    augmented = {
        "fixtures": len(augmented_rows),
        "strict_partial_order": sum(
            r["strict_partial_order"] for r in augmented_rows
        ),
        "token_r1_reproduces": sum(r["token_r1_reproduces"] for r in augmented_rows),
        "copy_event_issues_token_r1": sum(
            r["copy_event_issues_token_r1"] for r in augmented_rows
        ),
        "copy_event_issues_prov_r1": sum(
            r["copy_event_issues_prov_r1"] for r in augmented_rows
        ),
        "prov_r1_reproduces": sum(r["prov_r1_reproduces"] for r in augmented_rows),
        "prov_r1_issued_set_differs_from_token": sum(
            r["prov_r1_issued_set_differs_from_token"] for r in augmented_rows
        ),
        "origin_variable_multicarrier": sum(
            r["origin_variable_multicarrier"] for r in augmented_rows
        ),
        "prov_r2_partition_flip": sum(
            r["prov_r2_partition_flip"] for r in augmented_rows
        ),
    }
    demo = partition_flip_demo()

    n_i = family["record_equals_causal"]
    n_ii = family["record_strict_subset_causal"]
    per_regime_total = sweep.FIXTURES_PER_REGIME

    checks = [
        # Part A: class screen
        (
            "class_screen_R1_coextends_with_t587_typing",
            sorted(t587_admitted),
            sorted(admitted_r1),
        ),
        ("class_screen_R2_admits_nothing", [], sorted(admitted_r2)),
        # Part B: frozen fixture
        ("frozen_target_closure_pairs", 6, len(frozen_target)),
        ("frozen_biased_reference_incomparable", True, biased_incomparable),
        (
            "frozen_token_R1_reproduces_with_all_five_issuing",
            (True, 5),
            (token_r1["reproduces"], len(token_r1["issued_events"])),
        ),
        (
            "frozen_event_R1_reproduces",
            True,
            cells["event_level|R1|finest"]["reproduces"],
        ),
        (
            "frozen_token_R2_empty_and_fails",
            (False, 0),
            (
                cells["token_level|R2|finest"]["reproduces"],
                cells["token_level|R2|finest"]["closure_pairs"],
            ),
        ),
        (
            "frozen_prov_R1_copy_event_not_an_issuer",
            ["certify_erased_record", "erase_standard_record",
             "prepare_biased_reference", "seed_known_record"],
            cells["provenance_level|R1|finest"]["issued_events"],
        ),
        (
            "frozen_prov_R1_fails_reproduction",
            (False, 4),
            (
                cells["provenance_level|R1|finest"]["reproduces"],
                cells["provenance_level|R1|finest"]["closure_pairs"],
            ),
        ),
        (
            "frozen_prov_R2_only_seed_issues",
            (["seed_known_record"], False, 2),
            (
                cells["provenance_level|R2|finest"]["issued_events"],
                cells["provenance_level|R2|finest"]["reproduces"],
                cells["provenance_level|R2|finest"]["closure_pairs"],
            ),
        ),
        (
            "frozen_certified_stability_variant_fails",
            (["erase_standard_record"], False, 1),
            (
                cells["token_level|R1|certified_stability"]["issued_events"],
                cells["token_level|R1|certified_stability"]["reproduces"],
                cells["token_level|R1|certified_stability"]["closure_pairs"],
            ),
        ),
        (
            "frozen_no_reproducing_cell_has_a_multicarrier_issued_variable",
            [],
            nondegenerate_reproducing_cells,
        ),
        # Part C: family, causally-aligned regimes
        (
            "family_R1_reproduction_all_groupings_regime_i",
            [per_regime_total] * 3,
            [
                n_i["token_level_r1_reproduces"],
                n_i["event_level_r1_reproduces"],
                n_i["provenance_level_r1_reproduces"],
            ],
        ),
        (
            "family_R1_reproduction_all_groupings_regime_ii",
            [per_regime_total] * 3,
            [
                n_ii["token_level_r1_reproduces"],
                n_ii["event_level_r1_reproduces"],
                n_ii["provenance_level_r1_reproduces"],
            ],
        ),
        (
            "family_R1_issuance_is_carrier_nonemptiness",
            [per_regime_total] * 4,
            [
                n_i["token_r1_issued_equals_producing"],
                n_i["event_r1_issued_equals_producing"],
                n_ii["token_r1_issued_equals_producing"],
                n_ii["event_r1_issued_equals_producing"],
            ],
        ),
        (
            "family_R1_partition_invariance",
            [per_regime_total, per_regime_total],
            [n_i["r1_partition_invariant"], n_ii["r1_partition_invariant"]],
        ),
        (
            "family_plain_generators_are_copy_blind",
            [per_regime_total, per_regime_total],
            [n_i["prov_equals_event_issued_r1"], n_ii["prov_equals_event_issued_r1"]],
        ),
        (
            "family_no_nonvacuous_R2_reproduction_survives_single_block",
            [0, 0],
            [
                n_i["r2_nonvacuous_reproduction_survives_single_block"],
                n_ii["r2_nonvacuous_reproduction_survives_single_block"],
            ],
        ),
        # Part D: copy-augmented subfamily
        ("augmented_subfamily_size", AUGMENT_COUNT, augmented["fixtures"]),
        (
            "augmented_gate_passes",
            AUGMENT_COUNT,
            augmented["strict_partial_order"],
        ),
        (
            "augmented_token_R1_reproduces",
            AUGMENT_COUNT,
            augmented["token_r1_reproduces"],
        ),
        (
            "augmented_copy_event_issuer_status_flips_with_grouping",
            (AUGMENT_COUNT, 0),
            (
                augmented["copy_event_issues_token_r1"],
                augmented["copy_event_issues_prov_r1"],
            ),
        ),
        (
            "augmented_prov_R1_fails_reproduction",
            0,
            augmented["prov_r1_reproduces"],
        ),
        (
            "augmented_R1_issued_set_grouping_fragile",
            AUGMENT_COUNT,
            augmented["prov_r1_issued_set_differs_from_token"],
        ),
        (
            "augmented_prov_R2_partition_flip",
            AUGMENT_COUNT,
            augmented["prov_r2_partition_flip"],
        ),
        # Hand demo
        (
            "demo_three_event_R2_partition_flip",
            (True, False, ["ev0"], []),
            (
                demo["finest_reproduces"],
                demo["single_block_reproduces"],
                demo["issued_finest"],
                demo["issued_single"],
            ),
        ),
    ]

    check_table = [
        {
            "check_id": check_id,
            "expected": expected,
            "actual": actual,
            "match": expected == actual,
        }
        for check_id, expected, actual in checks
    ]
    all_match = all(item["match"] for item in check_table)

    summary = {
        "artifact": "redundancy-issuance-probe-2026-07-28",
        "framing": (
            "commit-module swing 2 (Debt L1, repair route 2): SBS-class "
            "redundancy-issuance reproduction test on the frozen T586 fixture "
            "and the sweep's causally-aligned regimes; review-only, no claim "
            "movement, no T-number"
        ),
        "registered_kill": (
            "redundancy-issuance must reproduce the T586 record order on "
            "causally-aligned fixtures without consuming D"
        ),
        "design": {
            "groupings": list(GROUPINGS),
            "thresholds": [1, 2],
            "partitions": ["finest", "single_block", "seeded"],
            "aligned_regimes": list(ALIGNED_REGIMES),
            "fixtures_per_regime": sweep.FIXTURES_PER_REGIME,
            "regime_seeds_reused_verbatim": {
                regime: sweep.REGIME_SEEDS[regime] for regime in ALIGNED_REGIMES
            },
            "probe_seeds": {
                "partition_seed": PARTITION_SEED,
                "seeded_partition_base": SEEDED_PARTITION_BASE,
                "augment_seed_base": AUGMENT_SEED_BASE,
            },
            "augment_count": AUGMENT_COUNT,
            "regime_iii_excluded": (
                "non-aligned sector is outside the series' carried scope entry"
            ),
        },
        "class_screen": {
            "t587_admitted": sorted(t587_admitted),
            "admitted_at_R1": sorted(admitted_r1),
            "admitted_at_R2": sorted(admitted_r2),
        },
        "frozen_fixture": {
            "target_closure_pairs": len(frozen_target),
            "cells": cells,
            "reproducing_cells": reproducing_cells,
        },
        "family": family,
        "augmented_subfamily": augmented,
        "partition_flip_demo": demo,
        "checks": check_table,
        "all_match": all_match,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
