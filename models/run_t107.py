"""Write T107 loss-relocation results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.loss_relocation import run_t107_analysis, t107_result_to_dict


RESULTS_JSON = Path("results/loss-relocation-v0.1.json")
RESULTS_MD = Path("results/loss-relocation-v0.1-results.md")


def main() -> None:
    payload = t107_result_to_dict(run_t107_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T107 Results: Loss Relocation",
        "",
        "## Aggregate Checks",
        "",
        f"- Derived debt count: {payload['derived_debt_count']}",
        f"- Stable constraint count: {payload['stable_constraint_count']}",
        f"- Absorbed freedom count: {payload['absorbed_freedom_count']}",
        f"- False conservation rejected: {payload['false_conservation_rejected']}",
        f"- Source-anchored derivation: {payload['source_anchored_derivation']}",
        "",
        "## Scenario Verdicts",
        "",
        "| Scenario | Lost axis | Displaced form | Relocation class |",
        "| --- | --- | --- | --- |",
    ]
    for verdict in payload["verdicts"]:
        lines.append(
            "| "
            f"{verdict['scenario']} | "
            f"{verdict['lost_axis']} | "
            f"{verdict['displaced_form']} | "
            f"{verdict['relocation_class']} |"
        )

    lines.extend(
        [
            "",
            "## Six-Axis Bridge",
            "",
            "| GU axis | Lost structure shape | TaF relocation target |",
            "| --- | --- | --- |",
        ]
    )
    for axis, lost_shape, relocation_target in payload["six_axis_bridge"]:
        lines.append(f"| {axis} | {lost_shape} | {relocation_target} |")

    lines.extend(
        [
            "",
            "## Strongest Claim",
            "",
            payload["strongest_claim"],
            "",
            "## What This Improved",
            "",
            payload["improved"],
            "",
            "## What This Weakened",
            "",
            payload["weakened"],
            "",
            "## Falsification Condition",
            "",
            payload["falsification_condition"],
            "",
            "## TF1 Update",
            "",
            payload["tf1_update"],
            "",
            "## Claim Ledger Update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Open Blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
