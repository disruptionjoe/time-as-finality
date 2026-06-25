"""Tests for T231 cover-refinement-stability of the coefficient-aware Z2 Cech-H1.

Real checks of the refinement-stability certificate:
  (1) The subdivision annular_n -> annular_2n is a genuine simplicial refinement:
      the vertex map respects patch containment, the edge images are real coarse
      1-simplices, and the fine transition cochain IS the pullback pi^* of the
      coarse transition cochain.
  (2) The coefficient-aware H1 verdict ([g] = 0 / != 0) AND the loop sign-product
      are INVARIANT across the refinement system: the nontrivial Mobius class and
      trivial cylinder class are preserved under subdivision through a directed
      chain annular_4 -> annular_8 -> annular_16.
  (3) Honesty-guard checks: the certificate is exhibited over the explicit
      annular chain; nothing here asserts a general continuum cohomology theorem.

Plus structural checks that the subdivision actually changes the cover (doubles
the patch count and edge count) so refinement-stability is a non-vacuous claim.
"""

from models.coefficient_sheaf_h1 import (
    annular_cover,
    h1_verdict,
    monodromy_sign,
    transition_is_coboundary,
)
from models.sheaf_h1_refinement import (
    annular_class_obstructed,
    annular_cycle_parity,
    pullback_is_consistent,
    poly_decider_matches_exhaustive,
    refinement_chain,
    refinement_step,
    run_t231_analysis,
    subdivide_annular,
    vertex_map_respects_containment,
)


# --- The poly_decider agrees with T226's exhaustive H1 ---------------------


def test_poly_decider_matches_exhaustive_search():
    """The linear wrap-cycle-parity decider returns the SAME [g]!=0 verdict as
    T226's exhaustive 2^n coboundary search, on both Mobius and cylinder covers
    up to annular_16 (2^16 frames, still tractable). This is what licenses
    using the poly_decider across the (otherwise 2^32) refinement chain."""
    for n in (4, 8, 16):
        mobius = annular_cover(n, {(n - 1, 0)})
        cylinder = annular_cover(n, set())
        assert poly_decider_matches_exhaustive(mobius)
        assert poly_decider_matches_exhaustive(cylinder)
        # spell it out: Mobius obstructed, cylinder not.
        assert annular_class_obstructed(mobius) is True
        assert (not transition_is_coboundary(mobius)) is True
        assert annular_class_obstructed(cylinder) is False
        assert transition_is_coboundary(cylinder) is True


def test_cycle_parity_is_z2_image_of_loop_sign():
    """The wrap-cycle Z2 parity is the Z2 image of the loop sign-product:
    parity 1 <-> loop sign -1, parity 0 <-> loop sign +1."""
    mobius = annular_cover(8, {(7, 0)})
    cylinder = annular_cover(8, set())
    assert annular_cycle_parity(mobius) == 1 and monodromy_sign(mobius) == -1
    assert annular_cycle_parity(cylinder) == 0 and monodromy_sign(cylinder) == 1


# --- The subdivision is a genuine refinement -------------------------------


def test_subdivision_doubles_the_cover():
    """annular_4 -> annular_8: patch count and edge count both double, so the
    refinement is non-trivial (not the identity cover)."""
    coarse, fine, _ = subdivide_annular(4, {(3, 0)})
    assert len(coarse.opens) == 4
    assert len(fine.opens) == 8
    assert len(coarse.overlaps) == 4
    assert len(fine.overlaps) == 8


def test_vertex_map_sends_both_halves_to_parent():
    """pi(2i)=pi(2i+1)=i: each coarse patch's two halves map to it."""
    _, _, ref = subdivide_annular(4, {(3, 0)})
    for i in range(4):
        assert ref.vertex_map[2 * i] == i
        assert ref.vertex_map[2 * i + 1] == i


def test_simplicial_map_is_valid():
    """The refinement map carries 1-simplices to 1-simplices (or collapses them
    inside a 0-simplex), never to a non-existent coarse overlap."""
    for reversed_edges in ({(3, 0)}, set()):
        _, _, ref = subdivide_annular(4, reversed_edges)
        assert vertex_map_respects_containment(ref)


def test_pullback_cochain_consistency():
    """The fine transition cochain equals the pullback pi^* of the coarse
    transition cochain along the refinement map (0 on collapsed intra edges)."""
    for reversed_edges in ({(3, 0)}, set()):
        _, _, ref = subdivide_annular(4, reversed_edges)
        assert pullback_is_consistent(ref)


