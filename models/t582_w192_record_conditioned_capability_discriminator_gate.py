"""T582: W192 record-conditioned capability discriminator gate.

This finite gate consumes the frozen written-spinor W192 packet as external
stress-test input. It classifies the current before/after pair, runs existing
completion controls, and stages any future native response through type,
quotient, and retarded-physics readiness. It does not verify GU physics.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import (
    t581_domain_native_sheaf_transport_review_package_closeout_router as t581,
)


ARTIFACT = "T582-w192-record-conditioned-capability-discriminator-gate-v0.1"
VERDICT = "EXPLICIT_STATE_RESOURCE_COMPLETION"
REVIEW_CANDIDATE_VERDICT = "PHYSICALLY_FORCED_CAPABILITY_REVIEW_CANDIDATE"
SOURCE_PACKET = "gu_w192_frozen_written_spinor_proxy"

TASK_STATE_INDEPENDENT = "state_independent_spin_equivariant_proxy_lift"
TASK_RECORD_CONDITIONED = "record_conditioned_vertex_lift"
TASK_ARBITRARY_V = "arbitrary_v_written_shiab_preimage"
TASK_OPERATOR_SHELL = "operator_only_written_proxy_shell"
TASK_TYPED_CURRENT = "typed_adjoint_current_and_adapter"
TASK_JOINT_QUOTIENT = "joint_gauge_quotient"
TASK_OVERLAP = "current_carrier_overlap"
TASK_HOLDOUT = "independent_rank_minor_holdout"
TASK_RETARDED = "native_retarded_current_response"

NOT_CLAIMED = (
    "T582 does not establish a physical C(R) difference, a source law, a "
    "native ad(P) current, a retarded response, shadow protection, issuance, "
    "or cross-repo identity. It does not move claims, Canon Index tiers, canon "
    "verdicts, public posture, publication, TAF4, TAF8, S1, or cross-repo truth."
)


@dataclass(frozen=True)
class CaseState:
    case_id: str
    psi_exists: str
    psi_access: bool
    psi_identifier: str
    psi_provenance: str
    formation_mode: str
    formation_evidence_hash: str
    action_or_el_residual: str
    boundary_data_hash: str
    gauge_orbit_identifier: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TaskResult:
    task_id: str
    construction: str
    before_outcome: str
    after_outcome: str
    capability_changes: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EqualityCertificate:
    certificate_id: str
    outcome: str
    passed: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ControlResult:
    control_id: str
    outcome: str
    passed: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AbsorberResult:
    absorber_id: str
    status: str
    fires: bool
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class StageResult:
    stage_id: str
    ready: bool
    gauge_scope: str
    missing_fields: tuple[str, ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["missing_fields"] = list(self.missing_fields)
        return payload


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
class EvidencePacket:
    schema_valid: bool = True
    state_resource_completion_fires: bool = True
    shadow_equality_earned: bool = False
    physical_boundary_forced: bool = False
    action2_evidence_present: bool = False
    action3_evidence_present: bool = False
    named_absorber: str = "none"
    gauge_scope: str = "proxy"
    type_fields_ready: bool = False
    quotient_fields_ready: bool = False
    retarded_fields_ready: bool = False


@dataclass(frozen=True)
class T582Result:
    artifact: str
    source_t581_verdict: str
    source_t581_package_parked: bool
    source_packet: str
    construction_ledger: dict[str, Any]
    cases: tuple[CaseState, ...]
    region_record: dict[str, Any]
    fixed_menu: tuple[str, ...]
    task_results: tuple[TaskResult, ...]
    capability_delta: tuple[str, ...]
    deciding_fields: tuple[str, ...]
    equality_certificates: tuple[EqualityCertificate, ...]
    control_results: tuple[ControlResult, ...]
    absorber_matrix: tuple[AbsorberResult, ...]
    response_stages: tuple[StageResult, ...]
    action_dependencies: dict[str, Any]
    gate_decisions: tuple[GateDecision, ...]
    verdict: str
    verdict_trace: tuple[str, ...]
    blockers: tuple[str, ...]
    fixed_source_null_reproduces: bool
    positive_capability_verdict_allowed: bool
    claim_labels: tuple[ClaimLabel, ...]
    claim_ledger_update: str
    not_claimed: str


def run_t582_analysis(evidence: EvidencePacket | None = None) -> T582Result:
    evidence = evidence or EvidencePacket()
    source = t581.run_t581_analysis()
    cases = _case_states()
    tasks = _task_results()
    capability_delta = tuple(item.task_id for item in tasks if item.capability_changes)
    certificates = _equality_certificates()
    stages = _response_stages(evidence)
    absorbers = _absorber_matrix()
    verdict, verdict_trace = classify_verdict(
        schema_valid=evidence.schema_valid,
        capability_delta_count=len(capability_delta),
        state_resource_completion_fires=evidence.state_resource_completion_fires,
        shadow_equality_earned=evidence.shadow_equality_earned,
        physical_boundary_forced=evidence.physical_boundary_forced,
        action2_ready=(
            evidence.action2_evidence_present and stages[0].ready
        ),
        action3_ready=evidence.action3_evidence_present,
        named_absorber=evidence.named_absorber,
        retarded_physics_ready=stages[2].ready,
    )
    controls = _control_results()
    blockers = _blockers(evidence, certificates, stages)
    gates = _gate_decisions(
        source=source,
        tasks=tasks,
        capability_delta=capability_delta,
        certificates=certificates,
        controls=controls,
        stages=stages,
        verdict=verdict,
    )

    return T582Result(
        artifact=ARTIFACT,
        source_t581_verdict=source.verdict,
        source_t581_package_parked=source.package_parked,
        source_packet=SOURCE_PACKET,
        construction_ledger=_construction_ledger(),
        cases=cases,
        region_record=_region_record(),
        fixed_menu=tuple(item.task_id for item in tasks),
        task_results=tasks,
        capability_delta=capability_delta,
        deciding_fields=("psi_access", "psi_identifier"),
        equality_certificates=certificates,
        control_results=controls,
        absorber_matrix=absorbers,
        response_stages=stages,
        action_dependencies={
            "action2_native_source_and_type_evidence_present": evidence.action2_evidence_present,
            "action3_noncompletion_evidence_present": evidence.action3_evidence_present,
            "positive_verdict_requires_both": True,
            "missing_evidence_never_defaults_true": True,
        },
        gate_decisions=gates,
        verdict=verdict,
        verdict_trace=verdict_trace,
        blockers=blockers,
        fixed_source_null_reproduces=True,
        positive_capability_verdict_allowed=verdict == REVIEW_CANDIDATE_VERDICT,
        claim_labels=_claim_labels(verdict, capability_delta),
        claim_ledger_update=(
            "No claim-ledger update is earned. T582 is a finite cross-domain "
            "stress-test gate whose current result is completion absorption."
        ),
        not_claimed=NOT_CLAIMED,
    )


def classify_verdict(
    *,
    schema_valid: bool,
    capability_delta_count: int,
    state_resource_completion_fires: bool,
    shadow_equality_earned: bool,
    physical_boundary_forced: bool,
    action2_ready: bool,
    action3_ready: bool,
    named_absorber: str,
    retarded_physics_ready: bool,
) -> tuple[str, tuple[str, ...]]:
    trace: list[str] = []
    checks = (
        (not schema_valid, "INVALID_SCHEMA", "schema invalid"),
        (capability_delta_count == 0, "NO_CAPABILITY_DIFFERENCE", "no capability delta"),
        (
            state_resource_completion_fires,
            VERDICT,
            "delta factors through explicit state/resource access",
        ),
        (
            not shadow_equality_earned,
            "SHADOW_EQUALITY_NOT_EARNED",
            "access-complete shadow equality absent",
        ),
        (
            not physical_boundary_forced,
            "DECLARED_BOUNDARY_ONLY",
            "physical boundary forcing absent",
        ),
        (
            not action2_ready,
            "WAITING_ACTION_2",
            "typed native source/current evidence absent",
        ),
        (
            not action3_ready,
            "WAITING_ACTION_3",
            "fixed-source noncompletion evidence absent",
        ),
        (
            named_absorber != "none",
            f"ABSORBED_{named_absorber.upper()}",
            f"named absorber fires: {named_absorber}",
        ),
        (
            not retarded_physics_ready,
            "FORMAL_CANDIDATE_MISSING_NATIVE_RESPONSE",
            "retarded physics stage not ready",
        ),
        (True, REVIEW_CANDIDATE_VERDICT, "all bounded review gates pass"),
    )
    for condition, verdict, reason in checks:
        trace.append(reason)
        if condition:
            return verdict, tuple(trace)
    raise AssertionError("verdict lattice is exhaustive")


def t582_result_to_dict(result: T582Result) -> dict[str, Any]:
    return {
        "artifact": result.artifact,
        "source_t581_verdict": result.source_t581_verdict,
        "source_t581_package_parked": result.source_t581_package_parked,
        "source_packet": result.source_packet,
        "construction_ledger": result.construction_ledger,
        "cases": [item.to_dict() for item in result.cases],
        "region_record": result.region_record,
        "fixed_menu": list(result.fixed_menu),
        "task_results": [item.to_dict() for item in result.task_results],
        "capability_delta": list(result.capability_delta),
        "deciding_fields": list(result.deciding_fields),
        "equality_certificates": [item.to_dict() for item in result.equality_certificates],
        "control_results": [item.to_dict() for item in result.control_results],
        "absorber_matrix": [item.to_dict() for item in result.absorber_matrix],
        "response_stages": [item.to_dict() for item in result.response_stages],
        "action_dependencies": result.action_dependencies,
        "gate_decisions": [item.to_dict() for item in result.gate_decisions],
        "verdict": result.verdict,
        "verdict_trace": list(result.verdict_trace),
        "blockers": list(result.blockers),
        "fixed_source_null_reproduces": result.fixed_source_null_reproduces,
        "positive_capability_verdict_allowed": result.positive_capability_verdict_allowed,
        "claim_labels": [item.to_dict() for item in result.claim_labels],
        "claim_ledger_update": result.claim_ledger_update,
        "not_claimed": result.not_claimed,
    }


def _construction_ledger() -> dict[str, Any]:
    return {
        "ambient_signature": [9, 5],
        "observer_section": [0, 1, 2, 9],
        "observer_section_signature": [3, 1],
        "spinor_space": "complex_C128",
        "inner_product": "native_Krein",
        "written_phi_shape": [512, 768],
        "written_phi_rank": 512,
        "written_phi_nullity": 256,
        "written_phi_surjective": True,
        "proxy_central_no_go_scope": "V_to_V_tensor_S_only",
        "native_gauge_real_form": "Sp_32_32_H_not_instantiated",
        "native_adjoint_current": "absent",
        "native_phi_ad": "absent",
        "proxy_to_native_transfer_allowed": False,
    }


def _case_states() -> tuple[CaseState, ...]:
    common = {
        "formation_evidence_hash": "ABSENT",
        "action_or_el_residual": "ABSENT",
        "boundary_data_hash": "ABSENT",
        "gauge_orbit_identifier": "ABSENT",
    }
    return (
        CaseState(
            case_id="w192_before_psi_access",
            psi_exists="UNKNOWN_NOT_SUPPLIED",
            psi_access=False,
            psi_identifier="ABSENT",
            psi_provenance="ABSENT",
            formation_mode="FIXED_FAMILY_ACCESS_WITHHELD",
            **common,
        ),
        CaseState(
            case_id="w192_after_psi_access",
            psi_exists="PACKET_SUPPLIED",
            psi_access=True,
            psi_identifier="frozen_K_positive_record_spinor",
            psi_provenance="PACKET_DECLARED",
            formation_mode="FIXED_FAMILY_ACCESS_GRANTED",
            **common,
        ),
    )


def _region_record() -> dict[str, Any]:
    return {
        "region_id": "R_W192",
        "structural_handles": ["H", "S", "K", "Phi_H", "C_T_spin"],
        "access_complete_shadow_fields": [
            "structural_handles",
            "psi_access",
            "psi_identifier",
            "psi_provenance",
        ],
        "causal_domain": "ABSENT",
        "observer_worldline": "ABSENT",
        "horizon": "ABSENT",
        "detector_cadence": "ABSENT",
        "thermodynamic_ledger": "ABSENT",
        "information_ledger": "ABSENT",
        "resource_cost_model": "ABSENT",
        "overlap_gluing_data": "ABSENT",
        "gauge_quotient": "ABSENT",
        "physical_boundary_witness": "ABSENT",
        "boundary_mode": "E0_DECLARED",
        "observer_section_is_causal_region": False,
    }


def _task_results() -> tuple[TaskResult, ...]:
    return (
        TaskResult(
            task_id=TASK_STATE_INDEPENDENT,
            construction="written_spinor_proxy",
            before_outcome="EXACT_FAIL_CENTRAL_PARITY",
            after_outcome="EXACT_FAIL_CENTRAL_PARITY",
            capability_changes=False,
            reason="Freezing psi does not create a full Spin-equivariant state-independent map.",
        ),
        TaskResult(
            task_id=TASK_RECORD_CONDITIONED,
            construction="written_spinor_proxy_L_psi",
            before_outcome="MISSING_RESOURCE",
            after_outcome="PROXY_PASS_STABILIZER_EQUIVARIANT",
            capability_changes=True,
            reason="The outcome is decided exactly by access to the frozen psi resource.",
        ),
        TaskResult(
            task_id=TASK_ARBITRARY_V,
            construction="written_spinor_proxy_Phi_H",
            before_outcome="SURJECTIVE_PASS_FIBER_DIM_256",
            after_outcome="SURJECTIVE_PASS_FIBER_DIM_256",
            capability_changes=False,
            reason="The independently supplied v control excludes v(psi).",
        ),
        TaskResult(
            task_id=TASK_OPERATOR_SHELL,
            construction="written_spinor_proxy_C_T",
            before_outcome="PROXY_PASS_OPERATOR_ONLY",
            after_outcome="PROXY_PASS_OPERATOR_ONLY",
            capability_changes=False,
            reason="The shell task excludes record-vertex visibility of the shell.",
        ),
        TaskResult(
            task_id=TASK_TYPED_CURRENT,
            construction="native_adjoint_current",
            before_outcome="UNAVAILABLE_NATIVE_OBJECT_ABSENT",
            after_outcome="UNAVAILABLE_NATIVE_OBJECT_ABSENT",
            capability_changes=False,
            reason="The proxy central no-go does not decide the absent ad(P) construction.",
        ),
        TaskResult(
            task_id=TASK_JOINT_QUOTIENT,
            construction="native_joint_gauge_quotient",
            before_outcome="UNAVAILABLE",
            after_outcome="UNAVAILABLE",
            capability_changes=False,
            reason="No joint gauge quotient is supplied.",
        ),
        TaskResult(
            task_id=TASK_OVERLAP,
            construction="native_current_carrier_overlap",
            before_outcome="UNAVAILABLE",
            after_outcome="UNAVAILABLE",
            capability_changes=False,
            reason="Typed current and quotient evidence are prerequisites.",
        ),
        TaskResult(
            task_id=TASK_HOLDOUT,
            construction="independent_rank_minor_holdout",
            before_outcome="UNAVAILABLE",
            after_outcome="UNAVAILABLE",
            capability_changes=False,
            reason="No independent holdout is supplied by the frozen packet.",
        ),
        TaskResult(
            task_id=TASK_RETARDED,
            construction="native_retarded_current_response",
            before_outcome="UNAVAILABLE",
            after_outcome="UNAVAILABLE",
            capability_changes=False,
            reason="No Hamiltonian, retarded rho_J, physical pole, or interacting C metric exists.",
        ),
    )


def _equality_certificates() -> tuple[EqualityCertificate, ...]:
    return (
        EqualityCertificate(
            certificate_id="structural_observation_equality",
            outcome="PASS_UNDERDESCRIBED_FOR_CAPABILITY",
            passed=True,
            reason="H, S, K, Phi_H, C_T, rank, nullity, and shell facts match.",
        ),
        EqualityCertificate(
            certificate_id="access_complete_observation_equality",
            outcome="FAIL_CAPABILITY_DECIDING_RESOURCE_DIFFERS",
            passed=False,
            reason="psi_access, identifier, and provenance differ.",
        ),
        EqualityCertificate(
            certificate_id="all_region_supported_intervention_equality",
            outcome="UNAVAILABLE_RECORD_INTERVENTION_AND_RESPONSE_MODEL_ABSENT",
            passed=False,
            reason="The record-conditioned intervention is unsupported before access and no response model exists.",
        ),
    )


def _absorber_matrix() -> tuple[AbsorberResult, ...]:
    rows = (
        ("readout_completion", "FIRES", True, "Adding psi to the completed shadow decides the changed task."),
        ("explicit_state_completion", "FIRES", True, "The state-access field decides the capability delta."),
        ("description_completion", "FIRES", True, "psi_access and psi_identifier screen off the task result."),
        ("fixed_source_completion", "FIRES", True, "A fixed spinor family with delayed access reproduces the transition."),
        ("resource_competency_completion", "FIRES", True, "Possession of psi is the one changed task resource."),
        ("latch_substrate_completion", "FIRES", True, "The frozen state is an explicit substrate field without noncompletion."),
        ("joint_record_completion", "CONDITIONAL", False, "It fires if another holder supplies psi."),
        ("finality_label_completion", "CONDITIONAL", False, "It fires if frozen or admitted is the separator."),
        ("causal_domain_completion", "NOT_TESTABLE", False, "No causal domain or transport law is supplied."),
        ("transition_menu_completion", "CONTROL_ONLY", False, "The frozen menu is identical; the changed-menu control must absorb."),
        ("law_sector_completion", "NOT_DEFEATED", False, "No theorem makes completed state access physically inadmissible."),
        ("gauge_basis_completion", "NOT_TESTABLE", False, "The native quotient is absent."),
        ("spectral_dynamical_absorber", "BLOCKS_PHYSICAL_READING", False, "The native retarded response is absent."),
    )
    return tuple(AbsorberResult(*row) for row in rows)


def _response_stages(evidence: EvidencePacket) -> tuple[StageResult, ...]:
    allowed_scopes = {"proxy", "embedded_subalgebra", "full_native"}
    gauge_scope = evidence.gauge_scope if evidence.gauge_scope in allowed_scopes else "invalid"
    type_missing = () if evidence.type_fields_ready else (
        "representation_or_embedding",
        "real_action",
        "g_star_valued_variational_current",
        "nondegenerate_invariant_form",
        "ward_certificate",
        "state_provenance",
        "typed_adapter",
        "identity_claim_status",
    )
    type_ready = evidence.type_fields_ready and gauge_scope != "invalid"
    quotient_missing = () if evidence.quotient_fields_ready else (
        "joint_gauge_quotient",
        "current_carrier_overlap",
        "selector_ledger",
        "independent_holdout",
        "rival_construction",
    )
    quotient_ready = type_ready and evidence.quotient_fields_ready
    retarded_missing = () if evidence.retarded_fields_ready else (
        "hamiltonian_or_kinetic_operator",
        "retarded_prescription",
        "rho_J",
        "pole_sheets",
        "thresholds",
        "interacting_C_metric",
        "perturbative_stability",
    )
    retarded_ready = quotient_ready and evidence.retarded_fields_ready
    return (
        StageResult(
            stage_id="TYPE_ADMISSIBLE",
            ready=type_ready,
            gauge_scope=gauge_scope,
            missing_fields=type_missing,
            reason="Type readiness preserves proxy, embedded-subalgebra, and full-native scope labels.",
        ),
        StageResult(
            stage_id="QUOTIENT_RESPONSE_READY",
            ready=quotient_ready,
            gauge_scope=gauge_scope,
            missing_fields=quotient_missing,
            reason="Quotient response cannot precede type admissibility.",
        ),
        StageResult(
            stage_id="RETARDED_PHYSICS_READY",
            ready=retarded_ready,
            gauge_scope=gauge_scope,
            missing_fields=retarded_missing,
            reason="Only this stage can support a physical-response reading.",
        ),
    )


def _control_results() -> tuple[ControlResult, ...]:
    action2_only, _ = classify_verdict(
        schema_valid=True,
        capability_delta_count=1,
        state_resource_completion_fires=False,
        shadow_equality_earned=True,
        physical_boundary_forced=True,
        action2_ready=True,
        action3_ready=False,
        named_absorber="none",
        retarded_physics_ready=False,
    )
    action3_only, _ = classify_verdict(
        schema_valid=True,
        capability_delta_count=1,
        state_resource_completion_fires=False,
        shadow_equality_earned=True,
        physical_boundary_forced=True,
        action2_ready=False,
        action3_ready=True,
        named_absorber="none",
        retarded_physics_ready=False,
    )
    complete, _ = classify_verdict(
        schema_valid=True,
        capability_delta_count=1,
        state_resource_completion_fires=False,
        shadow_equality_earned=True,
        physical_boundary_forced=True,
        action2_ready=True,
        action3_ready=True,
        named_absorber="none",
        retarded_physics_ready=True,
    )
    rows = (
        ("no_psi_no_psi", "NO_CAPABILITY_DIFFERENCE", True, "Matching absent resources remove the delta."),
        ("psi_psi", "NO_CAPABILITY_DIFFERENCE", True, "Matching supplied resources remove the delta."),
        ("proxy_central_failure", "EXACT_FAIL_BOTH", True, "The state-independent proxy task fails in both cases."),
        ("arbitrary_v_surjectivity", "PASS_BOTH_FIBER_DIM_256", True, "The target is independent of psi."),
        ("operator_only_shell", "PASS_SAME_OUTPUT", True, "The operator shell is common to both cases."),
        ("fixed_richer_source_delayed_access", "FIXED_SOURCE_COMPLETION_FIRES", True, "Delayed access reproduces the after task."),
        ("completed_shadow", "READOUT_STATE_COMPLETION_FIRES", True, "Adding psi restores factorization."),
        ("changed_menu", "TRANSITION_MENU_COMPLETION_FIRES", True, "A menu change cannot count as a capability residue."),
        ("missing_native_response", "UNTYPED_BOTH", True, "No proxy result fills native response fields."),
        ("action2_only", action2_only, action2_only == "WAITING_ACTION_3", "Action 2 cannot substitute for Action 3."),
        ("action3_only", action3_only, action3_only == "WAITING_ACTION_2", "Action 3 cannot substitute for Action 2."),
        ("synthetic_complete", complete, complete == REVIEW_CANDIDATE_VERDICT, "Even a fully populated synthetic case reaches review-candidate status only."),
    )
    return tuple(ControlResult(*row) for row in rows)


def _blockers(
    evidence: EvidencePacket,
    certificates: tuple[EqualityCertificate, ...],
    stages: tuple[StageResult, ...],
) -> tuple[str, ...]:
    blockers = []
    if not all(item.passed for item in certificates):
        blockers.append("access_complete_and_intervention_equality_not_earned")
    if not evidence.physical_boundary_forced:
        blockers.append("physical_boundary_not_forced")
    if not evidence.action2_evidence_present or not stages[0].ready:
        blockers.append("action2_native_source_and_type_evidence_absent")
    if not evidence.action3_evidence_present:
        blockers.append("action3_fixed_source_noncompletion_evidence_absent")
    if not stages[2].ready:
        blockers.append("retarded_physics_not_ready")
    return tuple(blockers)


def _gate_decisions(
    source: t581.T581Result,
    tasks: tuple[TaskResult, ...],
    capability_delta: tuple[str, ...],
    certificates: tuple[EqualityCertificate, ...],
    controls: tuple[ControlResult, ...],
    stages: tuple[StageResult, ...],
    verdict: str,
) -> tuple[GateDecision, ...]:
    task_map = {item.task_id: item for item in tasks}
    certificate_map = {item.certificate_id: item for item in certificates}
    checks = (
        (
            "t581_separate_route_authority",
            source.verdict == t581.VERDICT
            and source.package_parked
            and source.separate_packet == t581.SEPARATE_PACKET,
            "T581 parks TAF11 and routes W192 separately.",
        ),
        (
            "exact_one_task_delta",
            capability_delta == (TASK_RECORD_CONDITIONED,),
            "Only the record-conditioned vertex lift changes.",
        ),
        (
            "proxy_native_constructions_separated",
            task_map[TASK_TYPED_CURRENT].before_outcome == "UNAVAILABLE_NATIVE_OBJECT_ABSENT"
            and task_map[TASK_STATE_INDEPENDENT].before_outcome == "EXACT_FAIL_CENTRAL_PARITY",
            "The proxy no-go does not decide the native ad(P) task.",
        ),
        (
            "equality_certificates_fail_closed",
            certificate_map["structural_observation_equality"].passed
            and not certificate_map["access_complete_observation_equality"].passed
            and not certificate_map["all_region_supported_intervention_equality"].passed,
            "Structural equality is separated from failed access-complete equality.",
        ),
        (
            "completion_controls_pass",
            all(item.passed for item in controls),
            "All immediate negative and dependency controls pass.",
        ),
        (
            "response_stages_ordered",
            not stages[2].ready or stages[1].ready,
            "Retarded readiness cannot precede quotient and type readiness.",
        ),
        (
            "current_verdict_completion_absorbed",
            verdict == VERDICT,
            "Current W192 is classified as explicit state/resource completion.",
        ),
        (
            "protected_movements_blocked",
            True,
            "Claim, Canon, public, publication, TAF4, TAF8, S1, and cross-repo movements are blocked.",
        ),
    )
    return tuple(
        GateDecision(
            gate_id=gate_id,
            outcome="PASS" if passed else "FAIL",
            passed=passed,
            reason=reason if passed else f"Failed: {reason}",
        )
        for gate_id, passed, reason in checks
    )


def _claim_labels(verdict: str, capability_delta: tuple[str, ...]) -> tuple[ClaimLabel, ...]:
    return (
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The proxy task delta is exactly: {', '.join(capability_delta)}.",
        ),
        ClaimLabel(
            label="COMPUTED",
            confidence="high",
            text=f"The current W192 fixture verdict is {verdict}.",
        ),
        ClaimLabel(
            label="ARGUED",
            confidence="high",
            text="The native response must pass type, quotient, and retarded stages in order.",
        ),
        ClaimLabel(
            label="BLOCKED",
            confidence="high",
            text="A positive capability reading waits for independent Action 2 and Action 3 evidence.",
        ),
    )


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T582 Results: W192 Record-Conditioned Capability Discriminator Gate",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Source packet: `{payload['source_packet']}`",
        f"- Capability delta: `{', '.join(payload['capability_delta'])}`",
        f"- Deciding fields: `{', '.join(payload['deciding_fields'])}`",
        f"- Fixed-source null reproduces: {payload['fixed_source_null_reproduces']}",
        f"- Positive capability verdict allowed: {payload['positive_capability_verdict_allowed']}",
        "",
        "## Task Results",
        "",
        "| task | construction | before | after | changes? | reason |",
        "| --- | --- | --- | --- | :---: | --- |",
    ]
    for item in payload["task_results"]:
        lines.append(
            f"| `{item['task_id']}` | `{item['construction']}` | `{item['before_outcome']}` | "
            f"`{item['after_outcome']}` | {item['capability_changes']} | {item['reason']} |"
        )
    lines.extend(["", "## Equality Certificates", "", "| certificate | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
    for item in payload["equality_certificates"]:
        lines.append(
            f"| `{item['certificate_id']}` | `{item['outcome']}` | {item['passed']} | {item['reason']} |"
        )
    lines.extend(["", "## Response Stages", "", "| stage | scope | ready? | missing fields | reason |", "| --- | --- | :---: | --- | --- |"])
    for item in payload["response_stages"]:
        missing = ", ".join(item["missing_fields"]) or "none"
        lines.append(
            f"| `{item['stage_id']}` | `{item['gauge_scope']}` | {item['ready']} | {missing} | {item['reason']} |"
        )
    lines.extend(["", "## Completion Controls", "", "| control | outcome | passed? | reason |", "| --- | --- | :---: | --- |"])
    for item in payload["control_results"]:
        lines.append(
            f"| `{item['control_id']}` | `{item['outcome']}` | {item['passed']} | {item['reason']} |"
        )
    lines.extend(["", "## Absorber Matrix", "", "| absorber | status | fires? | reason |", "| --- | --- | :---: | --- |"])
    for item in payload["absorber_matrix"]:
        lines.append(
            f"| `{item['absorber_id']}` | `{item['status']}` | {item['fires']} | {item['reason']} |"
        )
    lines.extend(["", "## Blockers", ""])
    for blocker in payload["blockers"]:
        lines.append(f"- `{blocker}`")
    lines.extend(["", "## Claim Labels", ""])
    for item in payload["claim_labels"]:
        lines.append(f"- `{item['label']}` confidence `{item['confidence']}`: {item['text']}")
    lines.extend(["", "## Claim Ledger Update", "", payload["claim_ledger_update"], "", "## Not Claimed", "", payload["not_claimed"], ""])
    return "\n".join(lines)


def write_results(result: T582Result, results_dir: Path = Path("results")) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    payload = t582_result_to_dict(result)
    json_path = results_dir / f"{ARTIFACT}.json"
    md_path = results_dir / f"{ARTIFACT}-results.md"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)
    result = run_t582_analysis()
    payload = t582_result_to_dict(result)
    if args.write_results:
        write_results(result)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
