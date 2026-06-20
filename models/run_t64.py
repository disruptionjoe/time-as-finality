"""Runner for T64: Stern-Gerlach detector access-window discriminator."""

from __future__ import annotations

import json
from pathlib import Path

from models.stern_gerlach_access_window import (
    run_t64_analysis,
    t64_result_to_dict,
)


JSON_PATH = Path("results") / "stern-gerlach-access-window-v0.1.json"
MD_PATH = Path("results") / "stern-gerlach-access-window-v0.1-results.md"


def render_markdown(data: dict[str, object]) -> str:
    lines = [
        "# T64 Results: Stern-Gerlach Detector Access-Window Discriminator",
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
        "| Scenario | t | threshold | coherence | Total R_delta | Accessible raw | Independent | D1 profile | Classification |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for scenario in data["scenarios"]:  # type: ignore[assignment]
        lines.append(
            "| {name} | {time} | {threshold} | {coherence} | {total} | {accessible} | {independent} | {profile} | {classification} |".format(
                name=scenario["name"],
                time=scenario["observer_time"],
                threshold=scenario["information_threshold_bits"],
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
            "## Threshold Sweep",
            "",
            "| threshold | t | Total R_delta | Independent accessible | Finalized | Classification |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for point in data["threshold_sweep"]:  # type: ignore[assignment]
        lines.append(
            "| {threshold} | {time} | {total} | {independent} | {finalized} | {classification} |".format(
                threshold=point["information_threshold_bits"],
                time=point["observer_time"],
                total=point["total_r_delta_raw"],
                independent=point["accessible_r_delta_independent"],
                finalized=point["observer_finalized"],
                classification=point["classification"],
            )
        )
    lines.extend(
        [
            "",
            f"Threshold-sensitive time slices: {data['threshold_flip_count']}",
            "",
            "## No-Signalling Audit",
            "",
            "| Local setting | Local readout marginals by remote setting | Max delta | Passed |",
            "| --- | --- | ---: | --- |",
        ]
    )
    for audit in data["no_signalling_audits"]:  # type: ignore[assignment]
        marginals = ", ".join(
            f"{setting}: {value}"
            for setting, value in audit["readout_up_probability_by_remote_setting"]
        )
        lines.append(
            "| {setting} | {marginals} | {delta} | {passed} |".format(
                setting=audit["local_setting"],
                marginals=marginals,
                delta=audit["max_delta"],
                passed=audit["passed"],
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
    result = run_t64_analysis()
    data = t64_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    MD_PATH.write_text(render_markdown(data), encoding="utf-8")

    print("T64: Stern-Gerlach Detector Access-Window Discriminator")
    print()
    print(result.strongest_claim)
    print()
    for scenario in result.scenarios:
        print(f"  {scenario.scenario.name}: {scenario.classification}")
        print(
            "    t={time}, threshold={threshold}, total_R={total}, accessible_R={accessible}, independent_R={independent}, D1={profile}".format(
                time=scenario.scenario.observer_time,
                threshold=scenario.scenario.information_threshold_bits,
                total=scenario.total_r_delta_raw,
                accessible=scenario.accessible_r_delta_raw,
                independent=scenario.accessible_r_delta_independent,
                profile=scenario.d1_profile.as_tuple(),
            )
        )
    print()
    print(f"Threshold-sensitive time slices: {result.threshold_flip_count}")
    print(
        "No-signalling audits passed: {passed}/{total}".format(
            passed=sum(1 for audit in result.no_signalling_audits if audit.passed),
            total=len(result.no_signalling_audits),
        )
    )
    print()
    print(f"JSON written to {JSON_PATH}")
    print(f"Markdown written to {MD_PATH}")


if __name__ == "__main__":
    main()
