"""Write T137 weak-measurement postprocessed second-meter obstruction results."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_postprocessed_second_meter_obstruction import (
    run_t137_analysis,
    t137_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-postprocessed-second-meter-obstruction-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-postprocessed-second-meter-obstruction-v0.1-results.md")


def main() -> None:
    payload = t137_result_to_dict(run_t137_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T137 Results: Weak-Measurement Postprocessed Second-Meter Obstruction",
        "",
        "| Scenario | Classification | Postprocessed | Fixed-record split | Witness record | Hot-probability gap |",
        "| --- | --- | --- | --- | --- | ---: |",
    ]
    for audit in payload["audits"]:
        witness_record = audit["witness_record"] if audit["witness_record"] is not None else "none"
        lines.append(
            "| "
            f"`{audit['scenario_name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['postprocessed_from_standard_record']}` | "
            f"`{audit['fixed_record_split_exists']}` | "
            f"`{witness_record}` | "
            f"{audit['witness_gap']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1C update", "q1c_update"),
        ("Open blocker", "blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
