"""Write T139 weak-measurement full-record sufficiency boundary results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_full_record_sufficiency_boundary import (
    run_t139_analysis,
    t139_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-full-record-sufficiency-boundary-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-full-record-sufficiency-boundary-v0.1-results.md")


def main() -> None:
    payload = t139_result_to_dict(run_t139_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T139 Results: Weak-Measurement Full-Record Sufficiency Boundary",
        "",
        "| Scenario | Classification | Screened by full record | Screened by coarse summary | Coarse-summary split | Full-record split | Witness summary | Witness full record |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        witness_summary = audit["witness_summary"] if audit["witness_summary"] is not None else "none"
        witness_full = audit["witness_full_record"] if audit["witness_full_record"] is not None else "none"
        lines.append(
            "| "
            f"`{audit['scenario_name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['screened_off_by_full_record']}` | "
            f"`{audit['screened_off_by_coarse_summary']}` | "
            f"`{audit['fixed_coarse_summary_split_exists']}` | "
            f"`{audit['fixed_full_record_split_exists']}` | "
            f"`{witness_summary}` | "
            f"`{witness_full}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1C update", "q1c_update"),
        ("Open blocker", "blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
