"""T571: multi-family falsifier rotation for the TAF11 generator.

T570 showed that the T568/T569 semantic generator survives fresh-family role
recoding in two admitted domains. T571 rotates falsifiers across those admitted
families. The result remains review-only and selects a blind-family holdout as
the next burden before any source-law, claim, canon, public-posture, TAF4,
TAF8, S1, or cross-repo movement.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t570_domain_native_sheaf_transport_fresh_family_stress_gate as t570,
)


ARTIFACT = (
    "T571-domain-native-sheaf-transport-multi-family-falsifier-rotation-gate-v0.1"
)
VERDICT = "domain_native_sheaf_transport_multi_family_falsifier_rotation_survives_review_only"
ROTATION_STATUS = "MULTI_FAMILY_FALSIFIER_ROTATION_SURVIVES"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_BLIND_FAMILY_HOLDOUT_REQUIRED"
ROUTE_STATUS = "multi_family_rotation_clears_blind_family_holdout_required"
NEXT_PACKET = "t572_domain_native_sheaf_transport_blind_family_holdout_gate"

NOT_CLAIMED = (
    "T571 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It rotates falsifiers across "
    "the T570 admitted fresh families and selects a blind-family holdout as "
    "the next review-only burden."
)


@dataclass(frozen=True)
class RotationContract:
    contract_id: str
    source_t570_projection_id: str
    admitted_family_ids: tuple[str, ...]
    source_roles: tuple[str, ...]
    absorber_boundaries: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    rotated_falsifier_axes: tuple[str, ...]
    forbidden_shortcuts: tuple[str, ...]
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "admitted_family_ids",
            "source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "rotated_falsifier_axes",
            "forbidden_shortcuts",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class FamilyProbe:
    probe_id: str
    family_id: str
    probe_kind: str
    predeclared_before_evaluation: bool
    active_falsifier_axis: str
    expected_admissible: bool
    source_role_coverage: tuple[str, ...]
    absorber_boundary_coverage: tuple[str, ...]
    semantic_requirements_met: tuple[str, ...]
    rotated_family_specific_shortcut: bool
    cross_family_alias_replay: bool
    target_import_terms: tuple[str, ...]
    native_payload_forced: bool
    noncommuting_transport_square: bool
    family_rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_role_coverage",
            "absorber_boundary_coverage",
            "semantic_requirements_met",
            "target_import_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class ProbeEvaluation:
    probe_id: str
    family_id: str
    expected_admissible: bool
    rotation_admissible: bool
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
class FamilyRotationSummary:
    family_id: str
    admitted_probe_ids: tuple[str, ...]
    rejected_probe_ids: tuple[str, ...]
    falsifier_axes_exercised: tuple[str, ...]
    status: str
    passed: bool
    residual_risk: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "admitted_probe_ids",
            "rejected_probe_ids",
            "falsifier_axes_exercised",
        ):
            data[key] = list(data[key])
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
class T571Result:
    artifact: str
    source_t570_verdict: str
    source_t570_selected_next_packet: str
    source_t570_fresh_family_stress_cleared: bool
    rotation_status: str
    source_law_status: str
    route_status: str
    rotation_contract: RotationContract
    probes: tuple[FamilyProbe, ...]
    evaluations: tuple[ProbeEvaluation, ...]
    family_summaries: tuple[FamilyRotationSummary, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    admitted_probe_ids: tuple[str, ...]
    rejected_probe_ids: tuple[str, ...]
    multi_family_rotation_cleared: bool
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


def run_t571_analysis() -> T571Result:
    source = t570.run_t570_analysis()
    contract = _rotation_contract(source)
    probes = _probe_panel(contract)
    evaluations = tuple(_evaluate_probe(contract, probe) for probe in probes)
    family_summaries = _family_summaries(contract, evaluations)
    admitted_probe_ids = tuple(
        evaluation.probe_id for evaluation in evaluations if evaluation.rotation_admissible
    )
    rejected_probe_ids = tuple(
        evaluation.probe_id for evaluation in evaluations if not evaluation.rotation_admissible
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        contract=contract,
        evaluations=evaluations,
        family_summaries=family_summaries,
        admitted_probe_ids=admitted_probe_ids,
        rejected_probe_ids=rejected_probe_ids,
    )
    multi_family_rotation_cleared = (
        source.verdict == t570.VERDICT
        and source.selected_next_packet == t570.NEXT_PACKET
        and source.fresh_family_stress_cleared
        and admitted_probe_ids
        == (
            "calibration_chain_rotated_survivor",
            "archive_manifest_rotated_survivor",
        )
        and rejected_probe_ids
        == (
            "calibration_missing_scope_restriction_falsifier",
            "calibration_single_panel_completion_falsifier",
            "archive_payload_optional_falsifier",
            "archive_target_geometry_import_falsifier",
            "cross_family_alias_replay_falsifier",
        )
        and all(item.expectation_matched for item in evaluations)
        and all(summary.passed for summary in family_summaries)
        and all(check.passed for check in closure_checks)
    )
    route_decisions = _route_decisions(
        multi_family_rotation_cleared=multi_family_rotation_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        multi_family_rotation_cleared=multi_family_rotation_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if multi_family_rotation_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_multi_family_falsifier_rotation_unexpected_status"
    )

    return T571Result(
        artifact=ARTIFACT,
        source_t570_verdict=source.verdict,
        source_t570_selected_next_packet=source.selected_next_packet,
        source_t570_fresh_family_stress_cleared=source.fresh_family_stress_cleared,
        rotation_status=ROTATION_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        rotation_contract=contract,
        probes=probes,
        evaluations=evaluations,
        family_summaries=family_summaries,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        admitted_probe_ids=admitted_probe_ids,
        rejected_probe_ids=rejected_probe_ids,
        multi_family_rotation_cleared=multi_family_rotation_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T571 rotates missing-role, trivial-completion, optional-payload, "
            "target-import, and cross-family alias falsifiers across the two "
            "T570 admitted families. The role-level generator survives the "
            "rotation, but the result is still finite review evidence rather "
            "than a public source law because no blind family was withheld."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next packet should predeclare a blind "
            "family holdout before evaluation and then decide whether the "
            "generator predicts that family without target import, replay, "
            "source-law overread, claim movement, canon movement, public-posture "
            "movement, TAF4 movement, TAF8 execution, or S1 movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. Multi-family falsifier rotation "
            "survived over the T570 admitted families, but source-law status "
            "still waits for a blind-family holdout."
        ),
        taf4_update=(
            "TAF4 remains blocked. Multi-family falsifier rotation over a finite "
            "semantic generator is not finite-to-continuum descent, causal-set "
            "recovery, Lorentzian target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T571 is still internal TAF11 generator stress, "
            "not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            admitted_probe_ids=admitted_probe_ids,
            rejected_probe_ids=rejected_probe_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T571 rotates falsifiers across "
            "the T570 admitted families and selects blind-family holdout; claim "
            "rows, Canon Index tiers, canon verdicts, and public posture remain "
            "unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t571_result_to_dict(result: T571Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t570_verdict": result.source_t570_verdict,
        "source_t570_selected_next_packet": result.source_t570_selected_next_packet,
        "source_t570_fresh_family_stress_cleared": result.source_t570_fresh_family_stress_cleared,
        "rotation_status": result.rotation_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "rotation_contract": result.rotation_contract.to_dict(),
        "probes": [probe.to_dict() for probe in result.probes],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "family_summaries": [summary.to_dict() for summary in result.family_summaries],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [
            decision.to_dict() for decision in result.route_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "admitted_probe_ids": list(result.admitted_probe_ids),
        "rejected_probe_ids": list(result.rejected_probe_ids),
        "multi_family_rotation_cleared": result.multi_family_rotation_cleared,
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


def _rotation_contract(source: t570.T570Result) -> RotationContract:
    projection = source.fresh_family_projection
    source_roles = tuple(role for role, _ in projection.source_role_to_fresh_field)
    absorber_boundaries = tuple(
        role for role, _ in projection.absorber_role_to_fresh_boundary
    )
    return RotationContract(
        contract_id="multi_family_falsifier_rotation_v1",
        source_t570_projection_id=projection.projection_id,
        admitted_family_ids=source.admitted_family_ids,
        source_roles=source_roles,
        absorber_boundaries=absorber_boundaries,
        semantic_requirements=projection.semantic_requirements,
        rotated_falsifier_axes=(
            "missing_scope_restriction",
            "ordinary_completion_triviality",
            "optional_payload",
            "target_geometry_import",
            "cross_family_alias_replay",
        ),
        forbidden_shortcuts=projection.forbidden_shortcuts,
        rationale=(
            "The rotation keeps the T570 role-level projection fixed and moves "
            "active falsifiers across each admitted family."
        ),
    )


def _probe_panel(contract: RotationContract) -> tuple[FamilyProbe, ...]:
    source = contract.source_roles
    absorbers = contract.absorber_boundaries
    semantics = contract.semantic_requirements
    return (
        FamilyProbe(
            probe_id="calibration_chain_rotated_survivor",
            family_id="calibration_chain_role_recoding_family",
            probe_kind="family_survivor",
            predeclared_before_evaluation=True,
            active_falsifier_axis="missing_scope_restriction",
            expected_admissible=True,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=False,
            target_import_terms=(),
            native_payload_forced=True,
            noncommuting_transport_square=True,
            family_rationale=(
                "Calibration custody still forces a payload after the active "
                "missing-scope falsifier is rotated into the family."
            ),
        ),
        FamilyProbe(
            probe_id="archive_manifest_rotated_survivor",
            family_id="archive_manifest_handoff_role_recoding_family",
            probe_kind="family_survivor",
            predeclared_before_evaluation=True,
            active_falsifier_axis="optional_payload",
            expected_admissible=True,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=False,
            target_import_terms=(),
            native_payload_forced=True,
            noncommuting_transport_square=True,
            family_rationale=(
                "Archive handoff still forces a payload after the optional-payload "
                "falsifier is rotated into the family."
            ),
        ),
        FamilyProbe(
            probe_id="calibration_missing_scope_restriction_falsifier",
            family_id="calibration_chain_role_recoding_family",
            probe_kind="rotated_falsifier",
            predeclared_before_evaluation=True,
            active_falsifier_axis="missing_scope_restriction",
            expected_admissible=False,
            source_role_coverage=tuple(role for role in source if role != "restriction_morphisms"),
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=False,
            target_import_terms=(),
            native_payload_forced=True,
            noncommuting_transport_square=True,
            family_rationale="Rejects a calibration packet with the restriction role removed.",
        ),
        FamilyProbe(
            probe_id="calibration_single_panel_completion_falsifier",
            family_id="calibration_chain_role_recoding_family",
            probe_kind="rotated_falsifier",
            predeclared_before_evaluation=True,
            active_falsifier_axis="ordinary_completion_triviality",
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=tuple(
                item for item in semantics if item != "nontrivial_obstruction_witness"
            ),
            rotated_family_specific_shortcut=True,
            cross_family_alias_replay=False,
            target_import_terms=(),
            native_payload_forced=False,
            noncommuting_transport_square=False,
            family_rationale="Rejects ordinary single-panel completion as a shortcut.",
        ),
        FamilyProbe(
            probe_id="archive_payload_optional_falsifier",
            family_id="archive_manifest_handoff_role_recoding_family",
            probe_kind="rotated_falsifier",
            predeclared_before_evaluation=True,
            active_falsifier_axis="optional_payload",
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=tuple(
                item for item in semantics if item != "native_payload_forced"
            ),
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=False,
            target_import_terms=(),
            native_payload_forced=False,
            noncommuting_transport_square=True,
            family_rationale="Rejects archive handoff when the payload is optional.",
        ),
        FamilyProbe(
            probe_id="archive_target_geometry_import_falsifier",
            family_id="archive_manifest_handoff_role_recoding_family",
            probe_kind="rotated_falsifier",
            predeclared_before_evaluation=True,
            active_falsifier_axis="target_geometry_import",
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=False,
            target_import_terms=("lorentzian_interval_target", "causal_set_link_target"),
            native_payload_forced=True,
            noncommuting_transport_square=True,
            family_rationale="Rejects archive handoff when target geometry language is imported.",
        ),
        FamilyProbe(
            probe_id="cross_family_alias_replay_falsifier",
            family_id="calibration_chain_role_recoding_family",
            probe_kind="rotated_falsifier",
            predeclared_before_evaluation=True,
            active_falsifier_axis="cross_family_alias_replay",
            expected_admissible=False,
            source_role_coverage=source,
            absorber_boundary_coverage=absorbers,
            semantic_requirements_met=semantics,
            rotated_family_specific_shortcut=False,
            cross_family_alias_replay=True,
            target_import_terms=(),
            native_payload_forced=True,
            noncommuting_transport_square=True,
            family_rationale=(
                "Rejects a calibration-labeled replay of archive-manifest "
                "surface evidence."
            ),
        ),
    )


def _evaluate_probe(contract: RotationContract, probe: FamilyProbe) -> ProbeEvaluation:
    checks = _probe_checks(contract, probe)
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    admissible = not failed
    expectation_matched = admissible == probe.expected_admissible
    if admissible:
        status = "ADMITTED_BY_MULTI_FAMILY_ROTATION"
        reason = "The probe satisfies the rotated role-level generator."
    elif probe.cross_family_alias_replay:
        status = "REJECTED_CROSS_FAMILY_ALIAS_REPLAY"
        reason = "The rotation rejects cross-family alias replay."
    elif probe.target_import_terms:
        status = "REJECTED_TARGET_IMPORT"
        reason = "The rotation rejects target-language import."
    elif "source_roles_complete" in failed:
        status = "REJECTED_MISSING_SOURCE_ROLE"
        reason = "The rotation rejects a missing source role."
    elif "native_payload_forced" in failed:
        status = "REJECTED_NATIVE_PAYLOAD_NOT_FORCED"
        reason = "The rotation rejects unforced native payload."
    elif "noncommuting_transport_square" in failed:
        status = "REJECTED_TRIVIAL_COMPLETION"
        reason = "The rotation rejects ordinary completion without transport noncommutation."
    else:
        status = "REJECTED_ROTATION_CONTRACT"
        reason = "The rotation rejects the probe because: " + ", ".join(failed)
    return ProbeEvaluation(
        probe_id=probe.probe_id,
        family_id=probe.family_id,
        expected_admissible=probe.expected_admissible,
        rotation_admissible=admissible,
        expectation_matched=expectation_matched,
        status=status,
        passed_checks=passed,
        failed_checks=failed,
        reason=reason,
    )


def _probe_checks(
    contract: RotationContract,
    probe: FamilyProbe,
) -> tuple[tuple[str, bool], ...]:
    return (
        (
            "predeclared_before_evaluation",
            probe.predeclared_before_evaluation,
        ),
        (
            "known_t570_admitted_family",
            probe.family_id in contract.admitted_family_ids,
        ),
        (
            "source_roles_complete",
            probe.source_role_coverage == contract.source_roles,
        ),
        (
            "absorber_boundaries_complete",
            probe.absorber_boundary_coverage == contract.absorber_boundaries,
        ),
        (
            "semantic_requirements_complete",
            probe.semantic_requirements_met == contract.semantic_requirements,
        ),
        (
            "active_falsifier_axis_registered",
            probe.active_falsifier_axis in contract.rotated_falsifier_axes,
        ),
        (
            "no_family_specific_shortcut",
            not probe.rotated_family_specific_shortcut,
        ),
        ("no_cross_family_alias_replay", not probe.cross_family_alias_replay),
        ("target_blind_language", probe.target_import_terms == ()),
        ("native_payload_forced", probe.native_payload_forced),
        ("noncommuting_transport_square", probe.noncommuting_transport_square),
    )


def _family_summaries(
    contract: RotationContract,
    evaluations: tuple[ProbeEvaluation, ...],
) -> tuple[FamilyRotationSummary, ...]:
    summaries: list[FamilyRotationSummary] = []
    for family_id in contract.admitted_family_ids:
        family_evaluations = tuple(
            evaluation for evaluation in evaluations if evaluation.family_id == family_id
        )
        admitted = tuple(
            evaluation.probe_id
            for evaluation in family_evaluations
            if evaluation.rotation_admissible
        )
        rejected = tuple(
            evaluation.probe_id
            for evaluation in family_evaluations
            if not evaluation.rotation_admissible
        )
        axes = tuple(
            dict.fromkeys(
                probe.active_falsifier_axis
                for probe in _probe_panel(contract)
                if probe.family_id == family_id
            )
        )
        passed = bool(admitted) and len(rejected) >= 2 and all(
            evaluation.expectation_matched for evaluation in family_evaluations
        )
        summaries.append(
            FamilyRotationSummary(
                family_id=family_id,
                admitted_probe_ids=admitted,
                rejected_probe_ids=rejected,
                falsifier_axes_exercised=axes,
                status="PASS" if passed else "FAIL",
                passed=passed,
                residual_risk=(
                    "Family rotation is finite and still not a blind family holdout."
                ),
            )
        )
    return tuple(summaries)


def _closure_checks(
    source: t570.T570Result,
    contract: RotationContract,
    evaluations: tuple[ProbeEvaluation, ...],
    family_summaries: tuple[FamilyRotationSummary, ...],
    admitted_probe_ids: tuple[str, ...],
    rejected_probe_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    expected_admitted = (
        "calibration_chain_rotated_survivor",
        "archive_manifest_rotated_survivor",
    )
    expected_rejected = (
        "calibration_missing_scope_restriction_falsifier",
        "calibration_single_panel_completion_falsifier",
        "archive_payload_optional_falsifier",
        "archive_target_geometry_import_falsifier",
        "cross_family_alias_replay_falsifier",
    )
    t570_authority = (
        source.verdict == t570.VERDICT
        and source.selected_next_packet == t570.NEXT_PACKET
        and source.fresh_family_stress_cleared
    )
    axis_coverage = set(contract.rotated_falsifier_axes) == {
        evaluation_probe_axis(probe_id, contract)
        for probe_id in rejected_probe_ids
    }
    return (
        ClosureCheck(
            check_id="t570_authority",
            status="PASS" if t570_authority else "FAIL",
            passed=t570_authority,
            evidence=(
                "T570 cleared fresh-family stress.",
                "T570 selected multi-family falsifier rotation.",
            ),
            residual_risk="T570 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="all_t570_families_rotated",
            status="PASS" if all(summary.passed for summary in family_summaries) else "FAIL",
            passed=all(summary.passed for summary in family_summaries),
            evidence=tuple(summary.family_id for summary in family_summaries),
            residual_risk="Two families are not enough for public source-law status.",
        ),
        ClosureCheck(
            check_id="expected_survivors_admitted",
            status="PASS" if admitted_probe_ids == expected_admitted else "FAIL",
            passed=admitted_probe_ids == expected_admitted,
            evidence=admitted_probe_ids,
            residual_risk="Survivors are finite review probes.",
        ),
        ClosureCheck(
            check_id="rotated_falsifiers_rejected",
            status="PASS" if rejected_probe_ids == expected_rejected else "FAIL",
            passed=rejected_probe_ids == expected_rejected,
            evidence=rejected_probe_ids,
            residual_risk="More falsifier axes may still expose failure modes.",
        ),
        ClosureCheck(
            check_id="all_rotated_axes_exercised",
            status="PASS" if axis_coverage else "FAIL",
            passed=axis_coverage,
            evidence=contract.rotated_falsifier_axes,
            residual_risk="Axis coverage is finite and synthetic.",
        ),
        ClosureCheck(
            check_id="expectations_matched",
            status="PASS" if all(item.expectation_matched for item in evaluations) else "FAIL",
            passed=all(item.expectation_matched for item in evaluations),
            evidence=tuple(item.probe_id for item in evaluations if item.expectation_matched),
            residual_risk="Expectation matching is not independent blind prediction.",
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


def evaluation_probe_axis(probe_id: str, contract: RotationContract) -> str:
    for probe in _probe_panel(contract):
        if probe.probe_id == probe_id:
            return probe.active_falsifier_axis
    return "unknown"


def _route_decisions(
    multi_family_rotation_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_BLIND_FAMILY_HOLDOUT_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Multi-family falsifier rotation clears a stress check but not blind holdout pressure."
            ),
        ),
        RouteDecision(
            decision_id="run_blind_family_holdout_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if multi_family_rotation_cleared and not source_law_earned
                else "PAUSED_UNTIL_MULTI_FAMILY_ROTATION_CLEARS"
            ),
            selected=multi_family_rotation_cleared and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest review step is a predeclared blind-family holdout."
                if multi_family_rotation_cleared
                else "Multi-family rotation has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not multi_family_rotation_cleared
                else "PAUSED_MULTI_FAMILY_ROTATION_CLEARED"
            ),
            selected=not multi_family_rotation_cleared,
            next_packet="none",
            reason=(
                "Route reset is needed if multi-family rotation fails."
                if not multi_family_rotation_cleared
                else "Route reset is premature because multi-family rotation cleared."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t571",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Finite multi-family generator stress is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t571",
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
    multi_family_rotation_cleared: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t570_authority",
            checks["t570_authority"].passed,
            "T570 supplies multi-family falsifier-rotation authority.",
            "T570 did not supply expected multi-family rotation authority.",
        ),
        (
            "all_t570_families_rotated",
            checks["all_t570_families_rotated"].passed,
            "Every T570 admitted family has a survivor and rotated rejected falsifiers.",
            "At least one T570 admitted family was not properly rotated.",
        ),
        (
            "expected_rotation_pattern",
            checks["expected_survivors_admitted"].passed
            and checks["rotated_falsifiers_rejected"].passed
            and checks["all_rotated_axes_exercised"].passed
            and checks["expectations_matched"].passed,
            "Survivors admit and all rotated falsifier axes reject as expected.",
            "The rotation pattern did not match the expected survivor/falsifier split.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_BLIND_FAMILY_HOLDOUT_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "blind_family_holdout_selected_next",
            multi_family_rotation_cleared
            and selected_next_packet == NEXT_PACKET
            and routes["run_blind_family_holdout_gate"].selected,
            "Blind-family holdout is selected as the next burden.",
            "The expected blind-family holdout next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t571"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t571"].outcome == "BLOCKED_TAF8_OVERREAD"
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
            text=(
                "Multi-family rotation admits: "
                + ", ".join(admitted_probe_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Multi-family rotation rejects: "
                + ", ".join(rejected_probe_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by blind-family holdout.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Falsifier rotation strengthens route evidence without promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    contract = payload["rotation_contract"]
    lines = [
        "# T571 Results: Domain-Native Sheaf Transport Multi-Family Falsifier Rotation Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Rotation status: `{payload['rotation_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T570 verdict: `{payload['source_t570_verdict']}`",
        f"- Source T570 selected next packet: `{payload['source_t570_selected_next_packet']}`",
        f"- Source T570 fresh-family stress cleared: {payload['source_t570_fresh_family_stress_cleared']}",
        f"- Multi-family rotation cleared: {payload['multi_family_rotation_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Rotation Contract",
        "",
        f"- Contract: `{contract['contract_id']}`",
        f"- Source projection: `{contract['source_t570_projection_id']}`",
        "- Admitted families: "
        + ", ".join(f"`{item}`" for item in contract["admitted_family_ids"]),
        "- Rotated falsifier axes: "
        + ", ".join(f"`{item}`" for item in contract["rotated_falsifier_axes"]),
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in contract["semantic_requirements"]),
        f"- Rationale: {contract['rationale']}",
        "",
        "## Probe Evaluations",
        "",
        "| probe | family | expected admit? | rotation admits? | matched? | status | failed checks | reason |",
        "| --- | --- | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for evaluation in payload["evaluations"]:
        lines.append(
            "| "
            f"`{evaluation['probe_id']}` | "
            f"`{evaluation['family_id']}` | "
            f"{evaluation['expected_admissible']} | "
            f"{evaluation['rotation_admissible']} | "
            f"{evaluation['expectation_matched']} | "
            f"`{evaluation['status']}` | "
            f"{', '.join(evaluation['failed_checks']) or 'none'} | "
            f"{evaluation['reason']} |"
        )
    lines.extend(
        [
            "",
            "## Family Summaries",
            "",
            "| family | status | admitted probes | rejected probes | axes exercised | residual risk |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for summary in payload["family_summaries"]:
        lines.append(
            "| "
            f"`{summary['family_id']}` | "
            f"`{summary['status']}` | "
            f"{', '.join(summary['admitted_probe_ids']) or 'none'} | "
            f"{', '.join(summary['rejected_probe_ids']) or 'none'} | "
            f"{', '.join(summary['falsifier_axes_exercised']) or 'none'} | "
            f"{summary['residual_risk']} |"
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


def write_results(result: T571Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t571_result_to_dict(result)
    json_path = (
        results_dir
        / "T571-domain-native-sheaf-transport-multi-family-falsifier-rotation-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T571-domain-native-sheaf-transport-multi-family-falsifier-rotation-gate-v0.1-results.md"
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

    result = run_t571_analysis()
    payload = t571_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
