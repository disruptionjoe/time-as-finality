"""Write T144 Q1A current-family closure results."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_current_family_closure import run_t144_analysis, t144_result_to_dict


RESULTS_JSON = Path("results/q1a-current-family-closure-v0.1.json")
RESULTS_MD = Path("results/q1a-current-family-closure-v0.1-results.md")


def main() -> None:
    payload = t144_result_to_dict(run_t144_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T144 Results: Q1A Current-Family Closure",
        "",
        "## Aggregate checks",
        "",
        (
            "- Closure classifier matches D1: "
            f"{payload['closure_classifier_matches_d1']}"
        ),
        (
            "- D1 factors through closure key: "
            f"{payload['d1_factors_through_closure_key']}"
        ),
        (
            "- Branch support factors through closure key: "
            f"{payload['branch_support_factors_through_closure_key']}"
        ),
        (
            "- Reversal cost factors through closure key: "
            f"{payload['reversal_cost_factors_through_closure_key']}"
        ),
        (
            "- Raw redundancy is not sufficient: "
            f"{payload['raw_redundancy_is_not_sufficient']}"
        ),
        (
            "- Branch support load-bearing: "
            f"{payload['branch_support_load_bearing']}"
        ),
        (
            "- Reversal cost load-bearing: "
            f"{payload['reversal_cost_load_bearing']}"
        ),
        (
            "- Current family closed under declared dimensions: "
            f"{payload['current_family_closed_under_declared_dimensions']}"
        ),
        "",
        "## Closure fibers",
        "",
        (
            "| Partition visible | Accessible support | Cases | D1 verdicts | Raw "
            "redundancies | Branch supports | Reversal-cost proxies |"
        ),
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for fiber in payload["fibers"]:
        lines.append(
            "| "
            f"{fiber['partition_visible']} | "
            f"{fiber['accessible_provenance_support']} | "
            f"{fiber['case_count']} | "
            f"{fiber['d1_verdicts']} | "
            f"{fiber['raw_accessible_redundancies']} | "
            f"{fiber['rooted_branch_support_values']} | "
            f"{fiber['reversal_cost_proxy_values']} |"
        )

    hidden = payload["hidden_partition_case"]
    lines.extend(
        [
            "",
            "## Hidden partition control",
            "",
            f"- Case: {hidden['case_id']}",
            f"- D1 verdict: {hidden['d1_verdict']}",
            f"- Closure verdict: {hidden['closure_verdict']}",
            "",
        ]
    )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1A update", "q1a_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
