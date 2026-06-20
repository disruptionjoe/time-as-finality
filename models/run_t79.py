"""Write T79 coarse dashboard nonidentifiability results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.dashboard_summary_nonidentifiability import (
    run_t79_analysis,
    t79_result_to_dict,
)


RESULTS_JSON = Path("results/dashboard-summary-nonidentifiability-v0.1.json")
RESULTS_MD = Path("results/dashboard-summary-nonidentifiability-v0.1-results.md")


def main() -> None:
    result = run_t79_analysis()
    payload = t79_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T79 Results: Dashboard Summary Nonidentifiability",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        f"Dashboard projections identical: `{payload['dashboard_equal']}`",
        "",
        "## Completion audits",
        "",
        "| Completion | Verdict | Robust rate | False independence rate | Withhold rate |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        outcome = audit["outcome"]
        lines.append(
            "| "
            f"{audit['name']} | "
            f"{audit['verdict']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['false_independence_rate']} | "
            f"{outcome['withhold_rate']} |"
        )
    lines.extend(
        [
            "",
            "## Shared dashboard summary",
            "",
        ]
    )
    dashboard = payload["audits"][0]["dashboard"]
    lines.extend(
        [
            f"- `local_sigma`: {dashboard['local_sigma']}",
            f"- `archive_sigma`: {dashboard['archive_sigma']}",
            f"- `batching_window`: {dashboard['batching_window']}",
            f"- `tag_retention`: {dashboard['tag_retention']}",
            f"- `signature_verification`: {dashboard['signature_verification']}",
            f"- `threshold_coverage`: {dashboard['threshold_coverage']}",
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
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
