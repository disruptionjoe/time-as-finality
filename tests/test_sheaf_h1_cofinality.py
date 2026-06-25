"""T236 tests: full-poset cofinality + multi-cycle stability + Cech->derived step.

Real checks (no placeholders). Three groups:
  (A) general Z2 cycle-space cohomology decider correctness + cross-validation
      against T226's exhaustive 2^n coboundary search (the licensing condition
      for the poly_decider);
  (B) the wider staggered-refinement poset: class stability on every edge +
      cofinality of the uniform bisection;
  (C) the multi-cycle theta witness (H1 rank 2, four independent classes,
      refinement-stable) + the honest Cech->derived comparison (iso flag MUST be
      None, residual obstruction NAMED).

Imports T226/T231 BY IMPORT ONLY; modifies neither.
"""

from __future__ import annotations

from itertools import combinations

import pytest

from models.coefficient_sheaf_h1 import (
    annular_cover,
    monodromy_sign,
    transition_is_coboundary,
)
from models.sheaf_h1_refinement import (
    annular_class_obstructed,
    subdivide_annular,
)
from models.sheaf_h1_cofinality import (
    cech_derived_comparison,
    cofinality_certificate,
    general_class_obstructed,
    general_class_vector,
    general_decider_matches_exhaustive,
    general_h1_rank,
    num_components,
    poset_refinement_check,
    run_t236_analysis,
    spanning_forest,
    staggered_subdivide,
    theta_two_cycle,
)


# ---------------------------------------------------------------------------
# (A) General Z2 cycle-space cohomology decider
# ---------------------------------------------------------------------------


def test_betti_number_annular_is_one():
    """A single annular cover is one wrap cycle: b1 = 1."""
    nerve = annular_cover(5, set())
    assert general_h1_rank(nerve) == 1
    assert num_components(nerve) == 1


def test_betti_number_theta_is_two():
    """The theta (two-cycle) witness has H1 rank exactly 2."""
    for tl in (False, True):
        for tr in (False, True):
            assert general_h1_rank(theta_two_cycle(3, tl, tr)) == 2


def test_spanning_forest_partitions_edges():
    """tree + cotree partition the edges; #cotree == b1 for a connected nerve."""
    nerve = theta_two_cycle(3, True, False)
    tree, cotree = spanning_forest(nerve)
    assert len(tree) + len(cotree) == len(nerve.overlaps)
    assert set(tree).isdisjoint(set(cotree))
    assert len(cotree) == general_h1_rank(nerve) == 2


def test_general_decider_recovers_annular_wrap_parity():
    """On a single-cycle annular cover the general cycle-space decider must agree
    with T231's wrap-parity decider AND the loop sign (rank-1 specialization)."""
    for n in (3, 4, 5, 6):
        # cylinder (no twist): not obstructed, loop +1
        cyl = annular_cover(n, set())
        assert general_class_obstructed(cyl) is False
        assert general_class_obstructed(cyl) == annular_class_obstructed(cyl)
        assert (monodromy_sign(cyl) == -1) == general_class_obstructed(cyl)
        # mobius (one wrap twist): obstructed, loop -1
        mob = annular_cover(n, {(n - 1, 0)})
        assert general_class_obstructed(mob) is True
        assert general_class_obstructed(mob) == annular_class_obstructed(mob)
        assert (monodromy_sign(mob) == -1) == general_class_obstructed(mob)


def test_general_decider_cross_validates_against_exhaustive():
    """The poly cycle-space decider == not-a-coboundary (exhaustive 2^n) on every
    small witness. This is the condition that licenses the poly_decider."""
    nerves = []
    for n in (3, 4, 5):
        nerves.append(annular_cover(n, set()))
        nerves.append(annular_cover(n, {(n - 1, 0)}))
    for tl in (False, True):
        for tr in (False, True):
            nerves.append(theta_two_cycle(2, tl, tr))
    for nerve in nerves:
        assert general_decider_matches_exhaustive(nerve), nerve
        # and explicitly: obstructed iff not a coboundary
        assert general_class_obstructed(nerve) == (not transition_is_coboundary(nerve))


def test_even_twists_on_one_cycle_are_trivial():
    """Two reversals on the SAME wrap cycle cancel (Z2): class trivial, loop +1.
    Confirms the decider reads parity, not raw reversal count."""
    n = 6
    nerve = annular_cover(n, {(0, 1), (2, 3)})  # two reversals, even -> trivial
    assert general_class_obstructed(nerve) is False
    assert monodromy_sign(nerve) == 1


# ---------------------------------------------------------------------------
# (B) Wider staggered-refinement poset + cofinality
# ---------------------------------------------------------------------------


def test_staggered_refinement_is_genuine_and_single_cycle():
    """A staggered split of a subset S yields n+|S| patches, still one wrap cycle
    (b1 = 1), and is a real refinement (more patches than coarse)."""
    n = 4
    coarse = annular_cover(n, {(3, 0)})
    for r in range(n + 1):
        for S in combinations(range(n), r):
            S = frozenset(S)
            stag = staggered_subdivide(n, {(3, 0)}, S)
            assert len(stag.opens) == n + len(S)
            assert general_h1_rank(stag) == 1  # still a single annular cycle
            assert len(stag.opens) >= len(coarse.opens)


