"""Runner for T256-T263 ordinal-neighborhood diagnostics."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from models.t256_t263_ordinal_neighborhood_diagnostics import (
    run_t256_analysis,
    run_t257_analysis,
    run_t258_analysis,
    run_t259_analysis,
    run_t260_analysis,
    run_t261_analysis,
    run_t262_analysis,
    run_t263_analysis,
    t256_result_to_dict,
    t257_result_to_dict,
    t258_result_to_dict,
    t259_result_to_dict,
    t260_result_to_dict,
    t261_result_to_dict,
    t262_result_to_dict,
    t263_result_to_dict,
)


OutputSpec = tuple[str, str, Callable[[], object], Callable[[Any], dict[str, Any]]]


OUTPUTS: tuple[OutputSpec, ...] = (
    (
        "t256-t252-interval-profile-audit-v0.1",
        "T256 Results: T252 Interval Profile Audit",
        run_t256_analysis,
        t256_result_to_dict,
    ),
    (
        "t257-t252-cover-locality-audit-v0.1",
        "T257 Results: T252 Cover Locality Audit",
        run_t257_analysis,
        t257_result_to_dict,
    ),
    (
        "t258-t255-positive-neighbor-shape-catalog-v0.1",
        "T258 Results: T255 Positive Neighbor Shape Catalog",
        run_t258_analysis,
        t258_result_to_dict,
    ),
    (
        "t259-t255-inside-band-obstruction-catalog-v0.1",
        "T259 Results: T255 Inside-Band Obstruction Catalog",
        run_t259_analysis,
        t259_result_to_dict,
    ),
    (
        "t260-t255-outside-band-edge-cases-v0.1",
        "T260 Results: T255 Outside-Band Edge Cases",
        run_t260_analysis,
        t260_result_to_dict,
    ),
    (
        "t261-grid-vs-ordinal-shape-comparison-v0.1",
        "T261 Results: Grid Vs Ordinal Shape Comparison",
        run_t261_analysis,
        t261_result_to_dict,
    ),
    (
        "t262-next-route-selection-gate-v0.1",
        "T262 Results: Next Route Selection Gate",
        run_t262_analysis,
        t262_result_to_dict,
    ),
    (
        "t263-eight-task-ordinal-neighborhood-synthesis-v0.1",
        "T263 Results: Eight-Task Ordinal Neighborhood Synthesis",
        run_t263_analysis,
        t263_result_to_dict,
    ),
)


def main() -> None:
    Path("results").mkdir(exist_ok=True)
    for slug, title, runner, serializer in OUTPUTS:
        payload = serializer(runner())
        json_path = Path("results") / f"{slug}.json"
        md_path = Path("results") / f"{slug}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(_render_markdown(title, payload), encoding="utf-8")


def _render_markdown(title: str, payload: dict[str, Any]) -> str:
    lines = [f"# {title}", "", "## Aggregate Checks", ""]
    if title.startswith("T256"):
        lines.extend(_render_t256_checks(payload))
    elif title.startswith("T257"):
        lines.extend(_render_t257_checks(payload))
    elif title.startswith("T258"):
        lines.extend(_render_t258_checks(payload))
    elif title.startswith("T259"):
        lines.extend(_render_t259_checks(payload))
    elif title.startswith("T260"):
        lines.extend(_render_t260_checks(payload))
    elif title.startswith("T261"):
        lines.extend(_render_t261_checks(payload))
    elif title.startswith("T262"):
        lines.extend(_render_t262_checks(payload))
    else:
        lines.extend(_render_t263_checks(payload))
    return _append_common(lines, payload)


def _render_t256_checks(payload: dict[str, Any]) -> list[str]:
    parent = payload["parent_shape"]
    return [
        f"- Parent largest interval size: {parent['largest_interval_size']}",
        f"- Parent interval counts: `{parent['interval_counts_by_size']}`",
        (
            "- Deletion largest-interval distribution: "
            f"`{payload['deletion_largest_interval_distribution']}`"
        ),
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t257_checks(payload: dict[str, Any]) -> list[str]:
    parent = payload["parent_shape"]
    return [
        f"- Parent cover count: {parent['cover_relation_count']}",
        (
            "- Parent largest cover hub fraction: "
            f"{_fraction(parent['largest_cover_hub_fraction'])}"
        ),
        f"- Deletion cover-count distribution: `{payload['deletion_cover_count_distribution']}`",
        f"- Deletion cover-hub distribution: `{payload['deletion_cover_hub_distribution']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t258_checks(payload: dict[str, Any]) -> list[str]:
    return [
        f"- Positive neighbors: {payload['positive_neighbor_count']}",
        f"- Ordering-fraction distribution: `{payload['ordering_fraction_distribution']}`",
        f"- Width distribution: `{payload['width_distribution']}`",
        f"- Cover-count distribution: `{payload['cover_count_distribution']}`",
        f"- Largest-interval distribution: `{payload['largest_interval_distribution']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t259_checks(payload: dict[str, Any]) -> list[str]:
    return [
        f"- Blocked inside-band neighbors: {payload['blocked_inside_band_count']}",
        f"- Classification distribution: `{payload['classification_distribution']}`",
        (
            "- Profile-spread obstruction count: "
            f"{payload['profile_spread_obstruction_count']}"
        ),
        f"- Rank-profile distribution: `{payload['rank_profile_distribution']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t260_checks(payload: dict[str, Any]) -> list[str]:
    return [
        f"- Outside-band neighbors: {payload['outside_band_count']}",
        f"- Outside-band swaps: `{payload['outside_band_swaps']}`",
        f"- Ordering-fraction distribution: `{payload['ordering_fraction_distribution']}`",
        f"- Cover-count distribution: `{payload['cover_count_distribution']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t261_checks(payload: dict[str, Any]) -> list[str]:
    grid = payload["grid_shape"]
    ordinal = payload["ordinal_shape"]
    return [
        f"- Grid ordering fraction: {_fraction(grid['ordering_fraction'])}",
        f"- Ordinal ordering fraction: {_fraction(ordinal['ordering_fraction'])}",
        (
            "- Ordering-fraction gap grid minus ordinal: "
            f"{_fraction(payload['ordering_fraction_gap_grid_minus_ordinal'])}"
        ),
        (
            "- Strict-pair delta grid minus ordinal: "
            f"{payload['strict_pair_delta_grid_minus_ordinal']}"
        ),
        (
            "- Largest-interval delta grid minus ordinal: "
            f"{payload['largest_interval_delta_grid_minus_ordinal']}"
        ),
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t262_checks(payload: dict[str, Any]) -> list[str]:
    return [
        f"- Mutation count covered: {payload['mutation_count']}",
        f"- Positive neighbor rate: {_fraction(payload['positive_neighbor_rate'])}",
        f"- Band neighbor rate: {_fraction(payload['band_neighbor_rate'])}",
        f"- Selected next route: `{payload['selected_next_route']}`",
        f"- Secondary route: `{payload['secondary_route']}`",
        f"- Rejected route: `{payload['rejected_route']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]


def _render_t263_checks(payload: dict[str, Any]) -> list[str]:
    return [
        f"- Completed task count: {payload['completed_task_count']}",
        f"- T256 verdict: `{payload['t256_verdict']}`",
        f"- T257 verdict: `{payload['t257_verdict']}`",
        f"- T258 verdict: `{payload['t258_verdict']}`",
        f"- T259 verdict: `{payload['t259_verdict']}`",
        f"- T260 verdict: `{payload['t260_verdict']}`",
        f"- T261 verdict: `{payload['t261_verdict']}`",
        f"- T262 verdict: `{payload['t262_verdict']}`",
        f"- Round verdict: `{payload['round_verdict']}`",
    ]


def _append_common(lines: list[str], payload: dict[str, Any]) -> str:
    for heading, key in (
        ("Strongest Claim", "strongest_claim"),
        ("What This Improved", "improved"),
        ("What This Weakened Or Falsified", "weakened_or_falsified"),
        ("Falsification Condition", "falsification_condition"),
        ("S1 Update", "s1_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Open Blocker", "open_blocker"),
        ("Suggested Next", "suggested_next"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def _fraction(value: dict[str, Any]) -> str:
    return f"{value['fraction']} ({value['float']:.3f})"


if __name__ == "__main__":
    main()
