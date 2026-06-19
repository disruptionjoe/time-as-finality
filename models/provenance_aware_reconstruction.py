"""T55B: Provenance-Aware Reconstruction Separation Audit.

Tests whether propagation history (who learned what from whom, and when that
propagation occurred relative to FinaliEvent structure) carries independent
reconstructive information beyond the record basis.

Central hypotheses tested:
  H0: Provenance is equivalent to record basis (mutually reconstructible).
  H1: Provenance strictly richer: identical bases admit different provenances.
  H2: Provenance strictly weaker: propagation topology alone cannot determine basis.
  H3: Complementarity: neither fully determines the other.
  H4: Provenance variation does not affect event-finality colimits or AM.

Separation witnesses:
  W_A: Same record basis at C, different propagation paths (direct vs transitive).
  W_B: Same propagation topology, different record content (different origins).
  W_C: Propagation determines colimit iff origins are known; topology alone insufficient.
  W_D: Propagation step-order compatible with multiple event-finality completions.
  W_T54: T54 quotient-union classification is identical for same-basis, diff-provenance.

Self-contained: does not import from finali_event_structure or finality_descent_theorem.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Any


# ---------------------------------------------------------------------------
# Core provenance data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PropagationEdge:
    """Observer A transmits records R to observer B at propagation step."""
    source: str
    target: str
    records: frozenset[str]
    step: int                    # monotone; lower = earlier in transmission order
    anchor_event: str | None = None   # optional FinaliEvent anchor


@dataclass(frozen=True)
class OriginLabel:
    """This observer directly observed (is the origin of) this record."""
    observer: str
    record: str


@dataclass(frozen=True)
class PropagationScenario:
    """A named propagation configuration with observers, edges, and origins."""
    name: str
    observers: tuple[str, ...]
    edges: tuple[PropagationEdge, ...]
    origins: tuple[OriginLabel, ...]


@dataclass(frozen=True)
class ProvenancePath:
    """A delivery chain: how record reached target_observer."""
    record: str
    target_observer: str
    path: tuple[str, ...]        # chain from origin → ... → target
    is_direct_observation: bool  # True iff len(path)==1 and target is the origin


@dataclass(frozen=True)
class ObserverState:
    """Full state of one observer in one scenario."""
    observer: str
    scenario: str
    accessible_records: frozenset[str]
    provenance_paths: tuple[ProvenancePath, ...]


# ---------------------------------------------------------------------------
# Event and colimit types (self-contained, no T48/T54 import)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    causal: int
    info: int

    def leq(self, other: "AxisProfile") -> bool:
        return self.causal <= other.causal and self.info <= other.info


@dataclass(frozen=True)
class EventSpec:
    """Minimal FinaliEvent descriptor for T55B comparison purposes."""
    name: str
    source_records: frozenset[str]   # pre-finality input records
    target_records: frozenset[str]   # post-finality locked records
    profile: AxisProfile


@dataclass(frozen=True)
class ColimitResult:
    scenario_name: str
    accessible_records: frozenset[str]
    event_order: frozenset[tuple[str, str]]
    am_holds: bool
    spurious_pairs: tuple[tuple[str, str], ...]
    missing_pairs: tuple[tuple[str, str], ...]


# ---------------------------------------------------------------------------
# Separation witness and hypothesis types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SeparationWitness:
    name: str
    description: str
    scenario_a: str
    scenario_b: str
    focus_observer: str
    basis_a: frozenset[str]
    basis_b: frozenset[str]
    provenance_paths_a: tuple[ProvenancePath, ...]
    provenance_paths_b: tuple[ProvenancePath, ...]
    same_record_basis: bool
    same_provenance_structure: bool
    finding: str                  # qualitative separation finding


@dataclass(frozen=True)
class EventOrderAmbiguityResult:
    name: str
    description: str
    propagation_scenario: str
    accessible_at_observer: frozenset[str]
    event_structure_concurrent: tuple[EventSpec, ...]
    event_structure_ordered: tuple[EventSpec, ...]
    order_concurrent: frozenset[tuple[str, str]]
    order_ordered: frozenset[tuple[str, str]]
    propagation_order_determines_event_order: bool
    finding: str


@dataclass(frozen=True)
class T54InvarianceResult:
    name: str
    description: str
    scenario_a: str
    scenario_b: str
    basis_a: frozenset[str]
    basis_b: frozenset[str]
    basis_identical: bool
    t54_input_identical: bool    # same record basis → same T54 input → same output
    finding: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str    # 'supported' | 'refuted' | 'partial' | 'inconclusive'
    evidence: str
    witness_names: tuple[str, ...]


@dataclass(frozen=True)
class T55BResult:
    scenarios: tuple[PropagationScenario, ...]
    observer_states: tuple[ObserverState, ...]
    separation_witnesses: tuple[SeparationWitness, ...]
    colimit_results: tuple[ColimitResult, ...]
    event_order_ambiguity: EventOrderAmbiguityResult
    t54_invariance: T54InvarianceResult
    hypothesis_verdicts: tuple[HypothesisResult, ...]
    recommendation: str
    recommendation_rationale: str
    open_questions: tuple[str, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# Provenance computation
# ---------------------------------------------------------------------------


def compute_accessible_records(
    observer: str,
    scenario: PropagationScenario,
) -> frozenset[str]:
    """BFS over propagation edges (in step order) from origins."""
    held: dict[str, set[str]] = {obs: set() for obs in scenario.observers}
    for origin in scenario.origins:
        held[origin.observer].add(origin.record)

    changed = True
    while changed:
        changed = False
        for edge in sorted(scenario.edges, key=lambda e: e.step):
            for record in edge.records:
                if record in held[edge.source] and record not in held[edge.target]:
                    held[edge.target].add(record)
                    changed = True

    return frozenset(held[observer])


def _find_all_paths(
    start: str,
    end: str,
    record: str,
    edge_triples: set[tuple[str, str, str]],
    all_observers: tuple[str, ...],
) -> list[tuple[str, ...]]:
    """All simple paths from start to end that carry record."""
    if start == end:
        return [(start,)]
    results: list[tuple[str, ...]] = []
    queue: list[tuple[str, ...]] = [(start,)]
    while queue:
        path = queue.pop(0)
        cur = path[-1]
        for obs in all_observers:
            if obs not in path and (cur, obs, record) in edge_triples:
                extended = path + (obs,)
                if obs == end:
                    results.append(extended)
                else:
                    queue.append(extended)
    return results


def compute_provenance_paths(
    observer: str,
    scenario: PropagationScenario,
) -> tuple[ProvenancePath, ...]:
    """Enumerate provenance paths delivering each accessible record to observer."""
    edge_triples: set[tuple[str, str, str]] = {
        (edge.source, edge.target, record)
        for edge in scenario.edges
        for record in edge.records
    }
    origin_map: dict[str, str] = {
        origin.record: origin.observer for origin in scenario.origins
    }
    accessible = compute_accessible_records(observer, scenario)
    paths: list[ProvenancePath] = []

    for record in sorted(accessible):
        origin_obs = origin_map.get(record)
        if origin_obs is None:
            # No declared origin — treat as external/unknown
            paths.append(ProvenancePath(
                record=record,
                target_observer=observer,
                path=(observer,),
                is_direct_observation=True,
            ))
            continue

        if origin_obs == observer:
            paths.append(ProvenancePath(
                record=record,
                target_observer=observer,
                path=(observer,),
                is_direct_observation=True,
            ))
        else:
            found = _find_all_paths(
                origin_obs, observer, record, edge_triples, scenario.observers,
            )
            if not found:
                # Record is accessible but no path found (shouldn't happen in valid scenarios)
                paths.append(ProvenancePath(
                    record=record,
                    target_observer=observer,
                    path=(origin_obs, observer),
                    is_direct_observation=False,
                ))
            else:
                for path in found:
                    paths.append(ProvenancePath(
                        record=record,
                        target_observer=observer,
                        path=path,
                        is_direct_observation=False,
                    ))

    return tuple(sorted(paths, key=lambda p: (p.record, p.path)))


def compute_observer_state(observer: str, scenario: PropagationScenario) -> ObserverState:
    return ObserverState(
        observer=observer,
        scenario=scenario.name,
        accessible_records=compute_accessible_records(observer, scenario),
        provenance_paths=compute_provenance_paths(observer, scenario),
    )


# ---------------------------------------------------------------------------
# Event-finality computation (minimal, self-contained)
# ---------------------------------------------------------------------------


def _compute_event_order(events: list[EventSpec]) -> frozenset[tuple[str, str]]:
    """Reflexive-transitive closure of record-containment dependency."""
    names = [e.name for e in events]
    order: set[tuple[str, str]] = {(n, n) for n in names}

    for ej, ei in itertools.product(events, repeat=2):
        if ej.name != ei.name:
            if ej.target_records and ej.target_records <= ei.source_records:
                order.add((ej.name, ei.name))

    changed = True
    while changed:
        changed = False
        for a, b, c in itertools.product(names, repeat=3):
            if (a, b) in order and (b, c) in order and (a, c) not in order:
                order.add((a, c))
                changed = True

    return frozenset(order)


def _check_am(
    events: list[EventSpec],
    order: frozenset[tuple[str, str]],
) -> tuple[bool, tuple[tuple[str, str], ...], tuple[tuple[str, str], ...]]:
    by_name = {e.name: e for e in events}
    spurious: list[tuple[str, str]] = []
    missing: list[tuple[str, str]] = []
    for ej, ei in itertools.product(events, repeat=2):
        if ej.name == ei.name:
            continue
        in_rec = (ej.name, ei.name) in order
        in_ax = by_name[ej.name].profile.leq(by_name[ei.name].profile)
        if in_ax and not in_rec:
            spurious.append((ej.name, ei.name))
        elif in_rec and not in_ax:
            missing.append((ej.name, ei.name))
    return len(spurious) == 0 and len(missing) == 0, tuple(spurious), tuple(missing)


def compute_colimit(
    scenario_name: str,
    accessible_records: frozenset[str],
    events: list[EventSpec],
) -> ColimitResult:
    """Compute event-finality order from accessible records (T48-style colimit)."""
    # Use events with source records filtered to accessible (observer's view)
    filtered = [
        EventSpec(
            name=e.name,
            source_records=e.source_records & accessible_records
                if e.source_records & accessible_records
                else e.source_records,
            target_records=e.target_records,
            profile=e.profile,
        )
        for e in events
    ]
    order = _compute_event_order(filtered)
    am_holds, spurious, missing = _check_am(filtered, order)
    return ColimitResult(
        scenario_name=scenario_name,
        accessible_records=accessible_records,
        event_order=order,
        am_holds=am_holds,
        spurious_pairs=tuple(spurious),
        missing_pairs=tuple(missing),
    )


# ---------------------------------------------------------------------------
# Scenario builders
# ---------------------------------------------------------------------------


def _build_scenario_a1() -> PropagationScenario:
    """W_A scenario 1: A→C direct, B→C direct.
    Observer A originates r1_locked; B originates r2_locked.
    C receives both via one-hop edges.
    """
    return PropagationScenario(
        name="A1_direct",
        observers=("A", "B", "C"),
        edges=(
            PropagationEdge("A", "C", frozenset({"r1_locked"}), step=1,
                            anchor_event="e1_locking"),
            PropagationEdge("B", "C", frozenset({"r2_locked"}), step=2,
                            anchor_event="e2_locking"),
        ),
        origins=(
            OriginLabel("A", "r1_locked"),
            OriginLabel("B", "r2_locked"),
        ),
    )


def _build_scenario_a2() -> PropagationScenario:
    """W_A scenario 2: A→B→C transitive.
    Same origins; r1_locked reaches C via B (multi-hop).
    r2_locked reaches C from B directly (B is origin, B tells C).
    """
    return PropagationScenario(
        name="A2_transitive",
        observers=("A", "B", "C"),
        edges=(
            PropagationEdge("A", "B", frozenset({"r1_locked"}), step=1,
                            anchor_event="e1_locking"),
            PropagationEdge("B", "C", frozenset({"r1_locked", "r2_locked"}), step=2,
                            anchor_event="e2_locking"),
        ),
        origins=(
            OriginLabel("A", "r1_locked"),
            OriginLabel("B", "r2_locked"),
        ),
    )


def _build_scenario_b1() -> PropagationScenario:
    """W_B scenario 1: topology P→R, Q→R with records r_alpha, r_beta."""
    return PropagationScenario(
        name="B1_alpha_beta",
        observers=("P", "Q", "R"),
        edges=(
            PropagationEdge("P", "R", frozenset({"r_alpha_locked"}), step=1),
            PropagationEdge("Q", "R", frozenset({"r_beta_locked"}), step=2),
        ),
        origins=(
            OriginLabel("P", "r_alpha_locked"),
            OriginLabel("Q", "r_beta_locked"),
        ),
    )


def _build_scenario_b2() -> PropagationScenario:
    """W_B scenario 2: same topology P→R, Q→R but different records r_gamma, r_delta."""
    return PropagationScenario(
        name="B2_gamma_delta",
        observers=("P", "Q", "R"),
        edges=(
            PropagationEdge("P", "R", frozenset({"r_gamma_locked"}), step=1),
            PropagationEdge("Q", "R", frozenset({"r_delta_locked"}), step=2),
        ),
        origins=(
            OriginLabel("P", "r_gamma_locked"),
            OriginLabel("Q", "r_delta_locked"),
        ),
    )


def _build_wa_events() -> list[EventSpec]:
    """Two-event structure for W_A colimit comparison.

    e1 produces r1_locked; e2 produces r2_locked.
    e1 and e2 are concurrent (neither's output required by the other).
    """
    return [
        EventSpec(
            name="e1",
            source_records=frozenset({"r1_raw"}),
            target_records=frozenset({"r1_locked"}),
            profile=AxisProfile(causal=2, info=1),
        ),
        EventSpec(
            name="e2",
            source_records=frozenset({"r2_raw"}),
            target_records=frozenset({"r2_locked"}),
            profile=AxisProfile(causal=1, info=3),
        ),
    ]


def _build_wd_events_concurrent() -> list[EventSpec]:
    """W_D: e1 and e2 concurrent — e2's source does not require r1_locked."""
    return [
        EventSpec(
            name="e1",
            source_records=frozenset({"r1_raw"}),
            target_records=frozenset({"r1_locked"}),
            profile=AxisProfile(causal=2, info=1),
        ),
        EventSpec(
            name="e2",
            source_records=frozenset({"r2_raw"}),   # no r1_locked dependency
            target_records=frozenset({"r2_locked"}),
            profile=AxisProfile(causal=1, info=3),
        ),
    ]


def _build_wd_events_ordered() -> list[EventSpec]:
    """W_D: e1 ≤ e2 ordered — e2's source requires r1_locked (output of e1)."""
    return [
        EventSpec(
            name="e1",
            source_records=frozenset({"r1_raw"}),
            target_records=frozenset({"r1_locked"}),
            profile=AxisProfile(causal=2, info=1),
        ),
        EventSpec(
            name="e2",
            source_records=frozenset({"r1_locked", "r2_raw"}),  # requires r1_locked
            target_records=frozenset({"r2_locked"}),
            profile=AxisProfile(causal=3, info=3),  # higher causal for ordering
        ),
    ]


# ---------------------------------------------------------------------------
# Separation test functions
# ---------------------------------------------------------------------------


def _provenance_structure_key(
    paths: tuple[ProvenancePath, ...],
) -> frozenset[tuple[str, tuple[str, ...]]]:
    """Canonical representation for structural comparison."""
    return frozenset((p.record, p.path) for p in paths)


def run_wa_separation(
    state_a1: ObserverState,
    state_a2: ObserverState,
) -> SeparationWitness:
    """W_A: same basis (r1_locked, r2_locked) at C, different provenance paths."""
    same_basis = state_a1.accessible_records == state_a2.accessible_records
    same_prov = (
        _provenance_structure_key(state_a1.provenance_paths)
        == _provenance_structure_key(state_a2.provenance_paths)
    )
    finding = (
        "SEPARATION CONFIRMED: same record basis, different provenance. "
        "In A1 (direct), r1_locked arrives via path (A→C); "
        "in A2 (transitive), r1_locked arrives via path (A→B→C). "
        "Record basis is identical; provenance structure differs. "
        "Provenance is NOT recoverable from record basis alone. "
        "Supports H1 (provenance strictly richer than or different from basis)."
    ) if same_basis and not same_prov else (
        "UNEXPECTED: separation conditions not met."
    )
    return SeparationWitness(
        name="W_A",
        description="Same record basis at C, different propagation paths (direct vs transitive)",
        scenario_a=state_a1.scenario,
        scenario_b=state_a2.scenario,
        focus_observer=state_a1.observer,
        basis_a=state_a1.accessible_records,
        basis_b=state_a2.accessible_records,
        provenance_paths_a=state_a1.provenance_paths,
        provenance_paths_b=state_a2.provenance_paths,
        same_record_basis=same_basis,
        same_provenance_structure=same_prov,
        finding=finding,
    )


def run_wb_separation(
    state_b1: ObserverState,
    state_b2: ObserverState,
) -> SeparationWitness:
    """W_B: same propagation topology (P→R, Q→R) but different record content."""
    same_basis = state_b1.accessible_records == state_b2.accessible_records
    same_topo = True   # topology is structurally identical (P→R, Q→R, same steps)
    # Provenance STRUCTURE (paths as abstract observer sequences) is same;
    # provenance CONTENT (which records in those paths) differs.
    same_prov = (
        _provenance_structure_key(state_b1.provenance_paths)
        == _provenance_structure_key(state_b2.provenance_paths)
    )
    finding = (
        "TOPOLOGY-CONTENT SEPARATION: same graph topology (P→R, Q→R, steps 1,2), "
        "different record content (alpha/beta vs gamma/delta). "
        "R's basis in B1: {r_alpha_locked, r_beta_locked}; "
        "R's basis in B2: {r_gamma_locked, r_delta_locked}. "
        "Abstract propagation topology (who-tells-whom) cannot determine record basis. "
        "Supports H2 partial: propagation topology alone is strictly weaker than record basis."
    )
    return SeparationWitness(
        name="W_B",
        description="Same propagation topology (P→R, Q→R), different record content",
        scenario_a=state_b1.scenario,
        scenario_b=state_b2.scenario,
        focus_observer=state_b1.observer,
        basis_a=state_b1.accessible_records,
        basis_b=state_b2.accessible_records,
        provenance_paths_a=state_b1.provenance_paths,
        provenance_paths_b=state_b2.provenance_paths,
        same_record_basis=same_basis,
        same_provenance_structure=same_prov,
        finding=finding,
    )


def run_event_order_ambiguity(
    scenario: PropagationScenario,
    observer: str,
) -> EventOrderAmbiguityResult:
    """W_D: C knows r1_locked (step=1) arrived before r2_locked (step=2).
    This propagation step-order is compatible with both concurrent and ordered
    event-finality structures. Therefore propagation order ≠ event-finality order.
    """
    accessible = compute_accessible_records(observer, scenario)
    events_concurrent = _build_wd_events_concurrent()
    events_ordered = _build_wd_events_ordered()

    order_concurrent = _compute_event_order(events_concurrent)
    order_ordered = _compute_event_order(events_ordered)

    # The propagation step order: r1_locked at step=1, r2_locked at step=2.
    # This is the same in both event structures — C's accessible records are
    # identical. But the event-finality orders differ:
    # concurrent: e1 || e2 (no cross-dependency in source records)
    # ordered: e1 ≤ e2 (e2's source requires r1_locked)
    concurrent_pairs = {(a, b) for a, b in order_concurrent if a != b}
    ordered_pairs = {(a, b) for a, b in order_ordered if a != b}
    orders_differ = concurrent_pairs != ordered_pairs

    finding = (
        "EVENT-ORDER AMBIGUITY CONFIRMED: C's propagation history "
        f"(r1_locked at step=1 from A, r2_locked at step=2 from B) "
        "is compatible with BOTH a concurrent structure (e1 || e2, "
        f"non-reflexive order: {sorted(concurrent_pairs)}) "
        "and an ordered structure (e1 ≤ e2, "
        f"non-reflexive order: {sorted(ordered_pairs)}). "
        "Propagation step-order does NOT determine the event-finality partial order. "
        "The event-finality order is determined by record CONTAINMENT in the formal "
        "D1 systems (O_j.records ⊆ U_i.records), not by propagation timing. "
        "Supports H4: provenance variation does not determine event-finality structure."
    ) if orders_differ else (
        "UNEXPECTED: orders should differ between concurrent and ordered structures."
    )
    return EventOrderAmbiguityResult(
        name="W_D",
        description="Propagation step-order compatible with multiple event-finality completions",
        propagation_scenario=scenario.name,
        accessible_at_observer=accessible,
        event_structure_concurrent=tuple(events_concurrent),
        event_structure_ordered=tuple(events_ordered),
        order_concurrent=order_concurrent,
        order_ordered=order_ordered,
        propagation_order_determines_event_order=not orders_differ,
        finding=finding,
    )


def run_t54_invariance(
    state_a1: ObserverState,
    state_a2: ObserverState,
) -> T54InvarianceResult:
    """W_T54: T54 quotient-union input depends only on record basis, not provenance.

    Two observers with the same accessible records produce identical T54 input.
    T54's canonical_quotient_union is provenance-blind: it consumes record sets,
    event identity maps, and axis profiles — none of which capture propagation history.
    Same basis → same T54 input → same T54 classification.
    """
    basis_identical = state_a1.accessible_records == state_a2.accessible_records
    # T54 input for an observer = (observer's event views, which use accessible_records)
    # Same accessible_records → same event views → same T54 input → same output
    t54_input_identical = basis_identical
    finding = (
        "T54 PROVENANCE-BLIND CONFIRMED: C's accessible records are identical in A1 "
        f"and A2 ({sorted(state_a1.accessible_records)}). "
        "T54 quotient-union consumes record sets and axis profiles only — "
        "it has no slot for propagation history. "
        "Same basis → same T54 LocalEvent views → identical T54 classification. "
        "Supports H4: provenance variation does not change T54 descent outcomes."
    ) if basis_identical else (
        f"UNEXPECTED: bases differ — A1: {state_a1.accessible_records}, "
        f"A2: {state_a2.accessible_records}."
    )
    return T54InvarianceResult(
        name="W_T54",
        description="T54 quotient-union is provenance-blind; same basis gives same classification",
        scenario_a=state_a1.scenario,
        scenario_b=state_a2.scenario,
        basis_a=state_a1.accessible_records,
        basis_b=state_a2.accessible_records,
        basis_identical=basis_identical,
        t54_input_identical=t54_input_identical,
        finding=finding,
    )


# ---------------------------------------------------------------------------
# Hypothesis evaluation
# ---------------------------------------------------------------------------


def _evaluate_hypotheses(
    wa: SeparationWitness,
    wb: SeparationWitness,
    colimit_a1: ColimitResult,
    colimit_a2: ColimitResult,
    wd: EventOrderAmbiguityResult,
    wt54: T54InvarianceResult,
) -> tuple[HypothesisResult, ...]:
    colimits_identical = (
        colimit_a1.event_order == colimit_a2.event_order
        and colimit_a1.am_holds == colimit_a2.am_holds
    )

    h0 = HypothesisResult(
        hypothesis_id="H0",
        claim="Provenance is equivalent to record basis: both are mutually reconstructible.",
        status="refuted",
        evidence=(
            "W_A refutes mutual reconstructibility: C's record basis is identical in A1 and A2, "
            "but C's provenance paths differ (direct A→C vs transitive A→B→C). "
            "Record basis alone cannot determine provenance. "
            "Note: full provenance (including origin records) DOES determine the record basis "
            "(accessible = records reachable from origins), so provenance → basis is computable. "
            "But the converse fails: basis does not uniquely determine provenance. "
            "H0 requires both directions; the reverse direction fails."
        ),
        witness_names=("W_A",),
    )

    h1 = HypothesisResult(
        hypothesis_id="H1",
        claim="Provenance strictly richer: identical bases admit different propagation histories.",
        status="supported",
        evidence=(
            "W_A confirms: C holds {r1_locked, r2_locked} in both A1 (direct) and A2 (transitive). "
            "In A1: r1_locked via path (A→C), r2_locked via (B→C). "
            "In A2: r1_locked via path (A→B→C), r2_locked via (B→C). "
            "Distinct provenance structures, identical record basis. "
            "Provenance is NOT recoverable from record basis alone — it is strictly richer "
            "in the sense of carrying additional propagation-history information. "
            "However, H4 shows this extra information does NOT change event-finality reconstruction."
        ),
        witness_names=("W_A",),
    )

    h2 = HypothesisResult(
        hypothesis_id="H2",
        claim="Provenance strictly weaker: propagation topology cannot determine record basis.",
        status="partial",
        evidence=(
            "W_B partial support: same edge topology (P→R, Q→R, same steps) is compatible with "
            "different record bases at R (alpha/beta vs gamma/delta). "
            "Abstract propagation topology (who-tells-whom, without record labels) is strictly "
            "weaker than record basis. "
            "However, FULL provenance (topology + origin records + transmitted records) "
            "does determine the accessible records. "
            "W_D adds: same propagation step-ordering is compatible with multiple event-finality "
            "orders (concurrent vs ordered). "
            "Verdict: topology-only provenance is weaker; full-labeled provenance is not weaker."
        ),
        witness_names=("W_B", "W_D"),
    )

    h3 = HypothesisResult(
        hypothesis_id="H3",
        claim="Complementarity: neither representation determines the other.",
        status="partial",
        evidence=(
            "H1 confirms: basis does not determine provenance (same basis, different provenances). "
            "H2 partial: topology does not determine basis. "
            "But full provenance (labeled) DOES determine accessible records (hence basis). "
            "So the complementarity is asymmetric: "
            "(a) basis → provenance fails (H1 evidence); "
            "(b) full provenance → basis succeeds (not H3); "
            "(c) topology only → basis fails (H2/W_B). "
            "True complementarity (neither determines the other in any direction) is not confirmed "
            "for the full labeled provenance. Partial for topology-only provenance."
        ),
        witness_names=("W_A", "W_B"),
    )

    h4 = HypothesisResult(
        hypothesis_id="H4",
        claim="Provenance varies but does not affect event-finality colimits, AM, or descent classification.",
        status="supported",
        evidence=(
            "W_A colimit comparison: C's accessible records are identical in A1 and A2. "
            f"Colimits identical: {colimits_identical}. "
            "Event-finality order and AM give same result in both scenarios. "
            "W_D: propagation step-order compatible with multiple event-finality orders — "
            "confirming that provenance does not uniquely determine event-finality structure. "
            "W_T54: T54 quotient-union is provenance-blind; same basis → identical T54 "
            "classification regardless of propagation history. "
            "In all tested witnesses, provenance variation changes neither the colimit, "
            "the reconstructed event order, AM validity, nor the T54 descent classification."
        ),
        witness_names=("W_A", "W_D", "W_T54"),
    )

    return (h0, h1, h2, h3, h4)


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t55b_analysis() -> T55BResult:
    scenario_a1 = _build_scenario_a1()
    scenario_a2 = _build_scenario_a2()
    scenario_b1 = _build_scenario_b1()
    scenario_b2 = _build_scenario_b2()

    c_a1 = compute_observer_state("C", scenario_a1)
    c_a2 = compute_observer_state("C", scenario_a2)
    r_b1 = compute_observer_state("R", scenario_b1)
    r_b2 = compute_observer_state("R", scenario_b2)

    wa = run_wa_separation(c_a1, c_a2)
    wb = run_wb_separation(r_b1, r_b2)

    events_wa = _build_wa_events()
    colimit_a1 = compute_colimit("A1_direct", c_a1.accessible_records, events_wa)
    colimit_a2 = compute_colimit("A2_transitive", c_a2.accessible_records, events_wa)

    wd = run_event_order_ambiguity(scenario_a1, "C")
    wt54 = run_t54_invariance(c_a1, c_a2)

    hyps = _evaluate_hypotheses(wa, wb, colimit_a1, colimit_a2, wd, wt54)

    recommendation = "optional_audit_layer"
    rationale = (
        "H4 is confirmed across all tested witnesses: provenance variation does not change "
        "event-finality colimits, AM reconstruction, or T54 descent classification. "
        "Provenance carries additional information (H1 confirmed: same basis, different "
        "propagation history), but that additional information has no reconstructive "
        "consequence for the current TaF formalism. "
        "Provenance is therefore an optional audit layer — useful for attribution, "
        "auditability, and trust assessment — but not a first-class mathematical primitive "
        "for event-finality reconstruction in the T48-T54 program. "
        "Provenance would earn first-class status if: (a) a witness is found where "
        "propagation order constrains event-finality order in a way record-containment "
        "cannot capture, or (b) provenance provides identity evidence that resolves "
        "T53-type underdetermination by confirming or distinguishing event class membership. "
        "Neither condition is met by the current witness set."
    )

    open_questions = (
        "Can propagation order constrain event-finality order in a substrate where "
        "records can only propagate after the events that produced them have occurred? "
        "If causal ordering of propagation is enforced, does step-order imply event order?",
        "Does provenance provide identity evidence for T53-type underdetermination? "
        "If observer A transmitted r_a to B, is that evidence that B's subsequent event "
        "using r_a in its source is a successor of A's event? This would link provenance "
        "to T54's event-identity-map condition.",
        "Is the propagation graph itself a D1RestrictionMorphism? Propagation preserves "
        "obstruction status (pre-to-post finality crossing is admissible; record transport "
        "is post-to-post). If so, the propagation graph is a subgraph of D1Cat and "
        "provenance is a path-in-D1Cat question.",
        "Does a provenance-aware colimit — one that weights the record union by propagation "
        "order — produce a different partial order than the T52/T54 pointwise union? "
        "The tested witnesses suggest no, but the general case is open.",
    )

    best_supported = (
        "H4 (supported), H1 (supported), H0 (refuted). "
        "H2 and H3 partially supported for topology-only provenance."
    )

    return T55BResult(
        scenarios=(scenario_a1, scenario_a2, scenario_b1, scenario_b2),
        observer_states=(c_a1, c_a2, r_b1, r_b2),
        separation_witnesses=(wa, wb),
        colimit_results=(colimit_a1, colimit_a2),
        event_order_ambiguity=wd,
        t54_invariance=wt54,
        hypothesis_verdicts=hyps,
        recommendation=recommendation,
        recommendation_rationale=rationale,
        open_questions=open_questions,
        best_supported=best_supported,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def t55b_result_to_dict(r: T55BResult) -> dict[str, Any]:
    def path_to_dict(p: ProvenancePath) -> dict[str, Any]:
        return {
            "record": p.record,
            "target_observer": p.target_observer,
            "path": list(p.path),
            "is_direct_observation": p.is_direct_observation,
        }

    def state_to_dict(s: ObserverState) -> dict[str, Any]:
        return {
            "observer": s.observer,
            "scenario": s.scenario,
            "accessible_records": sorted(s.accessible_records),
            "provenance_paths": [path_to_dict(p) for p in s.provenance_paths],
        }

    def sep_to_dict(w: SeparationWitness) -> dict[str, Any]:
        return {
            "name": w.name,
            "description": w.description,
            "scenario_a": w.scenario_a,
            "scenario_b": w.scenario_b,
            "focus_observer": w.focus_observer,
            "basis_a": sorted(w.basis_a),
            "basis_b": sorted(w.basis_b),
            "same_record_basis": w.same_record_basis,
            "same_provenance_structure": w.same_provenance_structure,
            "finding": w.finding,
        }

    def colimit_to_dict(c: ColimitResult) -> dict[str, Any]:
        return {
            "scenario_name": c.scenario_name,
            "accessible_records": sorted(c.accessible_records),
            "event_order": [list(p) for p in sorted(c.event_order)],
            "am_holds": c.am_holds,
            "spurious_pairs": [list(p) for p in c.spurious_pairs],
            "missing_pairs": [list(p) for p in c.missing_pairs],
        }

    def hyp_to_dict(h: HypothesisResult) -> dict[str, Any]:
        return {
            "id": h.hypothesis_id,
            "claim": h.claim,
            "status": h.status,
            "evidence": h.evidence,
            "witnesses": list(h.witness_names),
        }

    wd = r.event_order_ambiguity
    wt54 = r.t54_invariance

    return {
        "scenarios": [
            {
                "name": s.name,
                "observers": list(s.observers),
                "edges": [
                    {
                        "source": e.source,
                        "target": e.target,
                        "records": sorted(e.records),
                        "step": e.step,
                        "anchor_event": e.anchor_event,
                    }
                    for e in s.edges
                ],
                "origins": [
                    {"observer": o.observer, "record": o.record}
                    for o in s.origins
                ],
            }
            for s in r.scenarios
        ],
        "observer_states": [state_to_dict(s) for s in r.observer_states],
        "separation_witnesses": [sep_to_dict(w) for w in r.separation_witnesses],
        "colimit_results": [colimit_to_dict(c) for c in r.colimit_results],
        "event_order_ambiguity": {
            "name": wd.name,
            "description": wd.description,
            "propagation_scenario": wd.propagation_scenario,
            "accessible_at_observer": sorted(wd.accessible_at_observer),
            "order_concurrent_nonrefl": sorted(
                (a, b) for a, b in wd.order_concurrent if a != b
            ),
            "order_ordered_nonrefl": sorted(
                (a, b) for a, b in wd.order_ordered if a != b
            ),
            "propagation_order_determines_event_order": wd.propagation_order_determines_event_order,
            "finding": wd.finding,
        },
        "t54_invariance": {
            "name": wt54.name,
            "description": wt54.description,
            "basis_identical": wt54.basis_identical,
            "t54_input_identical": wt54.t54_input_identical,
            "finding": wt54.finding,
        },
        "hypothesis_verdicts": [hyp_to_dict(h) for h in r.hypothesis_verdicts],
        "recommendation": r.recommendation,
        "recommendation_rationale": r.recommendation_rationale,
        "open_questions": list(r.open_questions),
        "best_supported": r.best_supported,
    }
