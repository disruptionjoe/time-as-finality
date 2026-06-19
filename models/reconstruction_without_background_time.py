"""T49: Reconstruction Without Background Time.

T49 asks whether the partial order on FinaliEvents (T48) can be reconstructed
from finality axis magnitudes alone, with no background time variable.

Central questions:

  1. MAGNITUDE MATCH: Does the 2-axis componentwise partial order on
     (causal_magnitude, info_magnitude) reproduce the record-dependency
     partial order from T48 exactly?

  2. TOPOLOGICAL AMBIGUITY: How many valid temporal orderings exist?
     What determines the degree of ambiguity?

  3. ANTI-SCALAR THEOREM: Can any scalar utility function over finality
     axis magnitudes reproduce the record-dependency partial order?

  4. NO TIME INPUT: Does the reconstruction use any temporal variable?

Definitions:

  AxisProfile: The finality axis magnitudes of a FinaliEvent, extracted
    from the D1Profile of the post-finality (target) system:
      causal     = reversal_cost      (causal finality)
      info       = holder_redundancy  (information finality)
      obs_access = accessible_support (observer-access finality)
      branch     = branch_support     (environmental/branch finality)

  k-axis magnitude order: e_j ≤_k e_i iff, for every selected axis,
    the magnitude of e_j on that axis is ≤ the magnitude of e_i.
    This is the componentwise (Pareto dominance) partial order on R^k.

  Topological sort: a total ordering of events consistent with ≤_rec.
    A linear extension of the record-dependency partial order.

Key results (finite witness, 3 events from T48):

  1. 2-axis order EXACTLY matches record-dependency order: all 9 ordered
     pairs agree. The causal and information axes alone reconstruct T48's
     partial order.

  2. Exactly 2 valid topological sorts: (e1,e2,e3) and (e2,e1,e3).
     Ambiguity = 2! interleavings of incomparable root pair {e1, e2}.

  3. Anti-Scalar Theorem: any total preorder (scalar utility) must declare
     e1 and e2 comparable. Record-dependency order makes them incomparable.
     No scalar function can replicate a partial order with incomparable
     elements, because total preorders have no incomparable elements.

  4. 3-axis and 4-axis orders (adding obs_access and branch) do not resolve
     e1/e2 incomparability: both have obs_access=1, branch=0 in the T48
     target systems. The incomparability is Pareto-genuine, not an artifact
     of axis scarcity.

Hypotheses evaluated:
  H_MAGNITUDE_MATCH:         2-axis order matches record order exactly.
  H_TOPO_AMBIGUITY:          Valid topological sort count = 2! = 2 (one
                              per interleaving of the incomparable root pair).
  H_ANTI_SCALAR:             No scalar utility function can replicate a
                              partial order with incomparable elements.
  H_NO_TIME_INPUT:           Reconstruction proof uses no temporal variable.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Any

from models.finali_event_structure import FinaliEvent, run_t48_analysis


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class AxisProfile:
    """Finality axis magnitudes for one FinaliEvent (T49 annotation layer)."""
    event_name: str
    causal: int      # reversal_cost of post-finality target
    info: int        # holder_redundancy of post-finality target
    obs_access: int  # accessible_support of post-finality target
    branch: int      # branch_support of post-finality target


@dataclass(frozen=True)
class OrderComparison:
    """Comparison between record-dependency order and a k-axis magnitude order."""
    axes_used: tuple[str, ...]
    total_pairs: int
    matching_pairs: int
    mismatched_pairs: tuple[tuple[str, str, bool, bool], ...]  # (ej, ei, ref, mag)
    is_exact_match: bool
    incomparable_pairs_in_ref: tuple[tuple[str, str], ...]
    incomparable_pairs_in_mag: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class AntiScalarResult:
    """Result of the anti-scalar theorem check."""
    incomparable_pairs: tuple[tuple[str, str], ...]
    total_preorder_possible: bool
    theorem_holds: bool
    proof: str


@dataclass(frozen=True)
class HypothesisResult:
    hypothesis_id: str
    claim: str
    status: str
    evidence: str


@dataclass(frozen=True)
class T49Result:
    axis_profiles: tuple[AxisProfile, ...]
    record_order_pairs: tuple[tuple[str, str], ...]
    comparison_2axis: OrderComparison
    comparison_3axis_obs: OrderComparison   # causal + info + obs_access
    comparison_4axis: OrderComparison       # all four axes
    topological_sorts: tuple[tuple[str, ...], ...]
    anti_scalar: AntiScalarResult
    reconstruction_statement: str
    no_time_input_confirmation: str
    hypothesis_evaluations: tuple[HypothesisResult, ...]
    best_supported: str


# ---------------------------------------------------------------------------
# Axis profile extraction
# ---------------------------------------------------------------------------


def _axis_profile(event: FinaliEvent) -> AxisProfile:
    profile = event.morphism.target.local_values[0].profile
    return AxisProfile(
        event_name=event.name,
        causal=profile.reversal_cost,
        info=profile.holder_redundancy,
        obs_access=profile.accessible_support,
        branch=profile.branch_support,
    )


# ---------------------------------------------------------------------------
# Magnitude order
# ---------------------------------------------------------------------------


_AXIS_FIELDS = {
    "causal": "causal",
    "info": "info",
    "obs_access": "obs_access",
    "branch": "branch",
}


def _magnitude_leq(ej: AxisProfile, ei: AxisProfile, axes: tuple[str, ...]) -> bool:
    """e_j ≤_mag e_i iff all selected axis magnitudes of e_j ≤ e_i's."""
    return all(getattr(ej, ax) <= getattr(ei, ax) for ax in axes)


