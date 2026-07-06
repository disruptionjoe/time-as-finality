"""T477: budget-index gate for valid coarse-graining packets.

T467-T471 built and hardened a finite valid-coarse-graining packet. This module
checks whether the admission behavior is genuinely indexed to the declared
observer budget rather than acting as a fixed global whitelist.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable

from models.coarse_graining_task_naturalness_gate import (
    NaturalnessCandidate,
    TaskNaturalnessEvidence,
    evaluate_naturalness_candidate,
    evaluate_packet,
)
from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
    finite_record_states,
)


State = tuple[int, ...]
Labeler = Callable[[State], str]

ARTIFACT_ID = "T477-coarse-graining-budget-index-gate-v0.1"
VERDICT = "BUDGET_INDEX_GATE_BUILT_OBSERVER_INDEXED_NO_PROMOTION"


def three_holder_budget() -> CertificationBudget:
    """Return the T469/T471 local three-holder observer budget."""

    return CertificationBudget(
        accessible_fields=(0, 1, 2),
        max_fields_read=3,
        max_predicate_cost=4,
        min_holder_redundancy=2,
        max_reversal_cost=2,
    )


def four_holder_budget() -> CertificationBudget:
    """Return an expanded observer budget that includes the fourth holder."""

    return CertificationBudget(
        accessible_fields=(0, 1, 2, 3),
        max_fields_read=4,
        max_predicate_cost=4,
        min_holder_redundancy=2,
        max_reversal_cost=2,
    )


def budget_catalogue() -> tuple[tuple[str, CertificationBudget], ...]:
    """Return the nested observer budgets used by T477."""

    return (
        ("three_holder_budget", three_holder_budget()),
        ("four_holder_budget", four_holder_budget()),
    )


def budget_candidates() -> tuple[NaturalnessCandidate, ...]:
    """Return the candidate catalogue evaluated across nested budgets."""

    return (
        _candidate(
            candidate_id="three_holder_finality_band",
            description=(
                "Three accessible holders certify one stable value or an "
                "unsettled mixed-status class."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="three_holder_finality_status_band",
                certified_record_object="three_holder_finalized_value_status",
                declared_before_relation=True,
                preserves_record_value_or_support=True,
                semantics_not_label_restatement=True,
                demotion_condition_declared=True,
            ),
            role="positive_control",
        ),
        _candidate(
            candidate_id="three_holder_support_count",
            description=(
                "Three accessible holders certify finalized-support "
                "multiplicity."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=2,
            finality_native_task=True,
            labeler=lambda state: f"support_count_{sum(state[:3])}",
            evidence=TaskNaturalnessEvidence(
                task_family="three_holder_support_multiplicity",
                certified_record_object="three_holder_support_count",
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
                "A record task comparing holder zero with the fourth holder; "
                "blocked until the observer budget includes the fourth holder."
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
            candidate_id="cheap_accessible_parity_with_task_label",
            description=(
                "A cheap accessible arithmetic partition with a finality-task "
                "label asserted."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: f"parity_{sum(state[:3]) % 2}",
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
            description="A bounded lookup whose task account restates labels.",
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
            description="A full microstate identity relation over all holders.",
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
            description=(
                "A forbidden packet that treats observer equivalencing as "
                "truth creation."
            ),
            fields_read=(0, 1, 2),
            predicate_cost=3,
            holder_redundancy=3,
            reversal_cost=1,
            finality_native_task=True,
            labeler=lambda state: _finality_band_label(state, width=3),
            evidence=TaskNaturalnessEvidence(
                task_family="observer_makes_truth",
                certified_record_object="three_holder_record",
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
    """Run the T477 budget-index gate."""

    states = finite_record_states(width=4)
    candidates = {
        candidate.base.candidate_id: candidate for candidate in budget_candidates()
    }
    budget_results: list[dict[str, Any]] = []
    all_evaluations: dict[str, dict[str, Any]] = {}

    for budget_id, budget in budget_catalogue():
        evaluations = {
            candidate_id: evaluate_naturalness_candidate(candidate, budget, states)
            for candidate_id, candidate in candidates.items()
        }
        packet = evaluate_packet(
            packet_id=f"{budget_id}_packet",
            candidate_ids=tuple(candidates),
            positive_control_ids=_positive_control_ids(budget_id),
            hostile_control_ids=(
                "cheap_accessible_parity_with_task_label",
                "label_restatement_lookup",
                "microstate_identity",
                "observer_creates_truth_overread",
            ),
            candidates=candidates,
            evaluations=evaluations,
            states=states,
        )
        all_evaluations[budget_id] = {
            evaluation.candidate_id: _evaluation_dict(evaluation)
            for evaluation in evaluations.values()
        }
        budget_results.append(
            {
                "budget_id": budget_id,
                "budget": _budget_dict(budget),
                "candidate_evaluations": [
                    _evaluation_dict(evaluation)
                    for evaluation in evaluations.values()
                ],
                "packet_evaluation": _packet_dict(packet),
            }
        )

    transitions = _transition_rows(all_evaluations)
    verdict = _overall_verdict(all_evaluations, budget_results)

    return {
        "artifact_id": ARTIFACT_ID,
        "objective": (
            "Test whether valid coarse-graining admission is indexed to the "
            "observer budget: local positives persist under budget expansion, "
            "a boundary-pair record becomes admissible only when the boundary "
            "field enters access, and non-finality hostiles remain blocked."
        ),
        "state_count": len(states),
        "budget_results": budget_results,
        "budget_transition_rows": transitions,
        "overall_verdict": verdict,
        "future_packet_minimum": [
            "declare the observer budget before selecting the relation",
            "report budget transitions for every candidate relation",
            "treat newly accessible record tasks as observer-indexed admissions, not global criteria",
            "show that cheap arithmetic and label-restatement controls remain blocked under expanded budgets",
            "keep microstate identity and observer-creates-truth overreads blocked before claim movement",
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
    """Render T477 results as Markdown."""

    verdict = result["overall_verdict"]
    budget_sections: list[str] = []
    for budget_result in result["budget_results"]:
        candidate_rows = []
        for row in budget_result["candidate_evaluations"]:
            blockers = ", ".join(row["blockers"]) or "none"
            candidate_rows.append(
                "| {candidate_id} | {role} | {decision} | {route_label} | "
                "{base_route_label} | {blockers} |".format(
                    candidate_id=row["candidate_id"],
                    role=row["role"],
                    decision=row["decision"],
                    route_label=row["route_label"],
                    base_route_label=row["base_route_label"],
                    blockers=blockers,
                )
            )
        packet = budget_result["packet_evaluation"]
        packet_blockers = ", ".join(packet["blockers"]) or "none"
        budget_sections.extend(
            [
                f"## Budget: {budget_result['budget_id']}",
                "",
                "- accessible fields: `{}`".format(
                    budget_result["budget"]["accessible_fields"]
                ),
                f"- packet decision: `{packet['decision']}`",
                f"- packet route: `{packet['route_label']}`",
                f"- packet blockers: `{packet_blockers}`",
                "",
                "| candidate | role | decision | route | base route | blockers |",
                "| --- | --- | --- | --- | --- | --- |",
                *candidate_rows,
                "",
            ]
        )

    transition_rows = []
    for row in result["budget_transition_rows"]:
        transition_rows.append(
            "| {candidate_id} | {three_holder_route} | {four_holder_route} | "
            "{transition} |".format(**row)
        )

    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T477 - Coarse-Graining Budget-Index Gate - v0.1 results",
            "",
            "> Budget-index stress gate only. No claim status, roadmap, README, "
            "North Star, public-posture, hard-policy, or cross-repo movement.",
            "",
            "- Spec: `tests/T477-coarse-graining-budget-index-gate.md`",
            "- Model: `models/coarse_graining_budget_index_gate.py`",
            "- Tests: `tests/test_coarse_graining_budget_index_gate.py`",
            "- Artifact JSON: `results/T477-coarse-graining-budget-index-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gates: T467, T468, T469, and T471",
            "",
            f"## Overall verdict: {verdict['verdict']}",
            "",
            verdict["reading"],
            "",
            "## Budget Transitions",
            "",
            "| candidate | three-holder route | four-holder route | transition |",
            "| --- | --- | --- | --- |",
            *transition_rows,
            "",
            *budget_sections,
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


def _positive_control_ids(budget_id: str) -> tuple[str, ...]:
    controls = (
        "three_holder_finality_band",
        "three_holder_support_count",
    )
    if budget_id == "four_holder_budget":
        return controls + ("boundary_pair_status",)
    return controls


def _overall_verdict(
    all_evaluations: dict[str, dict[str, Any]],
    budget_results: list[dict[str, Any]],
) -> dict[str, Any]:
    three = all_evaluations["three_holder_budget"]
    four = all_evaluations["four_holder_budget"]

    local_positives_persist = all(
        three[candidate_id]["admitted"] and four[candidate_id]["admitted"]
        for candidate_id in (
            "three_holder_finality_band",
            "three_holder_support_count",
        )
    )
    boundary_pair_is_budget_indexed = (
        not three["boundary_pair_status"]["admitted"]
        and three["boundary_pair_status"]["base_route_label"]
        == "INACCESSIBLE_RECORD_FIELD"
        and four["boundary_pair_status"]["admitted"]
    )
    hostile_controls_stay_blocked = all(
        not four[candidate_id]["admitted"]
        for candidate_id in (
            "cheap_accessible_parity_with_task_label",
            "label_restatement_lookup",
            "microstate_identity",
            "observer_creates_truth_overread",
        )
    )
    packets_admitted = all(
        budget_result["packet_evaluation"]["admitted"]
        for budget_result in budget_results
    )

    return {
        "verdict": VERDICT,
        "local_positives_persist_under_expansion": local_positives_persist,
        "boundary_pair_routes_by_observer_budget": boundary_pair_is_budget_indexed,
        "hostile_controls_stay_blocked_under_expansion": hostile_controls_stay_blocked,
        "all_budget_packets_admitted_for_review": packets_admitted,
        "claim_ledger_update": "none",
        "d1_promotion_earned": False,
        "t10_promotion_earned": False,
        "t29_promotion_earned": False,
        "observer_theory_identification_earned": False,
        "physics_claim_earned": False,
        "reading": (
            "The repaired valid-coarse-graining packet is observer-budget "
            "indexed. Three-holder positives persist when the observer budget "
            "expands; the boundary-pair record is rejected as inaccessible "
            "under the three-holder budget and admitted only after the fourth "
            "holder enters the declared access boundary. Cheap arithmetic, "
            "label restatement, microstate identity, and observer-creates-truth "
            "controls remain blocked under expanded access. This is a "
            "budget-index guardrail only, not an Observer Theory equivalence "
            "theorem or claim promotion."
        ),
    }


def _transition_rows(
    all_evaluations: dict[str, dict[str, Any]],
) -> list[dict[str, str]]:
    three = all_evaluations["three_holder_budget"]
    four = all_evaluations["four_holder_budget"]
    rows: list[dict[str, str]] = []
    for candidate_id in three:
        three_admitted = three[candidate_id]["admitted"]
        four_admitted = four[candidate_id]["admitted"]
        if three_admitted and four_admitted:
            transition = "persists_admitted"
        elif not three_admitted and four_admitted:
            transition = "observer_budget_reveals_new_admission"
        elif not three_admitted and not four_admitted:
            transition = "stays_blocked"
        else:
            transition = "loses_admission_under_expansion"
        rows.append(
            {
                "candidate_id": candidate_id,
                "three_holder_route": three[candidate_id]["route_label"],
                "four_holder_route": four[candidate_id]["route_label"],
                "transition": transition,
            }
        )
    return rows


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
            },
            labeler=labeler,
            observer_creates_truth_overread=observer_creates_truth_overread,
        ),
        evidence=evidence,
        role=role,
    )


def _finality_band_label(state: State, width: int) -> str:
    observed = state[:width]
    first = observed[0]
    if all(value == first for value in observed):
        return f"stable_value_{first}"
    return "unsettled"


def _state_label(state: State) -> str:
    return "".join(str(bit) for bit in state)


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


def _packet_dict(packet: Any) -> dict[str, Any]:
    return {
        "packet_id": packet.packet_id,
        "admitted": packet.admitted,
        "decision": packet.decision,
        "route_label": packet.route_label,
        "blockers": list(packet.blockers),
        "positive_control_ids": list(packet.positive_control_ids),
        "positive_controls_independent": packet.positive_controls_independent,
        "hostile_control_ids": list(packet.hostile_control_ids),
        "hostile_controls_blocked": packet.hostile_controls_blocked,
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
