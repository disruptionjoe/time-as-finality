"""Write T136 detector pre-registration manifest results."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_preregistration_manifest import (
    run_t136_analysis,
    t136_result_to_dict,
)


RESULTS_JSON = Path("results/detector-preregistration-manifest-v0.1.json")
RESULTS_MD = Path("results/detector-preregistration-manifest-v0.1-results.md")


def main() -> None:
    payload = t136_result_to_dict(run_t136_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T136 Results: Detector Pre-registration Manifest",
        "",
        "## Manifest requirements",
        "",
        f"- T97 tables: `{payload['required_t97_tables']}`",
        f"- Provisional fields: `{payload['provisional_commitment_fields']}`",
        f"- Claim-review fields: `{payload['claim_review_commitment_fields']}`",
        "",
        "## Manifest audits",
        "",
        "| Manifest | Claimed tier | Max tier | Claimed admissible | T97 valid | Wrapper valid | Authority valid | Predata valid | Hash valid | Failures |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        failures = ", ".join(audit["failure_reasons"]) or "none"
        lines.append(
            "| "
            f"`{audit['manifest_name']}` | "
            f"`{audit['claimed_tier']}` | "
            f"`{audit['max_certifiable_tier']}` | "
            f"`{audit['claimed_tier_admissible']}` | "
            f"`{audit['t97_table_commitments_valid']}` | "
            f"`{audit['wrapper_commitments_valid']}` | "
            f"`{audit['authority_partition_admissible']}` | "
            f"`{audit['predata_boundary_respected']}` | "
            f"`{audit['manifest_hash_valid']}` | "
            f"`{failures}` |"
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
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
