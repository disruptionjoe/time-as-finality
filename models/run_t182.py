"""Write T182 weak-measurement platform-family screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_platform_family_screen import (
    run_t182_analysis,
    t182_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-platform-family-screen-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-platform-family-screen-v0.1-results.md")


def main() -> None:
    payload = t182_result_to_dict(run_t182_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T182 Results: Weak-Measurement Platform Family Screen",
        "",
        "## Aggregate checks",
        "",
        f"- Named platforms screened: {payload['named_platforms_screened']}",
        f"- Named platforms live: {payload['named_platforms_live']}",
        f"- Positive controls admitted: {payload['positive_controls_admitted']}",
        "",
        "## Platform audits",
        "",
        "| Family | Classification | Live for Q1C | Route type | Required next |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['family_id']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['q1c_live']}` | "
            f"`{audit['route_type']}` | "
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
