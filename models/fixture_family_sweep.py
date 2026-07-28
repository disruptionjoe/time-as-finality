"""Fixture-family sweep for the T586/T587/foliation-overlay finding set.

Every fixture-derived finding in the T586 -> T587 -> foliation-overlay chain
rests on the single five-event `_landauer_record_events` fixture, whose two
causal-only edges (seed -> prepare, prepare -> certify) are hand-declared.
This sweep separates typing-theorems from hand-built-world artifacts by
running the same derivations -- T586's own `build_order_report`,
`causal_relation`, and `transitive_closure`, plus the overlay module's
admissibility helpers, imported rather than copied -- across a randomized
family of 600 fixtures in three regimes:

- regime (i)   RECORD=CAUSAL: every direct causal edge carries a record;
- regime (ii)  RECORD strictly inside CAUSAL at the direct-edge level, at
  varying record density (the T586 fixture's shape);
- regime (iii) RECORD not inside CAUSAL: at least one record dependence is
  planted between events with no declared causal path (type-legal; nothing
  in `build_order_report` consults `causal_parents`).

Findings under test (see explorations/fixture-family-sweep-2026-07-28.md for
the pre-registered predictions, written before this file was first run):

- F1: record closure contained (strictly) in causal closure;
- F2: a foliation overlay changes nothing about the record closure, and
  everything a foliation adds lacks a record basis;
- F3: record-admissible foliations strictly contain causally-admissible
  ones, with a residual degeneracy after both constraints.

The script is pure stdlib and deterministic: all randomness comes from
`random.Random` instances seeded with the fixed literals below; there are no
clock, date, or filesystem-order dependences. It prints a JSON summary with
an expected/actual/match check table (theorem confirmations, anchor
reproduction, and hand demos are gated; empirical fractions are reported as
measurements, not gated) and exits 0 only if all gated checks match.

Run from the repository root:

    python3 -m models.fixture_family_sweep
"""

from __future__ import annotations

import json
from dataclasses import replace
from itertools import permutations
from random import Random
from statistics import median

from models import t586_record_capability_order_gate as t586
from models.foliation_overlay_t586_reproduction import (
    foliation_comparabilities,
    foliation_respects,
)

FIXTURES_PER_REGIME = 200
EVENT_SIZES = (5, 6, 7, 8, 9)
EDGE_DENSITIES = (0.2, 0.35, 0.5, 0.7)
RECORD_DENSITIES = (0.35, 0.6, 0.85)
REGIME_SEEDS = {
    "record_equals_causal": 58601,
    "record_strict_subset_causal": 58602,
    "record_not_subset_causal": 58603,
}
REGIMES = tuple(REGIME_SEEDS)
OVERLAY_SEED_BASE = 58610

Relation = frozenset


# ---------------------------------------------------------------------------
# Fixture generation
# ---------------------------------------------------------------------------


def random_dag(rng: Random, n: int, p_edge: float) -> tuple[tuple[int, int], ...]:
    """Forward-oriented random DAG on 0..n-1; at least one edge."""
    edges = [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if rng.random() < p_edge
    ]
    if not edges:
        edges = [(0, n - 1)]
    return tuple(edges)


def index_closure(n: int, edges: tuple[tuple[int, int], ...]) -> frozenset:
    reach = [[False] * n for _ in range(n)]
    for a, b in edges:
        reach[a][b] = True
    for k in range(n):
        for a in range(n):
            if reach[a][k]:
                row_a, row_k = reach[a], reach[k]
                for b in range(n):
                    if row_k[b]:
                        row_a[b] = True
    return frozenset(
        (a, b) for a in range(n) for b in range(n) if reach[a][b]
    )


