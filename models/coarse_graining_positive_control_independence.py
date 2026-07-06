"""T468: positive-control independence audit for T467.

T467 made valid coarse-graining executable as an admission gate. This follow-up
checks whether its positive controls are independent in the binary two-holder
fixture and whether bounded certification alone is enough without a
finality-native task.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable

from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
    evaluate_candidate,
    finite_record_states,
)


State = tuple[int, ...]
Labeler = Callable[[State], str]
Partition = tuple[tuple[str, ...], ...]

ARTIFACT_ID = "T468-coarse-graining-positive-control-independence-v0.1"
VERDICT = "T467_POSITIVE_CONTROLS_COLLAPSE_TASK_GATE_LOAD_BEARING"


def binary_holder_states(width: int) -> tuple[State, ...]:
    """Enumerate binary holder states used by the positive-control audit."""

    if width < 1:
        raise ValueError("width must be positive")
    return finite_record_states(width=width)


def finality_band_label(state: State) -> str:
    """Label all-zero, all-one, and mixed holder configurations."""

    if all(bit == 0 for bit in state):
        return "stable_zero"
    if all(bit == 1 for bit in state):
        return "stable_one"
    return "unsettled"


def local_count_label(state: State) -> str:
    """Label by the number of finalized-one holders."""

    return f"count_{sum(state)}"


def normalized_partition(states: tuple[State, ...], labeler: Labeler) -> Partition:
    """Return a label-independent partition signature."""

    classes: dict[str, list[str]] = {}
    for state in states:
        label = labeler(state)
        classes.setdefault(label, []).append(_state_label(state))
    return tuple(sorted(tuple(sorted(members)) for members in classes.values()))


def compare_positive_controls(width: int) -> dict[str, Any]:
    """Compare T467's two positive-control partitions at one holder width."""

    states = binary_holder_states(width)
    finality_partition = normalized_partition(states, finality_band_label)
    count_partition = normalized_partition(states, local_count_label)

    return {
        "holder_width": width,
        "state_count": len(states),
        "finality_band_class_count": len(finality_partition),
        "local_count_class_count": len(count_partition),
        "partitions_identical": finality_partition == count_partition,
        "finality_band_partition": finality_partition,
        "local_count_partition": count_partition,
    }


def minimum_width_for_positive_independence(max_width: int = 6) -> int | None:
    """Find the first holder width where band and count controls diverge."""

    for width in range(1, max_width + 1):
        if not compare_positive_controls(width)["partitions_identical"]:
            return width
    return None


def task_semantics_probe() -> dict[str, Any]:
    """Show that the finality-native task field is load-bearing in T467."""

    states = finite_record_states(width=4)
    budget = CertificationBudget()
    without_task = _xor_candidate(finality_native_task=False)
    with_task_label = _xor_candidate(finality_native_task=True)

    rejected = evaluate_candidate(without_task, budget, states)
    admitted_if_misdeclared = evaluate_candidate(with_task_label, budget, states)

    return {
        "candidate_shape": "cheap accessible xor over two holders",
        "without_finality_task": _evaluation_summary(rejected),
        "with_finality_task_label": _evaluation_summary(admitted_if_misdeclared),
        "task_semantics_load_bearing": (
            not rejected.admitted and admitted_if_misdeclared.admitted
        ),
        "reading": (
            "A cheap accessible xor partition is rejected when no finality-native "
            "task is declared, but it would pass the mechanical budget gate if "
            "the task flag were simply asserted. Future packets therefore need "
            "a task-naturalness audit, not just access and cost fields."
        ),
    }


