"""Write T99 LossKernel quotient-separation results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.losskernel_quotient_separation import (
    run_t99_analysis,
    t99_result_to_dict,
)


RESULTS_JSON = Path("results/losskernel-quotient-separation-v0.1.json")
RESULTS_MD = Path("results/losskernel-quotient-separation-v0.1-results.md")


def main() -> None:
    payload = t99_result_to_dict(run_t99_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T99 Results: LossKernel Quotient Separation",
        "",
        "## Cases",
        "",
        "| Case | Family | Naive labels | Verdict | Purpose |",
        "| --- | --- | --- | --- | --- |",
    ]
    for case in payload["cases"]:
        labels = ", ".join(case["naive_loss_labels"]) or "none"
        lines.append(
            "| "
            f"{case['name']} | "
            f"{case['family']} | "
            f"{labels} | "
            f"{case['attribution_verdict']} | "
            f"{case['purpose']} |"
        )

    lines.extend(
        [
            "",
            "## Naive quotient groups",
            "",
            "| Group | Cases | Verdicts | Naive collision | Typed witness separates |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for group in payload["quotient_groups"]:
        lines.append(
            "| "
            f"{group['group_id']} | "
            f"{', '.join(group['case_names'])} | "
            f"{', '.join(group['verdicts'])} | "
            f"{group['naive_collision']} | "
            f"{group['typed_witness_separates']} |"
        )

    lines.extend(
        [
            "",
            "## Audit flags",
            "",
            f"- Naive label kernel fails quotient gate: {payload['naive_label_kernel_fails_quotient_gate']}",
            f"- Typed witness kernel separates collision: {payload['typed_witness_kernel_separates_collision']}",
            f"- Same-typed control collapses: {payload['same_typed_control_collapses']}",
            f"- Endpoint-difference control excluded: {payload['endpoint_difference_control_excluded']}",
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
            "## TF1 update",
            "",
            payload["tf1_update"],
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
