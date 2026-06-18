"""T46: Open causal scarcity and closed synchronization boundary.

This module adds a finite RecordAccessSystem sidecar to the T42-T44 local
persistence work. It compares two scarcity regimes for finalized records:

  1. open causal scarcity:
     first access is determined by propagation delay from a record generator

  2. closed synchronization scarcity:
     accepted order is determined by membership, bounded uncertainty, and a
     commit rule inside a controlled boundary

The model is deliberately finite and synthetic. It does not model market
microstructure, does not implement Spanner, does not derive relativity, and
does not claim a physical measurement theory.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from heapq import heappop, heappush
from typing import Any


@dataclass(frozen=True)
class RecordNode:
    """A finite node that can generate, hold, or observe records."""

    node_id: str
    role: str
    member: bool
    description: str


@dataclass(frozen=True)
class PropagationEdge:
    """Directed propagation channel with finite non-negative delay."""

    source_id: str
    target_id: str
    delay: int
    medium: str
    description: str = ""


@dataclass(frozen=True)
class RecordEvent:
    """A generated record candidate before any observer-specific access."""

    event_id: str
    source_id: str
    generated_at: int
    payload: str
    event_kind: str


@dataclass(frozen=True)
class AccessObservation:
    """One observer's access to one record event."""

    observer_id: str
    event_id: str
    arrival_time: int
    path_delay: int
    inside_boundary: bool
    access_mode: str


@dataclass(frozen=True)
class FinalityGradientPoint:
    """Open-system advantage induced by record arrival time."""

    observer_id: str
    arrival_time: int
    access_rank: int
    advantage_over_slowest: int
    scarcity_axis: str


@dataclass(frozen=True)
class OpenCausalScarcityResult:
    """Finite witness for open causal scarcity."""

    system_name: str
    event_id: str
    observations: tuple[AccessObservation, ...]
    first_access_order: tuple[str, ...]
    gradient: tuple[FinalityGradientPoint, ...]
    proximity_advantage: int
    proximity_driven: bool
    finding: str


@dataclass(frozen=True)
class SynchronizationBoundary:
    """Closed-system synchronization boundary."""

    boundary_id: str
    member_ids: tuple[str, ...]
    quorum: int
    uncertainty_bound: int
    rule: str
    description: str


@dataclass(frozen=True)
class TransactionEvent:
    """Record event whose accepted order is assigned by a closed boundary."""

    event_id: str
    coordinator_id: str
    generated_at: int
    commit_timestamp: int
    quorum_delay: int
    payload: str


@dataclass(frozen=True)
class CommitObservation:
    """Observed order/access data for one closed-boundary transaction."""

    event_id: str
    coordinator_id: str
    generated_at: int
    commit_timestamp: int
    quorum_delay: int
    commit_visible_inside_at: int
    raw_external_arrival_at: int
    commit_record_external_arrival_at: int
    commit_wait_cost: int
    external_path_delay: int


@dataclass(frozen=True)
class ClosedSynchronizationResult:
    """Finite witness for closed synchronization scarcity."""

    system_name: str
    boundary: SynchronizationBoundary
    transactions: tuple[CommitObservation, ...]
    internal_commit_order: tuple[str, ...]
    outside_raw_arrival_order: tuple[str, ...]
    outside_commit_record_arrival_order: tuple[str, ...]
    outside_reconstruction_time: int
    raw_order_differs_from_commit_order: bool
    membership_boundary_active: bool
    propagation_constraints_respected: bool
    synchronization_cost_total: int
    finding: str


@dataclass(frozen=True)
class BoundaryComparison:
    """Comparison between open and closed scarcity regimes."""

    open_scarcity_axis: str
    closed_scarcity_axis: str
    shared_record_access_frontier: bool
    synchronization_relocates_scarcity: bool
    outside_observer_lag: int
    statement: str


@dataclass(frozen=True)
class MeasurementProjectionBoundary:
    """Conservative measurement-projection table.

    This is not a full PO1 proof and does not assume the dimensionality of the
    richer layer. It records what a T46-style access boundary would need to
    name before any stronger quantum claim is earned.
    """

    source_layer: str
    target_layer: str
    morphism_name: str
    preserved_structure: tuple[str, ...]
    forgotten_structure: tuple[str, ...]
    accessible_record_condition: str
    record_layer_propagation_constraint: str
    assumes_fourteen_dimensional_y: bool
    po1_status: str
    caution: str


