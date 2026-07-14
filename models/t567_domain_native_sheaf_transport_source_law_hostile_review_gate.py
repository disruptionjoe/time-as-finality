"""T567: hostile review of the domain-native sheaf transport source-law packet.

T566 completed the internal T564/T565/T566 source-law review packet, but only
at review tier. T567 stress-tests the typed generator with same-field
adversaries before any claim, canon, public-posture, TAF4, TAF8, S1, external
publication, or cross-repo movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565
from models import t566_domain_native_sheaf_transport_typed_generator_gate as t566


ARTIFACT = "T567-domain-native-sheaf-transport-source-law-hostile-review-gate-v0.1"
VERDICT = (
    "domain_native_sheaf_transport_hostile_review_exposes_semantic_generator_burden_review_only"
)
HOSTILE_REVIEW_STATUS = "HOSTILE_REVIEW_NARROWS_TYPED_GENERATOR"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_SEMANTIC_GENERATOR_REQUIRED"
ROUTE_STATUS = "semantic_generator_strengthening_required"
NEXT_PACKET = "t568_domain_native_sheaf_transport_semantic_generator_strengthening_gate"

NOT_CLAIMED = (
    "T567 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It hostile-reviews the "
    "internal T564/T565/T566 packet and selects a semantic-generator "
    "strengthening burden."
)


@dataclass(frozen=True)
class HostileAdversary:
    adversary_id: str
    adversary_class: str
    native_record_scenario: str
    predeclared_before_outcome_reading: bool
    source_variables: tuple[str, ...]
    absorber_ids: tuple[str, ...]
    forbidden_shortcuts_used: tuple[str, ...]
    outcome_label_read: bool
    nontrivial_obstruction_witnesses: bool
    noncommuting_transport_square: bool
    native_payload_forced: bool
    disguised_target_import_terms: tuple[str, ...]
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_variables",
            "absorber_ids",
            "forbidden_shortcuts_used",
            "disguised_target_import_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class HostileEvaluation:
    adversary_id: str
    t566_selector_admissible: bool
    hostile_review_admissible: bool
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
class ReviewCheck:
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
class T567Result:
    artifact: str
    source_t566_verdict: str
    source_t566_selected_next_packet: str
    source_t566_review_packet_complete: bool
    hostile_review_status: str
    source_law_status: str
    route_status: str
    adversaries: tuple[HostileAdversary, ...]
    hostile_evaluations: tuple[HostileEvaluation, ...]
    review_checks: tuple[ReviewCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    valid_alternate_survivor_ids: tuple[str, ...]
    semantic_gap_adversary_ids: tuple[str, ...]
    t566_field_selector_survives_narrow_contract: bool
    semantic_generator_burden_exposed: bool
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


def run_t567_analysis() -> T567Result:
    source = t566.run_t566_analysis()
    adversaries = _hostile_adversaries()
    evaluations = tuple(_evaluate_adversary(adversary) for adversary in adversaries)
    valid_alternate_survivor_ids = tuple(
        item.adversary_id
        for item in evaluations
        if item.hostile_review_admissible
    )
    semantic_gap_adversary_ids = tuple(
        item.adversary_id
        for item in evaluations
        if item.t566_selector_admissible and not item.hostile_review_admissible
    )
    semantic_generator_burden_exposed = bool(semantic_gap_adversary_ids)
    t566_field_selector_survives_narrow_contract = (
        source.verdict == t566.VERDICT
        and source.selected_next_packet == t566.NEXT_PACKET
        and source.source_law_review_packet_complete
    )
    source_law_earned = False
    review_checks = _review_checks(
        source=source,
        evaluations=evaluations,
        valid_alternate_survivor_ids=valid_alternate_survivor_ids,
        semantic_gap_adversary_ids=semantic_gap_adversary_ids,
    )
    route_decisions = _route_decisions(
        semantic_generator_burden_exposed=semantic_generator_burden_exposed,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        t566_field_selector_survives_narrow_contract=t566_field_selector_survives_narrow_contract,
        valid_alternate_survivor_ids=valid_alternate_survivor_ids,
        semantic_gap_adversary_ids=semantic_gap_adversary_ids,
        semantic_generator_burden_exposed=semantic_generator_burden_exposed,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        route_decisions=route_decisions,
    )
    verdict = (
        VERDICT
        if t566_field_selector_survives_narrow_contract
        and semantic_generator_burden_exposed
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_hostile_review_unexpected_status"
    )

    return T567Result(
        artifact=ARTIFACT,
        source_t566_verdict=source.verdict,
        source_t566_selected_next_packet=source.selected_next_packet,
        source_t566_review_packet_complete=source.source_law_review_packet_complete,
        hostile_review_status=HOSTILE_REVIEW_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        adversaries=adversaries,
        hostile_evaluations=evaluations,
        review_checks=review_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        valid_alternate_survivor_ids=valid_alternate_survivor_ids,
        semantic_gap_adversary_ids=semantic_gap_adversary_ids,
        t566_field_selector_survives_narrow_contract=t566_field_selector_survives_narrow_contract,
        semantic_generator_burden_exposed=semantic_generator_burden_exposed,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T567 preserves T566 as a field-complete selector but hostile "
            "review exposes a semantic gap: field-name completeness alone can "
            "admit absorber-complete trivial packets and disguised target-import "
            "language. The source-law route is narrowed, not promoted."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next gate should strengthen the generator "
            "with semantic nontriviality, noncommuting transport-square, "
            "native-payload-forcing, and target-language screens before any "
            "source-law, claim, canon, public-posture, TAF4, TAF8, or S1 movement."
        ),
        taf11_update=(
            "TAF11 remains the active top lane, but the route is narrowed: "
            "hostile review found valid alternate same-field survivors and "
            "also found semantic adversaries that T566's field selector is too "
            "coarse to reject."
        ),
        taf4_update=(
            "TAF4 remains blocked. T567 is a finite generator hostile-review "
            "gate, not finite-to-continuum descent, causal-set recovery, "
            "Lorentzian target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T567 is internal TAF11 source-law hygiene, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            valid_alternate_survivor_ids=valid_alternate_survivor_ids,
            semantic_gap_adversary_ids=semantic_gap_adversary_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T567 narrows the TAF11 route to "
            "a semantic-generator strengthening burden; claim rows, Canon Index "
            "tiers, canon verdicts, and public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t567_result_to_dict(result: T567Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t566_verdict": result.source_t566_verdict,
        "source_t566_selected_next_packet": result.source_t566_selected_next_packet,
        "source_t566_review_packet_complete": result.source_t566_review_packet_complete,
        "hostile_review_status": result.hostile_review_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "adversaries": [item.to_dict() for item in result.adversaries],
        "hostile_evaluations": [
            item.to_dict() for item in result.hostile_evaluations
        ],
        "review_checks": [item.to_dict() for item in result.review_checks],
        "route_decisions": [item.to_dict() for item in result.route_decisions],
        "gate_decisions": [item.to_dict() for item in result.gate_decisions],
        "valid_alternate_survivor_ids": list(result.valid_alternate_survivor_ids),
        "semantic_gap_adversary_ids": list(result.semantic_gap_adversary_ids),
        "t566_field_selector_survives_narrow_contract": result.t566_field_selector_survives_narrow_contract,
        "semantic_generator_burden_exposed": result.semantic_generator_burden_exposed,
        "source_law_earned": result.source_law_earned,
        "selected_next_packet": result.selected_next_packet,
        "verdict": result.verdict,
        "source_law_reading": result.source_law_reading,
        "recommended_next": result.recommended_next,
        "taf11_update": result.taf11_update,
        "taf4_update": result.taf4_update,
        "taf8_update": result.taf8_update,
        "claim_labels": [item.to_dict() for item in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _hostile_adversaries() -> tuple[HostileAdversary, ...]:
    return (
        HostileAdversary(
            adversary_id="alternate_multisig_delay_repair_survivor",
            adversary_class="alternate_native_record_scenario",
            native_record_scenario="multi-signature delay repair with rotating certificate windows",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            nontrivial_obstruction_witnesses=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            disguised_target_import_terms=(),
            rationale=(
                "A same-field finality-native alternate with nontrivial "
                "obstruction and transport-square content."
            ),
        ),
        HostileAdversary(
            adversary_id="alternate_checkpoint_quorum_repair_survivor",
            adversary_class="alternate_native_record_scenario",
            native_record_scenario="checkpoint quorum repair with staggered local finality sections",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            nontrivial_obstruction_witnesses=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            disguised_target_import_terms=(),
            rationale=(
                "A second same-field survivor that changes the native record "
                "scenario without target labels or replay."
            ),
        ),
        HostileAdversary(
            adversary_id="absorber_complete_trivial_gluing_case",
            adversary_class="absorber_complete_but_trivial_case",
            native_record_scenario="same-cover sheaf gluing bookkeeping",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            nontrivial_obstruction_witnesses=False,
            noncommuting_transport_square=False,
            native_payload_forced=False,
            disguised_target_import_terms=(),
            rationale=(
                "Has every field name and absorber boundary, but carries no "
                "nontrivial obstruction, no noncommuting square, and no forced "
                "record-finality payload."
            ),
        ),
        HostileAdversary(
            adversary_id="disguised_lorentzian_target_import",
            adversary_class="disguised_target_import",
            native_record_scenario="record repair described by causal-set link recovery",
            predeclared_before_outcome_reading=True,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            nontrivial_obstruction_witnesses=True,
            noncommuting_transport_square=True,
            native_payload_forced=False,
            disguised_target_import_terms=(
                "causal_set_link_recovery",
                "lorentzian_dimension_target",
            ),
            rationale=(
                "Keeps the same field names but smuggles target geometry into "
                "the scenario language instead of forcing a finality-native payload."
            ),
        ),
        HostileAdversary(
            adversary_id="missing_obstruction_witness_underdeclared_control",
            adversary_class="underdeclared_generator_control",
            native_record_scenario="underdeclared repair packet",
            predeclared_before_outcome_reading=True,
            source_variables=tuple(
                item
                for item in t565.FROZEN_SOURCE_VARIABLES
                if item != "settlement_obstruction_witnesses"
            ),
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=False,
            nontrivial_obstruction_witnesses=False,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            disguised_target_import_terms=(),
            rationale="Verifies T566 still rejects missing source-variable controls.",
        ),
        HostileAdversary(
            adversary_id="posthoc_outcome_reading_control",
            adversary_class="posthoc_control",
            native_record_scenario="post-hoc repair packet",
            predeclared_before_outcome_reading=False,
            source_variables=t565.FROZEN_SOURCE_VARIABLES,
            absorber_ids=t565.FROZEN_ABSORBER_IDS,
            forbidden_shortcuts_used=(),
            outcome_label_read=True,
            nontrivial_obstruction_witnesses=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            disguised_target_import_terms=(),
            rationale="Verifies outcome-reading controls still reject.",
        ),
    )


def _evaluate_adversary(adversary: HostileAdversary) -> HostileEvaluation:
    checks = (
        (
            "t566_field_selector_admits",
            _t566_selector_admits(adversary),
        ),
        (
            "semantic_nontriviality",
            adversary.nontrivial_obstruction_witnesses
            and adversary.noncommuting_transport_square,
        ),
        ("native_payload_forced", adversary.native_payload_forced),
        (
            "target_blind_language",
            adversary.disguised_target_import_terms == (),
        ),
        (
            "forbidden_shortcuts_absent",
            adversary.forbidden_shortcuts_used == (),
        ),
    )
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    t566_selector_admissible = "t566_field_selector_admits" in passed
    hostile_review_admissible = not failed
    if hostile_review_admissible:
        status = "SURVIVES_HOSTILE_REVIEW"
        reason = "The same-field alternate survives both T566 and semantic hostile review."
    elif t566_selector_admissible:
        status = "T566_SELECTOR_ADMITS_HOSTILE_REJECTS"
        reason = (
            "The T566 field selector admits this case, but hostile review rejects "
            "it because: "
            + ", ".join(failed)
        )
    else:
        status = "REJECTED_BY_T566_AND_HOSTILE_REVIEW"
        reason = (
            "The case is already rejected before semantic hostile review because: "
            + ", ".join(failed)
        )
    return HostileEvaluation(
        adversary_id=adversary.adversary_id,
        t566_selector_admissible=t566_selector_admissible,
        hostile_review_admissible=hostile_review_admissible,
        status=status,
        passed_checks=passed,
        failed_checks=failed,
        reason=reason,
    )


def _t566_selector_admits(adversary: HostileAdversary) -> bool:
    return (
        adversary.predeclared_before_outcome_reading
        and not adversary.outcome_label_read
        and adversary.source_variables == t565.FROZEN_SOURCE_VARIABLES
        and adversary.absorber_ids == t565.FROZEN_ABSORBER_IDS
        and adversary.forbidden_shortcuts_used == ()
        and adversary.native_record_scenario
        != "t565 rotating multi-ledger repair holdout"
    )


def _review_checks(
    source: t566.T566Result,
    evaluations: tuple[HostileEvaluation, ...],
    valid_alternate_survivor_ids: tuple[str, ...],
    semantic_gap_adversary_ids: tuple[str, ...],
) -> tuple[ReviewCheck, ...]:
    by_id = {item.adversary_id: item for item in evaluations}
    t566_authority = (
        source.verdict == t566.VERDICT
        and source.selected_next_packet == t566.NEXT_PACKET
        and source.source_law_review_packet_complete
    )
    original_controls_rejected = (
        not by_id["missing_obstruction_witness_underdeclared_control"].t566_selector_admissible
        and not by_id["posthoc_outcome_reading_control"].t566_selector_admissible
    )
    return (
        ReviewCheck(
            check_id="t566_authority",
            status="PASS" if t566_authority else "FAIL",
            passed=t566_authority,
            evidence=(
                "T566 verdict is the typed-generator review-only clearance.",
                "T566 selected T567 as hostile review.",
                "T566 marked the internal T564/T565/T566 packet complete but not promoted.",
            ),
            residual_risk="T566 is a narrow field selector, not source-law status.",
        ),
        ReviewCheck(
            check_id="valid_same_field_alternates_survive",
            status="PASS" if len(valid_alternate_survivor_ids) == 2 else "FAIL",
            passed=len(valid_alternate_survivor_ids) == 2,
            evidence=valid_alternate_survivor_ids,
            residual_risk=(
                "The surviving alternates show the route is not empty, but they "
                "do not erase the semantic generator burden."
            ),
        ),
        ReviewCheck(
            check_id="absorber_complete_trivial_case_exposes_ceiling",
            status=(
                "FIRES"
                if by_id["absorber_complete_trivial_gluing_case"].adversary_id
                in semantic_gap_adversary_ids
                else "CLEARED"
            ),
            passed=(
                by_id["absorber_complete_trivial_gluing_case"].adversary_id
                in semantic_gap_adversary_ids
            ),
            evidence=(
                "The trivial case has every frozen field name and absorber boundary.",
                "T566 admits it under the field-selector contract.",
                "Hostile review rejects it for missing semantic nontriviality and native payload forcing.",
            ),
            residual_risk=(
                "A strengthened generator must inspect nontrivial obstruction "
                "and noncommuting transport-square content, not only field names."
            ),
        ),
        ReviewCheck(
            check_id="disguised_target_import_exposes_ceiling",
            status=(
                "FIRES"
                if by_id["disguised_lorentzian_target_import"].adversary_id
                in semantic_gap_adversary_ids
                else "CLEARED"
            ),
            passed=(
                by_id["disguised_lorentzian_target_import"].adversary_id
                in semantic_gap_adversary_ids
            ),
            evidence=(
                "The disguised import has every frozen field name and absorber boundary.",
                "T566 admits it because the explicit shortcut list is empty.",
                "Hostile review rejects target-geometry language and absent native-payload forcing.",
            ),
            residual_risk=(
                "A strengthened generator must screen scenario language for "
                "target imports instead of relying only on declared shortcut flags."
            ),
        ),
        ReviewCheck(
            check_id="original_t566_controls_still_reject",
            status="PASS" if original_controls_rejected else "FAIL",
            passed=original_controls_rejected,
            evidence=(
                "Missing source-variable control is rejected.",
                "Post-hoc outcome-reading control is rejected.",
            ),
            residual_risk=(
                "The original T566 checks still matter, but they are insufficient "
                "for semantic source-law readiness."
            ),
        ),
        ReviewCheck(
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
    semantic_generator_burden_exposed: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_SEMANTIC_GENERATOR_BURDEN"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Hostile review exposed a semantic generator burden, so source-law promotion is rejected."
            ),
        ),
        RouteDecision(
            decision_id="run_semantic_generator_strengthening_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if semantic_generator_burden_exposed
                else "PAUSED_NO_SEMANTIC_GAP"
            ),
            selected=semantic_generator_burden_exposed and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The T566 field selector must be strengthened against semantic triviality and disguised target import."
                if semantic_generator_burden_exposed
                else "No semantic gap was found."
            ),
        ),
        RouteDecision(
            decision_id="run_independent_reimplementation_now",
            outcome="PAUSED_UNTIL_SEMANTIC_GENERATOR_STRENGTHENED",
            selected=False,
            next_packet="none",
            reason="Independent reimplementation is premature until the generator's semantic fields are tightened.",
        ),
        RouteDecision(
            decision_id="move_taf4_from_t567",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A finite hostile-review result is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t567",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 hostile review is not cross-domain shadow protection.",
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
    t566_field_selector_survives_narrow_contract: bool,
    valid_alternate_survivor_ids: tuple[str, ...],
    semantic_gap_adversary_ids: tuple[str, ...],
    semantic_generator_burden_exposed: bool,
    source_law_earned: bool,
    selected_next_packet: str,
    route_decisions: tuple[RouteDecision, ...],
) -> tuple[GateDecision, ...]:
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t566_authority",
            t566_field_selector_survives_narrow_contract,
            "T566 supplies the expected hostile-review authority.",
            "T566 did not supply the expected hostile-review authority.",
        ),
        (
            "same_field_alternates_survive",
            len(valid_alternate_survivor_ids) == 2,
            "Two alternate finality-native same-field cases survive hostile review.",
            "The hostile review did not preserve valid same-field alternates.",
        ),
        (
            "semantic_gaps_detected",
            semantic_gap_adversary_ids
            == (
                "absorber_complete_trivial_gluing_case",
                "disguised_lorentzian_target_import",
            ),
            "Hostile review detects both absorber-complete triviality and disguised target import gaps.",
            "The expected semantic gaps were not detected.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_SEMANTIC_GENERATOR_BURDEN",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "semantic_strengthening_selected_next",
            semantic_generator_burden_exposed
            and selected_next_packet == NEXT_PACKET
            and routes["run_semantic_generator_strengthening_gate"].selected,
            "Semantic generator strengthening is selected as the next burden.",
            "The expected T568 semantic-strengthening burden was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t567"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t567"].outcome == "BLOCKED_TAF8_OVERREAD"
            and routes["move_s1_or_cross_repo_truth"].outcome == "BLOCKED_GOVERNANCE",
            "TAF4, TAF8, S1, cross-repo, publication, claim, canon, and public-posture shortcuts are blocked.",
            "A forbidden route movement was allowed.",
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
    valid_alternate_survivor_ids: tuple[str, ...],
    semantic_gap_adversary_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Same-field alternate survivors: "
                + ", ".join(valid_alternate_survivor_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Semantic generator gaps exposed by: "
                + ", ".join(semantic_gap_adversary_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by semantic generator strengthening.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Hostile review narrows the route rather than killing it or promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T567 Results: Domain-Native Sheaf Transport Source-Law Hostile Review Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Hostile review status: `{payload['hostile_review_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T566 verdict: `{payload['source_t566_verdict']}`",
        f"- Source T566 selected next packet: `{payload['source_t566_selected_next_packet']}`",
        f"- Source T566 review packet complete: {payload['source_t566_review_packet_complete']}",
        f"- T566 field selector survives narrow contract: {payload['t566_field_selector_survives_narrow_contract']}",
        f"- Semantic generator burden exposed: {payload['semantic_generator_burden_exposed']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Hostile Evaluations",
        "",
        "| adversary | T566 selector admits? | hostile review admits? | status | failed checks | reason |",
        "| --- | :---: | :---: | --- | --- | --- |",
    ]
    for evaluation in payload["hostile_evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['adversary_id']}` | "
            f"{evaluation['t566_selector_admissible']} | "
            f"{evaluation['hostile_review_admissible']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Review Checks",
            "",
            "| check | status | passed? | residual risk |",
            "| --- | --- | :---: | --- |",
        ]
    )
    for check in payload["review_checks"]:
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


def write_results(result: T567Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t567_result_to_dict(result)
    json_path = (
        results_dir
        / "T567-domain-native-sheaf-transport-source-law-hostile-review-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T567-domain-native-sheaf-transport-source-law-hostile-review-gate-v0.1-results.md"
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

    result = run_t567_analysis()
    payload = t567_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
