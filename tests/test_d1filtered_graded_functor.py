"""T237 tests: functoriality of gr: D1FilteredCat -> GradedSets.

Real assertion-backed checks (no placeholders) over the fixed 4-element
dimension universe. Decides whether the associated-graded drop-schedule map gr is
a (strict / lax / partial) functor under filtered composition.

Run:
    python -m pytest tests/test_d1filtered_graded_functor.py -q
"""

from __future__ import annotations

import json

from models.d1_restriction_system import D1_DIMENSIONS, SiteMap
from models.d1cat_filtered_colimit import (
    D1FilteredMorphism,
    associated_graded,
    compose_filtered,
    make_filtered_identity,
    _one_site_system,
    _normalize_layer,
)
from models.d1filtered_graded_functor import (
    GradedComparison,
    graded_bottom,
    graded_comparison,
    graded_dropped,
    graded_equal,
    graded_identity,
    graded_support,
    gr,
    gr_composable,
    gr_on_object,
    gr_preserves_identity,
    chain_associativity_report,
    honesty_boundary_report,
    mu,
    run_decision,
)


def _base():
    return _one_site_system("X", (1, 1, 1, 1))


def _endo(filt, name):
    base = _base()
    return D1FilteredMorphism(
        name=name,
        source=base,
        target=base,
        site_map=tuple(SiteMap(s, s) for s in base.site_ids()),
        filtration=filt,
    )


def _two(top, bot):
    return (_normalize_layer(top), _normalize_layer(bot))


# ---------------------------------------------------------------------------
# gr on objects + morphisms is well-defined
# ---------------------------------------------------------------------------


def test_gr_on_object_returns_carrier_label():
    base = _base()
    assert gr_on_object(base) == base.name


def test_gr_on_morphism_is_the_associated_graded():
    """gr(m) is EXACTLY T232's associated_graded(m.filtration) -- the content the
    filtered colimit was shown to carry. Same value, by construction."""
    m = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:2]), "m")
    assert gr(m) == associated_graded(m.filtration)


def test_gr_records_drop_schedule_strata():
    """A 4->2 drop records dropping the bottom two dimensions, floor = {a,h}."""
    m = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:2]), "m")
    g = gr(m)
    assert graded_dropped(g) == {D1_DIMENSIONS[2], D1_DIMENSIONS[3]}
    assert set(graded_bottom(g)) == {D1_DIMENSIONS[0], D1_DIMENSIONS[1]}
    # support = everything mentioned = the full universe
    assert graded_support(g) == frozenset(D1_DIMENSIONS)


# ---------------------------------------------------------------------------
# Functor law 1: identity preservation  gr(id) == id_gr
# ---------------------------------------------------------------------------


def test_identity_law_holds():
    out = gr_preserves_identity()
    assert out["identity_law_holds"] is True
    assert out["identity_drops_nothing"] is True
    assert graded_equal(gr(make_filtered_identity(_base())), graded_identity())


def test_graded_identity_is_single_full_bottom_stratum():
    gid = graded_identity()
    assert len(gid) == 1
    assert set(gid[0]) == set(D1_DIMENSIONS)
    assert graded_dropped(gid) == frozenset()


# ---------------------------------------------------------------------------
# Functor law 2 (composition) on the gr-composable (nested) sub-domain: STRICT
# ---------------------------------------------------------------------------


def test_strict_composition_on_successive_nested_drops():
    """4->3 then 3->2: gr(f;g) equals the schedule concatenation mu(gr f, gr g),
    strictly. The classic two-stage descending case."""
    f = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    g = _endo(_two(D1_DIMENSIONS[:3], D1_DIMENSIONS[:2]), "g")
    assert gr_composable(f, g)
    fg = compose_filtered(f, g)
    assert graded_equal(gr(fg), mu(gr(f), gr(g)))


def test_strict_composition_with_shared_top_nested_bottoms():
    """f:4->3, g:4->2 (bottoms nested). Forces _refine_filtrations dedupe/re-sort;
    the schedule is still recovered strictly."""
    f = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    g = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:2]), "g")
    assert gr_composable(f, g)
    fg = compose_filtered(f, g)
    assert graded_equal(gr(fg), mu(gr(f), gr(g)))


def test_right_identity_reduces_to_gr_f():
    f = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    idm = make_filtered_identity(_base())
    fg = compose_filtered(f, idm)
    assert graded_equal(gr(fg), mu(gr(f), gr(idm)))
    # mu with identity on the right recovers gr(f)
    assert graded_equal(mu(gr(f), gr(idm)), gr(f))


def test_left_identity_reduces_to_gr_g():
    g = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:2]), "g")
    idm = make_filtered_identity(_base())
    fg = compose_filtered(idm, g)
    assert graded_equal(gr(fg), mu(gr(idm), gr(g)))
    assert graded_equal(mu(gr(idm), gr(g)), gr(g))


def test_no_loss_no_gain_on_every_composable_pair():
    """Across the whole composable battery, gr(f;g) records exactly the same set of
    dropped dimensions as the schedule concatenation -- nothing lost, nothing
    invented."""
    d = run_decision()
    for p in d["composition_battery"]:
        if p["composite_legal"]:
            assert p["no_loss_no_gain"] is True, p["label"]


def test_strict_everywhere_on_composable_subdomain():
    d = run_decision()
    composable = [p for p in d["composition_battery"] if p["composite_legal"]]
    assert len(composable) >= 5
    assert all(p["strict_equal"] for p in composable)
    assert all(p["comparison_exists"] for p in composable)


