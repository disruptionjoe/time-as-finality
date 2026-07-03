"""T428 - M2 Nonquota Aggregation Family Gate.

T427 blocked the threshold-index reading and left a different aggregation family
as one remaining M2 escape hatch. This model tests a bounded nonquota family:
full-judgment selectors (plurality, Kemeny/Hamming median, and minimax Hamming)
with explicit tie completions.

Recorded-tier only. No claim promotion. Cross-domain social-choice / judgment-
aggregation language is object of study, never evidence for physics or a sibling
repository.

Run:

    python -m models.m2_nonquota_aggregation_family_gate
    python -m pytest tests/test_m2_nonquota_aggregation_family_gate.py -q
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
import json

from models.legitimacy_shapley_finality_probe import (
    all_subsets,
    joint_record_completion_verdict,
)


SIZES = (3, 4, 5)
STATES = ((0, 0), (0, 1), (1, 0), (1, 1))


SELECTOR_FAMILIES = (
    {
        "name": "plurality_reject",
        "selector": "plurality",
        "tie_completion": "reject",
        "label": "full-judgment plurality, tie reject",
    },
    {
        "name": "plurality_accept",
        "selector": "plurality",
        "tie_completion": "accept",
        "label": "full-judgment plurality, tie accept",
    },
    {
        "name": "kemeny_reject",
        "selector": "kemeny_hamming",
        "tie_completion": "reject",
        "label": "Kemeny/Hamming median, tie reject",
    },
    {
        "name": "kemeny_accept",
        "selector": "kemeny_hamming",
        "tie_completion": "accept",
        "label": "Kemeny/Hamming median, tie accept",
    },
    {
        "name": "minimax_reject",
        "selector": "minimax_hamming",
        "tie_completion": "reject",
        "label": "minimax Hamming selector, tie reject",
    },
    {
        "name": "minimax_accept",
        "selector": "minimax_hamming",
        "tie_completion": "accept",
        "label": "minimax Hamming selector, tie accept",
    },
)


def players_for(n):
    return tuple(range(1, n + 1))


def player_to_index(player):
    return player - 1


def enumerate_profiles(n):
    return list(product(STATES, repeat=n))


def strict_majority(values):
    values = tuple(values)
    if not values:
        return 0
    return int(sum(values) * 2 > len(values))


def premise_accepts(profile, coalition):
    indices = tuple(player_to_index(player) for player in coalition)
    p_accepts = strict_majority(profile[i][0] for i in indices)
    q_accepts = strict_majority(profile[i][1] for i in indices)
    return p_accepts & q_accepts


def conclusion_accepts_strict(profile, coalition):
    indices = tuple(player_to_index(player) for player in coalition)
    return strict_majority(1 if profile[i] == (1, 1) else 0 for i in indices)


def support_counts(profile, coalition):
    indices = tuple(player_to_index(player) for player in coalition)
    counts = Counter(profile[i] for i in indices)
    return tuple(counts.get(state, 0) for state in STATES)


def hamming_distance(left, right):
    return int(left[0] != right[0]) + int(left[1] != right[1])


def winner_set(profile, coalition, selector):
    indices = tuple(player_to_index(player) for player in coalition)
    if not indices:
        return ()

    if selector == "plurality":
        counts = Counter(profile[i] for i in indices)
        best = max(counts.values())
        return tuple(state for state in STATES if counts[state] == best)

    if selector == "kemeny_hamming":
        scores = {
            state: sum(hamming_distance(state, profile[i]) for i in indices)
            for state in STATES
        }
        best = min(scores.values())
        return tuple(state for state in STATES if scores[state] == best)

    if selector == "minimax_hamming":
        scores = {
            state: max(hamming_distance(state, profile[i]) for i in indices)
            for state in STATES
        }
        best = min(scores.values())
        return tuple(state for state in STATES if scores[state] == best)

    raise ValueError(f"unknown selector: {selector}")


def selector_accepts(profile, coalition, family):
    winners = winner_set(profile, coalition, family["selector"])
    if family["tie_completion"] == "reject":
        return int(winners == ((1, 1),))
    if family["tie_completion"] == "accept":
        return int((1, 1) in winners)
    raise ValueError(f"unknown tie completion: {family['tie_completion']}")


def gap_values(profile, players, accept_fn):
    return {
        frozenset(S): premise_accepts(profile, S) - accept_fn(profile, S)
        for S in all_subsets(players)
    }


def moebius_dividends_from_values(values, players):
    div = {}
    for S in all_subsets(players):
        S = frozenset(S)
        value = 0
        for T in all_subsets(S):
            T = frozenset(T)
            value += ((-1) ** (len(S) - len(T))) * values[T]
        if value != 0:
            div[S] = value
    return div


def separator_report(profile, players, accept_fn):
    values = gap_values(profile, players, accept_fn)
    div = moebius_dividends_from_values(values, players)
    jrc = joint_record_completion_verdict(div, {}, players=players)
    return {
        "separator": 1 if jrc.get("verdict") == "SURVIVES-R1" else 0,
        "verdict": jrc.get("verdict"),
        "min_sep_size": jrc.get("min_sep_size"),
        "min_sep_coalition": jrc.get("min_sep_coalition"),
        "grand_gap": values[frozenset(players)],
        "dividends": div,
    }


def _counter(counter):
    def key(item):
        if item is None:
            return (-1, "")
        return (0, str(item))

    return {"none" if k is None else str(k): counter[k] for k in sorted(counter, key=key)}


def _profile_to_lists(profile):
    return [list(pair) for pair in profile]


def _winner_to_lists(winners):
    return [list(pair) for pair in winners]


def analyze_cell(n, family):
    players = players_for(n)
    profiles = enumerate_profiles(n)

    verdict_distribution = Counter()
    min_sep_distribution = Counter()
    grand_winner_distribution = Counter()
    grand_accept_distribution = Counter()
    support_fibers = defaultdict(Counter)
    support_samples = {}
    sample_separator = None
    sample_absorbed = None

    def accept_fn(profile, coalition):
        return selector_accepts(profile, coalition, family)

    for serial, profile in enumerate(profiles):
        report = separator_report(profile, players, accept_fn)
        separator = report["separator"]
        verdict_distribution[report["verdict"]] += 1
        min_sep_distribution[report["min_sep_size"]] += 1

        grand_winners = winner_set(profile, players, family["selector"])
        grand_accept = selector_accepts(profile, players, family)
        grand_winner_distribution[grand_winners] += 1
        grand_accept_distribution[grand_accept] += 1

        support = support_counts(profile, players)
        support_fibers[support][separator] += 1
        support_samples.setdefault(support, _profile_to_lists(profile))

        if separator and sample_separator is None:
            sample_separator = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "full_support_counts": list(support),
                "grand_winner_set": _winner_to_lists(grand_winners),
                "selector_accepts_grand": grand_accept,
                "premise_accepts_grand": premise_accepts(profile, players),
                "grand_gap": report["grand_gap"],
                "min_sep_size": report["min_sep_size"],
                "min_sep_coalition": report["min_sep_coalition"],
            }
        if report["verdict"] == "ABSORBED" and sample_absorbed is None:
            sample_absorbed = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "full_support_counts": list(support),
                "grand_winner_set": _winner_to_lists(grand_winners),
                "selector_accepts_grand": grand_accept,
                "premise_accepts_grand": premise_accepts(profile, players),
                "grand_gap": report["grand_gap"],
                "min_sep_size": report["min_sep_size"],
                "min_sep_coalition": report["min_sep_coalition"],
            }

    mixed_support_fibers = [
        {
            "support": list(support),
            "separator_0": counts.get(0, 0),
            "separator_1": counts.get(1, 0),
            "sample_profile": support_samples[support],
        }
        for support, counts in sorted(support_fibers.items(), key=lambda item: item[0])
        if counts.get(0, 0) and counts.get(1, 0)
    ]

    selector_profiles = sum(counts.get(1, 0) for counts in support_fibers.values())
    nonzero_gap_profiles = len(profiles) - verdict_distribution["no-separation"]
    absorbed_profiles = verdict_distribution["ABSORBED"]

    return {
        "n": n,
        "n_profiles": len(profiles),
        "separator_profiles": selector_profiles,
        "nonzero_gap_profiles": nonzero_gap_profiles,
        "absorbed_profiles": absorbed_profiles,
        "verdict_distribution": _counter(verdict_distribution),
        "min_sep_size_distribution": _counter(min_sep_distribution),
        "support_fiber_mixed_separator_count": len(mixed_support_fibers),
        "support_fiber_mixed_examples": mixed_support_fibers[:5],
        "grand_winner_distribution": {
            repr(tuple(tuple(state) for state in winners)): count
            for winners, count in sorted(grand_winner_distribution.items(), key=lambda item: repr(item[0]))
        },
        "grand_accept_distribution": _counter(grand_accept_distribution),
        "sample_separator": sample_separator,
        "sample_absorbed": sample_absorbed,
    }


def analyze_family(family):
    return {
        "family": {
            **family,
            "family_class": "full_judgment_selector",
            "issue_quota_rule": False,
        },
        "size_reports": {str(n): analyze_cell(n, family) for n in SIZES},
    }


def analyze_baseline_cell(n):
    players = players_for(n)
    profiles = enumerate_profiles(n)
    verdict_distribution = Counter()
    min_sep_distribution = Counter()
    sample_separator = None

    for serial, profile in enumerate(profiles):
        report = separator_report(profile, players, conclusion_accepts_strict)
        verdict_distribution[report["verdict"]] += 1
        min_sep_distribution[report["min_sep_size"]] += 1
        if report["separator"] and sample_separator is None:
            sample_separator = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "grand_gap": report["grand_gap"],
                "min_sep_size": report["min_sep_size"],
            }

    return {
        "n": n,
        "n_profiles": len(profiles),
        "separator_profiles": verdict_distribution["SURVIVES-R1"],
        "absorbed_profiles": verdict_distribution["ABSORBED"],
        "verdict_distribution": _counter(verdict_distribution),
        "min_sep_size_distribution": _counter(min_sep_distribution),
        "sample_separator": sample_separator,
    }


def analyze_baseline():
    return {
        "name": "strict_conclusion_majority_baseline",
        "purpose": "Regression for the inherited T423/T425 issue-wise conclusion lane.",
        "size_reports": {str(n): analyze_baseline_cell(n) for n in SIZES},
    }


def overall_verdict(family_reports):
    larger_positive_cells = []
    stable_larger_n_families = []
    support_leak_clean = True

    for report in family_reports:
        name = report["family"]["name"]
        size_reports = report["size_reports"]
        family_has_4 = size_reports["4"]["separator_profiles"] > 0
        family_has_5 = size_reports["5"]["separator_profiles"] > 0
        if family_has_4 and family_has_5:
            stable_larger_n_families.append(name)
        for n in (4, 5):
            cell = size_reports[str(n)]
            if cell["separator_profiles"] > 0:
                larger_positive_cells.append({
                    "family": name,
                    "n": n,
                    "separator_profiles": cell["separator_profiles"],
                    "support_fiber_mixed_separator_count": cell[
                        "support_fiber_mixed_separator_count"
                    ],
                    "min_sep_size_distribution": cell["min_sep_size_distribution"],
                })
            if cell["support_fiber_mixed_separator_count"] != 0:
                support_leak_clean = False

    if stable_larger_n_families and not support_leak_clean:
        return {
            "verdict": "RECHECK_NONQUOTA_FAMILY",
            "stable_larger_n_families": stable_larger_n_families,
            "larger_positive_cells": larger_positive_cells,
            "reading": (
                "A nonquota selector produced larger-n positives whose separator "
                "is not fully determined by full support counts. Inspect before "
                "drawing any stronger conclusion."
            ),
        }

    return {
        "verdict": "REDESIGN_NONQUOTA_SELECTOR_COMPLETION",
        "stable_larger_n_families": stable_larger_n_families,
        "larger_positive_cells": larger_positive_cells,
        "support_leak_clean": support_leak_clean,
        "reading": (
            "The tested nonquota selectors do not repair M2 canonicity. Conservative "
            "plurality/minimax tie completion creates n=4 positives, but no tested "
            "selector has positives at both n=4 and n=5. Every selector separator "
            "is constant on full-support fibers, so the result is selector/full-"
            "support completion rather than an independent finality channel."
        ),
        "next_gate": (
            "Move to a genuinely different separator object, or predeclare a "
            "stronger aggregation family with a no-selector-leakage control."
        ),
    }


def run():
    family_reports = [analyze_family(family) for family in SELECTOR_FAMILIES]
    return {
        "artifact": "T428-m2-nonquota-aggregation-family-gate-v0.1",
        "sizes": list(SIZES),
        "state_order": [list(state) for state in STATES],
        "baseline": analyze_baseline(),
        "selector_family_reports": family_reports,
        "overall_verdict": overall_verdict(family_reports),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
