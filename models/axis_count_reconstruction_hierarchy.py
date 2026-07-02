"""T394: Axis-Count Reconstruction Hierarchy.

Generalizes the T49/T50 Anti-Scalar and reconstruction results from the
3-event T48 witness to arbitrary finite event structures, by identifying
d-axis finality reconstruction with order dimension (candidate prior art,
from memory, unverified: Dushnik-Miller 1941; see the T394 spec's
prior-art register).

House vocabulary <-> neutral order-theory vocabulary:

  FinaliEvent structure record-dependency order  <->  finite poset P = (E, <=)
  d monotone finality axis magnitudes            <->  map m: E -> R^d
  exact reconstruction (T50 AM w.r.t. d axes)    <->  for all e != f:
                                                      e <= f iff m(e) <=_cw m(f)
  minimal axis count of P                        <->  order dimension dim(P)

Theorems verified here (finitely; caps documented below):

  THEOREM 1 (Reconstruction). A finite poset P is exactly reconstructible by
    d monotone axis magnitudes under componentwise order iff P is the
    intersection of d linear extensions (dim(P) <= d).
    Verified: (a) for every poset up to n = N_MAX_ISO_SWEEP = 6 (up to
    isomorphism), the minimal d is computed by exhaustive search over
    d-tuples of linear extensions, and the realizer's rank magnitudes are
    re-verified to reproduce P on all n^2 ordered pairs; (b) the tie-collapse
    loophole (real axes may have ties, i.e., are total preorders, not linear
    orders) is closed exhaustively for n <= N_MAX_PREORDER_SWEEP = 5 at
    d <= D_MAX_PREORDER_SWEEP = 2 (all pairs of weak orders), plus a targeted
    exhaustive refutation at n = 6, d = 2 for every dimension-3 class; and
    (c) the general tie-collapse lemma (any preorder realizer lexicographically
    linearizes to a linear-extension realizer) is implemented and verified on
    every first-found preorder witness. Beyond these caps the lemma is
    proof-backed (short proof in the spec), not enumeration-backed.

  THEOREM 2 (Anti-Scalar as d = 1). T49's Anti-Scalar Theorem is exactly the
    d = 1 rung: dim(P) = 1 iff P is a chain, so any incomparable pair forces
    dim(P) >= 2. Verified over all classes up to n = 6, plus a regression on
    T49's own 3-event witness (its 2-axis success falls out as dim = 2).

  THEOREM 3 (Axis-Count Obstruction). For every d there are finite record
    structures requiring more than d axes: the standard examples S_d
    (a_1..a_d minimal, b_1..b_d maximal, a_i < b_j iff i != j; candidate
    prior art, from memory: the Dushnik-Miller "standard examples").
    Verified: dim(S_3) = 3 and dim(S_4) = 4 by exhaustive (automorphism-
    orbit-pruned, coverage argued in the spec) search; dim(S_5) = 5 by a
    fully machine-checked finite certificate (diagonal-pair pigeonhole:
    every linear extension of S_d reverses at most one diagonal pair --
    checked both by C(d,2) cycle certificates and by enumerating ALL
    linear extensions -- plus an explicit verified 5-realizer). The
    brute-force d = 4 refutation for S_5 is computationally infeasible
    (~4e10 pruned pair-scans) and is NOT claimed; the certificate carries
    the lower bound, and it is cross-validated against brute force on S_3
    and S_4. Consequence: D1's four named axes reconstruct exactly the
    event structures of order dimension <= 4, and S_5 (10 events) escapes.

  THEOREM 4 (Realizability). Every finite poset arises as the
    record-dependency order of a FinaliEvent structure, via principal-downset
    record bases under T48's actual containment rule (target record basis of
    e_j a NON-EMPTY subset of source record basis of e_i). Verified for all
    classes up to n = 6 in both the faithful two-basis variant and the
    single-basis variant, plus an honest edge-case demonstration: with
    STRICT downsets the non-empty clause (and spurious containments between
    incomparable events) break the reconstruction -- the principal
    (inclusive) downset is the exact fix, and it matches what T48's own
    witness already does (O3 carries its predecessors' locked records).

House-object spotlight: S_3 is built as six actual PO1-admissible
FinaliEvents over D1RestrictionSystems, its record-dependency order is
computed with T48's own `_compute_order`, and T50's AM condition is checked
with T49's own `_compare_orders`: AM holds with the three axes
(causal = reversal_cost, info = holder_redundancy, obs_access =
accessible_support) assigned from the verified 3-realizer ranks, and fails
for every proper subset of those axes.

Labeling convention (house convention post-T392 review): events are labeled
by integers 0..n-1; enumeration uses natural labelings (i <_P j implies
i < j as integers); S_d uses a_i = i-1, b_j = d+j-1 (index-sorted: all a's
before all b's); ordered pairs (i, j) always mean i <_P j and pair LISTS are
sorted lexicographically.

Runtime caps (documented, chosen for < ~60 s total): N_MAX_ISO_SWEEP = 6
(318 iso classes at n = 6; n = 7 has 2045 classes and was not attempted),
N_MAX_PREORDER_SWEEP = 5 with D_MAX_PREORDER_SWEEP = 2 (541 weak orders at
n = 5; the full n = 6 pair sweep over 4683^2 weak-order pairs is replaced by
the targeted dimension-3 refutation), S_5 kept certificate-only for d = 4.

Determinism: no randomness anywhere; all enumeration orders are fixed by
construction (itertools orders and index-sorted tie-breaks).

Run:  python -m models.axis_count_reconstruction_hierarchy
"""

from __future__ import annotations

import itertools
import time
from dataclasses import dataclass
from math import factorial
from typing import Any

# ---------------------------------------------------------------------------
# Caps (documented in module docstring and in the spec)
# ---------------------------------------------------------------------------

N_MAX_ISO_SWEEP = 6
N_MAX_PREORDER_SWEEP = 5
D_MAX_PREORDER_SWEEP = 2
D_CAP_SEARCH = 4  # never reached at n <= 6; guarded honestly

LABELING_CONVENTION = (
    "events labeled 0..n-1; natural labelings in enumeration (i <_P j implies "
    "i < j); S_d labeled a_i = i-1, b_j = d+j-1 (index-sorted, a's before "
    "b's); ordered pairs (i, j) mean i <_P j; pair lists sorted "
    "lexicographically"
)

