"""T52: Symmetric Colimit Theorem.

Four events; two observers each with complementary bounded record access.
Neither observer holds the full event-finality order. The colimit recovers it.

─────────────────────────────────────────────────────────────────────────
Witness
─────────────────────────────────────────────────────────────────────────

Events and axis profiles (target D1Profile magnitudes):
  e1_alpha  causal=2  info=1   (O1: reversal_cost=2, holder_redundancy=1)
  e2_beta   causal=1  info=3   (O2: reversal_cost=1, holder_redundancy=3)
  e3_gamma  causal=4  info=2   (O3: reversal_cost=4, holder_redundancy=2)
  e4_delta  causal=3  info=4   (O4: reversal_cost=3, holder_redundancy=4)

Full event-finality record bases:
  U3_gamma_source.records = {r1_locked, r3_raw}   → e1 ≤ e3
  U4_delta_source.records = {r1_locked, r2_locked, r4_raw}  → e1 ≤ e4, e2 ≤ e4

Observer A restricts U4: removes r1_locked → loses e1 ≤ e4.
Observer B restricts U3: removes r1_locked → loses e1 ≤ e3.

Colimit (union of record bases) restores both: recovers full reference order.

─────────────────────────────────────────────────────────────────────────
New phenomenon: AM is an event-finality property
─────────────────────────────────────────────────────────────────────────

Axis Monotonicity (AM) holds on the full event-finality order (axis profiles
designed for exact match). But it FAILS on each observer's apparent order:

  Observer A apparent: magnitude says e1 ≤ e4 (causal 2≤3, info 1≤4),
    but A's record order says e1 || e4.  → SPURIOUS violation.
  Observer B apparent: magnitude says e1 ≤ e3 (causal 2≤4, info 1≤2),
    but B's record order says e1 || e3.  → SPURIOUS violation.

The colimit resolves both phantom incomparabilities and restores AM.
AM is not a property of bounded apparent structures — it is a property
of the full event-finality order.

─────────────────────────────────────────────────────────────────────────
Hypotheses evaluated
─────────────────────────────────────────────────────────────────────────

  H_COLIMIT_CONSISTENT:  Colimit is a valid partial order (T47 holds at 4 events).
  H_SYMMETRIC_PHANTOM:   A loses (e1,e4); B loses (e1,e3). Distinct, symmetric.
  H_COLIMIT_COMPLETE:    Colimit = reference. Both observers contribute new pairs.
  H_AM_RESTORED:         AM fails locally (1 SPURIOUS each); holds on colimit.
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
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import AdmissibilityCheck, check_admissibility
from models.projection_obstruction_schema import ProjectionCase
from models.finali_event_structure import FinaliEvent, RecordBasis


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class BasisView:
    name: str
    source_records: dict[str, frozenset]
    target_records: dict[str, frozenset]
    apparent_order: frozenset[tuple[str, str]]
    incomparable_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class AMResult:
    witness_name: str
    am_holds: bool
    pairs_checked: int
    spurious: tuple[tuple[str, str], ...]
    missing: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class ColimitResult:
    colimit_order: frozenset[tuple[str, str]]
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    is_valid_partial_order: bool
    new_from_a: tuple[tuple[str, str], ...]
    new_from_b: tuple[tuple[str, str], ...]
    equals_reference: bool


@dataclass(frozen=True)
class PhantomResult:
    observer: str
    event_j: str
    event_i: str
    observer_says: str
    colimit_says: str
    is_phantom: bool


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T52Result:
    events: tuple[FinaliEvent, ...]
    reference: BasisView
    observer_a: BasisView
    observer_b: BasisView
    colimit: ColimitResult
    am_reference: AMResult
    am_observer_a: AMResult
    am_observer_b: AMResult
    am_colimit: AMResult
    phantoms: tuple[PhantomResult, ...]
    t47_consistency: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# D1 system builders
# ---------------------------------------------------------------------------


def _site(sid: str, pop: str) -> ObserverSite:
    return ObserverSite(sid, pop, "finite_site", 0, "t52")


def _lv(sid: str, pop: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(site=_site(sid, pop), proposition_value="true", profile=profile)


def _consistent_system(name: str, prop: str, pfx: str, profile: D1Profile) -> D1RestrictionSystem:
    """Unobstructed 3-site triangle (all same-constraints → no parity conflict)."""
    a, b, c = f"{pfx}a", f"{pfx}b", f"{pfx}c"
    return D1RestrictionSystem(
        name=name,
        proposition=prop,
        local_values=(_lv(a, "pre", profile), _lv(b, "pre", profile), _lv(c, "pre", profile)),
        transport_edges=(TransportEdge(a, b, "edge", True), TransportEdge(b, c, "edge", True)),
        source_site=a,
        target_site=c,
        patches=(
            RestrictionPatch(f"{pfx}_ab", (a, b), ("s", "t"), (PatchConstraint("s", "t", "same"),)),
            RestrictionPatch(f"{pfx}_bc", (b, c), ("t", "u"), (PatchConstraint("t", "u", "same"),)),
            RestrictionPatch(f"{pfx}_ac", (a, c), ("s", "u"), (PatchConstraint("s", "u", "same"),)),
        ),
    )


def _conflict_system(name: str, prop: str, pfx: str, profile: D1Profile) -> D1RestrictionSystem:
    """Obstructed 3-site triangle (same-same-different parity conflict)."""
    a, b, c = f"{pfx}a", f"{pfx}b", f"{pfx}c"
    return D1RestrictionSystem(
        name=name,
        proposition=prop,
        local_values=(_lv(a, "post", profile), _lv(b, "post", profile), _lv(c, "post", profile)),
        transport_edges=(TransportEdge(a, b, "edge", True), TransportEdge(b, c, "edge", True)),
        source_site=a,
        target_site=c,
        patches=(
            RestrictionPatch(f"{pfx}_ab", (a, b), ("s", "t"), (PatchConstraint("s", "t", "same"),)),
            RestrictionPatch(f"{pfx}_bc", (b, c), ("t", "u"), (PatchConstraint("t", "u", "same"),)),
            RestrictionPatch(f"{pfx}_ac", (a, c), ("s", "u"), (PatchConstraint("s", "u", "different"),)),
        ),
    )


def _build_event(name: str, u_sys: D1RestrictionSystem, o_sys: D1RestrictionSystem) -> FinaliEvent:
    src_sites = list(u_sys.site_ids())
    tgt_sites = list(o_sys.site_ids())
    n = len(tgt_sites)
    site_map = tuple(SiteMap(s, tgt_sites[i % n]) for i, s in enumerate(src_sites))
    morphism = D1RestrictionMorphism(
        name=f"finali_{name}",
        source=u_sys,
        target=o_sys,
        site_map=site_map,
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
    case = ProjectionCase(
        name=name,
        source="T52",
        richer_system=u_sys,
        restricted_system=o_sys,
        morphism=morphism,
        forgotten_structure=("pre_finality_variance",),
        preserved_structure=(),
        intended_reading=f"finality crossing {name}",
    )
    adm = check_admissibility(case)
    tp = o_sys.local_values[0].profile
    return FinaliEvent(
        name=name,
        morphism=morphism,
        causal_magnitude=tp.reversal_cost,
        info_magnitude=tp.holder_redundancy,
        admissibility=adm,
    )


# ---------------------------------------------------------------------------
# Record order computation
# ---------------------------------------------------------------------------


def _compute_order(
    events: list[FinaliEvent],
    src: dict[str, frozenset],
    tgt: dict[str, frozenset],
) -> frozenset[tuple[str, str]]:
    """Reflexive-transitive closure of record-containment dependencies."""
    order: set[tuple[str, str]] = {(e.name, e.name) for e in events}
    for ej, ei in itertools.product(events, repeat=2):
        if ej.name == ei.name:
            continue
        ej_out = tgt.get(ej.morphism.target.name, frozenset())
        ei_in = src.get(ei.morphism.source.name, frozenset())
        if ej_out and ej_out <= ei_in:
            order.add((ej.name, ei.name))
    names = [e.name for e in events]
    changed = True
    while changed:
        changed = False
        for a, b, c in itertools.product(names, repeat=3):
            if (a, b) in order and (b, c) in order and (a, c) not in order:
                order.add((a, c))
                changed = True
    return frozenset(order)


def _incomparable(names: list[str], order: frozenset) -> tuple[tuple[str, str], ...]:
    return tuple(
        (j, i) for j, i in itertools.product(names, repeat=2)
        if j < i and (j, i) not in order and (i, j) not in order
    )


def _relation(j: str, i: str, order: frozenset) -> str:
    if (j, i) in order:
        return "leq"
    if (i, j) in order:
        return "geq"
    return "incomparable"


def _verify_po(names: list[str], order: frozenset) -> tuple[bool, bool, bool]:
    ref = all((n, n) in order for n in names)
    anti = not any(
        (j, i) in order and (i, j) in order
        for j, i in itertools.product(names, repeat=2) if j != i
    )
    trans = all(
        (a, c) in order
        for a, b, c in itertools.product(names, repeat=3)
        if (a, b) in order and (b, c) in order
    )
    return ref, anti, trans


# ---------------------------------------------------------------------------
# AM check
# ---------------------------------------------------------------------------


def _check_am(witness_name: str, events: list[FinaliEvent], order: frozenset) -> AMResult:
    names = [e.name for e in events]
    mag = {e.name: (e.causal_magnitude, e.info_magnitude) for e in events}
    spurious, missing = [], []
    for j, i in itertools.product(names, repeat=2):
        if j == i:
            continue
        in_rec = (j, i) in order
        mj, mi = mag[j], mag[i]
        in_mag = mj[0] <= mi[0] and mj[1] <= mi[1]
        if in_mag and not in_rec:
            spurious.append((j, i))
        elif in_rec and not in_mag:
            missing.append((j, i))
    return AMResult(
        witness_name=witness_name,
        am_holds=not spurious and not missing,
        pairs_checked=len(names) * (len(names) - 1),
        spurious=tuple(spurious),
        missing=tuple(missing),
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t52_analysis() -> T52Result:
    # ── D1 profiles ──
    # Source systems: pre-finality (unobstructed, high reversal_cost)
    p_u1 = D1Profile(3, 2, 2, 3)
    p_u2 = D1Profile(3, 4, 2, 3)
    p_u3 = D1Profile(4, 3, 3, 5)
    p_u4 = D1Profile(4, 5, 3, 4)
    # Target systems: post-finality (obstructed)
    # causal = reversal_cost, info = holder_redundancy
    p_o1 = D1Profile(1, 1, 0, 2)  # causal=2, info=1
    p_o2 = D1Profile(1, 3, 0, 1)  # causal=1, info=3
    p_o3 = D1Profile(1, 2, 0, 4)  # causal=4, info=2
    p_o4 = D1Profile(1, 4, 0, 3)  # causal=3, info=4

    # ── D1 systems ──
    u1 = _consistent_system("U1_alpha_source", "pre_alpha", "u1", p_u1)
    u2 = _consistent_system("U2_beta_source", "pre_beta", "u2", p_u2)
    u3 = _consistent_system("U3_gamma_source", "pre_gamma_absorbs_alpha", "u3", p_u3)
    u4 = _consistent_system("U4_delta_source", "pre_delta_absorbs_alpha_beta", "u4", p_u4)
    o1 = _conflict_system("O1_alpha_locked", "locked_alpha", "o1", p_o1)
    o2 = _conflict_system("O2_beta_locked", "locked_beta", "o2", p_o2)
    o3 = _conflict_system("O3_gamma_locked", "locked_gamma", "o3", p_o3)
    o4 = _conflict_system("O4_delta_locked", "locked_delta", "o4", p_o4)

    # ── FinaliEvents ──
    e1 = _build_event("e1_alpha_locking", u1, o1)
    e2 = _build_event("e2_beta_locking", u2, o2)
    e3 = _build_event("e3_gamma_locking", u3, o3)
    e4 = _build_event("e4_delta_locking", u4, o4)
    events = [e1, e2, e3, e4]
    names = [e.name for e in events]

    # ── Full record bases (event-finality reference) ──
    full_src = {
        u1.name: frozenset({"r1_raw"}),
        u2.name: frozenset({"r2_raw"}),
        u3.name: frozenset({"r1_locked", "r3_raw"}),   # absorbs e1 output → e1 ≤ e3
        u4.name: frozenset({"r1_locked", "r2_locked", "r4_raw"}),  # → e1 ≤ e4, e2 ≤ e4
    }
    full_tgt = {
        o1.name: frozenset({"r1_locked"}),
        o2.name: frozenset({"r2_locked"}),
        o3.name: frozenset({"r3_locked"}),
        o4.name: frozenset({"r4_locked"}),
    }
    ref_order = _compute_order(events, full_src, full_tgt)
    reference = BasisView(
        name="Reference",
        source_records=full_src,
        target_records=full_tgt,
        apparent_order=ref_order,
        incomparable_pairs=_incomparable(names, ref_order),
    )

    # ── Observer A: U4 missing r1_locked ──
    a_src = dict(full_src)
    a_src[u4.name] = frozenset({"r2_locked", "r4_raw"})
    order_a = _compute_order(events, a_src, full_tgt)
    obs_a = BasisView(
        name="Observer_A",
        source_records=a_src,
        target_records=full_tgt,
        apparent_order=order_a,
        incomparable_pairs=_incomparable(names, order_a),
    )

    # ── Observer B: U3 missing r1_locked ──
    b_src = dict(full_src)
    b_src[u3.name] = frozenset({"r3_raw"})
    order_b = _compute_order(events, b_src, full_tgt)
    obs_b = BasisView(
        name="Observer_B",
        source_records=b_src,
        target_records=full_tgt,
        apparent_order=order_b,
        incomparable_pairs=_incomparable(names, order_b),
    )

    # ── Colimit: pointwise union of A and B's source records ──
    col_src = {
        name: a_src.get(name, frozenset()) | b_src.get(name, frozenset())
        for name in full_src
    }
    col_order = _compute_order(events, col_src, full_tgt)
    ref_col, anti_col, trans_col = _verify_po(names, col_order)
    new_from_a = tuple(p for p in col_order if p[0] != p[1] and p not in order_a)
    new_from_b = tuple(p for p in col_order if p[0] != p[1] and p not in order_b)
    colimit = ColimitResult(
        colimit_order=col_order,
        reflexive=ref_col,
        antisymmetric=anti_col,
        transitive=trans_col,
        is_valid_partial_order=ref_col and anti_col and trans_col,
        new_from_a=new_from_a,
        new_from_b=new_from_b,
        equals_reference=col_order == ref_order,
    )

    # ── AM checks ──
    am_ref = _check_am("Reference", events, ref_order)
    am_a = _check_am("Observer_A", events, order_a)
    am_b = _check_am("Observer_B", events, order_b)
    am_col = _check_am("Colimit", events, col_order)

    # ── Phantom incomparability ──
    phantoms: list[PhantomResult] = []
    for obs_name, obs_order in (("Observer_A", order_a), ("Observer_B", order_b)):
        for j, i in itertools.product(names, repeat=2):
            if j >= i:
                continue
            obs_rel = _relation(j, i, obs_order)
            col_rel = _relation(j, i, col_order)
            phantoms.append(PhantomResult(
                observer=obs_name,
                event_j=j,
                event_i=i,
                observer_says=obs_rel,
                colimit_says=col_rel,
                is_phantom=(obs_rel == "incomparable" and col_rel in ("leq", "geq")),
            ))

    # ── T47 consistency ──
    t47 = (
        "Colimit is antisymmetric: T47 acyclicity guarantees no record cycle "
        "for PO1-admissible events. Colimit consistency holds."
        if anti_col else
        "VIOLATION: colimit not antisymmetric — check PO1 admissibility or record-basis design."
    )

    # ── Hypothesis evaluations ──
    h_consistent = colimit.is_valid_partial_order
    h_symmetric = (
        len([p for p in phantoms if p.observer == "Observer_A" and p.is_phantom]) == 1
        and len([p for p in phantoms if p.observer == "Observer_B" and p.is_phantom]) == 1
    )
    h_complete = (
        colimit.equals_reference
        and len(colimit.new_from_a) > 0
        and len(colimit.new_from_b) > 0
    )
    h_am = (
        not am_a.am_holds
        and not am_b.am_holds
        and am_col.am_holds
    )

    hyps = (
        HypothesisResult(
            "H_COLIMIT_CONSISTENT",
            "Colimit of S_A and S_B is a valid partial order (T47 holds at 4 events)",
            "supported" if h_consistent else "refuted",
            f"reflexive={ref_col}, antisymmetric={anti_col}, transitive={trans_col}",
        ),
        HypothesisResult(
            "H_SYMMETRIC_PHANTOM",
            "Observer A loses (e1,e4); Observer B loses (e1,e3) — distinct and symmetric phantoms",
            "supported" if h_symmetric else "refuted",
            str([(p.observer, p.event_j, p.event_i) for p in phantoms if p.is_phantom]),
        ),
        HypothesisResult(
            "H_COLIMIT_COMPLETE",
            "Colimit equals reference; both observers contribute new orderings",
            "supported" if h_complete else "refuted",
            f"equals_reference={colimit.equals_reference}, "
            f"new_from_A={colimit.new_from_a}, new_from_B={colimit.new_from_b}",
        ),
        HypothesisResult(
            "H_AM_RESTORED",
            "AM fails locally on each observer (1 SPURIOUS each); AM holds on colimit (0 violations)",
            "supported" if h_am else "refuted",
            f"AM_A: holds={am_a.am_holds}, spurious={am_a.spurious}; "
            f"AM_B: holds={am_b.am_holds}, spurious={am_b.spurious}; "
            f"AM_colimit: holds={am_col.am_holds}",
        ),
    )

    all_sup = all(h.status == "supported" for h in hyps)
    best = (
        "H_COLIMIT_CONSISTENT, H_SYMMETRIC_PHANTOM, H_COLIMIT_COMPLETE, H_AM_RESTORED (all four hold)"
        if all_sup else
        "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T52Result(
        events=tuple(events),
        reference=reference,
        observer_a=obs_a,
        observer_b=obs_b,
        colimit=colimit,
        am_reference=am_ref,
        am_observer_a=am_a,
        am_observer_b=am_b,
        am_colimit=am_col,
        phantoms=tuple(phantoms),
        t47_consistency=t47,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _am_dict(r: AMResult) -> dict[str, Any]:
    return {
        "witness": r.witness_name,
        "am_holds": r.am_holds,
        "pairs_checked": r.pairs_checked,
        "spurious": [list(p) for p in r.spurious],
        "missing": [list(p) for p in r.missing],
    }


def t52_result_to_dict(r: T52Result) -> dict[str, Any]:
    def order_list(o):
        return sorted([list(p) for p in o if p[0] != p[1]])

    return {
        "events": [
            {"name": e.name, "causal": e.causal_magnitude, "info": e.info_magnitude,
             "po1_admissible": e.admissibility.po1_evidence}
            for e in r.events
        ],
        "reference_order": order_list(r.reference.apparent_order),
        "observer_a_order": order_list(r.observer_a.apparent_order),
        "observer_b_order": order_list(r.observer_b.apparent_order),
        "colimit": {
            "order": order_list(r.colimit.colimit_order),
            "reflexive": r.colimit.reflexive,
            "antisymmetric": r.colimit.antisymmetric,
            "transitive": r.colimit.transitive,
            "is_valid_partial_order": r.colimit.is_valid_partial_order,
            "new_from_a": [list(p) for p in r.colimit.new_from_a],
            "new_from_b": [list(p) for p in r.colimit.new_from_b],
            "equals_reference": r.colimit.equals_reference,
        },
        "am_reference": _am_dict(r.am_reference),
        "am_observer_a": _am_dict(r.am_observer_a),
        "am_observer_b": _am_dict(r.am_observer_b),
        "am_colimit": _am_dict(r.am_colimit),
        "phantoms": [
            {"observer": p.observer, "event_j": p.event_j, "event_i": p.event_i,
             "observer_says": p.observer_says, "colimit_says": p.colimit_says,
             "is_phantom": p.is_phantom}
            for p in r.phantoms if p.is_phantom
        ],
        "t47_consistency": r.t47_consistency,
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
