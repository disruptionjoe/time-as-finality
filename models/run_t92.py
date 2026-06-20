"""Write T92 accessible-witness gap restriction results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.accessible_witness_gap_restriction import (
    run_t92_analysis,
    t92_result_to_dict,
)


RESULTS_JSON = Path("results/accessible-witness-gap-restriction-v0.1.json")
RESULTS_MD = Path("results/accessible-witness-gap-restriction-v0.1-results.md")


def main() -> None:
    payload = t92_result_to_dict(run_t92_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T92 Results: Accessible-Witness Gap Restriction",
        "",
        f"Theorem status: `{payload['theorem_status']}`",
        "",
        "## Audit Summary",
        "",
        "| System | Classification | Ambient | Audit monotone | Stable typing | Gap closed | Violations | Non-lifting |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"{audit['system_name']} | "
            f"{audit['classification']} | "
            f"{audit['ambient_restriction_holds']} | "
            f"{audit['audit_monotonicity_holds']} | "
            f"{audit['stable_typing_holds']} | "
            f"{audit['gap_restriction_holds']} | "
            f"{len(audit['violations'])} | "
            f"{len(audit['non_lifting_examples'])} |"
        )
    lines.extend(
        [
            "",
            "## Patch Tables",
            "",
        ]
    )
    for audit in payload["audits"]:
        lines.extend(
            [
                f"### {audit['system_name']}",
                "",
                "| Patch | A(U) | F(U) | G(U) |",
                "| --- | --- | --- | --- |",
            ]
        )
        for row in audit["patch_table"]:
            lines.append(
                "| "
                f"{row['patch']} | "
                f"{', '.join(row['A']) or 'empty'} | "
                f"{', '.join(row['F']) or 'empty'} | "
                f"{', '.join(row['G']) or 'empty'} |"
            )
        lines.append("")
    lines.extend(
        [
            "## Strongest Claim",
            "",
            payload["strongest_claim"],
            "",
            "## Weakened Claim",
            "",
            payload["weakened_claim"],
            "",
            "## Falsification Condition",
            "",
            payload["falsification_condition"],
            "",
            "## Claim Update",
            "",
            payload["claim_update"],
            "",
            "## Open Blocker",
            "",
            payload["open_blocker"],
            "",
            "## Suggested Next",
            "",
            payload["suggested_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
