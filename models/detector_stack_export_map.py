"""T95: map a named detector stack to the T87 raw-log contract.

T87 says which event-level tables a real detector deployment must publish before
the Q1 detector branch may populate the locked T76/T86 counts. T95 asks a
narrower feasibility question: does the named photon time-tagging stack already
export those tables, or does it require custom pre-registered middleware?

This is not a D1 scorer and not empirical support. It is an admission map for
one candidate deployment packet.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS


@dataclass(frozen=True)
class TableExport:
    table_name: str
    component: str
    provided_columns: frozenset[str]
    instrument_native: bool
    event_level: bool
    immutable_export: bool
    preregistered_before_data: bool
    stable_event_ids: bool
    purpose: str


@dataclass(frozen=True)
class DetectorStackExportMap:
    name: str
    stack: str
    table_exports: tuple[TableExport, ...]
    pre_data_plan: bool
    real_event_rows_present: bool
    locked_to_t87_schema: bool
    purpose: str


@dataclass(frozen=True)
class ExportMapAudit:
    map_name: str
    verdict: str
    missing_tables: tuple[str, ...]
    missing_columns: tuple[str, ...]
    non_event_level_tables: tuple[str, ...]
    mutable_tables: tuple[str, ...]
    posthoc_tables: tuple[str, ...]
    unjoinable_tables: tuple[str, ...]
    instrument_native_tables: tuple[str, ...]
    middleware_required_tables: tuple[str, ...]
    failure_reasons: tuple[str, ...]
    next_allowed_audit: str


@dataclass(frozen=True)
class T95Result:
    audits: tuple[ExportMapAudit, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    open_blocker: str
    recommended_next: str


def hydraharp_white_rabbit_native_timing_only_map() -> DetectorStackExportMap:
    """Native timing export without the archive/control middleware."""

    return DetectorStackExportMap(
        name="hydraharp_white_rabbit_native_timing_only",
        stack="HydraHarp time tags plus White Rabbit synchronization",
        table_exports=(
            TableExport(
                table_name="event_time_tag_stream",
                component="time_tagger_and_sync_fabric",
                provided_columns=frozenset(
                    {
                        "event_id",
                        "detector_id",
                        "local_time",
                        "local_sigma",
                        "archive_time",
                        "archive_sigma",
                    }
                ),
                instrument_native=True,
                event_level=True,
                immutable_export=True,
                preregistered_before_data=True,
                stable_event_ids=True,
                purpose=(
                    "Native detector timing and synchronized timestamp export; "
                    "does not provide provenance controls."
                ),
            ),
        ),
        pre_data_plan=True,
        real_event_rows_present=False,
        locked_to_t87_schema=False,
        purpose=(
            "A timing-only deployment that tests whether the named hardware is "
            "sufficient without signed archive and control middleware."
        ),
    )


def signed_archive_without_controls_map() -> DetectorStackExportMap:
    """Signed archive layer added, but no T87 controls or perturbation tests."""

    return DetectorStackExportMap(
        name="signed_archive_without_control_packet",
        stack="HydraHarp + White Rabbit + signed hash-chain archive",
        table_exports=(
            _complete_export(
                "event_time_tag_stream",
                "time_tagger_and_sync_fabric",
                instrument_native=True,
                purpose="Event timing stream with batch fields supplied by logger.",
            ),
            _complete_export(
                "signature_verification_log",
                "signed_archive",
                purpose="Signature verification results for event batches.",
            ),
            _complete_export(
                "ancestry_dag_edge_export",
                "hash_chain_archive",
                purpose="Hash-chain ancestry edges for copied archive records.",
            ),
            _complete_export(
                "trust_boundary_audit_log",
                "lab_boundary_audit",
                purpose="Operator, key-scope, detector, transport, and archive checks.",
            ),
        ),
        pre_data_plan=True,
        real_event_rows_present=False,
        locked_to_t87_schema=False,
        purpose=(
            "The T75 stack with signed archive evidence but without the "
            "pre-registered copied/independent controls required by T87."
        ),
    )


def augmented_preregistered_time_tagging_plan() -> DetectorStackExportMap:
    """Full export map for a future deployment packet, with no real rows yet."""

    return DetectorStackExportMap(
        name="augmented_preregistered_time_tagging_plan",
        stack=(
            "HydraHarp + White Rabbit + signed hash-chain archive + "
            "pre-registered control middleware"
        ),
        table_exports=tuple(
            _complete_export(
                table_name,
                component=_component_for_table(table_name),
                instrument_native=(table_name == "event_time_tag_stream"),
                purpose=_purpose_for_table(table_name),
            )
            for table_name in REQUIRED_TABLE_COLUMNS
        ),
        pre_data_plan=True,
        real_event_rows_present=False,
        locked_to_t87_schema=True,
        purpose=(
            "A complete pre-data deployment map showing which concrete stack "
            "component must export each T87 table before any Q1 scoring."
        ),
    )


def posthoc_augmented_time_tagging_map() -> DetectorStackExportMap:
    base = augmented_preregistered_time_tagging_plan()
    return replace(
        base,
        name="posthoc_augmented_time_tagging_map",
        table_exports=tuple(
            replace(export, preregistered_before_data=False)
            for export in base.table_exports
        ),
        pre_data_plan=False,
        purpose=(
            "A complete-looking export packet assembled after data collection."
        ),
    )


def dashboard_summary_export_map() -> DetectorStackExportMap:
    return DetectorStackExportMap(
        name="dashboard_summary_export_map",
        stack="coarse run dashboard",
        table_exports=(
            TableExport(
                table_name="dashboard_summary",
                component="operator_dashboard",
                provided_columns=frozenset(
                    {
                        "run_id",
                        "event_count",
                        "mean_timing_sigma",
                        "signature_pass_rate",
                    }
                ),
                instrument_native=False,
                event_level=False,
                immutable_export=False,
                preregistered_before_data=False,
                stable_event_ids=False,
                purpose="A dashboard export with no event-level provenance rows.",
            ),
        ),
        pre_data_plan=False,
        real_event_rows_present=True,
        locked_to_t87_schema=False,
        purpose="A coarse summary control matching the T79/T87 rejection path.",
    )


def detector_stack_export_map_fixtures() -> tuple[DetectorStackExportMap, ...]:
    return (
        hydraharp_white_rabbit_native_timing_only_map(),
        signed_archive_without_controls_map(),
        augmented_preregistered_time_tagging_plan(),
        posthoc_augmented_time_tagging_map(),
        dashboard_summary_export_map(),
    )


def audit_detector_stack_export_map(
    export_map: DetectorStackExportMap,
) -> ExportMapAudit:
    exports_by_table: dict[str, list[TableExport]] = {}
    for table_export in export_map.table_exports:
        exports_by_table.setdefault(table_export.table_name, []).append(table_export)

    missing_tables = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if table_name not in exports_by_table
    )
    missing_columns = _missing_columns(exports_by_table)
    non_event_level = _tables_failing(exports_by_table, "event_level")
    mutable = _tables_failing(exports_by_table, "immutable_export")
    posthoc = _tables_failing(exports_by_table, "preregistered_before_data")
    unjoinable = _tables_failing(exports_by_table, "stable_event_ids")
    instrument_native = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if any(
            export.instrument_native
            for export in exports_by_table.get(table_name, ())
        )
    )
    middleware_required = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if table_name in exports_by_table and table_name not in instrument_native
    )

    failures: list[str] = []
    if not export_map.pre_data_plan:
        failures.append("not_a_pre_data_deployment_plan")
    if not export_map.locked_to_t87_schema:
        failures.append("not_locked_to_t87_schema")
    if missing_tables:
        failures.append("missing_required_t87_tables")
    if missing_columns:
        failures.append("missing_required_t87_columns")
    if non_event_level:
        failures.append("required_tables_not_event_level")
    if mutable:
        failures.append("required_tables_not_immutable_exports")
    if posthoc:
        failures.append("required_tables_not_preregistered")
    if unjoinable:
        failures.append("required_tables_not_joinable")

    if failures:
        verdict = "inadmissible_for_detector_q1_upgrade"
        next_allowed = "withhold_detector_q1_upgrade"
    elif export_map.real_event_rows_present:
        verdict = "admissible_for_t87_population"
        next_allowed = "populate_locked_t76_t86_counts"
    else:
        verdict = "admissible_as_preregistered_deployment_plan_only"
        next_allowed = "collect_real_event_rows_without_schema_changes"

    return ExportMapAudit(
        map_name=export_map.name,
        verdict=verdict,
        missing_tables=missing_tables,
        missing_columns=missing_columns,
        non_event_level_tables=non_event_level,
        mutable_tables=mutable,
        posthoc_tables=posthoc,
        unjoinable_tables=unjoinable,
        instrument_native_tables=instrument_native,
        middleware_required_tables=middleware_required,
        failure_reasons=tuple(failures),
        next_allowed_audit=next_allowed,
    )


def run_t95_analysis() -> T95Result:
    audits = tuple(
        audit_detector_stack_export_map(export_map)
        for export_map in detector_stack_export_map_fixtures()
    )
    native, signed_archive, augmented, posthoc, dashboard = audits
    expected_shape = (
        native.verdict == "inadmissible_for_detector_q1_upgrade"
        and signed_archive.verdict == "inadmissible_for_detector_q1_upgrade"
        and augmented.verdict == "admissible_as_preregistered_deployment_plan_only"
        and posthoc.verdict == "inadmissible_for_detector_q1_upgrade"
        and dashboard.verdict == "inadmissible_for_detector_q1_upgrade"
    )
    if expected_shape:
        strongest = (
            "The T75 photon time-tagging stack is feasible only as an "
            "augmented pre-registered deployment packet. Native timing export "
            "and a signed archive are not enough; the T87 controls, "
            "perturbation log, ancestry edge export, trust audit, and demotion "
            "log must be engineered before data collection."
        )
    else:
        strongest = (
            "The detector export map failed to separate native timing, signed "
            "archive, pre-registered augmented plan, post hoc plan, and "
            "dashboard summary controls."
        )

    return T95Result(
        audits=audits,
        strongest_claim=strongest,
        improved=(
            "T95 turns the T87 next step into an instrument-level checklist: "
            "each required raw-log table is assigned to a concrete stack "
            "component, and the audit states which tables are native versus "
            "middleware-only."
        ),
        weakened=(
            "This weakens the T75 source-anchored detector route. The named "
            "hardware stack does not natively satisfy the Q1 raw-log contract; "
            "most of the admissible packet is custom provenance/control "
            "infrastructure rather than detector physics."
        ),
        falsification_condition=(
            "T95 fails if native instrument exports alone can supply every "
            "T87 table and required column before data collection, or if an "
            "augmented deployment packet with real rows cannot preserve the "
            "T86 signed recovery, ambiguous withhold, perturbation/DAG rescue, "
            "and contaminated-control withhold separations."
        ),
        q1_update=(
            "Keep Q1 partially supported only as a detector-record "
            "admissibility protocol. The next non-null detector move is not "
            "another synthetic fixture; it is a real event-row deployment "
            "using the augmented T95 map without adding fields after the run."
        ),
        open_blocker=(
            "No real event rows exist for the augmented map. Passing T95 is "
            "only a deployment-plan admission, not empirical support and not "
            "a D1 verdict."
        ),
        recommended_next=(
            "Build the augmented packet for one dry-run dataset: publish row "
            "schemas, event-id joins, manifest hashes, and immutable export "
            "checksums, then run T87 before any T76/T86 population."
        ),
    )


def t95_result_to_dict(result: T95Result) -> dict[str, object]:
    return {
        "required_t87_tables": {
            table: list(columns) for table, columns in REQUIRED_TABLE_COLUMNS.items()
        },
        "audits": [
            {
                "map_name": audit.map_name,
                "verdict": audit.verdict,
                "missing_tables": list(audit.missing_tables),
                "missing_columns": list(audit.missing_columns),
                "non_event_level_tables": list(audit.non_event_level_tables),
                "mutable_tables": list(audit.mutable_tables),
                "posthoc_tables": list(audit.posthoc_tables),
                "unjoinable_tables": list(audit.unjoinable_tables),
                "instrument_native_tables": list(audit.instrument_native_tables),
                "middleware_required_tables": list(audit.middleware_required_tables),
                "failure_reasons": list(audit.failure_reasons),
                "next_allowed_audit": audit.next_allowed_audit,
            }
            for audit in result.audits
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _complete_export(
    table_name: str,
    component: str,
    *,
    instrument_native: bool = False,
    purpose: str,
) -> TableExport:
    return TableExport(
        table_name=table_name,
        component=component,
        provided_columns=frozenset(REQUIRED_TABLE_COLUMNS[table_name]),
        instrument_native=instrument_native,
        event_level=True,
        immutable_export=True,
        preregistered_before_data=True,
        stable_event_ids=True,
        purpose=purpose,
    )


def _component_for_table(table_name: str) -> str:
    return {
        "preregistration_manifest": "pre_run_manifest_signer",
        "control_pair_manifest": "control_pair_scheduler",
        "event_time_tag_stream": "time_tagger_and_sync_fabric",
        "signature_verification_log": "signed_archive_verifier",
        "tag_ambiguity_challenge_log": "tag_challenge_harness",
        "perturbation_trial_log": "perturbation_controller",
        "ancestry_dag_edge_export": "hash_chain_archive",
        "trust_boundary_audit_log": "lab_boundary_audit",
        "demotion_decision_log": "pre_registered_demotion_engine",
    }[table_name]


def _purpose_for_table(table_name: str) -> str:
    return {
        "preregistration_manifest": "Freeze policy, schema, code, and demotion hashes.",
        "control_pair_manifest": "Declare copied and independent witness pairs.",
        "event_time_tag_stream": "Export event-level detector and archive timing.",
        "signature_verification_log": "Verify event tags and spoof/forgery challenges.",
        "tag_ambiguity_challenge_log": "Measure ambiguous, forged, and spoofed tag behavior.",
        "perturbation_trial_log": "Separate copied-record response from independent channels.",
        "ancestry_dag_edge_export": "Publish signed raw ancestry edges and controls.",
        "trust_boundary_audit_log": "Audit detector, transport, archive, key, and operator boundaries.",
        "demotion_decision_log": "Apply pre-registered withhold rules before D1 scoring.",
    }[table_name]


def _missing_columns(exports_by_table: dict[str, list[TableExport]]) -> tuple[str, ...]:
    missing: list[str] = []
    for table_name, required_columns in REQUIRED_TABLE_COLUMNS.items():
        exports = exports_by_table.get(table_name)
        if not exports:
            continue
        provided = frozenset(
            column
            for table_export in exports
            for column in table_export.provided_columns
        )
        for column in required_columns:
            if column not in provided:
                missing.append(f"{table_name}.{column}")
    return tuple(missing)


def _tables_failing(
    exports_by_table: dict[str, list[TableExport]],
    flag_name: str,
) -> tuple[str, ...]:
    failing: list[str] = []
    for table_name in REQUIRED_TABLE_COLUMNS:
        exports = exports_by_table.get(table_name)
        if exports and not all(bool(getattr(export, flag_name)) for export in exports):
            failing.append(table_name)
    return tuple(failing)
