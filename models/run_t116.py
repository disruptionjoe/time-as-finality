"""Write T116 open Markov record-entropy comparison results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.open_markov_record_entropy import (
    run_t116_analysis,
    t116_result_to_dict,
)


RESULTS_JSON = Path("results/open-markov-record-entropy-v0.1.json")
RESULTS_MD = Path("results/open-markov-record-entropy-v0.1-results.md")


def main() -> None:
    payload = t116_result_to_dict(run_t116_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    scenario_keys = (
        "detailed_balance_control",
        "nonequilibrium_cycle_control",
        "open_export_recorder",
        "reversible_append_only_control",
    )
    lines = [
        "# T116 Results: Open Markov Record-Entropy Comparison",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## Scenario table",
        "",
        "| Scenario | Accounted score | Irreversibility nats | Exported | Fresh capacity used | Classification |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for key in scenario_keys:
        scenario = payload[key]
        lines.append(
            "| "
            f"{scenario['name']} | "
            f"`{scenario['accounted_score_sequence']}` | "
            f"{scenario['total_irreversibility_nats']:.6f} | "
            f"{scenario['exported_records_added']} | "
            f"{scenario['fresh_capacity_consumed']} | "
            f"`{scenario['classification']}` |"
        )

    for key in scenario_keys:
        scenario = payload[key]
        lines.extend(
            [
                "",
                f"## {scenario['name']}",
                "",
                f"- Local score sequence: `{scenario['local_score_sequence']}`",
                f"- Accounted score sequence: `{scenario['accounted_score_sequence']}`",
                f"- Local nondecreasing: `{scenario['local_nondecreasing']}`",
                f"- Accounted nondecreasing: `{scenario['accounted_nondecreasing']}`",
                f"- Strict accounted increases: `{scenario['accounted_strict_increase_edges']}`",
                f"- Total path irreversibility: `{scenario['total_irreversibility_nats']:.6f}` nats",
                f"- Exported records added: `{scenario['exported_records_added']}`",
                f"- Fresh capacity consumed: `{scenario['fresh_capacity_consumed']}`",
                f"- Candidate independent H7 arrow: `{scenario['candidate_independent_h7_arrow']}`",
                "",
                scenario["verdict"],
            ]
        )

    lines.extend(
        [
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
            "## H7 update",
            "",
            payload["h7_update"],
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
