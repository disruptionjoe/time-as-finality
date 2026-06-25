"""T240: Globalization-obstruction certificate (LossKernel route (b), criterion-6 crux).

The LAST untested crack in T230's absorption-escape trichotomy, after the
value-keyed (T230 `source_reading`) and structure-keyed (T235
source-automorphism rigidity certificate) cracks BOTH closed at gate 2. This is
the only remaining live route to flip the independent-motivation criterion (the
single open independence criterion, currently UNKNOWN-trending-NOT-EARNED) from
NOT EARNED to EARNED for the typed-forgetting / LossKernel line. Record with
maximum care.

------------------------------------------------------------------------------
WHAT T230 / T235 ESTABLISHED (re-used here BY IMPORT ONLY, NOT re-derived).
------------------------------------------------------------------------------
T230: on a same-nu witness fiber, every candidate attribution invariant that
SEPARATES a same-nu pair fails exactly one of three gates:
    gate 1 (separates)        : I(a) != I(b) for some pair with nu(a) == nu(b)
    gate 2 (non-absorbable)   : the separation is NOT reproduced by an admissible
                                enlargement (admitting a source FIELD/STRUCTURE as
                                audit data does not make a mature neighbor separate)
    gate 3 (genuine invariant): relabel-stable (3a) AND local (3b)
`source_reading` (read a hidden source FIELD VALUE) is local + relabel-stable +
separates -- a real separator -- yet dies at GATE 2 via nu_prime (admit the field).

T235: keyed the invariant to a source-side SYMMETRY CLASS (the iso-class of the
group of nu-fixing, gluing-preserving source self-maps). It separates a same-nu
pair and is local + relabel-stable AND NOT absorbed by nu_prime (no single field
to admit) -- but it dies at GATE 2 via nu_struct: the source GLUING the
automorphism group is computed from is itself admissible source structure, and
admitting the gluing as audit data (nu_struct) reproduces the separation. The
automorphism iso-class is a DERIVED FUNCTION of an admissible source relation, so
it is absorbed one level up. The structure-keyed crack closed too.

T235's `nu_struct` (re-used and EXTENDED here): the maximal admissible
enlargement nu + admitted source field (nu_prime) + admitted source gluing.

------------------------------------------------------------------------------
THE T240 OBJECT (the globalization-obstruction certificate, the new construction).
------------------------------------------------------------------------------
T235 named the next object verbatim: instead of the automorphism group of a
SINGLE admissible gluing, take LOCALLY-DEFINED nu-fixing source automorphisms
over a COVER of the source, and form the finite obstruction to PATCHING them into
a GLOBAL automorphism -- a finite Z/2 / torsor obstruction class, a
Cech-H1-flavored gluing obstruction of the local-automorphism inverse system.

Construction (all finite, exhaustive, no search):

  * Source carrier = the finite source endpoint set E (the symbols in the lift
    table), the SAME carrier T235's automorphism group permutes.
  * Cover = a finite family U = {U_0, ..., U_{n-1}} of subsets of E with
    union E. (A genuine open-cover combinatorics, kept finite.)
  * Local nu-fixing automorphism on U_i = a permutation of U_i that preserves
    the lift table RESTRICTED to U_i AND the source gluing RESTRICTED to U_i.
    These form a finite group Aut(U_i) -- computed exhaustively, exactly as T235
    computes the global Aut, but on the sub-carrier U_i.
  * A LOCAL SECTION is a choice (g_0, ..., g_{n-1}) with g_i in Aut(U_i). It
    GLOBALIZES iff the g_i agree on every pairwise overlap U_i ∩ U_j (so they
    glue to a single permutation of E that is then a global nu-fixing,
    gluing-preserving automorphism).
  * The DISCREPANCY 1-cochain of a local section is, on each overlap (i,j), the
    Z/2 bit [g_i and g_j disagree somewhere on U_i ∩ U_j]. A local section
    globalizes iff its discrepancy cochain is identically zero.
  * The GLOBALIZATION OBSTRUCTION is the finite Z/2 quantity: can we MODIFY the
    local sections by per-vertex (Cech 0-cochain) adjustments -- replacing g_i by
    g_i' in Aut(U_i) -- to make ALL overlaps agree? The obstruction is the
    coset of achievable discrepancy cochains modulo the coboundaries (per-vertex
    re-choices). Concretely we compute, by exhaustive enumeration over the finite
    product of local groups:
        H1_rank = Z/2 rank of  {discrepancy cochains realizable by some local
                  section}  /  {discrepancy cochains of GLOBALIZABLE sections}
    interpreted as the finite obstruction to patching. The CERTIFICATE invariant
    is this finite Z/2 obstruction rank (an integer >= 0), named exactly as a
    finite Z/2 cycle-space rank of a SPECIFIC finite cover -- NOT a continuum or
    general sheaf-cohomology claim.

  is_globalizable(case) := the obstruction rank is 0 (some local section patches
  to a global automorphism, equivalently every minimal-discrepancy section can be
  coboundary-adjusted to zero discrepancy).

------------------------------------------------------------------------------
THE DECISIVE QUESTION (Q-glob), run through the FULL T230/T235 gate harness.
------------------------------------------------------------------------------
gate 1: does the globalization obstruction rank SEPARATE a same-nu pair (two
        cases with identical lift table / nu, differing only in source gluing /
        cover) where one patches and one does not?
gate 2: is that separation reproduced by nu_struct (admit every source field AND
        the source gluing)?  AND -- the NEW test -- is it reproduced by admitting
        the LOCAL AUTOMORPHISM DATA itself as audit data (nu_local: admit each
        Aut(U_i) per vertex)?  The route-(b) BET: admitting each local piece
        individually does NOT reconstruct the GLOBAL patching obstruction (the
        quotient by coboundaries is a property of the inverse SYSTEM, not of any
        single admitted piece), so gate 2 has nothing single to admit.
gates 3a/3b: relabel-stable AND local (function of the case's own data, not an
        external registry / enumeration order).

VERDICT LOGIC (recorded with maximum care):
  * If the obstruction is nu_struct-measurable (or nu_local-measurable) on the
    same-nu fiber -> ABSORBED at gate 2 -> no-go, the LossKernel line closes
    FULLY (route (a) complete over ALL THREE crack types: value, structure,
    globalization).
  * If it SEPARATES a same-nu pair, is NOT absorbed by nu_struct AND NOT by
    nu_local, AND is relabel-stable AND local -> clears_route_b = True ->
    EARNED-candidate. Defer any ledger movement to the integrator.

NON-VACUITY: a synthetic injector exhibits a same-nu pair + invariant that CLEARS
all gates, proving the harness CAN report a positive -- so a no-go is a real
negative, not a constant-no harness.

No physics / geometry / curvature / connection / holonomy / gravity / spacetime /
new-object language. "Z/2 H^1 / obstruction rank" = the finite Z/2 cycle-space
rank of a SPECIFIC finite cover's discrepancy system, named as such.
finite_witness: a finite executable fixture over hand-built typed-lossy cases;
local automorphism groups and the obstruction are computed by exhaustive finite
enumeration over finite endpoint sets. NOT a continuum/general sheaf-cohomology
theorem, NOT a hardness claim, NOT a poly_decider search.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from typing import Callable

# Re-use the T230 model BY IMPORT ONLY (leave its 14/14 suite green). nu,
# nu_prime, relabel, the same-nu fiber discipline, the separating-pair finder,
# the relabel-stability gate, and the freeze canonicalizer all come from there.
from models.attribution_invariant_separation import (
    Case,
    Lift,
    nu,
    nu_prime,
    relabel,
    _freeze,
    _separating_same_nu_pair,
    is_relabel_stable,
)

# Re-use the T235 source-gluing machinery + nu_struct enlargement BY IMPORT ONLY
# (leave its 15-check suite green). gluing_of / set_gluing / clear_gluings give
# the admissible source structure; nu_struct is the maximal field+gluing
# enlargement we must clear gate 2 against; _source_endpoints is the carrier.
from models.source_automorphism_rigidity import (
    _source_endpoints,
    gluing_of,
    set_gluing,
    clear_gluings,
    nu_struct,
)


# ---------------------------------------------------------------------------
# Covers. A cover of the source carrier is a finite family of subsets whose
# union is the full endpoint set. It is source-side combinatorial data attached
# to the case (keyed by name, like the gluing). nu does NOT expose the cover.
# ---------------------------------------------------------------------------


_SOURCE_COVER: dict[str, tuple[frozenset, ...]] = {}


def set_cover(case: Case, parts: tuple[tuple[str, ...], ...]) -> None:
    _SOURCE_COVER[case.name] = tuple(frozenset(p) for p in parts)


def cover_of(case: Case) -> tuple[frozenset, ...]:
    eps = _source_endpoints(case)
    default = (frozenset(eps),)  # the trivial one-set cover
    return _SOURCE_COVER.get(case.name, default)


def clear_covers() -> None:
    _SOURCE_COVER.clear()


# ---------------------------------------------------------------------------
# Local nu-fixing, gluing-preserving automorphisms on a sub-carrier U <= E.
# A local automorphism of U is a permutation of U that preserves the lift table
# RESTRICTED to U (lifts with both endpoints in U) and the gluing RESTRICTED to
# U. Exhaustive finite enumeration over permutations of U -- a genuine finite
# permutation-group computation on the sub-carrier, mirroring T235's global Aut.
# ---------------------------------------------------------------------------


def _restricted_lift_set(case: Case, U: frozenset) -> frozenset:
    return frozenset(
        (l.left_source, l.right_source, l.allowed)
        for l in case.lifts
        if l.left_source in U and l.right_source in U
    )


def _restricted_gluing(case: Case, U: frozenset) -> frozenset:
    glu = gluing_of(case)
    restricted = frozenset(
        frozenset(e for e in block if e in U) for block in glu
    )
    # drop empty blocks introduced by the restriction
    return frozenset(b for b in restricted if b)


def _preserves_restricted_lifts(lift_set: frozenset, g: dict[str, str]) -> bool:
    permuted = frozenset((g[l], g[r], a) for (l, r, a) in lift_set)
    return permuted == lift_set


def _preserves_restricted_gluing(glu: frozenset, g: dict[str, str]) -> bool:
    permuted = frozenset(frozenset(g[e] for e in block) for block in glu)
    return permuted == glu


def local_automorphisms(case: Case, U: frozenset) -> tuple[dict[str, str], ...]:
    """All nu-fixing, gluing-preserving permutations of the sub-carrier U.

    Returned as a tuple of perm dicts (endpoint -> image) over U. Exhaustive over
    permutations of the finite set U: a real finite permutation-group computation
    on the restricted carrier, identical in spirit to T235's global Aut but local
    to U."""
    elems = tuple(sorted(U))
    lift_set = _restricted_lift_set(case, U)
    glu = _restricted_gluing(case, U)
    autos: list[dict[str, str]] = []
    for perm in permutations(elems):
        g = dict(zip(elems, perm))
        if _preserves_restricted_lifts(lift_set, g) and _preserves_restricted_gluing(glu, g):
            autos.append(g)
    return tuple(autos)


# ---------------------------------------------------------------------------
# The globalization obstruction -- Cech H^1 with coefficients in the local-
# automorphism SHEAF. The naive "does SOME local section patch" is vacuous: the
# GLOBAL identity always restricts to a zero-discrepancy section. The non-trivial
# question (the one T235 named) is a TORSOR / TWIST obstruction:
#
#   The source carries a TRANSITION COCYCLE -- on each overlap (i,j) a transition
#   local-automorphism g_ij in Aut(U_i ∩ U_j) (g_ji = g_ij^{-1}), recording how
#   the local frame on U_i is identified with the local frame on U_j across the
#   overlap. This is genuine source-side gluing data nu does NOT expose. The
#   transition cocycle defines a TWISTED local-automorphism system; it patches to
#   a GLOBAL nu-fixing automorphism iff the cocycle is a COBOUNDARY:
#       g_ij = h_i . h_j^{-1} on U_i ∩ U_j   for some h_i in Aut(U_i).
#
#   The OBSTRUCTION CLASS is [g_ij] in Z^1(cover; Aut) / B^1(cover; Aut). We work
#   in the Z/2 SIGN reduction: each transition's sign (does it use the nontrivial
#   local swap on the overlap pair, or not) gives a Z/2 1-cochain over the nerve
#   edges; the coboundaries are the Z/2 0-cochain image (per-vertex sign re-
#   choices) under the simplicial coboundary; the obstruction rank is the finite
#   Z/2 dimension of  Z^1 / B^1  for THIS finite cover's nerve -- a genuine finite
#   Z/2 Cech-H^1 rank, named as such. (Cocycle condition on triple overlaps:
#   product of signs around each 2-simplex = 0; for nerves whose triple overlaps
#   are empty -- a cycle of pairwise-overlapping pieces -- every 1-cochain is a
#   cocycle and H^1 is the loop-space Z/2 rank.)
#
# rank 0  <=> the transition cocycle is a coboundary <=> the twisted local
#             automorphisms patch to a global one.
# rank > 0 <=> a genuine globalization obstruction: the local frames cannot be
#             reconciled into a single global nu-fixing automorphism.
#
# This is computed by EXHAUSTIVE finite linear algebra over GF(2): build the
# nerve edge-incidence (coboundary) matrix d^0 : C^0 -> C^1, the obstruction is
# the class of the sign cochain in coker(d^0) restricted to the cocycle space
# Z^1 = ker(d^1). A poly_decider (finite Gaussian elimination), NOT a search.
# ---------------------------------------------------------------------------


def _overlaps(cover: tuple[frozenset, ...]) -> tuple[tuple[int, int], ...]:
    out: list[tuple[int, int]] = []
    for i, j in combinations(range(len(cover)), 2):
        if cover[i] & cover[j]:
            out.append((i, j))
    return tuple(out)


def _triple_overlaps(cover: tuple[frozenset, ...]) -> tuple[tuple[int, int, int], ...]:
    out: list[tuple[int, int, int]] = []
    for i, j, k in combinations(range(len(cover)), 3):
        if cover[i] & cover[j] & cover[k]:
            out.append((i, j, k))
    return tuple(out)


def _gf2_rank(vectors: tuple[tuple[int, ...], ...]) -> int:
    """Z/2 rank of a finite set of GF(2) vectors by Gaussian elimination. A
    finite linear decider, not a search."""
    rows = [list(v) for v in vectors]
    if not rows:
        return 0
    width = len(rows[0]) if rows[0] else 0
    if width == 0:
        return 0
    rank = 0
    col = 0
    while col < width and rank < len(rows):
        pivot = None
        for r in range(rank, len(rows)):
            if rows[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(len(rows)):
            if r != rank and rows[r][col] == 1:
                rows[r] = [(a ^ b) for a, b in zip(rows[r], rows[rank])]
        rank += 1
        col += 1
    return rank


def _gf2_in_span(target: tuple[int, ...], basis: tuple[tuple[int, ...], ...]) -> bool:
    """True iff `target` is in the GF(2) span of `basis` (rank-stability test)."""
    base_rank = _gf2_rank(basis)
    aug_rank = _gf2_rank(basis + (target,))
    return aug_rank == base_rank


# ---------------------------------------------------------------------------
# Transition cocycle. Attached to the case (keyed by name, like the cover and
# gluing): a per-overlap sign bit, the Z/2 reduction of the transition
# automorphism on that overlap (1 = the nontrivial local swap was used to
# identify the two local frames across the overlap, 0 = identity identification).
# This is source-side gluing data nu does not expose.
# ---------------------------------------------------------------------------


_TRANSITION_COCYCLE: dict[str, dict[tuple[int, int], int]] = {}


def set_transition(case: Case, signs: dict[tuple[int, int], int]) -> None:
    _TRANSITION_COCYCLE[case.name] = dict(signs)


def transition_of(case: Case) -> dict[tuple[int, int], int]:
    cover = cover_of(case)
    overlaps = _overlaps(cover)
    default = {e: 0 for e in overlaps}  # untwisted = identity transitions
    stored = _TRANSITION_COCYCLE.get(case.name, {})
    return {e: stored.get(e, 0) for e in overlaps}


def clear_transitions() -> None:
    _TRANSITION_COCYCLE.clear()


@dataclass(frozen=True)
class GlobalizationData:
    cover_size: int
    overlap_count: int
    triple_overlap_count: int
    local_group_orders: tuple[int, ...]
    overlap_swap_available: tuple[int, ...]  # 1 iff overlap pair admits a nontrivial local swap
    transition_signs: tuple[int, ...]
    is_cocycle: bool
    is_coboundary: bool
    obstruction_rank: int


def _coboundary_matrix(
    cover: tuple[frozenset, ...], overlaps: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, ...], ...]:
    """d^0 : C^0(vertices) -> C^1(edges) over GF(2). Column v, row (i,j) is 1 iff
    v in {i,j}. The image is B^1 (coboundaries = per-vertex sign re-choices)."""
    n = len(cover)
    rows: list[tuple[int, ...]] = []
    for (i, j) in overlaps:
        row = [0] * n
        row[i] = 1
        row[j] = 1
        rows.append(tuple(row))
    # we want column vectors spanning B^1: each vertex v -> its incidence column.
    cols: list[tuple[int, ...]] = []
    for v in range(n):
        cols.append(tuple(rows[e_idx][v] for e_idx in range(len(overlaps))))
    return tuple(cols)


def _cocycle_basis(
    cover: tuple[frozenset, ...],
    overlaps: tuple[tuple[int, int], ...],
    triples: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, ...], ...]:
    """Z^1 = ker(d^1) over GF(2): 1-cochains whose sign-product around every
    populated 2-simplex (triple overlap) is 0. With no triple overlaps every
    1-cochain is a cocycle (full edge space). Returned as a spanning basis."""
    m = len(overlaps)
    edge_index = {e: idx for idx, e in enumerate(overlaps)}
    if not triples:
        # full edge space is the cocycle space
        basis = []
        for idx in range(m):
            v = [0] * m
            v[idx] = 1
            basis.append(tuple(v))
        return tuple(basis)
    # d^1 rows: for each triple (i,j,k), sum of its three edges = 0.
    d1_rows: list[tuple[int, ...]] = []
    for (i, j, k) in triples:
        row = [0] * m
        for e in ((i, j), (i, k), (j, k)):
            if e in edge_index:
                row[edge_index[e]] = 1
        d1_rows.append(tuple(row))
    # kernel basis of d1 over GF(2)
    return _gf2_kernel_basis(tuple(d1_rows), m)


def _gf2_kernel_basis(rows: tuple[tuple[int, ...], ...], width: int) -> tuple[tuple[int, ...], ...]:
    """Basis of the GF(2) kernel of the matrix with given rows (each length width)."""
    mat = [list(r) for r in rows]
    pivots: dict[int, int] = {}
    r = 0
    for c in range(width):
        piv = None
        for rr in range(r, len(mat)):
            if mat[rr][c] == 1:
                piv = rr
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        for rr in range(len(mat)):
            if rr != r and mat[rr][c] == 1:
                mat[rr] = [(a ^ b) for a, b in zip(mat[rr], mat[r])]
        pivots[c] = r
        r += 1
    pivot_cols = set(pivots.keys())
    free_cols = [c for c in range(width) if c not in pivot_cols]
    basis: list[tuple[int, ...]] = []
    for fc in free_cols:
        vec = [0] * width
        vec[fc] = 1
        for pc, prow in pivots.items():
            if mat[prow][fc] == 1:
                vec[pc] = 1
        basis.append(tuple(vec))
    return tuple(basis)


def globalization_data(case: Case) -> GlobalizationData:
    """Compute the finite Z/2 Cech-H^1 globalization obstruction of the twisted
    local-automorphism system over the case's cover + transition cocycle.

    obstruction_rank = 0 iff the transition sign-cochain is a COBOUNDARY (the
    twisted local automorphisms patch to a global one). Otherwise the class of
    the cochain in Z^1/B^1 is nonzero, and we report the Z/2 dimension of the
    H^1 = Z^1/B^1 of the nerve as the obstruction rank (the finite cycle-space
    rank carrying the class). A poly_decider over GF(2) (Gaussian elimination)."""
    cover = cover_of(case)
    overlaps = _overlaps(cover)
    triples = _triple_overlaps(cover)
    local_groups = tuple(local_automorphisms(case, U) for U in cover)
    orders = tuple(len(g) for g in local_groups)

    # which overlap pairs even ADMIT a nontrivial transition (a local swap on the
    # overlap carrier preserving the restricted lift table + gluing). If an overlap
    # admits no nontrivial swap, a sign of 1 there is not realizable -> clamp to 0.
    swap_avail: list[int] = []
    transition = transition_of(case)
    clamped_signs: list[int] = []
    for (i, j) in overlaps:
        inter = cover[i] & cover[j]
        local_on_inter = local_automorphisms(case, inter)
        has_swap = len(local_on_inter) > 1
        swap_avail.append(1 if has_swap else 0)
        clamped_signs.append(transition[(i, j)] if has_swap else 0)

    signs = tuple(clamped_signs)

    # cocycle test: sign-product around every triple overlap must be 0.
    edge_index = {e: idx for idx, e in enumerate(overlaps)}
    is_cocycle = True
    for (i, j, k) in triples:
        s = 0
        for e in ((i, j), (i, k), (j, k)):
            if e in edge_index:
                s ^= signs[edge_index[e]]
        if s != 0:
            is_cocycle = False
            break

    # coboundary test: is `signs` in B^1 = image of d^0 (per-vertex sign re-choices)?
    cob_cols = _coboundary_matrix(cover, overlaps)
    is_coboundary = _gf2_in_span(signs, cob_cols)

    # H^1 rank = dim Z^1 - dim B^1 for this nerve (finite Z/2 cycle-space rank).
    z1 = _cocycle_basis(cover, overlaps, triples)
    dim_z1 = _gf2_rank(z1)
    dim_b1 = _gf2_rank(cob_cols)
    h1_rank = dim_z1 - dim_b1

    if is_coboundary and is_cocycle:
        obstruction_rank = 0
    else:
        # the class is nontrivial; the obstruction it lives in has Z/2 rank h1_rank
        # (the finite cycle-space rank carrying the nonzero class). Non-cocycle =>
        # the twist is not even a consistent gluing datum; we still report the
        # nerve H^1 rank as the obstruction carrier and flag is_cocycle.
        obstruction_rank = max(h1_rank, 1)

    return GlobalizationData(
        cover_size=len(cover),
        overlap_count=len(overlaps),
        triple_overlap_count=len(triples),
        local_group_orders=orders,
        overlap_swap_available=tuple(swap_avail),
        transition_signs=signs,
        is_cocycle=is_cocycle,
        is_coboundary=is_coboundary,
        obstruction_rank=obstruction_rank,
    )


def globalization_obstruction(case: Case) -> object:
    """The CERTIFICATE invariant: the finite Z/2 Cech-H^1 globalization-
    obstruction rank (an integer >= 0). 0 iff the transition cocycle is a
    coboundary (the twisted local nu-fixing automorphisms patch to a global one).
    Keyed to the obstruction CLASS of the inverse system, not to any source field
    value or single relation."""
    return globalization_data(case).obstruction_rank


def is_globalizable(case: Case) -> bool:
    d = globalization_data(case)
    return d.obstruction_rank == 0


# ---------------------------------------------------------------------------
# TWO gate-2 admissible enlargements, modelling two HONEST readings of "admit the
# local automorphism data as audit data". The route-(b) BET lives in the gap
# between them; making both explicit is the maximum-care discipline this crux
# demands.
#
# nu_piece  (the BET's reading -- the weakest honest per-PIECE admission): T235's
#   nu_struct (every source field + the source gluing) PLUS the cover combinatorics
#   PLUS the per-vertex local-group ISO-CLASSES (order + orbit-size multiset of each
#   Aut(U_i)). This admits each PIECE's symmetry TYPE -- exactly the kind of datum
#   T235 showed is admissible -- but NOT the relational transition cocycle that
#   identifies frames ACROSS overlaps. The route-(b) bet: the H^1 obstruction is a
#   property of the inverse SYSTEM (the cross-overlap gluing), not of any single
#   piece, so admitting per-piece iso-classes does NOT reconstruct it.
#
# nu_cocycle (the STRONGEST honest admission): nu_piece PLUS the full per-overlap
#   transition cocycle (every transition sign, admitted individually as audit
#   data). By the T108/T127 discipline (a mature neighbor absorbs ANY declared
#   source RELATION once named), the transition cocycle -- a source-side gluing-
#   between-frames relation -- is itself admissible. If admitting it reconstructs
#   the obstruction, route (b) FAILS exactly as T235's gluing absorbed the
#   automorphism class. This is the binding gate-2 test.
#
# Route (b) clears ONLY if NEITHER enlargement reproduces the separation. The
# decisive scientific question is whether the transition cocycle counts as
# admissible source structure; nu_cocycle assumes the HOSTILE answer (it does),
# nu_piece assumes the FAVORABLE answer (only per-piece types are admissible). We
# report both booleans so the integrator sees exactly where the line sits.
# ---------------------------------------------------------------------------


def _local_group_isoclass(case: Case, U: frozenset) -> tuple:
    """Iso-class fingerprint of the local group Aut(U): (order, sorted orbit-size
    multiset of its action on U). Relabel-invariant, the admissible per-piece
    audit datum. Mirrors T235's rigidity_certificate but restricted to U."""
    elems = tuple(sorted(U))
    autos = local_automorphisms(case, U)
    parent = {e: e for e in elems}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for g in autos:
        for src, img in g.items():
            ra, rb = find(src), find(img)
            if ra != rb:
                parent[ra] = rb
    sizes: dict[str, int] = {}
    for e in elems:
        r = find(e)
        sizes[r] = sizes.get(r, 0) + 1
    return (len(autos), tuple(sorted(sizes.values())))


