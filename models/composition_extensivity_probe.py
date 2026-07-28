"""Composition/extensivity probe: un-T-numbered exploration companion.

Executes the rho_1 witness and the full check slate specified by the reopening
packet `explorations/proposed-composition-extensivity-gate-2026-07-28.md`, via
that packet's own fallback path: "run the rho_1 witness of the Setup as an
un-T-numbered exploration companion (the same discipline as the wave-3 note's
overlay model) and re-submit this packet with the run attached." No T-number
is minted here; the owner mints the number and decides adoption.

The probe composes two (and, for associativity, three) T585-class declared
contexts under the packet's declared parallel composition clause:

- intensive fields (source theory, bath temperature, time budget as one
  equal-and-shared window, error bound, horizon) must be equal, fail closed;
- extensive budgets (energy, communication, memory) add under a declared
  partition, with each namespace's tasks charged only against its own share;
- task and record vocabularies are tagged (namespaced) disjoint unions;
- records are always issued into the producing component's namespace; a
  declared consumption rule rho governs cross-namespace consumption only.

Firebreak (inherited from T587's boundary typing): Delta, like any capability
delta, is never counted as a record-order edge, an issuance, or a temporal
quantity by itself. Nothing here derives time, temporal order, or issuance.
Deterministic pure-stdlib run: no randomness, no wall-clock or date values in
the output.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, replace
from typing import Any, Iterable

from models import t583_capability_contract_v1 as t583
from models import t585_landauer_physical_capability_gate as t585


ARTIFACT = "composition-extensivity-probe-exploration-companion-v0.1"
STATUS = "UN_T_NUMBERED_EXPLORATION_COMPANION_REVIEW_ONLY"
EXIT_A = "EXIT_A_INDEPENDENT_ENVELOPE_EXTENSIVITY_HOLDS"
EXIT_B = "EXIT_B_ADDITIVITY_OR_T584_EXTENSION_FAILS"
NO_TEETH = "GATE_WITHOUT_TEETH_CONTROL_DID_NOT_FAIL"

ERASE_TASK = "erase_to_standard_record"
CERTIFY_TASK = "certify_record_stability"
CROSS_TASK = "certify_cross_record_stability"
STANDARD_RECORD = "r_erased_standard"

FIREBREAK_STATEMENT = (
    "Delta, like any capability delta, is never counted as a record-order "
    "edge, an issuance, or a temporal quantity by itself; the record layer "
    "acts only as a typed record-prerequisite filter on executable tasks."
)


@dataclass(frozen=True)
class DeclaredCell:
    """One T585-class declared context with its declared thermal access datum."""

    namespace: str
    bath_temperature_kelvin: float
    context: t583.CapabilityContext
    state: t585.MemoryState
    representation: str = "normalized"


@dataclass(frozen=True)
class CouplingEdge:
    """One declared rho edge: cross-namespace record consumption only."""

    record_id: str
    producer_namespace: str
    consumer_namespace: str
    consumer_task: str


@dataclass(frozen=True)
class CompositionRejection:
    reason_class: str
    detail: str


@dataclass(frozen=True)
class CompositeContext:
    composite_id: str
    components: tuple[DeclaredCell, ...]
    rho: tuple[CouplingEdge, ...]
    shared_source_theory: str
    bath_temperature_kelvin: float
    shared_time_budget: float
    shared_error_bound: float
    shared_horizon: str
    tagging: str


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


@dataclass(frozen=True)
class ControlResult:
    control_id: str
    must_fail_mode: str
    failed_closed: bool
    detail: str


# ---------------------------------------------------------------------------
# Cell and state constructors (T585 fixture class, unchanged physics)
# ---------------------------------------------------------------------------


def make_state(kind: str, namespace: str, gauge_swapped: bool = False) -> t585.MemoryState:
    p_by_kind = {"known": 0.0, "biased": 0.10, "max_entropy": 0.50}
    p = p_by_kind[kind]
    if gauge_swapped:
        return t585.MemoryState(
            f"{kind}_record_bit_label_swapped",
            round(1.0 - p, 9),
            True,
            "bit_label_swapped",
            f"{kind}-swapped",
            f"S-{namespace}-swapped",
        )
    return t585.MemoryState(
        f"{kind}_record", p, True, "canonical", kind, f"S-{namespace}"
    )


def make_cell(
    namespace: str,
    state: t585.MemoryState,
    *,
    energy: float = 0.75,
    time: float = 5.0,
    error: float = 0.01,
    bath_temperature_kelvin: float = t585.REFERENCE_TEMPERATURE_K,
    horizon: str = "single_reset_cycle",
    source_theory: str | None = None,
    region_id: str | None = None,
    representation: str = "normalized",
) -> DeclaredCell:
    base = t585._base_context()  # fixture reused unchanged, house precedent
    context = replace(
        base,
        context_id=f"ctx_cell_{namespace}",
        region_id=region_id or f"R_cell_{namespace}",
        observer_id=f"O_cell_{namespace}",
        resource_provenance=f"fixed_thermal_bath_and_work_store::{namespace}",
        budget=replace(base.budget, energy=energy, time=time, error=error),
        horizon=horizon,
        source_theory=source_theory or base.source_theory,
    )
    return DeclaredCell(namespace, bath_temperature_kelvin, context, state, representation)


# ---------------------------------------------------------------------------
# The composition clause: intensive restriction fail-closed, extensive
# partition, tagged unions, declared rho
# ---------------------------------------------------------------------------


def _flatten(parts: Iterable[DeclaredCell | CompositeContext]) -> tuple[
    tuple[DeclaredCell, ...], tuple[CouplingEdge, ...]
]:
    cells: list[DeclaredCell] = []
    rho: list[CouplingEdge] = []
    for part in parts:
        if isinstance(part, CompositeContext):
            cells.extend(part.components)
            rho.extend(part.rho)
        else:
            cells.append(part)
    return tuple(cells), tuple(rho)


def compose(
    *parts: DeclaredCell | CompositeContext,
    rho: tuple[CouplingEdge, ...] = (),
    tagging: str = "namespaced",
) -> CompositeContext | CompositionRejection:
    cells, inherited_rho = _flatten(parts)
    all_rho = tuple(inherited_rho) + tuple(rho)

    if tagging == "untagged":
        vocabularies = [set(cell.context.task_family) for cell in cells]
        for i in range(len(vocabularies)):
            for j in range(i + 1, len(vocabularies)):
                shared = sorted(vocabularies[i] & vocabularies[j])
                if shared:
                    return CompositionRejection(
                        "UNTAGGED_NAMESPACE_COLLISION",
                        "untagged task/record vocabulary merge collides on "
                        f"{shared}; the merge changes the native envelope and "
                        "is inadmissible (T584 merge-counterexample descendant)",
                    )
    namespaces = [cell.namespace for cell in cells]
    if len(set(namespaces)) != len(namespaces):
        return CompositionRejection(
            "DUPLICATE_NAMESPACE", f"namespaces not distinct: {sorted(namespaces)}"
        )
    regions = [cell.context.region_id for cell in cells]
    if len(set(regions)) != len(regions):
        return CompositionRejection(
            "OVERLAPPING_REGIONS",
            f"regions must be a declared disjoint union, got {sorted(regions)}",
        )
    source_theories = sorted({cell.context.source_theory for cell in cells})
    if len(source_theories) != 1:
        return CompositionRejection(
            "SOURCE_THEORY_MISMATCH", f"distinct source theories: {source_theories}"
        )
    baths = sorted({cell.bath_temperature_kelvin for cell in cells})
    if len(baths) != 1:
        return CompositionRejection(
            "UNEQUAL_BATH_TEMPERATURE",
            f"declared bath temperatures {baths} K are unequal; composition is "
            "rejected, not silently unit-normalized (unequal-T admits a "
            "heat-engine channel that would contaminate Delta)",
        )
    times = sorted({cell.context.budget.time for cell in cells})
    if len(times) != 1:
        return CompositionRejection(
            "TIME_WINDOW_MISMATCH",
            f"time budget is one equal-and-shared window; got {times} "
            "(summing would model serial scheduling; max would hand undeclared slack)",
        )
    errors = sorted({cell.context.budget.error for cell in cells})
    if len(errors) != 1:
        return CompositionRejection(
            "ERROR_BOUND_MISMATCH", f"distinct error bounds: {errors}"
        )
    horizons = sorted({cell.context.horizon for cell in cells})
    if len(horizons) != 1:
        return CompositionRejection(
            "HORIZON_MISMATCH", f"distinct horizons: {horizons}"
        )
    for edge in all_rho:
        if edge.producer_namespace not in namespaces or edge.consumer_namespace not in namespaces:
            return CompositionRejection(
                "RHO_EDGE_UNKNOWN_NAMESPACE", f"edge references unknown namespace: {edge}"
            )
        if edge.producer_namespace == edge.consumer_namespace:
            return CompositionRejection(
                "RHO_EDGE_NOT_CROSS_NAMESPACE",
                f"rho governs cross-namespace consumption only: {edge}",
            )
        if not edge.record_id.startswith(f"{edge.producer_namespace}::"):
            return CompositionRejection(
                "SILENT_REISSUE_ACROSS_BOUNDARY",
                "records are always issued into the producing component's "
                f"namespace; edge {edge} tries to issue "
                f"{edge.record_id} outside producer {edge.producer_namespace}",
            )
    return CompositeContext(
        composite_id="ctx_composite(" + "+".join(namespaces) + ")"
        + (f"|rho={len(all_rho)}" if all_rho else ""),
        components=cells,
        rho=tuple(sorted(all_rho, key=lambda e: (e.record_id, e.consumer_namespace))),
        shared_source_theory=source_theories[0],
        bath_temperature_kelvin=baths[0],
        shared_time_budget=times[0],
        shared_error_bound=errors[0],
        shared_horizon=horizons[0],
        tagging=tagging,
    )


# ---------------------------------------------------------------------------
# Envelopes: components via T585's own machinery, composites via the clause
# ---------------------------------------------------------------------------


def component_envelope(cell: DeclaredCell) -> t583.CapabilityEnvelope:
    return t585.envelope_for(
        context=cell.context,
        state=cell.state,
        state_id=f"{cell.namespace}::{cell.state.state_id}",
        representation=cell.representation,
    )


def iota_points(
    envelope: t583.CapabilityEnvelope, namespace: str
) -> tuple[t583.PerformancePoint, ...]:
    """The embedding iota_i on envelope points: namespace the task identifiers."""
    return tuple(
        replace(point, task_id=f"{namespace}::{point.task_id}")
        for point in envelope.points
    )


def _sort_points(points: Iterable[t583.PerformancePoint]) -> tuple[t583.PerformancePoint, ...]:
    return tuple(
        sorted(
            points,
            key=lambda point: (
                point.task_id,
                -point.success,
                point.energy_cost,
                point.time_cost,
                point.communication_cost,
                point.memory_cost,
                point.error,
            ),
        )
    )


def oplus_points(cells: Iterable[DeclaredCell]) -> tuple[t583.PerformancePoint, ...]:
    """Env(C1) (+) Env(C2): namespaced disjoint union of canonical frontiers."""
    merged: list[t583.PerformancePoint] = []
    for cell in cells:
        merged.extend(iota_points(component_envelope(cell), cell.namespace))
    return _sort_points(merged)


def _share_budget(cell: DeclaredCell, composite: CompositeContext) -> t583.Budget:
    """The component's declared extensive share plus the shared intensive data."""
    return replace(
        cell.context.budget,
        time=composite.shared_time_budget,
        error=composite.shared_error_bound,
    )


