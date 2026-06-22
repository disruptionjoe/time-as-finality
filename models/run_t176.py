"""Write T176 detector challenge-window freeze screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_challenge_window_freeze_screen import (
    run_t176_analysis,
    t176_result_to_dict,
)


RESULTS_JSON = Path("results/detector-challenge-window-freeze-screen-v0.1.json")
RESULTS_MD = Path("results/detector-challenge-window-freeze-screen-v0.1-results.md")


def main() -> None:
    payload = t176_result_to_dict(run_t176_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T176 Results: Detector Challenge-Window Freeze Screen",
        "",
        "## Profile audits",
        "",
        "| Profile | Classification | Mutable targets | Mutable effects | Mutable authorities | Required next |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        targets = ", ".join(f"`{item}`" for item in audit["mutable_targets"])
        effects = ", ".join(f"`{item}`" for item in audit["mutable_effects"])
        authorities = ", ".join(
            f"`{item}`" for item in audit["mutable_authorities"]
        )
        lines.append(
            "| "
            f"`{audit['profile_id']}` | "
            f"`{audit['classification']}` | "
            f"{targets or '`none`'} | "
            f"{effects or '`none`'} | "
            f"{authorities or '`none`'} | "
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
