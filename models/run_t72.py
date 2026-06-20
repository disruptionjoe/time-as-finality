"""Write T72 physical provenance protocol results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.physical_provenance_protocol import (
    run_t72_analysis,
    t72_result_to_dict,
)


RESULTS_JSON = Path("results/physical-provenance-protocol-v0.1.json")
RESULTS_MD = Path("results/physical-provenance-protocol-v0.1-results.md")


def main() -> None:
    result = run_t72_analysis()
    payload = t72_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    passive = payload["passive_statistics"]
    lines = [
        "# T72 Results: Physical Provenance Protocol",
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
        "## Regime table",
        "",
        "| Regime | Verdict | D1 computable | Threshold source |",
        "| --- | --- | --- | --- |",
    ]
    for row in payload["regime_table"]:
        lines.append(
            "| "
            f"{row['name']} | "
            f"{row['verdict']} | "
            f"{row['computable_d1']} | "
            f"{row['threshold_source']} |"
        )
    lines.extend(
        [
            "",
            "## Minimal physical conditions",
            "",
            payload["minimal_physical_conditions"],
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