def _cross_point() -> t583.PerformancePoint:
    """Declared performance point for the cross-record certification task."""
    return t583.PerformancePoint(
        CROSS_TASK,
        success=0.995,
        energy_cost=0.05,
        time_cost=0.2,
        communication_cost=0.1,
        memory_cost=0.1,
        error=0.002,
        protocol_id="cross_stability_readout",
    )


def _erase_feasible(cell: DeclaredCell, composite: CompositeContext) -> bool:
    raw = t585._points_for_state(
        context=cell.context,
        state=cell.state,
        observer_mode="state_aware",
        representation=cell.representation,
    )
    share = _share_budget(cell, composite)
    return any(
        point.task_id == ERASE_TASK
        and t583.point_is_feasible(point.canonical(), share)
        for point in raw
    )


def _register_unique_producer(
    producers: dict[str, str], record_id: str, event: str
) -> None:
    """T586's unique-producer discipline: a record has exactly one producer."""
    if record_id in producers:
        raise ValueError(f"record produced twice: {record_id}")
    producers[record_id] = event


def attainable_producers(composite: CompositeContext) -> dict[str, str]:
    """Unique-producer map (T586 mechanism): record -> producing event.

    A record exists only when its unique producer (the namespace's erase
    event) is actually executable inside that namespace's declared share.
    Issuance is always into the producing component's namespace.
    """
    producers: dict[str, str] = {}
    for cell in composite.components:
        if _erase_feasible(cell, composite):
            _register_unique_producer(
                producers,
                f"{cell.namespace}::{STANDARD_RECORD}",
                f"{cell.namespace}::erase_standard_record",
            )
    return producers


