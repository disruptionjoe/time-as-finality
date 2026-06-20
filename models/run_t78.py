"""Write T78 pre-registered detector deployment protocol results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.preregistered_detector_deployment_protocol import (
    run_t78_analysis,
    t78_result_to_dict,
)


RESULTS_JSON = Path("results/preregistered-detector-deployment-protocol-v0.1.json")
RESULTS_MD = Path("results/preregistered-detector-deployment-protocol-v0.1-results.md")


def main() -> None:
    result = run_t78_analysis()
    payload = t78_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T78 Results: Pre-registered Detector Deployment Protocol",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Required evidence fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in payload["required_evidence_fields"])
    lines.extend(
        [
            "",
            "## Required controls",
            "",
        ]
    )
    lines.extend(f"- `{role}`" for role in payload["required_control_roles"])
    lines.extend(
        [
            "",
            "## Required raw log sources",
            "",
        ]
    )
    lines.extend(f"- `{source}`" for source in payload["required_raw_log_sources"])
    lines.extend(
        [
            "",
            "## Audit table",
            "",
            "| Plan | Verdict | Failure reasons | Next allowed audit |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        reasons = ", ".join(audit["failure_reasons"]) or "none"
        lines.append(
            "| "
            f"{audit['plan_name']} | "
            f"{audit['verdict']} | "
            f"{reasons} | "
            f"{audit['next_allowed_audit']} |"
        )
    lines.extend(
        [
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
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
