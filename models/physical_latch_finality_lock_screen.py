"""T405: Physical-latch finality-lock screen.

T403 showed that a same-domain provisional/sealed split is absorbed by
explicit finality-state completion. T405 makes that finality state less
stipulative: it derives revision availability from a finite physical latch
substrate while holding the T403 causal payload and T145 fixed-accounting
absorbers constant.

The conservative result is still absorptive. A rewritable latch and a fused
latch can share causal-domain data, joint payload, verdict payload, revision
budget, operation menu, resource accounting, provenance, reversible-control
class, and observer boundary, while only the rewritable latch can revise the
final verdict. That split survives the fixed-accounting projection but is
absorbed by explicit latch-substrate completion. No claim promotion follows.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
import json
from typing import Any

from models.physical_record_deletion_fixed_accounting import (
    AbsorberVector,
    one_bit_blind_reset_vector,
)
from models.same_domain_finality_lock_screen import (
    run_same_domain_finality_lock_screen,
)


ARTIFACT = "T405-physical-latch-finality-lock-screen-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_ARTIFACT = "T403-same-domain-finality-lock-screen-v0.1"

OPERATION_MENU = (
    "read_verdict",
    "append_correction",
    "revise_verdict",
    "certify_verdict",
)

VERDICT = (
    "finite physical-latch finality-lock screen built: a rewritable latch and "
    "a fused latch have identical T403 causal-domain data, joint payload, "
    "verdict payload, revision budget, operation menu, resource accounting, "
    "provenance, control class, and observer boundary, while only the "
    "rewritable latch can revise the final verdict; the split is not a "
    "stipulated finality label and survives the fixed-accounting projection, "
    "but it is absorbed by explicit latch-substrate completion, so no "
    "claim-ledger movement is earned"
)

FALSIFICATION_CONDITION = (
    "This screen would fail if the main pair differed in causal-domain data, "
    "joint payload, revision budget, operation menu, resource accounting, "
    "provenance, control class, or observer boundary; if a stipulated label "
    "or hidden marker performed the separation; if latch-substrate completion "
    "did not restore factorization; or if the finite latch were treated as "
    "evidence for a physical arrow or new physics."
)


@dataclass(frozen=True)
class PhysicalLatch:
    carrier: str
    material_topology: str
    rewrite_handle_present: bool
    seal_bridge_closed: bool
    mechanical_continuity: str
    seal_basis: str


@dataclass(frozen=True)
class LatchCase:
    case_id: str
    joint_payload: tuple[int, int]
    latch: PhysicalLatch
    absorber: AbsorberVector
    revision_budget: int = 1
    operation_menu: tuple[str, ...] = OPERATION_MENU
    accepted_finality_label: str | None = None
    hidden_source_label: str | None = None


def _verdict_payload(joint_payload: tuple[int, int]) -> str:
    return "same" if joint_payload[0] == joint_payload[1] else "different"


def _causal_domain_signature() -> dict[str, Any]:
    t403 = run_same_domain_finality_lock_screen()
    return t403["causal_domain_signature"]


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


def _rewritable_latch() -> PhysicalLatch:
    return PhysicalLatch(
        carrier="matched_record_cell",
        material_topology="rewritable_gate",
        rewrite_handle_present=True,
        seal_bridge_closed=False,
        mechanical_continuity="unfused_bridge",
        seal_basis="finite latch topology",
    )


def _fused_latch() -> PhysicalLatch:
    return PhysicalLatch(
        carrier="matched_record_cell",
        material_topology="fused_gate",
        rewrite_handle_present=True,
        seal_bridge_closed=True,
        mechanical_continuity="fused_bridge",
        seal_basis="finite latch topology",
    )


def _derived_lock_state(latch: PhysicalLatch) -> str:
    if (
        latch.material_topology == "rewritable_gate"
        and latch.rewrite_handle_present
        and not latch.seal_bridge_closed
    ):
        return "physically_rewritable"
    if latch.material_topology == "fused_gate" and latch.seal_bridge_closed:
        return "physically_sealed"
    return "underdeclared_latch_state"


def _resource_within_declared_account(absorber: AbsorberVector) -> bool:
    base = _base_absorber()
    return (
        absorber.erased_bits <= base.erased_bits
        and absorber.beta_work_floor <= base.beta_work_floor + 1e-12
        and absorber.blank_capacity_delta <= base.blank_capacity_delta
        and absorber.sink_delta == base.sink_delta
    )


def _visible_causal_payload_projection(case: LatchCase) -> dict[str, Any]:
    return {
        "causal_domain_signature": _causal_domain_signature(),
        "joint_payload": list(case.joint_payload),
        "verdict_payload": _verdict_payload(case.joint_payload),
    }


def _fixed_accounting_projection(case: LatchCase) -> dict[str, Any]:
    return {
        "visible_projection": _visible_causal_payload_projection(case),
        "revision_budget": case.revision_budget,
        "operation_menu": list(case.operation_menu),
        "absorber_vector": asdict(case.absorber),
        "latch_support_without_topology": {
            "carrier": case.latch.carrier,
            "rewrite_handle_present": case.latch.rewrite_handle_present,
            "seal_basis": case.latch.seal_basis,
        },
    }


def _latch_substrate_completion(case: LatchCase) -> dict[str, Any]:
    completion = _fixed_accounting_projection(case)
    completion["physical_latch"] = asdict(case.latch)
    completion["derived_lock_state"] = _derived_lock_state(case.latch)
    return completion


def _capability(case: LatchCase) -> dict[str, Any]:
    boundary_open = case.absorber.boundary_access == "matched_observer_boundary"
    provenance_valid = case.absorber.provenance_state == "matched_valid_provenance"
    control_enabled = case.absorber.reversible_control == "blind_reset_only"
    resource_ok = _resource_within_declared_account(case.absorber)
    latch_rewritable = _derived_lock_state(case.latch) == "physically_rewritable"
    can_read = "read_verdict" in case.operation_menu and boundary_open
    can_append = "append_correction" in case.operation_menu and can_read
    can_revise = (
        "revise_verdict" in case.operation_menu
        and can_read
        and can_append
        and provenance_valid
        and control_enabled
        and resource_ok
        and case.revision_budget > 0
        and latch_rewritable
    )
    can_certify = "certify_verdict" in case.operation_menu and can_read and provenance_valid
    return {
        "verdict_payload": _verdict_payload(case.joint_payload),
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
    left: LatchCase,
    right: LatchCase,
    same_fixed_projection: bool,
    capability_split: bool,
    absorber_mismatches: list[str],
    shortcut_attempt: bool,
    stipulated_label_attempt: bool,
) -> str:
    if shortcut_attempt:
        return "blocked_hidden_label_shortcut"
    if stipulated_label_attempt:
        return "blocked_stipulated_finality_label"
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
    if capability_split and same_fixed_projection and left.latch != right.latch:
        return "absorbed_by_physical_latch_substrate_completion"
    if not capability_split:
        return "no_capability_split"
    return "unclassified_same_accounting_split_requires_review"


def _pair_audit(pair_id: str, left: LatchCase, right: LatchCase) -> dict[str, Any]:
    left_projection = _fixed_accounting_projection(left)
    right_projection = _fixed_accounting_projection(right)
    left_completion = _latch_substrate_completion(left)
    right_completion = _latch_substrate_completion(right)
    left_capability = _capability(left)
    right_capability = _capability(right)
    absorber_mismatches = _absorber_mismatch_fields(left.absorber, right.absorber)
    same_fixed_projection = left_projection == right_projection
    capability_differences = _differing_fields(left_capability, right_capability)
    completion_differences = _differing_fields(left_completion, right_completion)
    shortcut_attempt = (
        left.hidden_source_label is not None
        or right.hidden_source_label is not None
    ) and left.hidden_source_label != right.hidden_source_label
    stipulated_label_attempt = (
        left.accepted_finality_label is not None
        or right.accepted_finality_label is not None
    ) and left.accepted_finality_label != right.accepted_finality_label

    return {
        "pair_id": pair_id,
        "left": _case_to_dict(left),
        "right": _case_to_dict(right),
        "visible_causal_payload_equal": (
            _visible_causal_payload_projection(left)
            == _visible_causal_payload_projection(right)
        ),
        "fixed_accounting_projection_equal": same_fixed_projection,
        "same_joint_payload": left.joint_payload == right.joint_payload,
        "same_verdict_payload": (
            _verdict_payload(left.joint_payload)
            == _verdict_payload(right.joint_payload)
        ),
        "same_revision_budget": left.revision_budget == right.revision_budget,
        "same_operation_menu": left.operation_menu == right.operation_menu,
        "same_latch_support_without_topology": (
            left_projection["latch_support_without_topology"]
            == right_projection["latch_support_without_topology"]
        ),
        "absorber_mismatch_fields": absorber_mismatches,
        "derived_lock_states": {
            "left": _derived_lock_state(left.latch),
            "right": _derived_lock_state(right.latch),
        },
        "capability": {
            "left": left_capability,
            "right": right_capability,
            "differs": bool(capability_differences),
            "differing_fields": capability_differences,
        },
        "latch_substrate_completion": {
            "left": left_completion,
            "right": right_completion,
            "restores_factorization": (
                bool(capability_differences) and bool(completion_differences)
            )
            or not capability_differences,
            "differing_fields": completion_differences,
        },
        "hidden_label_shortcut_attempt": shortcut_attempt,
        "stipulated_finality_label_attempt": stipulated_label_attempt,
        "residue_label": _residue_label(
            left,
            right,
            same_fixed_projection,
            bool(capability_differences),
            absorber_mismatches,
            shortcut_attempt,
            stipulated_label_attempt,
        ),
    }


def _case_to_dict(case: LatchCase) -> dict[str, Any]:
    data = asdict(case)
    data["absorber"] = asdict(case.absorber)
    data["derived_lock_state"] = _derived_lock_state(case.latch)
    return data


def _cases() -> dict[str, LatchCase]:
    base = _base_absorber()
    return {
        "rewritable_same": LatchCase(
            case_id="rewritable_same",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
        ),
        "fused_same": LatchCase(
            case_id="fused_same",
            joint_payload=(1, 1),
            latch=_fused_latch(),
            absorber=base,
        ),
        "rewritable_same_copy": LatchCase(
            case_id="rewritable_same_copy",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
        ),
        "rewritable_two_bit_resource": LatchCase(
            case_id="rewritable_two_bit_resource",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=_two_bit_absorber(),
        ),
        "rewritable_invalid_provenance": LatchCase(
            case_id="rewritable_invalid_provenance",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=_provenance_absorber(),
        ),
        "rewritable_disabled_control": LatchCase(
            case_id="rewritable_disabled_control",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=_control_absorber(),
        ),
        "rewritable_closed_boundary": LatchCase(
            case_id="rewritable_closed_boundary",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=_boundary_absorber(),
        ),
        "hidden_alpha": LatchCase(
            case_id="hidden_alpha",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
            hidden_source_label="alpha",
        ),
        "hidden_beta": LatchCase(
            case_id="hidden_beta",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
            hidden_source_label="beta",
        ),
        "stipulated_provisional": LatchCase(
            case_id="stipulated_provisional",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
            accepted_finality_label="provisional",
        ),
        "stipulated_sealed": LatchCase(
            case_id="stipulated_sealed",
            joint_payload=(1, 1),
            latch=_rewritable_latch(),
            absorber=base,
            accepted_finality_label="sealed",
        ),
    }


def _pair_audits() -> list[dict[str, Any]]:
    cases = _cases()
    return [
        _pair_audit(
            "physical_latch_finality_lock_pair",
            cases["rewritable_same"],
            cases["fused_same"],
        ),
        _pair_audit(
            "matched_latch_control",
            cases["rewritable_same"],
            cases["rewritable_same_copy"],
        ),
        _pair_audit(
            "resource_accounting_control",
            cases["rewritable_same"],
            cases["rewritable_two_bit_resource"],
        ),
        _pair_audit(
            "provenance_completion_control",
            cases["rewritable_same"],
            cases["rewritable_invalid_provenance"],
        ),
        _pair_audit(
            "control_completion_control",
            cases["rewritable_same"],
            cases["rewritable_disabled_control"],
        ),
        _pair_audit(
            "boundary_completion_control",
            cases["rewritable_same"],
            cases["rewritable_closed_boundary"],
        ),
        _pair_audit(
            "hidden_label_shortcut_control",
            cases["hidden_alpha"],
            cases["hidden_beta"],
        ),
        _pair_audit(
            "stipulated_finality_label_control",
            cases["stipulated_provisional"],
            cases["stipulated_sealed"],
        ),
    ]


def _absorber_audit(main_pair: dict[str, Any]) -> dict[str, Any]:
    return {
        "causal_reachability_and_domain_of_dependence": {
            "status": "matched_not_explanatory",
            "reason": (
                "The main pair imports the same T403/T402 causal-domain "
                "signature, so causal reachability does not separate the "
                "revision capability."
            ),
        },
        "ordinary_joint_input_completion": {
            "status": "matched_not_explanatory",
            "reason": (
                "The main pair has the same joint payload and verdict payload."
            ),
        },
        "stipulated_finality_state": {
            "status": "blocked",
            "reason": (
                "Accepted finality labels are not used by the capability "
                "function; the lock state is derived from latch topology."
            ),
        },
        "fixed_accounting_resource_provenance_control_boundary": {
            "status": "matched_not_explanatory_for_main_pair",
            "reason": (
                "The T145-style absorber vector is identical in the main pair; "
                "resource, provenance, reversible-control, and observer-boundary "
                "variation are isolated as controls."
            ),
        },
        "physical_latch_substrate_completion": {
            "status": "absorbs",
            "reason": (
                "Adding the finite latch topology and seal-bridge state "
                "restores factorization of the revision capability."
            ),
            "main_pair_completion_differences": main_pair[
                "latch_substrate_completion"
            ]["differing_fields"],
        },
        "hidden_label_or_class_marker": {
            "status": "blocked",
            "reason": (
                "A source label can separate only as an extra hidden marker; it "
                "is not accepted as latch-substrate or fixed-accounting evidence."
            ),
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": (
                "The artifact supplies a finite latch-substrate absorber screen, "
                "not a physical-arrow theorem or claim-status change."
            ),
        },
    }


def run_physical_latch_finality_lock_screen() -> dict[str, Any]:
    audits = _pair_audits()
    main_pair = next(
        audit
        for audit in audits
        if audit["pair_id"] == "physical_latch_finality_lock_pair"
    )
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "source_artifact": SOURCE_ARTIFACT,
        "setup": {
            "task": (
                "given a common-future final verdict with fixed causal-domain "
                "data, fixed joint payload, and fixed accounting, decide "
                "whether the verdict can still be physically rewritten"
            ),
            "visible_projection": (
                "T403 causal-domain signature + joint payload + verdict payload"
            ),
            "fixed_accounting_projection": (
                "visible projection + revision budget + operation menu + "
                "T145-style absorber vector + latch support without topology"
            ),
            "capability_object": (
                "future operation availability for reading, appending, "
                "revising, and certifying the final verdict"
            ),
            "declared_before_pair": True,
            "lock_state_source": "derived from finite latch topology, not an accepted label",
        },
        "causal_domain_signature": _causal_domain_signature(),
        "pair_audits": audits,
        "main_pair_summary": {
            "pair_id": main_pair["pair_id"],
            "visible_causal_payload_equal": main_pair[
                "visible_causal_payload_equal"
            ],
            "fixed_accounting_projection_equal": main_pair[
                "fixed_accounting_projection_equal"
            ],
            "same_joint_payload": main_pair["same_joint_payload"],
            "same_operation_menu": main_pair["same_operation_menu"],
            "same_revision_budget": main_pair["same_revision_budget"],
            "same_latch_support_without_topology": main_pair[
                "same_latch_support_without_topology"
            ],
            "absorber_mismatch_fields": main_pair["absorber_mismatch_fields"],
            "derived_lock_states": main_pair["derived_lock_states"],
            "capability_split": main_pair["capability"]["differs"],
            "differing_capability_fields": main_pair["capability"][
                "differing_fields"
            ],
            "residue_label": main_pair["residue_label"],
        },
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
        "residue_label": "physical_latch_substrate_split_absorbed",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat T405 as a latch-substrate absorber screen, not a claim upgrade.",
            "Do not count a finite fused latch as physical-arrow evidence.",
            "A future upgrade needs a substrate-native irreversibility or operation-unavailability result that does not factor through explicit latch, resource, provenance, control, or boundary state.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_physical_latch_finality_lock_screen(),
            indent=2,
            sort_keys=True,
        )
    )