def generate_fixture(regime: str, rng: Random, n: int) -> dict | None:
    p_edge = rng.choice(EDGE_DENSITIES)
    causal = random_dag(rng, n, p_edge)
    planted = None
    if regime == "record_equals_causal":
        p_rec = 1.0
        record = causal
    elif regime == "record_strict_subset_causal":
        p_rec = rng.choice(RECORD_DENSITIES)
        record = tuple(edge for edge in causal if rng.random() < p_rec)
        if len(record) == len(causal):
            record = record[:-1]  # enforce at least one record-free causal edge
    else:
        p_rec = rng.choice(RECORD_DENSITIES)
        base = tuple(edge for edge in causal if rng.random() < p_rec)
        causally_related = index_closure(n, causal)
        candidates = [
            (i, j)
            for i in range(n)
            for j in range(i + 1, n)
            if (i, j) not in causally_related
        ]
        if not candidates:
            return None  # causal closure is total; resample
        planted = candidates[rng.randrange(len(candidates))]
        record = tuple(sorted(set(base) | {planted}))
    return {
        "regime": regime,
        "n": n,
        "p_edge": p_edge,
        "p_rec": p_rec,
        "causal_edges": causal,
        "record_edges": record,
        "planted": planted,
    }


def make_events(
    n: int,
    causal_edges: tuple[tuple[int, int], ...],
    record_edges: tuple[tuple[int, int], ...],
) -> tuple:
    """Build CapabilityEvents: one fresh record per record edge, unique
    producer, all required records produced in-fixture, one executable task
    per event (so record dependences always materialize as edges)."""
    produced: dict[int, list[str]] = {i: [] for i in range(n)}
    required: dict[int, list[str]] = {i: [] for i in range(n)}
    parents: dict[int, list[str]] = {i: [] for i in range(n)}
    for a, b in sorted(record_edges):
        record_id = f"r_{a}_{b}"
        produced[a].append(record_id)
        required[b].append(record_id)
    for a, b in sorted(causal_edges):
        parents[b].append(f"ev{a}")
    return tuple(
        t586.CapabilityEvent(
            event_id=f"ev{i}",
            produced_records=tuple(produced[i]),
            required_records=tuple(required[i]),
            executable_tasks=(f"task_{i}",),
            clock_label=i,
            entropy_rank=i / 10.0,
            causal_parents=tuple(parents[i]),
            irreversible_operation=False,
        )
        for i in range(n)
    )


# ---------------------------------------------------------------------------
# Order machinery on top of T586's helpers
# ---------------------------------------------------------------------------


def count_extensions(ids: tuple[str, ...], relation: Relation) -> int:
    """Exact linear-extension count via a downset bitmask DP (n <= 9).

    Counts exactly what brute-force permutation filtering counts; the anchor
    check verifies this against the overlay note's brute-force values."""
    n = len(ids)
    index = {event_id: i for i, event_id in enumerate(ids)}
    pred = [0] * n
    for a, b in relation:
        pred[index[b]] |= 1 << index[a]
    counts = [0] * (1 << n)
    counts[0] = 1
    for mask in range(1 << n):
        here = counts[mask]
        if not here:
            continue
        for j in range(n):
            bit = 1 << j
            if mask & bit or pred[j] & ~mask:
                continue
            counts[mask | bit] += here
    return counts[(1 << n) - 1]


def predecessor_sets(ids: tuple[str, ...], relation: Relation) -> dict:
    return {
        event_id: {a for a, b in relation if b == event_id} for event_id in ids
    }


def linear_extension(
    ids: tuple[str, ...], relation: Relation, rng: Random | None
) -> tuple[str, ...]:
    """Topological completion; lexicographically-first when rng is None,
    otherwise rng-chosen among minimal elements."""
    preds = predecessor_sets(ids, relation)
    remaining = list(ids)
    placed: set[str] = set()
    out: list[str] = []
    while remaining:
        minimal = sorted(e for e in remaining if preds[e] <= placed)
        pick = minimal[0] if rng is None else minimal[rng.randrange(len(minimal))]
        out.append(pick)
        placed.add(pick)
        remaining.remove(pick)
    return tuple(out)


