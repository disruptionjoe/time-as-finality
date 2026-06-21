"""Write T94 weak-measurement priority demotion results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.weak_measurement_priority_demotion import (
    run_t94_analysis,
    t94_result_to_dict,
)


RESULTS_JSON = Path("results/weak-measurement-priority-demotion-v0.1.json")
RESULTS_MD = Path("results/weak-measurement-priority-demotion-v0.1-results.md")


def main() -> None:
    payload = t94_result_to_dict(run_t94_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    detector = payload["detector_state"]
    weak = payload["weak_measurement_state"]
    audit = payload["audit"]
    lines = [
        "# T94 Results: Weak-Measurement Priority Demotion",
        "",
        "## Route states",
        "",
        "| Route | Real platform | Pre-registered raw-log protocol | Survives current null criterion | Independent axis named before analysis | Source-anchored candidate | Empirical deployment present |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        "| detector provenance | "
        f"{detector['has_real_platform']} | "
        f"{detector['has_preregistered_raw_log_protocol']} | "
        f"{detector['survives_current_null_criterion']} | "
        f"{detector['has_independent_axis_named_before_analysis']} | "
        f"{detector['has_source_anchored_candidate']} | "
        f"{detector['empirical_deployment_present']} |",
        "| weak measurement | "
        f"{weak['has_real_platform']} | "
        f"{weak['has_preregistered_raw_log_protocol']} | "
        f"{weak['survives_current_null_criterion']} | "
        f"{weak['has_independent_axis_named_before_analysis']} | "
        f"{weak['has_source_anchored_candidate']} | "
        f"{weak['empirical_deployment_present']} |",
        "",
        "## Priority verdict",
        "",
        f"Preferred route: `{audit['preferred_route']}`",
        "",
        f"Weak-measurement status: `{audit['weak_measurement_status']}`",
        "",
        f"Detector status: `{audit['detector_status']}`",
        "",
        audit["justification"],
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## What this improved",
        "",
        payload["improved"],
        "",
        "## What this weakened",
        "",
        payload["weakened"],
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
        "## Recommended next",
        "",
        payload["recommended_next"],
        "",
    ]
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
