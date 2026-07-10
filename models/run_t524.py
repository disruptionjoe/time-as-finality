"""Runner for T524: T126 random-sprinkle diagnostic repair."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t524_t126_random_sprinkle_diagnostic_repair import (
    run_t524_analysis,
    t524_result_to_dict,
)


RESULTS_JSON = Path("results/T524-t126-random-sprinkle-diagnostic-repair-v0.1.json")
RESULTS_MD = Path("results/T524-t126-random-sprinkle-diagnostic-repair-v0.1-results.md")


def main() -> None:
    payload = t524_result_to_dict(run_t524_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.4f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T524 Results: T126 Random-Sprinkle Diagnostic Repair",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Artifact confirmed: `{payload['artifact_confirmed']}`",
        f"- Calibration control: `{payload['calibration_control_classification']}` "
        f"(passed={payload['calibration_control_passed']}, "
        f"ordering_fraction={_fraction(payload['calibration_control_ordering_fraction'])})",
        "",
        "## Comparison Target",
        "",
        f"- Target: `{payload['comparison_target']}`",
        f"- Basis: {payload['target_basis']}",
        "",
        "## Size Summary",
        "",
        (
            "| n | samples | T126 pass | order_dimension reject | other reject | "
            "T156 band pass | mean ordering fraction | mean gap from 1/2 | "
            "order-dim reject rate |"
        ),
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for summary in payload["size_summaries"]:
        lines.append(
            "| "
            f"{summary['event_count']} | "
            f"{summary['sample_count']} | "
            f"{summary['t126_pass_count']} | "
            f"{summary['order_dimension_obstruction_count']} | "
            f"{summary['other_obstruction_count']} | "
            f"{summary['t156_band_pass_count']} | "
            f"{_fraction(summary['mean_ordering_fraction'])} | "
            f"{_fraction(summary['mean_absolute_gap_from_half'])} | "
            f"{_fraction(summary['order_dimension_obstruction_rate'])} |"
        )

    lines.extend(
        [
            "",
            "## Repair Checks",
            "",
            "| Check | Result |",
            "| --- | :---: |",
            (
                "| Mean ordering-fraction gap decreases with size | "
                f"{payload['mean_ordering_gap_decreases_with_size']} |"
            ),
            (
                "| Order-dimension rejection rate increases with size | "
                f"{payload['order_dimension_rejection_rate_increases_with_size']} |"
            ),
            (
                "| All N>=16 samples rejected by order-dimension leg | "
                f"{payload['larger_sprinkles_all_order_dimension_rejected']} |"
            ),
            "",
            "## Per-Sample Audit",
            "",
            "| n | seed | ordering fraction | gap | T156 band | T126 classification | height | width |",
            "| ---: | ---: | ---: | ---: | :---: | --- | ---: | ---: |",
        ]
    )
    for audit in payload["sample_audits"]:
        lines.append(
            "| "
            f"{audit['event_count']} | "
            f"{audit['seed']} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"{_fraction(audit['absolute_gap_from_half'])} | "
            f"{audit['t156_band_passed']} | "
            f"`{audit['t126_classification']}` | "
            f"{audit['height']} | "
            f"{audit['width']} |"
        )

    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Rescoped", "weakened_or_rescoped"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
