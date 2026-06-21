"""Write T148 H7 paper-facing demotion gate results."""

from __future__ import annotations

import json
from pathlib import Path

from models.h7_paper_facing_demotion_gate import (
    run_t148_analysis,
    t148_result_to_dict,
)


RESULTS_JSON = Path("results/h7-paper-facing-demotion-gate-v0.1.json")
RESULTS_MD = Path("results/h7-paper-facing-demotion-gate-v0.1-results.md")


def main() -> None:
    payload = t148_result_to_dict(run_t148_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T148 Results: H7 Paper-Facing Demotion Gate",
        "",
        "## Status",
        "",
        f"`{payload['paper_facing_status']}`",
        "",
        "## Gate Profile",
        "",
        "| Gate | Value |",
        "| --- | --- |",
    ]
    profile = payload["profile"]
    for key, value in profile.items():
        lines.append(f"| `{key}` | `{value}` |")

    for heading, key in (
        ("Allowed Claims", "allowed_claims"),
        ("Rejected Claims", "rejected_claims"),
        ("Open Blockers", "open_blockers"),
    ):
        lines.extend(["", f"## {heading}", ""])
        for item in payload[key]:
            lines.append(f"- {item}")

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
