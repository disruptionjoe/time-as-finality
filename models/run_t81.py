"""Write T81 measured schema ablation results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.measured_schema_ablation import run_t81_analysis, t81_result_to_dict


RESULTS_JSON = Path("results/measured-schema-ablation-v0.1.json")
RESULTS_MD = Path("results/measured-schema-ablation-v0.1-results.md")


def main() -> None:
    result = run_t81_analysis()
    payload = t81_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T81 Results: Measured Schema Ablation",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Signed baseline",
        "",
        f"- verdict: `{payload['signed']['verdict']}`",
        f"- robust rate: `{payload['signed']['outcome']['robust_rate']}`",
        "",
        "## Single-category ablations",
        "",
        "| Category | Verdict | Load-bearing | Robust rate | Threshold-dependent rate | Withhold rate |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for case in payload["ablations"]:
        outcome = case["outcome"]
        lines.append(
            "| "
            f"{case['category']} | "
            f"{case['verdict']} | "
            f"{case['load_bearing']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['threshold_dependent_rate']} | "
            f"{outcome['withhold_rate']} |"
        )
    lines.extend(
        [
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
