"""Capability-graded finality probe: commit-module series S3 companion (un-T-numbered).

Executes the S3 swing of the commit-module series
(`explorations/commit-module-schema-2026-07-28.md`, Debt L2): define
commit(A, r) on the T585/T586 fixture class and run the pre-registered checks.

Definition implemented here (stated in full in the S3 exploration note):

- The transition-level functionals come first, with zero record vocabulary
  (the schema's cycle-breaker): a destabilization entropy production omega
  (nats) prices any stabilizing transition; its spontaneous reversal carries
  probability suppressed by e^{-omega} (Crooks Eq. (2), cited, not re-derived);
  its driven reversal carries a work bill of omega * kBT = (omega/ln 2) units
  of kBT ln 2 (the same number in two unit systems - the two faces).
- commit(A, r) then APPLIES those functionals to a record r via declared
  D-data (carrier map, per-event stabilization ledger, record-dependency
  closure): the un-commit task for r is priced as a T583 PerformancePoint and
  graded against the declared class A's T583 envelope machinery
  (point_is_feasible; access and menu gating per T583's completion
  vocabulary). FINAL(A, r) iff the un-commit task is not attainable in A's
  declared context. The margin is a per-axis vector (native Pareto
  discipline; no scalarization anywhere).

Fixture idealizations, declared (fixture-honesty discipline):

- omega per stabilizing event is DECLARED, not derived: the fixture has no
  microdynamics to derive it from (G is D-conditional per the schema; N8's
  ledger variables are granted as declared inputs).
- environment traces are summarized by omega plus the record-dependency
  closure; microtrajectory bookkeeping is idealized away.
- the horizon-crossed record is a DECLARED unbounded-cost edge (carriers
  departed from every declarable region; divergent work/time); the fixture
  cannot derive causal disconnection - it declares it.

Firebreak (inherited from T587's boundary typing): no grade computed here is
a record-order edge, an issuance, or a temporal quantity by itself. Nothing
here derives time, temporal order, or issuance, and nothing moves a claim.
Deterministic pure-stdlib run: no randomness, no wall-clock or date values in
the output; byte-identical output across repeat runs; exit 0 iff all checks
pass (must-fail controls pass by failing closed).

Run: python3 -m models.capability_graded_finality_probe   (from repo root)
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, replace
from typing import Any

from models import t583_capability_contract_v1 as t583
from models import t585_landauer_physical_capability_gate as t585
from models import t586_record_capability_order_gate as t586


ARTIFACT = "capability-graded-finality-probe-s3-companion-v0.1"
STATUS = "UN_T_NUMBERED_EXPLORATION_COMPANION_REVIEW_ONLY"
LN2 = math.log(2.0)
ROUND = 9

REVERSE_OPERATION = "crooks_reverse_protocol"
UN_COMMIT_TASK_PREFIX = "un_commit"
DISTRIBUTION_ACCESS = "memory_record_distribution"

IN_ENVELOPE = "IN_ENVELOPE"
OUT_BUDGET = "OUT_OF_ENVELOPE_BUDGET"
OUT_ACCESS = "OUT_OF_ENVELOPE_ACCESS"
OUT_MENU = "OUT_OF_ENVELOPE_MENU"

DIVERGENT = "DECLARED_DIVERGENT"

FIREBREAK_STATEMENT = (
    "FINAL(A, r) is class-indexed inaccessibility of the un-commit task, "
    "never constructor impossibility (N8 promotion gate item 8 binds): the "
    "spontaneous face e^{-omega} stays strictly nonzero for every finite "
    "omega, and no grade here is a record-order edge, an issuance, or a "
    "temporal quantity by itself."
)

BUDGET_AXES = ("energy", "time", "communication", "memory", "error")


# ---------------------------------------------------------------------------
# Declared D-data (fixture extension, priced as declarations)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RecordCarrier:
    """Declared carrier bookkeeping for one issued record (D-content)."""

    record_id: str
    producer_event: str
    carrier_id: str
    p_one: float  # current carrier distribution (for Landauer floors)
    omega_stab_nats: float  # declared stabilization entropy production
    metadata: dict[str, str]


def _declared_carriers() -> tuple[RecordCarrier, ...]:
    """The stabilization ledger: DECLARED omega per stabilizing event.

    The T586 entropy_rank column is NOT reused here: it is a control column
    (the entropy-scalar control shows it does not reproduce the record
    order), and reusing it as physical omega would overread a control.
    """
    return (
        RecordCarrier(
            "r_known_zero", "seed_known_record", "cell_seed", 0.0, 4.0,
            {"physical_payload": "seed", "display_label": "alpha",
             "sensor_serial": "S-A", "coordinate_name": "x_seed"},
        ),
        RecordCarrier(
            "r_copied_zero", "copy_known_record", "cell_copy", 0.0, 6.0,
            {"physical_payload": "copy", "display_label": "alpha",
             "sensor_serial": "S-B", "coordinate_name": "x_copy"},
        ),
        RecordCarrier(
            "r_erased_standard", "erase_standard_record", "cell_erase", 0.0, 9.0,
            {"physical_payload": "standard", "display_label": "alpha",
             "sensor_serial": "S-C", "coordinate_name": "x_erase"},
        ),
        RecordCarrier(
            "r_erasure_certificate", "certify_erased_record", "cell_cert", 0.0, 5.0,
            {"physical_payload": "certificate", "display_label": "alpha",
             "sensor_serial": "S-D", "coordinate_name": "x_cert"},
        ),
        RecordCarrier(
            "r_biased_reference", "prepare_biased_reference", "cell_bias", 0.10, 3.0,
            {"physical_payload": "reference", "display_label": "alpha",
             "sensor_serial": "S-E", "coordinate_name": "x_bias"},
        ),
    )


HORIZON_RECORD = "r_horizon_departed"
HORIZON_CARRIER = "cell_departed"  # outside every declarable access region

# The declarable carrier-access universe (the horizon carrier is NOT in it).
CARRIER_UNIVERSE = (
    "cell_seed", "cell_copy", "cell_erase", "cell_cert", "cell_bias",
)


# ---------------------------------------------------------------------------
# Declared agent classes (T583 contexts + carrier access)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AgentClass:
    """A declared T583 context extended with declared carrier access."""

    class_id: str
    context: t583.CapabilityContext
    carrier_access: tuple[str, ...]
    distribution_access: bool

    def budget(self) -> t583.Budget:
        return self.context.budget


def _s3_context(class_id: str, budget: t583.Budget, *, menu_has_reverse: bool,
                access_profile: tuple[str, ...]) -> t583.CapabilityContext:
    base = t585._base_context()
    menu = base.operation_menu + ((REVERSE_OPERATION,) if menu_has_reverse else ())
    tasks = base.task_family + tuple(
        f"{UN_COMMIT_TASK_PREFIX}::{carrier.record_id}"
        for carrier in _declared_carriers()
    ) + (f"{UN_COMMIT_TASK_PREFIX}::{HORIZON_RECORD}",)
    return replace(
        base,
        context_id=class_id,
        task_family=tasks,
        operation_menu=menu,
        menu_provenance="law_derived_landauer_bound_plus_declared_reverse_protocol",
        access_profile=access_profile,
        budget=budget,
        horizon="declared_reversal_window",
    )


def _scaled_budget(scale: float) -> t583.Budget:
    base = t585._base_context().budget
    return t583.Budget(
        energy=round(base.energy * scale, ROUND),
        time=round(base.time * scale, ROUND),
        communication=round(base.communication * scale, ROUND),
        memory=round(base.memory * scale, ROUND),
        error=base.error,  # error bound held fixed across the sweep (chain preserved)
    )


def _custom_budget(energy_scale: float, time_scale: float, other_scale: float) -> t583.Budget:
    base = t585._base_context().budget
    return t583.Budget(
        energy=round(base.energy * energy_scale, ROUND),
        time=round(base.time * time_scale, ROUND),
        communication=round(base.communication * other_scale, ROUND),
        memory=round(base.memory * other_scale, ROUND),
        error=base.error,
    )


SWEEP_SCALES = (1, 2, 4, 8, 16, 32, 40, 48, 64, 128)


def _declared_class_grid() -> tuple[AgentClass, ...]:
    base_access = t585._base_context().access_profile
    sighted = base_access  # includes memory_record_distribution
    blind = tuple(a for a in base_access if a != DISTRIBUTION_ACCESS)
    classes: list[AgentClass] = []
    for scale in SWEEP_SCALES:
        classes.append(
            AgentClass(
                class_id=f"A_scale_{scale:04d}",
                context=_s3_context(
                    f"A_scale_{scale:04d}", _scaled_budget(scale),
                    menu_has_reverse=True, access_profile=sighted,
                ),
                carrier_access=CARRIER_UNIVERSE,
                distribution_access=True,
            )
        )
    classes.append(
        AgentClass(
            class_id="A_blind_0048",
            context=_s3_context(
                "A_blind_0048", _scaled_budget(48),
                menu_has_reverse=True, access_profile=blind,
            ),
            carrier_access=CARRIER_UNIVERSE,
            distribution_access=False,
        )
    )
    classes.append(
        AgentClass(
            class_id="A_no_copy_access_0128",
            context=replace(
                _s3_context(
                    "A_no_copy_access_0128", _scaled_budget(128),
                    menu_has_reverse=True, access_profile=sighted,
                ),
                access_provenance="copy_carrier_access_revoked",
            ),
            carrier_access=tuple(c for c in CARRIER_UNIVERSE if c != "cell_copy"),
            distribution_access=True,
        )
    )
    classes.append(
        AgentClass(
            class_id="A_no_reverse_0128",
            context=_s3_context(
                "A_no_reverse_0128", _scaled_budget(128),
                menu_has_reverse=False, access_profile=sighted,
            ),
            carrier_access=CARRIER_UNIVERSE,
            distribution_access=True,
        )
    )
    classes.append(
        AgentClass(
            class_id="A_energy_poor_time_rich",
            context=_s3_context(
                "A_energy_poor_time_rich", _custom_budget(32, 128, 128),
                menu_has_reverse=True, access_profile=sighted,
            ),
            carrier_access=CARRIER_UNIVERSE,
            distribution_access=True,
        )
    )
    classes.append(
        AgentClass(
            class_id="A_time_poor_energy_rich",
            context=_s3_context(
                "A_time_poor_energy_rich", _custom_budget(128, 4, 128),
                menu_has_reverse=True, access_profile=sighted,
            ),
            carrier_access=CARRIER_UNIVERSE,
            distribution_access=True,
        )
    )
    return tuple(classes)


def class_extends(smaller: AgentClass, larger: AgentClass) -> bool:
    """The natural contract order A <= A': componentwise dominance on every
    declared capability field (region/access/menu/resources/budget dominance,
    schema Debt L2 (b))."""
    sb, lb = smaller.budget(), larger.budget()
    budget_ok = all(getattr(sb, axis) <= getattr(lb, axis) for axis in BUDGET_AXES)
    access_ok = set(smaller.carrier_access) <= set(larger.carrier_access)
    profile_ok = set(smaller.context.access_profile) <= set(larger.context.access_profile)
    menu_ok = set(smaller.context.operation_menu) <= set(larger.context.operation_menu)
    tasks_ok = set(smaller.context.task_family) <= set(larger.context.task_family)
    distribution_ok = (not smaller.distribution_access) or larger.distribution_access
    return budget_ok and access_ok and profile_ok and menu_ok and tasks_ok and distribution_ok


# ---------------------------------------------------------------------------
# The un-commit operation and its price (transition-level functionals applied
# to records through declared D-data)
# ---------------------------------------------------------------------------


def un_commit_closure(record_id: str, closure: frozenset[tuple[str, str]],
                      carriers: tuple[RecordCarrier, ...]) -> tuple[str, ...]:
    """Records whose pre-issuance restoration is entailed by un-committing r:
    r itself plus every record whose producing event is strictly downstream of
    r's producer in the T586 RECORD order (record-layer only; the fixture's
    two causal-only edges are deliberately NOT consumed)."""
    by_record = {c.record_id: c for c in carriers}
    producer = by_record[record_id].producer_event
    downstream = {
        c.record_id for c in carriers
        if (producer, c.producer_event) in closure
    }
    ordered = tuple(
        c.record_id for c in carriers
        if c.record_id == record_id or c.record_id in downstream
    )
    return ordered


def landauer_floor_bits(carrier: RecordCarrier, distribution_access: bool) -> float:
    """Landauer reset floor for one carrier, access-conditional exactly as in
    T585 (blind classes owe the worst-case bit, T585's blind_worst_case)."""
    if not distribution_access:
        return 1.0
    return round(t585.binary_entropy_bits(carrier.p_one), ROUND)


@dataclass(frozen=True)
class UnCommitPrice:
    record_id: str
    closure_records: tuple[str, ...]
    closure_carriers: tuple[str, ...]
    omega_total_nats: float          # spontaneous face: log(1/P_spont)
    destabilization_units: float     # paid face: omega/ln2 in kBT ln 2 units
    floor_units: float               # Landauer floors over the closure
    point: t583.PerformancePoint | None  # None iff declared-divergent
    divergent: bool


def price_un_commit(record_id: str, closure: frozenset[tuple[str, str]],
                    carriers: tuple[RecordCarrier, ...],
                    distribution_access: bool) -> UnCommitPrice:
    if record_id == HORIZON_RECORD:
        return UnCommitPrice(
            record_id=HORIZON_RECORD,
            closure_records=(HORIZON_RECORD,),
            closure_carriers=(HORIZON_CARRIER,),
            omega_total_nats=math.inf,
            destabilization_units=math.inf,
            floor_units=0.0,
            point=None,
            divergent=True,
        )
    by_record = {c.record_id: c for c in carriers}
    closure_ids = un_commit_closure(record_id, closure, carriers)
    members = [by_record[r] for r in closure_ids]
    omega_total = sum(m.omega_stab_nats for m in members)
    destab_units = omega_total / LN2
    floors = sum(landauer_floor_bits(m, distribution_access) for m in members)
    n = len(members)
    energy = round(destab_units + floors, ROUND)
    time_cost = round(n * 1.0 + destab_units + floors, ROUND)  # T585's 1.0+units law, per event
    point = t583.PerformancePoint(
        task_id=f"{UN_COMMIT_TASK_PREFIX}::{record_id}",
        success=round(0.999 ** n, ROUND),
        energy_cost=energy,
        time_cost=time_cost,
        communication_cost=round(0.05 * n, ROUND),
        memory_cost=round(0.1 * n, ROUND),
        error=round(0.001 + 0.0005 * n, ROUND),
        protocol_id=REVERSE_OPERATION,
    )
    return UnCommitPrice(
        record_id=record_id,
        closure_records=closure_ids,
        closure_carriers=tuple(m.carrier_id for m in members),
        omega_total_nats=round(omega_total, ROUND),
        destabilization_units=round(destab_units, ROUND),
        floor_units=round(floors, ROUND),
        point=point,
        divergent=False,
    )


# ---------------------------------------------------------------------------
# The grade
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CommitGrade:
    record_id: str
    class_id: str
    status: str
    final: bool
    margin: dict[str, Any]           # per-axis slack (+) / deficit (-); vector, never scalarized
    w_rev_units: Any                 # energy component (destabilization + floors) or DECLARED_DIVERGENT
    omega_total_nats: Any            # class-independent spontaneous face
    spontaneous_reversal_probability: Any  # e^{-omega_total}; class-independent


def grade_commit(agent: AgentClass, price: UnCommitPrice) -> CommitGrade:
    task_id = f"{UN_COMMIT_TASK_PREFIX}::{price.record_id}"
    menu_ok = (REVERSE_OPERATION in agent.context.operation_menu
               and task_id in agent.context.task_family)
    access_ok = set(price.closure_carriers) <= set(agent.carrier_access)
    budget = agent.budget()
    if price.divergent:
        margin = {axis: DIVERGENT for axis in BUDGET_AXES}
        status = OUT_ACCESS if not access_ok else OUT_BUDGET
        if not menu_ok:
            status = OUT_MENU
        return CommitGrade(
            record_id=price.record_id, class_id=agent.class_id, status=status,
            final=True, margin=margin, w_rev_units=DIVERGENT,
            omega_total_nats=DIVERGENT, spontaneous_reversal_probability=0.0,
        )
    point = price.point
    assert point is not None
    margin = {
        "energy": round(budget.energy - point.energy_cost, ROUND),
        "time": round(budget.time - point.time_cost, ROUND),
        "communication": round(budget.communication - point.communication_cost, ROUND),
        "memory": round(budget.memory - point.memory_cost, ROUND),
        "error": round(budget.error - point.error, ROUND),
    }
    if not menu_ok:
        status, final = OUT_MENU, True
    elif not access_ok:
        status, final = OUT_ACCESS, True
    elif t583.point_is_feasible(point, budget):
        status, final = IN_ENVELOPE, False
    else:
        status, final = OUT_BUDGET, True
    return CommitGrade(
        record_id=price.record_id, class_id=agent.class_id, status=status,
        final=final, margin=margin,
        w_rev_units=round(point.energy_cost, ROUND),
        omega_total_nats=price.omega_total_nats,
        spontaneous_reversal_probability=round(
            math.exp(-price.omega_total_nats), 15
        ),
    )


def grade_table(agents: tuple[AgentClass, ...],
                closure: frozenset[tuple[str, str]],
                carriers: tuple[RecordCarrier, ...],
                record_ids: tuple[str, ...]) -> dict[str, dict[str, CommitGrade]]:
    table: dict[str, dict[str, CommitGrade]] = {}
    for agent in agents:
        row: dict[str, CommitGrade] = {}
        for record_id in record_ids:
            price = price_un_commit(record_id, closure, carriers,
                                    agent.distribution_access)
            row[record_id] = grade_commit(agent, price)
        table[agent.class_id] = row
    return table


# ---------------------------------------------------------------------------
# T584 morphism legs (applied to (A, r) jointly)
# ---------------------------------------------------------------------------


def _representation_leg(agents: tuple[AgentClass, ...],
                        closure: frozenset[tuple[str, str]],
                        carriers: tuple[RecordCarrier, ...],
                        record_ids: tuple[str, ...]) -> bool:
    """Unit representation (joule round trip through T585's own converters),
    task-interface aliasing, protocol/context relabeling: FINAL and margins
    must be preserved after canonicalization."""
    baseline = grade_table(agents, closure, carriers, record_ids)
    ok = True
    for agent in agents:
        relabeled = AgentClass(
            class_id=agent.class_id,
            context=replace(
                agent.context,
                representation_label="joule_sensor_bus_interface",
                gauge_representative="gauge_rep_b",
            ),
            carrier_access=agent.carrier_access,
            distribution_access=agent.distribution_access,
        )
        semantic_stable = (
            relabeled.context.semantic_dict() == agent.context.semantic_dict()
        )
        for record_id in record_ids:
            price = price_un_commit(record_id, closure, carriers,
                                    agent.distribution_access)
            if price.divergent:
                transformed = grade_commit(relabeled, price)
            else:
                point = price.point
                assert point is not None
                # joule representation round trip on the energy axis, alias +
                # protocol relabel, then canonicalize back (T584 discipline).
                joule_point = replace(
                    point,
                    task_id=f"uc::{record_id}",
                    energy_cost=t585.units_to_joules(point.energy_cost),
                    protocol_id="reverse_bus_b",
                )
                canonical_point = replace(
                    joule_point,
                    task_id=point.task_id,
                    energy_cost=round(t585.joules_to_units(joule_point.energy_cost), ROUND),
                    protocol_id=point.protocol_id,
                )
                canonical_price = replace(price, point=canonical_point)
                transformed = grade_commit(relabeled, canonical_price)
            base = baseline[agent.class_id][record_id]
            if not (semantic_stable
                    and transformed.final == base.final
                    and transformed.status == base.status
                    and transformed.margin == base.margin):
                ok = False
    return ok


def _gauge_leg(agents: tuple[AgentClass, ...],
               closure: frozenset[tuple[str, str]],
               carriers: tuple[RecordCarrier, ...],
               record_ids: tuple[str, ...]) -> bool:
    """Bit-label gauge swap on every carrier (p -> 1-p, T585's gauge class):
    binary entropy is invariant, so every floor, price, and grade must be."""
    baseline = grade_table(agents, closure, carriers, record_ids)
    swapped_carriers = tuple(
        replace(c, p_one=round(1.0 - c.p_one, ROUND)) for c in carriers
    )
    swapped = grade_table(agents, closure, swapped_carriers, record_ids)
    return all(
        swapped[a.class_id][r].final == baseline[a.class_id][r].final
        and swapped[a.class_id][r].status == baseline[a.class_id][r].status
        and swapped[a.class_id][r].margin == baseline[a.class_id][r].margin
        for a in agents
        for r in record_ids
    )


def _coarse_graining_leg(carriers: tuple[RecordCarrier, ...]) -> bool:
    """Declared irrelevant coarse-graining (T585's declared fields): dropping
    display/sensor/coordinate metadata preserves the physical payload the
    grade consumes."""
    context = t585._base_context()
    ok = True
    for carrier in carriers:
        recoated = replace(
            carrier,
            metadata={
                **carrier.metadata,
                "display_label": "recoated",
                "sensor_serial": "S-Z",
                "coordinate_name": "y_shifted",
            },
        )
        left = t583.project_irrelevant_metadata(carrier.metadata, context)
        right = t583.project_irrelevant_metadata(recoated.metadata, context)
        if left != right:
            ok = False
    return ok


def _merge_counterexample_leg(agents: tuple[AgentClass, ...],
                              closure: frozenset[tuple[str, str]],
                              carriers: tuple[RecordCarrier, ...],
                              record_ids: tuple[str, ...]) -> bool:
    """MUST-FAIL control (T584's inadmissible class): merging the per-record
    un-commit task vocabulary into one task id must CHANGE the native envelope
    (records lose their identity in the Pareto frontier) and be caught."""
    agent = next(a for a in agents if a.class_id == "A_scale_0128")
    finite_ids = tuple(r for r in record_ids if r != HORIZON_RECORD)
    points = []
    for record_id in finite_ids:
        price = price_un_commit(record_id, closure, carriers, True)
        assert price.point is not None
        points.append(price.point)
    distinct_context = replace(
        agent.context,
        context_id="ctx_merge_control_distinct",
    )
    merged_context = replace(
        agent.context,
        context_id="ctx_merge_control_merged",
        task_family=agent.context.task_family + (f"{UN_COMMIT_TASK_PREFIX}::any",),
    )
    baseline_envelope = t583.attainable_envelope(
        context=distinct_context, state_id="merge_control_distinct",
        candidates=tuple(points),
    )
    merged_envelope = t583.attainable_envelope(
        context=merged_context, state_id="merge_control_merged",
        candidates=tuple(points),
        task_aliases={
            f"{UN_COMMIT_TASK_PREFIX}::{r}": f"{UN_COMMIT_TASK_PREFIX}::any"
            for r in finite_ids
        },
    )
    relation = t583.compare_envelopes(baseline_envelope, merged_envelope)
    lost_record_resolution = len(merged_envelope.points) < len(baseline_envelope.points)
    return relation != "EQUIVALENT" and lost_record_resolution


# ---------------------------------------------------------------------------
# Monotonicity, limit, order-compatibility
# ---------------------------------------------------------------------------


def _comparable_pairs(agents: tuple[AgentClass, ...]) -> tuple[tuple[str, str], ...]:
    pairs = []
    for a in agents:
        for b in agents:
            if a.class_id != b.class_id and class_extends(a, b):
                pairs.append((a.class_id, b.class_id))
    return tuple(sorted(pairs))


def _monotone_final(table: dict[str, dict[str, CommitGrade]],
                    pairs: tuple[tuple[str, str], ...],
                    record_ids: tuple[str, ...]) -> tuple[bool, int]:
    ok = True
    flips = 0
    for small_id, large_id in pairs:
        for record_id in record_ids:
            small = table[small_id][record_id]
            large = table[large_id][record_id]
            if large.final and not small.final:
                ok = False
            if small.final and not large.final:
                flips += 1
    return ok, flips


def _monotone_margins(table: dict[str, dict[str, CommitGrade]],
                      pairs: tuple[tuple[str, str], ...],
                      record_ids: tuple[str, ...]) -> bool:
    ok = True
    budget_graded = {IN_ENVELOPE, OUT_BUDGET}
    for small_id, large_id in pairs:
        for record_id in record_ids:
            small = table[small_id][record_id]
            large = table[large_id][record_id]
            if small.status in budget_graded and large.status in budget_graded:
                for axis in BUDGET_AXES:
                    sm, lg = small.margin[axis], large.margin[axis]
                    if isinstance(sm, float) and isinstance(lg, float) and lg < sm - 1e-9:
                        ok = False
    return ok


def _unfinalization_thresholds(closure: frozenset[tuple[str, str]],
                               carriers: tuple[RecordCarrier, ...],
                               agents: tuple[AgentClass, ...]) -> dict[str, Any]:
    sweep = [a for a in agents if a.class_id.startswith("A_scale_")]
    sweep.sort(key=lambda a: a.budget().energy)
    thresholds: dict[str, Any] = {}
    for carrier in carriers:
        found = None
        for agent in sweep:
            price = price_un_commit(carrier.record_id, closure, carriers, True)
            if not grade_commit(agent, price).final:
                found = int(round(agent.budget().energy / t585._base_context().budget.energy))
                break
        thresholds[carrier.record_id] = found if found is not None else "NEVER_IN_SWEEP"
    price = price_un_commit(HORIZON_RECORD, closure, carriers, True)
    horizon_final_everywhere = all(
        grade_commit(agent, price).final for agent in agents
    )
    thresholds[HORIZON_RECORD] = (
        "UNIFORMLY_FINAL_ACROSS_ALL_DECLARED_BOUNDED_CLASSES"
        if horizon_final_everywhere
        else "HORIZON_EDGE_ESCAPED"
    )
    return thresholds


def _constructive_covering(closure: frozenset[tuple[str, str]],
                           carriers: tuple[RecordCarrier, ...]) -> bool:
    """The finite side of the limit schema, constructively: for every finite
    record a bounded class covering its un-commit exists (budget = cost + 1
    on every axis, via T583's own feasibility predicate)."""
    ok = True
    for carrier in carriers:
        price = price_un_commit(carrier.record_id, closure, carriers, True)
        assert price.point is not None
        point = price.point
        cover = t583.Budget(
            energy=point.energy_cost + 1.0,
            time=point.time_cost + 1.0,
            communication=point.communication_cost + 1.0,
            memory=point.memory_cost + 1.0,
            error=point.error + 0.001,
        )
        if not t583.point_is_feasible(point, cover):
            ok = False
    return ok


def _order_compatibility(closure: frozenset[tuple[str, str]],
                         carriers: tuple[RecordCarrier, ...],
                         table: dict[str, dict[str, CommitGrade]],
                         agents: tuple[AgentClass, ...]) -> dict[str, bool]:
    by_record = {c.record_id: c for c in carriers}
    record_pairs = [
        (up.record_id, down.record_id)
        for up in carriers
        for down in carriers
        if (up.producer_event, down.producer_event) in closure
    ]
    containment_ok = True
    price_ok = True
    finality_ok = True
    for up_id, down_id in record_pairs:
        up_price = price_un_commit(up_id, closure, carriers, True)
        down_price = price_un_commit(down_id, closure, carriers, True)
        if not set(down_price.closure_records) <= set(up_price.closure_records):
            containment_ok = False
        assert up_price.point is not None and down_price.point is not None
        if up_price.point.energy_cost < down_price.point.energy_cost - 1e-9:
            price_ok = False
        if up_price.omega_total_nats < down_price.omega_total_nats - 1e-9:
            price_ok = False
        for agent in agents:
            if table[agent.class_id][down_id].final and not table[agent.class_id][up_id].final:
                finality_ok = False
    biased_price = price_un_commit("r_biased_reference", closure, carriers, True)
    biased_unconstrained = (
        biased_price.closure_records == ("r_biased_reference",)
        and all("r_biased_reference" not in pair for pair in record_pairs)
    )
    return {
        "record_pairs_checked": len(record_pairs),
        "closure_containment": containment_ok,
        "price_monotone_with_record_order": price_ok,
        "finality_monotone_with_record_order": finality_ok,
        "incomparable_record_unconstrained": biased_unconstrained,
    }


def _consumer_proliferation(closure: frozenset[tuple[str, str]],
                            carriers: tuple[RecordCarrier, ...]) -> dict[str, bool]:
    """Add one declared downstream consumer (archive of the certificate) and
    check: every ancestor's W_rev weakly increases, nothing else moves, and
    finality at fixed class only moves toward FINAL."""
    extended_carriers = carriers + (
        RecordCarrier(
            "r_archived_certificate", "archive_certificate", "cell_archive",
            0.0, 4.0,
            {"physical_payload": "archive", "display_label": "alpha",
             "sensor_serial": "S-F", "coordinate_name": "x_arch"},
        ),
    )
    extended_closure = frozenset(
        set(closure)
        | {("certify_erased_record", "archive_certificate")}
        | {(up, "archive_certificate")
           for up, down in closure if down == "certify_erased_record"}
    )
    ancestors = {"r_known_zero", "r_copied_zero", "r_erased_standard",
                 "r_erasure_certificate"}
    weakly_increase = True
    others_unchanged = True
    finality_one_way = True
    probe_agent = next(
        a for a in _declared_class_grid() if a.class_id == "A_scale_0048"
    )
    for carrier in carriers:
        before = price_un_commit(carrier.record_id, closure, carriers, True)
        after = price_un_commit(carrier.record_id, extended_closure,
                                extended_carriers, True)
        assert before.point is not None and after.point is not None
        if carrier.record_id in ancestors:
            if after.point.energy_cost < before.point.energy_cost - 1e-9:
                weakly_increase = False
            if after.omega_total_nats < before.omega_total_nats - 1e-9:
                weakly_increase = False
        else:
            if after.point != before.point:
                others_unchanged = False
        grade_before = grade_commit(probe_agent, before)
        grade_after = grade_commit(probe_agent, after)
        if grade_before.final and not grade_after.final:
            finality_one_way = False
    return {
        "ancestor_prices_weakly_increase": weakly_increase,
        "non_ancestors_unchanged": others_unchanged,
        "finality_moves_only_toward_final": finality_one_way,
    }


def _two_faces_tie(closure: frozenset[tuple[str, str]],
                   carriers: tuple[RecordCarrier, ...]) -> bool:
    """Construction identity carrying the Crooks content (Eq. (2)/(4), cited):
    the paid face's destabilization work (in kBT ln 2 units) times ln 2 equals
    the spontaneous face's log-suppression omega, record by record."""
    ok = True
    for carrier in carriers:
        price = price_un_commit(carrier.record_id, closure, carriers, True)
        if abs(price.destabilization_units * LN2 - price.omega_total_nats) > 1e-9:
            ok = False
    return ok


def _completion_classification(table: dict[str, dict[str, CommitGrade]],
                               agents: tuple[AgentClass, ...],
                               pairs: tuple[tuple[str, str], ...],
                               record_ids: tuple[str, ...]) -> tuple[bool, dict[str, int]]:
    """Every cross-class finality flip on the grid must be absorbed by a named
    T583 completion class (finality deltas between declared classes are
    context completions, never intrinsic physics)."""
    by_id = {a.class_id: a for a in agents}
    counts: dict[str, int] = {}
    all_named = True
    for small_id, large_id in pairs:
        flip = any(
            table[small_id][r].final != table[large_id][r].final
            for r in record_ids
        )
        if not flip:
            continue
        differences = t583.context_differences(
            by_id[small_id].context, by_id[large_id].context
        )
        carrier_delta = set(by_id[small_id].carrier_access) != set(
            by_id[large_id].carrier_access
        )
        if "operation_menu" in differences or "menu_provenance" in differences:
            completion = "MENU_COMPLETION"
        elif ("access_profile" in differences or "access_provenance" in differences
              or carrier_delta):
            completion = "ACCESS_COMPLETION"
        elif "cost_error_budget" in differences or "resource_provenance" in differences:
            completion = "RESOURCE_BUDGET_COMPLETION"
        else:
            completion = "NO_ADMITTED_COMPLETION_FOUND_IN_DECLARED_SCOPE"
            all_named = False
        counts[completion] = counts.get(completion, 0) + 1
    return all_named, counts


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Check:
    check_id: str
    passed: bool
    reason: str


def run_analysis() -> dict[str, Any]:
    t585_result = t585.run_t585_analysis()
    t586_result = t586.run_t586_analysis()
    closure = frozenset(tuple(pair) for pair in t586_result.order_report.closure)
    carriers = _declared_carriers()
    record_ids = tuple(c.record_id for c in carriers) + (HORIZON_RECORD,)
    agents = _declared_class_grid()
    pairs = _comparable_pairs(agents)
    table = grade_table(agents, closure, carriers, record_ids)

    representation_ok = _representation_leg(agents, closure, carriers, record_ids)
    gauge_ok = _gauge_leg(agents, closure, carriers, record_ids)
    coarse_ok = _coarse_graining_leg(carriers)
    merge_caught = _merge_counterexample_leg(agents, closure, carriers, record_ids)

    final_monotone, finality_flips = _monotone_final(table, pairs, record_ids)
    margin_monotone = _monotone_margins(table, pairs, record_ids)

    thresholds = _unfinalization_thresholds(closure, carriers, agents)
    finite_all_unfinalize = all(
        isinstance(thresholds[c.record_id], int) for c in carriers
    )
    horizon_uniform = (
        thresholds[HORIZON_RECORD]
        == "UNIFORMLY_FINAL_ACROSS_ALL_DECLARED_BOUNDED_CLASSES"
    )
    covering_ok = _constructive_covering(closure, carriers)

    order_report = _order_compatibility(closure, carriers, table, agents)
    proliferation = _consumer_proliferation(closure, carriers)
    faces_ok = _two_faces_tie(closure, carriers)

    grade_ep = table["A_energy_poor_time_rich"]["r_known_zero"]
    grade_tp = table["A_time_poor_energy_rich"]["r_known_zero"]
    incomparable_margins = (
        grade_ep.status == OUT_BUDGET and grade_tp.status == OUT_BUDGET
        and grade_ep.margin["energy"] < 0 <= grade_ep.margin["time"]
        and grade_tp.margin["time"] < 0 <= grade_tp.margin["energy"]
    )
    completions_named, completion_counts = _completion_classification(
        table, agents, pairs, record_ids
    )

    checks = (
        Check(
            "source_fixtures_reexecuted",
            t585_result.verdict == t585.VERDICT
            and t586_result.verdict == t586.VERDICT,
            "T585 and T586 are re-executed at run time and their review-only "
            "verdicts hold; the record order is consumed from T586's own "
            "closure, not restated.",
        ),
        Check(
            "grade_total_on_grid",
            all(
                table[a.class_id][r] is not None
                and table[a.class_id][r].status in
                {IN_ENVELOPE, OUT_BUDGET, OUT_ACCESS, OUT_MENU}
                for a in agents for r in record_ids
            ),
            "commit(A, r) is defined for every declared class x record pair "
            "on the grid (15 classes x 6 records), with a typed status and a "
            "vector margin.",
        ),
        Check(
            "t584_representation_invariance",
            representation_ok,
            "Joule round trip (T585's own converters), un-commit task "
            "aliasing, protocol and context relabeling preserve FINAL, "
            "status, and the margin vector for every (A, r).",
        ),
        Check(
            "t584_gauge_invariance",
            gauge_ok,
            "The bit-label gauge swap (p -> 1-p on every carrier) preserves "
            "every floor, price, status, and margin (binary entropy is gauge "
            "invariant).",
        ),
        Check(
            "t584_coarse_graining_invariance",
            coarse_ok,
            "Dropping the declared irrelevant metadata fields preserves the "
            "physical payload the grade consumes.",
        ),
        Check(
            "t584_merge_counterexample_caught",
            merge_caught,
            "MUST-FAIL control: merging the per-record un-commit task "
            "vocabulary into one task id changes the native envelope (record "
            "resolution is lost) and is rejected as inadmissible - the gate "
            "has teeth.",
        ),
        Check(
            "capability_extension_monotone_final",
            final_monotone and finality_flips > 0,
            f"On all {len(pairs)} comparable pairs of the declared class "
            "order, extending capability never makes any record MORE final "
            f"(and the constraint bites: {finality_flips} genuine "
            "finality flips occur in the extending direction).",
        ),
        Check(
            "capability_extension_monotone_margins",
            margin_monotone,
            "On budget-graded pairs, every margin axis weakly improves under "
            "capability extension (slack grows, deficits shrink), "
            "componentwise - no scalarization used.",
        ),
        Check(
            "bounded_sweep_unfinalizes_every_finite_record",
            finite_all_unfinalize,
            "Every finite-omega record leaves finality at a finite sweep "
            "scale (the honest outcome: nothing in a finite fixture is "
            "absolutely final), with thresholds ordered by un-commit "
            "closure depth.",
        ),
        Check(
            "horizon_edge_uniformly_final",
            horizon_uniform,
            "The declared unbounded-cost edge (carriers departed from every "
            "declarable region; divergent work) is FINAL for every declared "
            "bounded class at every sweep scale - uniform, not "
            "threshold-crossed.",
        ),
        Check(
            "limit_separation_schema",
            finite_all_unfinalize and horizon_uniform and covering_ok,
            "The schema 'FINAL for all bounded classes iff W_rev diverges' "
            "holds on the fixture class: constructively, every finite record "
            "has a covering bounded class (budget = cost + 1, via T583's own "
            "feasibility predicate); the declared divergent edge has none.",
        ),
        Check(
            "order_compatibility_with_t586",
            all(v for k, v in order_report.items() if isinstance(v, bool)),
            "Along the T586 record order: un-commit closures nest, W_rev and "
            "omega are weakly decreasing downstream (upstream records are at "
            "least as final), finality propagates upstream for every class, "
            "and the T586-incomparable record participates in no constraint.",
        ),
        Check(
            "consumer_proliferation_monotone",
            all(proliferation.values()),
            "Adding one declared downstream consumer weakly increases every "
            "ancestor's un-commit price, changes no non-ancestor, and moves "
            "finality only toward FINAL - the redundancy connection, "
            "forward-cited to S2.",
        ),
        Check(
            "two_faces_tie",
            faces_ok,
            "Paid face x ln2 = spontaneous face's log-suppression omega, "
            "record by record: a construction identity carrying the Crooks "
            "Eq. (2)/(4) content by citation, not re-derivation.",
        ),
        Check(
            "anti_scalarization_incomparable_margins",
            incomparable_margins,
            "Two declared classes are FINAL for the same record with "
            "incomparable margin vectors (energy-deficit/time-slack vs "
            "time-deficit/energy-slack): the grade is native-Pareto, not a "
            "scalar.",
        ),
        Check(
            "finality_deltas_are_named_completions",
            completions_named,
            "Every cross-class finality flip on the grid is absorbed by a "
            "named T583 completion class (resource/budget, access, or menu) "
            "- no intrinsic finality delta anywhere.",
        ),
    )

    exhibit_classes = (
        "A_scale_0001", "A_scale_0008", "A_scale_0016", "A_scale_0032",
        "A_scale_0040", "A_scale_0048", "A_blind_0048", "A_no_copy_access_0128",
        "A_no_reverse_0128", "A_scale_0128",
    )
    grades_out = {
        class_id: {
            record_id: {
                "status": table[class_id][record_id].status,
                "final": table[class_id][record_id].final,
                "margin": table[class_id][record_id].margin,
                "w_rev_units": table[class_id][record_id].w_rev_units,
                "omega_total_nats": table[class_id][record_id].omega_total_nats,
                "spontaneous_reversal_probability":
                    table[class_id][record_id].spontaneous_reversal_probability,
            }
            for record_id in record_ids
        }
        for class_id in exhibit_classes
    }
    prices_out = {}
    for carrier in carriers:
        price = price_un_commit(carrier.record_id, closure, carriers, True)
        assert price.point is not None
        prices_out[carrier.record_id] = {
            "closure_records": list(price.closure_records),
            "closure_carriers": list(price.closure_carriers),
            "omega_total_nats": price.omega_total_nats,
            "destabilization_units": price.destabilization_units,
            "landauer_floor_units": price.floor_units,
            "w_rev_units_energy": price.point.energy_cost,
            "time_cost": price.point.time_cost,
            "spontaneous_reversal_probability": round(
                math.exp(-price.omega_total_nats), 15
            ),
        }
    prices_out[HORIZON_RECORD] = {
        "closure_records": [HORIZON_RECORD],
        "closure_carriers": [HORIZON_CARRIER],
        "omega_total_nats": DIVERGENT,
        "destabilization_units": DIVERGENT,
        "landauer_floor_units": 0.0,
        "w_rev_units_energy": DIVERGENT,
        "time_cost": DIVERGENT,
        "spontaneous_reversal_probability": 0.0,
    }

    all_passed = all(check.passed for check in checks)
    return {
        "artifact": ARTIFACT,
        "status": STATUS,
        "definition": {
            "un_commit_operation": (
                "erase r AND restore the pre-issuance state of its carriers "
                "and every downstream copy/derivative in the T586 "
                "record-dependency closure (record-layer only; the fixture's "
                "two causal-only edges are not consumed), with environment "
                "traces summarized by the declared per-event omega ledger "
                "(microtrajectory bookkeeping idealized away - declared)."
            ),
            "price": (
                "W_rev(r) = sum over the closure of (omega_i/ln2 "
                "destabilization work + access-conditional Landauer reset "
                "floor), in T585's normalized kBT ln 2 units; spontaneous "
                "face P = e^{-sum omega_i} (Crooks Eq. (2), cited)."
            ),
            "grade": (
                "g(A, r) = typed feasibility of the un-commit task against "
                "A's declared T583 context (menu, access, budget), with a "
                "per-axis vector margin; never scalarized."
            ),
            "final": "FINAL(A, r) iff un-commit(r) is not in Env(A).",
        },
        "declared_idealizations": [
            "omega per stabilizing event is declared, not derived (no fixture microdynamics)",
            "environment traces summarized by omega + record-dependency closure",
            "reverse-protocol time/communication/memory/error prices are fixture-declared",
            "the horizon record's divergent cost and departed carrier are declared, not derived from geometry",
        ],
        "stabilization_ledger_nats": {
            c.record_id: c.omega_stab_nats for c in carriers
        },
        "un_commit_prices": prices_out,
        "class_grid": {
            "sweep_scales": list(SWEEP_SCALES),
            "classes": [a.class_id for a in agents],
            "comparable_pairs": len(pairs),
        },
        "grades_exhibit": grades_out,
        "unfinalization_thresholds": thresholds,
        "order_compatibility": order_report,
        "consumer_proliferation": proliferation,
        "completion_classification_of_finality_flips": completion_counts,
        "checks": [
            {"check_id": c.check_id, "passed": c.passed, "reason": c.reason}
            for c in checks
        ],
        "kill_verdict": (
            "S3_KILL_DOES_NOT_FIRE" if all_passed else "S3_KILL_FIRES"
        ),
        "firebreak": FIREBREAK_STATEMENT,
        "compliance_statement": (
            "No T-number is minted; nothing is written under results/; no "
            "time, temporal order, or issuance is derived; no claim, canon, "
            "guardrail, or posture moves. The grade is the module's candidate "
            "for finality, not THE physical finality."
        ),
        "not_claimed": (
            "No continuum claim, no quantum-measurement claim, no horizon "
            "geometry derived (the divergent edge is declared), no universal "
            "capability measure, no scalar finality, no promotion of "
            "exponential unlikelihood to impossibility (N8 gate item 8), and "
            "no anticipation of the parallel S2 arm's verdict."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    payload = run_analysis()
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(c["passed"] for c in payload["checks"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
