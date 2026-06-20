"""Write T120 ASP typed-subpresheaf absorption audit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.asp_typed_subpresheaf_absorption import (
    run_t120_analysis,
    t120_result_to_dict,
)


RESULTS_JSON = Path("results/asp-typed-subpresheaf-absorption-v0.2.json")
RESULTS_MD = Path("results/asp-typed-subpresheaf-absorption-v0.2-results.md")


def main() -> None:
    payload = t120_result_to_dict(run_t120_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    positive = payload["positive_restriction"]
    negative = payload["negative_restriction"]
    boundary = payload["boundary"]
    absorption = payload["absorption"]
    lines = [
        "# T120 Results: ASP Typed Subpresheaf And Absorption Audit v0.2",
        "",
        "## Strongest version",
        "",
        payload["strongest_version"],
        "",
        "## Weakest point",
        "",
        payload["weakest_point"],
        "",
        "## Typed subpresheaf check",
        "",
        "| System | Closure holds | ASP by patch | Violations |",
        "| --- | --- | --- | --- |",
        (
            f"| `{positive['name']}` | `{positive['closure_holds']}` | "
            f"`{positive['asp_by_patch']}` | `{positive['violations']}` |"
        ),
        (
            f"| `{negative['name']}` | `{negative['closure_holds']}` | "
            f"`{negative['asp_by_patch']}` | `{negative['violations']}` |"
        ),
        "",
        "## Relabeling invariance",
        "",
        f"Relabeling invariant: `{payload['relabeling']['invariant']}`",
        "",
        "## Boundary covariance",
        "",
        "| Coarse ASP | Refined ASP | Invariant? | Covariant change? |",
        "| --- | --- | --- | --- |",
        (
            f"| `{boundary['coarse_asp']}` | `{boundary['refined_asp']}` | "
            f"`{boundary['invariant_under_boundary_change']}` | "
            f"`{boundary['covariant_change_detected']}` |"
        ),
        "",
        boundary["explanation"],
        "",
        "## Absorption rerun",
        "",
        "| Check | Result |",
        "| --- | --- |",
        f"| Coarse metrics match | `{absorption['coarse_metrics_match']}` |",
        (
            "| Coarse reachability separates | "
            f"`{absorption['coarse_reachability_separates']}` |"
        ),
        f"| ASP separates | `{absorption['asp_separates']}` |",
        (
            "| Enriched reachability absorbs | "
            f"`{absorption['enriched_reachability_absorbs']}` |"
        ),
        f"| Opportunity set absorbs | `{absorption['opportunity_set_absorbs']}` |",
        f"| High ASP tasks | `{absorption['high_asp_tasks']}` |",
        f"| Low ASP tasks | `{absorption['low_asp_tasks']}` |",
        "",
        "## Prior-art comparison",
        "",
        "| Comparator | Capture |",
        "| --- | --- |",
    ]
    for comparator, capture in absorption["prior_art"].items():
        lines.append(f"| {comparator} | `{capture}` |")
    lines.extend(
        [
            "",
            "## Verdict",
            "",
            payload["verdict"],
            "",
            "## Recommendation",
            "",
            payload["recommendation"],
            "",
            "## Claim impact",
            "",
            payload["claim_impact"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
