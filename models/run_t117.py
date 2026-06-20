"""Write T117 Accessible State Space separation-audit results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.accessible_state_space_separation import (
    run_t117_analysis,
    t117_result_to_dict,
)


RESULTS_JSON = Path("results/accessible-state-space-separation-v0.1.json")
RESULTS_MD = Path("results/accessible-state-space-separation-v0.1-results.md")


def main() -> None:
    payload = t117_result_to_dict(run_t117_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T117 Results: Accessible State Space Separation Audit",
        "",
        "## Current strongest claim",
        "",
        payload["current_strongest_claim"],
        "",
        "## Strongest separation case",
        "",
        payload["strongest_separation_case"],
        "",
        "## Strongest absorption case",
        "",
        payload["strongest_absorption_case"],
        "",
        "## Domain verdicts",
        "",
        "| Domain | Entropy | Information | Finality | Viability | Persistence | ASP split | Verdict |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['domain']}` | "
            f"`{audit['entropy_comparison']}` | "
            f"`{audit['information_comparison']}` | "
            f"`{audit['finality_comparison']}` | "
            f"`{audit['viability_comparison']}` | "
            f"`{audit['persistence_comparison']}` | "
            f"`{audit['asp_comparison']}` | "
            f"{audit['separation_verdict']} |"
        )
    lines.extend(
        [
            "",
            "## ASP task sets",
            "",
            "| Domain | High-ASP tasks | Low-ASP tasks | Lost-structure chain |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['domain']}` | "
            f"`{audit['asp_a']}` | "
            f"`{audit['asp_b']}` | "
            f"`{audit['lost_structure_chain_present']}` |"
        )
    lines.extend(
        [
            "",
            "## Prior-art pressure",
            "",
            "| Domain | Target | Capture | Explanation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        for item in audit["prior_art"]:
            lines.append(
                "| "
                f"`{audit['domain']}` | "
                f"{item['target']} | "
                f"`{item['capture']}` | "
                f"{item['explanation']} |"
            )
    lines.extend(
        [
            "",
            "## Falsification result",
            "",
            payload["falsification_result"],
            "",
            "## Missing object",
            "",
            payload["missing_object"],
            "",
            "## Recommended disposition",
            "",
            payload["recommended_disposition"],
            "",
            "## Claim ledger update",
            "",
            payload["claim_ledger_update"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
