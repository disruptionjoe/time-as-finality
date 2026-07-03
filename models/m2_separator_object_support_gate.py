"""T429 - M2 Separator-Object Support Gate.

T428 blocked the common nonquota aggregation-family branch and left a genuinely
different separator object as the remaining bounded M2 escape hatch. This model
tests a small predeclared family of full-profile separator objects over the same
AND-doctrine judgment-state universe.

Recorded-tier only. No claim promotion. Cross-domain social-choice / index
language is object of study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_separator_object_support_gate --write-results
    python -m pytest tests/test_m2_separator_object_support_gate.py -q
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations, product
import json
from pathlib import Path


SIZES = (3, 4, 5)
STATES = ((0, 0), (0, 1), (1, 0), (1, 1))

OBJECT_FAMILIES = (
    {
        "name": "full_support_seen",
        "label": "all four judgment states appear",
        "object_class": "support_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "both_cross_diagonals_seen",
        "label": "both crossing diagonals appear",
        "object_class": "support_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "compatibility_cycle_positive",
        "label": "compatibility graph has positive cycle rank",
        "object_class": "compatibility_graph_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "signed_frustration_positive",
        "label": "complete signed graph has positive frustration index",
        "object_class": "signed_graph_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "crossing_count_exactly_one",
        "label": "exactly one crossing edge",
        "object_class": "crossing_graph_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "support_two_two",
        "label": "two states appear twice each",
        "object_class": "exact_support_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "support_2111",
        "label": "one duplicate plus all four states",
        "object_class": "exact_support_predicate",
        "uses_ambient_size": False,
    },
    {
        "name": "ambient_even_support_shape",
        "label": "ambient-size even support shape",
        "object_class": "ambient_size_support_predicate",
        "uses_ambient_size": True,
    },
)


def all_subsets(items):
    items = tuple(items)
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            yield tuple(combo)


def enumerate_profiles(n):
    return tuple(product(STATES, repeat=n))


def coalition_values(profile, coalition):
    return tuple(profile[i] for i in coalition)


def support_counts(values):
    counts = Counter(values)
    return tuple(counts.get(state, 0) for state in STATES)


def support_shape(values):
    return tuple(sorted(support_counts(values)))


def crosses(left, right):
    return left[0] != right[0] and left[1] != right[1]


def crossing_count(values):
    return sum(1 for i, j in combinations(range(len(values)), 2) if crosses(values[i], values[j]))


def compatibility_edges(values):
    return tuple(
        (i, j)
        for i, j in combinations(range(len(values)), 2)
        if not crosses(values[i], values[j])
    )


def component_count(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in edges:
        union(a, b)
    return len({find(i) for i in range(n)})


def compatibility_cycle_rank(values):
    if not values:
        return 0
    edges = compatibility_edges(values)
    return len(edges) - len(values) + component_count(len(values), edges)


def signed_frustration_index(values):
    n = len(values)
    if n < 2:
        return 0

    best = None
    for switch in product((1, -1), repeat=n):
        negative_edges = 0
        for i, j in combinations(range(n), 2):
            sign = -1 if crosses(values[i], values[j]) else 1
            if switch[i] * switch[j] * sign == -1:
                negative_edges += 1
        best = negative_edges if best is None else min(best, negative_edges)
    return best or 0


def ambient_even_shape(ambient_n):
    base, extra = divmod(ambient_n, len(STATES))
    return tuple(sorted([base + 1] * extra + [base] * (len(STATES) - extra)))


def object_value(name, values, ambient_n):
    counts = support_counts(values)
    shape = tuple(sorted(counts))
    nonzero_support = sum(1 for count in counts if count > 0)

    if name == "full_support_seen":
        return nonzero_support == len(STATES)
    if name == "both_cross_diagonals_seen":
        return bool(counts[0] and counts[1] and counts[2] and counts[3])
    if name == "compatibility_cycle_positive":
        return compatibility_cycle_rank(values) > 0
    if name == "signed_frustration_positive":
        return signed_frustration_index(values) > 0
    if name == "crossing_count_exactly_one":
        return crossing_count(values) == 1
    if name == "support_two_two":
        return shape == (0, 0, 2, 2)
    if name == "support_2111":
        return shape == (1, 1, 1, 2)
    if name == "ambient_even_support_shape":
        return shape == ambient_even_shape(ambient_n)
    raise ValueError(f"unknown separator object: {name}")


def separator_report(profile, family):
    n = len(profile)
    grand = tuple(range(n))
    proper_coalitions = tuple(S for S in all_subsets(grand) if len(S) < n)
    grand_value = object_value(family["name"], coalition_values(profile, grand), n)
    proper_value_exists = any(
        object_value(family["name"], coalition_values(profile, S), n)
        for S in proper_coalitions
    )

    if grand_value and not proper_value_exists:
        verdict = "SURVIVES-R1"
    elif grand_value and proper_value_exists:
        verdict = "ABSORBED"
    else:
        verdict = "no-separation"

    return {
        "separator": 1 if verdict == "SURVIVES-R1" else 0,
        "verdict": verdict,
        "grand_value": grand_value,
        "proper_value_exists": proper_value_exists,
    }


def _counter(counter):
    return {str(key): counter[key] for key in sorted(counter, key=str)}


def _profile_to_lists(profile):
    return [list(item) for item in profile]


def analyze_cell(n, family):
    verdict_distribution = Counter()
    support_fibers = defaultdict(Counter)
    support_shape_fibers = defaultdict(Counter)
    sample_separator = None
    sample_absorbed = None

    for serial, profile in enumerate(enumerate_profiles(n)):
        report = separator_report(profile, family)
        separator = report["separator"]
        verdict_distribution[report["verdict"]] += 1

        counts = support_counts(profile)
        shape = support_shape(profile)
        support_fibers[counts][separator] += 1
        support_shape_fibers[shape][separator] += 1

        if separator and sample_separator is None:
            sample_separator = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "support_counts": list(counts),
                "support_shape": list(shape),
                "compatibility_cycle_rank": compatibility_cycle_rank(profile),
                "signed_frustration_index": signed_frustration_index(profile),
                "crossing_count": crossing_count(profile),
            }
        if report["verdict"] == "ABSORBED" and sample_absorbed is None:
            sample_absorbed = {
                "serial": serial,
                "profile": _profile_to_lists(profile),
                "support_counts": list(counts),
                "support_shape": list(shape),
                "compatibility_cycle_rank": compatibility_cycle_rank(profile),
                "signed_frustration_index": signed_frustration_index(profile),
                "crossing_count": crossing_count(profile),
            }

    mixed_support_fibers = [
        {
            "support_counts": list(counts),
            "separator_0": values.get(0, 0),
            "separator_1": values.get(1, 0),
        }
        for counts, values in sorted(support_fibers.items())
        if values.get(0, 0) and values.get(1, 0)
    ]
    mixed_shape_fibers = [
        {
            "support_shape": list(shape),
            "separator_0": values.get(0, 0),
            "separator_1": values.get(1, 0),
        }
        for shape, values in sorted(support_shape_fibers.items())
        if values.get(0, 0) and values.get(1, 0)
    ]

    return {
        "n": n,
        "n_profiles": len(enumerate_profiles(n)),
        "separator_profiles": verdict_distribution["SURVIVES-R1"],
        "absorbed_profiles": verdict_distribution["ABSORBED"],
        "grand_true_profiles": (
            verdict_distribution["SURVIVES-R1"] + verdict_distribution["ABSORBED"]
        ),
        "verdict_distribution": _counter(verdict_distribution),
        "support_fiber_mixed_separator_count": len(mixed_support_fibers),
        "support_fiber_mixed_examples": mixed_support_fibers[:5],
        "support_shape_mixed_separator_count": len(mixed_shape_fibers),
        "support_shape_mixed_examples": mixed_shape_fibers[:5],
        "sample_separator": sample_separator,
        "sample_absorbed": sample_absorbed,
    }


def analyze_family(family):
    return {
        "family": dict(family),
        "ambient_even_shape_by_size": {
            str(n): list(ambient_even_shape(n))
            for n in SIZES
            if family["name"] == "ambient_even_support_shape"
        },
        "size_reports": {str(n): analyze_cell(n, family) for n in SIZES},
    }


def overall_verdict(family_reports):
    stable_larger_families = []
    clean_stable_families = []
    support_completed_stable_families = []
    any_support_mixed = False

    for report in family_reports:
        name = report["family"]["name"]
        n4 = report["size_reports"]["4"]
        n5 = report["size_reports"]["5"]
        has_larger_stability = n4["separator_profiles"] > 0 and n5["separator_profiles"] > 0
        support_mixed = (
            n4["support_fiber_mixed_separator_count"] > 0
            or n5["support_fiber_mixed_separator_count"] > 0
        )
        any_support_mixed = any_support_mixed or support_mixed

        if has_larger_stability:
            record = {
                "family": name,
                "object_class": report["family"]["object_class"],
                "uses_ambient_size": report["family"]["uses_ambient_size"],
                "n4_separator_profiles": n4["separator_profiles"],
                "n5_separator_profiles": n5["separator_profiles"],
                "support_fiber_mixed_separator_count": (
                    n4["support_fiber_mixed_separator_count"]
                    + n5["support_fiber_mixed_separator_count"]
                ),
            }
            stable_larger_families.append(record)
            if support_mixed and not report["family"]["uses_ambient_size"]:
                clean_stable_families.append(record)
            else:
                support_completed_stable_families.append(record)

    if clean_stable_families:
        return {
            "verdict": "RECHECK_CLEAN_SEPARATOR_OBJECT",
            "stable_larger_families": stable_larger_families,
            "clean_stable_families": clean_stable_families,
            "support_completed_stable_families": support_completed_stable_families,
            "reading": (
                "At least one larger-n separator object is stable across n=4 and n=5 "
                "without reducing to full-support fibers. Inspect before drawing a "
                "stronger conclusion."
            ),
        }

    if stable_larger_families:
        return {
            "verdict": "REDESIGN_SEPARATOR_SUPPORT_COMPLETION",
            "stable_larger_families": stable_larger_families,
            "clean_stable_families": clean_stable_families,
            "support_completed_stable_families": support_completed_stable_families,
            "any_support_mixed": any_support_mixed,
            "reading": (
                "The only tested separator object with positives at both n=4 and "
                "n=5 is an ambient-size support-shape predicate. All tested separator "
                "positives are constant on full-support fibers, so the branch produces "
                "support/ambient-size completion artifacts rather than an independent "
                "M2 canonicity channel."
            ),
            "next_gate": (
                "Move off this bounded separator-object family, or predeclare a "
                "separator whose value is not recoverable from full support counts, "
                "ambient size, or explicit deletion-critical completion."
            ),
        }

    return {
        "verdict": "REDESIGN_NO_STABLE_SEPARATOR_OBJECT",
        "stable_larger_families": stable_larger_families,
        "clean_stable_families": clean_stable_families,
        "support_completed_stable_families": support_completed_stable_families,
        "any_support_mixed": any_support_mixed,
        "reading": (
            "No tested separator object produces SURVIVES-R1 positives at both "
            "n=4 and n=5."
        ),
        "next_gate": "Move off this bounded separator-object family.",
    }


def run():
    family_reports = [analyze_family(family) for family in OBJECT_FAMILIES]
    return {
        "artifact": "T429-m2-separator-object-support-gate-v0.1",
        "sizes": list(SIZES),
        "state_order": [list(state) for state in STATES],
        "object_family_reports": family_reports,
        "overall_verdict": overall_verdict(family_reports),
    }


def render_markdown(result):
    reports = result["object_family_reports"]
    verdict = result["overall_verdict"]

    rows = []
    for report in reports:
        family = report["family"]
        n4 = report["size_reports"]["4"]
        n5 = report["size_reports"]["5"]
        rows.append(
            "| {name} | {object_class} | {ambient} | {n4_sep} | {n4_abs} | "
            "{n5_sep} | {n5_abs} |".format(
                name=family["name"],
                object_class=family["object_class"],
                ambient="yes" if family["uses_ambient_size"] else "no",
                n4_sep=n4["separator_profiles"],
                n4_abs=n4["absorbed_profiles"],
                n5_sep=n5["separator_profiles"],
                n5_abs=n5["absorbed_profiles"],
            )
        )

    stable = verdict.get("stable_larger_families", [])
    stable_lines = "\n".join(
        f"- `{item['family']}`: n=4 {item['n4_separator_profiles']} positives; "
        f"n=5 {item['n5_separator_profiles']} positives; "
        f"ambient-size leak = {item['uses_ambient_size']}"
        for item in stable
    ) or "- none"

    return "\n".join(
        [
            "# T429 - M2 Separator-Object Support Gate - v0.1 results",
            "",
            "> Recorded-tier exploratory guardrail. `TESTS.md` and `CLAIM-LEDGER.md` "
            "are UNTOUCHED; the T-number lives only in this header / the spec header. "
            "NO claim promotion; ledger actions pause for Joe. Cross-domain social-"
            "choice / index language is the OBJECT OF STUDY, never evidence for physics "
            "or a sibling repo.",
            "",
            "- Spec (frozen first): `tests/T429-m2-separator-object-support-gate.md`",
            "- Model: `models/m2_separator_object_support_gate.py`",
            "- Tests: `tests/test_m2_separator_object_support_gate.py`",
            "- Artifact JSON: `results/T429-m2-separator-object-support-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_m2_separator_object_support_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Separator-object map",
            "",
            "| object | class | ambient size? | n=4 SURVIVES-R1 | n=4 absorbed | "
            "n=5 SURVIVES-R1 | n=5 absorbed |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: |",
            *rows,
            "",
            "## Stable larger-size cells",
            "",
            stable_lines,
            "",
            "The stable larger-size row is not clean M2 canonicity progress: it reads the "
            "ambient support shape directly. In every tested object family, separator "
            "status is constant on full support-count fibers, so support completion "
            "recovers the signal.",
            "",
            "## What this says about M2",
            "",
            "The bounded separator-object branch does not repair the M2 canonicity problem. "
            "Non-ambient objects either appear only at one finite size or are absorbed by "
            "proper subsets at the next size. The only cross-size object is an explicit "
            "ambient-size support predicate, which is exactly the kind of completion leak "
            "the gate was built to reject.",
            "",
            "Future M2 work should move off this family, or predeclare a separator whose "
            "value is not recoverable from support counts, ambient size, deletion-"
            "critical wording, or the same graph diagnostics already tested.",
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite guardrail for the remaining simple separator-object escape "
            "hatch after T428.",
            "",
            "Does not earn: a universal no-go theorem, a stable M2 rescue, a canonical "
            "separator object, any claim-ledger movement, any physics-facing claim, or "
            "any cross-repo evidential use.",
            "",
        ]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T429-m2-separator-object-support-gate-v0.1.json"
        md_path = results_dir / "T429-m2-separator-object-support-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
