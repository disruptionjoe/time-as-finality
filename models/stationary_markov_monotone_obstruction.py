"""T122: stationary Markov monotone obstruction for H7.

T116 left a precise gate for H7: find a finite stochastic record process with
strict finality increase that is not paid for by path irreversibility,
exported history, fresh capacity, postselection, or nonstationary resource
drawdown. T122 closes the stationary finite-Markov version of that gate.

If pi is stationary and f is any scalar finality score, then the pi-weighted
one-step drift of f is exactly zero. Therefore a score with nonnegative
expected drift on every state in the stationary support must have zero drift
on that support. Strict monotone finality can only occur off the stationary
support or after importing a nonstationary/resource/boundary assumption.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import isclose


TOLERANCE = 1e-12


@dataclass(frozen=True)
class MarkovScenario:
    name: str
    transition: tuple[tuple[float, ...], ...]
    stationary: tuple[float, ...]
    score: tuple[float, ...]
    declared_resource: str


@dataclass(frozen=True)
class DriftAudit:
    name: str
    score: tuple[float, ...]
    stationary: tuple[float, ...]
    expected_next_score: tuple[float, ...]
    drift_by_state: tuple[float, ...]
    stationary_weighted_drift: float
    stationary_support: tuple[int, ...]
    nonnegative_on_stationary_support: bool
    strict_positive_on_stationary_support: bool
    strict_positive_off_stationary_support: bool
    theorem_violation: bool
    classification: str
    verdict: str


@dataclass(frozen=True)
class DeterministicFunctionCheck:
    state_count: int
    value_count: int
    transition_count: int
    score_assignment_count: int
    recurrent_strict_monotone_assignments: int
    all_state_nondecreasing_assignments: int
    transient_only_strict_assignments: int
    theorem_holds: bool


@dataclass(frozen=True)
class T122Result:
    theorem_name: str
    detailed_balance_control: DriftAudit
    biased_cycle_control: DriftAudit
    absorbing_append_control: DriftAudit
    deterministic_function_checks: tuple[DeterministicFunctionCheck, ...]
    strongest_claim: str
    improved: str
    weakened: str
    falsification_condition: str
    h7_update: str
    claim_ledger_update: str
    open_blocker: str
    recommended_next: str


def detailed_balance_control() -> MarkovScenario:
    return MarkovScenario(
        name="detailed_balance_two_state_control",
        transition=((0.8, 0.2), (0.2, 0.8)),
        stationary=(0.5, 0.5),
        score=(0.0, 1.0),
        declared_resource="none: stationary detailed-balance control",
    )


def biased_cycle_control() -> MarkovScenario:
    return MarkovScenario(
        name="biased_three_cycle_control",
        transition=(
            (0.0, 0.9, 0.1),
            (0.1, 0.0, 0.9),
            (0.9, 0.1, 0.0),
        ),
        stationary=(1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0),
        score=(0.0, 1.0, 2.0),
        declared_resource=(
            "none for stationarity; the circulation can be entropy-producing "
            "but the scalar score still cannot drift up everywhere"
        ),
    )


def absorbing_append_control() -> MarkovScenario:
    return MarkovScenario(
        name="absorbing_append_transient_control",
        transition=(
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
            (0.0, 0.0, 0.0, 1.0),
        ),
        stationary=(0.0, 0.0, 0.0, 1.0),
        score=(0.0, 1.0, 2.0, 3.0),
        declared_resource=(
            "transient append path into an absorbing full-record state; the "
            "strict drift is off stationary support"
        ),
    )


def audit_markov_scenario(scenario: MarkovScenario) -> DriftAudit:
    _validate_scenario(scenario)
    expected_next = tuple(
        sum(probability * scenario.score[target] for target, probability in enumerate(row))
        for row in scenario.transition
    )
    drift = tuple(
        expected_next[state] - scenario.score[state]
        for state in range(len(scenario.score))
    )
    support = tuple(
        state for state, probability in enumerate(scenario.stationary)
        if probability > TOLERANCE
    )
    weighted_drift = sum(
        scenario.stationary[state] * drift[state]
        for state in range(len(scenario.score))
    )
    nonnegative_on_support = all(drift[state] >= -TOLERANCE for state in support)
    strict_on_support = any(drift[state] > TOLERANCE for state in support)
    strict_off_support = any(
        drift[state] > TOLERANCE and state not in support
        for state in range(len(scenario.score))
    )
    theorem_violation = (
        nonnegative_on_support
        and strict_on_support
        and isclose(weighted_drift, 0.0, abs_tol=TOLERANCE)
    )
    classification = _classify_audit(
        nonnegative_on_support=nonnegative_on_support,
        strict_on_support=strict_on_support,
        strict_off_support=strict_off_support,
    )
    return DriftAudit(
        name=scenario.name,
        score=scenario.score,
        stationary=scenario.stationary,
        expected_next_score=expected_next,
        drift_by_state=drift,
        stationary_weighted_drift=weighted_drift,
        stationary_support=support,
        nonnegative_on_stationary_support=nonnegative_on_support,
        strict_positive_on_stationary_support=strict_on_support,
        strict_positive_off_stationary_support=strict_off_support,
        theorem_violation=theorem_violation,
        classification=classification,
        verdict=_verdict_for(classification),
    )


def deterministic_function_check(
    state_count: int,
    value_count: int = 3,
) -> DeterministicFunctionCheck:
    """Exhaust deterministic finite maps as a sanity check.

    A deterministic finite Markov chain is a function graph. Recurrent states
    sit on cycles; transient states feed into those cycles. Nondecreasing
    scores may climb along transient trees, but they cannot strictly climb on
    any recurrent cycle.
    """

    if state_count < 1:
        raise ValueError("state_count must be positive")
    if value_count < 1:
        raise ValueError("value_count must be positive")

    transition_count = 0
    score_assignment_count = value_count**state_count
    recurrent_strict = 0
    all_state_nondecreasing = 0
    transient_only_strict = 0
    theorem_holds = True

    for transition in product(range(state_count), repeat=state_count):
        transition_count += 1
        recurrent_states = _deterministic_recurrent_states(tuple(transition))
        transient_states = set(range(state_count)) - set(recurrent_states)
        for score in product(range(value_count), repeat=state_count):
            drifts = tuple(score[transition[state]] - score[state] for state in range(state_count))
            nonnegative_on_recurrent = all(
                drifts[state] >= 0 for state in recurrent_states
            )
            strict_on_recurrent = any(
                drifts[state] > 0 for state in recurrent_states
            )
            if nonnegative_on_recurrent and strict_on_recurrent:
                recurrent_strict += 1
                theorem_holds = False
            if all(delta >= 0 for delta in drifts):
                all_state_nondecreasing += 1
                if any(drifts[state] > 0 for state in transient_states) and not strict_on_recurrent:
                    transient_only_strict += 1

    return DeterministicFunctionCheck(
        state_count=state_count,
        value_count=value_count,
        transition_count=transition_count,
        score_assignment_count=score_assignment_count,
        recurrent_strict_monotone_assignments=recurrent_strict,
        all_state_nondecreasing_assignments=all_state_nondecreasing,
        transient_only_strict_assignments=transient_only_strict,
        theorem_holds=theorem_holds,
    )


def run_t122_analysis() -> T122Result:
    detailed_balance = audit_markov_scenario(detailed_balance_control())
    biased_cycle = audit_markov_scenario(biased_cycle_control())
    absorbing_append = audit_markov_scenario(absorbing_append_control())
    checks = tuple(
        deterministic_function_check(state_count, value_count=3)
        for state_count in range(2, 5)
    )
    return T122Result(
        theorem_name="Stationary Markov monotone obstruction",
        detailed_balance_control=detailed_balance,
        biased_cycle_control=biased_cycle,
        absorbing_append_control=absorbing_append,
        deterministic_function_checks=checks,
        strongest_claim=(
            "In a finite Markov model at a stationary distribution, any scalar "
            "finality score with nonnegative one-step expected drift on every "
            "state in the stationary support has zero drift on that support. "
            "Strict H7-style monotonicity can appear only in transient or "
            "nonstationary sectors, or after naming a sink, boundary, capacity "
            "resource, postselection, or excluded reverse channel."
        ),
        improved=(
            "T122 turns the T116 zero-resource stochastic record-arrow gate "
            "into a stationary finite-Markov obstruction. It separates true "
            "stationary support from positive-looking transient append paths."
        ),
        weakened=(
            "H7 is weakened as an independent thermodynamic-arrow proposal. "
            "Finite stationary stochastic dynamics cannot carry a strict "
            "scalar expected-finality arrow on their stationary support; any "
            "candidate arrow must be paid for by nonstationary resource "
            "drawdown, a boundary condition, or ordinary stochastic "
            "thermodynamic structure."
        ),
        falsification_condition=(
            "T122 is falsified by a finite Markov chain with a declared "
            "stationary distribution pi, piP=pi, and scalar D1-relevant score "
            "f such that E[f(X_{t+1})-f(X_t)|X_t=i] >= 0 for every state i "
            "with pi_i>0, with strict positivity for at least one such state, "
            "and with no time-dependent score, hidden state, omitted reverse "
            "channel, transient-only support, or nonstationary resource "
            "drawdown."
        ),
        h7_update=(
            "Add T122 to H7: the finite stationary Markov obstruction blocks "
            "the stationary version of a zero-resource record arrow. Strict "
            "expected finality cannot increase on stationary support without "
            "leaving the assumptions."
        ),
        claim_ledger_update=(
            "H7 remains partially supported only as a conditional "
            "constructor/resource-accounting claim. T122 proves the finite "
            "stationary Markov obstruction: for piP=pi, the pi-weighted "
            "expected drift of any scalar finality score is zero, so "
            "nonnegative drift on every stationary-support state must be zero "
            "there. Strict stochastic record arrows require transient "
            "support, nonstationary resource drawdown, boundary/sink "
            "accounting, postselection, or excluded reverse channels."
        ),
        open_blocker=(
            "The remaining H7 route must be nonstationary, infinite-state, "
            "coarse-grained, or resource-explicit. It must quantify the "
            "free-energy, boundary, memory, or capacity drawdown rather than "
            "calling that drawdown finality."
        ),
        recommended_next=(
            "Demote H7's paper-facing label from thermodynamic-arrow claim to "
            "constructor/resource-accounting lemma, then decide whether a "
            "nonstationary free-energy model is still worth pursuing."
        ),
    )


def t122_result_to_dict(result: T122Result) -> dict[str, object]:
    return {
        "theorem_name": result.theorem_name,
        "detailed_balance_control": _audit_to_dict(result.detailed_balance_control),
        "biased_cycle_control": _audit_to_dict(result.biased_cycle_control),
        "absorbing_append_control": _audit_to_dict(result.absorbing_append_control),
        "deterministic_function_checks": [
            {
                "state_count": check.state_count,
                "value_count": check.value_count,
                "transition_count": check.transition_count,
                "score_assignment_count": check.score_assignment_count,
                "recurrent_strict_monotone_assignments": (
                    check.recurrent_strict_monotone_assignments
                ),
                "all_state_nondecreasing_assignments": (
                    check.all_state_nondecreasing_assignments
                ),
                "transient_only_strict_assignments": (
                    check.transient_only_strict_assignments
                ),
                "theorem_holds": check.theorem_holds,
            }
            for check in result.deterministic_function_checks
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


def _validate_scenario(scenario: MarkovScenario) -> None:
    state_count = len(scenario.transition)
    if state_count == 0:
        raise ValueError("transition must not be empty")
    if len(scenario.stationary) != state_count or len(scenario.score) != state_count:
        raise ValueError("stationary distribution and score must match transition size")
    for row in scenario.transition:
        if len(row) != state_count:
            raise ValueError("transition matrix must be square")
        if any(probability < -TOLERANCE for probability in row):
            raise ValueError("transition probabilities must be nonnegative")
        if not isclose(sum(row), 1.0, abs_tol=TOLERANCE):
            raise ValueError("each transition row must sum to 1")
    if any(probability < -TOLERANCE for probability in scenario.stationary):
        raise ValueError("stationary distribution probabilities must be nonnegative")
    if not isclose(sum(scenario.stationary), 1.0, abs_tol=TOLERANCE):
        raise ValueError("stationary distribution must sum to 1")

    pushed_forward = tuple(
        sum(
            scenario.stationary[source] * scenario.transition[source][target]
            for source in range(state_count)
        )
        for target in range(state_count)
    )
    for actual, expected in zip(pushed_forward, scenario.stationary):
        if not isclose(actual, expected, abs_tol=TOLERANCE):
            raise ValueError("stationary distribution must satisfy piP=pi")


def _classify_audit(
    *,
    nonnegative_on_support: bool,
    strict_on_support: bool,
    strict_off_support: bool,
) -> str:
    if nonnegative_on_support and strict_on_support:
        return "stationary_support_counterexample"
    if strict_off_support:
        return "transient_only_monotonicity"
    if nonnegative_on_support:
        return "zero_drift_on_stationary_support"
    return "not_a_monotone"


def _verdict_for(classification: str) -> str:
    verdicts = {
        "stationary_support_counterexample": (
            "This would refute the stationary Markov obstruction."
        ),
        "transient_only_monotonicity": (
            "Strict increase occurs only off stationary support, so the arrow "
            "is a transient/resource-boundary effect."
        ),
        "zero_drift_on_stationary_support": (
            "The score is nonnegative on stationary support only because the "
            "expected drift is zero there."
        ),
        "not_a_monotone": (
            "The score has a negative expected drift on part of the "
            "stationary support, so it is not an H7 monotone."
        ),
    }
    return verdicts[classification]


def _deterministic_recurrent_states(transition: tuple[int, ...]) -> tuple[int, ...]:
    recurrent: set[int] = set()
    for start in range(len(transition)):
        seen_at: dict[int, int] = {}
        path: list[int] = []
        current = start
        while current not in seen_at:
            seen_at[current] = len(path)
            path.append(current)
            current = transition[current]
        recurrent.update(path[seen_at[current] :])
    return tuple(sorted(recurrent))


def _audit_to_dict(audit: DriftAudit) -> dict[str, object]:
    return {
        "name": audit.name,
        "score": list(audit.score),
        "stationary": list(audit.stationary),
        "expected_next_score": list(audit.expected_next_score),
        "drift_by_state": list(audit.drift_by_state),
        "stationary_weighted_drift": audit.stationary_weighted_drift,
        "stationary_support": list(audit.stationary_support),
        "nonnegative_on_stationary_support": (
            audit.nonnegative_on_stationary_support
        ),
        "strict_positive_on_stationary_support": (
            audit.strict_positive_on_stationary_support
        ),
        "strict_positive_off_stationary_support": (
            audit.strict_positive_off_stationary_support
        ),
        "theorem_violation": audit.theorem_violation,
        "classification": audit.classification,
        "verdict": audit.verdict,
    }
