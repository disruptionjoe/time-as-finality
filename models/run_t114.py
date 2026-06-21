"""Write T114 viability-filter results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.viability_filter import run_t114_analysis, t114_result_to_dict


RESULTS_JSON = Path("results/viability-filter-v0.1.json")
RESULTS_MD = Path("results/viability-filter-v0.1-results.md")


def main() -> None:
    payload = t114_result_to_dict(run_t114_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T114 Results: Viability Filter",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## Aggregate checks",
        "",
        f"- Geometry not sufficient: `{payload['geometry_not_sufficient']}`",
        f"- Maintenance not sufficient: `{payload['maintenance_not_sufficient']}`",
        f"- Finality not platform: `{payload['finality_not_platform']}`",
        (
            "- Finality separates fixed standard state: "
            f"`{payload['finality_separates_fixed_standard_state']}`"
        ),
        f"- Observer-experienced cases: `{payload['observer_experienced_cases']}`",
        f"- Emergence-platform cases: `{payload['platform_positive_cases']}`",
        "",
        "## Candidate table",
        "",
        "| Candidate | First failed gate | Observer-experienced | Platform | Interpretation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for evaluation in payload["evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['name']}` | "
            f"`{evaluation['first_failed_gate']}` | "
            f"`{evaluation['observer_experienced']}` | "
            f"`{evaluation['emergence_platform']}` | "
            f"{evaluation['interpretation']} |"
        )

    lines.extend(
        [
            "",
            "## Gate traces",
            "",
        ]
    )
    for evaluation in payload["evaluations"]:
        lines.append(f"### {evaluation['name']}")
        lines.append("")
        for gate in evaluation["gates"]:
            lines.append(f"- `{gate['gate']}`: `{gate['passed']}` - {gate['reason']}")
        lines.append("")

    lines.extend(
        [
            "## What this improved",
            "",
            payload["improved"],
            "",
            "## What this weakened",
            "",
            payload["weakened"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
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
