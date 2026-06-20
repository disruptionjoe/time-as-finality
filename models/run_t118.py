"""Write T118 reversal-cost collapse results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_reversal_cost_collapse import run_t118_analysis, t118_result_to_dict


RESULTS_JSON = Path("results/q1a-reversal-cost-collapse-v0.1.json")
RESULTS_MD = Path("results/q1a-reversal-cost-collapse-v0.1-results.md")


def main() -> None:
    payload = t118_result_to_dict(run_t118_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    hidden_case = payload["hidden_partition_case"]
    lines = [
        "# T118 Results: Q1A Reversal-Cost Collapse",
        "",
        "## Aggregate checks",
        "",
        (
            "- Proxy defined exactly when partition visible: "
            f"{payload['proxy_defined_exactly_when_partition_visible']}"
        ),
        (
            "- Proxy equals support on all visible cases: "
            f"{payload['proxy_equals_support_on_all_visible_cases']}"
        ),
        (
            "- Proxy splits any same-support class: "
            f"{payload['proxy_splits_same_support_class']}"
        ),
        (
            "- Branch-history changes leave fixed-data gate: "
            f"{payload['branch_history_changes_leave_fixed_data_gate']}"
        ),
        (
            "- Any load-bearing reversal-cost witness in current family: "
            f"{payload['any_load_bearing_reversal_cost_witness_in_current_family']}"
        ),
        "",
        "## Support to reversal-cost mapping",
        "",
        "| Case | Accessible provenance support | D1 verdict | Reversal-cost proxy |",
        "| --- | --- | --- | --- |",
    ]
    for case in payload["visible_cases"]:
        lines.append(
            "| "
            f"{case['case_id']} | "
            f"{case['accessible_provenance_support']} | "
            f"{case['d1_verdict']} | "
            f"{case['reversal_cost_proxy']} |"
        )

    lines.extend(
        [
            "",
            "## Hidden partition control",
            "",
            f"- Case: {hidden_case['case_id']}",
            f"- D1 verdict: {hidden_case['d1_verdict']}",
            f"- Reversal-cost proxy: {hidden_case['reversal_cost_proxy']}",
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
            "## Q1A update",
            "",
            payload["q1a_update"],
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
