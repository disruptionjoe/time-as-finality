"""T61: MMO reconciliation finality as a hostile engineered domain.

This module tests observer-relative finality in a finite distributed
simulation. It is not a metaphor for physics. The engineered domain is used
because client prediction, authoritative commits, propagation delay, rollback,
and conflict repair have operational meanings there.

The model composes existing repo machinery:

* T46 RecordAccessSystem for propagation and membership/access boundaries;
* T37 TypedTransportNetwork and D1RestrictionSystem for state movement;
* T55 ConflictDescentDatum for incompatible FinaliEvents;
* D1Profile axes for observer-access support, holder redundancy, branch
  support, and reversal cost.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from models.conflict_finalievent_descent import (
    AxisProfile,
    ConflictCompletionResult,
    ConflictDescentDatum,
    EventIdentityMap,
    LocalConflictEvent,
    ObserverConflictView,
    complete_conflict_descent,
)
from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    SiteMap,
    TransportEdge,
)
from models.multiscale_observer_field import D1Profile, ObserverSite
from models.record_access_systems import (
    PropagationEdge,
    RecordAccessSystem,
    RecordEvent,
    RecordNode,
    SynchronizationBoundary,
)
from models.transport_network import (
    NetworkLayer,
    NetworkTransport,
    TypedTransportNetwork,
    analyze_network,
)


@dataclass(frozen=True)
class SimulationObservation:
    observer_id: str
    event_id: str
    arrival_time: int
    status: str
    local_reading: str
    d1_profile: D1Profile


@dataclass(frozen=True)
class ReversalCostTrace:
    event_id: str
    before_authoritative_commit: int
    after_authoritative_commit: int
    reason: str


@dataclass(frozen=True)
class TransportUseSummary:
    network_name: str
    path_labels: tuple[str, ...]
    path_verdicts: tuple[tuple[str, str], ...]
    accumulated_forgotten_by_path: tuple[tuple[str, tuple[str, ...]], ...]
    path_dependent: bool
    verdict: str


@dataclass(frozen=True)
class FinalityAnswer:
    locally_final: tuple[str, ...]
    authoritatively_final: tuple[str, ...]
    predicted_only: tuple[str, ...]
    rolled_back: tuple[str, ...]
    propagated_records: tuple[str, ...]
    observer_event_times: tuple[tuple[str, str, int, str], ...]
    reversal_costs: tuple[ReversalCostTrace, ...]
    reconciliation_statement: str


@dataclass(frozen=True)
class MMOWitness:
    name: str
    classification: str
    system: RecordAccessSystem
    observations: tuple[SimulationObservation, ...]
    transport: TransportUseSummary
    finality_answer: FinalityAnswer
    conflict_completion: ConflictCompletionResult | None
    strengthens_formalism: bool
    claim_recommendation: str


@dataclass(frozen=True)
class T61Result:
    positive_witness: MMOWitness
    failure_witness: MMOWitness
    axis_mapping: tuple[tuple[str, str], ...]
    theorem_candidate: str
    boundary: str
    claim_classification: str
    recommendation: str


CLIENT_PREDICTED = D1Profile(
    accessible_support=1,
    holder_redundancy=1,
    branch_support=1,
    reversal_cost=1,
)
EDGE_APPARENT = D1Profile(
    accessible_support=2,
    holder_redundancy=1,
    branch_support=1,
    reversal_cost=2,
)
EDGE_CONFLICT = D1Profile(
    accessible_support=2,
    holder_redundancy=1,
    branch_support=2,
    reversal_cost=2,
)
AUTHORITY_COMMITTED = D1Profile(
    accessible_support=3,
    holder_redundancy=3,
    branch_support=1,
    reversal_cost=7,
)
RECONCILED_CLIENT = D1Profile(
    accessible_support=3,
    holder_redundancy=2,
    branch_support=1,
    reversal_cost=4,
)
ROLLBACK_RECORD = D1Profile(
    accessible_support=3,
    holder_redundancy=2,
    branch_support=2,
    reversal_cost=3,
)


def axis_mapping() -> tuple[tuple[str, str], ...]:
    return (
        ("causal_finality", "T46 propagation order plus T55 AxisProfile.causal"),
        ("information_finality", "D1Profile.holder_redundancy and propagated record content"),
        ("observer_access_finality", "D1Profile.accessible_support for each observer view"),
        ("branch_conflict_support", "D1Profile.branch_support and T55 conflict pairs"),
        ("reversal_cost", "D1Profile.reversal_cost before and after authority commit"),
    )


def _nodes() -> tuple[RecordNode, ...]:
    return (
        RecordNode("client_a", "client", False, "bounded client observer A"),
        RecordNode("client_b", "client", False, "bounded client observer B"),
        RecordNode("edge_cache", "edge_replica", False, "local cache with stale state risk"),
        RecordNode("authority_region", "authority", True, "authoritative simulation region"),
    )


def _edges() -> tuple[PropagationEdge, ...]:
    return (
        PropagationEdge("client_a", "edge_cache", 1, "client_to_edge"),
        PropagationEdge("client_b", "edge_cache", 1, "client_to_edge"),
        PropagationEdge("edge_cache", "client_a", 1, "edge_to_client"),
        PropagationEdge("edge_cache", "client_b", 1, "edge_to_client"),
        PropagationEdge("edge_cache", "authority_region", 4, "edge_to_authority"),
        PropagationEdge("authority_region", "edge_cache", 4, "authority_to_edge"),
    )


def _boundary() -> SynchronizationBoundary:
    return SynchronizationBoundary(
        boundary_id="authority_membership_boundary",
        member_ids=("authority_region",),
        quorum=1,
        uncertainty_bound=0,
        rule="single_authoritative_region_commit_order",
        description="Only the authority region can turn predicted actions into committed world events.",
    )


def positive_record_access_system() -> RecordAccessSystem:
    events = (
        RecordEvent(
            "pred_move_a",
            "client_a",
            1,
            "client_a predicts move_to_gate",
            "predicted_client_action",
        ),
        RecordEvent(
            "commit_move_a",
            "authority_region",
            7,
            "authority commits move_to_gate",
            "authoritative_commit",
        ),
    )
    return RecordAccessSystem(
        name="t61_positive_mmo_system",
        description="Two clients, one edge cache, and one authority; one prediction is later confirmed.",
        nodes=_nodes(),
        edges=_edges(),
        events=events,
        boundary=_boundary(),
    )


def failure_record_access_system() -> RecordAccessSystem:
    events = (
        RecordEvent(
            "pred_claim_a",
            "client_a",
            1,
            "client_a predicts claim_gem",
            "predicted_client_action",
        ),
        RecordEvent(
            "pred_claim_b",
            "client_b",
            2,
            "client_b predicts claim_gem from stale local view",
            "predicted_client_action",
        ),
        RecordEvent(
            "commit_claim_a",
            "authority_region",
            8,
            "authority commits claim_gem to client_a",
            "authoritative_commit",
        ),
        RecordEvent(
            "rollback_claim_b",
            "authority_region",
            8,
            "authority rejects and rolls back client_b predicted claim",
            "rollback_correction",
        ),
        RecordEvent(
            "compensate_b",
            "authority_region",
            9,
            "authority emits compensation record for client_b",
            "compensation",
        ),
    )
    return RecordAccessSystem(
        name="t61_failure_mmo_system",
        description="Two stale local predictions conflict over one authoritative resource.",
        nodes=_nodes(),
        edges=_edges(),
        events=events,
        boundary=_boundary(),
    )


def _layer(name: str, profile: D1Profile, proposition: str) -> NetworkLayer:
    site_id = f"{name}_site"
    system = D1RestrictionSystem(
        name=f"{name}_d1_system",
        proposition=proposition,
        local_values=(
            LocalD1Value(
                site=ObserverSite(site_id, "mmo", "simulation_view", 0, name),
                proposition_value="true",
                profile=profile,
            ),
        ),
        transport_edges=(),
        source_site=site_id,
        target_site=site_id,
    )
    return NetworkLayer(name=name, system=system)


def _transport(
    name: str,
    source: NetworkLayer,
    target: NetworkLayer,
    forgotten: tuple[str, ...],
    preserved: tuple[str, ...],
) -> NetworkTransport:
    source_site = source.system.local_values[0].site.observer_id
    target_site = target.system.local_values[0].site.observer_id
    morphism = D1RestrictionMorphism(
        name=f"{name}_morphism",
        source=source.system,
        target=target.system,
        site_map=(SiteMap(source_site, target_site),),
        preserved_dimensions=preserved,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
    return NetworkTransport(
        name=name,
        source_name=source.name,
        target_name=target.name,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=preserved,
    )


def _typed_transport_network(conflict: bool) -> TypedTransportNetwork:
    local_profile = CLIENT_PREDICTED if not conflict else D1Profile(1, 1, 2, 1)
    edge_profile = EDGE_APPARENT if not conflict else EDGE_CONFLICT
    authority_profile = AUTHORITY_COMMITTED
    reconciled_profile = RECONCILED_CLIENT if not conflict else ROLLBACK_RECORD
    local = _layer("client_local_view", local_profile, "world_event")
    edge = _layer("edge_cache_view", edge_profile, "world_event")
    authority = _layer("authority_region_view", authority_profile, "world_event")
    reconciled = _layer("reconciled_client_view", reconciled_profile, "world_event")
    transports = (
        _transport(
            "local_to_edge",
            local,
            edge,
            forgotten=("remote_client_state", "authority_membership"),
            preserved=("accessible_support", "branch_support"),
        ),
        _transport(
            "edge_to_authority",
            edge,
            authority,
            forgotten=("client_prediction_certainty", "cache_freshness"),
            preserved=("accessible_support", "holder_redundancy", "branch_support"),
        ),
        _transport(
            "authority_to_reconciled",
            authority,
            reconciled,
            forgotten=("losing_branch_as_world_state",) if conflict else (),
            preserved=("accessible_support", "holder_redundancy", "reversal_cost"),
        ),
    )
    return TypedTransportNetwork(
        name="t61_mmo_state_transport_conflict" if conflict else "t61_mmo_state_transport_positive",
        description="Typed state movement from client prediction through edge cache to authority and reconciliation.",
        layers=(local, edge, authority, reconciled),
        transports=transports,
    )


def _transport_summary(network: TypedTransportNetwork) -> TransportUseSummary:
    analysis = analyze_network(network, "client_local_view", "reconciled_client_view")
    path_rows = []
    forgotten_rows = []
    for item in analysis.path_admissibilities:
        forgotten = tuple(item.endpoint_case.forgotten_structure)
        path_rows.append((item.path_label, item.admissibility.verdict))
        forgotten_rows.append((item.path_label, forgotten))
    return TransportUseSummary(
        network_name=network.name,
        path_labels=tuple(item.path_label for item in analysis.path_admissibilities),
        path_verdicts=tuple(path_rows),
        accumulated_forgotten_by_path=tuple(forgotten_rows),
        path_dependent=analysis.path_dependent,
        verdict=analysis.verdict,
    )


def _obs(
    system: RecordAccessSystem,
    observer_id: str,
    event_id: str,
    status: str,
    reading: str,
    profile: D1Profile,
) -> SimulationObservation:
    return SimulationObservation(
        observer_id=observer_id,
        event_id=event_id,
        arrival_time=system.arrival_time(event_id, observer_id),
        status=status,
        local_reading=reading,
        d1_profile=profile,
    )


def _event_times(observations: tuple[SimulationObservation, ...]) -> tuple[tuple[str, str, int, str], ...]:
    return tuple(
        (item.observer_id, item.event_id, item.arrival_time, item.status)
        for item in sorted(observations, key=lambda obs: (obs.arrival_time, obs.observer_id, obs.event_id))
    )


def positive_witness() -> MMOWitness:
    system = positive_record_access_system()
    observations = (
        _obs(system, "client_a", "pred_move_a", "apparent_local_final", "predicted move is locally usable", CLIENT_PREDICTED),
        _obs(system, "edge_cache", "pred_move_a", "cached_prediction", "edge forwards prediction", EDGE_APPARENT),
        _obs(system, "authority_region", "pred_move_a", "authority_received_prediction", "authority can decide", EDGE_APPARENT),
        _obs(system, "authority_region", "commit_move_a", "authoritative_final", "commit accepted inside boundary", AUTHORITY_COMMITTED),
        _obs(system, "client_a", "commit_move_a", "reconciled_authoritative_final", "local view repaired by matching commit", RECONCILED_CLIENT),
        _obs(system, "client_b", "commit_move_a", "remote_authoritative_final", "other client receives committed record", RECONCILED_CLIENT),
    )
    finality = FinalityAnswer(
        locally_final=("client_a:pred_move_a@1",),
        authoritatively_final=("authority_region:commit_move_a@7",),
        predicted_only=("pred_move_a before commit_move_a arrives",),
        rolled_back=(),
        propagated_records=("pred_move_a", "commit_move_a"),
        observer_event_times=_event_times(observations),
        reversal_costs=(
            ReversalCostTrace(
                "pred_move_a/commit_move_a",
                before_authoritative_commit=CLIENT_PREDICTED.reversal_cost,
                after_authoritative_commit=AUTHORITY_COMMITTED.reversal_cost,
                reason="authority commit increases holder redundancy and reversal cost",
            ),
        ),
        reconciliation_statement=(
            "The client has apparent local finality before the authority has event finality; "
            "the later commit matches the prediction, so reconciliation upgrades the local view without rollback."
        ),
    )
    return MMOWitness(
        name="positive_prediction_confirmed",
        classification="reconciled_without_contradiction",
        system=system,
        observations=observations,
        transport=_transport_summary(_typed_transport_network(conflict=False)),
        finality_answer=finality,
        conflict_completion=None,
        strengthens_formalism=True,
        claim_recommendation="Strengthens A1 as a hostile engineered-domain analogy; no new claim yet.",
    )


def _failure_conflict_completion() -> ConflictCompletionResult:
    client_a_event = LocalConflictEvent(
        observer="client_a",
        name="claim_a",
        source_records=frozenset({"gem_available"}),
        target_records=frozenset({"gem_owned_by_a"}),
        profile=AxisProfile(causal=1, info=2),
    )
    client_b_event = LocalConflictEvent(
        observer="client_b",
        name="claim_b",
        source_records=frozenset({"gem_available"}),
        target_records=frozenset({"gem_owned_by_b"}),
        profile=AxisProfile(causal=2, info=1),
    )
    edge_a_event = LocalConflictEvent(
        observer="edge_cache",
        name="claim_a",
        source_records=frozenset({"gem_available"}),
        target_records=frozenset({"gem_owned_by_a"}),
        profile=AxisProfile(causal=1, info=2),
    )
    edge_b_event = LocalConflictEvent(
        observer="edge_cache",
        name="claim_b",
        source_records=frozenset({"gem_available"}),
        target_records=frozenset({"gem_owned_by_b"}),
        profile=AxisProfile(causal=2, info=1),
    )
    datum = ConflictDescentDatum(
        name="t61_stale_prediction_conflict",
        description="Two observer-local predicted claims are incompatible over one authoritative resource.",
        observer_views=(
            ObserverConflictView("client_a", (client_a_event,)),
            ObserverConflictView("client_b", (client_b_event,)),
            ObserverConflictView(
                "edge_cache",
                (edge_a_event, edge_b_event),
                conflict_pairs=(("claim_a", "claim_b"),),
            ),
        ),
        identity_maps=(
            EventIdentityMap("client_a", "claim_a", "e_claim_a"),
            EventIdentityMap("client_b", "claim_b", "e_claim_b"),
            EventIdentityMap("edge_cache", "claim_a", "e_claim_a"),
            EventIdentityMap("edge_cache", "claim_b", "e_claim_b"),
        ),
        overlap_witnesses=frozenset({"e_claim_a", "e_claim_b"}),
        expected_classification="canonical",
    )
    return complete_conflict_descent(datum)


def failure_witness() -> MMOWitness:
    system = failure_record_access_system()
    observations = (
        _obs(system, "client_a", "pred_claim_a", "apparent_local_final", "client_a sees gem as claimed locally", D1Profile(1, 1, 2, 1)),
        _obs(system, "client_b", "pred_claim_b", "apparent_local_final", "client_b sees gem as claimed locally from stale cache", D1Profile(1, 1, 2, 1)),
        _obs(system, "client_b", "pred_claim_a", "remote_prediction_late", "client_b learns of client_a prediction after making its own prediction", EDGE_CONFLICT),
        _obs(system, "client_a", "pred_claim_b", "remote_conflict_late", "client_a learns of client_b incompatible prediction", EDGE_CONFLICT),
        _obs(system, "edge_cache", "pred_claim_a", "cached_prediction", "edge sees first predicted branch", EDGE_CONFLICT),
        _obs(system, "edge_cache", "pred_claim_b", "cached_conflicting_prediction", "edge sees incompatible predicted branch", EDGE_CONFLICT),
        _obs(system, "authority_region", "pred_claim_a", "authority_received_prediction", "authority receives branch A first", EDGE_CONFLICT),
        _obs(system, "authority_region", "pred_claim_b", "authority_received_conflict", "authority receives branch B second", EDGE_CONFLICT),
        _obs(system, "authority_region", "commit_claim_a", "authoritative_final", "authority commits branch A", AUTHORITY_COMMITTED),
        _obs(system, "authority_region", "rollback_claim_b", "authoritative_correction", "authority rejects branch B", ROLLBACK_RECORD),
        _obs(system, "client_b", "rollback_claim_b", "rollback_required", "client_b must remove predicted ownership", ROLLBACK_RECORD),
        _obs(system, "client_b", "compensate_b", "compensation_record", "client_b receives explicit compensation", ROLLBACK_RECORD),
        _obs(system, "client_a", "commit_claim_a", "reconciled_authoritative_final", "client_a receives winning commit", RECONCILED_CLIENT),
    )
    conflict = _failure_conflict_completion()
    finality = FinalityAnswer(
        locally_final=("client_a:pred_claim_a@1", "client_b:pred_claim_b@2"),
        authoritatively_final=("authority_region:commit_claim_a@8", "authority_region:rollback_claim_b@8"),
        predicted_only=("pred_claim_b until rollback_claim_b arrives at client_b",),
        rolled_back=("pred_claim_b",),
        propagated_records=("pred_claim_a", "pred_claim_b", "commit_claim_a", "rollback_claim_b", "compensate_b"),
        observer_event_times=_event_times(observations),
        reversal_costs=(
            ReversalCostTrace(
                "pred_claim_b",
                before_authoritative_commit=1,
                after_authoritative_commit=3,
                reason="rollback is cheap before commit but still needs an explicit correction record after conflict is known",
            ),
            ReversalCostTrace(
                "commit_claim_a",
                before_authoritative_commit=1,
                after_authoritative_commit=AUTHORITY_COMMITTED.reversal_cost,
                reason="reversing the authoritative winner is expensive after holder redundancy and commit record propagation",
            ),
        ),
        reconciliation_statement=(
            "The two apparent local finalities cannot both become authoritative. "
            "Clean reconciliation fails unless the losing branch is represented by rollback, compensation, or explicit conflict."
        ),
    )
    return MMOWitness(
        name="failure_stale_conflicting_prediction",
        classification="rollback_required_conflict_handled",
        system=system,
        observations=observations,
        transport=_transport_summary(_typed_transport_network(conflict=True)),
        finality_answer=finality,
        conflict_completion=conflict,
        strengthens_formalism=True,
        claim_recommendation=(
            "Strengthens A1 and T55/T46 integration as a hostile engineered-domain result; "
            "does not motivate a new claim until more rollback policies are tested."
        ),
    )


def run_t61_analysis() -> T61Result:
    return T61Result(
        positive_witness=positive_witness(),
        failure_witness=failure_witness(),
        axis_mapping=axis_mapping(),
        theorem_candidate=(
            "Finite MMO Reconciliation Separation: in the tested finite simulation, apparent "
            "local finality can precede authoritative event finality; matching authority commits "
            "upgrade apparent finality without contradiction, while incompatible stale predictions "
            "require rollback, compensation, or explicit conflict handling."
        ),
        boundary=(
            "This is a hostile engineered-domain test of observer-relative finality, not a physical "
            "metaphor. It composes existing sidecars and exposes no need for a new primitive in the "
            "two witnesses, though richer rollback policies may require additional machinery."
        ),
        claim_classification=(
            "Strengthens A1 as a formal analogy/homology candidate inside engineered distributed "
            "simulation. It does not justify a new named claim yet."
        ),
        recommendation=(
            "Keep T61 as an A1/T46/T55 integration test. Next hostile cases should add partitioned "
            "authority, authority migration, and compensation policies that alter downstream records."
        ),
    )


def _d1_to_dict(profile: D1Profile) -> dict[str, int]:
    return {
        "accessible_support": profile.accessible_support,
        "holder_redundancy": profile.holder_redundancy,
        "branch_support": profile.branch_support,
        "reversal_cost": profile.reversal_cost,
    }


def _observation_to_dict(obs: SimulationObservation) -> dict[str, Any]:
    return {
        "observer_id": obs.observer_id,
        "event_id": obs.event_id,
        "arrival_time": obs.arrival_time,
        "status": obs.status,
        "local_reading": obs.local_reading,
        "d1_profile": _d1_to_dict(obs.d1_profile),
    }


def _transport_to_dict(summary: TransportUseSummary) -> dict[str, Any]:
    return asdict(summary)


def _conflict_to_dict(completion: ConflictCompletionResult | None) -> dict[str, Any] | None:
    if completion is None:
        return None
    return {
        "datum_name": completion.datum_name,
        "classification": completion.classification,
        "condition_failures": list(completion.condition_failures),
        "theorem_applies": completion.theorem_applies,
        "conflict_pairs": (
            []
            if completion.conflict_check is None
            else [list(pair) for pair in completion.conflict_check.conflict_pairs]
        ),
        "conflict_valid": None if completion.conflict_check is None else completion.conflict_check.valid,
        "am_holds": None if completion.axis_monotonicity is None else completion.axis_monotonicity.am_holds,
        "evidence": completion.evidence,
    }


def _answer_to_dict(answer: FinalityAnswer) -> dict[str, Any]:
    return {
        "locally_final": list(answer.locally_final),
        "authoritatively_final": list(answer.authoritatively_final),
        "predicted_only": list(answer.predicted_only),
        "rolled_back": list(answer.rolled_back),
        "propagated_records": list(answer.propagated_records),
        "observer_event_times": [list(item) for item in answer.observer_event_times],
        "reversal_costs": [asdict(item) for item in answer.reversal_costs],
        "reconciliation_statement": answer.reconciliation_statement,
    }


def _system_to_dict(system: RecordAccessSystem) -> dict[str, Any]:
    return {
        "name": system.name,
        "nodes": [asdict(node) for node in system.nodes],
        "edges": [asdict(edge) for edge in system.edges],
        "events": [asdict(event) for event in system.events],
        "boundary": None if system.boundary is None else asdict(system.boundary),
    }


def _witness_to_dict(witness: MMOWitness) -> dict[str, Any]:
    return {
        "name": witness.name,
        "classification": witness.classification,
        "system": _system_to_dict(witness.system),
        "observations": [_observation_to_dict(obs) for obs in witness.observations],
        "transport": _transport_to_dict(witness.transport),
        "finality_answer": _answer_to_dict(witness.finality_answer),
        "conflict_completion": _conflict_to_dict(witness.conflict_completion),
        "strengthens_formalism": witness.strengthens_formalism,
        "claim_recommendation": witness.claim_recommendation,
    }


def t61_result_to_dict(result: T61Result) -> dict[str, Any]:
    return {
        "positive_witness": _witness_to_dict(result.positive_witness),
        "failure_witness": _witness_to_dict(result.failure_witness),
        "axis_mapping": [list(item) for item in result.axis_mapping],
        "theorem_candidate": result.theorem_candidate,
        "boundary": result.boundary,
        "claim_classification": result.claim_classification,
        "recommendation": result.recommendation,
    }


__all__ = [
    "FinalityAnswer",
    "MMOWitness",
    "ReversalCostTrace",
    "SimulationObservation",
    "T61Result",
    "axis_mapping",
    "failure_record_access_system",
    "failure_witness",
    "positive_record_access_system",
    "positive_witness",
    "run_t61_analysis",
    "t61_result_to_dict",
]