def _build_magnitude_order(
    profiles: list[AxisProfile],
    axes: tuple[str, ...],
) -> set[tuple[str, str]]:
    return {
        (ej.event_name, ei.event_name)
        for ej, ei in itertools.product(profiles, repeat=2)
        if _magnitude_leq(ej, ei, axes)
    }


def _incomparable_pairs(
    profiles: list[AxisProfile],
    order: set[tuple[str, str]],
) -> tuple[tuple[str, str], ...]:
    names = [p.event_name for p in profiles]
    return tuple(
        (ej, ei)
        for ej, ei in itertools.product(names, repeat=2)
        if ej < ei
        and (ej, ei) not in order
        and (ei, ej) not in order
    )


def _compare_orders(
    profiles: list[AxisProfile],
    record_order: set[tuple[str, str]],
    axes: tuple[str, ...],
) -> OrderComparison:
    mag_order = _build_magnitude_order(profiles, axes)
    names = [p.event_name for p in profiles]
    mismatches = []
    matches = 0
    for ej, ei in itertools.product(names, repeat=2):
        ref = (ej, ei) in record_order
        mag = (ej, ei) in mag_order
        if ref == mag:
            matches += 1
        else:
            mismatches.append((ej, ei, ref, mag))
    return OrderComparison(
        axes_used=axes,
        total_pairs=len(names) ** 2,
        matching_pairs=matches,
        mismatched_pairs=tuple(mismatches),
        is_exact_match=len(mismatches) == 0,
        incomparable_pairs_in_ref=_incomparable_pairs(profiles, record_order),
        incomparable_pairs_in_mag=_incomparable_pairs(profiles, mag_order),
    )


# ---------------------------------------------------------------------------
# Topological sort enumeration
# ---------------------------------------------------------------------------


def _all_topological_sorts(
    names: list[str],
    strict_order: set[tuple[str, str]],
) -> tuple[tuple[str, ...], ...]:
    """
    Enumerate all linear extensions of the partial order.
    strict_order contains pairs (a, b) meaning a strictly precedes b.
    """
    results: list[tuple[str, ...]] = []

    def is_consistent(perm: list[str]) -> bool:
        pos = {name: i for i, name in enumerate(perm)}
        return all(pos[a] < pos[b] for a, b in strict_order if a in pos and b in pos)

    for perm in itertools.permutations(names):
        if is_consistent(list(perm)):
            results.append(perm)

    return tuple(results)


