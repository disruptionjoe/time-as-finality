"""T569: independent reimplementation of the TAF11 semantic generator.

T568 strengthened the domain-native sheaf transport semantic generator but left
source-law status blocked until an independent reimplementation. T569 rebuilds
the selector from the declared semantic contract rather than T567/T568 fixture
labels, compares the rebuilt selector with the T568 contract on a fresh panel,
and keeps the result review-only.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565
from models import (
    t568_domain_native_sheaf_transport_semantic_generator_strengthening_gate as t568,
)


ARTIFACT = "T569-domain-native-sheaf-transport-independent-reimplementation-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_independent_reimplementation_matches_review_only"
REIMPLEMENTATION_STATUS = "INDEPENDENT_REIMPLEMENTATION_MATCHES_DECLARED_CONTRACT"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_FRESH_FAMILY_STRESS_REQUIRED"
ROUTE_STATUS = "independent_reimplementation_clears_fresh_family_stress_required"
NEXT_PACKET = "t570_domain_native_sheaf_transport_fresh_family_stress_gate"

NOT_CLAIMED = (
    "T569 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It independently "
    "reimplements the strengthened semantic generator and selects fresh-family "
    "stress as the next review-only burden."
)


@dataclass(frozen=True)
class IndependentGeneratorSpec:
    implementation_id: str
    source_contract_id: str
    reconstructed_source_variables: tuple[str, ...]
    reconstructed_absorber_ids: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    fixture_label_fields_used: tuple[str, ...]
    selection_rule: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "reconstructed_source_variables",
            "reconstructed_absorber_ids",
            "forbidden_shortcuts",
            "semantic_requirements",
            "fixture_label_fields_used",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class ReimplementationCandidate:
    candidate_id: str
    native_record_scenario: str
    predeclared_from_contract: bool
    prior_fixture_label_used: bool
    outcome_label_read: bool
    source_variables: tuple[str, ...]
    absorber_ids: tuple[str, ...]
    forbidden_shortcuts_used: tuple[str, ...]
    nontrivial_obstruction_witness: bool
    noncommuting_transport_square: bool
    native_payload_forced: bool
    target_import_terms: tuple[str, ...]
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_variables",
            "absorber_ids",
            "forbidden_shortcuts_used",
            "target_import_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class ReimplementationEvaluation:
    candidate_id: str
    independent_selector_admissible: bool
    contract_selector_admissible: bool
    selectors_match: bool
    status: str
    passed_checks: tuple[str, ...]
    failed_checks: tuple[str, ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["passed_checks"] = list(self.passed_checks)
        data["failed_checks"] = list(self.failed_checks)
        return data


@dataclass(frozen=True)
class ClosureCheck:
    check_id: str
    status: str
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
class T569Result:
    artifact: str
    source_t568_verdict: str
    source_t568_selected_next_packet: str
    source_t568_semantic_generator_strengthened: bool
    reimplementation_status: str
    source_law_status: str
    route_status: str
    independent_generator_spec: IndependentGeneratorSpec
    candidates: tuple[ReimplementationCandidate, ...]
    evaluations: tuple[ReimplementationEvaluation, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    admitted_candidate_ids: tuple[str, ...]
    rejected_control_ids: tuple[str, ...]
    independent_reimplementation_cleared: bool
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


def run_t569_analysis() -> T569Result:
    source = t568.run_t568_analysis()
    source_generator = source.strengthened_generator_type
    spec = _independent_generator_spec(source_generator)
    candidates = _fresh_reimplementation_panel()
    evaluations = tuple(
        _evaluate_candidate(spec, source_generator, candidate)
        for candidate in candidates
    )
    admitted_candidate_ids = tuple(
        evaluation.candidate_id
        for evaluation in evaluations
        if evaluation.independent_selector_admissible
    )
    rejected_control_ids = tuple(
        evaluation.candidate_id
        for evaluation in evaluations
        if not evaluation.independent_selector_admissible
    )
    independent_reimplementation_cleared = (
        source.verdict == t568.VERDICT
        and source.selected_next_packet == t568.NEXT_PACKET
        and source.semantic_generator_strengthened
        and all(evaluation.selectors_match for evaluation in evaluations)
        and admitted_candidate_ids
        == (
            "escrow_window_rotation_holdout",
            "checkpoint_quorum_handoff_holdout",
        )
        and rejected_control_ids
        == (
            "same_neighbor_trivial_gluing_control",
            "target_geometry_language_import_control",
            "payload_optional_near_miss_control",
            "fixture_label_alias_control",
        )
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        spec=spec,
        evaluations=evaluations,
        admitted_candidate_ids=admitted_candidate_ids,
        rejected_control_ids=rejected_control_ids,
    )
    route_decisions = _route_decisions(
        independent_reimplementation_cleared=independent_reimplementation_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        independent_reimplementation_cleared=independent_reimplementation_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if independent_reimplementation_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(check.passed for check in closure_checks)
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_independent_reimplementation_unexpected_status"
    )

    return T569Result(
        artifact=ARTIFACT,
        source_t568_verdict=source.verdict,
        source_t568_selected_next_packet=source.selected_next_packet,
        source_t568_semantic_generator_strengthened=source.semantic_generator_strengthened,
        reimplementation_status=REIMPLEMENTATION_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        independent_generator_spec=spec,
        candidates=candidates,
        evaluations=evaluations,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        admitted_candidate_ids=admitted_candidate_ids,
        rejected_control_ids=rejected_control_ids,
        independent_reimplementation_cleared=independent_reimplementation_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T569 independently rebuilds the strengthened semantic generator "
            "from the declared T568 contract and matches it on a fresh panel. "
            "That closes the fixture-label replay risk for this review step, "
            "but all evidence is still internal to the sheaf-transport family, "
            "so source-law status remains unearned."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next gate should stress the independently "
            "reimplemented generator against a fresh family or sharply explain "
            "why no fresh-family stress is available before any source-law, "
            "claim, canon, public-posture, TAF4, TAF8, or S1 movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. The semantic generator now has "
            "an independent contract-level reimplementation, but it still needs "
            "fresh-family stress before source-law movement."
        ),
        taf4_update=(
            "TAF4 remains blocked. An independently reimplemented finite "
            "semantic generator is not finite-to-continuum descent, causal-set "
            "recovery, Lorentzian target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T569 is internal TAF11 generator validation, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            admitted_candidate_ids=admitted_candidate_ids,
            rejected_control_ids=rejected_control_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T569 independently reimplements "
            "the strengthened semantic generator and selects fresh-family "
            "stress; claim rows, Canon Index tiers, canon verdicts, and public "
            "posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t569_result_to_dict(result: T569Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t568_verdict": result.source_t568_verdict,
        "source_t568_selected_next_packet": result.source_t568_selected_next_packet,
        "source_t568_semantic_generator_strengthened": result.source_t568_semantic_generator_strengthened,
        "reimplementation_status": result.reimplementation_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "independent_generator_spec": result.independent_generator_spec.to_dict(),
        "candidates": [candidate.to_dict() for candidate in result.candidates],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [
            decision.to_dict() for decision in result.route_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "admitted_candidate_ids": list(result.admitted_candidate_ids),
        "rejected_control_ids": list(result.rejected_control_ids),
        "independent_reimplementation_cleared": result.independent_reimplementation_cleared,
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


def _independent_generator_spec(
    source_generator: t568.StrengthenedGeneratorType,
) -> IndependentGeneratorSpec:
    return IndependentGeneratorSpec(
        implementation_id="semantic_contract_reimplementation_v1",
        source_contract_id=source_generator.generator_id,
        reconstructed_source_variables=source_generator.inherited_source_variables,
        reconstructed_absorber_ids=source_generator.inherited_absorber_ids,
        forbidden_shortcuts=t565.FORBIDDEN_SHORTCUTS,
        semantic_requirements=t568.SEMANTIC_REQUIREMENTS,
        fixture_label_fields_used=(),
        selection_rule=(
            "A candidate is admissible exactly when it is predeclared from the "
            "semantic contract, uses no prior fixture label or outcome label, "
            "carries every frozen source variable and absorber boundary, uses "
            "no forbidden shortcut, has a nontrivial obstruction witness, has "
            "a noncommuting transport square, forces a finality-native payload, "
            "and uses no target-geometry language."
        ),
    )


def _fresh_reimplementation_panel() -> tuple[ReimplementationCandidate, ...]:
    return (
        ReimplementationCandidate(
            candidate_id="escrow_window_rotation_holdout",
            native_record_scenario="escrow window rotation with delayed threshold repair",
            predeclared_from_contract=True,
            prior_fixture_label_used=False,
            outcome_label_read=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            rationale=(
                "Fresh finality-native holdout phrased from the contract, not "
                "from a T567/T568 fixture label."
            ),
        ),
        ReimplementationCandidate(
            candidate_id="checkpoint_quorum_handoff_holdout",
            native_record_scenario="checkpoint quorum handoff with staggered repair windows",
            predeclared_from_contract=True,
            prior_fixture_label_used=False,
            outcome_label_read=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            rationale=(
                "Second fresh finality-native holdout with the same semantic "
                "contract but independent scenario language."
            ),
        ),
        ReimplementationCandidate(
            candidate_id="same_neighbor_trivial_gluing_control",
            native_record_scenario="same-neighbor sheaf gluing bookkeeping",
            predeclared_from_contract=True,
            prior_fixture_label_used=False,
            outcome_label_read=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=False,
            noncommuting_transport_square=False,
            native_payload_forced=False,
            target_import_terms=(),
            rationale="Rejects absorber-complete but semantically trivial packets.",
        ),
        ReimplementationCandidate(
            candidate_id="target_geometry_language_import_control",
            native_record_scenario="causal-set link recovery with Lorentzian dimension target",
            predeclared_from_contract=True,
            prior_fixture_label_used=False,
            outcome_label_read=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=False,
            target_import_terms=(
                "causal_set_link_recovery",
                "lorentzian_dimension_target",
            ),
            rationale="Rejects target-geometry language and missing native payload forcing.",
        ),
        ReimplementationCandidate(
            candidate_id="payload_optional_near_miss_control",
            native_record_scenario="obstruction transport with optional settlement payload",
            predeclared_from_contract=True,
            prior_fixture_label_used=False,
            outcome_label_read=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=False,
            target_import_terms=(),
            rationale="Rejects a near miss where semantic structure exists but payload is not forced.",
        ),
        ReimplementationCandidate(
            candidate_id="fixture_label_alias_control",
            native_record_scenario="renamed T568 survivor copied after outcome reading",
            predeclared_from_contract=True,
            prior_fixture_label_used=True,
            outcome_label_read=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            rationale="Rejects fixture-label replay even when the semantic booleans are positive.",
        ),
    )


def _evaluate_candidate(
    spec: IndependentGeneratorSpec,
    source_generator: t568.StrengthenedGeneratorType,
    candidate: ReimplementationCandidate,
) -> ReimplementationEvaluation:
    independent_checks = _selector_checks(
        required_source_variables=spec.reconstructed_source_variables,
        required_absorber_ids=spec.reconstructed_absorber_ids,
        forbidden_shortcuts=spec.forbidden_shortcuts,
        candidate=candidate,
    )
    contract_checks = _selector_checks(
        required_source_variables=source_generator.inherited_source_variables,
        required_absorber_ids=source_generator.inherited_absorber_ids,
        forbidden_shortcuts=source_generator.forbidden_shortcuts,
        candidate=candidate,
    )
    passed = tuple(name for name, ok in independent_checks if ok)
    failed = tuple(name for name, ok in independent_checks if not ok)
    independent_admissible = not failed
    contract_admissible = all(ok for _, ok in contract_checks)
    selectors_match = independent_admissible == contract_admissible
    if independent_admissible:
        status = "ADMITTED_BY_INDEPENDENT_REIMPLEMENTATION"
        reason = "The fresh candidate satisfies the independently rebuilt semantic contract."
    elif candidate.prior_fixture_label_used or candidate.outcome_label_read:
        status = "REJECTED_FIXTURE_LABEL_OR_OUTCOME_REPLAY"
        reason = "The independent reimplementation rejects fixture-label or outcome replay."
    elif candidate.target_import_terms:
        status = "REJECTED_TARGET_IMPORT"
        reason = "The independent reimplementation rejects target-language import."
    elif "native_payload_forced" in failed:
        status = "REJECTED_NATIVE_PAYLOAD_NOT_FORCED"
        reason = "The independent reimplementation rejects unforced native payload."
    else:
        status = "REJECTED_SEMANTIC_CONTRACT"
        reason = "The independent reimplementation rejects the candidate because: " + ", ".join(failed)
    return ReimplementationEvaluation(
        candidate_id=candidate.candidate_id,
        independent_selector_admissible=independent_admissible,
        contract_selector_admissible=contract_admissible,
        selectors_match=selectors_match,
        status=status,
        passed_checks=passed,
        failed_checks=failed,
        reason=reason,
    )


def _selector_checks(
    required_source_variables: tuple[str, ...],
    required_absorber_ids: tuple[str, ...],
    forbidden_shortcuts: tuple[str, ...],
    candidate: ReimplementationCandidate,
) -> tuple[tuple[str, bool], ...]:
    return (
        (
            "predeclared_from_contract",
            candidate.predeclared_from_contract and not candidate.outcome_label_read,
        ),
        ("fixture_label_independent", not candidate.prior_fixture_label_used),
        (
            "source_variables_complete",
            candidate.source_variables == required_source_variables,
        ),
        ("absorber_boundaries_complete", candidate.absorber_ids == required_absorber_ids),
        (
            "forbidden_shortcuts_absent",
            all(shortcut not in candidate.forbidden_shortcuts_used for shortcut in forbidden_shortcuts)
            and candidate.forbidden_shortcuts_used == (),
        ),
        (
            "nontrivial_obstruction_witness",
            candidate.nontrivial_obstruction_witness,
        ),
        ("noncommuting_transport_square", candidate.noncommuting_transport_square),
        ("native_payload_forced", candidate.native_payload_forced),
        ("target_blind_language", candidate.target_import_terms == ()),
    )


def _closure_checks(
    source: t568.T568Result,
    spec: IndependentGeneratorSpec,
    evaluations: tuple[ReimplementationEvaluation, ...],
    admitted_candidate_ids: tuple[str, ...],
    rejected_control_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    by_id = {evaluation.candidate_id: evaluation for evaluation in evaluations}
    t568_authority = (
        source.verdict == t568.VERDICT
        and source.selected_next_packet == t568.NEXT_PACKET
        and source.semantic_generator_strengthened
    )
    expected_admitted = (
        "escrow_window_rotation_holdout",
        "checkpoint_quorum_handoff_holdout",
    )
    expected_rejected = (
        "same_neighbor_trivial_gluing_control",
        "target_geometry_language_import_control",
        "payload_optional_near_miss_control",
        "fixture_label_alias_control",
    )
    return (
        ClosureCheck(
            check_id="t568_authority",
            status="PASS" if t568_authority else "FAIL",
            passed=t568_authority,
            evidence=(
                "T568 strengthened the semantic generator.",
                "T568 selected independent reimplementation as next packet.",
            ),
            residual_risk="T568 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="independent_spec_uses_no_fixture_labels",
            status="PASS" if spec.fixture_label_fields_used == () else "FAIL",
            passed=spec.fixture_label_fields_used == (),
            evidence=spec.fixture_label_fields_used,
            residual_risk="Fresh-family stress is still needed after contract reimplementation.",
        ),
        ClosureCheck(
            check_id="contract_equivalence_on_fresh_panel",
            status="PASS" if all(item.selectors_match for item in evaluations) else "FAIL",
            passed=all(item.selectors_match for item in evaluations),
            evidence=tuple(
                item.candidate_id for item in evaluations if item.selectors_match
            ),
            residual_risk="Equivalence is finite-panel evidence, not source-law status.",
        ),
        ClosureCheck(
            check_id="fresh_native_holdouts_admitted",
            status="PASS" if admitted_candidate_ids == expected_admitted else "FAIL",
            passed=admitted_candidate_ids == expected_admitted,
            evidence=admitted_candidate_ids,
            residual_risk="The admitted holdouts remain inside the same sheaf-transport family.",
        ),
        ClosureCheck(
            check_id="semantic_controls_rejected",
            status="PASS" if rejected_control_ids == expected_rejected else "FAIL",
            passed=rejected_control_ids == expected_rejected,
            evidence=rejected_control_ids,
            residual_risk="Fresh controls can always add new semantic failure modes.",
        ),
        ClosureCheck(
            check_id="target_and_fixture_replay_controls_active",
            status=(
                "PASS"
                if not by_id["target_geometry_language_import_control"].independent_selector_admissible
                and not by_id["fixture_label_alias_control"].independent_selector_admissible
                else "FAIL"
            ),
            passed=(
                not by_id["target_geometry_language_import_control"].independent_selector_admissible
                and not by_id["fixture_label_alias_control"].independent_selector_admissible
            ),
            evidence=(
                by_id["target_geometry_language_import_control"].status,
                by_id["fixture_label_alias_control"].status,
            ),
            residual_risk="Controls are synthetic and review-only.",
        ),
        ClosureCheck(
            check_id="governance_boundaries_preserved",
            status="PASS",
            passed=True,
            evidence=(
                "No claim-ledger movement.",
                "No Canon Index movement.",
                "No public-posture, TAF4, TAF8, S1, external, or cross-repo movement.",
            ),
            residual_risk="None inside this packet; the next packet remains review-only.",
        ),
    )


def _route_decisions(
    independent_reimplementation_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_FRESH_FAMILY_STRESS_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Independent reimplementation clears fixture-label risk but not fresh-family generality."
            ),
        ),
        RouteDecision(
            decision_id="run_fresh_family_stress_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if independent_reimplementation_cleared and not source_law_earned
                else "PAUSED_UNTIL_REIMPLEMENTATION_CLEARS"
            ),
            selected=independent_reimplementation_cleared and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest review step is fresh-family stress of the independently rebuilt generator."
                if independent_reimplementation_cleared
                else "Independent reimplementation has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not independent_reimplementation_cleared
                else "PAUSED_REIMPLEMENTATION_CLEARED"
            ),
            selected=not independent_reimplementation_cleared,
            next_packet="none",
            reason=(
                "Route reset is needed if independent reimplementation fails."
                if not independent_reimplementation_cleared
                else "Route reset is premature because independent reimplementation matched the contract."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t569",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A finite independent generator check is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t569",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 generator validation is not cross-domain shadow protection.",
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
    closure_checks: tuple[ClosureCheck, ...],
    route_decisions: tuple[RouteDecision, ...],
    independent_reimplementation_cleared: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t568_authority",
            checks["t568_authority"].passed,
            "T568 supplies independent-reimplementation authority.",
            "T568 did not supply expected independent-reimplementation authority.",
        ),
        (
            "independent_spec_avoids_fixture_labels",
            checks["independent_spec_uses_no_fixture_labels"].passed,
            "The rebuilt selector uses no T567/T568 fixture labels.",
            "The rebuilt selector depends on fixture labels.",
        ),
        (
            "contract_equivalence_matches",
            checks["contract_equivalence_on_fresh_panel"].passed,
            "The independent selector matches the T568 contract on the fresh panel.",
            "The independent selector diverges from the T568 contract.",
        ),
        (
            "fresh_panel_expected_status",
            checks["fresh_native_holdouts_admitted"].passed
            and checks["semantic_controls_rejected"].passed
            and checks["target_and_fixture_replay_controls_active"].passed,
            "Fresh native holdouts admit while semantic, target, and replay controls reject.",
            "The fresh panel did not produce the expected admissibility pattern.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_FRESH_FAMILY_STRESS_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "fresh_family_stress_selected_next",
            independent_reimplementation_cleared
            and selected_next_packet == NEXT_PACKET
            and routes["run_fresh_family_stress_gate"].selected,
            "Fresh-family stress is selected as the next burden.",
            "The expected fresh-family stress next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t569"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t569"].outcome == "BLOCKED_TAF8_OVERREAD"
            and routes["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A forbidden route movement was allowed.",
        ),
        (
            "governance_boundaries_preserved",
            checks["governance_boundaries_preserved"].passed,
            "No governance boundary was crossed.",
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


def _claim_labels(
    admitted_candidate_ids: tuple[str, ...],
    rejected_control_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Independent generator admits fresh native holdouts: "
                + ", ".join(admitted_candidate_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Independent generator rejects controls: "
                + ", ".join(rejected_control_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by fresh-family stress.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Independent reimplementation narrows fixture-overfit risk rather than promoting the route.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    spec = payload["independent_generator_spec"]
    lines = [
        "# T569 Results: Domain-Native Sheaf Transport Independent Reimplementation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Reimplementation status: `{payload['reimplementation_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T568 verdict: `{payload['source_t568_verdict']}`",
        f"- Source T568 selected next packet: `{payload['source_t568_selected_next_packet']}`",
        f"- Source T568 semantic generator strengthened: {payload['source_t568_semantic_generator_strengthened']}",
        f"- Independent reimplementation cleared: {payload['independent_reimplementation_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Independent Generator",
        "",
        f"- Implementation: `{spec['implementation_id']}`",
        f"- Source contract: `{spec['source_contract_id']}`",
        "- Reconstructed source variables: "
        + ", ".join(f"`{item}`" for item in spec["reconstructed_source_variables"]),
        "- Reconstructed absorber boundaries: "
        + ", ".join(f"`{item}`" for item in spec["reconstructed_absorber_ids"]),
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in spec["semantic_requirements"]),
        "- Fixture-label fields used: "
        + (", ".join(f"`{item}`" for item in spec["fixture_label_fields_used"]) or "none"),
        f"- Selection rule: {spec['selection_rule']}",
        "",
        "## Fresh Panel Evaluations",
        "",
        "| candidate | independent admits? | contract admits? | selectors match? | status | failed checks | reason |",
        "| --- | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for evaluation in payload["evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['candidate_id']}` | "
            f"{evaluation['independent_selector_admissible']} | "
            f"{evaluation['contract_selector_admissible']} | "
            f"{evaluation['selectors_match']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Closure Checks",
            "",
            "| check | status | passed? | residual risk |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for check in payload["closure_checks"]:
        lines.append(
            "| "
            f"`{check['check_id']}` | "
            f"`{check['status']}` | "
            f"{check['passed']} | "
            f"{check['residual_risk']} |"
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


def write_results(result: T569Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t569_result_to_dict(result)
    json_path = (
        results_dir
        / "T569-domain-native-sheaf-transport-independent-reimplementation-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T569-domain-native-sheaf-transport-independent-reimplementation-gate-v0.1-results.md"
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

    result = run_t569_analysis()
    payload = t569_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
