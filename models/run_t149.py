"""Write T149 weak-measurement conditional-sufficiency gate results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_conditional_sufficiency_gate import (
    run_t149_analysis,
    t149_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-conditional-sufficiency-gate-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-conditional-sufficiency-gate-v0.1-results.md")


def main() -> None:
    payload = t149_result_to_dict(run_t149_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _risk(payload: dict[str, object], key: str) -> str:
    value = payload[key]
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T149 Results: Weak-Measurement Conditional-Sufficiency Gate",
        "",
        "## Aggregate checks",
        "",
        f"- Null controls rejected: {payload['all_null_controls_rejected']}",
        f"- Live cases have positive lift: {payload['live_cases_have_positive_lift']}",
        f"- Current frontier active: {payload['current_frontier_active']}",
        "",
        "## Conditional decision audits",
        "",
        (
            "| Case | Classification | Active route | Risk with R | Risk with "
            "(R,A) | Conditional lift | Required next |"
        ),
        "| --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['active_route']}` | "
            f"{_risk(audit, 'record_only_risk')} | "
            f"{_risk(audit, 'record_auxiliary_risk')} | "
            f"{_risk(audit, 'conditional_lift')} | "
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
