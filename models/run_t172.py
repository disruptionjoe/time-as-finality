"""Write T172 issuance-to-finality bridge results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.issuance_to_finality_bridge import (
    run_t172_analysis,
    t172_result_to_dict,
)


RESULTS_JSON = Path("results/issuance-to-finality-bridge-v0.1.json")
RESULTS_MD = Path("results/issuance-to-finality-bridge-v0.1-results.md")


def main() -> None:
    payload = t172_result_to_dict(run_t172_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T172 Results: Issuance-To-Finality Bridge",
        "",
        "## Summary",
        "",
        str(payload["strongest_claim"]),
        "",
        "## Audit Table",
        "",
        (
            "| Fixture | Same source order | Same records | Same readout | Same mu | "
            "Source split | Readout split | Verdict |"
        ),
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['fixture_id']}` | "
            f"`{audit['same_source_order']}` | "
            f"`{audit['same_observer_records']}` | "
            f"`{audit['same_taf_readout_edges']}` | "
            f"`{audit['same_mu']}` | "
            f"`{audit['source_capability_split']}` | "
            f"`{audit['taf_readout_split']}` | "
            f"`{audit['verdict']}` |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['fixture_id']}",
                "",
                f"- Kind: `{audit['fixture_kind']}`",
                f"- Task: `{audit['task']}`",
                f"- Same source order: `{audit['same_source_order']}`",
                f"- Same observer records: `{audit['same_observer_records']}`",
                f"- Same TaF readout edges: `{audit['same_taf_readout_edges']}`",
                f"- Same `mu`: `{audit['same_mu']}`",
                f"- Finality profile split: `{audit['finality_profile_split']}`",
                f"- Source capability split: `{audit['source_capability_split']}`",
                f"- TaF readout split: `{audit['taf_readout_split']}`",
                f"- Left source order recovered: `{audit['left_source_order_recovered']}`",
                f"- Right source order recovered: `{audit['right_source_order_recovered']}`",
                f"- Left access scores: `{audit['left_access_scores']}`",
                f"- Right access scores: `{audit['right_access_scores']}`",
                f"- Left access monotone: `{audit['left_access_monotone']}`",
                f"- Right access monotone: `{audit['right_access_monotone']}`",
                (
                    "- H7 source-arrow upgrade candidate: "
                    f"`{audit['h7_source_arrow_upgrade_candidate']}`"
                ),
                f"- Verdict: `{audit['verdict']}`",
                f"- Interpretation: {audit['interpretation']}",
            ]
        )

    for heading, key in (
        ("Reflection Controls", "reflection_controls"),
        ("Cadence Boundaries", "cadence_boundaries"),
        ("Source Capability Losses", "source_capability_losses"),
        ("Mu-Invisible Losses", "mu_invisible_losses"),
        ("Access Boundary Cases", "access_boundary_cases"),
        ("Gluing Failures", "gluing_failures"),
        ("H7 Arrow Candidates", "h7_arrow_candidates"),
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("H7 Update", "h7_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", ""])
        value = payload[key]
        if isinstance(value, list):
            if value:
                lines.extend(f"- `{item}`" for item in value)
            else:
                lines.append("None.")
        else:
            lines.append(str(value))

    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
