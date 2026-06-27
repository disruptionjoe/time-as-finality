"""Runner for T250: T249 ordering-fraction screen."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t250_t249_ordering_fraction_screen import (
    run_t250_analysis,
    t250_result_to_dict,
)


RESULTS_JSON = Path("results/t250-t249-ordering-fraction-screen-v0.1.json")
RESULTS_MD = Path("results/t250-t249-ordering-fraction-screen-v0.1-results.md")


def main() -> None:
    payload = t250_result_to_dict(run_t250_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any] | None) -> str:
    if value is None:
        return "-"
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    audit = payload["t156_audit"]
    lines = [
        "# T250 Results: T249 Ordering-Fraction Screen",
        "",
        "## Aggregate Checks",
        "",
        f"- T249 T54 classification: `{payload['t249_t54_classification']}`",
        f"- T249 T54 theorem applies: `{payload['t249_t54_theorem_applies']}`",
        f"- T249 T126 classification: `{payload['t249_t126_classification']}`",
        f"- T249 T126 filter passed: `{payload['t249_t126_filter_passed']}`",
        f"- Ordering fraction: {_fraction(audit['ordering_fraction'])}",
        f"- Target fraction: {_fraction(audit['target_fraction'])}",
        f"- Tolerance: {_fraction(audit['tolerance'])}",
        f"- Absolute gap: {_fraction(audit['absolute_gap'])}",
        f"- Target verdict: `{audit['target_verdict']}`",
        f"- Verdict: `{payload['verdict']}`",
        "",
        "## Diagnostic Finding",
        "",
        audit["reason"],
    ]
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
