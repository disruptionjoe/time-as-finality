"""T241: lim^1 / Mittag-Leffler vanishing certificate for the orientation-sheaf
H^0 inverse system over the CSP-PO1 band's cofinal cover tower, plus retirement
of the thin-cover (d1 = 0) restriction via a genuine TRIPLE-OVERLAP witness.

T236 (`models/sheaf_h1_cofinality.py`) pinned the CSP-PO1 continuum row to a
SINGLE residual gap: the Cech->derived comparison
    H^1_Cech(colim covers)  ->  H^1_derived(orientation sheaf on the band)
is an iso ONLY AFTER a lim^1 / Mittag-Leffler vanishing over the directed tower of
covers, and T236 honestly left `derived_comparison_is_iso = None` (never True),
because that vanishing is a statement about the FULL tower, not certifiable from a
single finite stage. T236 also flagged a SECONDARY honesty note: every witness so
far (annular, staggered, theta) is a THIN cover (no triple overlaps), so the
cocycle condition `d1 = 0` was VACUOUS.

This module attacks BOTH, importing T226/T231/T236 BY IMPORT ONLY (it modifies
none of them; the 54-test T226+T231+T236 suite stays green):

  OBJECT (1) -- the lim^1 / Mittag-Leffler certificate.
  -----------------------------------------------------
  The Cech-to-derived comparison's correction at H^1 is the `lim^1 H^0` term of the
  inverse system { H^0(orientation sheaf | cover) } over the refinement tower, with
  connecting maps the RESTRICTION-along-refinement maps. We encode that inverse
  system as finite stages over the COFINAL uniform-bisection chain (T231's
  `subdivide_annular`, which T236 proved cofinal in the full staggered poset) and
  certify Mittag-Leffler:

    * For a CONNECTED cover of the band, H^0 of the constant Z2 orientation sheaf =
      locally-constant Z2 functions = Z2 (one bit per connected component).
    * Every refinement of a connected cover is connected, so H^0 = Z2 at EVERY
      stage and the restriction map H^0(coarse) -> H^0(fine) is the IDENTITY
      isomorphism (a global section restricts to the unique global section of the
      same value).
    * An inverse system all of whose connecting maps are ISOMORPHISMS is CONSTANT;
      its images are eventually (in fact always) stable -> Mittag-Leffler holds,
      and `lim^1` of a constant (or even just surjective-transition) system VANISHES.

  This is a genuine FINITE-TO-TOWER argument, NOT an illegitimate continuum leap:
  cofinality (T236, discharged) reduces lim/lim^1 over the FULL cover poset to
  lim/lim^1 over the cofinal chain; the chain's connecting maps are verified
  isomorphisms; "all connecting maps iso => lim^1 = 0" is an exact, finite-input
  theorem of homological algebra (Mittag-Leffler with stable images). The honest
  scope (the BINDING T236 guard): this licenses the iso for the TOWER-level
  comparison -- Cech-H^1 of the colimit equals the lim-corrected Cech-H^1 (now with
  zero correction) -- and we set THAT flag (`tower_cech_iso`) to True with the ML
  certificate as its license. It does NOT license the identification of the
  cover-colimit with the DERIVED sheaf cohomology of a CONTINUUM band, which would
  additionally require the annular tower to be cofinal in ALL open covers of the
  continuum (a good-cover / hypercover condition a countable annular tower does NOT
  establish). That strictly-larger continuum-sheaf identification is kept at
  `continuum_derived_iso = None` and its missing object is NAMED.

  OBJECT (2) -- retire the thin-cover (d1 = 0) restriction.
  ---------------------------------------------------------
  Every prior witness was thin, so `is_cocycle` was vacuously True. We build a
  TRIANGULATED-ANNULUS cover with GENUINE triple overlaps (d1 != 0 is exercised):
  a cyclic spine of n patches plus a bridge patch over each spine edge, giving n
  real triple intersections (i, i+1, b_i). The orientation reversal is carried as a
  NON-COBOUNDARY Z2 1-COCYCLE: a single spine-wrap reversal balanced on one bridge
  edge of the wrap triple, so EVERY triple's cocycle sum is 0 (a valid cocycle --
  the d1 = 0 cocycle condition is now a non-vacuous, genuinely-checked constraint)
  while the global wrap parity is odd ([g] != 0, no global section). The class is
  read by the FULL coefficient-aware coboundary computation
  (`transition_is_coboundary`, the exhaustive 2^n d0-image search -- NOT the
  cycle-space shortcut), and it reports the correct Z2 class, refinement-stably,
  on a cover where the triple-overlap cocycle condition is load-bearing.

BINDING HONESTY GUARD (inherited verbatim in spirit from T236 / T231 / T226):
  `finite_witness` + `poly_decider`. Object (1) sets a tower-level iso flag True
  ONLY because an exact finite-input ML theorem licenses it from the verified
  cofinal-chain isomorphisms; the strictly-larger CONTINUUM derived-sheaf iso stays
  None with its missing object named. A general continuum sheaf-cohomology theorem
  is FORBIDDEN. No physics / curvature / connection / holonomy / new-object
  language: "monodromy" = loop sign-product only; "H^1"/"H^0" = finite Z2
  cochain-complex (co)homology of a SPECIFIC finite cover.

This is the COEFFICIENT-SHEAF continuum lane. It is EXPLICITLY DISTINCT from and
does NOT touch the D1FilteredMorphism category-colimit lane (T237/T242): different
object, different indexing system. Imports T226/T231/T236 by import only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# Import-only reuse of the T226 Cech machinery, T231 refinement, T236 cofinality.
from models.coefficient_sheaf_h1 import (
    CoverNerve,
    annular_cover,
    is_cocycle,
    monodromy_sign,
    transition_is_coboundary,
    z2_add,
)
from models.sheaf_h1_refinement import (
    annular_class_obstructed,
    subdivide_annular,
)
from models.sheaf_h1_cofinality import (
    cofinality_certificate,
    general_class_obstructed,
    general_class_vector,
    general_h1_rank,
    num_components,
)


# ===========================================================================
# (1) THE H^0 INVERSE SYSTEM AND ITS lim^1 / MITTAG-LEFFLER CERTIFICATE
# ===========================================================================
#
# H^0 of the constant Z2 orientation sheaf restricted to a finite cover nerve is
# the group of GLOBAL SECTIONS = locally-constant Z2 functions on the nerve =
# Z2^(#connected components). For the connected band cover this is Z2 (dim 1).
#
# The refinement tower gives an INVERSE system of these H^0 groups, with the
# connecting map being RESTRICTION along refinement: a global section on the
# coarse cover restricts to a global section on the fine cover. Because both
# covers are connected and the constant sheaf has the same stalk, this restriction
# is the IDENTITY isomorphism Z2 -> Z2 (the unique value-preserving map of global
# sections). An inverse system of isomorphisms is CONSTANT; Mittag-Leffler holds
# with stable images and lim^1 vanishes.
#
# We encode the system as finite stages along the COFINAL uniform-bisection chain
# (T236 proved this chain cofinal in the full staggered poset, so its lim^1
# controls the full poset's lim^1), verify each stage is connected (H^0 = Z2) and
# each connecting map is an iso, then certify ML + lim^1 = 0 as an exact
# finite-input consequence.


def h0_dimension(nerve: CoverNerve) -> int:
    """dim_{Z2} H^0(constant Z2 orientation sheaf | nerve) = #connected components.

    Global sections of the constant sheaf are locally-constant functions: one free
    Z2 bit per connected component of the nerve. poly_decider (union-find, linear).
    """
    return num_components(nerve)


@dataclass(frozen=True)
class H0InverseStage:
    """One stage of the H^0 inverse system: a cover, its H^0 dimension, and the
    connecting (restriction) map TO it from the previous (coarser) stage."""

    label: str
    cover_size: int
    h0_dim: int
    connected: bool
    # the restriction map H^0(prev coarse) -> H^0(this fine):
    connecting_map_is_defined: bool
    connecting_map_is_iso: bool        # iso of Z2^k -> Z2^k (here k = 1)
    image_dim: int                     # rank of the connecting map's image


def _restriction_is_iso(coarse: CoverNerve, fine: CoverNerve) -> tuple[bool, int]:
    """The restriction map H^0(coarse) -> H^0(fine) for the constant Z2 sheaf.

    A global section is a locally-constant Z2 function; restriction along a
    refinement re-expresses it on the finer cover WITHOUT changing its values, so
    it is injective, and it is surjective iff every fine connected component lies
    inside a coarse connected component (always true for a refinement). Hence it is
    an isomorphism exactly when the component counts agree. Returns (is_iso,
    image_dim). image_dim = dim H^0(fine) when surjective.

    This is computed structurally (component counts + the refinement containment),
    not asserted: a refinement NEVER splits a connected component, and a connected
    coarse cover stays connected, so for the connected band both are Z2 and the map
    is the identity iso. We verify the component counts to make it a real check.
    """
    cc_coarse = num_components(coarse)
    cc_fine = num_components(fine)
    # Restriction of a locally-constant function is injective (values preserved).
    # It is surjective iff the fine cover has no MORE components than the coarse
    # (a refinement of a connected cover stays connected => equal counts here).
    is_iso = (cc_coarse == cc_fine)
    image_dim = cc_fine if is_iso else min(cc_coarse, cc_fine)
    return is_iso, image_dim


@dataclass(frozen=True)
class MittagLefflerCertificate:
    """Mittag-Leffler + lim^1-vanishing certificate for the H^0 inverse system over
    the cofinal uniform-bisection chain of the band.

    Fields are all VERIFIED on finite stages; the lim^1 = 0 conclusion is the exact
    finite-input ML theorem ("connecting maps all iso => constant system => stable
    images => ML => lim^1 = 0"), with cofinality (T236) reducing the full-poset
    lim^1 to this chain's lim^1.
    """

    chain_depth: int
    stages: tuple[H0InverseStage, ...]
    every_stage_connected: bool             # H^0 = Z2 at every stage
    every_connecting_map_iso: bool          # the system is constant
    images_eventually_stable: bool          # Mittag-Leffler condition
    system_is_constant: bool                # strictly: all maps iso
    lim1_vanishes: bool                     # exact consequence of constant/ML
    cofinal_chain_controls_tower: bool      # imported T236 cofinality
    detail: str


def mittag_leffler_certificate(
    base_n: int = 4,
    reversed_edges_base: set[tuple[int, int]] | None = None,
    depth: int = 4,
) -> MittagLefflerCertificate:
    """Build the H^0 inverse system over the cofinal bisection chain
    annular_{base_n} -> annular_{2 base_n} -> ... (depth steps) and certify
    Mittag-Leffler + lim^1 = 0.

    The reversal set does not affect H^0 (the orientation twist lives in H^1, not
    H^0 -- H^0 only sees connectivity), but we carry it so the chain is the SAME
    one whose H^1 class T231/T236 tracked.
    """
    if reversed_edges_base is None:
        reversed_edges_base = {(base_n - 1, 0)}

    stages: list[H0InverseStage] = []
    n = base_n
    reversed_edges = set(reversed_edges_base)

    prev: CoverNerve | None = None
    # stage 0: the base coarse cover (no incoming connecting map)
    base_cover = annular_cover(n, reversed_edges)
    stages.append(
        H0InverseStage(
            label=f"annular_{n}",
            cover_size=len(base_cover.opens),
            h0_dim=h0_dimension(base_cover),
            connected=num_components(base_cover) == 1,
            connecting_map_is_defined=False,
            connecting_map_is_iso=True,  # vacuous (no incoming map)
            image_dim=h0_dimension(base_cover),
        )
    )
    prev = base_cover

    for _ in range(depth):
        coarse, fine, _ = subdivide_annular(n, reversed_edges)
        is_iso, image_dim = _restriction_is_iso(coarse, fine)
        stages.append(
            H0InverseStage(
                label=f"annular_{2 * n}",
                cover_size=len(fine.opens),
                h0_dim=h0_dimension(fine),
                connected=num_components(fine) == 1,
                connecting_map_is_defined=True,
                connecting_map_is_iso=is_iso,
                image_dim=image_dim,
            )
        )
        # advance the chain (recover fine reversal set faithfully, as T231 does)
        reversed_edges = {e for e, c in fine.transition.items() if c == 1}
        n = 2 * n
        prev = fine

    every_connected = all(s.connected for s in stages)
    every_iso = all(s.connecting_map_is_iso for s in stages if s.connecting_map_is_defined)
    # Mittag-Leffler: the images of the connecting maps are eventually stable. With
    # all maps iso the image at every stage equals the full group, so the images
    # are stable from stage 0 (the strongest form of ML).
    image_dims = [s.image_dim for s in stages if s.connecting_map_is_defined]
    images_stable = len(set(image_dims)) <= 1  # all equal -> stable
    system_constant = every_iso
    # lim^1 of a Mittag-Leffler inverse system of (finite) abelian groups VANISHES;
    # a constant system is the strongest such case. This is the exact finite-input
    # theorem -- we are NOT inferring a continuum fact, we are applying ML to the
    # verified-iso chain.
    lim1_zero = system_constant and images_stable and every_connected

    # cofinality: the bisection chain is cofinal in the full staggered poset
    # (imported from T236), so lim^1 over the full poset = lim^1 over this chain.
    cof_cert, _ = cofinality_certificate(base_n, set(reversed_edges_base))
    cofinal_controls = cof_cert.cofinal

    detail = (
        f"H^0 inverse system over the cofinal bisection chain (depth {depth}): "
        f"H^0 dim = 1 (connected) at every stage; every restriction connecting map "
        f"is the identity iso Z2->Z2; the system is CONSTANT; images are stable "
        f"(all = Z2); Mittag-Leffler holds; lim^1 = 0. Cofinality (T236) reduces "
        f"the full-poset lim^1 to this chain's lim^1, so lim^1 = 0 over the full "
        f"cover poset. EXACT finite-input ML theorem; not a continuum inference."
    )

    return MittagLefflerCertificate(
        chain_depth=depth,
        stages=tuple(stages),
        every_stage_connected=every_connected,
        every_connecting_map_iso=every_iso,
        images_eventually_stable=images_stable,
        system_is_constant=system_constant,
        lim1_vanishes=lim1_zero,
        cofinal_chain_controls_tower=cofinal_controls,
        detail=detail,
    )


# ===========================================================================
# (2) TRIPLE-OVERLAP WITNESS: retire the thin-cover (d1 = 0) restriction
# ===========================================================================
#
# Every prior witness was THIN (triples = ()), so `is_cocycle` was vacuously True.
# Here we build a TRIANGULATED-ANNULUS cover with GENUINE triple overlaps so the
# cocycle (d1 = 0) condition is a non-vacuous, load-bearing constraint, and carry
# the orientation reversal as a real NON-COBOUNDARY 1-COCYCLE.
#
# Nerve: a cyclic SPINE of n patches 0..n-1 (the loop), plus a BRIDGE patch
# b_i = n+i sitting over each spine edge (i, i+1), forming a real triple overlap
# (i, i+1, b_i). Edges: the spine cycle (i, i+1), plus (i, b_i) and (i+1, b_i) for
# each bridge. Triples: (i, i+1, b_i) -- n genuine triple intersections.
#
# The orientation reversal (the Mobius wrap) is placed so that EVERY triple's
# cocycle sum g(a,b) + g(b,c) + g(a,c) = 0 (a valid 1-cocycle) while the GLOBAL
# wrap parity is odd: put the reversal on the spine wrap edge AND on one bridge
# edge of the wrap triple, balancing that triple to 0 but leaving the loop parity 1.


def triangulated_annulus(n: int, wrap_twist: bool) -> CoverNerve:
    """A triangulated-annulus cover with GENUINE triple overlaps (d1 != 0 exercised).

    Spine patches 0..n-1 in a cycle; bridge patch b_i = n+i over spine edge
    (i, (i+1) mod n). Triples (i, (i+1) mod n, b_i) are real triple intersections.

    `wrap_twist=False`  -> cylinder: trivial cocycle, global section exists ([g]=0).
    `wrap_twist=True`   -> Mobius: a single spine-wrap reversal balanced on one
                           bridge edge of the wrap triple, so every triple's cocycle
                           sum is 0 (VALID cocycle, d1 = 0 satisfied non-vacuously)
                           but the global wrap parity is odd ([g] != 0, no section).
    """
    opens = tuple(f"U{i}" for i in range(2 * n))
    overlaps: list[tuple[int, int]] = []
    triples: list[tuple[int, int, int]] = []
    transition: dict[tuple[int, int], int] = {}

    for i in range(n):
        j = (i + 1) % n
        bi = n + i
        e_spine = tuple(sorted((i, j)))
        e_ib = tuple(sorted((i, bi)))
        e_jb = tuple(sorted((j, bi)))
        for e in (e_spine, e_ib, e_jb):
            if e not in transition:
                overlaps.append(e)  # type: ignore[arg-type]
                transition[e] = 0   # type: ignore[index]
        triples.append(tuple(sorted((i, j, bi))))  # type: ignore[arg-type]

    if wrap_twist:
        # wrap triple is (0, n-1, 2n-1): spine wrap edge (n-1, 0) + bridge edge
        # (0, 2n-1). Reverse BOTH so that triple's cocycle sum stays 0 (valid
        # cocycle) while the global spine wrap parity is odd.
        e_spine_wrap = tuple(sorted((n - 1, 0)))
        e_bridge = tuple(sorted((0, 2 * n - 1)))
        transition[e_spine_wrap] = 1  # type: ignore[index]
        transition[e_bridge] = 1      # type: ignore[index]

    return CoverNerve(
        opens=opens,
        overlaps=tuple(overlaps),
        triples=tuple(triples),
        transition=transition,
    )


@dataclass(frozen=True)
class TripleOverlapVerdict:
    """Verdict for a triple-overlap cover: the cocycle (d1) condition is exercised
    non-vacuously, and the FULL coboundary computation reports the class."""

    name: str
    num_triples: int
    d1_nonvacuous: bool                 # there ARE triples (cocycle condition real)
    is_valid_cocycle: bool              # passes the d1 = 0 cocycle check
    full_coboundary_section: bool       # transition_is_coboundary (exhaustive d0)
    class_obstructed: bool              # [g] != 0 (no global section)
    loop_sign: int
    detail: str


def triple_overlap_verdict(nerve: CoverNerve, name: str) -> TripleOverlapVerdict:
    num_tri = len(nerve.triples)
    cocyc = is_cocycle(nerve)
    section = transition_is_coboundary(nerve)  # FULL exhaustive d0-image search
    obstructed = not section
    loop = monodromy_sign(nerve)
    detail = (
        f"'{name}': {len(nerve.opens)} patches, {len(nerve.overlaps)} overlaps, "
        f"{num_tri} GENUINE triples (d1 condition non-vacuous: {num_tri > 0}). "
        f"Valid cocycle (every triple sums to 0): {cocyc}. Full coboundary "
        f"computation reports a global section: {section}. [g] != 0 "
        f"(obstructed): {obstructed}. Loop sign: {loop:+d}."
    )
    return TripleOverlapVerdict(
        name=name,
        num_triples=num_tri,
        d1_nonvacuous=num_tri > 0,
        is_valid_cocycle=cocyc,
        full_coboundary_section=section,
        class_obstructed=obstructed,
        loop_sign=loop,
        detail=detail,
    )


def _spine_reversed_set(n: int) -> set[tuple[int, int]]:
    """The reversed-edge set carried by `triangulated_annulus(n, True)` -- used to
    rebuild the twist after a refinement, so the wrap parity is preserved."""
    return {tuple(sorted((n - 1, 0))), tuple(sorted((0, 2 * n - 1)))}


def triple_overlap_refinement_stable() -> tuple[bool, list[TripleOverlapVerdict]]:
    """Check the triple-overlap class is refinement-stable: across n = 4, 6, 8 the
    cylinder stays a section ([g] = 0) and the Mobius stays obstructed ([g] != 0),
    with the cocycle condition non-vacuous (real triples) at every scale, read by
    the FULL coboundary computation (not the cycle-space shortcut).

    'Refinement' here is densification of the triangulated annulus (more spine
    patches => finer cover of the same band, more triple overlaps). The class
    verdict must be invariant across the densification.
    """
    verdicts: list[TripleOverlapVerdict] = []
    cyl_obstructed: list[bool] = []
    mob_obstructed: list[bool] = []
    all_have_triples = True
    all_valid_cocycle = True

    for n in (4, 6, 8):
        cyl = triangulated_annulus(n, wrap_twist=False)
        mob = triangulated_annulus(n, wrap_twist=True)
        vc = triple_overlap_verdict(cyl, f"triangulated_cylinder_{n}")
        vm = triple_overlap_verdict(mob, f"triangulated_mobius_{n}")
        verdicts.extend([vc, vm])
        cyl_obstructed.append(vc.class_obstructed)
        mob_obstructed.append(vm.class_obstructed)
        if not (vc.d1_nonvacuous and vm.d1_nonvacuous):
            all_have_triples = False
        if not (vc.is_valid_cocycle and vm.is_valid_cocycle):
            all_valid_cocycle = False

    stable = (
        all(not o for o in cyl_obstructed)    # cylinder: section at every scale
        and all(o for o in mob_obstructed)    # mobius: obstructed at every scale
        and all_have_triples                  # d1 non-vacuous at every scale
        and all_valid_cocycle                 # valid cocycle at every scale
    )
    return stable, verdicts


# ===========================================================================
# (3) THE Cech -> DERIVED COMPARISON, NOW WITH THE ML CERTIFICATE
# ===========================================================================
#
# T236 left `derived_comparison_is_iso = None`. With the ML certificate (lim^1 = 0)
# we can now license the TOWER-LEVEL iso -- Cech-H^1 of the colimit equals the
# lim-corrected Cech-H^1, and the correction (lim^1 H^0) is zero -- and we set THAT
# flag True with the ML certificate as its explicit license.
#
# What we DO NOT do (the BINDING T236 honesty guard): we do NOT set the strictly
# larger CONTINUUM derived-sheaf iso. Identifying the cover-colimit with the
# DERIVED functor sheaf cohomology of a CONTINUUM band requires, beyond lim^1 = 0,
# that the annular tower be COFINAL IN ALL OPEN COVERS of the continuum (a good-
# cover / hypercover condition). A countable annular tower does NOT establish that.
# So `continuum_derived_iso` stays None and its missing object is NAMED.


@dataclass(frozen=True)
class Lim1Comparison:
    """The Cech->derived comparison, upgraded with the lim^1 certificate.

    Distinguishes TWO comparison maps that T236 conflated under one None flag:
      * `tower_cech_iso`: Cech-H^1(colim covers) == lim-corrected Cech-H^1, with the
        lim^1 H^0 correction now CERTIFIED zero. LICENSED True by the ML certificate.
      * `continuum_derived_iso`: cover-colimit == derived sheaf cohomology of the
        CONTINUUM band. Still None -- needs the tower to be cofinal in ALL open
        covers (good-cover/hypercover), which a countable annular tower does not give.
    """

    ml_certified: bool                       # lim^1 H^0 = 0 certified
    tower_cech_iso: bool | None              # now True, licensed by ML
    tower_cech_iso_license: str
    continuum_derived_iso: bool | None       # still None: the strictly-larger claim
    continuum_missing_object: str
    forbidden: str


def lim1_comparison(base_n: int = 4) -> Lim1Comparison:
    cert = mittag_leffler_certificate(base_n=base_n, depth=4)
    ml_ok = cert.lim1_vanishes and cert.cofinal_chain_controls_tower

    return Lim1Comparison(
        ml_certified=ml_ok,
        # The tower-level Cech iso is licensed ONLY by the genuine ML certificate
        # (lim^1 = 0 from verified cofinal-chain isomorphisms + T236 cofinality).
        # If the ML certificate fails, this stays None (honest).
        tower_cech_iso=True if ml_ok else None,
        tower_cech_iso_license=(
            "Cech-H^1(colim covers) == lim-corrected Cech-H^1 with the lim^1 H^0 "
            "correction CERTIFIED zero: the H^0 inverse system over the cofinal "
            "bisection chain has all connecting (restriction) maps equal to the "
            "identity iso Z2->Z2 (every stage connected => H^0 = Z2), so the system "
            "is constant, Mittag-Leffler holds with stable images, and lim^1 = 0. "
            "Cofinality (T236) reduces the full-poset lim^1 to this chain's lim^1. "
            "This is an EXACT finite-input ML theorem, not a continuum inference."
        ),
        # The strictly-larger continuum-sheaf identification is NOT licensed.
        continuum_derived_iso=None,
        continuum_missing_object=(
            "Identifying the cover-colimit Cech-H^1 with the DERIVED functor sheaf "
            "cohomology of a CONTINUUM band needs, BEYOND lim^1 H^0 = 0, that the "
            "annular refinement tower be COFINAL IN ALL OPEN COVERS of the band (a "
            "good-cover / hypercover cofinality), so that Cech computes the derived "
            "functor. A countable annular tower does NOT establish that good-cover "
            "cofinality; this is the one remaining tower-level object, and a finite "
            "witness cannot supply it. (Distinct from the lim^1 term, which IS now "
            "certified.)"
        ),
        forbidden=(
            "Asserting the CONTINUUM derived-sheaf iso, or a general continuum "
            "sheaf-cohomology theorem, is FORBIDDEN from this finite witness: the "
            "ML certificate clears the lim^1 correction but NOT the good-cover "
            "cofinality that the continuum derived identification additionally needs."
        ),
    )


# ===========================================================================
# Top-level analysis
# ===========================================================================


@dataclass(frozen=True)
class T241Result:
    # (1) lim^1 / Mittag-Leffler
    ml: MittagLefflerCertificate
    # (2) triple-overlap witness (retire thin-cover restriction)
    triple_overlap_stable: bool
    triple_overlap_verdicts: tuple[TripleOverlapVerdict, ...]
    # (3) upgraded Cech->derived comparison
    comparison: Lim1Comparison
    # roll-up
    verdict: str
    summary: str


def run_t241_analysis(base_n: int = 4) -> T241Result:
    # ---- (1) lim^1 / Mittag-Leffler certificate ----
    ml = mittag_leffler_certificate(base_n=base_n, depth=4)

    # ---- (2) triple-overlap witness ----
    triple_stable, triple_verdicts = triple_overlap_refinement_stable()

    # ---- (3) upgraded comparison ----
    comparison = lim1_comparison(base_n=base_n)

    # ---- roll-up verdict ----
    # The ML certificate must genuinely fire (lim^1 = 0 from verified isomorphisms +
    # cofinality); the triple-overlap witness must exercise d1 non-vacuously and
    # report the correct class refinement-stably; the tower-level Cech iso is now
    # licensed True while the strictly-larger CONTINUUM derived iso is honestly None.
    ml_ok = (
        ml.every_stage_connected
        and ml.every_connecting_map_iso
        and ml.images_eventually_stable
        and ml.system_is_constant
        and ml.lim1_vanishes
        and ml.cofinal_chain_controls_tower
    )
    comparison_ok = (
        comparison.ml_certified
        and comparison.tower_cech_iso is True       # licensed by ML
        and comparison.continuum_derived_iso is None  # honest: NOT closed at continuum
    )
    ok = ml_ok and triple_stable and comparison_ok

    # conditional: the lim^1 gap T236 named is now CLEARED at the tower level (a
    # real positive result), but the CONTINUUM derived-sheaf identification remains
    # bounded by a NEWLY-NAMED hypothesis (good-cover cofinality). conditional, not
    # closed: the named binding hypothesis is the good-cover cofinality.
    verdict = "conditional" if ok else "fail"

    summary = (
        "T241 attacks the SINGLE residual gap T236 pinned the CSP-PO1 continuum row "
        "to (the Cech->derived comparison's lim^1 / Mittag-Leffler vanishing) and "
        "retires the thin-cover (d1 = 0) restriction. (1) lim^1 / MITTAG-LEFFLER: "
        "the orientation-sheaf H^0 inverse system over the COFINAL uniform-bisection "
        "chain has H^0 = Z2 (connected) at every stage and every restriction "
        "connecting map equal to the identity iso, so the system is CONSTANT, "
        "Mittag-Leffler holds with stable images, and lim^1 VANISHES; cofinality "
        "(imported from T236, discharged) reduces the full-poset lim^1 to this "
        "chain's lim^1. This is an EXACT finite-input ML theorem and it LICENSES the "
        "TOWER-LEVEL Cech iso (Cech-H^1 of the colimit == lim-corrected Cech-H^1, "
        "correction now zero) -- the flag T236 left None is set True WITH the ML "
        "certificate as its license. (2) TRIPLE-OVERLAP WITNESS: a "
        "triangulated-annulus cover with GENUINE triple intersections (d1 != 0 "
        "exercised) carries the orientation reversal as a valid NON-COBOUNDARY "
        "1-cocycle (every triple's cocycle sum 0, global wrap parity odd); the FULL "
        "coboundary computation (exhaustive d0-image search, NOT the cycle-space "
        "shortcut) reports the correct Z2 class -- cylinder a section, Mobius "
        "obstructed -- refinement-stably across n = 4, 6, 8, retiring the vacuous-"
        "cocycle restriction. (3) The strictly-LARGER CONTINUUM derived-sheaf iso "
        "stays None: identifying the cover-colimit with the DERIVED sheaf cohomology "
        "of a continuum band needs, BEYOND lim^1 = 0, a GOOD-COVER / hypercover "
        "cofinality (the annular tower cofinal in ALL open covers) that a countable "
        "tower does not establish -- the one newly-named binding hypothesis. Verdict "
        "CONDITIONAL: the lim^1 gap is CLEARED at the tower level and the thin-cover "
        "restriction is RETIRED, but the continuum derived identification is bounded "
        "by the good-cover cofinality hypothesis (binding honesty guard: a general "
        "continuum sheaf-cohomology theorem is FORBIDDEN from this finite witness). "
        "Tag: finite_witness + poly_decider."
    )

    return T241Result(
        ml=ml,
        triple_overlap_stable=triple_stable,
        triple_overlap_verdicts=tuple(triple_verdicts),
        comparison=comparison,
        verdict=verdict,
        summary=summary,
    )


def t241_result_to_dict(result: T241Result) -> dict[str, Any]:
    def _stage(s: H0InverseStage) -> dict[str, Any]:
        return {
            "label": s.label,
            "cover_size": s.cover_size,
            "h0_dim": s.h0_dim,
            "connected": s.connected,
            "connecting_map_is_defined": s.connecting_map_is_defined,
            "connecting_map_is_iso": s.connecting_map_is_iso,
            "image_dim": s.image_dim,
        }

    def _tov(v: TripleOverlapVerdict) -> dict[str, Any]:
        return {
            "name": v.name,
            "num_triples": v.num_triples,
            "d1_nonvacuous": v.d1_nonvacuous,
            "is_valid_cocycle": v.is_valid_cocycle,
            "full_coboundary_section": v.full_coboundary_section,
            "class_obstructed": v.class_obstructed,
            "loop_sign": v.loop_sign,
            "detail": v.detail,
        }

    return {
        "mittag_leffler": {
            "chain_depth": result.ml.chain_depth,
            "stages": [_stage(s) for s in result.ml.stages],
            "every_stage_connected": result.ml.every_stage_connected,
            "every_connecting_map_iso": result.ml.every_connecting_map_iso,
            "images_eventually_stable": result.ml.images_eventually_stable,
            "system_is_constant": result.ml.system_is_constant,
            "lim1_vanishes": result.ml.lim1_vanishes,
            "cofinal_chain_controls_tower": result.ml.cofinal_chain_controls_tower,
            "detail": result.ml.detail,
        },
        "triple_overlap_stable": result.triple_overlap_stable,
        "triple_overlap_verdicts": [_tov(v) for v in result.triple_overlap_verdicts],
        "comparison": {
            "ml_certified": result.comparison.ml_certified,
            "tower_cech_iso": result.comparison.tower_cech_iso,
            "tower_cech_iso_license": result.comparison.tower_cech_iso_license,
            "continuum_derived_iso": result.comparison.continuum_derived_iso,
            "continuum_missing_object": result.comparison.continuum_missing_object,
            "forbidden": result.comparison.forbidden,
        },
        "verdict": result.verdict,
        "summary": result.summary,
    }


if __name__ == "__main__":
    import json

    res = run_t241_analysis()
    print(json.dumps(t241_result_to_dict(res), indent=2))
