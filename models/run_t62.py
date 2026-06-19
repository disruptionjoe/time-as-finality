"""Runner for T62: noisy measurement access-boundary discriminator."""

from __future__ import annotations

import json
from pathlib import Path

from models.noisy_measurement_access_boundary import (
    run_t62_analysis,
    t62_result_to_dict,
)


JSON_PATH = Path("results") / "noisy-measurement-access-boundary-v0.1.json"
MD_PATH = Path("results") / "noisy-measurement-access-boundary-v0.1-results.md"


def render_markdown(data: dict[str, object]) -> str:
    lines = [
        "# T62 Results: Noisy Measurement Access-Boundary Discriminator",
        "",
        "## Strongest Claim",
        "",
        str(data["strongest_claim"]),
        "",
        "## Weakened Claim",
        "",
        str(data["weakened_claim"]),
        "",
        "## Scenario Matrix",
        "",
        "| Scenario | Coherence | Total R_delta | Accessible R_delta | Independent R_delta | D1 profile | Classification |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for scenario in data["scenarios"]:  # type: ignore[assignment]
        lines.append(
            "| {name} | {coherence} | {total} | {accessible} | {independent} | {profile} | {classification} |".format(
                name=scenario["name"],
                coherence=scenario["pointer_coherence_abs"],
                total=scenario["total_r_delta_raw"],
                accessible=scenario["accessible_r_delta_raw"],
                independent=scenario["accessible_r_delta_independent"],
                profile=tuple(scenario["d1_profile"]["profile_tuple"]),
                classification=scenario["classification"],
            )
        )
    lines.extend(
        [
            "",
            "## Hypothesis Results",
            "",
        ]
    )
    for evaluation in data["hypothesis_evaluations"]:  # type: ignore[assignment]
        lines.append(f"### {evaluation['id']}: {evaluation['status']}")
        lines.append("")
        lines.append(str(evaluation["claim"]))
        lines.append("")
        lines.append(f"Evidence: {evaluation['evidence']}")
        lines.append("")
    lines.extend(
        [
            "## Falsification Condition",
            "",
            str(data["falsification_condition"]),
            "",
            "## Recommended Next",
            "",
            str(data["recommended_next"]),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = run_t62_analysis()
    data = t62_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    MD_PATH.write_text(render_markdown(data), encoding="utf-8")

    print("T62: Noisy Measurement Access-Boundary Discriminator")
    print()
    print(result.strongest_claim)
    print()
    for scenario in result.scenarios:
        print(f"  {scenario.scenario.name}: {scenario.classification}")
        print(
            "    coherence={coherence}, total_R={total}, accessible_R={accessible}, independent_R={independent}, D1={profile}".format(
                coherence=scenario.pointer_coherence_abs,
                total=scenario.total_r_delta_raw,
                accessible=scenario.accessible_r_delta_raw,
                independent=scenario.accessible_r_delta_independent,
                profile=scenario.d1_profile.as_tuple(),
            )
        )
    print()
    print(f"JSON written to {JSON_PATH}")
    print(f"Markdown written to {MD_PATH}")


if __name__ == "__main__":
    main()
