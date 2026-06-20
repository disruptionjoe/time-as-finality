"""Write T96 detector feasibility-checklist results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_feasibility_checklist import (
    run_t96_analysis,
    t96_result_to_dict,
)


RESULTS_JSON = Path("results/detector-feasibility-checklist-v0.1.json")
RESULTS_MD = Path("results/detector-feasibility-checklist-v0.1-results.md")


def main() -> None:
    payload = t96_result_to_dict(run_t96_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    audit = payload["audit"]
    lines = [
        "# T96 Results: Detector Feasibility Checklist",
        "",
        "## Route status",
        "",
        f"Checklist: `{audit['checklist_name']}`",
        "",
        f"Route status: `{audit['route_status']}`",
        "",
        f"Next allowed step: `{audit['next_allowed_step']}`",
        "",
        "## Requirement split",
        "",
        f"- Native tables: {', '.join(audit['native_tables']) or 'none'}",
        f"- Middleware tables: {', '.join(audit['middleware_tables']) or 'none'}",
        (
            f"- Custom control tables: "
            f"{', '.join(audit['custom_control_tables']) or 'none'}"
        ),
        f"- Governance tables: {', '.join(audit['governance_tables']) or 'none'}",
        f"- Blocker tables: {', '.join(audit['blocker_tables']) or 'none'}",
        "",
        "## Required T87 tables",
        "",
    ]
    for table_name, columns in payload["required_t87_tables"].items():
        joined = ", ".join(f"`{column}`" for column in columns)
        lines.append(f"- `{table_name}`: {joined}")

    lines.extend(
        [
            "",
            "## Strongest claim",
            "",
            payload["strongest_claim"],
            "",
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
            "## Q1 update",
            "",
            payload["q1_update"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
