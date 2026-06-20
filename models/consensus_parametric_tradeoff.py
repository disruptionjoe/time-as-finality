"""Parametric classification of the T17 consensus tradeoff.

T17 showed that one finite consensus-finality model has no configuration that
jointly maximizes D1 dimensions and bounded progress at budget=10 and
adversarial_delay=2. This module exposes the finite caps behind that model and
maps where the tradeoff is preserved or collapses.

This module does not change T17. It reuses the same evaluation semantics while
making the parameter surface explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from models.consensus_finality_crosswalk import (
    D1Vector,
    ProtocolConfig,
    ProtocolEvaluation,
    THEOREM_OBJECTIVES,
    evaluate_config,
)


RegimeName = str


@dataclass(frozen=True)
class ParameterSurface:
    max_nodes: int = 6
    max_branches: int = 4
    max_confirmations: int = 4
    max_timeout: int = 4
    min_budget: int = 4
    max_budget: int = 32
    min_adversarial_delay: int = 1
    max_adversarial_delay: int = 8
    canonical_budget: int = 10
    canonical_adversarial_delay: int = 2

    def validate(self) -> None:
        if min(
            self.max_nodes,
            self.max_branches,
            self.max_confirmations,
            self.max_timeout,
            self.min_budget,
            self.max_budget,
            self.min_adversarial_delay,
            self.max_adversarial_delay,
        ) < 1:
            raise ValueError("parameter surface values must be positive")
        if self.min_budget > self.max_budget:
            raise ValueError("min_budget cannot exceed max_budget")
        if self.min_adversarial_delay > self.max_adversarial_delay:
            raise ValueError(
                "min_adversarial_delay cannot exceed max_adversarial_delay"
            )


@dataclass(frozen=True)
class ParameterPoint:
    budget: int
    adversarial_delay: int


@dataclass(frozen=True)
class TradeoffPointResult:
    point: ParameterPoint
    checked_configurations: int
    component_maxima: D1Vector
    progress_maximum: int
    joint_maximizers: tuple[ProtocolEvaluation, ...]
    holds: bool
    regime: RegimeName
    regime_reason: str

    def objective_maxima(self) -> tuple[int, int, int, int, int]:
        return self.component_maxima.as_tuple() + (self.progress_maximum,)


@dataclass(frozen=True)
class BudgetWindow:
    adversarial_delay: int
    start_budget: int
    end_budget: int
    regime: RegimeName


@dataclass(frozen=True)
class MinimalConditionReport:
    preserved_tradeoff_windows: tuple[BudgetWindow, ...]
    minimal_preserved_point: ParameterPoint | None
    minimal_degenerate_failure: TradeoffPointResult | None
    minimal_saturated_failure: TradeoffPointResult | None
    minimal_collapse_failure: TradeoffPointResult | None
    recommendation: str


@dataclass(frozen=True)
class ConsensusParametricTradeoffResult:
    surface: ParameterSurface
    points: tuple[TradeoffPointResult, ...]
    regime_counts: dict[RegimeName, int]
    minimal_conditions: MinimalConditionReport
    strongest_claim: str
    weakened_claim: str
    claim_impact: str
    recommended_next: str


def generate_protocol_space(
    surface: ParameterSurface,
    budget: int,
    adversarial_delay: int,
) -> tuple[ProtocolEvaluation, ...]:
    surface.validate()
    evaluations: list[ProtocolEvaluation] = []
    for nodes, branches, confirmations, timeout_rounds in product(
        range(1, surface.max_nodes + 1),
        range(1, surface.max_branches + 1),
        range(1, surface.max_confirmations + 1),
        range(1, surface.max_timeout + 1),
    ):
        resource_cost = nodes + branches + confirmations + timeout_rounds
        if resource_cost > budget:
            continue
        for quorum in range(1, nodes + 1):
            config = ProtocolConfig(
                name=(
                    f"n{nodes}-q{quorum}-b{branches}-"
                    f"c{confirmations}-t{timeout_rounds}"
                ),
                nodes=nodes,
                quorum=quorum,
                branches=branches,
                confirmations=confirmations,
                timeout_rounds=timeout_rounds,
                budget=budget,
            )
            evaluations.append(evaluate_config(config, adversarial_delay))
    return tuple(evaluations)


def verify_parameter_point(
    surface: ParameterSurface,
    budget: int,
    adversarial_delay: int,
) -> TradeoffPointResult:
    evaluations = generate_protocol_space(surface, budget, adversarial_delay)
    if not evaluations:
        raise ValueError("parameter point has no admissible configurations")

    component_maxima = D1Vector(
        accessible_support=max(item.d1.accessible_support for item in evaluations),
        holder_redundancy=max(item.d1.holder_redundancy for item in evaluations),
        branch_support=max(item.d1.branch_support for item in evaluations),
        reversal_cost=max(item.d1.reversal_cost for item in evaluations),
    )
    progress_maximum = max(item.progress_score for item in evaluations)
    objective_maxima = component_maxima.as_tuple() + (progress_maximum,)
    joint_maximizers = tuple(
        item for item in evaluations if item.objective_tuple() == objective_maxima
    )
    holds = not joint_maximizers
    regime, reason = classify_regime(
        surface=surface,
        budget=budget,
        adversarial_delay=adversarial_delay,
        component_maxima=component_maxima,
        progress_maximum=progress_maximum,
        joint_maximizers=joint_maximizers,
    )
    return TradeoffPointResult(
        point=ParameterPoint(budget, adversarial_delay),
        checked_configurations=len(evaluations),
        component_maxima=component_maxima,
        progress_maximum=progress_maximum,
        joint_maximizers=joint_maximizers,
        holds=holds,
        regime=regime,
        regime_reason=reason,
    )


def classify_regime(
    surface: ParameterSurface,
    budget: int,
    adversarial_delay: int,
    component_maxima: D1Vector,
    progress_maximum: int,
    joint_maximizers: tuple[ProtocolEvaluation, ...],
) -> tuple[RegimeName, str]:
    if not joint_maximizers:
        if (
            budget == surface.canonical_budget
            and adversarial_delay == surface.canonical_adversarial_delay
        ):
            return (
                "canonical_tradeoff",
                "The original T17 parameter point preserves the joint-maximizer obstruction.",
            )
        return (
            "scarcity",
            "Resources are expressive enough for multiple objectives but too scarce to maximize all objectives together.",
        )

    if _is_degenerate(component_maxima):
        return (
            "degenerate",
            "The search space is too small to express independent D1/progress objectives.",
        )

    if _is_saturated(surface, component_maxima, progress_maximum):
        return (
            "saturated",
            "Finite caps are all reachable while bounded progress is also satisfied.",
        )

    return (
        "collapse_no_tradeoff",
        "A joint maximizer exists outside the low-budget degeneracy and finite-cap saturation cases.",
    )


def run_consensus_parametric_tradeoff_analysis(
    surface: ParameterSurface | None = None,
) -> ConsensusParametricTradeoffResult:
    active_surface = surface or ParameterSurface()
    points = tuple(
        verify_parameter_point(active_surface, budget, adversarial_delay)
        for adversarial_delay in range(
            active_surface.min_adversarial_delay,
            active_surface.max_adversarial_delay + 1,
        )
        for budget in range(
            active_surface.min_budget,
            active_surface.max_budget + 1,
        )
    )
    regime_counts = _regime_counts(points)
    minimal_conditions = _minimal_conditions(points)
    return ConsensusParametricTradeoffResult(
        surface=active_surface,
        points=points,
        regime_counts=regime_counts,
        minimal_conditions=minimal_conditions,
        strongest_claim=(
            "In the bounded T17-style consensus model, D1/progress finality "
            "tradeoffs are preserved in scarcity regimes but collapse in "
            "degenerate low-budget regimes and saturated finite-cap regimes."
        ),
        weakened_claim=(
            "The original T17 result should not be treated as parameter-free. "
            "It is a bounded theorem candidate only when its resource, delay, "
            "and cap conditions are stated."
        ),
        claim_impact=(
            "RL-003 gains a cleaner external theorem candidate, but only as a "
            "parameter-conditioned finite result. No claim status changes."
        ),
        recommended_next=(
            "Derive symbolic inequalities for the scarcity window instead of "
            "relying on grid enumeration, then test whether richer protocol "
            "features shift the boundaries."
        ),
    )


def consensus_parametric_tradeoff_result_to_dict(
    result: ConsensusParametricTradeoffResult,
) -> dict[str, object]:
    return {
        "surface": {
            "max_nodes": result.surface.max_nodes,
            "max_branches": result.surface.max_branches,
            "max_confirmations": result.surface.max_confirmations,
            "max_timeout": result.surface.max_timeout,
            "min_budget": result.surface.min_budget,
            "max_budget": result.surface.max_budget,
            "min_adversarial_delay": result.surface.min_adversarial_delay,
            "max_adversarial_delay": result.surface.max_adversarial_delay,
            "canonical_budget": result.surface.canonical_budget,
            "canonical_adversarial_delay": (
                result.surface.canonical_adversarial_delay
            ),
        },
        "regime_counts": dict(result.regime_counts),
        "regime_table": [_point_to_dict(point) for point in result.points],
        "minimal_conditions": _minimal_conditions_to_dict(
            result.minimal_conditions
        ),
        "strongest_claim": result.strongest_claim,
        "weakened_claim": result.weakened_claim,
        "claim_impact": result.claim_impact,
        "recommended_next": result.recommended_next,
    }


def _is_degenerate(component_maxima: D1Vector) -> bool:
    return (
        component_maxima.accessible_support <= 1
        and component_maxima.holder_redundancy <= 1
        and component_maxima.branch_support <= 1
    )


def _is_saturated(
    surface: ParameterSurface,
    component_maxima: D1Vector,
    progress_maximum: int,
) -> bool:
    support_cap = min(surface.max_nodes, surface.max_timeout)
    branch_cap = min(surface.max_branches, support_cap)
    reversal_cap = support_cap * surface.max_confirmations
    return (
        progress_maximum == 1
        and component_maxima.accessible_support == support_cap
        and component_maxima.holder_redundancy == support_cap
        and component_maxima.branch_support == branch_cap
        and component_maxima.reversal_cost == reversal_cap
    )


def _regime_counts(
    points: tuple[TradeoffPointResult, ...],
) -> dict[RegimeName, int]:
    counts: dict[RegimeName, int] = {}
    for point in points:
        counts[point.regime] = counts.get(point.regime, 0) + 1
    return counts


def _minimal_conditions(
    points: tuple[TradeoffPointResult, ...],
) -> MinimalConditionReport:
    preserved = tuple(point for point in points if point.holds)
    minimal_preserved = min(
        (point.point for point in preserved),
        key=lambda item: (item.budget, item.adversarial_delay),
        default=None,
    )
    degenerate = _minimal_failure(points, "degenerate")
    saturated = _minimal_failure(points, "saturated")
    collapse = _minimal_failure(points, "collapse_no_tradeoff")
    recommendation = (
        "Upgrade T17 from a single finite witness to a bounded theorem with "
        "explicit parameter conditions: exclude degenerate low-budget points, "
        "exclude saturated finite-cap points, and state the verified scarcity "
        "window. Do not promote RL-003 until those inequalities are proved or "
        "the grid classification is accepted as the intended finite theorem."
    )
    return MinimalConditionReport(
        preserved_tradeoff_windows=_budget_windows(preserved),
        minimal_preserved_point=minimal_preserved,
        minimal_degenerate_failure=degenerate,
        minimal_saturated_failure=saturated,
        minimal_collapse_failure=collapse,
        recommendation=recommendation,
    )


def _minimal_failure(
    points: tuple[TradeoffPointResult, ...],
    regime: RegimeName,
) -> TradeoffPointResult | None:
    candidates = tuple(point for point in points if point.regime == regime)
    if not candidates:
        return None
    return min(
        candidates,
        key=lambda item: (item.point.budget, item.point.adversarial_delay),
    )


def _budget_windows(
    points: tuple[TradeoffPointResult, ...],
) -> tuple[BudgetWindow, ...]:
    by_delay: dict[int, list[TradeoffPointResult]] = {}
    for point in points:
        by_delay.setdefault(point.point.adversarial_delay, []).append(point)

    windows: list[BudgetWindow] = []
    for delay, delay_points in sorted(by_delay.items()):
        sorted_points = sorted(delay_points, key=lambda item: item.point.budget)
        start = sorted_points[0].point.budget
        previous = start
        regime = sorted_points[0].regime
        for point in sorted_points[1:]:
            current = point.point.budget
            if current == previous + 1 and point.regime == regime:
                previous = current
                continue
            windows.append(BudgetWindow(delay, start, previous, regime))
            start = current
            previous = current
            regime = point.regime
        windows.append(BudgetWindow(delay, start, previous, regime))
    return tuple(windows)


def _point_to_dict(point: TradeoffPointResult) -> dict[str, object]:
    return {
        "budget": point.point.budget,
        "adversarial_delay": point.point.adversarial_delay,
        "checked_configurations": point.checked_configurations,
        "component_maxima": {
            "accessible_support": point.component_maxima.accessible_support,
            "holder_redundancy": point.component_maxima.holder_redundancy,
            "branch_support": point.component_maxima.branch_support,
            "reversal_cost": point.component_maxima.reversal_cost,
            "bounded_progress": point.progress_maximum,
        },
        "objective_order": list(THEOREM_OBJECTIVES),
        "holds": point.holds,
        "regime": point.regime,
        "regime_reason": point.regime_reason,
        "joint_maximizers": [
            _evaluation_to_dict(item) for item in point.joint_maximizers[:8]
        ],
        "joint_maximizer_count": len(point.joint_maximizers),
    }


def _minimal_conditions_to_dict(
    report: MinimalConditionReport,
) -> dict[str, object]:
    return {
        "preserved_tradeoff_windows": [
            {
                "adversarial_delay": window.adversarial_delay,
                "start_budget": window.start_budget,
                "end_budget": window.end_budget,
                "regime": window.regime,
            }
            for window in report.preserved_tradeoff_windows
        ],
        "minimal_preserved_point": (
            _parameter_point_to_dict(report.minimal_preserved_point)
            if report.minimal_preserved_point
            else None
        ),
        "minimal_degenerate_failure": (
            _point_to_dict(report.minimal_degenerate_failure)
            if report.minimal_degenerate_failure
            else None
        ),
        "minimal_saturated_failure": (
            _point_to_dict(report.minimal_saturated_failure)
            if report.minimal_saturated_failure
            else None
        ),
        "minimal_collapse_failure": (
            _point_to_dict(report.minimal_collapse_failure)
            if report.minimal_collapse_failure
            else None
        ),
        "recommendation": report.recommendation,
    }


def _parameter_point_to_dict(point: ParameterPoint) -> dict[str, int]:
    return {
        "budget": point.budget,
        "adversarial_delay": point.adversarial_delay,
    }


def _evaluation_to_dict(evaluation: ProtocolEvaluation) -> dict[str, object]:
    return {
        "config": {
            "name": evaluation.config.name,
            "nodes": evaluation.config.nodes,
            "quorum": evaluation.config.quorum,
            "branches": evaluation.config.branches,
            "confirmations": evaluation.config.confirmations,
            "timeout_rounds": evaluation.config.timeout_rounds,
            "resource_cost": evaluation.config.resource_cost,
        },
        "d1": {
            "accessible_support": evaluation.d1.accessible_support,
            "holder_redundancy": evaluation.d1.holder_redundancy,
            "branch_support": evaluation.d1.branch_support,
            "reversal_cost": evaluation.d1.reversal_cost,
        },
        "bounded_progress": evaluation.progress_score,
        "safety_final": evaluation.safety_final,
        "live_under_delay": evaluation.live_under_delay,
        "economic_reversal_cost": evaluation.economic_reversal_cost,
    }
