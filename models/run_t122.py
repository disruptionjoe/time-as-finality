"""Write T122 stationary Markov monotone obstruction results."""

from __future__ import annotations

import json
from pathlib import Path

from models.stationary_markov_monotone_obstruction import (
    run_t122_analysis,
    t122_result_to_dict,
)


RESULTS_JSON = Path("results/stationary-markov-monotone-obstruction-v0.1.json")
RESULTS_MD = Path("results/stationary-markov-monotone-obstruction-v0.1-results.md")


def main() -> None:
    payload = t122_result_to_dict(run_t122_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    scenario_keys = (
        "detailed_balance_control",
        "biased_cycle_control",
        "absorbing_append_control",
    )
    lines = [
        "# T122 Results: Stationary Markov Monotone Obstruction",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## Scenario table",
        "",
        "| Scenario | Score | Stationary support | Drift | Weighted drift | Classification |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for key in scenario_keys:
        audit = payload[key]
        lines.append(
            "| "
            f"`{audit['name']}` | "
            f"`{audit['score']}` | "
            f"`{audit['stationary_support']}` | "
            f"`{audit['drift_by_state']}` | "
            f"{audit['stationary_weighted_drift']:.12f} | "
            f"`{audit['classification']}` |"
        )

    lines.extend(
        [
            "",
            "## Deterministic finite-map sanity checks",
            "",
            "| States | Transitions checked | Score assignments each | Recurrent strict monotones | All-state nondecreasing | Transient-only strict | Theorem holds |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for check in payload["deterministic_function_checks"]:
        lines.append(
            "| "
            f"{check['state_count']} | "
            f"{check['transition_count']} | "
            f"{check['score_assignment_count']} | "
            f"{check['recurrent_strict_monotone_assignments']} | "
            f"{check['all_state_nondecreasing_assignments']} | "
            f"{check['transient_only_strict_assignments']} | "
            f"`{check['theorem_holds']}` |"
        )

    sections = (
        ("What this improved", "improved"),
        ("What this weakened", "weakened"),
        ("Falsification condition", "falsification_condition"),
        ("H7 update", "h7_update"),
        ("Claim ledger update", "claim_ledger_update"),
        ("Open blocker", "open_blocker"),
        ("Recommended next", "recommended_next"),
    )
    for heading, key in sections:
        lines.extend(["", f"## {heading}", "", payload[key]])
    lines.append("")
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
