"""Write T418 Schwarzschild horizon access-profile screen results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.schwarzschild_horizon_access_profile_screen import (
    run_schwarzschild_horizon_access_profile_screen,
)


RESULTS_JSON = Path("results/T418-schwarzschild-horizon-access-profile-screen-v0.1.json")
RESULTS_MD = Path("results/T418-schwarzschild-horizon-access-profile-screen-v0.1-results.md")


def main() -> None:
    payload = run_schwarzschild_horizon_access_profile_screen()
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    geometry = payload["horizon_geometry_audit"]
    alignment = payload["access_profile_alignment_audit"]
    positive = payload["positive_control"]
    lines = [
        "# T418 - Schwarzschild Horizon Access-Profile Screen - Results v0.1",
        "",
        f"- **Artifact:** `{payload['artifact']}`",
        f"- **Status:** `{payload['status']}`",
        f"- **Claim ledger update:** {payload['claim_ledger_update']}",
        f"- **North Star / public posture update:** {payload['north_star_or_public_posture_update']}",
        "",
        "## Verdict",
        "",
        payload["verdict"],
        "",
        "## Horizon Geometry Audit",
        "",
        "| Probe | dr/dv | Trace classification | Escapes exterior cutoff? |",
        "| --- | ---: | --- | --- |",
        (
            f"| inside r=1.5 | {geometry['slope_inside']} | "
            f"`{geometry['inside_trace']['classification']}` | "
            f"`{geometry['inside_trace']['escaped_to_exterior_cutoff']}` |"
        ),
        (
            f"| horizon r=2.0 | {geometry['slope_on_horizon']} | "
            f"`{geometry['horizon_trace']['classification']}` | "
            f"`{geometry['horizon_trace']['escaped_to_exterior_cutoff']}` |"
        ),
        (
            f"| outside r=3.0 | {geometry['slope_outside']} | "
            f"`{geometry['outside_trace']['classification']}` | "
            f"`{geometry['outside_trace']['escaped_to_exterior_cutoff']}` |"
        ),
        "",
        "## Access-Profile Alignment Audit",
        "",
        f"- Exterior projections equal: `{alignment['exterior_projection_equal']}`",
        (
            "- Aligned exterior capabilities equal: "
            f"`{alignment['aligned_exterior_capability_equal']}`"
        ),
        (
            "- Cross-profile infalling/full-slice capability splits: "
            f"`{alignment['cross_profile_capability_split']}`"
        ),
        f"- Alignment verdict: `{alignment['alignment_gate_verdict']}`",
        f"- Mismatch verdict: `{alignment['mismatch_verdict']}`",
        f"- Residue label: `{alignment['residue_label']}`",
        "",
        "## Positive Control",
        "",
        f"- Both outside signals reach exterior: `{positive['both_reach_exterior']}`",
        (
            "- Exterior profile distinguishes outside records: "
            f"`{positive['records_distinguished_by_exterior_profile']}`"
        ),
        f"- Residue label: `{positive['residue_label']}`",
        f"- Reason: {positive['reason']}",
        "",
        "## Absorber Audit",
        "",
    ]
    for name, audit in payload["absorber_audit"].items():
        lines.extend(
            [
                f"### {name}",
                "",
                f"- Status: `{audit['status']}`",
                f"- Reason: {audit['reason']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Recommended Next",
            "",
            *[f"- {item}" for item in payload["recommended_next"]],
            "",
            "## Falsification Condition",
            "",
            payload["falsification_condition"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
