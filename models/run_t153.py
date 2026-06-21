"""Write T153 Lorentzian causal-diamond screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.lorentzian_causal_diamond_screen import (
    run_t153_analysis,
    t153_result_to_dict,
)


RESULTS_JSON = Path("results/lorentzian-causal-diamond-screen-v0.1.json")
RESULTS_MD = Path("results/lorentzian-causal-diamond-screen-v0.1-results.md")


def main() -> None:
    payload = t153_result_to_dict(run_t153_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T153 Results: Lorentzian Causal-Diamond Screen",
        "",
        "## Aggregate Checks",
        "",
        f"- Remote-signal guardrail passed: {payload['remote_signal_guardrail_passed']}",
        (
            "- Spacelike reconciliation guardrail passed: "
            f"{payload['spacelike_reconciliation_guardrail_passed']}"
        ),
        (
            "- Domain of dependence absorbs reconstructability: "
            f"{payload['domain_dependence_absorbs_reconstructability']}"
        ),
        f"- Changed access diamond absorbed: {payload['changed_diamond_absorbed']}",
        (
            "- Fixed Lorentzian data gives no residue: "
            f"{payload['fixed_lorentzian_data_no_residue']}"
        ),
        "",
        "## Audit Table",
        "",
        (
            "| Case | Classification | Residue | TaF independent? | Matched "
            "Lorentzian data | Capability split | Causal relation | Required next |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['case_id']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['residue_label']}` | "
            f"`{audit['taf_adds_independent_content']}` | "
            f"`{audit['lorentzian_data_matched']}` | "
            f"`{audit['capability_split']}` | "
            f"`{audit['causal_relation']}` | "
            f"{audit['required_next']} |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['case_id']}",
                "",
                f"- Classification: `{audit['classification']}`",
                f"- Domain-of-dependence status: `{audit['domain_of_dependence_status']}`",
                f"- Reason: {audit['reason']}",
                f"- Weakened claim: {audit['weakened_claim']}",
            ]
        )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("R1 Update", "r1_update"),
        ("S1 Update", "s1_update"),
        ("B1 Update", "b1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
