"""T42: Local persistence and reconciliation split audit.

This module tests whether a finite record-finality model can separate two
observables that are easy to blur in relativity-facing prose:

  1. local persistence accumulation:
     irreversible local constraint formation along one node's history

  2. reconciliation delay:
     how late another node can access and compare those records

The model is deliberately finite and synthetic. It does not derive physical
proper time, does not replace relativity, and does not use metric proper time
as an input. The only claim tested here is structural: local accumulation
difference and reconciliation lag are independent axes in this toy system.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class LocalConstraintEvent:
    """One local event in a persistent node's history."""

    node_id: str
    local_index: int
    irreversible_delta: int
    label: str


@dataclass(frozen=True)
class PersistentNode:
    """A finite local history of irreversible constraint formation."""

    node_id: str
    description: str
    events: tuple[LocalConstraintEvent, ...]

    @property
    def event_count(self) -> int:
        return len(self.events)


@dataclass(frozen=True)
class RecordChannel:
    """A causal record channel between two persistent nodes.

    delay_events is measured in target-local event indices. It is simulator
    bookkeeping, not physical time.
    """

    source_id: str
    target_id: str
    delay_events: int
    noise: float = 0.0
    capacity: int | None = None


@dataclass(frozen=True)
class ComparisonEvent:
    """A target-local event where records from a source are compared."""

    name: str
    source_id: str
    target_id: str
    source_local_index: int
    target_local_index: int


@dataclass(frozen=True)
class ComparisonObservation:
    """Computed observables at one comparison event."""

    comparison_name: str
    source_id: str
    target_id: str
    source_local_index: int
    target_local_index: int
    source_total_accumulation: int
    target_total_accumulation: int
    source_visible_index: int
    source_visible_accumulation: int
    hidden_source_accumulation_due_to_delay: int
    reconciliation_lag_events: int
    propagation_delay_events: int
    local_accumulation_difference: int
    source_local_rate: float
    target_local_rate: float
    accumulation_difference_present: bool
    reconciliation_lag_present: bool
    classification: str


@dataclass(frozen=True)
class LocalPersistenceReconciliationSystem:
    """Finite system separating local accumulators from record channels."""

    name: str
    description: str
    nodes: tuple[PersistentNode, ...]
    channels: tuple[RecordChannel, ...]
    comparisons: tuple[ComparisonEvent, ...]

    def node(self, node_id: str) -> PersistentNode:
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        raise KeyError(f"unknown node_id: {node_id}")

    def channel(self, source_id: str, target_id: str) -> RecordChannel:
        for channel in self.channels:
            if channel.source_id == source_id and channel.target_id == target_id:
                return channel
        raise KeyError(f"unknown channel: {source_id}->{target_id}")


@dataclass(frozen=True)
class ScenarioResult:
    """One executable T42 witness."""

    name: str
    expected_classification: str
    observed_classification: str
    passed: bool
    observation: ComparisonObservation
    finding: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    """T42 hypothesis verdict."""

    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T42Result:
    """Full T42 analysis output."""

    scenarios: tuple[ScenarioResult, ...]
    all_witnesses_pass: bool
    independence_witnessed: bool
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    best_supported_hypothesis: str
    theorem: str
    boundary: str
    recommendation: str


def make_node(node_id: str, deltas: tuple[int, ...], description: str = "") -> PersistentNode:
    """Build a persistent node from local irreversible-delta values."""

    events = tuple(
        LocalConstraintEvent(
            node_id=node_id,
            local_index=i + 1,
            irreversible_delta=delta,
            label=f"{node_id}_e{i + 1}",
        )
        for i, delta in enumerate(deltas)
    )
    return PersistentNode(node_id=node_id, description=description, events=events)


def make_uniform_node(node_id: str, event_count: int, delta: int = 1) -> PersistentNode:
    """Build a node whose local persistence accumulator grows uniformly."""

    return make_node(
        node_id,
        tuple(delta for _ in range(event_count)),
        description=f"{event_count} local events with delta={delta}",
    )