# Prior technical report cross-check targets (computed independently by
# technical-reports/TECHNICAL-REPORT-direction-a-finite-anti-scalar-
# generalization-v0.1.md): labeled poset counts n=3 -> 19, n=4 -> 219.
PRIOR_REPORT_LABELED_COUNTS = {3: 19, 4: 219}


# ---------------------------------------------------------------------------
# Finite poset primitives
# ---------------------------------------------------------------------------


def natural_transitive_relations(n: int) -> list[frozenset]:
    """All strict partial orders on {0..n-1} with i <_P j implying i < j.

    Every isomorphism class of n-element posets has at least one natural
    labeling (relabel along any linear extension), so canonicalizing this
    family reaches every class.
    """
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    idx = {p: k for k, p in enumerate(pairs)}
    triples = list(itertools.combinations(range(n), 3))
    out: list[frozenset] = []
    for mask in range(1 << len(pairs)):
        ok = True
        for i, j, k in triples:
            if (
                (mask >> idx[(i, j)]) & 1
                and (mask >> idx[(j, k)]) & 1
                and not (mask >> idx[(i, k)]) & 1
            ):
                ok = False
                break
        if ok:
            out.append(frozenset(p for p in pairs if (mask >> idx[p]) & 1))
    return out


def canonical_form(n: int, rel: frozenset) -> tuple:
    """Canonical form: minimum, over all NATURAL relabelings, of the sorted
    pair tuple. Valid across iso classes because isomorphic natural relations
    share the same set of natural relabelings (all natural labelings of the
    class), hence the same minimum."""
    best: tuple | None = None
    for sigma in itertools.permutations(range(n)):
        mapped = []
        ok = True
        for (a, b) in rel:
            x, y = sigma[a], sigma[b]
            if x > y:
                ok = False
                break
            mapped.append((x, y))
        if not ok:
            continue
        t = tuple(sorted(mapped))
        if best is None or t < best:
            best = t
    assert best is not None, "input relation must admit a natural relabeling"
    return best


def automorphism_count(n: int, rel: frozenset) -> int:
    count = 0
    for sigma in itertools.permutations(range(n)):
        if all((sigma[a], sigma[b]) in rel for (a, b) in rel):
            count += 1
    return count


def linear_extensions(n: int, rel: frozenset) -> list[tuple[int, ...]]:
    """All linear extensions, deterministic (lexicographic backtracking)."""
    preds: list[set[int]] = [set() for _ in range(n)]
    for (a, b) in rel:
        preds[b].add(a)
    out: list[tuple[int, ...]] = []

    def rec(placed: list[int], placed_set: set[int]) -> None:
        if len(placed) == n:
            out.append(tuple(placed))
            return
        for x in range(n):
            if x not in placed_set and preds[x] <= placed_set:
                placed.append(x)
                placed_set.add(x)
                rec(placed, placed_set)
                placed.pop()
                placed_set.discard(x)

    rec([], set())
    return out


def pairs_of_extension(perm: tuple[int, ...]) -> frozenset:
    s = set()
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            s.add((perm[i], perm[j]))
    return frozenset(s)


