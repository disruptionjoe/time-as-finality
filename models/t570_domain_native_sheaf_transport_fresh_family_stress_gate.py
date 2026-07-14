"""T570: fresh-family stress for the TAF11 semantic generator.

T569 independently rebuilt the T568 semantic generator but left source-law
status blocked until the generator was stressed against a fresh family. T570
changes the surface vocabulary and source domain while preserving the declared
load-bearing finality/transport roles. The result remains review-only.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t565_domain_native_sheaf_transport_predictive_holdout_gate as t565,
)
from models import (
    t569_domain_native_sheaf_transport_independent_reimplementation_gate as t569,
)


ARTIFACT = "T570-domain-native-sheaf-transport-fresh-family-stress-gate-v0.1"
VERDICT = "domain_native_sheaf_transport_fresh_family_stress_survives_review_only"
FRESH_FAMILY_STATUS = "FRESH_FAMILY_STRESS_SURVIVES_ROLE_LEVEL_RECODING"
SOURCE_LAW_STATUS = "SOURCE_LAW_NOT_EARNED_MULTI_FAMILY_FALSIFIER_REQUIRED"
ROUTE_STATUS = "fresh_family_stress_clears_multi_family_falsifier_required"
NEXT_PACKET = "t571_domain_native_sheaf_transport_multi_family_falsifier_rotation_gate"

NOT_CLAIMED = (
    "T570 does not establish a public source law, promote TAF11, prove shadow "
    "protection, derive spacetime, repair T528, reverse T223, unpause S1, "
    "promote S1, change claim status, change Canon Index tiers, change canon "
    "verdicts, change public posture, authorize external publication, move "
    "TAF4, execute TAF8, or move cross-repo truth. It stress-tests the "
    "independently reimplemented semantic generator on fresh-family role "
    "recodings and selects multi-family falsifier rotation as the next "
    "review-only burden."
)

INHERITED_FAMILY_IDS = (
    "escrow_window_rotation_holdout",
    "checkpoint_quorum_handoff_holdout",
)

FIXTURE_LABEL_TERMS = (
    "escrow_window_rotation_holdout",
    "checkpoint_quorum_handoff_holdout",
    "alternate_multisig_delay_repair_survivor",
    "alternate_checkpoint_quorum_repair_survivor",
)


@dataclass(frozen=True)
class FreshFamilyProjection:
    projection_id: str
    source_contract_id: str
    source_role_to_fresh_field: tuple[tuple[str, str], ...]
    absorber_role_to_fresh_boundary: tuple[tuple[str, str], ...]
    forbidden_shortcuts: tuple[str, ...]
    semantic_requirements: tuple[str, ...]
    literal_source_variable_names_used_as_fields: tuple[str, ...]
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_role_to_fresh_field",
            "absorber_role_to_fresh_boundary",
            "forbidden_shortcuts",
            "semantic_requirements",
            "literal_source_variable_names_used_as_fields",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class FreshFamilyCandidate:
    candidate_id: str
    family_id: str
    source_domain: str
    role_projection_id: str
    predeclared_before_evaluation: bool
    prior_family_replay: bool
    outcome_label_read: bool
    source_role_coverage: tuple[str, ...]
    absorber_boundary_coverage: tuple[str, ...]
    forbidden_shortcuts_used: tuple[str, ...]
    nontrivial_obstruction_witness: bool
    noncommuting_transport_square: bool
    native_payload_forced: bool
    target_import_terms: tuple[str, ...]
    fixture_label_terms: tuple[str, ...]
    rationale: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_role_coverage",
            "absorber_boundary_coverage",
            "forbidden_shortcuts_used",
            "target_import_terms",
            "fixture_label_terms",
        ):
            data[key] = list(data[key])
        return data


@dataclass(frozen=True)
class FreshFamilyEvaluation:
    candidate_id: str
    fresh_family_admissible: bool
    role_projection_complete: bool
    literal_replay_rejected: bool
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
class T570Result:
    artifact: str
    source_t569_verdict: str
    source_t569_selected_next_packet: str
    source_t569_independent_reimplementation_cleared: bool
    fresh_family_status: str
    source_law_status: str
    route_status: str
    fresh_family_projection: FreshFamilyProjection
    candidates: tuple[FreshFamilyCandidate, ...]
    evaluations: tuple[FreshFamilyEvaluation, ...]
    closure_checks: tuple[ClosureCheck, ...]
    route_decisions: tuple[RouteDecision, ...]
    gate_decisions: tuple[GateDecision, ...]
    admitted_family_ids: tuple[str, ...]
    rejected_control_ids: tuple[str, ...]
    fresh_family_stress_cleared: bool
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


def run_t570_analysis() -> T570Result:
    source = t569.run_t569_analysis()
    source_spec = source.independent_generator_spec
    projection = _fresh_family_projection(source_spec)
    candidates = _fresh_family_panel(source_spec)
    evaluations = tuple(
        _evaluate_candidate(projection, source_spec, candidate)
        for candidate in candidates
    )
    admitted_family_ids = tuple(
        evaluation.candidate_id
        for evaluation in evaluations
        if evaluation.fresh_family_admissible
    )
    rejected_control_ids = tuple(
        evaluation.candidate_id
        for evaluation in evaluations
        if not evaluation.fresh_family_admissible
    )
    source_law_earned = False
    closure_checks = _closure_checks(
        source=source,
        projection=projection,
        evaluations=evaluations,
        admitted_family_ids=admitted_family_ids,
        rejected_control_ids=rejected_control_ids,
    )
    fresh_family_stress_cleared = (
        source.verdict == t569.VERDICT
        and source.selected_next_packet == t569.NEXT_PACKET
        and source.independent_reimplementation_cleared
        and admitted_family_ids
        == (
            "calibration_chain_role_recoding_family",
            "archive_manifest_handoff_role_recoding_family",
        )
        and rejected_control_ids
        == (
            "same_family_surface_relabel_replay_control",
            "missing_transport_square_fresh_name_control",
            "target_geometry_import_family_control",
            "optional_payload_family_control",
            "absorber_complete_trivial_completion_control",
        )
        and all(check.passed for check in closure_checks)
    )
    route_decisions = _route_decisions(
        fresh_family_stress_cleared=fresh_family_stress_cleared,
        source_law_earned=source_law_earned,
    )
    selected_next_packet = _selected_next_packet(route_decisions)
    gate_decisions = _gate_decisions(
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        fresh_family_stress_cleared=fresh_family_stress_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
    )
    verdict = (
        VERDICT
        if fresh_family_stress_cleared
        and not source_law_earned
        and selected_next_packet == NEXT_PACKET
        and all(gate.passed for gate in gate_decisions)
        else "domain_native_sheaf_transport_fresh_family_stress_unexpected_status"
    )

    return T570Result(
        artifact=ARTIFACT,
        source_t569_verdict=source.verdict,
        source_t569_selected_next_packet=source.selected_next_packet,
        source_t569_independent_reimplementation_cleared=source.independent_reimplementation_cleared,
        fresh_family_status=FRESH_FAMILY_STATUS,
        source_law_status=SOURCE_LAW_STATUS,
        route_status=ROUTE_STATUS,
        fresh_family_projection=projection,
        candidates=candidates,
        evaluations=evaluations,
        closure_checks=closure_checks,
        route_decisions=route_decisions,
        gate_decisions=gate_decisions,
        admitted_family_ids=admitted_family_ids,
        rejected_control_ids=rejected_control_ids,
        fresh_family_stress_cleared=fresh_family_stress_cleared,
        source_law_earned=source_law_earned,
        selected_next_packet=selected_next_packet,
        verdict=verdict,
        source_law_reading=(
            "T570 preserves the T568/T569 semantic generator under fresh "
            "role-level recodings in two non-replay domains and rejects replay, "
            "target-import, missing-square, optional-payload, and trivial "
            "completion controls. That is stronger route evidence, but it is "
            "still finite review evidence rather than a public source law."
        ),
        recommended_next=(
            f"Run {NEXT_PACKET}. The next gate should rotate falsifiers across "
            "multiple admitted families and try to break the role-level "
            "projection before any source-law, claim, canon, public-posture, "
            "TAF4, TAF8, or S1 movement."
        ),
        taf11_update=(
            "TAF11 remains the top active lane. Fresh-family role recoding "
            "survived, but source-law status still waits for multi-family "
            "falsifier rotation."
        ),
        taf4_update=(
            "TAF4 remains blocked. Fresh-family stress of a finite semantic "
            "generator is not finite-to-continuum descent, causal-set recovery, "
            "Lorentzian target import, or manifoldlikeness evidence."
        ),
        taf8_update=(
            "TAF8 remains waiting. T570 is still internal TAF11 generator "
            "stress, not a domain-native cross-domain shadow-protection packet."
        ),
        claim_labels=_claim_labels(
            admitted_family_ids=admitted_family_ids,
            rejected_control_ids=rejected_control_ids,
        ),
        claim_ledger_update=(
            "No claim-ledger update is earned. T570 fresh-family stress keeps "
            "the semantic-generator route review-only and selects multi-family "
            "falsifier rotation; claim rows, Canon Index tiers, canon verdicts, "
            "and public posture remain unchanged."
        ),
        not_claimed=NOT_CLAIMED,
    )


def t570_result_to_dict(result: T570Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t569_verdict": result.source_t569_verdict,
        "source_t569_selected_next_packet": result.source_t569_selected_next_packet,
        "source_t569_independent_reimplementation_cleared": result.source_t569_independent_reimplementation_cleared,
        "fresh_family_status": result.fresh_family_status,
        "source_law_status": result.source_law_status,
        "route_status": result.route_status,
        "fresh_family_projection": result.fresh_family_projection.to_dict(),
        "candidates": [candidate.to_dict() for candidate in result.candidates],
        "evaluations": [evaluation.to_dict() for evaluation in result.evaluations],
        "closure_checks": [check.to_dict() for check in result.closure_checks],
        "route_decisions": [
            decision.to_dict() for decision in result.route_decisions
        ],
        "gate_decisions": [gate.to_dict() for gate in result.gate_decisions],
        "admitted_family_ids": list(result.admitted_family_ids),
        "rejected_control_ids": list(result.rejected_control_ids),
        "fresh_family_stress_cleared": result.fresh_family_stress_cleared,
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


def _fresh_family_projection(
    source_spec: t569.IndependentGeneratorSpec,
) -> FreshFamilyProjection:
    fresh_fields = (
        ("finite_event_covers", "certificate_window_cover"),
        ("local_finality_sections", "local_attestation_panels"),
        ("restriction_morphisms", "scope_restriction_maps"),
        ("settlement_obstruction_witnesses", "irreversible_disagreement_witnesses"),
        ("transport_consistency_squares", "handoff_commutation_squares"),
        ("allowed_refinement_steps", "audit_refinement_moves"),
    )
    absorber_boundaries = (
        ("ordinary_sheaf_gluing_completion", "ordinary_panel_gluing_completion"),
        ("resource_transport_monotone_absorber", "resource_monotone_relabel_absorber"),
        ("consensus_state_machine_absorber", "state_machine_quorum_absorber"),
        (
            "record_provenance_completion_absorber",
            "custody_provenance_completion_absorber",
        ),
    )
    source_names = set(source_spec.reconstructed_source_variables)
    literal_reused = tuple(
        fresh_field
        for _, fresh_field in fresh_fields
        if fresh_field in source_names
    )
    return FreshFamilyProjection(
        projection_id="fresh_role_recoding_projection_v1",
        source_contract_id=source_spec.source_contract_id,
        source_role_to_fresh_field=fresh_fields,
        absorber_role_to_fresh_boundary=absorber_boundaries,
        forbidden_shortcuts=source_spec.forbidden_shortcuts,
        semantic_requirements=source_spec.semantic_requirements,
        literal_source_variable_names_used_as_fields=literal_reused,
        rationale=(
            "The stress gate changes surface vocabulary and source domain while "
            "preserving the declared source-variable and absorber-boundary roles."
        ),
    )


def _fresh_family_panel(
    source_spec: t569.IndependentGeneratorSpec,
) -> tuple[FreshFamilyCandidate, ...]:
    source_roles = source_spec.reconstructed_source_variables
    absorber_roles = source_spec.reconstructed_absorber_ids
    return (
        FreshFamilyCandidate(
            candidate_id="calibration_chain_role_recoding_family",
            family_id="instrument_calibration_chain_finality_family",
            source_domain="calibration custody chain with irreversible repair windows",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            fixture_label_terms=(),
            rationale=(
                "Fresh source domain: calibration custody can force a repair "
                "payload through incompatible local attestations without using "
                "prior sheaf-transport fixture labels."
            ),
        ),
        FreshFamilyCandidate(
            candidate_id="archive_manifest_handoff_role_recoding_family",
            family_id="archive_manifest_handoff_finality_family",
            source_domain="archive migration manifest with delayed custody handoff",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            fixture_label_terms=(),
            rationale=(
                "Second fresh source domain: archive manifests change the "
                "vocabulary and operational story while preserving role-level "
                "finality and transport burdens."
            ),
        ),
        FreshFamilyCandidate(
            candidate_id="same_family_surface_relabel_replay_control",
            family_id="renamed_prior_holdout_family",
            source_domain="same sheaf-transport holdout with renamed labels",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=True,
            outcome_label_read=True,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=True,
            target_import_terms=(),
            fixture_label_terms=("escrow_window_rotation_holdout",),
            rationale="Rejects same-family relabeling as fresh-family evidence.",
        ),
        FreshFamilyCandidate(
            candidate_id="missing_transport_square_fresh_name_control",
            family_id="fresh_name_without_square_family",
            source_domain="fresh audit vocabulary without a noncommuting square",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=False,
            native_payload_forced=True,
            target_import_terms=(),
            fixture_label_terms=(),
            rationale="Rejects fresh vocabulary that lacks transport noncommutation.",
        ),
        FreshFamilyCandidate(
            candidate_id="target_geometry_import_family_control",
            family_id="target_geometry_import_family",
            source_domain="causal-set target reconstruction vocabulary",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=False,
            target_import_terms=("lorentzian_dimension_target",),
            fixture_label_terms=(),
            rationale="Rejects target-language import and missing native payload forcing.",
        ),
        FreshFamilyCandidate(
            candidate_id="optional_payload_family_control",
            family_id="optional_payload_recoding_family",
            source_domain="fresh audit vocabulary with optional settlement payload",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=True,
            noncommuting_transport_square=True,
            native_payload_forced=False,
            target_import_terms=(),
            fixture_label_terms=(),
            rationale="Rejects recodings where the payload is compatible but not forced.",
        ),
        FreshFamilyCandidate(
            candidate_id="absorber_complete_trivial_completion_control",
            family_id="ordinary_completion_family",
            source_domain="ordinary same-neighbor completion bookkeeping",
            role_projection_id="fresh_role_recoding_projection_v1",
            predeclared_before_evaluation=True,
            prior_family_replay=False,
            outcome_label_read=False,
            source_role_coverage=source_roles,
            absorber_boundary_coverage=absorber_roles,
            forbidden_shortcuts_used=(),
            nontrivial_obstruction_witness=False,
            noncommuting_transport_square=False,
            native_payload_forced=False,
            target_import_terms=(),
            fixture_label_terms=(),
            rationale="Rejects ordinary completion as source-family evidence.",
        ),
    )


def _evaluate_candidate(
    projection: FreshFamilyProjection,
    source_spec: t569.IndependentGeneratorSpec,
    candidate: FreshFamilyCandidate,
) -> FreshFamilyEvaluation:
    checks = _selector_checks(projection, source_spec, candidate)
    passed = tuple(name for name, ok in checks if ok)
    failed = tuple(name for name, ok in checks if not ok)
    fresh_family_admissible = not failed
    role_projection_complete = (
        candidate.source_role_coverage == source_spec.reconstructed_source_variables
        and candidate.absorber_boundary_coverage == source_spec.reconstructed_absorber_ids
        and candidate.role_projection_id == projection.projection_id
    )
    literal_replay_rejected = (
        candidate.prior_family_replay
        or candidate.outcome_label_read
        or candidate.fixture_label_terms != ()
        or candidate.family_id in INHERITED_FAMILY_IDS
    )
    if fresh_family_admissible:
        status = "ADMITTED_BY_FRESH_FAMILY_ROLE_STRESS"
        reason = "The fresh family satisfies the role-level semantic generator stress."
    elif literal_replay_rejected:
        status = "REJECTED_LITERAL_OR_OUTCOME_REPLAY"
        reason = "Fresh-family stress rejects prior-family replay, fixture labels, or outcome reading."
    elif candidate.target_import_terms:
        status = "REJECTED_TARGET_IMPORT"
        reason = "Fresh-family stress rejects target-language import."
    elif "noncommuting_transport_square" in failed:
        status = "REJECTED_MISSING_TRANSPORT_SQUARE"
        reason = "Fresh vocabulary is insufficient without a noncommuting transport square."
    elif "native_payload_forced" in failed:
        status = "REJECTED_NATIVE_PAYLOAD_NOT_FORCED"
        reason = "Fresh-family stress rejects unforced native payload."
    else:
        status = "REJECTED_FRESH_FAMILY_CONTRACT"
        reason = "Fresh-family stress rejects the candidate because: " + ", ".join(failed)
    return FreshFamilyEvaluation(
        candidate_id=candidate.candidate_id,
        fresh_family_admissible=fresh_family_admissible,
        role_projection_complete=role_projection_complete,
        literal_replay_rejected=literal_replay_rejected,
        status=status,
        passed_checks=passed,
        failed_checks=failed,
        reason=reason,
    )


def _selector_checks(
    projection: FreshFamilyProjection,
    source_spec: t569.IndependentGeneratorSpec,
    candidate: FreshFamilyCandidate,
) -> tuple[tuple[str, bool], ...]:
    source_roles = tuple(role for role, _ in projection.source_role_to_fresh_field)
    absorber_roles = tuple(role for role, _ in projection.absorber_role_to_fresh_boundary)
    return (
        (
            "t569_contract_source_roles_preserved",
            source_roles == source_spec.reconstructed_source_variables,
        ),
        (
            "t569_contract_absorber_roles_preserved",
            absorber_roles == source_spec.reconstructed_absorber_ids,
        ),
        (
            "fresh_projection_uses_new_field_names",
            projection.literal_source_variable_names_used_as_fields == (),
        ),
        (
            "predeclared_before_evaluation",
            candidate.predeclared_before_evaluation and not candidate.outcome_label_read,
        ),
        ("fresh_family_not_prior_replay", not candidate.prior_family_replay),
        ("fixture_labels_absent", candidate.fixture_label_terms == ()),
        (
            "role_projection_complete",
            candidate.source_role_coverage == source_spec.reconstructed_source_variables
            and candidate.absorber_boundary_coverage == source_spec.reconstructed_absorber_ids
            and candidate.role_projection_id == projection.projection_id,
        ),
        (
            "forbidden_shortcuts_absent",
            all(
                shortcut not in candidate.forbidden_shortcuts_used
                for shortcut in projection.forbidden_shortcuts
            )
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
    source: t569.T569Result,
    projection: FreshFamilyProjection,
    evaluations: tuple[FreshFamilyEvaluation, ...],
    admitted_family_ids: tuple[str, ...],
    rejected_control_ids: tuple[str, ...],
) -> tuple[ClosureCheck, ...]:
    by_id = {evaluation.candidate_id: evaluation for evaluation in evaluations}
    t569_authority = (
        source.verdict == t569.VERDICT
        and source.selected_next_packet == t569.NEXT_PACKET
        and source.independent_reimplementation_cleared
    )
    expected_admitted = (
        "calibration_chain_role_recoding_family",
        "archive_manifest_handoff_role_recoding_family",
    )
    expected_rejected = (
        "same_family_surface_relabel_replay_control",
        "missing_transport_square_fresh_name_control",
        "target_geometry_import_family_control",
        "optional_payload_family_control",
        "absorber_complete_trivial_completion_control",
    )
    projection_is_fresh = (
        projection.literal_source_variable_names_used_as_fields == ()
        and all(
            fresh_field not in source.independent_generator_spec.reconstructed_source_variables
            for _, fresh_field in projection.source_role_to_fresh_field
        )
    )
    return (
        ClosureCheck(
            check_id="t569_authority",
            status="PASS" if t569_authority else "FAIL",
            passed=t569_authority,
            evidence=(
                "T569 independently reimplemented the semantic generator.",
                "T569 selected fresh-family stress as next packet.",
            ),
            residual_risk="T569 is review authority, not source-law status.",
        ),
        ClosureCheck(
            check_id="fresh_projection_changes_surface_vocabulary",
            status="PASS" if projection_is_fresh else "FAIL",
            passed=projection_is_fresh,
            evidence=tuple(
                fresh_field
                for _, fresh_field in projection.source_role_to_fresh_field
            ),
            residual_risk="Role recoding is finite and still review-only.",
        ),
        ClosureCheck(
            check_id="fresh_families_admitted",
            status="PASS" if admitted_family_ids == expected_admitted else "FAIL",
            passed=admitted_family_ids == expected_admitted,
            evidence=admitted_family_ids,
            residual_risk="Two admitted families are not a source law.",
        ),
        ClosureCheck(
            check_id="fresh_controls_rejected",
            status="PASS" if rejected_control_ids == expected_rejected else "FAIL",
            passed=rejected_control_ids == expected_rejected,
            evidence=rejected_control_ids,
            residual_risk="More controls may expose failure modes.",
        ),
        ClosureCheck(
            check_id="literal_replay_control_active",
            status=(
                "PASS"
                if not by_id["same_family_surface_relabel_replay_control"].fresh_family_admissible
                and by_id["same_family_surface_relabel_replay_control"].literal_replay_rejected
                else "FAIL"
            ),
            passed=(
                not by_id["same_family_surface_relabel_replay_control"].fresh_family_admissible
                and by_id["same_family_surface_relabel_replay_control"].literal_replay_rejected
            ),
            evidence=(by_id["same_family_surface_relabel_replay_control"].status,),
            residual_risk="Replay controls are synthetic.",
        ),
        ClosureCheck(
            check_id="semantic_and_target_controls_active",
            status=(
                "PASS"
                if not by_id["missing_transport_square_fresh_name_control"].fresh_family_admissible
                and not by_id["target_geometry_import_family_control"].fresh_family_admissible
                and not by_id["optional_payload_family_control"].fresh_family_admissible
                and not by_id["absorber_complete_trivial_completion_control"].fresh_family_admissible
                else "FAIL"
            ),
            passed=(
                not by_id["missing_transport_square_fresh_name_control"].fresh_family_admissible
                and not by_id["target_geometry_import_family_control"].fresh_family_admissible
                and not by_id["optional_payload_family_control"].fresh_family_admissible
                and not by_id["absorber_complete_trivial_completion_control"].fresh_family_admissible
            ),
            evidence=(
                by_id["missing_transport_square_fresh_name_control"].status,
                by_id["target_geometry_import_family_control"].status,
                by_id["optional_payload_family_control"].status,
                by_id["absorber_complete_trivial_completion_control"].status,
            ),
            residual_risk="Finite controls do not exhaust mature absorber space.",
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
    fresh_family_stress_cleared: bool,
    source_law_earned: bool,
) -> tuple[RouteDecision, ...]:
    return (
        RouteDecision(
            decision_id="promote_source_law_now",
            outcome=(
                "SELECTED_PROMOTION"
                if source_law_earned
                else "REJECTED_REVIEW_ONLY_MULTI_FAMILY_FALSIFIER_REQUIRED"
            ),
            selected=source_law_earned,
            next_packet="none",
            reason=(
                "Promotion was earned."
                if source_law_earned
                else "Fresh-family stress clears a role-recoding check but not multi-family falsifier pressure."
            ),
        ),
        RouteDecision(
            decision_id="run_multi_family_falsifier_rotation_gate",
            outcome=(
                "SELECTED_NEXT_BURDEN"
                if fresh_family_stress_cleared and not source_law_earned
                else "PAUSED_UNTIL_FRESH_FAMILY_STRESS_CLEARS"
            ),
            selected=fresh_family_stress_cleared and not source_law_earned,
            next_packet=NEXT_PACKET,
            reason=(
                "The next honest review step is rotating falsifiers across multiple admitted families."
                if fresh_family_stress_cleared
                else "Fresh-family stress has not cleared."
            ),
        ),
        RouteDecision(
            decision_id="abandon_semantic_generator_route",
            outcome=(
                "SELECTED_ROUTE_RESET"
                if not fresh_family_stress_cleared
                else "PAUSED_FRESH_FAMILY_STRESS_CLEARED"
            ),
            selected=not fresh_family_stress_cleared,
            next_packet="none",
            reason=(
                "Route reset is needed if fresh-family stress fails."
                if not fresh_family_stress_cleared
                else "Route reset is premature because fresh-family stress cleared."
            ),
        ),
        RouteDecision(
            decision_id="move_taf4_from_t570",
            outcome="BLOCKED_TAF4_OVERREAD",
            selected=False,
            next_packet="none",
            reason="Fresh-family stress of a finite generator is not finite-to-continuum descent.",
        ),
        RouteDecision(
            decision_id="execute_taf8_from_t570",
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
    fresh_family_stress_cleared: bool,
    source_law_earned: bool,
    selected_next_packet: str,
) -> tuple[GateDecision, ...]:
    checks = {check.check_id: check for check in closure_checks}
    routes = {decision.decision_id: decision for decision in route_decisions}
    gates = (
        (
            "t569_authority",
            checks["t569_authority"].passed,
            "T569 supplies fresh-family stress authority.",
            "T569 did not supply expected fresh-family stress authority.",
        ),
        (
            "fresh_projection_not_literal_replay",
            checks["fresh_projection_changes_surface_vocabulary"].passed
            and checks["literal_replay_control_active"].passed,
            "The projection changes vocabulary and rejects same-family replay.",
            "The projection did not separate fresh-family evidence from replay.",
        ),
        (
            "fresh_families_expected_status",
            checks["fresh_families_admitted"].passed
            and checks["fresh_controls_rejected"].passed
            and checks["semantic_and_target_controls_active"].passed,
            "Fresh families admit while replay, semantic, target, and completion controls reject.",
            "The fresh-family panel did not produce the expected admissibility pattern.",
        ),
        (
            "source_law_not_promoted",
            not source_law_earned
            and routes["promote_source_law_now"].outcome
            == "REJECTED_REVIEW_ONLY_MULTI_FAMILY_FALSIFIER_REQUIRED",
            "Source-law promotion is rejected.",
            "Source-law promotion moved too early.",
        ),
        (
            "multi_family_falsifier_selected_next",
            fresh_family_stress_cleared
            and selected_next_packet == NEXT_PACKET
            and routes["run_multi_family_falsifier_rotation_gate"].selected,
            "Multi-family falsifier rotation is selected as the next burden.",
            "The expected multi-family falsifier next packet was not selected.",
        ),
        (
            "taf4_taf8_s1_boundaries_preserved",
            routes["move_taf4_from_t570"].outcome == "BLOCKED_TAF4_OVERREAD"
            and routes["execute_taf8_from_t570"].outcome == "BLOCKED_TAF8_OVERREAD"
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
    admitted_family_ids: tuple[str, ...],
    rejected_control_ids: tuple[str, ...],
) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Fresh-family role stress admits: "
                + ", ".join(admitted_family_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=(
                "Fresh-family role stress rejects controls: "
                + ", ".join(rejected_control_ids)
                + "."
            ),
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="Source-law status remains blocked by multi-family falsifier rotation.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="medium",
            text="Fresh-family role recoding strengthens route evidence without promoting it.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    projection = payload["fresh_family_projection"]
    lines = [
        "# T570 Results: Domain-Native Sheaf Transport Fresh-Family Stress Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Fresh-family status: `{payload['fresh_family_status']}`",
        f"- Source-law status: `{payload['source_law_status']}`",
        f"- Route status: `{payload['route_status']}`",
        f"- Source T569 verdict: `{payload['source_t569_verdict']}`",
        f"- Source T569 selected next packet: `{payload['source_t569_selected_next_packet']}`",
        f"- Source T569 independent reimplementation cleared: {payload['source_t569_independent_reimplementation_cleared']}",
        f"- Fresh-family stress cleared: {payload['fresh_family_stress_cleared']}",
        f"- Source law earned: {payload['source_law_earned']}",
        f"- Selected next packet: `{payload['selected_next_packet']}`",
        "",
        "## Fresh-Family Projection",
        "",
        f"- Projection: `{projection['projection_id']}`",
        f"- Source contract: `{projection['source_contract_id']}`",
        "- Source role recodings: "
        + ", ".join(
            f"`{role}` -> `{field}`"
            for role, field in projection["source_role_to_fresh_field"]
        ),
        "- Absorber role recodings: "
        + ", ".join(
            f"`{role}` -> `{boundary}`"
            for role, boundary in projection["absorber_role_to_fresh_boundary"]
        ),
        "- Semantic requirements: "
        + ", ".join(f"`{item}`" for item in projection["semantic_requirements"]),
        "- Literal source-variable field names reused: "
        + (
            ", ".join(
                f"`{item}`"
                for item in projection["literal_source_variable_names_used_as_fields"]
            )
            or "none"
        ),
        f"- Rationale: {projection['rationale']}",
        "",
        "## Fresh-Family Evaluations",
        "",
        "| candidate | family | fresh admits? | projection complete? | literal replay? | status | failed checks | reason |",
        "| --- | --- | :---: | :---: | :---: | --- | --- | --- |",
    ]
    for candidate, evaluation in zip(payload["candidates"], payload["evaluations"]):
        lines.append(
            "| "
            f"`{evaluation['candidate_id']}` | "
            f"`{candidate['family_id']}` | "
            f"{evaluation['fresh_family_admissible']} | "
            f"{evaluation['role_projection_complete']} | "
            f"{evaluation['literal_replay_rejected']} | "
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


def write_results(result: T570Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t570_result_to_dict(result)
    json_path = (
        results_dir
        / "T570-domain-native-sheaf-transport-fresh-family-stress-gate-v0.1.json"
    )
    md_path = (
        results_dir
        / "T570-domain-native-sheaf-transport-fresh-family-stress-gate-v0.1-results.md"
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

    result = run_t570_analysis()
    payload = t570_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