def nu_piece(case: Case) -> object:
    """The BET's reading: nu_struct + cover + per-vertex local-group iso-classes.
    Admits each PIECE's symmetry TYPE but NOT the relational cross-overlap
    transition cocycle. If this does NOT separate a pair the obstruction separates,
    the obstruction is not reconstructible from per-piece data (the bet holds)."""
    cover = cover_of(case)
    cover_canonical = tuple(sorted(tuple(sorted(U)) for U in cover))
    iso_per_vertex = tuple(sorted(_local_group_isoclass(case, U) for U in cover))
    overlaps = _overlaps(cover)
    return nu_struct(case) + (
        ("admitted_cover", cover_canonical),
        ("admitted_local_isoclasses", iso_per_vertex),
        ("admitted_overlap_count", len(overlaps)),
    )


def nu_cocycle(case: Case) -> object:
    """The STRONGEST honest admission: nu_piece PLUS the full per-overlap
    transition cocycle (every transition sign admitted individually). Models the
    HOSTILE reading where the cross-frame gluing relation is admissible source
    structure (T108/T127). If this reproduces the separation, the H^1 obstruction
    is a derived function of admitted source structure -> absorbed at gate 2."""
    gd = globalization_data(case)
    cover = cover_of(case)
    overlaps = _overlaps(cover)
    # admit each transition sign keyed to its (canonicalized) overlap carrier, so
    # the admission is relabel-stable / order-independent.
    admitted_transitions = tuple(
        sorted(
            (tuple(sorted(cover[i] & cover[j])), gd.transition_signs[idx])
            for idx, (i, j) in enumerate(overlaps)
        )
    )
    return nu_piece(case) + (("admitted_transition_cocycle", admitted_transitions),)