def is_acyclic(n: int, rel: set | frozenset) -> bool:
    adj: list[list[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for (a, b) in rel:
        adj[a].append(b)
        indeg[b] += 1
    queue = [i for i in range(n) if indeg[i] == 0]
    seen = 0
    while queue:
        x = queue.pop()
        seen += 1
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                queue.append(y)
    return seen == n


def deterministic_topological_sort(n: int, rel: set | frozenset) -> tuple[int, ...]:
    """Smallest-available-index topological sort (deterministic)."""
    preds: list[set[int]] = [set() for _ in range(n)]
    for (a, b) in rel:
        preds[b].add(a)
    placed: list[int] = []
    placed_set: set[int] = set()
    while len(placed) < n:
        for x in range(n):
            if x not in placed_set and preds[x] <= placed_set:
                placed.append(x)
                placed_set.add(x)
                break
        else:  # pragma: no cover - guarded by acyclicity checks upstream
            raise ValueError("relation is cyclic")
    return tuple(placed)


def is_chain(n: int, rel: frozenset) -> bool:
    comp = set(rel) | {(b, a) for (a, b) in rel}
    return all(
        (i, j) in comp for i in range(n) for j in range(i + 1, n)
    )


def incomparable_pairs(n: int, rel: frozenset) -> tuple[tuple[int, int], ...]:
    comp = set(rel) | {(b, a) for (a, b) in rel}
    return tuple(
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if (i, j) not in comp
    )


# ---------------------------------------------------------------------------
# Axis reconstruction / minimal axis count (order dimension by search)
# ---------------------------------------------------------------------------


def find_axis_realizer(
    n: int,
    rel: frozenset,
    d: int,
    exts: list[tuple[int, ...]] | None = None,
    first_extension_candidates: list[tuple[int, ...]] | None = None,
) -> tuple[tuple[int, ...], ...] | None:
    """Exhaustive search for d linear extensions whose intersection is rel.

    Completeness of the scan: if a d-realizer (L_1..L_d) exists, then for the
    (d-1)-tuple (L_1..L_{d-1}) every extra pair (a, b) of its intersection
    (comparable in all of L_1..L_{d-1} but not in P) must be reversed by L_d,
    so rel + {(b, a)} over all extras is acyclic and the scan finds a
    completion. `first_extension_candidates` optionally restricts the FIRST
    coordinate only (used with automorphism-orbit representatives; coverage
    argument in the T394 spec).
    """
    if d == 1:
        return (deterministic_topological_sort(n, rel),) if is_chain(n, rel) else None
    if exts is None:
        exts = linear_extensions(n, rel)
    ext_pairs = [pairs_of_extension(e) for e in exts]
    if first_extension_candidates is None:
        first_indices = range(len(exts))
    else:
        index_of = {e: k for k, e in enumerate(exts)}
        first_indices = [index_of[e] for e in first_extension_candidates]
    for first in first_indices:
        for tail in itertools.product(range(len(exts)), repeat=d - 2):
            inter = set(ext_pairs[first])
            for k in tail:
                inter &= ext_pairs[k]
            extras = inter - rel
            candidate = set(rel) | {(b, a) for (a, b) in extras}
            if is_acyclic(n, candidate):
                last = deterministic_topological_sort(n, candidate)
                tup = (exts[first],) + tuple(exts[k] for k in tail) + (last,)
                return tup
    return None


def minimal_axis_count(
    n: int, rel: frozenset, d_cap: int = D_CAP_SEARCH
) -> tuple[int, tuple[tuple[int, ...], ...]]:
    """Smallest d with a d-realizer, by exhaustive search for each d < answer."""
    exts = linear_extensions(n, rel)
    for d in range(1, d_cap + 1):
        realizer = find_axis_realizer(n, rel, d, exts)
        if realizer is not None:
            return d, realizer
    raise ValueError(
        f"minimal axis count exceeds cap {d_cap} (not expected for n <= 6)"
    )


def magnitudes_from_realizer(
    n: int, realizer: tuple[tuple[int, ...], ...]
) -> list[tuple[int, ...]]:
    """Axis magnitudes: event's rank (1-based) in each realizer extension."""
    ranks = [{x: i + 1 for i, x in enumerate(ext)} for ext in realizer]
    return [tuple(r[e] for r in ranks) for e in range(n)]


def componentwise_strict_order(mags: list[tuple[int, ...]]) -> frozenset:
    n = len(mags)
    return frozenset(
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and all(mags[i][k] <= mags[j][k] for k in range(len(mags[i])))
    )


def verify_reconstruction(
    n: int, rel: frozenset, realizer: tuple[tuple[int, ...], ...]
) -> bool:
    """All n^2 ordered pairs: componentwise magnitude order == rel exactly."""
    mags = magnitudes_from_realizer(n, realizer)
    if len(set(mags)) != n:
        return False
    return componentwise_strict_order(mags) == rel


# ---------------------------------------------------------------------------
# Total preorders (scalar axes with ties) - the tie-collapse leg
# ---------------------------------------------------------------------------


def weak_orders(n: int) -> list[tuple[int, ...]]:
    """All total preorders on {0..n-1} as level maps (ordered set partitions)."""
    out: list[tuple[int, ...]] = []

    def rec(remaining: list[int], levels: list[tuple[int, ...]]) -> None:
        if not remaining:
            lev = [0] * n
            for li, block in enumerate(levels):
                for x in block:
                    lev[x] = li
            out.append(tuple(lev))
            return
        rem = tuple(remaining)
        for k in range(1, len(rem) + 1):
            for block in itertools.combinations(rem, k):
                rest = [x for x in rem if x not in block]
                rec(rest, levels + [block])

    rec(list(range(n)), [])
    return out


def preorder_intersection(
    n: int, level_maps: list[tuple[int, ...]]
) -> frozenset | None:
    """Intersection of total preorders, on distinct pairs; None if not
    antisymmetric (then it is not a partial order)."""
    rel = frozenset(
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and all(lev[i] <= lev[j] for lev in level_maps)
    )
    for (i, j) in rel:
        if (j, i) in rel:
            return None
    return rel


def linearize_preorder_realizer(
    n: int, rel: frozenset, level_maps: list[tuple[int, ...]]
) -> list[tuple[int, ...]]:
    """Tie-collapse lemma, constructively: refine each total preorder by a
    fixed linear extension L0 of rel. Each result is a linear extension of
    rel, and their intersection is rel (proof in the T394 spec)."""
    base = deterministic_topological_sort(n, rel)
    pos0 = {x: i for i, x in enumerate(base)}
    return [
        tuple(sorted(range(n), key=lambda x: (lev[x], pos0[x])))
        for lev in level_maps
    ]


# ---------------------------------------------------------------------------
# Standard examples S_d
# ---------------------------------------------------------------------------


def standard_example(d: int) -> tuple[int, frozenset]:
    """S_d on 2d events: a_i = i-1 (i = 1..d), b_j = d+j-1; a_i < b_j iff
    i != j. Index-sorted labeling: all a's before all b's."""
    n = 2 * d
    rel = frozenset((i, d + j) for i in range(d) for j in range(d) if i != j)
    return n, rel


def explicit_standard_realizer(d: int) -> tuple[tuple[int, ...], ...]:
    """d linear extensions of S_d; L_k reverses exactly diagonal pair k."""
    exts = []
    for k in range(d):
        seq = (
            [i for i in range(d) if i != k]
            + [d + k, k]
            + [d + j for j in range(d) if j != k]
        )
        exts.append(tuple(seq))
    return tuple(exts)


def standard_example_certificate(d: int, enumerate_extensions: bool = True) -> dict:
    """Machine-checked ingredients for dim(S_d) >= d.

    (i)   every cross pair a_i < b_j (i != j) is in the order;
    (ii)  every diagonal pair (a_i, b_i) is incomparable;
    (iii) no linear extension reverses two diagonal pairs: for every i < j,
          S_d + {(b_i, a_i), (b_j, a_j)} contains a cycle (C(d,2) checks),
          and (if enumerated) EVERY linear extension reverses at most one;
    (iv)  extension count matches the derived closed form
          (d!)^2 + d*((d-1)!)^2, verified by enumeration.

    The remaining steps to dim(S_d) >= d are two-line logic, stated and
    proved in the T394 spec: exact reconstruction forces each diagonal pair
    to be strictly reversed on some axis, and by (i) one axis cannot
    strictly reverse two diagonal pairs (numeric cycle), so d axes are the
    minimum. The pigeonhole is validated against brute-force search on S_3
    and S_4 below.
    """
    n, rel = standard_example(d)
    cross_ok = all(
        ((i, d + j) in rel) == (i != j) for i in range(d) for j in range(d)
    )
    incs = set(incomparable_pairs(n, rel))
    diag_ok = all((i, d + i) in incs for i in range(d))
    cycle_certs = all(
        not is_acyclic(n, set(rel) | {(d + i, i), (d + j, j)})
        for i in range(d)
        for j in range(i + 1, d)
    )
    closed_form = factorial(d) ** 2 + d * factorial(d - 1) ** 2
    ext_count = None
    max_diag_reversals = None
    if enumerate_extensions:
        exts = linear_extensions(n, rel)
        ext_count = len(exts)
        max_diag_reversals = 0
        for ext in exts:
            pos = {x: i for i, x in enumerate(ext)}
            reversals = sum(1 for i in range(d) if pos[d + i] < pos[i])
            max_diag_reversals = max(max_diag_reversals, reversals)
    realizer = explicit_standard_realizer(d)
    realizer_extends = all(rel <= pairs_of_extension(L) for L in realizer)
    inter = set(pairs_of_extension(realizer[0]))
    for L in realizer[1:]:
        inter &= pairs_of_extension(L)
    realizer_exact = frozenset(inter) == rel
    realizer_reconstructs = verify_reconstruction(n, rel, realizer)
    return {
        "d": d,
        "n": n,
        "cross_pairs_all_present": cross_ok,
        "diagonal_pairs_incomparable": diag_ok,
        "pairwise_reversal_cycle_certificates": cycle_certs,
        "extension_count": ext_count,
        "closed_form_count": closed_form,
        "counts_match": (ext_count == closed_form) if ext_count is not None else None,
        "max_diagonal_reversals_any_extension": max_diag_reversals,
        "explicit_realizer": [list(L) for L in realizer],
        "realizer_all_linear_extensions": realizer_extends,
        "realizer_intersection_exact": realizer_exact,
        "realizer_rank_magnitudes_reconstruct": realizer_reconstructs,
        "lower_bound_certified": cross_ok and diag_ok and cycle_certs,
        "dim_upper_bound": d if realizer_exact else None,
    }


def standard_example_automorphisms(d: int) -> list[tuple[int, ...]]:
    n, rel = standard_example(d)
    return [
        sigma
        for sigma in itertools.permutations(range(n))
        if frozenset((sigma[a], sigma[b]) for (a, b) in rel) == rel
    ]


def refute_dimension_by_orbit_pruned_search(d_target: int, d_example: int) -> dict:
    """Exhaustively refute a d_target-realizer for S_{d_example} using
    automorphism-orbit representatives for the first extension.

    Coverage: if (L_1..L_{d_target}) realizes S_d, so does
    (sigma L_1..sigma L_{d_target}) for any automorphism sigma; choosing
    sigma so that sigma L_1 is its orbit representative shows scanning
    representatives for the first coordinate (all extensions for the rest)
    is complete. Soundness of the orbit action (automorphisms map linear
    extensions to linear extensions) is asserted below.
    """
    n, rel = standard_example(d_example)
    exts = linear_extensions(n, rel)
    ext_set = set(exts)
    auts = standard_example_automorphisms(d_example)
    reps: list[tuple[int, ...]] = []
    seen: set[tuple[int, ...]] = set()
    for ext in exts:
        images = [tuple(sigma[x] for x in ext) for sigma in auts]
        assert all(im in ext_set for im in images), "orbit action unsound"
        rep = min(images)
        if rep not in seen:
            seen.add(rep)
            reps.append(ext)
    realizer = find_axis_realizer(
        n, rel, d_target, exts, first_extension_candidates=reps
    )
    scanned = len(reps) * (len(exts) ** (d_target - 2))
    return {
        "example": f"S_{d_example}",
        "d_refuted": d_target,
        "automorphism_count": len(auts),
        "extension_count": len(exts),
        "orbit_representatives": len(reps),
        "tuples_scanned": scanned,
        "realizer_found": realizer is not None,
    }


# ---------------------------------------------------------------------------
# Theorem 4: record-basis realization via T48's containment rule
# ---------------------------------------------------------------------------


def record_bases(n: int, rel: frozenset, variant: str) -> tuple[dict, dict]:
    """Source/target record bases per event, per variant.

    faithful:  target(e) = locked records of the principal downset of e;
               source(e) = locked records of the strict downset of e,
               plus e's own raw record (mirrors T48's witness: U3 =
               {r_A_locked, r_B_locked, r_composite_raw}).
    single:    one basis per event (locked principal downset) used as both
               source and target (the simplified statement).
    strict:    target(e) = locked records of the STRICT downset (empty for
               minimal events) -- the variant the non-empty clause and
               spurious containments break; kept as the edge-case witness.
    """
    down = {e: {x for (x, y) in rel if y == e} | {e} for e in range(n)}
    strict_down = {e: down[e] - {e} for e in range(n)}
    source: dict[int, frozenset] = {}
    target: dict[int, frozenset] = {}
    for e in range(n):
        if variant == "faithful":
            source[e] = frozenset(
                {("locked", x) for x in strict_down[e]} | {("raw", e)}
            )
            target[e] = frozenset(("locked", x) for x in down[e])
        elif variant == "single":
            source[e] = frozenset(("locked", x) for x in down[e])
            target[e] = source[e]
        elif variant == "strict":
            source[e] = frozenset(
                {("locked", x) for x in strict_down[e]} | {("raw", e)}
            )
            target[e] = frozenset(("locked", x) for x in strict_down[e])
        else:
            raise ValueError(f"unknown variant {variant!r}")
    return source, target


def t48_record_dependency_closure(
    n: int, source: dict, target: dict
) -> frozenset:
    """T48's rule verbatim: e_j directly precedes e_i iff the record basis of
    e_j's target is a NON-EMPTY subset of the record basis of e_i's source;
    then take the reflexive-transitive closure. Returned as the strict part
    (reflexive pairs implicit), for comparison with rel."""
    direct = set()
    for ej in range(n):
        for ei in range(n):
            if ej == ei:
                continue
            if target[ej] and target[ej] <= source[ei]:
                direct.add((ej, ei))
    # transitive closure
    changed = True
    while changed:
        changed = False
        for (a, b) in list(direct):
            for (c, d) in list(direct):
                if b == c and (a, d) not in direct and a != d:
                    direct.add((a, d))
                    changed = True
    return frozenset(direct)


# ---------------------------------------------------------------------------
# House-object spotlight: S_3 as PO1-admissible FinaliEvents
# ---------------------------------------------------------------------------


def build_s3_finalievent_spotlight() -> dict:
    """S_3 built with the repo's own objects: D1RestrictionSystems,
    PO1 admissibility via `check_admissibility`, the record-dependency order
    via T48's `_compute_order`, and AM via T49's `_compare_orders`."""
    from models.d1_restriction_system import (
        D1RestrictionMorphism,
        D1RestrictionSystem,
        LocalD1Value,
        RestrictionPatch,
        SiteMap,
        TransportEdge,
    )
    from models.finali_event_structure import (
        FinaliEvent,
        _compute_order,
        _verify_partial_order,
    )
    from models.multiscale_observer_field import (
        D1Profile,
        ObserverSite,
        PatchConstraint,
    )
    from models.po1_admissibility_conditions import check_admissibility
    from models.projection_obstruction_schema import ProjectionCase
    from models.reconstruction_without_background_time import (
        AxisProfile,
        _compare_orders,
    )

    def _site(sid: str) -> ObserverSite:
        return ObserverSite(sid, "t394", "finite_site", 0, "t394")

    def _lv(sid: str, profile: D1Profile) -> LocalD1Value:
        return LocalD1Value(
            site=_site(sid), proposition_value="true", profile=profile
        )

    def build_system(
        name: str, prefix: str, profile: D1Profile, obstructed: bool
    ) -> D1RestrictionSystem:
        a, b, c = prefix + "a", prefix + "b", prefix + "c"
        closing = "different" if obstructed else "same"
        return D1RestrictionSystem(
            name=name,
            proposition=f"{name}_prop",
            local_values=(_lv(a, profile), _lv(b, profile), _lv(c, profile)),
            transport_edges=(
                TransportEdge(a, b, "link", True),
                TransportEdge(b, c, "link", True),
            ),
            source_site=a,
            target_site=c,
            patches=(
                RestrictionPatch(
                    prefix + "_ab", (a, b), ("x", "y"),
                    (PatchConstraint("x", "y", "same"),),
                ),
                RestrictionPatch(
                    prefix + "_bc", (b, c), ("y", "z"),
                    (PatchConstraint("y", "z", "same"),),
                ),
                RestrictionPatch(
                    prefix + "_ac", (a, c), ("x", "z"),
                    (PatchConstraint("x", "z", closing),),
                ),
            ),
        )

    def build_event(
        name: str, src: D1RestrictionSystem, tgt: D1RestrictionSystem
    ) -> FinaliEvent:
        src_sites = list(src.site_ids())
        tgt_sites = list(tgt.site_ids())
        m = len(tgt_sites)
        site_map = tuple(
            SiteMap(s, tgt_sites[i % m]) for i, s in enumerate(src_sites)
        )
        morphism = D1RestrictionMorphism(
            name=f"finali_{name}",
            source=src,
            target=tgt,
            site_map=site_map,
            preserved_dimensions=("reversal_cost",),
            require_trust_path_preservation=False,
            require_obstruction_preservation=False,
        )
        case = ProjectionCase(
            name=name,
            source="T394",
            richer_system=src,
            restricted_system=tgt,
            morphism=morphism,
            forgotten_structure=("pre_lock_coherence",),
            preserved_structure=(),
            intended_reading="finality-crossing event",
        )
        adm = check_admissibility(case)
        profile = tgt.local_values[0].profile
        return FinaliEvent(
            name=name,
            morphism=morphism,
            causal_magnitude=profile.reversal_cost,
            info_magnitude=profile.holder_redundancy,
            admissibility=adm,
        )

    d = 3
    n, rel = standard_example(d)
    labels = ["a1", "a2", "a3", "b1", "b2", "b3"]  # index-sorted 0..5
    realizer = explicit_standard_realizer(d)
    ranks = [{x: i + 1 for i, x in enumerate(L)} for L in realizer]
    down = {e: {x for (x, y) in rel if y == e} | {e} for e in range(n)}
    strict_down = {e: down[e] - {e} for e in range(n)}

    events = []
    source_records: dict[str, frozenset] = {}
    target_records: dict[str, frozenset] = {}
    for e in range(n):
        tgt_profile = D1Profile(
            accessible_support=ranks[2][e],
            holder_redundancy=ranks[1][e],
            branch_support=0,
            reversal_cost=ranks[0][e],
        )
        src_profile = D1Profile(
            accessible_support=ranks[2][e] + 1,
            holder_redundancy=ranks[1][e] + 1,
            branch_support=1,
            reversal_cost=ranks[0][e] + 1,
        )
        src = build_system(f"U_{labels[e]}", f"u{e}", src_profile, obstructed=False)
        tgt = build_system(f"O_{labels[e]}", f"o{e}", tgt_profile, obstructed=True)
        event = build_event(f"s3_{labels[e]}", src, tgt)
        events.append(event)
        source_records[src.name] = frozenset(
            {("locked", x) for x in strict_down[e]} | {("raw", e)}
        )
        target_records[tgt.name] = frozenset(("locked", x) for x in down[e])

    order_pairs, _direct = _compute_order(events, source_records, target_records)
    po_check = _verify_partial_order(events, order_pairs)
    expected = {
        (f"s3_{labels[i]}", f"s3_{labels[j]}") for (i, j) in rel
    } | {(ev.name, ev.name) for ev in events}
    order_matches = set(order_pairs) == expected

    profiles = [
        AxisProfile(
            event_name=ev.name,
            causal=ev.causal_magnitude,
            info=ev.info_magnitude,
            obs_access=ev.morphism.target.local_values[0].profile.accessible_support,
            branch=ev.morphism.target.local_values[0].profile.branch_support,
        )
        for ev in events
    ]
    record_order = set(order_pairs)
    am_axes = ("causal", "info", "obs_access")
    cmp_full = _compare_orders(profiles, record_order, am_axes)
    subset_results = {}
    for r in (1, 2):
        for axes in itertools.combinations(am_axes, r):
            subset_results[",".join(axes)] = _compare_orders(
                profiles, record_order, axes
            ).is_exact_match
    return {
        "event_names": [ev.name for ev in events],
        "all_po1_admissible": all(ev.admissibility.po1_evidence for ev in events),
        "verdicts": [ev.admissibility.verdict for ev in events],
        "is_partial_order": po_check.is_partial_order,
        "order_matches_s3": order_matches,
        "axis_assignment": (
            "causal=reversal_cost=rank in L1, info=holder_redundancy=rank in "
            "L2, obs_access=accessible_support=rank in L3, branch=0 (unused)"
        ),
        "am_3axis_exact": cmp_full.is_exact_match,
        "am_3axis_matching_pairs": cmp_full.matching_pairs,
        "am_3axis_total_pairs": cmp_full.total_pairs,
        "am_proper_subsets_exact": subset_results,
        "am_proper_subsets_all_fail": not any(subset_results.values()),
    }


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class T394Result:
    caps: dict
    labeling_convention: str
    enumeration: dict
    theorem1: dict
    theorem2: dict
    theorem3: dict
    theorem4: dict
    house_spotlight: dict
    runtimes_s: dict
    all_theorems_hold: bool
    verdict_language: str


def _sweep_classes() -> dict[int, dict[tuple, frozenset]]:
    classes_by_n: dict[int, dict[tuple, frozenset]] = {}
    for n in range(1, N_MAX_ISO_SWEEP + 1):
        classes: dict[tuple, frozenset] = {}
        for rel in natural_transitive_relations(n):
            canon = canonical_form(n, rel)
            classes.setdefault(canon, rel)
        classes_by_n[n] = classes
    return classes_by_n


def run_analysis() -> T394Result:
    runtimes: dict[str, float] = {}
    t_start = time.time()

    # -- enumeration + self-consistency ------------------------------------
    t0 = time.time()
    classes_by_n = _sweep_classes()
    natural_counts = {
        n: len(natural_transitive_relations(n))
        for n in range(1, N_MAX_ISO_SWEEP + 1)
    }
    iso_counts = {n: len(classes_by_n[n]) for n in classes_by_n}
    ext_counts: dict[int, dict[tuple, int]] = {}
    aut_counts: dict[int, dict[tuple, int]] = {}
    labeled_counts: dict[int, int] = {}
    natural_identity_ok = True
    for n, classes in classes_by_n.items():
        ext_counts[n] = {}
        aut_counts[n] = {}
        labeled_total = 0
        natural_total = 0
        for canon, rel in classes.items():
            e_count = len(linear_extensions(n, rel))
            a_count = automorphism_count(n, rel)
            ext_counts[n][canon] = e_count
            aut_counts[n][canon] = a_count
            if factorial(n) % a_count != 0 or e_count % a_count != 0:
                natural_identity_ok = False
            labeled_total += factorial(n) // a_count
            natural_total += e_count // a_count
        labeled_counts[n] = labeled_total
        if natural_total != natural_counts[n]:
            natural_identity_ok = False
    prior_report_match = all(
        labeled_counts.get(n) == v for n, v in PRIOR_REPORT_LABELED_COUNTS.items()
    )
    runtimes["enumeration"] = time.time() - t0

    # -- Theorem 1: minimal axis counts + realizer verification ------------
    t0 = time.time()
    dims_by_n: dict[int, dict[tuple, int]] = {}
    census: dict[int, dict[int, int]] = {}
    realizer_verified_all = True
    classes_checked = 0
    for n, classes in classes_by_n.items():
        dims_by_n[n] = {}
        census[n] = {}
        for canon, rel in classes.items():
            dmin, realizer = minimal_axis_count(n, rel)
            dims_by_n[n][canon] = dmin
            census[n][dmin] = census[n].get(dmin, 0) + 1
            if not verify_reconstruction(n, rel, realizer):
                realizer_verified_all = False
            classes_checked += 1
    runtimes["theorem1_dimension_sweep"] = time.time() - t0

    # -- Theorem 1: tie-collapse (total preorders add nothing) -------------
    t0 = time.time()
    tie_collapse: dict[int, dict] = {}
    linearization_checked = 0
    linearization_all_ok = True
    for n in range(1, N_MAX_PREORDER_SWEEP + 1):
        levels = weak_orders(n)
        achieved: set[frozenset] = set()
        witnesses: dict[frozenset, tuple] = {}
        for l1 in levels:
            for l2 in levels:
                rel = preorder_intersection(n, [l1, l2])
                if rel is not None and rel not in achieved:
                    achieved.add(rel)
                    witnesses[rel] = (l1, l2)
        achieved_canons = {canonical_form(n, r) for r in achieved}
        dim_le_2 = {c for c, d in dims_by_n[n].items() if d <= 2}
        # d = 1: a single total preorder is antisymmetric iff it is a total
        # order, so 1-preorder-representable == chain == dim 1.
        singles = {
            preorder_intersection(n, [l1]) for l1 in levels
        } - {None}
        singles_canons = {canonical_form(n, r) for r in singles}
        dim_le_1 = {c for c, d in dims_by_n[n].items() if d == 1}
        for rel, (l1, l2) in witnesses.items():
            exts = linearize_preorder_realizer(n, rel, [l1, l2])
            ok = all(rel <= pairs_of_extension(L) for L in exts)
            inter = pairs_of_extension(exts[0]) & pairs_of_extension(exts[1])
            ok = ok and frozenset(inter) == rel
            linearization_all_ok = linearization_all_ok and ok
            linearization_checked += 1
        tie_collapse[n] = {
            "weak_order_count": len(levels),
            "achieved_labeled_posets_d2": len(achieved),
            "achieved_equals_dim_le_2": achieved_canons == dim_le_2,
            "achieved_equals_dim_le_1_at_d1": singles_canons == dim_le_1,
        }
    # targeted n = 6, d = 2 refutation for every dimension-3 class
    levels6 = weak_orders(6)
    dim3_refutations = []
    for canon, dmin in dims_by_n[N_MAX_ISO_SWEEP].items():
        if dmin != 3:
            continue
        rel = classes_by_n[N_MAX_ISO_SWEEP][canon]
        extending = [
            lev for lev in levels6 if all(lev[i] <= lev[j] for (i, j) in rel)
        ]
        found = False
        pairs_scanned = 0
        for l1 in extending:
            for l2 in extending:
                pairs_scanned += 1
                if preorder_intersection(6, [l1, l2]) == rel:
                    found = True
                    break
            if found:
                break
        dim3_refutations.append(
            {
                "class_pairs_index_sorted": sorted(rel),
                "extending_weak_orders": len(extending),
                "pairs_scanned": pairs_scanned,
                "two_preorder_representation_found": found,
            }
        )
    runtimes["theorem1_tie_collapse"] = time.time() - t0

    theorem1 = {
        "statement": (
            "P exactly reconstructible by d monotone axis magnitudes under "
            "componentwise order iff dim(P) <= d (P = intersection of d "
            "linear extensions)"
        ),
        "classes_checked": classes_checked,
        "dimension_census": {n: dict(sorted(c.items())) for n, c in census.items()},
        "realizer_rank_magnitudes_reconstruct_all": realizer_verified_all,
        "minimality_by_exhaustive_scan": True,
        "tie_collapse": tie_collapse,
        "dim3_two_preorder_refutation_n6": dim3_refutations,
        "dim3_refutation_all_negative": all(
            not r["two_preorder_representation_found"] for r in dim3_refutations
        ),
        "linearization_witnesses_checked": linearization_checked,
        "linearization_all_ok": linearization_all_ok,
        "holds": (
            realizer_verified_all
            and linearization_all_ok
            and all(
                tc["achieved_equals_dim_le_2"] and tc["achieved_equals_dim_le_1_at_d1"]
                for tc in tie_collapse.values()
            )
            and all(
                not r["two_preorder_representation_found"] for r in dim3_refutations
            )
        ),
    }

    # -- Theorem 2: Anti-Scalar as d = 1 ------------------------------------
    t0 = time.time()
    dim1_iff_chain = True
    for n, classes in classes_by_n.items():
        for canon, rel in classes.items():
            chain = is_chain(n, rel)
            if (dims_by_n[n][canon] == 1) != chain:
                dim1_iff_chain = False
            if incomparable_pairs(n, rel) and dims_by_n[n][canon] < 2:
                dim1_iff_chain = False
    # T49 witness regression: the 3-event shape e1, e2 < e3, e1 || e2
    t49_rel = frozenset({(0, 2), (1, 2)})
    t49_dim, t49_realizer = minimal_axis_count(3, t49_rel)
    t49_incs = incomparable_pairs(3, t49_rel)
    t49_reconstructs = verify_reconstruction(3, t49_rel, t49_realizer)
    # cross-artifact regression against the actual T49 model
    from models.reconstruction_without_background_time import run_t49_analysis

    t49_run = run_t49_analysis()
    t49_names = sorted({a for (a, b) in t49_run.record_order_pairs})
    name_index = {name: k for k, name in enumerate(t49_names)}  # index-sorted
    t49_model_rel = frozenset(
        (name_index[a], name_index[b])
        for (a, b) in t49_run.record_order_pairs
        if a != b
    )
    t49_model_dim, _ = minimal_axis_count(3, t49_model_rel)
    theorem2 = {
        "statement": (
            "dim(P) = 1 iff P is a chain; any incomparable pair forces "
            "dim(P) >= 2 -- T49's Anti-Scalar Theorem is the d = 1 rung"
        ),
        "dim1_iff_chain_all_classes": dim1_iff_chain,
        "t49_shape_dim": t49_dim,
        "t49_shape_incomparable_pairs_index_sorted": sorted(t49_incs),
        "t49_shape_realizer_reconstructs": t49_reconstructs,
        "t49_model_record_order_dim": t49_model_dim,
        "t49_model_2axis_exact_match": t49_run.comparison_2axis.is_exact_match,
        "t49_model_relation_matches_shape": t49_model_rel == t49_rel,
        "holds": (
            dim1_iff_chain
            and t49_dim == 2
            and t49_reconstructs
            and t49_model_dim == 2
            and t49_run.comparison_2axis.is_exact_match
            and t49_model_rel == t49_rel
        ),
    }
    runtimes["theorem2"] = time.time() - t0

    # -- Theorem 3: standard examples ---------------------------------------
    t0 = time.time()
    s3_cert = standard_example_certificate(3)
    s4_cert = standard_example_certificate(4)
    s5_cert = standard_example_certificate(5)
    # brute-force cross-validation of the certificate lower bounds
    n3, rel3 = standard_example(3)
    s3_dmin, _ = minimal_axis_count(n3, rel3)
    s4_refute_d3 = refute_dimension_by_orbit_pruned_search(3, 4)
    n4, rel4 = standard_example(4)
    s4_d2 = find_axis_realizer(n4, rel4, 2) is not None
    theorem3 = {
        "statement": (
            "for every d, S_d (2d events) needs exactly d axes; hence the "
            "four D1 axes reconstruct exactly the event structures of order "
            "dimension <= 4, and S_5 (10 events) escapes 4-axis "
            "reconstruction"
        ),
        "S3": {**s3_cert, "brute_force_minimal_axis_count": s3_dmin},
        "S4": {
            **s4_cert,
            "d2_realizer_found": s4_d2,
            "d3_refutation": s4_refute_d3,
        },
        "S5": {
            **s5_cert,
            "d4_brute_force": (
                "not attempted: ~4e10 orbit-pruned pair scans; infeasible. "
                "dim(S_5) >= 5 rests on the machine-checked certificate "
                "(cross pairs + diagonal incomparability + at-most-one "
                "reversal, the latter verified over all 17280 extensions) "
                "plus the two-line pigeonhole in the spec."
            ),
        },
        "certificate_cross_validated_on": ["S_3", "S_4"],
        "holds": (
            s3_cert["lower_bound_certified"]
            and s4_cert["lower_bound_certified"]
            and s5_cert["lower_bound_certified"]
            and s3_cert["realizer_intersection_exact"]
            and s4_cert["realizer_intersection_exact"]
            and s5_cert["realizer_intersection_exact"]
            and s3_cert["max_diagonal_reversals_any_extension"] == 1
            and s4_cert["max_diagonal_reversals_any_extension"] == 1
            and s5_cert["max_diagonal_reversals_any_extension"] == 1
            and s3_cert["counts_match"]
            and s4_cert["counts_match"]
            and s5_cert["counts_match"]
            and s3_dmin == 3
            and not s4_d2
            and not s4_refute_d3["realizer_found"]
        ),
    }
    runtimes["theorem3"] = time.time() - t0

    # -- Theorem 4: record-basis realization --------------------------------
    t0 = time.time()
    faithful_all = True
    single_all = True
    strict_success = 0
    strict_success_all_antichains = True
    strict_total = 0
    nonempty_clause_vacuous_for_principal = True
    for n, classes in classes_by_n.items():
        for canon, rel in classes.items():
            for variant in ("faithful", "single", "strict"):
                source, target = record_bases(n, rel, variant)
                closure = t48_record_dependency_closure(n, source, target)
                exact = closure == rel
                if variant == "faithful":
                    faithful_all = faithful_all and exact
                    if any(not target[e] for e in range(n)):
                        nonempty_clause_vacuous_for_principal = False
                elif variant == "single":
                    single_all = single_all and exact
                else:
                    strict_total += 1
                    if exact:
                        strict_success += 1
                        if rel:  # non-antichain success would be anomalous
                            strict_success_all_antichains = False
    # explicit 2-chain failure witness for the strict variant
    chain2 = frozenset({(0, 1)})
    src2, tgt2 = record_bases(2, chain2, "strict")
    strict_chain2_closure = t48_record_dependency_closure(2, src2, tgt2)
    theorem4 = {
        "statement": (
            "every finite poset is the record-dependency order of a "
            "FinaliEvent structure via principal-downset record bases under "
            "T48's non-empty-subset containment rule"
        ),
        "classes_checked": classes_checked,
        "faithful_variant_exact_all": faithful_all,
        "single_basis_variant_exact_all": single_all,
        "nonempty_clause_vacuous_for_principal_downsets":
            nonempty_clause_vacuous_for_principal,
        "strict_downset_variant_exact_count": strict_success,
        "strict_downset_variant_total": strict_total,
        "strict_variant_succeeds_only_on_antichains":
            strict_success_all_antichains,
        "strict_two_chain_failure_witness": {
            "poset_pairs_index_sorted": sorted(chain2),
            "closure_pairs_index_sorted": sorted(strict_chain2_closure),
            "fails": strict_chain2_closure != chain2,
        },
        "holds": (
            faithful_all
            and single_all
            and nonempty_clause_vacuous_for_principal
            and strict_success_all_antichains
            and strict_chain2_closure != chain2
        ),
    }
    runtimes["theorem4"] = time.time() - t0

    # -- house spotlight -----------------------------------------------------
    t0 = time.time()
    spotlight = build_s3_finalievent_spotlight()
    runtimes["house_spotlight"] = time.time() - t0
    runtimes["total"] = time.time() - t_start

    enumeration = {
        "iso_class_counts": iso_counts,
        "natural_labeled_counts": natural_counts,
        "labeled_counts": labeled_counts,
        "natural_count_identity_holds": natural_identity_ok,
        "labeled_counts_match_prior_report": prior_report_match,
        "prior_report_targets": PRIOR_REPORT_LABELED_COUNTS,
    }

    spotlight_holds = (
        spotlight["all_po1_admissible"]
        and spotlight["is_partial_order"]
        and spotlight["order_matches_s3"]
        and spotlight["am_3axis_exact"]
        and spotlight["am_proper_subsets_all_fail"]
    )
    all_hold = (
        enumeration["natural_count_identity_holds"]
        and enumeration["labeled_counts_match_prior_report"]
        and theorem1["holds"]
        and theorem2["holds"]
        and theorem3["holds"]
        and theorem4["holds"]
        and spotlight_holds
    )

    verdict_language = (
        "All four theorems hold in the verified finite ranges (posets up to "
        "n = 6 up to isomorphism; tie-collapse exhaustively at n <= 5, d <= 2 "
        "and at n = 6, d = 2 for the dimension-3 classes; S_3/S_4 by "
        "exhaustive search; S_5 by machine-checked certificate). This is "
        "finite mathematics about the reconstruction formalism: no claim "
        "promotion, no physics claim, no spacetime claim. Whether physical "
        "causal orders exceed order dimension 4 is an open question flagged "
        "as candidate prior-art territory in the spec."
    )

    return T394Result(
        caps={
            "N_MAX_ISO_SWEEP": N_MAX_ISO_SWEEP,
            "N_MAX_PREORDER_SWEEP": N_MAX_PREORDER_SWEEP,
            "D_MAX_PREORDER_SWEEP": D_MAX_PREORDER_SWEEP,
            "D_CAP_SEARCH": D_CAP_SEARCH,
        },
        labeling_convention=LABELING_CONVENTION,
        enumeration=enumeration,
        theorem1=theorem1,
        theorem2=theorem2,
        theorem3=theorem3,
        theorem4=theorem4,
        house_spotlight=spotlight,
        runtimes_s={k: round(v, 3) for k, v in runtimes.items()},
        all_theorems_hold=all_hold,
        verdict_language=verdict_language,
    )


def result_to_dict(result: T394Result) -> dict[str, Any]:
    return {
        "artifact": "T394-axis-count-reconstruction-hierarchy-v0.1",
        "caps": result.caps,
        "labeling_convention": result.labeling_convention,
        "enumeration": result.enumeration,
        "theorem1_reconstruction": result.theorem1,
        "theorem2_anti_scalar_d1": result.theorem2,
        "theorem3_axis_count_obstruction": result.theorem3,
        "theorem4_realizability": result.theorem4,
        "house_spotlight_s3_finalievents": result.house_spotlight,
        "runtimes_s": result.runtimes_s,
        "all_theorems_hold": result.all_theorems_hold,
        "verdict_language": result.verdict_language,
    }


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(result_to_dict(res), indent=2, default=str))
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"iso classes checked (n=1..6):        {res.theorem1['classes_checked']}")
    print(f"iso counts:                          {res.enumeration['iso_class_counts']}")
    print(f"labeled counts:                      {res.enumeration['labeled_counts']}")
    print(f"dimension census:                    {res.theorem1['dimension_census']}")
    print(f"T1 realizer magnitudes reconstruct:  {res.theorem1['realizer_rank_magnitudes_reconstruct_all']}")
    print(f"T1 tie-collapse adds nothing:        {res.theorem1['holds']}")
    print(f"T2 dim=1 iff chain (all classes):    {res.theorem2['dim1_iff_chain_all_classes']}")
    print(f"T2 T49 witness dim:                  {res.theorem2['t49_shape_dim']} (model regression: {res.theorem2['t49_model_record_order_dim']})")
    print(f"T3 S_3 minimal axes (brute force):   {res.theorem3['S3']['brute_force_minimal_axis_count']}")
    print(f"T3 S_4 d=3 refuted, d=4 realizer:    {not res.theorem3['S4']['d3_refutation']['realizer_found']}, {res.theorem3['S4']['realizer_intersection_exact']}")
    print(f"T3 S_5 cert (>=5) + 5-realizer:      {res.theorem3['S5']['lower_bound_certified']}, {res.theorem3['S5']['realizer_intersection_exact']}")
    print(f"T4 faithful / single variants:       {res.theorem4['faithful_variant_exact_all']} / {res.theorem4['single_basis_variant_exact_all']}")
    print(f"T4 strict variant only antichains:   {res.theorem4['strict_variant_succeeds_only_on_antichains']}")
    print(f"House S_3 FinaliEvents (PO1/AM):     {res.house_spotlight['all_po1_admissible']} / {res.house_spotlight['am_3axis_exact']} (subsets fail: {res.house_spotlight['am_proper_subsets_all_fail']})")
    print(f"runtimes (s):                        {res.runtimes_s}")
    print("-" * 70)
    print(f"ALL THEOREMS HOLD: {res.all_theorems_hold}")
    print(res.verdict_language)
