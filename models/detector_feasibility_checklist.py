"""T96: instrument-facing feasibility checklist for the detector raw-log route.

T87 specified the event-level raw-log contract and T95 mapped one named
time-tagging stack into that contract. The remaining question is feasibility:
which requirements are native instrument exports, which are ordinary logging
middleware, and which are custom experiment/governance commitments that can
still kill the detector branch before any D1 scoring?

This module does not score D1 and does not claim a detector effect. It only
classifies the load-bearing requirements of the current T75/T87/T95 route.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS


@dataclass(frozen=True)
class FeasibilityItem:
    table_name: str
    owner: str
    requirement_class: str
    instrument_native: bool
    required_before_first_event: bool
    provides_real_event_rows: bool
    failure_if_missing: str
    purpose: str


@dataclass(frozen=True)
class FeasibilityChecklist:
    name: str
    stack: str
    items: tuple[FeasibilityItem, ...]
    purpose: str


@dataclass(frozen=True)
class FeasibilityAudit:
    checklist_name: str
    route_status: str
    native_tables: tuple[str, ...]
    middleware_tables: tuple[str, ...]
    custom_control_tables: tuple[str, ...]
    governance_tables: tuple[str, ...]
    blocker_tables: tuple[str, ...]
    failure_modes: tuple[str, ...]
    next_allowed_step: str


@dataclass(frozen=True)
class T96Result:
    audit: FeasibilityAudit
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1_update: str
    open_blocker: str
    recommended_next: str


def t75_t87_t95_feasibility_checklist() -> FeasibilityChecklist:
    items = (
        FeasibilityItem(
            table_name="preregistration_manifest",
            owner="analysis_governance",
            requirement_class="governance_lock",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=False,
            failure_if_missing="posthoc_schema_or_policy_choice",
            purpose=(
                "Freeze policy, analysis code, evidence schema, and demotion "
                "hashes before the run."
            ),
        ),
        FeasibilityItem(
            table_name="control_pair_manifest",
            owner="experiment_design",
            requirement_class="custom_control_middleware",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=False,
            failure_if_missing="copied_vs_independent_controls_absent",
            purpose=(
                "Declare copied and independent witness pairs before event "
                "collection."
            ),
        ),
        FeasibilityItem(
            table_name="event_time_tag_stream",
            owner="instrument_stack",
            requirement_class="native_instrument_export",
            instrument_native=True,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="no_detector_time_tag_rows",
            purpose="Provide native event-level detector timing rows.",
        ),
        FeasibilityItem(
            table_name="signature_verification_log",
            owner="archive_middleware",
            requirement_class="provenance_logging_middleware",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="unsigned_or_unverified_archive_rows",
            purpose="Verify event-level signatures for retained and challenged tags.",
        ),
        FeasibilityItem(
            table_name="tag_ambiguity_challenge_log",
            owner="experiment_design",
            requirement_class="custom_control_middleware",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="no_deliberate_ambiguity_controls",
            purpose=(
                "Run and log retained, forged, spoofed, and unique-tag "
                "ambiguity challenges."
            ),
        ),
        FeasibilityItem(
            table_name="perturbation_trial_log",
            owner="experiment_design",
            requirement_class="custom_control_middleware",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="no_isolated_perturbation_trials",
            purpose=(
                "Log perturbation-only controls and back-action contamination "
                "controls."
            ),
        ),
        FeasibilityItem(
            table_name="ancestry_dag_edge_export",
            owner="archive_middleware",
            requirement_class="provenance_logging_middleware",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="no_signed_raw_ancestry_edges",
            purpose="Export signed raw parent-child record edges.",
        ),
        FeasibilityItem(
            table_name="trust_boundary_audit_log",
            owner="lab_governance",
            requirement_class="governance_lock",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="trust_boundary_unaudited",
            purpose=(
                "Audit detector, transport, archive, operator, and key-scope "
                "boundaries."
            ),
        ),
        FeasibilityItem(
            table_name="demotion_decision_log",
            owner="analysis_governance",
            requirement_class="governance_lock",
            instrument_native=False,
            required_before_first_event=True,
            provides_real_event_rows=True,
            failure_if_missing="demotion_rules_not_fixed_predata",
            purpose=(
                "Apply pre-registered demotion decisions before any D1-style "
                "interpretation."
            ),
        ),
    )
    return FeasibilityChecklist(
        name="t75_t87_t95_detector_route_feasibility",
        stack=(
            "HydraHarp + White Rabbit + signed archive + copied/independent "
            "controls + ambiguity/perturbation middleware + governance locks"
        ),
        items=items,
        purpose=(
            "Classify the T87/T95 detector route by what is native hardware, "
            "what is provenance middleware, and what is pre-data governance."
        ),
    )


def audit_detector_feasibility(
    checklist: FeasibilityChecklist,
) -> FeasibilityAudit:
    table_names = {item.table_name for item in checklist.items}
    missing_from_contract = tuple(
        table_name
        for table_name in REQUIRED_TABLE_COLUMNS
        if table_name not in table_names
    )
    if missing_from_contract:
        raise ValueError(
            "Checklist must classify every T87 table: "
            + ", ".join(missing_from_contract)
        )

    native_tables = tuple(
        item.table_name for item in checklist.items if item.instrument_native
    )
    middleware_tables = tuple(
        item.table_name
        for item in checklist.items
        if item.requirement_class == "provenance_logging_middleware"
    )
    custom_control_tables = tuple(
        item.table_name
        for item in checklist.items
        if item.requirement_class == "custom_control_middleware"
    )
    governance_tables = tuple(
        item.table_name
        for item in checklist.items
        if item.requirement_class == "governance_lock"
    )
    blocker_tables = tuple(
        item.table_name
        for item in checklist.items
        if not item.instrument_native
        and item.required_before_first_event
        and item.failure_if_missing
        in {
            "copied_vs_independent_controls_absent",
            "no_deliberate_ambiguity_controls",
            "no_isolated_perturbation_trials",
            "demotion_rules_not_fixed_predata",
        }
    )

    failure_modes = tuple(item.failure_if_missing for item in checklist.items)

    if len(native_tables) == len(REQUIRED_TABLE_COLUMNS):
        route_status = "native_instrument_route"
        next_allowed = "collect_real_event_rows"
    else:
        route_status = "feasible_as_governance_heavy_dry_run_only"
        next_allowed = "publish_locked_dry_run_packet_before_any_q1_claim"

    return FeasibilityAudit(
        checklist_name=checklist.name,
        route_status=route_status,
        native_tables=native_tables,
        middleware_tables=middleware_tables,
        custom_control_tables=custom_control_tables,
        governance_tables=governance_tables,
        blocker_tables=blocker_tables,
        failure_modes=failure_modes,
        next_allowed_step=next_allowed,
    )


def run_t96_analysis() -> T96Result:
    audit = audit_detector_feasibility(t75_t87_t95_feasibility_checklist())

    assert audit.route_status == "feasible_as_governance_heavy_dry_run_only"
    assert audit.native_tables == ("event_time_tag_stream",)

    return T96Result(
        audit=audit,
        strongest_claim=(
            "The surviving detector-side Q1 route is not a native detector "
            "measurement path. It survives only as a governance-heavy dry-run "
            "protocol in which the decisive bottlenecks are copied/independent "
            "controls, ambiguity challenges, perturbation controls, and "
            "pre-data demotion rules rather than detector timing itself."
        ),
        improved=(
            "T96 converts the vague phrase 'instrument-facing feasibility' into "
            "a table-by-table burden split. A serious reader can now see which "
            "requirements come from hardware, which come from provenance "
            "logging, and which are pre-data governance commitments that can "
            "kill the route before any D1 audit."
        ),
        weakened=(
            "This weakens the detector branch again. Only one required T87 "
            "table is native to the named time-tagging hardware. The rest of "
            "the route is carried by archive middleware, control design, and "
            "analysis governance, so the branch should not be described as a "
            "detector-physics discriminator."
        ),
        falsification_condition=(
            "T96 fails if a realistic detector stack can natively export most "
            "of the T87 control, provenance, and demotion packet without "
            "custom middleware or governance locks, or if a dry run lacking the "
            "listed blocker tables still legitimately upgrades Q1."
        ),
        q1_update=(
            "Q1 remains partially supported, but the detector branch should now "
            "be read as a dry-run admissibility program over classical record "
            "governance. Until a locked packet with copied/independent "
            "controls, ambiguity challenges, perturbation trials, signed raw "
            "ancestry edges, trust audits, and pre-data demotion rules is "
            "executed, the route does not rise above provenance bookkeeping."
        ),
        open_blocker=(
            "The repo still has no locked dry-run packet with real rows. The "
            "main blocker is not timing hardware; it is the pre-data assembly "
            "of control manifests and governance logs that would let a hostile "
            "reviewer reject post hoc choices."
        ),
        recommended_next=(
            "Build one dry-run packet skeleton with file names, row schemas, "
            "hash commitments, copied/independent controls, ambiguity "
            "challenges, perturbation trial plan, trust audit template, and "
            "demotion log template, then reject the route if a lab cannot fill "
            "it before data collection."
        ),
    )


def t96_result_to_dict(result: T96Result) -> dict[str, object]:
    return {
        "audit": {
            "checklist_name": result.audit.checklist_name,
            "route_status": result.audit.route_status,
            "native_tables": list(result.audit.native_tables),
            "middleware_tables": list(result.audit.middleware_tables),
            "custom_control_tables": list(result.audit.custom_control_tables),
            "governance_tables": list(result.audit.governance_tables),
            "blocker_tables": list(result.audit.blocker_tables),
            "failure_modes": list(result.audit.failure_modes),
            "next_allowed_step": result.audit.next_allowed_step,
        },
        "required_t87_tables": {
            table_name: list(columns)
            for table_name, columns in REQUIRED_TABLE_COLUMNS.items()
        },
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1_update": result.q1_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }
