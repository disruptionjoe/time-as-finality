"""Write T98 detector operator-handoff audit results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_operator_handoff_audit import (
    run_t98_analysis,
    t98_result_to_dict,
)


RESULTS_JSON = Path("results/detector-operator-handoff-audit-v0.1.json")
RESULTS_MD = Path("results/detector-operator-handoff-audit-v0.1-results.md")


def main() -> None:
    payload = t98_result_to_dict(run_t98_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T98 Results: Detector Operator-Handoff Audit",
        "",
        "## Staffing profiles",
        "",
        "| Profile | Verdict | Distinct operators | Independent trust auditor | Failure reasons | Next step |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        failures = ", ".join(audit["failure_reasons"]) or "none"
        lines.append(
            "| "
            f"{audit['profile_name']} | "
            f"{audit['verdict']} | "
            f"{audit['distinct_operator_count']} | "
            f"{audit['independent_trust_auditor']} | "
            f"{failures} | "
            f"{audit['next_allowed_step']} |"
        )

    lines.extend(
        [
            "",
            "## Authority domains",
            "",
            "| Domain | T97-owned tables |",
            "| --- | --- |",
        ]
    )
    for domain, tables in payload["table_owner_by_domain"].items():
        lines.append(f"| {domain} | {', '.join(tables)} |")

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
            "## Claim ledger update",
            "",
            payload["claim_ledger_update"],
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
