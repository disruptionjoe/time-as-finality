"""Write T169 detector deployment-archetype screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_deployment_archetype_screen import (
    run_t169_analysis,
    t169_result_to_dict,
)


RESULTS_JSON = Path("results/detector-deployment-archetype-screen-v0.1.json")
RESULTS_MD = Path("results/detector-deployment-archetype-screen-v0.1-results.md")


def main() -> None:
    payload = t169_result_to_dict(run_t169_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T169 Results: Detector Deployment-Archetype Screen",
        "",
        "## Archetype audits",
        "",
        "| Archetype | Workflow verdict | Control verdict | Row commitment | Classification | Required next |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['archetype_id']}` | "
            f"`{audit['workflow_verdict']}` | "
            f"`{audit['control_verdict']}` | "
            f"`{audit['row_commitment_kind']}` | "
            f"`{audit['classification']}` | "
            f"{audit['required_next']} |"
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
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