def test_class_stable_on_every_staggered_edge_mobius():
    """The obstructed-verdict and loop sign are invariant along EVERY refinement
    edge coarse -> staggered(S) for the Mobius witness (all 2^n subsets)."""
    n = 4
    coarse = annular_cover(n, {(3, 0)})
    assert general_class_obstructed(coarse) is True
    for r in range(n + 1):
        for S in combinations(range(n), r):
            stag = staggered_subdivide(n, {(3, 0)}, frozenset(S))
            chk = poset_refinement_check("t", coarse, stag)
            assert chk.class_preserved
            assert chk.loop_sign_preserved
            assert chk.stable
            assert general_class_obstructed(stag) is True  # stays obstructed
            assert monodromy_sign(stag) == -1


def test_class_stable_on_every_staggered_edge_cylinder():
    """Same, for the trivial (cylinder) witness: stays non-obstructed, loop +1."""
    n = 4
    for r in range(n + 1):
        for S in combinations(range(n), r):
            stag = staggered_subdivide(n, set(), frozenset(S))
            assert general_class_obstructed(stag) is False
            assert monodromy_sign(stag) == 1


def test_uniform_bisection_is_cofinal_in_wider_poset():
    """Cofinality certificate: every staggered cover is dominated by the uniform
    bisection, every poset edge is stable, and the chain value == poset value."""
    for n in (3, 4):
        for rev in (set(), {(n - 1, 0)}):
            cert, checks = cofinality_certificate(n, rev)
            assert cert.num_staggered_covers == 2 ** n
            assert cert.every_staggered_stable
            assert cert.uniform_dominates_every_staggered
            assert cert.chain_value_equals_poset_value
            assert cert.cofinal
            # every individual edge check is stable
            assert all(c.stable for c in checks)


def test_cofinality_value_matches_uniform_bisection_decider():
    """The colimit value taken over the wider poset equals the uniform-bisection
    value (T231's chain) -- cross-check against subdivide_annular directly."""
    n = 4
    rev = {(3, 0)}
    coarse = annular_cover(n, rev)
    _, uniform_fine, _ = subdivide_annular(n, rev)
    assert general_class_obstructed(coarse) == general_class_obstructed(uniform_fine)
    # and both equal the loop-sign verdict
    assert general_class_obstructed(coarse) == (monodromy_sign(coarse) == -1)


# ---------------------------------------------------------------------------
# (C) Multi-cycle theta witness + Cech->derived comparison
# ---------------------------------------------------------------------------


def test_theta_four_independent_classes():
    """The two cycles are independently twistable: the four configs give four
    DISTINCT class vectors, and exactly one (no-twist) is the zero class."""
    vecs = {
        (tl, tr): general_class_vector(theta_two_cycle(3, tl, tr))
        for tl in (False, True)
        for tr in (False, True)
    }
    assert len(set(vecs.values())) == 4  # all distinct -> genuine rank-2 freedom
    assert vecs[(False, False)] == (0, 0)  # no twist -> trivial class
    # any twist -> obstructed
    for (tl, tr), v in vecs.items():
        obstructed = (tl or tr)
        assert general_class_obstructed(theta_two_cycle(3, tl, tr)) == obstructed


def test_theta_class_vector_length_equals_rank():
    """The class vector length == H1 rank == 2 for every theta config."""
    for tl in (False, True):
        for tr in (False, True):
            v = general_class_vector(theta_two_cycle(3, tl, tr))
            assert len(v) == general_h1_rank(theta_two_cycle(3, tl, tr)) == 2


def test_theta_class_refinement_stable_all_configs():
    """Subdividing the theta arcs (longer chains) preserves the obstructed-verdict
    AND the multiset of fundamental-cycle parities, for all four twist configs."""
    for tl in (False, True):
        for tr in (False, True):
            coarse = theta_two_cycle(2, tl, tr)
            fine = theta_two_cycle(5, tl, tr)
            assert general_class_obstructed(coarse) == general_class_obstructed(fine)
            assert general_h1_rank(fine) == 2
            assert sorted(general_class_vector(coarse)) == sorted(
                general_class_vector(fine)
            )


def test_cech_derived_comparison_is_honestly_open():
    """The Cech->derived iso flag MUST be None (undecided from finite data); the
    finite identity holds; the residual obstruction names lim^1 / Mittag-Leffler."""
    cmp = cech_derived_comparison(4, {(3, 0)})
    assert cmp.finite_colimit_equals_cycle_space_h1 is True
    assert cmp.class_stable_along_cofinal_system is True
    # the binding honesty guard: NOT claimed to be an iso
    assert cmp.derived_comparison_is_iso is None
    assert "lim^1" in cmp.residual_obstruction or "Mittag-Leffler" in cmp.residual_obstruction
    assert "FORBIDDEN" in cmp.forbidden


# ---------------------------------------------------------------------------
# Top-level verdict
# ---------------------------------------------------------------------------


def test_t236_verdict_conditional():
    """Roll-up: conditional (positive but NOT closed) with all sub-certificates
    passing and the continuum theorem honestly left open."""
    res = run_t236_analysis()
    assert res.verdict == "conditional"
    assert res.theta_h1_rank == 2
    assert len(set(res.theta_class_vectors.values())) == 4
    assert res.theta_decider_cross_validated is True
    assert res.multi_cycle_refinement_stable is True
    assert res.cofinality.cofinal is True
    assert res.cofinality_cross_validated_vs_loop_sign is True
    assert res.comparison.derived_comparison_is_iso is None  # honest: not closed


def test_t236_not_closed_guard():
    """The verdict is never 'closed': a finite witness must not promote to a
    continuum theorem (binding honesty guard)."""
    res = run_t236_analysis()
    assert res.verdict != "closed"
    assert "FORBIDDEN" in res.comparison.forbidden
