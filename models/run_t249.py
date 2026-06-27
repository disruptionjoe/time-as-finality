"""Runner for T249: larger T54/T126 canonical colimit witness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t249_larger_t54_t126_colimit import (
    run_t249_analysis,
    t249_result_to_dict,
)


RESULTS_JSON = Path("results/t249-larger-t54-t126-colimit-v0.1.json")
RESULTS_MD = Path("results/t249-larger-t54-t126-colimit-v0.1-results.md")


def main() -> None:
    payload = t249_result_to_dict(run_t249_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    completion = payload["completion"]
    audit = payload["t126_audit"]
    diagnostics = audit["diagnostics"]
    lines = [
        "# T249 Results: Larger T54/T126 Canonical Colimit",
        "",
        "## Aggregate Checks",
        "",
        f"- T54 classification: `{completion['classification']}`",
        f"- T54 theorem applies: `{completion['theorem_applies']}`",
        f"- Global events: {completion['global_event_count']}",
        f"- Strict pairs: {completion['strict_pair_count']}",
        f"- Product order exact: `{completion['product_order_exact']}`",
        f"- T126 classification: `{audit['classification']}`",
        f"- Causal-set candidate: `{audit['causal_set_candidate']}`",
        f"- Manifold filter passed: `{audit['manifold_filter_passed']}`",
        "",
        "## Observer Patch Gap Check",
        "",
        "| Observer | Local events | Ambient pairs | Local pairs | Gaps | Local suborder |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for summary in payload["local_gap_summaries"]:
        lines.append(
            "| "
            f"`{summary['observer']}` | "
            f"{summary['local_event_count']} | "
            f"{summary['ambient_pair_count']} | "
            f"{summary['local_pair_count']} | "
            f"{summary['gap_count']} | "
            f"`{summary['local_is_suborder']}` |"
        )

    lines.extend(
        [
            "",
            "## T126 Diagnostics",
            "",
            f"- Reason: {audit['reason']}",
            f"- Required next: {audit['required_next']}",
            f"- Not claimed: {audit['not_claimed']}",
        ]
    )
    if diagnostics is not None:
        lines.extend(
            [
                f"- Comparable fraction: {_fraction(diagnostics['comparable_fraction'])}",
                f"- Cover relation count: {diagnostics['cover_relation_count']}",
                f"- Link density: {_fraction(diagnostics['link_density'])}",
                f"- Height: {diagnostics['height']}",
                f"- Width: {diagnostics['width']}",
                f"- Rank profile: `{diagnostics['rank_profile']}`",
                (
                    "- Largest cover hub fraction: "
                    f"{_fraction(diagnostics['largest_cover_hub_fraction'])}"
                ),
                (
                    "- Profile spread obstruction: "
                    f"`{diagnostics['profile_spread_obstruction']}`"
                ),
            ]
        )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
