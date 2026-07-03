"""T420 - Finite-cycle anti-relabel gate.

This model turns the decisive T419 K4 failure into a reusable finite guardrail:
on a closed finite public permutation, the predecessor of a state on a known or
discoverable cycle is obtained by forward iteration around the cycle. A toy
finite permutation therefore cannot earn a computational arrow merely by naming a
trapdoor inverse; it must either declare a family-level period-hardness
assumption, leave the closed public-permutation regime, or demote to T417.

No claim promotion. Cryptography and number theory remain objects of study, not
physics evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Callable, Iterable, Sequence

from models.computational_arrow_of_time import N, SEED, forward, quad_residues


@dataclass(frozen=True)
class CycleAudit:
    start_label: int
    cycle_labels: tuple[int, ...]
    cycle_length: int
    public_predecessor_label: int
    forward_steps_to_predecessor: int
    within_feasible_bound: bool


@dataclass(frozen=True)
class PermutationGateAudit:
    name: str
    state_labels: tuple[int, ...]
    feasible_step_bound: int
    cycles: tuple[CycleAudit, ...]
    max_forward_steps_to_predecessor: int
    every_predecessor_recovered_within_bound: bool
    bounded_nonrecovery_is_evidence: bool
    anti_relabel_claim_allowed: bool
    verdict: str


@dataclass(frozen=True)
class T420Result:
    artifact: str
    target: str
    t419_qr77_gate: PermutationGateAudit
    t419_seed_orbit: CycleAudit
    long_cycle_small_bound_control: PermutationGateAudit
    long_cycle_full_bound_control: PermutationGateAudit
    finite_cycle_theorem: str
    redesign_rule: str
    relation_to_t110: str
    claim_ledger_update: str


def closed_cycle_transition(length: int) -> tuple[int, ...]:
    if length < 1:
        raise ValueError("length must be positive")
    return tuple((index + 1) % length for index in range(length))


def transition_from_labels(
    labels: Sequence[int],
    transition_fn: Callable[[int], int],
) -> tuple[int, ...]:
    if not labels:
        raise ValueError("labels must not be empty")
    label_to_index = {label: index for index, label in enumerate(labels)}
    if len(label_to_index) != len(labels):
        raise ValueError("labels must be unique")

    transition: list[int] = []
    for label in labels:
        image = transition_fn(label)
        if image not in label_to_index:
            raise ValueError("transition image is not in the declared state set")
        transition.append(label_to_index[image])
    _validate_permutation(tuple(transition))
    return tuple(transition)


def audit_public_permutation(
    transition: tuple[int, ...],
    labels: Iterable[int] | None = None,
    feasible_step_bound: int | None = None,
    name: str = "public_permutation",
) -> PermutationGateAudit:
    _validate_permutation(transition)
    state_labels = tuple(labels) if labels is not None else tuple(range(len(transition)))
    if len(state_labels) != len(transition):
        raise ValueError("labels and transition must have the same length")
    if feasible_step_bound is None:
        feasible_step_bound = len(transition) - 1
    if feasible_step_bound < 0:
        raise ValueError("feasible_step_bound must be nonnegative")

    cycles = tuple(
        _audit_cycle(transition, state_labels, orbit, feasible_step_bound)
        for orbit in _orbit_decomposition(transition)
    )
    max_steps = max(cycle.forward_steps_to_predecessor for cycle in cycles)
    recovered_within_bound = all(cycle.within_feasible_bound for cycle in cycles)

    if recovered_within_bound:
        verdict = (
            "finite_public_cycle_absorbs_arrow: public forward iteration recovers "
            "each predecessor within the declared feasible bound"
        )
        anti_relabel_claim_allowed = False
    else:
        verdict = (
            "bounded_search_inconclusive: non-recovery within this bound is not "
            "arrow evidence; a family-level period-hardness assumption or a "
            "different regime must be declared"
        )
        anti_relabel_claim_allowed = False

    return PermutationGateAudit(
        name=name,
        state_labels=state_labels,
        feasible_step_bound=feasible_step_bound,
        cycles=cycles,
        max_forward_steps_to_predecessor=max_steps,
        every_predecessor_recovered_within_bound=recovered_within_bound,
        bounded_nonrecovery_is_evidence=False,
        anti_relabel_claim_allowed=anti_relabel_claim_allowed,
        verdict=verdict,
    )


def cycle_audit_for_label(audit: PermutationGateAudit, label: int) -> CycleAudit:
    for cycle in audit.cycles:
        if label in cycle.cycle_labels:
            return cycle
    raise ValueError("label not found in audit")


def run_t420_analysis() -> T420Result:
    qr77 = tuple(quad_residues(N))
    qr_transition = transition_from_labels(qr77, lambda x: forward(x, N))
    qr_audit = audit_public_permutation(
        qr_transition,
        labels=qr77,
        feasible_step_bound=3,
        name="T419 QR_77 squaring permutation",
    )
    seed_orbit = cycle_audit_for_label(qr_audit, SEED)

    long_transition = closed_cycle_transition(17)
    long_small = audit_public_permutation(
        long_transition,
        feasible_step_bound=5,
        name="length-17 cycle with small feasible bound",
    )
    long_full = audit_public_permutation(
        long_transition,
        feasible_step_bound=16,
        name="length-17 cycle with full cycle bound",
    )

    return T420Result(
        artifact="T420-finite-cycle-anti-relabel-gate-v0.1",
        target="D2 computational-finality arrow after T419 REDESIGN",
        t419_qr77_gate=qr_audit,
        t419_seed_orbit=seed_orbit,
        long_cycle_small_bound_control=long_small,
        long_cycle_full_bound_control=long_full,
        finite_cycle_theorem=(
            "For a closed finite public permutation F on a state set S, every "
            "state y lies on a finite cycle of length L, and the predecessor of "
            "y is F^(L-1)(y). If L-1 is feasible or discoverable inside the "
            "declared bound, trapdoor-free predecessor recovery is public."
        ),
        redesign_rule=(
            "A D2 redesign cannot rely on a toy finite public cycle. It must "
            "declare family-level period hardness, change the agent's public "
            "transition knowledge, leave the closed permutation regime, or "
            "demote the temporal story to T417's static E2 boundary."
        ),
        relation_to_t110=(
            "T110 blocks strict scalar finality monotones on closed finite "
            "permutation orbits. T420 blocks a sibling anti-relabel move: "
            "closed finite public permutation orbits also provide their own "
            "public predecessor recovery once the cycle is traversable."
        ),
        claim_ledger_update="none; guardrail only; no D2 discharge or promotion",
    )


def t420_result_to_dict(result: T420Result) -> dict[str, object]:
    return {
        "artifact": result.artifact,
        "target": result.target,
        "t419_qr77_gate": _audit_to_dict(result.t419_qr77_gate),
        "t419_seed_orbit": _cycle_to_dict(result.t419_seed_orbit),
        "long_cycle_small_bound_control": _audit_to_dict(
            result.long_cycle_small_bound_control
        ),
        "long_cycle_full_bound_control": _audit_to_dict(
            result.long_cycle_full_bound_control
        ),
        "finite_cycle_theorem": result.finite_cycle_theorem,
        "redesign_rule": result.redesign_rule,
        "relation_to_t110": result.relation_to_t110,
        "claim_ledger_update": result.claim_ledger_update,
    }


def _orbit_decomposition(transition: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    orbits: list[tuple[int, ...]] = []
    for start in range(len(transition)):
        if start in seen:
            continue
        current = start
        orbit: list[int] = []
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = transition[current]
        orbits.append(tuple(orbit))
    return tuple(orbits)


def _audit_cycle(
    transition: tuple[int, ...],
    labels: tuple[int, ...],
    orbit: tuple[int, ...],
    feasible_step_bound: int,
) -> CycleAudit:
    start = orbit[0]
    cycle_length = len(orbit)
    predecessor_index = start
    for _ in range(cycle_length - 1):
        predecessor_index = transition[predecessor_index]
    if transition[predecessor_index] != start:
        raise AssertionError("cycle predecessor computation failed")
    return CycleAudit(
        start_label=labels[start],
        cycle_labels=tuple(labels[index] for index in orbit),
        cycle_length=cycle_length,
        public_predecessor_label=labels[predecessor_index],
        forward_steps_to_predecessor=cycle_length - 1,
        within_feasible_bound=(cycle_length - 1) <= feasible_step_bound,
    )


def _validate_permutation(transition: tuple[int, ...]) -> None:
    if not transition:
        raise ValueError("transition must contain at least one state")
    if tuple(sorted(transition)) != tuple(range(len(transition))):
        raise ValueError("transition must be a permutation of state indices")


def _cycle_to_dict(cycle: CycleAudit) -> dict[str, object]:
    return {
        "start_label": cycle.start_label,
        "cycle_labels": list(cycle.cycle_labels),
        "cycle_length": cycle.cycle_length,
        "public_predecessor_label": cycle.public_predecessor_label,
        "forward_steps_to_predecessor": cycle.forward_steps_to_predecessor,
        "within_feasible_bound": cycle.within_feasible_bound,
    }


def _audit_to_dict(audit: PermutationGateAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "state_labels": list(audit.state_labels),
        "feasible_step_bound": audit.feasible_step_bound,
        "cycles": [_cycle_to_dict(cycle) for cycle in audit.cycles],
        "max_forward_steps_to_predecessor": audit.max_forward_steps_to_predecessor,
        "every_predecessor_recovered_within_bound": (
            audit.every_predecessor_recovered_within_bound
        ),
        "bounded_nonrecovery_is_evidence": audit.bounded_nonrecovery_is_evidence,
        "anti_relabel_claim_allowed": audit.anti_relabel_claim_allowed,
        "verdict": audit.verdict,
    }


if __name__ == "__main__":
    print(json.dumps(t420_result_to_dict(run_t420_analysis()), indent=2))
