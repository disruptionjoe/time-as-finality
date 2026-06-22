"""T182: executable screen for named Q1C weak-measurement platform families.

N9 established in prose that the currently named superconducting weak-
measurement, thermal-detector, nanocalorimetric, and calorimeter-assisted
families do not instantiate one of the two live Q1C escape classes. This
module makes that census executable so future review does not depend on a
reader trusting the narrative summary.
"""

from __future__ import annotations

from dataclasses import dataclass


LIVE_Q1C_CLASSES = frozenset({"extra_environment", "enlarged_instrument"})


@dataclass(frozen=True)
class PlatformFamilyCase:
    family_id: str
    source_family: str
    monitored_qubit_platform: bool
    ordinary_record_role: str
    simultaneous_auxiliary_channel: bool
    auxiliary_channel_independent_of_full_record: bool
    architecture_class: str
    preserved_target_declared: bool = False
    preserved_target_is_full_standard_record: bool = False
    back_projection_declared: bool = False
    packet_complete: bool = False


@dataclass(frozen=True)
class PlatformFamilyAudit:
    family_id: str
    classification: str
    q1c_live: bool
    route_type: str
    reason: str
    required_next: str


@dataclass(frozen=True)
class T182Result:
    audits: tuple[PlatformFamilyAudit, ...]
    named_platforms_live: int
    named_platforms_screened: int
    positive_controls_admitted: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def classify_platform_family(case: PlatformFamilyCase) -> PlatformFamilyAudit:
    if not case.monitored_qubit_platform:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_task_changed_non_monitored_qubit",
            q1c_live=False,
            route_type="task_change",
            reason=(
                "The source changes the measurement object or task rather than "
                "naming a monitored-qubit auxiliary channel over a fixed standard "
                "record."
            ),
            required_next="Return to a monitored-qubit platform with a fixed standard record.",
        )
    if case.ordinary_record_role == "ordinary_record_baseline":
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_ordinary_record_baseline",
            q1c_live=False,
            route_type="baseline_record",
            reason=(
                "The measured trace is the ordinary monitored record itself, so "
                "there is no separate Q1C auxiliary axis yet."
            ),
            required_next="Name an auxiliary channel beyond the ordinary monitored transcript.",
        )
    if case.ordinary_record_role == "same_instrument_postselected_control":
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_same_instrument_postselected_control",
            q1c_live=False,
            route_type="same_instrument_control",
            reason=(
                "The apparent discriminator is ordinary same-instrument monitoring "
                "or success-conditioned control rather than an independent TaF axis "
                "at fixed standard statistics."
            ),
            required_next="Hold reversal success fixed and expose a distinct auxiliary channel.",
        )
    if case.ordinary_record_role == "alternate_ordinary_record":
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_alternate_ordinary_record",
            q1c_live=False,
            route_type="alternate_record",
            reason=(
                "The calorimetric or click stream is itself the trajectory-defining "
                "ordinary record, not an auxiliary verdict-changing channel over a "
                "fixed standard record."
            ),
            required_next="Keep the standard record fixed and add a non-screened-off auxiliary axis.",
        )
    if case.architecture_class not in LIVE_Q1C_CLASSES:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_invalid_architecture_class",
            q1c_live=False,
            route_type="underdeclared_architecture",
            reason=(
                "The family does not instantiate either live Q1C class: extra-"
                "environment auxiliary structure or honest instrument enlargement."
            ),
            required_next="Declare one of the two live Q1C architecture classes.",
        )
    if case.architecture_class == "extra_environment":
        if not case.simultaneous_auxiliary_channel:
            return PlatformFamilyAudit(
                family_id=case.family_id,
                classification="blocked_missing_simultaneous_auxiliary_channel",
                q1c_live=False,
                route_type="extra_environment",
                reason=(
                    "An extra-environment route is named, but no simultaneous "
                    "auxiliary channel is exposed alongside the ordinary record."
                ),
                required_next="Expose a simultaneous auxiliary channel aligned eventwise with the ordinary record.",
            )
        if not case.auxiliary_channel_independent_of_full_record:
            return PlatformFamilyAudit(
                family_id=case.family_id,
                classification="null_screened_off_auxiliary_channel",
                q1c_live=False,
                route_type="extra_environment",
                reason=(
                    "The auxiliary content is screened off by the full ordinary "
                    "record, so it does not reopen Q1C."
                ),
                required_next="Show positive verdict lift beyond the full ordinary transcript.",
            )
        if not case.packet_complete:
            return PlatformFamilyAudit(
                family_id=case.family_id,
                classification="blocked_incomplete_t166_packet",
                q1c_live=False,
                route_type="extra_environment",
                reason=(
                    "The route has the right architecture shape but does not yet "
                    "freeze the full T166 packet."
                ),
                required_next="Freeze the full R/A/H/V/loss/support/control packet.",
            )
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="provisional_live_extra_environment_route",
            q1c_live=True,
            route_type="extra_environment",
            reason=(
                "The platform exposes a simultaneous auxiliary channel tied to "
                "extra environment structure, not screened off by the full ordinary "
                "record, and freezes the intake packet."
            ),
            required_next="Run T149/T150 event-level verdict-lift screens.",
        )
    if not case.preserved_target_declared:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="blocked_honest_enlargement_without_preserved_target",
            q1c_live=False,
            route_type="enlarged_instrument",
            reason=(
                "The family is an honest readout replacement or enlargement, but it "
                "does not predeclare the preserved fixed-standard comparison target."
            ),
            required_next="Declare the preserved comparison target before analysis.",
        )
    if not case.preserved_target_is_full_standard_record:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="null_coarse_preserved_target",
            q1c_live=False,
            route_type="enlarged_instrument",
            reason=(
                "The proposed preserved target is coarser than the full ordinary "
                "standard record."
            ),
            required_next="Preserve the full ordinary event-level standard record exactly.",
        )
    if not case.back_projection_declared:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="blocked_missing_back_projection",
            q1c_live=False,
            route_type="enlarged_instrument",
            reason=(
                "The platform does not declare an eventwise back-projection from "
                "enlarged data to the full ordinary standard record."
            ),
            required_next="Declare an eventwise back-projection to the full standard record.",
        )
    if not case.packet_complete:
        return PlatformFamilyAudit(
            family_id=case.family_id,
            classification="blocked_incomplete_t166_packet",
            q1c_live=False,
            route_type="enlarged_instrument",
            reason=(
                "The enlarged-instrument route declares the right honesty fields "
                "but still does not freeze the rest of the T166 packet."
            ),
            required_next="Freeze the remaining T166 packet fields before analysis.",
        )
    return PlatformFamilyAudit(
        family_id=case.family_id,
        classification="provisional_live_enlarged_instrument_route",
        q1c_live=True,
        route_type="enlarged_instrument",
        reason=(
            "The platform is an explicit enlarged instrument that preserves the "
            "full standard record under a declared back-projection and freezes the "
            "intake packet."
        ),
        required_next="Run T149/T150/T158 event-level verdict-lift screens.",
    )


