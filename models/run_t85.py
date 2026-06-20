"""Write T85 measured detector channel-dominance results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.measured_detector_channel_dominance import (
    run_t85_analysis,
    t85_result_to_dict,
)


RESULTS_JSON = Path("results/measured-detector-channel-dominance-v0.1.json")
RESULTS_MD = Path("results/measured-detector-channel-dominance-v0.1-results.md")


def main() -> None:
    payload = t85_result_to_dict(run_t85_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T85 Results: Measured Detector Channel Dominance",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Baseline",
        "",
        f"- Verdict: `{payload['baseline']['verdict']}`",
        f"- Robust rate: `{payload['baseline']['outcome']['robust_rate']}`",
        "",
        "## Hostile single-category families",
        "",
        "| Category | Verdict | Independently decisive | Robust rate | Withhold rate | False-independence rate | False-dependence rate |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for case in payload["cases"]:
        outcome = case["outcome"]
        lines.append(
            "| "
            f"{case['category']} | "
            f"{case['verdict']} | "
            f"{case['independently_decisive']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['withhold_rate']} | "
            f"{outcome['false_independence_rate']} | "
            f"{outcome['false_dependence_rate']} |"
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
