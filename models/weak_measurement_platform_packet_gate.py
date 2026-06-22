"""T166: intake gate for external Q1C platform packets.

Q1C is now externally bottlenecked: the next non-null move is not another toy
counterexample but a concrete platform packet that can be audited before any
measurement data are interpreted. This module turns the prose handoff into an
executable intake rule. A packet is admissible only if it freezes the ordinary
record, auxiliary channel, TaF axis, verdict rule, loss rule, architecture
class, and event-level audit burden up front. Enlarged-instrument packets must
also declare an eventwise back-projection to the full ordinary standard
record.
"""

from __future__ import annotations

from dataclasses import dataclass


VALID_ARCHITECTURE_CLASSES = frozenset(
    {"extra_environment", "enlarged_instrument"}
)


@dataclass(frozen=True)
class Q1CPlatformPacketInput:
    ordinary_record_frozen: bool
    ordinary_record_is_full_event_level: bool
    auxiliary_channel_frozen: bool
    architecture_class: str
    taf_axis_independently_typed: bool
    verdict_map_predeclared: bool
    class_support_floor_declared: bool
    loss_rule_declared: bool
    null_control_plan_declared: bool
    event_level_audit_data_promised: bool
    enlarged_instrument_back_projection_declared: bool = False
    enlarged_instrument_preserved_target_declared: bool = False
    preserved_target_is_full_standard_record: bool = False


@dataclass(frozen=True)
class Q1CPlatformPacketAudit:
    name: str
    classification: str
    admissible_packet: bool
    reason: str
    required_next: str


@dataclass(frozen=True)
class T166Result:
    audits: tuple[Q1CPlatformPacketAudit, ...]
    all_null_controls_rejected: bool
    current_frontier_admissible: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def classify_platform_packet(
    case: Q1CPlatformPacketInput,
    *,
    name: str,
) -> Q1CPlatformPacketAudit:
    if not case.ordinary_record_frozen:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_frozen_ordinary_record",
            admissible_packet=False,
            reason=(
                "The packet does not freeze the ordinary monitored record before "
                "analysis."
            ),
            required_next="Predeclare the ordinary monitored record schema.",
        )
    if not case.ordinary_record_is_full_event_level:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="null_coarse_ordinary_record",
            admissible_packet=False,
            reason=(
                "The packet freezes only a coarse export rather than the full "
                "ordinary event-level standard record."
            ),
            required_next="Freeze the full event-level ordinary record.",
        )
    if not case.auxiliary_channel_frozen:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_frozen_auxiliary_channel",
            admissible_packet=False,
            reason=(
                "The auxiliary channel is not predeclared with a fixed schema and "
                "alignment plan."
            ),
            required_next="Freeze the auxiliary-channel schema before analysis.",
        )
    if case.architecture_class not in VALID_ARCHITECTURE_CLASSES:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="null_invalid_architecture_class",
            admissible_packet=False,
            reason=(
                "The packet does not name one of the two live Q1C architecture "
                "classes."
            ),
            required_next=(
                "Use either extra-environment structure or explicit instrument "
                "enlargement."
            ),
        )
    if not case.taf_axis_independently_typed:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_untyped_taf_axis",
            admissible_packet=False,
            reason=(
                "The TaF axis is not typed independently of the auxiliary meter."
            ),
            required_next="Declare an independently typed TaF axis.",
        )
    if not case.verdict_map_predeclared:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_verdict_map",
            admissible_packet=False,
            reason=(
                "The verdict map is not frozen before analysis."
            ),
            required_next="Predeclare the verdict map V = g(H).",
        )
    if not case.class_support_floor_declared:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_support_floor",
            admissible_packet=False,
            reason=(
                "The packet does not declare a support floor for each verdict class."
            ),
            required_next="Freeze a nontrivial support floor for each verdict class.",
        )
    if not case.loss_rule_declared:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_loss_rule",
            admissible_packet=False,
            reason=(
                "The decision-loss rule is missing, so verdict lift cannot be audited "
                "honestly."
            ),
            required_next="Predeclare the loss rule for R versus (R,A).",
        )
    if not case.null_control_plan_declared:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="blocked_missing_null_control_plan",
            admissible_packet=False,
            reason=(
                "The packet does not commit to the required null-control screens."
            ),
            required_next=(
                "Include null controls for coarse-record refinement, postselection, "
                "auxiliary-defined labels, rare targets, and underdeclared same-"
                "instrument routes."
            ),
        )
    if not case.event_level_audit_data_promised:
        return Q1CPlatformPacketAudit(
            name=name,
            classification="scaffold_only_no_event_level_audit_data",
            admissible_packet=False,
            reason=(
                "The packet does not promise the event-level data needed to run the "
                "Q1C screens."
            ),
            required_next="Expose event-level audit data or keep Q1C dormant.",
        )
    if case.architecture_class == "enlarged_instrument":
        if not case.enlarged_instrument_preserved_target_declared:
            return Q1CPlatformPacketAudit(
                name=name,
                classification="blocked_missing_preserved_target",
                admissible_packet=False,
                reason=(
                    "The enlarged-instrument packet does not predeclare the preserved "
                    "comparison target."
                ),
                required_next="Declare the preserved comparison target explicitly.",
            )
        if not case.preserved_target_is_full_standard_record:
            return Q1CPlatformPacketAudit(
                name=name,
                classification="null_coarse_preserved_target",
                admissible_packet=False,
                reason=(
                    "The enlarged-instrument packet preserves only a coarse target, "
                    "not the full ordinary standard record."
                ),
                required_next="Preserve the full ordinary standard record exactly.",
            )
        if not case.enlarged_instrument_back_projection_declared:
            return Q1CPlatformPacketAudit(
                name=name,
                classification="blocked_missing_back_projection",
                admissible_packet=False,
                reason=(
                    "The enlarged-instrument packet does not declare an eventwise "
                    "back-projection to the full ordinary standard record."
                ),
                required_next="Declare the eventwise back-projection before analysis.",
            )
    return Q1CPlatformPacketAudit(
        name=name,
        classification="admissible_external_q1c_packet",
        admissible_packet=True,
        reason=(
            "The packet freezes the full ordinary record, auxiliary channel, TaF "
            "axis, verdict rule, loss rule, architecture class, null controls, and "
            "event-level audit burden. If enlarged, it also declares an honest "
            "full-record preserved target and back-projection."
        ),
        required_next=(
            "Supply the event-level packet and test whether (R,A) improves the "
            "predeclared verdict risk over R alone."
        ),
    )


