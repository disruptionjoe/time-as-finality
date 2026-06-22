"""Write T180 branch-support threshold minimality results."""

from __future__ import annotations

import json
from pathlib import Path

from models.branch_support_threshold_minimality import (
    run_t180_analysis,
    t180_result_to_dict,
)


RESULTS_JSON = Path("results/branch-support-threshold-minimality-v0.1.json")
RESULTS_MD = Path("results/branch-support-threshold-minimality-v0.1-results.md")


def main() -> None:
    payload = t180_result_to_dict(run_t180_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T180 Results: Branch-Support Threshold Minimality",
        "",
        "## Audit Table",
        "",
        "| Projection | Factors through task | Distinct values | Witness pair | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        witness = (
            "`" + " / ".join(audit["witness_pair"]) + "`"
            if audit["witness_pair"]
            else "None"
        )
        lines.append(
            "| "
            f"`{audit['projection_name']}` | "
            f"`{audit['factors_through_capability']}` | "
            f"`{audit['value_count']}` | "
            f"{witness} | "
            f"`{audit['verdict']}` |"
        )

    lines.extend(
        [
            "",
            "## Strongest Claim",
            "",
            str(payload["strongest_claim"]),
            "",
            "## What Improved",
            "",
            str(payload["improved"]),
            "",
            "## What Weakened",
            "",
            str(payload["weakened"]),
            "",
            "## Falsification Condition",
            "",
            str(payload["falsification_condition"]),
            "",
            "## Claim Ledger Update",
            "",
            str(payload["claim_ledger_update"]),
            "",
            "## Open Blocker",
            "",
            str(payload["open_blocker"]),
            "",
            "## Suggested Next",
            "",
            str(payload["suggested_next"]),
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
