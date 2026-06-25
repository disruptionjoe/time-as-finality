"""T231: Cover-refinement-stability colimit for coefficient-aware Z2 Cech-H1.

T226 ("Coefficient-Aware Cech-H1 Continuum-Obstruction Object",
`models/coefficient_sheaf_h1.py`) built a FINITE coefficient-aware Cech-H1 over a
finite annular nerve, valued in Z2, carrying the orientation transition 1-cochain.
On the `mobius_annular_4` witness it reports a NONTRIVIAL class (no global
section, loop sign -1) exactly where T222's coefficient-blind scalar encoding
falsely reports a section; on `cylinder_annular_4` both report a section. T226
closed the false-section trap but left the continuum row CONDITIONAL with the
bridge explicitly NAMED (T226 "Constructive next object" / "Next proof step"):

    "Build the directed colimit of the finite annular nerves under cover
     refinement and show the Z2 H1 class is STABLE across the refinement system
     (the class survives subdivision), giving a finite-data certificate that the
     continuum orientation class is what the finite nerve computes."

This module is that object. It constructs:

  (1) A genuine SUBDIVISION of an annular cover: `subdivide_annular` splits each
      of the n patches of an `annular_n` cover into two, producing `annular_2n`
      with a simplicial REFINEMENT MAP pi: nerve(annular_2n) -> nerve(annular_n)
      that sends each fine patch to the coarse patch containing it.

  (2) The induced PULLBACK of the Z2 transition 1-cochain along the refinement
      map, pi^* g, distributing each coarse reversal onto exactly one fine edge
      so the loop sign-product is preserved.

  (3) An executable REFINEMENT-STABILITY check: across the directed refinement
      system annular_4 -> annular_8 -> annular_16 -> ... the coefficient-aware
      H1 verdict ([g] = 0 / != 0, i.e. global-section / obstructed) AND the loop
      sign-product are INVARIANT. The nontrivial Mobius class and trivial
      cylinder class are PRESERVED under subdivision.

WHAT A FINITE REFINEMENT-STABILITY CERTIFICATE DOES AND DOES NOT LICENSE
(binding honesty guard, inherited verbatim in spirit from T226 / T222):

  DOES: it certifies that the finite-nerve Z2 class is REFINEMENT-STABLE -- the
  [g]-verdict and loop sign survive subdivision through the directed system, so
  the class the finite nerve computes is not an artifact of one particular cover
  granularity. This is the honest bridge FROM a `finite_witness` TOWARD a
  continuum statement: a finite-data certificate that refining the cover does not
  change the obstruction verdict.

  DOES NOT: it is STILL NOT a general continuum sheaf-cohomology theorem. No
  claim is made that the colimit over ALL covers equals the derived/sheaf
  cohomology of an orientation sheaf on a continuum space, nor that an arbitrary
  (non-annular, non-uniform) refinement system stabilizes. The certificate is
  exhibited over an explicit cofinal chain of annular subdivisions; promoting it
  to a continuum cohomology theorem is FORBIDDEN (honesty guard). Tag:
  finite_witness. No physics / curvature / connection / holonomy / new-object
  language: "monodromy" denotes only the loop sign-product, H1 is pure Z2 linear
  algebra on a finite cochain complex.

This is the CONTINUUM coefficient-sheaf bridge and is EXPLICITLY DISTINCT from
the discrete category-level D1FilteredMorphism object (a separate lane): T226 and
T228 both flag that the cover-refinement colimit and the D1Cat preserved-dims
colimit must NOT be conflated. They are different objects over different indexing
systems; this module touches only the coefficient-sheaf side.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.coefficient_sheaf_h1 import (
    CoverNerve,
    annular_cover,
    h1_verdict,
    is_cocycle,
    monodromy_sign,
    transition_is_coboundary,
    z2_add,
)


# ---------------------------------------------------------------------------
# Poly-time Z2 H1 decider for annular covers (avoids the 2^n frame search)
# ---------------------------------------------------------------------------
#
# T226's `transition_is_coboundary` enumerates all 2^(#opens) Z2 frame choices.
# That is fine for one small nerve but EXPONENTIAL across a refinement chain
# (annular_32 = 2^32 frames). For the refinement system we need a poly_decider.
#
# For an annular (single cover-cycle) nerve the H1 is one-dimensional: a Z2
# 1-cochain g is a coboundary  <=>  its XOR around the wrap cycle is 0. This is
# the cycle-space / spanning-tree computation specialized to one cycle: pick the
# spanning path (all edges but the wrap), set frames by accumulation, and g is a
# coboundary iff the wrap edge is then consistent, i.e. iff the total edge XOR
# is 0. Tag: poly_decider (linear in #edges, NOT a hidden search, NOT a hardness
# claim). The verdict it returns is cross-validated against the exhaustive
# `transition_is_coboundary` on small covers in the test suite.


def annular_cycle_parity(nerve: CoverNerve) -> int:
    """XOR (Z2 sum) of the transition cochain over all edges of an annular nerve.

    For a single-cycle (annular) cover this is the Z2 image of the loop
    sign-product: 0 == trivial class (global section), 1 == nontrivial class
    (no global section). Linear in the number of edges; poly_decider.
    """
    total = 0
    for c in nerve.transition.values():
        total = z2_add(total, c)
    return total


def annular_class_obstructed(nerve: CoverNerve) -> bool:
    """[g] != 0 for an annular nerve, via the wrap-cycle parity (poly_decider).

    True  == nontrivial class == no global section (Mobius).
    False == trivial class    == global section exists (cylinder).
    """
    return annular_cycle_parity(nerve) == 1


def poly_decider_matches_exhaustive(nerve: CoverNerve) -> bool:
    """Cross-validate the poly_decider against T226's exhaustive 2^n coboundary
    search on a (small) annular nerve: the wrap-cycle-parity verdict must equal
    the not-a-coboundary verdict. This is what licenses replacing the exponential
    search with the linear decider across the refinement chain. Only call on
    small nerves (the exhaustive side is 2^(#opens))."""
    poly = annular_class_obstructed(nerve)
    exhaustive = not transition_is_coboundary(nerve)
    return poly == exhaustive


# ---------------------------------------------------------------------------
# Refinement map between two annular nerves
# ---------------------------------------------------------------------------
#
# A refinement of an open cover V by an open cover U is a map pi : index(U) ->
# index(V) such that each fine patch U_a is contained in the coarse patch
# V_{pi(a)}. On nerves this induces a simplicial map sending a fine simplex to
# the (image) coarse simplex. On Cech 1-cochains it induces the PULLBACK
# pi^* : C^1(V) -> C^1(U); on cohomology the pullback is the canonical map of
# the directed system, and a refinement is a step in the directed colimit over
# covers. We work entirely with the explicit annular subdivision, so pi is
# concrete and the pullback is a finite, checkable map.


@dataclass(frozen=True)
class RefinementMap:
    """A simplicial refinement map from a fine nerve to a coarse nerve.

    `fine`        : the refining (finer) cover nerve.
    `coarse`      : the refined (coarser) cover nerve.
    `vertex_map`  : pi on 0-simplices, fine-open-index -> coarse-open-index, with
                    the containment U_a subset V_{pi(a)}.
    `edge_image`  : pi on the 1-simplices that actually carry the obstruction:
                    fine edge (a,b) -> the coarse edge it maps onto, or None when
                    pi(a)==pi(b) (the fine edge collapses INSIDE one coarse patch
                    and carries no coarse transition).
    """

    fine: CoverNerve
    coarse: CoverNerve
    vertex_map: dict[int, int]
    edge_image: dict[tuple[int, int], tuple[int, int] | None]


def subdivide_annular(
    coarse_count: int, reversed_edges: set[tuple[int, int]]
) -> tuple[CoverNerve, CoverNerve, RefinementMap]:
    """Subdivide an `annular_{n}` cover into an `annular_{2n}` cover + refinement.

    The coarse cover has n patches V_0..V_{n-1} arranged in a cycle, with the
    given `reversed_edges` carrying an orientation reversal (the same convention
    as `annular_cover`). Each coarse patch V_i is split into two fine patches
    U_{2i} and U_{2i+1} (left/right halves), giving a `annular_{2n}` cover with
    fine patches U_0..U_{2n-1} in a cycle.

    Containment / refinement map pi:
        pi(2i)   = i        (left half of V_i lies in V_i)
        pi(2i+1) = i        (right half of V_i lies in V_i)

    Fine cycle edges fall into two classes:
        * INTRA edges (2i, 2i+1): both endpoints map to the same coarse patch
          V_i; the fine overlap U_{2i} & U_{2i+1} sits INSIDE V_i, so it carries
          NO coarse transition -> transition 0, edge_image None.
        * INTER edges (2i+1, 2(i+1) mod 2n): endpoints map to adjacent coarse
          patches V_i, V_{i+1}; this fine overlap realizes the coarse overlap
          V_i & V_{i+1}, so it INHERITS the coarse edge's transition.

    This is a faithful subdivision: the wrap is preserved, the loop sign-product
    is carried onto exactly the INTER edges, and the INTRA edges are honest
    no-reversal overlaps. The pullback cochain pi^* g is exactly the fine
    transition built here.
    """
    n = coarse_count
    coarse = annular_cover(n, reversed_edges)

    fn = 2 * n
    fine_opens = tuple(f"U{a}" for a in range(fn))
    # fine cycle edges, normalized (a, (a+1) % fn)
    fine_edges = [(a, (a + 1) % fn) for a in range(fn)]

    vertex_map: dict[int, int] = {}
    for a in range(fn):
        vertex_map[a] = a // 2  # both halves of V_i map to i

    edge_image: dict[tuple[int, int], tuple[int, int] | None] = {}
    fine_transition: dict[tuple[int, int], int] = {}

    for (a, b) in fine_edges:
        ci, cj = vertex_map[a], vertex_map[b]
        if ci == cj:
            # INTRA edge: overlap inside a single coarse patch, no coarse datum.
            edge_image[(a, b)] = None
            fine_transition[(a, b)] = 0
        else:
            # INTER edge: realizes coarse overlap (ci, cj). Find the coarse edge.
            lo, hi = (ci, cj) if ci < cj else (cj, ci)
            # the coarse annular edge is stored as (i, (i+1)%n); the wrap edge is
            # (n-1, 0). Match against the coarse nerve's actual overlap keys.
            coarse_edge = _coarse_edge_for(coarse, ci, cj)
            edge_image[(a, b)] = coarse_edge
            fine_transition[(a, b)] = coarse.transition[coarse_edge]

    fine = CoverNerve(
        opens=fine_opens,
        overlaps=tuple(fine_edges),
        triples=(),  # thin subdivision: still no triple intersections
        transition=fine_transition,
    )
    refinement = RefinementMap(
        fine=fine,
        coarse=coarse,
        vertex_map=vertex_map,
        edge_image=edge_image,
    )
    return coarse, fine, refinement


def _coarse_edge_for(coarse: CoverNerve, ci: int, cj: int) -> tuple[int, int]:
    """Return the coarse nerve's 1-simplex key joining patches ci and cj."""
    for key in coarse.overlaps:
        if set(key) == {ci, cj}:
            return key
    raise KeyError(f"no coarse overlap joining {ci} and {cj}")


def pullback_is_consistent(refinement: RefinementMap) -> bool:
    """Check pi^* is a well-defined cochain pullback: every fine edge's transition
    equals the transition of its coarse image edge (0 when the image is None).

    This is the executable statement that the fine transition cochain IS the
    pullback pi^* g of the coarse transition cochain g along the refinement map.
    """
    coarse_g = refinement.coarse.transition
    fine_g = refinement.fine.transition
    for edge, img in refinement.edge_image.items():
        expected = 0 if img is None else coarse_g[img]
        if fine_g.get(edge, 0) != expected:
            return False
    return True


def vertex_map_respects_containment(refinement: RefinementMap) -> bool:
    """Check pi sends every fine open to a coarse open (a total well-typed map),
    and every fine INTER edge to an actual coarse 1-simplex (adjacent images).

    A real simplicial-map check: pi must carry 1-simplices to 1-simplices (or
    collapse them within a 0-simplex), never to a non-existent coarse overlap.
    """
    coarse_indices = set(range(len(refinement.coarse.opens)))
    for a, ci in refinement.vertex_map.items():
        if ci not in coarse_indices:
            return False
    for edge, img in refinement.edge_image.items():
        a, b = edge
        ci, cj = refinement.vertex_map[a], refinement.vertex_map[b]
        if img is None:
            if ci != cj:
                return False  # claimed intra but images differ
        else:
            if set(img) != {ci, cj}:
                return False  # image edge must join the two endpoint images
            if img not in refinement.coarse.overlaps:
                return False  # must be a real coarse 1-simplex
    return True


# ---------------------------------------------------------------------------
# Refinement-stability of the coefficient-aware H1 class
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class RefinementStep:
    """One step of the directed refinement system, with the H1 verdict on both
    the coarse and fine nerve and the stability check between them."""

    coarse_n: int
    fine_n: int
    coarse_loop_sign: int
    fine_loop_sign: int
    coarse_obstructed: bool          # [g] != 0 on the coarse nerve
    fine_obstructed: bool            # [g] != 0 on the fine nerve
    loop_sign_preserved: bool
    class_verdict_preserved: bool    # obstructed-flag invariant under refinement
    pullback_consistent: bool
    simplicial_map_valid: bool
    cocycle_valid_both: bool
    stable: bool                     # all of the above hold
    detail: str


def refinement_step(
    coarse_n: int, reversed_edges: set[tuple[int, int]]
) -> RefinementStep:
    """Build one subdivision annular_{n} -> annular_{2n} and certify stability.

    Uses the poly_decider `annular_class_obstructed` for the [g]-verdict so the
    chain scales (annular_32 would be 2^32 frames under the exhaustive search).
    The poly verdict is cross-validated against the exhaustive
    `transition_is_coboundary` on small covers in the test suite.
    """
    coarse, fine, refinement = subdivide_annular(coarse_n, reversed_edges)

    coarse_loop = monodromy_sign(coarse)
    fine_loop = monodromy_sign(fine)

    coarse_obstructed = annular_class_obstructed(coarse)
    fine_obstructed = annular_class_obstructed(fine)

    loop_preserved = coarse_loop == fine_loop
    class_preserved = coarse_obstructed == fine_obstructed
    pb_ok = pullback_is_consistent(refinement)
    simp_ok = vertex_map_respects_containment(refinement)
    cocycle_ok = is_cocycle(coarse) and is_cocycle(fine)

    stable = (
        loop_preserved
        and class_preserved
        and pb_ok
        and simp_ok
        and cocycle_ok
    )
    detail = (
        f"annular_{coarse_n} -> annular_{2 * coarse_n}: coarse loop sign "
        f"{coarse_loop:+d}, fine loop sign {fine_loop:+d} "
        f"(preserved: {loop_preserved}); coarse [g]!=0 = {coarse_obstructed}, "
        f"fine [g]!=0 = {fine_obstructed} (class verdict preserved: "
        f"{class_preserved}); pullback pi^* consistent: {pb_ok}; simplicial map "
        f"valid: {simp_ok}; cocycle valid both: {cocycle_ok}. STABLE: {stable}."
    )
    return RefinementStep(
        coarse_n=coarse_n,
        fine_n=2 * coarse_n,
        coarse_loop_sign=coarse_loop,
        fine_loop_sign=fine_loop,
        coarse_obstructed=coarse_obstructed,
        fine_obstructed=fine_obstructed,
        loop_sign_preserved=loop_preserved,
        class_verdict_preserved=class_preserved,
        pullback_consistent=pb_ok,
        simplicial_map_valid=simp_ok,
        cocycle_valid_both=cocycle_ok,
        stable=stable,
        detail=detail,
    )


def refinement_chain(
    base_n: int, reversed_edges_base: set[tuple[int, int]], depth: int
) -> list[RefinementStep]:
    """Build a directed refinement chain annular_{base_n} -> annular_{2 base_n}
    -> ... of `depth` subdivision steps, certifying stability at every step.

    The base reversal set is propagated correctly: the Mobius witness has exactly
    one reversed wrap edge at the base, which the subdivision distributes onto a
    single fine INTER edge each step, so the loop sign-product stays -1 (Mobius)
    or +1 (cylinder) throughout. To keep the reversal on the wrap at every scale
    we re-derive the fine reversal set from the fine transition cochain rather
    than re-specifying coordinates by hand.
    """
    steps: list[RefinementStep] = []
    n = base_n
    reversed_edges = set(reversed_edges_base)
    for _ in range(depth):
        step = refinement_step(n, reversed_edges)
        steps.append(step)
        # advance: the fine cover becomes the next coarse cover. Recover its
        # reversed edge set from the fine transition so the chain is faithful.
        _, fine, _ = subdivide_annular(n, reversed_edges)
        reversed_edges = {e for e, c in fine.transition.items() if c == 1}
        n = 2 * n
    return steps


# ---------------------------------------------------------------------------
# Top-level analysis
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class T231Result:
    mobius_steps: tuple[RefinementStep, ...]
    cylinder_steps: tuple[RefinementStep, ...]
    mobius_class_refinement_stable: bool   # nontrivial class preserved every step
    cylinder_class_refinement_stable: bool # trivial class preserved every step
    mobius_loop_sign_invariant: bool       # -1 at every scale
    cylinder_loop_sign_invariant: bool     # +1 at every scale
    all_steps_stable: bool
    verdict: str
    summary: str


def run_t231_analysis(depth: int = 3) -> T231Result:
    """Run the refinement-stability certificate over a directed annular chain.

    Mobius base: annular_4 with one reversed wrap edge (3, 0) -> loop sign -1,
    [g] != 0 (no global section). Cylinder base: annular_4 with no reversal ->
    loop sign +1, [g] = 0 (global section). Subdivide each `depth` times and
    certify the class verdict and loop sign are invariant across the chain.
    """
    mobius_steps = refinement_chain(4, {(3, 0)}, depth)
    cylinder_steps = refinement_chain(4, set(), depth)

    # Mobius: must be obstructed (nontrivial class) and loop sign -1 at EVERY
    # scale, both coarse and fine, with every per-step stability check passing.
    mobius_class_stable = all(
        s.coarse_obstructed and s.fine_obstructed and s.class_verdict_preserved
        for s in mobius_steps
    )
    mobius_loop_invariant = all(
        s.coarse_loop_sign == -1 and s.fine_loop_sign == -1 and s.loop_sign_preserved
        for s in mobius_steps
    )

    # Cylinder: must be NOT obstructed (trivial class) and loop sign +1 at every
    # scale, with every per-step stability check passing.
    cylinder_class_stable = all(
        (not s.coarse_obstructed)
        and (not s.fine_obstructed)
        and s.class_verdict_preserved
        for s in cylinder_steps
    )
    cylinder_loop_invariant = all(
        s.coarse_loop_sign == 1 and s.fine_loop_sign == 1 and s.loop_sign_preserved
        for s in cylinder_steps
    )

    all_stable = all(s.stable for s in mobius_steps + cylinder_steps)

    ok = (
        mobius_class_stable
        and cylinder_class_stable
        and mobius_loop_invariant
        and cylinder_loop_invariant
        and all_stable
    )
    verdict = "conditional" if ok else "fail"

    summary = (
        "Cover-refinement-stability certificate for the coefficient-aware Z2 "
        "Cech-H1. A genuine subdivision annular_n -> annular_2n (each coarse "
        "patch split in two) with an explicit simplicial refinement map pi and "
        "cochain pullback pi^* is built and iterated into a directed chain "
        "annular_4 -> annular_8 -> annular_16. The NONTRIVIAL Mobius class "
        "([g]!=0, loop sign -1) and the TRIVIAL cylinder class ([g]=0, loop sign "
        "+1) are PRESERVED at every refinement step: the obstruction verdict and "
        "the loop sign-product are invariant across the refinement system. This "
        "is a FINITE-DATA refinement-stability certificate -- the finite-nerve "
        "class survives subdivision -- and is the honest bridge from finite "
        "witness toward a continuum statement. IT IS NOT a general continuum "
        "sheaf-cohomology theorem (binding honesty guard): no claim is made over "
        "arbitrary covers or a derived/sheaf cohomology of a continuum space; the "
        "certificate is exhibited over an explicit cofinal annular subdivision "
        "chain only. Tag: finite_witness."
    )

    return T231Result(
        mobius_steps=tuple(mobius_steps),
        cylinder_steps=tuple(cylinder_steps),
        mobius_class_refinement_stable=mobius_class_stable,
        cylinder_class_refinement_stable=cylinder_class_stable,
        mobius_loop_sign_invariant=mobius_loop_invariant,
        cylinder_loop_sign_invariant=cylinder_loop_invariant,
        all_steps_stable=all_stable,
        verdict=verdict,
        summary=summary,
    )


def t231_result_to_dict(result: T231Result) -> dict[str, Any]:
    def _step(s: RefinementStep) -> dict[str, Any]:
        return {
            "coarse_n": s.coarse_n,
            "fine_n": s.fine_n,
            "coarse_loop_sign": s.coarse_loop_sign,
            "fine_loop_sign": s.fine_loop_sign,
            "coarse_obstructed": s.coarse_obstructed,
            "fine_obstructed": s.fine_obstructed,
            "loop_sign_preserved": s.loop_sign_preserved,
            "class_verdict_preserved": s.class_verdict_preserved,
            "pullback_consistent": s.pullback_consistent,
            "simplicial_map_valid": s.simplicial_map_valid,
            "cocycle_valid_both": s.cocycle_valid_both,
            "stable": s.stable,
            "detail": s.detail,
        }

    return {
        "mobius_steps": [_step(s) for s in result.mobius_steps],
        "cylinder_steps": [_step(s) for s in result.cylinder_steps],
        "mobius_class_refinement_stable": result.mobius_class_refinement_stable,
        "cylinder_class_refinement_stable": result.cylinder_class_refinement_stable,
        "mobius_loop_sign_invariant": result.mobius_loop_sign_invariant,
        "cylinder_loop_sign_invariant": result.cylinder_loop_sign_invariant,
        "all_steps_stable": result.all_steps_stable,
        "verdict": result.verdict,
        "summary": result.summary,
    }


if __name__ == "__main__":
    import json

    res = run_t231_analysis()
    print(json.dumps(t231_result_to_dict(res), indent=2))
