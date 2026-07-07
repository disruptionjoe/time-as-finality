"""T500 - competency/resource/permission/provenance stack gate.

The fourth composite absorber-stack lane asks whether C(R)-style residue
survives after the strongest native completion stack is granted:

full competency profile + resource preorder + permission lattice + provenance.

This gate keeps the current reading conservative. The present T493/T494 C(R)
line is absorbed as a composite operational profile once the full stack is
granted. Only a packet that still shows capability spread after every layer is
declared earns future review-target status.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ARTIFACT = "T500-competency-resource-permission-stack-gate-v0.1"
VERDICT = "COMPETENCY_RESOURCE_PERMISSION_STACK_BUILT_NO_RESIDUAL_AFTER_FULL_STACK"

SOURCE_PROGRESS_LANES = "open-problems/composite-absorber-stack-progress-lanes.md"
SOURCE_REGION_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
SOURCE_T493 = "results/T493-levin-competency-cr-absorber-gate-v0.1-results.md"
SOURCE_T494 = "results/T494-levin-fields-primary-source-absorber-gate-v0.1-results.md"
SOURCE_T497 = "results/T497-bounded-retrieval-source-checked-stack-gate-v0.1-results.md"
SOURCE_T498 = "results/T498-authoritative-commit-settlement-stack-gate-v0.1-results.md"
SOURCE_T499 = "results/T499-kappa-composite-residual-template-gate-v0.1-results.md"

STACK_LAYERS = (
    "full_competency_profile",
    "resource_preorder",
    "permission_lattice",
    "provenance_completion",
)

HONEST_CEILING = (
    "T500 is a composite explanation and admission gate only. It does not "
    "prove a new C(R) primitive, does not prove a region-indexed discriminator, "
    "does not import Levin/Fields mechanisms into TaF, and does not move claim "
    "ledger, roadmap, README, North Star, public posture, hard policy, "
    "protected license, external publication, or cross-repo truth."
)

READING = (
    "The current C(R) material is best treated as a composite operational "
    "profile when the full stack is granted: intervention-measured competency "
    "profile, resource preorder, permission lattice, and provenance completion. "
    "Weak readings that keep only a single success statistic, a resource order, "
    "a permission boundary, or provenance cannot carry the full C(R) burden. A "
    "future residual packet must show non-singleton capability spread after all "
    "four layers are declared and controlled."
)


@dataclass(frozen=True)
class StackPacket:
    packet_id: str
    description: str
    grants_full_competency_profile: bool
    grants_resource_preorder: bool
    grants_permission_lattice: bool
    grants_provenance_completion: bool
    declares_region_menu_task_context: bool
    native_positive_controls: bool
    capability_spread_after_stack: int
    uses_single_observed_success_statistic: bool = False
    imports_external_mechanism: bool = False
    claim_or_public_posture_requested: bool = False
    external_publication_requested: bool = False
    cross_repo_truth_requested: bool = False


@dataclass(frozen=True)
class StackDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    full_stack_complete: bool
    residual_survives_full_stack: bool
    missing_layers: tuple[str, ...]
    reason: str


def missing_layers(packet: StackPacket) -> tuple[str, ...]:
    missing: list[str] = []
    if not packet.grants_full_competency_profile:
        missing.append("full_competency_profile")
    if not packet.grants_resource_preorder:
        missing.append("resource_preorder")
    if not packet.grants_permission_lattice:
        missing.append("permission_lattice")
    if not packet.grants_provenance_completion:
        missing.append("provenance_completion")
    return tuple(missing)


def evaluate_packet(packet: StackPacket) -> StackDecision:
    missing = missing_layers(packet)
    full_stack_complete = not missing

    if packet.claim_or_public_posture_requested:
        return StackDecision(
            packet.packet_id,
            False,
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
            "stop",
            full_stack_complete,
            False,
            missing,
            "A stack gate does not authorize claim-ledger or public-posture movement.",
        )
    if packet.external_publication_requested or packet.cross_repo_truth_requested:
        return StackDecision(
            packet.packet_id,
            False,
            "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT",
            "stop",
            full_stack_complete,
            False,
            missing,
            "External publication and cross-repo truth updates are outside this run.",
        )
    if packet.imports_external_mechanism:
        return StackDecision(
            packet.packet_id,
            False,
            "REJECTED_EXTERNAL_MECHANISM_IMPORT",
            "reject",
            full_stack_complete,
            False,
            missing,
            "Competency neighbors calibrate and absorb; they do not import mechanisms into TaF.",
        )
    if packet.uses_single_observed_success_statistic:
        return StackDecision(
            packet.packet_id,
            False,
            "REJECTED_SINGLE_STATISTIC_NOT_FULL_STACK",
            "reject",
            full_stack_complete,
            False,
            missing,
            "T493 already shows a single observed statistic cannot absorb the full C(R) profile.",
        )
    if not packet.declares_region_menu_task_context:
        return StackDecision(
            packet.packet_id,
            False,
            "REJECTED_UNDECLARED_REGION_MENU_TASK_CONTEXT",
            "reject",
            full_stack_complete,
            False,
            missing,
            "The stack is not reviewable until region, menu, and task context are declared.",
        )
    if not full_stack_complete:
        return StackDecision(
            packet.packet_id,
            False,
            "REJECTED_INCOMPLETE_ABSORBER_STACK",
            "reject",
            False,
            False,
            missing,
            "The packet leaves at least one native absorber layer ungranted.",
        )
    if not packet.native_positive_controls:
        return StackDecision(
            packet.packet_id,
            False,
            "REJECTED_MISSING_NATIVE_POSITIVE_CONTROLS",
            "reject",
            True,
            False,
            missing,
            "A full stack still needs native positive controls before review.",
        )

    residual_survives = packet.capability_spread_after_stack > 1
    if residual_survives:
        return StackDecision(
            packet.packet_id,
            True,
            "ADMITTED_FUTURE_REVIEW_TARGET_AFTER_FULL_STACK",
            "review_only",
            True,
            True,
            missing,
            "The packet declares all four layers and still has non-singleton capability spread.",
        )

    return StackDecision(
        packet.packet_id,
        True,
        "ABSORBED_BY_FULL_COMPETENCY_RESOURCE_PERMISSION_PROVENANCE_STACK",
        "record_composite_explanation",
        True,
        False,
        missing,
        "Once all four layers are granted, no residual spread remains in this packet.",
    )


def example_packets() -> tuple[StackPacket, ...]:
    return (
        StackPacket(
            packet_id="current_t493_t494_c_r_full_stack",
            description=(
                "Current C(R) reading after T493/T494: full competency-style "
                "task-success profile plus resource, permission, and provenance completion."
            ),
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=1,
        ),
        StackPacket(
            packet_id="single_success_statistic_reading",
            description="A weak reading that keeps only one observed success statistic.",
            grants_full_competency_profile=False,
            grants_resource_preorder=False,
            grants_permission_lattice=False,
            grants_provenance_completion=False,
            declares_region_menu_task_context=True,
            native_positive_controls=False,
            capability_spread_after_stack=3,
            uses_single_observed_success_statistic=True,
        ),
        StackPacket(
            packet_id="resource_preorder_only",
            description="A resource-order packet that omits competency, permissions, and provenance.",
            grants_full_competency_profile=False,
            grants_resource_preorder=True,
            grants_permission_lattice=False,
            grants_provenance_completion=False,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
        ),
        StackPacket(
            packet_id="permission_boundary_only",
            description="A permission-boundary packet without full task profile or resource order.",
            grants_full_competency_profile=False,
            grants_resource_preorder=False,
            grants_permission_lattice=True,
            grants_provenance_completion=False,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
        ),
        StackPacket(
            packet_id="provenance_completion_only",
            description="A provenance-completion packet without resource and permission context.",
            grants_full_competency_profile=False,
            grants_resource_preorder=False,
            grants_permission_lattice=False,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
        ),
        StackPacket(
            packet_id="synthetic_full_stack_residual_packet",
            description=(
                "A future packet shape that grants all four absorber layers and "
                "still reports a controlled capability spread."
            ),
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
        ),
        StackPacket(
            packet_id="missing_region_menu_task_context",
            description="A nominal full-stack packet that does not declare region, menu, or task.",
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=False,
            native_positive_controls=True,
            capability_spread_after_stack=1,
        ),
        StackPacket(
            packet_id="external_mechanism_import",
            description="A packet that imports external competency mechanism language into TaF.",
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=1,
            imports_external_mechanism=True,
        ),
        StackPacket(
            packet_id="claim_public_posture_shortcut",
            description="A packet that treats the stack as claim or public-posture support.",
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
            claim_or_public_posture_requested=True,
        ),
        StackPacket(
            packet_id="external_or_cross_repo_shortcut",
            description="A packet that tries to publish externally or update another repo.",
            grants_full_competency_profile=True,
            grants_resource_preorder=True,
            grants_permission_lattice=True,
            grants_provenance_completion=True,
            declares_region_menu_task_context=True,
            native_positive_controls=True,
            capability_spread_after_stack=2,
            external_publication_requested=True,
            cross_repo_truth_requested=True,
        ),
    )


def future_packet_minimum() -> tuple[str, ...]:
    return (
        "declare region, menu, task family, observer, and boundary",
        "grant full competency-style task-success profile",
        "grant the resource preorder used for conversion or availability",
        "grant the permission lattice and completion rights",
        "grant provenance, log, or source-completion data",
        "include native positive controls",
        "show non-singleton capability spread after the full stack",
        "declare demotion path if any layer absorbs the spread",
        "stay review-only until a runnable artifact earns a narrower update",
    )


def run() -> dict[str, Any]:
    packets = example_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    current = next(
        decision
        for decision in decisions
        if decision.packet_id == "current_t493_t494_c_r_full_stack"
    )
    synthetic = next(
        decision
        for decision in decisions
        if decision.packet_id == "synthetic_full_stack_residual_packet"
    )

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "sources": {
            "progress_lanes": SOURCE_PROGRESS_LANES,
            "region_open_problem": SOURCE_REGION_OPEN_PROBLEM,
            "t493": SOURCE_T493,
            "t494": SOURCE_T494,
            "t497": SOURCE_T497,
            "t498": SOURCE_T498,
            "t499": SOURCE_T499,
        },
        "stack_layers": list(STACK_LAYERS),
        "reading": READING,
        "honest_ceiling": HONEST_CEILING,
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "future_packet_minimum": list(future_packet_minimum()),
        "overall": {
            "current_c_r_full_stack_absorbed": current.admitted
            and not current.residual_survives_full_stack,
            "current_c_r_residual_survives_full_stack": current.residual_survives_full_stack,
            "synthetic_full_stack_residual_admitted_for_review": synthetic.admitted
            and synthetic.residual_survives_full_stack,
            "review_target_only": True,
            "claim_movement": False,
            "roadmap_movement": False,
            "readme_movement": False,
            "north_star_movement": False,
            "public_posture_movement": False,
            "hard_policy_movement": False,
            "protected_license_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "The current T493/T494 C(R) reading is absorbed as a composite "
            "operational profile once competency, resource preorder, permission "
            "lattice, and provenance completion are all granted. The live route "
            "is not claim movement; it is a stricter admission burden for future "
            "packets that still show controlled capability spread after the full stack."
        ),
        "recommended_next": (
            "Use T500 as the default C(R)-stack screen before reopening the "
            "region-indexed capability discriminator. A future packet should "
            "show the spread that survives the full stack, or demote to a "
            "composite explanation."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    rows = [
        "| {packet_id} | {admitted} | {label} | {full_stack} | {residual} | {missing} | {action} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            full_stack="yes" if decision["full_stack_complete"] else "no",
            residual="yes" if decision["residual_survives_full_stack"] else "no",
            missing=", ".join(decision["missing_layers"]) or "none",
            action=decision["action"],
        )
        for decision in payload["decisions"]
    ]
    minimum = [f"- {item}" for item in payload["future_packet_minimum"]]

    return "\n".join(
        [
            "# T500 - Competency Resource Permission Stack Gate - v0.1 results",
            "",
            "> Composite explanation and admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, protected-license, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T500-competency-resource-permission-stack-gate.md`",
            "- Model: `models/competency_resource_permission_stack_gate.py`",
            "- Tests: `tests/test_competency_resource_permission_stack_gate.py`",
            "- Artifact JSON: `results/T500-competency-resource-permission-stack-gate-v0.1.json`",
            "- Progress lanes: `open-problems/composite-absorber-stack-progress-lanes.md`",
            "- Sources: T493, T494, T497, T498, T499, and the region-indexed capability discriminator open problem",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Stack Reading",
            "",
            payload["reading"],
            "",
            "## Packet Decisions",
            "",
            "| Packet | Admitted? | Label | Full stack? | Residual survives full stack? | Missing layers | Action |",
            "| --- | --- | --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Future Packet Minimum",
            "",
            *minimum,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: a stricter screen for C(R)-style packets that requires the full competency/resource/permission/provenance stack before residual language is reviewed.",
            "",
            "Does not earn: a new C(R) primitive, region-indexed discriminator success, claim-ledger movement, roadmap movement, README movement, North Star movement, public-posture movement, hard-policy movement, protected-license movement, external publication, or cross-repo truth movement.",
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
        json_path = results_dir / "T500-competency-resource-permission-stack-gate-v0.1.json"
        md_path = results_dir / "T500-competency-resource-permission-stack-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