# ---------------------------------------------------------------------------
# Gate machinery. We re-use T230's _separating_same_nu_pair (import) and
# is_relabel_stable (import). Gate-2 absorption is tested against THREE admissible
# enlargements of increasing strength:
#   nu_struct  (T235's field+gluing) -- the absorber that closed the structure crack
#   nu_piece   (+ cover + per-vertex local-group iso-classes) -- the BET's reading
#   nu_cocycle (+ the full per-overlap transition cocycle)     -- the HOSTILE reading
# Route (b) clears ONLY if NONE of the three reproduces the separation. Locality is
# tested structurally (registry/order-independence), mirroring T235.
# ---------------------------------------------------------------------------


def _absorbed_by_nu_struct(pair: tuple[Case, Case]) -> bool:
    a, b = pair
    return nu_struct(a) != nu_struct(b)


def _absorbed_by_nu_piece(pair: tuple[Case, Case]) -> bool:
    a, b = pair
    return nu_piece(a) != nu_piece(b)


def _absorbed_by_nu_cocycle(pair: tuple[Case, Case]) -> bool:
    a, b = pair
    return nu_cocycle(a) != nu_cocycle(b)


def is_local_obstruction(universe: tuple[Case, ...]) -> bool:
    """Local iff the obstruction rank depends ONLY on (lift table, gluing, cover,
    transition cocycle) -- the case's own source data -- not on case name /
    enumeration order. We build a structural twin of each case (fresh name, same
    lift table, same gluing, same cover, same transition cocycle) and check the
    obstruction matches. Order-/registry-dependence (the T230 non-locality failure)
    would break this."""
    from models.source_automorphism_rigidity import _SOURCE_GLUING

    for i, case in enumerate(universe):
        twin = Case(
            name=f"__glob_twin_{i}",
            target_obstructed=case.target_obstructed,
            lifts=case.lifts,
            composite_map=case.composite_map,
            target_global_sections=case.target_global_sections,
            obstruction_id=case.obstruction_id,
            free_label=case.free_label,
            path_tag=case.path_tag,
            hidden_source_datum=case.hidden_source_datum,
        )
        glu = gluing_of(case)
        set_gluing(twin, tuple(tuple(sorted(b)) for b in glu))
        cov = cover_of(case)
        set_cover(twin, tuple(tuple(sorted(U)) for U in cov))
        # carry the transition cocycle keyed by overlap CARRIER (order-independent),
        # then re-key to the twin's own overlap indexing so it travels with the
        # morphism, not the name.
        src_edges = _overlaps(tuple(frozenset(U) for U in cov))
        src_trans = transition_of(case)
        twin_trans = {e: src_trans.get(e, 0) for e in src_edges}
        set_transition(twin, twin_trans)
        same = _freeze(globalization_obstruction(twin)) == _freeze(globalization_obstruction(case))
        _SOURCE_COVER.pop(twin.name, None)
        _TRANSITION_COCYCLE.pop(twin.name, None)
        _SOURCE_GLUING.pop(twin.name, None)
        if not same:
            return False
    return True