def executable_cross_tasks(composite: CompositeContext) -> tuple[tuple[str, str, str], ...]:
    """(consumer namespace, task, record) for rho edges with attainable producers."""
    producers = attainable_producers(composite)
    admitted = [
        (edge.consumer_namespace, edge.consumer_task, edge.record_id)
        for edge in composite.rho
        if edge.record_id in producers
    ]
    return tuple(sorted(admitted))


def composite_envelope(
    composite: CompositeContext, *, inject_unlicensed_cross_point: bool = False
) -> t583.CapabilityEnvelope:
    candidates: list[t583.PerformancePoint] = []
    for cell in composite.components:
        raw = t585._points_for_state(
            context=cell.context,
            state=cell.state,
            observer_mode="state_aware",
            representation=cell.representation,
        )
        aliases = {task: f"{cell.namespace}::{task}" for task in cell.context.task_family}
        family = set(aliases.values())
        share = _share_budget(cell, composite)
        for point in raw:
            canonical = point.canonical(aliases)
            if canonical.task_id in family and t583.point_is_feasible(canonical, share):
                candidates.append(canonical)
    licensed_family: set[str] = set()
    for namespace, task, _record in executable_cross_tasks(composite):
        licensed_family.add(f"{namespace}::{task}")
        cell = _cell_by_namespace(composite, namespace)
        canonical = _cross_point().canonical({CROSS_TASK: f"{namespace}::{task}"})
        if t583.point_is_feasible(canonical, _share_budget(cell, composite)):
            candidates.append(canonical)
    if inject_unlicensed_cross_point:
        # Probe: a cross point smuggled in without a declared rho edge must be
        # inadmissible because its task is not in the composite task family
        # (namespaced component union plus rho-licensed cross tasks only).
        declared_family = {
            f"{cell.namespace}::{task}"
            for cell in composite.components
            for task in cell.context.task_family
        } | licensed_family
        for cell in composite.components:
            smuggled = _cross_point().canonical(
                {CROSS_TASK: f"{cell.namespace}::{CROSS_TASK}"}
            )
            if smuggled.task_id in declared_family and t583.point_is_feasible(
                smuggled, _share_budget(cell, composite)
            ):
                candidates.append(smuggled)
    frontier = [
        point
        for point in candidates
        if not any(
            t583.point_strictly_dominates(other, point)
            for other in candidates
            if other is not point
        )
    ]
    return t583.CapabilityEnvelope(
        context_id=composite.composite_id,
        state_id="+".join(
            f"{cell.namespace}::{cell.state.state_id}" for cell in composite.components
        ),
        native_structure="task_indexed_pareto_preorder",
        points=_sort_points(frontier),
    )


def _cell_by_namespace(composite: CompositeContext, namespace: str) -> DeclaredCell:
    for cell in composite.components:
        if cell.namespace == namespace:
            return cell
    raise KeyError(namespace)


def restrict_points(
    points: Iterable[t583.PerformancePoint], namespace: str
) -> tuple[t583.PerformancePoint, ...]:
    return tuple(p for p in points if p.task_id.startswith(f"{namespace}::"))


# ---------------------------------------------------------------------------
# Order-level machinery: dominations, incomparability, the deviation Delta
# ---------------------------------------------------------------------------


def point_key(point: t583.PerformancePoint) -> tuple[Any, ...]:
    return (
        point.task_id,
        point.success,
        point.energy_cost,
        point.time_cost,
        point.communication_cost,
        point.memory_cost,
        point.error,
    )


def dominations(points: Iterable[t583.PerformancePoint]) -> tuple[tuple[Any, ...], ...]:
    pts = tuple(points)
    return tuple(
        sorted(
            (point_key(a), point_key(b))
            for a in pts
            for b in pts
            if point_key(a) != point_key(b) and t583.point_covers(a, b)
        )
    )


def incomparable_pairs(points: Iterable[t583.PerformancePoint]) -> tuple[tuple[Any, ...], ...]:
    pts = tuple(points)
    seen: set[tuple[Any, ...]] = set()
    out: list[tuple[Any, ...]] = []
    for a in pts:
        for b in pts:
            ka, kb = point_key(a), point_key(b)
            if ka >= kb:
                continue
            if not t583.point_covers(a, b) and not t583.point_covers(b, a):
                pair = (ka, kb)
                if pair not in seen:
                    seen.add(pair)
                    out.append(pair)
    return tuple(sorted(out))


