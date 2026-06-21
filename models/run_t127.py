"""Write T127 same-neighbor-data LossKernel audit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.same_neighbor_data_losskernel_audit import (
    run_t127_analysis,
    t127_result_to_dict,
)


RESULTS_JSON = Path("results/same-neighbor-data-losskernel-audit-v0.1.json")
RESULTS_MD = Path("results/same-neighbor-data-losskernel-audit-v0.1-results.md")


def main() -> None:
    payload = t127_result_to_dict(run_t127_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T127 Results: Same-Neighbor-Data LossKernel Audit",
        "",
        "## Aggregate checks",
        "",
        f"- Strict separation found: {payload['strict_separation_found']}",
        f"- Positive attempt absorbed: {payload['positive_attempt_absorbed']}",
        f"- Label-only control collapses: {payload['label_only_control_collapses']}",
        f"- Endpoint-difference control rejected: {payload['endpoint_difference_control_rejected']}",
        f"- Path-metadata control rejected: {payload['path_metadata_control_rejected']}",
        f"- Same-neighbor alias collapses: {payload['same_neighbor_alias_collapses']}",
        f"- Absorbed-loss control demoted: {payload['absorbed_loss_control_demoted']}",
        "",
        "## Pair audits",
        "",
        (
            "| Pair | Classification | Same neighbor data | Left verdict | "
            "Right verdict | First absorber |"
        ),
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for audit in payload["pair_audits"]:
        lines.append(
            "| "
            f"`{audit['pair_id']}` | "
            f"`{audit['classification']}` | "
            f"`{audit['same_neighbor_data']}` | "
            f"`{audit['left_verdict']}` | "
            f"`{audit['right_verdict']}` | "
            f"`{audit['first_absorber']}` |"
        )

    for audit in payload["pair_audits"]:
        lines.extend(
            [
                "",
                f"## Pair: {audit['pair_id']}",
                "",
                f"- Left case: `{audit['left_case']}`",
                f"- Right case: `{audit['right_case']}`",
                f"- Classification: `{audit['classification']}`",
                f"- Same neighbor data: `{audit['same_neighbor_data']}`",
                f"- Differing neighbor fields: `{audit['differing_neighbor_fields']}`",
                f"- First absorber: `{audit['first_absorber']}`",
                f"- Left obligation: `{audit['left_obligation']}`",
                f"- Right obligation: `{audit['right_obligation']}`",
                f"- Interpretation: {audit['interpretation']}",
            ]
        )

    lines.extend(["", "## Single-case audits", ""])
    for audit in payload["single_case_audits"]:
        lines.extend(
            [
                f"### {audit['case_name']}",
                "",
                f"- Classification: `{audit['classification']}`",
                f"- Verdict: `{audit['verdict']}`",
                f"- Obligation: `{audit['obligation']}`",
                f"- Interpretation: {audit['interpretation']}",
                "",
            ]
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
    return "\n".join(lines)


if __name__ == "__main__":
    main()

