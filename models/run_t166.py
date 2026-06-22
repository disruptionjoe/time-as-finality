"""Write T166 weak-measurement platform-packet gate results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_platform_packet_gate import (
    run_t166_analysis,
    t166_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-platform-packet-gate-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-platform-packet-gate-v0.1-results.md")


def main() -> None:
    payload = t166_result_to_dict(run_t166_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T166 Results: Weak-Measurement Platform-Packet Gate",
        "",
        "## Aggregate checks",
        "",
        f"- Null controls rejected: {payload['all_null_controls_rejected']}",
        f"- Current frontier admissible: {payload['current_frontier_admissible']}",
        "",
        "## Packet audits",
        "",
        "| Case | Classification | Admissible packet | Required next |",
        "| --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['admissible_packet']}` | "
            f"{audit['required_next']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1C update", "q1c_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
