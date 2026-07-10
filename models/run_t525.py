"""Runner for T525: repaired S1 manifoldlikeness suite."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t525_repaired_s1_manifoldlikeness_suite import (
    run_t525_analysis,
    t525_result_to_dict,
)


RESULTS_JSON = Path("results/T525-repaired-s1-manifoldlikeness-suite-v0.1.json")
RESULTS_MD = Path("results/T525-repaired-s1-manifoldlikeness-suite-v0.1-results.md")


def main() -> None:
    payload = t525_result_to_dict(run_t525_analysis())
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.4f})"


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T525 Results: Repaired S1 Manifoldlikeness Suite",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        (
            "- Random controls pass repaired suite: "
            f"`{payload['random_controls_pass_repaired_suite']}`"
        ),
        (
            "- Hard negative controls rejected: "
            f"`{payload['hard_negative_controls_rejected']}`"
        ),
        (
            "- Current finite colimit survivors: "
            f"{payload['current_finite_colimit_survivor_count']}"
        ),
        "",
        "## Calibration Bands",
        "",
        (
            "| n | samples | ordering min | ordering max | height | width | "
            "largest interval | order-dim count |"
        ),
        "| ---: | ---: | ---: | ---: | --- | --- | --- | ---: |",
    ]
    for band in payload["calibration_bands"]:
        lines.append(
            "| "
            f"{band['event_count']} | "
            f"{band['sample_count']} | "
            f"{_fraction(band['ordering_fraction_min'])} | "
            f"{_fraction(band['ordering_fraction_max'])} | "
            f"{band['height_min']}..{band['height_max']} | "
            f"{band['width_min']}..{band['width_max']} | "
            f"{band['largest_interval_min']}..{band['largest_interval_max']} | "
            f"{band['order_dimension_obstruction_count']} |"
        )

    lines.extend(
        [
            "",
            "## Candidate Audits",
            "",
            (
                "| candidate | group | n | T126 class | orderdim quarantined | "
                "frac | height | width | max interval | repaired verdict | reason |"
            ),
            "| --- | --- | ---: | --- | :---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for audit in payload["candidate_audits"]:
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['group']}` | "
            f"{audit['event_count']} | "
            f"`{audit['original_t126_classification']}` | "
            f"{audit['order_dimension_quarantined']} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"{audit['height']} | "
            f"{audit['width']} | "
            f"{audit['largest_interval_size']} | "
            f"`{audit['verdict']}` | "
            f"{audit['reason']} |"
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