def canonical_platform_family_cases() -> tuple[PlatformFamilyCase, ...]:
    return (
        PlatformFamilyCase(
            family_id="murch_koolstra_homodyne_trajectory",
            source_family="Murch 2013 / Koolstra 2021",
            monitored_qubit_platform=True,
            ordinary_record_role="ordinary_record_baseline",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="ordinary_record",
        ),
        PlatformFamilyCase(
            family_id="minev_jump_reversal",
            source_family="Minev 2018/2019",
            monitored_qubit_platform=True,
            ordinary_record_role="same_instrument_postselected_control",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="same_instrument",
        ),
        PlatformFamilyCase(
            family_id="opremcak_photon_counter_replacement",
            source_family="Opremcak 2018",
            monitored_qubit_platform=True,
            ordinary_record_role="replacement_readout",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="enlarged_instrument",
        ),
        PlatformFamilyCase(
            family_id="gunyho_thermal_detector_replacement",
            source_family="Gunyho 2023/2024",
            monitored_qubit_platform=True,
            ordinary_record_role="replacement_readout",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="enlarged_instrument",
        ),
        PlatformFamilyCase(
            family_id="karimi_nanocalorimetric_trajectory",
            source_family="Karimi and Pekola 2020",
            monitored_qubit_platform=True,
            ordinary_record_role="alternate_ordinary_record",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="ordinary_record",
        ),
        PlatformFamilyCase(
            family_id="shojaee_calorimeter_assisted_quadrature",
            source_family="Shojaee et al. 2025",
            monitored_qubit_platform=False,
            ordinary_record_role="task_change",
            simultaneous_auxiliary_channel=False,
            auxiliary_channel_independent_of_full_record=False,
            architecture_class="enlarged_instrument",
        ),
        PlatformFamilyCase(
            family_id="positive_control_extra_environment",
            source_family="Hypothetical positive control",
            monitored_qubit_platform=True,
            ordinary_record_role="replacement_readout",
            simultaneous_auxiliary_channel=True,
            auxiliary_channel_independent_of_full_record=True,
            architecture_class="extra_environment",
            packet_complete=True,
        ),
        PlatformFamilyCase(
            family_id="positive_control_enlarged_instrument",
            source_family="Hypothetical positive control",
            monitored_qubit_platform=True,
            ordinary_record_role="replacement_readout",
            simultaneous_auxiliary_channel=True,
            auxiliary_channel_independent_of_full_record=True,
            architecture_class="enlarged_instrument",
            preserved_target_declared=True,
            preserved_target_is_full_standard_record=True,
            back_projection_declared=True,
            packet_complete=True,
        ),
    )


