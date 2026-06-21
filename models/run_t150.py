"""Write T150 weak-measurement verdict-admissibility gate results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_verdict_admissibility_gate import (
    run_t150_analysis,
    t150_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-verdict-admissibility-gate-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-verdict-admissibility-gate-v0.1-results.md")


def main() -> None:
    payload = t150_result_to_dict(run_t150_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _risk(payload: dict[str, object], key: str) -> str:
    value = payload[key]
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T150 Results: Weak-Measurement Verdict-Admissibility Gate",
        "",
        "## Aggregate checks",
        "",
        f"- Null controls rejected: {payload['all_null_controls_rejected']}",
        f"- Live cases clear target gate: {payload['live_cases_clear_target_gate']}",
        f"- Current frontier active: {payload['current_frontier_active']}",
        "",
        "## Verdict audits",
        "",
        (
            "| Case | Classification | Active route | Risk with R | Risk with "
            "(R,A) | Conditional lift | Smallest verdict support | Required next |"
        ),
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
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
            f"{_risk(audit, 'smallest_verdict_support')} | "
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
