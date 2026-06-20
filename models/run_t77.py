"""Write T77 measured detector policy sensitivity results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.measured_detector_policy_sensitivity import (
    run_t77_analysis,
    t77_result_to_dict,
)


RESULTS_JSON = Path("results/measured-detector-policy-sensitivity-v0.1.json")
RESULTS_MD = Path("results/measured-detector-policy-sensitivity-v0.1-results.md")


def main() -> None:
    result = run_t77_analysis()
    payload = t77_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T77 Results: Measured Detector Policy Sensitivity",
        "",
        (
            f"Policy-sensitivity audit over {payload['sample_count']} samples "
            f"per policy/deployment pair with deterministic seed {payload['seed']}."
        ),
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Audit table",
        "",
        "| Policy | Deployment | Verdict | Robust | Withhold | Threshold-dependent | False independence | False dependence |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        outcome = audit["outcome"]
        lines.append(
            "| "
            f"{audit['policy_name']} | "
            f"{audit['deployment_name']} | "
            f"{audit['verdict']} | "
            f"{outcome['robust_rate']} | "
            f"{outcome['withhold_rate']} | "
            f"{outcome['threshold_dependent_rate']} | "
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