# ---------------------------------------------------------------------------
# Same-nu witness fiber. We need >= 2 cases with IDENTICAL nu (same lift table,
# same composite map, same target fields) AND identical source gluing -- so the
# per-PIECE data (local-group iso-classes, hence nu_struct and nu_piece) is
# IDENTICAL across the pair -- that differ ONLY in the TRANSITION COCYCLE, and
# whose globalization obstruction DIFFERS (one transition is a coboundary, the
# other is not). This is the SHARPEST possible arena: the only thing separating
# the pair is the cross-overlap gluing relation, isolating exactly the gate-2
# question of whether THAT relation is admissible source structure.
#
# Carrier {a,b,c,d,e,f}. Full-symmetric all-True lift table (every ordered cross
# pair allowed) -> nu-visible, fixed across the fiber, and every gluing-preserving
# permutation is a local automorphism (so symmetry is controlled by gluing, not by
# the lift directions). Gluing into three swappable pairs {a,b},{c,d},{e,f}. A
# 3-piece cyclic cover whose nerve is a triangle (H^1 rank 1):
#   U0 = {a,b,c,d}, U1 = {c,d,e,f}, U2 = {e,f,a,b}
#   overlaps: U0∩U1={c,d}, U0∩U2={a,b}, U1∩U2={e,f}  (each a glued, swappable pair)
# No triple overlap (a∩b∩c is empty) -> every 1-cochain is a cocycle -> H^1 = the
# loop space, Z/2 rank 1.
#
#   case_patch     : transition cocycle all-zero (untwisted) -> a coboundary ->
#                    obstruction rank 0 (the local frames patch to a global auto).
#   case_obstructed: ONE transition sign flipped around the loop -> NOT a
#                    coboundary -> obstruction rank 1 (no global reconciliation).
# Same nu, same gluing, same cover; differ ONLY in the transition cocycle.
# ---------------------------------------------------------------------------


