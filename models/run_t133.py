"""Write T133 detector packet tiered minimality results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_packet_tiered_minimality import (
    run_t133_analysis,
    t133_result_to_dict,
)


RESULTS_JSON = Path("results/detector-packet-tiered-minimality-v0.1.json")
RESULTS_MD = Path("results/detector-packet-tiered-minimality-v0.1-results.md")


def main() -> None:
    payload = t133_result_to_dict(run_t133_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T133 Results: Detector Packet Tiered Minimality",
        "",
        "## Tier cores",
        "",
        f"- Raw identity fields: `{payload['raw_identity_fields']}`",
        f"- Provisional admission fields: `{payload['provisional_admission_fields']}`",
        f"- Claim-review extension fields: `{payload['claim_review_extension_fields']}`",
        "",
        "## Packet audits",
        "",
        "| Packet | Changed fields | Raw preserved | Provisionally admissible | Claim-review ready | Strict T121 verdict | Strict-only fields triggered |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['packet_id']}` | "
            f"`{audit['changed_packet_fields']}` | "
            f"`{audit['raw_evidence_preserved']}` | "
            f"`{audit['provisionally_admissible']}` | "
            f"`{audit['claim_review_ready']}` | "
            f"`{audit['strict_t121_verdict']}` | "
            f"`{audit['strict_only_fields_triggered']}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("Weakened claim", "weakened_claim"),
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
