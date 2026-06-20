"""Write T108 prior-art absorption results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.loss_relocation_prior_art import run_t108_analysis, t108_result_to_dict


RESULTS_JSON = Path("results/loss-relocation-prior-art-v0.1.json")
RESULTS_MD = Path("results/loss-relocation-prior-art-v0.1-results.md")


def main() -> None:
    payload = t108_result_to_dict(run_t108_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T108 Results: Loss Relocation Prior-Art Audit",
        "",
        "## Aggregate Verdict",
        "",
        f"- Strict separation from all neighbors: {payload['strict_separation_from_all_neighbors']}",
        f"- Label-only loss refuted again: {payload['label_only_loss_refuted_again']}",
        "",
        "## Neighbor Audit",
        "",
        "| Neighbor | Verdict | Remaining delta |",
        "| --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"{audit['neighbor']} | "
            f"{audit['verdict']} | "
            f"{audit['remaining_delta']} |"
        )

    lines.extend(
        [
            "",
            "## Surviving Delta",
            "",
            payload["surviving_delta"],
            "",
            "## Strongest Claim",
            "",
            payload["strongest_claim"],
            "",
            "## What This Improved",
            "",
            payload["improved"],
            "",
            "## What This Weakened",
            "",
            payload["weakened"],
            "",
            "## Falsification Condition",
            "",
            payload["falsification_condition"],
            "",
            "## TF1 Update",
            "",
            payload["tf1_update"],
            "",
            "## Claim Ledger Update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Open Blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
