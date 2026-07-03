"""T427 - M2 Threshold-Index Leakage Gate.

T426 found high-quota SURVIVES-R1 targets only in size-matched cells:
3/4 at n=4 and 4/5 at n=5. It required threshold-tuning controls before any
follow-up index reading. This model checks whether candidate index-style
channels distinguish those positives without merely reading quota/size/support
data.

Recorded-tier only. No claim promotion. Cross-domain social-choice / index
language is object of study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_threshold_index_leakage_gate
    python -m pytest tests/test_m2_threshold_index_leakage_gate.py -q
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
import json

from models import m2_threshold_rule_rescue_gate as t426


STATE_ORDER = ((0, 0), (0, 1), (1, 0), (1, 1))
CELL_SPECS = (
    ("three_quarters", 4),
    ("three_quarters", 5),
    ("four_fifths", 4),
    ("four_fifths", 5),
)
TARGET_CELLS = {("three_quarters", 4), ("four_fifths", 5)}


def rules_by_name():
    return {rule["name"]: rule for rule in t426.RULES}


def support_counts(profile):
    counts = Counter(profile)
    return tuple(counts.get(state, 0) for state in STATE_ORDER)


def premise_counts(profile):
    p_yes = sum(pair[0] for pair in profile)
    q_yes = sum(pair[1] for pair in profile)
    r_yes = sum(1 for pair in profile if pair[0] and pair[1])
    return p_yes, q_yes, r_yes


def crosses(profile, i, j):
    """Two judges cross when they disagree on both premises."""

    return profile[i][0] != profile[j][0] and profile[i][1] != profile[j][1]


def crossing_count(profile):
    return sum(
        1 for i, j in combinations(range(len(profile)), 2) if crosses(profile, i, j)
    )


def compatibility_edges(profile):
    return tuple(
        (i, j)
        for i, j in combinations(range(len(profile)), 2)
        if not crosses(profile, i, j)
    )


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


def compatibility_cycle_rank(profile):
    n = len(profile)
    edges = compatibility_edges(profile)
    return len(edges) - n + component_count(n, edges)


def signed_frustration_index(profile):
    """Minimum negative edges after switching the complete signed graph.

    Edges are negative exactly when the pair crosses. This is an exact finite
    signed-graph diagnostic, not a promoted index theorem.
    """

    n = len(profile)
    edges = tuple(combinations(range(n), 2))
    best = None
    for switch in product((1, -1), repeat=n):
        negative = 0
        for i, j in edges:
            sign = -1 if crosses(profile, i, j) else 1
            if switch[i] * switch[j] * sign == -1:
                negative += 1
        best = negative if best is None else min(best, negative)
    return best


def encode_value(value):
    if isinstance(value, tuple):
        return [encode_value(item) for item in value]
    return value


def channel_report(name, channel_type, values, separators):
    by_value = defaultdict(Counter)
    for item_id, value in values.items():
        by_value[value][separators[item_id]] += 1

    sep_values = {value for value, counts in by_value.items() if counts.get(1, 0) > 0}
    zero_values = {value for value, counts in by_value.items() if counts.get(0, 0) > 0}
    n_separator = sum(separators.values())
    perfectly_predicts = bool(n_separator) and not (sep_values & zero_values)

    if perfectly_predicts and channel_type == "candidate_index":
        guardrail_verdict = "CLEAN_INDEX"
    elif perfectly_predicts:
        guardrail_verdict = "REJECT_LEAKAGE"
    else:
        guardrail_verdict = "FAILS_SEPARATOR"

    records = []
    for value, counts in sorted(by_value.items(), key=lambda item: repr(item[0])):
        records.append({
            "value": encode_value(value),
            "separator_0": counts.get(0, 0),
            "separator_1": counts.get(1, 0),
        })

    collisions = [
        record for record in records
        if record["separator_0"] > 0 and record["separator_1"] > 0
    ]
    separator_only = [
        record for record in records
        if record["separator_0"] == 0 and record["separator_1"] > 0
    ]

    return {
        "name": name,
        "channel_type": channel_type,
        "n_distinct_values": len(by_value),
        "perfectly_predicts_separator": perfectly_predicts,
        "guardrail_verdict": guardrail_verdict,
        "n_collision_values": len(collisions),
        "collision_examples": collisions[:8],
        "separator_only_values": separator_only[:8],
    }


def profile_channels(rule_name, n, profile):
    rule = rules_by_name()[rule_name]
    support = support_counts(profile)
    p_yes, q_yes, r_yes = premise_counts(profile)
    grand_req = t426.quota_requirement(n, rule)
    top_req = t426.quota_requirement(n - 1, rule)
    x_count = crossing_count(profile)
    cycle_rank = compatibility_cycle_rank(profile)
    frustration = signed_frustration_index(profile)

    return {
        "support_only": support,
        "cell_local_support": (rule_name, n, support),
        "support_plus_quota_step": (support, grand_req, top_req),
        "quota_margin_signature": (
            p_yes - grand_req,
            q_yes - grand_req,
            r_yes - grand_req,
            top_req - grand_req,
        ),
        "crossing_count": x_count,
        "compatibility_cycle_rank": cycle_rank,
        "signed_frustration_index": frustration,
        "graph_index_triple": (x_count, cycle_rank, frustration),
    }


CHANNEL_TYPES = {
    "support_only": "support_control",
    "cell_local_support": "quota_support_leak",
    "support_plus_quota_step": "quota_support_leak",
    "quota_margin_signature": "quota_support_leak",
    "crossing_count": "candidate_index",
    "compatibility_cycle_rank": "candidate_index",
    "signed_frustration_index": "candidate_index",
    "graph_index_triple": "candidate_index",
}


def analyze_universe():
    rules = rules_by_name()
    separators = {}
    channel_values = {name: {} for name in CHANNEL_TYPES}
    cell_reports = []
    item_counter = 0

    for rule_name, n in CELL_SPECS:
        rule = rules[rule_name]
        players = t426.players_for(n)
        coalitions = t426.canonical_coalitions(players)
        cell_separator_count = 0
        verdict_distribution = Counter()

        for serial, profile in enumerate(t426.enumerate_profiles(n)):
            item_id = f"{rule_name}@{n}:{serial}"
            sreport = t426.separator_report(profile, players, rule, coalitions)
            separator = sreport["separator"]
            separators[item_id] = separator
            cell_separator_count += separator
            verdict_distribution[sreport["verdict"]] += 1

            for channel, value in profile_channels(rule_name, n, profile).items():
                channel_values[channel][item_id] = value
            item_counter += 1

        cell_reports.append({
            "rule": rule_name,
            "n": n,
            "target_cell": (rule_name, n) in TARGET_CELLS,
            "n_profiles": 4 ** n,
            "separator_profiles": cell_separator_count,
            "verdict_distribution": {
                key: verdict_distribution[key]
                for key in sorted(verdict_distribution)
            },
            "grand_requirement": t426.quota_requirement(n, rule),
            "top_proper_requirement": t426.quota_requirement(n - 1, rule),
        })

    reports = {
        name: channel_report(name, CHANNEL_TYPES[name], channel_values[name], separators)
        for name in CHANNEL_TYPES
    }
    clean_candidate_channels = [
        name for name, report in reports.items()
        if report["guardrail_verdict"] == "CLEAN_INDEX"
    ]
    leaking_perfect_channels = [
        name for name, report in reports.items()
        if report["guardrail_verdict"] == "REJECT_LEAKAGE"
    ]

    return {
        "cell_reports": cell_reports,
        "n_profiles": item_counter,
        "separator_profiles": sum(separators.values()),
        "channel_reports": reports,
        "clean_candidate_channels": clean_candidate_channels,
        "leaking_perfect_channels": leaking_perfect_channels,
    }


def overall_verdict(universe):
    if universe["clean_candidate_channels"]:
        return {
            "verdict": "RECHECK_CLEAN_INDEX",
            "reading": (
                "At least one quota-independent candidate index perfectly "
                "predicts the high-quota separator over the target/control "
                "universe. Inspect before drawing any stronger conclusion."
            ),
        }

    if universe["leaking_perfect_channels"]:
        return {
            "verdict": "REDESIGN_THRESHOLD_INDEX_LEAKAGE",
            "reading": (
                "The only perfect separator channels read quota/support data: "
                "cell-local support, support plus quota step, or the direct quota "
                "margin signature. Every graph/frustration-style candidate index "
                "collides with nonseparator profiles. The T426 positives remain "
                "finite threshold testbeds, not clean M2 canonicity progress."
            ),
            "next_gate": (
                "Move to a genuinely different aggregation family or separator "
                "object, or predeclare a new index with an explicit no-leakage "
                "control stronger than support/quota-step recovery."
            ),
        }

    return {
        "verdict": "REDESIGN_NO_SEPARATOR_CHANNEL",
        "reading": "No tested channel predicts the high-quota separator.",
        "next_gate": "Move off the threshold-index lane.",
    }


def run():
    universe = analyze_universe()
    return {
        "artifact": "T427-m2-threshold-index-leakage-gate-v0.1",
        "cell_specs": [[rule, n] for rule, n in CELL_SPECS],
        "target_cells": [[rule, n] for rule, n in sorted(TARGET_CELLS)],
        "universe": universe,
        "overall_verdict": overall_verdict(universe),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
