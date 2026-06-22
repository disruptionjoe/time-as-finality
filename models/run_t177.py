"""Write T177 Q1 absorber-owned field intake results."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1_absorber_owned_field_intake import (
    run_t177_analysis,
    t177_result_to_dict,
)


RESULTS_JSON = Path("results/q1-absorber-owned-field-intake-v0.1.json")
RESULTS_MD = Path("results/q1-absorber-owned-field-intake-v0.1-results.md")


def main() -> None:
    payload = t177_result_to_dict(run_t177_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T177 Results: Q1 Absorber-Owned Field Intake",
        "",
        "## Aggregate checks",
        "",
        f"- Null controls rejected: {payload['null_controls_rejected']}",
        (
            "- Hypothetical reopen controls admitted: "
            f"{payload['hypothetical_reopen_controls_admitted']}"
        ),
        f"- Q1 remains roadmap umbrella: {payload['q1_remains_roadmap_umbrella']}",
        "",
        "## Proposal audits",
        "",
        "| Proposal | Branch | Classification | Reopens branch | Required next |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['proposal_id']}` | "
            f"`{audit['branch']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['should_reopen_branch']}` | "
            f"{audit['required_next']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1 update", "q1_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