def overlay_recompute_matches(events: tuple, order: tuple[str, ...]) -> bool:
    """Apply a foliation overlay as a clock-label (and entropy-rank) relabel
    and recompute the record closure with T586's own derivation."""
    baseline = t586.build_order_report(events)
    position = {event_id: i for i, event_id in enumerate(order)}
    relabeled = tuple(
        replace(
            event,
            clock_label=position[event.event_id],
            entropy_rank=position[event.event_id] / 7.0,
        )
        for event in events
    )
    recomputed = t586.build_order_report(relabeled)
    return (
        frozenset(recomputed.closure) == frozenset(baseline.closure)
        and recomputed.strict_partial_order == baseline.strict_partial_order
    )


def addition_lemma_holds(
    order: tuple[str, ...], relation: Relation, incomparable_count: int
) -> bool:
    """L2: for a linear extension, added comparabilities are exactly the
    incomparable pairs, none with a basis in the relation either way."""
    if not foliation_respects(order, relation):
        return False
    added = foliation_comparabilities(order) - relation
    return len(added) == incomparable_count and all(
        (a, b) not in relation and (b, a) not in relation for a, b in added
    )


# ---------------------------------------------------------------------------
# Per-fixture analysis
# ---------------------------------------------------------------------------


def analyze_fixture(fixture: dict, overlay_rng: Random) -> dict:
    n = fixture["n"]
    events = make_events(n, fixture["causal_edges"], fixture["record_edges"])
    ids = tuple(event.event_id for event in events)
    report = t586.build_order_report(events)
    record = frozenset(report.closure)
    causal = t586.causal_relation(events)
    joint = t586.transitive_closure(ids, record | causal)

    e_record = count_extensions(ids, record)
    e_causal = count_extensions(ids, causal)
    e_joint = count_extensions(ids, joint)

    total_pairs = n * (n - 1) // 2
    incomparable_record = total_pairs - len(record)
    incomparable_causal = total_pairs - len(causal)
    incomparable_joint = total_pairs - len(joint)

    subset = record <= causal
    equal = record == causal
    inverted = causal < record  # causal strictly inside record

    overlay_orders = [
        ids,
        tuple(reversed(ids)),
        linear_extension(ids, record, None),
    ] + [tuple(overlay_rng.sample(ids, n)) for _ in range(3)]
    overlay_violations = sum(
        0 if overlay_recompute_matches(events, order) else 1
        for order in overlay_orders
    )

    record_extensions = [ids, linear_extension(ids, record, overlay_rng)]
    addition_violations = sum(
        0 if addition_lemma_holds(order, record, incomparable_record) else 1
        for order in record_extensions
    )
    causal_extension = linear_extension(ids, causal, overlay_rng)
    causal_addition_violations = (
        0 if addition_lemma_holds(causal_extension, causal, incomparable_causal) else 1
    )

    return {
        "regime": fixture["regime"],
        "n": n,
        "p_rec": fixture["p_rec"],
        "strict_partial_order": report.strict_partial_order,
        "missing_required_records": len(report.missing_required_records),
        "record_pairs": len(record),
        "causal_pairs": len(causal),
        "joint_pairs": len(joint),
        "incomparable_record": incomparable_record,
        "incomparable_joint": incomparable_joint,
        "record_incomparability_density": incomparable_record / total_pairs,
        "subset": subset,
        "equal": equal,
        "strict": subset and not equal,
        "inverted": inverted,
        "e_record": e_record,
        "e_causal": e_causal,
        "e_joint": e_joint,
        "ratio": e_record / e_causal,
        "overlay_violations": overlay_violations,
        "addition_violations": addition_violations,
        "causal_addition_violations": causal_addition_violations,
        "degeneracy_iff_violation": (e_record == 1) != (incomparable_record == 0),
        "equivalence_violation": subset and ((e_record > e_causal) != (record < causal)),
        "monotonicity_violation": subset and e_record < e_causal,
        "joint_equals_causal_violation": subset and e_joint != e_causal,
        "causal_extension_escapes_record": e_joint < e_causal,
    }