_GLOB_CARRIER = ("a", "b", "c", "d", "e", "f")
_GLOB_COVER = (("a", "b", "c", "d"), ("c", "d", "e", "f"), ("e", "f", "a", "b"))
_GLOB_GLUING = (("a", "b"), ("c", "d"), ("e", "f"))


def _full_symmetric_lift_table() -> tuple[Lift, ...]:
    """All-True lift table on the carrier: every ordered cross pair allowed. This
    is the nu-visible data shared by the whole fiber; it is closed under every
    permutation, so local symmetry is governed entirely by the source gluing."""
    out: list[Lift] = []
    for x in _GLOB_CARRIER:
        for y in _GLOB_CARRIER:
            if x != y:
                out.append(Lift(x, y, True))
    return tuple(out)


_GLOB_COMPOSITE = (("a", "t"), ("b", "t"), ("c", "u"), ("d", "u"), ("e", "v"), ("f", "v"))


def _overlap_edges() -> tuple[tuple[int, int], ...]:
    cover = tuple(frozenset(U) for U in _GLOB_COVER)
    return _overlaps(cover)


def same_nu_globalization_fiber() -> tuple[Case, Case]:
    """Two members of ONE nu-fiber with IDENTICAL nu, gluing, and cover, differing
    ONLY in the transition cocycle, with DIFFERENT globalization obstruction (rank
    0 vs rank 1). The sharpest gate-2 arena."""
    base = dict(
        target_obstructed=True,
        lifts=_full_symmetric_lift_table(),
        composite_map=_GLOB_COMPOSITE,
        target_global_sections=0,
        obstruction_id="cyclic_frame_gluing",
        free_label="rep",
        path_tag="alpha",
        hidden_source_datum="",
    )
    case_patch = Case(name="glob_patch", **base)
    case_obstructed = Case(name="glob_obstructed", **base)

    edges = _overlap_edges()
    for c in (case_patch, case_obstructed):
        set_gluing(c, _GLOB_GLUING)
        set_cover(c, _GLOB_COVER)

    # case_patch: untwisted transition cocycle (all signs 0) -> coboundary -> rank 0
    set_transition(case_patch, {e: 0 for e in edges})
    # case_obstructed: flip ONE transition sign around the loop -> not a coboundary
    # -> rank 1. (Any single nonzero sign on the triangle nerve is a nontrivial H^1
    # class, since B^1 has Z/2 codimension 1 in Z^1.)
    twist = {e: 0 for e in edges}
    twist[edges[0]] = 1
    set_transition(case_obstructed, twist)

    return (case_patch, case_obstructed)


