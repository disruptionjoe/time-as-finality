"""Runner for T528: S1 finality-native generator preflight."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t528_s1_finality_native_generator_preflight import (
    run_t528_analysis,
    t528_result_to_dict,
)


RESULTS_JSON = Path("results/T528-s1-finality-native-generator-preflight-v0.1.json")
RESULTS_MD = Path("results/T528-s1-finality-native-generator-preflight-v0.1-results.md")


def main() -> None:
    payload = t528_result_to_dict(run_t528_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.4f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T528 Results: S1 Finality-Native Generator Preflight",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Generator: `{payload['generator_id']}`",
        (
            "- Repaired-suite samples passing: "
            f"{payload['pass_count']}/{payload['sample_count']} "
            f"({_fraction(payload['pass_rate'])})"
        ),
        (
            "- Main packet classification: "
            f"`{payload['main_packet_classification']}`"
        ),
        (
            "- Main packet counts as S1 evidence: "
            f"`{payload['main_packet_counts_as_s1_evidence']}`"
        ),
        (
            "- Hostile controls rejected: "
            f"`{payload['hostile_controls_rejected']}`"
        ),
        "",
        "## Generator Basis",
        "",
        payload["generator_basis"],
        "",
        "## Pass Summary By Size",
        "",
        "| n | samples | pass count | pass rate |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for summary in payload["pass_summary_by_size"]:
        lines.append(
            "| "
            f"{summary['event_count']} | "
            f"{summary['sample_count']} | "
            f"{summary['pass_count']} | "
            f"{_fraction(summary['pass_rate'])} |"
        )

    failed = [audit for audit in payload["sample_audits"] if not audit["repaired_suite_passed"]]
    lines.extend(
        [
            "",
            "## Failed Sample Audits",
            "",
            "| n | seed | T126 class | frac | height | width | max interval | reason |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for audit in failed:
        lines.append(
            "| "
            f"{audit['event_count']} | "
            f"{audit['seed']} | "
            f"`{audit['t126_classification']}` | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"{audit['height']} | "
            f"{audit['width']} | "
            f"{audit['largest_interval_size']} | "
            f"{audit['reason']} |"
        )

    lines.extend(
        [
            "",
            "## Hostile Controls",
            "",
            "| control | n | T126 class | repaired pass | reason |",
            "| --- | ---: | --- | :---: | --- |",
        ]
    )
    for audit in payload["hostile_control_audits"]:
        lines.append(
            "| "
            f"`{audit['control_id']}` | "
            f"{audit['event_count']} | "
            f"`{audit['t126_classification']}` | "
            f"{audit['repaired_suite_passed']} | "
            f"{audit['reason']} |"
        )

    lines.extend(
        [
            "",
            "## Packet Decisions",
            "",
            "| packet | classification | future target? | counts as S1 evidence? | missing requirements | reason |",
            "| --- | --- | :---: | :---: | --- | --- |",
        ]
    )
    for decision in payload["packet_decisions"]:
        missing = ", ".join(decision["missing_requirements"]) or "none"
        lines.append(
            "| "
            f"`{decision['packet_id']}` | "
            f"`{decision['classification']}` | "
            f"{decision['admitted_as_future_review_target']} | "
            f"{decision['counts_as_s1_evidence']} | "
            f"{missing} | "
            f"{decision['reason']} |"
        )

    for heading, key in (
        ("Strongest Reading", "strongest_reading"),
        ("What This Improved", "improved"),
        ("Missing Object", "missing_object"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
