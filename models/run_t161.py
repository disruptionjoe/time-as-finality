"""Write T161 detector control-root independence results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_control_root_independence import (
    run_t161_analysis,
    t161_result_to_dict,
)


RESULTS_JSON = Path("results/detector-control-root-independence-v0.1.json")
RESULTS_MD = Path("results/detector-control-root-independence-v0.1-results.md")


def main() -> None:
    payload = t161_result_to_dict(run_t161_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T161 Results: Detector Control-Root Independence",
        "",
        "## Workflow audits",
        "",
        "| Profile | Nominal profile | Effective profile | Nominal count | Effective count | Effective admissible | Shared critical roots | Ignored noncritical roots |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        critical = ", ".join(audit["shared_critical_roots"]) or "none"
        noncritical = ", ".join(audit["ignored_noncritical_roots"]) or "none"
        lines.append(
            "| "
            f"`{audit['profile_name']}` | "
            f"`{audit['nominal_profile_name']}` | "
            f"`{audit['effective_profile_name']}` | "
            f"`{audit['nominal_authority_count']}` | "
            f"`{audit['effective_authority_count']}` | "
            f"`{audit['effective_admissible']}` | "
            f"`{critical}` | "
            f"`{noncritical}` |"
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
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
