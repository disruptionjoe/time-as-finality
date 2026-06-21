"""Write T164 T54 survivor isomorphism/locality audit results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_survivor_isomorphism_locality import (
    run_t164_analysis,
    t164_result_to_dict,
)


RESULTS_JSON = Path("results/t54-survivor-isomorphism-locality-v0.1.json")
RESULTS_MD = Path("results/t54-survivor-isomorphism-locality-v0.1-results.md")


def main() -> None:
    payload = t164_result_to_dict(run_t164_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T164 Results: T54 Survivor Isomorphism And Locality Audit",
        "",
        "## Aggregate Checks",
        "",
        (
            "- Stable labeled T163 survivors: "
            f"{payload['stable_labeled_survivor_count']}"
        ),
        (
            "- Oriented finite-poset isomorphism classes: "
            f"{payload['oriented_isomorphism_class_count']}"
        ),
        (
            "- Order-dual quotient classes: "
            f"{payload['order_dual_quotient_class_count']}"
        ),
        (
            "- Largest oriented class size: "
            f"{payload['largest_oriented_class_size']}"
        ),
        (
            "- Singleton oriented classes: "
            f"{payload['singleton_oriented_class_count']}"
        ),
        (
            "- All classes height three: "
            f"{payload['all_classes_height_three']}"
        ),
        (
            "- All classes parent-interval thin: "
            f"{payload['all_classes_parent_intervals_thin']}"
        ),
        (
            "- All classes below cover-hub warning: "
            f"{payload['all_classes_low_cover_hub']}"
        ),
        "",
        "## Strict-Pair Distribution By Oriented Class",
        "",
        "| Strict pairs | Class count |",
        "| ---: | ---: |",
    ]
    for row in payload["strict_pair_count_by_oriented_class"]:
        lines.append(f"| {row['strict_pair_count']} | {row['class_count']} |")

    lines.extend(
        [
            "",
            "## Cover-Degree Profiles By Oriented Class",
            "",
            "| Cover-degree profile | Class count |",
            "| --- | ---: |",
        ]
    )
    for row in payload["cover_degree_profiles_by_oriented_class"]:
        lines.append(f"| `{row['cover_degree_profile']}` | {row['class_count']} |")

    lines.extend(
        [
            "",
            "## Class Table",
            "",
            (
                "| Class | Dual quotient | Members | Representative | Strict pairs | "
                "Covers | Height | Width | Rank profile | Cover degree | "
                "Max interval | Cover hub | Label |"
            ),
            "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | --- |",
        ]
    )
    for audit in payload["class_audits"]:
        lines.append(
            "| "
            f"`{audit['class_id']}` | "
            f"`{audit['dual_quotient_id']}` | "
            f"{audit['labeled_member_count']} | "
            f"`{audit['representative_permutation']}` | "
            f"{audit['strict_pair_count']} | "
            f"{audit['cover_relation_count']} | "
            f"{audit['height']} | "
            f"{audit['width']} | "
            f"`{audit['rank_profile']}` | "
            f"`{audit['cover_degree_profile']}` | "
            f"{audit['max_interval_interior_size']} | "
            f"{_fraction(audit['max_cover_hub_fraction'])} | "
            f"`{audit['locality_label']}` |"
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