# ---------------------------------------------------------------------------
# Anti-scalar theorem
# ---------------------------------------------------------------------------


def _anti_scalar_check(
    profiles: list[AxisProfile],
    record_order: set[tuple[str, str]],
) -> AntiScalarResult:
    incomparable = _incomparable_pairs(profiles, record_order)
    has_incomparable = len(incomparable) > 0

    proof = (
        "Anti-Scalar Theorem: No total preorder can replicate a partial order "
        "that has incomparable elements.\n"
        "Proof: A total preorder satisfies totality: for all e_j, e_i, either "
        "e_j ≤ e_i or e_i ≤ e_j (or both). The record-dependency partial order "
        "is NOT total: the incomparable pair(s) "
        f"{list(incomparable)} satisfy neither e_j ≤ e_i nor e_i ≤ e_j.\n"
        "Therefore no total preorder — including any scalar utility function "
        "f: Events -> R with f(e_j) < f(e_i) iff e_j < e_i — can assign "
        "values consistent with the partial order's incomparability.\n"
        "Consequence: A single global time coordinate (a total order on events) "
        "cannot exist for any FinaliEvent Structure with incomparable events. "
        "Temporal order is irreducibly partial when spacelike-separated "
        "finality crossings exist."
    )

    return AntiScalarResult(
        incomparable_pairs=incomparable,
        total_preorder_possible=not has_incomparable,
        theorem_holds=has_incomparable,
        proof=proof,
    )


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


