"""Write T220 LossKernel witness-obligation factorization results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.losskernel_obligation_factorization import (
    run_t220_analysis,
    t220_result_to_dict,
)


RESULTS_JSON = Path("results/losskernel-obligation-factorization-v0.1.json")
RESULTS_MD = Path("results/losskernel-obligation-factorization-v0.1-results.md")


def main() -> None:
    payload = t220_result_to_dict(run_t220_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T220 Results: LossKernel Witness-Obligation Factorization",
        "",
        "## Aggregate checks",
        "",
        f"- Canonical factorization holds (obligation = psi . nu): {payload['canonical_factorization_holds']}",
        f"- Neighbor reconstruction matches obligation: {payload['neighbor_reconstruction_matches']}",
        (
            "- Same-neighbor-data separation impossible in canonical regime: "
            f"{payload['same_neighbor_separation_impossible_in_canonical_regime']}"
        ),
        f"- Strict same-neighbor-data separation found: {payload['strict_separation_found']}",
        f"- Hidden-source escape separates (non-factoring): {payload['hidden_escape_separates']}",
        (
            "- Hidden-source escape factors through neighbor: "
            f"{payload['hidden_escape_factors_through_neighbor']}"
        ),
        (
            "- Hidden-source escape is prior-art separation: "
            f"{payload['hidden_escape_is_prior_art_separation']}"
        ),
        f"- Verdict: {payload['verdict']}",
        "",
        "## Fiber-constancy certificate (fibers of nu)",
        "",
        "| Fiber | Cases | Obligation constant | Verdict constant | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for report in payload["fiber_reports"]:
        lines.append(
            "| "
            f"{report['signature_index']} | "
            f"{', '.join(report['case_names'])} | "
            f"{report['obligations_agree']} | "
            f"{report['verdicts_agree']} | "
            f"{report['verdict']} |"
        )

    lines.extend(
        [
            "",
            "## Pair probes",
            "",
            (
                "| Pair | Same neighbor data | Obligation diverges | "
                "Factors through nu | Classification |"
            ),
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for probe in payload["pair_probes"]:
        lines.append(
            "| "
            f"`{probe['pair_id']}` | "
            f"{probe['same_neighbor_data']} | "
            f"{probe['obligation_diverges']} | "
            f"{probe['obligation_factors_through_neighbor']} | "
            f"`{probe['classification']}` |"
        )

    for heading, key in (
        ("Strongest claim", "strongest_claim"),
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("TF1 update", "tf1_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