def run() -> dict[str, Any]:
    """Run the T468 audit."""

    comparisons = [compare_positive_controls(width) for width in range(1, 5)]
    first_divergence = minimum_width_for_positive_independence()
    task_probe = task_semantics_probe()

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Audit T467's positive controls for extensional independence and "
            "test whether the finality-native task requirement is load-bearing."
        ),
        "positive_control_comparisons": comparisons,
        "minimum_holder_width_for_positive_independence": first_divergence,
        "task_semantics_probe": task_probe,
        "overall_verdict": {
            "verdict": VERDICT,
            "t467_binary_two_holder_positives_independent": False,
            "minimum_holder_width_for_positive_independence": first_divergence,
            "task_semantics_load_bearing": task_probe["task_semantics_load_bearing"],
            "claim_ledger_update": "none",
            "d1_promotion_earned": False,
            "t10_promotion_earned": False,
            "t29_promotion_earned": False,
            "observer_theory_identification_earned": False,
            "physics_claim_earned": False,
            "reading": (
                "T467's two admitted positive controls are extensionally the "
                "same partition on a binary two-holder fixture. They first "
                "separate at three holders, where finality-band and local-count "
                "coarse-grainings diverge. The cheap-xor probe also shows that "
                "finality-task semantics is load-bearing: bounded access and "
                "cost alone do not select a valid finality coarse-graining."
            ),
        },
        "not_earned": [
            "D1 promotion",
            "T10 superselection result",
            "T29 projection-obstruction promotion",
            "observer-theory equivalence theorem",
            "physics or consciousness claim",
            "claim-ledger movement",
            "public-posture movement",
        ],
        "future_packet_minimum": [
            "use at least three binary holders or a multi-valued fixture when claiming independent positive controls",
            "include a cheap accessible non-finality partition as a hostile control",
            "supply a predeclared task-naturalness account rather than only a boolean finality-task flag",
            "keep bounded certification, certified record, and observer-creates-truth guardrails from T467",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render the result as a compact Markdown artifact."""

    verdict = result["overall_verdict"]
    comparison_rows = []
    for row in result["positive_control_comparisons"]:
        comparison_rows.append(
            "| {holder_width} | {state_count} | {finality_band_class_count} | "
            "{local_count_class_count} | {partitions_identical} |".format(**row)
        )

    task_probe = result["task_semantics_probe"]
    task_rows = [
        _task_row("without finality task", task_probe["without_finality_task"]),
        _task_row("with task label asserted", task_probe["with_finality_task_label"]),
    ]
    not_earned = [f"- {item}" for item in result["not_earned"]]
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]

    return "\n".join(
        [
            "# T468 - Coarse-Graining Positive-Control Independence - v0.1 results",
            "",
            "> Audit only. No claim status, roadmap, README, North Star, public-posture, "
            "hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T468-coarse-graining-positive-control-independence.md`",
            "- Model: `models/coarse_graining_positive_control_independence.py`",
            "- Tests: `tests/test_coarse_graining_positive_control_independence.py`",
            "- Artifact JSON: `results/T468-coarse-graining-positive-control-independence-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gate: `results/T467-valid-coarse-graining-admissibility-gate-v0.1-results.md`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Positive-Control Partition Comparison",
            "",
            "| holder width | state count | finality-band classes | local-count classes | identical? |",
            "| --- | --- | --- | --- | --- |",
            *comparison_rows,
            "",
            "Minimum holder width for positive-control independence: "
            f"`{result['minimum_holder_width_for_positive_independence']}`.",
            "",
            "## Task Semantics Probe",
            "",
            task_probe["reading"],
            "",
            "| case | decision | route | blockers |",
            "| --- | --- | --- | --- |",
            *task_rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What This Does Not Earn",
            "",
            *not_earned,
            "",
        ]
    )


def _xor_candidate(finality_native_task: bool) -> CoarseGrainingCandidate:
    return CoarseGrainingCandidate(
        candidate_id=(
            "cheap_accessible_xor_with_task"
            if finality_native_task
            else "cheap_accessible_xor_without_task"
        ),
        description=(
            "A cheap accessible xor partition over two holders; useful as a "
            "hostile control for task-naturalness."
        ),
        fields_read=(0, 1),
        predicate_cost=2,
        holder_redundancy=2,
        reversal_cost=1,
        declared_before_use=True,
        certified_record_available=True,
        finality_native_task=finality_native_task,
        expected_valid=False,
        labeler=lambda state: f"xor_{state[0] ^ state[1]}",
    )


def _evaluation_summary(evaluation: Any) -> dict[str, Any]:
    return {
        "candidate_id": evaluation.candidate_id,
        "admitted": evaluation.admitted,
        "decision": evaluation.decision,
        "route_label": evaluation.route_label,
        "blockers": list(evaluation.blockers),
        "class_count": evaluation.class_count,
    }


def _task_row(case: str, row: dict[str, Any]) -> str:
    blockers = ", ".join(row["blockers"]) or "none"
    return (
        f"| {case} | {row['decision']} | {row['route_label']} | {blockers} |"
    )


def _state_label(state: State) -> str:
    return "".join(str(bit) for bit in state)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    result = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / f"{ARTIFACT_ID}.json"
        md_path = results_dir / f"{ARTIFACT_ID}-results.md"
        json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(result), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
