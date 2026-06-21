"""T158: preserved-target honesty gate for enlarged-instrument Q1C proposals.

T146/T149/T150 leave one live Q1C architecture class in which the monitored
instrument is enlarged openly. That class is still too loose if "preserved
comparison target" remains prose. This module makes the burden executable: an
enlarged instrument is live only if it predeclares a projection back to the
full ordinary standard record, that projection is eventwise honest on the
admissible domain, and the enlarged record then adds positive verdict lift
beyond the preserved target rather than redefining it.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class PreservedTargetEvent:
    standard_record: str
    enlarged_record: str
    projected_standard_record: str
    verdict: str
    probability: Fraction


@dataclass(frozen=True)
class Q1CPreservedTargetInput:
    enlarged_instrument_declared: bool
    preserved_target_declared: bool
    target_declared_before_analysis: bool
    preserved_target_is_full_standard_record: bool
    events: tuple[PreservedTargetEvent, ...]
    minimum_lift: Fraction = Fraction(0, 1)


@dataclass(frozen=True)
class Q1CPreservedTargetAudit:
    name: str
    classification: str
    active_route: bool
    target_projection_error: Fraction
    standard_only_risk: Fraction
    enlarged_record_risk: Fraction
    conditional_lift: Fraction
    reason: str
    required_next: str


@dataclass(frozen=True)
class T158Result:
    audits: tuple[Q1CPreservedTargetAudit, ...]
    all_null_controls_rejected: bool
    live_cases_honest: bool
    current_frontier_active: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _total_probability(events: tuple[PreservedTargetEvent, ...]) -> Fraction:
    total = sum((event.probability for event in events), Fraction(0, 1))
    if total <= 0:
        raise ValueError("event probabilities must have positive total mass")
    return total


def bayes_error(
    events: tuple[PreservedTargetEvent, ...],
    feature_names: tuple[str, ...],
) -> Fraction:
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


def projection_error(events: tuple[PreservedTargetEvent, ...]) -> Fraction:
    total_probability = _total_probability(events)
    mismatch_mass = sum(
        (
            event.probability
            for event in events
            if event.standard_record != event.projected_standard_record
        ),
        Fraction(0, 1),
    )
    return mismatch_mass / total_probability


def classify_preserved_target(
    case: Q1CPreservedTargetInput,
    *,
    name: str,
) -> Q1CPreservedTargetAudit:
    target_projection_error = projection_error(case.events)
    standard_only_risk = bayes_error(case.events, ("standard_record",))
    enlarged_record_risk = bayes_error(case.events, ("enlarged_record",))
    conditional_lift = standard_only_risk - enlarged_record_risk
    has_positive_lift = conditional_lift > case.minimum_lift

    if not case.enlarged_instrument_declared:
        return Q1CPreservedTargetAudit(
            name=name,
            classification="null_not_an_enlarged_instrument_case",
            active_route=False,
            target_projection_error=target_projection_error,
            standard_only_risk=standard_only_risk,
            enlarged_record_risk=enlarged_record_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The proposal does not openly declare an enlarged monitored instrument, "
                "so the preserved-target gate does not apply."
            ),
            required_next="Either stay in the same-instrument null class or declare the enlargement.",
        )
    if not case.preserved_target_declared or not case.target_declared_before_analysis:
        return Q1CPreservedTargetAudit(
            name=name,
            classification="underdeclared_preserved_target",
            active_route=False,
            target_projection_error=target_projection_error,
            standard_only_risk=standard_only_risk,
            enlarged_record_risk=enlarged_record_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The enlargement is declared, but the preserved comparison target is "
                "missing or was not frozen before analysis."
            ),
            required_next="Predeclare the preserved comparison target and its projection rule.",
        )
    if not case.preserved_target_is_full_standard_record:
        return Q1CPreservedTargetAudit(
            name=name,
            classification="null_coarse_preserved_target",
            active_route=False,
            target_projection_error=target_projection_error,
            standard_only_risk=standard_only_risk,
            enlarged_record_risk=enlarged_record_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The declared preserved target is only a coarsened summary rather than "
                "the full ordinary event-level standard record."
            ),
            required_next="Project back to the full standard record, not a dashboard summary.",
        )
    if target_projection_error > 0:
        return Q1CPreservedTargetAudit(
            name=name,
            classification="null_target_drift_under_enlargement",
            active_route=False,
            target_projection_error=target_projection_error,
            standard_only_risk=standard_only_risk,
            enlarged_record_risk=enlarged_record_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The enlarged instrument does not preserve the declared fixed-standard "
                "target eventwise. Its back-projection drifts away from the ordinary record."
            ),
            required_next="Repair the enlargement so the declared target is exactly preserved.",
        )
    if not has_positive_lift:
        return Q1CPreservedTargetAudit(
            name=name,
            classification="null_honest_but_no_extra_lift",
            active_route=False,
            target_projection_error=target_projection_error,
            standard_only_risk=standard_only_risk,
            enlarged_record_risk=enlarged_record_risk,
            conditional_lift=conditional_lift,
            reason=(
                "The enlargement preserves the declared standard target, but it adds "
                "no positive verdict lift beyond that target."
            ),
            required_next="Show positive predeclared verdict lift beyond the preserved target.",
        )
    return Q1CPreservedTargetAudit(
        name=name,
        classification="candidate_honest_enlarged_instrument_route",
        active_route=True,
        target_projection_error=target_projection_error,
        standard_only_risk=standard_only_risk,
        enlarged_record_risk=enlarged_record_risk,
        conditional_lift=conditional_lift,
        reason=(
            "The enlargement is explicit, the full standard target is predeclared and "
            "preserved eventwise, and the enlarged record adds positive verdict lift "
            "beyond that preserved target."
        ),
        required_next="Bind this honest enlarged-instrument shape to a named monitored-qubit platform.",
    )


def _positive_lift_events() -> tuple[PreservedTargetEvent, ...]:
    return (
        PreservedTargetEvent("r0", "r0+e0", "r0", "v0", Fraction(1, 4)),
        PreservedTargetEvent("r0", "r0+e1", "r0", "v1", Fraction(1, 4)),
        PreservedTargetEvent("r1", "r1+e0", "r1", "v0", Fraction(1, 4)),
        PreservedTargetEvent("r1", "r1+e1", "r1", "v1", Fraction(1, 4)),
    )


def _drift_events() -> tuple[PreservedTargetEvent, ...]:
    return (
        PreservedTargetEvent("r0", "r0+e0", "r0", "v0", Fraction(1, 4)),
        PreservedTargetEvent("r0", "r0+e1", "r1", "v1", Fraction(1, 4)),
        PreservedTargetEvent("r1", "r1+e0", "r1", "v0", Fraction(1, 4)),
        PreservedTargetEvent("r1", "r1+e1", "r0", "v1", Fraction(1, 4)),
    )


def _no_lift_events() -> tuple[PreservedTargetEvent, ...]:
    return (
        PreservedTargetEvent("r0", "r0+e0", "r0", "v0", Fraction(1, 2)),
        PreservedTargetEvent("r1", "r1+e1", "r1", "v1", Fraction(1, 2)),
    )


def canonical_preserved_target_cases() -> tuple[tuple[str, Q1CPreservedTargetInput], ...]:
    return (
        (
            "honest_enlarged_instrument_candidate",
            Q1CPreservedTargetInput(
                enlarged_instrument_declared=True,
                preserved_target_declared=True,
                target_declared_before_analysis=True,
                preserved_target_is_full_standard_record=True,
                events=_positive_lift_events(),
            ),
        ),
        (
            "coarse_preserved_target",
            Q1CPreservedTargetInput(
                enlarged_instrument_declared=True,
                preserved_target_declared=True,
                target_declared_before_analysis=True,
                preserved_target_is_full_standard_record=False,
                events=_positive_lift_events(),
            ),
        ),
        (
            "target_drift_under_enlargement",
            Q1CPreservedTargetInput(
                enlarged_instrument_declared=True,
                preserved_target_declared=True,
                target_declared_before_analysis=True,
                preserved_target_is_full_standard_record=True,
                events=_drift_events(),
            ),
        ),
        (
            "underdeclared_preserved_target",
            Q1CPreservedTargetInput(
                enlarged_instrument_declared=True,
                preserved_target_declared=False,
                target_declared_before_analysis=False,
                preserved_target_is_full_standard_record=True,
                events=_positive_lift_events(),
            ),
        ),
        (
            "honest_but_no_lift",
            Q1CPreservedTargetInput(
                enlarged_instrument_declared=True,
                preserved_target_declared=True,
                target_declared_before_analysis=True,
                preserved_target_is_full_standard_record=True,
                events=_no_lift_events(),
            ),
        ),
    )


def current_frontier_case() -> tuple[str, Q1CPreservedTargetInput]:
    return (
        "current_frontier",
        Q1CPreservedTargetInput(
            enlarged_instrument_declared=True,
            preserved_target_declared=False,
            target_declared_before_analysis=False,
            preserved_target_is_full_standard_record=False,
            events=_positive_lift_events(),
        ),
    )


def run_t158_analysis() -> T158Result:
    audits = tuple(
        classify_preserved_target(case, name=name)
        for name, case in canonical_preserved_target_cases()
    )
    current_name, current_case = current_frontier_case()
    current_audit = classify_preserved_target(current_case, name=current_name)
    audits = audits + (current_audit,)

    null_control_names = {
        "coarse_preserved_target",
        "target_drift_under_enlargement",
        "underdeclared_preserved_target",
        "honest_but_no_lift",
        "current_frontier",
    }
    active_audits = tuple(audit for audit in audits if audit.active_route)
    all_null_controls_rejected = all(
        not audit.active_route for audit in audits if audit.name in null_control_names
    )
    live_cases_honest = all(
        audit.target_projection_error == 0 and audit.conditional_lift > 0
        for audit in active_audits
    )

    return T158Result(
        audits=audits,
        all_null_controls_rejected=all_null_controls_rejected,
        live_cases_honest=live_cases_honest,
        current_frontier_active=current_audit.active_route,
        strongest_claim=(
            "An enlarged-instrument Q1C proposal is live only if it predeclares a "
            "projection back to the full ordinary standard record, preserves that "
            "record eventwise on the admissible domain, and still adds positive "
            "verdict lift beyond the preserved target."
        ),
        improved=(
            "T158 turns the T146/T149/T150 phrase 'preserved comparison target' into "
            "an executable honesty gate. Enlarged-instrument proposals can no longer "
            "count by preserving only a coarse summary or by drifting the target they "
            "claim to hold fixed."
        ),
        weakened=(
            "This further weakens Q1C's enlarged-instrument escape hatch. Merely "
            "changing the hardware and naming a target is null unless the full "
            "ordinary transcript is recovered exactly and the new channel adds "
            "verdict lift beyond it."
        ),
        falsification_condition=(
            "T158 fails if a serious enlarged-instrument Q1C platform can count while "
            "preserving only a coarsened target, allowing target drift under back-"
            "projection, or never exposing an eventwise map back to the ordinary record."
        ),
        q1c_update=(
            "Q1C remains dormant. Reopen the enlarged-instrument branch only when the "
            "platform freezes an eventwise projection from enlarged data back to the "
            "full ordinary standard record and shows positive verdict lift beyond it."
        ),
        claim_ledger_update=(
            "Add T158 to Q1C: enlarged-instrument routes are null when they preserve "
            "only a coarse standard summary, let the declared target drift, or add no "
            "lift beyond the exactly preserved ordinary record."
        ),
        open_blocker=(
            "The repo still has no named monitored-qubit platform that both exposes an "
            "eventwise back-projection to the full ordinary record and clears the T149/"
            "T150 verdict screens."
        ),
        recommended_next=(
            "Treat enlarged-instrument Q1C proposals as admissible only if they specify "
            "the standard-record back-projection explicitly before data review."
        ),
    )


def _fraction_to_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _audit_to_dict(audit: Q1CPreservedTargetAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "active_route": audit.active_route,
        "target_projection_error": _fraction_to_payload(audit.target_projection_error),
        "standard_only_risk": _fraction_to_payload(audit.standard_only_risk),
        "enlarged_record_risk": _fraction_to_payload(audit.enlarged_record_risk),
        "conditional_lift": _fraction_to_payload(audit.conditional_lift),
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t158_result_to_dict(result: T158Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "all_null_controls_rejected": result.all_null_controls_rejected,
        "live_cases_honest": result.live_cases_honest,
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

    print(json.dumps(t158_result_to_dict(run_t158_analysis()), indent=2))
