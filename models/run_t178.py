"""Write T178 detector preserved-rights successor policy results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_preserved_rights_successor_policy_screen import (
    run_t178_analysis,
    t178_result_to_dict,
)


RESULTS_JSON = Path(
    "results/detector-preserved-rights-successor-policy-screen-v0.1.json"
)
RESULTS_MD = Path(
    "results/detector-preserved-rights-successor-policy-screen-v0.1-results.md"
)


def main() -> None:
    payload = t178_result_to_dict(run_t178_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T178 Results: Detector Preserved-Rights Successor Policy Screen",
        "",
        "## Profile audits",
        "",
        "| Profile | Classification | Predeclared | Guardians preserved | Review access preserved | Guardian identity preserved | Transition log immutable | Required next |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['profile_id']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['successor_predeclared']}` | "
            f"`{audit['preserves_required_guardians']}` | "
            f"`{audit['preserves_review_access']}` | "
            f"`{audit['preserves_guardian_identity']}` | "
            f"`{audit['immutable_transition_log']}` | "
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