def run_regime(regime: str) -> tuple[list[dict], int]:
    rng = Random(REGIME_SEEDS[regime])
    rows: list[dict] = []
    resamples = 0
    counter_base = REGIMES.index(regime) * FIXTURES_PER_REGIME
    for i in range(FIXTURES_PER_REGIME):
        n = EVENT_SIZES[i % len(EVENT_SIZES)]
        fixture = None
        while fixture is None:
            fixture = generate_fixture(regime, rng, n)
            if fixture is None:
                resamples += 1
        overlay_rng = Random(OVERLAY_SEED_BASE + counter_base + i)
        rows.append(analyze_fixture(fixture, overlay_rng))
    return rows, resamples


# ---------------------------------------------------------------------------
# Anchor and hand demos
# ---------------------------------------------------------------------------


def _anchor_overlay_violations(
    events: tuple, ids: tuple[str, ...], record: Relation
) -> int:
    rng = Random(OVERLAY_SEED_BASE - 1)
    orders = [
        ids,
        tuple(reversed(ids)),
        linear_extension(ids, record, None),
    ] + [tuple(rng.sample(ids, len(ids))) for _ in range(3)]
    return sum(
        0 if overlay_recompute_matches(events, order) else 1 for order in orders
    )


def anchor_checks() -> tuple[list[tuple], dict]:
    events = t586._landauer_record_events()
    ids = tuple(event.event_id for event in events)
    report = t586.build_order_report(events)
    record = frozenset(report.closure)
    causal = t586.causal_relation(events)
    joint = t586.transitive_closure(ids, record | causal)
    e_record = count_extensions(ids, record)
    e_causal = count_extensions(ids, causal)
    e_joint = count_extensions(ids, joint)
    brute_record = sum(
        1 for perm in permutations(ids) if foliation_respects(perm, record)
    )
    brute_causal = sum(
        1 for perm in permutations(ids) if foliation_respects(perm, causal)
    )
    total_pairs = len(ids) * (len(ids) - 1) // 2
    incomparable = total_pairs - len(record)
    identity_added = foliation_comparabilities(ids) - record
    checks = [
        ("anchor_record_closure_pairs", 6, len(record)),
        ("anchor_causal_closure_pairs", 8, len(causal)),
        ("anchor_record_incomparable_pairs", 4, incomparable),
        ("anchor_record_strict_subset_of_causal", True, record < causal),
        ("anchor_extensions_record", 5, e_record),
        ("anchor_extensions_causal", 3, e_causal),
        ("anchor_extensions_joint", 3, e_joint),
        ("anchor_record_admissible_causally_inadmissible", 2, e_record - e_joint),
        ("anchor_dp_matches_bruteforce", (5, 3), (brute_record, brute_causal)),
        ("anchor_identity_foliation_added_comparabilities", 4, len(identity_added)),
        (
            "anchor_added_equals_incomparable_and_unlicensed",
            True,
            addition_lemma_holds(ids, record, incomparable),
        ),
        (
            "anchor_identity_foliation_causally_inadmissible",
            True,
            not foliation_respects(ids, causal),
        ),
        (
            "anchor_overlay_invariance_all_six",
            0,
            _anchor_overlay_violations(events, ids, record),
        ),
    ]
    summary = {
        "event_ids": list(ids),
        "e_record": e_record,
        "e_causal": e_causal,
        "e_joint": e_joint,
    }
    return checks, summary


def shortcut_demo_checks() -> list[tuple]:
    """Three events, record chain 0->1->2, record-free direct causal edge
    0->2: closure equality despite direct-edge strictness -- the constructive
    existence proof that F1's strictness is not implied by regime (ii)."""
    causal = ((0, 1), (1, 2), (0, 2))
    record = ((0, 1), (1, 2))
    events = make_events(3, causal, record)
    ids = tuple(event.event_id for event in events)
    report = t586.build_order_report(events)
    record_closure = frozenset(report.closure)
    causal_closure = t586.causal_relation(events)
    return [
        ("shortcut_demo_direct_edge_sets_differ", True, set(causal) != set(record)),
        (
            "shortcut_demo_record_closure_equals_causal_closure",
            True,
            record_closure == causal_closure,
        ),
        (
            "shortcut_demo_single_extension_each",
            (1, 1),
            (count_extensions(ids, record_closure), count_extensions(ids, causal_closure)),
        ),
    ]


