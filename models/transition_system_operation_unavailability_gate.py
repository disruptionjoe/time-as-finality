"""T406: transition-system operation-unavailability gate.

T405 showed that a finite physical latch can make a revision capability split
less stipulative, but the split is still absorbed by explicit latch-substrate
completion. T406 tests the next candidate: operation unavailability itself.

The conservative result is absorptive. If two cases match the T405/T403
payload, fixed accounting, operation menu, and non-dynamic substrate support,
then changing only the transition relation can split `can_revise_final_verdict`.
But that split factors through the transition system: once the allowed
transition relation is admitted as native operation-availability data,
factorization is restored. When the transition relation is also matched, this
finite fixture has no revision-capability split. No claim promotion follows.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from functools import lru_cache
import json
from typing import Any

from models.physical_latch_finality_lock_screen import (
    OPERATION_MENU,
    run_physical_latch_finality_lock_screen,
)
from models.physical_record_deletion_fixed_accounting import (
    AbsorberVector,
    one_bit_blind_reset_vector,
)


ARTIFACT = "T406-transition-system-operation-unavailability-gate-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_ARTIFACT = "T405-physical-latch-finality-lock-screen-v0.1"

START_STATE = "final_verdict_same"
REVISED_STATE = "revised_verdict_same"
ANNOTATED_STATE = "correction_appended_same"
CERTIFIED_STATE = "certified_verdict_same"

VERDICT = (
    "finite transition-system operation-unavailability gate built: under "
    "matched T405/T403 payload, operation menu, fixed accounting, and "
    "non-dynamic substrate support, a revision capability split appears only "
    "when the declared transition relation differs; admitting that relation as "
    "native operation-availability data restores factorization, and matched "
    "transition systems do not split revision capability, so no claim-ledger "
    "movement is earned"
)

FALSIFICATION_CONDITION = (
    "This gate fails if two cases with identical fixed-accounting projection "
    "and identical transition-system completion split on revision capability; "
    "if the main pair differs in causal payload, operation menu, resource, "
    "provenance, control, boundary, or non-dynamic substrate support; if a "
    "hidden label or latch-topology shortcut performs the split; or if a "
    "transition-system absorber is treated as a physical-arrow theorem."
)


@dataclass(frozen=True)
class TransitionEdge:
    operation: str
    source: str
    target: str


@dataclass(frozen=True)
class OperationCase:
    case_id: str
    current_state: str
    transition_edges: tuple[TransitionEdge, ...]
    absorber: AbsorberVector
    revision_budget: int = 1
    operation_menu: tuple[str, ...] = OPERATION_MENU
    substrate_carrier: str = "matched_final_record_cell"
    substrate_support_class: str = "matched_non_dynamic_support"
    latch_topology_marker: str = "not_declared"
    hidden_source_label: str | None = None


def _base_absorber() -> AbsorberVector:
    return one_bit_blind_reset_vector()


def _two_bit_absorber() -> AbsorberVector:
    base = _base_absorber()
    return replace(
        base,
        erased_bits=2,
        beta_work_floor=2 * base.beta_work_floor,
        blank_capacity_delta=2,
    )


def _provenance_absorber() -> AbsorberVector:
    return replace(_base_absorber(), provenance_state="authority_invalidated")


def _control_absorber() -> AbsorberVector:
    return replace(_base_absorber(), reversible_control="rewrite_handle_disabled")


def _boundary_absorber() -> AbsorberVector:
    return replace(_base_absorber(), boundary_access="observer_boundary_closed")


def _transition_graph(kind: str) -> tuple[TransitionEdge, ...]:
    shared = (
        TransitionEdge("read_verdict", START_STATE, START_STATE),
        TransitionEdge("append_correction", START_STATE, ANNOTATED_STATE),
        TransitionEdge("certify_verdict", START_STATE, CERTIFIED_STATE),
    )
    if kind == "revision_reachable":
        return shared + (
            TransitionEdge("revise_verdict", START_STATE, REVISED_STATE),
        )
    if kind == "revision_unreachable":
        return shared
    raise ValueError(f"unknown transition graph kind: {kind}")


@lru_cache(maxsize=1)
def _causal_payload_signature() -> dict[str, Any]:
    t405 = run_physical_latch_finality_lock_screen()
    return {
        "source_artifact": t405["artifact"],
        "causal_domain_signature": t405["causal_domain_signature"],
        "joint_payload": [1, 1],
        "verdict_payload": "same",
    }


def _fixed_accounting_projection(case: OperationCase) -> dict[str, Any]:
    return {
        "visible_causal_payload": _causal_payload_signature(),
        "revision_budget": case.revision_budget,
        "operation_menu": list(case.operation_menu),
        "absorber_vector": asdict(case.absorber),
        "non_dynamic_substrate_support": {
            "carrier": case.substrate_carrier,
            "support_class": case.substrate_support_class,
        },
    }


def _transition_system_completion(case: OperationCase) -> dict[str, Any]:
    completion = _fixed_accounting_projection(case)
    completion["current_state"] = case.current_state
    completion["transition_edges"] = [
        asdict(edge) for edge in sorted(case.transition_edges, key=_edge_key)
    ]
    return completion


def _edge_key(edge: TransitionEdge) -> tuple[str, str, str]:
    return (edge.operation, edge.source, edge.target)


def _has_edge(case: OperationCase, operation: str, source: str, target: str) -> bool:
    return TransitionEdge(operation, source, target) in case.transition_edges


def _resource_within_declared_account(absorber: AbsorberVector) -> bool:
    base = _base_absorber()
    return (
        absorber.erased_bits <= base.erased_bits
        and absorber.beta_work_floor <= base.beta_work_floor + 1e-12
        and absorber.blank_capacity_delta <= base.blank_capacity_delta
        and absorber.sink_delta == base.sink_delta
    )


def _capability(case: OperationCase) -> dict[str, Any]:
    boundary_open = case.absorber.boundary_access == "matched_observer_boundary"
    provenance_valid = case.absorber.provenance_state == "matched_valid_provenance"
    control_enabled = case.absorber.reversible_control == "blind_reset_only"
    resource_ok = _resource_within_declared_account(case.absorber)
    can_read = (
        "read_verdict" in case.operation_menu
        and boundary_open
        and _has_edge(case, "read_verdict", START_STATE, START_STATE)
    )
    can_append = (
        "append_correction" in case.operation_menu
        and boundary_open
        and _has_edge(case, "append_correction", START_STATE, ANNOTATED_STATE)
    )
    can_certify = (
        "certify_verdict" in case.operation_menu
        and boundary_open
        and provenance_valid
        and _has_edge(case, "certify_verdict", START_STATE, CERTIFIED_STATE)
    )
    can_revise = (
        "revise_verdict" in case.operation_menu
        and can_read
        and can_append
        and provenance_valid
        and control_enabled
        and resource_ok
        and case.revision_budget > 0
        and _has_edge(case, "revise_verdict", START_STATE, REVISED_STATE)
    )
    return {
        "verdict_payload": "same",
        "can_read_verdict": can_read,
        "can_append_correction": can_append,
        "can_revise_final_verdict": can_revise,
        "can_certify_final_record": can_certify,
    }


def _differing_fields(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [key for key in left if left[key] != right.get(key)]


def _absorber_mismatch_fields(left: AbsorberVector, right: AbsorberVector) -> list[str]:
    left_values = asdict(left)
    right_values = asdict(right)
    return [
        field for field, value in left_values.items() if value != right_values[field]
    ]


def _residue_label(
    left: OperationCase,
    right: OperationCase,
    same_fixed_projection: bool,
    same_transition_completion: bool,
    capability_split: bool,
    absorber_mismatches: list[str],
    hidden_label_attempt: bool,
    latch_topology_attempt: bool,
) -> str:
    if hidden_label_attempt:
        return "blocked_hidden_label_shortcut"
    if latch_topology_attempt:
        return "blocked_latch_topology_shortcut"
    if absorber_mismatches:
        if {"erased_bits", "beta_work_floor", "blank_capacity_delta"} & set(
            absorber_mismatches
        ):
            return "absorbed_by_resource_accounting"
        if "provenance_state" in absorber_mismatches:
            return "absorbed_by_provenance_completion"
        if "reversible_control" in absorber_mismatches:
            return "absorbed_by_control_completion"
        if "boundary_access" in absorber_mismatches:
            return "absorbed_by_boundary_completion"
        return "absorbed_by_fixed_accounting_completion"
    if not same_fixed_projection:
        return "absorbed_by_fixed_accounting_or_menu_completion"
    if capability_split and not same_transition_completion:
        return "absorbed_by_transition_system_completion"
    if capability_split:
        return "invalid_same_transition_system_split_requires_review"
    return "no_capability_split"


def _case_to_dict(case: OperationCase) -> dict[str, Any]:
    data = asdict(case)
    data["absorber"] = asdict(case.absorber)
    data["transition_edges"] = [
        asdict(edge) for edge in sorted(case.transition_edges, key=_edge_key)
    ]
    return data


def _pair_audit(pair_id: str, left: OperationCase, right: OperationCase) -> dict[str, Any]:
    left_fixed = _fixed_accounting_projection(left)
    right_fixed = _fixed_accounting_projection(right)
    left_transition = _transition_system_completion(left)
    right_transition = _transition_system_completion(right)
    left_capability = _capability(left)
    right_capability = _capability(right)
    absorber_mismatches = _absorber_mismatch_fields(left.absorber, right.absorber)
    fixed_differences = _differing_fields(left_fixed, right_fixed)
    transition_differences = _differing_fields(left_transition, right_transition)
    capability_differences = _differing_fields(left_capability, right_capability)
    hidden_label_attempt = (
        left.hidden_source_label is not None
        or right.hidden_source_label is not None
    ) and left.hidden_source_label != right.hidden_source_label
    latch_topology_attempt = (
        left.latch_topology_marker != "not_declared"
        or right.latch_topology_marker != "not_declared"
    ) and left.latch_topology_marker != right.latch_topology_marker
    same_fixed_projection = left_fixed == right_fixed
    same_transition_completion = left_transition == right_transition

    return {
        "pair_id": pair_id,
        "left": _case_to_dict(left),
        "right": _case_to_dict(right),
        "fixed_accounting_projection_equal": same_fixed_projection,
        "fixed_accounting_projection_differences": fixed_differences,
        "transition_system_completion_equal": same_transition_completion,
        "transition_system_completion_differences": transition_differences,
        "same_operation_menu": left.operation_menu == right.operation_menu,
        "same_revision_budget": left.revision_budget == right.revision_budget,
        "same_non_dynamic_substrate_support": (
            left.substrate_carrier == right.substrate_carrier
            and left.substrate_support_class == right.substrate_support_class
        ),
        "absorber_mismatch_fields": absorber_mismatches,
        "capability": {
            "left": left_capability,
            "right": right_capability,
            "differs": bool(capability_differences),
            "differing_fields": capability_differences,
        },
        "hidden_label_shortcut_attempt": hidden_label_attempt,
        "latch_topology_shortcut_attempt": latch_topology_attempt,
        "residue_label": _residue_label(
            left,
            right,
            same_fixed_projection,
            same_transition_completion,
            bool(capability_differences),
            absorber_mismatches,
            hidden_label_attempt,
            latch_topology_attempt,
        ),
    }


def _cases() -> dict[str, OperationCase]:
    base = _base_absorber()
    reachable = _transition_graph("revision_reachable")
    unreachable = _transition_graph("revision_unreachable")
    return {
        "reachable": OperationCase(
            case_id="reachable",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
        ),
        "unreachable": OperationCase(
            case_id="unreachable",
            current_state=START_STATE,
            transition_edges=unreachable,
            absorber=base,
        ),
        "reachable_copy": OperationCase(
            case_id="reachable_copy",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
        ),
        "without_revision_menu": OperationCase(
            case_id="without_revision_menu",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
            operation_menu=("read_verdict", "append_correction", "certify_verdict"),
        ),
        "two_bit_resource": OperationCase(
            case_id="two_bit_resource",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=_two_bit_absorber(),
        ),
        "invalid_provenance": OperationCase(
            case_id="invalid_provenance",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=_provenance_absorber(),
        ),
        "disabled_control": OperationCase(
            case_id="disabled_control",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=_control_absorber(),
        ),
        "closed_boundary": OperationCase(
            case_id="closed_boundary",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=_boundary_absorber(),
        ),
        "hidden_alpha": OperationCase(
            case_id="hidden_alpha",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
            hidden_source_label="alpha",
        ),
        "hidden_beta": OperationCase(
            case_id="hidden_beta",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
            hidden_source_label="beta",
        ),
        "latch_rewritable_marker": OperationCase(
            case_id="latch_rewritable_marker",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
            latch_topology_marker="rewritable_gate",
        ),
        "latch_fused_marker": OperationCase(
            case_id="latch_fused_marker",
            current_state=START_STATE,
            transition_edges=reachable,
            absorber=base,
            latch_topology_marker="fused_gate",
        ),
    }


def _pair_audits() -> list[dict[str, Any]]:
    cases = _cases()
    return [
        _pair_audit(
            "transition_unavailability_main_pair",
            cases["reachable"],
            cases["unreachable"],
        ),
        _pair_audit("matched_transition_control", cases["reachable"], cases["reachable_copy"]),
        _pair_audit(
            "operation_menu_completion_control",
            cases["reachable"],
            cases["without_revision_menu"],
        ),
        _pair_audit(
            "resource_accounting_control",
            cases["reachable"],
            cases["two_bit_resource"],
        ),
        _pair_audit(
            "provenance_completion_control",
            cases["reachable"],
            cases["invalid_provenance"],
        ),
        _pair_audit(
            "control_completion_control",
            cases["reachable"],
            cases["disabled_control"],
        ),
        _pair_audit(
            "boundary_completion_control",
            cases["reachable"],
            cases["closed_boundary"],
        ),
        _pair_audit(
            "hidden_label_shortcut_control",
            cases["hidden_alpha"],
            cases["hidden_beta"],
        ),
        _pair_audit(
            "latch_topology_shortcut_control",
            cases["latch_rewritable_marker"],
            cases["latch_fused_marker"],
        ),
    ]


def _factorization_check(cases: dict[str, OperationCase]) -> dict[str, Any]:
    violations: list[dict[str, str]] = []
    items = list(cases.values())
    checked_pairs = 0
    matched_transition_pairs = 0
    for index, left in enumerate(items):
        for right in items[index + 1 :]:
            checked_pairs += 1
            if _transition_system_completion(left) != _transition_system_completion(right):
                continue
            matched_transition_pairs += 1
            if _capability(left) != _capability(right):
                violations.append(
                    {
                        "left": left.case_id,
                        "right": right.case_id,
                    }
                )
    return {
        "checked_pairs": checked_pairs,
        "matched_transition_completion_pairs": matched_transition_pairs,
        "violations": violations,
        "same_transition_system_implies_same_capability": not violations,
    }


def _absorber_audit(main_pair: dict[str, Any]) -> dict[str, Any]:
    return {
        "causal_reachability_and_domain_of_dependence": {
            "status": "matched_not_explanatory",
            "reason": (
                "The gate imports the same T405/T403 causal payload for both "
                "main-pair cases."
            ),
        },
        "ordinary_joint_input_completion": {
            "status": "matched_not_explanatory",
            "reason": "The main pair keeps the joint payload and verdict payload fixed.",
        },
        "operation_menu_completion": {
            "status": "matched_not_explanatory_for_main_pair",
            "reason": (
                "The main pair has the same declared operation menu and "
                "revision budget; operation-menu variation is isolated as a "
                "control."
            ),
        },
        "fixed_accounting_resource_provenance_control_boundary": {
            "status": "matched_not_explanatory_for_main_pair",
            "reason": (
                "The T145-style absorber vector is identical in the main pair."
            ),
        },
        "latch_topology_completion": {
            "status": "blocked_for_main_pair",
            "reason": (
                "The main pair does not vary latch topology; latch-marker "
                "variation is isolated as a blocked shortcut control."
            ),
        },
        "transition_system_completion": {
            "status": "absorbs",
            "reason": (
                "Adding the finite transition relation restores factorization "
                "of the revision capability."
            ),
            "main_pair_completion_differences": main_pair[
                "transition_system_completion_differences"
            ],
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": (
                "The artifact is a finite absorber/precheck for operation "
                "unavailability, not a physical-arrow theorem."
            ),
        },
    }


def run_transition_system_operation_unavailability_gate() -> dict[str, Any]:
    cases = _cases()
    audits = _pair_audits()
    main_pair = next(
        audit
        for audit in audits
        if audit["pair_id"] == "transition_unavailability_main_pair"
    )
    factorization = _factorization_check(cases)
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "source_artifact": SOURCE_ARTIFACT,
        "setup": {
            "task": (
                "given a common-future final verdict with fixed T405/T403 "
                "payload and accounting, decide whether revise_verdict is "
                "available under the declared finite transition relation"
            ),
            "fixed_projection": (
                "T405/T403 causal payload + revision budget + operation menu + "
                "T145-style absorber vector + non-dynamic substrate support"
            ),
            "transition_system_completion": (
                "fixed projection + current state + finite operation-labeled "
                "transition edges"
            ),
            "capability_object": (
                "future operation availability for reading, appending, "
                "revising, and certifying the final verdict"
            ),
            "declared_before_pair": True,
        },
        "pair_audits": audits,
        "main_pair_summary": {
            "pair_id": main_pair["pair_id"],
            "fixed_accounting_projection_equal": main_pair[
                "fixed_accounting_projection_equal"
            ],
            "transition_system_completion_equal": main_pair[
                "transition_system_completion_equal"
            ],
            "same_operation_menu": main_pair["same_operation_menu"],
            "same_revision_budget": main_pair["same_revision_budget"],
            "same_non_dynamic_substrate_support": main_pair[
                "same_non_dynamic_substrate_support"
            ],
            "absorber_mismatch_fields": main_pair["absorber_mismatch_fields"],
            "capability_split": main_pair["capability"]["differs"],
            "differing_capability_fields": main_pair["capability"][
                "differing_fields"
            ],
            "residue_label": main_pair["residue_label"],
        },
        "factorization_check": factorization,
        "absorber_audit": _absorber_audit(main_pair),
        "summary": {
            "same_fixed_accounting_split_cases": [
                audit["pair_id"]
                for audit in audits
                if audit["fixed_accounting_projection_equal"]
                and audit["capability"]["differs"]
            ],
            "absorbed_cases": {
                audit["pair_id"]: audit["residue_label"] for audit in audits
            },
        },
        "verdict": VERDICT,
        "residue_label": "operation_unavailability_absorbed_by_transition_system_completion",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Do not treat operation-unavailability language as progress unless the transition-system completion is already matched.",
            "A future positive route needs a domain-native law or measured substrate dynamics that forces the transition relation rather than restating it.",
            "Keep the T408/basis-free lane separate until Joe resolves the promotion posture (number collision resolved 2026-07-01, authorized by Joe: basis-free renumbered T404 to T408).",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_transition_system_operation_unavailability_gate(),
            indent=2,
            sort_keys=True,
        )
    )
