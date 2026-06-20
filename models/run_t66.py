"""Runner for T66: POVM detector calibration obstruction."""

from __future__ import annotations

import json
from pathlib import Path

from models.povm_detector_calibration_obstruction import (
    run_t66_analysis,
    t66_result_to_dict,
)


JSON_PATH = Path("results") / "povm-detector-calibration-obstruction-v0.1.json"
MD_PATH = Path("results") / "povm-detector-calibration-obstruction-v0.1-results.md"


def render_markdown(data: dict[str, object]) -> str:
    lines = [
        "# T66 Results: POVM Detector Calibration Obstruction",
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
        "| Scenario | t | threshold | Total R_delta | Accessible raw | Independent | D1 profile | Classification |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for scenario in data["scenarios"]:  # type: ignore[assignment]
        lines.append(
            "| {name} | {time} | {threshold} | {total} | {accessible} | {independent} | {profile} | {classification} |".format(
                name=scenario["name"],
                time=scenario["observer_time"],
                threshold=scenario["information_threshold_bits"],
                total=scenario["total_r_delta_raw"],
                accessible=scenario["accessible_r_delta_raw"],
                independent=scenario["accessible_r_delta_independent"],
                profile=tuple(scenario["d1_profile"]["profile_tuple"]),
                classification=scenario["classification"],
            )
        )
    threshold = data["threshold_obstruction"]  # type: ignore[assignment]
    partition = data["independence_obstruction"]  # type: ignore[assignment]
    lines.extend(
        [
            "",
            "## Threshold Obstruction",
            "",
            "| Low threshold | High threshold | Same POVM response | Low finalized | High finalized | Verdict flips |",
            "| ---: | ---: | --- | --- | --- | --- |",
            "| {low} | {high} | {same} | {low_final} | {high_final} | {flips} |".format(
                low=threshold["low_threshold_bits"],
                high=threshold["high_threshold_bits"],
                same=threshold["same_povm_response"],
                low_final=threshold["low_threshold_finalized"],
                high_final=threshold["high_threshold_finalized"],
                flips=threshold["verdict_flips"],
            ),
            "",
            str(threshold["interpretation"]),
            "",
            "## Independence Obstruction",
            "",
            "| Same POVM response | Same access window | Copy partition finalized | Independent partition finalized | Verdict flips |",
            "| --- | --- | --- | --- | --- |",
            "| {same_response} | {same_access} | {copy_final} | {ind_final} | {flips} |".format(
                same_response=partition["same_povm_response"],
                same_access=partition["same_access_window"],
                copy_final=partition["copy_partition_finalized"],
                ind_final=partition["independent_partition_finalized"],
                flips=partition["verdict_flips"],
            ),
            "",
            str(partition["interpretation"]),
            "",
            "## No-Signalling Audit",
            "",
            "| Local setting | Fragment | Local readout marginals by remote setting | Max delta | Passed |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    for audit in data["no_signalling_audits"]:  # type: ignore[assignment]
        marginals = ", ".join(
            f"{setting}: {value}"
            for setting, value in audit["readout_up_probability_by_remote_setting"]
        )
        lines.append(
            "| {setting} | {fragment} | {marginals} | {delta} | {passed} |".format(
                setting=audit["local_setting"],
                fragment=audit["fragment_name"],
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
    result = run_t66_analysis()
    data = t66_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    MD_PATH.write_text(render_markdown(data), encoding="utf-8")

    print("T66: POVM Detector Calibration Obstruction")
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
    print(
        "Threshold verdict flips: "
        f"{result.threshold_obstruction.verdict_flips}"
    )
    print(
        "Independence partition verdict flips: "
        f"{result.independence_obstruction.verdict_flips}"
    )
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
