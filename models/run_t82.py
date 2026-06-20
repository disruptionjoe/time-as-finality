"""Write T82 persistent-reconciler cost-boundary results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.persistent_reconciler_cost_boundary import (
    run_t82_analysis,
    t82_result_to_dict,
)


RESULTS_JSON = Path("results/persistent-reconciler-cost-boundary-v0.1.json")
RESULTS_MD = Path("results/persistent-reconciler-cost-boundary-v0.1-results.md")


def main() -> None:
    payload = t82_result_to_dict(run_t82_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T82 Results: Persistent Reconciler Cost Boundary",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## T80 observation sequence",
        "",
        f"- Observed masks: `{payload['observations']}`",
        f"- Raw support sequence: `{payload['raw_support_sequence']}`",
        f"- Raw support monotone: `{payload['raw_support_monotone']}`",
        "",
        "## Reconciler policies",
        "",
        "| Policy | Support sequence | Monotone | Injective | Lost bits | Boundary |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for policy in payload["policies"].values():
        transition = policy["transition_map"]
        lines.append(
            "| "
            f"`{policy['name']}` | "
            f"`{policy['support_sequence']}` | "
            f"`{policy['monotone_support']}` | "
            f"`{transition['injective']}` | "
            f"`{transition['lost_bits']}` | "
            f"{policy['resource_boundary']} |"
        )
    lines.extend(
        [
            "",
            "## Verdicts",
            "",
        ]
    )
    for policy in payload["policies"].values():
        lines.append(f"- `{policy['name']}`: {policy['verdict']}")
    lines.extend(
        [
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## H7 update",
            "",
            payload["h7_update"],
            "",
            "## Blocker",
            "",
            payload["blocker"],
            "",
            "## Next move",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    main()
