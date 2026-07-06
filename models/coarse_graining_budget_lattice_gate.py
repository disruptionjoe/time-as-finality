"""T478: budget-lattice gate for valid coarse-graining packets.

T477 tested one nested observer-budget transition. This module expands that
stress test to a finite access-budget lattice and checks that admission is
monotone, join/path independent, and still blocks cheap hostile controls.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Callable

from models.coarse_graining_task_naturalness_gate import (
    NaturalnessCandidate,
    TaskNaturalnessEvidence,
    evaluate_naturalness_candidate,
)
from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
    finite_record_states,
)


State = tuple[int, ...]
Labeler = Callable[[State], str]
Partition = tuple[tuple[str, ...], ...]

ARTIFACT_ID = "T478-coarse-graining-budget-lattice-gate-v0.1"
VERDICT = "BUDGET_LATTICE_GATE_BUILT_PATH_INDEPENDENT_NO_PROMOTION"


def budget_catalogue() -> tuple[tuple[str, CertificationBudget], ...]:
    """Return a small lattice of access budgets containing root holder 0."""

    field_sets = (
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (0, 1, 2, 3),
    )
    return tuple(
        (
            f"budget_{''.join(str(field_id) for field_id in fields)}",
            CertificationBudget(
                accessible_fields=fields,
                max_fields_read=len(fields),
                max_predicate_cost=4,
                min_holder_redundancy=2,
                max_reversal_cost=2,
            ),
        )
        for fields in field_sets
    )


def lattice_candidates() -> tuple[NaturalnessCandidate, ...]:
    """Return the candidate catalogue for the T478 lattice gate."""

    return (
        _candidate(
            candidate_id="pair_01_finality_band",
            description="Holder 0 and holder 1 certify stable or unsettled status.",
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, (0, 1)),
            evidence=TaskNaturalnessEvidence(
                task_family="pair_01_finality_status",
                certified_record_object="pair_01_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id="pair_02_finality_band",
            description="Holder 0 and holder 2 certify stable or unsettled status.",
            fields_read=(0, 2),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, (0, 2)),
            evidence=TaskNaturalnessEvidence(
                task_family="pair_02_finality_status",
                certified_record_object="pair_02_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id="boundary_pair_status",
            description=(
                "Holder 0 and holder 3 certify a boundary-pair record; this "
                "is admitted only in budgets that include holder 3."
            ),
            fields_read=(0, 3),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: (
                "boundary_pair_equal"
                if state[0] == state[3]
                else "boundary_pair_mismatch"
            ),
            evidence=TaskNaturalnessEvidence(
                task_family="boundary_pair_finality_status",
                certified_record_object="boundary_pair_record_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="observer_index_positive_control",
        ),
        _candidate(
            candidate_id="three_holder_finality_band",
            description="Holders 0, 1, and 2 certify a stable value or unsettled band.",
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, (0, 1, 2)),
            evidence=TaskNaturalnessEvidence(
                task_family="three_holder_finality_status_band",
                certified_record_object="three_holder_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="join_positive_control",
        ),
        _candidate(
            candidate_id="three_holder_support_count",
            description="Holders 0, 1, and 2 certify finalized-support count.",
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: f"support_count_{state[0] + state[1] + state[2]}",
            evidence=TaskNaturalnessEvidence(
                task_family="three_holder_support_multiplicity",
                certified_record_object="three_holder_support_count",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="join_positive_control",
        ),
        _candidate(
            candidate_id="cheap_pair01_parity_with_task_label",
            description="A cheap pair parity partition with a finality-task label asserted.",
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"pair01_parity_{state[0] ^ state[1]}",
            evidence=TaskNaturalnessEvidence(
                task_family="asserted_finality_task",
                certified_record_object="",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="cheap_triple_parity_with_task_label",
            description="A cheap triple arithmetic partition with a task label asserted.",
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"triple_parity_{(state[0] + state[1] + state[2]) % 2}",
            evidence=TaskNaturalnessEvidence(
                task_family="asserted_finality_task",
                certified_record_object="",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="label_restatement_lookup",
            description="A bounded lookup whose task semantics restate selected labels.",
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: (
                "selected_label"
                if state[:3] in {(1, 0, 1), (0, 1, 0)}
                else "other_label"
            ),
            evidence=TaskNaturalnessEvidence(
                task_family="lookup_label_preference",
                certified_record_object="lookup_label_table",
                declared_before_relation=True,
                preserves_record_value_or_support=False,
                semantics_not_label_restatement=False,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="microstate_identity",
            description="The relation tracks the complete four-holder microstate.",
            fields_read=(0, 1, 2, 3),
            predicate_cost=4,
            holder_redundancy=4,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: "state_" + _state_label(state),
            evidence=TaskNaturalnessEvidence(
                task_family="microstate_identity",
                certified_record_object="full_microstate_record",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="hostile_control",
        ),
        _candidate(
            candidate_id="observer_creates_truth_overread",
            description="A forbidden packet that treats equivalencing as truth creation.",
            fields_read=(0, 1),
            predicate_cost=2,
            holder_redundancy=2,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, (0, 1)),
            evidence=TaskNaturalnessEvidence(
                task_family="observer_makes_truth",
                certified_record_object="pair_01_record",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
                observer_creates_truth_overread=True,
            ),
            role="forbidden_control",
            observer_creates_truth_overread=True,
        ),
    )


def run() -> dict[str, Any]:
    """Run the T478 budget-lattice gate."""

    states = finite_record_states(width=4)
    budgets = budget_catalogue()
    candidates = {candidate.base.candidate_id: candidate for candidate in lattice_candidates()}
    evaluations_by_budget: dict[str, dict[str, Any]] = {}
    budget_results: list[dict[str, Any]] = []

    for budget_id, budget in budgets:
        evaluations = {
            candidate_id: evaluate_naturalness_candidate(candidate, budget, states)
            for candidate_id, candidate in candidates.items()
        }
        evaluation_dicts = {
            candidate_id: _evaluation_dict(evaluation)
            for candidate_id, evaluation in evaluations.items()
        }
        evaluations_by_budget[budget_id] = evaluation_dicts
        budget_results.append(
            {
                "budget_id": budget_id,
                "budget": _budget_dict(budget),
                "admitted_candidate_ids": _admitted_ids(evaluation_dicts),
                "candidate_evaluations": list(evaluation_dicts.values()),
            }
        )

    edge_checks = _edge_checks(budgets, evaluations_by_budget)
    join_checks = _join_checks(budgets, evaluations_by_budget, candidates)
    path_checks = _path_checks(evaluations_by_budget)
    transition_rows = _transition_rows(budgets, evaluations_by_budget, candidates)
    hostile_violations = _hostile_violations(budgets, evaluations_by_budget, candidates)
    top_budget_id = "budget_0123"
    top_admitted_positives = _admitted_positive_ids(
        evaluations_by_budget[top_budget_id],
        candidates,
    )
    top_positives_independent = _positive_controls_independent(
        tuple(top_admitted_positives),
        candidates,
        states,
    )

    verdict = _overall_verdict(
        edge_checks=edge_checks,
        join_checks=join_checks,
        path_checks=path_checks,
        hostile_violations=hostile_violations,
        top_positives_independent=top_positives_independent,
    )

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Test whether post-T477 valid-coarse-graining admission is coherent "
            "across a finite observer-budget lattice: no admitted relation is "
            "lost under access expansion, joins are path independent, newly "
            "accessible finality tasks are observer-indexed, and hostile "
            "controls remain blocked when they become accessible."
        ),
        "state_count": len(states),
        "budget_results": budget_results,
        "edge_checks": edge_checks,
        "join_checks": join_checks,
        "path_checks": path_checks,
        "candidate_transition_rows": transition_rows,
        "hostile_violations": hostile_violations,
        "top_budget_admitted_positive_ids": top_admitted_positives,
        "top_budget_positives_independent": top_positives_independent,
        "overall_verdict": verdict,
        "future_packet_minimum": [
            "declare a finite observer-budget poset, not only one chain",
            "report edge monotonicity for admitted finality-natural relations",
            "report join/path checks for incomparable budget expansions",
            "explain every new admission by newly accessible certified record fields",
            "keep cheap arithmetic, label-restatement, microstate, and observer-creates-truth controls blocked at every accessible budget",
            "treat budget-indexed admissions as local review targets, not global valid-coarse-graining criteria",
        ],
        "not_earned": [
            "D1 promotion",
            "T10 superselection result",
            "T29 projection-obstruction promotion",
            "observer-theory equivalence theorem",
            "global valid-coarse-graining criterion",
            "physics or consciousness claim",
            "claim-ledger movement",
            "roadmap movement",
            "public-posture movement",
        ],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """Render T478 results as Markdown."""

    verdict = result["overall_verdict"]
    budget_rows = [
        "| {budget_id} | {accessible_fields} | {admitted} |".format(
            budget_id=row["budget_id"],
            accessible_fields=row["budget"]["accessible_fields"],
            admitted=", ".join(row["admitted_candidate_ids"]) or "none",
        )
        for row in result["budget_results"]
    ]
    edge_rows = [
        "| {from_budget} | {to_budget} | {lost_admissions} | {monotone} |".format(
            from_budget=row["from_budget"],
            to_budget=row["to_budget"],
            lost_admissions=", ".join(row["lost_admissions"]) or "none",
            monotone=row["monotone"],
        )
        for row in result["edge_checks"]
    ]
    join_rows = [
        "| {left_budget} | {right_budget} | {join_budget} | {new_at_join} | {check} |".format(
            left_budget=row["left_budget"],
            right_budget=row["right_budget"],
            join_budget=row["join_budget"],
            new_at_join=", ".join(row["newly_admitted_at_join"]) or "none",
            check=row["path_independent_and_explained"],
        )
        for row in result["join_checks"]
    ]
    transition_rows = [
        "| {candidate_id} | {role} | {required_fields} | {admitted_budgets} | {first_admitted_budgets} |".format(
            candidate_id=row["candidate_id"],
            role=row["role"],
            required_fields=row["required_fields"],
            admitted_budgets=", ".join(row["admitted_budgets"]) or "none",
            first_admitted_budgets=", ".join(row["first_admitted_budgets"]) or "none",
        )
        for row in result["candidate_transition_rows"]
    ]
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T478 - Coarse-Graining Budget-Lattice Gate - v0.1 results",
            "",
            "> Budget-lattice stress gate only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T478-coarse-graining-budget-lattice-gate.md`",
            "- Model: `models/coarse_graining_budget_lattice_gate.py`",
            "- Tests: `tests/test_coarse_graining_budget_lattice_gate.py`",
            "- Artifact JSON: `results/T478-coarse-graining-budget-lattice-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gates: T467, T468, T469, T471, and T477",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Budget Lattice",
            "",
            "| budget | accessible fields | admitted candidates |",
            "| --- | --- | --- |",
            *budget_rows,
            "",
            "## Edge Monotonicity",
            "",
            "| from | to | lost admissions | monotone? |",
            "| --- | --- | --- | --- |",
            *edge_rows,
            "",
            "## Join Checks",
            "",
            "| left | right | join | newly admitted at join | path independent and explained? |",
            "| --- | --- | --- | --- | --- |",
            *join_rows,
            "",
            "## Candidate Transitions",
            "",
            "| candidate | role | required fields | admitted budgets | first admitted budgets |",
            "| --- | --- | --- | --- | --- |",
            *transition_rows,
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


def _candidate(
    *,
    candidate_id: str,
    description: str,
    fields_read: tuple[int, ...],
    predicate_cost: int,
    holder_redundancy: int,
    reversal_cost: int,
    finality_native_task: bool,
    labeler: Labeler,
    evidence: TaskNaturalnessEvidence,
    role: str,
    observer_creates_truth_overread: bool = False,
) -> NaturalnessCandidate:
    return NaturalnessCandidate(
        base=CoarseGrainingCandidate(
            candidate_id=candidate_id,
            description=description,
            fields_read=fields_read,
            predicate_cost=predicate_cost,
            holder_redundancy=holder_redundancy,
            reversal_cost=reversal_cost,
            declared_before_use=True,
            certified_record_available=True,
            finality_native_task=finality_native_task,
            expected_valid=role in {
                "positive_control",
                "observer_index_positive_control",
                "join_positive_control",
            },
            labeler=labeler,
            observer_creates_truth_overread=observer_creates_truth_overread,
        ),
        evidence=evidence,
        role=role,
    )


def _budget_dict(budget: CertificationBudget) -> dict[str, Any]:
    return {
        "accessible_fields": list(budget.accessible_fields),
        "max_fields_read": budget.max_fields_read,
        "max_predicate_cost": budget.max_predicate_cost,
        "min_holder_redundancy": budget.min_holder_redundancy,
        "max_reversal_cost": budget.max_reversal_cost,
    }


def _evaluation_dict(evaluation: Any) -> dict[str, Any]:
    return {
        "candidate_id": evaluation.candidate_id,
        "admitted": evaluation.admitted,
        "decision": evaluation.decision,
        "route_label": evaluation.route_label,
        "blockers": list(evaluation.blockers),
        "base_route_label": evaluation.base_route_label,
        "base_admitted": evaluation.base_admitted,
        "class_count": evaluation.class_count,
        "role": evaluation.role,
    }


def _edge_checks(
    budgets: tuple[tuple[str, CertificationBudget], ...],
    evaluations_by_budget: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for from_id, from_budget in budgets:
        from_fields = set(from_budget.accessible_fields)
        for to_id, to_budget in budgets:
            to_fields = set(to_budget.accessible_fields)
            if len(to_fields) != len(from_fields) + 1:
                continue
            if not from_fields.issubset(to_fields):
                continue
            lost = sorted(
                set(_admitted_ids(evaluations_by_budget[from_id]))
                - set(_admitted_ids(evaluations_by_budget[to_id]))
            )
            rows.append(
                {
                    "from_budget": from_id,
                    "to_budget": to_id,
                    "lost_admissions": lost,
                    "monotone": not lost,
                }
            )
    return rows


def _join_checks(
    budgets: tuple[tuple[str, CertificationBudget], ...],
    evaluations_by_budget: dict[str, dict[str, Any]],
    candidates: dict[str, NaturalnessCandidate],
) -> list[dict[str, Any]]:
    field_to_id = {
        tuple(budget.accessible_fields): budget_id for budget_id, budget in budgets
    }
    rows: list[dict[str, Any]] = []
    for (left_id, left_budget), (right_id, right_budget) in combinations(budgets, 2):
        left_fields = set(left_budget.accessible_fields)
        right_fields = set(right_budget.accessible_fields)
        if left_fields.issubset(right_fields) or right_fields.issubset(left_fields):
            continue
        join_fields = tuple(sorted(left_fields | right_fields))
        join_id = field_to_id.get(join_fields)
        if join_id is None:
            continue
        left_admitted = set(_admitted_ids(evaluations_by_budget[left_id]))
        right_admitted = set(_admitted_ids(evaluations_by_budget[right_id]))
        join_admitted = set(_admitted_ids(evaluations_by_budget[join_id]))
        combined_prior = left_admitted | right_admitted
        newly_admitted = sorted(join_admitted - combined_prior)
        no_prior_loss = combined_prior.issubset(join_admitted)
        new_explained = all(
            set(candidates[candidate_id].base.fields_read).issubset(join_fields)
            for candidate_id in newly_admitted
        )
        rows.append(
            {
                "left_budget": left_id,
                "right_budget": right_id,
                "join_budget": join_id,
                "newly_admitted_at_join": newly_admitted,
                "no_preexisting_admission_loss": no_prior_loss,
                "new_admissions_explained_by_join_budget": new_explained,
                "path_independent_and_explained": no_prior_loss and new_explained,
            }
        )
    return rows


def _path_checks(
    evaluations_by_budget: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    top_id = "budget_0123"
    paths = (
        ("pair01_then_three_then_top", ("budget_01", "budget_012", top_id)),
        ("pair02_then_three_then_top", ("budget_02", "budget_012", top_id)),
        ("boundary_then_013_then_top", ("budget_03", "budget_013", top_id)),
        ("boundary_then_023_then_top", ("budget_03", "budget_023", top_id)),
    )
    top_vector = _admission_vector(evaluations_by_budget[top_id])
    rows: list[dict[str, Any]] = []
    for path_id, path in paths:
        prior_admitted: set[str] = set()
        sequence: list[dict[str, Any]] = []
        for budget_id in path:
            admitted = set(_admitted_ids(evaluations_by_budget[budget_id]))
            sequence.append(
                {
                    "budget_id": budget_id,
                    "newly_admitted": sorted(admitted - prior_admitted),
                    "admitted": sorted(admitted),
                }
            )
            prior_admitted = admitted
        rows.append(
            {
                "path_id": path_id,
                "path": list(path),
                "sequence": sequence,
                "top_vector_matches_direct_top": (
                    _admission_vector(evaluations_by_budget[path[-1]]) == top_vector
                ),
            }
        )
    return rows


def _transition_rows(
    budgets: tuple[tuple[str, CertificationBudget], ...],
    evaluations_by_budget: dict[str, dict[str, Any]],
    candidates: dict[str, NaturalnessCandidate],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for candidate_id, candidate in candidates.items():
        admitted_budgets = [
            budget_id
            for budget_id, _budget in budgets
            if evaluations_by_budget[budget_id][candidate_id]["admitted"]
        ]
        minimal = []
        for budget_id in admitted_budgets:
            fields = set(_budget_fields(budgets, budget_id))
            if not any(
                set(_budget_fields(budgets, other_id)).issubset(fields)
                and set(_budget_fields(budgets, other_id)) != fields
                for other_id in admitted_budgets
            ):
                minimal.append(budget_id)
        rows.append(
            {
                "candidate_id": candidate_id,
                "role": candidate.role,
                "required_fields": list(candidate.base.fields_read),
                "admitted_budgets": admitted_budgets,
                "first_admitted_budgets": minimal,
            }
        )
    return rows


def _hostile_violations(
    budgets: tuple[tuple[str, CertificationBudget], ...],
    evaluations_by_budget: dict[str, dict[str, Any]],
    candidates: dict[str, NaturalnessCandidate],
) -> list[dict[str, Any]]:
    violations: list[dict[str, Any]] = []
    for budget_id, budget in budgets:
        fields = set(budget.accessible_fields)
        for candidate_id, candidate in candidates.items():
            if candidate.role not in {"hostile_control", "forbidden_control"}:
                continue
            if not set(candidate.base.fields_read).issubset(fields):
                continue
            evaluation = evaluations_by_budget[budget_id][candidate_id]
            if evaluation["admitted"]:
                violations.append(
                    {
                        "budget_id": budget_id,
                        "candidate_id": candidate_id,
                        "route_label": evaluation["route_label"],
                    }
                )
    return violations


def _overall_verdict(
    *,
    edge_checks: list[dict[str, Any]],
    join_checks: list[dict[str, Any]],
    path_checks: list[dict[str, Any]],
    hostile_violations: list[dict[str, Any]],
    top_positives_independent: bool,
) -> dict[str, Any]:
    edge_monotone = all(row["monotone"] for row in edge_checks)
    joins_ok = all(row["path_independent_and_explained"] for row in join_checks)
    paths_ok = all(row["top_vector_matches_direct_top"] for row in path_checks)
    hostiles_ok = not hostile_violations
    gate_passed = (
        edge_monotone
        and joins_ok
        and paths_ok
        and hostiles_ok
        and top_positives_independent
    )
    return {
        "verdict": VERDICT,
        "gate_passed": gate_passed,
        "edge_monotonicity_passed": edge_monotone,
        "join_path_independence_passed": joins_ok,
        "top_path_independence_passed": paths_ok,
        "hostile_controls_blocked_when_accessible": hostiles_ok,
        "top_budget_positive_controls_independent": top_positives_independent,
        "claim_ledger_update": "none",
        "d1_promotion_earned": False,
        "t10_promotion_earned": False,
        "t29_promotion_earned": False,
        "observer_theory_identification_earned": False,
        "global_valid_coarse_graining_criterion_earned": False,
        "physics_claim_earned": False,
        "reading": (
            "The repaired coarse-graining packet is coherent across this finite "
            "observer-budget lattice: admitted finality-natural relations do "
            "not disappear under access expansion, joins preserve prior "
            "admissions and admit only relations whose certified fields become "
            "available, and top-budget verdicts are independent of the access "
            "expansion path. Cheap arithmetic, label restatement, microstate "
            "identity, and observer-creates-truth controls remain blocked when "
            "they become accessible. This is an observer-indexed intake "
            "guardrail only, not a global valid-coarse-graining criterion."
        ),
    }


def _admitted_ids(evaluations: dict[str, dict[str, Any]]) -> list[str]:
    return sorted(
        candidate_id
        for candidate_id, evaluation in evaluations.items()
        if evaluation["admitted"]
    )


def _admitted_positive_ids(
    evaluations: dict[str, dict[str, Any]],
    candidates: dict[str, NaturalnessCandidate],
) -> list[str]:
    positive_roles = {
        "positive_control",
        "observer_index_positive_control",
        "join_positive_control",
    }
    return sorted(
        candidate_id
        for candidate_id, evaluation in evaluations.items()
        if evaluation["admitted"] and candidates[candidate_id].role in positive_roles
    )


def _admission_vector(evaluations: dict[str, dict[str, Any]]) -> tuple[tuple[str, bool], ...]:
    return tuple(
        sorted((candidate_id, row["admitted"]) for candidate_id, row in evaluations.items())
    )


def _budget_fields(
    budgets: tuple[tuple[str, CertificationBudget], ...],
    budget_id: str,
) -> tuple[int, ...]:
    for current_id, budget in budgets:
        if current_id == budget_id:
            return budget.accessible_fields
    raise KeyError(budget_id)


def _positive_controls_independent(
    positive_control_ids: tuple[str, ...],
    candidates: dict[str, NaturalnessCandidate],
    states: tuple[State, ...],
) -> bool:
    if len(positive_control_ids) < 2:
        return False
    partitions = [
        _normalized_partition(states, candidates[candidate_id].base.labeler)
        for candidate_id in positive_control_ids
        if candidate_id in candidates
    ]
    return len(partitions) == len(positive_control_ids) and len(set(partitions)) > 1


def _normalized_partition(states: tuple[State, ...], labeler: Labeler) -> Partition:
    classes: dict[str, list[str]] = {}
    for state in states:
        classes.setdefault(labeler(state), []).append(_state_label(state))
    return tuple(sorted(tuple(sorted(members)) for members in classes.values()))


def _finality_band_label(state: State, fields: tuple[int, ...]) -> str:
    observed = tuple(state[field_id] for field_id in fields)
    first = observed[0]
    if all(value == first for value in observed):
        return f"stable_value_{first}"
    return "unsettled"


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
