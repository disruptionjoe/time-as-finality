"""Runner for T46: open causal scarcity and closed synchronization boundary."""

from __future__ import annotations

import json
from pathlib import Path

from models.record_access_systems import run_t46_analysis, t46_result_to_dict


JSON_PATH = Path("results") / "open-causal-scarcity-synchronization-boundary-v0.1.json"
MD_PATH = Path("results") / "open-causal-scarcity-synchronization-boundary-v0.1-results.md"


def render_markdown(data: dict[str, object]) -> str:
    """Render a compact Markdown result artifact from serialized T46 data."""

    open_result = data["open_causal"]  # type: ignore[index]
    closed_result = data["closed_synchronization"]  # type: ignore[index]
    comparison = data["comparison"]  # type: ignore[index]
    projection = data["measurement_projection"]  # type: ignore[index]
    hypotheses = data["hypothesis_evaluations"]  # type: ignore[index]

    lines = [
        "# T46 Results: Open Causal Scarcity And Closed Synchronization Boundary",
        "",
        "## Verdict",
        "",
        f"- Best-supported hypothesis: `{data['best_supported_hypothesis']}`",
        f"- Named-claim recommendation: {data['named_claim_recommendation']}",
        "",
        "## Open Causal Scarcity",
        "",
        f"- First-access order: `{tuple(open_result['first_access_order'])}`",  # type: ignore[index]
        f"- Proximity advantage: `{open_result['proximity_advantage']}`",  # type: ignore[index]
        f"- Proximity driven: `{open_result['proximity_driven']}`",  # type: ignore[index]
        f"- Finding: {open_result['finding']}",  # type: ignore[index]
        "",
        "## Closed Synchronization Boundary",
        "",
        f"- Internal commit order: `{tuple(closed_result['internal_commit_order'])}`",  # type: ignore[index]
        f"- Outside raw arrival order: `{tuple(closed_result['outside_raw_arrival_order'])}`",  # type: ignore[index]
        f"- Outside commit-record arrival order: `{tuple(closed_result['outside_commit_record_arrival_order'])}`",  # type: ignore[index]
        f"- Outside reconstruction time: `{closed_result['outside_reconstruction_time']}`",  # type: ignore[index]
        f"- Raw order differs from commit order: `{closed_result['raw_order_differs_from_commit_order']}`",  # type: ignore[index]
        f"- Membership boundary active: `{closed_result['membership_boundary_active']}`",  # type: ignore[index]
        f"- Propagation constraints respected: `{closed_result['propagation_constraints_respected']}`",  # type: ignore[index]
        f"- Synchronization cost total: `{closed_result['synchronization_cost_total']}`",  # type: ignore[index]
        "",
        "## Boundary Comparison",
        "",
        f"- Open scarcity axis: `{comparison['open_scarcity_axis']}`",  # type: ignore[index]
        f"- Closed scarcity axis: `{comparison['closed_scarcity_axis']}`",  # type: ignore[index]
        f"- Outside observer lag: `{comparison['outside_observer_lag']}`",  # type: ignore[index]
        f"- Statement: {comparison['statement']}",  # type: ignore[index]
        "",
        "## Measurement Projection Boundary",
        "",
        f"- Source layer: `{projection['source_layer']}`",  # type: ignore[index]
        f"- Target layer: `{projection['target_layer']}`",  # type: ignore[index]
        f"- Assumes 14D Y: `{projection['assumes_fourteen_dimensional_y']}`",  # type: ignore[index]
        f"- PO1 status: {projection['po1_status']}",  # type: ignore[index]
        "- Preserved structure:",
    ]
    lines.extend(f"  - `{item}`" for item in projection["preserved_structure"])  # type: ignore[index]
    lines.append("- Forgotten structure:")
    lines.extend(f"  - `{item}`" for item in projection["forgotten_structure"])  # type: ignore[index]
    lines.extend(
        [
            "",
            "## Hypotheses",
            "",
        ]
    )
    for item in hypotheses:  # type: ignore[assignment]
        lines.append(f"- `{item['hypothesis_id']}`: `{item['status']}`")  # type: ignore[index]
    lines.extend(
        [
            "",
            "## Theorem",
            "",
            str(data["theorem"]),
            "",
            "## Boundary",
            "",
            str(data["boundary"]),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = run_t46_analysis()
    data = t46_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    MD_PATH.write_text(render_markdown(data), encoding="utf-8")

    print("T46: Open Causal Scarcity And Closed Synchronization Boundary")
    print()
    print("  Open causal scarcity:")
    print(f"    first access order: {result.open_causal.first_access_order}")
    print(f"    proximity advantage: {result.open_causal.proximity_advantage}")
    print()
    print("  Closed synchronization boundary:")
    print(f"    internal commit order: {result.closed_synchronization.internal_commit_order}")
    print(f"    outside raw order:     {result.closed_synchronization.outside_raw_arrival_order}")
    print(f"    reconstruction time:   {result.closed_synchronization.outside_reconstruction_time}")
    print()
    print("  Hypothesis verdicts:")
    for h in result.hypothesis_evaluations:
        print(f"    {h.hypothesis_id}: {h.status}")
    print()
    print(f"  Best supported: {result.best_supported_hypothesis}")
    print(f"  JSON written to {JSON_PATH}")
    print(f"  Markdown written to {MD_PATH}")


if __name__ == "__main__":
    main()
