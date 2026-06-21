"""Write T151 causal-access screen results."""

from __future__ import annotations

import json
from pathlib import Path

from models.causal_access_screen import run_t151_analysis, t151_result_to_dict


RESULTS_JSON = Path("results/causal-access-screen-v0.1.json")
RESULTS_MD = Path("results/causal-access-screen-v0.1-results.md")


def main() -> None:
    payload = t151_result_to_dict(run_t151_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T151 Results: Causal-Access Screen",
        "",
        "## Aggregate checks",
        "",
        f"- Remote-observation guardrail passed: {payload['remote_observation_guardrail_passed']}",
        (
            "- Horizon claim absorbed by causal reachability: "
            f"{payload['horizon_claim_absorbed_by_causal_reachability']}"
        ),
        f"- Encoded-channel overclaim rejected: {payload['encoded_channel_overclaim_rejected']}",
        f"- Soft boundary parameterized: {payload['soft_boundary_parameterized']}",
        "",
        "## Access audits",
        "",
        (
            "| Case | Classification | Residue | TaF independent? | Exterior "
            "classical | Exterior extended | Local classical | Boundary | Required next |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['residue_label']}` | "
            f"`{audit['taf_adds_independent_content']}` | "
            f"`{audit['exterior_classical_access']}` | "
            f"`{audit['exterior_extended_access']}` | "
            f"`{audit['local_classical_access']}` | "
            f"`{audit['boundary_permeability']}` | "
            f"{audit['required_next']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("B1 update", "b1_update"),
        ("S1 update", "s1_update"),
        ("R1 update", "r1_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
