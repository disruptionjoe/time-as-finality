"""Runner for T251: T249 deletion stability screen."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t251_t249_deletion_stability import (
    run_t251_analysis,
    t251_result_to_dict,
)


RESULTS_JSON = Path("results/t251-t249-deletion-stability-v0.1.json")
RESULTS_MD = Path("results/t251-t249-deletion-stability-v0.1-results.md")


def main() -> None:
    payload = t251_result_to_dict(run_t251_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T251 Results: T249 Deletion Stability Screen",
        "",
        "## Aggregate Checks",
        "",
        f"- Parent ordering fraction: {_fraction(payload['parent_ordering_fraction'])}",
        f"- Parent band passed: `{payload['parent_band_passed']}`",
        f"- Deletion cases: {payload['deletion_case_count']}",
        f"- Deletions passing T126: {payload['deletion_t126_pass_count']}",
        f"- Deletions passing ordering band: {payload['deletion_band_pass_count']}",
        f"- Deletion band pass rate: {_fraction(payload['deletion_band_pass_rate'])}",
        f"- Verdict: `{payload['verdict']}`",
        "",
        "## Deletion Table",
        "",
        "| Removed | T126 | Strict pairs | Ordering fraction | Band passed | Height | Width | Verdict |",
        "| --- | --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for audit in payload["deletion_audits"]:
        lines.append(
            "| "
            f"`{audit['removed_event']}` | "
            f"`{audit['t126_classification']}` | "
            f"{audit['strict_pair_count']} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"`{audit['ordering_band_passed']}` | "
            f"{audit['height']} | "
            f"{audit['width']} | "
            f"`{audit['verdict']}` |"
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
