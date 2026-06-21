"""Write T138 detector manifest workflow-fit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_manifest_workflow_fit import (
    run_t138_analysis,
    t138_result_to_dict,
)


RESULTS_JSON = Path("results/detector-manifest-workflow-fit-v0.1.json")
RESULTS_MD = Path("results/detector-manifest-workflow-fit-v0.1-results.md")


def main() -> None:
    payload = t138_result_to_dict(run_t138_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T138 Results: Detector Manifest Workflow Fit",
        "",
        "## Human-fillable manifest template",
        "",
        "| Section | Item | Tier | Pre-event | Acceptable fill | Null if missing |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for line in payload["template"]:
        lines.append(
            "| "
            f"`{line['section']}` | "
            f"`{line['item']}` | "
            f"`{line['required_for_tier']}` | "
            f"`{line['fill_before_event']}` | "
            f"{line['acceptable_fill']} | "
            f"{line['null_if_missing']} |"
        )

    lines.extend(
        [
            "",
            "## Workflow audits",
            "",
            "| Workflow | Claimed tier | Max tier | Admissible | Verdict | Missing template items | Failures |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        missing = ", ".join(audit["missing_template_items"]) or "none"
        failures = ", ".join(audit["t136_failure_reasons"]) or "none"
        lines.append(
            "| "
            f"`{audit['workflow_name']}` | "
            f"`{audit['claimed_tier']}` | "
            f"`{audit['max_certifiable_tier']}` | "
            f"`{audit['claimed_tier_admissible']}` | "
            f"`{audit['verdict']}` | "
            f"`{missing}` | "
            f"`{failures}` |"
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
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
