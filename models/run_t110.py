"""Write T110 finite-permutation monotone-obstruction results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.finite_permutation_monotone_obstruction import (
    run_t110_analysis,
    t110_result_to_dict,
)


RESULTS_JSON = Path("results/finite-permutation-monotone-obstruction-v0.1.json")
RESULTS_MD = Path("results/finite-permutation-monotone-obstruction-v0.1-results.md")


def main() -> None:
    payload = t110_result_to_dict(run_t110_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    t106 = payload["t106_closed_cycle_audit"]
    plateau = payload["plateau_control_audit"]
    open_branch = payload["open_branch_control"]

    lines = [
        "# T110 Results: Finite-Permutation Monotone Obstruction",
        "",
        "## Strongest claim",
        "",
        payload["strongest_claim"],
        "",
        "## Closed T106 cycle",
        "",
        (
            "- Score sequence: "
            f"`{t106['orbit_audits'][0]['score_sequence']}`"
        ),
        f"- Edge deltas: `{t106['orbit_audits'][0]['edge_deltas']}`",
        f"- Nondecreasing on all edges: `{t106['nondecreasing_on_all_edges']}`",
        f"- Has strict increase: `{t106['has_strict_increase']}`",
        f"- Has decrease: `{t106['has_decrease']}`",
        f"- Strict nondecreasing possible: `{t106['strict_nondecreasing_possible']}`",
        "",
        t106["verdict"],
        "",
        "## Plateau control",
        "",
        f"- Nondecreasing on all edges: `{plateau['nondecreasing_on_all_edges']}`",
        f"- Constant on each orbit: `{plateau['constant_on_each_orbit']}`",
        f"- Verdict: {plateau['verdict']}",
        "",
        "## Exhaustive finite-cycle check",
        "",
        "| Cycle length | Assignments | Nondecreasing | Constant | Strict without decrease | Theorem holds |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for check in payload["exhaustive_cycle_checks"]:
        lines.append(
            "| "
            f"{check['cycle_length']} | "
            f"{check['assignment_count']} | "
            f"{check['nondecreasing_assignments']} | "
            f"{check['constant_assignments']} | "
            f"{check['strict_without_decrease_assignments']} | "
            f"{check['theorem_holds']} |"
        )

    lines.extend(
        [
            "",
            "## Open-branch control",
            "",
            f"- Score sequence: `{open_branch['score_sequence']}`",
            f"- Nondecreasing: `{open_branch['nondecreasing']}`",
            f"- Strict increases: `{open_branch['strict_increase_edges']}`",
            f"- Closed reversible system: `{open_branch['reversible_closed_system']}`",
            "",
            open_branch["verdict"],
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
