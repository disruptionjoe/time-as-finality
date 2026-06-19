"""Runner for T53: Observer-Colimit Descent Boundary Audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.observer_colimit_descent_boundary import (
    run_t53_analysis,
    t53_result_to_dict,
)


def _write_markdown(data: dict, out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# T53 Results: Observer-Colimit Descent Boundary")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(data["best_supported"])
    lines.append("")
    lines.append("## Theorem Statement")
    lines.append("")
    lines.append(data["theorem_statement"])
    lines.append("")
    lines.append("## Required Descent Data")
    lines.append("")
    for item in data["descent_data_required"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Case Results")
    lines.append("")
    lines.append("| Case | Verdict | Compatible completions | Axis valid | Axis failing | Hidden repair |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for case in data["cases"]:
        completions = ", ".join(case["compatible_completion_names"]) or "none"
        lines.append(
            "| {case} | {verdict} | {completions} | {axis_valid} | {axis_failing} | {repair} |".format(
                case=case["case_name"],
                verdict=case["verdict"],
                completions=completions,
                axis_valid=case["has_axis_valid_completion"],
                axis_failing=case["has_axis_failing_completion"],
                repair=case["has_hidden_record_repair"],
            )
        )
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

    result = run_t53_analysis()
    data = t53_result_to_dict(result)

    json_path = Path("results") / "observer-colimit-descent-boundary-v0.1.json"
    md_path = Path("results") / "observer-colimit-descent-boundary-v0.1-results.md"
    json_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    _write_markdown(data, md_path)

    print("=== T53: Observer-Colimit Descent Boundary Audit ===")
    print()
    print(result.theorem_statement)
    print()
    print("--- Case Verdicts ---")
    for case in result.cases:
        print(f"{case.case_name}: {case.verdict}")
        print(f"  compatible completions: {list(case.compatible_completion_names)}")
        print(f"  distinct signatures:    {case.distinct_compatible_signatures}")
        print(f"  unique completion:      {case.unique_completion}")
        print(f"  axis valid/failing:     {case.has_axis_valid_completion}/{case.has_axis_failing_completion}")
        print(f"  evidence:               {case.evidence}")
        print()

    print("--- Hypothesis Verdicts ---")
    for h in result.hypothesis_evaluations:
        print(f"{h.hypothesis_id} [{h.status}]")
        print(f"  {h.claim}")
        print(f"  evidence: {h.evidence}")
        print()

    print(f"Best supported: {result.best_supported}")
    print()
    print(f"JSON written to {json_path}")
    print(f"Markdown written to {md_path}")


if __name__ == "__main__":
    main()
