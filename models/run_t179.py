"""Write T179 fixed-accounting capability topology results."""

from __future__ import annotations

import json
from pathlib import Path

from models.fixed_accounting_capability_topology import (
    run_t179_analysis,
    t179_result_to_dict,
)


RESULTS_JSON = Path("results/fixed-accounting-capability-topology-v0.1.json")
RESULTS_MD = Path("results/fixed-accounting-capability-topology-v0.1-results.md")


def main() -> None:
    payload = t179_result_to_dict(run_t179_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T179 Results: Fixed-Accounting Capability Topology",
        "",
        "## Theorem Candidate",
        "",
        str(payload["theorem_candidate"]),
        "",
        "## Audit Table",
        "",
        "| Case | Accounting matched | Topology split | Capability split | H7 candidate | Verdict |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['case_id']}` | "
            f"`{audit['absorber_vector_matched']}` | "
            f"`{audit['topology_profile_split']}` | "
            f"`{audit['future_capability_split']}` | "
            f"`{audit['h7_physical_arrow_candidate']}` | "
            f"`{audit['verdict']}` |"
        )

    lines.extend(
        [
            "",
            "## Residue Cases",
            "",
            _bullet_list(payload["residue_cases"]),
            "",
            "## H7 Candidates",
            "",
            _bullet_list(payload["h7_candidates"]),
        ]
    )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Falsification Condition", "falsification_condition"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def _bullet_list(items: object) -> str:
    if not items:
        return "None."
    return "\n".join(f"- `{item}`" for item in items)


if __name__ == "__main__":
    main()
