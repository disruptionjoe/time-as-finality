"""Write T75 real detector stack provenance mapping results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.real_detector_stack_provenance import (
    run_t75_analysis,
    t75_result_to_dict,
)


RESULTS_JSON = Path("results/real-detector-stack-provenance-v0.1.json")
RESULTS_MD = Path("results/real-detector-stack-provenance-v0.1-results.md")


def main() -> None:
    result = run_t75_analysis()
    payload = t75_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T75 Results: Real Detector Stack Provenance Mapping",
        "",
        (
            f"Selected stack: `{payload['selected_stack']}`. "
            f"Monte Carlo audit over {payload['sample_count']} samples with "
            f"deterministic seed {payload['seed']}."
        ),
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Source anchors",
        "",
        "| Parameter | Value used | Source |",
        "| --- | --- | --- |",
    ]
    for note in payload["source_notes"]:
        lines.append(
            "| "
            f"{note['parameter']} | "
            f"{note['value_used']} | "
            f"{note['source']} |"
        )
    lines.extend(
        [
            "",
            "## Stack classification",
            "",
            "| Mapping | Verdict | Robust | Withhold | Threshold-dependent | False independence | False dependence | D1 computable |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for mapping in payload["mappings"]:
        outcome = mapping["outcome"]
        lines.append(
            "| "
            f"{mapping['name']} | "
            f"{mapping['verdict']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['withhold_rate']} | "
            f"{outcome['threshold_dependent_rate']} | "
            f"{outcome['false_independence_rate']} | "
            f"{outcome['false_dependence_rate']} | "
            f"{outcome['computable_d1_rate']} |"
        )
    lines.extend(
        [
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
