"""Write T105 accessible-class sufficiency results to disk."""

from __future__ import annotations

import json
from pathlib import Path

from models.q1a_accessible_class_sufficiency import (
    run_t105_analysis,
    t105_result_to_dict,
)


RESULTS_JSON = Path("results/q1a-accessible-class-sufficiency-v0.1.json")
RESULTS_MD = Path("results/q1a-accessible-class-sufficiency-v0.1-results.md")


def main() -> None:
    payload = t105_result_to_dict(run_t105_analysis())
    RESULTS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    RESULTS_MD.write_text(_render_markdown(payload), encoding="utf-8")


def _render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# T105 Results: Q1A Accessible-Class Sufficiency",
        "",
        "## Aggregate checks",
        "",
        f"- Classifier matches all visible cases: {payload['classifier_matches_all_visible_cases']}",
        f"- Same support always same verdict: {payload['same_support_always_same_verdict']}",
        f"- Raw redundancy is not sufficient: {payload['raw_redundancy_is_not_sufficient']}",
        f"- External distinctness earned: {payload['external_distinctness_earned']}",
        "",
        "## Verdict histogram",
        "",
    ]
    for verdict, count in sorted(payload["verdict_histogram"].items()):
        lines.append(f"- {verdict}: {count}")

    lines.extend(["", "## Support histogram", ""])
    for support, count in sorted(payload["support_histogram"].items(), key=lambda item: item[0]):
        lines.append(f"- support {support}: {count}")

    hidden_case = payload["hidden_partition_case"]
    lines.extend(
        [
            "",
            "## Hidden partition control",
            "",
            f"- Case: {hidden_case['case_id']}",
            f"- D1 verdict: {hidden_case['d1_verdict']}",
            f"- Support classifier verdict: {hidden_case['support_classifier_verdict']}",
            "",
            "## Strongest claim",
            "",
            payload["strongest_claim"],
            "",
            "## What this improved",
            "",
            payload["improved"],
            "",
            "## What this weakened",
            "",
            payload["weakened"],
            "",
            "## Falsification condition",
            "",
            payload["falsification_condition"],
            "",
            "## Q1 update",
            "",
            payload["q1_update"],
            "",
            "## Claim ledger update",
            "",
            payload["claim_ledger_update"],
            "",
            "## Open blocker",
            "",
            payload["open_blocker"],
            "",
            "## Recommended next",
            "",
            payload["recommended_next"],
            "",
        ]
    )
    return "\n".join(str(line) for line in lines)


if __name__ == "__main__":
    main()
