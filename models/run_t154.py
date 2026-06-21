"""Runner for T154: T54/T58-to-T126 bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t54_t58_t126_bridge import run_t154_analysis, t154_result_to_dict


RESULTS_JSON = Path("results/t54-t58-t126-bridge-v0.1.json")
RESULTS_MD = Path("results/t54-t58-t126-bridge-v0.1-results.md")


def main() -> None:
    payload = t154_result_to_dict(run_t154_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any] | None) -> str:
    if value is None:
        return "-"
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T154 Results: T54/T58-to-T126 Bridge",
        "",
        "## Aggregate Checks",
        "",
        f"- Canonical completions audited: {payload['canonical_completions_audited']}",
        f"- T58 gate required and passed: {payload['t58_gate_required']}",
        (
            "- Actual canonical colimits blocked before manifold claims: "
            f"{payload['all_actual_canonical_colimits_blocked_before_manifold_claims']}"
        ),
        (
            "- No named dimension estimator applied: "
            f"{payload['no_named_dimension_estimator_applied']}"
        ),
        "",
        "## Bridge Table",
        "",
        (
            "| Source completion | T54 | T58 gate | T126 | Causet candidate | "
            "Manifold filter | Events | Strict pairs | Ordering fraction | Verdict |"
        ),
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for audit in payload["audits"]:
        strict_pairs = (
            "-"
            if audit["strict_pair_count"] is None
            else str(audit["strict_pair_count"])
        )
        lines.append(
            "| "
            f"`{audit['source_completion']}` | "
            f"`{audit['t54_classification']}` | "
            f"`{audit['t58_gap_gate_passed']}` | "
            f"`{audit['t126_classification']}` | "
            f"`{audit['causal_set_candidate']}` | "
            f"`{audit['manifold_filter_passed']}` | "
            f"{audit['event_count']} | "
            f"{strict_pairs} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['source_completion']}",
                "",
                f"- T126 classification: `{audit['t126_classification']}`",
                f"- Dimension diagnostic: `{audit['dimension_diagnostic']}`",
                f"- Reason: {audit['reason']}",
            ]
        )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
