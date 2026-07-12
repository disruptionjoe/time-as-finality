"""T533 - C(R) surplus starter packet classifier.

T533 starts the TAF2 lane after T529. It is a deterministic screen for future
C(R)-surplus packets over the completed competency/resource/permission/
provenance stack.

The classifier does not prove a region-indexed discriminator success. It only
checks whether a candidate packet has exact matched certificates for the full
stack plus a predeclared independent noncompletion witness for a
non-task-success capability.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import competency_resource_permission_stack_gate as t500
from models import competency_surplus_admission_gate as t529


ARTIFACT = "T533-cr-surplus-starter-packet-classifier-v0.1"
VERDICT = "CR_SURPLUS_STARTER_CLASSIFIER_BUILT_REVIEW_ONLY_NO_SUCCESS"

SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T500 = "results/T500-competency-resource-permission-stack-gate-v0.1-results.md"
SOURCE_T529 = "results/T529-competency-surplus-admission-gate-v0.1-results.md"

STACK_LAYERS = (
    "full_competency_profile",
    "resource_profile",
    "permission_profile",
    "provenance_profile",
)

HONEST_CEILING = (
    "T533 is a starter classifier and review gate only. It does not instantiate "
    "a successful C(R) surplus packet, does not prove a region-indexed "
    "discriminator, does not prove surplus over competency/resource completion, "
    "and does not move claim status, Canon Index tiers, canon verdicts, "
    "roadmap, README, North Star, public posture, hard policy, external "
    "publication, or cross-repo truth."
)

READING = (
    "Post-T529 C(R) surplus requires more than flat simple statistics and more "
    "than a completed resource account. A future packet must match the full "
    "competency, resource, permission, and provenance profiles while supplying "
    "an independent noncompletion witness for a capability that is not merely "
    "another task-success coordinate. T533 makes that burden reproducible as a "
    "classifier over packet shapes."
)


@dataclass(frozen=True)
class ProfileCertificate:
    layer: str
    left_profile: tuple[str, ...]
    right_profile: tuple[str, ...]
    certificate_source: str

    @property
    def exact_match(self) -> bool:
        return self.left_profile == self.right_profile


@dataclass(frozen=True)
class NoncompletionWitness:
    witness_id: str
    capability_kind: str
    left_value: str
    right_value: str
    predeclared: bool
    domain_native: bool
    independent_from_stack_profiles: bool
    not_task_success_coordinate: bool
    not_completion_field: bool

    @property
    def splits(self) -> bool:
        return self.left_value != self.right_value


@dataclass(frozen=True)
class Packet:
    packet_id: str
    description: str
    fixed_region_menu_task_context: bool
    checks_t500_t529_floor: bool
    competency: ProfileCertificate | None
    resource: ProfileCertificate | None
    permission: ProfileCertificate | None
    provenance: ProfileCertificate | None
    witness: NoncompletionWitness | None
    uses_simple_observed_statistic: bool = False
    declares_match_without_certificate: bool = False
    full_profile_equivalent: bool = False
    claims_current_success: bool = False
    requests_claim_or_canon_movement: bool = False
    requests_public_or_cross_repo_movement: bool = False


@dataclass(frozen=True)
class Classification:
    packet_id: str
    admitted: bool
    label: str
    action: str
    stack_complete: bool
    residual_survives_stack: bool
    missing_layers: tuple[str, ...]
    reason: str


def _certificate(layer: str, values: tuple[str, ...]) -> ProfileCertificate:
    return ProfileCertificate(
        layer=layer,
        left_profile=values,
        right_profile=values,
        certificate_source=f"synthetic_exact_{layer}_match_certificate",
    )


def _unmatched_certificate(
    layer: str,
    left: tuple[str, ...],
    right: tuple[str, ...],
) -> ProfileCertificate:
    return ProfileCertificate(
        layer=layer,
        left_profile=left,
        right_profile=right,
        certificate_source=f"synthetic_unmatched_{layer}_control",
    )


def absorber_floor() -> dict[str, Any]:
    t500_payload = t500.run()
    t529_payload = t529.run()
    return {
        "t500_verdict": t500_payload["verdict"],
        "t500_current_full_stack_absorbed": t500_payload["overall"][
            "current_c_r_full_stack_absorbed"
        ],
        "t500_current_residual_survives_full_stack": t500_payload["overall"][
            "current_c_r_residual_survives_full_stack"
        ],
        "t500_synthetic_residual_review_only": t500_payload["overall"][
            "synthetic_full_stack_residual_admitted_for_review"
        ],
        "t529_verdict": t529_payload["overall_verdict"]["verdict"],
        "t529_synthetic_future_target_admitted": t529_payload["overall_verdict"][
            "synthetic_future_review_target_admitted"
        ],
        "t529_current_success": t529_payload["overall_verdict"][
            "current_discriminator_success"
        ],
        "t529_claim_movement": t529_payload["overall_verdict"]["claim_movement"],
        "t529_canon_or_public_posture_movement": t529_payload["overall_verdict"][
            "canon_or_public_posture_movement"
        ],
    }


def packets() -> tuple[Packet, ...]:
    matched_competency = _certificate(
        "full_competency_profile",
        ("reconcile=1", "revise=1", "postdict=1", "recover=1"),
    )
    matched_resource = _certificate(
        "resource_profile",
        ("energy_budget=matched", "reference_access=matched", "conversion_order=matched"),
    )
    matched_permission = _certificate(
        "permission_profile",
        ("read=matched", "write=matched", "revise=matched", "boundary=matched"),
    )
    matched_provenance = _certificate(
        "provenance_profile",
        ("raw_log=matched", "source_chain=matched", "calibration=matched"),
    )
    noncompletion = NoncompletionWitness(
        witness_id="synthetic_non_task_success_noncompletion_axis",
        capability_kind="non_task_success_operation_availability",
        left_value="completion_blocked",
        right_value="completion_available",
        predeclared=True,
        domain_native=True,
        independent_from_stack_profiles=True,
        not_task_success_coordinate=True,
        not_completion_field=True,
    )

    return (
        Packet(
            packet_id="simple_statistic_flatness_packet",
            description="Flat simple observed statistics with no full-stack match.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=None,
            resource=None,
            permission=None,
            provenance=None,
            witness=None,
            uses_simple_observed_statistic=True,
        ),
        Packet(
            packet_id="full_profile_equivalent_task_success_packet",
            description="A packet whose alleged residual is another task-success coordinate.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=matched_competency,
            resource=matched_resource,
            permission=matched_permission,
            provenance=matched_provenance,
            witness=NoncompletionWitness(
                witness_id="task_success_coordinate",
                capability_kind="task_success_coordinate",
                left_value="task_pass",
                right_value="task_fail",
                predeclared=True,
                domain_native=True,
                independent_from_stack_profiles=False,
                not_task_success_coordinate=False,
                not_completion_field=True,
            ),
            full_profile_equivalent=True,
        ),
        Packet(
            packet_id="declared_only_completion_packet",
            description="A packet declaring full-stack equality without reproducible certificates.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=None,
            resource=None,
            permission=None,
            provenance=None,
            witness=noncompletion,
            declares_match_without_certificate=True,
        ),
        Packet(
            packet_id="resource_only_completion_packet",
            description="A resource-matched packet omitting competency, permission, and provenance completion.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=None,
            resource=matched_resource,
            permission=None,
            provenance=None,
            witness=noncompletion,
        ),
        Packet(
            packet_id="unmatched_permission_control_packet",
            description="A nominal packet whose permission profiles do not match.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=matched_competency,
            resource=matched_resource,
            permission=_unmatched_certificate(
                "permission_profile",
                ("read=matched", "write=left_only"),
                ("read=matched", "write=right_only"),
            ),
            provenance=matched_provenance,
            witness=noncompletion,
        ),
        Packet(
            packet_id="post_hoc_noncompletion_packet",
            description="A full-stack-matched packet with a split but no independent witness.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=matched_competency,
            resource=matched_resource,
            permission=matched_permission,
            provenance=matched_provenance,
            witness=NoncompletionWitness(
                witness_id="post_hoc_hidden_axis",
                capability_kind="non_task_success_operation_availability",
                left_value="blocked",
                right_value="available",
                predeclared=False,
                domain_native=True,
                independent_from_stack_profiles=False,
                not_task_success_coordinate=True,
                not_completion_field=False,
            ),
        ),
        Packet(
            packet_id="synthetic_future_noncompletion_review_target",
            description=(
                "A future-target shape with exact full-stack profile matches "
                "and an independent non-task-success noncompletion witness."
            ),
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=matched_competency,
            resource=matched_resource,
            permission=matched_permission,
            provenance=matched_provenance,
            witness=noncompletion,
        ),
        Packet(
            packet_id="claim_or_public_posture_shortcut",
            description="A packet asking the classifier to move claims or public posture.",
            fixed_region_menu_task_context=True,
            checks_t500_t529_floor=True,
            competency=matched_competency,
            resource=matched_resource,
            permission=matched_permission,
            provenance=matched_provenance,
            witness=noncompletion,
            claims_current_success=True,
            requests_claim_or_canon_movement=True,
            requests_public_or_cross_repo_movement=True,
        ),
    )


def _profile_map(packet: Packet) -> dict[str, ProfileCertificate | None]:
    return {
        "full_competency_profile": packet.competency,
        "resource_profile": packet.resource,
        "permission_profile": packet.permission,
        "provenance_profile": packet.provenance,
    }


def missing_layers(packet: Packet) -> tuple[str, ...]:
    missing: list[str] = []
    for layer, certificate in _profile_map(packet).items():
        if certificate is None or not certificate.exact_match:
            missing.append(layer)
    return tuple(missing)


def witness_is_admissible(witness: NoncompletionWitness | None) -> bool:
    if witness is None:
        return False
    return (
        witness.splits
        and witness.predeclared
        and witness.domain_native
        and witness.independent_from_stack_profiles
        and witness.not_task_success_coordinate
        and witness.not_completion_field
    )


def classify(packet: Packet, floor: dict[str, Any]) -> Classification:
    missing = missing_layers(packet)
    stack_complete = not missing
    witness_admissible = witness_is_admissible(packet.witness)
    residual_survives = stack_complete and witness_admissible

    if (
        packet.claims_current_success
        or packet.requests_claim_or_canon_movement
        or packet.requests_public_or_cross_repo_movement
    ):
        return Classification(
            packet.packet_id,
            False,
            "BLOCKED_GOVERNANCE_OR_POSTURE_SHORTCUT",
            "stop",
            stack_complete,
            False,
            missing,
            "T533 cannot move claims, canon, public posture, external publication, or cross-repo truth.",
        )
    if floor["t529_current_success"] or floor["t529_claim_movement"]:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_UNEXPECTED_ABSORBER_FLOOR_STATE",
            "reject",
            stack_complete,
            False,
            missing,
            "The T529 floor must remain review-only with no current success or claim movement.",
        )
    if not packet.checks_t500_t529_floor:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_MISSING_T500_T529_FLOOR",
            "reject",
            stack_complete,
            False,
            missing,
            "Post-T529 packets must explicitly consume the T500 and T529 floors.",
        )
    if not packet.fixed_region_menu_task_context:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_UNFIXED_REGION_MENU_TASK_CONTEXT",
            "reject",
            stack_complete,
            False,
            missing,
            "Region, menu, task family, observer, and boundary must be fixed before pair selection.",
        )
    if packet.uses_simple_observed_statistic:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_SIMPLE_STATISTIC_NOT_FULL_STACK_SURPLUS",
            "reject",
            stack_complete,
            False,
            missing,
            "Flat simple statistics are not surplus over the completed profile stack.",
        )
    if packet.declares_match_without_certificate:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_DECLARED_ONLY_NO_REPRODUCIBLE_CERTIFICATES",
            "reject",
            stack_complete,
            False,
            missing,
            "Declared equality without exact profile certificates is not a matched-stack packet.",
        )
    if not stack_complete:
        resource_only = (
            packet.resource is not None
            and packet.resource.exact_match
            and packet.competency is None
            and packet.permission is None
            and packet.provenance is None
        )
        if resource_only:
            label = "REJECTED_RESOURCE_ONLY_INCOMPLETE_COMPLETION_STACK"
        else:
            label = "REJECTED_INCOMPLETE_COMPLETION_STACK"
        return Classification(
            packet.packet_id,
            False,
            label,
            "reject",
            False,
            False,
            missing,
            "Every competency, resource, permission, and provenance profile must match exactly.",
        )
    if packet.full_profile_equivalent:
        return Classification(
            packet.packet_id,
            False,
            "ABSORBED_FULL_PROFILE_EQUIVALENT_TASK_SUCCESS_COORDINATE",
            "absorb",
            True,
            False,
            missing,
            "A task-success coordinate is already contained in the full competency profile.",
        )
    if packet.witness is None or not packet.witness.splits:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_NO_NONCOMPLETION_SPLIT",
            "reject",
            True,
            False,
            missing,
            "A surplus packet must split a noncompletion capability after the full stack matches.",
        )
    if not witness_admissible:
        return Classification(
            packet.packet_id,
            False,
            "REJECTED_NONCOMPLETION_WITNESS_NOT_INDEPENDENT",
            "reject",
            True,
            False,
            missing,
            "The witness must be predeclared, domain-native, independent from stack profiles, and not a completion field.",
        )
    return Classification(
        packet.packet_id,
        True,
        "ADMITTED_SYNTHETIC_FUTURE_REVIEW_TARGET_NO_SUCCESS",
        "review_only",
        True,
        True,
        missing,
        "The packet shape clears the starter screen, but T533 supplies no real packet and no C(R) success.",
    )


def claim_table() -> tuple[dict[str, str], ...]:
    return (
        {
            "claim": "T500 and T529 floors remain review-only and report no current C(R) success.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": "Read directly from t500.run() and t529.run().",
        },
        {
            "claim": "Simple-statistic, declared-only, full-profile-equivalent, and resource-only packets fail this screen.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": "Deterministic classifier labels over built-in negative controls.",
        },
        {
            "claim": "The synthetic future packet is admissible only as review-only and not as current success.",
            "status": "COMPUTED",
            "confidence": "high",
            "basis": "Deterministic classifier label and overall flags.",
        },
        {
            "claim": "This classifier is the right starter screen for TAF2 after T529.",
            "status": "ARGUED",
            "confidence": "medium",
            "basis": "It operationalizes the T500/T529 burdens but does not test a real domain packet.",
        },
    )


def run() -> dict[str, Any]:
    floor = absorber_floor()
    packet_list = packets()
    classifications = [classify(packet, floor) for packet in packet_list]
    admitted = [item.packet_id for item in classifications if item.admitted]
    synthetic_admitted = admitted == ["synthetic_future_noncompletion_review_target"]
    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "sources": {
            "open_problem": SOURCE_OPEN_PROBLEM,
            "t500": SOURCE_T500,
            "t529": SOURCE_T529,
        },
        "stack_layers": list(STACK_LAYERS),
        "reading": READING,
        "honest_ceiling": HONEST_CEILING,
        "absorber_floor": floor,
        "packets": [asdict(packet) for packet in packet_list],
        "classifications": [asdict(item) for item in classifications],
        "claim_table": list(claim_table()),
        "overall": {
            "admitted_packet_ids": admitted,
            "only_synthetic_future_target_admitted": synthetic_admitted,
            "current_c_r_success": False,
            "surplus_over_full_stack_proved": False,
            "review_target_only": True,
            "claim_movement": False,
            "canon_or_public_posture_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "recommended_next": (
            "Use T533 as the first post-T529 TAF2 starter screen. A later run "
            "may replace the synthetic future target with a real domain packet "
            "only if exact full-stack profile certificates and an independent "
            "noncompletion witness are supplied before pair selection."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {action} | {stack} | {residual} | {missing} | {reason} |".format(
            packet_id=item["packet_id"],
            admitted="yes" if item["admitted"] else "no",
            label=item["label"],
            action=item["action"],
            stack="yes" if item["stack_complete"] else "no",
            residual="yes" if item["residual_survives_stack"] else "no",
            missing=", ".join(item["missing_layers"]) or "none",
            reason=item["reason"],
        )
        for item in payload["classifications"]
    ]
    claims = [
        "| {status} | {confidence} | {claim} | {basis} |".format(**item)
        for item in payload["claim_table"]
    ]
    floor = payload["absorber_floor"]
    return "\n".join(
        [
            "# T533 - C(R) Surplus Starter Packet Classifier - v0.1 results",
            "",
            "> Starter classifier and review gate only. No claim-ledger, Canon Index, canon verdict, roadmap, README, North Star, public-posture, hard-policy, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T533-cr-surplus-starter-packet-classifier.md`",
            "- Model: `models/t533_cr_surplus_starter_packet_classifier.py`",
            "- Tests: `tests/test_t533_cr_surplus_starter_packet_classifier.py`",
            "- Artifact JSON: `results/T533-cr-surplus-starter-packet-classifier-v0.1.json`",
            "- Floors: T500 and T529",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["reading"],
            "",
            "## Absorber Floor",
            "",
            "| Check | Value |",
            "| --- | --- |",
            f"| T500 verdict | {floor['t500_verdict']} |",
            f"| T500 current full stack absorbed | {floor['t500_current_full_stack_absorbed']} |",
            f"| T500 current residual survives full stack | {floor['t500_current_residual_survives_full_stack']} |",
            f"| T529 verdict | {floor['t529_verdict']} |",
            f"| T529 current success | {floor['t529_current_success']} |",
            f"| T529 claim movement | {floor['t529_claim_movement']} |",
            "",
            "## Packet Classifications",
            "",
            "| Packet | Admitted? | Label | Action | Full stack? | Residual survives? | Missing layers | Reason |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Claims",
            "",
            "| Status | Confidence | Claim | Basis |",
            "| --- | --- | --- | --- |",
            *claims,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a reproducible starter screen for post-T529 C(R) surplus packets over the completed competency/resource/permission/provenance stack.",
            "",
            "Does not earn: a current C(R) success, surplus over the full stack, a region-indexed discriminator, claim movement, canon movement, public posture, external publication, or cross-repo truth.",
            "",
            f"Honest ceiling: {payload['honest_ceiling']}",
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args()

    payload = run()
    if args.write_results:
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)
        json_path = results_dir / "T533-cr-surplus-starter-packet-classifier-v0.1.json"
        md_path = results_dir / "T533-cr-surplus-starter-packet-classifier-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
