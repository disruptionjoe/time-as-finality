"""Runner for T530: T528 generator failure router."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t530_t528_generator_failure_router import (
    run_t530_analysis,
    t530_result_to_dict,
)


RESULTS_JSON = Path("results/T530-t528-generator-failure-router-v0.1.json")
RESULTS_MD = Path("results/T530-t528-generator-failure-router-v0.1-results.md")


def main() -> None:
    payload = t530_result_to_dict(run_t530_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.4f})"


def _sample_rate(passed: int, total: int, value: dict[str, Any]) -> str:
    return f"{passed}/{total} ({value['float']:.4f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T530 Results: T528 Generator Failure Router",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source: `{payload['source_artifact']}`",
        (
            "- T528 repaired-suite samples passing: "
            f"{_sample_rate(payload['t528_pass_count'], payload['t528_sample_count'], payload['t528_pass_rate'])}"
        ),
        f"- Failed samples routed: {payload['t528_failed_count']}",
        f"- Primary failure axis: `{payload['primary_failure_axis']}`",
        (
            "- Secondary failure axes: "
            + (", ".join(f"`{axis}`" for axis in payload["secondary_failure_axes"]) or "none")
        ),
        f"- Hard-gate failure count: {payload['hard_gate_failure_count']}",
        "",
        "## Failure Summary By Size",
        "",
        "| n | samples | pass count | failed count | pass rate |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for summary in payload["size_summaries"]:
        lines.append(
            "| "
            f"{summary['event_count']} | "
            f"{summary['sample_count']} | "
            f"{summary['pass_count']} | "
            f"{summary['failed_count']} | "
            f"{_sample_rate(summary['pass_count'], summary['sample_count'], summary['pass_rate'])} |"
        )

    lines.extend(
        [
            "",
            "## Failure Axes",
            "",
            "| axis | failed samples | event counts | representatives | reading |",
            "| --- | ---: | --- | --- | --- |",
        ]
    )
    for axis in payload["failure_axis_summaries"]:
        event_counts = ", ".join(str(item) for item in axis["event_counts"]) or "none"
        reps = ", ".join(axis["representative_samples"]) or "none"
        lines.append(
            "| "
            f"`{axis['axis']}` | "
            f"{axis['failed_sample_count']} | "
            f"{event_counts} | "
            f"{reps} | "
            f"{axis['reading']} |"
        )

    lines.extend(
        [
            "",
            "## Next Packet Routing",
            "",
            "| packet | classification | action | future target? | S1 evidence? | missing requirements | reason |",
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
            f"{decision['admitted_as_future_review_target']} | "
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
