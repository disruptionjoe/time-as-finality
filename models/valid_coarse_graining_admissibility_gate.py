"""T467: valid coarse-graining as finality-admissibility gate.

This module turns the valid-coarse-graining open problem into a finite
admission gate. It does not claim that TaF solves observer theory. It tests the
repo-local candidate criterion: a coarse-graining is valid for this purpose
only when a bounded observer can form and certify the corresponding finalized
record under explicit D1-style budget fields.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from itertools import product
from pathlib import Path
from typing import Any, Callable


State = tuple[int, ...]
Labeler = Callable[[State], str]

ARTIFACT_ID = "T467-valid-coarse-graining-admissibility-gate-v0.1"
VERDICT = "VALID_COARSE_GRAINING_ADMISSIBILITY_GATE_BUILT_NO_PROMOTION"


@dataclass(frozen=True)
class CertificationBudget:
    """Finite observer budget for certifying a record coarse-graining."""

    accessible_fields: tuple[int, ...] = (0, 1, 2)
    max_fields_read: int = 2
    max_predicate_cost: int = 3
    min_holder_redundancy: int = 2
    max_reversal_cost: int = 2


@dataclass(frozen=True)
class CoarseGrainingCandidate:
    """One proposed equivalence relation over finite record states."""

    candidate_id: str
    description: str
    fields_read: tuple[int, ...]
    predicate_cost: int
    holder_redundancy: int
    reversal_cost: int
    declared_before_use: bool
    certified_record_available: bool
    finality_native_task: bool
    expected_valid: bool
    labeler: Labeler = field(compare=False, repr=False)
    projection_only_no_record: bool = False
    observer_creates_truth_overread: bool = False
    claim_promotion_requested: bool = False
    public_posture_move_requested: bool = False
    cross_repo_truth_move_requested: bool = False


@dataclass(frozen=True)
class CandidateEvaluation:
    """Gate decision for one finite coarse-graining candidate."""

    candidate_id: str
    admitted: bool
    decision: str
    route_label: str
    blockers: tuple[str, ...]
    class_count: int
    singleton_classes: int
    partition_signature: tuple[tuple[str, tuple[State, ...]], ...]
    expected_valid: bool


def finite_record_states(width: int = 4) -> tuple[State, ...]:
    """Enumerate binary record states for the finite gate."""

    return tuple(tuple(bits) for bits in product((0, 1), repeat=width))


def partition_signature(
    candidate: CoarseGrainingCandidate,
    states: tuple[State, ...],
) -> tuple[tuple[str, tuple[State, ...]], ...]:
    """Return the equivalence classes induced by a candidate labeler."""

    classes: dict[str, list[State]] = {}
    for state in states:
        label = candidate.labeler(state)
        classes.setdefault(label, []).append(state)
    return tuple(
        (label, tuple(classes[label]))
        for label in sorted(classes)
    )


def evaluate_candidate(
    candidate: CoarseGrainingCandidate,
    budget: CertificationBudget,
    states: tuple[State, ...],
) -> CandidateEvaluation:
    """Evaluate one candidate under the bounded-certification rule."""

    signature = partition_signature(candidate, states)
    class_count = len(signature)
    singleton_classes = sum(1 for _label, members in signature if len(members) == 1)
    blockers: list[str] = []

    if candidate.claim_promotion_requested:
        blockers.append("claim_promotion_requested")
    if candidate.public_posture_move_requested:
        blockers.append("public_posture_move_requested")
    if candidate.cross_repo_truth_move_requested:
        blockers.append("cross_repo_truth_move_requested")
    if candidate.observer_creates_truth_overread:
        blockers.append("observer_creates_truth_overread")
    if not candidate.declared_before_use:
        blockers.append("posthoc_equivalence_relation")
    if candidate.projection_only_no_record or not candidate.certified_record_available:
        blockers.append("projection_without_certified_record")
    inaccessible = tuple(
        field_id
        for field_id in candidate.fields_read
        if field_id not in budget.accessible_fields
    )
    if inaccessible:
        blockers.append("uses_inaccessible_record_fields")
    if len(candidate.fields_read) > budget.max_fields_read:
        blockers.append("field_budget_exceeded")
    if candidate.predicate_cost > budget.max_predicate_cost:
        blockers.append("predicate_cost_ornate")
    if candidate.holder_redundancy < budget.min_holder_redundancy:
        blockers.append("holder_redundancy_below_d1_floor")
    if candidate.reversal_cost > budget.max_reversal_cost:
        blockers.append("reversal_cost_over_budget")
    if class_count <= 1:
        blockers.append("too_coarse_no_task_separation")
    if class_count >= len(states):
        blockers.append("too_fine_microstate_identity")
    if not candidate.finality_native_task:
        blockers.append("no_finalized_record_task")

    forbidden = {
        "claim_promotion_requested",
        "public_posture_move_requested",
        "cross_repo_truth_move_requested",
        "observer_creates_truth_overread",
    }
    if forbidden.intersection(blockers):
        decision = "blocked"
        route = "FORBIDDEN_POSTURE_OR_CREATION_OVERREAD"
    elif "posthoc_equivalence_relation" in blockers:
        decision = "not_admitted"
        route = "POSTHOC_EQUIVALENCE_NOT_VALID"
    elif "projection_without_certified_record" in blockers:
        decision = "not_admitted"
        route = "PROJECTION_IS_NOT_FINALITY"
    elif "too_fine_microstate_identity" in blockers:
        decision = "not_admitted"
        route = "TOO_FINE_MICROSTATE_TRACKING"
    elif "too_coarse_no_task_separation" in blockers:
        decision = "not_admitted"
        route = "TOO_COARSE_NO_TASK_SEPARATION"
    elif "uses_inaccessible_record_fields" in blockers:
        decision = "not_admitted"
        route = "INACCESSIBLE_RECORD_FIELD"
    elif {
        "field_budget_exceeded",
        "predicate_cost_ornate",
    }.intersection(blockers):
        decision = "not_admitted"
        route = "COMPUTATION_COST_ORNATE_OR_OVER_BUDGET"
    elif {
        "holder_redundancy_below_d1_floor",
        "reversal_cost_over_budget",
    }.intersection(blockers):
        decision = "not_admitted"
        route = "D1_CERTIFICATION_BUDGET_NOT_MET"
    elif "no_finalized_record_task" in blockers:
        decision = "not_admitted"
        route = "NO_FINALIZED_RECORD_TASK"
    else:
        decision = "admitted_for_review"
        route = "BOUNDED_OBSERVER_CERTIFIABLE"

    return CandidateEvaluation(
        candidate_id=candidate.candidate_id,
        admitted=decision == "admitted_for_review",
        decision=decision,
        route_label=route,
        blockers=tuple(blockers),
        class_count=class_count,
        singleton_classes=singleton_classes,
        partition_signature=signature,
        expected_valid=candidate.expected_valid,
    )


def example_candidates() -> tuple[CoarseGrainingCandidate, ...]:
    """Representative finite candidate equivalence relations."""

    return (
        CoarseGrainingCandidate(
            candidate_id="two_holder_finality_band",
            description=(
                "Two accessible holders certify 00, 11, or mismatch as the "
                "record-status band."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=True,
            labeler=lambda state: (
                "stable_zero"
                if state[0] == 0 and state[1] == 0
                else "stable_one"
                if state[0] == 1 and state[1] == 1
                else "unsettled"
            ),
        ),
        CoarseGrainingCandidate(
            candidate_id="bounded_local_count",
            description=(
                "A bounded observer records the count of finalized support in "
                "two accessible holders."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=2,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=True,
            labeler=lambda state: f"count_{state[0] + state[1]}",
        ),
        CoarseGrainingCandidate(
            candidate_id="microstate_identity",
            description="The equivalence relation is equality of the full state.",
            fields_read=(0, 1, 2, 3),
            predicate_cost=4,
            holder_redundancy=4,
            reversal_cost=4,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda state: "state_" + "".join(str(bit) for bit in state),
        ),
        CoarseGrainingCandidate(
            candidate_id="constant_all_states",
            description="All source states are collapsed into one class.",
            fields_read=(),
            predicate_cost=0,
            holder_redundancy=0,
            reversal_cost=0,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda _state: "all_states",
        ),
        CoarseGrainingCandidate(
            candidate_id="hidden_fourth_field",
            description="The class depends on a field outside the observer boundary.",
            fields_read=(0, 3),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda state: f"visible_hidden_{state[0]}_{state[3]}",
        ),
        CoarseGrainingCandidate(
            candidate_id="ornate_table_lookup",
            description=(
                "A declared but computationally ornate lookup table is required "
                "to recognize the class."
            ),
            fields_read=(0, 1),
            predicate_cost=12,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda state: f"lookup_{(state[0] + 2 * state[1]) % 3}",
        ),
        CoarseGrainingCandidate(
            candidate_id="posthoc_exception_partition",
            description="The relation is selected after seeing the state set.",
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=False,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda state: "exception" if state == (1, 1, 1, 1) else "other",
        ),
        CoarseGrainingCandidate(
            candidate_id="projection_only_shadow",
            description="A visible projection is present, but no record is certified.",
            fields_read=(0, 1),
            predicate_cost=1,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=False,
            finality_native_task=True,
            expected_valid=False,
            projection_only_no_record=True,
            labeler=lambda state: f"shadow_{state[0]}",
        ),
        CoarseGrainingCandidate(
            candidate_id="single_holder_dashboard",
            description="A one-holder dashboard label lacks D1-style redundancy.",
            fields_read=(0,),
            predicate_cost=1,
            holder_redundancy=1,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            labeler=lambda state: f"holder_{state[0]}",
        ),
        CoarseGrainingCandidate(
            candidate_id="observer_creates_truth_overread",
            description=(
                "The relation asks to treat observer equivalencing as making the "
                "underlying fact true."
            ),
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=True,
            expected_valid=False,
            observer_creates_truth_overread=True,
            labeler=lambda state: f"overread_{state[0] == state[1]}",
        ),
    )


def run() -> dict[str, Any]:
    """Run the T467 finite admission gate."""

    budget = CertificationBudget()
    states = finite_record_states()
    candidates = example_candidates()
    evaluations = tuple(
        evaluate_candidate(candidate, budget, states)
        for candidate in candidates
    )
    admitted = tuple(
        evaluation.candidate_id
        for evaluation in evaluations
        if evaluation.admitted
    )
    expected = tuple(
        candidate.candidate_id
        for candidate in candidates
        if candidate.expected_valid
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Make the valid-coarse-graining-as-finality-admissibility filter "
            "executable on a finite record-state universe."
        ),
        "budget": _budget_dict(budget),
        "state_count": len(states),
        "candidates": [_candidate_dict(candidate) for candidate in candidates],
        "evaluations": [
            _evaluation_dict(evaluation)
            for evaluation in evaluations
        ],
        "overall_verdict": {
            "verdict": VERDICT,
            "admitted_candidate_ids": list(admitted),
            "predeclared_valid_candidate_ids": list(expected),
            "filter_matches_predeclared_valid_set": admitted == expected,
            "claim_ledger_update": "none",
            "d1_promotion_earned": False,
            "t10_promotion_earned": False,
            "t29_promotion_earned": False,
            "observer_theory_identification_earned": False,
            "physics_claim_earned": False,
            "reading": (
                "In this finite fixture, the bounded-observer certification "
                "filter admits only the declared finality-record band and local "
                "count controls. Microstate identity, trivial collapse, hidden "
                "fields, ornate lookup, posthoc partitions, projection-only "
                "shadows, one-holder dashboards, and observer-creates-truth "
                "overreads all fail before claim movement."
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
            "finite state universe and candidate equivalence relation declared",
            "record fields needed to classify each state named before selection",
            "all fields inside the observer access boundary",
            "recognition predicate within the declared computation budget",
            "D1-style holder redundancy and reversal-cost floors satisfied",
            "nontrivial coarse-graining: neither all states nor microstate identity",
            "certified record available, not projection alone",
            "finality-native task declared without observer-creates-truth overread",
            "positive and hostile controls included before any claim movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render the result as a compact Markdown artifact."""

    verdict = result["overall_verdict"]
    rows = []
    for evaluation in result["evaluations"]:
        blockers = ", ".join(evaluation["blockers"]) or "none"
        rows.append(
            "| {candidate_id} | {decision} | {route_label} | {class_count} | {blockers} |".format(
                candidate_id=evaluation["candidate_id"],
                decision=evaluation["decision"],
                route_label=evaluation["route_label"],
                class_count=evaluation["class_count"],
                blockers=blockers,
            )
        )

    not_earned = [f"- {item}" for item in result["not_earned"]]
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]

    return "\n".join(
        [
            "# T467 - Valid Coarse-Graining Admissibility Gate - v0.1 results",
            "",
            "> Admission gate only. No claim status, roadmap, README, North Star, "
            "public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T467-valid-coarse-graining-admissibility-gate.md`",
            "- Model: `models/valid_coarse_graining_admissibility_gate.py`",
            "- Tests: `tests/test_valid_coarse_graining_admissibility_gate.py`",
            "- Artifact JSON: `results/T467-valid-coarse-graining-admissibility-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Budget",
            "",
            f"- accessible fields: `{result['budget']['accessible_fields']}`",
            f"- max fields read: `{result['budget']['max_fields_read']}`",
            f"- max predicate cost: `{result['budget']['max_predicate_cost']}`",
            f"- min holder redundancy: `{result['budget']['min_holder_redundancy']}`",
            f"- max reversal cost: `{result['budget']['max_reversal_cost']}`",
            "",
            "## Gate Table",
            "",
            "| candidate | decision | route | class count | blockers |",
            "| --- | --- | --- | --- | --- |",
            *rows,
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


def _budget_dict(budget: CertificationBudget) -> dict[str, Any]:
    return {
        "accessible_fields": list(budget.accessible_fields),
        "max_fields_read": budget.max_fields_read,
        "max_predicate_cost": budget.max_predicate_cost,
        "min_holder_redundancy": budget.min_holder_redundancy,
        "max_reversal_cost": budget.max_reversal_cost,
    }


def _candidate_dict(candidate: CoarseGrainingCandidate) -> dict[str, Any]:
    return {
        "candidate_id": candidate.candidate_id,
        "description": candidate.description,
        "fields_read": list(candidate.fields_read),
        "predicate_cost": candidate.predicate_cost,
        "holder_redundancy": candidate.holder_redundancy,
        "reversal_cost": candidate.reversal_cost,
        "declared_before_use": candidate.declared_before_use,
        "certified_record_available": candidate.certified_record_available,
        "finality_native_task": candidate.finality_native_task,
        "expected_valid": candidate.expected_valid,
        "projection_only_no_record": candidate.projection_only_no_record,
        "observer_creates_truth_overread": candidate.observer_creates_truth_overread,
        "claim_promotion_requested": candidate.claim_promotion_requested,
        "public_posture_move_requested": candidate.public_posture_move_requested,
        "cross_repo_truth_move_requested": candidate.cross_repo_truth_move_requested,
    }


def _state_label(state: State) -> str:
    return "".join(str(bit) for bit in state)


def _evaluation_dict(evaluation: CandidateEvaluation) -> dict[str, Any]:
    return {
        "candidate_id": evaluation.candidate_id,
        "admitted": evaluation.admitted,
        "decision": evaluation.decision,
        "route_label": evaluation.route_label,
        "blockers": list(evaluation.blockers),
        "class_count": evaluation.class_count,
        "singleton_classes": evaluation.singleton_classes,
        "partition_signature": [
            {
                "label": label,
                "members": [_state_label(state) for state in members],
            }
            for label, members in evaluation.partition_signature
        ],
        "expected_valid": evaluation.expected_valid,
    }


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
