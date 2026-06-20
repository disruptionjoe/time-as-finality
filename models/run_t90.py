"""Write T90 weak-measurement obstruction results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_reparameterization_obstruction import (
    run_t90_analysis,
    t90_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-reparameterization-obstruction-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-reparameterization-obstruction-v0.1-results.md")


def main() -> None:
    payload = t90_result_to_dict(run_t90_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    null_times = payload["null_times"]
    independent_pair = payload["independent_pair"]
    post_hoc_pair = payload["post_hoc_pair"]

    lines = [
        "# T90 Results: Weak-Measurement Reparameterization Obstruction",
        "",
        "## Null fixture",
        "",
        f"Verdict: `{payload['null_verdict']}`",
        "",
        "| Time | Value |",
        "| --- | ---: |",
        f"| `t_decohere` | {null_times['decoherence_time']} |",
        f"| `t_redundancy` | {null_times['redundancy_time']} |",
        f"| `t_access` | {null_times['access_time']} |",
        f"| `t_finality` | {null_times['taf_finality_time']} |",
        "",
        "## Identical-standard-statistics pair",
        "",
        "| Audit field | Independent branch | Post hoc branch |",
        "| --- | --- | --- |",
    ]
    for field in (
        "standard_timelines_equal",
        "standard_verdict_equal",
        "taf_verdict_changes",
        "has_independent_source",
        "rejected_for_post_hoc_source",
        "verdict",
    ):
        lines.append(
            "| "
            f"`{field}` | "
            f"{independent_pair[field]} | "
            f"{post_hoc_pair[field]} |"
        )

    lines.extend(
        [
            "",
            "## Strongest claim",
            "",
            payload["strongest_claim"],
            "",
            "## Weakened claim",
            "",
            payload["weakened_claim"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Q1 update",
            "",
            payload["q1_update"],
            "",
            "## Blocker",
            "",
            payload["blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
