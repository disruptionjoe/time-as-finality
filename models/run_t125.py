"""Write T125 D1 boundary-connection transport results."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.d1_boundary_connection_transport import (
    run_t125_analysis,
    t125_result_to_dict,
)


RESULTS_JSON = Path("results/d1-boundary-connection-transport-v0.1.json")
RESULTS_MD = Path("results/d1-boundary-connection-transport-v0.1-results.md")


def main() -> None:
    payload = t125_result_to_dict(run_t125_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T125 Results: D1 Boundary-Connection Transport",
        "",
        "## Strongest Claim",
        "",
        str(payload["strongest_claim"]),
        "",
        "## Boundary Objects",
        "",
        "| Boundary | Profile | Provenance |",
        "| --- | --- | --- |",
    ]
    for item in payload["objects"]:
        lines.append(
            "| "
            f"`{item['boundary_id']}` | "
            f"`{item['profile']['profile_tuple']}` | "
            f"`{item['provenance']}` |"
        )

    lines.extend(
        [
            "",
            "## Transport Audit",
            "",
            "| Arrow | Source | Target | Verdict | Transported profile |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["transport_audits"]:
        transported = (
            None
            if audit["transported_profile"] is None
            else audit["transported_profile"]["profile_tuple"]
        )
        lines.append(
            "| "
            f"`{audit['arrow_id']}` | "
            f"`{audit['source']}` | "
            f"`{audit['target']}` | "
            f"`{audit['admissibility_verdict']}` | "
            f"`{transported}` |"
        )

    lines.extend(
        [
            "",
            "## Composition Audit",
            "",
            "| Composition | Arrows | Direct arrow | Verdict | Deltas preserved |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["composition_audits"]:
        lines.append(
            "| "
            f"`{audit['composition_id']}` | "
            f"`{audit['arrows']}` | "
            f"`{audit['direct_arrow']}` | "
            f"`{audit['admissibility_verdict']}` | "
            f"`{audit['deltas_preserved']}` |"
        )

    lines.extend(
        [
            "",
            "## Closed-Loop Audit",
            "",
            "| Loop | Arrows | Classification | Residual delta |",
            "| --- | --- | --- | --- |",
        ]
    )
    for audit in payload["loop_audits"]:
        lines.append(
            "| "
            f"`{audit['loop_id']}` | "
            f"`{audit['arrows']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['residual_boundary_delta']}` |"
        )

    lines.extend(
        [
            "",
            "## Verdict Checks",
            "",
            f"- Identity transports pass: `{payload['identity_passes']}`",
            f"- Pure gauge loops close: `{payload['pure_gauge_loops_close']}`",
            f"- Lossy loops report residual deltas: `{payload['lossy_loops_report_residual_delta']}`",
            f"- Hostile maps are undefined: `{payload['hostile_maps_undefined']}`",
            "",
            "## What Improved",
            "",
            str(payload["improved"]),
            "",
            "## What Weakened",
            "",
            str(payload["weakened"]),
            "",
            "## Falsification Condition",
            "",
            str(payload["falsification_condition"]),
            "",
            "## Claim Ledger Update",
            "",
            str(payload["claim_ledger_update"]),
            "",
            "## Open Blocker",
            "",
            str(payload["open_blocker"]),
            "",
            "## Suggested Next",
            "",
            str(payload["recommended_next"]),
            "",
            "## Reproduction",
            "",
            "```bash",
            "python -m unittest tests.test_d1_boundary_connection_transport -v",
            "python -m models.run_t125",
            "```",
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
