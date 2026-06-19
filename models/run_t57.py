"""Runner for T57: Finality Reflection Property."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from models.finality_reflection_property import (
    run_t57_analysis,
    t57_result_to_dict,
)


def _write_markdown(data: dict, out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# T57 Results: Finality Reflection Property")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(data["best_supported"])
    lines.append("")
    lines.append("## Theorem Statement")
    lines.append("")
    lines.append(data["theorem_statement"])
    lines.append("")
    lines.append("## Reflection Checks")
    lines.append("")
    lines.append("| Cover | Nested patch pairs | Checked event pairs | FRP holds | Violations |")
    lines.append("| --- | ---: | ---: | --- | ---: |")
    for check in data["reflection_checks"]:
        lines.append(
            f"| {check['cover_name']} | {check['comparable_patch_pairs']} | "
            f"{check['checked_event_pairs']} | {check['holds']} | "
            f"{len(check['violations'])} |"
        )
    lines.append("")
    lines.append("## Gap Restriction Checks")
    lines.append("")
    lines.append("| Cover | Nested patch pairs | Closed | Violations | Non-lifting examples |")
    lines.append("| --- | ---: | --- | ---: | ---: |")
    for check in data["gap_checks"]:
        lines.append(
            f"| {check['cover_name']} | {check['comparable_patch_pairs']} | "
            f"{check['holds']} | {len(check['violations'])} | "
            f"{len(check['non_lifting_examples'])} |"
        )
    lines.append("")
    lines.append("## Generic Complement Counterexample")
    lines.append("")
    ce = data["complement_counterexample"]
    lines.append(f"- Witness pair: `{ce['witness_pair']}`")
    lines.append(f"- FRP holds: `{ce['frp_holds']}`")
    lines.append(
        f"- Complement restriction closed: `{ce['complement_restriction_closed']}`"
    )
    lines.append(f"- Explanation: {ce['explanation']}")
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
    lines.append("## Limits")
    lines.append("")
    for limit in data["limits"]:
        lines.append(f"- {limit}")
    lines.append("")
    lines.append("## Next Questions")
    lines.append("")
    for question in data["next_questions"]:
        lines.append(f"- {question}")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    result = run_t57_analysis()
    data = t57_result_to_dict(result)

    json_path = Path("results") / "finality-reflection-property-v0.1.json"
    md_path = Path("results") / "finality-reflection-property-v0.1-results.md"
    json_path.parent.mkdir(exist_ok=True)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    _write_markdown(data, md_path)

    print("=== T57: Finality Reflection Property ===")
    print()
    print(result.theorem_statement)
    print()
    print("--- Reflection Checks ---")
    for check in result.reflection_checks:
        print(f"{check.cover_name}: holds={check.holds}")
        print(f"  nested patch pairs: {check.comparable_patch_pairs}")
        print(f"  checked event pairs: {check.checked_event_pairs}")
        print(f"  violations: {len(check.violations)}")
        print()
    print("--- Gap Restriction Checks ---")
    for check in result.gap_checks:
        print(f"{check.cover_name}: closed={check.holds}")
        print(f"  violations: {len(check.violations)}")
        print(f"  non-lifting examples: {len(check.non_lifting_examples)}")
        print()
    ce = result.complement_counterexample
    print("--- Generic Complement Counterexample ---")
    print(f"witness pair: {ce.witness_pair}")
    print(f"FRP holds: {ce.frp_holds}")
    print(f"complement restriction closed: {ce.complement_restriction_closed}")
    print()
    print("--- Hypothesis Verdicts ---")
    for h in result.hypothesis_evaluations:
        print(f"{h.hypothesis_id} [{h.status}]")
        print(f"  {h.claim}")
        print(f"  evidence: {h.evidence}")
        print()
    print(result.best_supported)
    print()
    print(f"JSON written to {json_path}")
    print(f"Markdown written to {md_path}")


if __name__ == "__main__":
    main()
