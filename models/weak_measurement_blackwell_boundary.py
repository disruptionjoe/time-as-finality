"""T155: Blackwell-style boundary for weak-measurement auxiliary channels.

T149 and T150 phrase the Q1C frontier as positive decision-risk lift at fixed
full ordinary record. T155 adds the absorber underneath that gate: if the
auxiliary channel is conditionally screened off by the full ordinary transcript,
then no predeclared finite decision problem about an independently typed hidden
axis can improve by adding that channel.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class HiddenAxisEvent:
    hidden_axis: str
    record: str
    auxiliary: str
    probability: Fraction


@dataclass(frozen=True)
class LossTable:
    name: str
    actions: tuple[str, ...]
    losses: dict[tuple[str, str], Fraction]


@dataclass(frozen=True)
class T155Audit:
    name: str
    screened_off_by_record: bool
    record_only_risks: dict[str, Fraction]
    record_auxiliary_risks: dict[str, Fraction]
    every_loss_equal: bool
    some_loss_improves: bool
    classification: str
    reason: str
    required_next: str


@dataclass(frozen=True)
class T155Result:
    audits: tuple[T155Audit, ...]
    null_controls_hold: bool
    positive_control_improves: bool
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    q1c_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def _total_probability(events: tuple[HiddenAxisEvent, ...]) -> Fraction:
    total = sum((event.probability for event in events), Fraction(0, 1))
    if total <= 0:
        raise ValueError("event probabilities must have positive total mass")
    return total


def _mass_by(
    events: tuple[HiddenAxisEvent, ...],
    *,
    by_record: bool,
    by_auxiliary: bool,
) -> dict[tuple[str, ...], dict[str, Fraction]]:
    grouped: dict[tuple[str, ...], dict[str, Fraction]] = {}
    for event in events:
        key_parts: list[str] = []
        if by_record:
            key_parts.append(event.record)
        if by_auxiliary:
            key_parts.append(event.auxiliary)
        key = tuple(key_parts)
        hidden_mass = grouped.setdefault(key, {})
        hidden_mass[event.hidden_axis] = hidden_mass.get(event.hidden_axis, Fraction(0, 1)) + event.probability
    return grouped


def bayes_risk(
    events: tuple[HiddenAxisEvent, ...],
    *,
    features: tuple[str, ...],
    loss_table: LossTable,
) -> Fraction:
    total = _total_probability(events)
    grouped = _mass_by(
        events,
        by_record="record" in features,
        by_auxiliary="auxiliary" in features,
    )
    total_risk = Fraction(0, 1)
    for hidden_mass in grouped.values():
        best = min(
            sum(
                loss_table.losses[(action, hidden_axis)] * mass
                for hidden_axis, mass in hidden_mass.items()
            )
            for action in loss_table.actions
        )
        total_risk += best
    return total_risk / total


def is_screened_off_by_record(events: tuple[HiddenAxisEvent, ...]) -> bool:
    mass_by_record = _mass_by(events, by_record=True, by_auxiliary=False)
    mass_by_record_aux = _mass_by(events, by_record=True, by_auxiliary=True)
    for feature_key, hidden_mass in mass_by_record_aux.items():
        record_key = (feature_key[0],)
        coarse_mass = mass_by_record[record_key]
        fine_total = sum(hidden_mass.values(), Fraction(0, 1))
        coarse_total = sum(coarse_mass.values(), Fraction(0, 1))
        fine_posterior = {
            hidden_axis: mass / fine_total for hidden_axis, mass in hidden_mass.items()
        }
        coarse_posterior = {
            hidden_axis: mass / coarse_total for hidden_axis, mass in coarse_mass.items()
        }
        if fine_posterior != coarse_posterior:
            return False
    return True


def classify_blackwell_boundary(
    events: tuple[HiddenAxisEvent, ...],
    *,
    name: str,
    loss_tables: tuple[LossTable, ...],
) -> T155Audit:
    screened_off = is_screened_off_by_record(events)
    record_only_risks = {
        loss_table.name: bayes_risk(events, features=("record",), loss_table=loss_table)
        for loss_table in loss_tables
    }
    record_auxiliary_risks = {
        loss_table.name: bayes_risk(
            events,
            features=("record", "auxiliary"),
            loss_table=loss_table,
        )
        for loss_table in loss_tables
    }
    every_loss_equal = all(
        record_only_risks[name] == record_auxiliary_risks[name]
        for name in record_only_risks
    )
    some_loss_improves = any(
        record_auxiliary_risks[name] < record_only_risks[name]
        for name in record_only_risks
    )

    if screened_off and every_loss_equal:
        return T155Audit(
            name=name,
            screened_off_by_record=True,
            record_only_risks=record_only_risks,
            record_auxiliary_risks=record_auxiliary_risks,
            every_loss_equal=True,
            some_loss_improves=False,
            classification="null_blackwell_screened_off",
            reason=(
                "Conditioning on the auxiliary channel does not change the hidden-axis "
                "posterior once the full ordinary record is fixed, so every tested "
                "finite decision problem has the same Bayes risk with or without the "
                "auxiliary channel."
            ),
            required_next="Name extra environment structure or enlarge the instrument.",
        )
    if screened_off and some_loss_improves:
        return T155Audit(
            name=name,
            screened_off_by_record=True,
            record_only_risks=record_only_risks,
            record_auxiliary_risks=record_auxiliary_risks,
            every_loss_equal=False,
            some_loss_improves=True,
            classification="falsified_screened_off_improvement",
            reason=(
                "A screened-off auxiliary channel should not improve any tested loss. "
                "This case would falsify the absorber."
            ),
            required_next="Inspect the posterior calculation or the screening-off claim.",
        )
    if some_loss_improves:
        return T155Audit(
            name=name,
            screened_off_by_record=False,
            record_only_risks=record_only_risks,
            record_auxiliary_risks=record_auxiliary_risks,
            every_loss_equal=False,
            some_loss_improves=True,
            classification="candidate_extra_structure_or_enlargement",
            reason=(
                "The auxiliary channel changes the hidden-axis posterior at fixed "
                "ordinary record and improves at least one predeclared finite decision "
                "problem."
            ),
            required_next=(
                "Show whether the gain comes from extra environment structure or an "
                "explicit instrument enlargement."
            ),
        )
    return T155Audit(
        name=name,
        screened_off_by_record=False,
        record_only_risks=record_only_risks,
        record_auxiliary_risks=record_auxiliary_risks,
        every_loss_equal=False,
        some_loss_improves=False,
        classification="inactive_no_decision_gain",
        reason=(
            "The auxiliary channel changes the posterior class but does not improve any "
            "tested finite decision problem."
        ),
        required_next="State a different predeclared target or leave the route dormant.",
    )


def canonical_loss_tables() -> tuple[LossTable, ...]:
    return (
        LossTable(
            name="zero_one",
            actions=("predict_h0", "predict_h1"),
            losses={
                ("predict_h0", "h0"): Fraction(0, 1),
                ("predict_h0", "h1"): Fraction(1, 1),
                ("predict_h1", "h0"): Fraction(1, 1),
                ("predict_h1", "h1"): Fraction(0, 1),
            },
        ),
        LossTable(
            name="asymmetric_h1_cost",
            actions=("predict_h0", "predict_h1"),
            losses={
                ("predict_h0", "h0"): Fraction(0, 1),
                ("predict_h0", "h1"): Fraction(3, 2),
                ("predict_h1", "h0"): Fraction(1, 2),
                ("predict_h1", "h1"): Fraction(0, 1),
            },
        ),
    )


def canonical_cases() -> tuple[tuple[str, tuple[HiddenAxisEvent, ...]], ...]:
    return (
        (
            "garbled_same_instrument_meter",
            (
                HiddenAxisEvent("h0", "r0", "a0", Fraction(1, 4)),
                HiddenAxisEvent("h1", "r0", "a0", Fraction(1, 4)),
                HiddenAxisEvent("h0", "r1", "a1", Fraction(1, 4)),
                HiddenAxisEvent("h1", "r1", "a1", Fraction(1, 4)),
            ),
        ),
        (
            "independent_noise_meter",
            (
                HiddenAxisEvent("h0", "r0", "a0", Fraction(1, 8)),
                HiddenAxisEvent("h0", "r0", "a1", Fraction(1, 8)),
                HiddenAxisEvent("h1", "r0", "a0", Fraction(1, 8)),
                HiddenAxisEvent("h1", "r0", "a1", Fraction(1, 8)),
                HiddenAxisEvent("h0", "r1", "a0", Fraction(1, 8)),
                HiddenAxisEvent("h0", "r1", "a1", Fraction(1, 8)),
                HiddenAxisEvent("h1", "r1", "a0", Fraction(1, 8)),
                HiddenAxisEvent("h1", "r1", "a1", Fraction(1, 8)),
            ),
        ),
        (
            "record_already_sufficient",
            (
                HiddenAxisEvent("h0", "r0", "a0", Fraction(1, 2)),
                HiddenAxisEvent("h1", "r1", "a1", Fraction(1, 2)),
            ),
        ),
        (
            "extra_environment_candidate",
            (
                HiddenAxisEvent("h0", "r0", "a0", Fraction(1, 4)),
                HiddenAxisEvent("h1", "r0", "a1", Fraction(1, 4)),
                HiddenAxisEvent("h0", "r1", "a0", Fraction(1, 4)),
                HiddenAxisEvent("h1", "r1", "a1", Fraction(1, 4)),
            ),
        ),
    )


def run_t155_analysis() -> T155Result:
    loss_tables = canonical_loss_tables()
    audits = tuple(
        classify_blackwell_boundary(events, name=name, loss_tables=loss_tables)
        for name, events in canonical_cases()
    )
    audit_by_name = {audit.name: audit for audit in audits}
    null_controls_hold = all(
        audit_by_name[name].classification == "null_blackwell_screened_off"
        for name in (
            "garbled_same_instrument_meter",
            "independent_noise_meter",
            "record_already_sufficient",
        )
    )
    positive_control_improves = (
        audit_by_name["extra_environment_candidate"].classification
        == "candidate_extra_structure_or_enlargement"
    )

    return T155Result(
        audits=audits,
        null_controls_hold=null_controls_hold,
        positive_control_improves=positive_control_improves,
        strongest_claim=(
            "T155 adds the absorber underneath T149: if an auxiliary channel is "
            "screened off by the full ordinary monitored transcript, then adding that "
            "channel cannot improve any predeclared finite decision problem about an "
            "independently typed hidden axis."
        ),
        improved=(
            "This makes the Q1C null class more general and easier to evaluate. "
            "A same-instrument auxiliary channel is not merely zero-lift for one "
            "chosen verdict map; if it is screened off by the full transcript, it is "
            "decision-theoretically redundant across the tested loss family."
        ),
        weakened=(
            "This weakens weak-measurement rescue language again. A second channel "
            "that is only a garbling, refinement, or noise decoration of the ordinary "
            "transcript does not just fail one toy criterion; it fails the whole "
            "predeclared finite decision family tested here."
        ),
        falsification_condition=(
            "T155 fails if a genuinely screened-off auxiliary channel improves a "
            "predeclared finite decision problem at fixed full ordinary record, or "
            "if the extra-environment positive control does not improve any tested "
            "loss despite changing the hidden-axis posterior."
        ),
        q1c_update=(
            "Q1C remains dormant. Any future same-instrument auxiliary proposal must "
            "first show that its event-level content is not screened off by the full "
            "ordinary transcript; otherwise no predeclared verdict lift can count."
        ),
        claim_ledger_update=(
            "Add T155 to Q1C: once the full ordinary transcript screens off the "
            "auxiliary channel, that channel is null across the tested finite "
            "decision family, not just for one chosen verdict map."
        ),
        open_blocker=(
            "The repo still lacks a named monitored-qubit platform where the "
            "auxiliary channel provably changes the hidden-axis posterior at fixed "
            "full ordinary record and can be typed as extra environment structure or "
            "honest instrument enlargement."
        ),
        recommended_next=(
            "Do not search for more same-instrument meters. Search only for a platform "
            "that can exhibit non-screened-off event-level content before any verdict "
            "or loss rule is optimized."
        ),
    )


def _fraction_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": f"{value.numerator}/{value.denominator}", "float": float(value)}


def _audit_payload(audit: T155Audit) -> dict[str, object]:
    return {
        "name": audit.name,
        "screened_off_by_record": audit.screened_off_by_record,
        "record_only_risks": {
            loss_name: _fraction_payload(risk)
            for loss_name, risk in audit.record_only_risks.items()
        },
        "record_auxiliary_risks": {
            loss_name: _fraction_payload(risk)
            for loss_name, risk in audit.record_auxiliary_risks.items()
        },
        "every_loss_equal": audit.every_loss_equal,
        "some_loss_improves": audit.some_loss_improves,
        "classification": audit.classification,
        "reason": audit.reason,
        "required_next": audit.required_next,
    }


def t155_result_to_dict(result: T155Result) -> dict[str, object]:
    return {
        "audits": [_audit_payload(audit) for audit in result.audits],
        "null_controls_hold": result.null_controls_hold,
        "positive_control_improves": result.positive_control_improves,
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

    print(json.dumps(t155_result_to_dict(run_t155_analysis()), indent=2))
