"""Write T129 future capability preservation audit results."""

from __future__ import annotations

import json
from pathlib import Path

from models.future_capability_preservation_audit import (
    run_t129_analysis,
    t129_result_to_dict,
)


RESULTS_JSON = Path("results/future-capability-preservation-audit-v0.1.json")
RESULTS_MD = Path("results/future-capability-preservation-audit-v0.1-results.md")


def main() -> None:
    payload = t129_result_to_dict(run_t129_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T129 Results: Future Capability Preservation Audit",
        "",
        "## Strongest common object",
        "",
        payload["strongest_common_object"],
        "",
        "## Finite witness table",
        "",
        "| Witness | State held fixed | Future capability changed | Candidate cause |",
        "| --- | --- | --- | --- |",
    ]
    for row in payload["finite_witness_table"]:
        lines.append(
            "| "
            f"{row['witness']} | "
            f"{row['state_held_fixed']} | "
            f"{row['future_capability_changed']} | "
            f"{row['candidate_cause']} |"
        )

    lines.extend(
        [
            "",
            "## Branch representation",
            "",
            "| Branch | Components present | Strongest absorber | Verdict |",
            "| --- | --- | --- | --- |",
        ]
    )
    for witness in payload["witnesses"]:
        lines.append(
            "| "
            f"{witness['branch']} | "
            f"`{witness['capability_structure']['components_present']}` | "
            f"{witness['strongest_existing_absorber']} | "
            f"{witness['verdict']} |"
        )

    lines.extend(
        [
            "",
            "## Prior-art pressure",
            "",
            "| Framework | Verdict | Reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in payload["prior_art"]:
        lines.append(
            "| "
            f"{item['framework']} | "
            f"`{item['verdict']}` | "
            f"{item['reason']} |"
        )

    for heading, key in (
        ("Weakest point", "weakest_point"),
        ("Closest prior art", "closest_prior_art"),
        ("Strongest separation witness", "strongest_separation_witness"),
        ("Strongest absorption witness", "strongest_absorption_witness"),
        ("Recommendation", "recommendation_rationale"),
        ("Claim impact note", "claim_impact_note"),
    ):
        lines.extend(["", f"## {heading}", "", payload[key]])

    lines.extend(
        [
            "",
            "## Verdict flags",
            "",
            f"- Common structure exists: `{payload['common_structure_exists']}`",
            f"- Reducible to existing frameworks: `{payload['reducible_to_existing_frameworks']}`",
            f"- Recommendation: `{payload['recommendation']}`",
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