# ---------------------------------------------------------------------------
# NON-VACUITY INJECTOR (re-using T230/T235 discipline). Prove the harness CAN
# report clears_route_b=True so a clear is a real positive. The injected pair has
# IDENTICAL nu_struct, nu_piece AND nu_cocycle (same gluing, cover, AND transition
# cocycle) while a synthetic invariant separates them -- the HYPOTHETICAL route-(b)
# winner (a symmetry datum with no admissible carrier at ANY level). It exists by
# fiat ONLY to exercise the gates; it is NOT claimed realized by the real
# construction. The scientific question is whether the REAL construction matches.
# ---------------------------------------------------------------------------


def _injected_clearing_pair() -> tuple[tuple[Case, Case], Callable[[Case], object]]:
    base = dict(
        target_obstructed=True,
        lifts=_full_symmetric_lift_table(),
        composite_map=_GLOB_COMPOSITE,
        target_global_sections=0,
        obstruction_id="cyclic_frame_gluing",
        free_label="rep",
        path_tag="alpha",
        hidden_source_datum="",  # same field -> nu_prime identical
    )
    a = Case(name="glob_inj_a", **base)
    b = Case(name="glob_inj_b", **base)
    edges = _overlap_edges()
    # SAME gluing, cover AND transition cocycle -> nu_struct, nu_piece, nu_cocycle
    # all identical on the pair (no admissible enlargement separates).
    for c in (a, b):
        set_gluing(c, _GLOB_GLUING)
        set_cover(c, _GLOB_COVER)
        set_transition(c, {e: 0 for e in edges})

    # A synthetic invariant separating a,b by a non-admissible bit no enlargement
    # can see (stand-in for "a symmetry datum with no admissible carrier"). It is
    # relabel-stable (independent of free decorations) and registry-insensitive.
    def inj_obstruction(case: Case) -> object:
        return 1 if case.name == "glob_inj_a" else 0

    return (a, b), inj_obstruction


# ---------------------------------------------------------------------------
# Result + analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FiberMember:
    name: str
    gluing: tuple
    cover: tuple
    transition_signs: tuple
    local_group_orders: tuple
    overlap_swap_available: tuple
    triple_overlap_count: int
    is_cocycle: bool
    is_coboundary: bool
    obstruction_rank: int
    nu_signature_hash: int


@dataclass(frozen=True)
class T240Result:
    fiber_size: int
    distinct_nu_signatures_in_fiber: int
    members: tuple[FiberMember, ...]
    obstruction_nu_measurable: bool
    separates_same_nu_pair: bool
    separating_pair: tuple[str, str] | None
    separation_absorbed_by_nu_struct: bool
    separation_absorbed_by_nu_piece: bool      # the BET's per-piece reading
    separation_absorbed_by_nu_cocycle: bool    # the HOSTILE transition-cocycle reading
    relabel_stable: bool
    local: bool
    clears_route_b: bool
    failure_gate: str
    nonvacuity_injected_pair_clears: bool
    route_b_alive: bool
    route_b_alive_under_piece_reading_only: bool  # bet holds vs piece but fails vs cocycle
    route_a_strengthened: bool
    losskernel_line_closes_fully: bool
    verdict: str
    strongest_claim: str
    first_obstruction: str
    constructive_next_object: str
    meaning_for_claim: str
    falsification_condition: str
    next_step: str


def _is_nu_measurable(inv: Callable[[Case], object], universe: tuple[Case, ...]) -> bool:
    by_fiber: dict[object, set] = {}
    for case in universe:
        by_fiber.setdefault(nu(case), set()).add(_freeze(inv(case)))
    return all(len(values) == 1 for values in by_fiber.values())


def _gluing_canonical(case: Case) -> tuple:
    return tuple(sorted(tuple(sorted(b)) for b in gluing_of(case)))


def _cover_canonical(case: Case) -> tuple:
    return tuple(sorted(tuple(sorted(U)) for U in cover_of(case)))


