"""Write T174 forgotten-dims persistence-gap screen results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.ts_forgotten_dims_pg_screen import run_t174_analysis, t174_result_to_dict


RESULTS_JSON = Path("results/ts-forgotten-dims-pg-screen-v0.1.json")
RESULTS_MD = Path("results/ts-forgotten-dims-pg-screen-v0.1-results.md")


def main() -> None:
    payload = t174_result_to_dict(run_t174_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T174 Results: Forgotten-Dims Persistence-Gap Screen",
        "",
        "## Summary",
        "",
        str(payload["strongest_result"]),
        "",
        "## Audit Table",
        "",
        (
            "| Scenario | Rule | Forgotten dims | Micro PG | Meso inherited gap | "
            "Residual PG | Verdict |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['scenario_id']}` | "
            f"`{audit['holonic_rule']}` | "
            f"`{audit['forgotten_dims']}` | "
            f"`{audit['micro_relative_pg']}` | "
            f"`{audit['inherited_meso_gap']}` | "
            f"`{audit['residual_pg_after_lower_recovery']}` | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['scenario_id']}",
                "",
                f"- Holonic rule: `{audit['holonic_rule']}`",
                f"- Forgotten dims: `{audit['forgotten_dims']}`",
                f"- Micro last obstructed: `{audit['micro_last_obstructed']}`",
                f"- Meso last obstructed: `{audit['meso_last_obstructed']}`",
                f"- Lower last obstructed: `{audit['lower_last_obstructed']}`",
                f"- Holonic last obstructed: `{audit['holonic_last_obstructed']}`",
                f"- PG relative to micro: `{audit['micro_relative_pg']}`",
                f"- Inherited meso gap: `{audit['inherited_meso_gap']}`",
                (
                    "- Residual PG after lower recovery: "
                    f"`{audit['residual_pg_after_lower_recovery']}`"
                ),
                (
                    "- Residual requires explicit retention: "
                    f"`{audit['residual_requires_explicit_retention']}`"
                ),
                (
                    "- Forgotten dims alone generated residual PG: "
                    f"`{audit['forgotten_dims_alone_generated_residual_pg']}`"
                ),
                f"- Verdict: `{audit['verdict']}`",
                f"- Interpretation: {audit['interpretation']}",
            ]
        )

    for heading, key in (
        ("Governance Signal", "governance_signal"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])

    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
