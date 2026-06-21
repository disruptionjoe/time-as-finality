"""Write T155 weak-measurement Blackwell boundary results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_blackwell_boundary import (
    run_t155_analysis,
    t155_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-blackwell-boundary-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-blackwell-boundary-v0.1-results.md")


def main() -> None:
    payload = t155_result_to_dict(run_t155_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _risk_cell(audit: dict[str, object], loss_name: str, key: str) -> str:
    value = audit[key][loss_name]
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T155 Results: Weak-Measurement Blackwell Boundary",
        "",
        "## Aggregate checks",
        "",
        f"- Null controls hold: {payload['null_controls_hold']}",
        f"- Positive control improves: {payload['positive_control_improves']}",
        "",
        "## Audits",
        "",
        (
            "| Case | Classification | Screened off by record | "
            "0-1 risk with R | 0-1 risk with (R,A) | "
            "Asymmetric risk with R | Asymmetric risk with (R,A) | Required next |"
        ),
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['screened_off_by_record']}` | "
            f"{_risk_cell(audit, 'zero_one', 'record_only_risks')} | "
            f"{_risk_cell(audit, 'zero_one', 'record_auxiliary_risks')} | "
            f"{_risk_cell(audit, 'asymmetric_h1_cost', 'record_only_risks')} | "
            f"{_risk_cell(audit, 'asymmetric_h1_cost', 'record_auxiliary_risks')} | "
            f"{audit['required_next']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1C update", "q1c_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
