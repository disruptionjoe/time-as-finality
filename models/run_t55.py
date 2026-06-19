"""Runner for T55: Conflict-Enriched FinaliEvent Descent."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.conflict_finalievent_descent import run_t55_analysis, t55_result_to_dict


def _write_markdown(data: dict, out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# T55 Results: Conflict-Enriched FinaliEvent Descent")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(data["best_supported"])
    lines.append("")
    lines.append("## Theorem Statement")
    lines.append("")
    lines.append(data["theorem_statement"])
    lines.append("")
    lines.append("## Condition Basis")
    lines.append("")
    for condition in data["condition_basis"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Classification Table")
    lines.append("")
    lines.append("| Case | Classification | Theorem applies | Conflict valid | Failures |")
    lines.append("| --- | --- | --- | --- | --- |")
    for completion in data["completions"]:
        failures = ", ".join(completion["condition_failures"]) or "none"
        conflict = completion["conflict_check"]
        conflict_valid = "n/a" if conflict is None else str(conflict["valid"])
        lines.append(
            f"| {completion['datum_name']} | {completion['classification']} | "
            f"{completion['theorem_applies']} | {conflict_valid} | {failures} |"
        )
    lines.append("")
    lines.append("## Event-Structure Verdict")
    lines.append("")
    lines.append(data["event_structure_verdict"])
    lines.append("")
    lines.append("## Hypothesis Results")
    lines.append("")
    for h in data["hypothesis_evaluations"]:
        lines.append(f"### {h['id']}: {h['status']}")
        lines.append("")
        lines.append(h["claim"])
        lines.append("")
        lines.append(f"Evidence: {h['evidence']}")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t55_analysis()
    data = t55_result_to_dict(result)

    json_path = Path("results") / "conflict-finalievent-descent-v0.1.json"
    md_path = Path("results") / "conflict-finalievent-descent-v0.1-results.md"
    json_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    _write_markdown(data, md_path)

    print("=== T55: Conflict-Enriched FinaliEvent Descent ===")
    print()
    print(result.theorem_statement)
    print()
    print("--- Condition Basis ---")
    for condition in result.condition_basis:
        print(f"- {condition}")
    print()
    print("--- Classifications ---")
    for completion in result.completions:
        failures = ", ".join(completion.condition_failures) or "none"
        conflict_valid = (
            "n/a" if completion.conflict_check is None else str(completion.conflict_check.valid)
        )
        print(f"{completion.datum_name}: {completion.classification}")
        print(f"  theorem_applies: {completion.theorem_applies}")
        print(f"  conflict_valid:  {conflict_valid}")
        print(f"  failures:        {failures}")
        print(f"  evidence:        {completion.evidence}")
        print()
    print("--- Hypothesis Verdicts ---")
    for h in result.hypothesis_evaluations:
        print(f"{h.hypothesis_id} [{h.status}]")
        print(f"  {h.claim}")
        print(f"  evidence: {h.evidence}")
        print()
    print(f"Event-structure verdict: {result.event_structure_verdict}")
    print(f"Best supported: {result.best_supported}")
    print()
    print(f"JSON written to {json_path}")
    print(f"Markdown written to {md_path}")


if __name__ == "__main__":
    main()
