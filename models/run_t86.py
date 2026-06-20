"""Write T86 ambiguous-tag channel-independence results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.ambiguous_tag_channel_independence import (
    run_t86_analysis,
    t86_result_to_dict,
)


RESULTS_JSON = Path("results/ambiguous-tag-channel-independence-v0.1.json")
RESULTS_MD = Path("results/ambiguous-tag-channel-independence-v0.1-results.md")


def main() -> None:
    payload = t86_result_to_dict(run_t86_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T86 Results: Ambiguous-Tag Channel Independence",
        "",
        (
            f"Monte Carlo audit over {payload['sample_count']} samples per "
            f"raw-log fixture with deterministic seed {payload['seed']}."
        ),
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Fixture table",
        "",
        "| Case | Channel | Role | Verdict | Rescue | Robust | Withhold | D1 computable |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for case in payload["cases"]:
        outcome = case["outcome"]
        lines.append(
            "| "
            f"{case['name']} | "
            f"{case['channel_under_test']} | "
            f"{case['role']} | "
            f"{case['verdict']} | "
            f"{case['rescues_with_ambiguous_tags']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['withhold_rate']} | "
            f"{outcome['computable_d1_rate']} |"
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