def canonical_platform_packet_cases() -> tuple[tuple[str, Q1CPlatformPacketInput], ...]:
    return (
        (
            "admissible_extra_environment_packet",
            Q1CPlatformPacketInput(
                ordinary_record_frozen=True,
                ordinary_record_is_full_event_level=True,
                auxiliary_channel_frozen=True,
                architecture_class="extra_environment",
                taf_axis_independently_typed=True,
                verdict_map_predeclared=True,
                class_support_floor_declared=True,
                loss_rule_declared=True,
                null_control_plan_declared=True,
                event_level_audit_data_promised=True,
            ),
        ),
        (
            "enlarged_instrument_missing_back_projection",
            Q1CPlatformPacketInput(
                ordinary_record_frozen=True,
                ordinary_record_is_full_event_level=True,
                auxiliary_channel_frozen=True,
                architecture_class="enlarged_instrument",
                taf_axis_independently_typed=True,
                verdict_map_predeclared=True,
                class_support_floor_declared=True,
                loss_rule_declared=True,
                null_control_plan_declared=True,
                event_level_audit_data_promised=True,
                enlarged_instrument_preserved_target_declared=True,
                preserved_target_is_full_standard_record=True,
                enlarged_instrument_back_projection_declared=False,
            ),
        ),
        (
            "same_instrument_packet",
            Q1CPlatformPacketInput(
                ordinary_record_frozen=True,
                ordinary_record_is_full_event_level=True,
                auxiliary_channel_frozen=True,
                architecture_class="same_instrument",
                taf_axis_independently_typed=True,
                verdict_map_predeclared=True,
                class_support_floor_declared=True,
                loss_rule_declared=True,
                null_control_plan_declared=True,
                event_level_audit_data_promised=True,
            ),
        ),
        (
            "coarse_record_packet",
            Q1CPlatformPacketInput(
                ordinary_record_frozen=True,
                ordinary_record_is_full_event_level=False,
                auxiliary_channel_frozen=True,
                architecture_class="extra_environment",
                taf_axis_independently_typed=True,
                verdict_map_predeclared=True,
                class_support_floor_declared=True,
                loss_rule_declared=True,
                null_control_plan_declared=True,
                event_level_audit_data_promised=True,
            ),
        ),
        (
            "scaffold_only_packet",
            Q1CPlatformPacketInput(
                ordinary_record_frozen=True,
                ordinary_record_is_full_event_level=True,
                auxiliary_channel_frozen=True,
                architecture_class="extra_environment",
                taf_axis_independently_typed=True,
                verdict_map_predeclared=True,
                class_support_floor_declared=True,
                loss_rule_declared=True,
                null_control_plan_declared=True,
                event_level_audit_data_promised=False,
            ),
        ),
    )


