"""Write T91 weak-measurement platform audit results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_platform_audit import (
    run_t91_analysis,
    t91_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-platform-audit-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-platform-audit-v0.1-results.md")


def main() -> None:
    payload = t91_result_to_dict(run_t91_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T91 Results: Weak-Measurement Platform Audit",
        "",
        "## Platform audits",
        "",
        "| Platform | Candidate axis | Classification | Blocker |",
        "| --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"{audit['platform']} | "
            f"{audit['candidate_axis']} | "
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
