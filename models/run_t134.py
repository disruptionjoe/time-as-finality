"""Write T134 detector dry-run tier gate results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_dry_run_tier_gate import (
    run_t134_analysis,
    t134_result_to_dict,
)


RESULTS_JSON = Path("results/detector-dry-run-tier-gate-v0.1.json")
RESULTS_MD = Path("results/detector-dry-run-tier-gate-v0.1-results.md")


def main() -> None:
    payload = t134_result_to_dict(run_t134_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T134 Results: Detector Dry-Run Tier Gate",
        "",
        "## T97 native field coverage",
        "",
        "| T121/T133 field | T97 coverage |",
        "| --- | --- |",
    ]
    for field, coverage in payload["field_coverage_by_t97"].items():
        lines.append(f"| `{field}` | `{coverage}` |")

    lines.extend(
        [
            "",
            "## Integrated tier audits",
            "",
            "| Case | Claimed tier | T97 real rows | Raw preserved | Provisional | Claim review | Blocking reasons |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        reasons = ", ".join(audit["blocking_reasons"]) or "none"
        lines.append(
            "| "
            f"`{audit['case_name']}` | "
            f"`{audit['claimed_tier_before_event']}` | "
            f"`{audit['real_t97_rows_present']}` | "
            f"`{audit['raw_evidence_preserved']}` | "
            f"`{audit['provisionally_admissible']}` | "
            f"`{audit['claim_review_ready']}` | "
            f"`{reasons}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1B update", "q1b_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