@dataclass(frozen=True)
class HypothesisEvaluation:
    """T46 hypothesis verdict."""

    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T46Result:
    """Full T46 result."""

    open_causal: OpenCausalScarcityResult
    closed_synchronization: ClosedSynchronizationResult
    comparison: BoundaryComparison
    measurement_projection: MeasurementProjectionBoundary
    hypothesis_evaluations: tuple[HypothesisEvaluation, ...]
    best_supported_hypothesis: str
    theorem: str
    boundary: str
    recommendation: str
    named_claim_recommendation: str


@dataclass(frozen=True)
class RecordAccessSystem:
    """Finite propagation graph with optional closed synchronization boundary."""

    name: str
    description: str
    nodes: tuple[RecordNode, ...]
    edges: tuple[PropagationEdge, ...]
    events: tuple[RecordEvent, ...]
    boundary: SynchronizationBoundary | None = None

    def node(self, node_id: str) -> RecordNode:
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        raise KeyError(f"unknown node_id: {node_id}")

    def event(self, event_id: str) -> RecordEvent:
        for event in self.events:
            if event.event_id == event_id:
                return event
        raise KeyError(f"unknown event_id: {event_id}")

    def outgoing(self, node_id: str) -> tuple[PropagationEdge, ...]:
        return tuple(edge for edge in self.edges if edge.source_id == node_id)

    def shortest_delays_from(self, source_id: str) -> dict[str, int]:
        """Dijkstra shortest propagation delay from one source node."""

        self.node(source_id)
        distances: dict[str, int] = {source_id: 0}
        heap: list[tuple[int, str]] = [(0, source_id)]

        while heap:
            current_delay, node_id = heappop(heap)
            if current_delay != distances[node_id]:
                continue
            for edge in self.outgoing(node_id):
                if edge.delay < 0:
                    raise ValueError("edge delays must be non-negative")
                candidate = current_delay + edge.delay
                if candidate < distances.get(edge.target_id, 10**18):
                    distances[edge.target_id] = candidate
                    heappush(heap, (candidate, edge.target_id))

        return distances

    def arrival_time(self, event_id: str, observer_id: str) -> int:
        event = self.event(event_id)
        distances = self.shortest_delays_from(event.source_id)
        if observer_id not in distances:
            raise ValueError(f"{observer_id} is not reachable from {event.source_id}")
        return event.generated_at + distances[observer_id]


def nyse_style_open_system() -> RecordAccessSystem:
    """Build an abstract NYSE-style open propagation witness."""

    nodes = (
        RecordNode(
            "exchange_engine",
            "record_generator",
            False,
            "Market-data source. The model abstracts from actual exchange internals.",
        ),
        RecordNode(
            "colocated_rack",
            "observer",
            False,
            "Observer with a very short path to the record source.",
        ),
        RecordNode(
            "metro_pop",
            "observer",
            False,
            "Observer connected through a regional low-latency path.",
        ),
        RecordNode(
            "remote_region",
            "observer",
            False,
            "Observer connected over a much longer path.",
        ),
    )
    edges = (
        PropagationEdge(
            "exchange_engine",
            "colocated_rack",
            1,
            "local_link",
            "Finite local propagation delay.",
        ),
        PropagationEdge(
            "exchange_engine",
            "metro_pop",
            75,
            "regional_link",
            "Regional path delay in abstract units.",
        ),
        PropagationEdge(
            "exchange_engine",
            "remote_region",
            750,
            "wide_area_link",
            "Wide-area path delay in abstract units.",
        ),
    )
    events = (
        RecordEvent(
            "quote_update_001",
            "exchange_engine",
            0,
            "price update",
            "market_data",
        ),
    )
    return RecordAccessSystem(
        name="nyse_style_open_causal_scarcity",
        description=(
            "Abstract market-data propagation witness: observers receive the "
            "same generated record at different times because their paths from "
            "the source have different finite delays."
        ),
        nodes=nodes,
        edges=edges,
        events=events,
    )


