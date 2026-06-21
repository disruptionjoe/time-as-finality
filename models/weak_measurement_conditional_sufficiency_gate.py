"""T149: conditional-sufficiency gate for weak-measurement Q1C proposals.

T146 left two live architecture classes for Q1C, but the phrase "survives
full-record conditioning" still needed an operational test. This module gives
the finite version: after the full ordinary monitored record R is fixed, an
auxiliary channel A is non-null only if adding A strictly improves a declared
decision problem for the Q1C verdict V, and the source of that improvement is
physically typed as either extra environment structure or an explicit
instrument enlargement with a preserved comparison target.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class MeasurementEvent:
    record: str
    auxiliary: str
    verdict: str
    probability: Fraction


@dataclass(frozen=True)
class Q1CConditionalInput:
    full_event_standard_record_fixed: bool
    auxiliary_is_proxy_or_postselected: bool
    same_declared_instrument: bool
    captures_extra_environment_structure: bool
    explicitly_enlarges_instrument: bool
    preserved_comparison_target_declared: bool
    events: tuple[MeasurementEvent, ...]
    minimum_lift: Fraction = Fraction(0, 1)


@dataclass(frozen=True)
class Q1CConditionalAudit:
    name: str
    classification: str
    active_route: bool
    record_only_risk: Fraction
    record_auxiliary_risk: Fraction
    conditional_lift: Fraction
    reason: str
    required_next: str


@dataclass(frozen=True)
class T149Result:
    audits: tuple[Q1CConditionalAudit, ...]
    all_null_controls_rejected: bool
    live_cases_have_positive_lift: bool
    current_frontier_active: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _total_probability(events: tuple[MeasurementEvent, ...]) -> Fraction:
    total = sum((event.probability for event in events), Fraction(0, 1))
    if total <= 0:
        raise ValueError("event probabilities must have positive total mass")
    return total


def bayes_error(
    events: tuple[MeasurementEvent, ...],
    feature_names: tuple[str, ...],
) -> Fraction:
    """Return the optimal 0-1 decision risk for predicting verdict from features."""

    total_probability = _total_probability(events)
    grouped: dict[tuple[str, ...], dict[str, Fraction]] = {}
    for event in events:
        feature_key = tuple(getattr(event, feature_name) for feature_name in feature_names)
        verdict_mass = grouped.setdefault(feature_key, {})
        verdict_mass[event.verdict] = verdict_mass.get(event.verdict, Fraction(0, 1)) + event.probability

    correct_mass = Fraction(0, 1)
    for verdict_mass in grouped.values():
        correct_mass += max(verdict_mass.values())
    return Fraction(1, 1) - (correct_mass / total_probability)


def classify_conditional_sufficiency(
    case: Q1CConditionalInput,
    *,
    name: str,
) -> Q1CConditionalAudit:
    record_only_risk = bayes_error(case.events, ("record",))
    record_auxiliary_risk = bayes_error(case.events, ("record", "auxiliary"))
    conditional_lift = record_only_risk - record_auxiliary_risk
    has_positive_lift = conditional_lift > case.minimum_lift

    if not case.full_event_standard_record_fixed:
        return Q1CConditionalAudit(
            name=name,
            classification="null_coarse_standard_record",
            active_route=False,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The auxiliary channel improves a coarse record, but the full ordinary "
                "event-level transcript has not been fixed."
            ),
            required_next="Define the full ordinary monitored transcript before testing lift.",
        )
    if case.auxiliary_is_proxy_or_postselected:
        return Q1CConditionalAudit(
            name=name,
            classification="null_proxy_or_postselection",
            active_route=False,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The lift comes from a control proxy or success-conditioned subset, "
                "not from a pre-analysis auxiliary channel."
            ),
            required_next="Replace the proxy with a calibrated event-level auxiliary meter.",
        )
    if not has_positive_lift:
        return Q1CConditionalAudit(
            name=name,
            classification="null_conditionally_sufficient_record",
            active_route=False,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "Adding the auxiliary channel does not improve the declared verdict "
                "decision problem once the full ordinary record is fixed."
            ),
            required_next="Show a positive predeclared decision-risk lift at fixed full record.",
        )
    if case.explicitly_enlarges_instrument and not case.preserved_comparison_target_declared:
        return Q1CConditionalAudit(
            name=name,
            classification="underdeclared_instrument_enlargement",
            active_route=False,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The auxiliary channel has positive lift only after changing the "
                "instrument, but the preserved fixed-standard comparison target is "
                "not declared."
            ),
            required_next="Declare the enlarged instrument and preserved comparison target.",
        )
    if (
        case.same_declared_instrument
        and not case.captures_extra_environment_structure
        and not case.explicitly_enlarges_instrument
    ):
        return Q1CConditionalAudit(
            name=name,
            classification="underdeclared_same_instrument_lift",
            active_route=False,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The statistics show lift, but the proposal says the auxiliary channel "
                "is inside the same declared instrument and names no extra structure. "
                "That means either the full record was underdeclared or the physical "
                "source of the lift is missing."
            ),
            required_next="Name the extra structure or admit an instrument enlargement.",
        )
    if case.captures_extra_environment_structure and not case.explicitly_enlarges_instrument:
        return Q1CConditionalAudit(
            name=name,
            classification="candidate_extra_environment_conditional_lift",
            active_route=True,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The auxiliary channel gives positive decision lift at fixed full "
                "ordinary record and is tied to extra environment or detector "
                "structure."
            ),
            required_next="Bind this finite lift to a named monitored-qubit platform.",
        )
    if case.explicitly_enlarges_instrument and case.preserved_comparison_target_declared:
        return Q1CConditionalAudit(
            name=name,
            classification="candidate_enlarged_instrument_conditional_lift",
            active_route=True,
            record_only_risk=record_only_risk,
            record_auxiliary_risk=record_auxiliary_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The auxiliary channel gives positive decision lift and the instrument "
                "enlargement is explicit with a preserved comparison target."
            ),
            required_next="Audit whether the preserved comparison target is physically honest.",
        )
    return Q1CConditionalAudit(
        name=name,
        classification="underdescribed_positive_lift",
        active_route=False,
        record_only_risk=record_only_risk,
        record_auxiliary_risk=record_auxiliary_risk,
        conditional_lift=conditional_lift,
        reason="The finite lift is positive, but the physical architecture is not typed.",
        required_next="Declare the record, auxiliary source, instrument boundary, and verdict role.",
    )


def _screened_copy_events() -> tuple[MeasurementEvent, ...]:
    return (
        MeasurementEvent("r0", "a0", "v0", Fraction(1, 2)),
        MeasurementEvent("r1", "a1", "v1", Fraction(1, 2)),
    )


def _independent_noise_events() -> tuple[MeasurementEvent, ...]:
    return (
        MeasurementEvent("r0", "a0", "v0", Fraction(1, 8)),
        MeasurementEvent("r0", "a1", "v0", Fraction(1, 8)),
        MeasurementEvent("r0", "a0", "v1", Fraction(1, 8)),
        MeasurementEvent("r0", "a1", "v1", Fraction(1, 8)),
        MeasurementEvent("r1", "a0", "v0", Fraction(1, 8)),
        MeasurementEvent("r1", "a1", "v0", Fraction(1, 8)),
        MeasurementEvent("r1", "a0", "v1", Fraction(1, 8)),
        MeasurementEvent("r1", "a1", "v1", Fraction(1, 8)),
    )


def _positive_lift_events() -> tuple[MeasurementEvent, ...]:
    return (
        MeasurementEvent("r0", "a0", "v0", Fraction(1, 4)),
        MeasurementEvent("r0", "a1", "v1", Fraction(1, 4)),
        MeasurementEvent("r1", "a0", "v0", Fraction(1, 4)),
        MeasurementEvent("r1", "a1", "v1", Fraction(1, 4)),
    )


def canonical_conditional_cases() -> tuple[tuple[str, Q1CConditionalInput], ...]:
    positive_events = _positive_lift_events()
    return (
        (
            "screened_copy_meter",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=_screened_copy_events(),
            ),
        ),
        (
            "independent_noise_meter",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=_independent_noise_events(),
            ),
        ),
        (
            "coarse_record_refinement_only",
            Q1CConditionalInput(
                full_event_standard_record_fixed=False,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=positive_events,
            ),
        ),
        (
            "postselected_positive_lift",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=True,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=positive_events,
            ),
        ),
        (
            "same_instrument_positive_lift",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=positive_events,
            ),
        ),
        (
            "extra_environment_candidate",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                events=positive_events,
            ),
        ),
        (
            "underdeclared_enlarged_instrument",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=True,
                preserved_comparison_target_declared=False,
                events=positive_events,
            ),
        ),
        (
            "enlarged_instrument_candidate",
            Q1CConditionalInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=True,
                preserved_comparison_target_declared=True,
                events=positive_events,
            ),
        ),
    )


def current_frontier_case() -> tuple[str, Q1CConditionalInput]:
    return (
        "current_frontier",
        Q1CConditionalInput(
            full_event_standard_record_fixed=True,
            auxiliary_is_proxy_or_postselected=False,
            same_declared_instrument=True,
            captures_extra_environment_structure=False,
            explicitly_enlarges_instrument=False,
            preserved_comparison_target_declared=False,
            events=_screened_copy_events(),
        ),
    )


def run_t149_analysis() -> T149Result:
    audits = tuple(
        classify_conditional_sufficiency(case, name=name)
        for name, case in canonical_conditional_cases()
    )
    current_name, current_case = current_frontier_case()
    current_audit = classify_conditional_sufficiency(current_case, name=current_name)
    audits = audits + (current_audit,)

    active_audits = tuple(audit for audit in audits if audit.active_route)
    null_control_names = {
        "screened_copy_meter",
        "independent_noise_meter",
        "coarse_record_refinement_only",
        "postselected_positive_lift",
        "same_instrument_positive_lift",
        "underdeclared_enlarged_instrument",
        "current_frontier",
    }
    all_null_controls_rejected = all(
        not audit.active_route for audit in audits if audit.name in null_control_names
    )
    live_cases_have_positive_lift = all(
        audit.conditional_lift > 0 for audit in active_audits
    )

    return T149Result(
        audits=audits,
        all_null_controls_rejected=all_null_controls_rejected,
        live_cases_have_positive_lift=live_cases_have_positive_lift,
        current_frontier_active=current_audit.active_route,
        strongest_claim=(
            "Q1C's remaining weak-measurement gate should be stated as a "
            "conditional decision-sufficiency test. With the full ordinary "
            "event-level record R fixed, an auxiliary channel A is non-null "
            "only if adding A strictly lowers a predeclared verdict risk for "
            "V, and the source of that lift is physically typed as extra "
            "environment structure or an explicit instrument enlargement with "
            "a preserved comparison target."
        ),
        improved=(
            "T149 turns 'not screened off by the full record' into an executable "
            "finite risk comparison. A platform proposal now needs R, A, V, a "
            "loss rule, and an architecture declaration before it can be called "
            "a Q1C candidate."
        ),
        weakened=(
            "This further weakens Q1C: a physically distinct meter, a better "
            "coarse summary, or a positive lift with no typed physical source "
            "does not count. Current Q1C remains a reinstatement gate, not a "
            "measurement-dynamics claim."
        ),
        falsification_condition=(
            "T149 fails if a calibrated platform produces a pre-registered "
            "positive decision lift at fixed full ordinary record while neither "
            "extra environment structure nor instrument enlargement is needed, "
            "or if a zero-lift auxiliary channel can still force a legitimate "
            "verdict split under the declared loss."
        ),
        q1c_update=(
            "Q1C remains dormant. Reopen it only with a named monitored-qubit "
            "platform that supplies a positive conditional decision lift at "
            "fixed full ordinary record and clears either the extra-environment "
            "or enlarged-instrument architecture gate."
        ),
        claim_ledger_update=(
            "Add T149 to Q1C: 'survives full-record conditioning' now means "
            "positive predeclared decision-risk lift from adding the auxiliary "
            "channel to the full ordinary transcript, plus a physically typed "
            "source for that lift. Zero-lift, coarse-record, postselected, and "
            "underdeclared same-instrument routes are null."
        ),
        open_blocker=(
            "The repo still has no named monitored-qubit platform with R, A, V, "
            "loss function, event-level data schema, and architecture declaration "
            "sufficient to run this gate."
        ),
        recommended_next=(
            "Do not add more Q1C toy proposals unless they instantiate the T149 "
            "input tuple on a real platform. If no platform can supply the tuple, "
            "leave Q1C dormant and work another route."
        ),
    )


def _fraction_to_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _audit_to_dict(audit: Q1CConditionalAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "active_route": audit.active_route,
        "record_only_risk": _fraction_to_payload(audit.record_only_risk),
        "record_auxiliary_risk": _fraction_to_payload(audit.record_auxiliary_risk),
        "conditional_lift": _fraction_to_payload(audit.conditional_lift),
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t149_result_to_dict(result: T149Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "all_null_controls_rejected": result.all_null_controls_rejected,
        "live_cases_have_positive_lift": result.live_cases_have_positive_lift,
        "current_frontier_active": result.current_frontier_active,
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

    print(json.dumps(t149_result_to_dict(run_t149_analysis()), indent=2))
