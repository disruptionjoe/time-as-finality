"""Write T95 detector stack export-map results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_stack_export_map import run_t95_analysis, t95_result_to_dict


RESULTS_JSON = Path("results/detector-stack-export-map-v0.1.json")
RESULTS_MD = Path("results/detector-stack-export-map-v0.1-results.md")


def main() -> None:
    payload = t95_result_to_dict(run_t95_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T95 Results: Detector Stack Export Map",
        "",
        "## Required T87 tables",
        "",
    ]
    for table, columns in payload["required_t87_tables"].items():
        joined = ", ".join(f"`{column}`" for column in columns)
        lines.append(f"- `{table}`: {joined}")

    lines.extend(
        [
            "",
            "## Audit table",
            "",
            "| Map | Verdict | Native tables | Middleware tables | Failure reasons | Next allowed audit |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        native = ", ".join(audit["instrument_native_tables"]) or "none"
        middleware = ", ".join(audit["middleware_required_tables"]) or "none"
        failures = ", ".join(audit["failure_reasons"]) or "none"
        lines.append(
            "| "
            f"{audit['map_name']} | "
            f"{audit['verdict']} | "
            f"{native} | "
            f"{middleware} | "
            f"{failures} | "
            f"{audit['next_allowed_audit']} |"
        )

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