def task_typing_demo_checks() -> list[tuple]:
    """Two events; the consumer requires a record but declares no executable
    task: `record_dependency_edges` emits nothing (the edge loop runs over
    `executable_tasks`), so the record order is doubly typed -- record
    issuance AND task executability are both load-bearing."""
    producer = t586.CapabilityEvent(
        event_id="ev0",
        produced_records=("r_0_1",),
        required_records=(),
        executable_tasks=("task_0",),
        clock_label=0,
        entropy_rank=0.0,
        causal_parents=(),
        irreversible_operation=False,
    )
    taskless_consumer = t586.CapabilityEvent(
        event_id="ev1",
        produced_records=(),
        required_records=("r_0_1",),
        executable_tasks=(),
        clock_label=1,
        entropy_rank=0.1,
        causal_parents=("ev0",),
        irreversible_operation=False,
    )
    report = t586.build_order_report((producer, taskless_consumer))
    return [
        (
            "task_typing_demo_no_edges_without_executable_task",
            (0, 0, True),
            (
                len(report.direct_edges),
                len(report.closure),
                report.strict_partial_order,
            ),
        ),
    ]


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------


def _dist(values: list) -> dict:
    return {
        "min": min(values),
        "median": round(float(median(values)), 4),
        "max": max(values),
    }


def aggregate(rows: list[dict]) -> dict:
    ratios = [row["ratio"] for row in rows]
    return {
        "fixtures": len(rows),
        "strict_partial_order_pass": sum(r["strict_partial_order"] for r in rows),
        "record_subset_causal": sum(r["subset"] for r in rows),
        "record_equal_causal": sum(r["equal"] for r in rows),
        "record_strict_subset_causal": sum(r["strict"] for r in rows),
        "record_not_subset_causal": sum(not r["subset"] for r in rows),
        "causal_strict_subset_record": sum(r["inverted"] for r in rows),
        "record_closure_empty": sum(r["record_pairs"] == 0 for r in rows),
        "causal_extension_escapes_record": sum(
            r["causal_extension_escapes_record"] for r in rows
        ),
        "joint_extension_count_one": sum(r["e_joint"] == 1 for r in rows),
        "joint_extension_count_three": sum(r["e_joint"] == 3 for r in rows),
        "e_record": _dist([r["e_record"] for r in rows]),
        "e_causal": _dist([r["e_causal"] for r in rows]),
        "e_joint": _dist([r["e_joint"] for r in rows]),
        "degeneracy_ratio": {
            "min": round(min(ratios), 4),
            "median": round(float(median(ratios)), 4),
            "max": round(max(ratios), 4),
        },
        "record_incomparability_density": {
            "min": round(min(r["record_incomparability_density"] for r in rows), 4),
            "median": round(
                float(median(r["record_incomparability_density"] for r in rows)), 4
            ),
            "max": round(max(r["record_incomparability_density"] for r in rows), 4),
        },
        "overlay_violations": sum(r["overlay_violations"] for r in rows),
        "addition_violations": sum(r["addition_violations"] for r in rows),
        "causal_addition_violations": sum(
            r["causal_addition_violations"] for r in rows
        ),
        "degeneracy_iff_violations": sum(r["degeneracy_iff_violation"] for r in rows),
        "equivalence_violations": sum(r["equivalence_violation"] for r in rows),
        "monotonicity_violations": sum(r["monotonicity_violation"] for r in rows),
        "joint_equals_causal_violations": sum(
            r["joint_equals_causal_violation"] for r in rows
        ),
    }


def density_bins(rows: list[dict]) -> dict:
    bins: dict[str, dict] = {}
    for p_rec in RECORD_DENSITIES:
        subset = [r for r in rows if r["p_rec"] == p_rec]
        if not subset:
            continue
        bins[str(p_rec)] = {
            "fixtures": len(subset),
            "record_equal_causal": sum(r["equal"] for r in subset),
            "record_strict_subset_causal": sum(r["strict"] for r in subset),
            "degeneracy_ratio_median": round(
                float(median(r["ratio"] for r in subset)), 4
            ),
        }
    return bins


