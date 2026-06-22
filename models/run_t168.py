"""Write T168 exact-sector / gauge restriction screen results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.h7_sector_restriction_screen import (
    run_t168_analysis,
    t168_result_to_dict,
)


RESULTS_JSON = Path("results/h7-sector-restriction-screen-v0.1.json")
RESULTS_MD = Path("results/h7-sector-restriction-screen-v0.1-results.md")


def main() -> None:
    payload = t168_result_to_dict(run_t168_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T168 Results: H7 Sector-Restriction Screen",
        "",
        "## Summary",
        "",
        str(payload["strongest_claim"]),
        "",
        "## Audit Table",
        "",
        (
            "| Fixture | Matched accounting | Finite substrate | "
            "Gauge-invariant | FOA split | H7 candidate | Verdict |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['fixture_id']}` | "
            f"`{audit['absorber_vector_matched']}` | "
            f"`{audit['finite_operational_substrate']}` | "
            f"`{audit['gauge_invariant_difference']}` | "
            f"`{audit['future_operation_split']}` | "
            f"`{audit['h7_upgrade_candidate']}` | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['fixture_id']}",
                "",
                f"- Source: {audit['source']}",
                f"- Reverse-edge class: `{audit['reverse_edge_class']}`",
                f"- Absorber vector matched: `{audit['absorber_vector_matched']}`",
                f"- Absorber mismatch fields: `{audit['absorber_mismatch_fields']}`",
                f"- Finite operational substrate: `{audit['finite_operational_substrate']}`",
                f"- Gauge-invariant difference: `{audit['gauge_invariant_difference']}`",
                f"- D1 topology split: `{audit['d1_topology_split']}`",
                f"- Future operation: `{audit['future_operation']}`",
                f"- Future-operation split: `{audit['future_operation_split']}`",
                f"- Reverse status: `{audit['reverse_status']}`",
                f"- H7 upgrade candidate: `{audit['h7_upgrade_candidate']}`",
                f"- Verdict: `{audit['verdict']}`",
                f"- Interpretation: {audit['interpretation']}",
            ]
        )

    for heading, key in (
        ("Sector-Rule Stipulations", "sector_rule_stipulations"),
        ("Reservoir Absorptions", "reservoir_absorptions"),
        ("Gauge Redundancies", "gauge_redundancies"),
        ("Fixed-Accounting Topology Residues", "fixed_accounting_topology_residues"),
        ("H7 Arrow Candidates", "h7_arrow_candidates"),
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", ""])
        value = payload[key]
        if isinstance(value, list):
            if value:
                lines.extend(f"- `{item}`" for item in value)
            else:
                lines.append("None.")
        else:
            lines.append(str(value))
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
