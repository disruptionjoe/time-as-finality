"""Write T128 minimal living arrow results."""

from __future__ import annotations

import json
from pathlib import Path

from models.minimal_living_arrow import run_t128_analysis, t128_result_to_dict


RESULTS_JSON = Path("results/minimal-living-arrow-v0.1.json")
RESULTS_MD = Path("results/minimal-living-arrow-v0.1-results.md")


def main() -> None:
    payload = t128_result_to_dict(run_t128_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T128 Results: Minimal Living Arrow",
        "",
        "## Summary",
        "",
        f"- Strongest surviving minimal model: `{payload['strongest_surviving_minimal_model']}`",
        f"- Strongest failed model: `{payload['strongest_failed_model']}`",
        f"- Smallest formal ingredient set: {payload['smallest_formal_ingredient_set']}",
        f"- Smallest non-stipulative ingredient set: {payload['smallest_nonstipulative_ingredient_set']}",
        "",
        "## Model Audits",
        "",
        "| Model | Ingredient | Direction survives | T122 assumptions violated | Verdict |",
        "| --- | --- | --- | --- | --- |",
    ]
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"`{audit['model_id']}` | "
            f"{audit['ingredient']} | "
            f"`{audit['direction_survives']}` | "
            f"`{audit['t122_assumptions_violated']}` | "
            f"{audit['verdict']} |"
        )

    for audit in payload["audits"]:
        lines.extend(
            [
                "",
                f"## {audit['name']}",
                "",
                f"- State space: `{audit['state_names']}`",
                f"- Transition rules: `{audit['transition_rules']}`",
                f"- Resource accounting: {audit['resource_accounting']}",
                f"- Direction candidate: {audit['direction_candidate']}",
                f"- Direction values: `{audit['direction_values']}`",
                f"- Future operation sizes: `{audit['future_operation_sizes']}`",
                f"- Obstruction status: {audit['obstruction_status']}",
                f"- T122 assumptions violated: `{audit['t122_assumptions_violated']}`",
                f"- Direction survives: `{audit['direction_survives']}`",
                f"- Equivalence note: {audit['equivalence_note']}",
            ]
        )

    for heading, key in (
        ("What Improved", "improved"),
        ("What Weakened", "weakened"),
        ("Claim Impact Recommendation", "claim_impact_recommendation"),
        ("Open Blocker", "open_blocker"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Suggested Next", "suggested_next"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
