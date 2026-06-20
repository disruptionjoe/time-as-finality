"""Runner for T113: Gap Presheaf Classification."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from models.gap_presheaf_classification import run_t113_analysis, t113_result_to_dict


JSON_PATH = Path("results") / "gap-presheaf-classification-v0.1.json"
MD_PATH = Path("results") / "gap-presheaf-classification-v0.1-results.md"


def _render_markdown(data: dict[str, Any]) -> str:
    lines: list[str] = [
        "# T113 Results: Gap Presheaf Classification",
        "",
        "## Verdict",
        "",
        str(data["best_supported"]),
        "",
        "## Aggregate Comparison",
        "",
        f"- Raw H0(G) equals phantoms: `{data['raw_h0_equals_phantoms']}`",
        (
            "- Typed gap sections equal phantoms: "
            f"`{data['typed_gap_sections_equal_phantoms']}`"
        ),
        f"- FRP restriction closure preserved: `{data['frp_restriction_closure_preserved']}`",
        f"- Malformed controls rejected: `{data['malformed_controls_rejected']}`",
        (
            "- T53 noncanonical completions block raw classification: "
            f"`{data['t53_noncanonical_blocks_raw_classification']}`"
        ),
        "",
        "## Section Counts",
        "",
        f"- Raw gap sections: `{len(data['raw_h0_gap_sections'])}`",
        f"- Typed gap sections: `{len(data['typed_gap_sections'])}`",
        f"- Phantom sections: `{len(data['phantom_sections'])}`",
        "",
        "## Hypothesis Results",
        "",
    ]

    for hypothesis in data["hypothesis_evaluations"]:
        lines.extend(
            [
                f"### {hypothesis['id']}: {hypothesis['status']}",
                "",
                hypothesis["claim"],
                "",
                f"Evidence: {hypothesis['evidence']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Witness Table",
            "",
            (
                "| Source | Case | Observer | G(U) | Typed G(U) | Phantoms | "
                "Classification |"
            ),
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in data["section_audits"]:
        if not (audit["gap_pairs"] or audit["phantom_pairs"] or audit["spurious_apparent_pairs"]):
            continue
        lines.append(
            "| "
            f"{audit['source_pattern']} | "
            f"{audit['case_name']} | "
            f"{audit['observer']} | "
            f"`{audit['gap_pairs']}` | "
            f"`{audit['typed_gap_pairs']}` | "
            f"`{audit['phantom_pairs']}` | "
            f"{audit['classification']} |"
        )

    lines.extend(["", "## T53 Diagnostics", ""])
    lines.extend(
        [
            "| Case | Verdict | Role | Unique | Gap-bearing completions |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for diagnostic in data["t53_diagnostics"]:
        lines.append(
            "| "
            f"{diagnostic['case_name']} | "
            f"{diagnostic['verdict']} | "
            f"{diagnostic['classification_role']} | "
            f"`{diagnostic['unique_completion']}` | "
            f"`{diagnostic['gap_bearing_completion_names']}` |"
        )

    lines.extend(["", "## FRP Gap Checks", ""])
    lines.extend(
        [
            "| Cover | Closed | Violations | Non-lifting examples |",
            "| --- | --- | ---: | ---: |",
        ]
    )
    for check in data["frp_gap_checks"]:
        lines.append(
            "| "
            f"{check['cover_name']} | "
            f"`{check['holds']}` | "
            f"{len(check['violations'])} | "
            f"{len(check['non_lifting_examples'])} |"
        )

    lines.extend(["", "## Finding", "", str(data["finding"]), "", "## Guardrails", ""])
    for guardrail in data["guardrails"]:
        lines.append(f"- {guardrail}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    result = run_t113_analysis()
    data = t113_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    MD_PATH.write_text(_render_markdown(data), encoding="utf-8")

    print("=== T113: Gap Presheaf Classification ===")
    print()
    print(result.best_supported)
    print()
    for hypothesis in result.hypothesis_evaluations:
        print(f"{hypothesis.hypothesis_id} [{hypothesis.status}]")
        print(f"  {hypothesis.evidence}")
    print()
    print(result.finding)
    print()
    print(f"JSON written to {JSON_PATH}")
    print(f"Markdown written to {MD_PATH}")


if __name__ == "__main__":
    main()