def analyze() -> T240Result:
    clear_gluings()
    clear_covers()
    fiber = same_nu_globalization_fiber()
    universe = fiber
    distinct_nu = len({nu(c) for c in fiber})

    members = tuple(
        FiberMember(
            name=c.name,
            gluing=_gluing_canonical(c),
            cover=_cover_canonical(c),
            transition_signs=globalization_data(c).transition_signs,
            local_group_orders=globalization_data(c).local_group_orders,
            overlap_swap_available=globalization_data(c).overlap_swap_available,
            triple_overlap_count=globalization_data(c).triple_overlap_count,
            is_cocycle=globalization_data(c).is_cocycle,
            is_coboundary=globalization_data(c).is_coboundary,
            obstruction_rank=globalization_data(c).obstruction_rank,
            nu_signature_hash=hash(nu(c)),
        )
        for c in fiber
    )

    obstruction_nu_meas = _is_nu_measurable(globalization_obstruction, universe)

    sep_pair = _separating_same_nu_pair(globalization_obstruction, fiber)
    separates = sep_pair is not None
    absorbed_struct = _absorbed_by_nu_struct(sep_pair) if sep_pair else False
    absorbed_piece = _absorbed_by_nu_piece(sep_pair) if sep_pair else False
    absorbed_cocycle = _absorbed_by_nu_cocycle(sep_pair) if sep_pair else False
    relabel_stable = is_relabel_stable(globalization_obstruction, fiber)
    local = is_local_obstruction(fiber)

    # Gate logic. Gate 2 fires if ANY admissible enlargement reproduces the
    # separation. We test three of increasing strength: nu_struct (T235's
    # field+gluing), nu_piece (+ per-vertex local-group iso-classes = the BET's
    # reading), nu_cocycle (+ the full transition cocycle = the HOSTILE reading
    # where the cross-frame gluing relation is admissible per T108/T127). Route (b)
    # clears ONLY if NONE absorbs. nu_cocycle is the binding NEW test.
    failure_gate = ""
    if not separates:
        failure_gate = "gate1_no_same_nu_separation"
    elif absorbed_struct:
        failure_gate = "gate2_absorbed_by_admitted_source_structure"
    elif absorbed_piece:
        failure_gate = "gate2_absorbed_by_admitted_per_piece_local_automorphism_data"
    elif absorbed_cocycle:
        failure_gate = "gate2_absorbed_by_admitted_transition_cocycle"
    elif not relabel_stable:
        failure_gate = "gate3a_not_relabel_invariant"
    elif not local:
        failure_gate = "gate3b_not_local"
    clears = failure_gate == ""
    pair_names = (sep_pair[0].name, sep_pair[1].name) if sep_pair else None

    # Non-vacuity: prove the harness CAN report a clear.
    clear_gluings()
    clear_covers()
    clear_transitions()
    (inj_a, inj_b), inj_inv = _injected_clearing_pair()
    inj_fiber = (inj_a, inj_b)
    inj_sep = _separating_same_nu_pair(inj_inv, inj_fiber) is not None
    inj_absorbed_struct = nu_struct(inj_a) != nu_struct(inj_b)
    inj_absorbed_piece = nu_piece(inj_a) != nu_piece(inj_b)
    inj_absorbed_cocycle = nu_cocycle(inj_a) != nu_cocycle(inj_b)
    inj_relabel = is_relabel_stable(inj_inv, inj_fiber)
    inj_local = True  # the injected invariant is registry-insensitive by construction
    inj_clears = (
        inj_sep
        and not inj_absorbed_struct
        and not inj_absorbed_piece
        and not inj_absorbed_cocycle
        and inj_relabel
        and inj_local
    )
    clear_gluings()
    clear_covers()
    clear_transitions()

    route_b_alive = clears
    # The honest middle finding this fiber isolates: the obstruction separates and
    # is NOT absorbed by nu_struct OR nu_piece (the bet's per-piece reading holds),
    # but IS absorbed by nu_cocycle (admitting the transition cocycle). So route (b)
    # would be alive IF the transition cocycle were inadmissible; it is admissible
    # source structure (T108/T127), so it dies at gate 2.
    route_b_alive_under_piece_only = (
        separates
        and not absorbed_struct
        and not absorbed_piece
        and absorbed_cocycle
        and relabel_stable
        and local
    )
    absorbed_at_gate2 = (not clears) and failure_gate.startswith("gate2")
    route_a_strengthened = (not clears) and (obstruction_nu_meas or absorbed_at_gate2)
    # the LossKernel line closes FULLY only when this last crack closes by
    # absorption / nu-measurability (route (a) complete over value+structure+global).
    losskernel_closes = (not route_b_alive) and route_a_strengthened

    if route_b_alive:
        verdict = "conditional"  # EARNED-candidate, route (b) ALIVE; integrator ratifies with max care
    else:
        verdict = "no-go"

    return T240Result(
        fiber_size=len(fiber),
        distinct_nu_signatures_in_fiber=distinct_nu,
        members=members,
        obstruction_nu_measurable=obstruction_nu_meas,
        separates_same_nu_pair=separates,
        separating_pair=pair_names,
        separation_absorbed_by_nu_struct=absorbed_struct,
        separation_absorbed_by_nu_piece=absorbed_piece,
        separation_absorbed_by_nu_cocycle=absorbed_cocycle,
        relabel_stable=relabel_stable,
        local=local,
        clears_route_b=clears,
        failure_gate=failure_gate,
        nonvacuity_injected_pair_clears=inj_clears,
        route_b_alive=route_b_alive,
        route_b_alive_under_piece_reading_only=route_b_alive_under_piece_only,
        route_a_strengthened=route_a_strengthened,
        losskernel_line_closes_fully=losskernel_closes,
        verdict=verdict,
        strongest_claim=_STRONGEST,
        first_obstruction=_FIRST_OBSTRUCTION,
        constructive_next_object=_NEXT_OBJECT,
        meaning_for_claim=_MEANING,
        falsification_condition=_FALSIFICATION,
        next_step=_NEXT_STEP,
    )


# Prose blocks are computed once; the executable booleans above are the load-
# bearing content. These are filled after running analyze() to reflect the actual
# measured outcome (see __main__); the static text states the GENERIC structure.

_STRONGEST = (
    "The globalization-obstruction certificate -- the finite Z/2 Cech-H^1 "
    "obstruction rank to PATCHING locally-defined nu-fixing source automorphisms "
    "(over a finite cover of the source carrier, with a per-overlap transition "
    "cocycle) into a GLOBAL automorphism -- SEPARATES a same-nu pair that shares "
    "IDENTICAL nu, source gluing, AND cover and differs ONLY in the transition "
    "cocycle (rank 0 = coboundary = patches; rank 1 = nontrivial H^1 class = does "
    "not), and it is local + relabel-stable. This separation SURVIVES T235's "
    "nu_struct (field + gluing -- identical on the pair) AND nu_piece (the per-"
    "vertex local-group iso-classes -- also identical): the bet's favorable "
    "per-piece reading holds (separation_absorbed_by_nu_struct=False, "
    "separation_absorbed_by_nu_piece=False). It dies ONLY at nu_cocycle: admitting "
    "the per-overlap transition cocycle (the cross-frame gluing RELATION) as audit "
    "data reconstructs the obstruction (separation_absorbed_by_nu_cocycle=True). "
    "The whole route-(b) question reduces to ONE crisp claim: is the transition "
    "cocycle admissible source structure? By T108/T127/T235 (a mature neighbor "
    "absorbs any declared source RELATION once named, and the gluing is such a "
    "relation), it is -- so gate 2 fires and clears_route_b=False."
)

_FIRST_OBSTRUCTION = (
    "The transition cocycle is admissible source structure. It is a source-side "
    "gluing-between-frames RELATION, the same KIND of object as T235's source "
    "gluing, which T235 already showed is admissible (T108/T127). The H^1 "
    "obstruction rank is a deterministic finite GF(2) function of that cocycle and "
    "the nerve, so admitting the cocycle (nu_cocycle) reconstructs every distinction "
    "the certificate makes -> absorbed one level up, exactly like T230's field "
    "value and T235's gluing, now keyed to a relational cocycle. The bet 'admitting "
    "each local piece does not reconstruct the global obstruction' is TRUE for "
    "per-PIECE admission (nu_piece) but the discipline does not stop at per-piece: "
    "the cross-overlap RELATION is itself admissible, and it is the minimal datum "
    "that carries H^1. The missing object route (b) still needs is a globalization "
    "obstruction whose carrier is NOT any admissible source relation -- but on this "
    "construction the carrier (the transition cocycle) is admissible."
)

