"""Write T140 Q1 frontier escape-matrix results."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1_frontier_escape_matrix import run_t140_analysis, t140_result_to_dict


RESULTS_JSON = Path("results/q1-frontier-escape-matrix-v0.1.json")
RESULTS_MD = Path("results/q1-frontier-escape-matrix-v0.1-results.md")


def main() -> None:
    payload = t140_result_to_dict(run_t140_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T140 Results: Q1 Frontier Escape Matrix",
        "",
        "| Branch | Classification | Active internal route | Live evidence | Required next |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['branch']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['active_internal_route']}` | "
            f"`{audit['live_evidence']}` | "
            f"{audit['required_next']} |"
        )

    for heading, key in (
        ("Overall recommendation", "overall_recommendation"),
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