def evaluate_open_causal_scarcity(
    system: RecordAccessSystem | None = None,
) -> OpenCausalScarcityResult:
    """Evaluate first-access advantage in an open propagation system."""

    if system is None:
        system = nyse_style_open_system()
    event = system.events[0]
    observers = tuple(node for node in system.nodes if node.node_id != event.source_id)
    observations = tuple(
        AccessObservation(
            observer_id=node.node_id,
            event_id=event.event_id,
            arrival_time=system.arrival_time(event.event_id, node.node_id),
            path_delay=system.shortest_delays_from(event.source_id)[node.node_id],
            inside_boundary=False,
            access_mode="causal_arrival",
        )
        for node in observers
    )
    ordered = tuple(sorted(observations, key=lambda item: (item.arrival_time, item.observer_id)))
    slowest = max(item.arrival_time for item in observations)
    gradient = tuple(
        FinalityGradientPoint(
            observer_id=item.observer_id,
            arrival_time=item.arrival_time,
            access_rank=index + 1,
            advantage_over_slowest=slowest - item.arrival_time,
            scarcity_axis="causal_proximity",
        )
        for index, item in enumerate(ordered)
    )
    proximity_driven = tuple(item.observer_id for item in ordered) == (
        "colocated_rack",
        "metro_pop",
        "remote_region",
    )
    proximity_advantage = slowest - ordered[0].arrival_time
    finding = (
        "Open causal scarcity witnessed: first access follows finite path delay "
        f"from the generating node; advantage={proximity_advantage} abstract units."
    )
    return OpenCausalScarcityResult(
        system_name=system.name,
        event_id=event.event_id,
        observations=observations,
        first_access_order=tuple(item.observer_id for item in ordered),
        gradient=gradient,
        proximity_advantage=proximity_advantage,
        proximity_driven=proximity_driven,
        finding=finding,
    )


def spanner_style_closed_system() -> tuple[RecordAccessSystem, tuple[TransactionEvent, ...]]:
    """Build an abstract TrueTime-style closed synchronization witness."""

    boundary = SynchronizationBoundary(
        boundary_id="synchronized_commit_boundary",
        member_ids=("west_replica", "east_replica", "central_replica"),
        quorum=2,
        uncertainty_bound=5,
        rule="commit_timestamp_plus_uncertainty_wait",
        description=(
            "Finite abstraction of a bounded-uncertainty commit substrate. It "
            "models membership, quorum, timestamp order, and commit wait only."
        ),
    )
    nodes = (
        RecordNode("west_replica", "replica", True, "Closed-boundary member."),
        RecordNode("east_replica", "replica", True, "Closed-boundary member."),
        RecordNode("central_replica", "replica", True, "Closed-boundary member."),
        RecordNode(
            "outside_client",
            "external_observer",
            False,
            "Observer outside the synchronized commit boundary.",
        ),
    )
    edges = (
        PropagationEdge("west_replica", "central_replica", 20, "member_link"),
        PropagationEdge("central_replica", "west_replica", 20, "member_link"),
        PropagationEdge("east_replica", "central_replica", 20, "member_link"),
        PropagationEdge("central_replica", "east_replica", 20, "member_link"),
        PropagationEdge("west_replica", "east_replica", 40, "member_link"),
        PropagationEdge("east_replica", "west_replica", 40, "member_link"),
        PropagationEdge("west_replica", "outside_client", 90, "external_link"),
        PropagationEdge("east_replica", "outside_client", 5, "external_link"),
        PropagationEdge("central_replica", "outside_client", 25, "external_link"),
    )
    events = (
        RecordEvent("tx_west", "west_replica", 0, "write A", "transaction"),
        RecordEvent("tx_east", "east_replica", 4, "write B", "transaction"),
    )
    transactions = (
        TransactionEvent(
            event_id="tx_west",
            coordinator_id="west_replica",
            generated_at=0,
            commit_timestamp=10,
            quorum_delay=12,
            payload="write A",
        ),
        TransactionEvent(
            event_id="tx_east",
            coordinator_id="east_replica",
            generated_at=4,
            commit_timestamp=20,
            quorum_delay=8,
            payload="write B",
        ),
    )
    system = RecordAccessSystem(
        name="spanner_style_closed_synchronization_boundary",
        description=(
            "Abstract closed commit-boundary witness: internal order is assigned "
            "by commit timestamps plus bounded uncertainty, while outside raw "
            "arrival can follow a different path-delay order."
        ),
        nodes=nodes,
        edges=edges,
        events=events,
        boundary=boundary,
    )
    return system, transactions


