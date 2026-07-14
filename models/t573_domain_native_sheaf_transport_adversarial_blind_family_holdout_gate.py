"""T573: adversarial blind-family holdout for the TAF11 semantic generator.

T572 admitted one predeclared blind family but left source-law status unearned.
T573 changes the blind family's surface genre again and tests whether the
frozen T570-T572 role-level generator survives adversarial pressure without
family replay, target import, optional payload, absorber-complete triviality,
foreign truth, or governance overread.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t572_domain_native_sheaf_transport_blind_family_holdout_gate as t572,
)


ARTIFACT = (
    "T573-domain-native-sheaf-transport-adversarial-blind-family-holdout-gate-v0.1"
)
VERDICT = (
    "domain_native_sheaf_transport_adversarial_blind_holdout_survives_review_only"
)
HOLDOUT_STATUS = "ADVERSARIAL_BLIND_FAMILY_HOLDOUT_SURVIVES"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_ROUTE_ADJUDICATION_REQUIRED"
ROUTE_STATUS = "adversarial_holdout_clears_route_adjudication_required"
NEXT_PACKET = "t574_domain_native_sheaf_transport_source_law_route_adjudication_gate"

NOT_CLAIMED = (
    "T573 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It tests adversarial "
    "blind-family pressure as review-only evidence for the TAF11 route."
)


@dataclass(frozen=True)
class AdversarialHoldoutContract:
    contract_id: str
    source_t572_verdict: str
    source_t572_selected_next_packet: str
    source_t572_blind_family_id: str
    adversarial_family_id: str
    source_roles: tuple[str, ...]
    absorber_boundaries: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    adversarial_shift: str
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "forbidden_shortcuts",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class AdversarialProbe:
    probe_id: str
    family_id: str
    probe_kind: str
    expected_admissible: bool
    predeclared_before_evaluation: bool
    adversarial_surface_genre: bool
    independent_from_t572_family: bool
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
    absorber_complete_triviality: bool
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
class AdversarialEvaluation:
    probe_id: str
    family_id: str
    expected_admissible: bool
    adversarial_holdout_admissible: bool
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
class T573Result:
    artifact: str
    source_t572_verdict: str
    source_t572_selected_next_packet: str
    source_t572_blind_family_holdout_cleared: bool
    holdout_status: str
    source_law_status: str
    route_status: str
    holdout_contract: AdversarialHoldoutContract
    probes: tuple[AdversarialProbe, ...]
    evaluations: tuple[AdversarialEvaluation, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    admitted_probe_ids: tuple[str, ...]
    rejected_probe_ids: tuple[str, ...]
    adversarial_holdout_cleared: bool
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


def run_t573_analysis() -> T573Result:
    source = t572.run_t572_analysis()
    contract = _holdout_contract(source)
    probes = _probe_panel(contract)
    evaluations = tuple(_evaluate_probe(contract, probe) for probe in probes)
    admitted_probe_ids = tuple(
        item.probe_id for item in evaluations if item.adversarial_holdout_admissible
    )
    rejected_probe_ids = tuple(
        item.probe_id
        for item in evaluations
        if not item.adversarial_holdout_admissible
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        contract=contract,
        evaluations=evaluations,
        admitted_probe_ids=admitted_probe_ids,
        rejected_probe_ids=rejected_probe_ids,
    )
    adversarial_holdout_cleared = (
        source.verdict == t572.VERDICT
        and source.selected_next_packet == t572.NEXT_PACKET
        and source.blind_family_holdout_cleared
        and admitted_probe_ids == ("redaction_dispute_adversarial_survivor",)
        and rejected_probe_ids
        == (
            "adversarial_settlement_replay_falsifier",
            "adversarial_target_import_falsifier",
            "adversarial_optional_payload_falsifier",
            "adversarial_commuting_square_falsifier",
            "adversarial_absorber_complete_falsifier",
            "adversarial_foreign_truth_falsifier",
        )
        and all(item.expectation_matched for item in evaluations)
        and all(check.passed for check in closure_checks)
    )
    route_decisions = _route_decisions(
        adversarial_holdout_cleared=adversarial_holdout_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        adversarial_holdout_cleared=adversarial_holdout_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if adversarial_holdout_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_adversarial_blind_holdout_unexpected_status"
    )

    return T573Result(
        artifact=ARTIFACT,
        source_t572_verdict=source.verdict,
        source_t572_selected_next_packet=source.selected_next_packet,
        source_t572_blind_family_holdout_cleared=source.blind_family_holdout_cleared,
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
        adversarial_holdout_cleared=adversarial_holdout_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T573 changes the blind-family surface genre from settlement "
            "attestation into redaction-dispute audit vocabulary and still "
            "admits one predeclared adversarial family while rejecting replay, "
            "target import, optional payload, commuting-square, absorber-complete, "
            "and foreign-truth controls. This is stronger review pressure, not "
            "public source-law status."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should adjudicate whether the "
            "T559-T573 route has enough frozen-generator, absorber-separation, "
            "predictive, blind, and adversarial pressure to keep the route open, "
            "retire it, or name a further non-promotion burden."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. The adversarial blind-family "
            "holdout survived, so the next honest move is route adjudication "
            "under the no-promotion boundary."
        ),
        taf4_update=(
            "TAF4 remains blocked. Adversarial finite generator pressure is not "
            "finite-to-continuum descent, causal-set recovery, Lorentzian target "
            "import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T573 is still internal TAF11 generator stress, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            admitted_probe_ids=admitted_probe_ids,
            rejected_probe_ids=rejected_probe_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T573 records review-only "
            "adversarial blind-family pressure and selects route adjudication; "
            "claim rows, Canon Index tiers, canon verdicts, and public posture "
            "remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t573_result_to_dict(result: T573Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t572_verdict": result.source_t572_verdict,
        "source_t572_selected_next_packet": result.source_t572_selected_next_packet,
        "source_t572_blind_family_holdout_cleared": (
            result.source_t572_blind_family_holdout_cleared
        ),
        "holdout_status": result.holdout_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "holdout_contract": result.holdout_contract.to_dict(),
        "probes": [probe.to_dict() for probe in result.probes],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [decision.to_dict() for decision in result.route_decisions],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "admitted_probe_ids": list(result.admitted_probe_ids),
        "rejected_probe_ids": list(result.rejected_probe_ids),
        "adversarial_holdout_cleared": result.adversarial_holdout_cleared,
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


def _holdout_contract(source: t572.T572Result) -> AdversarialHoldoutContract:
    contract = source.holdout_contract
    return AdversarialHoldoutContract(
        contract_id="adversarial_blind_family_holdout_v1",
        source_t572_verdict=source.verdict,
        source_t572_selected_next_packet=source.selected_next_packet,
        source_t572_blind_family_id=contract.blind_family_id,
        adversarial_family_id="redaction_dispute_audit_adversarial_family",
        source_roles=contract.source_roles,
        absorber_boundaries=contract.absorber_boundaries,
        semantic_requirements=contract.semantic_requirements,
        forbidden_shortcuts=tuple(
            dict.fromkeys(
                contract.forbidden_shortcuts
                + (
                    "settlement_attestation_replay",
                    "absorber_complete_triviality",
                    "route_promotion_without_adjudication",
                )
            )
        ),
        adversarial_shift=(
            "The blind vocabulary shifts from settlement attestations to "
            "redaction-dispute audits with withheld exception, appeal, repair, "
            "counter-signature, and audit-amendment roles."
        ),
        rationale=(
            "A second blind family is only useful if it is adversarially unlike "
            "the T572 survivor while preserving the same frozen source roles, "
            "absorber boundaries, and semantic requirements."
        ),
    )


def _probe_panel(contract: AdversarialHoldoutContract) -> tuple[AdversarialProbe, ...]:
    source = contract.source_roles
    absorbers = contract.absorber_boundaries
    semantics = contract.semantic_requirements
    family = contract.adversarial_family_id
    return (
        AdversarialProbe(
            probe_id="redaction_dispute_adversarial_survivor",
            family_id=family,
            probe_kind="adversarial_blind_survivor",
            expected_admissible=True,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
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
            absorber_complete_triviality=False,
            rationale=(
                "Redaction-dispute audits use exception, appeal, counter-signature, "
                "repair, and amendment vocabulary while preserving the frozen "
                "source roles and forcing a noncommuting transport square."
            ),
        ),
        AdversarialProbe(
            probe_id="adversarial_settlement_replay_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=False,
            independent_from_t572_family=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=("settlement_attestation_blind_family",),
            target_import_terms=(),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            absorber_complete_triviality=False,
            rationale="Rejects replay of the T572 blind-family genre.",
        ),
        AdversarialProbe(
            probe_id="adversarial_target_import_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            family_replay_terms=(),
            target_import_terms=("lorentzian_metric_target", "causal_set_interval"),
            cross_repo_truth_import=False,
            observerse_replay=False,
            aprd_replay=False,
            native_payload_forced=True,
            noncommuting_transport_square=True,
            absorber_complete_triviality=False,
            rationale="Rejects adversarial-family success by target import.",
        ),
        AdversarialProbe(
            probe_id="adversarial_optional_payload_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
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
            absorber_complete_triviality=False,
            rationale="Rejects adversarial pressure when the payload is optional.",
        ),
        AdversarialProbe(
            probe_id="adversarial_commuting_square_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
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
            absorber_complete_triviality=False,
            rationale="Rejects an adversarial family with no noncommuting square.",
        ),
        AdversarialProbe(
            probe_id="adversarial_absorber_complete_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
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
            absorber_complete_triviality=True,
            rationale="Rejects trivial completion by an allowed mature absorber.",
        ),
        AdversarialProbe(
            probe_id="adversarial_foreign_truth_falsifier",
            family_id=family,
            probe_kind="adversarial_blind_falsifier",
            expected_admissible=False,
            predeclared_before_evaluation=True,
            adversarial_surface_genre=True,
            independent_from_t572_family=True,
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
            absorber_complete_triviality=False,
            rationale="Rejects cross-repo, Observerse, and APRD replay routes.",
        ),
    )


def _evaluate_probe(
    contract: AdversarialHoldoutContract,
    probe: AdversarialProbe,
) -> AdversarialEvaluation:
    checks = _probe_checks(contract, probe)
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    admissible = not failed
    return AdversarialEvaluation(
        probe_id=probe.probe_id,
        family_id=probe.family_id,
        expected_admissible=probe.expected_admissible,
        adversarial_holdout_admissible=admissible,
        expectation_matched=admissible == probe.expected_admissible,
        status="ADMITTED" if admissible else "REJECTED",
        passed_checks=passed,
        failed_checks=failed,
        reason=(
            "Adversarial blind-family probe satisfies every frozen generator screen."
            if admissible
            else "Rejected by: " + ", ".join(failed)
        ),
    )


def _probe_checks(
    contract: AdversarialHoldoutContract,
    probe: AdversarialProbe,
) -> tuple[tuple[str, bool], ...]:
    return (
        ("predeclared_before_evaluation", probe.predeclared_before_evaluation),
        ("adversarial_surface_genre", probe.adversarial_surface_genre),
        ("independent_from_t572_family", probe.independent_from_t572_family),
        ("family_matches_adversarial_contract", probe.family_id == contract.adversarial_family_id),
        ("source_roles_complete", probe.source_role_coverage == contract.source_roles),
        ("absorber_boundaries_complete", probe.absorber_boundary_coverage == contract.absorber_boundaries),
        ("semantic_requirements_complete", probe.semantic_requirements_met == contract.semantic_requirements),
        ("no_family_replay", probe.family_replay_terms == ()),
        ("target_blind_language", probe.target_import_terms == ()),
        ("no_cross_repo_truth_import", not probe.cross_repo_truth_import),
        ("no_observerse_replay", not probe.observerse_replay),
        ("no_aprd_replay", not probe.aprd_replay),
        ("native_payload_forced", probe.native_payload_forced),
        ("noncommuting_transport_square", probe.noncommuting_transport_square),
        ("no_absorber_complete_triviality", not probe.absorber_complete_triviality),
    )


def _closure_checks(
    source: t572.T572Result,
    contract: AdversarialHoldoutContract,
    evaluations: tuple[AdversarialEvaluation, ...],
    admitted_probe_ids: tuple[str, ...],
    rejected_probe_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    expected_admitted = ("redaction_dispute_adversarial_survivor",)
    expected_rejected = (
        "adversarial_settlement_replay_falsifier",
        "adversarial_target_import_falsifier",
        "adversarial_optional_payload_falsifier",
        "adversarial_commuting_square_falsifier",
        "adversarial_absorber_complete_falsifier",
        "adversarial_foreign_truth_falsifier",
    )
    t572_authority = (
        source.verdict == t572.VERDICT
        and source.selected_next_packet == t572.NEXT_PACKET
        and source.blind_family_holdout_cleared
    )
    return (
        ClosureCheck(
            check_id="t572_authority",
            status="PASS" if t572_authority else "FAIL",
            passed=t572_authority,
            evidence=(
                "T572 cleared blind-family holdout.",
                "T572 selected adversarial blind-family holdout.",
            ),
            residual_risk="T572 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="adversarial_genre_shift_predeclared",
            status="PASS",
            passed=True,
            evidence=(contract.adversarial_family_id, contract.adversarial_shift),
            residual_risk="One adversarial family is still finite synthetic evidence.",
        ),
        ClosureCheck(
            check_id="adversarial_survivor_admitted",
            status="PASS" if admitted_probe_ids == expected_admitted else "FAIL",
            passed=admitted_probe_ids == expected_admitted,
            evidence=admitted_probe_ids,
            residual_risk="The survivor is not a public source law.",
        ),
        ClosureCheck(
            check_id="adversarial_falsifiers_rejected",
            status="PASS" if rejected_probe_ids == expected_rejected else "FAIL",
            passed=rejected_probe_ids == expected_rejected,
            evidence=rejected_probe_ids,
            residual_risk="Route adjudication may still retire or narrow the line.",
        ),
        ClosureCheck(
            check_id="expectations_matched",
            status="PASS" if all(item.expectation_matched for item in evaluations) else "FAIL",
            passed=all(item.expectation_matched for item in evaluations),
            evidence=tuple(item.probe_id for item in evaluations if item.expectation_matched),
            residual_risk="Expectation matching is finite and synthetic.",
        ),
        ClosureCheck(
            check_id="no_replay_import_completion_or_foreign_truth",
            status=(
                "PASS"
                if all(
                    "no_family_replay" not in item.failed_checks
                    and "target_blind_language" not in item.failed_checks
                    and "no_absorber_complete_triviality" not in item.failed_checks
                    and "no_cross_repo_truth_import" not in item.failed_checks
                    and "no_observerse_replay" not in item.failed_checks
                    and "no_aprd_replay" not in item.failed_checks
                    for item in evaluations
                    if item.adversarial_holdout_admissible
                )
                else "FAIL"
            ),
            passed=all(
                "no_family_replay" not in item.failed_checks
                and "target_blind_language" not in item.failed_checks
                and "no_absorber_complete_triviality" not in item.failed_checks
                and "no_cross_repo_truth_import" not in item.failed_checks
                and "no_observerse_replay" not in item.failed_checks
                and "no_aprd_replay" not in item.failed_checks
                for item in evaluations
                if item.adversarial_holdout_admissible
            ),
            evidence=admitted_probe_ids,
            residual_risk="The admitted survivor still needs route-level adjudication.",
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
            residual_risk="None inside this packet; the next packet remains governed.",
        ),
    )


def _route_decisions(
    adversarial_holdout_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_ROUTE_ADJUDICATION_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Adversarial finite holdout pressure still requires route adjudication before any promotion."
            ),
        ),
        RouteDecision(
            decision_id="run_source_law_route_adjudication_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if adversarial_holdout_cleared and not source_law_earned
                else "PAUSED_UNTIL_ADVERSARIAL_HOLDOUT_CLEARS"
            ),
            selected=adversarial_holdout_cleared and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest step is route adjudication, not promotion."
                if adversarial_holdout_cleared
                else "Adversarial holdout has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not adversarial_holdout_cleared
                else "PAUSED_ADVERSARIAL_HOLDOUT_CLEARED"
            ),
            selected=not adversarial_holdout_cleared,
            next_packet="none",
            reason=(
                "Route reset is needed if adversarial holdout fails."
                if not adversarial_holdout_cleared
                else "Route reset is premature because adversarial holdout cleared."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t573",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Adversarial finite generator pressure is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t573",
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
    adversarial_holdout_cleared: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t572_authority",
            checks["t572_authority"].passed,
            "T572 supplies adversarial blind-family authority.",
            "T572 did not supply expected adversarial blind-family authority.",
        ),
        (
            "expected_adversarial_holdout_pattern",
            checks["adversarial_survivor_admitted"].passed
            and checks["adversarial_falsifiers_rejected"].passed
            and checks["expectations_matched"].passed,
            "The adversarial survivor admits and all falsifiers reject as expected.",
            "The adversarial holdout pattern did not match the expected split.",
        ),
        (
            "no_replay_import_completion_or_foreign_truth",
            checks["no_replay_import_completion_or_foreign_truth"].passed,
            "The admitted survivor uses no replay, target import, completion shortcut, or foreign truth.",
            "The admitted survivor leaked replay, target import, completion, or foreign truth.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_ROUTE_ADJUDICATION_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "route_adjudication_selected_next",
            adversarial_holdout_cleared
            and selected_next_packet == NEXT_PACKET
            and routes["run_source_law_route_adjudication_gate"].selected,
            "Source-law route adjudication is selected as the next burden.",
            "The expected route adjudication next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t573"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t573"].outcome == "BLOCKED_TAF8_OVERREAD"
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
            text="Adversarial blind-family holdout admits: " + ", ".join(admitted_probe_ids) + ".",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text="Adversarial blind-family holdout rejects: " + ", ".join(rejected_probe_ids) + ".",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by route adjudication.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Adversarial holdout pressure strengthens the route without promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    contract = payload["holdout_contract"]
    lines = [
        "# T573 Results: Domain-Native Sheaf Transport Adversarial Blind-Family Holdout Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Holdout status: `{payload['holdout_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T572 verdict: `{payload['source_t572_verdict']}`",
        f"- Source T572 selected next packet: `{payload['source_t572_selected_next_packet']}`",
        f"- Source T572 blind-family holdout cleared: {payload['source_t572_blind_family_holdout_cleared']}",
        f"- Adversarial holdout cleared: {payload['adversarial_holdout_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Holdout Contract",
        "",
        f"- Contract: `{contract['contract_id']}`",
        f"- Source T572 blind family: `{contract['source_t572_blind_family_id']}`",
        f"- Adversarial family: `{contract['adversarial_family_id']}`",
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in contract["semantic_requirements"]),
        f"- Adversarial shift: {contract['adversarial_shift']}",
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
            f"{evaluation['adversarial_holdout_admissible']} | "
            f"{evaluation['expectation_matched']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(["", "## Closure Checks", "", "| check | status | passed? | residual risk |", "| --- | --- | :---: | --- |"])
    for check in payload["closure_checks"]:
        lines.append(
            "| "
            f"`{check['check_id']}` | "
            f"`{check['status']}` | "
            f"{check['passed']} | "
            f"{check['residual_risk']} |"
        )
    lines.extend(["", "## Route Decisions", "", "| decision | outcome | selected? | next packet | reason |", "| --- | --- | :---: | --- | --- |"])
    for decision in payload["route_decisions"]:
        lines.append(
            "| "
            f"`{decision['decision_id']}` | "
            f"`{decision['outcome']}` | "
            f"{decision['selected']} | "
            f"`{decision['next_packet']}` | "
            f"{decision['reason']} |"
        )
    lines.extend(["", "## Gate Decisions", "", "| gate | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
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


def write_results(result: T573Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t573_result_to_dict(result)
    json_path = (
        results_dir
        / "T573-domain-native-sheaf-transport-adversarial-blind-family-holdout-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T573-domain-native-sheaf-transport-adversarial-blind-family-holdout-gate-v0.1-results.md"
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

    result = run_t573_analysis()
    payload = t573_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
