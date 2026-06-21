"""Write T126 finality-colimit causal-set audit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.finality_colimit_causal_set_embeddability import (
    run_t126_analysis,
    t126_result_to_dict,
)


RESULTS_JSON = Path("results/finality-colimit-causal-set-embeddability-v0.1.json")
RESULTS_MD = Path("results/finality-colimit-causal-set-embeddability-v0.1-results.md")


def main() -> None:
    payload = t126_result_to_dict(run_t126_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(payload: dict[str, object], key: str) -> str:
    value = payload[key]
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T126 Results: Finality-Colimit Causal-Set Embeddability Audit",
        "",
        "## Aggregate Checks",
        "",
        (
            "- Descent failures blocked before causal-set claims: "
            f"{payload['descent_failures_blocked_before_causet_claims']}"
        ),
        f"- T16 control passes causal-set gate: {payload['t16_control_passes_causet_gate']}",
        f"- Invalid relations rejected: {payload['invalid_relations_rejected']}",
        (
            "- Valid posets can fail manifold filter: "
            f"{payload['valid_posets_can_fail_manifold_filter']}"
        ),
        (
            "- Passing filter does not derive spacetime: "
            f"{payload['passing_filter_does_not_derive_spacetime']}"
        ),
        "",
        "## Audit Table",
        "",
        (
            "| Case | Classification | Causet candidate | Manifold filter | "
            "Events | Height | Width | Link density | Required next |"
        ),
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for audit in payload["audits"]:
        diagnostics = audit["diagnostics"]
        if diagnostics is None:
            event_count = height = width = "-"
            link_density = "-"
        else:
            event_count = diagnostics["event_count"]
            height = diagnostics["height"]
            width = diagnostics["width"]
            link_density = _fraction(diagnostics, "link_density")
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['causal_set_candidate']}` | "
            f"`{audit['manifold_filter_passed']}` | "
            f"{event_count} | "
            f"{height} | "
            f"{width} | "
            f"{link_density} | "
            f"{audit['required_next']} |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['name']}",
                "",
                f"- Classification: `{audit['classification']}`",
                f"- Causal-set candidate: `{audit['causal_set_candidate']}`",
                f"- Manifold filter passed: `{audit['manifold_filter_passed']}`",
                f"- Poset failures: `{', '.join(audit['poset_report']['failure_reasons'])}`",
                f"- Reason: {audit['reason']}",
                f"- Not claimed: {audit['not_claimed']}",
            ]
        )
        diagnostics = audit["diagnostics"]
        if diagnostics is not None:
            lines.extend(
                [
                    "",
                    "Diagnostics:",
                    "",
                    f"- Comparable fraction: {_fraction(diagnostics, 'comparable_fraction')}",
                    f"- Cover relation count: {diagnostics['cover_relation_count']}",
                    f"- Largest cover hub fraction: {_fraction(diagnostics, 'largest_cover_hub_fraction')}",
                    f"- Rank profile: `{diagnostics['rank_profile']}`",
                    f"- Interval counts by size: `{diagnostics['interval_counts_by_size']}`",
                    (
                        "- Profile spread obstruction: "
                        f"`{diagnostics['profile_spread_obstruction']}`"
                    ),
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
