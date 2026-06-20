"""T128: minimal finite models that survive the arrow obstruction stack.

The goal is not to derive a thermodynamic arrow. It is to identify the first
finite fixtures that produce a strict directional scalar after T80, T82, T84,
T106, T110, and T122 have removed closed reversible and stationary stochastic
routes.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArrowState:
    name: str
    resource: int
    health: int
    sink_fill: int
    constructor_rank: int
    future_operations: frozenset[str]


@dataclass(frozen=True)
class ArrowTransition:
    source: str
    target: str
    probability: float
    label: str


@dataclass(frozen=True)
class ArrowModel:
    model_id: str
    name: str
    ingredient: str
    state_space: tuple[ArrowState, ...]
    transitions: tuple[ArrowTransition, ...]
    resource_accounting: str
    direction_candidate: str
    direction_values: tuple[tuple[str, int], ...]
    t122_assumptions_violated: tuple[str, ...]
    obstruction_status: str
    equivalence_note: str


@dataclass(frozen=True)
class ArrowAudit:
    model_id: str
    name: str
    ingredient: str
    state_names: tuple[str, ...]
    transition_rules: tuple[str, ...]
    resource_accounting: str
    direction_candidate: str
    direction_values: tuple[tuple[str, int], ...]
    future_operation_sizes: tuple[tuple[str, int], ...]
    has_directed_cycle: bool
    every_edge_strictly_increases: bool
    direction_survives: bool
    obstruction_status: str
    t122_assumptions_violated: tuple[str, ...]
    equivalence_note: str
    verdict: str


@dataclass(frozen=True)
class T128Result:
    audits: tuple[ArrowAudit, ...]
    strongest_surviving_minimal_model: str
    strongest_failed_model: str
    smallest_formal_ingredient_set: str
    smallest_nonstipulative_ingredient_set: str
    improved: str
    weakened: str
    claim_impact_recommendation: str
    open_blocker: str
    claim_ledger_update: str
    suggested_next: str


def closed_reversible_control() -> ArrowModel:
    ops = frozenset({"inspect_state", "apply_forward_step", "apply_inverse_step"})
    return ArrowModel(
        model_id="control_a_closed_reversible",
        name="Control A: closed reversible finite cycle",
        ingredient="none",
        state_space=(
            ArrowState("A", 0, 1, 0, 0, ops),
            ArrowState("B", 0, 1, 0, 1, ops),
            ArrowState("C", 0, 1, 0, 2, ops),
        ),
        transitions=(
            ArrowTransition("A", "B", 1.0, "permutation step"),
            ArrowTransition("B", "C", 1.0, "permutation step"),
            ArrowTransition("C", "A", 1.0, "permutation return"),
        ),
        resource_accounting="none: closed finite permutation, no sink or drawdown",
        direction_candidate="constructor_rank",
        direction_values=(("A", 0), ("B", 1), ("C", 2)),
        t122_assumptions_violated=(),
        obstruction_status=(
            "Killed by T110: a strict scalar monotone cannot live on a finite "
            "closed reversible orbit."
        ),
        equivalence_note="Baseline obstruction control.",
    )


def stationary_markov_control() -> ArrowModel:
    ops = frozenset({"inspect_state", "sample_next", "resample_previous"})
    return ArrowModel(
        model_id="control_b_stationary_markov",
        name="Control B: stationary finite Markov chain",
        ingredient="stationary stochasticity only",
        state_space=(
            ArrowState("low", 0, 1, 0, 0, ops),
            ArrowState("high", 0, 1, 0, 1, ops),
        ),
        transitions=(
            ArrowTransition("low", "low", 0.7, "stationary self transition"),
            ArrowTransition("low", "high", 0.3, "stationary upward transition"),
            ArrowTransition("high", "low", 0.3, "stationary downward transition"),
            ArrowTransition("high", "high", 0.7, "stationary self transition"),
        ),
        resource_accounting="none: pi=(1/2,1/2), P is time-independent",
        direction_candidate="state_height",
        direction_values=(("low", 0), ("high", 1)),
        t122_assumptions_violated=(),
        obstruction_status=(
            "Killed by T122: stationarity forces zero stationary-weighted "
            "expected drift, so upward drift is balanced by downward drift."
        ),
        equivalence_note="Baseline stationary stochastic obstruction control.",
    )


def resource_drawdown_model() -> ArrowModel:
    return ArrowModel(
        model_id="test_c_resource_drawdown",
        name="Test C: finite resource drawdown",
        ingredient="finite nonrenewed capacity",
        state_space=(
            _resource_state("R3", 3),
            _resource_state("R2", 2),
            _resource_state("R1", 1),
            _resource_state("R0", 0),
        ),
        transitions=(
            ArrowTransition("R3", "R2", 1.0, "consume one unit"),
            ArrowTransition("R2", "R1", 1.0, "consume one unit"),
            ArrowTransition("R1", "R0", 1.0, "consume one unit"),
        ),
        resource_accounting="finite stock r=3,2,1,0 with no refill",
        direction_candidate="drawdown = 3 - resource",
        direction_values=(("R3", 0), ("R2", 1), ("R1", 2), ("R0", 3)),
        t122_assumptions_violated=(
            "nonstationary resource drawdown",
            "transient support",
            "absorbing depleted boundary",
        ),
        obstruction_status=(
            "Survives only by leaving the T110/T122 assumptions: the model is "
            "not closed reversible and not stationary."
        ),
        equivalence_note=(
            "Smallest non-stipulative survivor in this audit: direction is the "
            "declared loss of finite future capacity."
        ),
    )


def maintenance_cost_model() -> ArrowModel:
    return ArrowModel(
        model_id="test_d_maintenance_cost",
        name="Test D: maintenance burden with finite repair budget",
        ingredient="maintenance burden plus finite resource",
        state_space=(
            ArrowState("M3", 3, 1, 0, 0, frozenset({"persist", "repair", "certify"})),
            ArrowState("M2", 2, 1, 0, 0, frozenset({"persist", "repair"})),
            ArrowState("M1", 1, 1, 0, 0, frozenset({"persist"})),
            ArrowState("M0", 0, 0, 0, 0, frozenset()),
        ),
        transitions=(
            ArrowTransition("M3", "M2", 1.0, "pay one maintenance unit"),
            ArrowTransition("M2", "M1", 1.0, "pay one maintenance unit"),
            ArrowTransition("M1", "M0", 1.0, "budget exhausted; persistence fails"),
        ),
        resource_accounting=(
            "maintenance consumes one unit from a finite repair budget per "
            "step; health persists only while budget remains"
        ),
        direction_candidate="lost future operations",
        direction_values=(("M3", 0), ("M2", 1), ("M1", 2), ("M0", 3)),
        t122_assumptions_violated=(
            "nonstationary resource drawdown",
            "transient support",
            "absorbing failed-maintenance boundary",
        ),
        obstruction_status=(
            "Survives, but not independently: maintenance creates direction "
            "only because a finite repair budget is being depleted."
        ),
        equivalence_note=(
            "Equivalent to resource drawdown plus a persistence task label. "
            "Maintenance without finite budget is not shown to produce a new arrow."
        ),
    )


def open_boundary_model() -> ArrowModel:
    return ArrowModel(
        model_id="test_e_open_boundary",
        name="Test E: finite open boundary with sink fill",
        ingredient="open source/sink boundary",
        state_space=(
            ArrowState("S0", 1, 1, 0, 0, frozenset({"emit", "verify_empty_sink", "challenge"})),
            ArrowState("S1", 1, 1, 1, 0, frozenset({"emit", "verify_sink_1"})),
            ArrowState("S2", 1, 1, 2, 0, frozenset({"emit"})),
            ArrowState("S3", 1, 1, 3, 0, frozenset()),
        ),
        transitions=(
            ArrowTransition("S0", "S1", 1.0, "export one record to sink"),
            ArrowTransition("S1", "S2", 1.0, "export one record to sink"),
            ArrowTransition("S2", "S3", 1.0, "sink reaches capacity"),
        ),
        resource_accounting=(
            "system resource is refilled by source; boundary sink capacity "
            "fills from 0 to 3"
        ),
        direction_candidate="sink_fill",
        direction_values=(("S0", 0), ("S1", 1), ("S2", 2), ("S3", 3)),
        t122_assumptions_violated=(
            "open boundary",
            "exported history",
            "finite sink capacity",
            "transient support",
        ),
        obstruction_status=(
            "Survives only when the boundary state is counted. If the sink is "
            "not part of the state, this reduces to omitted history."
        ),
        equivalence_note=(
            "Equivalent to resource drawdown in the environment: sink capacity "
            "is the resource being consumed."
        ),
    )


def constructor_restricted_model() -> ArrowModel:
    return ArrowModel(
        model_id="test_f_constructor_restricted",
        name="Test F: constructor-restricted transformations",
        ingredient="explicit impossible reverse transformations",
        state_space=(
            ArrowState("C0", 0, 1, 0, 0, frozenset({"construct_1", "construct_2"})),
            ArrowState("C1", 0, 1, 0, 1, frozenset({"construct_2"})),
            ArrowState("C2", 0, 1, 0, 2, frozenset()),
        ),
        transitions=(
            ArrowTransition("C0", "C1", 1.0, "allowed constructor step"),
            ArrowTransition("C1", "C2", 1.0, "allowed constructor step"),
        ),
        resource_accounting=(
            "none internal; reverse transformations are excluded by the "
            "admissibility relation"
        ),
        direction_candidate="constructor_rank",
        direction_values=(("C0", 0), ("C1", 1), ("C2", 2)),
        t122_assumptions_violated=(
            "excluded reverse channel",
            "constructor admissibility restriction",
        ),
        obstruction_status=(
            "Formally survives, but direction is imported by stipulating the "
            "admissible transformation preorder."
        ),
        equivalence_note=(
            "Smallest formal survivor if stipulation is allowed; weakest "
            "physical survivor because it names no substrate cost."
        ),
    )


def all_models() -> tuple[ArrowModel, ...]:
    return (
        closed_reversible_control(),
        stationary_markov_control(),
        resource_drawdown_model(),
        maintenance_cost_model(),
        open_boundary_model(),
        constructor_restricted_model(),
    )


def audit_model(model: ArrowModel) -> ArrowAudit:
    values = dict(model.direction_values)
    state_names = tuple(state.name for state in model.state_space)
    _validate_model(model, state_names, values)

    has_cycle = _has_directed_cycle(state_names, model.transitions)
    every_edge_strict = all(
        values[transition.target] > values[transition.source]
        for transition in model.transitions
        if transition.probability > 0.0
    )
    survives = bool(model.transitions) and every_edge_strict and not has_cycle
    return ArrowAudit(
        model_id=model.model_id,
        name=model.name,
        ingredient=model.ingredient,
        state_names=state_names,
        transition_rules=tuple(
            f"{transition.source}->{transition.target} p={transition.probability:g} ({transition.label})"
            for transition in model.transitions
        ),
        resource_accounting=model.resource_accounting,
        direction_candidate=model.direction_candidate,
        direction_values=model.direction_values,
        future_operation_sizes=tuple(
            (state.name, len(state.future_operations))
            for state in model.state_space
        ),
        has_directed_cycle=has_cycle,
        every_edge_strictly_increases=every_edge_strict,
        direction_survives=survives,
        obstruction_status=model.obstruction_status,
        t122_assumptions_violated=model.t122_assumptions_violated,
        equivalence_note=model.equivalence_note,
        verdict=_verdict(model, survives, has_cycle, every_edge_strict),
    )


def run_t128_analysis() -> T128Result:
    audits = tuple(audit_model(model) for model in all_models())
    by_id = {audit.model_id: audit for audit in audits}

    if by_id["control_a_closed_reversible"].direction_survives:
        raise AssertionError("closed reversible control must not produce an arrow")
    if by_id["control_b_stationary_markov"].direction_survives:
        raise AssertionError("stationary Markov control must not produce an arrow")
    for model_id in (
        "test_c_resource_drawdown",
        "test_d_maintenance_cost",
        "test_e_open_boundary",
        "test_f_constructor_restricted",
    ):
        if not by_id[model_id].direction_survives:
            raise AssertionError(f"{model_id} should produce a declared direction")

    return T128Result(
        audits=audits,
        strongest_surviving_minimal_model="test_c_resource_drawdown",
        strongest_failed_model="control_b_stationary_markov",
        smallest_formal_ingredient_set=(
            "constructor restriction alone, but only because the reverse "
            "transformation is excluded by definition"
        ),
        smallest_nonstipulative_ingredient_set=(
            "finite nonrenewed resource drawdown with an absorbing depleted "
            "boundary"
        ),
        improved=(
            "T128 identifies the first finite models that live after the "
            "obstruction stack: strict direction appears only when a resource, "
            "sink, boundary, or constructor restriction is explicitly included."
        ),
        weakened=(
            "Maintenance and open-boundary arrows do not emerge as independent "
            "ingredients in these fixtures. They reduce to resource drawdown, "
            "exported history, sink-capacity accounting, or stipulated "
            "constructor admissibility."
        ),
        claim_impact_recommendation=(
            "Preserve H7 only as a resource-accounting or constructor lemma. "
            "Do not promote it as a thermodynamic-arrow claim."
        ),
        open_blocker=(
            "The strongest survivor is still an accounting model. A physical "
            "upgrade would need a named free-energy or capacity variable and a "
            "comparison to standard stochastic thermodynamics."
        ),
        claim_ledger_update=(
            "H7 remains partially supported only in narrowed form. T128 shows "
            "that closed reversible and finite stationary Markov controls still "
            "fail, while the smallest non-stipulative finite survivor is "
            "explicit finite resource drawdown. Maintenance and open boundary "
            "survive only as resource/sink/export accounting; constructor "
            "restriction survives by stipulation."
        ),
        suggested_next=(
            "Build a thermodynamic calibration for the resource-drawdown "
            "survivor and test whether its direction is anything beyond "
            "ordinary free-energy or capacity accounting."
        ),
    )


def t128_result_to_dict(result: T128Result) -> dict[str, object]:
    return {
        "audits": [_audit_to_dict(audit) for audit in result.audits],
        "strongest_surviving_minimal_model": result.strongest_surviving_minimal_model,
        "strongest_failed_model": result.strongest_failed_model,
        "smallest_formal_ingredient_set": result.smallest_formal_ingredient_set,
        "smallest_nonstipulative_ingredient_set": result.smallest_nonstipulative_ingredient_set,
        "improved": result.improved,
        "weakened": result.weakened,
        "claim_impact_recommendation": result.claim_impact_recommendation,
        "open_blocker": result.open_blocker,
        "claim_ledger_update": result.claim_ledger_update,
        "suggested_next": result.suggested_next,
    }


def _resource_state(name: str, resource: int) -> ArrowState:
    operations_by_resource = {
        3: frozenset({"persist", "repair", "reconstruct"}),
        2: frozenset({"persist", "repair"}),
        1: frozenset({"persist"}),
        0: frozenset(),
    }
    return ArrowState(
        name=name,
        resource=resource,
        health=1 if resource > 0 else 0,
        sink_fill=0,
        constructor_rank=0,
        future_operations=operations_by_resource[resource],
    )


def _validate_model(
    model: ArrowModel,
    state_names: tuple[str, ...],
    values: dict[str, int],
) -> None:
    if len(set(state_names)) != len(state_names):
        raise ValueError(f"{model.model_id}: duplicate state names")
    if set(values) != set(state_names):
        raise ValueError(f"{model.model_id}: direction values must cover every state")
    states = set(state_names)
    for transition in model.transitions:
        if transition.source not in states or transition.target not in states:
            raise ValueError(f"{model.model_id}: transition references unknown state")
        if transition.probability <= 0.0 or transition.probability > 1.0:
            raise ValueError(f"{model.model_id}: transition probability out of range")


def _has_directed_cycle(
    state_names: tuple[str, ...],
    transitions: tuple[ArrowTransition, ...],
) -> bool:
    adjacency: dict[str, list[str]] = {name: [] for name in state_names}
    for transition in transitions:
        if transition.probability > 0.0:
            adjacency[transition.source].append(transition.target)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for child in adjacency[node]:
            if visit(child):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(name) for name in state_names)


def _verdict(
    model: ArrowModel,
    survives: bool,
    has_cycle: bool,
    every_edge_strict: bool,
) -> str:
    if survives:
        if model.model_id == "test_f_constructor_restricted":
            return "lives formally, but by stipulated admissibility restriction"
        return "lives only with explicit resource/boundary accounting"
    if has_cycle:
        return "dead: directed cycle blocks a strict scalar monotone"
    if not every_edge_strict:
        return "dead: at least one allowed transition does not increase the score"
    return "dead: no strict finite direction"


def _audit_to_dict(audit: ArrowAudit) -> dict[str, object]:
    return {
        "model_id": audit.model_id,
        "name": audit.name,
        "ingredient": audit.ingredient,
        "state_names": list(audit.state_names),
        "transition_rules": list(audit.transition_rules),
        "resource_accounting": audit.resource_accounting,
        "direction_candidate": audit.direction_candidate,
        "direction_values": [
            {"state": state, "value": value}
            for state, value in audit.direction_values
        ],
        "future_operation_sizes": [
            {"state": state, "available_operation_count": count}
            for state, count in audit.future_operation_sizes
        ],
        "has_directed_cycle": audit.has_directed_cycle,
        "every_edge_strictly_increases": audit.every_edge_strictly_increases,
        "direction_survives": audit.direction_survives,
        "obstruction_status": audit.obstruction_status,
        "t122_assumptions_violated": list(audit.t122_assumptions_violated),
        "equivalence_note": audit.equivalence_note,
        "verdict": audit.verdict,
    }
