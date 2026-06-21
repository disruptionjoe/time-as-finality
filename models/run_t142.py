"""Write T142 thermodynamic erasure calibration results."""

from __future__ import annotations

import json
from pathlib import Path

from models.thermodynamic_erasure_calibration import (
    run_t142_analysis,
    t142_result_to_dict,
)


RESULTS_JSON = Path("results/thermodynamic-erasure-calibration-v0.1.json")
RESULTS_MD = Path("results/thermodynamic-erasure-calibration-v0.1-results.md")


def main() -> None:
    payload = t142_result_to_dict(run_t142_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T142 Results: Thermodynamic Erasure Calibration",
        "",
        "## Summary",
        "",
        payload["strongest_claim"],
        "",
        "## T1 Calibrations",
        "",
        "| Case | Strict D1 increase | D1 delta | Reverse modes | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for case in payload["t1_calibrations"]:
        modes = ", ".join(mode["mode_id"] for mode in case["reverse_modes"])
        lines.append(
            "| "
            f"`{case['case_id']}` | "
            f"`{case['strict_forward_increase']}` | "
            f"`{case['d1_delta']}` | "
            f"`{modes}` | "
            f"`{case['overall_verdict']}` |"
        )

    for case in payload["t1_calibrations"]:
        lines.extend(["", f"## {case['case_id']}", ""])
        lines.extend(
            [
                f"- Before profile: `{case['before_profile']}`",
                f"- After profile: `{case['after_profile']}`",
                f"- D1 delta: `{case['d1_delta']}`",
                f"- Overall verdict: `{case['overall_verdict']}`",
                f"- Reason: {case['reason']}",
                "",
                "| Reverse mode | Erased bits | beta*W lower bound | Absorber | Verdict |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for mode in case["reverse_modes"]:
            lines.append(
                "| "
                f"`{mode['mode_id']}` | "
                f"`{mode['erased_bits']}` | "
                f"`{mode['beta_work_lower_bound']}` | "
                f"{mode['standard_absorber']} | "
                f"`{mode['verdict']}` |"
            )

    drawdown = payload["resource_drawdown_calibration"]
    lines.extend(
        [
            "",
            "## Resource Drawdown Calibration",
            "",
            f"- Model: `{drawdown['model_id']}`",
            f"- Resource units drawn down: `{drawdown['resource_units_drawn_down']}`",
            f"- Physical unit named: `{drawdown['physical_unit_named']}`",
            f"- Interpretation: {drawdown['blank_memory_interpretation']}",
            f"- Verdict: `{drawdown['verdict']}`",
            f"- Reason: {drawdown['reason']}",
        ]
    )

    for heading, key in (
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
