"""Write T104 provenance-aware Darwinism absorption results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_provenance_absorption import run_t104_analysis, t104_result_to_dict


RESULTS_JSON = Path("results/q1a-provenance-aware-darwinism-absorption-v0.1.json")
RESULTS_MD = Path("results/q1a-provenance-aware-darwinism-absorption-v0.1-results.md")


def main() -> None:
    payload = t104_result_to_dict(run_t104_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T104 Results: Q1A Provenance-Aware Darwinism Absorption",
        "",
        "## Cases",
        "",
        "| Case | Raw redundancy | Provenance-aware redundancy | D1 support | D1 verdict | Provenance-aware QD verdict | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for case in payload["cases"]:
        support = case["d1_independent_support"]
        redundancy = case["provenance_aware_redundancy"]
        lines.append(
            "| "
            f"{case['case_id']} | "
            f"{case['raw_accessible_redundancy']} | "
            f"{redundancy if redundancy is not None else 'n/a'} | "
            f"{support if support is not None else 'n/a'} | "
            f"{case['d1_verdict']} | "
            f"{case['provenance_qd_verdict']} | "
            f"{case['absorption_status']} |"
        )

    lines.extend(
        [
            "",
            "## Audit flags",
            "",
            f"- Exact absorption on fixed-data cases: {payload['exact_absorption_on_fixed_data_cases']}",
            f"- Hidden partition withholds for both: {payload['hidden_partition_withholds_for_both']}",
            f"- External distinctness earned: {payload['external_distinctness_earned']}",
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