def commit_visible_inside_at(
    transaction: TransactionEvent,
    boundary: SynchronizationBoundary,
) -> int:
    """Return inside-visible commit time under bounded uncertainty."""

    quorum_ready = transaction.generated_at + transaction.quorum_delay
    timestamp_safe = transaction.commit_timestamp + boundary.uncertainty_bound
    return max(quorum_ready, timestamp_safe)


def commit_observation(
    system: RecordAccessSystem,
    transaction: TransactionEvent,
    outside_observer_id: str = "outside_client",
) -> CommitObservation:
    """Evaluate one closed-boundary transaction from inside and outside."""

    if system.boundary is None:
        raise ValueError("closed synchronization evaluation requires a boundary")
    distances = system.shortest_delays_from(transaction.coordinator_id)
    external_path_delay = distances[outside_observer_id]
    raw_external_arrival = transaction.generated_at + external_path_delay
    visible_inside = commit_visible_inside_at(transaction, system.boundary)
    commit_record_external_arrival = visible_inside + external_path_delay
    commit_wait_cost = visible_inside - (transaction.generated_at + transaction.quorum_delay)
    return CommitObservation(
        event_id=transaction.event_id,
        coordinator_id=transaction.coordinator_id,
        generated_at=transaction.generated_at,
        commit_timestamp=transaction.commit_timestamp,
        quorum_delay=transaction.quorum_delay,
        commit_visible_inside_at=visible_inside,
        raw_external_arrival_at=raw_external_arrival,
        commit_record_external_arrival_at=commit_record_external_arrival,
        commit_wait_cost=commit_wait_cost,
        external_path_delay=external_path_delay,
    )


def evaluate_closed_synchronization_boundary(
    system_and_transactions: tuple[RecordAccessSystem, tuple[TransactionEvent, ...]] | None = None,
) -> ClosedSynchronizationResult:
    """Evaluate a closed synchronized commit-boundary witness."""

    if system_and_transactions is None:
        system, transactions = spanner_style_closed_system()
    else:
        system, transactions = system_and_transactions
    if system.boundary is None:
        raise ValueError("system must have a synchronization boundary")

    observations = tuple(commit_observation(system, tx) for tx in transactions)
    internal_order = tuple(
        item.event_id
        for item in sorted(observations, key=lambda item: (item.commit_timestamp, item.event_id))
    )
    outside_raw_order = tuple(
        item.event_id
        for item in sorted(observations, key=lambda item: (item.raw_external_arrival_at, item.event_id))
    )
    outside_commit_order = tuple(
        item.event_id
        for item in sorted(
            observations,
            key=lambda item: (item.commit_record_external_arrival_at, item.event_id),
        )
    )
    outside_reconstruction_time = max(item.commit_record_external_arrival_at for item in observations)
    member_ids = frozenset(system.boundary.member_ids)
    membership_boundary_active = (
        "outside_client" not in member_ids
        and all(tx.coordinator_id in member_ids for tx in transactions)
    )
    propagation_constraints_respected = all(
        item.commit_record_external_arrival_at
        >= item.commit_visible_inside_at + item.external_path_delay
        for item in observations
    )
    sync_cost_total = sum(item.commit_wait_cost for item in observations)
    finding = (
        "Closed synchronization scarcity witnessed: internal commit order is "
        "available to members through timestamp/quorum/uncertainty rules, while "
        "the outside observer initially sees raw path-delay order."
    )
    return ClosedSynchronizationResult(
        system_name=system.name,
        boundary=system.boundary,
        transactions=observations,
        internal_commit_order=internal_order,
        outside_raw_arrival_order=outside_raw_order,
        outside_commit_record_arrival_order=outside_commit_order,
        outside_reconstruction_time=outside_reconstruction_time,
        raw_order_differs_from_commit_order=outside_raw_order != internal_order,
        membership_boundary_active=membership_boundary_active,
        propagation_constraints_respected=propagation_constraints_respected,
        synchronization_cost_total=sync_cost_total,
        finding=finding,
    )


