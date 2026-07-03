"""T425 - M2 Size-Sweep Absorption Gate.

T424 left one honest Route-A escape hatch: n=3 is too small for some index
channels, so a larger complex might provide a genuine index reading that both
escapes the v_gap relabel bar and equals the finality separator.

This model stress-tests the inherited T423/T424 separator before any new index
claim is allowed. It enumerates all AND-doctrine profiles for n = 3, 4, 5 under
the same strict-majority / tie-reject rule and asks whether the SURVIVES-R1
global-no-local datum still exists. If no larger-n profile has the inherited
separator, a larger index channel has no finality target to agree with.

Recorded-tier only. No claim promotion. Cross-domain index language is object of
study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_size_sweep_absorption_gate
    python -m pytest tests/test_m2_size_sweep_absorption_gate.py -q
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
import json

from models.legitimacy_shapley_finality_probe import (
    all_subsets,
    joint_record_completion_verdict,
)
from models.m2_observer_game import and_doctrine, gap_value, moebius_dividends


SIZES = (3, 4, 5)
STATES = ((0, 0), (0, 1), (1, 0), (1, 1))


def players_for(n):
    return tuple(range(1, n + 1))


def canonical_coalitions(players):
    return tuple(
        sorted((tuple(sorted(S)) for S in all_subsets(players)), key=lambda t: (len(t), t))
    )


def enumerate_profiles(n):
    return list(product(STATES, repeat=n))


def columns(profile, players):
    p = {players[i]: profile[i][0] for i in range(len(players))}
    q = {players[i]: profile[i][1] for i in range(len(players))}
    r = {players[i]: and_doctrine(profile[i][0], profile[i][1]) for i in range(len(players))}
    return p, q, r


def vgap_vector(profile, players):
    p, q, r = columns(profile, players)
    return tuple(
        int(gap_value(frozenset(S), p, q, r, and_doctrine))
        for S in canonical_coalitions(players)
    )


def gap_dividends(profile, players):
    p, q, r = columns(profile, players)
    return moebius_dividends(
        lambda S: gap_value(frozenset(S), p, q, r, and_doctrine),
        players,
    )


def separator_report(profile, players):
    div = gap_dividends(profile, players)
    jrc = joint_record_completion_verdict(div, {}, players=players)
    return {
        "separator": 1 if jrc.get("verdict") == "SURVIVES-R1" else 0,
        "verdict": jrc.get("verdict"),
        "min_sep_size": jrc.get("min_sep_size"),
        "datum_in_proper_subset": jrc.get("datum_in_proper_subset"),
    }


def crosses(profile, i, j):
    return profile[i][0] != profile[j][0] and profile[i][1] != profile[j][1]


def compatibility_edges(profile):
    n = len(profile)
    return tuple((i, j) for i, j in combinations(range(n), 2) if not crosses(profile, i, j))


def component_count(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in edges:
        union(a, b)
    return len({find(i) for i in range(n)})


def compatibility_graph_cycle_rank(profile):
    """Graph-cycle diagnostic only, not a promoted cohomology claim.

    It verifies that larger profiles do contain index-looking cycle structure.
    The T425 gate asks whether any such structure has a SURVIVES-R1 finality
    target to compute.
    """

    n = len(profile)
    edges = compatibility_edges(profile)
    return len(edges) - n + component_count(n, edges)


def _counter(counter):
    return {str(k): counter[k] for k in sorted(counter, key=lambda x: (-1 if x is None else x))}


def run_size(n):
    players = players_for(n)
    profiles = enumerate_profiles(n)
    fibers = defaultdict(list)
    separator_by_serial = {}
    verdict_distribution = Counter()
    min_sep_distribution = Counter()
    cycle_rank_distribution = Counter()
    cycle_rank_by_verdict = defaultdict(Counter)
    sample_absorbed = None
    sample_separator = None

    for serial, profile in enumerate(profiles):
        fibers[vgap_vector(profile, players)].append(serial)
        sreport = separator_report(profile, players)
        separator_by_serial[serial] = sreport["separator"]
        verdict_distribution[sreport["verdict"]] += 1
        min_sep_distribution[sreport["min_sep_size"]] += 1

        rank = compatibility_graph_cycle_rank(profile)
        cycle_rank_distribution[rank] += 1
        cycle_rank_by_verdict[sreport["verdict"]][rank] += 1

        if sreport["verdict"] == "ABSORBED" and sample_absorbed is None:
            sample_absorbed = {
                "serial": serial,
                "profile": profile,
                "v_gap": vgap_vector(profile, players),
                "min_sep_size": sreport["min_sep_size"],
                "cycle_rank": rank,
            }
        if sreport["separator"] == 1 and sample_separator is None:
            sample_separator = {
                "serial": serial,
                "profile": profile,
                "v_gap": vgap_vector(profile, players),
                "cycle_rank": rank,
            }

    mixed_fibers = 0
    separator_fiber_sizes = []
    for serials in fibers.values():
        seps = {separator_by_serial[s] for s in serials}
        if len(seps) > 1:
            mixed_fibers += 1
        if seps == {1}:
            separator_fiber_sizes.append(len(serials))

    separator_profiles = sum(separator_by_serial.values())
    nonzero_gap_profiles = len(profiles) - verdict_distribution["no-separation"]
    absorbed_profiles = verdict_distribution["ABSORBED"]
    larger_absorption_complete = (
        n > 3
        and separator_profiles == 0
        and absorbed_profiles == nonzero_gap_profiles
        and set(k for k, v in min_sep_distribution.items() if k is not None and v > 0) == {3}
    )

    positive_cycle_profiles = sum(
        count for rank, count in cycle_rank_distribution.items() if rank > 0
    )

    return {
        "n": n,
        "n_profiles": len(profiles),
        "n_vgap_fibers": len(fibers),
        "separator_profiles": separator_profiles,
        "nonzero_gap_profiles": nonzero_gap_profiles,
        "verdict_distribution": _counter(verdict_distribution),
        "min_sep_size_distribution": _counter(min_sep_distribution),
        "fiber_mixed_separator_count": mixed_fibers,
        "separator_fiber_sizes": sorted(separator_fiber_sizes),
        "larger_absorption_complete": larger_absorption_complete,
        "cycle_diagnostic": {
            "compatibility_graph_cycle_rank_distribution": _counter(
                cycle_rank_distribution
            ),
            "positive_cycle_profiles": positive_cycle_profiles,
            "positive_cycle_profiles_without_separator": (
                positive_cycle_profiles if separator_profiles == 0 else None
            ),
            "cycle_rank_by_verdict": {
                verdict: _counter(counter)
                for verdict, counter in sorted(cycle_rank_by_verdict.items())
            },
        },
        "sample_separator": sample_separator,
        "sample_absorbed": sample_absorbed,
    }


def overall_verdict(size_reports):
    larger = [size_reports[str(n)] for n in (4, 5)]
    larger_blocked = all(rep["larger_absorption_complete"] for rep in larger)
    n3_reference_ok = (
        size_reports["3"]["separator_profiles"] == 6
        and size_reports["3"]["verdict_distribution"].get("SURVIVES-R1") == 6
    )
    if n3_reference_ok and larger_blocked:
        return {
            "verdict": "REDESIGN",
            "reading": (
                "The inherited T423/T424 SURVIVES-R1 finality datum is atomic at "
                "n=3 in the finite AND strict-majority family. At n=4 and n=5, "
                "every nonzero gap is absorbed by a 3-judge proper subset, so a "
                "larger index complex is blocked before separator-agreement can "
                "even be tested."
            ),
            "next_gate": (
                "Any rescue must predeclare a different aggregation family, "
                "threshold rule, or separator object; it is not a direct Route-A "
                "continuation of T424."
            ),
        }
    return {
        "verdict": "RECHECK",
        "reading": "The size sweep did not match the expected absorption pattern.",
        "next_gate": "Inspect the per-size reports before drawing a research conclusion.",
    }


def run():
    reports = {str(n): run_size(n) for n in SIZES}
    return {
        "artifact": "T425-m2-size-sweep-absorption-gate-v0.1",
        "sizes": list(SIZES),
        "overall_verdict": overall_verdict(reports),
        "size_reports": reports,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
