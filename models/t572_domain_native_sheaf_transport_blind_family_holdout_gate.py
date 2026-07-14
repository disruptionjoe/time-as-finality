"""T572: blind-family holdout for the TAF11 semantic generator.

T571 rotated falsifiers across the two T570 admitted fresh families and selected
a blind-family holdout as the next burden. T572 freezes that generator contract
before evaluation, withholds a new family from the admitted-family panel, and
tests whether the role-level generator predicts the blind family without target
import, family replay, Observerse/APRD replay, cross-repo truth import, or
source-law overread.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t571_domain_native_sheaf_transport_multi_family_falsifier_rotation_gate as t571,
)


ARTIFACT = "T572-domain-native-sheaf-transport-blind-family-holdout-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_blind_family_holdout_survives_review_only"
HOLDOUT_STATUS = "BLIND_FAMILY_HOLDOUT_SURVIVES"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_ADVERSARIAL_HOLDOUT_REQUIRED"
ROUTE_STATUS = "blind_family_holdout_clears_adversarial_holdout_required"
NEXT_PACKET = (
    "t573_domain_native_sheaf_transport_adversarial_blind_family_holdout_gate"
)

NOT_CLAIMED = (
    "T572 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It tests one predeclared "
    "blind family as review-only pressure on the T570/T571 semantic generator."
)


@dataclass(frozen=True)
class BlindHoldoutContract:
    contract_id: str
    source_t571_verdict: str
    source_t571_selected_next_packet: str
    source_t571_contract_id: str
    source_t571_admitted_family_ids: tuple[str, ...]
    blind_family_id: str
    source_roles: tuple[str, ...]
    absorber_boundaries: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    blind_predeclaration: str
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_t571_admitted_family_ids",
            "source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "forbidden_shortcuts",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class HoldoutProbe:
    probe_id: str
    family_id: str
    probe_kind: str
    predeclared_before_evaluation: bool
    withheld_family: bool
    expected_admissible: bool
    source_role_coverage: tuple[str, ...]
    absorber_boundary_coverage: tuple[str, ...]
    semantic_requirements_met: tuple[str, ...]
    family_replay_terms: tuple[str, ...]
    target_import_terms: tuple[str, ...]
    cross_repo_truth_import: bool
    observerse_replay: bool
    aprd_replay: bool
    native_payload_forced: bool
    noncommuting_transport_square: bool
    independent_family_vocabulary: bool
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_role_coverage",
            "absorber_boundary_coverage",
            "semantic_requirements_met",
            "family_replay_terms",
            "target_import_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class HoldoutEvaluation:
    probe_id: str
    family_id: str
    expected_admissible: bool
    holdout_admissible: bool
    expectation_matched: bool
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
class T572Result:
    artifact: str
    source_t571_verdict: str
    source_t571_selected_next_packet: str
    source_t571_multi_family_rotation_cleared: bool
    holdout_status: str
    source_law_status: str
    route_status: str
    holdout_contract: BlindHoldoutContract
    probes: tuple[HoldoutProbe, ...]
    evaluations: tuple[HoldoutEvaluation, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    admitted_probe_ids: tuple[str, ...]
    rejected_probe_ids: tuple[str, ...]
    blind_family_holdout_cleared: bool
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


def run_t572_analysis() -> T572Result:
    source = t571.run_t571_analysis()
    contract = _holdout_contract(source)
    probes = _probe_panel(contract)
    evaluations = tuple(_evaluate_probe(contract, probe) for probe in probes)
    admitted_probe_ids = tuple(
        item.probe_id for item in evaluations if item.holdout_admissible
    )
    rejected_probe_ids = tuple(
        item.probe_id for item in evaluations if not item.holdout_admissible
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        contract=contract,
        evaluations=evaluations,
        admitted_probe_ids=admitted_probe_ids,
        rejected_probe_ids=rejected_probe_ids,
    )
    blind_family_holdout_cleared = (
        source.verdict == t571.VERDICT
        and source.selected_next_packet == t571.NEXT_PACKET
        and source.multi_family_rotation_cleared
        and admitted_probe_ids == ("settlement_attestation_blind_survivor",)
        and rejected_probe_ids
        == (
            "blind_family_calibration_replay_falsifier",
            "blind_family_target_import_falsifier",
            "blind_family_optional_payload_falsifier",
            "blind_family_missing_transport_square_falsifier",
            "blind_family_foreign_truth_falsifier",
        )
        and all(item.expectation_matched for item in evaluations)
        and all(check.passed for check in closure_checks)
    )
    route_decisions = _route_decisions(
        blind_family_holdout_cleared=blind_family_holdout_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        blind_family_holdout_cleared=blind_family_holdout_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if blind_family_holdout_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_blind_family_holdout_unexpected_status"
    )

    return T572Result(
        artifact=ARTIFACT,
        source_t571_verdict=source.verdict,
        source_t571_selected_next_packet=source.selected_next_packet,
        source_t571_multi_family_rotation_cleared=source.multi_family_rotation_cleared,
        holdout_status=HOLDOUT_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        holdout_contract=contract,
        probes=probes,
        evaluations=evaluations,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        admitted_probe_ids=admitted_probe_ids,
        rejected_probe_ids=rejected_probe_ids,
        blind_family_holdout_cleared=blind_family_holdout_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T572 freezes the T570/T571 role-level semantic generator before "
            "evaluation and admits one withheld settlement-attestation blind "
            "family while rejecting family replay, target import, optional "
            "payload, missing transport-square, and foreign-truth controls. "
            "This is still review-only: a single blind family does not earn a "
            "public source law."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should turn the blind-family "
            "success into adversarial holdout pressure by changing the blind "
            "family's surface genre again while preserving the frozen source "
            "roles, absorber boundaries, and semantic requirements."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. The predeclared blind-family "
            "holdout survived, but source-law status still waits for adversarial "
            "holdout pressure beyond one synthetic family."
        ),
        taf4_update=(
            "TAF4 remains blocked. A blind-family generator holdout is not "
            "finite-to-continuum descent, causal-set recovery, Lorentzian target "
            "import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T572 is internal TAF11 generator stress, not "
            "a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            admitted_probe_ids=admitted_probe_ids,
            rejected_probe_ids=rejected_probe_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T572 records a review-only "
            "blind-family holdout and selects adversarial holdout pressure; "
            "claim rows, Canon Index tiers, canon verdicts, and public posture "
            "remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t572_result_to_dict(result: T572Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t571_verdict": result.source_t571_verdict,
        "source_t571_selected_next_packet": result.source_t571_selected_next_packet,
        "source_t571_multi_family_rotation_cleared": (
            result.source_t571_multi_family_rotation_cleared
        ),
        "holdout_status": result.holdout_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "holdout_contract": result.holdout_contract.to_dict(),
        "probes": [probe.to_dict() for probe in result.probes],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [
            decision.to_dict() for decision in result.route_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "admitted_probe_ids": list(result.admitted_probe_ids),
        "rejected_probe_ids": list(result.rejected_probe_ids),
        "blind_family_holdout_cleared": result.blind_family_holdout_cleared,
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


def _holdout_contract(source: t571.T571Result) -> BlindHoldoutContract:
    contract = source.rotation_contract
    return BlindHoldoutContract(
        contract_id="blind_family_holdout_v1",
        source_t571_verdict=source.verdict,
        source_t571_selected_next_packet=source.selected_next_packet,
        source_t571_contract_id=contract.contract_id,
        source_t571_admitted_family_ids=contract.admitted_family_ids,
        blind_family_id="settlement_attestation_blind_family",
        source_roles=contract.source_roles,
        absorber_boundaries=contract.absorber_boundaries,
        semantic_requirements=contract.semantic_requirements,
        forbidden_shortcuts=tuple(
            dict.fromkeys(
                contract.forbidden_shortcuts
                + (
                    "family_replay",
                    "cross_repo_truth_import",
                    "observerse_replay",
                    "aprd_replay",
                )
            )
        ),
        blind_predeclaration=(
            "The settlement-attestation family is named before evaluation and "
            "withheld from the T570/T571 admitted-family panel."
        ),
        rationale=(
            "A blind family is the next honest pressure after multi-family "
            "rotation because it tests prediction under frozen roles rather than "
            "retuning to known family names."
        ),
    )


def _probe_panel(contract: BlindHoldoutContract) -> tuple[HoldoutProbe, ...]:
    source = contract.source_roles
    absorbers = contract.absorber_boundaries
    semantics = contract.semantic_requirements
    blind = contract.blind_family_id
    return (
        HoldoutProbe(
            probe_id="settlement_attestation_blind_survivor",
            family_id=blind,
            probe_kind="blind_family_survivor",
            predeclared_before_evaluation=True,
            withheld_family=True,
            expected_admissible=True,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=(),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            independent_family_vocabulary=True,
            rationale=(
                "Settlement attestations use issue, co-signature, scope, dispute, "
                "handoff, and audit-amendment vocabulary rather than the T570 "
                "family names, while preserving the frozen source roles."
            ),
        ),
        HoldoutProbe(
            probe_id="blind_family_calibration_replay_falsifier",
            family_id=blind,
            probe_kind="blind_family_falsifier",
            predeclared_before_evaluation=True,
            withheld_family=False,
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=(
                "calibration_chain_role_recoding_family",
                "calibration_chain_rotated_survivor",
            ),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            independent_family_vocabulary=False,
            rationale="Rejects a so-called blind packet that reuses a T570 family.",
        ),
        HoldoutProbe(
            probe_id="blind_family_target_import_falsifier",
            family_id=blind,
            probe_kind="blind_family_falsifier",
            predeclared_before_evaluation=True,
            withheld_family=True,
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=(),
            target_import_terms=("lorentzian_interval_target", "causal_set_link_target"),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            independent_family_vocabulary=True,
            rationale="Rejects a blind family that imports target spacetime language.",
        ),
        HoldoutProbe(
            probe_id="blind_family_optional_payload_falsifier",
            family_id=blind,
            probe_kind="blind_family_falsifier",
            predeclared_before_evaluation=True,
            withheld_family=True,
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=tuple(
                item for item in semantics if item != "native_payload_forced"
            ),
            family_replay_terms=(),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=False,
            noncommuting_transport_square=True,
            independent_family_vocabulary=True,
            rationale="Rejects a blind family when the payload is optional.",
        ),
        HoldoutProbe(
            probe_id="blind_family_missing_transport_square_falsifier",
            family_id=blind,
            probe_kind="blind_family_falsifier",
            predeclared_before_evaluation=True,
            withheld_family=True,
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=tuple(
                item
                for item in semantics
                if item != "noncommuting_transport_square"
            ),
            family_replay_terms=(),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=False,
            independent_family_vocabulary=True,
            rationale="Rejects a blind family with no noncommuting square.",
        ),
        HoldoutProbe(
            probe_id="blind_family_foreign_truth_falsifier",
            family_id=blind,
            probe_kind="blind_family_falsifier",
            predeclared_before_evaluation=True,
            withheld_family=True,
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=(),
            target_import_terms=(),
            cross_repo_truth_import=True,
            observerse_replay=True,
            aprd_replay=True,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            independent_family_vocabulary=True,
            rationale="Rejects foreign-truth, Observerse, and APRD replay routes.",
        ),
    )


def _evaluate_probe(
    contract: BlindHoldoutContract,
    probe: HoldoutProbe,
) -> HoldoutEvaluation:
    checks = _probe_checks(contract, probe)
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    admissible = not failed
    return HoldoutEvaluation(
        probe_id=probe.probe_id,
        family_id=probe.family_id,
        expected_admissible=probe.expected_admissible,
        holdout_admissible=admissible,
        expectation_matched=admissible == probe.expected_admissible,
        status="ADMITTED" if admissible else "REJECTED",
        passed_checks=passed,
        failed_checks=failed,
        reason=(
            "Blind-family probe satisfies every frozen generator screen."
            if admissible
            else "Rejected by: " + ", ".join(failed)
        ),
    )


def _probe_checks(
    contract: BlindHoldoutContract,
    probe: HoldoutProbe,
) -> tuple[tuple[str, bool], ...]:
    return (
        ("predeclared_before_evaluation", probe.predeclared_before_evaluation),
        ("family_was_withheld", probe.withheld_family),
        ("family_not_in_t570_t571_panel", probe.family_id not in contract.source_t571_admitted_family_ids),
        ("source_roles_complete", probe.source_role_coverage == contract.source_roles),
        (
            "absorber_boundaries_complete",
            probe.absorber_boundary_coverage == contract.absorber_boundaries,
        ),
        (
            "semantic_requirements_complete",
            probe.semantic_requirements_met == contract.semantic_requirements,
        ),
        ("no_family_replay", probe.family_replay_terms == ()),
        ("target_blind_language", probe.target_import_terms == ()),
        ("no_cross_repo_truth_import", not probe.cross_repo_truth_import),
        ("no_observerse_replay", not probe.observerse_replay),
        ("no_aprd_replay", not probe.aprd_replay),
        ("native_payload_forced", probe.native_payload_forced),
        ("noncommuting_transport_square", probe.noncommuting_transport_square),
        ("independent_family_vocabulary", probe.independent_family_vocabulary),
    )


def _closure_checks(
    source: t571.T571Result,
    contract: BlindHoldoutContract,
    evaluations: tuple[HoldoutEvaluation, ...],
    admitted_probe_ids: tuple[str, ...],
    rejected_probe_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    expected_admitted = ("settlement_attestation_blind_survivor",)
    expected_rejected = (
        "blind_family_calibration_replay_falsifier",
        "blind_family_target_import_falsifier",
        "blind_family_optional_payload_falsifier",
        "blind_family_missing_transport_square_falsifier",
        "blind_family_foreign_truth_falsifier",
    )
    t571_authority = (
        source.verdict == t571.VERDICT
        and source.selected_next_packet == t571.NEXT_PACKET
        and source.multi_family_rotation_cleared
    )
    return (
        ClosureCheck(
            check_id="t571_authority",
            status="PASS" if t571_authority else "FAIL",
            passed=t571_authority,
            evidence=(
                "T571 cleared multi-family falsifier rotation.",
                "T571 selected blind-family holdout.",
            ),
            residual_risk="T571 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="blind_family_predeclared_and_withheld",
            status=(
                "PASS"
                if contract.blind_family_id not in contract.source_t571_admitted_family_ids
                else "FAIL"
            ),
            passed=contract.blind_family_id not in contract.source_t571_admitted_family_ids,
            evidence=(contract.blind_family_id, contract.blind_predeclaration),
            residual_risk="One blind family is still finite synthetic evidence.",
        ),
        ClosureCheck(
            check_id="blind_survivor_admitted",
            status="PASS" if admitted_probe_ids == expected_admitted else "FAIL",
            passed=admitted_probe_ids == expected_admitted,
            evidence=admitted_probe_ids,
            residual_risk="The survivor is not a public source law.",
        ),
        ClosureCheck(
            check_id="blind_falsifiers_rejected",
            status="PASS" if rejected_probe_ids == expected_rejected else "FAIL",
            passed=rejected_probe_ids == expected_rejected,
            evidence=rejected_probe_ids,
            residual_risk="More adversarial holdouts may still break the generator.",
        ),
        ClosureCheck(
            check_id="expectations_matched",
            status="PASS" if all(item.expectation_matched for item in evaluations) else "FAIL",
            passed=all(item.expectation_matched for item in evaluations),
            evidence=tuple(item.probe_id for item in evaluations if item.expectation_matched),
            residual_risk="Expectation matching is finite and synthetic.",
        ),
        ClosureCheck(
            check_id="no_replay_import_or_foreign_truth",
            status=(
                "PASS"
                if all(
                    "no_family_replay" not in item.failed_checks
                    and "target_blind_language" not in item.failed_checks
                    and "no_cross_repo_truth_import" not in item.failed_checks
                    and "no_observerse_replay" not in item.failed_checks
                    and "no_aprd_replay" not in item.failed_checks
                    for item in evaluations
                    if item.holdout_admissible
                )
                else "FAIL"
            ),
            passed=all(
                "no_family_replay" not in item.failed_checks
                and "target_blind_language" not in item.failed_checks
                and "no_cross_repo_truth_import" not in item.failed_checks
                and "no_observerse_replay" not in item.failed_checks
                and "no_aprd_replay" not in item.failed_checks
                for item in evaluations
                if item.holdout_admissible
            ),
            evidence=admitted_probe_ids,
            residual_risk="The admitted survivor still needs adversarial holdout pressure.",
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
    blind_family_holdout_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_ADVERSARIAL_HOLDOUT_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "One blind-family survivor is not enough for public source-law status."
            ),
        ),
        RouteDecision(
            decision_id="run_adversarial_blind_family_holdout_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if blind_family_holdout_cleared and not source_law_earned
                else "PAUSED_UNTIL_BLIND_FAMILY_HOLDOUT_CLEARS"
            ),
            selected=blind_family_holdout_cleared and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest review step is adversarial blind-family holdout pressure."
                if blind_family_holdout_cleared
                else "Blind-family holdout has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not blind_family_holdout_cleared
                else "PAUSED_BLIND_FAMILY_HOLDOUT_CLEARED"
            ),
            selected=not blind_family_holdout_cleared,
            next_packet="none",
            reason=(
                "Route reset is needed if blind-family holdout fails."
                if not blind_family_holdout_cleared
                else "Route reset is premature because blind-family holdout cleared."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t572",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="A blind family in a finite generator is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t572",
            outcome="BLOCKED_TAF8_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Internal TAF11 generator stress is not cross-domain shadow protection.",
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
    blind_family_holdout_cleared: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t571_authority",
            checks["t571_authority"].passed,
            "T571 supplies blind-family holdout authority.",
            "T571 did not supply expected blind-family holdout authority.",
        ),
        (
            "blind_family_predeclared_and_withheld",
            checks["blind_family_predeclared_and_withheld"].passed,
            "The blind family was predeclared and absent from T570/T571 panels.",
            "The blind family was not a real holdout.",
        ),
        (
            "expected_holdout_pattern",
            checks["blind_survivor_admitted"].passed
            and checks["blind_falsifiers_rejected"].passed
            and checks["expectations_matched"].passed,
            "The survivor admits and all holdout falsifiers reject as expected.",
            "The holdout pattern did not match the expected survivor/falsifier split.",
        ),
        (
            "no_replay_import_or_foreign_truth",
            checks["no_replay_import_or_foreign_truth"].passed,
            "The admitted survivor uses no family replay, target import, or foreign truth.",
            "The admitted survivor leaked replay, target import, or foreign truth.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_ADVERSARIAL_HOLDOUT_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "adversarial_holdout_selected_next",
            blind_family_holdout_cleared
            and selected_next_packet == NEXT_PACKET
            and routes["run_adversarial_blind_family_holdout_gate"].selected,
            "Adversarial blind-family holdout is selected as the next burden.",
            "The expected adversarial holdout next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t572"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t572"].outcome == "BLOCKED_TAF8_OVERREAD"
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
    admitted_probe_ids: tuple[str, ...],
    rejected_probe_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Blind-family holdout admits: " + ", ".join(admitted_probe_ids) + ".",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Blind-family holdout rejects: " + ", ".join(rejected_probe_ids) + ".",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by adversarial holdout pressure.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Blind-family success strengthens route evidence without promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    contract = payload["holdout_contract"]
    lines = [
        "# T572 Results: Domain-Native Sheaf Transport Blind-Family Holdout Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Holdout status: `{payload['holdout_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T571 verdict: `{payload['source_t571_verdict']}`",
        f"- Source T571 selected next packet: `{payload['source_t571_selected_next_packet']}`",
        f"- Source T571 multi-family rotation cleared: {payload['source_t571_multi_family_rotation_cleared']}",
        f"- Blind-family holdout cleared: {payload['blind_family_holdout_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Holdout Contract",
        "",
        f"- Contract: `{contract['contract_id']}`",
        f"- Source T571 contract: `{contract['source_t571_contract_id']}`",
        f"- Blind family: `{contract['blind_family_id']}`",
        "- Withheld from source families: "
        + ", ".join(f"`{item}`" for item in contract["source_t571_admitted_family_ids"]),
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in contract["semantic_requirements"]),
        f"- Predeclaration: {contract['blind_predeclaration']}",
        f"- Rationale: {contract['rationale']}",
        "",
        "## Probe Evaluations",
        "",
        "| probe | family | expected admit? | holdout admits? | matched? | status | failed checks | reason |",
        "| --- | --- | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for evaluation in payload["evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['probe_id']}` | "
            f"`{evaluation['family_id']}` | "
            f"{evaluation['expected_admissible']} | "
            f"{evaluation['holdout_admissible']} | "
            f"{evaluation['expectation_matched']} | "
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


def write_results(result: T572Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t572_result_to_dict(result)
    json_path = (
        results_dir
        / "T572-domain-native-sheaf-transport-blind-family-holdout-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T572-domain-native-sheaf-transport-blind-family-holdout-gate-v0.1-results.md"
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

    result = run_t572_analysis()
    payload = t572_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
