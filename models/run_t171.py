"""Write T171 detector row-review substitution screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_row_review_substitution_screen import (
    run_t171_analysis,
    t171_result_to_dict,
)


RESULTS_JSON = Path("results/detector-row-review-substitution-screen-v0.1.json")
RESULTS_MD = Path("results/detector-row-review-substitution-screen-v0.1-results.md")


def main() -> None:
    payload = t171_result_to_dict(run_t171_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T171 Results: Detector Row-Review Substitution Screen",
        "",
        "## Substitute audits",
        "",
        "| Substitute | Classification | Missing claim-review operations | Required next |",
        "| --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        missing = ", ".join(
            f"`{item}`" for item in audit["operations_missing_vs_claim_review"]
        )
        lines.append(
            "| "
            f"`{audit['substitute_id']}` | "
            f"`{audit['classification']}` | "
            f"{missing or '`none`'} | "
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
