"""Write T124 constructor-admissibility grounding results."""

from __future__ import annotations

import json
from pathlib import Path

from models.constructor_admissibility_grounding_audit import (
    run_t124_analysis,
    t124_result_to_dict,
)


RESULTS_JSON = Path("results/constructor-admissibility-grounding-audit-v0.1.json")
RESULTS_MD = Path("results/constructor-admissibility-grounding-audit-v0.1-results.md")


def main() -> None:
    payload = t124_result_to_dict(run_t124_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T124 Results: Constructor-Admissibility Grounding Audit",
        "",
        "## Summary",
        "",
        payload["strongest_claim"],
        "",
        "## Transformation Ledger",
        "",
        "| Case | Source | Reverse status | Named resource/condition | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['case_id']}` | "
            f"{audit['source']} | "
            f"`{audit['reverse_status']}` | "
            f"{audit['named_resource_or_condition']} | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['case_id']}",
                "",
                f"- Source: {audit['source']}",
                f"- Forward edge: {audit['forward_edge']}",
                f"- D1 delta: {audit['d1_delta']}",
                f"- Accounting boundary: {audit['accounting_boundary']}",
                f"- Forward status: `{audit['forward_status']}`",
                f"- Reverse edge: {audit['reverse_edge']}",
                f"- Reverse status: `{audit['reverse_status']}`",
                f"- Reverse blocker: {audit['reverse_blocker']}",
                f"- Named resource or condition: {audit['named_resource_or_condition']}",
                f"- Permits unqualified physical arrow: `{audit['permits_unqualified_physical_arrow']}`",
                f"- Permits constructor reading: `{audit['permits_constructor_reading']}`",
                f"- Permits resource-accounting reading: `{audit['permits_resource_accounting_reading']}`",
                f"- Verdict: `{audit['verdict']}`",
                f"- Reason: {audit['reason']}",
            ]
        )

    for heading, key in (
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
