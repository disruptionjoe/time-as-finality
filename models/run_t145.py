"""Write T145 physical record deletion fixed-accounting results."""

from __future__ import annotations

import json
from pathlib import Path

from models.physical_record_deletion_fixed_accounting import (
    run_t145_analysis,
    t145_result_to_dict,
)


RESULTS_JSON = Path("results/physical-record-deletion-fixed-accounting-v0.1.json")
RESULTS_MD = Path("results/physical-record-deletion-fixed-accounting-v0.1-results.md")


def main() -> None:
    payload = t145_result_to_dict(run_t145_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T145 Results: Physical Record Deletion Fixed-Accounting Screen",
        "",
        "## Summary",
        "",
        payload["strongest_claim"],
        "",
        "## Audit Table",
        "",
        "| Fixture | Class | Matched accounting | FOA split | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['fixture_id']}` | "
            f"`{audit['reverse_edge_class']}` | "
            f"`{audit['absorber_vector_matched']}` | "
            f"`{audit['future_operation_split']}` | "
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
        ("Fixed-Accounting Capability Splits", "fixed_accounting_capability_splits"),
        ("H7 Arrow Candidates", "h7_arrow_candidates"),
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
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
