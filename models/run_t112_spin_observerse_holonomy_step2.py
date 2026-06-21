"""Write T112 spin-observerse holonomy Step 2 results to disk."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.t112_spin_observerse_holonomy import (
    run_t112_audit,
    t112_result_to_dict,
)


RESULTS_JSON = Path("results/spin-observerse-holonomy-step2-v0.1.json")
RESULTS_MD = Path("results/spin-observerse-holonomy-step2-v0.1-results.md")


def main() -> None:
    payload = t112_result_to_dict(run_t112_audit())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    topology = payload["topology"]
    phase = payload["phase"]
    chsh = payload["chsh"]
    causal = payload["causal_control"]
    representative = payload["representative_control"]

    lines = [
        "# T112 Results: Spin-Observerse Holonomy Step 2",
        "",
        "## Verdict",
        "",
        f"- Finite/proxy audit passed: `{payload['finite_proxy_passed']}`",
        f"- H3 status: {payload['h3_status']}",
        "",
        "## Strongest conditional claim",
        "",
        payload["strongest_conditional_claim"],
        "",
        "## Topology controls",
        "",
        (
            "- Naive `Y` nontrivial Z/2 holonomy available: "
            f"`{topology['naive_y_nontrivial_z2_holonomy_available']}`"
        ),
        (
            "- `Y_spin` Z/2 candidate available: "
            f"`{topology['spin_lift_z2_candidate_available']}`"
        ),
        f"- Verdict: {topology['verdict']}",
        "",
        "## Phase and CHSH sign",
        "",
        f"- Angle convention: `{phase['convention']['name']}`",
        f"- CHSH formula: {phase['convention']['chsh_formula']}",
        f"- CHSH value: `{chsh['chsh_value']}`",
        (
            "- `abs(CHSH) = 2*sqrt(2)`: "
            f"`{chsh['abs_chsh_matches_tsirelson']}`"
        ),
        (
            "- Positive-generator total angle: "
            f"`{phase['positive_generator_total_angle']}`"
        ),
        (
            "- Positive-generator Z/2 phase sign: "
            f"`{phase['positive_generator_z2_sign']}`"
        ),
        (
            "- Signed closed-angle control sign: "
            f"`{phase['signed_closed_z2_sign']}`"
        ),
        (
            "- Convention is load-bearing: "
            f"`{phase['convention_is_load_bearing']}`"
        ),
        f"- Phase verdict: {phase['verdict']}",
        "",
        "## T65 causal controls",
        "",
        f"- Total deterministic sections: `{causal['total_sections']}`",
        f"- Locally causal sections: `{causal['locally_causal_sections']}`",
        (
            "- LC sections all have holonomy +1: "
            f"`{causal['locally_causal_all_holonomy_plus_one']}`"
        ),
        f"- Holonomy +1 sections: `{causal['holonomy_plus_one_sections']}`",
        (
            "- Non-LC holonomy +1 sections: "
            f"`{causal['non_lc_holonomy_plus_one_sections']}`"
        ),
        f"- False biconditional restored: `{causal['biconditional_restored']}`",
        "",
        "## Representative controls",
        "",
        f"- Full support sections: `{representative['all_support_sections']}`",
        (
            "- Full support holonomy counts: "
            f"`{representative['all_support_holonomy_counts']}`"
        ),
        (
            "- Majority representatives all holonomy -1: "
            f"`{representative['majority_representatives_all_holonomy_minus_one']}`"
        ),
        (
            "- Representative dependence present: "
            f"`{representative['representative_dependence_present']}`"
        ),
        f"- Verdict: {representative['verdict']}",
        "",
        "## Not claimed",
        "",
    ]
    for claim in payload["not_claimed"]:
        lines.append(f"- {claim}")

    lines.extend(
        [
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
            "## Claim boundary",
            "",
            payload["claim_boundary"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
