"""Runner for T222: Finite-to-Infinite Boundary Theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.finite_to_infinite_boundary_theorem import (
    run_t222_analysis,
    t222_result_to_dict,
)


def render_markdown(data: dict) -> str:
    lines: list[str] = []
    lines.append("# T222 Results: Finite-to-Infinite Boundary Theorem")
    lines.append("")
    lines.append("## Verdict Summary")
    lines.append("")
    lines.append(data["summary"])
    lines.append("")
    lines.append(
        f"Counts: survives = {data['survives_count']}, "
        f"conditional = {data['conditional_count']}, "
        f"strictly_finite = {data['strictly_finite_count']}. "
        f"All witnesses hold = {data['all_witnesses_hold']}."
    )
    lines.append("")
    lines.append("## Per-Result Verdict Table")
    lines.append("")
    lines.append("| Result | Source tests | Verdict | Boundary line |")
    lines.append("| --- | --- | --- | --- |")
    for v in data["verdicts"]:
        lines.append(
            f"| {v['result_id']} ({v['result_name']}) | "
            f"{', '.join(v['source_tests'])} | **{v['verdict']}** | "
            f"{v['boundary_line']} |"
        )
    lines.append("")
    lines.append("## Witnesses")
    lines.append("")
    for v in data["verdicts"]:
        lines.append(f"### {v['result_id']} — {v['verdict']}")
        lines.append("")
        lines.append(f"Survival hypothesis: {v['survival_hypothesis']}")
        lines.append("")
        for w in v["witnesses"]:
            mark = "holds" if w["holds"] else "FAILS"
            lines.append(f"- **{w['side']}** [{mark}]: {w['description']}")
            lines.append(f"  - {w['detail']}")
        lines.append("")
        lines.append(f"Guardrail: {v['guardrail_note']}")
        lines.append("")
    lines.append("## Most Load-Bearing Finite Restriction")
    lines.append("")
    lines.append(data["most_load_bearing_finite_restriction"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t222_analysis()
    data = t222_result_to_dict(result)

    json_path = Path("results") / "finite-to-infinite-boundary-theorem-v0.1.json"
    md_path = Path("results") / "finite-to-infinite-boundary-theorem-v0.1-results.md"
    json_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(data), encoding="utf-8")

    print("=== T222: Finite-to-Infinite Boundary Theorem ===")
    print()
    print(result.summary)
    print()
    for v in result.verdicts:
        print(f"[{v.verdict.upper()}] {v.result_id}: {v.result_name}")
        for w in v.witnesses:
            mark = "OK" if w.holds else "FAIL"
            print(f"    ({mark}) {w.side}: {w.description}")
        print()
    print(f"All witnesses hold: {result.all_witnesses_hold}")
    print()
    print(f"Most load-bearing finite restriction:\n{result.most_load_bearing_finite_restriction}")
    print()
    print(f"JSON written to {json_path}")
    print(f"Markdown written to {md_path}")


if __name__ == "__main__":
    main()
