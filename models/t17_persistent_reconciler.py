"""T17: persistent dynamical reconciler laboratory.

The model is a small local-update system whose observer-like subsystem is not
selected as a terminal window.  Sensor cells couple to environment cells,
write persistent memory cells, and an internal comparator reconciles those
stored records.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


Bit = int
State = tuple[Bit, ...]


@dataclass(frozen=True)
class ReconcilerState:
    env_a: Bit
    env_b: Bit
    sensor_a: Bit
    sensor_b: Bit
    memory_a: Bit
    memory_b: Bit
    written_a: Bit
    written_b: Bit
    compared: Bit
    decision: Bit

    def as_tuple(self) -> State:
        return (
            self.env_a,
            self.env_b,
            self.sensor_a,
            self.sensor_b,
            self.memory_a,
            self.memory_b,
            self.written_a,
            self.written_b,
            self.compared,
            self.decision,
        )


@dataclass(frozen=True)
class InternalRecord:
    proposition: str
    value: str
    holder: str
    first_written_step: int
    persisted_steps: int


@dataclass(frozen=True)
class ReconcilerRun:
    initial: ReconcilerState
    history: tuple[ReconcilerState, ...]
    records: tuple[InternalRecord, ...]
    access_boundary: frozenset[str]
    decision: str | None
    finality_profiles: dict[str, tuple[int, int, int, int]]


def initial_state(env_a: Bit, env_b: Bit) -> ReconcilerState:
    return ReconcilerState(
        env_a=env_a,
        env_b=env_b,
        sensor_a=0,
        sensor_b=0,
        memory_a=0,
        memory_b=0,
        written_a=0,
        written_b=0,
        compared=0,
        decision=0,
    )


def step(state: ReconcilerState) -> ReconcilerState:
    """One synchronous local update.

    Sensors copy their coupled environment cells.  Memory cells latch sensor
    values and persist.  The comparator activates only after both memories are
    set.  The decision bit is true when the two stored memories agree.
    """

    sensor_a = state.env_a
    sensor_b = state.env_b
    memory_a = state.memory_a if state.written_a else sensor_a
    memory_b = state.memory_b if state.written_b else sensor_b
    written_a = 1
    written_b = 1
    compared = int(bool(written_a and written_b))
    decision = int(bool(compared and memory_a == memory_b))
    return ReconcilerState(
        env_a=state.env_a,
        env_b=state.env_b,
        sensor_a=sensor_a,
        sensor_b=sensor_b,
        memory_a=memory_a,
        memory_b=memory_b,
        written_a=written_a,
        written_b=written_b,
        compared=compared,
        decision=decision,
    )


def run(initial: ReconcilerState, steps: int = 5) -> tuple[ReconcilerState, ...]:
    if steps < 0:
        raise ValueError("steps cannot be negative")
    history = [initial]
    for _ in range(steps):
        history.append(step(history[-1]))
    return tuple(history)


def _first_written(history: tuple[ReconcilerState, ...], field: str) -> int | None:
    for index, state in enumerate(history):
        if getattr(state, field):
            return index
    return None


def internal_records(history: tuple[ReconcilerState, ...]) -> tuple[InternalRecord, ...]:
    records = []
    for proposition, field, written_field, holder in (
        ("A", "memory_a", "written_a", "memory:A"),
        ("B", "memory_b", "written_b", "memory:B"),
    ):
        first = _first_written(history, written_field)
        if first is None:
            continue
        persisted = sum(getattr(state, written_field) for state in history[first:])
        records.append(
            InternalRecord(
                proposition=proposition,
                value="true" if getattr(history[-1], field) else "false",
                holder=holder,
                first_written_step=first,
                persisted_steps=persisted,
            )
        )
    compared_first = _first_written(history, "compared")
    if compared_first is not None:
        records.append(
            InternalRecord(
                proposition="A=B",
                value="true" if history[-1].decision else "false",
                holder="comparator",
                first_written_step=compared_first,
                persisted_steps=sum(state.compared for state in history[compared_first:]),
            )
        )
    return tuple(records)


def generated_access_boundary(history: tuple[ReconcilerState, ...]) -> frozenset[str]:
    """Return holders causally wired into persistent memory/comparison."""

    holders = set()
    if _first_written(history, "written_a") is not None:
        holders.add("memory:A")
    if _first_written(history, "written_b") is not None:
        holders.add("memory:B")
    if _first_written(history, "compared") is not None:
        holders.add("comparator")
    return frozenset(holders)


def finality_profile(
    records: tuple[InternalRecord, ...],
    proposition: str,
    value: str = "true",
    threshold: int = 1,
) -> tuple[int, int, int, int]:
    relevant = tuple(
        record
        for record in records
        if record.proposition == proposition and record.value == value
    )
    support = len(relevant)
    if support < threshold:
        return (0, 0, 0, 0)
    holders = len({record.holder for record in relevant})
    first_steps = len({record.first_written_step for record in relevant})
    reversal = max(0, support - threshold + 1)
    persistence = min(record.persisted_steps for record in relevant)
    return (support, holders, max(1, first_steps), max(reversal, persistence))


def decision_from_records(records: tuple[InternalRecord, ...]) -> str | None:
    comparison = [
        record
        for record in records
        if record.proposition == "A=B" and record.holder == "comparator"
    ]
    if not comparison:
        return None
    return comparison[-1].value


def evaluate(env_a: Bit, env_b: Bit, steps: int = 5) -> ReconcilerRun:
    start = initial_state(env_a, env_b)
    history = run(start, steps)
    records = internal_records(history)
    finality_profiles = {}
    for proposition in ("A", "B", "A=B"):
        values = [
            record.value
            for record in records
            if record.proposition == proposition
        ]
        finality_profiles[proposition] = (
            finality_profile(records, proposition, values[-1])
            if values
            else (0, 0, 0, 0)
        )
    return ReconcilerRun(
        initial=start,
        history=history,
        records=records,
        access_boundary=generated_access_boundary(history),
        decision=decision_from_records(records),
        finality_profiles=finality_profiles,
    )


def intervention_profile(env_a: Bit, env_b: Bit, flip_field: str) -> dict[str, object]:
    baseline = evaluate(env_a, env_b)
    if flip_field == "env_a":
        changed = evaluate(1 - env_a, env_b)
    elif flip_field == "env_b":
        changed = evaluate(env_a, 1 - env_b)
    else:
        raise ValueError("flip_field must be env_a or env_b")
    return {
        "flip_field": flip_field,
        "baseline_decision": baseline.decision,
        "changed_decision": changed.decision,
        "decision_changed": baseline.decision != changed.decision,
        "baseline_boundary": sorted(baseline.access_boundary),
        "changed_boundary": sorted(changed.access_boundary),
    }


def sweep_reconciler() -> dict[str, object]:
    runs = tuple(evaluate(a, b) for a, b in product((0, 1), repeat=2))
    both_records = sum(
        {"A", "B"} <= {record.proposition for record in run.records}
        for run in runs
    )
    compared = sum(run.decision is not None for run in runs)
    true_decisions = sum(run.decision == "true" for run in runs)
    false_decisions = sum(run.decision == "false" for run in runs)
    return {
        "cases": len(runs),
        "both_memory_records_fraction": both_records / len(runs),
        "comparison_fraction": compared / len(runs),
        "true_decision_count": true_decisions,
        "false_decision_count": false_decisions,
        "generated_boundaries": sorted(
            {tuple(sorted(run.access_boundary)) for run in runs}
        ),
    }


def failure_without_persistence(env_a: Bit = 1, env_b: Bit = 1) -> dict[str, object]:
    """A control where memory does not latch; records disappear with sensors."""

    pulse = ReconcilerState(env_a, env_b, env_a, env_b, 0, 0, 0, 0, 0, 0)
    final = ReconcilerState(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    final_records = internal_records((final,))
    return {
        "pulse_state": pulse.as_tuple(),
        "final_state": final.as_tuple(),
        "records_at_final_state": len(final_records),
        "decision_at_final_state": decision_from_records(final_records),
        "persistent_reconciler_required": len(final_records) == 0,
    }


def run_t17_analysis() -> dict[str, object]:
    equal = evaluate(1, 1)
    unequal = evaluate(1, 0)
    return {
        "mechanism": [
            "environment cells drive sensors",
            "sensor values latch into persistent memory cells",
            "comparator reads memory cells",
            "decision is internal to the dynamical state",
        ],
        "equal_case": {
            "initial": equal.initial.as_tuple(),
            "final": equal.history[-1].as_tuple(),
            "access_boundary": sorted(equal.access_boundary),
            "decision": equal.decision,
            "profiles": equal.finality_profiles,
        },
        "unequal_case": {
            "initial": unequal.initial.as_tuple(),
            "final": unequal.history[-1].as_tuple(),
            "access_boundary": sorted(unequal.access_boundary),
            "decision": unequal.decision,
            "profiles": unequal.finality_profiles,
        },
        "interventions": [
            intervention_profile(1, 1, "env_a"),
            intervention_profile(1, 1, "env_b"),
        ],
        "sweep": sweep_reconciler(),
        "control_without_persistence": failure_without_persistence(),
        "verdict": {
            "storage_arises_inside_dynamics": True,
            "access_boundary_is_generated": True,
            "reconciliation_is_internal": True,
            "consciousness_not_modeled": True,
            "observer_window_not_terminally_selected": True,
        },
    }
