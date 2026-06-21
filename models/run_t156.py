"""Runner for T156: Myrheim-Meyer ordering-fraction screen."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.myrheim_meyer_ordering_fraction_screen import (
    run_t156_analysis,
    t156_result_to_dict,
)


RESULTS_JSON = Path("results/myrheim-meyer-ordering-fraction-screen-v0.1.json")
RESULTS_MD = Path("results/myrheim-meyer-ordering-fraction-screen-v0.1-results.md")


def main() -> None:
    payload = t156_result_to_dict(run_t156_analysis())
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
        "# T156 Results: Myrheim-Meyer Ordering-Fraction Screen",
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
            "- Positive target control passes: "
            f"{payload['positive_target_control_passes']}"
        ),
        (
            "- T126 pass can fail ordering-fraction target: "
            f"{payload['t126_pass_can_fail_ordering_fraction_target']}"
        ),
        (
            "- Product-grid T126 survivors fail target: "
            f"{payload['all_product_grid_survivors_fail_target']}"
        ),
        "",
        "## Audit Table",
        "",
        (
            "| Candidate | T126 | T126 filter | Events | Strict pairs | "
            "Ordering fraction | Gap | Verdict |"
        ),
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
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
                f"- Target verdict: `{audit['target_verdict']}`",
                f"- Source: {audit['source']}",
                f"- Reason: {audit['reason']}",
                f"- Required next: {audit['required_next']}",
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
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
