"""T87: real-run raw-log contract for the T86 detector branch.

T86 showed that perturbation response and signed DAG ancestry can rescue
ambiguous timing/tag fixtures, but only inside constructed counts. T87 defines
the event-level raw-log contract a real deployment must satisfy before those
counts may be populated.

This is an admission gate, not a D1 scorer and not detector dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.measured_detector_provenance_posterior import AuditPolicy
from models.preregistered_detector_deployment_protocol import (
    REQUIRED_CONTROL_ROLES,
    REQUIRED_EVIDENCE_FIELDS,
    REQUIRED_RAW_LOG_SOURCES,
    SAFE_CONFIDENCE_FLOOR_LOW,
    SAFE_FALSE_RISK_HIGH,
)
from models.provenance_protocol_monte_carlo import Range


REQUIRED_T86_CONTROL_ROLES: tuple[str, ...] = (
    "copied_record_control_pairs",
    "independent_record_control_pairs",
    "all_channels_ambiguous_negative_control",
    "clean_perturbation_only_positive_control",
    "backaction_perturbation_contamination_control",
    "clean_signed_dag_positive_control",
    "dag_truncation_false_edge_control",
)

REQUIRED_CHANNEL_ISOLATION_TESTS: tuple[str, ...] = (
    "perturbation_response",
    "signed_ancestry_dag",
)

REQUIRED_TABLE_COLUMNS: dict[str, tuple[str, ...]] = {
    "preregistration_manifest": (
        "run_id",
        "registered_at",
        "first_event_not_before",
        "policy_hash",
        "analysis_code_hash",
        "evidence_schema_hash",
        "demotion_rules_hash",
        "confidence_floor_low",
        "max_false_risk_high",
    ),
    "control_pair_manifest": (
        "pair_id",
        "role",
        "expected_relation",
        "local_record_id",
        "archive_record_id",
        "source_event_id",
        "timing_bin_id",
        "randomization_seed_commitment",
        "declared_before_event",
    ),
    "event_time_tag_stream": (
        "event_id",
        "detector_id",
        "local_time",
        "local_sigma",
        "archive_time",
        "archive_sigma",
        "batch_id",
        "batching_window",
        "timing_uncertainty_model_id",
    ),
    "signature_verification_log": (
        "event_id",
        "tag_id",
        "signature_id",
        "verification_result",
        "signer_key_id",
        "forgery_challenge_id",
        "spoof_challenge_id",
        "verification_timestamp",
    ),
    "tag_ambiguity_challenge_log": (
        "challenge_id",
        "event_id",
        "role",
        "retained_tag",
        "accepted_forged_tag",
        "accepted_spoofed_independent_tag",
        "unique_independent_tag",
        "verdict",
    ),
    "perturbation_trial_log": (
        "trial_id",
        "pair_id",
        "perturbed_record_id",
        "perturbation_type",
        "response_changed",
        "independent_false_change",
        "back_action_detected",
        "pre_trial_state_hash",
        "post_trial_state_hash",
    ),
    "ancestry_dag_edge_export": (
        "edge_id",
        "child_record_id",
        "parent_record_id",
        "edge_signature_id",
        "edge_verified",
        "export_snapshot_id",
        "truncation_flag",
        "false_shared_edge_challenge_id",
    ),
    "trust_boundary_audit_log": (
        "audit_id",
        "component",
        "boundary_type",
        "integrity_check_passed",
        "key_scope",
        "operator_id_hash",
        "audit_timestamp",
    ),
    "demotion_decision_log": (
        "run_id",
        "control_role",
        "demotion_condition",
        "triggered",
        "applied_before_d1",
        "reason",
    ),
}

TABLE_TO_T76_FIELDS: dict[str, tuple[str, ...]] = {
    "preregistration_manifest": ("pre_registered_threshold_coverage",),
    "event_time_tag_stream": ("local_sigma", "archive_sigma", "batching_window"),
    "signature_verification_log": (
        "tag_retention",
        "signature_verification",
        "accepted_forged_tags",
        "accepted_spoofed_independent_tags",
        "independent_unique_tags",
    ),
    "tag_ambiguity_challenge_log": (
        "tag_retention",
        "accepted_forged_tags",
        "accepted_spoofed_independent_tags",
        "independent_unique_tags",
    ),
    "perturbation_trial_log": (
        "dependent_perturbation_changes",
        "independent_perturbation_false_changes",
        "perturbation_back_action_events",
    ),
    "ancestry_dag_edge_export": (
        "dag_observability",
        "signed_dag_edges",
        "dag_truncation_events",
        "false_shared_dag_edges",
    ),
    "trust_boundary_audit_log": (
        "detector_boundary_integrity",
        "archive_boundary_integrity",
        "transport_boundary_integrity",
    ),
}


@dataclass(frozen=True)
class RawLogTable:
    name: str
    columns: frozenset[str]
    event_level: bool
    immutable_export: bool
    source: str
    purpose: str


@dataclass(frozen=True)
class RealRunRawLogContract:
    name: str
    registered_before_first_event: bool
    policy_registered_before_data: bool
    analysis_code_frozen: bool
    uses_real_raw_log: bool
    fixture_counts_only: bool
    declared_demote_on_control_leak: bool
    demotion_rules_registered_before_data: bool
    actual_class_labels_declared_before_data: bool
    linked_by_stable_event_ids: bool
    event_level_logs_public: bool
    policy: AuditPolicy
    evidence_fields: frozenset[str]
    t78_control_roles: frozenset[str]
    t86_control_roles: frozenset[str]
    raw_log_sources: frozenset[str]
    channel_isolation_tests: frozenset[str]
    raw_tables: tuple[RawLogTable, ...]
    threshold_fields_declared: int
    threshold_fields_required: int
    purpose: str


@dataclass(frozen=True)
class RawLogContractAudit:
    contract_name: str
    verdict: str
    missing_evidence_fields: tuple[str, ...]
    missing_t78_control_roles: tuple[str, ...]
    missing_t86_control_roles: tuple[str, ...]
    missing_raw_log_sources: tuple[str, ...]
    missing_channel_isolation_tests: tuple[str, ...]
    missing_tables: tuple[str, ...]
    missing_columns: tuple[str, ...]
    non_event_level_tables: tuple[str, ...]
    mutable_tables: tuple[str, ...]
    failure_reasons: tuple[str, ...]
    next_allowed_audit: str


@dataclass(frozen=True)
class T87Result:
    audits: tuple[RawLogContractAudit, ...]
    strongest_claim: str
    weakened_claim: str
    falsification_condition: str
    q1_update: str
    open_blocker: str
    recommended_next: str


def complete_t86_real_run_contract() -> RealRunRawLogContract:
    return RealRunRawLogContract(
        name="complete_t86_event_level_raw_log_contract",
        registered_before_first_event=True,
        policy_registered_before_data=True,
        analysis_code_frozen=True,
        uses_real_raw_log=True,
        fixture_counts_only=False,
        declared_demote_on_control_leak=True,
        demotion_rules_registered_before_data=True,
        actual_class_labels_declared_before_data=True,
        linked_by_stable_event_ids=True,
        event_level_logs_public=True,
        policy=AuditPolicy(),
        evidence_fields=frozenset(REQUIRED_EVIDENCE_FIELDS),
        t78_control_roles=frozenset(REQUIRED_CONTROL_ROLES),
        t86_control_roles=frozenset(REQUIRED_T86_CONTROL_ROLES),
        raw_log_sources=frozenset(REQUIRED_RAW_LOG_SOURCES),
        channel_isolation_tests=frozenset(REQUIRED_CHANNEL_ISOLATION_TESTS),
        raw_tables=_complete_raw_tables(),
        threshold_fields_declared=len(REQUIRED_EVIDENCE_FIELDS),
        threshold_fields_required=len(REQUIRED_EVIDENCE_FIELDS),
        purpose=(
            "A pre-data event-level deployment contract that can populate the "
            "T76/T86 evidence counts without changing the locked schema."
        ),
    )


def dashboard_only_summary_contract() -> RealRunRawLogContract:
    base = complete_t86_real_run_contract()
    summary = RawLogTable(
        name="dashboard_summary",
        columns=frozenset(
            {
                "run_id",
                "event_count",
                "mean_timing_sigma",
                "tag_retention_rate",
                "signature_pass_rate",
            }
        ),
        event_level=False,
        immutable_export=False,
        source="dashboard_export",
        purpose="A coarse run summary with no event-level provenance rows.",
    )
    return replace(
        base,
        name="dashboard_only_summary_control",
        uses_real_raw_log=False,
        fixture_counts_only=True,
        linked_by_stable_event_ids=False,
        event_level_logs_public=False,
        evidence_fields=frozenset({"local_sigma", "tag_retention"}),
        raw_log_sources=frozenset({"dashboard_export"}),
        raw_tables=(summary,),
        purpose=(
            "A dashboard-only export that resembles T79 and cannot instantiate "
            "the T86 ambiguous-tag tests."
        ),
    )


def missing_copied_independent_labels_contract() -> RealRunRawLogContract:
    base = complete_t86_real_run_contract()
    controls = set(REQUIRED_T86_CONTROL_ROLES)
    controls.remove("copied_record_control_pairs")
    controls.remove("independent_record_control_pairs")
    return replace(
        base,
        name="missing_copied_independent_control_labels",
        actual_class_labels_declared_before_data=False,
        t86_control_roles=frozenset(controls),
        purpose=(
            "A real-looking deployment with no pre-declared copied versus "
            "independent witness labels."
        ),
    )


def posthoc_policy_and_demotion_contract() -> RealRunRawLogContract:
    base = complete_t86_real_run_contract()
    return replace(
        base,
        name="posthoc_policy_and_demotion_control",
        policy_registered_before_data=False,
        declared_demote_on_control_leak=False,
        demotion_rules_registered_before_data=False,
        policy=AuditPolicy(
            confidence_floor=Range(0.65, 0.75),
            max_false_risk=Range(0.25, 0.35),
        ),
        threshold_fields_declared=len(REQUIRED_EVIDENCE_FIELDS) - 4,
        purpose=(
            "A complete-looking raw log whose policy corridor and demotion "
            "rules are chosen after inspecting the run."
        ),
    )


def dag_export_without_raw_edges_contract() -> RealRunRawLogContract:
    base = complete_t86_real_run_contract()
    tables = tuple(
        _remove_columns(
            table,
            {
                "parent_record_id",
                "edge_signature_id",
                "edge_verified",
                "truncation_flag",
                "false_shared_edge_challenge_id",
            },
        )
        if table.name == "ancestry_dag_edge_export"
        else table
        for table in base.raw_tables
    )
    return replace(
        base,
        name="dag_export_without_raw_edge_columns",
        raw_tables=tables,
        purpose=(
            "A deployment that claims DAG observability but exports only "
            "summary edge counts rather than signed raw edges."
        ),
    )


def unlinked_event_tables_contract() -> RealRunRawLogContract:
    base = complete_t86_real_run_contract()
    tables = tuple(
        replace(table, immutable_export=False)
        if table.name in {"perturbation_trial_log", "ancestry_dag_edge_export"}
        else table
        for table in base.raw_tables
    )
    return replace(
        base,
        name="unlinked_or_mutable_event_tables",
        linked_by_stable_event_ids=False,
        raw_tables=tables,
        purpose=(
            "A raw-log bundle whose main event tables cannot be joined by "
            "stable event identifiers and whose key exports remain mutable."
        ),
    )


def raw_log_contract_fixtures() -> tuple[RealRunRawLogContract, ...]:
    return (
        complete_t86_real_run_contract(),
        dashboard_only_summary_contract(),
        missing_copied_independent_labels_contract(),
        posthoc_policy_and_demotion_contract(),
        dag_export_without_raw_edges_contract(),
        unlinked_event_tables_contract(),
    )


def audit_raw_log_contract(contract: RealRunRawLogContract) -> RawLogContractAudit:
    table_by_name = {table.name: table for table in contract.raw_tables}
    missing_evidence = _missing(contract.evidence_fields, REQUIRED_EVIDENCE_FIELDS)
    missing_t78_controls = _missing(contract.t78_control_roles, REQUIRED_CONTROL_ROLES)
    missing_t86_controls = _missing(
        contract.t86_control_roles,
        REQUIRED_T86_CONTROL_ROLES,
    )
    missing_sources = _missing(contract.raw_log_sources, REQUIRED_RAW_LOG_SOURCES)
    missing_channel_tests = _missing(
        contract.channel_isolation_tests,
        REQUIRED_CHANNEL_ISOLATION_TESTS,
    )
    missing_tables = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if table_name not in table_by_name
    )
    missing_columns = _missing_columns(table_by_name)
    non_event_level = tuple(
        table.name
        for table in contract.raw_tables
        if table.name in REQUIRED_TABLE_COLUMNS and not table.event_level
    )
    mutable = tuple(
        table.name
        for table in contract.raw_tables
        if table.name in REQUIRED_TABLE_COLUMNS and not table.immutable_export
    )

    failures: list[str] = []
    if not contract.registered_before_first_event:
        failures.append("contract_not_registered_before_first_event")
    if not contract.policy_registered_before_data:
        failures.append("policy_chosen_after_data")
    if not contract.analysis_code_frozen:
        failures.append("analysis_code_not_frozen")
    if not contract.uses_real_raw_log:
        failures.append("no_real_raw_deployment_log")
    if contract.fixture_counts_only:
        failures.append("fixture_counts_only")
    if not contract.declared_demote_on_control_leak:
        failures.append("no_predeclared_demote_rule_for_control_leak")
    if not contract.demotion_rules_registered_before_data:
        failures.append("demotion_rules_chosen_after_data")
    if not contract.actual_class_labels_declared_before_data:
        failures.append("copied_independent_labels_not_preregistered")
    if not contract.linked_by_stable_event_ids:
        failures.append("raw_tables_not_joinable_by_stable_event_id")
    if not contract.event_level_logs_public:
        failures.append("event_level_logs_not_public_or_exportable")
    if missing_evidence:
        failures.append("missing_required_evidence_fields")
    if missing_t78_controls:
        failures.append("missing_t78_control_roles")
    if missing_t86_controls:
        failures.append("missing_t86_control_roles")
    if missing_sources:
        failures.append("missing_required_raw_log_sources")
    if missing_channel_tests:
        failures.append("missing_channel_isolation_tests")
    if missing_tables:
        failures.append("missing_required_raw_log_tables")
    if missing_columns:
        failures.append("missing_required_raw_log_columns")
    if non_event_level:
        failures.append("required_tables_not_event_level")
    if mutable:
        failures.append("required_tables_not_immutable_exports")
    if contract.threshold_fields_required <= 0:
        failures.append("invalid_threshold_field_count")
    elif contract.threshold_fields_declared < contract.threshold_fields_required:
        failures.append("incomplete_threshold_preregistration")
    if not _policy_inside_t77_safe_corridor(contract.policy):
        failures.append("policy_outside_t77_safe_corridor")

    verdict = (
        "admissible_for_t86_real_log_population"
        if not failures
        else "inadmissible_for_q1_upgrade"
    )
    next_allowed = (
        "populate_t76_t86_counts_without_schema_changes"
        if verdict == "admissible_for_t86_real_log_population"
        else "withhold_detector_q1_upgrade"
    )
    return RawLogContractAudit(
        contract_name=contract.name,
        verdict=verdict,
        missing_evidence_fields=missing_evidence,
        missing_t78_control_roles=missing_t78_controls,
        missing_t86_control_roles=missing_t86_controls,
        missing_raw_log_sources=missing_sources,
        missing_channel_isolation_tests=missing_channel_tests,
        missing_tables=missing_tables,
        missing_columns=missing_columns,
        non_event_level_tables=non_event_level,
        mutable_tables=mutable,
        failure_reasons=tuple(failures),
        next_allowed_audit=next_allowed,
    )


def run_t87_analysis() -> T87Result:
    audits = tuple(audit_raw_log_contract(contract) for contract in raw_log_contract_fixtures())
    complete = audits[0]
    if (
        complete.verdict == "admissible_for_t86_real_log_population"
        and all(audit.verdict == "inadmissible_for_q1_upgrade" for audit in audits[1:])
    ):
        strongest_claim = (
            "T87 turns T86's next-work item into a falsifiable admission "
            "contract: only pre-registered, event-level, joinable, immutable "
            "raw logs with copied/independent controls and isolated "
            "perturbation/DAG tests may populate the locked T76/T86 counts."
        )
    else:
        strongest_claim = (
            "The raw-log admission contract failed to separate a complete "
            "event-level deployment from dashboard, post hoc, unlabelled, or "
            "summary-DAG variants."
        )

    return T87Result(
        audits=audits,
        strongest_claim=strongest_claim,
        weakened_claim=(
            "T87 does not score D1, does not claim detector dynamics, and "
            "does not provide empirical support. It only specifies what a "
            "future detector deployment must log before Q1 can leave the "
            "fixture stage."
        ),
        falsification_condition=(
            "Demote the detector branch if no feasible deployment can publish "
            "these event-level tables before analysis, or if a complete raw "
            "log populates the locked T76/T86 adapter but loses the signed "
            "recovery, all-ambiguous withhold, perturbation/DAG rescue, or "
            "contaminated-control withhold separations."
        ),
        q1_update=(
            "Keep Q1 partially supported only as a pre-registered detector "
            "record admissibility protocol. A real ambiguous-tag deployment "
            "must first pass T87 before its counts can be treated as evidence; "
            "dashboard summaries, post hoc demotion rules, missing witness "
            "labels, and summary-only DAG exports withhold the detector branch."
        ),
        open_blocker=(
            "No actual detector event log is present. T87 supplies the table "
            "contract and rejection rules, but cannot populate the evidence "
            "counts or compare the result with decoherence/QD alternatives."
        ),
        recommended_next=(
            "Pick a concrete photon time-tagging or Stern-Gerlach readout "
            "stack, map each instrument export to the T87 tables, then run the "
            "locked T76/T86 scorer without adding fields or changing policy."
        ),
    )


def t87_result_to_dict(result: T87Result) -> dict[str, object]:
    return {
        "required_t86_control_roles": list(REQUIRED_T86_CONTROL_ROLES),
        "required_channel_isolation_tests": list(REQUIRED_CHANNEL_ISOLATION_TESTS),
        "required_raw_log_tables": {
            name: list(columns) for name, columns in REQUIRED_TABLE_COLUMNS.items()
        },
        "table_to_t76_fields": {
            name: list(fields) for name, fields in TABLE_TO_T76_FIELDS.items()
        },
        "audits": [
            {
                "contract_name": audit.contract_name,
                "verdict": audit.verdict,
                "missing_evidence_fields": list(audit.missing_evidence_fields),
                "missing_t78_control_roles": list(audit.missing_t78_control_roles),
                "missing_t86_control_roles": list(audit.missing_t86_control_roles),
                "missing_raw_log_sources": list(audit.missing_raw_log_sources),
                "missing_channel_isolation_tests": list(
                    audit.missing_channel_isolation_tests
                ),
                "missing_tables": list(audit.missing_tables),
                "missing_columns": list(audit.missing_columns),
                "non_event_level_tables": list(audit.non_event_level_tables),
                "mutable_tables": list(audit.mutable_tables),
                "failure_reasons": list(audit.failure_reasons),
                "next_allowed_audit": audit.next_allowed_audit,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _complete_raw_tables() -> tuple[RawLogTable, ...]:
    return tuple(
        RawLogTable(
            name=name,
            columns=frozenset(columns),
            event_level=True,
            immutable_export=True,
            source=_source_for_table(name),
            purpose=_purpose_for_table(name),
        )
        for name, columns in REQUIRED_TABLE_COLUMNS.items()
    )


def _source_for_table(table_name: str) -> str:
    return {
        "preregistration_manifest": "raw_time_tag_stream",
        "control_pair_manifest": "raw_time_tag_stream",
        "event_time_tag_stream": "raw_time_tag_stream",
        "signature_verification_log": "signature_verification_log",
        "tag_ambiguity_challenge_log": "signature_verification_log",
        "perturbation_trial_log": "perturbation_protocol_log",
        "ancestry_dag_edge_export": "ancestry_dag_export",
        "trust_boundary_audit_log": "trust_boundary_audit_log",
        "demotion_decision_log": "archive_receipt_chain",
    }[table_name]


def _purpose_for_table(table_name: str) -> str:
    return {
        "preregistration_manifest": "Freezes policy, schema, code, and demotion hashes.",
        "control_pair_manifest": "Declares copied and independent witness pairs.",
        "event_time_tag_stream": "Measures timing uncertainty and archive batching.",
        "signature_verification_log": "Records tag retention and signature challenge outcomes.",
        "tag_ambiguity_challenge_log": "Quantifies ambiguous, forged, and spoofed tags.",
        "perturbation_trial_log": "Separates dependent response from independent false changes.",
        "ancestry_dag_edge_export": "Exports signed ancestry edges and truncation challenges.",
        "trust_boundary_audit_log": "Measures detector, archive, and transport trust boundaries.",
        "demotion_decision_log": "Applies pre-registered withhold rules before D1 scoring.",
    }[table_name]


def _missing(provided: frozenset[str], required: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(field for field in required if field not in provided)


def _missing_columns(table_by_name: dict[str, RawLogTable]) -> tuple[str, ...]:
    missing: list[str] = []
    for table_name, required_columns in REQUIRED_TABLE_COLUMNS.items():
        table = table_by_name.get(table_name)
        if table is None:
            continue
        for column in required_columns:
            if column not in table.columns:
                missing.append(f"{table_name}.{column}")
    return tuple(missing)


def _remove_columns(table: RawLogTable, columns: set[str]) -> RawLogTable:
    return replace(table, columns=frozenset(table.columns - columns))


def _policy_inside_t77_safe_corridor(policy: AuditPolicy) -> bool:
    return (
        policy.confidence_floor.low >= SAFE_CONFIDENCE_FLOOR_LOW
        and policy.max_false_risk.high <= SAFE_FALSE_RISK_HIGH
    )
