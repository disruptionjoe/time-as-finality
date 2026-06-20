"""Write T123 same-payload packet FOA witness results."""

from __future__ import annotations

import json
from pathlib import Path

from models.same_payload_packet_foa_witness import (
    run_t123_analysis,
    t123_result_to_dict,
)


RESULTS_JSON = Path("results/same-payload-packet-foa-witness-v0.1.json")
RESULTS_MD = Path("results/same-payload-packet-foa-witness-v0.1-results.md")


def main() -> None:
    payload = t123_result_to_dict(run_t123_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T123 Results: Same-Payload Packet FOA Witness",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## Fixed measurement view",
        "",
        f"- Raw payload: `{payload['reference_view']['raw_payload']}`",
        f"- Measurement result: `{payload['reference_view']['measurement_result']}`",
        f"- Coarse detector summary: `{payload['reference_view']['coarse_detector_summary']}`",
        "",
        "## Packet variants",
        "",
        "| Packet | Changed packet fields | Verdict | Signature valid | Same raw/result/summary | Future operations | Removed vs reference |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        same_view = (
            audit["same_raw_payload"]
            and audit["same_measurement_result"]
            and audit["same_coarse_detector_summary"]
        )
        lines.append(
            "| "
            f"`{audit['packet_id']}` | "
            f"`{audit['changed_packet_fields']}` | "
            f"`{audit['packet_verdict']}` | "
            f"`{audit['signature_valid']}` | "
            f"`{same_view}` | "
            f"`{audit['future_operations']}` | "
            f"`{audit['operations_removed_vs_reference']}` |"
        )

    for heading, key in (
        ("What changed", "what_changed"),
        ("What did not change", "what_did_not_change"),
        ("Claim impact note", "claim_impact_note"),
        ("Falsification condition", "falsification_condition"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
        ("Claim ledger update", "claim_ledger_update"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
