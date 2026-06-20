"""Write consensus parametric tradeoff results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.consensus_parametric_tradeoff import (
    consensus_parametric_tradeoff_result_to_dict,
    run_consensus_parametric_tradeoff_analysis,
)


RESULTS_JSON = Path("results/consensus-parametric-tradeoff-v0.1.json")
RESULTS_MD = Path("results/consensus-parametric-tradeoff-v0.1-results.md")


def main() -> None:
    result = run_consensus_parametric_tradeoff_analysis()
    payload = consensus_parametric_tradeoff_result_to_dict(result)
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    surface = payload["surface"]
    conditions = payload["minimal_conditions"]
    degenerate = conditions["minimal_degenerate_failure"]
    saturated = conditions["minimal_saturated_failure"]
    collapse = conditions["minimal_collapse_failure"]
    canonical = _find_point(payload["regime_table"], 10, 2)

    lines = [
        "# T71 Results: Consensus Parametric Tradeoff",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Parameter surface",
        "",
        (
            f"- caps: nodes <= {surface['max_nodes']}, "
            f"branches <= {surface['max_branches']}, "
            f"confirmations <= {surface['max_confirmations']}, "
            f"timeout <= {surface['max_timeout']}"
        ),
        (
            f"- grid: budget {surface['min_budget']}..{surface['max_budget']}; "
            "adversarial_delay "
            f"{surface['min_adversarial_delay']}.."
            f"{surface['max_adversarial_delay']}"
        ),
        "",
        "## Regime counts",
        "",
    ]
    for regime, count in payload["regime_counts"].items():
        lines.append(f"- {regime}: {count}")

    lines.extend(
        [
            "",
            "## Canonical point",
            "",
            _point_line(canonical),
            "",
            "## Minimal failures",
            "",
            f"- degenerate: {_point_line(degenerate)}",
            f"- saturated: {_point_line(saturated)}",
            (
                "- collapse / no-tradeoff: none observed"
                if collapse is None
                else f"- collapse / no-tradeoff: {_point_line(collapse)}"
            ),
            "",
            "## Preserved tradeoff windows",
            "",
        ]
    )
    for window in conditions["preserved_tradeoff_windows"]:
        lines.append(
            "- delay={delay}: budget {start}..{end} ({regime})".format(
                delay=window["adversarial_delay"],
                start=window["start_budget"],
                end=window["end_budget"],
                regime=window["regime"],
            )
        )

    lines.extend(
        [
            "",
            "## Recommendation",
            "",
            conditions["recommendation"],
            "",
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


def _find_point(
    table: list[dict[str, object]],
    budget: int,
    adversarial_delay: int,
) -> dict[str, object]:
    for point in table:
        if (
            point["budget"] == budget
            and point["adversarial_delay"] == adversarial_delay
        ):
            return point
    raise ValueError("point not found")


def _point_line(point: dict[str, object] | None) -> str:
    if point is None:
        return "none"
    maxima = point["component_maxima"]
    return (
        f"budget={point['budget']}, delay={point['adversarial_delay']}, "
        f"regime={point['regime']}, holds={point['holds']}, "
        "maxima=("
        f"{maxima['accessible_support']}, "
        f"{maxima['holder_redundancy']}, "
        f"{maxima['branch_support']}, "
        f"{maxima['reversal_cost']}, "
        f"{maxima['bounded_progress']})"
    )


if __name__ == "__main__":
    main()
