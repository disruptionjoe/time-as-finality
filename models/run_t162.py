"""Write T162 Q1A SBS closure-key obstruction results."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_sbs_factorization_obstruction import (
    run_t162_analysis,
    t162_result_to_dict,
)


RESULTS_JSON = Path("results/q1a-sbs-factorization-obstruction-v0.1.json")
RESULTS_MD = Path("results/q1a-sbs-factorization-obstruction-v0.1-results.md")


def main() -> None:
    payload = t162_result_to_dict(run_t162_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T162 Results: Q1A SBS Factorization Obstruction",
        "",
        "## Aggregate checks",
        "",
        f"- Visible enumeration cases: {payload['visible_case_count']}",
        (
            "- D1 factors through SBS closure key: "
            f"{payload['d1_factors_through_sbs_closure_key']}"
        ),
        (
            "- Same full SBS-data split found: "
            f"{payload['same_full_sbs_data_split_found']}"
        ),
        (
            "- Raw redundancy is not sufficient: "
            f"{payload['raw_redundancy_is_not_sufficient']}"
        ),
        (
            "- Objectivity failures withhold: "
            f"{payload['objectivity_failures_withhold']}"
        ),
        f"- Hidden partition withholds: {payload['hidden_partition_withholds']}",
        (
            "- Nontrivial same-key variants exist: "
            f"{payload['nontrivial_same_key_variants_exist']}"
        ),
        (
            "- Current family has no same-SBS split: "
            f"{payload['q1a_current_family_has_no_same_sbs_split']}"
        ),
        "",
        "## Closure fibers",
        "",
        "| Closure key | Cases | D1 verdicts | Raw redundancies | Partitions |",
        "| --- | ---: | --- | --- | --- |",
    ]

    for fiber in payload["fibers"]:
        lines.append(
            "| "
            f"{fiber['sbs_closure_key']} | "
            f"{fiber['case_count']} | "
            f"{fiber['d1_verdicts']} | "
            f"{fiber['raw_redundancies']} | "
            f"{len(fiber['partition_signatures'])} signatures |"
        )

    hidden = payload["hidden_partition_case"]
    lines.extend(
        [
            "",
            "## Hidden partition control",
            "",
            f"- Case: {hidden['case_id']}",
            f"- SBS verdict: {hidden['sbs_objectivity_verdict']}",
            f"- D1 verdict: {hidden['d1_verdict']}",
            "",
            "## Objectivity failure controls",
            "",
            "| Case | SBS verdict | D1 verdict |",
            "| --- | --- | --- |",
        ]
    )
    for control in payload["objectivity_failure_controls"]:
        lines.append(
            "| "
            f"{control['case_id']} | "
            f"{control['sbs_objectivity_verdict']} | "
            f"{control['d1_verdict']} |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("Q1A update", "q1a_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
