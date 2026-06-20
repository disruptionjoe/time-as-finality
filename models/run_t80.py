"""Write T80 reversible-finality nonmonotonicity results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.reversible_finality_nonmonotonicity import (
    run_t80_analysis,
    t80_result_to_dict,
)


RESULTS_JSON = Path("results/reversible-finality-nonmonotonicity-v0.1.json")
RESULTS_MD = Path("results/reversible-finality-nonmonotonicity-v0.1-results.md")


def main() -> None:
    payload = t80_result_to_dict(run_t80_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    config = payload["configuration"]
    transition = payload["transition_map"]
    step = payload["first_nonmonotone_step"]
    lines = [
        "# T80 Results: Reversible Finality Nonmonotonicity",
        "",
        f"Strongest claim: {payload['strongest_claim']}",
        "",
        f"Weakened claim: {payload['weakened_claim']}",
        "",
        "## Configuration",
        "",
        f"- Rule: `{config['rule']}` second-order reversible lift",
        f"- Width: `{config['width']}`",
        f"- Initial previous/current: `{config['initial_previous']}` / `{config['initial_current']}`",
        f"- Seed index: `{config['seed_index']}`",
        f"- Observer window: `{config['observer_window']}`",
        "",
        "## Reversibility check",
        "",
        f"- State count: `{transition['state_count']}`",
        f"- Image count: `{transition['image_count']}`",
        f"- Injective: `{transition['injective']}`",
        f"- Lost bits: `{transition['lost_bits']}`",
        f"- Landauer lower-bound proxy: `{transition['landauer_minimum_joules']}`",
        f"- Direct inverse checked: `{transition['direct_inverse_checked']}`",
        "",
        "## Layer profiles",
        "",
        "| Layer | Trace mask | D1 trace profile |",
        "| ---: | --- | --- |",
    ]
    for profile in payload["layer_profiles"]:
        lines.append(
            f"| {profile['layer']} | `{profile['trace_mask']}` | "
            f"`{profile['d1_trace_profile']}` |"
        )
    lines.extend(
        [
            "",
            "## First nonmonotone physical step",
            "",
            f"- Layers: `{step['before_layer']} -> {step['after_layer']}`",
            f"- D1 trace profile: `{step['before_profile']} -> {step['after_profile']}`",
            f"- Decreased dimensions: `{step['decreased_dimensions']}`",
            f"- T18 classification: `{step['t18_kind']}`, possible under T18: `{step['t18_possible']}`",
            "",
            "## Persistent-memory control",
            "",
            f"- Retained support sequence: `{payload['persistent_memory_control']['support_sequence']}`",
            f"- Monotone: `{payload['persistent_memory_control']['monotone']}`",
            "",
            "Interpretation: "
            + payload["persistent_memory_control"]["interpretation"],
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
