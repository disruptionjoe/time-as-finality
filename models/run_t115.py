"""Write T115 maintenance-cost viability split results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.maintenance_viability_split import run_t115_analysis, t115_result_to_dict


RESULTS_JSON = Path("results/maintenance-viability-split-v0.1.json")
RESULTS_MD = Path("results/maintenance-viability-split-v0.1-results.md")


def main() -> None:
    payload = t115_result_to_dict(run_t115_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T115 Results: Maintenance-Cost Viability Split",
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
        "## Pair audits",
        "",
        "| Domain | Standard equivalent | Future split | Differing axes | Strongest absorption |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["pair_audits"]:
        lines.append(
            "| "
            f"`{audit['domain']}` | "
            f"`{audit['standard_equivalent']}` | "
            f"`{audit['future_operation_split']}` | "
            f"`{audit['differing_axis']}` | "
            f"{audit['strongest_absorption']} |"
        )

    lines.extend(
        [
            "",
            "## Existing-theory comparison",
            "",
            "| Domain | Framework | Capture verdict | Reason |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["pair_audits"]:
        for comparison in audit["comparisons"]:
            lines.append(
                "| "
                f"`{audit['domain']}` | "
                f"{comparison['framework']} | "
                f"`{comparison['capture']}` | "
                f"{comparison['reason']} |"
            )

    lines.extend(
        [
            "",
            "## Closest existing theory",
            "",
            payload["closest_existing_theory"],
            "",
            "## Missing mathematical object",
            "",
            payload["missing_mathematical_object"],
            "",
            "## Recommendation",
            "",
            payload["recommendation"],
            "",
            "## What this weakened or falsified",
            "",
            payload["weakened_or_falsified"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
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