def accumulation_until(node: PersistentNode, local_index: int) -> int:
    """Return local irreversible accumulation through local_index inclusive."""

    if local_index < 0:
        raise ValueError("local_index must be non-negative")
    if local_index > node.event_count:
        raise ValueError(
            f"local_index {local_index} exceeds event_count {node.event_count} "
            f"for node {node.node_id}"
        )
    return sum(event.irreversible_delta for event in node.events[:local_index])


def latest_visible_source_index(
    source_local_index: int,
    target_local_index: int,
    channel: RecordChannel,
) -> int:
    """Latest source index visible at target under channel delay."""

    visible = target_local_index - channel.delay_events
    return max(0, min(source_local_index, visible))


def classify_observation(accumulation_difference: int, reconciliation_lag: int) -> str:
    """Classify the pair of observables into one of the four T42 witnesses."""

    has_accumulation_difference = accumulation_difference != 0
    has_lag = reconciliation_lag > 0

    if not has_accumulation_difference and has_lag:
        return "delay_without_dilation"
    if has_accumulation_difference and not has_lag:
        return "dilation_like_accumulation_without_extra_delay"
    if has_accumulation_difference and has_lag:
        return "both_effects"
    return "null_case"


def observe_comparison(
    system: LocalPersistenceReconciliationSystem,
    comparison: ComparisonEvent,
) -> ComparisonObservation:
    """Compute local accumulation and reconciliation observables."""

    source = system.node(comparison.source_id)
    target = system.node(comparison.target_id)
    channel = system.channel(comparison.source_id, comparison.target_id)

    source_total = accumulation_until(source, comparison.source_local_index)
    target_total = accumulation_until(target, comparison.target_local_index)
    visible_index = latest_visible_source_index(
        comparison.source_local_index,
        comparison.target_local_index,
        channel,
    )
    visible_accumulation = accumulation_until(source, visible_index)
    hidden_accumulation = source_total - visible_accumulation
    lag = comparison.source_local_index - visible_index
    accumulation_difference = source_total - target_total
    source_rate = source_total / comparison.source_local_index
    target_rate = target_total / comparison.target_local_index
    classification = classify_observation(accumulation_difference, lag)

    return ComparisonObservation(
        comparison_name=comparison.name,
        source_id=comparison.source_id,
        target_id=comparison.target_id,
        source_local_index=comparison.source_local_index,
        target_local_index=comparison.target_local_index,
        source_total_accumulation=source_total,
        target_total_accumulation=target_total,
        source_visible_index=visible_index,
        source_visible_accumulation=visible_accumulation,
        hidden_source_accumulation_due_to_delay=hidden_accumulation,
        reconciliation_lag_events=lag,
        propagation_delay_events=channel.delay_events,
        local_accumulation_difference=accumulation_difference,
        source_local_rate=source_rate,
        target_local_rate=target_rate,
        accumulation_difference_present=accumulation_difference != 0,
        reconciliation_lag_present=lag > 0,
        classification=classification,
    )


def _single_comparison_system(
    name: str,
    description: str,
    source: PersistentNode,
    target: PersistentNode,
    delay_events: int,
) -> LocalPersistenceReconciliationSystem:
    """Build a two-node one-channel system for a T42 witness."""

    comparison = ComparisonEvent(
        name=f"{name}_comparison",
        source_id=source.node_id,
        target_id=target.node_id,
        source_local_index=source.event_count,
        target_local_index=target.event_count,
    )
    return LocalPersistenceReconciliationSystem(
        name=name,
        description=description,
        nodes=(source, target),
        channels=(
            RecordChannel(
                source_id=source.node_id,
                target_id=target.node_id,
                delay_events=delay_events,
                noise=0.0,
            ),
        ),
        comparisons=(comparison,),
    )


