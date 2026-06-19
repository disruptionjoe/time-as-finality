"""Runner for T59: Finite-to-Infinite Boundary Audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.finite_to_infinite_boundary_audit import (
    run_t59_analysis,
    t59_result_to_dict,
)


def render_markdown(data: dict) -> str:
    lines: list[str] = []
    lines.append("# T59 Results: Finite-to-Infinite Boundary Audit")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(data["best_supported"])
    lines.append("")
    lines.append("## Audit Table")
    lines.append("")
    lines.append(
        "| Cover | Encoding | Monodromy | Orientation global section | "
        "Parity global section | False global section |"
    )
    lines.append("| --- | --- | ---: | --- | --- | --- |")
    for audit in data["audits"]:
        lines.append(
            f"| {audit['cover_name']} | {audit['encoding']} | "
            f"{audit['topological_monodromy_sign']} | "
            f"{audit['orientation_global_section_exists']} | "
            f"{audit['parity_global_section_exists']} | "
            f"{audit['false_global_section']} |"
        )
    lines.append("")
    lines.append("## Hypothesis Results")
    lines.append("")
    for hypothesis in data["hypothesis_evaluations"]:
        lines.append(f"### {hypothesis['id']}: {hypothesis['status']}")
        lines.append("")
        lines.append(hypothesis["claim"])
        lines.append("")
        lines.append(f"Evidence: {hypothesis['evidence']}")
        lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append(data["boundary"])
    lines.append("")
    lines.append("## Recommended Next")
    lines.append("")
    lines.append(data["recommended_next"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t59_analysis()
    data = t59_result_to_dict(result)

    json_path = Path("results") / "finite-to-infinite-boundary-audit-v0.1.json"
    md_path = Path("results") / "finite-to-infinite-boundary-audit-v0.1-results.md"
    json_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(data), encoding="utf-8")

    print("=== T59: Finite-to-Infinite Boundary Audit ===")
    print()
    print(result.best_supported)
    print()
    print("--- Boundary Audits ---")
    for audit in result.audits:
        print(f"{audit.cover_name} / {audit.encoding}")
        print(f"  monodromy: {audit.topological_monodromy_sign}")
        print(f"  orientation global section: {audit.orientation_global_section_exists}")
        print(f"  parity global section: {audit.parity_global_section_exists}")
        print(f"  false global section: {audit.false_global_section}")
        print(f"  conclusion: {audit.conclusion}")
        print()
    print("--- Hypothesis Verdicts ---")
    for hypothesis in result.hypothesis_evaluations:
        print(f"{hypothesis.hypothesis_id} [{hypothesis.status}]")
        print(f"  {hypothesis.claim}")
        print(f"  evidence: {hypothesis.evidence}")
        print()
    print(f"Boundary: {result.boundary}")
    print()
    print(f"JSON written to {json_path}")
    print(f"Markdown written to {md_path}")


if __name__ == "__main__":
    main()
