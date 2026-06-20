"""T110: finite-permutation monotone obstruction for H7.

T106 showed a concrete bounded-sink reversible cycle where the forward
accounting curve loses monotonicity once the return path is included.  T110
turns that observation into the finite closed-reversible obstruction: on a
permutation orbit, any scalar score that is nondecreasing on every edge is
constant on that orbit.  Strict finality can appear only after using an open
branch, erasure, coarse graining, fresh capacity, or excluded degrees of
freedom.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable


T106_CLOSED_ACCOUNTED_SUPPORT = (0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0)


@dataclass(frozen=True)
class OrbitScoreAudit:
    orbit: tuple[int, ...]
    score_sequence: tuple[int, ...]
    edge_deltas: tuple[int, ...]
    nondecreasing: bool
    constant: bool
    strict_increase_edges: int
    decrease_edges: int


@dataclass(frozen=True)
class PermutationScoreAudit:
    state_count: int
    orbit_audits: tuple[OrbitScoreAudit, ...]
    nondecreasing_on_all_edges: bool
    constant_on_each_orbit: bool
    has_strict_increase: bool
    has_decrease: bool
    strict_nondecreasing_possible: bool
    theorem_holds_for_scores: bool
    verdict: str


@dataclass(frozen=True)
class CycleExhaustiveCheck:
    cycle_length: int
    value_count: int
    assignment_count: int
    nondecreasing_assignments: int
    constant_assignments: int
    strict_increase_assignments: int
    strict_without_decrease_assignments: int
    theorem_holds: bool


@dataclass(frozen=True)
class OpenBranchAudit:
    score_sequence: tuple[int, ...]
    nondecreasing: bool
    strict_increase_edges: int
    reversible_closed_system: bool
    verdict: str


@dataclass(frozen=True)
class T110Result:
    theorem_name: str
    t106_closed_cycle_audit: PermutationScoreAudit
    plateau_control_audit: PermutationScoreAudit
    open_branch_control: OpenBranchAudit
    exhaustive_cycle_checks: tuple[CycleExhaustiveCheck, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def closed_cycle_transition(length: int) -> tuple[int, ...]:
    if length < 1:
        raise ValueError("length must be positive")
    return tuple((index + 1) % length for index in range(length))


def orbit_decomposition(transition: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    _validate_permutation(transition)
    seen: set[int] = set()
    orbits: list[tuple[int, ...]] = []
    for start in range(len(transition)):
        if start in seen:
            continue
        orbit: list[int] = []
        current = start
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = transition[current]
        orbits.append(tuple(orbit))
    return tuple(orbits)


def audit_permutation_scores(
    transition: tuple[int, ...],
    scores: tuple[int, ...],
) -> PermutationScoreAudit:
    _validate_permutation(transition)
    if len(scores) != len(transition):
        raise ValueError("scores and transition must have the same length")

    orbit_audits = tuple(
        _audit_orbit_scores(orbit, transition, scores)
        for orbit in orbit_decomposition(transition)
    )
    nondecreasing = all(audit.nondecreasing for audit in orbit_audits)
    constant = all(audit.constant for audit in orbit_audits)
    has_strict = any(audit.strict_increase_edges > 0 for audit in orbit_audits)
    has_decrease = any(audit.decrease_edges > 0 for audit in orbit_audits)
    strict_nondecreasing_possible = nondecreasing and has_strict
    theorem_holds = all(
        (not audit.nondecreasing) or audit.constant for audit in orbit_audits
    )
    if strict_nondecreasing_possible:
        verdict = (
            "counterexample: a strict nondecreasing score was found on a "
            "closed permutation orbit"
        )
    elif nondecreasing:
        verdict = (
            "nondecreasing is possible only because the score is constant on "
            "each closed permutation orbit"
        )
    else:
        verdict = (
            "the closed reversible score is not monotone; any strict increase "
            "is paid back by a decrease on the same finite orbit"
        )
    return PermutationScoreAudit(
        state_count=len(transition),
        orbit_audits=orbit_audits,
        nondecreasing_on_all_edges=nondecreasing,
        constant_on_each_orbit=constant,
        has_strict_increase=has_strict,
        has_decrease=has_decrease,
        strict_nondecreasing_possible=strict_nondecreasing_possible,
        theorem_holds_for_scores=theorem_holds,
        verdict=verdict,
    )


def exhaustive_cycle_check(
    cycle_length: int,
    value_count: int = 3,
) -> CycleExhaustiveCheck:
    if value_count < 1:
        raise ValueError("value_count must be positive")
    transition = closed_cycle_transition(cycle_length)
    assignment_count = 0
    nondecreasing_assignments = 0
    constant_assignments = 0
    strict_increase_assignments = 0
    strict_without_decrease_assignments = 0
    theorem_holds = True
    for scores in product(range(value_count), repeat=cycle_length):
        assignment_count += 1
        audit = audit_permutation_scores(transition, tuple(scores))
        if audit.nondecreasing_on_all_edges:
            nondecreasing_assignments += 1
        if audit.constant_on_each_orbit:
            constant_assignments += 1
        if audit.has_strict_increase:
            strict_increase_assignments += 1
        if audit.has_strict_increase and not audit.has_decrease:
            strict_without_decrease_assignments += 1
        theorem_holds = theorem_holds and audit.theorem_holds_for_scores
    return CycleExhaustiveCheck(
        cycle_length=cycle_length,
        value_count=value_count,
        assignment_count=assignment_count,
        nondecreasing_assignments=nondecreasing_assignments,
        constant_assignments=constant_assignments,
        strict_increase_assignments=strict_increase_assignments,
        strict_without_decrease_assignments=strict_without_decrease_assignments,
        theorem_holds=theorem_holds,
    )


def audit_open_branch_scores(scores: Iterable[int]) -> OpenBranchAudit:
    sequence = tuple(scores)
    if len(sequence) < 2:
        raise ValueError("open branch requires at least two scores")
    deltas = tuple(
        sequence[index + 1] - sequence[index] for index in range(len(sequence) - 1)
    )
    nondecreasing = all(delta >= 0 for delta in deltas)
    strict = sum(1 for delta in deltas if delta > 0)
    if nondecreasing and strict:
        verdict = (
            "strict monotone accounting is possible on the open forward "
            "branch, but this is not a closed reversible system"
        )
    else:
        verdict = "the open branch does not exhibit strict monotone accounting"
    return OpenBranchAudit(
        score_sequence=sequence,
        nondecreasing=nondecreasing,
        strict_increase_edges=strict,
        reversible_closed_system=False,
        verdict=verdict,
    )


def run_t110_analysis() -> T110Result:
    t106_transition = closed_cycle_transition(len(T106_CLOSED_ACCOUNTED_SUPPORT))
    t106_audit = audit_permutation_scores(
        t106_transition,
        T106_CLOSED_ACCOUNTED_SUPPORT,
    )
    plateau_audit = audit_permutation_scores(
        t106_transition,
        tuple(3 for _ in T106_CLOSED_ACCOUNTED_SUPPORT),
    )
    exhaustive_checks = tuple(
        exhaustive_cycle_check(length, value_count=3) for length in range(2, 8)
    )
    open_branch = audit_open_branch_scores((0, 1, 3, 4, 4, 5, 7))
    return T110Result(
        theorem_name="Finite permutation monotone obstruction",
        t106_closed_cycle_audit=t106_audit,
        plateau_control_audit=plateau_audit,
        open_branch_control=open_branch,
        exhaustive_cycle_checks=exhaustive_checks,
        strongest_claim=(
            "In any finite closed reversible system represented by a "
            "permutation, a scalar finality score that is nondecreasing along "
            "every physical step is constant on each orbit. Strict H7-style "
            "increase cannot be generated inside the closed bounded state "
            "space."
        ),
        improved=(
            "T110 generalizes T106 from one bounded-sink witness to a finite "
            "permutation obstruction. It identifies exactly which assumption "
            "must be broken before an H7 arrow can be physical: closed finite "
            "reversibility, scalar/antisymmetric monotone scoring, or inclusion "
            "of all memory and sink degrees of freedom."
        ),
        weakened=(
            "H7 is weakened as a thermodynamic-arrow claim. The finite "
            "constructor theorem survives only as a conditional order on "
            "admissible transformations or as open-system/coarse-grained "
            "resource accounting, not as a strict scalar monotone on closed "
            "bounded reversible dynamics."
        ),
        falsification_condition=(
            "T110 is falsified only by a finite closed reversible model with a "
            "strict D1-relevant scalar monotone on every transition edge and no "
            "excluded environment, erasure, fresh blank capacity, postselected "
            "branch, non-invertible quotient, or time-dependent scoring rule. "
            "Otherwise the model has left the theorem's assumptions."
        ),
        h7_update=(
            "Add T110 to H7: finite closed reversible dynamics cannot carry a "
            "strict scalar finality monotone. H7 must explicitly declare the "
            "open-system, coarse-graining, erasure, resource, or constructor "
            "restriction that supplies direction."
        ),
        claim_ledger_update=(
            "H7 remains partially supported only as a conditional constructor "
            "or open-system resource-accounting claim. T110 proves the finite "
            "permutation obstruction: nondecreasing scalar finality on a "
            "closed reversible orbit is constant, so any strict increase on "
            "the forward branch requires omitted return degrees of freedom or "
            "a non-reversible/coarse-grained boundary."
        ),
        open_blocker=(
            "The project still lacks a physically grounded open-system H7 model "
            "that adds thermodynamic or coarse-grained direction without merely "
            "renaming standard entropy export."
        ),
        recommended_next=(
            "Either demote H7 to a constructor/resource-accounting lemma in "
            "claim-facing prose, or build an explicit open Markov/coarse-grained "
            "record model and compare its arrow to standard entropy production."
        ),
    )


def t110_result_to_dict(result: T110Result) -> dict[str, object]:
    return {
        "theorem_name": result.theorem_name,
        "t106_closed_cycle_audit": _permutation_audit_to_dict(
            result.t106_closed_cycle_audit
        ),
        "plateau_control_audit": _permutation_audit_to_dict(
            result.plateau_control_audit
        ),
        "open_branch_control": {
            "score_sequence": list(result.open_branch_control.score_sequence),
            "nondecreasing": result.open_branch_control.nondecreasing,
            "strict_increase_edges": result.open_branch_control.strict_increase_edges,
            "reversible_closed_system": (
                result.open_branch_control.reversible_closed_system
            ),
            "verdict": result.open_branch_control.verdict,
        },
        "exhaustive_cycle_checks": [
            {
                "cycle_length": check.cycle_length,
                "value_count": check.value_count,
                "assignment_count": check.assignment_count,
                "nondecreasing_assignments": check.nondecreasing_assignments,
                "constant_assignments": check.constant_assignments,
                "strict_increase_assignments": check.strict_increase_assignments,
                "strict_without_decrease_assignments": (
                    check.strict_without_decrease_assignments
                ),
                "theorem_holds": check.theorem_holds,
            }
            for check in result.exhaustive_cycle_checks
        ],
        "strongest_claim": result.strongest_claim,
        "improved": result.improved,
        "weakened": result.weakened,
        "falsification_condition": result.falsification_condition,
        "h7_update": result.h7_update,
        "claim_ledger_update": result.claim_ledger_update,
        "open_blocker": result.open_blocker,
        "recommended_next": result.recommended_next,
    }


def _audit_orbit_scores(
    orbit: tuple[int, ...],
    transition: tuple[int, ...],
    scores: tuple[int, ...],
) -> OrbitScoreAudit:
    score_sequence = tuple(scores[state] for state in orbit)
    deltas = tuple(scores[transition[state]] - scores[state] for state in orbit)
    return OrbitScoreAudit(
        orbit=orbit,
        score_sequence=score_sequence,
        edge_deltas=deltas,
        nondecreasing=all(delta >= 0 for delta in deltas),
        constant=len(set(score_sequence)) == 1,
        strict_increase_edges=sum(1 for delta in deltas if delta > 0),
        decrease_edges=sum(1 for delta in deltas if delta < 0),
    )


def _permutation_audit_to_dict(audit: PermutationScoreAudit) -> dict[str, object]:
    return {
        "state_count": audit.state_count,
        "orbit_audits": [
            {
                "orbit": list(orbit.orbit),
                "score_sequence": list(orbit.score_sequence),
                "edge_deltas": list(orbit.edge_deltas),
                "nondecreasing": orbit.nondecreasing,
                "constant": orbit.constant,
                "strict_increase_edges": orbit.strict_increase_edges,
                "decrease_edges": orbit.decrease_edges,
            }
            for orbit in audit.orbit_audits
        ],
        "nondecreasing_on_all_edges": audit.nondecreasing_on_all_edges,
        "constant_on_each_orbit": audit.constant_on_each_orbit,
        "has_strict_increase": audit.has_strict_increase,
        "has_decrease": audit.has_decrease,
        "strict_nondecreasing_possible": audit.strict_nondecreasing_possible,
        "theorem_holds_for_scores": audit.theorem_holds_for_scores,
        "verdict": audit.verdict,
    }


def _validate_permutation(transition: tuple[int, ...]) -> None:
    if not transition:
        raise ValueError("transition must contain at least one state")
    expected = tuple(range(len(transition)))
    if tuple(sorted(transition)) != expected:
        raise ValueError("transition must be a permutation of state indices")
