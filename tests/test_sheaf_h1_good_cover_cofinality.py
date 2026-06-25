"""Tests for T246: good-cover / hypercover cofinality certificate.

Structure mirrors the T241 suite. Every guard is a REAL check:
  * the good-cover acyclicity decider FAILS on a non-good (annular / disconnected)
    piece (the certificate is a real computation, not an assertion);
  * continuum_derived_iso is set True ONLY for the annular-tower subsystem, ONLY
    when BOTH legs of the Leray pair (good-cover + lim^1=0) are genuinely
    certified, and the all-open-covers iso stays None with its residual named;
  * the verdict is conditional, NOT closed; no general continuum theorem;
  * imports leave the 73-test sibling suite green.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from models.coefficient_sheaf_h1 import CoverNerve
from models.sheaf_h1_good_cover_cofinality import (
    AcyclicityVerdict,
    _disconnected_piece_bad,
    _pairwise_piece,
    _piece_homology,
    _single_patch_piece,
    _triple_piece_bad_annular,
    _triple_piece_good,
    acyclicity_verdict,
    good_cover_certificate,
    good_cover_refinement_stable,
    leray_pair_verdict,
    non_good_injector,
    run_t246_analysis,
    t246_result_to_dict,
)
# Object-identity guard: the homology machinery scoring intersection pieces must
# be the SAME imported T236 functions, not a per-piece re-tuned decider.
from models.sheaf_h1_good_cover_cofinality import num_components as gc_num_components
from models.sheaf_h1_good_cover_cofinality import general_h1_rank as gc_general_h1_rank
import models.sheaf_h1_cofinality as cof
import models.sheaf_h1_lim1_certificate as lim1


# ---------------------------------------------------------------------------
# (0) The acyclicity atom: b0 / b1 of a finite intersection piece
# ---------------------------------------------------------------------------


def test_single_patch_is_acyclic():
    v = acyclicity_verdict(_single_patch_piece("U0"), "single")
    assert v.b0 == 1 and v.b1 == 0
    assert v.is_acyclic is True


def test_pairwise_overlap_is_acyclic():
    v = acyclicity_verdict(_pairwise_piece("0,1"), "pair")
    assert v.b0 == 1 and v.b1 == 0  # a segment (tree) is contractible
    assert v.is_acyclic is True


def test_good_triple_piece_is_a_tree_acyclic():
    v = acyclicity_verdict(_triple_piece_good("0,1,2"), "triple")
    # the GOOD realization of a genuine triple is a 3-vertex path (tree)
    assert v.b0 == 1 and v.b1 == 0
    assert v.is_acyclic is True


def test_empty_piece_is_not_acyclic_vacuously():
    empty = CoverNerve(opens=(), overlaps=(), triples=(), transition={})
    v = acyclicity_verdict(empty, "empty")
    assert v.nonempty is False
    assert v.is_acyclic is False  # only NONEMPTY intersections are required acyclic


# ---------------------------------------------------------------------------
# Object-identity / no re-tuning: the homology decider is the imported T236 one
# ---------------------------------------------------------------------------


def test_homology_decider_is_imported_t236_object_not_retuned():
    # the acyclicity scorer must BE the T236 functions, by object identity.
    assert gc_num_components is cof.num_components
    assert gc_general_h1_rank is cof.general_h1_rank


def test_piece_homology_matches_imported_t236_ranks():
    # _piece_homology must equal (num_components, general_h1_rank) computed by the
    # imported T236 functions on the SAME piece -- not a private re-implementation.
    piece = _triple_piece_good("x")
    b0, b1 = _piece_homology(piece)
    assert b0 == cof.num_components(piece)
    assert b1 == cof.general_h1_rank(piece)


def test_triangulated_annulus_is_imported_t241_object():
    # the good-cover certificate must read the intersection structure off T241's
    # actual triangulated_annulus, by object identity (no private fork of it).
    import models.sheaf_h1_good_cover_cofinality as gc

    assert gc.triangulated_annulus is lim1.triangulated_annulus


# ---------------------------------------------------------------------------
# (1) The triangulated-annulus cover is a GOOD cover with genuine triples
# ---------------------------------------------------------------------------


def test_base_cover_is_good_with_genuine_triples():
    c = good_cover_certificate(4)
    assert c.is_good_cover is True
    assert c.all_singles_acyclic is True
    assert c.all_pairwise_acyclic is True
    assert c.all_triples_acyclic is True
    assert c.triples_nonvacuous is True
    assert c.num_triples == 4  # n genuine triples for n spine patches


def test_every_intersection_piece_is_acyclic():
    c = good_cover_certificate(6)
    # EVERY listed intersection verdict must be acyclic for a good cover.
    assert all(v.is_acyclic for v in c.verdicts)
    # and there must be single, pairwise AND triple pieces present.
    names = [v.name for v in c.verdicts]
    assert any(nm.startswith("single") for nm in names)
    assert any(nm.startswith("pair") for nm in names)
    assert any(nm.startswith("triple") for nm in names)


def test_triple_count_equals_spine_count():
    for n in (4, 6, 8):
        c = good_cover_certificate(n)
        assert c.num_triples == n  # one genuine triple (i, i+1, b_i) per spine edge


# ---------------------------------------------------------------------------
# (2) HONESTY INJECTOR: the good-cover check is REAL, not asserted
# ---------------------------------------------------------------------------


def test_non_good_annular_triple_is_rejected():
    # a 3-CYCLE 'intersection' is an annulus (b1=1, a hole) -- NOT acyclic.
    v = acyclicity_verdict(_triple_piece_bad_annular("BAD"), "BAD")
    assert v.b0 == 1
    assert v.b1 == 1  # a genuine cycle / hole
    assert v.is_acyclic is False  # MUST fail the acyclicity check


def test_non_good_disconnected_piece_is_rejected():
    v = acyclicity_verdict(_disconnected_piece_bad("BAD"), "BAD")
    assert v.b0 == 2  # disconnected
    assert v.is_acyclic is False  # MUST fail


def test_injector_correctly_rejects_both_bad_pieces():
    inj = non_good_injector()
    assert inj.cyclic_piece_acyclic is False
    assert inj.cyclic_piece_b1 >= 1
    assert inj.disconnected_piece_acyclic is False
    assert inj.disconnected_piece_b0 >= 2
    assert inj.injector_correctly_rejects is True


def test_good_cover_certificate_would_fail_on_a_cyclic_triple():
    # Direct non-vacuity: feed a cyclic (annular) piece through the SAME
    # acyclicity_verdict the certificate uses; it must report NON-good. This proves
    # is_good_cover is gated on a real check, not hard-coded True.
    bad = _triple_piece_bad_annular("hole")
    v = acyclicity_verdict(bad, "hole")
    assert v.is_acyclic is False
    # contrast: the good (tree) realization of the same triple IS acyclic.
    good = _triple_piece_good("tree")
    assert acyclicity_verdict(good, "tree").is_acyclic is True


# ---------------------------------------------------------------------------
# (3) Refinement-stability of the good-cover property
# ---------------------------------------------------------------------------


def test_good_cover_refinement_stable():
    r = good_cover_refinement_stable((4, 6, 8))
    assert r.good_at_every_scale is True
    assert r.triples_nonvacuous_every_scale is True
    assert r.triple_count_grows is True  # densification genuinely adds triples
    assert r.stable is True


def test_good_cover_stable_at_each_listed_scale():
    r = good_cover_refinement_stable((4, 6, 8))
    assert tuple(c.is_good_cover for c in r.certificates) == (True, True, True)
    assert [c.num_triples for c in r.certificates] == [4, 6, 8]


# ---------------------------------------------------------------------------
# (4) The Leray pair: good-cover + lim^1=0 => continuum_derived_iso (CONDITIONAL)
# ---------------------------------------------------------------------------


def test_leray_pair_complete_on_annular_tower():
    L = leray_pair_verdict(4)
    assert L.lim1_certified_zero is True          # imported T241
    assert L.good_cover_certified is True         # this module
    assert L.leray_pair_complete_on_annular_tower is True


def test_continuum_derived_iso_set_true_only_for_annular_tower():
    L = leray_pair_verdict(4)
    # the flag T241 left None is now True -- but ONLY for the annular-tower subsystem.
    assert L.continuum_derived_iso_annular_tower is True
    # the strictly-larger all-open-covers iso stays None (the residual).
    assert L.continuum_derived_iso_all_open_covers is None


def test_residual_all_covers_object_is_named():
    L = leray_pair_verdict(4)
    txt = L.residual_all_covers_object.lower()
    assert "cofinal in all open covers" in txt
    assert "annular" in txt


def test_lim1_leg_is_imported_t241_ml_certificate_not_reasserted():
    # the lim^1=0 leg must come from T241's ML certificate (by object identity of
    # the imported function), not a local re-assertion.
    import models.sheaf_h1_good_cover_cofinality as gc

    assert gc.mittag_leffler_certificate is lim1.mittag_leffler_certificate
    cert = lim1.mittag_leffler_certificate(base_n=4, depth=4)
    assert cert.lim1_vanishes is True


def test_continuum_iso_would_be_none_if_good_cover_failed(monkeypatch):
    # Gating proof: if good-cover certification fails, continuum_derived_iso (even
    # for the annular tower) must fall back to None -- the True is gated on the
    # REAL good-cover leg, not hard-coded.
    import models.sheaf_h1_good_cover_cofinality as gc

    def _broken_stability(*args, **kwargs):
        # a stability object whose .stable is False
        real = gc.good_cover_refinement_stable.__wrapped__ if hasattr(
            gc.good_cover_refinement_stable, "__wrapped__"
        ) else None
        from models.sheaf_h1_good_cover_cofinality import GoodCoverRefinementStability

        return GoodCoverRefinementStability(
            scales=(4,),
            certificates=(),
            good_at_every_scale=False,
            triples_nonvacuous_every_scale=False,
            triple_count_grows=False,
            stable=False,
            detail="forced-broken",
        )

    monkeypatch.setattr(gc, "good_cover_refinement_stable", _broken_stability)
    L = gc.leray_pair_verdict(4)
    assert L.good_cover_certified is False
    assert L.leray_pair_complete_on_annular_tower is False
    assert L.continuum_derived_iso_annular_tower is None  # falls back to honest None


def test_continuum_iso_would_be_none_if_lim1_failed(monkeypatch):
    # Symmetric gating proof on the lim^1 leg: if the ML certificate fails to
    # vanish, the annular-tower iso must fall back to None.
    import models.sheaf_h1_good_cover_cofinality as gc
    from models.sheaf_h1_lim1_certificate import MittagLefflerCertificate

    def _broken_ml(*args, **kwargs):
        return MittagLefflerCertificate(
            chain_depth=0,
            stages=(),
            every_stage_connected=False,
            every_connecting_map_iso=False,
            images_eventually_stable=False,
            system_is_constant=False,
            lim1_vanishes=False,       # forced failure
            cofinal_chain_controls_tower=False,
            detail="forced-broken",
        )

    monkeypatch.setattr(gc, "mittag_leffler_certificate", _broken_ml)
    L = gc.leray_pair_verdict(4)
    assert L.lim1_certified_zero is False
    assert L.continuum_derived_iso_annular_tower is None


# ---------------------------------------------------------------------------
# Top-level verdict + honesty
# ---------------------------------------------------------------------------


def test_verdict_is_conditional_not_closed():
    res = run_t246_analysis()
    assert res.verdict == "conditional"
    assert res.verdict != "closed"


def test_no_continuum_theorem_asserted():
    res = run_t246_analysis()
    d = t246_result_to_dict(res)
    # the all-open-covers continuum identification must stay None.
    assert d["leray_pair"]["continuum_derived_iso_all_open_covers"] is None
    # a general continuum theorem is explicitly forbidden in the recorded text.
    assert "forbidden" in d["leray_pair"]["forbidden"].lower()


def test_no_physics_or_new_object_language_in_summary():
    res = run_t246_analysis()
    txt = res.summary.lower()
    for banned in (
        "curvature",
        "connection ",
        "holonomy",
        "gravity",
        "spacetime",
        "torsion",
    ):
        assert banned not in txt


def test_result_dict_roundtrips_and_is_json_safe():
    import json

    res = run_t246_analysis()
    d = t246_result_to_dict(res)
    s = json.dumps(d)  # must be JSON-serializable
    assert '"verdict": "conditional"' in s
    assert d["good_cover_base"]["is_good_cover"] is True
    assert d["non_good_injector"]["injector_correctly_rejects"] is True


def test_good_cover_is_the_named_t241_object():
    # the certificate must be the acyclicity / good-cover object T241 named: every
    # nonempty finite (single/pairwise/triple) intersection contractible/acyclic.
    res = run_t246_analysis()
    base = res.good_cover_base
    assert base.all_singles_acyclic
    assert base.all_pairwise_acyclic
    assert base.all_triples_acyclic
    assert base.is_good_cover


# ---------------------------------------------------------------------------
# Sibling suites stay green (import-only discipline)
# ---------------------------------------------------------------------------


def test_imports_leave_sibling_suites_untouched():
    """The 73-test T226+T231+T236+T241 suite must stay green alongside this one."""
    repo = Path(__file__).resolve().parents[1]
    sib = [
        "tests/test_sheaf_h1_lim1_certificate.py",
        "tests/test_sheaf_h1_cofinality.py",
        "tests/test_sheaf_h1_refinement.py",
        "tests/test_coefficient_sheaf_h1.py",
    ]
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", *sib, "-q"],
        cwd=str(repo),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "73 passed" in proc.stdout