def main() -> int:
    anchor, anchor_summary = anchor_checks()
    demo_checks = shortcut_demo_checks() + task_typing_demo_checks()

    regime_rows: dict[str, list[dict]] = {}
    resample_counts: dict[str, int] = {}
    for regime in REGIMES:
        rows, resamples = run_regime(regime)
        regime_rows[regime] = rows
        resample_counts[regime] = resamples

    aggregates = {regime: aggregate(rows) for regime, rows in regime_rows.items()}
    all_rows = [row for rows in regime_rows.values() for row in rows]
    agg_i = aggregates["record_equals_causal"]
    agg_ii = aggregates["record_strict_subset_causal"]
    agg_iii = aggregates["record_not_subset_causal"]

    sweep_checks = [
        (
            "fixtures_per_regime",
            [FIXTURES_PER_REGIME] * 3,
            [agg["fixtures"] for agg in aggregates.values()],
        ),
        (
            "gate_passes_in_all_three_regimes",
            3 * FIXTURES_PER_REGIME,
            sum(agg["strict_partial_order_pass"] for agg in aggregates.values()),
        ),
        (
            "no_missing_required_records_anywhere",
            0,
            sum(r["missing_required_records"] for r in all_rows),
        ),
        ("overlay_invariance_violations", 0, sum(agg["overlay_violations"] for agg in aggregates.values())),
        ("extension_addition_violations", 0, sum(agg["addition_violations"] for agg in aggregates.values())),
        (
            "causal_extension_addition_violations",
            0,
            sum(agg["causal_addition_violations"] for agg in aggregates.values()),
        ),
        (
            "degeneracy_iff_incomparable_violations",
            0,
            sum(agg["degeneracy_iff_violations"] for agg in aggregates.values()),
        ),
        ("regime_i_record_equals_causal", FIXTURES_PER_REGIME, agg_i["record_equal_causal"]),
        (
            "regime_i_degeneracy_ratio_identically_one",
            (1.0, 1.0, 1.0),
            (
                agg_i["degeneracy_ratio"]["min"],
                agg_i["degeneracy_ratio"]["median"],
                agg_i["degeneracy_ratio"]["max"],
            ),
        ),
        ("regime_ii_record_subset_causal", FIXTURES_PER_REGIME, agg_ii["record_subset_causal"]),
        ("regime_ii_monotonicity_violations", 0, agg_ii["monotonicity_violations"]),
        ("regime_ii_strictness_equivalence_violations", 0, agg_ii["equivalence_violations"]),
        (
            "regime_ii_joint_count_equals_causal_count_violations",
            0,
            agg_ii["joint_equals_causal_violations"],
        ),
        (
            "regime_iii_record_not_subset_causal",
            FIXTURES_PER_REGIME,
            agg_iii["record_not_subset_causal"],
        ),
        (
            "regime_iii_causally_admissible_foliation_violates_record",
            FIXTURES_PER_REGIME,
            agg_iii["causal_extension_escapes_record"],
        ),
    ]

    checks = anchor + demo_checks + sweep_checks
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
        "artifact": "fixture-family-sweep-2026-07-28",
        "framing": (
            "formalism-internal robustness sweep for the T586/T587/"
            "foliation-overlay finding set; no new claim, no new T-number"
        ),
        "design": {
            "fixtures_per_regime": FIXTURES_PER_REGIME,
            "event_sizes": list(EVENT_SIZES),
            "edge_densities": list(EDGE_DENSITIES),
            "record_densities": list(RECORD_DENSITIES),
            "regime_seeds": REGIME_SEEDS,
            "overlay_seed_base": OVERLAY_SEED_BASE,
            "overlays_per_fixture": 6,
            "record_extensions_checked_per_fixture": 2,
            "regime_iii_resamples": resample_counts,
        },
        "anchor": anchor_summary,
        "aggregates": aggregates,
        "regime_ii_by_record_density": density_bins(
            regime_rows["record_strict_subset_causal"]
        ),
        "family_joint_extension_counts": _dist([r["e_joint"] for r in all_rows]),
        "checks": check_table,
        "all_match": all_match,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
