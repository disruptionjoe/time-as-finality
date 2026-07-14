"""T566: domain-native sheaf transport typed generator gate.

T565 cleared an independent predictive holdout but left the source-law route
blocked by `typed_source_generator`. T566 types the admissible-case generator
that selects future source-variable-complete holdout candidates before
fixture-specific outcome reading. It keeps the result review-only: no claim,
canon, public-posture, TAF4, TAF8, S1, external-publication, or cross-repo
movement follows from this packet.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565


ARTIFACT = "T566-domain-native-sheaf-transport-typed-generator-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_typed_generator_clears_review_only"
GENERATOR_STATUS = "TYPED_GENERATOR_CLEARS_SOURCE_LAW_REVIEW_GATE"
SOURCE_LAW_STATUS = "SOURCE_LAW_REVIEW_PACKET_COMPLETE_CLAIM_CANON_UNCHANGED"
ROUTE_STATUS = "typed_generator_clears_hostile_review_required"
NEXT_PACKET = "t567_domain_native_sheaf_transport_source_law_hostile_review_gate"

REQUIRED_GENERATOR_FIELDS = (
    "fixture_id",
    "native_record_scenario",
    "predeclared_before_outcome_reading",
    "finite_event_covers",
    "local_finality_sections",
    "restriction_morphisms",
    "settlement_obstruction_witnesses",
    "transport_consistency_squares",
    "allowed_refinement_steps",
    "absorber_boundary_profile",
)

FORBIDDEN_SHORTCUTS = t565.FORBIDDEN_SHORTCUTS

NOT_CLAIMED = (
    "T566 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It types an internal "
    "admissible-case generator and sends the route to hostile review."
)


@dataclass(frozen=True)
class GeneratorType:
    generator_id: str
    required_fields: tuple[str, ...]
    required_source_variables: tuple[str, ...]
    required_absorber_ids: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    selection_rule: str


@dataclass(frozen=True)
class CandidateCase:
    case_id: str
    native_record_scenario: str
    predeclared_before_outcome_reading: bool
    source_variables: tuple[str, ...]
    absorber_ids: tuple[str, ...]
    forbidden_shortcuts_used: tuple[str, ...]
    outcome_label_read: bool
    rationale: str


@dataclass(frozen=True)
class CandidateEvaluation:
    case_id: str
    admissible: bool
    status: str
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    reason: str


@dataclass(frozen=True)
class GeneratorAudit:
    audit_id: str
    outcome: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class RemainingBurden:
    burden_id: str
    status: str
    cleared: bool
    blocking: bool
    reason: str


@dataclass(frozen=True)
class RouteDecision:
    decision_id: str
    outcome: str
    selected: bool
    next_packet: str
    reason: str


@dataclass(frozen=True)
class GateDecision:
    gate_id: str
    outcome: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class HostileControl:
    control_id: str
    blocks: str
    reason: str


@dataclass(frozen=True)
class ClaimLabel:
    label: str
    confidence: str
    text: str


@dataclass(frozen=True)
class T566Result:
    artifact: str
    source_t565_verdict: str
    source_t565_selected_next_packet: str
    source_t565_predictive_holdout_cleared: bool
    generator_status: str
    source_law_status: str
    route_status: str
    generator_type: GeneratorType
    candidate_cases: tuple[CandidateCase, ...]
    candidate_evaluations: tuple[CandidateEvaluation, ...]
    generator_audits: tuple[GeneratorAudit, ...]
    remaining_burdens: tuple[RemainingBurden, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    hostile_controls: tuple[HostileControl, ...]
    typed_source_generator_cleared: bool
    source_law_review_packet_complete: bool
    source_law_public_or_canon_status_earned: bool
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


def run_t566_analysis() -> T566Result:
    t565_result = t565.run_t565_analysis()
    generator = _generator_type()
    cases = _candidate_cases()
    evaluations = tuple(_evaluate_candidate(generator, case) for case in cases)
    audits = _generator_audits(generator, evaluations)
    typed_source_generator_cleared = all(audit.passed for audit in audits)
    source_law_review_packet_complete = (
        t565_result.verdict == t565.VERDICT
        and t565_result.selected_next_packet == t565.NEXT_PACKET
        and t565_result.predictive_holdout_cleared
        and typed_source_generator_cleared
    )
    source_law_public_or_canon_status_earned = False
    remaining_burdens = _remaining_burdens(
        t565_result=t565_result,
        typed_source_generator_cleared=typed_source_generator_cleared,
        source_law_review_packet_complete=source_law_review_packet_complete,
    )
    route_decisions = _route_decisions(
        source_law_review_packet_complete=source_law_review_packet_complete,
        source_law_public_or_canon_status_earned=source_law_public_or_canon_status_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gates = _gate_decisions(
        t565_result=t565_result,
        generator=generator,
        evaluations=evaluations,
        audits=audits,
        remaining_burdens=remaining_burdens,
        route_decisions=route_decisions,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if source_law_review_packet_complete
        and not source_law_public_or_canon_status_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gates)
        else "domain_native_sheaf_transport_typed_generator_unexpected_status"
    )

    return T566Result(
        artifact=ARTIFACT,
        source_t565_verdict=t565_result.verdict,
        source_t565_selected_next_packet=t565_result.selected_next_packet,
        source_t565_predictive_holdout_cleared=t565_result.predictive_holdout_cleared,
        generator_status=GENERATOR_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        generator_type=generator,
        candidate_cases=cases,
        candidate_evaluations=evaluations,
        generator_audits=audits,
        remaining_burdens=remaining_burdens,
        route_decisions=route_decisions,
        gate_decisions=gates,
        hostile_controls=_hostile_controls(),
        typed_source_generator_cleared=typed_source_generator_cleared,
        source_law_review_packet_complete=source_law_review_packet_complete,
        source_law_public_or_canon_status_earned=source_law_public_or_canon_status_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "The typed generator selects source-variable-complete, "
            "absorber-boundary-complete holdout candidates before outcome "
            "reading and rejects incomplete, shortcut-bearing, replay, and "
            "post-hoc candidates. That completes the internal T564/T565 "
            "source-law review burden, but it is not a public source-law claim "
            "or canon movement."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. Hostile review should try to break the typed "
            "generator by supplying same-field adversaries, disguised target "
            "imports, absorber-complete-but-trivial cases, and alternate native "
            "record scenarios before any claim, canon, public-posture, TAF4, "
            "TAF8, or S1 movement."
        ),
        taf11_update=(
            "TAF11 now has an internal review packet: predictive holdout plus "
            "typed generator. It remains review-only until hostile review tests "
            "whether the generator is overfit or underdeclared."
        ),
        taf4_update=(
            "TAF4 remains blocked. A typed finite holdout generator is not "
            "finite-to-continuum descent, causal-set recovery, Lorentzian target "
            "import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T566 is an internal TAF11 generator packet, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(evaluations, remaining_burdens),
        claim_ledger_update=(
            "No claim-ledger update is earned. T566 clears an internal typed "
            "generator burden and selects hostile review; claim rows, Canon "
            "Index tiers, canon verdicts, and public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t566_result_to_dict(result: T566Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t565_verdict": result.source_t565_verdict,
        "source_t565_selected_next_packet": result.source_t565_selected_next_packet,
        "source_t565_predictive_holdout_cleared": result.source_t565_predictive_holdout_cleared,
        "generator_status": result.generator_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "generator_type": {
            "generator_id": result.generator_type.generator_id,
            "required_fields": list(result.generator_type.required_fields),
            "required_source_variables": list(result.generator_type.required_source_variables),
            "required_absorber_ids": list(result.generator_type.required_absorber_ids),
            "forbidden_shortcuts": list(result.generator_type.forbidden_shortcuts),
            "selection_rule": result.generator_type.selection_rule,
        },
        "candidate_cases": [
            {
                "case_id": case.case_id,
                "native_record_scenario": case.native_record_scenario,
                "predeclared_before_outcome_reading": case.predeclared_before_outcome_reading,
                "source_variables": list(case.source_variables),
                "absorber_ids": list(case.absorber_ids),
                "forbidden_shortcuts_used": list(case.forbidden_shortcuts_used),
                "outcome_label_read": case.outcome_label_read,
                "rationale": case.rationale,
            }
            for case in result.candidate_cases
        ],
        "candidate_evaluations": [
            {
                "case_id": evaluation.case_id,
                "admissible": evaluation.admissible,
                "status": evaluation.status,
                "passed_checks": list(evaluation.passed_checks),
                "failed_checks": list(evaluation.failed_checks),
                "reason": evaluation.reason,
            }
            for evaluation in result.candidate_evaluations
        ],
        "generator_audits": [
            {
                "audit_id": audit.audit_id,
                "outcome": audit.outcome,
                "passed": audit.passed,
                "reason": audit.reason,
            }
            for audit in result.generator_audits
        ],
        "remaining_burdens": [
            {
                "burden_id": burden.burden_id,
                "status": burden.status,
                "cleared": burden.cleared,
                "blocking": burden.blocking,
                "reason": burden.reason,
            }
            for burden in result.remaining_burdens
        ],
        "route_decisions": [
            {
                "decision_id": decision.decision_id,
                "outcome": decision.outcome,
                "selected": decision.selected,
                "next_packet": decision.next_packet,
                "reason": decision.reason,
            }
            for decision in result.route_decisions
        ],
        "gate_decisions": [
            {
                "gate_id": gate.gate_id,
                "outcome": gate.outcome,
                "passed": gate.passed,
                "reason": gate.reason,
            }
            for gate in result.gate_decisions
        ],
        "hostile_controls": [
            {
                "control_id": control.control_id,
                "blocks": control.blocks,
                "reason": control.reason,
            }
            for control in result.hostile_controls
        ],
        "typed_source_generator_cleared": result.typed_source_generator_cleared,
        "source_law_review_packet_complete": result.source_law_review_packet_complete,
        "source_law_public_or_canon_status_earned": result.source_law_public_or_canon_status_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [
            {
                "label": claim.label,
                "confidence": claim.confidence,
                "text": claim.text,
            }
            for claim in result.claim_labels
        ],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _generator_type() -> GeneratorType:
    return GeneratorType(
        generator_id="source_variable_complete_holdout_generator_v1",
        required_fields=REQUIRED_GENERATOR_FIELDS,
        required_source_variables=t565.FROZEN_SOURCE_VARIABLES,
        required_absorber_ids=t565.FROZEN_ABSORBER_IDS,
        forbidden_shortcuts=FORBIDDEN_SHORTCUTS,
        selection_rule=(
            "A candidate is admissible exactly when it is predeclared before "
            "outcome reading, includes every frozen source variable, includes "
            "every frozen absorber boundary, uses no forbidden shortcut, and "
            "is not a fixture replay."
        ),
    )


def _candidate_cases() -> tuple[CandidateCase, ...]:
    return (
        CandidateCase(
            case_id="new_multiphase_escrow_repair_holdout",
            native_record_scenario="multiphase escrow finality repair",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            rationale=(
                "A future holdout candidate with complete source variables and "
                "absorber boundaries, different from the T559-T565 fixtures."
            ),
        ),
        CandidateCase(
            case_id="missing_transport_square_control",
            native_record_scenario="incomplete transport repair",
            predeclared_before_outcome_reading=True,
            source_variables=tuple(
                item
                for item in t565.FROZEN_SOURCE_VARIABLES
                if item != "transport_consistency_squares"
            ),
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            rationale="Rejects candidates missing a load-bearing source variable.",
        ),
        CandidateCase(
            case_id="target_import_shortcut_control",
            native_record_scenario="target-labeled repair",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=("target_labels",),
            outcome_label_read=False,
            rationale="Rejects candidates that rely on target labels.",
        ),
        CandidateCase(
            case_id="posthoc_outcome_reading_control",
            native_record_scenario="post-hoc selected repair",
            predeclared_before_outcome_reading=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=True,
            rationale="Rejects candidates selected after fixture-specific outcome reading.",
        ),
        CandidateCase(
            case_id="prior_fixture_replay_control",
            native_record_scenario="t565 rotating multi-ledger repair holdout",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            rationale="Rejects direct replay of the already evaluated T565 holdout.",
        ),
    )


def _evaluate_candidate(
    generator: GeneratorType,
    candidate: CandidateCase,
) -> CandidateEvaluation:
    checks: list[tuple[str, bool]] = [
        (
            "predeclared_before_outcome_reading",
            candidate.predeclared_before_outcome_reading and not candidate.outcome_label_read,
        ),
        (
            "source_variables_complete",
            candidate.source_variables == generator.required_source_variables,
        ),
        (
            "absorber_boundaries_complete",
            candidate.absorber_ids == generator.required_absorber_ids,
        ),
        (
            "forbidden_shortcuts_absent",
            candidate.forbidden_shortcuts_used == (),
        ),
        (
            "not_prior_fixture_replay",
            candidate.native_record_scenario
            != "t565 rotating multi-ledger repair holdout",
        ),
    ]
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    admissible = not failed
    return CandidateEvaluation(
        case_id=candidate.case_id,
        admissible=admissible,
        status="ADMISSIBLE_TYPED_HOLDOUT_CANDIDATE" if admissible else "REJECTED_BY_TYPED_GENERATOR",
        passed_checks=passed,
        failed_checks=failed,
        reason=(
            "The candidate is selected by the typed generator before outcome reading."
            if admissible
            else "The typed generator rejects the candidate because: "
            + ", ".join(failed)
        ),
    )


def _generator_audits(
    generator: GeneratorType,
    evaluations: tuple[CandidateEvaluation, ...],
) -> tuple[GeneratorAudit, ...]:
    by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    expected_admissible = by_id["new_multiphase_escrow_repair_holdout"]
    rejected = tuple(
        evaluation
        for evaluation in evaluations
        if evaluation.case_id != "new_multiphase_escrow_repair_holdout"
    )
    return (
        GeneratorAudit(
            audit_id="generator_type_declared",
            outcome="PASS" if generator.required_fields == REQUIRED_GENERATOR_FIELDS else "FAIL",
            passed=generator.required_fields == REQUIRED_GENERATOR_FIELDS,
            reason="The generator declares every required source-variable and boundary field.",
        ),
        GeneratorAudit(
            audit_id="admits_complete_future_candidate",
            outcome="PASS" if expected_admissible.admissible else "FAIL",
            passed=expected_admissible.admissible,
            reason="A new source-variable-complete future holdout candidate is selected.",
        ),
        GeneratorAudit(
            audit_id="rejects_incomplete_or_shortcut_candidates",
            outcome="PASS" if all(not evaluation.admissible for evaluation in rejected) else "FAIL",
            passed=all(not evaluation.admissible for evaluation in rejected),
            reason="Incomplete, target-import, post-hoc, and replay controls are rejected.",
        ),
        GeneratorAudit(
            audit_id="selection_precedes_outcome_reading",
            outcome=(
                "PASS"
                if all(
                    evaluation.admissible == (not _case_by_id(evaluation.case_id).outcome_label_read)
                    or not evaluation.admissible
                    for evaluation in evaluations
                )
                else "FAIL"
            ),
            passed=all(
                evaluation.admissible == (not _case_by_id(evaluation.case_id).outcome_label_read)
                or not evaluation.admissible
                for evaluation in evaluations
            ),
            reason="No admitted candidate depends on fixture-specific outcome labels.",
        ),
    )


def _case_by_id(case_id: str) -> CandidateCase:
    for case in _candidate_cases():
        if case.case_id == case_id:
            return case
    raise KeyError(case_id)


def _remaining_burdens(
    t565_result: t565.T565Result,
    typed_source_generator_cleared: bool,
    source_law_review_packet_complete: bool,
) -> tuple[RemainingBurden, ...]:
    t565_authority = (
        t565_result.verdict == t565.VERDICT
        and t565_result.selected_next_packet == t565.NEXT_PACKET
        and t565_result.predictive_holdout_cleared
        and not t565_result.typed_source_generator_cleared
    )
    return (
        RemainingBurden(
            burden_id="t565_typed_generator_authority",
            status="CLEARED" if t565_authority else "FAILED",
            cleared=t565_authority,
            blocking=not t565_authority,
            reason=(
                "T565 selected the typed generator gate after clearing predictive holdout."
                if t565_authority
                else "T565 did not supply the expected typed-generator authority."
            ),
        ),
        RemainingBurden(
            burden_id="typed_source_generator",
            status="CLEARED" if typed_source_generator_cleared else "FAILED",
            cleared=typed_source_generator_cleared,
            blocking=not typed_source_generator_cleared,
            reason=(
                "The generator selects complete future candidates and rejects incomplete, shortcut, post-hoc, and replay controls."
                if typed_source_generator_cleared
                else "The generator failed at least one type or control audit."
            ),
        ),
        RemainingBurden(
            burden_id="source_law_review_packet",
            status="COMPLETE_REVIEW_ONLY" if source_law_review_packet_complete else "INCOMPLETE",
            cleared=source_law_review_packet_complete,
            blocking=not source_law_review_packet_complete,
            reason=(
                "T564/T565/T566 now provide absorber separation, predictive holdout, and typed generator review evidence."
                if source_law_review_packet_complete
                else "The review packet remains incomplete."
            ),
        ),
        RemainingBurden(
            burden_id="hostile_review_before_governance_movement",
            status="BLOCKING_NEXT_REVIEW",
            cleared=False,
            blocking=True,
            reason=(
                "A complete internal review packet still needs hostile review before any claim, canon, public-posture, TAF4, TAF8, or S1 movement."
            ),
        ),
        RemainingBurden(
            burden_id="governance_boundaries_preserved",
            status="CLEARED",
            cleared=True,
            blocking=False,
            reason="No governance, publication, TAF4, TAF8, S1, or cross-repo movement is made.",
        ),
    )


def _route_decisions(
    source_law_review_packet_complete: bool,
    source_law_public_or_canon_status_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_claim_or_canon_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_public_or_canon_status_earned
                else "REJECTED_REVIEW_ONLY_PACKET"
            ),
            selected=source_law_public_or_canon_status_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_public_or_canon_status_earned
                else "The packet is internal review evidence only and does not move claims or canon."
            ),
        ),
        RouteDecision(
            decision_id="run_hostile_review_gate",
            outcome="SELECTED_NEXT_BURDEN",
            selected=source_law_review_packet_complete
            and not source_law_public_or_canon_status_earned,
            next_packet=NEXT_PACKET,
            reason="The internal review packet is complete, so the next honest step is hostile review.",
        ),
        RouteDecision(
            decision_id="move_taf4_from_t566",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A typed finite generator is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t566",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 generator evidence is not cross-domain shadow protection.",
        ),
        RouteDecision(
            decision_id="move_s1_or_cross_repo_truth",
            outcome="BLOCKED_GOVERNANCE",
            selected=False,
            next_packet="none",
            reason="No S1, cross-repo, publication, or public-posture movement is authorized.",
        ),
    )


def _selected_next_packet(decisions: tuple[RouteDecision, ...]) -> str:
    selected = tuple(decision for decision in decisions if decision.selected)
    if len(selected) != 1:
        return "none"
    return selected[0].next_packet


def _gate_decisions(
    t565_result: t565.T565Result,
    generator: GeneratorType,
    evaluations: tuple[CandidateEvaluation, ...],
    audits: tuple[GeneratorAudit, ...],
    remaining_burdens: tuple[RemainingBurden, ...],
    route_decisions: tuple[RouteDecision, ...],
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    burdens_by_id = {burden.burden_id: burden for burden in remaining_burdens}
    decisions_by_id = {decision.decision_id: decision for decision in route_decisions}
    evaluation_by_id = {evaluation.case_id: evaluation for evaluation in evaluations}
    gates = (
        (
            "t565_authority",
            t565_result.verdict == t565.VERDICT
            and t565_result.selected_next_packet == t565.NEXT_PACKET
            and t565_result.predictive_holdout_cleared,
            "T565 supplies typed-generator authority.",
            "T565 did not supply the expected typed-generator authority.",
        ),
        (
            "generator_type_declared",
            generator.required_fields == REQUIRED_GENERATOR_FIELDS
            and generator.required_source_variables == t565.FROZEN_SOURCE_VARIABLES
            and generator.required_absorber_ids == t565.FROZEN_ABSORBER_IDS,
            "The typed generator declares every frozen source variable and absorber boundary.",
            "The typed generator is underdeclared.",
        ),
        (
            "future_candidate_admitted",
            evaluation_by_id["new_multiphase_escrow_repair_holdout"].admissible,
            "A new source-variable-complete future holdout candidate is admitted.",
            "The generator failed to admit the complete future candidate.",
        ),
        (
            "controls_rejected",
            all(
                not evaluation.admissible
                for case_id, evaluation in evaluation_by_id.items()
                if case_id != "new_multiphase_escrow_repair_holdout"
            ),
            "Incomplete, target-import, post-hoc, and replay controls are rejected.",
            "At least one hostile control was admitted.",
        ),
        (
            "generator_audits_pass",
            all(audit.passed for audit in audits),
            "All generator audits pass.",
            "At least one generator audit failed.",
        ),
        (
            "review_packet_complete_not_promoted",
            burdens_by_id["source_law_review_packet"].cleared
            and burdens_by_id["hostile_review_before_governance_movement"].blocking
            and decisions_by_id["promote_claim_or_canon_now"].outcome
            == "REJECTED_REVIEW_ONLY_PACKET",
            "The internal review packet is complete but not promoted.",
            "The packet either remains incomplete or promoted too early.",
        ),
        (
            "hostile_review_selected_next",
            selected_next_packet == NEXT_PACKET
            and decisions_by_id["run_hostile_review_gate"].selected,
            "Hostile review is selected as the next burden.",
            "The expected hostile-review next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            decisions_by_id["move_taf4_from_t566"].outcome == "BLOCKED_TAF4_OVERREAD"
            and decisions_by_id["execute_taf8_from_t566"].outcome == "BLOCKED_TAF8_OVERREAD"
            and decisions_by_id["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, and public-posture movements are blocked.",
            "A forbidden route movement was allowed.",
        ),
        (
            "governance_boundaries_preserved",
            burdens_by_id["governance_boundaries_preserved"].cleared,
            "No claim, canon, publication, public-posture, S1, TAF4, TAF8, or cross-repo movement is made.",
            "A governance boundary was crossed.",
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


def _hostile_controls() -> tuple[HostileControl, ...]:
    return (
        HostileControl(
            control_id="underdeclared_generator_control",
            blocks="Calling a selector typed while it omits a frozen source variable.",
            reason="The missing-transport-square control is rejected.",
        ),
        HostileControl(
            control_id="target_import_control",
            blocks="Using target labels, Lorentzian structure, or cross-repo truth as selection help.",
            reason="The target-import control is rejected.",
        ),
        HostileControl(
            control_id="posthoc_control",
            blocks="Selecting cases after reading fixture-specific outcomes.",
            reason="The post-hoc outcome-reading control is rejected.",
        ),
        HostileControl(
            control_id="replay_control",
            blocks="Counting T565 replay as a generated future candidate.",
            reason="The prior-fixture replay control is rejected.",
        ),
        HostileControl(
            control_id="review_only_control",
            blocks="Promoting claim, canon, TAF4, TAF8, S1, or public posture from internal generator evidence.",
            reason="The route selects hostile review rather than governance movement.",
        ),
    )


def _claim_labels(
    evaluations: tuple[CandidateEvaluation, ...],
    remaining_burdens: tuple[RemainingBurden, ...],
) -> tuple[ClaimLabel, ...]:
    admitted = ", ".join(
        evaluation.case_id for evaluation in evaluations if evaluation.admissible
    )
    rejected = ", ".join(
        evaluation.case_id for evaluation in evaluations if not evaluation.admissible
    )
    cleared = ", ".join(burden.burden_id for burden in remaining_burdens if burden.cleared)
    blocked = ", ".join(burden.burden_id for burden in remaining_burdens if burden.blocking)
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The typed generator admits: {admitted}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The typed generator rejects: {rejected}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The cleared burdens are: {cleared}.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text=f"Governance movement remains blocked by: {blocked}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="A complete internal review packet justifies hostile review, not promotion.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T566 Results: Domain-Native Sheaf Transport Typed Generator Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Generator status: `{payload['generator_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T565 verdict: `{payload['source_t565_verdict']}`",
        f"- Source T565 selected next packet: `{payload['source_t565_selected_next_packet']}`",
        f"- Source T565 predictive holdout cleared: {payload['source_t565_predictive_holdout_cleared']}",
        f"- Typed source generator cleared: {payload['typed_source_generator_cleared']}",
        f"- Source-law review packet complete: {payload['source_law_review_packet_complete']}",
        f"- Public/canon source-law status earned: {payload['source_law_public_or_canon_status_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Generator Type",
        "",
        f"- Generator: `{payload['generator_type']['generator_id']}`",
        "- Required fields: "
        + ", ".join(f"`{item}`" for item in payload["generator_type"]["required_fields"]),
        "- Required source variables: "
        + ", ".join(f"`{item}`" for item in payload["generator_type"]["required_source_variables"]),
        "- Required absorber boundaries: "
        + ", ".join(f"`{item}`" for item in payload["generator_type"]["required_absorber_ids"]),
        f"- Selection rule: {payload['generator_type']['selection_rule']}",
        "",
        "## Candidate Evaluations",
        "",
        "| candidate | admissible? | status | passed checks | failed checks | reason |",
        "| --- | :---: | --- | --- | --- | --- |",
    ]
    for evaluation in payload["candidate_evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['case_id']}` | "
            f"{evaluation['admissible']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['passed_checks']) or 'none'} | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Generator Audits",
            "",
            "| audit | outcome | passed? | reason |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for audit in payload["generator_audits"]:
        lines.append(
            "| "
            f"`{audit['audit_id']}` | "
            f"`{audit['outcome']}` | "
            f"{audit['passed']} | "
            f"{audit['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Remaining Burdens",
            "",
            "| burden | status | cleared? | blocking? | reason |",
            "| --- | --- | :---: | :---: | --- |",
        ]
    )
    for burden in payload["remaining_burdens"]:
        lines.append(
            "| "
            f"`{burden['burden_id']}` | "
            f"`{burden['status']}` | "
            f"{burden['cleared']} | "
            f"{burden['blocking']} | "
            f"{burden['reason']} |"
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
    lines.extend(["", "## Hostile Controls", "", "| control | blocks | reason |", "| --- | --- | --- |"])
    for control in payload["hostile_controls"]:
        lines.append(
            "| "
            f"`{control['control_id']}` | "
            f"{control['blocks']} | "
            f"{control['reason']} |"
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


def write_results(result: T566Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t566_result_to_dict(result)
    json_path = (
        results_dir
        / "T566-domain-native-sheaf-transport-typed-generator-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T566-domain-native-sheaf-transport-typed-generator-gate-v0.1-results.md"
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

    result = run_t566_analysis()
    payload = t566_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
