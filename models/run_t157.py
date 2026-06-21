"""Runner for T157: T54 ordering-fraction bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_ordering_fraction_bridge import (
    run_t157_analysis,
    t157_result_to_dict,
)


RESULTS_JSON = Path("results/t54-ordering-fraction-bridge-v0.1.json")
RESULTS_MD = Path("results/t54-ordering-fraction-bridge-v0.1-results.md")


def main() -> None:
    payload = t157_result_to_dict(run_t157_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any] | None) -> str:
    if value is None:
        return "-"
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    target = payload["target"]
    lines = [
        "# T157 Results: T54 Ordering-Fraction Bridge",
        "",
        "## Target",
        "",
        f"- Name: `{target['name']}`",
        f"- Ordering fraction: {_fraction(target['target_fraction'])}",
        f"- Tolerance: +/- {_fraction(target['tolerance'])}",
        f"- Basis: {target['basis']}",
        "",
        "## Aggregate Checks",
        "",
        (
            "- T54 flat candidate reaches T126 scale: "
            f"{payload['t54_flat_candidate_reaches_t126_scale']}"
        ),
        (
            "- T54 flat candidate matches target band: "
            f"{payload['t54_flat_candidate_matches_target_band']}"
        ),
        (
            "- T54 product-grid control fails target band: "
            f"{payload['t54_product_grid_control_fails_target_band']}"
        ),
        (
            "- T54 chain control blocked before target: "
            f"{payload['t54_chain_control_blocked_before_target']}"
        ),
        (
            "- Previous T156 open blocker removed: "
            f"{payload['previous_t156_open_blocker_removed']}"
        ),
        "",
        "## Audit Table",
        "",
        (
            "| Candidate | T54 | T126 | T126 filter | Events | Strict pairs | "
            "Ordering fraction | Gap | Verdict |"
        ),
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for audit in payload["audits"]:
        strict_pairs = (
            "-"
            if audit["strict_pair_count"] is None
            else str(audit["strict_pair_count"])
        )
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['t54_classification']}` | "
            f"`{audit['t126_classification']}` | "
            f"`{audit['t126_filter_passed']}` | "
            f"{audit['event_count']} | "
            f"{strict_pairs} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"{_fraction(audit['absolute_gap'])} | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['name']}",
                "",
                f"- T54 theorem applies: `{audit['t54_theorem_applies']}`",
                f"- Target verdict: `{audit['target_verdict']}`",
                f"- Reason: {audit['reason']}",
                f"- Required next: {audit['required_next']}",
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