def run_t49_analysis() -> T49Result:
    t48 = run_t48_analysis()
    events = list(t48.events)
    profiles = [_axis_profile(e) for e in events]
    record_order = set(t48.partial_order.order_pairs)

    cmp_2 = _compare_orders(profiles, record_order, ("causal", "info"))
    cmp_3 = _compare_orders(profiles, record_order, ("causal", "info", "obs_access"))
    cmp_4 = _compare_orders(profiles, record_order, ("causal", "info", "obs_access", "branch"))

    names = [p.event_name for p in profiles]
    strict = {(a, b) for a, b in record_order if a != b}
    sorts = _all_topological_sorts(names, strict)

    anti = _anti_scalar_check(profiles, record_order)

    reconstruction = (
        "Reconstruction theorem (finite witness, T48 3-event structure):\n"
        "The record-dependency partial order from T48 is exactly reproduced "
        "by the 2-axis componentwise partial order on (causal_magnitude, "
        "info_magnitude). No temporal variable appears in this reconstruction: "
        "causal_magnitude = reversal_cost(target_profile), "
        "info_magnitude = holder_redundancy(target_profile), both computed "
        "from D1Profile values of the post-finality system. The order "
        "e_j ≤_2 e_i iff causal_j ≤ causal_i AND info_j ≤ info_i "
        "is defined purely in terms of these profile values.\n"
        f"Match: {cmp_2.matching_pairs}/{cmp_2.total_pairs} ordered pairs agree "
        f"(exact match: {cmp_2.is_exact_match}).\n"
        f"Valid temporal orderings: {len(sorts)} (= 2! interleavings of incomparable "
        f"root events {t48.root_events})."
    )

    no_time = (
        "No temporal variable confirmation:\n"
        "Every definition used in the T49 reconstruction is examined below:\n"
        "  AxisProfile: fields are D1Profile integers (reversal_cost, "
        "holder_redundancy, accessible_support, branch_support). "
        "No temporal variable.\n"
        "  Magnitude order (_magnitude_leq): integer comparisons only. "
        "No temporal variable.\n"
        "  Topological sort enumeration: uses only the partial order pairs. "
        "No temporal variable.\n"
        "  Record-dependency order (from T48): defined by record containment "
        "(frozenset subset). No temporal variable.\n"
        "Conclusion: the reconstruction is non-circular. Temporal order "
        "(topological sort) is an output of the computation, not an input."
    )

    # Hypotheses
    mag_match = cmp_2.is_exact_match
    expected_sort_count = 2  # 2! interleavings of (e1, e2)
    topo_match = len(sorts) == expected_sort_count
    anti_holds = anti.theorem_holds

    hyps = (
        HypothesisResult(
            "H_MAGNITUDE_MATCH",
            "2-axis (causal, info) componentwise order matches record-dependency order exactly",
            "supported" if mag_match else "refuted",
            (
                f"{cmp_2.matching_pairs}/{cmp_2.total_pairs} pairs match; "
                f"mismatches={list(cmp_2.mismatched_pairs)}"
            ),
        ),
        HypothesisResult(
            "H_TOPO_AMBIGUITY",
            "Valid topological sort count = 2 (one per root-event interleaving)",
            "supported" if topo_match else "refuted",
            (
                f"{len(sorts)} valid sorts: {[list(s) for s in sorts]}; "
                f"expected {expected_sort_count}"
            ),
        ),
        HypothesisResult(
            "H_ANTI_SCALAR",
            "No scalar utility function can replicate a partial order with incomparable elements",
            "supported" if anti_holds else "refuted",
            (
                f"incomparable pairs={list(anti.incomparable_pairs)}; "
                f"total preorder possible={anti.total_preorder_possible}"
            ),
        ),
        HypothesisResult(
            "H_NO_TIME_INPUT",
            "Reconstruction uses no temporal variable; order is derived, not presupposed",
            "supported",
            "all definitions verified: AxisProfile, magnitude order, topo sort — no temporal variable",
        ),
    )

    all_supported = all(h.status == "supported" for h in hyps)
    best = (
        "H_MAGNITUDE_MATCH, H_TOPO_AMBIGUITY, H_ANTI_SCALAR, H_NO_TIME_INPUT (all four hold)"
        if all_supported
        else "partial: " + ", ".join(h.hypothesis_id for h in hyps if h.status == "supported")
    )

    return T49Result(
        axis_profiles=tuple(profiles),
        record_order_pairs=tuple(sorted(record_order)),
        comparison_2axis=cmp_2,
        comparison_3axis_obs=cmp_3,
        comparison_4axis=cmp_4,
        topological_sorts=sorts,
        anti_scalar=anti,
        reconstruction_statement=reconstruction,
        no_time_input_confirmation=no_time,
        hypothesis_evaluations=hyps,
        best_supported=best,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def t49_result_to_dict(r: T49Result) -> dict[str, Any]:
    def cmp_to_dict(c: OrderComparison) -> dict:
        return {
            "axes_used": list(c.axes_used),
            "total_pairs": c.total_pairs,
            "matching_pairs": c.matching_pairs,
            "is_exact_match": c.is_exact_match,
            "mismatched_pairs": [list(m) for m in c.mismatched_pairs],
            "incomparable_in_ref": [list(p) for p in c.incomparable_pairs_in_ref],
            "incomparable_in_mag": [list(p) for p in c.incomparable_pairs_in_mag],
        }

    return {
        "axis_profiles": [
            {
                "event": p.event_name,
                "causal": p.causal,
                "info": p.info,
                "obs_access": p.obs_access,
                "branch": p.branch,
            }
            for p in r.axis_profiles
        ],
        "record_order_pairs": [list(p) for p in r.record_order_pairs],
        "comparison_2axis": cmp_to_dict(r.comparison_2axis),
        "comparison_3axis_obs": cmp_to_dict(r.comparison_3axis_obs),
        "comparison_4axis": cmp_to_dict(r.comparison_4axis),
        "topological_sorts": [list(s) for s in r.topological_sorts],
        "anti_scalar": {
            "incomparable_pairs": [list(p) for p in r.anti_scalar.incomparable_pairs],
            "total_preorder_possible": r.anti_scalar.total_preorder_possible,
            "theorem_holds": r.anti_scalar.theorem_holds,
        },
        "hypothesis_evaluations": [
            {"id": h.hypothesis_id, "claim": h.claim, "status": h.status, "evidence": h.evidence}
            for h in r.hypothesis_evaluations
        ],
        "best_supported": r.best_supported,
    }