def run_t182_analysis() -> T182Result:
    audits = tuple(
        classify_platform_family(case) for case in canonical_platform_family_cases()
    )
    named_audits = tuple(
        audit for audit in audits if not audit.family_id.startswith("positive_control_")
    )
    positive_control_ids = {
        "positive_control_extra_environment",
        "positive_control_enlarged_instrument",
    }
    positive_controls_admitted = all(
        audit.q1c_live for audit in audits if audit.family_id in positive_control_ids
    )

    return T182Result(
        audits=audits,
        named_platforms_live=sum(audit.q1c_live for audit in named_audits),
        named_platforms_screened=len(named_audits),
        positive_controls_admitted=positive_controls_admitted,
        strongest_claim=(
            "The current named Q1C-adjacent platform families do not instantiate a "
            "live TaF discriminator. They fall into ordinary-record baseline, same-"
            "instrument/postselected control, honest readout replacement without a "
            "preserved fixed-standard target, alternate ordinary record, or task-"
            "changed non-monitored-qubit classes."
        ),
        improved=(
            "T182 turns N9's literature census into an executable screen. A reader "
            "can now see exactly which route each named family falls into and which "
            "missing field keeps it out of the live Q1C frontier."
        ),
        weakened=(
            "This weakens the residual hope that one of the already named hardware "
            "families is secretly close to a Q1C witness. None of them clears even "
            "the architecture-level screening burden."
        ),
        falsification_condition=(
            "T182 fails if one of the screened named families already preserves a "
            "fixed full ordinary record while adding an auxiliary verdict-changing "
            "channel or an honest enlarged-instrument back-projection that the "
            "screen misclassifies as null or blocked."
        ),
        q1c_update=(
            "Q1C remains dormant. N9 is no longer just a prose census: T182 makes "
            "the current named-platform verdict executable and keeps the branch shut "
            "until a genuinely live family appears."
        ),
        claim_ledger_update=(
            "Add T182 to Q1C: the named superconducting homodyne, jump-reversal, "
            "photon-counter, thermal-detector, nanocalorimetric, and calorimeter-"
            "assisted families are now executable null or blocked classes rather "
            "than prose-only exclusions."
        ),
        open_blocker=(
            "No named family currently supplies a monitored-qubit simultaneous "
            "auxiliary channel independent of the full ordinary record, and no "
            "named enlarged-instrument family declares the preserved full-standard "
            "target plus back-projection needed for T158."
        ),
        recommended_next=(
            "Do not rescan the same platform families. Look only for a new source "
            "family that either exposes extra-environment eventwise structure or "
            "predeclares an honest enlarged-instrument preserved target."
        ),
    )


def _audit_to_dict(audit: PlatformFamilyAudit) -> dict[str, object]:
    return {
        "family_id": audit.family_id,
        "classification": audit.classification,
        "q1c_live": audit.q1c_live,
        "route_type": audit.route_type,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t182_result_to_dict(result: T182Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "named_platforms_live": result.named_platforms_live,
        "named_platforms_screened": result.named_platforms_screened,
        "positive_controls_admitted": result.positive_controls_admitted,
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

    print(json.dumps(t182_result_to_dict(run_t182_analysis()), indent=2))