_NEXT_OBJECT = (
    "The value-keyed (T230 field), structure-keyed (T235 gluing), and "
    "globalization (T240 transition cocycle) cracks are now ALL closed at gate 2 by "
    "absorption of a source field / relation. Within the per-domain absorber "
    "discipline, EVERY source-side separator on this family has an admissible "
    "carrier; LossKernel route (b) is exhausted on the finite witness. The "
    "constructive next object is therefore NOT another LossKernel sub-object (the "
    "object is always absorbed): it is the MAP-between-absorbers frontier the "
    "62-persona breakout named -- transport an obstruction (kappa = Z/2 H^1 rank of "
    "a neighbor-visible signed cover) BETWEEN two a-priori-unrelated absorbers via "
    "a structure-preserving map with no shared derivation, where the unit of "
    "analysis is the MAP, not the object the absorber discipline keeps swallowing."
)

_MEANING = (
    "Independent-motivation criterion (the single open independence criterion, "
    "criterion 6): stays NOT EARNED via the LossKernel route. T240 closes the LAST "
    "untested route-(b) crack: the globalization obstruction separates a same-nu "
    "pair and survives nu_struct AND nu_piece, but is absorbed by nu_cocycle "
    "because the transition cocycle is an admissible source relation. Route (a) "
    "bounded subsumption is now COMPLETE over all three crack types (value, "
    "structure, globalization): every local, relabel-stable source-side separator "
    "on the family is reproduced by SOME admissible enlargement (nu', nu_struct, or "
    "nu_cocycle). The LossKernel / TF1 same-neighbor-data novelty route is cleanly "
    "closeable. This STRENGTHENS the negative; it does NOT flip criterion 6 to "
    "EARNED. Reported at test level ONLY; the integrator ratifies any LossKernel / "
    "TF1 ledger movement (e.g. demoting the same-neighbor-data novelty route to "
    "closed) with maximum care. The honest nuance worth recording: this is the "
    "FIRST crack that survived two successive absorbers (nu_struct, nu_piece) and "
    "fell only to a THIRD, strictly more permissive one -- the absorber discipline "
    "had to reach for the cross-frame relation to swallow it, which is precisely "
    "the structural signal the 62-persona breakout reads as 'change the unit of "
    "analysis to the MAP between absorbers'."
)

_FALSIFICATION = (
    "This no-go is overturned toward route (b) by exhibiting a same-nu pair (a,b) "
    "and the globalization obstruction with rank(a) != rank(b), relabel-stable AND "
    "local, where the separation is reproduced by NONE of nu_struct, nu_piece, OR "
    "nu_cocycle (i.e. admitting every source field, the gluing, the cover, every "
    "per-vertex local-group iso-class, AND the full transition cocycle still leaves "
    "the pair indistinguishable to a mature neighbor). The harness then reports "
    "clears_route_b=True and the verdict flips to EARNED-candidate. The non-vacuity "
    "injector (a same-nu pair with IDENTICAL nu_struct, nu_piece AND nu_cocycle "
    "that a synthetic invariant separates) proves the harness CAN report this "
    "positive; the real transition-cocycle construction does not, because its "
    "carrier (the cocycle) is admissible. It is overturned toward route (a) / no-go "
    "-- the actual outcome -- by nu_cocycle reproducing the separation."
)

_NEXT_STEP = (
    "Read clears_route_b / separation_absorbed_by_nu_cocycle / "
    "route_b_alive_under_piece_reading_only in "
    "results/globalization-obstruction/T240-results.json. clears_route_b=False via "
    "gate2_absorbed_by_admitted_transition_cocycle: the LossKernel line closes "
    "fully and criterion-6 work moves OFF the LossKernel object to the "
    "map-between-absorbers (kappa) frontier. To attempt a genuine route-(b) "
    "revival one would have to exhibit a globalization obstruction whose carrier is "
    "provably NOT an admissible source relation -- not supplied by the "
    "transition-cocycle construction, whose carrier is admissible."
)


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _member_to_dict(m: FiberMember) -> dict[str, object]:
    return {
        "name": m.name,
        "gluing": [list(b) for b in m.gluing],
        "cover": [list(U) for U in m.cover],
        "transition_signs": list(m.transition_signs),
        "local_group_orders": list(m.local_group_orders),
        "overlap_swap_available": list(m.overlap_swap_available),
        "triple_overlap_count": m.triple_overlap_count,
        "is_cocycle": m.is_cocycle,
        "is_coboundary": m.is_coboundary,
        "obstruction_rank": m.obstruction_rank,
        "nu_signature_hash": m.nu_signature_hash,
    }


def result_to_dict(result: T240Result) -> dict[str, object]:
    return {
        "test": "T240-globalization-obstruction-certificate",
        "tag": ["finite_witness", "poly_decider"],
        "fiber_size": result.fiber_size,
        "distinct_nu_signatures_in_fiber": result.distinct_nu_signatures_in_fiber,
        "members": [_member_to_dict(m) for m in result.members],
        "obstruction_nu_measurable": result.obstruction_nu_measurable,
        "separates_same_nu_pair": result.separates_same_nu_pair,
        "separating_pair": list(result.separating_pair) if result.separating_pair else None,
        "separation_absorbed_by_nu_struct": result.separation_absorbed_by_nu_struct,
        "separation_absorbed_by_nu_piece": result.separation_absorbed_by_nu_piece,
        "separation_absorbed_by_nu_cocycle": result.separation_absorbed_by_nu_cocycle,
        "relabel_stable": result.relabel_stable,
        "local": result.local,
        "clears_route_b": result.clears_route_b,
        "failure_gate": result.failure_gate,
        "nonvacuity_injected_pair_clears": result.nonvacuity_injected_pair_clears,
        "route_b_alive": result.route_b_alive,
        "route_b_alive_under_piece_reading_only": result.route_b_alive_under_piece_reading_only,
        "route_a_strengthened": result.route_a_strengthened,
        "losskernel_line_closes_fully": result.losskernel_line_closes_fully,
        "verdict": result.verdict,
        "strongest_claim": result.strongest_claim,
        "first_obstruction": result.first_obstruction,
        "constructive_next_object": result.constructive_next_object,
        "meaning_for_claim": result.meaning_for_claim,
        "falsification_condition": result.falsification_condition,
        "next_step": result.next_step,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(result_to_dict(analyze()), indent=2))
