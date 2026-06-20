"""Write T74 provenance protocol Monte Carlo results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.provenance_protocol_monte_carlo import (
    run_t74_analysis,
    t74_result_to_dict,
)


RESULTS_JSON = Path("results/provenance-protocol-monte-carlo-v0.1.json")
RESULTS_MD = Path("results/provenance-protocol-monte-carlo-v0.1-results.md")


def main() -> None:
    result = run_t74_analysis()
    payload = t74_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T74 Results: Provenance Protocol Monte Carlo",
        "",
        (
            f"Monte Carlo audit over {payload['sample_count']} samples per prior "
            f"family with deterministic seed {payload['seed']}."
        ),
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Family table",
        "",
        "| Prior family | Robust | Withhold | Threshold-dependent | False independence | False dependence | D1 computable |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for family, outcome in payload["family_outcomes"].items():
        lines.append(
            "| "
            f"{family} | "
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
