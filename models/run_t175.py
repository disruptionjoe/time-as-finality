"""Write T175 detector threshold-root quorum screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_threshold_root_quorum_screen import (
    run_t175_analysis,
    t175_result_to_dict,
)


RESULTS_JSON = Path("results/detector-threshold-root-quorum-screen-v0.1.json")
RESULTS_MD = Path("results/detector-threshold-root-quorum-screen-v0.1-results.md")


def main() -> None:
    payload = t175_result_to_dict(run_t175_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T175 Results: Detector Threshold-Root Quorum Screen",
        "",
        "## Policy audits",
        "",
        "| Policy | Classification | Release bypass | Revocation bypass | Audit bypass | Required next |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        release = ", ".join(f"`{item}`" for item in audit["release_bypass_domains"])
        revocation = ", ".join(f"`{item}`" for item in audit["revocation_bypass_domains"])
        audit_bypass = ", ".join(f"`{item}`" for item in audit["audit_bypass_domains"])
        lines.append(
            "| "
            f"`{audit['policy_id']}` | "
            f"`{audit['classification']}` | "
            f"{release or '`none`'} | "
            f"{revocation or '`none`'} | "
            f"{audit_bypass or '`none`'} | "
            f"{audit['required_next']} |"
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
