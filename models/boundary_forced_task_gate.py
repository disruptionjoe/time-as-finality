"""T400: Boundary-forced task gate.

T399 showed that a boundary-crossing menu can separate a pair that no
R-supported statistic can separate. It also showed why that version is
absorbed: the boundary menu was merely admitted as ordinary enlarged-state
access.

This artifact adds a small task-declaration gate. It preserves the T399
measurement substrate and asks whether the boundary-crossing readout is forced
by the declared task/setup. The positive case is intentionally only a synthetic
relational control; the artifact does not supply a domain-native physical or
finality task.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any

from models.boundary_crossing_intervention_screen import (
    run_boundary_crossing_intervention_screen,
)


ARTIFACT = "T400-boundary-forced-task-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"

VERDICT = (
    "finite forced-task gate operationalized: T399-style optional boundary "
    "access fails, a synthetic R:B relational parity task passes the formal "
    "forced-task control, and hidden-datum, closure-key, and class-marker "
    "shortcuts are blocked; no domain-native physical/finality task is earned"
)

FALSIFICATION_CONDITION = (
    "This gate would fail if optional enlarged-state access passed as forced, "
    "if a declared relational task did not require boundary variables, if any "
    "shortcut case passed, or if the synthetic control were treated as ledger "
    "movement."
)


@dataclass(frozen=True)
class TaskCandidate:
    case_id: str
    task_statement: str
    declared_before_pair: bool
    requires_boundary_variables: bool
    boundary_relation_is_task_native: bool
    boundary_menu_merely_admitted: bool
    smuggles_hidden_datum_into_R: bool = False
    closure_key_contains_separator: bool = False
    class_marker_signature_only: bool = False
    domain_native_physical_or_finality_task: bool = False


def _t399_metrics() -> dict[str, Any]:
    t399 = run_boundary_crossing_intervention_screen()
    audit = t399["main_pair_audit"]
    parity = audit["boundary_crossing_menu"]["joint_Z_parity_readout"]
    bell = audit["boundary_crossing_menu"]["bell_basis_readout"]
    return {
        "source_artifact": t399["artifact"],
        "pair": audit["pair"],
        "region_trace_distance": audit["region_trace_distance"],
        "boundary_local_trace_distance": audit["boundary_local_trace_distance"],
        "all_R_supported_statistic_bound": audit[
            "all_R_supported_statistic_bound"
        ],
        "finite_region_intervention_menu_max_diff": audit[
            "finite_region_intervention_menu"
        ]["max_diff"],
        "region_only_binary_success": audit["region_only_binary_success"],
        "boundary_local_binary_success": audit[
            "boundary_local_binary_success"
        ],
        "full_trace_distance": audit["full_trace_distance"],
        "joint_parity_success": parity["binary_success"],
        "bell_basis_success": bell["binary_success"],
        "boundary_crossing_success": max(
            parity["binary_success"], bell["binary_success"]
        ),
    }


def _candidate_cases() -> list[TaskCandidate]:
    return [
        TaskCandidate(
            case_id="t399_optional_state_label",
            task_statement=(
                "Separate phi_plus from psi_plus after admitting any joint RB "
                "readout."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=True,
        ),
        TaskCandidate(
            case_id="synthetic_RB_parity_task",
            task_statement=(
                "Output whether the R and B records have equal or unequal "
                "Z-parity in the event."
            ),
            declared_before_pair=True,
            requires_boundary_variables=True,
            boundary_relation_is_task_native=True,
            boundary_menu_merely_admitted=False,
        ),
        TaskCandidate(
            case_id="hidden_datum_in_R_shortcut",
            task_statement=(
                "Give R an extra task bit naming which Bell state was prepared."
            ),
            declared_before_pair=True,
            requires_boundary_variables=False,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=False,
            smuggles_hidden_datum_into_R=True,
        ),
        TaskCandidate(
            case_id="closure_key_shortcut",
            task_statement=(
                "Declare an SBS/closure key that already contains the parity "
                "separator."
            ),
            declared_before_pair=True,
            requires_boundary_variables=True,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=False,
            closure_key_contains_separator=True,
        ),
        TaskCandidate(
            case_id="class_marker_shortcut",
            task_statement=(
                "Use a generic class-marker signature rather than a boundary "
                "relation native to the task."
            ),
            declared_before_pair=True,
            requires_boundary_variables=True,
            boundary_relation_is_task_native=False,
            boundary_menu_merely_admitted=False,
            class_marker_signature_only=True,
        ),
    ]


def _first_failure(candidate: TaskCandidate, metrics: dict[str, Any]) -> str | None:
    if metrics["all_R_supported_statistic_bound"] != 0.0:
        return "fails_region_statistic_equality"
    if metrics["finite_region_intervention_menu_max_diff"] != 0.0:
        return "fails_region_intervention_equality"
    if metrics["boundary_local_trace_distance"] != 0.0:
        return "fails_boundary_local_equality"
    if metrics["boundary_crossing_success"] <= metrics["region_only_binary_success"]:
        return "fails_boundary_crossing_advantage"
    if not candidate.declared_before_pair:
        return "not_predeclared"
    if candidate.smuggles_hidden_datum_into_R:
        return "hidden_datum_smuggled_into_region"
    if candidate.closure_key_contains_separator:
        return "absorbed_by_closure_key"
    if candidate.class_marker_signature_only:
        return "absorbed_by_class_marker_signature"
    if candidate.boundary_menu_merely_admitted:
        return "optional_boundary_menu_only"
    if not candidate.requires_boundary_variables:
        return "task_does_not_require_boundary_variables"
    if not candidate.boundary_relation_is_task_native:
        return "boundary_relation_not_task_native"
    return None


def _audit_candidate(
    candidate: TaskCandidate, metrics: dict[str, Any]
) -> dict[str, Any]:
    failure = _first_failure(candidate, metrics)
    formal_pass = failure is None
    return {
        "candidate": asdict(candidate),
        "measurement_gate": {
            "region_statistics_equal": metrics[
                "all_R_supported_statistic_bound"
            ]
            == 0.0,
            "region_intervention_statistics_equal": metrics[
                "finite_region_intervention_menu_max_diff"
            ]
            == 0.0,
            "boundary_local_statistics_equal": metrics[
                "boundary_local_trace_distance"
            ]
            == 0.0,
            "boundary_crossing_advantage": round(
                metrics["boundary_crossing_success"]
                - metrics["region_only_binary_success"],
                12,
            ),
            "region_enlargement_restores_capability": metrics[
                "full_trace_distance"
            ]
            == 1.0,
        },
        "formal_forced_task_gate": "pass" if formal_pass else "fail",
        "failure_label": failure,
        "domain_native_burden_cleared": (
            formal_pass
            and candidate.domain_native_physical_or_finality_task
        ),
        "residue_label": _residue_label(candidate, formal_pass, failure),
    }


def _residue_label(
    candidate: TaskCandidate, formal_pass: bool, failure: str | None
) -> str:
    if formal_pass and not candidate.domain_native_physical_or_finality_task:
        return "formal_positive_control_only"
    if formal_pass:
        return "candidate_domain_native_forced_task"
    if failure == "optional_boundary_menu_only":
        return "absorbed_optional_enlarged_access"
    if failure == "hidden_datum_smuggled_into_region":
        return "blocked_hidden_datum_smuggling"
    if failure == "absorbed_by_closure_key":
        return "absorbed_closure_key_bookkeeping"
    if failure == "absorbed_by_class_marker_signature":
        return "absorbed_class_marker_signature"
    return "failed_forced_task_gate"


def run_boundary_forced_task_gate() -> dict[str, Any]:
    metrics = _t399_metrics()
    audits = [_audit_candidate(candidate, metrics) for candidate in _candidate_cases()]
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "uses_substrate": metrics,
        "gate_definition": {
            "required_measurement_conditions": [
                "all R-supported statistics equal",
                "declared finite R intervention/readout menu equal",
                "boundary-local statistics equal",
                "joint boundary-crossing menu improves capability",
            ],
            "required_task_conditions": [
                "task declared before selecting the witness pair",
                "task output requires variables from both R and B",
                "boundary relation is native to the declared task",
                "boundary menu is not merely optional enlarged-state access",
                "no hidden datum is smuggled into R",
                "no closure key already contains the separator",
                "no generic class-marker signature is doing the work",
            ],
        },
        "audits": audits,
        "summary": {
            "formal_pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["formal_forced_task_gate"] == "pass"
            ],
            "domain_native_pass_cases": [
                item["candidate"]["case_id"]
                for item in audits
                if item["domain_native_burden_cleared"]
            ],
            "blocked_cases": {
                item["candidate"]["case_id"]: item["failure_label"]
                for item in audits
                if item["formal_forced_task_gate"] == "fail"
            },
        },
        "verdict": VERDICT,
        "residue_label": "gate_operationalized_no_claim_promotion",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not repeat T399-style optional boundary-access screens.",
            "Use this gate before any future Direction-A boundary-crossing discriminator.",
            "Replace the synthetic parity control with a domain-native physical or finality task before asking for ledger movement.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(json.dumps(run_boundary_forced_task_gate(), indent=2, sort_keys=True))
