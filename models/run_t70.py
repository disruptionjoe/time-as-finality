"""Write T70 detector provenance robustness results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.detector_provenance_robustness import (
    run_t70_analysis,
    t70_result_to_dict,
)


RESULTS_JSON = Path("results/detector-provenance-robustness-v0.1.json")
RESULTS_MD = Path("results/detector-provenance-robustness-v0.1-results.md")


def main() -> None:
    result = run_t70_analysis()
    payload = t70_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    passive = payload["passive_statistics"]
    lines = [
        "# T70 Results: Detector Provenance Robustness",
        "",
        (
            "Passive statistics held fixed: agreement "
            f"{passive['agreement_probability']}; phi {passive['phi_correlation']}."
        ),
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Robustness table",
        "",
        (
            "| Regime | Verdict | Metadata used | Copied status | "
            "Independent status |"
        ),
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["robustness_table"]:
        metadata = ", ".join(row["minimal_metadata_used"]) or "none"
        lines.append(
            "| "
            f"{row['name']} | "
            f"{row['verdict']} | "
            f"{metadata} | "
            f"{row['copied_status']} | "
            f"{row['independent_status']} |"
        )
    lines.extend(
        [
            "",
            "## Minimal metadata requirement",
            "",
            payload["minimal_metadata_requirement"],
            "",
            "## Q1 recommendation",
            "",
            payload["q1_recommendation"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()