def current_frontier_case() -> tuple[str, Q1CPlatformPacketInput]:
    return (
        "current_frontier",
        Q1CPlatformPacketInput(
            ordinary_record_frozen=False,
            ordinary_record_is_full_event_level=False,
            auxiliary_channel_frozen=False,
            architecture_class="same_instrument",
            taf_axis_independently_typed=False,
            verdict_map_predeclared=False,
            class_support_floor_declared=False,
            loss_rule_declared=False,
            null_control_plan_declared=False,
            event_level_audit_data_promised=False,
        ),
    )


def run_t166_analysis() -> T166Result:
    audits = tuple(
        classify_platform_packet(case, name=name)
        for name, case in canonical_platform_packet_cases()
    )
    current_name, current_case = current_frontier_case()
    current_audit = classify_platform_packet(current_case, name=current_name)
    audits = audits + (current_audit,)

    null_control_names = {
        "enlarged_instrument_missing_back_projection",
        "same_instrument_packet",
        "coarse_record_packet",
        "scaffold_only_packet",
        "current_frontier",
    }

    return T166Result(
        audits=audits,
        all_null_controls_rejected=all(
            not audit.admissible_packet for audit in audits if audit.name in null_control_names
        ),
        current_frontier_admissible=current_audit.admissible_packet,
        strongest_claim=(
            "Q1C should not be reopened by platform prose alone. A weak-measurement "
            "route is admissible for external review only after it freezes the full "
            "ordinary event-level record, auxiliary channel, architecture class, "
            "independently typed TaF axis, verdict map, support floor, loss rule, "
            "null-control plan, and event-level audit packet in advance."
        ),
        improved=(
            "T163 converts the Q1C handoff from a narrative blocker into an intake "
            "gate. Future platform ideas can now be rejected before any new internal "
            "witness work unless they clear a concrete packet contract."
        ),
        weakened=(
            "This weakens the idea that a vague experimental sketch or named second "
            "meter is progress for Q1C. Without a full packet contract, the branch is "
            "still dormant."
        ),
        falsification_condition=(
            "T163 fails if a serious Q1C platform should count even though it does "
            "not freeze the full ordinary record, verdict map, loss rule, support "
            "floor, and event-level audit burden before analysis."
        ),
        q1c_update=(
            "Q1C remains dormant. Reinstatement now has two stages: first clear the "
            "T166 packet gate, then clear the T149/T150/T158 event-level verdict "
            "screens."
        ),
        claim_ledger_update=(
            "Add T166 to Q1C: external platform proposals are null or scaffold-only "
            "unless they first supply a complete pre-analysis packet, with enlarged-"
            "instrument routes also declaring a full-record preserved target and "
            "eventwise back-projection."
        ),
        open_blocker=(
            "No named monitored-qubit platform in the repo currently supplies a "
            "complete T166 packet, much less the event-level data needed for T149, "
            "T150, and T158."
        ),
        recommended_next=(
            "Do not run more internal Q1C toy models unless a concrete platform can "
            "fill a T166-valid packet template first."
        ),
    )


def _audit_to_dict(audit: Q1CPlatformPacketAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "admissible_packet": audit.admissible_packet,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t166_result_to_dict(result: T166Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "all_null_controls_rejected": result.all_null_controls_rejected,
        "current_frontier_admissible": result.current_frontier_admissible,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1c_update": result.q1c_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t166_result_to_dict(run_t166_analysis()), indent=2))
