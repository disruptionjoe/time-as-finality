"""Write T167 bounded ordinal-scaling stress-test results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_ordinal_scaling_stress import (
    run_t167_analysis,
    t167_result_to_dict,
)


RESULTS_JSON = Path("results/t54-ordinal-scaling-stress-v0.1.json")
RESULTS_MD = Path("results/t54-ordinal-scaling-stress-v0.1-results.md")


def main() -> None:
    payload = t167_result_to_dict(run_t167_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T167 Results: T54 Ordinal Scaling Stress Test",
        "",
        "## Exact Comparison Target",
        "",
        f"- Target: `{payload['comparison_target']}`",
        f"- Basis: {payload['target_basis']}",
        "",
        "## Size Summary",
        "",
        (
            "| n | Cases | T126 pass | T156 pass | Parent pass | Stable "
            "survivors | Stable fraction | Oriented classes | Dual classes | "
            "Largest class probability |"
        ),
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for audit in payload["size_audits"]:
        lines.append(
            "| "
            f"{audit['event_count']} | "
            f"{audit['total_rank_permutation_cases']} | "
            f"{audit['t126_pass_count']} | "
            f"{audit['t156_pass_count']} | "
            f"{audit['parent_interval_pass_count']} | "
            f"{audit['stable_labeled_survivor_count']} | "
            f"{_fraction(audit['stable_labeled_survivor_fraction'])} | "
            f"{audit['oriented_survivor_class_count']} | "
            f"{audit['order_dual_survivor_class_count']} | "
            f"{_fraction(audit['largest_oriented_class_probability'])} |"
        )

    lines.extend(
        [
            "",
            "## T126 Classifications",
            "",
        ]
    )
    for audit in payload["size_audits"]:
        lines.extend(
            [
                f"### n = {audit['event_count']}",
                "",
                "| Classification | Count |",
                "| --- | ---: |",
            ]
        )
        for row in audit["t126_classification_counts"]:
            lines.append(f"| `{row['classification']}` | {row['count']} |")
        lines.append("")

    lines.extend(["## Deletion Stability After Parent-Interval Pass", ""])
    for audit in payload["size_audits"]:
        lines.extend(
            [
                f"### n = {audit['event_count']}",
                "",
                "| Deletion pass count | Case count |",
                "| ---: | ---: |",
            ]
        )
        if audit["deletion_pass_distribution"]:
            for row in audit["deletion_pass_distribution"]:
                lines.append(f"| {row['deletion_pass_count']} | {row['case_count']} |")
        else:
            lines.append("| 0 | 0 |")
        lines.append("")

    lines.extend(["## Stable Strict-Pair Distributions", ""])
    for audit in payload["size_audits"]:
        lines.extend(
            [
                f"### n = {audit['event_count']}",
                "",
                "| Strict pairs | Stable labeled cases |",
                "| ---: | ---: |",
            ]
        )
        if audit["stable_strict_pair_distribution"]:
            for row in audit["stable_strict_pair_distribution"]:
                lines.append(f"| {row['strict_pair_count']} | {row['case_count']} |")
        else:
            lines.append("| 0 | 0 |")
        lines.append("")

    lines.extend(
        [
            "## One-Step Comparison",
            "",
            f"- n=6 stable fraction: {_fraction(payload['n6_stable_fraction'])}",
            f"- n=7 stable fraction: {_fraction(payload['n7_stable_fraction'])}",
            f"- Delta n=7 minus n=6: {_fraction(payload['one_step_fraction_delta'])}",
            (
                "- n=7 largest oriented class probability: "
                f"{_fraction(payload['n7_largest_class_probability'])}"
            ),
        ]
    )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened Or Falsified", "weakened_or_falsified"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
