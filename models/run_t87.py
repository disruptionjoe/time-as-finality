"""Write T87 real-run raw-log contract results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.real_run_raw_log_contract import run_t87_analysis, t87_result_to_dict


RESULTS_JSON = Path("results/real-run-raw-log-contract-v0.1.json")
RESULTS_MD = Path("results/real-run-raw-log-contract-v0.1-results.md")


def main() -> None:
    payload = t87_result_to_dict(run_t87_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T87 Results: Real-Run Raw-Log Contract",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Required T86 controls",
        "",
    ]
    lines.extend(f"- `{role}`" for role in payload["required_t86_control_roles"])
    lines.extend(
        [
            "",
            "## Required event-level tables",
            "",
        ]
    )
    for table, columns in payload["required_raw_log_tables"].items():
        joined = ", ".join(f"`{column}`" for column in columns)
        lines.append(f"- `{table}`: {joined}")
    lines.extend(
        [
            "",
            "## T76 field mapping",
            "",
        ]
    )
    for table, fields in payload["table_to_t76_fields"].items():
        joined = ", ".join(f"`{field}`" for field in fields)
        lines.append(f"- `{table}` -> {joined}")
    lines.extend(
        [
            "",
            "## Audit table",
            "",
            "| Contract | Verdict | Failure reasons | Next allowed audit |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        reasons = ", ".join(audit["failure_reasons"]) or "none"
        lines.append(
            "| "
            f"{audit['contract_name']} | "
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
            "## Open blocker",
            "",
            payload["open_blocker"],
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
