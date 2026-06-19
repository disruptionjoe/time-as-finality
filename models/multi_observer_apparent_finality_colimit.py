"""T51: Multi-Observer Apparent Finality Colimit.

Tests whether the colimit of two observer-relative FinaliEvent Structures
(over the union of their record bases) is a consistent partial order, and
whether bounded record access creates phantom incomparabilities — events
that appear unordered to a bounded observer but are actually ordered in
the colimit (event finality) structure.

─────────────────────────────────────────────────────────────────────────
Setup
─────────────────────────────────────────────────────────────────────────

Reuse the T48 witness (e1_A_locking, e2_B_locking, e3_composite_locking)
with two different record-basis views of the same underlying systems:

  Observer A (full access):
    U3_composite_source.records = {r_A_locked, r_B_locked, r_composite_raw}
    Apparent order: e1 ≤ e3, e2 ≤ e3, e1 || e2  (= T48 partial order)

  Observer B (restricted access):
    U3_composite_source.records = {r_B_locked, r_composite_raw}  — missing r_A_locked
    Apparent order: e2 ≤ e3 only; e1 and e3 appear incomparable (phantom)

  Colimit (event finality):
    Merge bases: U3.records = {r_A_locked, r_B_locked, r_composite_raw}  (restored)
    Colimit order: e1 ≤ e3 recovered; colimit = Observer A's apparent order.

─────────────────────────────────────────────────────────────────────────
Phantom incomparability
─────────────────────────────────────────────────────────────────────────

Observer B correctly infers, given their accessible records, that e1 and e3
are unordered. This is not a reasoning error — it is true that r_A_locked
does not appear in B's view of U3's source records. The incomparability is
real within B's apparent finality structure.

The colimit reveals it as a phantom: when record bases are merged, r_A_locked
IS in U3's source records (Observer A knew this), and so e1 ≤ e3 emerges.
Bounded causal access is the source of phantom incomparability, not reasoning failure.

─────────────────────────────────────────────────────────────────────────
Colimit consistency (T47 connection)
─────────────────────────────────────────────────────────────────────────

The colimit is guaranteed consistent (antisymmetric) for PO1-admissible events
by T47 (PO1 DAG Theorem). A record cycle — O_j.records ⊆ U_i.records AND
O_i.records ⊆ U_j.records for distinct i,j — would produce an antisymmetry
violation in the colimit. T47 rules this out: PO1-admissible morphisms form
an acyclic bipartite graph. No colimit of PO1-admissible FinaliEvent Structures
can violate antisymmetry.

─────────────────────────────────────────────────────────────────────────
Hypotheses evaluated
─────────────────────────────────────────────────────────────────────────

  H_COLIMIT_CONSISTENT:       Colimit is a valid partial order (no violations).
  H_PHANTOM_INCOMPARABILITY:  Observer B sees e1 || e3; colimit says e1 ≤ e3.
  H_COLIMIT_EXTENDS:          Colimit adds e1 ≤ e3 not present in Observer B's view.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Any

from models.finali_event_structure import FinaliEvent, RecordBasis, run_t48_analysis


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ObserverView:
    name: str
    record_bases: tuple[RecordBasis, ...]
    apparent_order: frozenset[tuple[str, str]]
    incomparable_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class ColimitStructure:
    merged_bases: tuple[RecordBasis, ...]
    colimit_order: frozenset[tuple[str, str]]
    reflexive: bool
    antisymmetric: bool
    transitive: bool
    is_partial_order: bool
    new_orderings: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class PhantomResult:
    observer_name: str
    event_j: str
    event_i: str
    observer_sees: str    # "leq", "geq", or "incomparable"
    colimit_says: str     # "leq", "geq", or "incomparable"
    is_phantom: bool      # observer says incomparable but colimit says ordered


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T51Result:
    events: tuple[FinaliEvent, ...]
    observer_a: ObserverView
    observer_b: ObserverView
    colimit: ColimitStructure
    phantom_results: tuple[PhantomResult, ...]
    t47_consistency: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------


def _compute_order(
    events: list[FinaliEvent],
    source_records: dict[str, frozenset],
    target_records: dict[str, frozenset],
) -> frozenset[tuple[str, str]]:
    """Reflexive-transitive closure of direct record-containment dependencies."""
    order: set[tuple[str, str]] = {(e.name, e.name) for e in events}
    for ej, ei in itertools.product(events, repeat=2):
        if ej.name == ei.name:
            continue
        ej_out = target_records.get(ej.morphism.target.name, frozenset())
        ei_in = source_records.get(ei.morphism.source.name, frozenset())
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


def _incomparable_pairs(
    names: list[str], order: frozenset[tuple[str, str]]
) -> tuple[tuple[str, str], ...]:
    return tuple(
        (j, i)
        for j, i in itertools.product(names, repeat=2)
        if j < i and (j, i) not in order and (i, j) not in order
    )


def _relation(j: str, i: str, order: frozenset[tuple[str, str]]) -> str:
    if j == i:
        return "eq"
    if (j, i) in order:
        return "leq"
    if (i, j) in order:
        return "geq"
    return "incomparable"


def _verify_po(
    names: list[str], order: frozenset[tuple[str, str]]
) -> tuple[bool, bool, bool]:
    reflexive = all((n, n) in order for n in names)
    antisymmetric = not any(
        (j, i) in order and (i, j) in order
        for j, i in itertools.product(names, repeat=2)
        if j != i
    )
    transitive = all(
        (a, c) in order
        for a, b, c in itertools.product(names, repeat=3)
        if (a, b) in order and (b, c) in order
    )
    return reflexive, antisymmetric, transitive


def _merge_record_bases(
    bases_a: tuple[RecordBasis, ...],
    bases_b: tuple[RecordBasis, ...],
) -> tuple[RecordBasis, ...]:
    """Pointwise union of record sets for each system name."""
    a = {b.system_name: b.records for b in bases_a}
    b = {rb.system_name: rb.records for rb in bases_b}
    all_names = sorted(set(a) | set(b))
    return tuple(
        RecordBasis(n, a.get(n, frozenset()) | b.get(n, frozenset()))
        for n in all_names
    )


def _split(bases: tuple[RecordBasis, ...]) -> tuple[dict, dict]:
    src = {b.system_name: b.records for b in bases if b.system_name.startswith("U")}
    tgt = {b.system_name: b.records for b in bases if b.system_name.startswith("O")}
    return src, tgt


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t51_analysis() -> T51Result:
    t48 = run_t48_analysis()
    events = list(t48.events)
    names = [e.name for e in events]

    # ── Observer A: full record basis (same as T48) ──
    bases_a = t48.record_bases

    # ── Observer B: restricted — U3 missing r_A_locked ──
    bases_b = tuple(
        RecordBasis(b.system_name, b.records - frozenset({"r_A_locked"}))
        if b.system_name == "U3_composite_source"
        else b
        for b in t48.record_bases
    )

    src_a, tgt_a = _split(bases_a)
    src_b, tgt_b = _split(bases_b)

    order_a = _compute_order(events, src_a, tgt_a)
    order_b = _compute_order(events, src_b, tgt_b)

    obs_a = ObserverView(
        name="Observer_A",
        record_bases=bases_a,
        apparent_order=order_a,
        incomparable_pairs=_incomparable_pairs(names, order_a),
    )
    obs_b = ObserverView(
        name="Observer_B",
        record_bases=bases_b,
        apparent_order=order_b,
        incomparable_pairs=_incomparable_pairs(names, order_b),
    )

    # ── Colimit: merge record bases, recompute order ──
    merged = _merge_record_bases(bases_a, bases_b)
    src_col, tgt_col = _split(merged)
    col_order = _compute_order(events, src_col, tgt_col)

    ref, anti, trans = _verify_po(names, col_order)

    new_orderings = tuple(
        pair
        for pair in col_order
        if pair[0] != pair[1] and pair not in order_b
    )

    colimit = ColimitStructure(
        merged_bases=merged,
        colimit_order=col_order,
        reflexive=ref,
        antisymmetric=anti,
        transitive=trans,
        is_partial_order=ref and anti and trans,
        new_orderings=new_orderings,
    )

    # ── Phantom incomparability check ──
    phantoms: list[PhantomResult] = []
    for obs_name, obs_order in (("Observer_A", order_a), ("Observer_B", order_b)):
        for j, i in itertools.product(names, repeat=2):
            if j >= i:
                continue
            obs_rel = _relation(j, i, obs_order)
            col_rel = _relation(j, i, col_order)
            phantoms.append(PhantomResult(
                observer_name=obs_name,
                event_j=j,
                event_i=i,
                observer_sees=obs_rel,
                colimit_says=col_rel,
                is_phantom=(obs_rel == "incomparable" and col_rel in ("leq", "geq")),
            ))

    # ── T47 consistency ──
    t47_msg = (
        "Colimit is antisymmetric: T47 acyclicity prevents record cycles for "
        "PO1-admissible events, guaranteeing colimit consistency."
        if anti else
        "VIOLATION: colimit is NOT antisymmetric. This contradicts T47 for "
        "PO1-admissible events — check record-basis or admissibility."
    )

    # ── Hypothesis evaluations ──
    h_consistent = colimit.is_partial_order
    h_phantom = any(p.is_phantom for p in phantoms)
    h_extends = len(colimit.new_orderings) > 0

    hyps = (
        HypothesisResult(
            "H_COLIMIT_CONSISTENT",
            "Colimit of S_A and S_B is a valid partial order (no antisymmetry violations)",
            "supported" if h_consistent else "refuted",
            f"reflexive={ref}, antisymmetric={anti}, transitive={trans}",
        ),
        HypothesisResult(
            "H_PHANTOM_INCOMPARABILITY",
            "Observer B's apparent order has phantom incomparability; colimit reveals ordering",
            "supported" if h_phantom else "refuted",
            str([(p.event_j, p.event_i, p.observer_sees, p.colimit_says)
                 for p in phantoms if p.is_phantom]),
        ),
        HypothesisResult(
            "H_COLIMIT_EXTENDS",
            "Colimit strictly extends Observer B's apparent order (new orderings emerge)",
            "supported" if h_extends else "refuted",
            f"new_orderings={colimit.new_orderings}",
        ),
    )

    all_sup = all(h.status == "supported" for h in hyps)
    best = (
        "H_COLIMIT_CONSISTENT, H_PHANTOM_INCOMPARABILITY, H_COLIMIT_EXTENDS (all three hold)"
        if all_sup else
        "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T51Result(
        events=t48.events,
        observer_a=obs_a,
        observer_b=obs_b,
        colimit=colimit,
        phantom_results=tuple(phantoms),
        t47_consistency=t47_msg,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _view_to_dict(v: ObserverView) -> dict[str, Any]:
    return {
        "name": v.name,
        "record_bases": [
            {"system": b.system_name, "records": sorted(b.records)}
            for b in v.record_bases
        ],
        "apparent_order_pairs": sorted(
            [list(p) for p in v.apparent_order if p[0] != p[1]]
        ),
        "incomparable_pairs": [list(p) for p in v.incomparable_pairs],
    }


def _colimit_to_dict(c: ColimitStructure) -> dict[str, Any]:
    return {
        "merged_bases": [
            {"system": b.system_name, "records": sorted(b.records)}
            for b in c.merged_bases
        ],
        "colimit_order_pairs": sorted(
            [list(p) for p in c.colimit_order if p[0] != p[1]]
        ),
        "reflexive": c.reflexive,
        "antisymmetric": c.antisymmetric,
        "transitive": c.transitive,
        "is_partial_order": c.is_partial_order,
        "new_orderings": [list(p) for p in c.new_orderings],
    }


def t51_result_to_dict(r: T51Result) -> dict[str, Any]:
    return {
        "observer_a": _view_to_dict(r.observer_a),
        "observer_b": _view_to_dict(r.observer_b),
        "colimit": _colimit_to_dict(r.colimit),
        "phantom_results": [
            {
                "observer": p.observer_name,
                "event_j": p.event_j,
                "event_i": p.event_i,
                "observer_sees": p.observer_sees,
                "colimit_says": p.colimit_says,
                "is_phantom": p.is_phantom,
            }
            for p in r.phantom_results
        ],
        "t47_consistency": r.t47_consistency,
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
