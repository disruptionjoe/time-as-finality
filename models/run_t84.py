"""Write T84 cyclic-reconciler entropy-export results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.cyclic_reconciler_entropy_export import (
    run_t84_analysis,
    t84_result_to_dict,
)


RESULTS_JSON = Path("results/cyclic-reconciler-entropy-export-v0.1.json")
RESULTS_MD = Path("results/cyclic-reconciler-entropy-export-v0.1-results.md")


def main() -> None:
    payload = t84_result_to_dict(run_t84_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T84 Results: Cyclic Reconciler Entropy Export",
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
        "## Cyclic policies",
        "",
        "| Policy | Local support | Local monotone | Accounted support | Accounted monotone | Injective | Lost bits | Boundary |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for policy in payload["policies"].values():
        transition = policy["transition_map"]
        lines.append(
            "| "
            f"`{policy['name']}` | "
            f"`{policy['local_support_sequence']}` | "
            f"`{policy['local_monotone']}` | "
            f"`{policy['accounted_support_sequence']}` | "
            f"`{policy['accounted_monotone']}` | "
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
