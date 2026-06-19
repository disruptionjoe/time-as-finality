"""Runner for T61: MMO reconciliation finality."""

from __future__ import annotations

import json
from pathlib import Path

from models.mmo_reconciliation_finality import run_t61_analysis, t61_result_to_dict


JSON_PATH = Path("results") / "mmo-reconciliation-finality-v0.1.json"
MD_PATH = Path("results") / "mmo-reconciliation-finality-v0.1-results.md"


def render_markdown(data: dict[str, object]) -> str:
    positive = data["positive_witness"]  # type: ignore[index]
    failure = data["failure_witness"]  # type: ignore[index]

    lines = [
        "# T61 Results: MMO Reconciliation Finality",
        "",
        "## Verdict",
        "",
        f"- Claim classification: {data['claim_classification']}",
        f"- Boundary: {data['boundary']}",
        "",
        "## Axis Mapping",
        "",
    ]
    for axis, meaning in data["axis_mapping"]:  # type: ignore[assignment]
        lines.append(f"- `{axis}`: {meaning}")
    lines.extend(
        [
            "",
            "## Positive Witness",
            "",
            f"- Name: `{positive['name']}`",  # type: ignore[index]
            f"- Classification: `{positive['classification']}`",  # type: ignore[index]
            f"- Local finality: `{tuple(positive['finality_answer']['locally_final'])}`",  # type: ignore[index]
            f"- Authoritative finality: `{tuple(positive['finality_answer']['authoritatively_final'])}`",  # type: ignore[index]
            f"- Rolled back: `{tuple(positive['finality_answer']['rolled_back'])}`",  # type: ignore[index]
            f"- Statement: {positive['finality_answer']['reconciliation_statement']}",  # type: ignore[index]
            "",
            "## Failure Witness",
            "",
            f"- Name: `{failure['name']}`",  # type: ignore[index]
            f"- Classification: `{failure['classification']}`",  # type: ignore[index]
            f"- Local finality: `{tuple(failure['finality_answer']['locally_final'])}`",  # type: ignore[index]
            f"- Authoritative finality: `{tuple(failure['finality_answer']['authoritatively_final'])}`",  # type: ignore[index]
            f"- Rolled back: `{tuple(failure['finality_answer']['rolled_back'])}`",  # type: ignore[index]
            f"- Conflict completion: `{failure['conflict_completion']['classification']}`",  # type: ignore[index]
            f"- Conflict valid: `{failure['conflict_completion']['conflict_valid']}`",  # type: ignore[index]
            f"- Statement: {failure['finality_answer']['reconciliation_statement']}",  # type: ignore[index]
            "",
            "## Observer Event Times",
            "",
            "| Witness | Observer | Event | Time | Status |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    for witness_name, witness in (("positive", positive), ("failure", failure)):
        for observer, event, arrival, status in witness["finality_answer"]["observer_event_times"]:  # type: ignore[index]
            lines.append(f"| {witness_name} | `{observer}` | `{event}` | {arrival} | `{status}` |")
    lines.extend(
        [
            "",
            "## Theorem Candidate",
            "",
            str(data["theorem_candidate"]),
            "",
            "## Recommendation",
            "",
            str(data["recommendation"]),
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = run_t61_analysis()
    data = t61_result_to_dict(result)

    JSON_PATH.parent.mkdir(exist_ok=True)
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    MD_PATH.write_text(render_markdown(data), encoding="utf-8")

    print("T61: MMO Reconciliation Finality")
    print()
    print(f"  positive: {result.positive_witness.classification}")
    print(f"  failure:  {result.failure_witness.classification}")
    print(f"  claim:    {result.claim_classification}")
    print()
    print(f"  JSON written to {JSON_PATH}")
    print(f"  Markdown written to {MD_PATH}")


if __name__ == "__main__":
    main()

