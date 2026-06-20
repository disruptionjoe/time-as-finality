"""Write T93 weak-measurement undo-cost independence results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_undo_cost_independence import (
    run_t93_analysis,
    t93_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-undo-cost-independence-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-undo-cost-independence-v0.1-results.md")


def main() -> None:
    payload = t93_result_to_dict(run_t93_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T93 Results: Weak-Measurement Undo-Cost Independence",
        "",
        "## Audits",
        "",
        "| Case | Standard timelines equal | Undo cost differs | TaF verdict changes | Classification | Blocker |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['case']}` | "
            f"{audit['standard_timelines_equal']} | "
            f"{audit['undo_cost_differs']} | "
            f"{audit['taf_verdict_changes']} | "
            f"`{audit['classification']}` | "
            f"{audit['blocker']} |"
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
            "## Blocker",
            "",
            payload["blocker"],
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
