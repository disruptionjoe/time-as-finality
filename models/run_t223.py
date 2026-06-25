"""Write T223 decisive ordinal-scaling verdict results.

This runs the full decisive analysis (n=5,6,7,8). The n=8 exact enumeration of
40320 rank permutations through the full T126/T156/T159 pipeline takes a few
minutes; this runner is the slow, authoritative path. The unit test uses the
cheaper sizes plus the cached verdict object.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_ordinal_scaling_decisive import (
    run_t223_analysis,
    t223_result_to_dict,
)


RESULTS_JSON = Path("results/t54-ordinal-scaling-decisive-v0.1.json")
RESULTS_MD = Path("results/t54-ordinal-scaling-decisive-v0.1-results.md")


def main() -> None:
    payload = t223_result_to_dict(run_t223_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.4f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T223 Results: T54 Ordinal Scaling Decisive Verdict",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Basis: {payload['verdict_basis']}",
        "",
        "## Exact Comparison Target",
        "",
        f"- Target: `{payload['comparison_target']}`",
        f"- Basis: {payload['target_basis']}",
        f"- Reproduces prior T165/T167 counts: {payload['reproduced_prior_counts']}",
        "",
        "## Size Summary",
        "",
        (
            "| n | Cases | T126 pass | T156 pass | Parent pass | Stable "
            "survivors | Stable fraction | Oriented classes | Dual classes | "
            "Largest class prob | Max survivor height | All thin |"
        ),
        (
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | "
            "---: | ---: | :---: |"
        ),
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
            f"{_fraction(audit['largest_oriented_class_probability'])} | "
            f"{audit['max_survivor_height']} | "
            f"{audit['all_survivors_thin_intervals']} |"
        )

    lines.extend(["", "## Stable-Survivor Trajectory", ""])
    lines.append("| n | Stable fraction | Conditional-after-parent | Largest class prob |")
    lines.append("| ---: | ---: | ---: | ---: |")
    by_size = {a["event_count"]: a for a in payload["size_audits"]}
    for entry in payload["stable_fraction_trajectory"]:
        n = entry["event_count"]
        cond = next(
            c["value"]
            for c in payload["conditional_survival_trajectory"]
            if c["event_count"] == n
        )
        lines.append(
            f"| {n} | {_fraction(entry['value'])} | {_fraction(cond)} | "
            f"{_fraction(by_size[n]['largest_oriented_class_probability'])} |"
        )

    lines.extend(
        [
            "",
            "## Monotone-Decay And Structure Tests",
            "",
            "| Test | Result |",
            "| --- | :---: |",
            (
                "| Stable fraction monotone non-increasing from n=6 | "
                f"{payload['stable_fraction_is_monotone_nonincreasing_from_n6']} |"
            ),
            (
                "| Conditional survival monotone non-increasing from n=6 | "
                f"{payload['conditional_survival_is_monotone_nonincreasing_from_n6']} |"
            ),
            (
                "| Survivor family stays thin + height-bounded | "
                f"{payload['survivor_family_stays_thin_height_bounded']} |"
            ),
            (
                "| Typical ensemble member rejected as stable band survivor | "
                f"{payload['typical_member_rejected']} |"
            ),
        ]
    )

    lines.extend(["", "## Survivor Height Distributions", ""])
    for audit in payload["size_audits"]:
        lines.extend(
            [
                f"### n = {audit['event_count']}",
                "",
                "| Survivor height | Count |",
                "| ---: | ---: |",
            ]
        )
        if audit["survivor_height_distribution"]:
            for row in audit["survivor_height_distribution"]:
                lines.append(f"| {row['height']} | {row['count']} |")
        else:
            lines.append("| n/a | 0 |")
        lines.append("")

    for heading, key in (
        ("Earned", "earned"),
        ("Not Earned (Either Direction)", "not_earned"),
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened Or Falsified", "weakened_or_falsified"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Most Important Follow-On Question", "most_important_followon"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
