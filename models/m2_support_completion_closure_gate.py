"""T430 - M2 Support-Completion Closure Gate.

T425-T429 tested the bounded post-Route-A M2 rescue branches one at a time:
inherited size sweep, threshold rules, threshold-index leakage, nonquota
selectors, and separator objects. This model turns those local negatives into a
single recorded-tier closure certificate for the tested support-family universe.

Recorded-tier only. No claim promotion. Cross-domain social-choice / index
language is object of study, never evidence for physics or a sibling repository.

Run:

    python -m models.m2_support_completion_closure_gate --write-results
    python -m pytest tests/test_m2_support_completion_closure_gate.py -q
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from models import m2_nonquota_aggregation_family_gate as t428
from models import m2_separator_object_support_gate as t429
from models import m2_size_sweep_absorption_gate as t425
from models import m2_threshold_index_leakage_gate as t427
from models import m2_threshold_rule_rescue_gate as t426


SOURCE_ARTIFACTS = {
    "T425": "results/T425-m2-size-sweep-absorption-gate-v0.1-results.md",
    "T426": "results/T426-m2-threshold-rule-rescue-gate-v0.1-results.md",
    "T427": "results/T427-m2-threshold-index-leakage-gate-v0.1-results.md",
    "T428": "results/T428-m2-nonquota-aggregation-family-gate-v0.1-results.md",
    "T429": "results/T429-m2-separator-object-support-gate-v0.1-results.md",
}


def inherited_size_absorption_certificate(t425_result):
    sizes = t425_result["size_reports"]
    n3 = sizes["3"]
    n4 = sizes["4"]
    n5 = sizes["5"]
    n4_absorbed = n4["verdict_distribution"]["ABSORBED"]
    n5_absorbed = n5["verdict_distribution"]["ABSORBED"]
    closed = (
        t425_result["overall_verdict"]["verdict"] == "REDESIGN"
        and n3["separator_profiles"] == 6
        and n4["separator_profiles"] == 0
        and n5["separator_profiles"] == 0
        and n4["larger_absorption_complete"]
        and n5["larger_absorption_complete"]
    )
    return {
        "branch": "inherited_strict_majority_size_sweep",
        "source": "T425",
        "closure_status": "closed_no_larger_target" if closed else "recheck",
        "closed": closed,
        "mechanism": "proper-subset absorption of every larger nonzero gap",
        "evidence": {
            "n3_separator_profiles": n3["separator_profiles"],
            "n4_separator_profiles": n4["separator_profiles"],
            "n5_separator_profiles": n5["separator_profiles"],
            "n4_absorbed_profiles": n4_absorbed,
            "n5_absorbed_profiles": n5_absorbed,
            "n4_larger_absorption_complete": n4["larger_absorption_complete"],
            "n5_larger_absorption_complete": n5["larger_absorption_complete"],
        },
        "reading": (
            "The inherited strict-majority M2 separator is atomic to n=3. At "
            "n=4 and n=5 there is no larger finality target for an index to "
            "compute because every nonzero gap is already absorbed by a proper "
            "3-judge subset."
        ),
    }


def threshold_leakage_certificate(t426_result, t427_result):
    t426_verdict = t426_result["overall_verdict"]
    t427_verdict = t427_result["overall_verdict"]
    t427_universe = t427_result["universe"]
    closed = (
        t426_verdict["verdict"] == "RECHECK_SIZE_MATCHED_THRESHOLD_ONLY"
        and t426_verdict["stable_fixed_quota_rules"] == []
        and t427_verdict["verdict"] == "REDESIGN_THRESHOLD_INDEX_LEAKAGE"
        and t427_universe["clean_candidate_channels"] == []
    )
    return {
        "branch": "threshold_rule_and_index_followup",
        "source": "T426+T427",
        "closure_status": "closed_threshold_support_leakage" if closed else "recheck",
        "closed": closed,
        "mechanism": "size-matched high-quota targets plus quota/support leakage",
        "evidence": {
            "survivor_cells": t426_verdict["survivor_cells"],
            "stable_fixed_quota_rules": t426_verdict["stable_fixed_quota_rules"],
            "clean_candidate_channels": t427_universe["clean_candidate_channels"],
            "leaking_perfect_channels": t427_universe["leaking_perfect_channels"],
            "separator_profiles_in_index_universe": t427_universe["separator_profiles"],
        },
        "reading": (
            "High quota rules create finite targets only in size-matched cells. "
            "The follow-up index probe finds no quota-independent clean index; "
            "perfect channels read support, quota step, or quota margin directly."
        ),
    }


def nonquota_selector_certificate(t428_result):
    verdict = t428_result["overall_verdict"]
    closed = (
        verdict["verdict"] == "REDESIGN_NONQUOTA_SELECTOR_COMPLETION"
        and verdict["stable_larger_n_families"] == []
        and verdict["support_leak_clean"] is True
    )
    return {
        "branch": "nonquota_full_judgment_selectors",
        "source": "T428",
        "closure_status": "closed_full_support_completion" if closed else "recheck",
        "closed": closed,
        "mechanism": "selector and tie-completion signal determined by full support counts",
        "evidence": {
            "stable_larger_n_families": verdict["stable_larger_n_families"],
            "larger_positive_cells": verdict["larger_positive_cells"],
            "support_leak_clean": verdict["support_leak_clean"],
        },
        "reading": (
            "Common nonquota selectors give only size-local larger positives, and "
            "every tested selector separator is constant on full support-count "
            "fibers over the four judgment states."
        ),
    }


def separator_object_certificate(t429_result):
    verdict = t429_result["overall_verdict"]
    closed = (
        verdict["verdict"] == "REDESIGN_SEPARATOR_SUPPORT_COMPLETION"
        and verdict["clean_stable_families"] == []
        and verdict["any_support_mixed"] is False
    )
    return {
        "branch": "separator_object_family",
        "source": "T429",
        "closure_status": "closed_ambient_support_completion" if closed else "recheck",
        "closed": closed,
        "mechanism": "stable larger-size object reads ambient support shape",
        "evidence": {
            "stable_larger_families": verdict["stable_larger_families"],
            "clean_stable_families": verdict["clean_stable_families"],
            "support_completed_stable_families": verdict[
                "support_completed_stable_families"
            ],
            "any_support_mixed": verdict["any_support_mixed"],
        },
        "reading": (
            "The only tested separator object stable at both n=4 and n=5 is an "
            "ambient-size support-shape predicate. All tested separator statuses "
            "are constant on full support-count fibers."
        ),
    }


def overall_verdict(certificates):
    closed = all(cert["closed"] for cert in certificates)
    if closed:
        return {
            "verdict": "REDESIGN_M2_BOUNDED_SUPPORT_COMPLETION_CLOSURE",
            "closed_branches": [cert["branch"] for cert in certificates],
            "open_branches": [],
            "reading": (
                "Within the bounded AND-doctrine M2 universe tested by T425-T429, "
                "the named rescue branches all close as no larger target, "
                "threshold/support leakage, full-support completion, or ambient-size "
                "support completion. The branch should not keep varying support, "
                "quota, selector, tie-completion, or simple separator-object knobs."
            ),
            "next_gate": (
                "A future M2 attempt must move off this support-family universe or "
                "predeclare an independent measurement channel with no-completion "
                "controls for support counts, ambient size, quota step, selector/tie "
                "completion, and proper-subset deletion-critical wording."
            ),
        }
    return {
        "verdict": "RECHECK_M2_CLOSURE",
        "closed_branches": [cert["branch"] for cert in certificates if cert["closed"]],
        "open_branches": [cert["branch"] for cert in certificates if not cert["closed"]],
        "reading": "At least one bounded M2 branch did not match its expected closure.",
        "next_gate": "Inspect the open branch certificate before drawing a conclusion.",
    }


def run():
    source_results = {
        "T425": t425.run(),
        "T426": t426.run(),
        "T427": t427.run(),
        "T428": t428.run(),
        "T429": t429.run(),
    }
    certificates = [
        inherited_size_absorption_certificate(source_results["T425"]),
        threshold_leakage_certificate(source_results["T426"], source_results["T427"]),
        nonquota_selector_certificate(source_results["T428"]),
        separator_object_certificate(source_results["T429"]),
    ]
    return {
        "artifact": "T430-m2-support-completion-closure-gate-v0.1",
        "scope": (
            "Finite recorded-tier closure over the already-tested M2 support-family "
            "branches in the AND-doctrine judgment-state universe, n in {3,4,5}."
        ),
        "source_artifacts": SOURCE_ARTIFACTS,
        "certificates": certificates,
        "overall_verdict": overall_verdict(certificates),
        "honest_ceiling": (
            "This is not a universal no-go theorem, not a claim-ledger movement, "
            "and not evidence for physics or a sibling repo. It closes only the "
            "bounded M2 support-family branches actually tested by T425-T429."
        ),
    }


def render_markdown(result):
    verdict = result["overall_verdict"]
    rows = []
    for cert in result["certificates"]:
        rows.append(
            "| {branch} | {source} | {status} | {mechanism} |".format(
                branch=cert["branch"],
                source=cert["source"],
                status=cert["closure_status"],
                mechanism=cert["mechanism"],
            )
        )

    source_lines = "\n".join(
        f"- {name}: `{path}`" for name, path in result["source_artifacts"].items()
    )

    return "\n".join(
        [
            "# T430 - M2 Support-Completion Closure Gate - v0.1 results",
            "",
            "> Recorded-tier exploratory closure artifact. `TESTS.md`, `ROADMAP.md`, "
            "and `CLAIM-LEDGER.md` are UNTOUCHED; the T-number lives only in this "
            "header / the spec header. NO claim promotion; ledger actions pause for "
            "Joe. Cross-domain social-choice / index language is the OBJECT OF STUDY, "
            "never evidence for physics or a sibling repo.",
            "",
            "- Spec (frozen first): `tests/T430-m2-support-completion-closure-gate.md`",
            "- Model: `models/m2_support_completion_closure_gate.py`",
            "- Tests: `tests/test_m2_support_completion_closure_gate.py`",
            "- Artifact JSON: `results/T430-m2-support-completion-closure-gate-v0.1.json`",
            "- Run: `python -m pytest tests/test_m2_support_completion_closure_gate.py -q`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Closure Map",
            "",
            "| branch | source | closure status | mechanism |",
            "| --- | --- | --- | --- |",
            *rows,
            "",
            "## Source Artifacts",
            "",
            source_lines,
            "",
            "## What this says about M2",
            "",
            "The T425-T429 support-family rescue sequence is closed at recorded tier. "
            "The inherited strict-majority lane has no larger target; threshold "
            "rules are size-matched testbeds whose index readings leak quota/support "
            "data; common nonquota selectors are full-support completions; and the "
            "only stable separator object reads ambient support shape directly.",
            "",
            verdict["next_gate"],
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a finite closure certificate for the bounded M2 support-family "
            "branches actually tested after T424.",
            "",
            "Does not earn: a universal no-go theorem, a closed M2 program, a stable "
            "M2 rescue, a canonical separator object, any claim-ledger movement, any "
            "physics-facing claim, or any cross-repo evidential use.",
            "",
            f"Honest ceiling: {result['honest_ceiling']}",
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
        json_path = results_dir / "T430-m2-support-completion-closure-gate-v0.1.json"
        md_path = results_dir / "T430-m2-support-completion-closure-gate-v0.1-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
