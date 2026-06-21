"""Runner for T159: T54 interval-abundance and jackknife screen."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_interval_jackknife_screen import (
    run_t159_analysis,
    t159_result_to_dict,
)


RESULTS_JSON = Path("results/t54-interval-jackknife-screen-v0.1.json")
RESULTS_MD = Path("results/t54-interval-jackknife-screen-v0.1-results.md")


def main() -> None:
    payload = t159_result_to_dict(run_t159_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any] | None) -> str:
    if value is None:
        return "-"
    return f"{value['fraction']} ({value['float']:.3f})"


def _interval_counts(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "-"
    return ", ".join(f"{row['size']}:{row['count']}" for row in rows)


def _render_markdown(payload: dict[str, Any]) -> str:
    target = payload["target"]
    ordering = target["ordering_target"]
    lines = [
        "# T159 Results: T54 Interval-Jackknife Screen",
        "",
        "## Target",
        "",
        f"- Name: `{target['name']}`",
        f"- Ordering target: `{ordering['name']}`",
        f"- Ordering fraction: {_fraction(ordering['target_fraction'])}",
        f"- Tolerance: +/- {_fraction(ordering['tolerance'])}",
        f"- Max parent interval size: `{target['max_parent_interval_size']}`",
        (
            "- Required single-deletion pass rate: "
            f"{_fraction(target['required_deletion_pass_rate'])}"
        ),
        f"- Basis: {target['basis']}",
        "",
        "## Aggregate Checks",
        "",
        (
            "- Flat parent interval support passes: "
            f"{payload['flat_parent_interval_support_passes']}"
        ),
        (
            "- Flat jackknife stability fails: "
            f"{payload['flat_jackknife_stability_fails']}"
        ),
        (
            "- Product-grid parent interval support fails: "
            f"{payload['product_grid_parent_interval_support_fails']}"
        ),
        (
            "- Chain control blocked before interval screen: "
            f"{payload['chain_control_blocked_before_interval_screen']}"
        ),
        (
            "- T157 survivor demoted to calibration-only: "
            f"{payload['t157_survivor_demoted_to_calibration_only']}"
        ),
        "",
        "## Audit Table",
        "",
        (
            "| Candidate | T126 | T156 | Events | Ordering fraction | "
            "Intervals | Deletion pass rate | Verdict |"
        ),
        "| --- | --- | --- | ---: | ---: | --- | ---: | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['t126_classification']}` | "
            f"`{audit['t156_verdict']}` | "
            f"{audit['event_count']} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"{_interval_counts(audit['interval_counts_by_size'])} | "
            f"{_fraction(audit['deletion_pass_rate'])} | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['name']}",
                "",
                f"- Parent interval support: `{audit['parent_interval_support_passed']}`",
                f"- Deletion stability: `{audit['deletion_stability_passed']}`",
                f"- Reason: {audit['reason']}",
                f"- Required next: {audit['required_next']}",
                "",
                "| Removed event | Ordering fraction | Band | Intervals | Support |",
                "| --- | ---: | --- | --- | --- |",
            ]
        )
        for deletion in audit["deletion_audits"]:
            lines.append(
                "| "
                f"`{deletion['removed_event']}` | "
                f"{_fraction(deletion['ordering_fraction'])} | "
                f"`{deletion['ordering_band_passed']}` | "
                f"{_interval_counts(deletion['interval_counts_by_size'])} | "
                f"`{deletion['interval_support_passed']}` |"
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
