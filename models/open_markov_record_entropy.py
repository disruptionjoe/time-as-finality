"""T116: open Markov record-entropy comparison for H7.

T110 blocked strict scalar finality monotones in finite closed reversible
systems. T116 tests the next loophole: perhaps an explicitly open stochastic
record process can supply an H7 arrow that is not merely standard entropy,
history export, or fresh-capacity accounting.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose, log


TOLERANCE = 1e-12


@dataclass(frozen=True)
class RecordState:
    local_records: int
    exported_records: int = 0
    fresh_capacity_remaining: int = 0

    @property
    def accounted_records(self) -> int:
        return self.local_records + self.exported_records


@dataclass(frozen=True)
class MarkovStep:
    before: RecordState
    after: RecordState
    forward_probability: float
    reverse_probability: float
    label: str

    @property
    def path_irreversibility_nats(self) -> float:
        return log(self.forward_probability / self.reverse_probability)

    @property
    def exported_delta(self) -> int:
        return self.after.exported_records - self.before.exported_records

    @property
    def fresh_capacity_delta(self) -> int:
        return (
            self.before.fresh_capacity_remaining
            - self.after.fresh_capacity_remaining
        )


@dataclass(frozen=True)
class ScenarioAudit:
    name: str
    steps: tuple[MarkovStep, ...]
    local_score_sequence: tuple[int, ...]
    accounted_score_sequence: tuple[int, ...]
    fresh_capacity_sequence: tuple[int, ...]
    step_irreversibility_nats: tuple[float, ...]
    total_irreversibility_nats: float
    exported_records_added: int
    fresh_capacity_consumed: int
    local_nondecreasing: bool
    accounted_nondecreasing: bool
    accounted_strict_increase_edges: int
    candidate_independent_h7_arrow: bool
    classification: str
    verdict: str


@dataclass(frozen=True)
class T116Result:
    detailed_balance_control: ScenarioAudit
    nonequilibrium_cycle_control: ScenarioAudit
    open_export_recorder: ScenarioAudit
    reversible_append_only_control: ScenarioAudit
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def audit_scenario(name: str, steps: tuple[MarkovStep, ...]) -> ScenarioAudit:
    if not steps:
        raise ValueError("scenario requires at least one step")
    _validate_path(steps)

    states = (steps[0].before,) + tuple(step.after for step in steps)
    local_scores = tuple(state.local_records for state in states)
    accounted_scores = tuple(state.accounted_records for state in states)
    fresh_capacity = tuple(state.fresh_capacity_remaining for state in states)
    entropy_terms = tuple(step.path_irreversibility_nats for step in steps)
    total_irreversibility = sum(entropy_terms)
    exported_added = sum(max(0, step.exported_delta) for step in steps)
    fresh_consumed = sum(max(0, step.fresh_capacity_delta) for step in steps)
    local_nondecreasing = _nondecreasing(local_scores)
    accounted_nondecreasing = _nondecreasing(accounted_scores)
    strict_edges = _strict_increase_edges(accounted_scores)
    candidate_independent = (
        accounted_nondecreasing
        and strict_edges > 0
        and isclose(total_irreversibility, 0.0, abs_tol=TOLERANCE)
        and exported_added == 0
        and fresh_consumed == 0
    )
    classification = _classify_scenario(
        accounted_nondecreasing=accounted_nondecreasing,
        strict_edges=strict_edges,
        total_irreversibility=total_irreversibility,
        exported_added=exported_added,
        fresh_consumed=fresh_consumed,
    )
    return ScenarioAudit(
        name=name,
        steps=steps,
        local_score_sequence=local_scores,
        accounted_score_sequence=accounted_scores,
        fresh_capacity_sequence=fresh_capacity,
        step_irreversibility_nats=entropy_terms,
        total_irreversibility_nats=total_irreversibility,
        exported_records_added=exported_added,
        fresh_capacity_consumed=fresh_consumed,
        local_nondecreasing=local_nondecreasing,
        accounted_nondecreasing=accounted_nondecreasing,
        accounted_strict_increase_edges=strict_edges,
        candidate_independent_h7_arrow=candidate_independent,
        classification=classification,
        verdict=_verdict_for(classification),
    )


def detailed_balance_shuffle_control() -> ScenarioAudit:
    states = (
        RecordState(0),
        RecordState(1),
        RecordState(0),
        RecordState(1),
        RecordState(0),
    )
    return audit_scenario(
        "detailed_balance_shuffle_control",
        _steps_from_states(
            states,
            forward_probability=0.5,
            reverse_probability=0.5,
            label="symmetric reversible record shuffle",
        ),
    )


def nonequilibrium_cycle_control() -> ScenarioAudit:
    states = (
        RecordState(0),
        RecordState(1),
        RecordState(2),
        RecordState(0),
    )
    return audit_scenario(
        "nonequilibrium_cycle_control",
        _steps_from_states(
            states,
            forward_probability=0.8,
            reverse_probability=0.2,
            label="biased local cycle with positive path irreversibility",
        ),
    )


def open_export_recorder() -> ScenarioAudit:
    states = (
        RecordState(0, exported_records=0),
        RecordState(1, exported_records=0),
        RecordState(2, exported_records=0),
        RecordState(0, exported_records=2),
        RecordState(1, exported_records=2),
        RecordState(2, exported_records=2),
        RecordState(0, exported_records=4),
    )
    return audit_scenario(
        "open_export_recorder",
        _steps_from_states(
            states,
            forward_probability=0.9,
            reverse_probability=0.1,
            label="record locally, export history, clear local slot",
        ),
    )


def reversible_append_only_control() -> ScenarioAudit:
    states = (
        RecordState(0, fresh_capacity_remaining=3),
        RecordState(1, fresh_capacity_remaining=2),
        RecordState(2, fresh_capacity_remaining=1),
        RecordState(3, fresh_capacity_remaining=0),
    )
    return audit_scenario(
        "reversible_append_only_control",
        _steps_from_states(
            states,
            forward_probability=0.5,
            reverse_probability=0.5,
            label="logically reversible append on blank capacity",
        ),
    )


def run_t116_analysis() -> T116Result:
    detailed_balance = detailed_balance_shuffle_control()
    cycle = nonequilibrium_cycle_control()
    export = open_export_recorder()
    append_only = reversible_append_only_control()
    return T116Result(
        detailed_balance_control=detailed_balance,
        nonequilibrium_cycle_control=cycle,
        open_export_recorder=export,
        reversible_append_only_control=append_only,
        strongest_claim=(
            "In the tested finite open Markov record fixtures, strict "
            "accounted finality appears only with standard path "
            "irreversibility plus history export, or with fresh blank "
            "capacity. Detailed-balance controls do not yield a strict record "
            "arrow, and a biased entropy-producing local cycle is not by "
            "itself a scalar finality monotone."
        ),
        improved=(
            "T116 answers T110's open-system next step by comparing H7 record "
            "arrows directly with stochastic path irreversibility, exported "
            "history, and append-only blank capacity in one finite audit."
        ),
        weakened=(
            "H7 is weakened as an independent thermodynamic-arrow proposal. "
            "The open recorder's monotone accounted finality is fully "
            "explained by the declared export channel and positive path "
            "log-ratio; the zero-log-ratio monotone uses fresh capacity."
        ),
        falsification_condition=(
            "T116 is falsified by a finite stochastic record model with a "
            "strict accounted-D1 monotone, zero path irreversibility, no "
            "distributional free-energy drawdown, no exported history, no "
            "fresh capacity consumption, no postselection, and reverse "
            "dynamics included rather than excluded."
        ),
        h7_update=(
            "Add T116 to H7: the explicit open Markov witness gives no "
            "independent open Markov arrow separating finality direction from "
            "entropy/export/fresh-capacity accounting. H7 remains a "
            "constructor/resource-accounting claim unless a zero-resource "
            "stochastic record arrow is produced."
        ),
        claim_ledger_update=(
            "H7 remains partially supported only as a conditional "
            "constructor or open-system resource-accounting claim. T116 finds "
            "no independent open Markov arrow: detailed-balance record "
            "shuffle has no strict finality direction, biased cyclic current "
            "is entropy-producing but not scalar-finality monotone, exported "
            "history gives monotone accounted records only with positive "
            "path irreversibility, and append-only monotonicity consumes "
            "fresh blank capacity."
        ),
        open_blocker=(
            "The repo still lacks a physically grounded H7 model whose record "
            "arrow is not absorbed by standard stochastic thermodynamics, "
            "history export, free-energy drawdown, or capacity accounting."
        ),
        recommended_next=(
            "Demote H7 in paper-facing prose to a constructor/resource "
            "accounting lemma, or search for a zero-resource stochastic "
            "record-arrow counterexample that clears the T116 gate."
        ),
    )


def t116_result_to_dict(result: T116Result) -> dict[str, object]:
    return {
        "detailed_balance_control": _scenario_to_dict(
            result.detailed_balance_control
        ),
        "nonequilibrium_cycle_control": _scenario_to_dict(
            result.nonequilibrium_cycle_control
        ),
        "open_export_recorder": _scenario_to_dict(result.open_export_recorder),
        "reversible_append_only_control": _scenario_to_dict(
            result.reversible_append_only_control
        ),
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _steps_from_states(
    states: tuple[RecordState, ...],
    *,
    forward_probability: float,
    reverse_probability: float,
    label: str,
) -> tuple[MarkovStep, ...]:
    if len(states) < 2:
        raise ValueError("state path requires at least two states")
    return tuple(
        MarkovStep(
            before=states[index],
            after=states[index + 1],
            forward_probability=forward_probability,
            reverse_probability=reverse_probability,
            label=label,
        )
        for index in range(len(states) - 1)
    )


def _validate_path(steps: tuple[MarkovStep, ...]) -> None:
    for step in steps:
        if not (0.0 < step.forward_probability <= 1.0):
            raise ValueError("forward probabilities must be in (0, 1]")
        if not (0.0 < step.reverse_probability <= 1.0):
            raise ValueError("reverse probabilities must be in (0, 1]")
    for previous, current in zip(steps, steps[1:]):
        if previous.after != current.before:
            raise ValueError("steps must form a contiguous path")


def _nondecreasing(values: tuple[int, ...]) -> bool:
    return all(after >= before for before, after in zip(values, values[1:]))


def _strict_increase_edges(values: tuple[int, ...]) -> int:
    return sum(1 for before, after in zip(values, values[1:]) if after > before)


def _classify_scenario(
    *,
    accounted_nondecreasing: bool,
    strict_edges: int,
    total_irreversibility: float,
    exported_added: int,
    fresh_consumed: int,
) -> str:
    if not accounted_nondecreasing or strict_edges == 0:
        return "no_strict_h7_arrow"
    if total_irreversibility > TOLERANCE and exported_added > 0:
        return "absorbed_by_entropy_export"
    if total_irreversibility > TOLERANCE:
        return "absorbed_by_path_irreversibility"
    if fresh_consumed > 0:
        return "absorbed_by_fresh_capacity"
    return "candidate_independent_h7_arrow"


def _verdict_for(classification: str) -> str:
    verdicts = {
        "no_strict_h7_arrow": (
            "No strict accounted finality arrow is present in this control."
        ),
        "absorbed_by_entropy_export": (
            "The strict accounted arrow is explained by the open export "
            "channel and positive path irreversibility."
        ),
        "absorbed_by_path_irreversibility": (
            "The strict accounted arrow tracks stochastic path "
            "irreversibility, not an independent H7 mechanism."
        ),
        "absorbed_by_fresh_capacity": (
            "The strict accounted arrow is paid for by consuming fresh blank "
            "record capacity."
        ),
        "candidate_independent_h7_arrow": (
            "This scenario would be a candidate independent H7 arrow."
        ),
    }
    return verdicts[classification]


def _scenario_to_dict(audit: ScenarioAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "states": [
            {
                "local_records": state.local_records,
                "exported_records": state.exported_records,
                "fresh_capacity_remaining": state.fresh_capacity_remaining,
                "accounted_records": state.accounted_records,
            }
            for state in (audit.steps[0].before,) + tuple(
                step.after for step in audit.steps
            )
        ],
        "steps": [
            {
                "before": {
                    "local_records": step.before.local_records,
                    "exported_records": step.before.exported_records,
                    "fresh_capacity_remaining": step.before.fresh_capacity_remaining,
                    "accounted_records": step.before.accounted_records,
                },
                "after": {
                    "local_records": step.after.local_records,
                    "exported_records": step.after.exported_records,
                    "fresh_capacity_remaining": step.after.fresh_capacity_remaining,
                    "accounted_records": step.after.accounted_records,
                },
                "forward_probability": step.forward_probability,
                "reverse_probability": step.reverse_probability,
                "path_irreversibility_nats": step.path_irreversibility_nats,
                "exported_delta": step.exported_delta,
                "fresh_capacity_delta": step.fresh_capacity_delta,
                "label": step.label,
            }
            for step in audit.steps
        ],
        "local_score_sequence": list(audit.local_score_sequence),
        "accounted_score_sequence": list(audit.accounted_score_sequence),
        "fresh_capacity_sequence": list(audit.fresh_capacity_sequence),
        "step_irreversibility_nats": list(audit.step_irreversibility_nats),
        "total_irreversibility_nats": audit.total_irreversibility_nats,
        "exported_records_added": audit.exported_records_added,
        "fresh_capacity_consumed": audit.fresh_capacity_consumed,
        "local_nondecreasing": audit.local_nondecreasing,
        "accounted_nondecreasing": audit.accounted_nondecreasing,
        "accounted_strict_increase_edges": audit.accounted_strict_increase_edges,
        "candidate_independent_h7_arrow": audit.candidate_independent_h7_arrow,
        "classification": audit.classification,
        "verdict": audit.verdict,
    }
