"""T150: verdict-admissibility gate for weak-measurement Q1C proposals.

T149 made "survives full-record conditioning" operational through positive
decision-risk lift at fixed full ordinary record. That still leaves an obvious
loophole: a proposal can manufacture lift by choosing a verdict target that is
just an auxiliary-meter label or a vanishingly rare event. T150 closes that
gap. A live Q1C verdict must be typed independently of the auxiliary channel
and must have nontrivial support before the auxiliary data are consulted.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from models.weak_measurement_conditional_sufficiency_gate import (
    MeasurementEvent,
    Q1CConditionalInput,
    classify_conditional_sufficiency,
)


@dataclass(frozen=True)
class VerdictEvent:
    hidden_axis: str
    record: str
    auxiliary: str
    verdict: str
    probability: Fraction


@dataclass(frozen=True)
class Q1CVerdictInput:
    full_event_standard_record_fixed: bool
    auxiliary_is_proxy_or_postselected: bool
    same_declared_instrument: bool
    captures_extra_environment_structure: bool
    explicitly_enlarges_instrument: bool
    preserved_comparison_target_declared: bool
    verdict_declared_before_analysis: bool
    hidden_axis_declared: bool
    hidden_axis_name: str
    minimum_class_support: Fraction
    events: tuple[VerdictEvent, ...]


@dataclass(frozen=True)
class Q1CVerdictAudit:
    name: str
    classification: str
    active_route: bool
    record_only_risk: Fraction
    record_auxiliary_risk: Fraction
    conditional_lift: Fraction
    smallest_verdict_support: Fraction
    reason: str
    required_next: str


@dataclass(frozen=True)
class T150Result:
    audits: tuple[Q1CVerdictAudit, ...]
    all_null_controls_rejected: bool
    live_cases_clear_target_gate: bool
    current_frontier_active: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _conditional_case(case: Q1CVerdictInput) -> Q1CConditionalInput:
    return Q1CConditionalInput(
        full_event_standard_record_fixed=case.full_event_standard_record_fixed,
        auxiliary_is_proxy_or_postselected=case.auxiliary_is_proxy_or_postselected,
        same_declared_instrument=case.same_declared_instrument,
        captures_extra_environment_structure=case.captures_extra_environment_structure,
        explicitly_enlarges_instrument=case.explicitly_enlarges_instrument,
        preserved_comparison_target_declared=case.preserved_comparison_target_declared,
        events=tuple(
            MeasurementEvent(
                record=event.record,
                auxiliary=event.auxiliary,
                verdict=event.verdict,
                probability=event.probability,
            )
            for event in case.events
        ),
    )


def _verdict_support(events: tuple[VerdictEvent, ...]) -> dict[str, Fraction]:
    total = sum((event.probability for event in events), Fraction(0, 1))
    if total <= 0:
        raise ValueError("event probabilities must have positive total mass")
    support: dict[str, Fraction] = {}
    for event in events:
        support[event.verdict] = support.get(event.verdict, Fraction(0, 1)) + event.probability
    return {verdict: mass / total for verdict, mass in support.items()}


def _hidden_axis_determines_verdict(events: tuple[VerdictEvent, ...]) -> bool:
    by_axis: dict[str, set[str]] = {}
    for event in events:
        by_axis.setdefault(event.hidden_axis, set()).add(event.verdict)
    return all(len(verdicts) == 1 for verdicts in by_axis.values())


def classify_verdict_admissibility(
    case: Q1CVerdictInput,
    *,
    name: str,
) -> Q1CVerdictAudit:
    conditional_audit = classify_conditional_sufficiency(_conditional_case(case), name=name)
    support = _verdict_support(case.events)
    smallest_support = min(support.values())

    if not conditional_audit.active_route:
        return Q1CVerdictAudit(
            name=name,
            classification="null_t149_architecture_not_cleared",
            active_route=False,
            record_only_risk=conditional_audit.record_only_risk,
            record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
            conditional_lift=conditional_audit.conditional_lift,
            smallest_verdict_support=smallest_support,
            reason=(
                "The proposal does not clear the T149 architecture gate, so verdict "
                "typing cannot rescue it."
            ),
            required_next=conditional_audit.required_next,
        )
    if not case.verdict_declared_before_analysis:
        return Q1CVerdictAudit(
            name=name,
            classification="null_posthoc_verdict_target",
            active_route=False,
            record_only_risk=conditional_audit.record_only_risk,
            record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
            conditional_lift=conditional_audit.conditional_lift,
            smallest_verdict_support=smallest_support,
            reason=(
                "The verdict target is chosen after analysis, so the positive lift "
                "is not a pre-registered Q1C result."
            ),
            required_next="Predeclare the verdict class before auxiliary data are scored.",
        )
    if not case.hidden_axis_declared:
        return Q1CVerdictAudit(
            name=name,
            classification="underdeclared_hidden_axis",
            active_route=False,
            record_only_risk=conditional_audit.record_only_risk,
            record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
            conditional_lift=conditional_audit.conditional_lift,
            smallest_verdict_support=smallest_support,
            reason=(
                "The verdict class has lift, but the underlying TaF-relevant axis is "
                "not declared independently of the auxiliary meter."
            ),
            required_next="Name the hidden TaF axis the verdict is supposed to track.",
        )
    if smallest_support < case.minimum_class_support:
        return Q1CVerdictAudit(
            name=name,
            classification="null_rare_verdict_gerrymander",
            active_route=False,
            record_only_risk=conditional_audit.record_only_risk,
            record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
            conditional_lift=conditional_audit.conditional_lift,
            smallest_verdict_support=smallest_support,
            reason=(
                "The positive lift comes from a verdict class with too little support "
                "to count as an honest predeclared Q1C target."
            ),
            required_next="Use a verdict partition whose smallest class clears the support floor.",
        )
    if not _hidden_axis_determines_verdict(case.events):
        return Q1CVerdictAudit(
            name=name,
            classification="null_auxiliary_defined_verdict",
            active_route=False,
            record_only_risk=conditional_audit.record_only_risk,
            record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
            conditional_lift=conditional_audit.conditional_lift,
            smallest_verdict_support=smallest_support,
            reason=(
                "The declared hidden axis does not determine the verdict. The verdict "
                "is being defined by the auxiliary output rather than inferred from an "
                "independently typed TaF target."
            ),
            required_next="Define the verdict as a fixed map from the declared TaF axis.",
        )
    return Q1CVerdictAudit(
        name=name,
        classification="candidate_typed_verdict_route",
        active_route=True,
        record_only_risk=conditional_audit.record_only_risk,
        record_auxiliary_risk=conditional_audit.record_auxiliary_risk,
        conditional_lift=conditional_audit.conditional_lift,
        smallest_verdict_support=smallest_support,
        reason=(
            "The proposal clears T149, names a hidden TaF axis independently of the "
            "auxiliary channel, and keeps every verdict class above the support floor."
        ),
        required_next="Bind the typed verdict target to a named monitored-qubit platform.",
    )


def _balanced_typed_events() -> tuple[VerdictEvent, ...]:
    return (
        VerdictEvent("h0", "r0", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h1", "r0", "a1", "v1", Fraction(1, 4)),
        VerdictEvent("h0", "r1", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h1", "r1", "a1", "v1", Fraction(1, 4)),
    )


def _rare_typed_events() -> tuple[VerdictEvent, ...]:
    return (
        VerdictEvent("h0", "r0", "a0", "v0", Fraction(9, 10)),
        VerdictEvent("h1", "r0", "a1", "v1", Fraction(1, 10)),
    )


def _auxiliary_echo_events() -> tuple[VerdictEvent, ...]:
    return (
        VerdictEvent("h0", "r0", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h0", "r0", "a1", "v1", Fraction(1, 4)),
        VerdictEvent("h1", "r1", "a0", "v0", Fraction(1, 4)),
        VerdictEvent("h1", "r1", "a1", "v1", Fraction(1, 4)),
    )


def canonical_verdict_cases() -> tuple[tuple[str, Q1CVerdictInput], ...]:
    return (
        (
            "typed_extra_environment_candidate",
            Q1CVerdictInput(
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
                events=_balanced_typed_events(),
            ),
        ),
        (
            "typed_enlarged_instrument_candidate",
            Q1CVerdictInput(
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
                events=_balanced_typed_events(),
            ),
        ),
        (
            "auxiliary_echo_gerrymander",
            Q1CVerdictInput(
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
                events=_auxiliary_echo_events(),
            ),
        ),
        (
            "rare_target_gerrymander",
            Q1CVerdictInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_declared_before_analysis=True,
                hidden_axis_declared=True,
                hidden_axis_name="rare_branch_label",
                minimum_class_support=Fraction(1, 5),
                events=_rare_typed_events(),
            ),
        ),
        (
            "posthoc_target_choice",
            Q1CVerdictInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=False,
                captures_extra_environment_structure=True,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_declared_before_analysis=False,
                hidden_axis_declared=True,
                hidden_axis_name="branch_support_state",
                minimum_class_support=Fraction(1, 5),
                events=_balanced_typed_events(),
            ),
        ),
        (
            "same_instrument_positive_lift",
            Q1CVerdictInput(
                full_event_standard_record_fixed=True,
                auxiliary_is_proxy_or_postselected=False,
                same_declared_instrument=True,
                captures_extra_environment_structure=False,
                explicitly_enlarges_instrument=False,
                preserved_comparison_target_declared=False,
                verdict_declared_before_analysis=True,
                hidden_axis_declared=True,
                hidden_axis_name="branch_support_state",
                minimum_class_support=Fraction(1, 5),
                events=_balanced_typed_events(),
            ),
        ),
    )


def current_frontier_case() -> tuple[str, Q1CVerdictInput]:
    return (
        "current_frontier",
        Q1CVerdictInput(
            full_event_standard_record_fixed=True,
            auxiliary_is_proxy_or_postselected=False,
            same_declared_instrument=True,
            captures_extra_environment_structure=False,
            explicitly_enlarges_instrument=False,
            preserved_comparison_target_declared=False,
            verdict_declared_before_analysis=False,
            hidden_axis_declared=False,
            hidden_axis_name="",
            minimum_class_support=Fraction(1, 5),
            events=_balanced_typed_events(),
        ),
    )


def run_t150_analysis() -> T150Result:
    audits = tuple(
        classify_verdict_admissibility(case, name=name)
        for name, case in canonical_verdict_cases()
    )
    current_name, current_case = current_frontier_case()
    current_audit = classify_verdict_admissibility(current_case, name=current_name)
    audits = audits + (current_audit,)

    active_audits = tuple(audit for audit in audits if audit.active_route)
    null_control_names = {
        "auxiliary_echo_gerrymander",
        "rare_target_gerrymander",
        "posthoc_target_choice",
        "same_instrument_positive_lift",
        "current_frontier",
    }
    all_null_controls_rejected = all(
        not audit.active_route for audit in audits if audit.name in null_control_names
    )
    live_cases_clear_target_gate = all(
        audit.classification == "candidate_typed_verdict_route" for audit in active_audits
    )

    return T150Result(
        audits=audits,
        all_null_controls_rejected=all_null_controls_rejected,
        live_cases_clear_target_gate=live_cases_clear_target_gate,
        current_frontier_active=current_audit.active_route,
        strongest_claim=(
            "Positive conditional lift is still not enough for Q1C. The verdict "
            "must be a predeclared map from an independently typed TaF axis, not "
            "an auxiliary-defined label or a vanishingly rare event class."
        ),
        improved=(
            "T150 closes the verdict-gerrymandering loophole left by T149. Future "
            "Q1C proposals must declare the target axis, verdict map, and support "
            "floor before auxiliary data are allowed to matter."
        ),
        weakened=(
            "This weakens Q1C again: auxiliary-echo labels, post hoc target choice, "
            "and rare-event verdict partitions no longer count as positive weak-"
            "measurement evidence even if they show decision lift."
        ),
        falsification_condition=(
            "T150 fails if a serious Q1C platform needs neither an independently "
            "typed TaF axis nor a non-gerrymandered verdict partition to produce "
            "its positive lift, or if an auxiliary-defined verdict is still judged "
            "an honest Q1C target."
        ),
        q1c_update=(
            "Q1C remains dormant. Reopen it only with a named monitored-qubit "
            "platform that clears T149 and uses a predeclared verdict class "
            "induced from an independently typed TaF axis with nontrivial support."
        ),
        claim_ledger_update=(
            "Add T150 to Q1C: positive lift must target a predeclared TaF verdict "
            "map rather than an auxiliary-defined or rare-event label. Verdict "
            "gerrymanders are null."
        ),
        open_blocker=(
            "The repo still has no named monitored-qubit platform that supplies a "
            "T149-cleared architecture together with an independently typed TaF "
            "target axis and non-gerrymandered verdict partition."
        ),
        recommended_next=(
            "Only consider future Q1C proposals that specify a concrete physical "
            "axis H and a fixed verdict map V=g(H) before scoring auxiliary data."
        ),
    )


def _fraction_to_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _audit_to_dict(audit: Q1CVerdictAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "classification": audit.classification,
        "active_route": audit.active_route,
        "record_only_risk": _fraction_to_payload(audit.record_only_risk),
        "record_auxiliary_risk": _fraction_to_payload(audit.record_auxiliary_risk),
        "conditional_lift": _fraction_to_payload(audit.conditional_lift),
        "smallest_verdict_support": _fraction_to_payload(audit.smallest_verdict_support),
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t150_result_to_dict(result: T150Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "all_null_controls_rejected": result.all_null_controls_rejected,
        "live_cases_clear_target_gate": result.live_cases_clear_target_gate,
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

    print(json.dumps(t150_result_to_dict(run_t150_analysis()), indent=2))