def deviation(composite: CompositeContext) -> dict[str, Any]:
    """Delta(rho): canonical frontier points and induced dominations of the
    coupled composite absent from the namespaced (+) of component envelopes."""
    coupled = composite_envelope(composite).points
    base = oplus_points(composite.components)
    base_keys = {point_key(p) for p in base}
    coupled_keys = {point_key(p) for p in coupled}
    extra_points = tuple(p for p in coupled if point_key(p) not in base_keys)
    lost_points = tuple(p for p in base if point_key(p) not in coupled_keys)
    extra_dominations = tuple(
        sorted(set(dominations(coupled)) - set(dominations(base)))
    )
    return {
        "extra_points": extra_points,
        "lost_points": lost_points,
        "extra_dominations": extra_dominations,
    }


def deviation_is_empty(delta: dict[str, Any]) -> bool:
    return not delta["extra_points"] and not delta["lost_points"] and not delta["extra_dominations"]


def deviation_subset(smaller: dict[str, Any], larger: dict[str, Any]) -> bool:
    small_points = {point_key(p) for p in smaller["extra_points"]}
    large_points = {point_key(p) for p in larger["extra_points"]}
    small_dom = set(smaller["extra_dominations"])
    large_dom = set(larger["extra_dominations"])
    return small_points <= large_points and small_dom <= large_dom


def rho_1(ns_producer: str, ns_consumer: str) -> tuple[CouplingEdge, ...]:
    return (
        CouplingEdge(
            record_id=f"{ns_producer}::{STANDARD_RECORD}",
            producer_namespace=ns_producer,
            consumer_namespace=ns_consumer,
            consumer_task=CROSS_TASK,
        ),
    )


def rho_2(ns_a: str, ns_b: str) -> tuple[CouplingEdge, ...]:
    return rho_1(ns_a, ns_b) + rho_1(ns_b, ns_a)


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def _points_summary(points: Iterable[t583.PerformancePoint]) -> list[dict[str, Any]]:
    return [asdict(point) for point in points]


def _expect_rejection(
    candidate: CompositeContext | CompositionRejection, reason_class: str
) -> tuple[bool, str]:
    if isinstance(candidate, CompositionRejection):
        return candidate.reason_class == reason_class, candidate.reason_class
    return False, "COMPOSITION_ACCEPTED"


