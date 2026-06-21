"""Write T163 six-event T54 rank-pair family census results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_rank_pair_family_census import run_t163_analysis, t163_result_to_dict


RESULTS_JSON = Path("results/t54-rank-pair-family-census-v0.1.json")
RESULTS_MD = Path("results/t54-rank-pair-family-census-v0.1-results.md")


def main() -> None:
    payload = t163_result_to_dict(run_t163_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T163 Results: T54 Rank-Pair Family Census",
        "",
        "## Aggregate Checks",
        "",
        f"- Total labeled six-event rank-pair cases: {payload['total_cases']}",
        f"- T156 failures after T126 pass: {payload['t156_fail_count']}",
        f"- Parent-interval failures after T156 pass: {payload['parent_interval_fail_count']}",
        f"- Jackknife-fragile cases after parent-interval pass: {payload['fragile_jackknife_count']}",
        f"- Stable survivors after all current screens: {payload['stable_survivor_count']}",
        (
            "- Stable-survivor fraction of full family: "
            f"{_fraction(payload['stable_survivor_fraction'])}"
        ),
        (
            "- T157 baseline permutation: "
            f"`{payload['t157_baseline_permutation']}`"
        ),
        f"- T157 baseline bucket: `{payload['t157_baseline_bucket']}`",
        f"- T157 baseline stable: `{payload['t157_baseline_stable']}`",
        "",
        "## T126 Classification Counts",
        "",
        "| Classification | Count |",
        "| --- | ---: |",
    ]
    for row in payload["t126_classification_counts"]:
        lines.append(f"| `{row['classification']}` | {row['count']} |")

    lines.extend(
        [
            "",
            "## Representative Cases",
            "",
            (
                "- Stable survivor permutations: "
                f"`{payload['representative_stable_permutations']}`"
            ),
            (
                "- Fragile survivor permutations: "
                f"`{payload['representative_fragile_permutations']}`"
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
