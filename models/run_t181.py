"""Write T181 branch-failure threshold theorem results."""

from __future__ import annotations

import json
from pathlib import Path

from models.branch_failure_threshold_theorem import (
    run_t181_analysis,
    t181_result_to_dict,
)


RESULTS_JSON = Path("results/branch-failure-threshold-theorem-v0.1.json")
RESULTS_MD = Path("results/branch-failure-threshold-theorem-v0.1-results.md")


def main() -> None:
    payload = t181_result_to_dict(run_t181_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T181 Results: Branch-Failure Threshold Theorem",
        "",
        "## Theorem Candidate",
        "",
        str(payload["theorem_candidate"]),
        "",
        "## Threshold Audits",
        "",
        "| Task | Projection | Factors | Projection values | Capability values | Witness |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["threshold_audits"]:
        lines.append(_audit_row(audit))

    lines.extend(
        [
            "",
            "## Boundary Audits",
            "",
            "| Task | Projection | Factors | Projection values | Capability values | Witness |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["boundary_audits"]:
        lines.append(_audit_row(audit))

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def _audit_row(audit: dict[str, object]) -> str:
    witness_pair = audit["witness_pair"]
    witness = "`" + " / ".join(witness_pair) + "`" if witness_pair else "None"
    return (
        "| "
        f"`{audit['task_name']}` | "
        f"`{audit['projection_name']}` | "
        f"`{audit['factors_through_capability']}` | "
        f"`{audit['projection_value_count']}` | "
        f"`{audit['capability_value_count']}` | "
        f"{witness} |"
    )


if __name__ == "__main__":
    main()
