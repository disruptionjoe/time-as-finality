"""T541: nonidentity shadow-protection witness packet.

T540 made the TAF8 transfer burden concrete. T541 instantiates the next packet:
one kappa nonidentity target and one typed-gap transfer target under the same
predeclared shadow-protection spine. The packet is review-only unless a future
domain-native artifact turns the synthetic target into an earned theorem.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models import kappa_composite_residual_template_gate as t499
from models import t540_cross_domain_shadow_protection_transfer_gate as t540
from models import typed_translation_object_identity_stack_gate as t501


ARTIFACT = "T541-nonidentity-shadow-protection-witness-packet-v0.1"
VERDICT = "T541_NONIDENTITY_WITNESS_PACKET_BUILT_REVIEW_ONLY"
THEOREM_STATUS = "NOT_EARNED_SYNTHETIC_PACKET_SHAPE_ONLY"
TAF8_STATUS = "EXECUTABLE_PACKET_SHAPE_BUILT_THEOREM_BURDEN_OPEN"

NOT_CLAIMED = (
    "T541 does not prove a cross-domain shadow-protection theorem, promote "
    "kappa, promote a typed-gap category theorem, move claim status, move "
    "Canon Index tiers, change canon verdicts, change public posture, change "
    "the North Star, authorize external publication, or move cross-repo truth. "
    "It is a review-only TAF8 witness-packet gate."
)


@dataclass(frozen=True)
class ShadowProtectionSpine:
    spine_id: str
    shadow_object_declared: bool
    capability_object_declared: bool
    native_comparison_declared: bool
    same_spine_before_examples: bool
    positive_controls_declared: bool
    negative_controls_declared: bool
    native_absorbers_completed: bool
    demoter_named: bool
    no_per_domain_retuning: bool


@dataclass(frozen=True)
class WitnessPacket:
    packet_id: str
    description: str
    spine: ShadowProtectionSpine
    source_artifacts: tuple[str, ...]
    kappa_target_source_rank_fixed: bool
    kappa_transport_map_predeclared: bool
    kappa_native_witness_nonidentity: bool
    kappa_synthetic_nu_not_written_from_target: bool
    typed_gap_same_carrier_and_target: bool
    typed_gap_transfer_morphism_or_identity_key: bool
    typed_gap_direct_preservation_theorem: bool
    typed_gap_residual_survives_stack: bool
    domain_native_instantiation: bool
    identity_by_construction: bool = False
    claim_movement_requested: bool = False
    public_posture_requested: bool = False
    external_publication_requested: bool = False
    cross_repo_truth_requested: bool = False


@dataclass(frozen=True)
class PacketDecision:
    packet_id: str
    decision: str
    route_label: str
    spine_passes: bool
    kappa_nonidentity_passes: bool
    typed_gap_transfer_passes: bool
    theorem_ready: bool
    blockers: tuple[str, ...]
    allowed_action: str


def _spine_blockers(spine: ShadowProtectionSpine) -> list[str]:
    checks = (
        ("shadow_object_missing", spine.shadow_object_declared),
        ("capability_object_missing", spine.capability_object_declared),
        ("native_comparison_missing", spine.native_comparison_declared),
        ("same_spine_not_predeclared", spine.same_spine_before_examples),
        ("positive_controls_missing", spine.positive_controls_declared),
        ("negative_controls_missing", spine.negative_controls_declared),
        ("native_absorbers_not_completed", spine.native_absorbers_completed),
        ("demoter_missing", spine.demoter_named),
        ("per_domain_retuning", spine.no_per_domain_retuning),
    )
    return [name for name, ok in checks if not ok]


def evaluate_packet(packet: WitnessPacket) -> PacketDecision:
    blockers = _spine_blockers(packet.spine)

    if packet.claim_movement_requested:
        blockers.append("claim_movement_requested")
    if packet.public_posture_requested:
        blockers.append("public_posture_requested")
    if packet.external_publication_requested:
        blockers.append("external_publication_requested")
    if packet.cross_repo_truth_requested:
        blockers.append("cross_repo_truth_requested")
    if packet.identity_by_construction:
        blockers.append("identity_by_construction")

    if not packet.kappa_target_source_rank_fixed:
        blockers.append("kappa_source_rank_not_fixed")
    if not packet.kappa_transport_map_predeclared:
        blockers.append("kappa_transport_map_not_predeclared")
    if not packet.kappa_native_witness_nonidentity:
        blockers.append("kappa_native_witness_not_nonidentity")
    if not packet.kappa_synthetic_nu_not_written_from_target:
        blockers.append("kappa_synthetic_nu_written_from_target")

    if not packet.typed_gap_same_carrier_and_target:
        blockers.append("typed_gap_same_carrier_target_not_supplied")
    if not packet.typed_gap_transfer_morphism_or_identity_key:
        blockers.append("typed_gap_transfer_morphism_or_identity_key_missing")
    if not packet.typed_gap_direct_preservation_theorem:
        blockers.append("typed_gap_direct_preservation_theorem_missing")
    if not packet.typed_gap_residual_survives_stack:
        blockers.append("typed_gap_residual_not_preserved")

    forbidden = {
        "claim_movement_requested",
        "public_posture_requested",
        "external_publication_requested",
        "cross_repo_truth_requested",
    }
    spine_burden = {
        "shadow_object_missing",
        "capability_object_missing",
        "native_comparison_missing",
        "same_spine_not_predeclared",
        "positive_controls_missing",
        "negative_controls_missing",
        "native_absorbers_not_completed",
        "demoter_missing",
        "per_domain_retuning",
    }
    kappa_burden = {
        "kappa_source_rank_not_fixed",
        "kappa_transport_map_not_predeclared",
        "kappa_native_witness_not_nonidentity",
        "kappa_synthetic_nu_written_from_target",
    }
    typed_gap_burden = {
        "typed_gap_same_carrier_target_not_supplied",
        "typed_gap_transfer_morphism_or_identity_key_missing",
        "typed_gap_direct_preservation_theorem_missing",
        "typed_gap_residual_not_preserved",
    }
    blocker_set = set(blockers)
    spine_passes = not blocker_set.intersection(spine_burden)
    kappa_passes = spine_passes and not blocker_set.intersection(kappa_burden)
    typed_gap_passes = spine_passes and not blocker_set.intersection(typed_gap_burden)
    packet_shape_passes = kappa_passes and typed_gap_passes and not blocker_set
    theorem_ready = packet_shape_passes and packet.domain_native_instantiation

    if blocker_set.intersection(forbidden):
        return PacketDecision(
            packet.packet_id,
            "blocked",
            "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT",
            spine_passes,
            kappa_passes,
            typed_gap_passes,
            False,
            tuple(blockers),
            "record blocker only",
        )
    if "identity_by_construction" in blocker_set:
        return PacketDecision(
            packet.packet_id,
            "rejected",
            "IDENTITY_BY_CONSTRUCTION_BLOCKED",
            spine_passes,
            kappa_passes,
            typed_gap_passes,
            False,
            tuple(blockers),
            "reject same-object shortcut",
        )
    if not spine_passes:
        return PacketDecision(
            packet.packet_id,
            "not_admitted",
            "PREDECLARED_SPINE_BURDEN_NOT_MET",
            False,
            kappa_passes,
            typed_gap_passes,
            False,
            tuple(blockers),
            "repair spine before review",
        )
    if not kappa_passes or not typed_gap_passes:
        return PacketDecision(
            packet.packet_id,
            "not_admitted",
            "NONIDENTITY_OR_TYPED_GAP_BURDEN_NOT_MET",
            True,
            kappa_passes,
            typed_gap_passes,
            False,
            tuple(blockers),
            "repair missing target burden",
        )
    if theorem_ready:
        return PacketDecision(
            packet.packet_id,
            "admitted_theorem_candidate",
            "DOMAIN_NATIVE_PACKET_READY_FOR_THEOREM_REVIEW",
            True,
            True,
            True,
            True,
            (),
            "review theorem proof before any claim movement",
        )
    if packet_shape_passes:
        return PacketDecision(
            packet.packet_id,
            "admitted_review_only",
            "SYNTHETIC_PACKET_SHAPE_ONLY_THEOREM_NOT_EARNED",
            True,
            True,
            True,
            False,
            (),
            "use as executable packet shape; no claim movement",
        )
    return PacketDecision(
        packet.packet_id,
        "not_admitted",
        "UNCLASSIFIED_PACKET_FAILURE",
        spine_passes,
        kappa_passes,
        typed_gap_passes,
        False,
        tuple(blockers),
        "repair packet before review",
    )


def default_spine() -> ShadowProtectionSpine:
    return ShadowProtectionSpine(
        spine_id="taf8_shadow_capability_spine_v1",
        shadow_object_declared=True,
        capability_object_declared=True,
        native_comparison_declared=True,
        same_spine_before_examples=True,
        positive_controls_declared=True,
        negative_controls_declared=True,
        native_absorbers_completed=True,
        demoter_named=True,
        no_per_domain_retuning=True,
    )


def bad_spine() -> ShadowProtectionSpine:
    return ShadowProtectionSpine(
        spine_id="posthoc_retuned_spine",
        shadow_object_declared=True,
        capability_object_declared=True,
        native_comparison_declared=False,
        same_spine_before_examples=False,
        positive_controls_declared=True,
        negative_controls_declared=False,
        native_absorbers_completed=False,
        demoter_named=True,
        no_per_domain_retuning=False,
    )


def source_summary() -> dict[str, Any]:
    kappa_payload = t499.run()
    typed_gap_payload = t501.run()
    t540_payload = t540.run_t540_analysis()
    return {
        "t499_verdict": kappa_payload["verdict"],
        "t501_verdict": typed_gap_payload["verdict"],
        "t540_verdict": t540_payload["verdict"],
        "t540_theorem_status": t540_payload["theorem_status"],
        "kappa_synthetic_nonidentity_review_target": kappa_payload["overall"][
            "synthetic_nonidentity_packet_admitted_for_review"
        ],
        "typed_gap_synthetic_exact_packet_review_target": typed_gap_payload["overall"][
            "synthetic_exact_packet_admitted_for_review"
        ],
        "current_catalogue_theorem_preconditions_pass": t540_payload["overall"][
            "current_catalogue_theorem_preconditions_pass"
        ],
    }


def witness_packets() -> tuple[WitnessPacket, ...]:
    spine = default_spine()
    source = source_summary()
    return (
        WitnessPacket(
            packet_id="current_t499_t501_catalogue_pair",
            description=(
                "The current catalogue pair from T540. It has the shared spine "
                "but still lacks the nonidentity and typed-gap theorem burdens."
            ),
            spine=spine,
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=False,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=False,
            kappa_synthetic_nu_not_written_from_target=False,
            typed_gap_same_carrier_and_target=False,
            typed_gap_transfer_morphism_or_identity_key=False,
            typed_gap_direct_preservation_theorem=False,
            typed_gap_residual_survives_stack=False,
            domain_native_instantiation=False,
        ),
        WitnessPacket(
            packet_id="synthetic_t466_t501_nonidentity_packet",
            description=(
                "The T541 target shape: T466's synthetic nonidentity kappa "
                "packet plus T501's synthetic exact-object preservation packet "
                "under the same TAF8 spine."
            ),
            spine=spine,
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=True,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=source[
                "kappa_synthetic_nonidentity_review_target"
            ],
            kappa_synthetic_nu_not_written_from_target=True,
            typed_gap_same_carrier_and_target=True,
            typed_gap_transfer_morphism_or_identity_key=source[
                "typed_gap_synthetic_exact_packet_review_target"
            ],
            typed_gap_direct_preservation_theorem=True,
            typed_gap_residual_survives_stack=True,
            domain_native_instantiation=False,
        ),
        WitnessPacket(
            packet_id="domain_native_future_theorem_candidate",
            description=(
                "A future stronger packet with the same burdens plus domain-native "
                "instantiation. T541 records the gate but does not claim this exists."
            ),
            spine=spine,
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=True,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=True,
            kappa_synthetic_nu_not_written_from_target=True,
            typed_gap_same_carrier_and_target=True,
            typed_gap_transfer_morphism_or_identity_key=True,
            typed_gap_direct_preservation_theorem=True,
            typed_gap_residual_survives_stack=True,
            domain_native_instantiation=True,
        ),
        WitnessPacket(
            packet_id="identity_by_construction_shortcut",
            description="A shortcut that treats shared spine or schema as object identity.",
            spine=spine,
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=True,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=True,
            kappa_synthetic_nu_not_written_from_target=True,
            typed_gap_same_carrier_and_target=True,
            typed_gap_transfer_morphism_or_identity_key=True,
            typed_gap_direct_preservation_theorem=True,
            typed_gap_residual_survives_stack=True,
            domain_native_instantiation=True,
            identity_by_construction=True,
        ),
        WitnessPacket(
            packet_id="retuned_missing_controls_pair",
            description="A pair assembled after seeing domains, without native controls.",
            spine=bad_spine(),
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=True,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=True,
            kappa_synthetic_nu_not_written_from_target=True,
            typed_gap_same_carrier_and_target=True,
            typed_gap_transfer_morphism_or_identity_key=True,
            typed_gap_direct_preservation_theorem=True,
            typed_gap_residual_survives_stack=True,
            domain_native_instantiation=True,
        ),
        WitnessPacket(
            packet_id="claim_public_posture_shortcut",
            description="A structurally strong packet that asks for immediate posture movement.",
            spine=spine,
            source_artifacts=(t499.ARTIFACT, t501.ARTIFACT, t540.ARTIFACT),
            kappa_target_source_rank_fixed=True,
            kappa_transport_map_predeclared=True,
            kappa_native_witness_nonidentity=True,
            kappa_synthetic_nu_not_written_from_target=True,
            typed_gap_same_carrier_and_target=True,
            typed_gap_transfer_morphism_or_identity_key=True,
            typed_gap_direct_preservation_theorem=True,
            typed_gap_residual_survives_stack=True,
            domain_native_instantiation=True,
            claim_movement_requested=True,
            public_posture_requested=True,
            external_publication_requested=True,
        ),
    )


def run_t541_analysis() -> dict[str, Any]:
    packets = witness_packets()
    decisions = tuple(evaluate_packet(packet) for packet in packets)
    decisions_by_id = {decision.packet_id: decision for decision in decisions}
    synthetic = decisions_by_id["synthetic_t466_t501_nonidentity_packet"]
    future = decisions_by_id["domain_native_future_theorem_candidate"]
    current = decisions_by_id["current_t499_t501_catalogue_pair"]

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "theorem_status": THEOREM_STATUS,
        "taf8_status": TAF8_STATUS,
        "sources": {
            "t499": "results/T499-kappa-composite-residual-template-gate-v0.1-results.md",
            "t501": "results/T501-typed-translation-object-identity-stack-gate-v0.1-results.md",
            "t540": "results/T540-cross-domain-shadow-protection-transfer-gate-v0.1-results.md",
            "taf8_open_problem": "open-problems/cross-domain-shadow-protection-theorem.md",
        },
        "source_summary": source_summary(),
        "spine": asdict(default_spine()),
        "packets": [asdict(packet) for packet in packets],
        "decisions": [asdict(decision) for decision in decisions],
        "overall": {
            "current_catalogue_still_not_theorem": not current.theorem_ready,
            "synthetic_packet_admitted_review_only": (
                synthetic.decision == "admitted_review_only"
            ),
            "domain_native_future_packet_would_reach_theorem_review": (
                future.decision == "admitted_theorem_candidate"
            ),
            "cross_domain_theorem_earned": False,
            "claim_movement": False,
            "canon_movement": False,
            "public_posture_movement": False,
            "north_star_movement": False,
            "external_publication": False,
            "cross_repo_truth_movement": False,
        },
        "strongest_result": (
            "T541 turns T540's recommendation into an executable witness-packet "
            "gate. The current catalogues remain scaffold-only. The synthetic "
            "T466/T501 packet clears the shared-spine, kappa nonidentity, and "
            "typed-gap transfer burdens as a review-only shape, but it is not "
            "domain-native and therefore does not earn a cross-domain theorem."
        ),
        "recommended_next": (
            "Use the T541 gate only when a real domain-native packet is available: "
            "same predeclared spine, independent kappa nonidentity target, typed-gap "
            "transfer morphism or identity key, direct preservation theorem, and "
            "native absorber completion. Until then, TAF8 remains executable but "
            "review-only."
        ),
        "claim_labels": [
            {
                "label": "COMPUTED",
                "confidence": "high",
                "text": (
                    "The current T499/T501 catalogue pair still fails the T541 "
                    "nonidentity and typed-gap transfer burdens."
                ),
            },
            {
                "label": "COMPUTED",
                "confidence": "high",
                "text": (
                    "The synthetic T466/T501 packet clears the executable packet "
                    "shape but remains review-only because it is not domain-native."
                ),
            },
            {
                "label": "ARGUED",
                "confidence": "medium",
                "text": (
                    "A future theorem review should start only after a real packet "
                    "instantiates this same spine without identity by construction."
                ),
            },
        ],
        "not_claimed": NOT_CLAIMED,
    }


def render_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# T541 Results: Nonidentity Shadow-Protection Witness Packet",
        "",
        "## Verdict",
        "",
        f"- Verdict: `{payload['verdict']}`",
        f"- Theorem status: `{payload['theorem_status']}`",
        f"- TAF8 status: `{payload['taf8_status']}`",
        "",
        "## Source Summary",
        "",
        "| Source fact | Value |",
        "| --- | --- |",
    ]
    for key, value in payload["source_summary"].items():
        lines.append(f"| `{key}` | `{value}` |")

    lines.extend(
        [
            "",
            "## Predeclared Spine",
            "",
            "| Field | Value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["spine"].items():
        lines.append(f"| `{key}` | `{value}` |")

    lines.extend(
        [
            "",
            "## Packet Decisions",
            "",
            "| Packet | Decision | Route | Spine? | Kappa? | Typed gap? | Theorem ready? | Blockers | Allowed action |",
            "| --- | --- | --- | :---: | :---: | :---: | :---: | --- | --- |",
        ]
    )
    for decision in payload["decisions"]:
        blockers = ", ".join(decision["blockers"]) or "none"
        lines.append(
            "| `{packet_id}` | `{decision}` | `{route_label}` | {spine} | {kappa} | "
            "{typed_gap} | {theorem} | {blockers} | {allowed_action} |".format(
                packet_id=decision["packet_id"],
                decision=decision["decision"],
                route_label=decision["route_label"],
                spine=decision["spine_passes"],
                kappa=decision["kappa_nonidentity_passes"],
                typed_gap=decision["typed_gap_transfer_passes"],
                theorem=decision["theorem_ready"],
                blockers=blockers,
                allowed_action=decision["allowed_action"],
            )
        )

    lines.extend(
        [
            "",
            "## Strongest Result",
            "",
            payload["strongest_result"],
            "",
            "## Recommended Next",
            "",
            payload["recommended_next"],
            "",
            "## Claim Labels",
            "",
        ]
    )
    for claim in payload["claim_labels"]:
        lines.append(
            f"- `{claim['label']}` confidence `{claim['confidence']}`: {claim['text']}"
        )
    lines.extend(["", "## Not Claimed", "", payload["not_claimed"], ""])
    return "\n".join(lines)


def write_results(
    payload: dict[str, Any], results_dir: Path = Path("results")
) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    json_path = results_dir / "T541-nonidentity-shadow-protection-witness-packet-v0.1.json"
    md_path = (
        results_dir
        / "T541-nonidentity-shadow-protection-witness-packet-v0.1-results.md"
    )
    json_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    md_path.write_text(render_markdown(payload), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", action="store_true")
    args = parser.parse_args(argv)

    payload = run_t541_analysis()
    if args.write_results:
        write_results(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