# ---------------------------------------------------------------------------
# Chain associativity (the T232 colimit witness, path-independence)
# ---------------------------------------------------------------------------


def test_chain_associativity_strict():
    c = chain_associativity_report()
    assert c["strict_equal"] is True
    assert c["comparison_exists"] is True
    assert c["same_dropped_support"] is True
    assert c["same_bottom"] is True
    assert c["full_recovers_universe"] is True


# ---------------------------------------------------------------------------
# THE OBSTRUCTION: compose_filtered is NOT closed on legal morphisms
# ---------------------------------------------------------------------------


def test_non_nested_composite_is_illegal_so_gr_undefined():
    """The first exact obstruction. f:4->{a,h,b} (drops r) and g:4->{h,r} (drops
    a,b) are each legal descending morphisms, but their filtrations are NON-NESTED
    ({a,h,b} and {h,r} are incomparable). compose_filtered re-sorts by size and
    yields a NON-descending composite -> an ILLEGAL morphism -> gr(f;g) UNDEFINED.
    So gr is NOT a functor on all of D1FilteredCat."""
    f = _endo(_two(D1_DIMENSIONS, ("accessible_support", "holder_redundancy", "branch_support")), "f")
    g = _endo(_two(D1_DIMENSIONS, ("holder_redundancy", "reversal_cost")), "g")
    assert f.is_legal() and g.is_legal()
    assert not gr_composable(f, g)
    fg = compose_filtered(f, g)
    assert fg.is_legal() is False
    # gr refuses the illegal composite (domain guard)
    try:
        gr(fg)
        raised = False
    except ValueError:
        raised = True
    assert raised is True


def test_obstruction_is_present_in_decision():
    d = run_decision()
    assert d["summary"]["obstruction_present"] is True
    assert d["summary"]["obstructed_pairs"] >= 1


def test_nested_pair_is_gr_composable():
    """Sanity counterpart: a properly nested pair IS gr-composable (composite stays
    descending), so the obstruction is specifically about NON-nesting, not about
    composition in general."""
    f = _endo(_two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    g = _endo(_two(D1_DIMENSIONS[:3], D1_DIMENSIONS[:1]), "g")
    assert gr_composable(f, g)
    assert compose_filtered(f, g).is_legal()


# ---------------------------------------------------------------------------
# GradedSets comparison morphism behaves as a thin-category refinement witness
# ---------------------------------------------------------------------------


def test_comparison_exists_iff_same_schedule():
    """The canonical comparison gr(f;g) -> mu exists iff the two gradings drop the
    same dimensions and share the same floor."""
    a = ((D1_DIMENSIONS[3],), (D1_DIMENSIONS[2],), tuple(_normalize_layer(D1_DIMENSIONS[:2])))
    # identical schedule, different grouping (merge first two drops)
    b = (tuple(_normalize_layer((D1_DIMENSIONS[2], D1_DIMENSIONS[3]))), tuple(_normalize_layer(D1_DIMENSIONS[:2])))
    cmp = graded_comparison(a, b)
    assert cmp.same_dropped_support is True
    assert cmp.same_bottom is True
    assert cmp.exists is True
    # but they are NOT strictly equal (different layering) -> lax, not strict
    assert cmp.strict is False


def test_comparison_absent_when_floor_differs():
    a = ((D1_DIMENSIONS[3],), tuple(_normalize_layer(D1_DIMENSIONS[:3])))  # floor {a,h,b}
    b = ((D1_DIMENSIONS[2],), tuple(_normalize_layer(D1_DIMENSIONS[:3])))  # drops b, floor differs
    cmp = graded_comparison(a, b)
    assert isinstance(cmp, GradedComparison)
    assert cmp.same_dropped_support is False
    assert cmp.exists is False


# ---------------------------------------------------------------------------
# Honesty guard: confined to monotone-descending; cocompleteness still open
# ---------------------------------------------------------------------------


def test_gr_rejects_non_monotone_filtration():
    out = honesty_boundary_report()
    assert out["non_monotone_is_legal"] is False
    assert out["gr_rejects_non_monotone"] is True
    assert out["functoriality_confined_to_descending"] is True
    assert out["general_cocompleteness_still_open"] is True


def test_gr_raises_on_illegal_filtration_directly():
    bad = _endo((D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS), "bad")  # re-adds a dim
    try:
        gr(bad)
        raised = False
    except ValueError:
        raised = True
    assert raised is True


# ---------------------------------------------------------------------------
# Aggregate verdict
# ---------------------------------------------------------------------------


def test_verdict_is_conditional_partial_functor():
    """The decision: identity law holds; STRICT on the gr-composable (nested)
    subcategory including the full T232 colimit chain; UNDEFINED off it because
    compose_filtered is not legality-closed. Hence a CONDITIONAL partial functor,
    not a total (strict) functor on all of D1FilteredCat."""
    d = run_decision()
    s = d["summary"]
    assert s["identity_law_holds"] is True
    assert s["strict_on_composable_subdomain"] is True
    assert s["no_loss_no_gain_on_composable"] is True
    assert s["comparisons_exist_on_composable"] is True
    assert s["obstruction_present"] is True
    assert s["verdict"] == "conditional_partial_functor"


def test_decision_payload_is_json_serializable():
    d = run_decision()
    json.dumps(d, default=str)  # must not raise
