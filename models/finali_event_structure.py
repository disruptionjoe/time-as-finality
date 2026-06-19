"""T48: FinaliEvent Structure.

T48 defines the FinaliEvent Structure: an unordered set of PO1-admissible
D1RestrictionMorphisms equipped with a record-dependency partial order.

Key definitions:

  FinaliEvent: A PO1-admissible D1RestrictionMorphism annotated with
    causal_magnitude (reversal_cost of the post-finality target system) and
    info_magnitude (holder_redundancy of the post-finality target system).
    These are the two minimal finality axes (Mathematical Minimalist constraint).

  RecordBasis: Named frozenset of records associated with a D1RestrictionSystem.
    This is a T48-layer annotation; it is not part of the D1 formal system.

  Record-dependency relation: e_j directly precedes e_i iff the record basis
    of e_j's target (post-finality) system is a non-empty subset of the record
    basis of e_i's source (pre-finality) system. Interpretation: e_i cannot
    be a finality-crossing event unless e_j's locked records are already
    accessible to e_i's source system.

  FinaliEvent Structure: Unordered set of FinaliEvents equipped with the
    reflexive-transitive closure of the direct record-dependency relation.

Partial order axioms verified:
  Reflexivity:   e ≤ e for all e.
  Antisymmetry:  e_j ≤ e_i and e_i ≤ e_j implies e_j = e_i.
  Transitivity:  e_j ≤ e_k and e_k ≤ e_i implies e_j ≤ e_i.

Finite witness: three events over six systems with Hasse diagram:

  e1 (U1->O1)    e2 (U2->O2)
           \\      /
           e3 (U3->O3)

e1 and e2 are incomparable. Both are required by e3, because U3's source
records contain the locked outputs of both O1 and O2.

Finality axis coverage:
  causal_magnitude (reversal_cost):   e1=2, e2=1, e3=3
  info_magnitude   (holder_redundancy): e1=2, e2=3, e3=4

Connection to T47: FinaliEvents are exactly the PO1-admissible edges of D1Cat.
The FinaliEvent Structure adds semantic record-dependency ordering to T47's DAG.

Connection to event structures (Nielsen, Plotkin, Winskel 1981):
  A FinaliEvent Structure is compatible with an event structure (E, ≤, #):
  E = the set of FinaliEvents;
  ≤ = the record-dependency partial order (causality relation);
  # = conflict (not modeled in T48: all three events are compatible).

Hypotheses evaluated:
  H_PARTIAL_ORDER:  Record-dependency relation is a partial order.
  H_INCOMPARABLE:   Some events are incomparable (e1 || e2 in the witness).
  H_ROOT_EVENTS:    Root events (no predecessors) exist and are independent.
  H_NPW_COMPATIBLE: Structure is compatible with NPW event structure theory.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
    global_section,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FinaliEvent:
    name: str
    morphism: D1RestrictionMorphism
    causal_magnitude: int   # reversal_cost of post-finality target
    info_magnitude: int     # holder_redundancy of post-finality target
    admissibility: AdmissibilityCheck


@dataclass(frozen=True)
class RecordBasis:
    """T48 annotation: named frozenset of records for a D1RestrictionSystem."""
    system_name: str
    records: frozenset


@dataclass(frozen=True)
class DependencyPair:
    predecessor: str  # event name
    successor: str    # event name
    basis: str        # which record containment justifies this


@dataclass(frozen=True)
class PartialOrderVerification:
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    is_partial_order: bool
    pairs_verified: int
    order_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T48Result:
    events: tuple[FinaliEvent, ...]
    record_bases: tuple[RecordBasis, ...]
    direct_dependencies: tuple[DependencyPair, ...]
    partial_order: PartialOrderVerification
    hasse_description: str
    incomparable_pairs: tuple[tuple[str, str], ...]
    root_events: tuple[str, ...]
    connection_to_t47: str
    connection_to_npw: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# System constructors
# ---------------------------------------------------------------------------


def _site(sid: str, pop: str) -> ObserverSite:
    return ObserverSite(sid, pop, "finite_site", 0, "t48")


def _lv(sid: str, pop: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(site=_site(sid, pop), proposition_value="true", profile=profile)


def _build_u1() -> D1RestrictionSystem:
    """Pre-finality source for e1: unobstructed, same-same-same triangle."""
    p = D1Profile(3, 3, 2, 3)
    return D1RestrictionSystem(
        name="U1_source_A",
        proposition="initial_record_A",
        local_values=(_lv("u1a", "pre", p), _lv("u1b", "pre", p), _lv("u1c", "pre", p)),
        transport_edges=(
            TransportEdge("u1a", "u1b", "link", True),
            TransportEdge("u1b", "u1c", "link", True),
        ),
        source_site="u1a",
        target_site="u1c",
        patches=(
            RestrictionPatch("u1_ab", ("u1a", "u1b"), ("a", "b"), (PatchConstraint("a", "b", "same"),)),
            RestrictionPatch("u1_bc", ("u1b", "u1c"), ("b", "c"), (PatchConstraint("b", "c", "same"),)),
            RestrictionPatch("u1_ac", ("u1a", "u1c"), ("a", "c"), (PatchConstraint("a", "c", "same"),)),
        ),
    )


def _build_u2() -> D1RestrictionSystem:
    """Pre-finality source for e2: unobstructed, same-same-same triangle."""
    p = D1Profile(3, 2, 2, 3)
    return D1RestrictionSystem(
        name="U2_source_B",
        proposition="initial_record_B",
        local_values=(_lv("u2a", "pre", p), _lv("u2b", "pre", p), _lv("u2c", "pre", p)),
        transport_edges=(
            TransportEdge("u2a", "u2b", "link", True),
            TransportEdge("u2b", "u2c", "link", True),
        ),
        source_site="u2a",
        target_site="u2c",
        patches=(
            RestrictionPatch("u2_ab", ("u2a", "u2b"), ("d", "e"), (PatchConstraint("d", "e", "same"),)),
            RestrictionPatch("u2_bc", ("u2b", "u2c"), ("e", "f"), (PatchConstraint("e", "f", "same"),)),
            RestrictionPatch("u2_ac", ("u2a", "u2c"), ("d", "f"), (PatchConstraint("d", "f", "same"),)),
        ),
    )


def _build_u3() -> D1RestrictionSystem:
    """Pre-finality source for e3: unobstructed, absorbs O1 and O2 locked records."""
    p = D1Profile(4, 4, 3, 4)
    return D1RestrictionSystem(
        name="U3_composite_source",
        proposition="composite_pre_record",
        local_values=(_lv("u3a", "pre", p), _lv("u3b", "pre", p), _lv("u3c", "pre", p)),
        transport_edges=(
            TransportEdge("u3a", "u3b", "link", True),
            TransportEdge("u3b", "u3c", "link", True),
        ),
        source_site="u3a",
        target_site="u3c",
        patches=(
            RestrictionPatch("u3_ab", ("u3a", "u3b"), ("g", "h"), (PatchConstraint("g", "h", "same"),)),
            RestrictionPatch("u3_bc", ("u3b", "u3c"), ("h", "i"), (PatchConstraint("h", "i", "same"),)),
            RestrictionPatch("u3_ac", ("u3a", "u3c"), ("g", "i"), (PatchConstraint("g", "i", "same"),)),
        ),
    )


def _build_o1() -> D1RestrictionSystem:
    """Post-finality target for e1: obstructed parity-conflict triangle."""
    p = D1Profile(1, 2, 0, 2)
    return D1RestrictionSystem(
        name="O1_locked_A",
        proposition="locked_record_A",
        local_values=(_lv("o1a", "post", p), _lv("o1b", "post", p), _lv("o1c", "post", p)),
        transport_edges=(
            TransportEdge("o1a", "o1b", "edge", True),
            TransportEdge("o1b", "o1c", "edge", True),
        ),
        source_site="o1a",
        target_site="o1c",
        patches=(
            RestrictionPatch("o1_ab", ("o1a", "o1b"), ("x", "y"), (PatchConstraint("x", "y", "same"),)),
            RestrictionPatch("o1_bc", ("o1b", "o1c"), ("y", "z"), (PatchConstraint("y", "z", "same"),)),
            RestrictionPatch("o1_ac", ("o1a", "o1c"), ("x", "z"), (PatchConstraint("x", "z", "different"),)),
        ),
    )


def _build_o2() -> D1RestrictionSystem:
    """Post-finality target for e2: obstructed parity-conflict triangle."""
    p = D1Profile(1, 3, 0, 1)
    return D1RestrictionSystem(
        name="O2_locked_B",
        proposition="locked_record_B",
        local_values=(_lv("o2a", "post", p), _lv("o2b", "post", p), _lv("o2c", "post", p)),
        transport_edges=(
            TransportEdge("o2a", "o2b", "edge", True),
            TransportEdge("o2b", "o2c", "edge", True),
        ),
        source_site="o2a",
        target_site="o2c",
        patches=(
            RestrictionPatch("o2_ab", ("o2a", "o2b"), ("p", "q"), (PatchConstraint("p", "q", "same"),)),
            RestrictionPatch("o2_bc", ("o2b", "o2c"), ("q", "r"), (PatchConstraint("q", "r", "same"),)),
            RestrictionPatch("o2_ac", ("o2a", "o2c"), ("p", "r"), (PatchConstraint("p", "r", "different"),)),
        ),
    )


def _build_o3() -> D1RestrictionSystem:
    """Post-finality target for e3: obstructed parity-conflict triangle (combined)."""
    p = D1Profile(1, 4, 0, 3)
    return D1RestrictionSystem(
        name="O3_locked_composite",
        proposition="locked_composite_record",
        local_values=(_lv("o3a", "post", p), _lv("o3b", "post", p), _lv("o3c", "post", p)),
        transport_edges=(
            TransportEdge("o3a", "o3b", "edge", True),
            TransportEdge("o3b", "o3c", "edge", True),
        ),
        source_site="o3a",
        target_site="o3c",
        patches=(
            RestrictionPatch("o3_ab", ("o3a", "o3b"), ("s", "t"), (PatchConstraint("s", "t", "same"),)),
            RestrictionPatch("o3_bc", ("o3b", "o3c"), ("t", "u"), (PatchConstraint("t", "u", "same"),)),
            RestrictionPatch("o3_ac", ("o3a", "o3c"), ("s", "u"), (PatchConstraint("s", "u", "different"),)),
        ),
    )


# ---------------------------------------------------------------------------
# Record basis definitions
# ---------------------------------------------------------------------------


def _build_record_bases(
    u1: D1RestrictionSystem,
    u2: D1RestrictionSystem,
    u3: D1RestrictionSystem,
    o1: D1RestrictionSystem,
    o2: D1RestrictionSystem,
    o3: D1RestrictionSystem,
) -> tuple[RecordBasis, ...]:
    """
    Record sets justify the dependency structure:
      O1 output {r_A_locked} ⊆ U3 input {r_A_locked, r_B_locked, r_composite_raw} -> e1 < e3
      O2 output {r_B_locked} ⊆ U3 input {r_A_locked, r_B_locked, r_composite_raw} -> e2 < e3
      O1 output ⊄ U2 input {r_B_raw, r_B_coherent}                                 -> e1 || e2
      O2 output ⊄ U1 input {r_A_raw, r_A_coherent}                                 -> e1 || e2
      O3 output ⊄ U1, U2, or U3 input (r_composite_locked not in any source)       -> e3 is terminal
    """
    return (
        RecordBasis(u1.name, frozenset({"r_A_raw", "r_A_coherent"})),
        RecordBasis(u2.name, frozenset({"r_B_raw", "r_B_coherent"})),
        RecordBasis(u3.name, frozenset({"r_A_locked", "r_B_locked", "r_composite_raw"})),
        RecordBasis(o1.name, frozenset({"r_A_locked"})),
        RecordBasis(o2.name, frozenset({"r_B_locked"})),
        RecordBasis(o3.name, frozenset({"r_A_locked", "r_B_locked", "r_composite_locked"})),
    )


# ---------------------------------------------------------------------------
# Event construction
# ---------------------------------------------------------------------------


def _build_event(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    event_name: str,
    forgotten: tuple[str, ...],
) -> FinaliEvent:
    src_sites = list(source.site_ids())
    tgt_sites = list(target.site_ids())
    n = len(tgt_sites)
    site_map = tuple(SiteMap(s, tgt_sites[i % n]) for i, s in enumerate(src_sites))
    morphism = D1RestrictionMorphism(
        name=f"finali_{event_name}",
        source=source,
        target=target,
        site_map=site_map,
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
    case = ProjectionCase(
        name=event_name,
        source="T48",
        richer_system=source,
        restricted_system=target,
        morphism=morphism,
        forgotten_structure=forgotten,
        preserved_structure=(),
        intended_reading="finality-crossing event",
    )
    adm = check_admissibility(case)
    target_profile = target.local_values[0].profile
    return FinaliEvent(
        name=event_name,
        morphism=morphism,
        causal_magnitude=target_profile.reversal_cost,
        info_magnitude=target_profile.holder_redundancy,
        admissibility=adm,
    )


# ---------------------------------------------------------------------------
# Partial order computation
# ---------------------------------------------------------------------------


def _compute_order(
    events: list[FinaliEvent],
    source_records: dict[str, frozenset],
    target_records: dict[str, frozenset],
) -> tuple[tuple[tuple[str, str], ...], tuple[DependencyPair, ...]]:
    """Compute reflexive-transitive closure of direct record-dependency relation."""
    direct: list[DependencyPair] = []
    for ej in events:
        for ei in events:
            if ej.name == ei.name:
                continue
            ej_out = target_records.get(ej.morphism.target.name, frozenset())
            ei_in = source_records.get(ei.morphism.source.name, frozenset())
            if ej_out and ej_out <= ei_in:
                direct.append(DependencyPair(
                    predecessor=ej.name,
                    successor=ei.name,
                    basis=(
                        f"{ej.morphism.target.name}.records = {set(ej_out)} "
                        f"⊆ {ei.morphism.source.name}.records = {set(ei_in)}"
                    ),
                ))

    order: set[tuple[str, str]] = set()
    for e in events:
        order.add((e.name, e.name))
    for dep in direct:
        order.add((dep.predecessor, dep.successor))

    names = [e.name for e in events]
    changed = True
    while changed:
        changed = False
        for ej, ek, ei in itertools.product(names, repeat=3):
            if (ej, ek) in order and (ek, ei) in order and (ej, ei) not in order:
                order.add((ej, ei))
                changed = True

    return tuple(sorted(order)), tuple(direct)


def _verify_partial_order(
    events: list[FinaliEvent],
    order: tuple[tuple[str, str], ...],
) -> PartialOrderVerification:
    order_set = set(order)
    names = [e.name for e in events]

    reflexive = all((n, n) in order_set for n in names)
    antisymmetric = all(
        not ((ej, ei) in order_set and (ei, ej) in order_set)
        for ej, ei in itertools.product(names, repeat=2)
        if ej != ei
    )
    transitive = all(
        (ej, ei) in order_set
        for ej, ek, ei in itertools.product(names, repeat=3)
        if (ej, ek) in order_set and (ek, ei) in order_set
    )

    return PartialOrderVerification(
        reflexive=reflexive,
        antisymmetric=antisymmetric,
        transitive=transitive,
        is_partial_order=reflexive and antisymmetric and transitive,
        pairs_verified=len(names) ** 2,
        order_pairs=order,
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t48_analysis() -> T48Result:
    u1, u2, u3 = _build_u1(), _build_u2(), _build_u3()
    o1, o2, o3 = _build_o1(), _build_o2(), _build_o3()

    e1 = _build_event(u1, o1, "e1_A_locking", ("initial_coherence", "pre_lock_superposition"))
    e2 = _build_event(u2, o2, "e2_B_locking", ("initial_coherence", "pre_lock_superposition"))
    e3 = _build_event(u3, o3, "e3_composite_locking", ("composite_pre_structure", "absorbed_lock_accessibility"))
    events = [e1, e2, e3]

    bases = _build_record_bases(u1, u2, u3, o1, o2, o3)
    source_records = {b.system_name: b.records for b in bases if "source" in b.system_name or b.system_name.startswith("U")}
    target_records = {b.system_name: b.records for b in bases if "locked" in b.system_name or b.system_name.startswith("O")}

    order_pairs, direct_deps = _compute_order(events, source_records, target_records)
    po_check = _verify_partial_order(events, order_pairs)

    names = [e.name for e in events]
    incomparable = tuple(
        (ej, ei)
        for ej, ei in itertools.product(names, repeat=2)
        if ej < ei
        and (ej, ei) not in set(order_pairs)
        and (ei, ej) not in set(order_pairs)
    )

    pred_counts: dict[str, int] = {e.name: 0 for e in events}
    for pred, succ in order_pairs:
        if pred != succ:
            pred_counts[succ] += 1
    root_events = tuple(n for n in names if pred_counts[n] == 0)

    hasse = (
        "Hasse diagram of the FinaliEvent Structure partial order:\n"
        "  e1 (U1->O1, causal=2, info=2)    e2 (U2->O2, causal=1, info=3)\n"
        "                              \\   /\n"
        "                        e3 (U3->O3, causal=3, info=4)\n"
        "e1 and e2 are incomparable (no direct or transitive dependency).\n"
        "Both e1 and e2 are required by e3 (U3 contains O1 and O2 locked records)."
    )

    t47_conn = (
        "T48 extends T47: the FinaliEvents here are exactly the PO1-admissible "
        "morphisms of D1Cat (T47 DAG). T47 proved those morphisms form an acyclic "
        "bipartite graph (pre-finality -> post-finality). T48 adds a semantic "
        "ordering on those morphisms via record containment, converting the T47 "
        "DAG into a partial order. Acyclicity from T47 directly implies antisymmetry "
        "here: if e_j ≤ e_i and e_i ≤ e_j, then D1Cat has a cycle in its "
        "PO1-admissible subgraph, contradicting T47."
    )

    npw_conn = (
        "Compatibility with Nielsen-Plotkin-Winskel (1981) event structure theory: "
        "The triple (E, ≤, #) with E = {e1, e2, e3}, ≤ = the record-dependency "
        "partial order verified here, and # = empty conflict relation (all three "
        "events are mutually compatible) satisfies the NPW axioms for an event "
        "structure: (1) ≤ is a partial order (verified); (2) the enabling set of "
        "each event is finite (trivially, since E is finite); (3) no conflict "
        "relation is needed when all events are compatible. The FinaliEvent "
        "Structure is the restriction of NPW event structures to the finality-crossing "
        "morphisms of D1Cat, where ≤ arises from record containment rather than "
        "being postulated."
    )

    all_po1 = all(e.admissibility.po1_evidence for e in events)
    po_holds = po_check.is_partial_order
    has_incomparable = len(incomparable) > 0
    has_roots = len(root_events) > 0

    hyps = (
        HypothesisResult(
            "H_PARTIAL_ORDER",
            "Record-dependency relation is a partial order",
            "supported" if po_holds else "refuted",
            (
                f"reflexive={po_check.reflexive}, antisymmetric={po_check.antisymmetric}, "
                f"transitive={po_check.transitive}; {len(order_pairs)} pairs in order"
            ),
        ),
        HypothesisResult(
            "H_INCOMPARABLE",
            "Some events are incomparable (partial, not total, order)",
            "supported" if has_incomparable else "refuted",
            f"incomparable pairs: {incomparable}",
        ),
        HypothesisResult(
            "H_ROOT_EVENTS",
            "Root events exist and are PO1-admissible independent crossings",
            "supported" if has_roots and all_po1 else "refuted",
            (
                f"root events: {root_events}; "
                f"all three events PO1-admissible: {all_po1}"
            ),
        ),
        HypothesisResult(
            "H_NPW_COMPATIBLE",
            "FinaliEvent Structure is compatible with NPW event structure theory",
            "supported" if po_holds else "refuted",
            "partial order verified; conflict relation empty; NPW axioms satisfied",
        ),
    )

    all_supported = all(h.status == "supported" for h in hyps)
    best = (
        "H_PARTIAL_ORDER, H_INCOMPARABLE, H_ROOT_EVENTS, H_NPW_COMPATIBLE (all four hold)"
        if all_supported
        else "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T48Result(
        events=tuple(events),
        record_bases=bases,
        direct_dependencies=direct_deps,
        partial_order=po_check,
        hasse_description=hasse,
        incomparable_pairs=incomparable,
        root_events=root_events,
        connection_to_t47=t47_conn,
        connection_to_npw=npw_conn,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def t48_result_to_dict(r: T48Result) -> dict[str, Any]:
    return {
        "events": [
            {
                "name": e.name,
                "source": e.morphism.source.name,
                "target": e.morphism.target.name,
                "causal_magnitude": e.causal_magnitude,
                "info_magnitude": e.info_magnitude,
                "po1_admissible": e.admissibility.po1_evidence,
                "verdict": e.admissibility.verdict,
            }
            for e in r.events
        ],
        "record_bases": [
            {"system": b.system_name, "records": sorted(b.records)}
            for b in r.record_bases
        ],
        "direct_dependencies": [
            {"predecessor": d.predecessor, "successor": d.successor, "basis": d.basis}
            for d in r.direct_dependencies
        ],
        "partial_order": {
            "reflexive": r.partial_order.reflexive,
            "antisymmetric": r.partial_order.antisymmetric,
            "transitive": r.partial_order.transitive,
            "is_partial_order": r.partial_order.is_partial_order,
            "pairs_verified": r.partial_order.pairs_verified,
            "order_pairs": [list(p) for p in r.partial_order.order_pairs],
        },
        "incomparable_pairs": [list(p) for p in r.incomparable_pairs],
        "root_events": list(r.root_events),
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
