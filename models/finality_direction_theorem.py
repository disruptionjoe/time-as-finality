"""T18: finality-induced temporal direction theorem.

This module tests a narrow constructor-style claim: if admissible
transformations are monotone in D1 finality, then strict finalization has an
intrinsic direction. The result is deliberately conditional and finite; it
does not derive the thermodynamic arrow or replace ordinary dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True, order=True)
class FinalityVector:
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

    @property
    def rank(self) -> int:
        return sum(self.as_tuple())

    def dominates(self, other: "FinalityVector") -> bool:
        return all(left >= right for left, right in zip(self.as_tuple(), other.as_tuple()))

    def strictly_dominates(self, other: "FinalityVector") -> bool:
        return self.dominates(other) and self.as_tuple() != other.as_tuple()

    def incomparable_with(self, other: "FinalityVector") -> bool:
        return not self.dominates(other) and not other.dominates(self)


@dataclass(frozen=True)
class FinalityState:
    name: str
    d1: FinalityVector
    thermodynamic_cost_proxy: int


@dataclass(frozen=True)
class Transformation:
    before: FinalityState
    after: FinalityState
    kind: str
    possible: bool
    explanation: str

    @property
    def reverse(self) -> "Transformation":
        return classify_transformation(self.after, self.before)


@dataclass(frozen=True)
class ArrowTheoremResult:
    theorem_name: str
    statement: str
    assumptions: tuple[str, ...]
    checked_states: int
    checked_transformations: int
    strict_finalization_edges: int
    impossible_transformations: int
    arrow_graph_acyclic: bool
    strict_edges_have_impossible_reverse: bool
    impossible_set_not_closed_under_reversal: bool
    partial_order_not_total: bool
    thermodynamic_divergence_witness: Transformation | None
    impossible_reversal_witness: Transformation | None
    incomparable_witness: tuple[FinalityState, FinalityState] | None
    holds: bool


def generate_finality_state_space(
    max_support: int = 3,
    max_reversal_cost: int = 6,
    max_thermodynamic_cost: int = 2,
) -> tuple[FinalityState, ...]:
    states: list[FinalityState] = []
    for support, redundancy, branch_support, reversal_cost, thermal_cost in product(
        range(max_support + 1),
        range(max_support + 1),
        range(max_support + 1),
        range(max_reversal_cost + 1),
        range(max_thermodynamic_cost + 1),
    ):
        d1 = FinalityVector(
            accessible_support=support,
            holder_redundancy=redundancy,
            branch_support=branch_support,
            reversal_cost=reversal_cost,
        )
        if not _is_well_formed(d1):
            continue
        states.append(
            FinalityState(
                name=f"s{support}-h{redundancy}-b{branch_support}-r{reversal_cost}-k{thermal_cost}",
                d1=d1,
                thermodynamic_cost_proxy=thermal_cost,
            )
        )
    return tuple(states)


def classify_transformation(before: FinalityState, after: FinalityState) -> Transformation:
    if after.d1 == before.d1:
        return Transformation(
            before=before,
            after=after,
            kind="finality_neutral",
            possible=True,
            explanation="D1 is unchanged, so the transformation has no finality direction.",
        )
    if after.d1.strictly_dominates(before.d1):
        return Transformation(
            before=before,
            after=after,
            kind="strict_finalization",
            possible=True,
            explanation="Every D1 dimension is preserved or increased, with at least one strict increase.",
        )
    if before.d1.strictly_dominates(after.d1):
        return Transformation(
            before=before,
            after=after,
            kind="strict_definalization",
            possible=False,
            explanation="The transformation decreases finalized record structure.",
        )
    return Transformation(
        before=before,
        after=after,
        kind="mixed_tradeoff",
        possible=False,
        explanation="At least one D1 dimension decreases, so this is not admissible in one step.",
    )


def verify_arrow_theorem(
    states: tuple[FinalityState, ...] | None = None,
) -> ArrowTheoremResult:
    checked_states = states or generate_finality_state_space()
    transformations = tuple(
        classify_transformation(before, after)
        for before in checked_states
        for after in checked_states
        if before != after
    )
    strict_edges = tuple(
        transformation
        for transformation in transformations
        if transformation.kind == "strict_finalization"
    )
    impossible = tuple(
        transformation for transformation in transformations if not transformation.possible
    )
    acyclic = _strict_finalization_graph_is_acyclic(checked_states, strict_edges)
    strict_reverses_impossible = all(
        not transformation.reverse.possible for transformation in strict_edges
    )
    nonclosed_witness = next(
        (
            transformation
            for transformation in impossible
            if transformation.reverse.possible
        ),
        None,
    )
    thermal_witness = next(
        (
            transformation
            for transformation in strict_edges
            if (
                transformation.before.d1.rank > 0
                and
                transformation.after.thermodynamic_cost_proxy
                <= transformation.before.thermodynamic_cost_proxy
            )
        ),
        None,
    )
    incomparable = _find_incomparable_witness(checked_states)
    impossible_reversal = next(
        (
            transformation.reverse
            for transformation in strict_edges
            if not transformation.reverse.possible
        ),
        None,
    )
    holds = (
        bool(strict_edges)
        and acyclic
        and strict_reverses_impossible
        and nonclosed_witness is not None
        and incomparable is not None
    )
    return ArrowTheoremResult(
        theorem_name="T18 finality-induced direction theorem",
        statement=(
            "In a finite constructor model where admissible transformations are "
            "D1-monotone, strict finalization induces an acyclic partial order; "
            "the reverse of every strict finalization is impossible."
        ),
        assumptions=(
            "States carry a D1 vector: support, redundancy, branch support, and reversal cost.",
            "A transformation is admissible only if no D1 dimension decreases.",
            "Strict finalization means at least one D1 dimension increases while none decrease.",
            "The theorem derives a finality direction, not coordinate time, proper time, or entropy increase.",
            "The thermodynamic-cost proxy is tracked separately and is not used to orient transformations.",
        ),
        checked_states=len(checked_states),
        checked_transformations=len(transformations),
        strict_finalization_edges=len(strict_edges),
        impossible_transformations=len(impossible),
        arrow_graph_acyclic=acyclic,
        strict_edges_have_impossible_reverse=strict_reverses_impossible,
        impossible_set_not_closed_under_reversal=nonclosed_witness is not None,
        partial_order_not_total=incomparable is not None,
        thermodynamic_divergence_witness=thermal_witness,
        impossible_reversal_witness=impossible_reversal,
        incomparable_witness=incomparable,
        holds=holds,
    )


def run_t18_analysis() -> dict[str, object]:
    result = verify_arrow_theorem()
    return {
        "theorem": {
            "name": result.theorem_name,
            "statement": result.statement,
            "assumptions": list(result.assumptions),
            "holds": result.holds,
        },
        "search": {
            "checked_states": result.checked_states,
            "checked_transformations": result.checked_transformations,
            "strict_finalization_edges": result.strict_finalization_edges,
            "impossible_transformations": result.impossible_transformations,
        },
        "checks": {
            "arrow_graph_acyclic": result.arrow_graph_acyclic,
            "strict_edges_have_impossible_reverse": result.strict_edges_have_impossible_reverse,
            "impossible_set_not_closed_under_reversal": result.impossible_set_not_closed_under_reversal,
            "partial_order_not_total": result.partial_order_not_total,
        },
        "witnesses": {
            "thermodynamic_divergence": _transformation_to_dict(
                result.thermodynamic_divergence_witness
            ),
            "impossible_reversal": _transformation_to_dict(
                result.impossible_reversal_witness
            ),
            "incomparable_pair": (
                [
                    _state_to_dict(result.incomparable_witness[0]),
                    _state_to_dict(result.incomparable_witness[1]),
                ]
                if result.incomparable_witness
                else None
            ),
        },
        "verdict": {
            "conditional_finality_arrow_derived": result.holds,
            "does_not_derive_thermodynamic_arrow": True,
            "does_not_replace_proper_time": True,
            "arrow_is_partial_not_total": result.partial_order_not_total,
        },
    }


def _is_well_formed(d1: FinalityVector) -> bool:
    if d1.accessible_support == 0:
        return d1.as_tuple() == (0, 0, 0, 0)
    return (
        0 <= d1.holder_redundancy <= d1.accessible_support
        and 0 <= d1.branch_support <= d1.accessible_support
        and d1.reversal_cost >= d1.accessible_support
    )


def _strict_finalization_graph_is_acyclic(
    states: tuple[FinalityState, ...],
    edges: tuple[Transformation, ...],
) -> bool:
    adjacency = {state: [] for state in states}
    for edge in edges:
        adjacency[edge.before].append(edge.after)

    visiting: set[FinalityState] = set()
    visited: set[FinalityState] = set()

    def visit(state: FinalityState) -> bool:
        if state in visiting:
            return False
        if state in visited:
            return True
        visiting.add(state)
        for child in adjacency[state]:
            if not visit(child):
                return False
        visiting.remove(state)
        visited.add(state)
        return True

    return all(visit(state) for state in states)


def _find_incomparable_witness(
    states: tuple[FinalityState, ...],
) -> tuple[FinalityState, FinalityState] | None:
    for left in states:
        for right in states:
            if left.name >= right.name:
                continue
            if left.d1.incomparable_with(right.d1):
                return left, right
    return None


def _state_to_dict(state: FinalityState) -> dict[str, object]:
    return {
        "name": state.name,
        "d1": state.d1.as_tuple(),
        "d1_rank": state.d1.rank,
        "thermodynamic_cost_proxy": state.thermodynamic_cost_proxy,
    }


def _transformation_to_dict(
    transformation: Transformation | None,
) -> dict[str, object] | None:
    if transformation is None:
        return None
    return {
        "before": _state_to_dict(transformation.before),
        "after": _state_to_dict(transformation.after),
        "kind": transformation.kind,
        "possible": transformation.possible,
        "explanation": transformation.explanation,
    }
