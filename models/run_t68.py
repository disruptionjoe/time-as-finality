"""Write T68 results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.intervention_sensitive_detector_provenance import (
    run_t68_analysis,
    t68_result_to_dict,
)


RESULTS_JSON = Path("results/intervention-sensitive-detector-provenance-v0.1.json")
RESULTS_MD = Path(
    "results/intervention-sensitive-detector-provenance-v0.1-results.md"
)


def main() -> None:
    result = run_t68_analysis()
    payload = t68_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    audit = payload["separation_audit"]
    lines = [
        "# T68 Results: Intervention-Sensitive Detector Provenance",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Separation audit",
        "",
        f"- passive statistics identical: {audit['passive_statistics_identical']}",
        (
            "- intervention partitions distinct: "
            f"{audit['intervention_partitions_distinct']}"
        ),
        f"- D1 computed after partition: {audit['d1_computed_after_partition']}",
        f"- success: {audit['success']}",
        f"- interpretation: {audit['interpretation']}",
        "",
        "## Scenario verdicts",
        "",
    ]
    for scenario in payload["scenarios"]:
        passive = scenario["passive_statistics"]
        d1 = scenario["d1_profile"]
        partition = scenario["partition"]
        lines.extend(
            [
                f"### {scenario['name']}",
                "",
                (
                    f"- passive agreement: {passive['agreement_probability']}; "
                    f"phi: {passive['phi_correlation']}"
                ),
                (
                    "- inferred same independence class: "
                    f"{partition['inferred_same_independence_class']}"
                ),
                f"- inferred classes: {partition['inferred_classes']}",
                f"- D1 profile: {d1['profile_tuple']}",
                f"- observer finalized: {scenario['observer_finalized']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
