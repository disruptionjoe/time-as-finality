"""T17: consensus finality crosswalk.

This lab compares D1-style record finality with distributed-systems finality
definitions. It deliberately treats consensus as an analogy and formal
collapse map, not as a claim that physics literally runs a protocol.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True, order=True)
class D1Vector:
    accessible_support: int
    holder_redundancy: int
    branch_support: int
    reversal_cost: int

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (
            self.accessible_support,
            self.holder_redundancy,
            self.branch_support,
            self.reversal_cost,
        )

    def dominates(self, other: "D1Vector") -> bool:
        return all(left >= right for left, right in zip(self.as_tuple(), other.as_tuple()))

    def strictly_dominates(self, other: "D1Vector") -> bool:
        return self.dominates(other) and self.as_tuple() != other.as_tuple()


@dataclass(frozen=True)
class ProtocolConfig:
    name: str
    nodes: int
    quorum: int
    branches: int
    confirmations: int
    timeout_rounds: int
    budget: int

    @property
    def resource_cost(self) -> int:
        return self.nodes + self.branches + self.confirmations + self.timeout_rounds


@dataclass(frozen=True)
class ProtocolEvaluation:
    config: ProtocolConfig
    d1: D1Vector
    safety_final: bool
    live_under_delay: bool
    economic_reversal_cost: int
    quorum_margin: int

    def distributed_signature(self) -> tuple[bool, bool, int]:
        return (
            self.safety_final,
            self.live_under_delay,
            self.economic_reversal_cost,
        )


@dataclass(frozen=True)
class CollapseMap:
    name: str
    distributed_definition: str
    d1_dimensions_used: tuple[str, ...]
    d1_dimensions_collapsed: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class DivergenceWitness:
    kind: str
    left: ProtocolEvaluation
    right: ProtocolEvaluation
    explanation: str


@dataclass(frozen=True)
class ImpossibilityWitness:
    budget: int
    component_maxima: D1Vector
    pareto_frontier: tuple[ProtocolEvaluation, ...]
    witness: str


@dataclass(frozen=True)
class CrosswalkResult:
    collapse_maps: tuple[CollapseMap, ...]
    evaluations: tuple[ProtocolEvaluation, ...]
    divergence_witnesses: tuple[DivergenceWitness, ...]
    impossibility_witness: ImpossibilityWitness


D1_DIMENSIONS = (
    "accessible_support",
    "holder_redundancy",
    "branch_support",
    "reversal_cost",
)


def evaluate_config(config: ProtocolConfig, adversarial_delay: int = 2) -> ProtocolEvaluation:
    if config.quorum > config.nodes:
        raise ValueError("quorum cannot exceed node count")
    if config.resource_cost > config.budget:
        raise ValueError("configuration exceeds its resource budget")

    reachable_messages = min(config.nodes, config.timeout_rounds)
    accessible_support = min(config.quorum, reachable_messages)
    holder_redundancy = accessible_support
    branch_support = min(config.branches, accessible_support)
    reversal_cost = accessible_support * config.confirmations
    quorum_margin = config.quorum - (config.nodes // 2)
    safety_final = quorum_margin > 0 and accessible_support >= config.quorum
    live_under_delay = config.timeout_rounds <= adversarial_delay and accessible_support >= config.quorum
    return ProtocolEvaluation(
        config=config,
        d1=D1Vector(
            accessible_support=accessible_support,
            holder_redundancy=holder_redundancy,
            branch_support=branch_support,
            reversal_cost=reversal_cost,
        ),
        safety_final=safety_final,
        live_under_delay=live_under_delay,
        economic_reversal_cost=reversal_cost,
        quorum_margin=quorum_margin,
    )


def collapse_maps() -> tuple[CollapseMap, ...]:
    return (
        CollapseMap(
            name="safety_finality",
            distributed_definition="a decided value cannot be contradicted by another quorum decision",
            d1_dimensions_used=("accessible_support", "holder_redundancy", "reversal_cost"),
            d1_dimensions_collapsed=("branch_support",),
            verdict="partial collapse: safety ignores independent branch structure",
        ),
        CollapseMap(
            name="liveness_finality",
            distributed_definition="a value becomes decided within a bounded delay assumption",
            d1_dimensions_used=("accessible_support",),
            d1_dimensions_collapsed=("holder_redundancy", "branch_support", "reversal_cost"),
            verdict="not a D1 dimension: liveness is a protocol progress condition",
        ),
        CollapseMap(
            name="economic_finality",
            distributed_definition="reversal is expensive enough to be irrational or infeasible",
            d1_dimensions_used=("reversal_cost",),
            d1_dimensions_collapsed=("accessible_support", "holder_redundancy", "branch_support"),
            verdict="strict collapse: economic finality keeps only one D1 dimension",
        ),
    )


def generate_protocol_space(budget: int = 10) -> tuple[ProtocolEvaluation, ...]:
    evaluations = []
    for nodes, branches, confirmations, timeout_rounds in product(
        range(1, 7),
        range(1, 5),
        range(1, 5),
        range(1, 5),
    ):
        for quorum in range(1, nodes + 1):
            config = ProtocolConfig(
                name=f"n{nodes}-q{quorum}-b{branches}-c{confirmations}-t{timeout_rounds}",
                nodes=nodes,
                quorum=quorum,
                branches=branches,
                confirmations=confirmations,
                timeout_rounds=timeout_rounds,
                budget=budget,
            )
            if config.resource_cost <= budget:
                evaluations.append(evaluate_config(config))
    return tuple(evaluations)


def find_divergence_witnesses(
    evaluations: tuple[ProtocolEvaluation, ...],
) -> tuple[DivergenceWitness, ...]:
    witnesses: list[DivergenceWitness] = []

    for left, right in _ordered_pairs(evaluations):
        if (
            left.safety_final
            and right.safety_final
            and left.d1.branch_support != right.d1.branch_support
        ):
            witnesses.append(
                DivergenceWitness(
                    kind="same_safety_different_branch_finality",
                    left=left,
                    right=right,
                    explanation="safety finality agrees, but D1 distinguishes independent branch support",
                )
            )
            break

    for left, right in _ordered_pairs(evaluations):
        if (
            left.economic_reversal_cost == right.economic_reversal_cost
            and left.d1.as_tuple() != right.d1.as_tuple()
        ):
            witnesses.append(
                DivergenceWitness(
                    kind="same_economic_cost_different_d1_profile",
                    left=left,
                    right=right,
                    explanation="economic finality agrees, but support/redundancy/branch structure differ",
                )
            )
            break

    for left, right in _ordered_pairs(evaluations):
        if (
            left.distributed_signature() == right.distributed_signature()
            and left.d1.as_tuple() != right.d1.as_tuple()
        ):
            witnesses.append(
                DivergenceWitness(
                    kind="same_distributed_signature_different_d1_profile",
                    left=left,
                    right=right,
                    explanation="standard distributed summary collapses distinctions retained by D1",
                )
            )
            break

    return tuple(witnesses)


def impossibility_witness(
    evaluations: tuple[ProtocolEvaluation, ...],
    budget: int = 10,
) -> ImpossibilityWitness:
    maxima = D1Vector(
        accessible_support=max(evaluation.d1.accessible_support for evaluation in evaluations),
        holder_redundancy=max(evaluation.d1.holder_redundancy for evaluation in evaluations),
        branch_support=max(evaluation.d1.branch_support for evaluation in evaluations),
        reversal_cost=max(evaluation.d1.reversal_cost for evaluation in evaluations),
    )
    maximizers = [
        evaluation for evaluation in evaluations if evaluation.d1.as_tuple() == maxima.as_tuple()
    ]
    frontier = tuple(
        evaluation
        for evaluation in evaluations
        if not any(other.d1.strictly_dominates(evaluation.d1) for other in evaluations)
    )
    witness = (
        "no admissible configuration reaches all component maxima"
        if not maximizers
        else "a configuration reaches all component maxima"
    )
    return ImpossibilityWitness(
        budget=budget,
        component_maxima=maxima,
        pareto_frontier=tuple(sorted(frontier, key=lambda item: item.config.name)),
        witness=witness,
    )


def run_crosswalk_analysis(budget: int = 10) -> CrosswalkResult:
    evaluations = generate_protocol_space(budget)
    return CrosswalkResult(
        collapse_maps=collapse_maps(),
        evaluations=evaluations,
        divergence_witnesses=find_divergence_witnesses(evaluations),
        impossibility_witness=impossibility_witness(evaluations, budget),
    )


def run_t17_analysis() -> dict[str, object]:
    result = run_crosswalk_analysis()
    return {
        "collapse_maps": [
            {
                "name": item.name,
                "distributed_definition": item.distributed_definition,
                "d1_dimensions_used": list(item.d1_dimensions_used),
                "d1_dimensions_collapsed": list(item.d1_dimensions_collapsed),
                "verdict": item.verdict,
            }
            for item in result.collapse_maps
        ],
        "search": {
            "configurations": len(result.evaluations),
            "safety_final_count": sum(item.safety_final for item in result.evaluations),
            "live_under_delay_count": sum(item.live_under_delay for item in result.evaluations),
            "pareto_frontier_count": len(result.impossibility_witness.pareto_frontier),
        },
        "divergence_witnesses": [
            {
                "kind": witness.kind,
                "left": _evaluation_to_dict(witness.left),
                "right": _evaluation_to_dict(witness.right),
                "explanation": witness.explanation,
            }
            for witness in result.divergence_witnesses
        ],
        "impossibility_witness": {
            "budget": result.impossibility_witness.budget,
            "component_maxima": result.impossibility_witness.component_maxima.as_tuple(),
            "witness": result.impossibility_witness.witness,
            "frontier_examples": [
                _evaluation_to_dict(item)
                for item in result.impossibility_witness.pareto_frontier[:8]
            ],
        },
        "verdict": {
            "distributed_finality_is_safe_analogy": True,
            "d1_is_more_expressive_than_standard_distributed_signature": True,
            "liveness_is_not_a_d1_dimension": True,
            "bounded_impossibility_witness_found": (
                result.impossibility_witness.witness
                == "no admissible configuration reaches all component maxima"
            ),
            "physics_not_reduced_to_protocol": True,
        },
    }


def _ordered_pairs(
    evaluations: tuple[ProtocolEvaluation, ...],
) -> tuple[tuple[ProtocolEvaluation, ProtocolEvaluation], ...]:
    return tuple(
        (left, right)
        for left in evaluations
        for right in evaluations
        if left.config.name < right.config.name
    )


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
        "d1": evaluation.d1.as_tuple(),
        "safety_final": evaluation.safety_final,
        "live_under_delay": evaluation.live_under_delay,
        "economic_reversal_cost": evaluation.economic_reversal_cost,
        "quorum_margin": evaluation.quorum_margin,
    }