def compare_boundaries(
    open_result: OpenCausalScarcityResult,
    closed_result: ClosedSynchronizationResult,
) -> BoundaryComparison:
    """Compare open and closed scarcity regimes."""

    inside_latest = max(item.commit_visible_inside_at for item in closed_result.transactions)
    outside_lag = closed_result.outside_reconstruction_time - inside_latest
    synchronization_relocates = (
        closed_result.membership_boundary_active
        and closed_result.raw_order_differs_from_commit_order
        and closed_result.propagation_constraints_respected
    )
    statement = (
        "Open systems expose a causal-proximity gradient. Closed systems can "
        "impose an internal commit order, but only for members and only with "
        "bounded synchronization costs; outside observers wait for propagated "
        "records before reconstructing that order."
    )
    return BoundaryComparison(
        open_scarcity_axis="causal_proximity",
        closed_scarcity_axis="membership_plus_synchronization_rule",
        shared_record_access_frontier=open_result.proximity_driven
        and closed_result.membership_boundary_active,
        synchronization_relocates_scarcity=synchronization_relocates,
        outside_observer_lag=outside_lag,
        statement=statement,
    )


def measurement_projection_boundary() -> MeasurementProjectionBoundary:
    """Return the conservative T46 measurement-projection boundary table."""

    return MeasurementProjectionBoundary(
        source_layer="richer_pre_record_structure_Y_candidate",
        target_layer="observer_accessible_record_layer_X",
        morphism_name="measurement_or_finalization_projection",
        preserved_structure=(
            "classical_outcome_label",
            "stable_pointer_record",
            "accessible_correlation_statistics",
            "conservation-compatible coarse quantities",
            "record-holder accessibility relation",
        ),
        forgotten_structure=(
            "relative_phase_information",
            "unmeasured_counterfactual_contexts",
            "coherence_not_preserved_in_accessible_records",
            "environment_entanglement_not_available_to_the_observer",
        ),
        accessible_record_condition=(
            "The target object is information only after it is stable enough to "
            "be accessed, copied, compared, or communicated as a record."
        ),
        record_layer_propagation_constraint=(
            "Once projected into the accessible record layer, communication of "
            "the record is bounded by the propagation channels available in that layer."
        ),
        assumes_fourteen_dimensional_y=False,
        po1_status=(
            "candidate_projection_boundary_only; AC5-like forgotten structure is "
            "named, but T46 does not claim AC1-AC7 or a full measurement PO1 theorem"
        ),
        caution=(
            "This table does not derive a 14D layer, does not demote the Standard "
            "Model to classical residue, and does not claim superluminal usable information."
        ),
    )


