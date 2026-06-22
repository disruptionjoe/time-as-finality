"""Write T183 Q1C reinstatement stack results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_reinstatement_stack import (
    run_t183_analysis,
    t183_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-reinstatement-stack-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-reinstatement-stack-v0.1-results.md")


def main() -> None:
    payload = t183_result_to_dict(run_t183_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T183 Results: Weak-Measurement Reinstatement Stack",
        "",
        "## Aggregate checks",
        "",
        f"- Positive controls admitted: {payload['positive_controls_admitted']}",
        f"- Null controls rejected: {payload['null_controls_rejected']}",
        f"- Current frontier reopened: {payload['current_frontier_reopened']}",
        "",
        "## Stack audits",
        "",
        (
            "| Proposal | Classification | Reinstatement candidate | "
            "Packet | Verdict | Preserved target |"
        ),
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['reinstatement_candidate']}` | "
            f"`{audit['packet_classification']}` | "
            f"`{audit['verdict_classification']}` | "
            f"`{audit['preserved_target_classification']}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1C update", "q1c_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Suggested next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
