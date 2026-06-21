"""Write T100 detector authority-domain bound results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_authority_domain_bound import (
    run_t100_analysis,
    t100_result_to_dict,
)


RESULTS_JSON = Path("results/detector-authority-domain-bound-v0.1.json")
RESULTS_MD = Path("results/detector-authority-domain-bound-v0.1-results.md")


def main() -> None:
    payload = t100_result_to_dict(run_t100_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T100 Results: Detector Authority-Domain Bound",
        "",
        "## Partition audit",
        "",
        "| Profile | Authorities | Admissible | Trust auditor independent | Governance conflicts | Reason |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        conflicts = ", ".join(audit["governance_conflicts"]) or "none"
        lines.append(
            "| "
            f"{audit['profile_name']} | "
            f"{audit['authority_count']} | "
            f"{audit['admissible']} | "
            f"{audit['trust_auditor_independent']} | "
            f"{conflicts} | "
            f"{audit['reason']} |"
        )

    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Minimum admissible authority count: {payload['minimum_admissible_authority_count']}",
            f"- No three-domain profile survives: {payload['no_three_domain_profile_survives']}",
            f"- Minimal surviving profiles: {', '.join(payload['admissible_four_domain_profiles'])}",
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
