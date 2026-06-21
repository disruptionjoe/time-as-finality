"""Write T121 real detector packet schema audit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.real_detector_packet_schema_audit import (
    run_t121_analysis,
    t121_result_to_dict,
)


RESULTS_JSON = Path("results/real-detector-packet-schema-audit-v0.1.json")
RESULTS_MD = Path("results/real-detector-packet-schema-audit-v0.1-results.md")


def main() -> None:
    payload = t121_result_to_dict(run_t121_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T121 Results: Real Detector Packet Schema Audit",
        "",
        "## Schema fields",
        "",
        ", ".join(f"`{field}`" for field in payload["schema_fields"]),
        "",
        "## Packet cases",
        "",
        "| Packet | Raw payload valid | Verdict | Failures | Future operations | Missing schema requirements |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['packet_id']}` | "
            f"`{audit['raw_payload_valid']}` | "
            f"`{audit['packet_verdict']}` | "
            f"`{audit['admissibility_failures']}` | "
            f"`{audit['future_operations']}` | "
            f"`{audit['missing_schema_requirements_revealed']}` |"
        )

    sections = (
        ("Strongest claim", "strongest_claim"),
        ("Fields strictly necessary", "fields_strictly_necessary"),
        ("Failures changing admissibility", "failures_change_admissibility"),
        (
            "Failures changing future operation availability",
            "failures_change_future_operation_availability",
        ),
        (
            "Handled by existing protocol artifacts",
            "handled_by_existing_protocol_artifacts",
        ),
        ("Missing schema requirements", "missing_schema_requirements"),
        ("Claim impact recommendation", "claim_impact_recommendation"),
        ("Recommended next", "recommended_next"),
    )
    for heading, key in sections:
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
