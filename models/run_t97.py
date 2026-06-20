"""Write T97 detector dry-run packet skeleton results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_dry_run_packet_skeleton import (
    locked_detector_dry_run_packet_skeleton,
    packet_manifest_to_dict,
    run_t97_analysis,
    t97_result_to_dict,
)


RESULTS_JSON = Path("results/detector-dry-run-packet-skeleton-v0.1.json")
RESULTS_MD = Path("results/detector-dry-run-packet-skeleton-v0.1-results.md")


def main() -> None:
    result = run_t97_analysis()
    payload = t97_result_to_dict(result)
    payload["locked_packet_manifest"] = packet_manifest_to_dict(
        locked_detector_dry_run_packet_skeleton()
    )
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T97 Results: Detector Dry-Run Packet Skeleton",
        "",
        "## Audit table",
        "",
        "| Packet | Verdict | Evidence verdict | Failures | T87 verdict now | T87 failures now | Next step |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        failures = ", ".join(audit["failure_reasons"]) or "none"
        t87_failures = (
            ", ".join(audit["t87_failure_reasons_if_scored_now"]) or "none"
        )
        lines.append(
            "| "
            f"{audit['packet_name']} | "
            f"{audit['verdict']} | "
            f"{audit['evidence_verdict']} | "
            f"{failures} | "
            f"{audit['t87_verdict_if_scored_now']} | "
            f"{t87_failures} | "
            f"{audit['next_allowed_step']} |"
        )

    manifest = payload["locked_packet_manifest"]
    lines.extend(
        [
            "",
            "## Locked packet manifest",
            "",
            f"Packet: `{manifest['name']}`",
            "",
            f"Run id: `{manifest['run_id']}`",
            "",
            f"Manifest hash: `{manifest['manifest_hash']}`",
            "",
            "## Frozen table files",
            "",
            "| Table | File | Join keys | Planned rows | Real rows present |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for table in manifest["tables"]:
        lines.append(
            "| "
            f"{table['table_name']} | "
            f"{table['file_name']} | "
            f"{', '.join(table['join_keys'])} | "
            f"{table['min_planned_rows']} | "
            f"{table['real_rows_present']} |"
        )

    lines.extend(
        [
            "",
            "## Strongest claim",
            "",
            payload["strongest_claim"],
            "",
            "## What this improved",
            "",
            payload["improved"],
            "",
            "## What this weakened",
            "",
            payload["weakened"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Q1 update",
            "",
            payload["q1_update"],
            "",
            "## Claim ledger update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
