"""Write T170 Q1D correlation-record guardrail results."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1d_correlation_record_guardrail import (
    run_t170_analysis,
    t170_result_to_dict,
)


RESULTS_JSON = Path("results/q1d-correlation-record-guardrail-v0.1.json")
RESULTS_MD = Path("results/q1d-correlation-record-guardrail-v0.1-results.md")


def main() -> None:
    payload = t170_result_to_dict(run_t170_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T170 Results: Q1D Correlation-Record Guardrail",
        "",
        "## Scenario audits",
        "",
        "| Scenario | No-signalling | Max CHSH | Stage | Classification | Rejected language |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['scenario_id']}` | "
            f"`{audit['no_signalling']}` | "
            f"`{audit['max_chsh_score']}` | "
            f"`{audit['correlation_record_stage']}` | "
            f"`{audit['classification']}` | "
            f"{audit['rejected_language']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1D update", "q1d_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