def delay_without_dilation_system() -> LocalPersistenceReconciliationSystem:
    """Same local accumulation, delayed source records."""

    source = make_uniform_node("clock_a", 10, 1)
    target = make_uniform_node("clock_b", 10, 1)
    return _single_comparison_system(
        name="delay_without_dilation",
        description=(
            "Both nodes accumulate ten irreversible local constraints, but "
            "clock_a records reach clock_b four target-local events late."
        ),
        source=source,
        target=target,
        delay_events=4,
    )


def dilation_like_without_delay_system() -> LocalPersistenceReconciliationSystem:
    """Different local accumulation, no extra reconciliation delay."""

    source = make_uniform_node("clock_fast", 10, 1)
    target = make_node(
        "clock_slow",
        (1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
        description="ten local events, six irreversible constraints",
    )
    return _single_comparison_system(
        name="dilation_like_without_delay",
        description=(
            "clock_fast accumulates ten constraints while clock_slow "
            "accumulates six; the comparison channel has zero extra delay."
        ),
        source=source,
        target=target,
        delay_events=0,
    )


def both_effects_system() -> LocalPersistenceReconciliationSystem:
    """Different local accumulation plus delayed source records."""

    source = make_uniform_node("clock_fast", 10, 1)
    target = make_node(
        "clock_slow",
        (1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
        description="ten local events, six irreversible constraints",
    )
    return _single_comparison_system(
        name="both_effects",
        description=(
            "Local accumulation differs and source records arrive three "
            "target-local events late."
        ),
        source=source,
        target=target,
        delay_events=3,
    )


def null_case_system() -> LocalPersistenceReconciliationSystem:
    """No local accumulation difference and no reconciliation delay."""

    source = make_uniform_node("clock_a", 10, 1)
    target = make_uniform_node("clock_b", 10, 1)
    return _single_comparison_system(
        name="null_case",
        description="Identical local accumulators and zero extra channel delay.",
        source=source,
        target=target,
        delay_events=0,
    )


def evaluate_scenario(
    system: LocalPersistenceReconciliationSystem,
    expected_classification: str,
) -> ScenarioResult:
    """Run one witness system and check its expected class."""

    observation = observe_comparison(system, system.comparisons[0])
    passed = observation.classification == expected_classification
    finding = (
        f"{system.name}: classification={observation.classification}, "
        f"accumulation_difference={observation.local_accumulation_difference}, "
        f"reconciliation_lag={observation.reconciliation_lag_events}"
    )
    return ScenarioResult(
        name=system.name,
        expected_classification=expected_classification,
        observed_classification=observation.classification,
        passed=passed,
        observation=observation,
        finding=finding,
    )


def evaluate_hypotheses(scenarios: tuple[ScenarioResult, ...]) -> tuple[HypothesisEvaluation, ...]:
    """Evaluate H0-H4 from the scenario witnesses."""

    all_pass = all(s.passed for s in scenarios)
    classes = frozenset(s.observed_classification for s in scenarios)
    expected_classes = frozenset(
        (
            "delay_without_dilation",
            "dilation_like_accumulation_without_extra_delay",
            "both_effects",
            "null_case",
        )
    )
    full_independence_grid = classes == expected_classes and all_pass

    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            claim=(
                "Proper time remains primitive physics; TaF only reconstructs "
                "accessible temporal order from records."
            ),
            status="retained_guardrail",
            evidence_for=(
                "T42 does not use metric proper time and does not derive it.",
                "The executable result is a finite separation, not a physics recovery.",
            ),
            evidence_against=(
                "The finite model shows a local accumulator worth studying as a proxy.",
            ),
            verdict=(
                "Retain H0 as the physics guardrail. T42 adds a toy split, not a "
                "replacement for proper time."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            claim=(
                "Local irreversible constraint accumulation is a useful finite "
                "proxy for proper-time-like behavior."
            ),
            status="partially_supported",
            evidence_for=(
                "The dilation-like witness changes local accumulation while delay is zero.",
                "The null and delay-only witnesses prevent the accumulator from collapsing into channel delay.",
            ),
            evidence_against=(
                "No mapping to Lorentzian interval or physical clock dynamics is provided.",
                "The local accumulator is hand-authored in the toy systems.",
            ),
            verdict=(
                "Supported only as a finite proxy. It is not yet a physical "
                "proper-time observable."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            claim=(
                "Network propagation explains reconciliation and synchronization "
                "lag, but not proper-time-like accumulation difference."
            ),
            status="best_supported",
            evidence_for=(
                "Delay without dilation witnesses lag with zero accumulation difference.",
                "Dilation-like without delay witnesses accumulation difference with zero lag.",
                "Both-effects and null witnesses complete the independence grid.",
            ),
            evidence_against=(
                "The result is finite and synthetic, not a physical measurement model.",
            ),
            verdict=(
                "Best supported. T42 cleanly separates reconciliation delay from "
                "local accumulation."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            claim=(
                "Proper time and local persistence are dual descriptions of one "
                "invariant under a declared mapping."
            ),
            status="not_earned",
            evidence_for=(
                "The local accumulator has the right shape to be compared with a local clock proxy.",
            ),
            evidence_against=(
                "No invariant-interval mapping is defined.",
                "No relativity recovery or physical clock experiment is modeled.",
            ),
            verdict=(
                "Not earned. H3 should wait for a recovery test that does not "
                "insert proper time as an input."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            claim="No clean mapping exists; the idea is only metaphorical.",
            status="rejected_for_finite_split",
            evidence_for=(
                "The physical mapping remains open.",
            ),
            evidence_against=(
                "The four synthetic witnesses define a clean finite separation.",
                "Local accumulation and reconciliation lag are independently variable.",
            ),
            verdict=(
                "Rejected at the finite-model level if all witnesses pass; still "
                "available against any stronger physics claim."
                if full_independence_grid
                else "Open because the finite witness grid did not fully pass."
            ),
        ),
    )


def run_t42_analysis() -> T42Result:
    """Run all T42 witness systems and return a structured result."""

    scenarios = (
        evaluate_scenario(delay_without_dilation_system(), "delay_without_dilation"),
        evaluate_scenario(
            dilation_like_without_delay_system(),
            "dilation_like_accumulation_without_extra_delay",
        ),
        evaluate_scenario(both_effects_system(), "both_effects"),
        evaluate_scenario(null_case_system(), "null_case"),
    )
    all_pass = all(s.passed for s in scenarios)
    classifications = frozenset(s.observed_classification for s in scenarios)
    independence_witnessed = all_pass and classifications == frozenset(
        (
            "delay_without_dilation",
            "dilation_like_accumulation_without_extra_delay",
            "both_effects",
            "null_case",
        )
    )
    hypotheses = evaluate_hypotheses(scenarios)
    return T42Result(
        scenarios=scenarios,
        all_witnesses_pass=all_pass,
        independence_witnessed=independence_witnessed,
        hypothesis_evaluations=hypotheses,
        best_supported_hypothesis="H2",
        theorem=(
            "Finite Accumulation/Reconciliation Independence Theorem: in the "
            "LocalPersistenceReconciliationSystem toy model, local accumulation "
            "difference and reconciliation lag are independent finite observables. "
            "All four combinations are witnessed: lag-only, accumulation-only, "
            "both, and neither."
        ),
        boundary=(
            "The theorem is finite and synthetic. It does not derive proper time, "
            "does not recover Lorentz transformations, and does not replace metric "
            "geometry. The simulator event index is bookkeeping only."
        ),
        recommendation=(
            "Promote T42 as a guardrail test track for relativity-facing language. "
            "Do not promote a physics claim. A future recovery test would need to "
            "map local persistence accumulation to a known proper-time pattern "
            "without inserting that pattern as an input."
        ),
    )


def t42_result_to_dict(result: T42Result) -> dict[str, Any]:
    """Serialize T42 result for JSON output."""

    return asdict(result)
