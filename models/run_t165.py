"""Write T165 exact ordinal-sprinkling stress-test results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_survivor_sprinkling_stress import (
    run_t165_analysis,
    t165_result_to_dict,
)


RESULTS_JSON = Path("results/t54-survivor-sprinkling-stress-v0.1.json")
RESULTS_MD = Path("results/t54-survivor-sprinkling-stress-v0.1-results.md")


def main() -> None:
    payload = t165_result_to_dict(run_t165_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T165 Results: T54 Survivor Sprinkling Stress Test",
        "",
        "## Exact Comparison Target",
        "",
        f"- Target: `{payload['comparison_target']}`",
        f"- Basis: {payload['target_basis']}",
        "",
        "## Aggregate Checks",
        "",
        f"- Total rank-permutation cases: {payload['total_rank_permutation_cases']}",
        f"- T126 pass count: {payload['t126_pass_count']}",
        f"- T156 pass count: {payload['t156_pass_count']}",
        f"- Parent-interval pass count: {payload['parent_interval_pass_count']}",
        f"- Stable labeled survivors: {payload['stable_labeled_survivor_count']}",
        (
            "- Stable labeled survivor fraction: "
            f"{_fraction(payload['stable_labeled_survivor_fraction'])}"
        ),
        (
            "- Oriented survivor classes: "
            f"{payload['oriented_survivor_class_count']}"
        ),
        (
            "- Order-dual survivor classes: "
            f"{payload['order_dual_survivor_class_count']}"
        ),
        (
            "- Largest oriented class probability: "
            f"{_fraction(payload['largest_oriented_class_probability'])}"
        ),
        (
            "- All oriented classes below one percent: "
            f"{payload['all_oriented_classes_below_one_percent']}"
        ),
        "",
        "## Conditioning Stages",
        "",
        (
            "| Stage | Pass count | Unconditional fraction | "
            "Conditional fraction | Interpretation |"
        ),
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for stage in payload["conditioning_stages"]:
        lines.append(
            "| "
            f"{stage['stage']} | "
            f"{stage['pass_count']} | "
            f"{_fraction(stage['unconditional_fraction'])} | "
            f"{_fraction(stage['conditional_fraction'])} | "
            f"{stage['interpretation']} |"
        )

    lines.extend(
        [
            "",
            "## Strict-Pair Distributions",
            "",
            "### Full 720-Case Ensemble",
            "",
            "| Strict pairs | Count |",
            "| ---: | ---: |",
        ]
    )
    for row in payload["all_strict_pair_distribution"]:
        lines.append(f"| {row['strict_pair_count']} | {row['count']} |")

    lines.extend(
        [
            "",
            "### Stable Labeled Survivors",
            "",
            "| Strict pairs | Count |",
            "| ---: | ---: |",
        ]
    )
    for row in payload["stable_labeled_strict_pair_distribution"]:
        lines.append(f"| {row['strict_pair_count']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Parent-Pass Deletion Stability",
            "",
            "| Deletion pass count | Parent-pass cases |",
            "| ---: | ---: |",
        ]
    )
    for row in payload["parent_deletion_pass_distribution"]:
        lines.append(f"| {row['deletion_pass_count']} | {row['count']} |")

    lines.extend(
        [
            "",
            "## Stable Oriented Class Profiles",
            "",
            "| Rank profile | Class count |",
            "| --- | ---: |",
        ]
    )
    for row in payload["stable_oriented_rank_profile_distribution"]:
        lines.append(f"| `{row['rank_profile']}` | {row['class_count']} |")

    lines.extend(
        [
            "",
            "| Width | Class count |",
            "| ---: | ---: |",
        ]
    )
    for row in payload["stable_oriented_width_distribution"]:
        lines.append(f"| {row['width']} | {row['count']} |")

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
