"""T426 - M2 Threshold-Rule Rescue Gate.

T425 closed the direct larger-index rescue under the inherited AND doctrine and
strict-majority / tie-reject rule. This model checks the threshold-rule rescue
class named by T425 before any new index channel is allowed.

It keeps the AND doctrine fixed, derives every judge's conclusion as r_i = p_i
AND q_i, and varies only a predeclared quota rule for coalition aggregation.
The question is whether a fixed quota creates a non-atomic n=4 or n=5
SURVIVES-R1 finality target, or whether the apparent target is a size-matched
threshold artifact.

Recorded-tier only. No claim promotion. Cross-domain social-choice / index
language is object of study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_threshold_rule_rescue_gate
    python -m pytest tests/test_m2_threshold_rule_rescue_gate.py -q
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
import json

from models.legitimacy_shapley_finality_probe import (
    all_subsets,
    joint_record_completion_verdict,
)
from models.m2_observer_game import and_doctrine


SIZES = (3, 4, 5)
STATES = ((0, 0), (0, 1), (1, 0), (1, 1))

RULES = (
    {"name": "strict_majority", "kind": "strict_majority"},
    {"name": "weak_half", "kind": "quota", "num": 1, "den": 2},
    {"name": "two_thirds", "kind": "quota", "num": 2, "den": 3},
    {"name": "three_quarters", "kind": "quota", "num": 3, "den": 4},
    {"name": "four_fifths", "kind": "quota", "num": 4, "den": 5},
    {"name": "unanimity", "kind": "quota", "num": 1, "den": 1},
)


def players_for(n):
    return tuple(range(1, n + 1))


def canonical_coalitions(players):
    return tuple(
        sorted((frozenset(S) for S in all_subsets(players)), key=lambda s: (len(s), tuple(s)))
    )


def enumerate_profiles(n):
    return list(product(STATES, repeat=n))


def columns(profile, players):
    p = {players[i]: profile[i][0] for i in range(len(players))}
    q = {players[i]: profile[i][1] for i in range(len(players))}
    r = {players[i]: and_doctrine(profile[i][0], profile[i][1]) for i in range(len(players))}
    return p, q, r


def _ceil_div(a, b):
    return (a + b - 1) // b


def quota_requirement(size, rule):
    """Number of yes votes needed for a coalition of this size to accept."""
    if size == 0:
        return None
    if rule["kind"] == "strict_majority":
        return (size // 2) + 1
    return _ceil_div(rule["num"] * size, rule["den"])


def accepts(ones, size, rule):
    req = quota_requirement(size, rule)
    return 0 if req is None else int(ones >= req)


def premise_verdict(S, p, q, rule):
    S = frozenset(S)
    return (
        accepts(sum(p[i] for i in S), len(S), rule)
        & accepts(sum(q[i] for i in S), len(S), rule)
    )


def conclusion_verdict(S, r, rule):
    S = frozenset(S)
    return accepts(sum(r[i] for i in S), len(S), rule)


def gap_value(S, p, q, r, rule):
    return premise_verdict(S, p, q, rule) - conclusion_verdict(S, r, rule)


def vgap_vector(profile, players, rule, coalitions):
    p, q, r = columns(profile, players)
    return tuple(gap_value(S, p, q, r, rule) for S in coalitions)


def moebius_dividends_from_values(values, coalitions):
    div = {}
    for S in coalitions:
        d = 0
        for T in coalitions:
            if T <= S:
                d += ((-1) ** (len(S) - len(T))) * values[T]
        if d != 0:
            div[S] = d
    return div


def gap_dividends(profile, players, rule, coalitions):
    p, q, r = columns(profile, players)
    values = {S: gap_value(S, p, q, r, rule) for S in coalitions}
    return moebius_dividends_from_values(values, coalitions)


def separator_report(profile, players, rule, coalitions):
    div = gap_dividends(profile, players, rule, coalitions)
    jrc = joint_record_completion_verdict(div, {}, players=players)
    return {
        "separator": 1 if jrc.get("verdict") == "SURVIVES-R1" else 0,
        "verdict": jrc.get("verdict"),
        "min_sep_size": jrc.get("min_sep_size"),
        "datum_in_proper_subset": jrc.get("datum_in_proper_subset"),
        "min_sep_coalition": jrc.get("min_sep_coalition"),
    }


def _counter(counter):
    def sort_key(k):
        if k is None:
            return (0, "")
        return (1, str(k))

    return {"none" if k is None else str(k): counter[k] for k in sorted(counter, key=sort_key)}


def _profile_to_lists(profile):
    return [list(pair) for pair in profile]


def run_cell(n, rule):
    players = players_for(n)
    coalitions = canonical_coalitions(players)
    profiles = enumerate_profiles(n)

    verdict_distribution = Counter()
    min_sep_distribution = Counter()
    fibers = defaultdict(list)
    separator_by_serial = {}
    sample_separator = None
    sample_absorbed = None

    for serial, profile in enumerate(profiles):
        key = vgap_vector(profile, players, rule, coalitions)
        fibers[key].append(serial)

        sreport = separator_report(profile, players, rule, coalitions)
        separator_by_serial[serial] = sreport["separator"]
        verdict_distribution[sreport["verdict"]] += 1
        min_sep_distribution[sreport["min_sep_size"]] += 1

        if sreport["verdict"] == "SURVIVES-R1" and sample_separator is None:
            sample_separator = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "v_gap": list(key),
                "min_sep_size": sreport["min_sep_size"],
                "min_sep_coalition": sreport["min_sep_coalition"],
            }
        if sreport["verdict"] == "ABSORBED" and sample_absorbed is None:
            sample_absorbed = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "v_gap": list(key),
                "min_sep_size": sreport["min_sep_size"],
                "min_sep_coalition": sreport["min_sep_coalition"],
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
    no_separation = verdict_distribution["no-separation"]
    nonzero_gap_profiles = len(profiles) - no_separation
    absorbed_profiles = verdict_distribution["ABSORBED"]
    reqs = {str(size): quota_requirement(size, rule) for size in range(0, n + 1)}

    top_proper = quota_requirement(n - 1, rule) if n > 1 else None
    grand_req = quota_requirement(n, rule)
    size_matched_high_quota_shape = (
        n >= 4
        and grand_req == n - 1
        and top_proper == n - 1
    )

    return {
        "n": n,
        "rule": rule["name"],
        "quota_requirements_by_coalition_size": reqs,
        "n_profiles": len(profiles),
        "n_vgap_fibers": len(fibers),
        "separator_profiles": separator_profiles,
        "nonzero_gap_profiles": nonzero_gap_profiles,
        "absorbed_profiles": absorbed_profiles,
        "verdict_distribution": _counter(verdict_distribution),
        "min_sep_size_distribution": _counter(min_sep_distribution),
        "fiber_mixed_separator_count": mixed_fibers,
        "separator_fiber_sizes": sorted(separator_fiber_sizes),
        "size_matched_high_quota_shape": size_matched_high_quota_shape,
        "sample_separator": sample_separator,
        "sample_absorbed": sample_absorbed,
    }


def run_rule(rule):
    return {str(n): run_cell(n, rule) for n in SIZES}


def _rule_label(rule):
    if rule["kind"] == "strict_majority":
        return "strict majority / tie reject"
    return f'{rule["num"]}/{rule["den"]} quota'


def overall_verdict(rule_reports):
    strict = rule_reports["strict_majority"]
    strict_regression_ok = (
        strict["3"]["separator_profiles"] == 6
        and strict["4"]["separator_profiles"] == 0
        and strict["5"]["separator_profiles"] == 0
        and strict["4"]["absorbed_profiles"] == 60
        and strict["5"]["absorbed_profiles"] == 390
    )

    survivor_cells = []
    for rule in RULES:
        if rule["name"] == "strict_majority":
            continue
        for n in (4, 5):
            cell = rule_reports[rule["name"]][str(n)]
            if cell["separator_profiles"] > 0:
                survivor_cells.append({
                    "rule": rule["name"],
                    "label": _rule_label(rule),
                    "n": n,
                    "separator_profiles": cell["separator_profiles"],
                    "min_sep_size_distribution": cell["min_sep_size_distribution"],
                    "size_matched_high_quota_shape": cell["size_matched_high_quota_shape"],
                })

    stable_fixed_quota_rules = []
    for rule in RULES:
        if rule["name"] == "strict_majority":
            continue
        if (
            rule_reports[rule["name"]]["4"]["separator_profiles"] > 0
            and rule_reports[rule["name"]]["5"]["separator_profiles"] > 0
        ):
            stable_fixed_quota_rules.append(rule["name"])

    if survivor_cells and not stable_fixed_quota_rules:
        verdict = "RECHECK_SIZE_MATCHED_THRESHOLD_ONLY"
        reading = (
            "Fixed high quota fractions can create larger-n SURVIVES-R1 targets, "
            "but only in size-matched cells: 3/4 at n=4 and 4/5 at n=5. No single "
            "fixed quota survives both n=4 and n=5, and moving the same rule one "
            "size up either absorbs the datum into proper subsets or removes it."
        )
        next_gate = (
            "Treat the high-quota targets as finite testbeds, not a stable M2 "
            "rescue. A follow-up index/fiber probe must include threshold-tuning "
            "controls before claiming progress on canonicity."
        )
    elif survivor_cells:
        verdict = "RECHECK_STABLE_THRESHOLD_CANDIDATE"
        reading = (
            "At least one predeclared fixed quota has larger-n SURVIVES-R1 targets "
            "at both n=4 and n=5; inspect it as a possible threshold-rule rescue."
        )
        next_gate = "Run an index/fiber agreement probe on the stable quota rule."
    else:
        verdict = "REDESIGN"
        reading = (
            "No predeclared quota rule creates a larger-n SURVIVES-R1 target under "
            "the AND doctrine."
        )
        next_gate = (
            "Move off threshold rules toward a different aggregation family or "
            "separator object."
        )

    return {
        "verdict": verdict,
        "strict_majority_regression_ok": strict_regression_ok,
        "survivor_cells": survivor_cells,
        "stable_fixed_quota_rules": stable_fixed_quota_rules,
        "reading": reading,
        "next_gate": next_gate,
    }


def run():
    rules = {rule["name"]: {**rule, "label": _rule_label(rule)} for rule in RULES}
    reports = {rule["name"]: run_rule(rule) for rule in RULES}
    return {
        "artifact": "T426-m2-threshold-rule-rescue-gate-v0.1",
        "sizes": list(SIZES),
        "rules": rules,
        "overall_verdict": overall_verdict(reports),
        "rule_reports": reports,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
