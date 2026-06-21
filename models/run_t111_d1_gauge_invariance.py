"""Write T111 D1 gauge-invariance audit results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.t111_d1_gauge_invariance_audit import run_t111_analysis


RESULTS_JSON = Path("results/d1-gauge-invariance-audit-v0.1.json")
RESULTS_MD = Path("results/d1-gauge-invariance-audit-v0.1-results.md")


def main() -> None:
    payload = run_t111_analysis()
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    reference = payload["reference_profile"]
    verdict = payload["verdict"]
    lines = [
        "# T111 Results: D1 Gauge-Invariance Audit",
        "",
        "## Strongest Claim",
        "",
        payload["strongest_claim"],
        "",
        "## Reference Profile",
        "",
        f"- Tuple order: `{reference['tuple_order']}`",
        f"- Profile tuple: `{reference['profile_tuple']}`",
        "",
        "## Allowed Transformations",
        "",
    ]
    for transformation in payload["allowed_transformations"]:
        lines.append(f"- {transformation}")

    lines.extend(
        [
            "",
            "## Transformation Audit",
            "",
            "| Transformation | Kind | Admissible | Pure gauge | Before | After | Verdict |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for audit in payload["audits"]:
        lines.append(
            "| "
            f"{audit['name']} | "
            f"{audit['kind']} | "
            f"{audit['admissible']} | "
            f"{audit['gauge_pure']} | "
            f"`{audit['before_profile']['profile_tuple']}` | "
            f"`{audit['after_profile']['profile_tuple']}` | "
            f"{audit['verdict']} |"
        )

    lines.extend(
        [
            "",
            "## Dimension Classification",
            "",
            "| Dimension | Pure gauge | Boundary maps | Negative-control failures | Future status |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for summary in payload["dimension_summaries"]:
        failures = ", ".join(summary["negative_control_failures"]) or "none"
        lines.append(
            "| "
            f"{summary['dimension']} | "
            f"{summary['pure_gauge_classification']} | "
            f"{summary['boundary_classification']} | "
            f"{failures} | "
            f"{summary['future_connection_status']} |"
        )

    lines.extend(
        [
            "",
            "## Verdict Checks",
            "",
            f"- Pure gauge maps preserve all D1 dimensions: `{verdict['pure_gauge_maps_preserve_all_d1_dimensions']}`",
            f"- Boundary maps are not treated as gauge: `{verdict['boundary_maps_are_not_treated_as_gauge']}`",
            f"- Negative controls change alleged invariants: `{verdict['negative_controls_change_alleged_invariants']}`",
            f"- No curvature/gravity/anomaly claim: `{verdict['no_curvature_gravity_or_anomaly_claim']}`",
            "",
            "## Guardrail",
            "",
            payload["guardrail"],
            "",
            "## Recommendation",
            "",
            payload["recommendation"],
            "",
            "## Reproduction",
            "",
            "```bash",
            "python -m unittest tests.test_t111_d1_gauge_invariance_audit -v",
            "python -m models.run_t111_d1_gauge_invariance",
            "```",
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