def evaluate_hypotheses(
    open_result: OpenCausalScarcityResult,
    closed_result: ClosedSynchronizationResult,
    comparison: BoundaryComparison,
    projection: MeasurementProjectionBoundary,
) -> tuple[HypothesisEvaluation, ...]:
    """Evaluate T46 hypotheses from the finite witnesses."""

    return (
        HypothesisEvaluation(
            hypothesis_id="H0",
            claim="The NYSE/Spanner contrast is only analogy and adds no formal structure.",
            status="rejected_for_finite_abstraction",
            evidence_for=(
                "The real systems are used only as motivating analogies.",
                "The model does not implement market microstructure or Spanner.",
            ),
            evidence_against=(
                "The finite model separates open causal arrival from closed commit order.",
                "Open and closed witnesses have different scarcity axes.",
            ),
            verdict=(
                "Rejected at the finite-abstraction level. The contrast adds a "
                "useful RecordAccessSystem object, while real-system claims remain guarded."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H1",
            claim="Open causal scarcity is already captured by T42 propagation delay.",
            status="supported",
            evidence_for=(
                open_result.finding,
                "First-access order is determined by finite path delay from the source.",
            ),
            evidence_against=(
                "T46 adds economic/value-gradient language not present in T42.",
            ),
            verdict=(
                "Supported. Open causal scarcity is T42-style reconciliation/access "
                "lag applied to first actionable record access."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H2",
            claim="Closed synchronization scarcity requires a boundary/membership object beyond T42-T44.",
            status="supported",
            evidence_for=(
                "The closed witness uses member_ids, quorum, uncertainty_bound, and commit timestamps.",
                "The outside observer is reachable by propagation but excluded from the commit boundary.",
            ),
            evidence_against=(
                "The model is finite and does not implement a full database protocol.",
            ),
            verdict=(
                "Supported. Propagation edges alone do not express the membership "
                "boundary that makes internal commit order authoritative."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H3",
            claim="Both regimes are instances of a common finite record-access frontier structure.",
            status="best_supported",
            evidence_for=(
                "Both witnesses use finite generating nodes, propagation edges, observers, and access times.",
                comparison.statement,
            ),
            evidence_against=(
                "The common object is a sidecar, not a replacement for D1RestrictionSystem.",
            ),
            verdict=(
                "Best supported. RecordAccessSystem is the smallest common object "
                "found for both scarcity regimes."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H4",
            claim=(
                "The distinction exposes a PO1-style projection boundary between "
                "open causal structure and closed commit structure."
            ),
            status="partially_supported",
            evidence_for=(
                "The measurement table names preserved and forgotten structure.",
                "The closed boundary hides internal commit membership and timestamp rules from outsiders until records propagate.",
            ),
            evidence_against=(
                projection.po1_status,
                "No T26 D1RestrictionSystem pair is constructed in T46.",
            ),
            verdict=(
                "Partially supported only as boundary language. Full PO1 status "
                "requires a separate admissibility proof."
            ),
        ),
        HypothesisEvaluation(
            hypothesis_id="H5",
            claim=(
                "The framework is too underdeveloped to distinguish physical "
                "propagation, architectural synchronization, and measurement projection cleanly."
            ),
            status="rejected_for_finite_access_distinction",
            evidence_for=(
                "Measurement projection remains only a conservative table.",
                "No physical derivation of c, relativity, or quantum measurement is attempted.",
            ),
            evidence_against=(
                "Open propagation and closed synchronization are separated by executable witnesses.",
                "The report distinguishes finite access order, internal commit order, and projection into records.",
            ),
            verdict=(
                "Rejected for the finite access distinction, retained as a guardrail "
                "against stronger physical interpretation."
            ),
        ),
    )


def run_t46_analysis() -> T46Result:
    """Run the T46 audit."""

    open_result = evaluate_open_causal_scarcity()
    closed_result = evaluate_closed_synchronization_boundary()
    comparison = compare_boundaries(open_result, closed_result)
    projection = measurement_projection_boundary()
    hypotheses = evaluate_hypotheses(open_result, closed_result, comparison, projection)
    return T46Result(
        open_causal=open_result,
        closed_synchronization=closed_result,
        comparison=comparison,
        measurement_projection=projection,
        hypothesis_evaluations=hypotheses,
        best_supported_hypothesis="H3",
        theorem=(
            "Finite Record-Access Scarcity Theorem: in the T46 "
            "RecordAccessSystem witnesses, open systems expose finality scarcity "
            "as causal-proximity advantage, while closed synchronized systems "
            "relocate scarcity to membership plus bounded commit rules. The "
            "closed system does not abolish propagation delay; outside observers "
            "can reconstruct internal order only after commit records propagate outward."
        ),
        boundary=(
            "The theorem is finite and synthetic. It does not model actual NYSE "
            "market microstructure, does not implement Google Spanner, does not "
            "derive the speed of light, and does not claim a quantum measurement theorem."
        ),
        recommendation=(
            "Add RecordAccessSystem as a sidecar formal object for R1/A1-facing "
            "work. Use it to distinguish open causal finality gradients from "
            "closed synchronization boundaries before making any physics-facing "
            "interpretation."
        ),
        named_claim_recommendation=(
            "CS1 should remain a candidate claim, not a new claim file yet: "
            "T46 supports the finite principle, but more hostile cases are needed."
        ),
    )


def t46_result_to_dict(result: T46Result) -> dict[str, Any]:
    """Serialize T46 result for JSON output."""

    return asdict(result)
