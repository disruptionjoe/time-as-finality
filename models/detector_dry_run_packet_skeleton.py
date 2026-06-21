"""T97: locked dry-run packet skeleton for the detector raw-log route.

T96 showed that the surviving detector-side Q1 path is not carried by native
timing hardware. The next useful artifact is a concrete pre-data packet
skeleton: filenames, exact schemas, join keys, hash commitments, and control
roles that a lab must freeze before collecting events.

This module deliberately does not score D1 and does not create empirical
support. It checks whether the packet is a valid scaffold and blocks any attempt
to populate T76/T86 evidence counts from template rows.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import hashlib

from models.real_run_raw_log_contract import (
    REQUIRED_CHANNEL_ISOLATION_TESTS,
    REQUIRED_TABLE_COLUMNS,
    REQUIRED_T86_CONTROL_ROLES,
    RawLogTable,
    audit_raw_log_contract,
    complete_t86_real_run_contract,
)


JOIN_KEYS_BY_TABLE: dict[str, tuple[str, ...]] = {
    "preregistration_manifest": ("run_id",),
    "control_pair_manifest": ("pair_id", "source_event_id", "timing_bin_id"),
    "event_time_tag_stream": ("event_id", "batch_id"),
    "signature_verification_log": ("event_id", "tag_id"),
    "tag_ambiguity_challenge_log": ("challenge_id", "event_id"),
    "perturbation_trial_log": ("trial_id", "pair_id"),
    "ancestry_dag_edge_export": (
        "edge_id",
        "child_record_id",
        "parent_record_id",
    ),
    "trust_boundary_audit_log": ("audit_id", "component"),
    "demotion_decision_log": ("run_id", "control_role"),
}

MIN_PLANNED_ROWS_BY_TABLE: dict[str, int] = {
    "preregistration_manifest": 1,
    "control_pair_manifest": len(REQUIRED_T86_CONTROL_ROLES),
    "event_time_tag_stream": 1,
    "signature_verification_log": 1,
    "tag_ambiguity_challenge_log": 4,
    "perturbation_trial_log": 4,
    "ancestry_dag_edge_export": 1,
    "trust_boundary_audit_log": 5,
    "demotion_decision_log": len(REQUIRED_T86_CONTROL_ROLES),
}


@dataclass(frozen=True)
class DryRunTableSpec:
    table_name: str
    file_name: str
    columns: frozenset[str]
    join_keys: tuple[str, ...]
    row_state: str
    min_planned_rows: int
    real_rows_present: bool
    locked_before_first_event: bool
    immutable_export: bool
    schema_hash: str
    export_checksum: str
    purpose: str


@dataclass(frozen=True)
class DetectorDryRunPacket:
    name: str
    run_id: str
    registered_at: str
    first_event_not_before: str
    policy_hash: str
    analysis_code_hash: str
    evidence_schema_hash: str
    demotion_rules_hash: str
    manifest_hash: str
    tables: tuple[DryRunTableSpec, ...]
    declared_t86_control_roles: frozenset[str]
    channel_isolation_tests: frozenset[str]
    attempt_to_populate_counts: bool
    no_data_analyzed: bool
    purpose: str


@dataclass(frozen=True)
class DryRunPacketAudit:
    packet_name: str
    verdict: str
    evidence_verdict: str
    missing_tables: tuple[str, ...]
    missing_columns: tuple[str, ...]
    extra_columns: tuple[str, ...]
    unlocked_tables: tuple[str, ...]
    mutable_tables: tuple[str, ...]
    unjoinable_tables: tuple[str, ...]
    missing_control_roles: tuple[str, ...]
    missing_channel_isolation_tests: tuple[str, ...]
    placeholder_tables: tuple[str, ...]
    real_row_tables: tuple[str, ...]
    failure_reasons: tuple[str, ...]
    t87_verdict_if_scored_now: str
    t87_failure_reasons_if_scored_now: tuple[str, ...]
    next_allowed_step: str


@dataclass(frozen=True)
class T97Result:
    audits: tuple[DryRunPacketAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def locked_detector_dry_run_packet_skeleton() -> DetectorDryRunPacket:
    """Schema-complete pre-data packet with no real event rows yet."""

    tables = tuple(_table_spec(table_name) for table_name in REQUIRED_TABLE_COLUMNS)
    policy_hash = _digest("t97-policy-v0.1")
    analysis_hash = _digest("t97-analysis-code-v0.1")
    schema_hash = _digest(
        "|".join(
            f"{table}:{','.join(REQUIRED_TABLE_COLUMNS[table])}"
            for table in REQUIRED_TABLE_COLUMNS
        )
    )
    demotion_hash = _digest("t97-predata-demotion-rules-v0.1")
    return _packet(
        name="locked_t97_detector_dry_run_packet_skeleton",
        tables=tables,
        policy_hash=policy_hash,
        analysis_code_hash=analysis_hash,
        evidence_schema_hash=schema_hash,
        demotion_rules_hash=demotion_hash,
        declared_t86_control_roles=frozenset(REQUIRED_T86_CONTROL_ROLES),
        channel_isolation_tests=frozenset(REQUIRED_CHANNEL_ISOLATION_TESTS),
        attempt_to_populate_counts=False,
        no_data_analyzed=True,
        purpose=(
            "A frozen packet scaffold for the T87 detector route. It supplies "
            "schemas, filenames, join keys, and hashes, but no detector event "
            "rows and no T76/T86 counts."
        ),
    )


def placeholder_population_attempt_packet() -> DetectorDryRunPacket:
    base = locked_detector_dry_run_packet_skeleton()
    return replace(
        base,
        name="placeholder_population_attempt_packet",
        manifest_hash=_manifest_hash(
            base.tables,
            base.policy_hash,
            base.analysis_code_hash,
            base.evidence_schema_hash,
            base.demotion_rules_hash,
            "placeholder_population_attempt_packet",
        ),
        attempt_to_populate_counts=True,
        purpose=(
            "A hostile control: the packet is structurally complete but tries "
            "to populate evidence counts from template rows."
        ),
    )


def schema_drift_packet() -> DetectorDryRunPacket:
    base = locked_detector_dry_run_packet_skeleton()
    drifted = _replace_table(
        base.tables,
        _table_spec(
            "event_time_tag_stream",
            extra_columns=("operator_note",),
        ),
    )
    return _packet(
        name="schema_drift_dry_run_packet",
        tables=drifted,
        policy_hash=base.policy_hash,
        analysis_code_hash=base.analysis_code_hash,
        evidence_schema_hash=base.evidence_schema_hash,
        demotion_rules_hash=base.demotion_rules_hash,
        declared_t86_control_roles=base.declared_t86_control_roles,
        channel_isolation_tests=base.channel_isolation_tests,
        attempt_to_populate_counts=False,
        no_data_analyzed=True,
        purpose=(
            "A complete-looking packet with an unregistered timing-stream "
            "column, testing schema drift before data collection."
        ),
    )


def posthoc_packet_skeleton() -> DetectorDryRunPacket:
    base = locked_detector_dry_run_packet_skeleton()
    unlocked = tuple(
        replace(table, locked_before_first_event=False) for table in base.tables
    )
    return _packet(
        name="posthoc_detector_packet_skeleton",
        tables=unlocked,
        policy_hash=base.policy_hash,
        analysis_code_hash=base.analysis_code_hash,
        evidence_schema_hash=base.evidence_schema_hash,
        demotion_rules_hash=base.demotion_rules_hash,
        declared_t86_control_roles=base.declared_t86_control_roles,
        channel_isolation_tests=base.channel_isolation_tests,
        attempt_to_populate_counts=False,
        no_data_analyzed=False,
        purpose=(
            "A complete schema assembled after data access, testing the "
            "pre-registration boundary."
        ),
    )


def missing_control_roles_packet() -> DetectorDryRunPacket:
    base = locked_detector_dry_run_packet_skeleton()
    roles = set(REQUIRED_T86_CONTROL_ROLES)
    roles.remove("all_channels_ambiguous_negative_control")
    roles.remove("dag_truncation_false_edge_control")
    return replace(
        base,
        name="missing_ambiguous_and_dag_control_roles_packet",
        declared_t86_control_roles=frozenset(roles),
        manifest_hash=_manifest_hash(
            base.tables,
            base.policy_hash,
            base.analysis_code_hash,
            base.evidence_schema_hash,
            base.demotion_rules_hash,
            "missing_ambiguous_and_dag_control_roles_packet",
        ),
        purpose=(
            "A packet with exact tables but without the hostile T86 ambiguity "
            "and DAG contamination controls."
        ),
    )


def dry_run_packet_fixtures() -> tuple[DetectorDryRunPacket, ...]:
    return (
        locked_detector_dry_run_packet_skeleton(),
        placeholder_population_attempt_packet(),
        schema_drift_packet(),
        posthoc_packet_skeleton(),
        missing_control_roles_packet(),
    )


def audit_detector_dry_run_packet(
    packet: DetectorDryRunPacket,
) -> DryRunPacketAudit:
    table_by_name = {table.table_name: table for table in packet.tables}

    missing_tables = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if table_name not in table_by_name
    )
    missing_columns: list[str] = []
    extra_columns: list[str] = []
    for table_name, required_columns in REQUIRED_TABLE_COLUMNS.items():
        table = table_by_name.get(table_name)
        if table is None:
            continue
        required = set(required_columns)
        provided = set(table.columns)
        missing_columns.extend(
            f"{table_name}.{column}" for column in required_columns if column not in provided
        )
        extra_columns.extend(
            f"{table_name}.{column}"
            for column in sorted(provided - required)
        )

    unlocked_tables = tuple(
        table.table_name for table in packet.tables if not table.locked_before_first_event
    )
    mutable_tables = tuple(
        table.table_name for table in packet.tables if not table.immutable_export
    )
    unjoinable_tables = tuple(
        table.table_name
        for table in packet.tables
        if not _has_required_join_keys(table)
    )
    missing_control_roles = tuple(
        role
        for role in REQUIRED_T86_CONTROL_ROLES
        if role not in packet.declared_t86_control_roles
    )
    missing_channel_tests = tuple(
        test
        for test in REQUIRED_CHANNEL_ISOLATION_TESTS
        if test not in packet.channel_isolation_tests
    )
    placeholder_tables = tuple(
        table.table_name
        for table in packet.tables
        if table.table_name in REQUIRED_TABLE_COLUMNS and not table.real_rows_present
    )
    real_row_tables = tuple(
        table.table_name
        for table in packet.tables
        if table.table_name in REQUIRED_TABLE_COLUMNS and table.real_rows_present
    )

    failure_reasons: list[str] = []
    if missing_tables:
        failure_reasons.append("missing_required_t87_tables")
    if missing_columns:
        failure_reasons.append("missing_required_t87_columns")
    if extra_columns:
        failure_reasons.append("unregistered_schema_columns")
    if unlocked_tables:
        failure_reasons.append("packet_not_locked_before_first_event")
    if mutable_tables:
        failure_reasons.append("exports_not_immutable")
    if unjoinable_tables:
        failure_reasons.append("tables_missing_declared_join_keys")
    if missing_control_roles:
        failure_reasons.append("missing_t86_control_roles")
    if missing_channel_tests:
        failure_reasons.append("missing_channel_isolation_tests")
    if not packet.no_data_analyzed:
        failure_reasons.append("data_accessed_before_packet_lock")
    if not _hashes_are_well_formed(packet):
        failure_reasons.append("malformed_hash_commitments")
    if packet.manifest_hash != _expected_manifest_hash(packet):
        failure_reasons.append("manifest_hash_mismatch")
    if packet.attempt_to_populate_counts and placeholder_tables:
        failure_reasons.append("attempts_to_populate_counts_from_placeholders")

    t87_audit = audit_raw_log_contract(_t87_contract_view(packet))
    all_real_rows = set(real_row_tables) == set(REQUIRED_TABLE_COLUMNS)
    if failure_reasons:
        verdict = "inadmissible_dry_run_packet"
        evidence_verdict = "withhold_detector_q1_upgrade"
        next_allowed = "repair_packet_before_collection"
    elif all_real_rows:
        verdict = "ready_for_t87_real_log_population"
        evidence_verdict = "eligible_for_locked_t76_t86_population"
        next_allowed = "run_t87_then_locked_t76_t86_without_schema_changes"
    else:
        verdict = "schema_complete_predata_scaffold_only"
        evidence_verdict = "withhold_detector_q1_upgrade"
        next_allowed = "collect_real_rows_without_schema_or_policy_changes"

    return DryRunPacketAudit(
        packet_name=packet.name,
        verdict=verdict,
        evidence_verdict=evidence_verdict,
        missing_tables=missing_tables,
        missing_columns=tuple(missing_columns),
        extra_columns=tuple(extra_columns),
        unlocked_tables=unlocked_tables,
        mutable_tables=mutable_tables,
        unjoinable_tables=unjoinable_tables,
        missing_control_roles=missing_control_roles,
        missing_channel_isolation_tests=missing_channel_tests,
        placeholder_tables=placeholder_tables,
        real_row_tables=real_row_tables,
        failure_reasons=tuple(failure_reasons),
        t87_verdict_if_scored_now=t87_audit.verdict,
        t87_failure_reasons_if_scored_now=t87_audit.failure_reasons,
        next_allowed_step=next_allowed,
    )


def run_t97_analysis() -> T97Result:
    audits = tuple(audit_detector_dry_run_packet(packet) for packet in dry_run_packet_fixtures())
    locked, placeholder, drift, posthoc, missing_controls = audits
    expected_shape = (
        locked.verdict == "schema_complete_predata_scaffold_only"
        and locked.t87_failure_reasons_if_scored_now == ("no_real_raw_deployment_log",)
        and placeholder.verdict == "inadmissible_dry_run_packet"
        and drift.verdict == "inadmissible_dry_run_packet"
        and posthoc.verdict == "inadmissible_dry_run_packet"
        and missing_controls.verdict == "inadmissible_dry_run_packet"
    )
    strongest = (
        "A detector-side Q1 dry-run packet can now be specified without "
        "schema ambiguity, but it remains only a pre-data scaffold. T87 would "
        "still reject it as evidence until real event rows replace template "
        "exports without changing schema, policy, demotion rules, or control "
        "roles."
        if expected_shape
        else "The dry-run packet audit failed to separate a locked scaffold "
        "from placeholder, schema-drift, post hoc, or missing-control variants."
    )
    return T97Result(
        audits=audits,
        strongest_claim=strongest,
        improved=(
            "T97 turns the T96 next-work item into a concrete, reviewable "
            "packet skeleton: every T87 table has an exact schema, file name, "
            "join key, schema hash, export checksum, and pre-data role. A lab "
            "can now fail the detector route by failing to freeze this packet "
            "before the first event."
        ),
        weakened=(
            "This weakens detector-side Q1 again. The route is no longer "
            "blocked by vague schema design; it is blocked by actual pre-data "
            "execution and real event-row population. Template rows, post hoc "
            "schema drift, and missing hostile controls do not upgrade Q1."
        ),
        falsification_condition=(
            "Demote the detector branch if a realistic lab workflow cannot "
            "freeze the T97 packet before event collection, or if the filled "
            "packet cannot pass T87 and preserve the T86 signed-DAG, "
            "perturbation, ambiguous-control, and contaminated-control "
            "separations under the locked schema."
        ),
        q1_update=(
            "Q1 remains partially supported only as a detector-record "
            "admissibility protocol. T97 supplies a pre-data dry-run scaffold, "
            "not evidence; detector-side Q1 still withholds until real rows "
            "populate the locked packet and pass T87 before T76/T86 scoring."
        ),
        claim_ledger_update=(
            "Add T97 to Q1 as a further narrowing: the detector branch has a "
            "schema-complete dry-run packet skeleton, but the strongest "
            "current claim is only that reviewers can check pre-data packet "
            "freezing. Placeholder rows, schema drift, post hoc packets, and "
            "missing hostile controls falsify any attempted detector upgrade."
        ),
        open_blocker=(
            "No actual detector event rows have been collected under the "
            "locked packet. The live blocker is operational: freeze the "
            "packet before first event, then fill it without schema changes."
        ),
        recommended_next=(
            "Instantiate the T97 packet in a real lab dry run with empty "
            "files, signed manifests, immutable export points, and operator "
            "handoff checks. If the lab cannot do that pre-data, demote the "
            "detector route below the active Q1 frontier."
        ),
    )


def t97_result_to_dict(result: T97Result) -> dict[str, object]:
    return {
        "audits": [
            {
                "packet_name": audit.packet_name,
                "verdict": audit.verdict,
                "evidence_verdict": audit.evidence_verdict,
                "missing_tables": list(audit.missing_tables),
                "missing_columns": list(audit.missing_columns),
                "extra_columns": list(audit.extra_columns),
                "unlocked_tables": list(audit.unlocked_tables),
                "mutable_tables": list(audit.mutable_tables),
                "unjoinable_tables": list(audit.unjoinable_tables),
                "missing_control_roles": list(audit.missing_control_roles),
                "missing_channel_isolation_tests": list(
                    audit.missing_channel_isolation_tests
                ),
                "placeholder_tables": list(audit.placeholder_tables),
                "real_row_tables": list(audit.real_row_tables),
                "failure_reasons": list(audit.failure_reasons),
                "t87_verdict_if_scored_now": audit.t87_verdict_if_scored_now,
                "t87_failure_reasons_if_scored_now": list(
                    audit.t87_failure_reasons_if_scored_now
                ),
                "next_allowed_step": audit.next_allowed_step,
            }
            for audit in result.audits
        ],
        "required_t87_tables": {
            table_name: list(columns)
            for table_name, columns in REQUIRED_TABLE_COLUMNS.items()
        },
        "required_t86_control_roles": list(REQUIRED_T86_CONTROL_ROLES),
        "required_channel_isolation_tests": list(REQUIRED_CHANNEL_ISOLATION_TESTS),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def packet_manifest_to_dict(packet: DetectorDryRunPacket) -> dict[str, object]:
    return {
        "name": packet.name,
        "run_id": packet.run_id,
        "registered_at": packet.registered_at,
        "first_event_not_before": packet.first_event_not_before,
        "policy_hash": packet.policy_hash,
        "analysis_code_hash": packet.analysis_code_hash,
        "evidence_schema_hash": packet.evidence_schema_hash,
        "demotion_rules_hash": packet.demotion_rules_hash,
        "manifest_hash": packet.manifest_hash,
        "declared_t86_control_roles": sorted(packet.declared_t86_control_roles),
        "channel_isolation_tests": sorted(packet.channel_isolation_tests),
        "attempt_to_populate_counts": packet.attempt_to_populate_counts,
        "no_data_analyzed": packet.no_data_analyzed,
        "tables": [
            {
                "table_name": table.table_name,
                "file_name": table.file_name,
                "columns": _ordered_columns(table),
                "join_keys": list(table.join_keys),
                "row_state": table.row_state,
                "min_planned_rows": table.min_planned_rows,
                "real_rows_present": table.real_rows_present,
                "locked_before_first_event": table.locked_before_first_event,
                "immutable_export": table.immutable_export,
                "schema_hash": table.schema_hash,
                "export_checksum": table.export_checksum,
                "purpose": table.purpose,
            }
            for table in packet.tables
        ],
        "purpose": packet.purpose,
    }


def _table_spec(
    table_name: str,
    *,
    extra_columns: tuple[str, ...] = (),
    drop_columns: tuple[str, ...] = (),
) -> DryRunTableSpec:
    base_columns = tuple(
        column
        for column in REQUIRED_TABLE_COLUMNS[table_name]
        if column not in set(drop_columns)
    )
    columns = base_columns + extra_columns
    schema_hash = _digest(f"{table_name}|{','.join(columns)}")
    export_checksum = _digest(
        "empty-export|"
        f"{table_name}|{schema_hash}|{MIN_PLANNED_ROWS_BY_TABLE[table_name]}"
    )
    return DryRunTableSpec(
        table_name=table_name,
        file_name=f"dry-run/t97/{table_name}.jsonl",
        columns=frozenset(columns),
        join_keys=JOIN_KEYS_BY_TABLE[table_name],
        row_state="planned_template_rows_only",
        min_planned_rows=MIN_PLANNED_ROWS_BY_TABLE[table_name],
        real_rows_present=False,
        locked_before_first_event=True,
        immutable_export=True,
        schema_hash=schema_hash,
        export_checksum=export_checksum,
        purpose=_purpose_for_table(table_name),
    )


def _packet(
    *,
    name: str,
    tables: tuple[DryRunTableSpec, ...],
    policy_hash: str,
    analysis_code_hash: str,
    evidence_schema_hash: str,
    demotion_rules_hash: str,
    declared_t86_control_roles: frozenset[str],
    channel_isolation_tests: frozenset[str],
    attempt_to_populate_counts: bool,
    no_data_analyzed: bool,
    purpose: str,
) -> DetectorDryRunPacket:
    return DetectorDryRunPacket(
        name=name,
        run_id="t97-dry-run-0001",
        registered_at="2026-06-20T00:00:00Z",
        first_event_not_before="2026-06-21T00:00:00Z",
        policy_hash=policy_hash,
        analysis_code_hash=analysis_code_hash,
        evidence_schema_hash=evidence_schema_hash,
        demotion_rules_hash=demotion_rules_hash,
        manifest_hash=_manifest_hash(
            tables,
            policy_hash,
            analysis_code_hash,
            evidence_schema_hash,
            demotion_rules_hash,
            name,
        ),
        tables=tables,
        declared_t86_control_roles=declared_t86_control_roles,
        channel_isolation_tests=channel_isolation_tests,
        attempt_to_populate_counts=attempt_to_populate_counts,
        no_data_analyzed=no_data_analyzed,
        purpose=purpose,
    )


def _replace_table(
    tables: tuple[DryRunTableSpec, ...],
    replacement: DryRunTableSpec,
) -> tuple[DryRunTableSpec, ...]:
    return tuple(
        replacement if table.table_name == replacement.table_name else table
        for table in tables
    )


def _has_required_join_keys(table: DryRunTableSpec) -> bool:
    expected = JOIN_KEYS_BY_TABLE.get(table.table_name, ())
    return all(key in table.columns for key in expected)


def _ordered_columns(table: DryRunTableSpec) -> list[str]:
    required = list(REQUIRED_TABLE_COLUMNS.get(table.table_name, ()))
    extras = sorted(column for column in table.columns if column not in required)
    return [column for column in required if column in table.columns] + extras


def _hashes_are_well_formed(packet: DetectorDryRunPacket) -> bool:
    hashes = (
        packet.policy_hash,
        packet.analysis_code_hash,
        packet.evidence_schema_hash,
        packet.demotion_rules_hash,
        packet.manifest_hash,
        *(table.schema_hash for table in packet.tables),
        *(table.export_checksum for table in packet.tables),
    )
    return all(len(value) == 64 and all(char in "0123456789abcdef" for char in value) for value in hashes)


def _expected_manifest_hash(packet: DetectorDryRunPacket) -> str:
    return _manifest_hash(
        packet.tables,
        packet.policy_hash,
        packet.analysis_code_hash,
        packet.evidence_schema_hash,
        packet.demotion_rules_hash,
        packet.name,
    )


def _manifest_hash(
    tables: tuple[DryRunTableSpec, ...],
    policy_hash: str,
    analysis_code_hash: str,
    evidence_schema_hash: str,
    demotion_rules_hash: str,
    packet_name: str,
) -> str:
    table_lines = [
        "|".join(
            (
                table.table_name,
                table.file_name,
                ",".join(sorted(table.columns)),
                ",".join(table.join_keys),
                table.schema_hash,
                table.export_checksum,
            )
        )
        for table in tables
    ]
    payload = "\n".join(
        (
            packet_name,
            policy_hash,
            analysis_code_hash,
            evidence_schema_hash,
            demotion_rules_hash,
            *table_lines,
        )
    )
    return _digest(payload)


def _t87_contract_view(packet: DetectorDryRunPacket):
    all_real_rows = all(
        table.real_rows_present for table in packet.tables if table.table_name in REQUIRED_TABLE_COLUMNS
    )
    return replace(
        complete_t86_real_run_contract(),
        name=f"{packet.name}_t87_view",
        uses_real_raw_log=all_real_rows,
        fixture_counts_only=packet.attempt_to_populate_counts,
        registered_before_first_event=all(
            table.locked_before_first_event for table in packet.tables
        ),
        policy_registered_before_data=packet.no_data_analyzed,
        analysis_code_frozen=packet.no_data_analyzed,
        demotion_rules_registered_before_data=packet.no_data_analyzed,
        actual_class_labels_declared_before_data=(
            not _missing_roles(packet.declared_t86_control_roles)
        ),
        linked_by_stable_event_ids=all(_has_required_join_keys(table) for table in packet.tables),
        event_level_logs_public=True,
        t86_control_roles=packet.declared_t86_control_roles,
        channel_isolation_tests=packet.channel_isolation_tests,
        raw_tables=tuple(
            RawLogTable(
                name=table.table_name,
                columns=table.columns,
                event_level=True,
                immutable_export=table.immutable_export,
                source=table.file_name,
                purpose=table.purpose,
            )
            for table in packet.tables
        ),
    )


def _missing_roles(provided: frozenset[str]) -> tuple[str, ...]:
    return tuple(role for role in REQUIRED_T86_CONTROL_ROLES if role not in provided)


def _digest(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _purpose_for_table(table_name: str) -> str:
    return {
        "preregistration_manifest": (
            "Freeze run id, first-event bound, policy, code, schema, and "
            "demotion hashes."
        ),
        "control_pair_manifest": (
            "Declare copied, independent, ambiguous, perturbation, and DAG "
            "control roles before events."
        ),
        "event_time_tag_stream": (
            "Reserve the native event timing stream and stable event ids."
        ),
        "signature_verification_log": (
            "Reserve event-level signature and spoof/forgery challenge exports."
        ),
        "tag_ambiguity_challenge_log": (
            "Reserve rows for retained, forged, spoofed, and unique tag controls."
        ),
        "perturbation_trial_log": (
            "Reserve rows for perturbation-only and back-action controls."
        ),
        "ancestry_dag_edge_export": (
            "Reserve signed raw ancestry edges and DAG contamination controls."
        ),
        "trust_boundary_audit_log": (
            "Reserve detector, archive, transport, key, and operator boundary audits."
        ),
        "demotion_decision_log": (
            "Reserve pre-D1 demotion decisions for each hostile control role."
        ),
    }[table_name]
