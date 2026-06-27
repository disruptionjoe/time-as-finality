"""Runner for T252-T255 nine-event ordinal controls."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t252_t255_nine_event_ordinal_controls import (
    run_t252_analysis,
    run_t253_analysis,
    run_t254_analysis,
    run_t255_analysis,
    t252_result_to_dict,
    t253_result_to_dict,
    t254_result_to_dict,
    t255_result_to_dict,
)


OUTPUTS = (
    (
        "t252-nine-event-ordinal-t54-band-v0.1",
        "T252 Results: Nine-Event Ordinal T54 Band Witness",
        t252_result_to_dict,
        run_t252_analysis,
    ),
    (
        "t253-nine-event-ordinal-deletion-stability-v0.1",
        "T253 Results: Nine-Event Ordinal Deletion Stability",
        t253_result_to_dict,
        run_t253_analysis,
    ),
    (
        "t254-grid-vs-ordinal-nine-event-comparison-v0.1",
        "T254 Results: Grid Vs Ordinal Nine-Event Comparison",
        t254_result_to_dict,
        run_t254_analysis,
    ),
    (
        "t255-nine-event-ordinal-mutation-sensitivity-v0.1",
        "T255 Results: Nine-Event Ordinal Mutation Sensitivity",
        t255_result_to_dict,
        run_t255_analysis,
    ),
)


def main() -> None:
    Path("results").mkdir(exist_ok=True)
    for slug, title, serializer, runner in OUTPUTS:
        payload = serializer(runner())
        json_path = Path("results") / f"{slug}.json"
        md_path = Path("results") / f"{slug}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(_render_markdown(title, payload), encoding="utf-8")


def _fraction(value: dict[str, Any] | None) -> str:
    if value is None:
        return "-"
    return f"{value['fraction']} ({value['float']:.3f})"


def _render_markdown(title: str, payload: dict[str, Any]) -> str:
    if title.startswith("T252"):
        return _render_t252(title, payload)
    if title.startswith("T253"):
        return _render_t253(title, payload)
    if title.startswith("T254"):
        return _render_t254(title, payload)
    return _render_t255(title, payload)


def _render_t252(title: str, payload: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        "## Aggregate Checks",
        "",
        f"- Permutation: `{payload['permutation']}`",
        f"- T54 classification: `{payload['t54_classification']}`",
        f"- T54 theorem applies: `{payload['t54_theorem_applies']}`",
        f"- T126 classification: `{payload['t126_classification']}`",
        f"- T126 filter passed: `{payload['t126_filter_passed']}`",
        f"- Event count: {payload['event_count']}",
        f"- Strict pairs: {payload['strict_pair_count']}",
        f"- Ordering fraction: {_fraction(payload['ordering_fraction'])}",
        f"- Height: {payload['height']}",
        f"- Width: {payload['width']}",
        f"- T156 verdict: `{payload['t156_verdict']}`",
        f"- Verdict: `{payload['verdict']}`",
    ]
    return _append_common(lines, payload)


def _render_t253(title: str, payload: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        "## Aggregate Checks",
        "",
        f"- Parent ordering fraction: {_fraction(payload['parent_ordering_fraction'])}",
        f"- Parent band passed: `{payload['parent_band_passed']}`",
        f"- Deletion cases: {payload['deletion_case_count']}",
        f"- Deletions passing T126: {payload['deletion_t126_pass_count']}",
        f"- Deletions passing band: {payload['deletion_band_pass_count']}",
        f"- Deletion band pass rate: {_fraction(payload['deletion_band_pass_rate'])}",
        f"- Verdict: `{payload['verdict']}`",
        "",
        "## Deletion Table",
        "",
        "| Removed | T126 | Strict pairs | Ordering fraction | Band passed | Height | Width | Verdict |",
        "| --- | --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for audit in payload["deletion_audits"]:
        lines.append(
            "| "
            f"`{audit['removed_event']}` | "
            f"`{audit['t126_classification']}` | "
            f"{audit['strict_pair_count']} | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"`{audit['ordering_band_passed']}` | "
            f"{audit['height']} | "
            f"{audit['width']} | "
            f"`{audit['verdict']}` |"
        )
    return _append_common(lines, payload)


def _render_t254(title: str, payload: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        "## Comparison",
        "",
        "| Witness | Ordering fraction | Band passed | Deletion band passes |",
        "| --- | ---: | --- | ---: |",
        (
            "| `T249 grid` | "
            f"{_fraction(payload['grid_ordering_fraction'])} | "
            f"`{payload['grid_band_passed']}` | "
            f"{payload['grid_deletion_band_pass_count']} |"
        ),
        (
            "| `T252 ordinal` | "
            f"{_fraction(payload['ordinal_ordering_fraction'])} | "
            f"`{payload['ordinal_band_passed']}` | "
            f"{payload['ordinal_deletion_band_pass_count']} |"
        ),
        "",
        f"- Verdict: `{payload['verdict']}`",
    ]
    return _append_common(lines, payload)


def _render_t255(title: str, payload: dict[str, Any]) -> str:
    lines = [
        f"# {title}",
        "",
        "## Aggregate Checks",
        "",
        f"- Mutation count: {payload['mutation_count']}",
        f"- T126 pass and band pass: {payload['t126_pass_and_band_count']}",
        f"- T126 pass outside band: {payload['t126_pass_outside_band_count']}",
        f"- T126 blocked inside band: {payload['t126_blocked_inside_band_count']}",
        f"- Band total: {payload['band_total_count']}",
        f"- Verdict: `{payload['verdict']}`",
        "",
        "## Mutation Table",
        "",
        "| Swap | T126 | Ordering fraction | Band passed | Height | Width |",
        "| --- | --- | ---: | --- | ---: | ---: |",
    ]
    for audit in payload["mutation_audits"]:
        lines.append(
            "| "
            f"`{audit['swapped_positions']}` | "
            f"`{audit['t126_classification']}` | "
            f"{_fraction(audit['ordering_fraction'])} | "
            f"`{audit['ordering_band_passed']}` | "
            f"{audit['height']} | "
            f"{audit['width']} |"
        )
    return _append_common(lines, payload)


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


if __name__ == "__main__":
    main()
