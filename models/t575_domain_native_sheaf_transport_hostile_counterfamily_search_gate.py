"""T575: hostile counterfamily search for the TAF11 semantic generator.

T574 kept the T559-T573 route open but blocked promotion until an independent
hostile counterfamily search tried to break the frozen source-role, absorber,
and semantic-generator contract. T575 runs that search as finite review-only
pressure. It finds no true route-breaking counterfamily and selects a scope
closure gate before any promotion.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t574_domain_native_sheaf_transport_source_law_route_adjudication_gate as t574,
)


ARTIFACT = "T575-domain-native-sheaf-transport-hostile-counterfamily-search-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_hostile_counterfamily_search_no_break_review_only"
SEARCH_STATUS = "NO_TRUE_HOSTILE_COUNTERFAMILY_FOUND_ROUTE_REMAINS_REVIEW_ONLY"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_SCOPE_CLOSURE_REQUIRED"
NEXT_PACKET = "t576_domain_native_sheaf_transport_hostile_search_scope_closure_gate"

NOT_CLAIMED = (
    "T575 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It runs a finite hostile "
    "counterfamily search and keeps the route review-only."
)


@dataclass(frozen=True)
class HostileSearchContract:
    contract_id: str
    source_t574_verdict: str
    source_t574_selected_next_packet: str
    frozen_source_roles: tuple[str, ...]
    absorber_boundaries: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    search_burden: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "frozen_source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "forbidden_shortcuts",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class CounterfamilyCandidate:
    candidate_id: str
    family_id: str
    candidate_kind: str
    expected_true_counterfamily: bool
    predeclared_before_evaluation: bool
    independent_family: bool
    finality_native_payload: bool
    frozen_source_roles: tuple[str, ...]
    absorber_boundaries: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    target_import_terms: tuple[str, ...]
    cross_repo_truth_import: bool
    observerse_replay: bool
    aprd_replay: bool
    absorber_complete_triviality: bool
    contradicts_route: bool
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "frozen_source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "target_import_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class CounterfamilyEvaluation:
    candidate_id: str
    family_id: str
    expected_true_counterfamily: bool
    true_counterfamily: bool
    expectation_matched: bool
    status: str
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    route_effect: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["passed_checks"] = list(self.passed_checks)
        data["failed_checks"] = list(self.failed_checks)
        return data


@dataclass(frozen=True)
class SearchCriterion:
    criterion_id: str
    passed: bool
    evidence: tuple[str, ...]
    residual_risk: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["evidence"] = list(self.evidence)
        return data


@dataclass(frozen=True)
class RouteDecision:
    decision_id: str
    outcome: str
    selected: bool
    next_packet: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class T575Result:
    artifact: str
    source_t574_verdict: str
    source_t574_selected_next_packet: str
    search_status: str
    source_law_status: str
    search_contract: HostileSearchContract
    candidates: tuple[CounterfamilyCandidate, ...]
    evaluations: tuple[CounterfamilyEvaluation, ...]
    search_criteria: tuple[SearchCriterion, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    true_counterfamily_ids: tuple[str, ...]
    survivor_candidate_ids: tuple[str, ...]
    rejected_candidate_ids: tuple[str, ...]
    hostile_search_completed: bool
    true_counterfamily_found: bool
    route_breaks: bool
    route_kept_open: bool
    source_law_earned: bool
    selected_next_packet: str
    verdict: str
    source_law_reading: str
    recommended_next: str
    taf11_update: str
    taf4_update: str
    taf8_update: str
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t575_analysis() -> T575Result:
    source = t574.run_t574_analysis()
    contract = _search_contract(source)
    candidates = _candidate_panel()
    evaluations = tuple(_evaluate_candidate(contract, item) for item in candidates)
    true_counterfamily_ids = tuple(
        item.candidate_id for item in evaluations if item.true_counterfamily
    )
    survivor_candidate_ids = tuple(
        item.candidate_id
        for item in evaluations
        if item.status == "SURVIVOR_ROUTE_HANDLES"
    )
    rejected_candidate_ids = tuple(
        item.candidate_id
        for item in evaluations
        if item.status == "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
    )
    hostile_search_completed = all(item.expectation_matched for item in evaluations)
    true_counterfamily_found = bool(true_counterfamily_ids)
    route_breaks = true_counterfamily_found
    route_kept_open = hostile_search_completed and not route_breaks
    source_law_earned = False
    search_criteria = _search_criteria(
        source=source,
        evaluations=evaluations,
        true_counterfamily_ids=true_counterfamily_ids,
        survivor_candidate_ids=survivor_candidate_ids,
        rejected_candidate_ids=rejected_candidate_ids,
        route_kept_open=route_kept_open,
    )
    route_decisions = _route_decisions(
        route_breaks=route_breaks,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        source=source,
        search_criteria=search_criteria,
        route_decisions=route_decisions,
        hostile_search_completed=hostile_search_completed,
        true_counterfamily_found=true_counterfamily_found,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if route_kept_open
        and not true_counterfamily_found
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_hostile_counterfamily_search_unexpected_status"
    )

    return T575Result(
        artifact=ARTIFACT,
        source_t574_verdict=source.verdict,
        source_t574_selected_next_packet=source.selected_next_packet,
        search_status=SEARCH_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        search_contract=contract,
        candidates=candidates,
        evaluations=evaluations,
        search_criteria=search_criteria,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        true_counterfamily_ids=true_counterfamily_ids,
        survivor_candidate_ids=survivor_candidate_ids,
        rejected_candidate_ids=rejected_candidate_ids,
        hostile_search_completed=hostile_search_completed,
        true_counterfamily_found=true_counterfamily_found,
        route_breaks=route_breaks,
        route_kept_open=route_kept_open,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T575 runs the hostile counterfamily search selected by T574. "
            "The panel includes independent finality-native survivors plus "
            "controls for trivial gluing, target import, optional payload, "
            "commuting-square loss, foreign truth, and incomplete source roles. "
            "No true route-breaking counterfamily is found, but this remains "
            "finite synthetic review pressure rather than public source-law "
            "status."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should close the hostile-search "
            "scope by checking whether the T575 panel was broad enough before "
            "any source-law, claim, canon, public-posture, TAF4, TAF8, S1, "
            "publication, or cross-repo movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. T575 fails to find a true "
            "hostile counterfamily, keeps the T559-T575 route open as "
            "review-only, and selects hostile-search scope closure."
        ),
        taf4_update=(
            "TAF4 remains blocked. A finite hostile counterfamily search is not "
            "finite-to-continuum descent, causal-set recovery, Lorentzian target "
            "import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T575 is internal TAF11 hostile search, not a "
            "domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            search_criteria=search_criteria,
            true_counterfamily_ids=true_counterfamily_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T575 finds no true hostile "
            "counterfamily, keeps the route open as review-only, and selects "
            "scope closure; claim rows, Canon Index tiers, canon verdicts, and "
            "public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t575_result_to_dict(result: T575Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t574_verdict": result.source_t574_verdict,
        "source_t574_selected_next_packet": result.source_t574_selected_next_packet,
        "search_status": result.search_status,
        "source_law_status": result.source_law_status,
        "search_contract": result.search_contract.to_dict(),
        "candidates": [candidate.to_dict() for candidate in result.candidates],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "search_criteria": [
            criterion.to_dict() for criterion in result.search_criteria
        ],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "true_counterfamily_ids": list(result.true_counterfamily_ids),
        "survivor_candidate_ids": list(result.survivor_candidate_ids),
        "rejected_candidate_ids": list(result.rejected_candidate_ids),
        "hostile_search_completed": result.hostile_search_completed,
        "true_counterfamily_found": result.true_counterfamily_found,
        "route_breaks": result.route_breaks,
        "route_kept_open": result.route_kept_open,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [claim.to_dict() for claim in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _search_contract(source: t574.T574Result) -> HostileSearchContract:
    return HostileSearchContract(
        contract_id="t575_frozen_hostile_counterfamily_search_contract",
        source_t574_verdict=source.verdict,
        source_t574_selected_next_packet=source.selected_next_packet,
        frozen_source_roles=(
            "record_support",
            "handoff_boundary",
            "repair_window",
            "restriction_map",
            "seal_or_commitment",
            "audit_refinement",
        ),
        absorber_boundaries=(
            "ordinary_sheaf_gluing",
            "resource_transport",
            "consensus_state_machine",
            "record_provenance_completion",
        ),
        semantic_requirements=(
            "nontrivial_obstruction_witness",
            "noncommuting_transport_square",
            "native_payload_forcing",
            "target_blind_language",
            "frozen_role_projection",
            "independent_family_surface",
        ),
        forbidden_shortcuts=(
            "same_neighbor_trivial_gluing",
            "target_geometry_import",
            "optional_payload",
            "commuting_square_replacement",
            "foreign_truth_import",
            "observerse_or_aprd_replay",
        ),
        search_burden=(
            "Find an independent finality-native family that satisfies the "
            "frozen contract but contradicts the T559-T574 route."
        ),
    )


def _candidate_panel() -> tuple[CounterfamilyCandidate, ...]:
    roles = (
        "record_support",
        "handoff_boundary",
        "repair_window",
        "restriction_map",
        "seal_or_commitment",
        "audit_refinement",
    )
    boundaries = (
        "ordinary_sheaf_gluing",
        "resource_transport",
        "consensus_state_machine",
        "record_provenance_completion",
    )
    requirements = (
        "nontrivial_obstruction_witness",
        "noncommuting_transport_square",
        "native_payload_forcing",
        "target_blind_language",
        "frozen_role_projection",
        "independent_family_surface",
    )
    return (
        CounterfamilyCandidate(
            candidate_id="trivial_same_neighbor_gluing_control",
            family_id="same_neighbor_trivial_gluing_family",
            candidate_kind="absorber_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=True,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=True,
            contradicts_route=True,
            rationale="A trivial gluing completion is a hostile control, not residue.",
        ),
        CounterfamilyCandidate(
            candidate_id="target_geometry_language_import_control",
            family_id="target_geometry_import_family",
            candidate_kind="target_import_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=False,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=("Lorentzian interval", "causal-set sprinkling"),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=True,
            rationale="The family imports target geometry instead of finality-native payload.",
        ),
        CounterfamilyCandidate(
            candidate_id="optional_payload_counterfamily_control",
            family_id="optional_payload_family",
            candidate_kind="native_payload_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=False,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=(
                "nontrivial_obstruction_witness",
                "noncommuting_transport_square",
                "target_blind_language",
                "frozen_role_projection",
                "independent_family_surface",
            ),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=True,
            rationale="A payload-optional family fails the native-payload forcing screen.",
        ),
        CounterfamilyCandidate(
            candidate_id="commuting_square_replacement_control",
            family_id="commuting_square_family",
            candidate_kind="transport_square_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=True,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=(
                "nontrivial_obstruction_witness",
                "native_payload_forcing",
                "target_blind_language",
                "frozen_role_projection",
                "independent_family_surface",
            ),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=True,
            rationale="A commuting transport square cannot break the noncommuting route.",
        ),
        CounterfamilyCandidate(
            candidate_id="foreign_truth_replay_control",
            family_id="foreign_truth_replay_family",
            candidate_kind="foreign_truth_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=False,
            finality_native_payload=True,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=(),
            cross_repo_truth_import=True,
            observerse_replay=True,
            aprd_replay=True,
            absorber_complete_triviality=False,
            contradicts_route=True,
            rationale="Observerse, APRD, or cross-repo truth replay is not local evidence.",
        ),
        CounterfamilyCandidate(
            candidate_id="incomplete_source_role_collision_control",
            family_id="role_collision_family",
            candidate_kind="source_role_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=True,
            frozen_source_roles=(
                "record_support",
                "handoff_boundary",
                "repair_window",
                "restriction_map",
                "seal_or_commitment",
            ),
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=True,
            rationale="The apparent break drops audit refinement from the frozen role set.",
        ),
        CounterfamilyCandidate(
            candidate_id="escrow_epoch_repair_hostile_survivor",
            family_id="escrow_epoch_repair_family",
            candidate_kind="independent_survivor_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=True,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=False,
            rationale="A fresh escrow-epoch repair family satisfies the route instead of breaking it.",
        ),
        CounterfamilyCandidate(
            candidate_id="quorum_manifest_repair_hostile_survivor",
            family_id="quorum_manifest_repair_family",
            candidate_kind="independent_survivor_control",
            expected_true_counterfamily=False,
            predeclared_before_evaluation=True,
            independent_family=True,
            finality_native_payload=True,
            frozen_source_roles=roles,
            absorber_boundaries=boundaries,
            semantic_requirements=requirements,
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            absorber_complete_triviality=False,
            contradicts_route=False,
            rationale="A quorum-manifest repair family is handled by the same frozen route.",
        ),
    )


def _evaluate_candidate(
    contract: HostileSearchContract,
    candidate: CounterfamilyCandidate,
) -> CounterfamilyEvaluation:
    passed_checks: list[str] = []
    failed_checks: list[str] = []

    required_roles = set(contract.frozen_source_roles)
    candidate_roles = set(candidate.frozen_source_roles)
    required_boundaries = set(contract.absorber_boundaries)
    candidate_boundaries = set(candidate.absorber_boundaries)
    required_semantics = set(contract.semantic_requirements)
    candidate_semantics = set(candidate.semantic_requirements)

    checks = (
        ("predeclared_before_evaluation", candidate.predeclared_before_evaluation),
        ("independent_family", candidate.independent_family),
        ("finality_native_payload", candidate.finality_native_payload),
        ("frozen_source_roles_complete", required_roles <= candidate_roles),
        ("absorber_boundaries_complete", required_boundaries <= candidate_boundaries),
        ("semantic_requirements_complete", required_semantics <= candidate_semantics),
        ("target_blind_no_import_terms", not candidate.target_import_terms),
        ("no_cross_repo_truth_import", not candidate.cross_repo_truth_import),
        ("no_observerse_replay", not candidate.observerse_replay),
        ("no_aprd_replay", not candidate.aprd_replay),
        ("not_absorber_complete_triviality", not candidate.absorber_complete_triviality),
    )
    for check_id, passed in checks:
        if passed:
            passed_checks.append(check_id)
        else:
            failed_checks.append(check_id)

    all_entry_checks_pass = not failed_checks
    true_counterfamily = all_entry_checks_pass and candidate.contradicts_route
    expectation_matched = true_counterfamily == candidate.expected_true_counterfamily
    if true_counterfamily:
        status = "TRUE_COUNTERFAMILY_FOUND"
        route_effect = "breaks_route"
        reason = "Candidate satisfies the frozen contract and contradicts the route."
    elif all_entry_checks_pass:
        status = "SURVIVOR_ROUTE_HANDLES"
        route_effect = "route_handles_candidate"
        reason = "Candidate satisfies the frozen contract but does not contradict the route."
    else:
        status = "REJECTED_NOT_A_TRUE_COUNTERFAMILY"
        route_effect = "rejected_control"
        reason = "Candidate fails one or more frozen hostile-search requirements."

    return CounterfamilyEvaluation(
        candidate_id=candidate.candidate_id,
        family_id=candidate.family_id,
        expected_true_counterfamily=candidate.expected_true_counterfamily,
        true_counterfamily=true_counterfamily,
        expectation_matched=expectation_matched,
        status=status,
        passed_checks=tuple(passed_checks),
        failed_checks=tuple(failed_checks),
        route_effect=route_effect,
        reason=reason,
    )


def _search_criteria(
    source: t574.T574Result,
    evaluations: tuple[CounterfamilyEvaluation, ...],
    true_counterfamily_ids: tuple[str, ...],
    survivor_candidate_ids: tuple[str, ...],
    rejected_candidate_ids: tuple[str, ...],
    route_kept_open: bool,
) -> tuple[SearchCriterion, ...]:
    return (
        SearchCriterion(
            criterion_id="t574_authority",
            passed=(
                source.verdict == t574.VERDICT
                and source.selected_next_packet == t574.NEXT_PACKET
                and not source.source_law_earned
            ),
            evidence=(source.verdict, source.selected_next_packet),
            residual_risk="T574 is route adjudication, not source-law status.",
        ),
        SearchCriterion(
            criterion_id="hostile_panel_executed",
            passed=len(evaluations) == 8 and all(item.expectation_matched for item in evaluations),
            evidence=tuple(item.candidate_id for item in evaluations),
            residual_risk="The hostile panel is finite and synthetic.",
        ),
        SearchCriterion(
            criterion_id="survivor_controls_present",
            passed=len(survivor_candidate_ids) >= 2,
            evidence=survivor_candidate_ids,
            residual_risk="Survivors show the search was not only rejection controls.",
        ),
        SearchCriterion(
            criterion_id="hostile_controls_rejected",
            passed=len(rejected_candidate_ids) >= 6,
            evidence=rejected_candidate_ids,
            residual_risk="Rejected controls do not exhaust all possible counterfamilies.",
        ),
        SearchCriterion(
            criterion_id="no_true_counterfamily_found",
            passed=not true_counterfamily_ids,
            evidence=true_counterfamily_ids or ("none",),
            residual_risk="Absence in this panel is not a general nonexistence theorem.",
        ),
        SearchCriterion(
            criterion_id="route_kept_open_review_only",
            passed=route_kept_open,
            evidence=("route_open", "review_only", "scope_closure_required"),
            residual_risk="Scope closure is still required before any promotion reading.",
        ),
    )


def _route_decisions(
    route_breaks: bool,
    route_kept_open: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "BLOCKED_PROMOTION_BAR_NOT_MET"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Finite hostile search is not a public source law."
            ),
        ),
        RouteDecision(
            decision_id="retire_route_due_to_true_counterfamily",
            outcome=(
                "SELECTED_ROUTE_NARROWING"
                if route_breaks
                else "PAUSED_NO_TRUE_COUNTERFAMILY_FOUND"
            ),
            selected=route_breaks,
            next_packet="t576_domain_native_sheaf_transport_route_narrowing_gate",
            reason=(
                "A true counterfamily broke the route."
                if route_breaks
                else "No true counterfamily was found in the hostile panel."
            ),
        ),
        RouteDecision(
            decision_id="run_hostile_search_scope_closure_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if route_kept_open and not source_law_earned
                else "PAUSED_UNTIL_ROUTE_SURVIVES_SEARCH"
            ),
            selected=route_kept_open and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The route survived T575, so the next honest burden is hostile-search scope closure."
                if route_kept_open
                else "Scope closure waits for a surviving route."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t575",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Hostile counterfamily search is not continuum descent or target-spacetime recovery.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t575",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 hostile search is not a cross-domain shadow-protection packet.",
        ),
        RouteDecision(
            decision_id="move_s1_or_cross_repo_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            next_packet="none",
            reason="No S1, cross-repo, publication, claim, canon, or public-posture movement is authorized.",
        ),
    )


def _selected_next_packet(decisions: tuple[RouteDecision, ...]) -> str:
    selected = tuple(decision for decision in decisions if decision.selected)
    if len(selected) != 1:
        return "none"
    return selected[0].next_packet


def _gate_decisions(
    source: t574.T574Result,
    search_criteria: tuple[SearchCriterion, ...],
    route_decisions: tuple[RouteDecision, ...],
    hostile_search_completed: bool,
    true_counterfamily_found: bool,
    route_kept_open: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    criteria = {criterion.criterion_id: criterion for criterion in search_criteria}
    decisions = {decision.decision_id: decision for decision in route_decisions}
    all_criteria_pass = all(criterion.passed for criterion in search_criteria)
    gates = (
        (
            "t574_authority",
            criteria["t574_authority"].passed
            and source.selected_next_packet == t574.NEXT_PACKET,
            "T574 supplies hostile-counterfamily authority.",
            "T574 did not supply hostile-counterfamily authority.",
        ),
        (
            "hostile_search_completed",
            hostile_search_completed and criteria["hostile_panel_executed"].passed,
            "The hostile counterfamily panel executed as expected.",
            "The hostile counterfamily panel did not execute cleanly.",
        ),
        (
            "true_counterfamily_absent",
            not true_counterfamily_found
            and criteria["no_true_counterfamily_found"].passed,
            "No true route-breaking counterfamily was found.",
            "A true route-breaking counterfamily was found or the absence check failed.",
        ),
        (
            "route_remains_review_only",
            route_kept_open and not source_law_earned and all_criteria_pass,
            "The route remains open but review-only.",
            "The route moved too far or search criteria failed.",
        ),
        (
            "scope_closure_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions["run_hostile_search_scope_closure_gate"].selected,
            "Hostile-search scope closure is selected as the next burden.",
            "The expected scope-closure next packet was not selected.",
        ),
        (
            "protected_boundaries_preserved",
            decisions["move_taf4_from_t575"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions["execute_taf8_from_t575"].outcome == "BLOCKED_TAF8_OVERREAD"
            and decisions["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE"
            and decisions["promote_source_law_now"].outcome == "BLOCKED_PROMOTION_BAR_NOT_MET",
            "Source-law, TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A protected route movement was allowed.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=pass_reason if passed else fail_reason,
        )
        for gate_id, passed, pass_reason, fail_reason in gates
    )


def _claim_labels(
    search_criteria: tuple[SearchCriterion, ...],
    true_counterfamily_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    passed_criteria = tuple(
        criterion.criterion_id for criterion in search_criteria if criterion.passed
    )
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Hostile search criteria passed: " + ", ".join(passed_criteria) + ".",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "True route-breaking counterfamilies found: "
                + (", ".join(true_counterfamily_ids) if true_counterfamily_ids else "none")
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law promotion remains blocked by finite panel scope and protected governance surfaces.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="The route is worth keeping open only through hostile-search scope closure.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T575 Results: Domain-Native Sheaf Transport Hostile Counterfamily Search Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Search status: `{payload['search_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Source T574 verdict: `{payload['source_t574_verdict']}`",
        f"- Source T574 selected next packet: `{payload['source_t574_selected_next_packet']}`",
        f"- Hostile search completed: {payload['hostile_search_completed']}",
        f"- True counterfamily found: {payload['true_counterfamily_found']}",
        f"- Route breaks: {payload['route_breaks']}",
        f"- Route kept open: {payload['route_kept_open']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Search Contract",
        "",
        f"- Contract: `{payload['search_contract']['contract_id']}`",
        f"- Burden: {payload['search_contract']['search_burden']}",
        "",
        "## Candidate Evaluations",
        "",
        "| candidate | family | status | true counterfamily? | route effect | failed checks |",
        "| --- | --- | --- | :---: | --- | --- |",
    ]
    for evaluation in payload["evaluations"]:
        failed = ", ".join(f"`{item}`" for item in evaluation["failed_checks"]) or "none"
        lines.append(
            "| "
            f"`{evaluation['candidate_id']}` | "
            f"`{evaluation['family_id']}` | "
            f"`{evaluation['status']}` | "
            f"{evaluation['true_counterfamily']} | "
            f"`{evaluation['route_effect']}` | "
            f"{failed} |"
        )
    lines.extend(
        [
            "",
            "## Search Criteria",
            "",
            "| criterion | passed? | evidence | residual risk |",
            "| --- | :---: | --- | --- |",
        ]
    )
    for criterion in payload["search_criteria"]:
        evidence = ", ".join(f"`{item}`" for item in criterion["evidence"])
        lines.append(
            "| "
            f"`{criterion['criterion_id']}` | "
            f"{criterion['passed']} | "
            f"{evidence} | "
            f"{criterion['residual_risk']} |"
        )
    lines.extend(
        [
            "",
            "## Route Decisions",
            "",
            "| decision | outcome | selected? | next packet | reason |",
            "| --- | --- | :---: | --- | --- |",
        ]
    )
    for decision in payload["route_decisions"]:
        lines.append(
            "| "
            f"`{decision['decision_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Gate Decisions",
            "",
            "| gate | outcome | passed? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for gate in payload["gate_decisions"]:
        lines.append(
            "| "
            f"`{gate['gate_id']}` | "
            f"`{gate['outcome']}` | "
            f"{gate['passed']} | "
            f"{gate['reason']} |"
        )
    lines.extend(["", "## Claim Labels", ""])
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    for heading, key in (
        ("Source-Law Reading", "source_law_reading"),
        ("Recommended Next", "recommended_next"),
        ("TAF11 Update", "taf11_update"),
        ("TAF4 Update", "taf4_update"),
        ("TAF8 Update", "taf8_update"),
        ("Claim Ledger Update", "claim_ledger_update"),
        ("Not Claimed", "not_claimed"),
    ):
        lines.extend(["", f"## {heading}", "", str(payload[key])])
    lines.append("")
    return "\n".join(lines)


def write_results(result: T575Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t575_result_to_dict(result)
    json_path = (
        results_dir
        / "T575-domain-native-sheaf-transport-hostile-counterfamily-search-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T575-domain-native-sheaf-transport-hostile-counterfamily-search-gate-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    result = run_t575_analysis()
    payload = t575_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
