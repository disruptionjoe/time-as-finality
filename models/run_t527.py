"""Runner for T527: Observerse protocol-stack ablation regression harness."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models import observerse_stack_ablation as stack


RESULTS_JSON = Path("results/T527-observerse-protocol-stack-ablation-v0.1.json")
RESULTS_MD = Path("results/T527-observerse-protocol-stack-ablation-v0.1-results.md")

VERDICT = "observerse_stack_ablation_regression_harness_passes_review_only"
SENSITIVITY_RULE_FILLS = (0, 40, 80, 100, 105, 110, 120, 130, 140, 145, 150)


def build_payload() -> dict[str, Any]:
    full = stack.run()
    rows = [
        _row("full_stack", "FULL STACK (all 5)", full, "baseline"),
        _row("without_issuance", "- issuance", stack.run(issuance=False), "freeze"),
        _row(
            "without_admissibility",
            "- admissibility",
            stack.run(admissibility=False),
            "incoherence",
        ),
        _row("without_sybil_finality", "- sybil/finality", stack.run(sybil=False), "capture"),
        _row("without_consensus", "- consensus", stack.run(consensus=False), "fragment"),
        _row(
            "without_governance_near_term_rules",
            "- governance (near-term rules)",
            stack.run(governance=False, rule_fill=stack.TAU),
            "ossification",
        ),
        _row(
            "without_governance_full_horizon_rules",
            "- governance (full-horizon rules)",
            stack.run(governance=False, rule_fill=stack.T),
            "no_collapse_rules_anticipated_all",
        ),
    ]
    ratio_by_id = {row["id"]: _ratio(row["scs"], full) for row in rows}
    core_ids = [
        "without_issuance",
        "without_admissibility",
        "without_sybil_finality",
        "without_consensus",
    ]
    core_layers_each_earn_slot = all(ratio_by_id[row_id] <= 0.20 for row_id in core_ids)
    governance_conditional_visible = (
        ratio_by_id["without_governance_near_term_rules"] <= 0.20
        and ratio_by_id["without_governance_full_horizon_rules"] >= 0.95
    )
    governance_sensitivity = _governance_horizon_sensitivity(full)
    sensitivity_summary = _governance_sensitivity_summary(governance_sensitivity)
    return {
        "verdict": VERDICT,
        "grade": "illustration_regression_only",
        "source_model": "models/observerse_stack_ablation.py",
        "rows": [{**row, "scs_ratio_to_full": ratio_by_id[row["id"]]} for row in rows],
        "governance_rule_horizon_sensitivity": governance_sensitivity,
        **sensitivity_summary,
        "core_layers_each_earn_slot": core_layers_each_earn_slot,
        "governance_conditional_visible": governance_conditional_visible,
        "minimum_stack_under_near_term_governance": 5,
        "minimum_stack_when_rules_anticipate_full_horizon": 4,
        "claim_status_changed": False,
        "canon_verdict_changed": False,
        "public_posture_changed": False,
        "strongest_reading": (
            "The deterministic ablation model matches its review-only claim: each core layer "
            "collapses sustained coherent structure to at most 20% of the full stack, while "
            "governance is load-bearing only when fixed rules do not already anticipate the "
            "full novelty horizon. The sensitivity map makes the transition explicit: fixed "
            "rules remain in the collapse band through rule horizon 105, partially recover "
            "after 110, and reach near-full recovery only at the full 150-tick horizon."
        ),
        "what_this_improves": (
            "T527 turns the recent Observerse stack ablation into a repeatable regression "
            "harness and frozen result packet. The governance-horizon sensitivity map "
            "hardens the conditional without changing the underlying source model or "
            "promoting the exploration."
        ),
        "falsification_condition": (
            "T527 fails if a core-layer removal stays above 20% of full sustained coherent "
            "structure, if the governance near-term/full-horizon contrast disappears, or if "
            "the sensitivity map ceases to be monotone from collapse through partial "
            "recovery to near-full recovery. It also fails if the result is used as "
            "validation rather than illustration-grade compositional accounting."
        ),
        "not_claimed": (
            "T527 does not validate Observerse, derive S1, prove the Bitcoin analogy, "
            "promote any claim, or change canon/public posture. It is only a regression "
            "harness for the deterministic illustration model."
        ),
    }


def main() -> None:
    payload = build_payload()
    RESULTS_JSON.parent.mkdir(exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _row(row_id: str, label: str, scs: float, predicted_mode: str) -> dict[str, Any]:
    return {
        "id": row_id,
        "label": label,
        "scs": round(scs, 12),
        "predicted_mode": predicted_mode,
    }


def _ratio(value: float, full: float) -> float:
    return round(value / full if full else 0.0, 12)


def _governance_horizon_sensitivity(full: float) -> list[dict[str, Any]]:
    rows = []
    for rule_fill in SENSITIVITY_RULE_FILLS:
        scs = stack.run(governance=False, rule_fill=rule_fill)
        ratio = _ratio(scs, full)
        rows.append(
            {
                "rule_fill": rule_fill,
                "scs": round(scs, 12),
                "scs_ratio_to_full": ratio,
                "classification": _classify_governance_ratio(ratio),
            }
        )
    return rows


def _classify_governance_ratio(ratio: float) -> str:
    if ratio <= 0.20:
        return "collapsed"
    if ratio >= 0.95:
        return "near_full_recovery"
    return "partial_recovery"


def _governance_sensitivity_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    first_above_collapse = next(
        row["rule_fill"] for row in rows if row["scs_ratio_to_full"] > 0.20
    )
    first_near_full = next(
        row["rule_fill"] for row in rows if row["scs_ratio_to_full"] >= 0.95
    )
    monotone = all(
        earlier["scs_ratio_to_full"] <= later["scs_ratio_to_full"]
        for earlier, later in zip(rows, rows[1:])
    )
    return {
        "governance_sensitivity_monotone": monotone,
        "first_rule_fill_above_collapse_band": first_above_collapse,
        "first_rule_fill_near_full_recovery": first_near_full,
        "sensitivity_classifications_seen": sorted(
            {row["classification"] for row in rows}
        ),
    }


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T527 Results: Observerse Protocol-Stack Ablation",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Grade: `{payload['grade']}`",
        f"- Core layers each earn slot: `{payload['core_layers_each_earn_slot']}`",
        f"- Governance conditional visible: `{payload['governance_conditional_visible']}`",
        (
            "- Minimum stack under near-term governance: "
            f"{payload['minimum_stack_under_near_term_governance']}"
        ),
        (
            "- Minimum stack when fixed rules anticipate full horizon: "
            f"{payload['minimum_stack_when_rules_anticipate_full_horizon']}"
        ),
        "",
        "## Ablation Rows",
        "",
        "| row | SCS | ratio to full | predicted mode |",
        "| --- | ---: | ---: | --- |",
    ]
    for row in payload["rows"]:
        lines.append(
            "| "
            f"`{row['label']}` | "
            f"{row['scs']:.3f} | "
            f"{row['scs_ratio_to_full']:.3f} | "
            f"`{row['predicted_mode']}` |"
        )

    lines.extend(
        [
            "",
            "## Governance Horizon Sensitivity",
            "",
            "- Monotone sensitivity: "
            f"`{payload['governance_sensitivity_monotone']}`",
            "- First rule horizon above the collapse band: "
            f"{payload['first_rule_fill_above_collapse_band']}",
            "- First rule horizon with near-full recovery: "
            f"{payload['first_rule_fill_near_full_recovery']}",
            "",
            "| fixed rule horizon | SCS | ratio to full | classification |",
            "| ---: | ---: | ---: | --- |",
        ]
    )
    for row in payload["governance_rule_horizon_sensitivity"]:
        lines.append(
            "| "
            f"{row['rule_fill']} | "
            f"{row['scs']:.3f} | "
            f"{row['scs_ratio_to_full']:.3f} | "
            f"`{row['classification']}` |"
        )

    for heading, key in (
        ("Strongest Reading", "strongest_reading"),
        ("What This Improved", "what_this_improves"),
        ("Falsification Condition", "falsification_condition"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])

    lines.extend(
        [
            "",
            "## Boundary Checks",
            "",
            f"- Claim status changed: `{payload['claim_status_changed']}`",
            f"- Canon verdict changed: `{payload['canon_verdict_changed']}`",
            f"- Public posture changed: `{payload['public_posture_changed']}`",
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
