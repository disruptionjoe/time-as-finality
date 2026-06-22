"""T183: stack-level reinstatement gate for Q1C weak-measurement proposals.

T166, T149, T150, T155, T158, and T182 each close one loophole. T183 composes
the still-live gates into a single executable burden: a proposal is only a Q1C
reinstatement candidate after it clears packet intake, architecture consistency,
typed-verdict lift, and, for enlarged instruments, preserved-target honesty.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from models.weak_measurement_platform_packet_gate import (
    Q1CPlatformPacketInput,
    classify_platform_packet,
)
from models.weak_measurement_preserved_target_gate import (
    PreservedTargetEvent,
    Q1CPreservedTargetInput,
    classify_preserved_target,
)
from models.weak_measurement_verdict_admissibility_gate import (
    Q1CVerdictInput,
    VerdictEvent,
    classify_verdict_admissibility,
)


@dataclass(frozen=True)
class Q1CReinstatementProposal:
    packet: Q1CPlatformPacketInput
    verdict: Q1CVerdictInput | None
    preserved_target: Q1CPreservedTargetInput | None = None


@dataclass(frozen=True)
class Q1CReinstatementAudit:
    name: str
    classification: str
    reinstatement_candidate: bool
    packet_classification: str
    verdict_classification: str | None
    preserved_target_classification: str | None
    reason: str
    required_next: str


@dataclass(frozen=True)
class T183Result:
    audits: tuple[Q1CReinstatementAudit, ...]
    positive_controls_admitted: bool
    null_controls_rejected: bool
    current_frontier_reopened: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    suggested_next: str


def classify_reinstatement_stack(
    proposal: Q1CReinstatementProposal,
    *,
    name: str,
) -> Q1CReinstatementAudit:
    packet_audit = classify_platform_packet(proposal.packet, name=name)
    if not packet_audit.admissible_packet:
        return Q1CReinstatementAudit(
            name=name,
            classification=f"blocked_at_packet_gate:{packet_audit.classification}",
            reinstatement_candidate=False,
            packet_classification=packet_audit.classification,
            verdict_classification=None,
            preserved_target_classification=None,
            reason=packet_audit.reason,
            required_next=packet_audit.required_next,
        )

    if proposal.verdict is None:
        return Q1CReinstatementAudit(
            name=name,
            classification="blocked_missing_event_level_verdict_data",
            reinstatement_candidate=False,
            packet_classification=packet_audit.classification,
            verdict_classification=None,
            preserved_target_classification=None,
            reason=(
                "The packet clears intake, but no event-level R,A,H,V data are supplied "
                "for the T149/T150 verdict screens."
            ),
            required_next="Supply event-level verdict data before calling the packet live.",
        )

    if not _architecture_matches_verdict(proposal.packet, proposal.verdict):
        return Q1CReinstatementAudit(
            name=name,
            classification="blocked_architecture_mismatch",
            reinstatement_candidate=False,
            packet_classification=packet_audit.classification,
            verdict_classification=None,
            preserved_target_classification=None,
            reason=(
                "The packet's declared live architecture class does not match the "
                "architecture flags used by the event-level verdict input."
            ),
            required_next="Make the packet architecture and event-level screen use the same class.",
        )

    preserved_classification: str | None = None
    if proposal.packet.architecture_class == "enlarged_instrument":
        if proposal.preserved_target is None:
            return Q1CReinstatementAudit(
                name=name,
                classification="blocked_missing_preserved_target_screen",
                reinstatement_candidate=False,
                packet_classification=packet_audit.classification,
                verdict_classification=None,
                preserved_target_classification=None,
                reason=(
                    "The packet declares an enlarged instrument but does not supply the "
                    "eventwise preserved-target audit required by T158."
                ),
                required_next="Run the preserved-target honesty screen on event-level data.",
            )
        preserved_audit = classify_preserved_target(
            proposal.preserved_target,
            name=name,
        )
        preserved_classification = preserved_audit.classification
        if not preserved_audit.active_route:
            return Q1CReinstatementAudit(
                name=name,
                classification=f"blocked_at_preserved_target_gate:{preserved_audit.classification}",
                reinstatement_candidate=False,
                packet_classification=packet_audit.classification,
                verdict_classification=None,
                preserved_target_classification=preserved_classification,
                reason=preserved_audit.reason,
                required_next=preserved_audit.required_next,
            )

    verdict_audit = classify_verdict_admissibility(proposal.verdict, name=name)
    if not verdict_audit.active_route:
        return Q1CReinstatementAudit(
            name=name,
            classification=f"blocked_at_verdict_gate:{verdict_audit.classification}",
            reinstatement_candidate=False,
            packet_classification=packet_audit.classification,
            verdict_classification=verdict_audit.classification,
            preserved_target_classification=preserved_classification,
            reason=verdict_audit.reason,
            required_next=verdict_audit.required_next,
        )

    return Q1CReinstatementAudit(
        name=name,
        classification="candidate_q1c_reinstatement_route",
        reinstatement_candidate=True,
        packet_classification=packet_audit.classification,
        verdict_classification=verdict_audit.classification,
        preserved_target_classification=preserved_classification,
        reason=(
            "The proposal clears packet intake, architecture consistency, typed "
            "verdict lift, and any required preserved-target honesty screen."
        ),
        required_next=(
            "Bind this stack-positive shape to a named monitored-qubit platform and "
            "run the event-level screens on real data."
        ),
    )


def _architecture_matches_verdict(
    packet: Q1CPlatformPacketInput,
    verdict: Q1CVerdictInput,
) -> bool:
    if packet.architecture_class == "extra_environment":
        return (
            verdict.captures_extra_environment_structure
            and not verdict.explicitly_enlarges_instrument
        )
    if packet.architecture_class == "enlarged_instrument":
        return (
            verdict.explicitly_enlarges_instrument
            and verdict.preserved_comparison_target_declared
            and not verdict.captures_extra_environment_structure
        )
    return False


def canonical_reinstatement_cases() -> tuple[
    tuple[str, Q1CReinstatementProposal],
    ...
]:
    extra_packet = _extra_environment_packet()
    enlarged_packet = _enlarged_instrument_packet()
    return (
        (
            "positive_control_extra_environment_stack",
            Q1CReinstatementProposal(
                packet=extra_packet,
                verdict=_typed_extra_environment_verdict(),
            ),
        ),
        (
            "positive_control_enlarged_instrument_stack",
            Q1CReinstatementProposal(
                packet=enlarged_packet,
                verdict=_typed_enlarged_instrument_verdict(),
                preserved_target=_honest_preserved_target(),
            ),
        ),
        (
            "packet_only_no_event_data",
            Q1CReinstatementProposal(packet=extra_packet, verdict=None),
        ),
        (
            "zero_lift_extra_environment_packet",
            Q1CReinstatementProposal(
                packet=extra_packet,
                verdict=_zero_lift_extra_environment_verdict(),
            ),
        ),
        (
            "auxiliary_defined_verdict_packet",
            Q1CReinstatementProposal(
                packet=extra_packet,
                verdict=_auxiliary_defined_extra_environment_verdict(),
            ),
        ),
        (
            "enlarged_instrument_target_drift",
            Q1CReinstatementProposal(
                packet=enlarged_packet,
                verdict=_typed_enlarged_instrument_verdict(),
                preserved_target=_drifting_preserved_target(),
            ),
        ),
        (
            "coarse_record_packet",
            Q1CReinstatementProposal(
                packet=_coarse_record_packet(),
                verdict=_typed_extra_environment_verdict(),
            ),
        ),
        current_frontier_case(),
    )


def current_frontier_case() -> tuple[str, Q1CReinstatementProposal]:
    return (
        "current_frontier",
        Q1CReinstatementProposal(
            packet=Q1CPlatformPacketInput(
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
            verdict=None,
        ),
    )


def run_t183_analysis() -> T183Result:
    audits = tuple(
        classify_reinstatement_stack(proposal, name=name)
        for name, proposal in canonical_reinstatement_cases()
    )
    audit_by_name = {audit.name: audit for audit in audits}
    positive_controls = (
        "positive_control_extra_environment_stack",
        "positive_control_enlarged_instrument_stack",
    )
    null_controls = (
        "packet_only_no_event_data",
        "zero_lift_extra_environment_packet",
        "auxiliary_defined_verdict_packet",
        "enlarged_instrument_target_drift",
        "coarse_record_packet",
        "current_frontier",
    )

    return T183Result(
        audits=audits,
        positive_controls_admitted=all(
            audit_by_name[name].reinstatement_candidate for name in positive_controls
        ),
        null_controls_rejected=all(
            not audit_by_name[name].reinstatement_candidate for name in null_controls
        ),
        current_frontier_reopened=audit_by_name["current_frontier"].reinstatement_candidate,
        strongest_claim=(
            "Q1C is not reopened by clearing one local gate. Reinstatement requires "
            "a stack-positive proposal: T166 packet intake, architecture consistency, "
            "T149/T150 typed verdict lift, and T158 preserved-target honesty for "
            "enlarged instruments."
        ),
        improved=(
            "T183 composes the previously separate Q1C gates into one executable "
            "proposal-level screen. A reviewer no longer has to infer how packet "
            "intake, verdict lift, and enlarged-instrument honesty interact."
        ),
        weakened=(
            "This weakens Q1C's remaining positive-control language. A packet that "
            "only promises data, a zero-lift packet, an auxiliary-defined verdict, "
            "or an enlarged instrument with target drift cannot reopen the branch."
        ),
        falsification_condition=(
            "T183 fails if a serious Q1C platform should be treated as reinstated "
            "after clearing only one of the packet, verdict, or preserved-target "
            "gates, or if either stack-positive control is rejected despite satisfying "
            "all lower-level assumptions."
        ),
        q1c_update=(
            "Q1C remains dormant. The live burden is now a stack-level reinstatement "
            "packet, not a platform-family name or a local positive control."
        ),
        claim_ledger_update=(
            "Add T183 to Q1C: reinstatement requires the composed T166/T149/T150/"
            "T158 stack. Packet-only, zero-lift, auxiliary-defined, target-drift, "
            "coarse-record, and current-frontier proposals remain blocked."
        ),
        open_blocker=(
            "No named monitored-qubit platform in the repo supplies a stack-positive "
            "Q1C proposal with frozen packet, typed verdict lift, and, if enlarged, "
            "eventwise preserved-target honesty."
        ),
        suggested_next=(
            "Stop internal Q1C toy work unless a named platform can instantiate the "
            "full T183 stack. Otherwise shift the quantum route toward Q1B deployment "
            "or away from Q1 entirely."
        ),
    )


def _extra_environment_packet() -> Q1CPlatformPacketInput:
    return Q1CPlatformPacketInput(
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
    )


def _enlarged_instrument_packet() -> Q1CPlatformPacketInput:
    return Q1CPlatformPacketInput(
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
        enlarged_instrument_back_projection_declared=True,
        enlarged_instrument_preserved_target_declared=True,
        preserved_target_is_full_standard_record=True,
    )


def _coarse_record_packet() -> Q1CPlatformPacketInput:
    return Q1CPlatformPacketInput(
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
    )


def _typed_extra_environment_verdict() -> Q1CVerdictInput:
    return Q1CVerdictInput(
        full_event_standard_record_fixed=True,
        auxiliary_is_proxy_or_postselected=False,
        same_declared_instrument=False,
        captures_extra_environment_structure=True,
        explicitly_enlarges_instrument=False,
        preserved_comparison_target_declared=False,
        verdict_declared_before_analysis=True,
        hidden_axis_declared=True,
        hidden_axis_name="branch_support_state",
        minimum_class_support=Fraction(1, 5),
        events=_balanced_verdict_events(),
    )


def _typed_enlarged_instrument_verdict() -> Q1CVerdictInput:
    return Q1CVerdictInput(
        full_event_standard_record_fixed=True,
        auxiliary_is_proxy_or_postselected=False,
        same_declared_instrument=False,
        captures_extra_environment_structure=False,
        explicitly_enlarges_instrument=True,
        preserved_comparison_target_declared=True,
        verdict_declared_before_analysis=True,
        hidden_axis_declared=True,
        hidden_axis_name="undo_cost_class",
        minimum_class_support=Fraction(1, 5),
        events=_balanced_verdict_events(),
    )


def _zero_lift_extra_environment_verdict() -> Q1CVerdictInput:
    return Q1CVerdictInput(
        full_event_standard_record_fixed=True,
        auxiliary_is_proxy_or_postselected=False,
        same_declared_instrument=False,
        captures_extra_environment_structure=True,
        explicitly_enlarges_instrument=False,
        preserved_comparison_target_declared=False,
        verdict_declared_before_analysis=True,
        hidden_axis_declared=True,
        hidden_axis_name="branch_support_state",
        minimum_class_support=Fraction(1, 5),
        events=(
            VerdictEvent("h0", "r0", "a0", "v0", Fraction(1, 2)),
            VerdictEvent("h1", "r1", "a1", "v1", Fraction(1, 2)),
        ),
    )


def _auxiliary_defined_extra_environment_verdict() -> Q1CVerdictInput:
    return Q1CVerdictInput(
        full_event_standard_record_fixed=True,
        auxiliary_is_proxy_or_postselected=False,
        same_declared_instrument=False,
        captures_extra_environment_structure=True,
        explicitly_enlarges_instrument=False,
        preserved_comparison_target_declared=False,
        verdict_declared_before_analysis=True,
        hidden_axis_declared=True,
        hidden_axis_name="provenance_state",
        minimum_class_support=Fraction(1, 5),
        events=(
            VerdictEvent("h0", "r0", "a0", "v0", Fraction(1, 4)),
            VerdictEvent("h0", "r0", "a1", "v1", Fraction(1, 4)),
            VerdictEvent("h1", "r1", "a0", "v0", Fraction(1, 4)),
            VerdictEvent("h1", "r1", "a1", "v1", Fraction(1, 4)),
        ),
    )


def _balanced_verdict_events() -> tuple[VerdictEvent, ...]:
    return (
        VerdictEvent("h0", "r0", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h1", "r0", "a1", "v1", Fraction(1, 4)),
        VerdictEvent("h0", "r1", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h1", "r1", "a1", "v1", Fraction(1, 4)),
    )


def _honest_preserved_target() -> Q1CPreservedTargetInput:
    return Q1CPreservedTargetInput(
        enlarged_instrument_declared=True,
        preserved_target_declared=True,
        target_declared_before_analysis=True,
        preserved_target_is_full_standard_record=True,
        events=(
            PreservedTargetEvent("r0", "r0+e0", "r0", "v0", Fraction(1, 4)),
            PreservedTargetEvent("r0", "r0+e1", "r0", "v1", Fraction(1, 4)),
            PreservedTargetEvent("r1", "r1+e0", "r1", "v0", Fraction(1, 4)),
            PreservedTargetEvent("r1", "r1+e1", "r1", "v1", Fraction(1, 4)),
        ),
    )


def _drifting_preserved_target() -> Q1CPreservedTargetInput:
    return Q1CPreservedTargetInput(
        enlarged_instrument_declared=True,
        preserved_target_declared=True,
        target_declared_before_analysis=True,
        preserved_target_is_full_standard_record=True,
        events=(
            PreservedTargetEvent("r0", "r0+e0", "r0", "v0", Fraction(1, 4)),
            PreservedTargetEvent("r0", "r0+e1", "r1", "v1", Fraction(1, 4)),
            PreservedTargetEvent("r1", "r1+e0", "r1", "v0", Fraction(1, 4)),
            PreservedTargetEvent("r1", "r1+e1", "r0", "v1", Fraction(1, 4)),
        ),
    )


def _audit_to_dict(audit: Q1CReinstatementAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "reinstatement_candidate": audit.reinstatement_candidate,
        "packet_classification": audit.packet_classification,
        "verdict_classification": audit.verdict_classification,
        "preserved_target_classification": audit.preserved_target_classification,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t183_result_to_dict(result: T183Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "positive_controls_admitted": result.positive_controls_admitted,
        "null_controls_rejected": result.null_controls_rejected,
        "current_frontier_reopened": result.current_frontier_reopened,
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "q1c_update": result.q1c_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "suggested_next": result.suggested_next,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(t183_result_to_dict(run_t183_analysis()), indent=2))