def run_analysis() -> dict[str, Any]:
    # ---- source fixture provenance (re-executed, not cached) ----
    source = t585.run_t585_analysis()
    source_check = Check(
        "t585_source_available",
        source.verdict == t585.VERDICT,
        "T585 re-executed as the source-owned physical capability fixture class.",
    )

    ns1, ns2, ns3 = "ns1", "ns2", "ns3"

    def witness_cells() -> tuple[DeclaredCell, DeclaredCell]:
        return (
            make_cell(ns1, make_state("biased", ns1), energy=0.75),
            make_cell(ns2, make_state("biased", ns2), energy=0.75),
        )

    cell1, cell2 = witness_cells()

    # ---- intensive restriction: every mutation must fail closed ----
    mutations: list[tuple[str, DeclaredCell | CompositeContext | CompositionRejection, str]] = []
    mutations.append(
        (
            "unequal_bath_temperature",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), bath_temperature_kelvin=350.0)),
            "UNEQUAL_BATH_TEMPERATURE",
        )
    )
    mutations.append(
        (
            "unequal_time_budget",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), time=7.0)),
            "TIME_WINDOW_MISMATCH",
        )
    )
    mutations.append(
        (
            "unequal_error_bound",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), error=0.05)),
            "ERROR_BOUND_MISMATCH",
        )
    )
    mutations.append(
        (
            "unequal_horizon",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), horizon="double_cycle")),
            "HORIZON_MISMATCH",
        )
    )
    mutations.append(
        (
            "unequal_source_theory",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), source_theory="other_law")),
            "SOURCE_THEORY_MISMATCH",
        )
    )
    mutations.append(
        (
            "overlapping_regions",
            compose(cell1, make_cell(ns2, make_state("biased", ns2), region_id="R_cell_ns1")),
            "OVERLAPPING_REGIONS",
        )
    )
    mutations.append(
        (
            "duplicate_namespace",
            compose(cell1, make_cell(ns1, make_state("known", ns1))),
            "DUPLICATE_NAMESPACE",
        )
    )
    intensive_rows = []
    intensive_all_fail_closed = True
    for mutation_id, outcome, expected in mutations:
        ok, got = _expect_rejection(outcome, expected)
        intensive_all_fail_closed = intensive_all_fail_closed and ok
        intensive_rows.append(
            {"mutation": mutation_id, "expected": expected, "got": got, "fail_closed": ok}
        )

    # ---- extensivity grid on independent composites ----
    state_kinds = ("biased", "known", "max_entropy")
    energies = (0.30, 0.75)
    grid_rows: list[str] = []
    grid_failures: list[str] = []
    grid_total = 0
    grid_equal = 0
    delta_rho1_nonempty = 0
    delta_rho2_nonempty = 0
    monotone_all = True
    delta_empty_iff_extensivity = True
    producer_gating_consistent = True
    for kind1 in state_kinds:
        for e1 in energies:
            for kind2 in state_kinds:
                for e2 in energies:
                    grid_total += 1
                    a = make_cell(ns1, make_state(kind1, ns1), energy=e1)
                    b = make_cell(ns2, make_state(kind2, ns2), energy=e2)
                    independent = compose(a, b)
                    assert isinstance(independent, CompositeContext)
                    env = composite_envelope(independent).points
                    base = oplus_points((a, b))
                    equal_bitwise = env == base
                    dom_equal = dominations(env) == dominations(base)
                    inc_equal = incomparable_pairs(env) == incomparable_pairs(base)
                    no_cross_dom = not any(
                        pair[0][0].split("::")[0] != pair[1][0].split("::")[0]
                        for pair in dominations(env)
                    )
                    delta0 = deviation(independent)
                    coupled1 = compose(a, b, rho=rho_1(ns1, ns2))
                    coupled2 = compose(a, b, rho=rho_2(ns1, ns2))
                    assert isinstance(coupled1, CompositeContext)
                    assert isinstance(coupled2, CompositeContext)
                    d1 = deviation(coupled1)
                    d2 = deviation(coupled2)
                    if not deviation_is_empty(d1):
                        delta_rho1_nonempty += 1
                    if not deviation_is_empty(d2):
                        delta_rho2_nonempty += 1
                    monotone = deviation_subset(d1, d2)
                    monotone_all = monotone_all and monotone
                    if deviation_is_empty(delta0) != (equal_bitwise and dom_equal and inc_equal):
                        delta_empty_iff_extensivity = False
                    # rho_1 gating: nonempty exactly when ns1's erase is
                    # feasible in its declared share (attainable producer)
                    producer_ok = _erase_feasible(a, independent)
                    if (not deviation_is_empty(d1)) != producer_ok:
                        producer_gating_consistent = False
                    ok = equal_bitwise and dom_equal and inc_equal and no_cross_dom
                    if ok:
                        grid_equal += 1
                    else:
                        grid_failures.append(
                            f"{kind1}@{e1}|{kind2}@{e2} equal={equal_bitwise} "
                            f"dom={dom_equal} inc={inc_equal} nocross={no_cross_dom}"
                        )
                    grid_rows.append(
                        f"{kind1}@{e1}|{kind2}@{e2} equal={equal_bitwise} "
                        f"delta_rho1={len(d1['extra_points'])} "
                        f"delta_rho2={len(d2['extra_points'])} monotone={monotone}"
                    )
    extensivity_holds = grid_equal == grid_total and intensive_all_fail_closed

    # ---- the rho_1 witness: the contract question, made concrete ----
    independent = compose(cell1, cell2)
    coupled1 = compose(cell1, cell2, rho=rho_1(ns1, ns2))
    coupled2 = compose(cell1, cell2, rho=rho_2(ns1, ns2))
    assert isinstance(independent, CompositeContext)
    assert isinstance(coupled1, CompositeContext)
    assert isinstance(coupled2, CompositeContext)
    env_independent = composite_envelope(independent)
    env_coupled1 = composite_envelope(coupled1)
    env_coupled2 = composite_envelope(coupled2)
    witness_delta1 = deviation(coupled1)
    witness_delta2 = deviation(coupled2)
    reissue_attempt = compose(
        cell1,
        cell2,
        rho=(
            CouplingEdge(
                record_id=f"{ns2}::{STANDARD_RECORD}",
                producer_namespace=ns1,
                consumer_namespace=ns2,
                consumer_task=CROSS_TASK,
            ),
        ),
    )
    reissue_rejected, reissue_reason = _expect_rejection(
        reissue_attempt, "SILENT_REISSUE_ACROSS_BOUNDARY"
    )
    same_ns_edge = compose(
        cell1,
        cell2,
        rho=(
            CouplingEdge(
                record_id=f"{ns1}::{STANDARD_RECORD}",
                producer_namespace=ns1,
                consumer_namespace=ns1,
                consumer_task=CROSS_TASK,
            ),
        ),
    )
    same_ns_rejected, same_ns_reason = _expect_rejection(
        same_ns_edge, "RHO_EDGE_NOT_CROSS_NAMESPACE"
    )
    smuggle_env = composite_envelope(independent, inject_unlicensed_cross_point=True)
    smuggle_blocked = smuggle_env.points == env_independent.points
    starved_producer = compose(
        make_cell(ns1, make_state("biased", ns1), energy=0.30),
        make_cell(ns2, make_state("biased", ns2), energy=0.75),
        rho=rho_1(ns1, ns2),
    )
    assert isinstance(starved_producer, CompositeContext)
    starved_delta = deviation(starved_producer)
    duplicate_producer_guard = False
    try:
        guard_probe: dict[str, str] = {}
        _register_unique_producer(guard_probe, STANDARD_RECORD, f"{ns1}::erase_standard_record")
        _register_unique_producer(guard_probe, STANDARD_RECORD, f"{ns2}::erase_standard_record")
    except ValueError:
        duplicate_producer_guard = True
    witness = {
        "contract_question": (
            "when declared contexts compose, into which namespace is a record "
            "issued, and which tasks may consume records across the composite "
            "boundary?"
        ),
        "scenarios": [
            {
                "answer": "issued into producer namespace; no cross consumption (rho empty)",
                "cross_task_executable": False,
                "frontier_size": len(env_independent.points),
                "delta_points": 0,
            },
            {
                "answer": "issued into producer namespace; ns2 may consume ns1 record (rho_1)",
                "cross_task_executable": bool(executable_cross_tasks(coupled1)),
                "frontier_size": len(env_coupled1.points),
                "delta_points": len(witness_delta1["extra_points"]),
            },
            {
                "answer": "issued into producer namespace; symmetric consumption (rho_2)",
                "cross_task_executable": bool(executable_cross_tasks(coupled2)),
                "frontier_size": len(env_coupled2.points),
                "delta_points": len(witness_delta2["extra_points"]),
            },
            {
                "answer": "record silently re-namespaced across the boundary",
                "cross_task_executable": None,
                "frontier_size": None,
                "delta_points": None,
                "rejected": reissue_reason,
            },
            {
                "answer": "rho_1 declared but producer starved (ns1 share 0.30 < reset cost)",
                "cross_task_executable": bool(executable_cross_tasks(starved_producer)),
                "frontier_size": len(composite_envelope(starved_producer).points),
                "delta_points": len(starved_delta["extra_points"]),
            },
        ],
        "delta_rho1_points": _points_summary(witness_delta1["extra_points"]),
        "delta_rho1_extra_dominations": [
            [list(a), list(b)] for a, b in witness_delta1["extra_dominations"]
        ],
        "unlicensed_cross_consumption_blocked": smuggle_blocked,
        "same_namespace_rho_edge_rejected": same_ns_rejected,
        "unique_producer_guard_active": duplicate_producer_guard,
    }
    witness_ok = (
        deviation_is_empty(deviation(independent))
        and len(witness_delta1["extra_points"]) == 1
        and witness_delta1["extra_points"][0].task_id == f"{ns2}::{CROSS_TASK}"
        and not witness_delta1["lost_points"]
        and len(witness_delta2["extra_points"]) == 2
        and deviation_subset(witness_delta1, witness_delta2)
        and reissue_rejected
        and same_ns_rejected
        and smuggle_blocked
        and deviation_is_empty(starved_delta)
        and duplicate_producer_guard
    )

    # ---- T584 morphism legs on composites ----
    baseline_points = env_independent.points
    joule1 = make_cell(ns1, make_state("biased", ns1), representation="joule")
    rep_composite = compose(joule1, cell2)
    assert isinstance(rep_composite, CompositeContext)
    representation_preserved = composite_envelope(rep_composite).points == baseline_points

    swapped2 = make_cell(ns2, make_state("biased", ns2, gauge_swapped=True))
    gauge_composite = compose(cell1, swapped2)
    assert isinstance(gauge_composite, CompositeContext)
    gauge_preserved = composite_envelope(gauge_composite).points == baseline_points

    coarse_state = replace(
        make_state("biased", ns2), display_label="coarse", sensor_serial="S-Z"
    )
    coarse2 = make_cell(ns2, coarse_state)
    coarse_composite = compose(cell1, coarse2)
    assert isinstance(coarse_composite, CompositeContext)
    coarse_env_preserved = composite_envelope(coarse_composite).points == baseline_points
    coarse_payload_preserved = t585.projected_metadata(
        coarse_state, coarse2.context
    ) == t585.projected_metadata(make_state("biased", ns2), cell2.context)

    both_morphed = compose(joule1, swapped2)
    assert isinstance(both_morphed, CompositeContext)
    interchange_env = composite_envelope(both_morphed).points
    interchange_preserves = interchange_env == baseline_points
    interchange_square = all(
        restrict_points(interchange_env, cell.namespace)
        == iota_points(component_envelope(cell), cell.namespace)
        for cell in (joule1, swapped2)
    ) and all(
        iota_points(component_envelope(morphed), morphed.namespace)
        == iota_points(component_envelope(orig), orig.namespace)
        for morphed, orig in ((joule1, cell1), (swapped2, cell2))
    )

    swapped_order = compose(cell2, cell1)
    assert isinstance(swapped_order, CompositeContext)
    swap_symmetry = composite_envelope(swapped_order).points == baseline_points

    cell3 = make_cell(ns3, make_state("known", ns3), energy=0.75)
    left_assoc = compose(compose(cell1, cell2), cell3)
    right_assoc = compose(cell1, compose(cell2, cell3))
    assert isinstance(left_assoc, CompositeContext)
    assert isinstance(right_assoc, CompositeContext)
    associativity = (
        composite_envelope(left_assoc).points == composite_envelope(right_assoc).points
    )

    strong1 = make_cell(ns1, make_state("known", ns1), energy=0.75)
    weak1 = make_cell(ns1, make_state("max_entropy", ns1), energy=0.75)
    strong2 = make_cell(ns2, make_state("biased", ns2), energy=0.75)
    weak2 = make_cell(ns2, make_state("biased", ns2), energy=0.30)
    component_premise = t583.envelope_covers(
        component_envelope(strong1), component_envelope(weak1)
    ) and t583.envelope_covers(component_envelope(strong2), component_envelope(weak2))
    big = compose(strong1, strong2)
    small = compose(weak1, weak2)
    assert isinstance(big, CompositeContext)
    assert isinstance(small, CompositeContext)
    order_compatibility = component_premise and t583.envelope_covers(
        composite_envelope(big), composite_envelope(small)
    )

    restriction_independent = all(
        restrict_points(baseline_points, cell.namespace)
        == iota_points(component_envelope(cell), cell.namespace)
        for cell in (cell1, cell2)
    )
    coupled_points = env_coupled1.points
    r2 = restrict_points(coupled_points, ns2)
    i2 = iota_points(component_envelope(cell2), ns2)
    restriction_coupled = (
        restrict_points(coupled_points, ns1)
        == iota_points(component_envelope(cell1), ns1)
        and all(any(t583.point_covers(a, b) for a in r2) for b in i2)
        and len(r2) == len(i2) + 1
    )

    morphism_rows = [
        {"law": "componentwise_representation_change_joule", "passed": representation_preserved},
        {"law": "componentwise_gauge_bit_label_swap", "passed": gauge_preserved},
        {"law": "declared_irrelevant_coarse_graining", "passed": coarse_env_preserved and coarse_payload_preserved},
        {"law": "interchange_square_f1xf2_iota", "passed": interchange_preserves and interchange_square},
        {"law": "swap_symmetry", "passed": swap_symmetry},
        {"law": "associativity", "passed": associativity},
        {"law": "order_compatibility_component_covers_imply_composite_cover", "passed": order_compatibility},
        {"law": "restriction_law_independent_equality", "passed": restriction_independent},
        {"law": "restriction_law_coupled_cover_never_loses", "passed": restriction_coupled},
    ]
    morphisms_ok = all(row["passed"] for row in morphism_rows)

    # ---- Delta invariance on T584 orbits ----
    def delta_signature(delta: dict[str, Any]) -> tuple[Any, ...]:
        return (
            tuple(point_key(p) for p in delta["extra_points"]),
            delta["extra_dominations"],
        )

    baseline_delta_signature = delta_signature(witness_delta1)
    invariance_rows = []
    invariance_ok = True
    orbit_variants = [
        ("representation_joule_on_producer", make_cell(ns1, make_state("biased", ns1), representation="joule"), cell2),
        ("gauge_swap_on_producer", make_cell(ns1, make_state("biased", ns1, gauge_swapped=True)), cell2),
        ("gauge_swap_on_consumer", cell1, make_cell(ns2, make_state("biased", ns2, gauge_swapped=True))),
        ("coarse_graining_on_consumer", cell1, coarse2),
    ]
    for variant_id, variant1, variant2 in orbit_variants:
        variant_composite = compose(variant1, variant2, rho=rho_1(ns1, ns2))
        assert isinstance(variant_composite, CompositeContext)
        same = delta_signature(deviation(variant_composite)) == baseline_delta_signature
        invariance_ok = invariance_ok and same
        invariance_rows.append({"morphism": variant_id, "delta_unchanged": same})

    # ---- the four must-fail controls ----
    controls: list[ControlResult] = []

    scalar_a = compose(
        make_cell(ns1, make_state("known", ns1)), make_cell(ns2, make_state("known", ns2))
    )
    scalar_b = compose(
        make_cell(ns1, make_state("biased", ns1)), make_cell(ns2, make_state("biased", ns2))
    )
    assert isinstance(scalar_a, CompositeContext)
    assert isinstance(scalar_b, CompositeContext)
    env_a = composite_envelope(scalar_a)
    env_b = composite_envelope(scalar_b)
    count_a, count_b = len(env_a.points), len(env_b.points)
    success_a = round(sum(p.success for p in env_a.points), 9)
    success_b = round(sum(p.success for p in env_b.points), 9)
    native_relation = t583.compare_envelopes(env_a, env_b)
    scalar_collapses = (
        count_a == count_b and success_a == success_b and native_relation != "EQUIVALENT"
    )
    controls.append(
        ControlResult(
            "scalarized_capability_control",
            "a summed composite capability scalar must fail to stand in for the envelope verdict",
            scalar_collapses,
            f"point counts {count_a}={count_b}, success sums {success_a}={success_b}, "
            f"but native relation is {native_relation}: the scalar collapses a "
            "distinction the native order keeps and is rejected as a T583 "
            "failure-criterion violation (capability defaults to one scalar).",
        )
    )

    collision_attempt = compose(
        make_cell(ns1, make_state("known", ns1)),
        make_cell(ns2, make_state("biased", ns2)),
        tagging="untagged",
    )
    collision_rejected, collision_reason = _expect_rejection(
        collision_attempt, "UNTAGGED_NAMESPACE_COLLISION"
    )
    tagged_pair = compose(
        make_cell(ns1, make_state("known", ns1)), make_cell(ns2, make_state("biased", ns2))
    )
    assert isinstance(tagged_pair, CompositeContext)
    tagged_values = {
        point_key(replace(p, task_id=p.task_id.split("::", 1)[1]))
        for p in composite_envelope(tagged_pair).points
    }
    untagged_candidates = []
    for cell in tagged_pair.components:
        raw = t585._points_for_state(
            context=cell.context,
            state=cell.state,
            observer_mode="state_aware",
            representation=cell.representation,
        )
        share = _share_budget(cell, tagged_pair)
        for point in raw:
            canonical = point.canonical()
            if t583.point_is_feasible(canonical, share):
                untagged_candidates.append(canonical)
    untagged_frontier = {
        point_key(p)
        for p in untagged_candidates
        if not any(
            t583.point_strictly_dominates(o, p) for o in untagged_candidates if o is not p
        )
    }
    untagged_changes_envelope = untagged_frontier != tagged_values
    untagged_record_collision = False
    try:
        merged_records: dict[str, str] = {}
        for cell in tagged_pair.components:
            # the untagged merge drops the namespace tag from the record id
            _register_unique_producer(
                merged_records, STANDARD_RECORD, f"{cell.namespace}::erase_standard_record"
            )
    except ValueError:
        untagged_record_collision = True
    controls.append(
        ControlResult(
            "namespace_collision_control",
            "the untagged task/record-vocabulary merge must be rejected as inadmissible",
            collision_rejected and untagged_changes_envelope and untagged_record_collision,
            f"untagged compose rejected with {collision_reason}; the merged "
            f"envelope would change ({len(tagged_values)} namespaced-frontier "
            f"values collapse to {len(untagged_frontier)}: cross-cell domination "
            "erases the biased cell's erase point), and the merged record "
            "vocabulary violates unique production of r_erased_standard.",
        )
    )

    pool_declared_1 = make_cell(ns1, make_state("biased", ns1), energy=0.30)
    pool_declared_2 = make_cell(ns2, make_state("known", ns2), energy=0.75)
    pool_declared = compose(pool_declared_1, pool_declared_2)
    pooled_1 = make_cell(ns1, make_state("biased", ns1), energy=1.00)
    pooled_2 = make_cell(ns2, make_state("known", ns2), energy=0.05)
    pooled = compose(pooled_1, pooled_2)
    assert isinstance(pool_declared, CompositeContext)
    assert isinstance(pooled, CompositeContext)
    declared_tasks = {p.task_id for p in composite_envelope(pool_declared).points}
    pooled_tasks = {p.task_id for p in composite_envelope(pooled).points}
    pooling_new_point = (
        f"{ns1}::{ERASE_TASK}" in pooled_tasks and f"{ns1}::{ERASE_TASK}" not in declared_tasks
    )
    pooling_assessment = t583.assess_pair(
        pair_id="budget_pooling_reallocation_control",
        left_context=pool_declared_1.context,
        right_context=pooled_1.context,
        left_envelope=component_envelope(pool_declared_1),
        right_envelope=component_envelope(pooled_1),
        evidence=t583.PairEvidence(source_law_present=True),
    )
    pooling_not_synergy = deviation_is_empty(deviation(pooled)) and deviation_is_empty(
        deviation(pool_declared)
    )
    controls.append(
        ControlResult(
            "budget_pooling_control",
            "reallocating shares across the declared partition must classify as "
            "RESOURCE_BUDGET_COMPLETION, never composite capability or synergy",
            pooling_new_point
            and pooling_assessment.verdict == "RESOURCE_BUDGET_COMPLETION"
            and pooling_not_synergy,
            f"pooling makes {ns1}::{ERASE_TASK} feasible (reset cost 0.468995594 "
            "vs declared share 0.30); T583 classifies the reallocation as "
            f"{pooling_assessment.verdict}; both partitions remain extensive "
            "(Delta empty), so the pooled gain never enters any deviation set.",
        )
    )

    unequal_bath = compose(
        cell1, make_cell(ns2, make_state("biased", ns2), bath_temperature_kelvin=350.0)
    )
    bath_rejected, bath_reason = _expect_rejection(unequal_bath, "UNEQUAL_BATH_TEMPERATURE")
    controls.append(
        ControlResult(
            "unequal_bath_control",
            "composition at unequal declared temperatures must fail closed, "
            "not silently unit-normalize",
            bath_rejected,
            f"compose returned {bath_reason}; no envelope was produced and no "
            "kBT ln 2 renormalization across baths was attempted.",
        )
    )

    controls_ok = all(control.failed_closed for control in controls)

    # ---- checks and the two-exit verdict ----
    checks = (
        source_check,
        Check(
            "intensive_restrictions_fail_closed",
            intensive_all_fail_closed,
            "Bath, time-window, error, horizon, source-theory, region, and "
            "namespace mutations are each rejected with a typed reason.",
        ),
        Check(
            "time_budget_equal_and_shared_not_summed",
            independent.shared_time_budget == 5.0,
            "The composite window is the shared 5.0, not the 10.0 a serial sum would give.",
        ),
        Check(
            "extensivity_grid_equality",
            grid_equal == grid_total,
            f"Env(C1 (x) C2) equals Env(C1) (+) Env(C2) bitwise after "
            f"canonicalization on {grid_equal}/{grid_total} independent grid composites, "
            "with domination sets equal, incomparability preserved, and no "
            "cross-namespace domination.",
        ),
        Check(
            "delta_empty_iff_independent_extensivity",
            delta_empty_iff_extensivity,
            "Delta(empty rho) is empty exactly where independent envelope extensivity holds.",
        ),
        Check(
            "delta_rho1_nonempty_witness",
            witness_ok,
            "At the packet's witness configuration Delta(rho_1) is exactly one "
            "frontier point (ns2::certify_cross_record_stability) with no lost "
            "points, and the contract-question scenarios separate as specified.",
        ),
        Check(
            "delta_monotone_in_rho",
            monotone_all,
            f"Delta(rho_1) is contained in Delta(rho_2) on all {grid_total} grid composites.",
        ),
        Check(
            "delta_gated_by_attainable_producer",
            producer_gating_consistent,
            "Delta(rho_1) is nonempty exactly when the producing namespace can "
            "actually execute erase inside its declared share; a declared edge "
            "with a starved producer yields Delta empty.",
        ),
        Check(
            "delta_t584_invariant",
            invariance_ok,
            "Delta(rho_1) is unchanged under componentwise representation, "
            "gauge, and declared coarse-graining morphisms.",
        ),
        Check(
            "t584_extension_laws",
            morphisms_ok,
            "Componentwise preservation, the interchange square, swap symmetry, "
            "associativity, order-compatibility, and both restriction laws pass.",
        ),
        Check(
            "controls_have_teeth",
            controls_ok,
            "All four must-fail controls fail closed; none can stand in for the "
            "envelope verdict or leak completion into capability.",
        ),
    )
    all_pass = all(check.passed for check in checks)
    if extensivity_holds and morphisms_ok:
        exit_taken = EXIT_A
    else:
        exit_taken = EXIT_B
    if not controls_ok:
        exit_taken = NO_TEETH
    verdict = (
        "COMPOSITION_EXTENSIVITY_WITNESS_EXECUTED_" + exit_taken + "_REVIEW_ONLY"
        if all_pass
        else "COMPOSITION_EXTENSIVITY_WITNESS_CHECK_FAILED_" + exit_taken
    )

    return {
        "artifact": ARTIFACT,
        "status": STATUS,
        "spec": "explorations/proposed-composition-extensivity-gate-2026-07-28.md",
        "source_contract": "T583 CapabilityContract v1 + T584 invariance quotient",
        "source_fixture_class": "T585 one-bit Landauer memory cell (re-executed)",
        "witness_configuration": {
            "cells": "two biased one-bit Landauer cells (p_one=0.10, reset cost 0.468995594)",
            "bath_temperature_kelvin": 300.0,
            "energy_partition": [0.75, 0.75],
            "time_budget": {"mode": "equal_and_shared", "value": 5.0},
            "error_bound": 0.01,
            "horizon": "single_reset_cycle",
            "task_families": "{erase_to_standard_record, certify_record_stability} x {ns1, ns2}",
        },
        "intensive_fail_closed": intensive_rows,
        "extensivity_grid": {
            "combos": grid_total,
            "bitwise_equal": grid_equal,
            "failures": grid_failures,
            "rows": grid_rows,
        },
        "coupled_grid": {
            "delta_rho1_nonempty": delta_rho1_nonempty,
            "delta_rho2_nonempty": delta_rho2_nonempty,
            "monotone_rho1_subset_rho2": monotone_all,
            "delta_empty_iff_extensivity": delta_empty_iff_extensivity,
            "producer_attainability_gates_delta": producer_gating_consistent,
        },
        "rho_witness": witness,
        "morphism_laws": morphism_rows,
        "delta_invariance": invariance_rows,
        "controls": [asdict(control) for control in controls],
        "checks": [asdict(check) for check in checks],
        "exit_taken": exit_taken,
        "verdict": verdict,
        "firebreak": FIREBREAK_STATEMENT,
        "compliance_statement": (
            "No T-number is minted; no fixture result is written under "
            "results/; no time, temporal order, or issuance is derived; the "
            "record layer supplies executable-task prerequisites only. The "
            "owner mints the T-number and decides adoption of the reopening."
        ),
        "not_claimed": (
            "This run does not establish a rate constant, endorse any collapse "
            "model, construct a capability density or scalarization, move any "
            "claim, canon, Lane posture, or public posture, or extend beyond "
            "the T585 fixture class. Capability remains T583's operational "
            "executable-task measure and nothing else."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    payload = run_analysis()
    print(json.dumps(payload, indent=2, sort_keys=True))
    checks_ok = all(check["passed"] for check in payload["checks"])
    return 0 if checks_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
