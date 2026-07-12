"""Runner for T531: ordering-fraction measure-law contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t531_ordering_fraction_measure_law_contract import (
    run_t531_analysis,
    t531_result_to_dict,
)


RESULTS_JSON = Path("results/T531-ordering-fraction-measure-law-contract-v0.1.json")
RESULTS_MD = Path("results/T531-ordering-fraction-measure-law-contract-v0.1-results.md")


def main() -> None:
    payload = t531_result_to_dict(run_t531_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T531 Results: Ordering-Fraction Measure-Law Contract",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source artifact: `{payload['source_artifact']}`",
        f"- Source verdict: `{payload['source_verdict']}`",
        f"- Source primary failure axis: `{payload['source_primary_failure_axis']}`",
        f"- Source admitted packet: `{payload['source_admitted_packet_id']}`",
        "- Admitted T531 packet ids: "
        + (", ".join(f"`{item}`" for item in payload["admitted_packet_ids"]) or "none"),
        "",
        "## Required Contract Terms",
        "",
    ]
    lines.extend(f"- `{term}`" for term in payload["required_contract_terms"])
    lines.extend(
        [
            "",
            "## Packet Decisions",
            "",
            "| packet | classification | action | contract? | S1 evidence? | missing requirements | reason |",
            "| --- | --- | --- | :---: | :---: | --- | --- |",
        ]
    )
    for decision in payload["packet_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['packet_id']}` | "
            f"`{decision['classification']}` | "
            f"`{decision['action']}` | "
            f"{decision['admitted_as_pre_execution_contract']} | "
            f"{decision['counts_as_s1_evidence']} | "
            f"{missing} | "
            f"{decision['reason']} |"
        )

    for heading, key in (
        ("Strongest Reading", "strongest_reading"),
        ("Recommended Next", "recommended_next"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()

