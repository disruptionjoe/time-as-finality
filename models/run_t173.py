"""Write T173 detector claim-review authority-bound results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_claim_review_authority_bound import (
    run_t173_analysis,
    t173_result_to_dict,
)


RESULTS_JSON = Path("results/detector-claim-review-authority-bound-v0.1.json")
RESULTS_MD = Path("results/detector-claim-review-authority-bound-v0.1-results.md")


def main() -> None:
    payload = t173_result_to_dict(run_t173_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T173 Results: Detector Claim-Review Authority Bound",
        "",
        "## Partition audits",
        "",
        "| Profile | Authorities | Admissible | Governance conflicts | Escrow conflicts | Reason |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        governance = ", ".join(f"`{item}`" for item in audit["governance_conflicts"])
        escrow = ", ".join(f"`{item}`" for item in audit["escrow_conflicts"])
        lines.append(
            "| "
            f"`{audit['profile_name']}` | "
            f"{audit['authority_count']} | "
            f"`{audit['admissible']}` | "
            f"{governance or '`none`'} | "
            f"{escrow or '`none`'} | "
            f"`{audit['reason']}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1B update", "q1b_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
