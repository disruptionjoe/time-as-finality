"""T50: Axis Monotonicity Theorem.

T50 formalizes the condition under which finality-axis dominance matches
record-dependency order, proves sufficiency, constructs the minimal
counterexample, proves axis necessity, and derives the Anti-Scalar Corollary.

All four results follow from one underlying theorem.

─────────────────────────────────────────────────────────────────────────
Axis Monotonicity (AM)
─────────────────────────────────────────────────────────────────────────

A FinaliEvent Structure (E, ≤_rec, profiles) satisfies Axis Monotonicity
with respect to axes A iff for all distinct e_j, e_i in E:

    e_j ≤_rec e_i  ←→  for all a in A: magnitude_a(e_j) ≤ magnitude_a(e_i)

Forward  (→): if e_j ≤_rec e_i then e_j dominates e_i on every A axis.
Backward (←): if e_j dominates e_i on every A axis then e_j ≤_rec e_i.

Both directions are required. The condition is independent of the specific
systems; it is a coherence property of the record structure and the D1 profiles.

─────────────────────────────────────────────────────────────────────────
Sufficiency Theorem
─────────────────────────────────────────────────────────────────────────

If (E, ≤_rec, profiles) satisfies AM w.r.t. A, then the A-axis magnitude
order (componentwise domination on axis magnitudes) is identical to ≤_rec.

Proof: AM says the two relations coincide on every distinct pair.
Reflexive pairs match trivially. Therefore the relations are identical. □

─────────────────────────────────────────────────────────────────────────
Counterexample (minimal AM violation)
─────────────────────────────────────────────────────────────────────────

The T48 witness is extended with one new event e3_viol (U3 → O3_violating):

  O3_violating has D1Profile(..., reversal_cost=1)
  O1 has D1Profile(..., reversal_cost=2)

  Record containment: O1.records = {r_A_locked} ⊆ U3.records → e1 ≤_rec e3_viol
  Axis reversal:      causal(e3_viol)=1 < causal(e1)=2       → NOT e1 ≤_mag e3_viol

  AM violated on pair (e1, e3_viol): in record order but not magnitude order.
  The magnitude order under-estimates the record order (missing dependency).
  This proves AM is a genuine mathematical condition, not a tautology.

─────────────────────────────────────────────────────────────────────────
Axis Necessity
─────────────────────────────────────────────────────────────────────────

On the T48 witness (e1: causal=2,info=2; e2: causal=1,info=3; e3: causal=3,info=4):

  Causal only: e2 ≤_causal e1 (1≤2) — spurious; record order has e1 || e2.
  Info only:   e1 ≤_info e2   (2≤3) — spurious; record order has e1 || e2.
  Both axes:   e1 || e2 correctly (Pareto-incomparable). 9/9 pairs match.

Neither axis alone is sufficient. Their combination is the minimal basis.

─────────────────────────────────────────────────────────────────────────
Anti-Scalar Corollary
─────────────────────────────────────────────────────────────────────────

If (E, ≤_rec, profiles) satisfies AM and ≤_rec has incomparable events,
then no scalar utility function f: E → R can reproduce ≤_rec.

Proof:
  (1) AM → magnitude order = ≤_rec (Sufficiency Theorem).
  (2) ≤_rec has incomparable events (given).
  (3) Therefore magnitude order has incomparable events.
  (4) Any scalar f induces a total preorder (totality: for all e_j, e_i,
      f(e_j) ≤ f(e_i) or f(e_i) ≤ f(e_j)).
  (5) Total preorders have no incomparable elements.
  (6) Therefore no scalar f matches the magnitude order (step 3 vs 5). □

Scalar time is ruled out by incomparability, not by complexity of the model.

─────────────────────────────────────────────────────────────────────────
Hypotheses evaluated
─────────────────────────────────────────────────────────────────────────

  H_AM_SUFFICIENCY:        AM holds on T48 witness; 2-axis order matches record order.
  H_AM_VIOLATION:          AM fails on violating witness; reconstruction diverges.
  H_AXIS_NECESSITY:        Causal alone and info alone each introduce spurious pairs.
  H_ANTI_SCALAR_COROLLARY: AM + incomparability → no scalar reproduces the order.
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
from models.finali_event_structure import FinaliEvent, RecordBasis, run_t48_analysis


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    """Finality axis magnitudes for a FinaliEvent (extracted from target D1Profile)."""
    event_name: str
    causal: int       # reversal_cost
    info: int         # holder_redundancy
    obs_access: int   # accessible_support
    branch: int       # branch_support


@dataclass(frozen=True)
class AMPairResult:
    event_j: str
    event_i: str
    in_record_order: bool
    in_magnitude_order: bool
    am_satisfied: bool   # True iff both sides agree


@dataclass(frozen=True)
class AMCheck:
    witness_name: str
    axes: tuple[str, ...]
    pairs_checked: int
    am_holds: bool
    pair_results: tuple[AMPairResult, ...]
    violations: tuple[AMPairResult, ...]
    spurious_count: int   # in magnitude but not record (false positive)
    missing_count: int    # in record but not magnitude (false negative)


@dataclass(frozen=True)
class AxisNecessityResult:
    axes_used: tuple[str, ...]
    total_pairs: int
    matching_pairs: int
    is_exact_match: bool
    spurious_pairs: tuple[tuple[str, str], ...]
    missing_pairs: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T50Result:
    # Normal witness (T48): AM holds
    am_normal: AMCheck
    # Violating witness (counterexample): AM fails
    am_violating: AMCheck
    # Axis necessity on T48 witness
    necessity_causal_only: AxisNecessityResult
    necessity_info_only: AxisNecessityResult
    necessity_2axis: AxisNecessityResult
    # Anti-scalar corollary
    anti_scalar_corollary: str
    anti_scalar_holds: bool
    # Hypothesis evaluations
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _site(sid: str, pop: str, tag: str = "t50") -> ObserverSite:
    return ObserverSite(sid, pop, "finite_site", 0, tag)


def _lv(sid: str, pop: str, profile: D1Profile) -> LocalD1Value:
    return LocalD1Value(site=_site(sid, pop), proposition_value="true", profile=profile)


def _axis_profile(event: FinaliEvent) -> AxisProfile:
    p = event.morphism.target.local_values[0].profile
    return AxisProfile(
        event_name=event.name,
        causal=p.reversal_cost,
        info=p.holder_redundancy,
        obs_access=p.accessible_support,
        branch=p.branch_support,
    )


def _magnitude_leq(ej: AxisProfile, ei: AxisProfile, axes: tuple[str, ...]) -> bool:
    return all(getattr(ej, ax) <= getattr(ei, ax) for ax in axes)


# ---------------------------------------------------------------------------
# Violating counterexample
# ---------------------------------------------------------------------------


def _build_o3_violating() -> D1RestrictionSystem:
    """Counterexample target: record structure same as O3 but causal axis reversed.

    D1Profile(..., reversal_cost=1): causal=1 < O1.causal=2.
    With O1.records ⊆ U3.records, record containment forces e1 ≤_rec e3_viol.
    But causal(e1)=2 > causal(e3_viol)=1 breaks AM on the causal axis.
    """
    p = D1Profile(1, 4, 0, 1)  # reversal_cost=1 is the violation
    return D1RestrictionSystem(
        name="O3_violating",
        proposition="locked_composite_record_violating",
        local_values=(
            _lv("ov3a", "post", p),
            _lv("ov3b", "post", p),
            _lv("ov3c", "post", p),
        ),
        transport_edges=(
            TransportEdge("ov3a", "ov3b", "edge", True),
            TransportEdge("ov3b", "ov3c", "edge", True),
        ),
        source_site="ov3a",
        target_site="ov3c",
        patches=(
            RestrictionPatch("ov3_ab", ("ov3a", "ov3b"), ("s", "t"), (PatchConstraint("s", "t", "same"),)),
            RestrictionPatch("ov3_bc", ("ov3b", "ov3c"), ("t", "u"), (PatchConstraint("t", "u", "same"),)),
            RestrictionPatch("ov3_ac", ("ov3a", "ov3c"), ("s", "u"), (PatchConstraint("s", "u", "different"),)),
        ),
    )


def _build_violating_event(
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
) -> FinaliEvent:
    src_sites = list(source.site_ids())
    tgt_sites = list(target.site_ids())
    n = len(tgt_sites)
    site_map = tuple(SiteMap(s, tgt_sites[i % n]) for i, s in enumerate(src_sites))
    morphism = D1RestrictionMorphism(
        name="finali_e3_violating",
        source=source,
        target=target,
        site_map=site_map,
        preserved_dimensions=("reversal_cost",),
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )
    case = ProjectionCase(
        name="e3_violating",
        source="T50",
        richer_system=source,
        restricted_system=target,
        morphism=morphism,
        forgotten_structure=("composite_pre_structure", "absorbed_lock_accessibility"),
        preserved_structure=(),
        intended_reading="violating counterexample: causal axis reversed",
    )
    adm = check_admissibility(case)
    target_profile = target.local_values[0].profile
    return FinaliEvent(
        name="e3_violating",
        morphism=morphism,
        causal_magnitude=target_profile.reversal_cost,
        info_magnitude=target_profile.holder_redundancy,
        admissibility=adm,
    )


# ---------------------------------------------------------------------------
# AM check
# ---------------------------------------------------------------------------


def _compute_record_order_from_bases(
    events: list[FinaliEvent],
    source_records: dict[str, frozenset],
    target_records: dict[str, frozenset],
) -> set[tuple[str, str]]:
    """Reflexive-transitive closure of direct record-containment dependencies."""
    order: set[tuple[str, str]] = {(e.name, e.name) for e in events}
    for ej, ei in itertools.product(events, repeat=2):
        if ej.name == ei.name:
            continue
        ej_out = target_records.get(ej.morphism.target.name, frozenset())
        ei_in = source_records.get(ei.morphism.source.name, frozenset())
        if ej_out and ej_out <= ei_in:
            order.add((ej.name, ei.name))
    # Transitive closure
    names = [e.name for e in events]
    changed = True
    while changed:
        changed = False
        for a, b, c in itertools.product(names, repeat=3):
            if (a, b) in order and (b, c) in order and (a, c) not in order:
                order.add((a, c))
                changed = True
    return order


def _check_am(
    witness_name: str,
    events: list[FinaliEvent],
    record_order: set[tuple[str, str]],
    axes: tuple[str, ...],
) -> AMCheck:
    profiles = {e.name: _axis_profile(e) for e in events}
    names = [e.name for e in events]

    pairs: list[AMPairResult] = []
    for ej_name, ei_name in itertools.product(names, repeat=2):
        if ej_name == ei_name:
            continue
        ej_p = profiles[ej_name]
        ei_p = profiles[ei_name]
        in_rec = (ej_name, ei_name) in record_order
        in_mag = _magnitude_leq(ej_p, ei_p, axes)
        pairs.append(AMPairResult(
            event_j=ej_name,
            event_i=ei_name,
            in_record_order=in_rec,
            in_magnitude_order=in_mag,
            am_satisfied=(in_rec == in_mag),
        ))

    violations = tuple(p for p in pairs if not p.am_satisfied)
    spurious = sum(1 for p in violations if p.in_magnitude_order and not p.in_record_order)
    missing = sum(1 for p in violations if p.in_record_order and not p.in_magnitude_order)

    return AMCheck(
        witness_name=witness_name,
        axes=axes,
        pairs_checked=len(pairs),
        am_holds=len(violations) == 0,
        pair_results=tuple(pairs),
        violations=violations,
        spurious_count=spurious,
        missing_count=missing,
    )


# ---------------------------------------------------------------------------
# Axis necessity
# ---------------------------------------------------------------------------


def _axis_necessity(
    events: list[FinaliEvent],
    record_order: set[tuple[str, str]],
    axes: tuple[str, ...],
) -> AxisNecessityResult:
    profiles = {e.name: _axis_profile(e) for e in events}
    names = [e.name for e in events]

    spurious: list[tuple[str, str]] = []
    missing: list[tuple[str, str]] = []
    matches = 0
    total = 0

    for ej_name, ei_name in itertools.product(names, repeat=2):
        if ej_name == ei_name:
            continue
        total += 1
        in_rec = (ej_name, ei_name) in record_order
        in_mag = _magnitude_leq(profiles[ej_name], profiles[ei_name], axes)
        if in_rec == in_mag:
            matches += 1
        elif in_mag and not in_rec:
            spurious.append((ej_name, ei_name))
        else:
            missing.append((ej_name, ei_name))

    return AxisNecessityResult(
        axes_used=axes,
        total_pairs=total,
        matching_pairs=matches,
        is_exact_match=len(spurious) == 0 and len(missing) == 0,
        spurious_pairs=tuple(spurious),
        missing_pairs=tuple(missing),
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t50_analysis() -> T50Result:
    t48 = run_t48_analysis()
    e1, e2, e3 = t48.events

    # ── Normal witness record order (from T48) ──
    normal_events = [e1, e2, e3]
    normal_src = {b.system_name: b.records for b in t48.record_bases
                  if b.system_name.startswith("U")}
    normal_tgt = {b.system_name: b.records for b in t48.record_bases
                  if b.system_name.startswith("O")}
    normal_rec_order = _compute_record_order_from_bases(normal_events, normal_src, normal_tgt)

    am_normal = _check_am("T48_normal", normal_events, normal_rec_order, ("causal", "info"))

    # ── Violating witness ──
    u3 = e3.morphism.source          # reuse U3 from T48
    o3_viol = _build_o3_violating()
    e3_viol = _build_violating_event(u3, o3_viol)

    viol_events = [e1, e2, e3_viol]

    # Record bases for violating witness: same U/O1/O2 bases; new O3_violating
    # O3_violating has same record structure as O3 (same locked outputs), so
    # O1.records ⊆ U3.records still holds → e1 ≤_rec e3_viol
    viol_tgt = dict(normal_tgt)
    viol_tgt[o3_viol.name] = frozenset({"r_A_locked", "r_B_locked", "r_composite_locked"})

    viol_rec_order = _compute_record_order_from_bases(viol_events, normal_src, viol_tgt)

    am_violating = _check_am("T50_violating", viol_events, viol_rec_order, ("causal", "info"))

    # ── Axis necessity on T48 witness ──
    necessity_causal = _axis_necessity(normal_events, normal_rec_order, ("causal",))
    necessity_info = _axis_necessity(normal_events, normal_rec_order, ("info",))
    necessity_2axis = _axis_necessity(normal_events, normal_rec_order, ("causal", "info"))

    # ── Anti-Scalar Corollary ──
    incomparable_in_normal = [
        (ej, ei)
        for ej, ei in itertools.product([e.name for e in normal_events], repeat=2)
        if ej < ei
        and (ej, ei) not in normal_rec_order
        and (ei, ej) not in normal_rec_order
    ]
    anti_scalar_holds = am_normal.am_holds and len(incomparable_in_normal) > 0

    anti_scalar_corollary = (
        "Anti-Scalar Corollary (from AM + Sufficiency + T49 Anti-Scalar):\n"
        "  (1) AM holds on T48 witness (confirmed above).\n"
        "  (2) Sufficiency Theorem: AM → magnitude order = record order.\n"
        "  (3) Record order has incomparable pairs: "
        f"{incomparable_in_normal}.\n"
        "  (4) Therefore magnitude order has incomparable pairs.\n"
        "  (5) T49 Anti-Scalar Theorem: no total preorder matches a partial\n"
        "      order with incomparable elements.\n"
        "  (6) Therefore no scalar f: Events → R can reproduce the record order.\n"
        "  Conclusion: scalar time is ruled out by incomparability, not by\n"
        "  model complexity. Any FinaliEvent Structure satisfying AM with\n"
        f"  incomparable events ({incomparable_in_normal}) cannot be\n"
        "  represented by a single global time coordinate. □"
    )

    # ── Hypothesis evaluations ──
    h_suf = am_normal.am_holds and necessity_2axis.is_exact_match
    h_viol = not am_violating.am_holds
    h_nec = (
        not necessity_causal.is_exact_match
        and not necessity_info.is_exact_match
        and necessity_2axis.is_exact_match
    )

    hyps = (
        HypothesisResult(
            "H_AM_SUFFICIENCY",
            "AM holds on T48 witness; 2-axis order matches record order exactly",
            "supported" if h_suf else "refuted",
            (
                f"AM: violations={len(am_normal.violations)}; "
                f"2-axis match={necessity_2axis.matching_pairs}/{necessity_2axis.total_pairs}"
            ),
        ),
        HypothesisResult(
            "H_AM_VIOLATION",
            "AM fails on violating witness; magnitude order diverges from record order",
            "supported" if h_viol else "refuted",
            (
                f"violations={len(am_violating.violations)}; "
                f"missing={am_violating.missing_count}; "
                f"spurious={am_violating.spurious_count}; "
                f"pairs: {[(v.event_j, v.event_i) for v in am_violating.violations]}"
            ),
        ),
        HypothesisResult(
            "H_AXIS_NECESSITY",
            "Causal alone and info alone each introduce spurious pairs; both axes are necessary",
            "supported" if h_nec else "refuted",
            (
                f"causal-only spurious={necessity_causal.spurious_pairs}; "
                f"info-only spurious={necessity_info.spurious_pairs}; "
                f"2-axis spurious={necessity_2axis.spurious_pairs}"
            ),
        ),
        HypothesisResult(
            "H_ANTI_SCALAR_COROLLARY",
            "AM + incomparability implies no scalar time coordinate can reproduce the order",
            "supported" if anti_scalar_holds else "refuted",
            (
                f"AM holds={am_normal.am_holds}; "
                f"incomparable pairs={incomparable_in_normal}; "
                f"corollary holds={anti_scalar_holds}"
            ),
        ),
    )

    all_supported = all(h.status == "supported" for h in hyps)
    best = (
        "H_AM_SUFFICIENCY, H_AM_VIOLATION, H_AXIS_NECESSITY, H_ANTI_SCALAR_COROLLARY (all four hold)"
        if all_supported
        else "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T50Result(
        am_normal=am_normal,
        am_violating=am_violating,
        necessity_causal_only=necessity_causal,
        necessity_info_only=necessity_info,
        necessity_2axis=necessity_2axis,
        anti_scalar_corollary=anti_scalar_corollary,
        anti_scalar_holds=anti_scalar_holds,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _am_to_dict(c: AMCheck) -> dict[str, Any]:
    return {
        "witness_name": c.witness_name,
        "axes": list(c.axes),
        "pairs_checked": c.pairs_checked,
        "am_holds": c.am_holds,
        "violation_count": len(c.violations),
        "spurious_count": c.spurious_count,
        "missing_count": c.missing_count,
        "violations": [
            {
                "event_j": v.event_j,
                "event_i": v.event_i,
                "in_record_order": v.in_record_order,
                "in_magnitude_order": v.in_magnitude_order,
            }
            for v in c.violations
        ],
    }


def _nec_to_dict(r: AxisNecessityResult) -> dict[str, Any]:
    return {
        "axes_used": list(r.axes_used),
        "total_pairs": r.total_pairs,
        "matching_pairs": r.matching_pairs,
        "is_exact_match": r.is_exact_match,
        "spurious_pairs": [list(p) for p in r.spurious_pairs],
        "missing_pairs": [list(p) for p in r.missing_pairs],
    }


def t50_result_to_dict(r: T50Result) -> dict[str, Any]:
    return {
        "am_normal": _am_to_dict(r.am_normal),
        "am_violating": _am_to_dict(r.am_violating),
        "axis_necessity": {
            "causal_only": _nec_to_dict(r.necessity_causal_only),
            "info_only": _nec_to_dict(r.necessity_info_only),
            "two_axis": _nec_to_dict(r.necessity_2axis),
        },
        "anti_scalar_holds": r.anti_scalar_holds,
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
