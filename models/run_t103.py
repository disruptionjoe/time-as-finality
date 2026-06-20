"""Write T103 Q1A fixed-data witness results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_fixed_data_witness import run_t103_analysis, t103_result_to_dict


RESULTS_JSON = Path("results/q1a-fixed-data-witness-v0.1.json")
RESULTS_MD = Path("results/q1a-fixed-data-witness-v0.1-results.md")


def main() -> None:
    payload = t103_result_to_dict(run_t103_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T103 Results: Q1A Fixed-Data Witness",
        "",
        f"Baseline case: `{payload['baseline_case_id']}`",
        "",
        "## Cases",
        "",
        "| Case | Fixed standard data | Raw redundancy | Independent support | D1 verdict | Gate verdict |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for case in payload["cases"]:
        support = case["independent_accessible_support"]
        lines.append(
            "| "
            f"{case['case_id']} | "
            f"{case['standard_data_matches_baseline']} | "
            f"{case['accessible_raw_redundancy']} | "
            f"{support if support is not None else 'n/a'} | "
            f"{case['d1_verdict']} | "
            f"{case['gate_verdict']} |"
        )

    lines.extend(
        [
            "",
            "## Audit flags",
            "",
            f"- Fixed-data internal witness exists: {payload['fixed_data_internal_witness_exists']}",
            f"- Negative controls rejected: {payload['negative_controls_rejected']}",
            f"- Hidden partition withholds: {payload['hidden_partition_withholds']}",
            f"- External measurement distinction earned: {payload['external_measurement_distinction_earned']}",
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
            "## Claim ledger update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
