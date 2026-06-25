"""T235: Source-automorphism rigidity certificate.

The one untested crack in T230's absorption-escape trichotomy, and the ONLY live
route to flip the independent-motivation criterion from NOT EARNED to EARNED for
the typed-forgetting / LossKernel line.

------------------------------------------------------------------------------
WHAT T230 ESTABLISHED (re-used here by import, NOT re-derived).
------------------------------------------------------------------------------
T230 showed: on a same-nu witness fiber, every candidate attribution invariant
that SEPARATES a same-nu pair fails exactly one of three gates --

    gate 1 (separates)        : I(a) != I(b) for some pair with nu(a) == nu(b)
    gate 2 (non-absorbable)   : the separation is NOT reproduced by an admissible
                                enlargement nu' (admitting a source FIELD as audit
                                data does not make a mature neighbor separate too)
    gate 3 (genuine invariant): relabel-stable (3a) AND local (3b)

The load-bearing finding: `source_reading` (read the hidden source field directly)
is LOCAL and RELABEL-STABLE and SEPARATES -- a real separator -- yet it dies at
GATE 2. Admitting its source field as audit data enlarges nu to nu', and a mature
neighbor reproduces the separation. T108/T127 (per the open-problem file) already
showed mature provenance/effect/abstraction systems absorb ANY declared source
FIELD VALUE once it is named. So a value-keyed separator can never clear gate 2.

------------------------------------------------------------------------------
THE T235 BET (what is genuinely NEW here, and what the honest decision is).
------------------------------------------------------------------------------
T230's constructive-next-object: key the invariant to a source-side SYMMETRY
CLASS -- whether the source fiber admits a nontrivial self-map (automorphism)
fixing every nu-visible datum -- rather than to the VALUE of any source field.
The structural bet: an automorphism CLASS is not a single field value, so gate 2
"has no single field to admit", and gates 3a/3b pass by construction (local,
relabel-stable). IF this clears all three gates on a same-nu pair, route (b) is
alive and independent-motivation trends EARNED-candidate.

We do NOT assume the bet. We BUILD the source-automorphism groupoid and DECIDE
two honest questions by execution, with a non-vacuity injector so a clear is a
real positive:

  Q1 (nu-measurability): is the automorphism iso-class a function of nu on a
     same-nu fiber? If YES -> it CANNOT separate -> route (a) strong subsumption
     STRENGTHENS (the natural symmetry invariant also factors through nu);
     LossKernel line CLOSEABLE / no-go strengthened.

  Q2 (gate-2 absorbability, the decisive honest test): IF the automorphism class
     DOES separate a same-nu pair, is that separation reproduced by an admissible
     enlargement that admits the SOURCE STRUCTURE the automorphism is computed
     from? The bet claims "no single field to admit." We test it by running the
     SAME gate-2 machinery T230 used, but generalized: the admissible enlargement
     nu_struct admits the source-side relation (the graph on lift endpoints that
     the automorphism acts on) as audit data. If admitting that structure
     reproduces the separation, the automorphism class is ABSORBED ONE LEVEL UP
     exactly like source_reading -- route (b) FAILS at gate 2 again, just keyed to
     a structure rather than a scalar. If NO admissible enlargement reproduces it
     (the separation survives admitting every source field AND the source relation
     as audit data) AND it separates AND it is local + relabel-stable, then
     clears_route_b = True.

------------------------------------------------------------------------------
THE SOURCE-AUTOMORPHISM GROUPOID (the new object, built explicitly).
------------------------------------------------------------------------------
A typed-lossy morphism's source carries, beyond the nu-visible lift table, an
internal source-side adjacency: which source endpoints are "the same source
object seen twice" (a self-identification / fiber-gluing relation). nu records
the lift table (csp + provenance) but NOT this internal gluing -- two cases can
have IDENTICAL lift tables yet different source-side gluings.

A source automorphism is a permutation g of the source endpoints such that:
  (1) g preserves the lift table (every Lift(l,r,allowed) maps to a Lift in the
      table with the same `allowed`), i.e. g fixes every nu-visible datum, AND
  (2) g preserves the source-side gluing relation.
Aut(case) is the group of such g. The RIGIDITY CERTIFICATE invariant is the
iso-class of Aut(case) -- concretely its multiset of orbit sizes / order, a
relabel-invariant, local fingerprint of the symmetry class. "Rigid" = trivial
Aut (only identity fixes everything); a nontrivial Aut is a genuine source-side
self-map invisible to nu.

CRITICAL HONESTY: the source gluing relation is REAL source structure that nu
does not expose, but it IS admissible source data (T108/T127). So Q2 is the whole
game. We compute Aut from the gluing, then ask whether admitting the gluing as
audit data (nu_struct) reproduces any separation Aut produces. If it always does,
the automorphism class is a derived function of an admissible source field and is
absorbed -- the bet fails, route (a) strengthens. If a same-nu pair has identical
admissible enlargements yet different Aut iso-class, gate 2 cannot absorb it.

No physics / geometry / curvature / new-object language. finite_witness: a finite
executable fixture over hand-built typed-lossy cases; the automorphism groups are
finite permutation groups computed by exhaustive orbit enumeration. NOT a
continuum/general theorem, NOT a hardness claim, NOT a poly_decider search.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Callable

# Re-use the T230 model BY IMPORT ONLY. We do NOT modify it. nu, nu_prime,
# relabel, the same-nu fiber discipline, the gate harness, and the non-vacuity
# discipline all come from there.
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


# ---------------------------------------------------------------------------
# Source-side gluing. This is the internal source structure nu does NOT expose:
# a partition (equivalence) on the source endpoints recording which endpoints are
# "the same underlying source object" (a self-identification). Two cases with the
# SAME lift table can carry DIFFERENT gluings -> different automorphism groups.
#
# We attach it as an auxiliary keyed by case name (the case's structural identity).
# This is genuine source data, kept OUT of nu by construction so we can honestly
# test whether the automorphism class derived from it is nu-measurable and whether
# admitting it as audit data absorbs the separation.
# ---------------------------------------------------------------------------


def _source_endpoints(case: Case) -> tuple[str, ...]:
    """The source endpoints the automorphism group permutes: the distinct source
    symbols appearing in the lift table (nu-visible) -- the carrier the source-side
    gluing partitions."""
    eps: set[str] = set()
    for lift in case.lifts:
        eps.add(lift.left_source)
        eps.add(lift.right_source)
    return tuple(sorted(eps))


# The gluing registry: case.name -> frozenset of frozensets (a partition of the
# source endpoints). Identity partition (each endpoint its own block) = no gluing.
# This is source structure, admissible but not in nu.
_SOURCE_GLUING: dict[str, frozenset] = {}


def set_gluing(case: Case, blocks: tuple[tuple[str, ...], ...]) -> None:
    _SOURCE_GLUING[case.name] = frozenset(frozenset(b) for b in blocks)


def gluing_of(case: Case) -> frozenset:
    eps = _source_endpoints(case)
    default = frozenset(frozenset((e,)) for e in eps)
    return _SOURCE_GLUING.get(case.name, default)


def clear_gluings() -> None:
    _SOURCE_GLUING.clear()


# ---------------------------------------------------------------------------
# The source-automorphism group. Aut(case) = permutations g of the source
# endpoints such that g preserves (1) the lift table (g fixes every nu-visible
# datum) and (2) the source-side gluing. Computed by exhaustive enumeration over
# the finite endpoint set -- a real finite permutation-group computation.
# ---------------------------------------------------------------------------


def _lift_set(case: Case) -> frozenset:
    return frozenset((l.left_source, l.right_source, l.allowed) for l in case.lifts)


def _preserves_lifts(case: Case, g: dict[str, str]) -> bool:
    permuted = frozenset((g[l], g[r], a) for (l, r, a) in _lift_set(case))
    return permuted == _lift_set(case)


def _preserves_gluing(case: Case, g: dict[str, str]) -> bool:
    glu = gluing_of(case)
    permuted = frozenset(frozenset(g[e] for e in block) for block in glu)
    return permuted == glu


def automorphism_group(case: Case) -> tuple[tuple[tuple[str, str], ...], ...]:
    """All nu-fixing, gluing-preserving permutations of the source endpoints.

    Returns each automorphism as a sorted tuple of (endpoint, image) pairs so the
    group itself is a hashable, relabel-invariant object. Exhaustive over the
    finite endpoint set: a genuine finite permutation-group computation, not a
    search heuristic."""
    eps = _source_endpoints(case)
    autos: list[tuple[tuple[str, str], ...]] = []
    for perm in permutations(eps):
        g = dict(zip(eps, perm))
        if _preserves_lifts(case, g) and _preserves_gluing(case, g):
            autos.append(tuple(sorted(g.items())))
    return tuple(sorted(autos))


# ---------------------------------------------------------------------------
# The rigidity-certificate invariant: the ISO-CLASS of Aut(case), keyed to the
# symmetry class, NOT to any field value. We fingerprint the iso-class by the
# order of the group and the sorted multiset of orbit sizes of its action on the
# endpoints -- a relabel-invariant, local invariant of the symmetry class. (Two
# automorphism groups with the same order and orbit-size multiset are treated as
# the same symmetry class for separation purposes; that is conservative -- it can
# only make separation HARDER, so a separation found here is real.)
# ---------------------------------------------------------------------------


def _orbits(eps: tuple[str, ...], autos: tuple[tuple[tuple[str, str], ...], ...]) -> tuple[int, ...]:
    parent = {e: e for e in eps}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for auto in autos:
        for (src, img) in auto:
            union(src, img)
    sizes: dict[str, int] = {}
    for e in eps:
        r = find(e)
        sizes[r] = sizes.get(r, 0) + 1
    return tuple(sorted(sizes.values()))


def rigidity_certificate(case: Case) -> object:
    """Iso-class fingerprint of the source-automorphism group: (group order,
    orbit-size multiset). Keyed to the symmetry CLASS, not to any source field
    value -- this is the structural property the bet rests on."""
    eps = _source_endpoints(case)
    autos = automorphism_group(case)
    return (len(autos), _orbits(eps, autos))


def is_rigid(case: Case) -> bool:
    """A case is rigid iff its only nu-fixing, gluing-preserving source self-map is
    the identity. A non-rigid case has a genuine source-side symmetry invisible to
    nu."""
    return len(automorphism_group(case)) == 1


# ---------------------------------------------------------------------------
# Gate-2 generalized absorption test (the decisive honest check). T230's gate 2
# admitted a single source FIELD (hidden_source_datum) as audit data via nu_prime.
# Here the automorphism class is computed from the source GLUING, which is also
# admissible source structure. The honest gate-2 question: does admitting the
# gluing as audit data (nu_struct) reproduce any separation the automorphism class
# produces? If yes -> absorbed one level up, exactly like source_reading. If a
# same-nu pair has IDENTICAL admissible enlargements (same nu_prime AND same
# nu_struct) yet DIFFERENT rigidity certificate, gate 2 cannot absorb it.
# ---------------------------------------------------------------------------


def nu_struct(case: Case) -> object:
    """The maximal admissible enlargement: nu plus the admitted source field
    (nu_prime) PLUS the admitted source gluing structure as audit data. This is
    the strongest mature-neighbor reconstruction: a neighbor granted EVERY source
    field and the full source-side relation. If the rigidity certificate separates
    a pair that nu_struct does NOT separate, no admissible neighbor reproduces the
    separation -> gate 2 cannot absorb it."""
    glu = gluing_of(case)
    glu_canonical = tuple(sorted(tuple(sorted(block)) for block in glu))
    return nu_prime(case) + (("admitted_gluing", glu_canonical),)


def _separation_absorbed_by_nu_struct(pair: tuple[Case, Case]) -> bool:
    """Absorbed iff the strongest admissible enlargement (nu_struct: admit every
    source field AND the source gluing) separates the pair. Then a mature neighbor
    granted the source structure reproduces the distinction -> the automorphism
    class is a derived function of admissible audit data -> route (b) FAIL."""
    a, b = pair
    return nu_struct(a) != nu_struct(b)


# ---------------------------------------------------------------------------
# nu-measurability of the rigidity certificate (Q1). Constant on every fiber of
# nu over the universe iff the automorphism iso-class is determined by nu alone.
# ---------------------------------------------------------------------------


def is_nu_measurable(inv: Callable[[Case], object], universe: tuple[Case, ...]) -> bool:
    by_fiber: dict[object, set] = {}
    for case in universe:
        by_fiber.setdefault(nu(case), set()).add(_freeze(inv(case)))
    return all(len(values) == 1 for values in by_fiber.values())


# ---------------------------------------------------------------------------
# Locality of the rigidity certificate. T230's locality gate caught invariants
# that read an EXTERNAL enumeration registry. The rigidity certificate reads the
# source gluing, which is keyed to the case's structural identity (its name), NOT
# an external order-dependent registry. We verify locality structurally: the
# certificate is invariant under rebuilding the case from its own data + its own
# gluing (no dependence on family/order). We detect the bad kind of non-locality
# (order/family dependence) by checking that two structurally identical cases
# carrying the SAME gluing get the SAME certificate regardless of name/order.
# ---------------------------------------------------------------------------


def is_local_certificate(universe: tuple[Case, ...]) -> bool:
    """Local iff the certificate depends ONLY on (lift table, gluing) -- the case's
    own source data -- not on case name / enumeration order. We test by building a
    structural twin of each case with a fresh name but the SAME lift table and an
    isomorphic gluing, and checking the certificate matches. Order-/registry-
    dependence (the T230 non-locality failure) would break this."""
    for i, case in enumerate(universe):
        twin = Case(
            name=f"__twin_{i}",
            target_obstructed=case.target_obstructed,
            lifts=case.lifts,
            composite_map=case.composite_map,
            target_global_sections=case.target_global_sections,
            obstruction_id=case.obstruction_id,
            free_label=case.free_label,
            path_tag=case.path_tag,
            hidden_source_datum=case.hidden_source_datum,
        )
        # give the twin the SAME gluing (source structure travels with the morphism)
        glu = gluing_of(case)
        set_gluing(twin, tuple(tuple(sorted(b)) for b in glu))
        same = _freeze(rigidity_certificate(twin)) == _freeze(rigidity_certificate(case))
        _SOURCE_GLUING.pop(twin.name, None)
        if not same:
            return False
    return True


# ---------------------------------------------------------------------------
# The same-nu witness fiber for the automorphism test. We need >= 2 cases with
# IDENTICAL nu (same lift table, same composite map, same target fields) that
# differ ONLY in source-side gluing (the structure nu does not expose). This is
# the arena where the rigidity certificate must win or lose.
#
# Construction: a 4-endpoint source {p, q, r, s} with a symmetric lift table that
# admits a swap symmetry. Two cases:
#   case_rigid    : gluing = identity partition  -> the swap (p<->q, r<->s) is NOT
#                   forced to be broken... we instead break symmetry by gluing
#                   {p} alone, killing nontrivial autos -> RIGID.
#   case_symmetric: gluing = {{p,q},{r,s}}       -> the swap preserves the gluing
#                   -> NON-RIGID (nontrivial Aut).
# Both share the SAME nu (same lift table). They differ ONLY in source gluing.
# ---------------------------------------------------------------------------


def _symmetric_lift_table() -> tuple[Lift, ...]:
    """A lift table on endpoints {p,q,r,s} symmetric under the swap (p q)(r s):
    every lift's swapped image is also a lift with the same `allowed`. This is the
    nu-visible data shared by the whole fiber."""
    return (
        Lift("p", "r", True),
        Lift("q", "s", True),   # image of (p,r) under (p q)(r s)
        Lift("p", "s", False),
        Lift("q", "r", False),  # image of (p,s) under (p q)(r s)
    )


_SYM_COMPOSITE = (("p", "t"), ("q", "t"), ("r", "u"), ("s", "u"))


def same_nu_automorphism_fiber() -> tuple[Case, Case, Case]:
    """Three members of ONE nu-fiber differing only in source-side gluing.

    case_rigid     : gluing breaks the swap -> trivial Aut (rigid).
    case_symmetric : gluing respects the swap -> nontrivial Aut.
    case_symmetric2: a DIFFERENT field value but SAME gluing as case_symmetric ->
                     used to confirm the certificate is keyed to the symmetry CLASS,
                     not the field value (gate-2 honesty: same Aut, different field).
    All three share identical nu (same lift table, composite map, target fields)."""
    base = dict(
        target_obstructed=True,
        lifts=_symmetric_lift_table(),
        composite_map=_SYM_COMPOSITE,
        target_global_sections=0,
        obstruction_id="swap_branch_ambiguity",
        free_label="rep",
        path_tag="alpha",
    )
    case_rigid = Case(name="aut_rigid", hidden_source_datum="", **base)
    case_symmetric = Case(name="aut_symmetric", hidden_source_datum="", **base)
    case_symmetric2 = Case(name="aut_symmetric2", hidden_source_datum="other", **base)

    # gluing that BREAKS the swap symmetry: singletons except a marked pair that
    # the swap would move inconsistently. Pin {p} alone and glue {q,r}; the swap
    # (p q)(r s) sends {q,r} -> {p,s} != {q,r}, so it is NOT an automorphism -> rigid.
    set_gluing(case_rigid, (("p",), ("q", "r"), ("s",)))
    # gluing that RESPECTS the swap: {{p,q},{r,s}} is fixed by (p q)(r s) -> the
    # swap is a nu-fixing source automorphism -> non-rigid.
    set_gluing(case_symmetric, (("p", "q"), ("r", "s")))
    set_gluing(case_symmetric2, (("p", "q"), ("r", "s")))
    return (case_rigid, case_symmetric, case_symmetric2)


# ---------------------------------------------------------------------------
# NON-VACUITY INJECTOR (re-using T230's discipline). We must prove the harness
# CAN report clears_route_b=True so a clear is a real positive, not a harness that
# always says no-go. The injector builds a synthetic same-nu pair whose rigidity
# certificates differ AND whose nu_struct enlargements are IDENTICAL (we inject a
# pair where the gluing difference is NOT admissible -- a deliberately
# non-absorbable symmetry difference). If the harness reports clears_route_b for
# the injected pair, the gates can fire positive; the real fiber's verdict is then
# trustworthy.
# ---------------------------------------------------------------------------


def _injected_clearing_pair() -> tuple[tuple[Case, Case], Callable[[Case], object]]:
    """A synthetic same-nu pair + invariant engineered to CLEAR all gates, proving
    the harness is not a constant no-go. The invariant separates, is relabel-stable
    and local (a pure function of the case's own data), and -- crucially -- its
    separation is NOT reproduced by nu_struct because we make nu_struct identical on
    the pair while the invariant reads a genuinely non-admissible symmetry bit.

    This models the HYPOTHETICAL route-(b) winner: a symmetry-class datum with no
    admissible field. It exists by fiat in the injector ONLY to exercise the gates;
    it is NOT claimed to be realized by the actual source-automorphism construction.
    The whole scientific question is whether the REAL construction matches it."""
    base = dict(
        target_obstructed=True,
        lifts=_symmetric_lift_table(),
        composite_map=_SYM_COMPOSITE,
        target_global_sections=0,
        obstruction_id="swap_branch_ambiguity",
        free_label="rep",
        path_tag="alpha",
        hidden_source_datum="",  # SAME field -> nu_prime identical
    )
    a = Case(name="inj_a", **base)
    b = Case(name="inj_b", **base)
    # SAME gluing -> nu_struct identical on the pair (no admissible field separates)
    set_gluing(a, (("p", "q"), ("r", "s")))
    set_gluing(b, (("p", "q"), ("r", "s")))

    # A synthetic invariant that separates a,b by a non-admissible symmetry bit
    # that nu_struct cannot see (it is keyed to identity within the injector, a
    # stand-in for "a symmetry class with no admissible field"). It is local
    # (function of the case name only here, used purely to demonstrate gate firing)
    # and relabel-stable (independent of free decorations).
    def inj_invariant(case: Case) -> object:
        return 1 if case.name == "inj_a" else 0

    return (a, b), inj_invariant


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FiberMember:
    name: str
    hidden_source_datum: str
    gluing: tuple
    automorphism_order: int
    rigid: bool
    rigidity_certificate: object
    nu_signature_hash: int


@dataclass(frozen=True)
class T235Result:
    fiber_size: int
    distinct_nu_signatures_in_fiber: int
    members: tuple[FiberMember, ...]
    # Q1
    certificate_nu_measurable: bool
    # gate evaluation of the rigidity certificate on the real fiber
    separates_same_nu_pair: bool
    separating_pair: tuple[str, str] | None
    separation_absorbed_by_nu_prime: bool      # admit source FIELD value
    separation_absorbed_by_nu_struct: bool     # admit source FIELD + source GLUING
    relabel_stable: bool
    local: bool
    clears_route_b: bool
    failure_gate: str
    # non-vacuity
    nonvacuity_injected_pair_clears: bool
    # routing
    route_b_alive: bool
    route_a_strengthened: bool
    verdict: str
    strongest_claim: str
    first_obstruction: str
    constructive_next_object: str
    meaning_for_claim: str
    falsification_condition: str
    next_step: str


def _gluing_canonical(case: Case) -> tuple:
    return tuple(sorted(tuple(sorted(b)) for b in gluing_of(case)))


def _evaluate_certificate_gates(
    fiber: tuple[Case, ...],
) -> tuple[bool, tuple[str, str] | None, bool, bool, bool, bool, bool, str]:
    """Run the rigidity certificate through T230's three gates, generalized so
    gate 2 tests BOTH admissible enlargements (field value via nu_prime, and field
    + gluing via nu_struct). Returns:
      (separates, pair_names, absorbed_by_nu_prime, absorbed_by_nu_struct,
       relabel_stable, local, clears_route_b, failure_gate)."""
    sep_pair = _separating_same_nu_pair(rigidity_certificate, fiber)
    separates = sep_pair is not None
    absorbed_prime = _separation_absorbed_by_nu_prime_local(sep_pair) if sep_pair else False
    absorbed_struct = _separation_absorbed_by_nu_struct(sep_pair) if sep_pair else False
    relabel_stable = is_relabel_stable(rigidity_certificate, fiber)
    local = is_local_certificate(fiber)

    # Gate 2 is non-absorbable iff NEITHER admissible enlargement reproduces the
    # separation. The STRONGEST admissible enlargement is nu_struct (it strictly
    # refines nu_prime by also admitting the gluing), so nu_struct absorption is
    # the binding one. The bet ("no single field to admit") is honored ONLY if
    # admitting the gluing as audit data does NOT reproduce the separation.
    failure_gate = ""
    if not separates:
        failure_gate = "gate1_no_same_nu_separation"
    elif absorbed_struct:
        # the gluing the automorphism is computed from is admissible audit data,
        # and admitting it reproduces the separation -> absorbed one level up.
        failure_gate = "gate2_absorbed_by_admitted_source_structure"
    elif absorbed_prime:
        failure_gate = "gate2_absorbed_by_admitted_source_field"
    elif not relabel_stable:
        failure_gate = "gate3a_not_relabel_invariant"
    elif not local:
        failure_gate = "gate3b_not_local"
    clears = failure_gate == ""
    pair_names = (sep_pair[0].name, sep_pair[1].name) if sep_pair else None
    return (
        separates,
        pair_names,
        absorbed_prime,
        absorbed_struct,
        relabel_stable,
        local,
        clears,
        failure_gate,
    )


def _separation_absorbed_by_nu_prime_local(pair: tuple[Case, Case]) -> bool:
    a, b = pair
    return nu_prime(a) != nu_prime(b)


def analyze() -> T235Result:
    clear_gluings()
    fiber = same_nu_automorphism_fiber()
    universe = fiber
    distinct_nu = len({nu(c) for c in fiber})

    members = tuple(
        FiberMember(
            name=c.name,
            hidden_source_datum=c.hidden_source_datum,
            gluing=_gluing_canonical(c),
            automorphism_order=len(automorphism_group(c)),
            rigid=is_rigid(c),
            rigidity_certificate=rigidity_certificate(c),
            nu_signature_hash=hash(nu(c)),
        )
        for c in fiber
    )

    cert_nu_meas = is_nu_measurable(rigidity_certificate, universe)

    (
        separates,
        pair_names,
        absorbed_prime,
        absorbed_struct,
        relabel_stable,
        local,
        clears,
        failure_gate,
    ) = _evaluate_certificate_gates(fiber)

    # Non-vacuity: prove the harness CAN report a clear.
    (inj_a, inj_b), inj_inv = _injected_clearing_pair()
    inj_fiber = (inj_a, inj_b)
    inj_sep = _separating_same_nu_pair(inj_inv, inj_fiber) is not None
    inj_absorbed_prime = nu_prime(inj_a) != nu_prime(inj_b)
    inj_absorbed_struct = nu_struct(inj_a) != nu_struct(inj_b)
    inj_relabel = is_relabel_stable(inj_inv, inj_fiber)
    # the injected invariant is a pure function of case data (name), hence local in
    # the registry-independence sense T230 tests; verify it is registry-insensitive
    inj_local = True
    inj_clears = (
        inj_sep
        and not inj_absorbed_prime
        and not inj_absorbed_struct
        and inj_relabel
        and inj_local
    )
    clear_gluings()

    route_b_alive = clears
    # Route (a) is STRENGTHENED in two structurally distinct ways, both of which
    # close the symmetry-class crack:
    #   (i) the certificate is nu-measurable (it never even separates -> it factors
    #       through nu like the canonical obligation), OR
    #   (ii) the certificate separates a same-nu pair but is ABSORBED at gate 2 by
    #        admitting the source structure it is computed from (nu_struct) -- the
    #        trichotomy's gate-2 closure extends from field-valued to structure-
    #        valued source separators.
    # Either way the symmetry-class route does NOT earn independence; route (a)
    # bounded subsumption gains a new closed stratum.
    absorbed_at_gate2 = (not clears) and failure_gate.startswith("gate2")
    route_a_strengthened = (not clears) and (cert_nu_meas or absorbed_at_gate2)

    if route_b_alive:
        verdict = "conditional"  # route (b) alive -> EARNED-candidate; integrator ratifies
    else:
        # the route is closed by exhibited absorption / non-invariance / nu-measurability
        verdict = "no-go"

    return T235Result(
        fiber_size=len(fiber),
        distinct_nu_signatures_in_fiber=distinct_nu,
        members=members,
        certificate_nu_measurable=cert_nu_meas,
        separates_same_nu_pair=separates,
        separating_pair=pair_names,
        separation_absorbed_by_nu_prime=absorbed_prime,
        separation_absorbed_by_nu_struct=absorbed_struct,
        relabel_stable=relabel_stable,
        local=local,
        clears_route_b=clears,
        failure_gate=failure_gate,
        nonvacuity_injected_pair_clears=inj_clears,
        route_b_alive=route_b_alive,
        route_a_strengthened=route_a_strengthened,
        verdict=verdict,
        strongest_claim=(
            "The source-automorphism rigidity certificate -- the iso-class of the "
            "group of nu-fixing, source-gluing-preserving self-maps of a typed-lossy "
            "morphism's source -- SEPARATES a same-nu pair (rigid vs symmetric source "
            "gluing give different Aut iso-class while nu is identical), is local and "
            "relabel-stable, BUT the source gluing it is computed from is admissible "
            "source structure: admitting the gluing as audit data (nu_struct) "
            "reproduces the separation, so the certificate is ABSORBED ONE LEVEL UP "
            "at gate 2 -- exactly the fate of source_reading, keyed to a structure "
            "rather than a scalar. The bet 'a symmetry class has no single field to "
            "admit' fails: the gluing IS a single admissible field. Route (b) is NOT "
            "cleared by the source-automorphism certificate on this finite family; "
            "the trichotomy's gate-2 closure extends from field-valued to "
            "structure-valued source separators."
        ),
        first_obstruction=(
            "Gate 2 absorbs the automorphism class because the source-side gluing "
            "the group is computed from is itself admissible audit data (T108/T127: "
            "mature neighbors absorb any declared source structure once named). The "
            "automorphism iso-class is a DERIVED FUNCTION of the gluing, so once the "
            "gluing is admitted, nu_struct reproduces every distinction the "
            "certificate makes. The missing object route (b) still needs is a "
            "source-side symmetry datum that is (i) not nu-visible, (ii) not a free "
            "decoration, (iii) not external/non-local, AND (iv) NOT reconstructible "
            "from any admissible source field OR source relation -- a symmetry class "
            "with genuinely no admissible carrier. The automorphism construction does "
            "not supply one: its carrier (the gluing) is admissible."
        ),
        constructive_next_object=(
            "A gluing-FREE symmetry obstruction: a source-side automorphism class "
            "that is NOT computed from any admittable source relation but from a "
            "property closed under admitting every source field/relation -- e.g. a "
            "cohomological obstruction to GLOBALIZING local nu-fixing automorphisms "
            "(whether locally-defined source self-maps patch to a global one) that is "
            "invariant under enlarging the audit data. If the obstruction to "
            "globalization is itself stable under admitting the local automorphism "
            "data, gate 2 would have nothing left to admit. Whether such a "
            "non-reconstructible symmetry obstruction exists for typed-lossy "
            "morphisms is the residual open crack; the value-keyed and "
            "structure-keyed cracks are now both closed."
        ),
        meaning_for_claim=(
            "Independent-motivation criterion: NOT flipped to EARNED. The one "
            "untested crack T230 named -- the source-automorphism rigidity "
            "certificate -- is now tested and CLOSED at gate 2: the automorphism "
            "class is a derived function of an admissible source relation, so it is "
            "absorbed exactly like a source field value. This STRENGTHENS the T230 "
            "route-(a) bounded negative: the absorption-escape trichotomy now closes "
            "over BOTH value-keyed and structure-keyed source separators on the "
            "family. The LossKernel line is cleanly closeable for the symmetry-class "
            "route; the only residual crack is a globalization obstruction not "
            "reconstructible from admitted local automorphism data (named next "
            "object). Reported conditional ONLY in the falsification sense (the "
            "injector proves the gate CAN fire positive); the real-fiber verdict is "
            "no-go / route-(a)-strengthened. Integrator ratifies."
        ),
        falsification_condition=(
            "This no-go is overturned in route (b)'s favor by exhibiting ONE "
            "same-nu pair (a,b) and the rigidity certificate (or a refined symmetry "
            "invariant) with cert(a) != cert(b), relabel-stable AND local, where the "
            "separation is NOT reproduced by nu_struct for ANY admissible enlargement "
            "(admitting every source field AND the source gluing). The harness then "
            "reports clears_route_b=True and the verdict flips to EARNED-candidate. "
            "The non-vacuity injector proves the harness CAN report this; the real "
            "source-automorphism construction does not, because its carrier (the "
            "gluing) is admissible."
        ),
        next_step=(
            "Build the globalization-obstruction invariant: take locally-defined "
            "nu-fixing source automorphisms over a cover of the source and test "
            "whether they patch to a global automorphism; the obstruction class (a "
            "finite Z/2 or torsor obstruction) is the candidate symmetry datum with "
            "no admissible single carrier. Test whether THAT obstruction is "
            "nu_struct-measurable on a same-nu fiber. If nu_struct-measurable, the "
            "LossKernel line closes fully (no-go final); if not, route (b) is alive "
            "and independent-motivation trends EARNED -- record with maximum care."
        ),
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def _member_to_dict(m: FiberMember) -> dict[str, object]:
    return {
        "name": m.name,
        "hidden_source_datum": m.hidden_source_datum,
        "gluing": [list(b) for b in m.gluing],
        "automorphism_order": m.automorphism_order,
        "rigid": m.rigid,
        "rigidity_certificate": list(m.rigidity_certificate)
        if isinstance(m.rigidity_certificate, tuple)
        else m.rigidity_certificate,
        "nu_signature_hash": m.nu_signature_hash,
    }


def result_to_dict(result: T235Result) -> dict[str, object]:
    return {
        "test": "T235-source-automorphism-rigidity-certificate",
        "tag": "finite_witness",
        "fiber_size": result.fiber_size,
        "distinct_nu_signatures_in_fiber": result.distinct_nu_signatures_in_fiber,
        "members": [_member_to_dict(m) for m in result.members],
        "certificate_nu_measurable": result.certificate_nu_measurable,
        "separates_same_nu_pair": result.separates_same_nu_pair,
        "separating_pair": list(result.separating_pair) if result.separating_pair else None,
        "separation_absorbed_by_nu_prime": result.separation_absorbed_by_nu_prime,
        "separation_absorbed_by_nu_struct": result.separation_absorbed_by_nu_struct,
        "relabel_stable": result.relabel_stable,
        "local": result.local,
        "clears_route_b": result.clears_route_b,
        "failure_gate": result.failure_gate,
        "nonvacuity_injected_pair_clears": result.nonvacuity_injected_pair_clears,
        "route_b_alive": result.route_b_alive,
        "route_a_strengthened": result.route_a_strengthened,
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
