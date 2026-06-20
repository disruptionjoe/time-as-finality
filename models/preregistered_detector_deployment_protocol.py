"""T78: pre-registered detector deployment protocol gate.

T76 and T77 made the detector branch executable, but still at fixture level.
T78 moves the test boundary before data collection: a detector run can only
upgrade Q1 if its evidence fields, controls, policy corridor, and demotion
rules were fixed before the first event and are backed by real raw logs.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.measured_detector_provenance_posterior import (
    AuditPolicy,
    DeploymentEvidence,
)
from models.provenance_protocol_monte_carlo import Range


REQUIRED_EVIDENCE_FIELDS: tuple[str, ...] = tuple(
    field
    for field in DeploymentEvidence.__dataclass_fields__
    if field not in {"name", "purpose"}
)

REQUIRED_CONTROL_ROLES: tuple[str, ...] = (
    "timing_only_unsigned_negative_control",
    "copied_record_spoof_challenge",
    "independent_record_uniqueness_challenge",
    "perturbation_positive_negative_controls",
    "dag_truncation_and_replay_challenge",
)

REQUIRED_RAW_LOG_SOURCES: tuple[str, ...] = (
    "raw_time_tag_stream",
    "signature_verification_log",
    "archive_receipt_chain",
    "trust_boundary_audit_log",
    "perturbation_protocol_log",
    "ancestry_dag_export",
)

SAFE_CONFIDENCE_FLOOR_LOW = 0.78
SAFE_FALSE_RISK_HIGH = 0.22


@dataclass(frozen=True)
class DeploymentPreregistration:
    name: str
    registered_before_first_event: bool
    policy_registered_before_data: bool
    analysis_code_frozen: bool
    uses_real_raw_log: bool
    fixture_counts_only: bool
    declared_demote_on_control_leak: bool
    policy: AuditPolicy
    evidence_fields: frozenset[str]
    control_roles: frozenset[str]
    raw_log_sources: frozenset[str]
    threshold_fields_declared: int
    threshold_fields_required: int
    purpose: str


@dataclass(frozen=True)
class PreregistrationAudit:
    plan_name: str
    verdict: str
    missing_evidence_fields: tuple[str, ...]
    missing_control_roles: tuple[str, ...]
    missing_raw_log_sources: tuple[str, ...]
    failure_reasons: tuple[str, ...]
    next_allowed_audit: str


@dataclass(frozen=True)
class T78Result:
    audits: tuple[PreregistrationAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    recommended_next: str
    blocker: str


def complete_lab_preregistration() -> DeploymentPreregistration:
    return DeploymentPreregistration(
        name="complete_signed_detector_deployment_preregistration",
        registered_before_first_event=True,
        policy_registered_before_data=True,
        analysis_code_frozen=True,
        uses_real_raw_log=True,
        fixture_counts_only=False,
        declared_demote_on_control_leak=True,
        policy=AuditPolicy(),
        evidence_fields=frozenset(REQUIRED_EVIDENCE_FIELDS),
        control_roles=frozenset(REQUIRED_CONTROL_ROLES),
        raw_log_sources=frozenset(REQUIRED_RAW_LOG_SOURCES),
        threshold_fields_declared=len(REQUIRED_EVIDENCE_FIELDS),
        threshold_fields_required=len(REQUIRED_EVIDENCE_FIELDS),
        purpose=(
            "A lab-facing detector run whose evidence schema, controls, and "
            "acceptance policy are fixed before data collection."
        ),
    )


def posthoc_policy_preregistration() -> DeploymentPreregistration:
    base = complete_lab_preregistration()
    return replace(
        base,
        name="posthoc_policy_after_data_control",
        policy_registered_before_data=False,
        purpose=(
            "A strong-looking detector run whose acceptance corridor is "
            "chosen after inspecting deployment data."
        ),
    )


def missing_unsigned_control_preregistration() -> DeploymentPreregistration:
    base = complete_lab_preregistration()
    controls = set(REQUIRED_CONTROL_ROLES)
    controls.remove("timing_only_unsigned_negative_control")
    return replace(
        base,
        name="missing_unsigned_timing_control",
        control_roles=frozenset(controls),
        purpose=(
            "A signed detector run with no timing-matched unsigned "
            "negative control."
        ),
    )


def fixture_only_preregistration() -> DeploymentPreregistration:
    base = complete_lab_preregistration()
    return replace(
        base,
        name="fixture_counts_without_raw_log",
        uses_real_raw_log=False,
        fixture_counts_only=True,
        purpose=(
            "A reproduction of T76/T77 fixture counts without a real "
            "deployment log."
        ),
    )


def permissive_policy_preregistration() -> DeploymentPreregistration:
    base = complete_lab_preregistration()
    return replace(
        base,
        name="permissive_policy_control_leak",
        policy=AuditPolicy(
            confidence_floor=Range(0.65, 0.75),
            max_false_risk=Range(0.25, 0.35),
        ),
        purpose=(
            "A run with complete instrumentation but the T77 permissive "
            "corridor that leaked unsigned false positives."
        ),
    )


def preregistration_fixtures() -> tuple[DeploymentPreregistration, ...]:
    return (
        complete_lab_preregistration(),
        posthoc_policy_preregistration(),
        missing_unsigned_control_preregistration(),
        fixture_only_preregistration(),
        permissive_policy_preregistration(),
    )


def audit_preregistration(plan: DeploymentPreregistration) -> PreregistrationAudit:
    missing_evidence = _missing(plan.evidence_fields, REQUIRED_EVIDENCE_FIELDS)
    missing_controls = _missing(plan.control_roles, REQUIRED_CONTROL_ROLES)
    missing_logs = _missing(plan.raw_log_sources, REQUIRED_RAW_LOG_SOURCES)
    failures: list[str] = []

    if not plan.registered_before_first_event:
        failures.append("contract_not_registered_before_first_event")
    if not plan.policy_registered_before_data:
        failures.append("policy_chosen_after_data")
    if not plan.analysis_code_frozen:
        failures.append("analysis_code_not_frozen")
    if not plan.uses_real_raw_log:
        failures.append("no_real_raw_deployment_log")
    if plan.fixture_counts_only:
        failures.append("fixture_counts_only")
    if not plan.declared_demote_on_control_leak:
        failures.append("no_predeclared_demote_rule_for_control_leak")
    if missing_evidence:
        failures.append("missing_required_evidence_fields")
    if missing_controls:
        failures.append("missing_required_negative_controls")
    if missing_logs:
        failures.append("missing_required_raw_log_sources")
    if plan.threshold_fields_required <= 0:
        failures.append("invalid_threshold_field_count")
    elif plan.threshold_fields_declared < plan.threshold_fields_required:
        failures.append("incomplete_threshold_preregistration")
    if not _policy_inside_t77_safe_corridor(plan.policy):
        failures.append("policy_outside_t77_safe_corridor")

    verdict = (
        "admissible_for_real_deployment_audit"
        if not failures
        else "inadmissible_for_q1_upgrade"
    )
    next_allowed = (
        "run_t76_t77_on_real_log"
        if verdict == "admissible_for_real_deployment_audit"
        else "withhold_detector_q1_upgrade"
    )
    return PreregistrationAudit(
        plan_name=plan.name,
        verdict=verdict,
        missing_evidence_fields=missing_evidence,
        missing_control_roles=missing_controls,
        missing_raw_log_sources=missing_logs,
        failure_reasons=tuple(failures),
        next_allowed_audit=next_allowed,
    )


def run_t78_analysis() -> T78Result:
    audits = tuple(audit_preregistration(plan) for plan in preregistration_fixtures())
    complete, posthoc, missing_control, fixture_only, permissive = audits
    if (
        complete.verdict == "admissible_for_real_deployment_audit"
        and posthoc.verdict == "inadmissible_for_q1_upgrade"
        and missing_control.verdict == "inadmissible_for_q1_upgrade"
        and fixture_only.verdict == "inadmissible_for_q1_upgrade"
        and permissive.verdict == "inadmissible_for_q1_upgrade"
    ):
        strongest_claim = (
            "The detector branch now has a pre-data gate: a real deployment "
            "can only test Q1 if it fixes the T76 evidence schema, T77-safe "
            "policy corridor, negative controls, raw log sources, and demotion "
            "rule before the first event."
        )
    else:
        strongest_claim = (
            "The pre-registration gate failed to separate admissible real "
            "deployment audits from post hoc, fixture-only, or permissive "
            "control-leaking variants."
        )

    return T78Result(
        audits=audits,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "T78 weakens the detector branch by making T76/T77 insufficient "
            "for any further Q1 upgrade. Fixture counts, post hoc policy "
            "choice, missing unsigned controls, and permissive corridors are "
            "all rejected before D1 scoring."
        ),
        falsification_condition=(
            "Demote detector-level Q1 if no real deployment can satisfy this "
            "pre-data contract and still preserve signed recovery, unsigned "
            "withhold, and incomplete-pre-registration failure under the "
            "locked T76/T77 audit."
        ),
        q1_update=(
            "Keep Q1 partially supported only as a pre-registered, real-log "
            "detector-provenance protocol claim. Synthetic fixtures and "
            "post hoc policy selection cannot upgrade the detector branch."
        ),
        recommended_next=(
            "Populate the T78 contract from an actual detector run, then run "
            "the locked T76/T77 pipeline without changing the evidence fields "
            "or policy corridor."
        ),
        blocker=(
            "No real deployment log is present; T78 only defines the gate that "
            "future evidence must pass."
        ),
    )


def t78_result_to_dict(result: T78Result) -> dict[str, object]:
    return {
        "required_evidence_fields": list(REQUIRED_EVIDENCE_FIELDS),
        "required_control_roles": list(REQUIRED_CONTROL_ROLES),
        "required_raw_log_sources": list(REQUIRED_RAW_LOG_SOURCES),
        "t77_safe_corridor": {
            "confidence_floor_low_minimum": SAFE_CONFIDENCE_FLOOR_LOW,
            "max_false_risk_high_maximum": SAFE_FALSE_RISK_HIGH,
        },
        "audits": [
            {
                "plan_name": audit.plan_name,
                "verdict": audit.verdict,
                "missing_evidence_fields": list(audit.missing_evidence_fields),
                "missing_control_roles": list(audit.missing_control_roles),
                "missing_raw_log_sources": list(audit.missing_raw_log_sources),
                "failure_reasons": list(audit.failure_reasons),
                "next_allowed_audit": audit.next_allowed_audit,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "recommended_next": result.recommended_next,
        "blocker": result.blocker,
    }


def _missing(provided: frozenset[str], required: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(field for field in required if field not in provided)


def _policy_inside_t77_safe_corridor(policy: AuditPolicy) -> bool:
    return (
        policy.confidence_floor.low >= SAFE_CONFIDENCE_FLOOR_LOW
        and policy.max_false_risk.high <= SAFE_FALSE_RISK_HIGH
    )
