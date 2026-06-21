"""Write T132 weak-measurement non-null criterion results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_nonnull_criterion import (
    run_t132_analysis,
    t132_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-nonnull-criterion-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-nonnull-criterion-v0.1-results.md")


def main() -> None:
    payload = t132_result_to_dict(run_t132_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T132 Results: Weak-Measurement Non-Null Criterion",
        "",
        f"Null protocols: `{payload['null_count']}`",
        f"Candidate protocols: `{payload['candidate_count']}`",
        "",
        "| Protocol | Independent axes | Classification | Passes gate |",
        "| --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        axes = ", ".join(audit["independent_axes"]) if audit["independent_axes"] else "none"
        lines.append(
            f"| `{audit['name']}` | {axes} | `{audit['classification']}` | `{audit['passes_nonnull_gate']}` |"
        )

    lines.extend(
        [
            "",
            "## Strongest claim",
            "",
            payload["strongest_claim"],
            "",
            "## What improved",
            "",
            payload["what_improved"],
            "",
            "## Weakened claim",
            "",
            payload["weakened_claim"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Q1C update",
            "",
            payload["q1c_update"],
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
