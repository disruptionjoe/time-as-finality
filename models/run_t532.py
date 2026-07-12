"""Runner for T532: finality-native ordering-fraction law starter."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t532_finality_native_ordering_fraction_law_starter import (
    run_t532_analysis,
    t532_result_to_dict,
)


RESULTS_JSON = Path("results/T532-finality-native-ordering-fraction-law-starter-v0.1.json")
RESULTS_MD = Path("results/T532-finality-native-ordering-fraction-law-starter-v0.1-results.md")


def main() -> None:
    payload = t532_result_to_dict(run_t532_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T532 Results: Finality-Native Ordering-Fraction Law Starter Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source T531 verdict: `{payload['source_t531_verdict']}`",
        "- Source T531 admitted packet ids: "
        + (
            ", ".join(f"`{item}`" for item in payload["source_t531_admitted_packet_ids"])
            or "none"
        ),
        f"- Source T530 primary failure axis: `{payload['source_t530_primary_failure_axis']}`",
        "- Source T528 repaired-suite pass count: "
        f"{payload['source_t528_pass_count']}/{payload['source_t528_sample_count']}",
        "- Source T528 failed samples with ordering-fraction miss: "
        f"{payload['source_t528_ordering_failure_count']}",
        "- Independent-naturality candidate ids: "
        + (
            ", ".join(f"`{item}`" for item in payload["independent_naturality_candidate_ids"])
            or "none"
        ),
        "- Cleared real candidate ids: "
        + (", ".join(f"`{item}`" for item in payload["cleared_candidate_ids"]) or "none"),
        "",
        "## Candidate Decisions",
        "",
        "| candidate | classification | action | independent? | T531 terms? | real clear? | S1 evidence? | expected fraction | missing requirements | reason |",
        "| --- | --- | --- | :---: | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for decision in payload["candidate_decisions"]:
        expected = decision["expected_ordering_fraction"]
        expected_text = "none" if expected is None else expected["fraction"]
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['law_id']}` | "
            f"`{decision['classification']}` | "
            f"`{decision['action']}` | "
            f"{decision['independent_naturality_candidate']} | "
            f"{decision['clears_t531_contract_terms']} | "
            f"{decision['clears_as_real_candidate']} | "
            f"{decision['counts_as_s1_evidence']} | "
            f"{expected_text} | "
            f"{missing} | "
            f"{decision['reason']} |"
        )

    lines.extend(
        [
            "",
            "## Deterministic Evidence",
            "",
            "| candidate | evidence |",
            "| --- | --- |",
        ]
    )
    for decision in payload["candidate_decisions"]:
        lines.append(
            f"| `{decision['law_id']}` | {decision['deterministic_evidence']} |"
        )

    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
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
