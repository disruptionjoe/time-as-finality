"""Write T101 Q1 branch adjudication results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1_branch_adjudication import run_t101_analysis, t101_result_to_dict


RESULTS_JSON = Path("results/q1-branch-adjudication-v0.1.json")
RESULTS_MD = Path("results/q1-branch-adjudication-v0.1-results.md")


def main() -> None:
    payload = t101_result_to_dict(run_t101_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T101 Results: Q1 Branch Adjudication",
        "",
        "## Branch verdicts",
        "",
        "| Branch | Proposed claim | Status | Evidence | Next gate |",
        "| --- | --- | --- | --- | --- |",
    ]
    for branch in payload["branches"]:
        lines.append(
            "| "
            f"{branch['branch_id']} | "
            f"{branch['proposed_claim_id']} | "
            f"{branch['current_status']} | "
            f"{', '.join(branch['evidence_ids'])} | "
            f"{branch['next_gate']} |"
        )

    lines.extend(
        [
            "",
            "## Summary flags",
            "",
            f"- Q1 should split before paper language: {payload['q1_should_split_before_paper_language']}",
            f"- No branch earns new measurement dynamics: {payload['no_branch_earns_new_measurement_dynamics']}",
            f"- Detector branch externally blocked: {payload['detector_branch_externally_blocked']}",
            f"- Weak measurement reinstatement-only: {payload['weak_measurement_reinstatement_only']}",
            f"- Contextuality branch guardrail-only: {payload['contextuality_branch_is_guardrail_only']}",
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