def test_intra_edges_carry_no_reversal():
    """Fine edges whose endpoints map to the same coarse patch (the split-seam
    overlaps) carry transition 0 by construction."""
    _, fine, ref = subdivide_annular(4, {(3, 0)})
    intra = [e for e, img in ref.edge_image.items() if img is None]
    assert intra, "subdivision must create intra (split-seam) edges"
    for e in intra:
        assert fine.transition[e] == 0


def test_inter_edges_inherit_coarse_transition():
    """Fine edges crossing between coarse patches inherit the coarse edge's
    transition; exactly one inter edge carries the Mobius reversal."""
    coarse, fine, ref = subdivide_annular(4, {(3, 0)})
    inter = {e: img for e, img in ref.edge_image.items() if img is not None}
    assert inter, "subdivision must create inter (patch-crossing) edges"
    reversed_inter = [e for e, img in inter.items() if coarse.transition[img] == 1]
    assert len(reversed_inter) == 1
    assert fine.transition[reversed_inter[0]] == 1


# --- Loop sign is preserved under subdivision ------------------------------


def test_mobius_loop_sign_minus_one_at_every_scale():
    coarse, fine, _ = subdivide_annular(4, {(3, 0)})
    assert monodromy_sign(coarse) == -1
    assert monodromy_sign(fine) == -1


def test_cylinder_loop_sign_plus_one_at_every_scale():
    coarse, fine, _ = subdivide_annular(4, set())
    assert monodromy_sign(coarse) == 1
    assert monodromy_sign(fine) == 1


# --- The H1 class verdict is refinement-stable -----------------------------


def test_mobius_class_nontrivial_preserved_one_step():
    """annular_4 -> annular_8: [g] != 0 (no global section) on both, preserved."""
    step = refinement_step(4, {(3, 0)})
    assert step.coarse_obstructed is True
    assert step.fine_obstructed is True
    assert step.class_verdict_preserved is True
    assert step.loop_sign_preserved is True
    assert step.stable is True


def test_cylinder_class_trivial_preserved_one_step():
    """annular_4 -> annular_8: [g] = 0 (global section exists) on both, preserved."""
    step = refinement_step(4, set())
    assert step.coarse_obstructed is False
    assert step.fine_obstructed is False
    assert step.class_verdict_preserved is True
    assert step.loop_sign_preserved is True
    assert step.stable is True


def test_mobius_directed_chain_all_steps_stable():
    """annular_4 -> annular_8 -> annular_16: nontrivial class + loop sign -1
    preserved at every step of the directed refinement chain."""
    steps = refinement_chain(4, {(3, 0)}, depth=3)
    assert len(steps) == 3
    sizes = [(s.coarse_n, s.fine_n) for s in steps]
    assert sizes == [(4, 8), (8, 16), (16, 32)]
    for s in steps:
        assert s.coarse_obstructed and s.fine_obstructed
        assert s.coarse_loop_sign == -1 and s.fine_loop_sign == -1
        assert s.stable


def test_cylinder_directed_chain_all_steps_stable():
    steps = refinement_chain(4, set(), depth=3)
    assert len(steps) == 3
    for s in steps:
        assert (not s.coarse_obstructed) and (not s.fine_obstructed)
        assert s.coarse_loop_sign == 1 and s.fine_loop_sign == 1
        assert s.stable


def test_class_verdict_matches_direct_h1_on_fine_cover():
    """The refinement step's fine verdict matches a direct H1 computation on the
    independently-rebuilt fine cover (the step is not fabricating the verdict)."""
    coarse, fine, _ = subdivide_annular(4, {(3, 0)})
    direct = h1_verdict(fine, "annular_8_direct")
    step = refinement_step(4, {(3, 0)})
    assert step.fine_obstructed == (not direct.coefficient_aware_class_trivial)


# --- Top-level certificate -------------------------------------------------


def test_run_t231_analysis_conditional_and_stable():
    res = run_t231_analysis(depth=3)
    assert res.verdict == "conditional"
    assert res.mobius_class_refinement_stable is True
    assert res.cylinder_class_refinement_stable is True
    assert res.mobius_loop_sign_invariant is True
    assert res.cylinder_loop_sign_invariant is True
    assert res.all_steps_stable is True


def test_summary_states_finite_witness_not_continuum_theorem():
    """Honesty guard is encoded in the artifact: the summary must disclaim a
    general continuum cohomology theorem and tag finite_witness."""
    res = run_t231_analysis(depth=2)
    s = res.summary.lower()
    assert "finite_witness" in s
    assert "not a general continuum sheaf-cohomology theorem" in s
    assert "preserved" in s
