"""Write T109 branch-support collapse results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_branch_support_collapse import run_t109_analysis, t109_result_to_dict


RESULTS_JSON = Path("results/q1a-branch-support-collapse-v0.1.json")
RESULTS_MD = Path("results/q1a-branch-support-collapse-v0.1-results.md")


def main() -> None:
    payload = t109_result_to_dict(run_t109_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T109 Results: Q1A Branch-Support Collapse",
        "",
        "## Aggregate checks",
        "",
        (
            "- Rooted branch support constant on nonzero-support cases: "
            f"{payload['rooted_branch_support_constant_on_nonzero_support_cases']}"
        ),
        (
            "- Rooted branch support varies only with zero-access boundary: "
            f"{payload['rooted_branch_support_varies_only_with_zero_access_boundary']}"
        ),
        (
            "- Rooted branch support splits any same-support class: "
            f"{payload['rooted_branch_support_splits_same_support_class']}"
        ),
        (
            "- Branch-history changes leave fixed-data gate: "
            f"{payload['branch_history_changes_leave_fixed_data_gate']}"
        ),
        (
            "- Any load-bearing branch-support witness in current family: "
            f"{payload['any_load_bearing_branch_support_witness_in_current_family']}"
        ),
        "",
        "## Support to rooted-branch mapping",
        "",
        "| Case | Accessible provenance support | D1 verdict | Rooted branch support |",
        "| --- | --- | --- | --- |",
    ]
    for case in payload["visible_cases"]:
        lines.append(
            "| "
            f"{case['case_id']} | "
            f"{case['accessible_provenance_support']} | "
            f"{case['d1_verdict']} | "
            f"{case['rooted_branch_support']} |"
        )

    lines.extend(
        [
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
