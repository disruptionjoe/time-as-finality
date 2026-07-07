"""T503: Knuth-Bendix-style finality admission gate.

The Gorard intake suggested a concrete rival model for finality: a branching
rewrite system becomes one authoritative history by a completion/confluence
operation. This module does not import Wolfram-model physics. It makes the
shape executable against existing repo objects: T61 reconciliation/conflict
fixtures and the T467/T489 valid-coarse-graining admission/closure gates.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from models.mmo_reconciliation_finality import run_t61_analysis
from models.valid_coarse_graining_admissibility_gate import (
    CertificationBudget,
    CoarseGrainingCandidate,
    evaluate_candidate,
    finite_record_states,
)


ARTIFACT_ID = "T503-knuth-bendix-finality-admission-gate-v0.1"
VERDICT = "REWRITE_COMPLETION_FINALITY_GATE_BUILT_REFINES_D1_REVIEW_ONLY"
COMPLETION_RULE_BUDGET = 2


@dataclass(frozen=True)
class RewriteRule:
    rule_id: str
    source: str
    target: str
    added_by_completion: bool = False
    requires_hidden_authority: bool = False


@dataclass(frozen=True)
class RewriteCompletionCase:
    case_id: str
    description: str
    t61_anchor: str | None
    start_terms: tuple[str, ...]
    rules: tuple[RewriteRule, ...]
    candidate: CoarseGrainingCandidate
    expected_relationship: str
    completion_rule_budget: int = COMPLETION_RULE_BUDGET


@dataclass(frozen=True)
class CompletionEvaluation:
    case_id: str
    t61_anchor: str | None
    rewrite_terminates: bool
    rewrite_confluent_to_single_normal_form: bool
    completion_cost: int
    completion_within_budget: bool
    completion_admitted: bool
    d1_admitted: bool
    d1_route_label: str
    relationship: str
    normal_forms_by_start: tuple[tuple[str, tuple[str, ...]], ...]
    terminal_normal_forms: tuple[str, ...]
    hidden_completion_rule_used: bool
    route_label: str
    counts_as_claim_evidence: bool


def run() -> dict[str, Any]:
    """Run T503 and return a serializable result."""

    t61_anchor = _t61_anchor()
    states = finite_record_states()
    budget = CertificationBudget()
    cases = completion_cases()
    evaluations = tuple(
        evaluate_completion_case(case, budget, states) for case in cases
    )
    by_relationship = _relationship_index(evaluations)
    t61_cases_ok = all(
        item.relationship == "coincident_admission"
        for item in evaluations
        if item.t61_anchor is not None
    )
    completion_refines_d1 = bool(by_relationship["completion_refines_d1"])
    completion_not_sufficient = bool(by_relationship["completion_not_sufficient"])

    return {
        "artifact_id": ARTIFACT_ID,
        "verdict": VERDICT,
        "source_status": {
            "gorard_sources": "abstract-level arXiv anchors checked; no theorem imported",
            "knuth_bendix_use": "style/analogy for finite completion-confluence gate only",
            "repo_objects": ["T61", "T55", "T467", "T489"],
        },
        "objective": (
            "Test whether a finite rewrite-completion/confluence criterion adds "
            "new branch/cost structure beyond the existing D1-style bounded "
            "observer certification gate."
        ),
        "t61_anchor": t61_anchor,
        "completion_rule_budget": COMPLETION_RULE_BUDGET,
        "cases": [_case_dict(case) for case in cases],
        "evaluations": [_evaluation_dict(item) for item in evaluations],
        "relationship_index": by_relationship,
        "overall": {
            "t61_anchor_cases_remain_admitted_by_both": t61_cases_ok,
            "completion_refines_d1_on_branch_or_cost_controls": completion_refines_d1,
            "completion_alone_is_not_sufficient_without_d1_access": completion_not_sufficient,
            "t489_route": "future_domain_native_cost_certifiability_review_target_only",
            "t489_thread_reopened_as_claim_evidence": False,
            "domain_native_theorem_supplied": False,
            "claim_ledger_update": "none",
            "d1_t10_t29_promotion_earned": False,
            "observer_theory_equivalence_earned": False,
            "global_valid_coarse_graining_criterion_earned": False,
            "physics_or_wolfram_model_claim_earned": False,
            "public_posture_movement": False,
            "cross_repo_truth_movement": False,
            "strongest_reading": (
                "A finite rewrite-completion check is useful as an intake gate: "
                "T61-style confirmed and rollback branches normalize cleanly, "
                "while accessible but nonconfluent, cyclic, or over-budget "
                "branch systems are D1-admissible yet completion-rejected. "
                "Conversely, a confluent hidden-authority or microstate case is "
                "not TaF-admissible without the certified-record/access guards. "
                "So completion refines D1 for branching/cost controls, but it "
                "does not replace D1 and does not prove Observer Theory/TaF identity."
            ),
        },
        "future_packet_minimum": [
            "verify primary Gorard/Wolfram sources before load-bearing use",
            "cite T489 and state why T467-T478 budget-lattice closure is insufficient",
            "declare the finite abstract rewrite system before scoring",
            "report termination, single-normal-form confluence, and completion-rule cost",
            "compare the completion verdict against D1 bounded-observer certification on the same cases",
            "include D1-admitted but nonconfluent/cyclic/over-budget hostile controls",
            "include completion-confluent but D1-inaccessible or too-fine hostile controls",
            "keep admission review-only until a domain-native cost/certifiability theorem is supplied",
        ],
        "not_earned": [
            "Knuth-Bendix theorem inside TaF",
            "direct Observer Theory/TaF equivalence theorem",
            "global valid-coarse-graining criterion",
            "D1/T10/T29 promotion",
            "Wolfram-model physics claim",
            "claim-ledger movement",
            "roadmap movement",
            "README movement",
            "North Star movement",
            "public-posture movement",
            "hard-policy movement",
            "protected-license movement",
            "external publication",
            "cross-repo truth movement",
        ],
    }


def completion_cases() -> tuple[RewriteCompletionCase, ...]:
    return (
        RewriteCompletionCase(
            case_id="t61_positive_prediction_completion",
            description=(
                "T61 positive branch: client prediction and authority commit "
                "normalize to one reconciled history."
            ),
            t61_anchor="positive_prediction_confirmed",
            start_terms=("client_pred_move_a", "authority_commit_move_a"),
            rules=(
                RewriteRule(
                    "prediction_confirmed_by_authority",
                    "client_pred_move_a",
                    "authority_commit_move_a",
                ),
                RewriteRule(
                    "authority_commit_reconciles_client",
                    "authority_commit_move_a",
                    "reconciled_move_a",
                    added_by_completion=True,
                ),
            ),
            candidate=_finality_band_candidate("t61_positive_finality_band"),
            expected_relationship="coincident_admission",
        ),
        RewriteCompletionCase(
            case_id="t61_conflict_rollback_completion",
            description=(
                "T61 failure branch: incompatible stale predictions normalize "
                "only after explicit rollback/conflict completion."
            ),
            t61_anchor="failure_stale_conflicting_prediction",
            start_terms=("client_a_claim_gem", "client_b_claim_gem"),
            rules=(
                RewriteRule(
                    "client_a_claim_wins_authority",
                    "client_a_claim_gem",
                    "authority_claim_a",
                ),
                RewriteRule(
                    "client_b_claim_rolls_back",
                    "client_b_claim_gem",
                    "rollback_claim_b",
                ),
                RewriteRule(
                    "winner_enters_resolved_thread",
                    "authority_claim_a",
                    "resolved_claim_a_with_rollback_b",
                    added_by_completion=True,
                ),
                RewriteRule(
                    "rollback_enters_resolved_thread",
                    "rollback_claim_b",
                    "resolved_claim_a_with_rollback_b",
                    added_by_completion=True,
                ),
            ),
            candidate=_support_count_candidate("t61_rollback_support_count"),
            expected_relationship="coincident_admission",
        ),
        RewriteCompletionCase(
            case_id="accessible_two_normal_forms_no_join",
            description=(
                "Accessible certified branches terminate, but they keep two "
                "normal forms because no completion rule joins them."
            ),
            t61_anchor=None,
            start_terms=("branch_left", "branch_right"),
            rules=(
                RewriteRule("left_settles", "branch_left", "normal_left"),
                RewriteRule("right_settles", "branch_right", "normal_right"),
            ),
            candidate=_finality_band_candidate("accessible_nonconfluent_band"),
            expected_relationship="completion_refines_d1",
        ),
        RewriteCompletionCase(
            case_id="accessible_cycle_no_final_normal_form",
            description=(
                "Accessible certified branches cycle under rewrite, so the "
                "observer has no terminating completion."
            ),
            t61_anchor=None,
            start_terms=("cycle_a",),
            rules=(
                RewriteRule("cycle_a_to_b", "cycle_a", "cycle_b"),
                RewriteRule("cycle_b_to_a", "cycle_b", "cycle_a"),
            ),
            candidate=_finality_band_candidate("accessible_cycle_band"),
            expected_relationship="completion_refines_d1",
        ),
        RewriteCompletionCase(
            case_id="accessible_over_budget_completion",
            description=(
                "The branches are finitely joinable, but require more completion "
                "rules than the declared observer budget permits."
            ),
            t61_anchor=None,
            start_terms=("branch_0", "branch_1", "branch_2"),
            rules=(
                RewriteRule("join_branch_0", "branch_0", "joined", added_by_completion=True),
                RewriteRule("join_branch_1", "branch_1", "joined", added_by_completion=True),
                RewriteRule("join_branch_2", "branch_2", "joined", added_by_completion=True),
            ),
            candidate=_support_count_candidate("accessible_over_budget_support_count"),
            expected_relationship="completion_refines_d1",
        ),
        RewriteCompletionCase(
            case_id="hidden_authority_completion_shortcut",
            description=(
                "A hidden authority rule makes the rewrite system confluent, "
                "but the required record field is outside the observer budget."
            ),
            t61_anchor=None,
            start_terms=("hidden_left", "hidden_right"),
            rules=(
                RewriteRule(
                    "hidden_left_authority_join",
                    "hidden_left",
                    "hidden_authority_normal",
                    requires_hidden_authority=True,
                ),
                RewriteRule(
                    "hidden_right_authority_join",
                    "hidden_right",
                    "hidden_authority_normal",
                    requires_hidden_authority=True,
                ),
            ),
            candidate=_hidden_field_candidate("hidden_authority_record"),
            expected_relationship="completion_not_sufficient",
        ),
        RewriteCompletionCase(
            case_id="microstate_identity_completion_shortcut",
            description=(
                "A single microstate is trivially normal, but the corresponding "
                "coarse-graining is full state identity."
            ),
            t61_anchor=None,
            start_terms=("state_0101",),
            rules=(),
            candidate=_microstate_identity_candidate("microstate_identity_completion"),
            expected_relationship="completion_not_sufficient",
        ),
    )


def evaluate_completion_case(
    case: RewriteCompletionCase,
    budget: CertificationBudget,
    states: tuple[tuple[int, ...], ...],
) -> CompletionEvaluation:
    adjacency = _adjacency(case.rules)
    reachable = {
        start: _reachable_from(start, adjacency)
        for start in case.start_terms
    }
    normal_forms_by_start = tuple(
        (
            start,
            tuple(sorted(term for term in terms if not adjacency.get(term))),
        )
        for start, terms in reachable.items()
    )
    terminal_normal_forms = tuple(
        sorted({term for _start, terms in normal_forms_by_start for term in terms})
    )
    terminates = not _has_reachable_cycle(adjacency, case.start_terms)
    confluent = terminates and len(terminal_normal_forms) == 1
    completion_cost = sum(1 for rule in case.rules if rule.added_by_completion)
    within_budget = completion_cost <= case.completion_rule_budget
    completion_admitted = confluent and within_budget
    d1_evaluation = evaluate_candidate(case.candidate, budget, states)
    d1_admitted = d1_evaluation.admitted
    relationship = _relationship(completion_admitted, d1_admitted)
    hidden_used = any(rule.requires_hidden_authority for rule in case.rules)

    return CompletionEvaluation(
        case_id=case.case_id,
        t61_anchor=case.t61_anchor,
        rewrite_terminates=terminates,
        rewrite_confluent_to_single_normal_form=confluent,
        completion_cost=completion_cost,
        completion_within_budget=within_budget,
        completion_admitted=completion_admitted,
        d1_admitted=d1_admitted,
        d1_route_label=d1_evaluation.route_label,
        relationship=relationship,
        normal_forms_by_start=normal_forms_by_start,
        terminal_normal_forms=terminal_normal_forms,
        hidden_completion_rule_used=hidden_used,
        route_label=_route_label(relationship, hidden_used, within_budget, confluent, terminates),
        counts_as_claim_evidence=False,
    )


def render_markdown(result: dict[str, Any]) -> str:
    rows = []
    for item in result["evaluations"]:
        normals = ", ".join(item["terminal_normal_forms"]) or "none"
        rows.append(
            "| {case_id} | {completion} | {d1} | {relationship} | {route} | {cost} | {normals} |".format(
                case_id=item["case_id"],
                completion="yes" if item["completion_admitted"] else "no",
                d1="yes" if item["d1_admitted"] else "no",
                relationship=item["relationship"],
                route=item["route_label"],
                cost=item["completion_cost"],
                normals=normals,
            )
        )
    minimum = [f"- {item}" for item in result["future_packet_minimum"]]
    not_earned = [f"- {item}" for item in result["not_earned"]]

    return "\n".join(
        [
            "# T503 - Knuth-Bendix-Style Finality Admission Gate - v0.1 results",
            "",
            "> Rewrite-completion intake gate only. No claim-ledger, roadmap, README, "
            "North Star, public-posture, hard-policy, protected-license, "
            "external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T503-knuth-bendix-finality-admission-gate.md`",
            "- Model: `models/knuth_bendix_finality_admission_gate.py`",
            "- Tests: `tests/test_knuth_bendix_finality_admission_gate.py`",
            "- Artifact JSON: `results/T503-knuth-bendix-finality-admission-gate-v0.1.json`",
            "- Source open problem: `open-problems/valid-coarse-graining-as-finality-admissibility.md`",
            "- Prior gates: T61, T467, T489",
            "",
            f"## Overall verdict: {result['verdict']}",
            "",
            result["overall"]["strongest_reading"],
            "",
            "## Source Status",
            "",
            f"- Gorard sources: {result['source_status']['gorard_sources']}",
            f"- Knuth-Bendix use: {result['source_status']['knuth_bendix_use']}",
            "",
            "## Gate Table",
            "",
            "| case | completion admitted? | D1 admitted? | relationship | route | completion cost | terminal forms |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## T489 Status",
            "",
            f"- Route: `{result['overall']['t489_route']}`",
            f"- Thread reopened as claim evidence: `{result['overall']['t489_thread_reopened_as_claim_evidence']}`",
            f"- Domain-native theorem supplied: `{result['overall']['domain_native_theorem_supplied']}`",
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


def _t61_anchor() -> dict[str, Any]:
    result = run_t61_analysis()
    positive = result.positive_witness
    failure = result.failure_witness
    conflict = failure.conflict_completion
    anchor_ok = (
        positive.classification == "reconciled_without_contradiction"
        and failure.classification == "rollback_required_conflict_handled"
        and conflict is not None
        and conflict.classification == "canonical"
        and conflict.theorem_applies is True
        and "does not justify a new named claim" in result.claim_classification
    )
    return {
        "anchor_ok": anchor_ok,
        "positive_classification": positive.classification,
        "failure_classification": failure.classification,
        "failure_conflict_classification": None if conflict is None else conflict.classification,
        "failure_conflict_theorem_applies": None if conflict is None else conflict.theorem_applies,
        "claim_classification": result.claim_classification,
    }


def _finality_band_candidate(candidate_id: str) -> CoarseGrainingCandidate:
    return CoarseGrainingCandidate(
        candidate_id=candidate_id,
        description="Two accessible holders certify stable zero, stable one, or unsettled mismatch.",
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
    )


def _support_count_candidate(candidate_id: str) -> CoarseGrainingCandidate:
    return CoarseGrainingCandidate(
        candidate_id=candidate_id,
        description="Two accessible holders certify the local support count.",
        fields_read=(0, 1),
        predicate_cost=2,
        holder_redundancy=2,
        reversal_cost=2,
        declared_before_use=True,
        certified_record_available=True,
        finality_native_task=True,
        expected_valid=True,
        labeler=lambda state: f"count_{state[0] + state[1]}",
    )


def _hidden_field_candidate(candidate_id: str) -> CoarseGrainingCandidate:
    return CoarseGrainingCandidate(
        candidate_id=candidate_id,
        description="The rewrite join depends on an authority field outside the observer boundary.",
        fields_read=(0, 3),
        predicate_cost=2,
        holder_redundancy=2,
        reversal_cost=1,
        declared_before_use=True,
        certified_record_available=True,
        finality_native_task=True,
        expected_valid=False,
        labeler=lambda state: f"visible_hidden_{state[0]}_{state[3]}",
    )


def _microstate_identity_candidate(candidate_id: str) -> CoarseGrainingCandidate:
    return CoarseGrainingCandidate(
        candidate_id=candidate_id,
        description="The equivalence relation is full microstate identity.",
        fields_read=(0, 1, 2, 3),
        predicate_cost=4,
        holder_redundancy=4,
        reversal_cost=4,
        declared_before_use=True,
        certified_record_available=True,
        finality_native_task=True,
        expected_valid=False,
        labeler=lambda state: "state_" + "".join(str(bit) for bit in state),
    )


def _adjacency(rules: tuple[RewriteRule, ...]) -> dict[str, tuple[str, ...]]:
    graph: dict[str, list[str]] = {}
    for rule in rules:
        graph.setdefault(rule.source, []).append(rule.target)
        graph.setdefault(rule.target, [])
    return {node: tuple(targets) for node, targets in graph.items()}


def _reachable_from(start: str, adjacency: dict[str, tuple[str, ...]]) -> frozenset[str]:
    seen = {start}
    queue = [start]
    while queue:
        node = queue.pop(0)
        for target in adjacency.get(node, ()):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return frozenset(seen)


def _has_reachable_cycle(
    adjacency: dict[str, tuple[str, ...]],
    starts: tuple[str, ...],
) -> bool:
    visited: set[str] = set()
    active: set[str] = set()

    def visit(node: str) -> bool:
        if node in active:
            return True
        if node in visited:
            return False
        active.add(node)
        for target in adjacency.get(node, ()):
            if visit(target):
                return True
        active.remove(node)
        visited.add(node)
        return False

    return any(visit(start) for start in starts)


def _relationship(completion_admitted: bool, d1_admitted: bool) -> str:
    if completion_admitted and d1_admitted:
        return "coincident_admission"
    if not completion_admitted and d1_admitted:
        return "completion_refines_d1"
    if completion_admitted and not d1_admitted:
        return "completion_not_sufficient"
    return "coincident_rejection"


def _route_label(
    relationship: str,
    hidden_used: bool,
    within_budget: bool,
    confluent: bool,
    terminates: bool,
) -> str:
    if relationship == "coincident_admission":
        return "ADMITTED_BY_D1_AND_COMPLETION_REVIEW_ONLY"
    if relationship == "completion_refines_d1":
        if not terminates:
            return "COMPLETION_REJECTS_D1_ADMITTED_CYCLE"
        if not confluent:
            return "COMPLETION_REJECTS_D1_ADMITTED_NONCONFLUENCE"
        if not within_budget:
            return "COMPLETION_REJECTS_D1_ADMITTED_OVER_BUDGET_JOIN"
        return "COMPLETION_REFINES_D1"
    if relationship == "completion_not_sufficient":
        if hidden_used:
            return "D1_REJECTS_HIDDEN_COMPLETION_SHORTCUT"
        return "D1_REJECTS_COMPLETION_ONLY_MICROSTATE_OR_ACCESS_SHORTCUT"
    return "REJECTED_BY_D1_AND_COMPLETION"


def _relationship_index(
    evaluations: tuple[CompletionEvaluation, ...],
) -> dict[str, list[str]]:
    keys = (
        "coincident_admission",
        "completion_refines_d1",
        "completion_not_sufficient",
        "coincident_rejection",
    )
    indexed = {key: [] for key in keys}
    for item in evaluations:
        indexed[item.relationship].append(item.case_id)
    return indexed


def _case_dict(case: RewriteCompletionCase) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "description": case.description,
        "t61_anchor": case.t61_anchor,
        "start_terms": list(case.start_terms),
        "rules": [
            {
                "rule_id": rule.rule_id,
                "source": rule.source,
                "target": rule.target,
                "added_by_completion": rule.added_by_completion,
                "requires_hidden_authority": rule.requires_hidden_authority,
            }
            for rule in case.rules
        ],
        "candidate_id": case.candidate.candidate_id,
        "expected_relationship": case.expected_relationship,
        "completion_rule_budget": case.completion_rule_budget,
    }


def _evaluation_dict(item: CompletionEvaluation) -> dict[str, Any]:
    return {
        "case_id": item.case_id,
        "t61_anchor": item.t61_anchor,
        "rewrite_terminates": item.rewrite_terminates,
        "rewrite_confluent_to_single_normal_form": (
            item.rewrite_confluent_to_single_normal_form
        ),
        "completion_cost": item.completion_cost,
        "completion_within_budget": item.completion_within_budget,
        "completion_admitted": item.completion_admitted,
        "d1_admitted": item.d1_admitted,
        "d1_route_label": item.d1_route_label,
        "relationship": item.relationship,
        "normal_forms_by_start": [
            {"start": start, "normal_forms": list(forms)}
            for start, forms in item.normal_forms_by_start
        ],
        "terminal_normal_forms": list(item.terminal_normal_forms),
        "hidden_completion_rule_used": item.hidden_completion_rule_used,
        "route_label": item.route_label,
        "counts_as_claim_evidence": item.counts_as_claim_evidence,
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
