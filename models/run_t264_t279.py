"""Runner for T264-T279 exact n=9 ordinal count tasks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.t264_t279_nine_event_ordinal_exact_count import (
    TASK_RUNNERS,
    TaskResult,
    task_result_to_dict,
)


def main() -> None:
    Path("results").mkdir(exist_ok=True)
    for runner in TASK_RUNNERS:
        result = runner()
        payload = task_result_to_dict(result)
        slug = _slug(result)
        json_path = Path("results") / f"{slug}.json"
        md_path = Path("results") / f"{slug}-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(_render_markdown(payload), encoding="utf-8")


def _slug(result: TaskResult) -> str:
    return f"{result.task_id.lower()}-{_slugify(result.title)}-v0.1"


def _slugify(value: str) -> str:
    return (
        value.lower()
        .replace("=", "")
        .replace("+", "plus")
        .replace(" ", "-")
        .replace("/", "-")
    )


def _render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        f"# {payload['task_id']} Results: {payload['title']}",
        "",
        "## Aggregate Checks",
        "",
        "| Metric | Value |",
        "| --- | --- |",
    ]
    for metric in payload["metrics"]:
        lines.append(f"| `{metric['name']}` | `{metric['value']}` |")
    lines.extend(["", f"- Verdict: `{payload['verdict']}`"])
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
