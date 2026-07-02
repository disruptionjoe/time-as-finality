"""T403: Same-domain finality-lock screen.

T402 showed that a physically forced boundary task can still be absorbed by
ordinary causal-domain completion plus joint input access. T403 tests the next
constraint: keep the causal-domain data and joint payload fixed, then ask
whether a capability split can live only in record-finality state.

The conservative result is absorptive. A provisional and sealed record can
share the same causal domain, same joint payload, same verdict payload, same
revision budget, and same declared operation menu while splitting on whether
the final verdict can be revised. That split is not causal reachability or
joint input completion, but it is absorbed by explicit finality-state
completion. No claim promotion follows.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Any

from models.causal_domain_boundary_forcing_screen import (
    run_causal_domain_boundary_forcing_screen,
)


ARTIFACT = "T403-same-domain-finality-lock-screen-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_ARTIFACT = "T402-causal-domain-boundary-forcing-screen-v0.1"

DEFAULT_OPERATION_MENU = (
    "read_verdict",
    "append_correction",
    "revise_verdict",
)

VERDICT = (
    "finite same-causal-domain finality-state screen built: a provisional and "
    "sealed record have identical causal-domain data, joint payload, verdict "
    "payload, revision budget, and declared operation menu, while only the "
    "provisional record can revise the final verdict; the split is not causal "
    "reachability or joint input completion, but is absorbed by explicit "
    "finality-state completion, so no claim-ledger movement is earned"
)

FALSIFICATION_CONDITION = (
    "This screen would fail if the main pair differed in causal-domain data, "
    "joint payload, revision budget, or operation menu; if the revision split "
    "survived after finality-state completion; if a hidden label performed the "
    "separation; or if the finite lock state were treated as a physical claim."
)


@dataclass(frozen=True)
class RecordCase:
    case_id: str
    joint_payload: tuple[int, int]
    finality_state: str
    revision_budget: int = 1
    operation_menu: tuple[str, ...] = DEFAULT_OPERATION_MENU
    hidden_source_label: str | None = None


def _verdict_payload(joint_payload: tuple[int, int]) -> str:
    return "same" if joint_payload[0] == joint_payload[1] else "different"


def _causal_domain_signature() -> dict[str, Any]:
    t402 = run_causal_domain_boundary_forcing_screen()
    geometry = t402["causal_geometry"]
    return {
        "source_artifact": t402["artifact"],
        "events": geometry["events"],
        "initial_data_intervals": geometry["initial_data_intervals"],
        "R_and_B_are_spacelike": geometry["R_and_B_are_spacelike"],
        "verdict_in_common_future": geometry["verdict_in_common_future"],
        "R_only_domain_contains_verdict": geometry["R_only_domain_contains_verdict"],
        "B_only_domain_contains_verdict": geometry["B_only_domain_contains_verdict"],
        "RB_joint_domain_contains_verdict": geometry[
            "RB_joint_domain_contains_verdict"
        ],
    }


def _visible_causal_payload_projection(case: RecordCase) -> dict[str, Any]:
    return {
        "causal_domain_signature": _causal_domain_signature(),
        "joint_payload": list(case.joint_payload),
        "verdict_payload": _verdict_payload(case.joint_payload),
    }


def _finality_state_completion(case: RecordCase) -> dict[str, Any]:
    return {
        "visible_projection": _visible_causal_payload_projection(case),
        "finality_state": case.finality_state,
        "revision_budget": case.revision_budget,
        "operation_menu": list(case.operation_menu),
    }


def _capability(case: RecordCase) -> dict[str, Any]:
    return {
        "verdict_payload": _verdict_payload(case.joint_payload),
        "can_read_verdict": "read_verdict" in case.operation_menu,
        "can_append_correction": "append_correction" in case.operation_menu,
        "can_revise_final_verdict": (
            case.finality_state == "provisional"
            and case.revision_budget > 0
            and "revise_verdict" in case.operation_menu
        ),
    }


def _differing_fields(left: dict[str, Any], right: dict[str, Any]) -> list[str]:
    return [key for key in left if left[key] != right.get(key)]


def _residue_label(
    left: RecordCase,
    right: RecordCase,
    same_visible_projection: bool,
    same_operation_menu: bool,
    capability_split: bool,
    shortcut_attempt: bool,
) -> str:
    if shortcut_attempt:
        return "blocked_hidden_label_shortcut"
    if not same_visible_projection:
        return "absorbed_by_causal_or_joint_input_completion"
    if not same_operation_menu:
        return "absorbed_by_operation_menu_completion"
    if capability_split and left.finality_state != right.finality_state:
        return "absorbed_by_finality_state_completion"
    if capability_split:
        return "unclassified_same_domain_split_requires_review"
    return "no_capability_split"


def _pair_audit(pair_id: str, left: RecordCase, right: RecordCase) -> dict[str, Any]:
    left_projection = _visible_causal_payload_projection(left)
    right_projection = _visible_causal_payload_projection(right)
    left_completion = _finality_state_completion(left)
    right_completion = _finality_state_completion(right)
    left_capability = _capability(left)
    right_capability = _capability(right)
    same_visible_projection = left_projection == right_projection
    same_operation_menu = left.operation_menu == right.operation_menu
    capability_differences = _differing_fields(left_capability, right_capability)
    completion_differences = _differing_fields(left_completion, right_completion)
    shortcut_attempt = (
        left.hidden_source_label is not None
        or right.hidden_source_label is not None
    ) and left.hidden_source_label != right.hidden_source_label

    return {
        "pair_id": pair_id,
        "left": asdict(left),
        "right": asdict(right),
        "visible_projection_equal": same_visible_projection,
        "same_causal_domain_data": (
            left_projection["causal_domain_signature"]
            == right_projection["causal_domain_signature"]
        ),
        "same_joint_payload": left.joint_payload == right.joint_payload,
        "same_verdict_payload": (
            _verdict_payload(left.joint_payload)
            == _verdict_payload(right.joint_payload)
        ),
        "same_revision_budget": left.revision_budget == right.revision_budget,
        "same_operation_menu": same_operation_menu,
        "capability": {
            "left": left_capability,
            "right": right_capability,
            "differs": bool(capability_differences),
            "differing_fields": capability_differences,
        },
        "state_completion": {
            "left": left_completion,
            "right": right_completion,
            "restores_factorization": (
                bool(capability_differences) and bool(completion_differences)
            )
            or not capability_differences,
            "differing_fields": completion_differences,
        },
        "hidden_label_shortcut_attempt": shortcut_attempt,
        "residue_label": _residue_label(
            left,
            right,
            same_visible_projection,
            same_operation_menu,
            bool(capability_differences),
            shortcut_attempt,
        ),
    }


def _record_cases() -> dict[str, RecordCase]:
    return {
        "provisional_same": RecordCase(
            case_id="provisional_same",
            joint_payload=(1, 1),
            finality_state="provisional",
        ),
        "sealed_same": RecordCase(
            case_id="sealed_same",
            joint_payload=(1, 1),
            finality_state="sealed",
        ),
        "provisional_same_copy": RecordCase(
            case_id="provisional_same_copy",
            joint_payload=(1, 1),
            finality_state="provisional",
        ),
        "provisional_different": RecordCase(
            case_id="provisional_different",
            joint_payload=(1, 0),
            finality_state="provisional",
        ),
        "provisional_without_revision_menu": RecordCase(
            case_id="provisional_without_revision_menu",
            joint_payload=(1, 1),
            finality_state="provisional",
            operation_menu=("read_verdict", "append_correction"),
        ),
        "hidden_alpha": RecordCase(
            case_id="hidden_alpha",
            joint_payload=(1, 1),
            finality_state="provisional",
            hidden_source_label="alpha",
        ),
        "hidden_beta": RecordCase(
            case_id="hidden_beta",
            joint_payload=(1, 1),
            finality_state="provisional",
            hidden_source_label="beta",
        ),
    }


def _pair_audits() -> list[dict[str, Any]]:
    cases = _record_cases()
    return [
        _pair_audit(
            "same_domain_finality_lock_pair",
            cases["provisional_same"],
            cases["sealed_same"],
        ),
        _pair_audit(
            "matched_finality_control",
            cases["provisional_same"],
            cases["provisional_same_copy"],
        ),
        _pair_audit(
            "joint_input_completion_control",
            cases["provisional_same"],
            cases["provisional_different"],
        ),
        _pair_audit(
            "operation_menu_completion_control",
            cases["provisional_same"],
            cases["provisional_without_revision_menu"],
        ),
        _pair_audit(
            "hidden_label_shortcut_control",
            cases["hidden_alpha"],
            cases["hidden_beta"],
        ),
    ]


def _absorber_audit(main_pair: dict[str, Any]) -> dict[str, Any]:
    return {
        "causal_reachability_and_domain_of_dependence": {
            "status": "matched_not_explanatory",
            "reason": (
                "The main pair shares the same T402 causal-domain signature, "
                "so reachability and domain-of-dependence data do not separate "
                "the revision capability."
            ),
        },
        "ordinary_joint_input_completion": {
            "status": "matched_not_explanatory",
            "reason": (
                "The main pair has the same joint payload and same verdict "
                "payload, so ordinary joint input completion does not separate "
                "the revision capability."
            ),
        },
        "operation_menu_completion": {
            "status": "matched_not_explanatory_for_main_pair",
            "reason": (
                "The declared operation menu and revision budget are identical "
                "in the main pair; operation-menu variation is isolated as a "
                "separate absorber control."
            ),
        },
        "finality_state_completion": {
            "status": "absorbs",
            "reason": (
                "Adding the provisional/sealed record-finality state restores "
                "factorization of the revision capability."
            ),
            "main_pair_completion_differences": main_pair["state_completion"][
                "differing_fields"
            ],
        },
        "hidden_label_or_class_marker": {
            "status": "blocked",
            "reason": (
                "A source label can separate only as an extra hidden marker; it "
                "is not accepted as causal-domain, joint-input, or finality "
                "state evidence."
            ),
        },
        "claim_promotion": {
            "status": "blocked",
            "reason": (
                "The artifact supplies a finite finality-state absorber screen, "
                "not a physical-substrate result or claim-status change."
            ),
        },
    }


def run_same_domain_finality_lock_screen() -> dict[str, Any]:
    audits = _pair_audits()
    main_pair = next(
        audit
        for audit in audits
        if audit["pair_id"] == "same_domain_finality_lock_pair"
    )
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "source_artifact": SOURCE_ARTIFACT,
        "setup": {
            "task": (
                "given a common-future final verdict with fixed causal-domain "
                "data and fixed joint payload, decide whether the verdict can "
                "still be revised before the horizon"
            ),
            "visible_projection": (
                "T402 causal-domain signature + joint payload + verdict payload"
            ),
            "capability_object": (
                "future operation availability for reading, appending a "
                "correction, and revising the final verdict"
            ),
            "declared_before_pair": True,
        },
        "causal_domain_signature": _causal_domain_signature(),
        "pair_audits": audits,
        "main_pair_summary": {
            "pair_id": main_pair["pair_id"],
            "visible_projection_equal": main_pair["visible_projection_equal"],
            "same_causal_domain_data": main_pair["same_causal_domain_data"],
            "same_joint_payload": main_pair["same_joint_payload"],
            "same_operation_menu": main_pair["same_operation_menu"],
            "same_revision_budget": main_pair["same_revision_budget"],
            "capability_split": main_pair["capability"]["differs"],
            "differing_capability_fields": main_pair["capability"][
                "differing_fields"
            ],
            "residue_label": main_pair["residue_label"],
        },
        "absorber_audit": _absorber_audit(main_pair),
        "summary": {
            "same_domain_split_cases": [
                audit["pair_id"]
                for audit in audits
                if audit["visible_projection_equal"]
                and audit["same_operation_menu"]
                and audit["same_revision_budget"]
                and audit["capability"]["differs"]
            ],
            "absorbed_cases": {
                audit["pair_id"]: audit["residue_label"] for audit in audits
            },
        },
        "verdict": VERDICT,
        "residue_label": "same_domain_finality_state_split_absorbed",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat T403 as a finality-state absorber screen, not a claim upgrade.",
            "Do not count sealed/provisional state as a hidden causal-domain discriminator.",
            "A future upgrade needs a physically typed finality-lock substrate whose state is not merely stipulated.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(
        json.dumps(
            run_same_domain_finality_lock_screen(),
            indent=2,
            sort_keys=True,
        )
    )
