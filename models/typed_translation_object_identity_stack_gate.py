"""T501 - typed translation / object-identity stack gate.

The fifth composite absorber-stack lane follows T492. T492 found a shared
finite typed-gap schema across T113 order-pair gaps and T92 unary proposition
gaps, while blocking object identity.

This gate makes the next burden executable: a bridge may preserve a typed
interface under relabeling and quotient controls, but object identity requires
same carrier, same target semantics, same admissibility rule, and a direct
preservation theorem. The current T492 bridge remains a composite explanation:
same interface, not same object.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from models.typed_gap_category_bridge import run as run_t492


ARTIFACT = "T501-typed-translation-object-identity-stack-gate-v0.1"
VERDICT = "TYPED_TRANSLATION_OBJECT_IDENTITY_STACK_BUILT_SCHEMA_PRESERVATION_ONLY"

SOURCE_PROGRESS_LANES = "open-problems/composite-absorber-stack-progress-lanes.md"
SOURCE_T492 = "results/T492-typed-gap-category-bridge-v0.1-results.md"
SOURCE_T496 = "results/T496-bridge-functor-admission-packet-gate-v0.1-results.md"
SOURCE_T92 = "results/accessible-witness-gap-restriction-v0.1-results.md"
SOURCE_T113 = "results/gap-presheaf-classification-v0.1-results.md"

STACK_LAYERS = (
    "typed_schema_interface",
    "relabeling_quotient",
    "object_identity_criterion",
    "gauge_coordinate_quotient",
    "direct_preservation_theorem",
)

HONEST_CEILING = (
    "T501 is a finite typed-translation/object-identity admission gate only. "
    "It does not prove a category theorem, cohomology theorem, physical torsion "
    "claim, consciousness claim, complexity claim, geometry claim, claim-ledger "
    "movement, roadmap movement, README movement, North Star movement, public "
    "posture movement, hard-policy movement, protected-license movement, "
    "external publication, or cross-repo truth."
)


@dataclass(frozen=True)
class TypedGapSystem:
    system_id: str
    source: str
    schema_slots: tuple[str, ...]
    carrier_kind: str
    target_kind: str
    admissibility_rule: str
    restriction_rule: str
    object_identity_key: tuple[str, ...]
    relabeling_quotient_signature: tuple[str, ...]
    gauge_coordinate_quotient_signature: tuple[str, ...]
    preserved_invariants: tuple[str, ...]
    blocked_overreads: tuple[str, ...]


@dataclass(frozen=True)
class TranslationPacket:
    packet_id: str
    description: str
    source_system_id: str
    target_system_id: str
    declares_typed_schema_interface: bool
    grants_relabeling_quotient: bool
    grants_object_identity_criterion: bool
    grants_gauge_coordinate_quotient: bool
    supplies_direct_preservation_theorem: bool
    theorem_preserves_target_semantics: bool
    invariant_obstruction_survives_stack: bool
    asks_same_object_identity: bool = False
    uses_raw_h0_classifier: bool = False
    uses_semantic_relabeling_as_identity: bool = False
    uses_gauge_coordinate_choice_as_identity: bool = False
    promotes_cohomology_or_physical_torsion: bool = False
    promotes_consciousness_or_complexity: bool = False
    requests_claim_or_public_posture: bool = False
    requests_external_publication: bool = False
    requests_cross_repo_truth: bool = False


@dataclass(frozen=True)
class TranslationDecision:
    packet_id: str
    admitted: bool
    label: str
    action: str
    interface_preserved: bool
    object_identity_passes: bool
    direct_preservation_passes: bool
    residual_survives_stack: bool
    missing_layers: tuple[str, ...]
    blocked_shortcuts: tuple[str, ...]
    reason: str


def typed_gap_systems() -> dict[str, TypedGapSystem]:
    t492 = run_t492()
    schema_slots = tuple(t492.abstract_schema)
    t113 = t492.t113_summary
    t92 = t492.t92_summary

    return {
        "t113_order_pair": TypedGapSystem(
            system_id="t113_order_pair",
            source=SOURCE_T113,
            schema_slots=schema_slots,
            carrier_kind=t113.carrier_kind,
            target_kind=t113.target_kind,
            admissibility_rule=t113.typed_rule,
            restriction_rule=t113.closure_status,
            object_identity_key=(
                "carrier:nonreflexive_order_pair_sections",
                "target:phantom_incomparability_witnesses",
                "tau:endpoint_canonical_local_incomparability",
                "raw_h0:refuted",
            ),
            relabeling_quotient_signature=(
                "event_name_relabeling_removed",
                "endpoint_role_preserved",
                "local_incomparability_preserved",
            ),
            gauge_coordinate_quotient_signature=(
                "presentation_order_removed",
                "canonical_ambient_completion_preserved",
            ),
            preserved_invariants=(
                "typed_gap_schema",
                "restriction_closure",
                "phantom_incomparability_target",
            ),
            blocked_overreads=(
                "raw_h0_classifier",
                "same_object_as_unary_proposition",
                "cohomology_or_physical_torsion",
            ),
        ),
        "t92_unary_proposition": TypedGapSystem(
            system_id="t92_unary_proposition",
            source=SOURCE_T92,
            schema_slots=schema_slots,
            carrier_kind=t92.carrier_kind,
            target_kind=t92.target_kind,
            admissibility_rule=t92.typed_rule,
            restriction_rule=t92.closure_status,
            object_identity_key=(
                "carrier:unary_typed_proposition_sections",
                "target:accessible_witness_unauditability_gaps",
                "tau:ambient_restriction_audit_monotonicity_stable_proposition",
                "raw_h0:not_order_pair_object",
            ),
            relabeling_quotient_signature=(
                "proposition_name_relabeling_removed",
                "audit_boundary_preserved",
                "stable_typing_preserved",
            ),
            gauge_coordinate_quotient_signature=(
                "presentation_order_removed",
                "audit_monotonicity_preserved",
            ),
            preserved_invariants=(
                "typed_gap_schema",
                "restriction_closure",
                "accessible_witness_gap_target",
            ),
            blocked_overreads=(
                "same_object_as_order_pair",
                "consciousness_or_complexity_claim",
                "semantic_relabeling_identity",
            ),
        ),
        "future_exact_gap_system": TypedGapSystem(
            system_id="future_exact_gap_system",
            source="synthetic_future_packet",
            schema_slots=schema_slots,
            carrier_kind="future_exact_typed_gap_sections",
            target_kind="future_exact_obstruction_targets",
            admissibility_rule="same_tau_same_carrier_same_target",
            restriction_rule="direct_preservation_theorem_supplied",
            object_identity_key=(
                "carrier:future_exact_typed_gap_sections",
                "target:future_exact_obstruction_targets",
                "tau:same_tau_same_carrier_same_target",
                "theorem:direct_preservation",
            ),
            relabeling_quotient_signature=(
                "label_relabeling_removed",
                "target_semantics_preserved",
            ),
            gauge_coordinate_quotient_signature=(
                "coordinate_choice_removed",
                "obstruction_class_preserved",
            ),
            preserved_invariants=(
                "typed_gap_schema",
                "object_identity_key",
                "invariant_obstruction_class",
            ),
            blocked_overreads=(
                "claim_promotion",
                "geometry_or_physics_promotion",
            ),
        ),
    }


def fixture_packets() -> tuple[TranslationPacket, ...]:
    return (
        TranslationPacket(
            packet_id="t92_t113_schema_translation",
            description=(
                "The actual T492 bridge: T92 and T113 share the typed-gap "
                "interface, but carrier, target, and admissibility semantics differ."
            ),
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
        ),
        TranslationPacket(
            packet_id="same_object_identity_overread",
            description="A packet that treats shared schema as same object identity.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            asks_same_object_identity=True,
        ),
        TranslationPacket(
            packet_id="raw_h0_classifier_overread",
            description="A packet that revives raw H0(G) as the shared classifier.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            uses_raw_h0_classifier=True,
        ),
        TranslationPacket(
            packet_id="semantic_relabeling_identity",
            description="A packet that uses semantic relabeling as identity.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=False,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            uses_semantic_relabeling_as_identity=True,
        ),
        TranslationPacket(
            packet_id="gauge_coordinate_choice_identity",
            description="A packet that treats quotienting presentation choices as object identity.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=False,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            uses_gauge_coordinate_choice_as_identity=True,
        ),
        TranslationPacket(
            packet_id="cohomology_physical_torsion_shortcut",
            description="A packet that upgrades schema preservation to cohomology or torsion.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            promotes_cohomology_or_physical_torsion=True,
        ),
        TranslationPacket(
            packet_id="consciousness_complexity_shortcut",
            description="A packet that upgrades unary proposition gaps to consciousness or complexity.",
            source_system_id="t92_unary_proposition",
            target_system_id="t113_order_pair",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
            promotes_consciousness_or_complexity=True,
        ),
        TranslationPacket(
            packet_id="incomplete_schema_only_packet",
            description="A packet that names the interface but omits quotient and identity burdens.",
            source_system_id="t113_order_pair",
            target_system_id="t92_unary_proposition",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=False,
            grants_object_identity_criterion=False,
            grants_gauge_coordinate_quotient=False,
            supplies_direct_preservation_theorem=False,
            theorem_preserves_target_semantics=False,
            invariant_obstruction_survives_stack=False,
        ),
        TranslationPacket(
            packet_id="synthetic_exact_object_preservation_packet",
            description=(
                "A future packet shape: same carrier, target, tau, quotients, "
                "and direct theorem still leave an invariant obstruction."
            ),
            source_system_id="future_exact_gap_system",
            target_system_id="future_exact_gap_system",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=True,
            theorem_preserves_target_semantics=True,
            invariant_obstruction_survives_stack=True,
        ),
        TranslationPacket(
            packet_id="claim_public_posture_shortcut",
            description="A packet that asks to treat typed translation as public-facing support.",
            source_system_id="future_exact_gap_system",
            target_system_id="future_exact_gap_system",
            declares_typed_schema_interface=True,
            grants_relabeling_quotient=True,
            grants_object_identity_criterion=True,
            grants_gauge_coordinate_quotient=True,
            supplies_direct_preservation_theorem=True,
            theorem_preserves_target_semantics=True,
            invariant_obstruction_survives_stack=True,
            requests_claim_or_public_posture=True,
            requests_external_publication=True,
            requests_cross_repo_truth=True,
        ),
    )


def missing_layers(packet: TranslationPacket) -> tuple[str, ...]:
    checks = (
        ("typed_schema_interface", packet.declares_typed_schema_interface),
        ("relabeling_quotient", packet.grants_relabeling_quotient),
        ("object_identity_criterion", packet.grants_object_identity_criterion),
        ("gauge_coordinate_quotient", packet.grants_gauge_coordinate_quotient),
    )
    missing = [name for name, ok in checks if not ok]
    if packet.invariant_obstruction_survives_stack and not packet.supplies_direct_preservation_theorem:
        missing.append("direct_preservation_theorem")
    return tuple(missing)


def blocked_shortcuts(packet: TranslationPacket) -> tuple[str, ...]:
    blocked: list[str] = []
    if packet.requests_claim_or_public_posture:
        blocked.append("claim_or_public_posture")
    if packet.requests_external_publication:
        blocked.append("external_publication")
    if packet.requests_cross_repo_truth:
        blocked.append("cross_repo_truth")
    return tuple(blocked)


def schema_interface_preserved(source: TypedGapSystem, target: TypedGapSystem) -> bool:
    return source.schema_slots == target.schema_slots


def object_identity_passes(source: TypedGapSystem, target: TypedGapSystem) -> bool:
    return (
        source.carrier_kind == target.carrier_kind
        and source.target_kind == target.target_kind
        and source.admissibility_rule == target.admissibility_rule
        and source.object_identity_key == target.object_identity_key
    )


def direct_preservation_passes(packet: TranslationPacket, object_identity: bool) -> bool:
    return (
        object_identity
        and packet.supplies_direct_preservation_theorem
        and packet.theorem_preserves_target_semantics
    )


def evaluate_packet(
    packet: TranslationPacket,
    systems: dict[str, TypedGapSystem],
) -> TranslationDecision:
    source = systems[packet.source_system_id]
    target = systems[packet.target_system_id]
    blocked = blocked_shortcuts(packet)
    missing = missing_layers(packet)
    interface_preserved = packet.declares_typed_schema_interface and schema_interface_preserved(
        source, target
    )
    identity_ok = object_identity_passes(source, target)
    direct_ok = direct_preservation_passes(packet, identity_ok)
    residual = direct_ok and packet.invariant_obstruction_survives_stack

    if blocked:
        return TranslationDecision(
            packet.packet_id,
            False,
            "BLOCKED_GOVERNANCE_OR_EXTERNAL_SHORTCUT",
            "stop",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "Typed translation gates cannot move claims, posture, publication, or cross-repo truth.",
        )
    if packet.promotes_cohomology_or_physical_torsion:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_COHOMOLOGY_OR_PHYSICAL_TORSION_SHORTCUT",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "T492/T501 do not supply a cohomology theorem or physical torsion result.",
        )
    if packet.promotes_consciousness_or_complexity:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_CONSCIOUSNESS_OR_COMPLEXITY_SHORTCUT",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "Unary proposition gaps do not promote to consciousness or complexity-class claims.",
        )
    if packet.uses_raw_h0_classifier:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_RAW_H0_CLASSIFIER_REVIVAL",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "T113 already refutes raw H0(G) as the classifier.",
        )
    if packet.uses_semantic_relabeling_as_identity:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_SEMANTIC_RELABELING_IDENTITY",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "Relabeling quotient removes naming conventions; it does not supply object identity.",
        )
    if packet.uses_gauge_coordinate_choice_as_identity:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_GAUGE_COORDINATE_IDENTITY",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "Gauge or coordinate quotient removes presentation choices; it does not identify target semantics.",
        )
    if missing:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_INCOMPLETE_TRANSLATION_STACK",
            "reject",
            interface_preserved,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "The packet omits at least one required stack layer.",
        )
    if not interface_preserved:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_SCHEMA_INTERFACE_NOT_PRESERVED",
            "reject",
            False,
            identity_ok,
            direct_ok,
            False,
            missing,
            blocked,
            "The source and target do not share the declared typed schema interface.",
        )
    if packet.asks_same_object_identity and not identity_ok:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_OBJECT_IDENTITY_CRITERION_FAILS",
            "reject",
            interface_preserved,
            False,
            direct_ok,
            False,
            missing,
            blocked,
            "Carrier, target semantics, admissibility rule, or identity key differ.",
        )
    if packet.supplies_direct_preservation_theorem and not direct_ok:
        return TranslationDecision(
            packet.packet_id,
            False,
            "REJECTED_DIRECT_PRESERVATION_THEOREM_DOES_NOT_TYPECHECK",
            "reject",
            interface_preserved,
            identity_ok,
            False,
            False,
            missing,
            blocked,
            "A direct theorem must preserve target semantics over an object-identity match.",
        )
    if residual:
        return TranslationDecision(
            packet.packet_id,
            True,
            "ADMITTED_FUTURE_REVIEW_TARGET_OBJECT_IDENTITY_AND_RESIDUAL",
            "review_only",
            interface_preserved,
            identity_ok,
            direct_ok,
            True,
            missing,
            blocked,
            "The packet clears object identity and direct preservation while retaining an invariant obstruction.",
        )

    return TranslationDecision(
        packet.packet_id,
        True,
        "COMPOSITE_ABSORBER_EXPLANATION_SCHEMA_TRANSLATION_ONLY",
        "record_composite_explanation",
        interface_preserved,
        identity_ok,
        direct_ok,
        False,
        missing,
        blocked,
        "The typed interface is preserved, but object identity or direct theorem burden is not met.",
    )


def packet_to_dict(packet: TranslationPacket) -> dict[str, Any]:
    return asdict(packet)


def system_to_dict(system: TypedGapSystem) -> dict[str, Any]:
    return asdict(system)


def decision_to_dict(decision: TranslationDecision) -> dict[str, Any]:
    return asdict(decision)


def run() -> dict[str, Any]:
    systems = typed_gap_systems()
    packets = fixture_packets()
    decisions = tuple(evaluate_packet(packet, systems) for packet in packets)
    actual = next(
        decision for decision in decisions if decision.packet_id == "t92_t113_schema_translation"
    )
    synthetic = next(
        decision
        for decision in decisions
        if decision.packet_id == "synthetic_exact_object_preservation_packet"
    )

    return {
        "artifact": ARTIFACT,
        "verdict": VERDICT,
        "sources": {
            "progress_lanes": SOURCE_PROGRESS_LANES,
            "t492": SOURCE_T492,
            "t496": SOURCE_T496,
            "t92": SOURCE_T92,
            "t113": SOURCE_T113,
        },
        "stack_layers": list(STACK_LAYERS),
        "honest_ceiling": HONEST_CEILING,
        "systems": {key: system_to_dict(system) for key, system in sorted(systems.items())},
        "packets": [packet_to_dict(packet) for packet in packets],
        "decisions": [decision_to_dict(decision) for decision in decisions],
        "overall": {
            "actual_t92_t113_interface_preserved": actual.interface_preserved,
            "actual_t92_t113_object_identity_passes": actual.object_identity_passes,
            "actual_t92_t113_direct_preservation_passes": actual.direct_preservation_passes,
            "actual_t92_t113_residual_survives_stack": actual.residual_survives_stack,
            "synthetic_exact_packet_admitted_for_review": synthetic.admitted
            and synthetic.residual_survives_stack,
            "review_target_only_for_residuals": True,
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
            "The current T92/T113 bridge preserves a typed-gap schema interface "
            "under quotient discipline, but it fails object identity because "
            "carrier kind, target kind, and admissibility rule remain distinct. "
            "No direct preservation theorem is supplied for the actual pair, so "
            "the honest result is a composite absorber explanation: same "
            "interface, not same object."
        ),
        "recommended_next": (
            "Treat the five composite absorber-stack lanes as executed. Future "
            "typed-gap work should not reopen object identity unless it supplies "
            "a same-carrier/same-target identity key plus a direct preservation "
            "theorem and an invariant obstruction that survives the full stack."
        ),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    decision_rows = [
        "| {packet_id} | {admitted} | {label} | {interface} | {identity} | {theorem} | {residual} | {missing} | {blocked} | {action} |".format(
            packet_id=decision["packet_id"],
            admitted="yes" if decision["admitted"] else "no",
            label=decision["label"],
            interface="yes" if decision["interface_preserved"] else "no",
            identity="yes" if decision["object_identity_passes"] else "no",
            theorem="yes" if decision["direct_preservation_passes"] else "no",
            residual="yes" if decision["residual_survives_stack"] else "no",
            missing=", ".join(decision["missing_layers"]) or "none",
            blocked=", ".join(decision["blocked_shortcuts"]) or "none",
            action=decision["action"],
        )
        for decision in payload["decisions"]
    ]
    layer_lines = [f"- {item}" for item in payload["stack_layers"]]
    system_rows = [
        "| {system_id} | {carrier_kind} | {target_kind} | {admissibility_rule} |".format(
            **system
        )
        for system in payload["systems"].values()
    ]

    return "\n".join(
        [
            "# T501 - Typed Translation Object-Identity Stack Gate - v0.1 results",
            "",
            "> Composite explanation and admission gate only. No claim-ledger, roadmap, README, North Star, public-posture, hard-policy, protected-license, external-publication, or cross-repo truth movement.",
            "",
            "- Spec: `tests/T501-typed-translation-object-identity-stack-gate.md`",
            "- Model: `models/typed_translation_object_identity_stack_gate.py`",
            "- Tests: `tests/test_typed_translation_object_identity_stack_gate.py`",
            "- Artifact JSON: `results/T501-typed-translation-object-identity-stack-gate-v0.1.json`",
            "- Sources: T492, T496, T92, T113, and `open-problems/composite-absorber-stack-progress-lanes.md`",
            "",
            f"## Overall verdict: {payload['verdict']}",
            "",
            payload["strongest_result"],
            "",
            "## Stack Layers",
            "",
            *layer_lines,
            "",
            "## Typed Systems",
            "",
            "| System | Carrier | Target | Admissibility rule |",
            "| --- | --- | --- | --- |",
            *system_rows,
            "",
            "## Packet Decisions",
            "",
            "| Packet | Admitted? | Label | Interface preserved? | Object identity? | Direct theorem? | Residual survives? | Missing layers | Blocked shortcuts | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *decision_rows,
            "",
            "## What this earns / does not earn",
            "",
            "Earns: the fifth composite absorber-stack lane is executable. The actual T92/T113 bridge is preserved as a schema-level composite explanation, and the object-identity burden is now explicit.",
            "",
            "Does not earn: same-object identity for T92/T113, raw H0 classification, a category theorem, cohomology, physical torsion, consciousness or complexity claims, geometry/physics support, claim-ledger movement, roadmap movement, README movement, North Star movement, public-posture movement, hard-policy movement, protected-license movement, external publication, or cross-repo truth movement.",
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
        json_path = results_dir / "T501-typed-translation-object-identity-stack-gate-v0.1.json"
        md_path = results_dir / "T501-typed-translation-object-identity-stack-gate-v0.1-results.md"
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        md_path.write_text(render_markdown(payload), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
