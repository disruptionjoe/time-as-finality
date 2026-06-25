"""Tests for T232: D1FilteredMorphism and the filtered (graded) colimit decision.

Real assertion checks of the categorical mechanics that decide whether the
content-bearing filtered colimit exists where T228's bare-intersection colimit
was content-free. No placeholders. Finite enumeration over the 4-element
dimension universe (poly_decider / finite_witness).
"""

from models.d1_restriction_system import D1_DIMENSIONS
from models.d1cat_filtered_colimit import (
    associated_graded,
    bare_intersection,
    build_filtered_descending_chain,
    chain_composite_filtration,
    compose_filtered,
    filtered_colimit_is_content_bearing,
    filtered_composition_is_associative,
    filtered_equal,
    filtered_identity_laws_hold,
    filtration_is_legal,
    forgetful_functor_lands_in_d1cat,
    general_cocompleteness_still_open,
    make_filtered_identity,
    non_monotone_pseudofiltration_is_illegal,
    run_decision,
    D1FilteredMorphism,
)
from models.d1_restriction_system import D1RestrictionSystem, LocalD1Value, SiteMap
from models.multiscale_observer_field import D1Profile, ObserverSite


def _base() -> D1RestrictionSystem:
    site = ObserverSite("s", "pop", "scale", 0, "trusted")
    value = LocalD1Value(site, "true", D1Profile(1, 1, 1, 1))
    return D1RestrictionSystem(
        name="base",
        proposition="p",
        local_values=(value,),
        transport_edges=(),
        source_site="s",
        target_site="s",
    )


# --- filtration typing ------------------------------------------------------


def test_descending_filtration_is_legal():
    assert filtration_is_legal((D1_DIMENSIONS, D1_DIMENSIONS[:2], ()))


def test_non_monotone_filtration_is_illegal():
    # Re-adding a dropped dimension breaks the descending typing.
    assert not filtration_is_legal((D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS))


def test_empty_filtration_is_illegal():
    assert not filtration_is_legal(())


def test_bare_intersection_is_bottom_of_filtration():
    assert bare_intersection((D1_DIMENSIONS, D1_DIMENSIONS[:2], D1_DIMENSIONS[:1])) == D1_DIMENSIONS[:1]
    assert bare_intersection((D1_DIMENSIONS, ())) == ()


# --- D1FilteredCat is a proper category ------------------------------------


def test_filtered_composition_is_associative():
    assert filtered_composition_is_associative()


def test_filtered_identity_laws_hold():
    assert filtered_identity_laws_hold()


def test_identity_is_legal_and_has_full_bare_intersection():
    idm = make_filtered_identity(_base())
    assert idm.is_legal()
    assert bare_intersection(idm.filtration) == D1_DIMENSIONS


def test_compose_filtered_stays_legal_and_descending():
    base = _base()
    f = D1FilteredMorphism("f", base, base, (SiteMap("s", "s"),), (D1_DIMENSIONS, D1_DIMENSIONS[:3]))
    g = D1FilteredMorphism("g", base, base, (SiteMap("s", "s"),), (D1_DIMENSIONS[:3], D1_DIMENSIONS[:1]))
    fg = compose_filtered(f, g)
    assert fg.is_legal()
    assert filtration_is_legal(fg.filtration)
    # Composite retains the schedule: top is full, bottom is the bare intersection.
    assert set(fg.filtration[0]) == set(D1_DIMENSIONS)
    assert bare_intersection(fg.filtration) == D1_DIMENSIONS[:1]


def test_filtered_equality_is_modulo_name():
    base = _base()
    a = D1FilteredMorphism("a", base, base, (SiteMap("s", "s"),), (D1_DIMENSIONS, ()))
    b = D1FilteredMorphism("DIFFERENT_NAME", base, base, (SiteMap("s", "s"),), (D1_DIMENSIONS, ()))
    assert filtered_equal(a, b)


# --- forgetful functor onto D1Cat (recovers T228's content-free colimit) ----


def test_forgetful_functor_lands_in_d1cat():
    assert forgetful_functor_lands_in_d1cat()


def test_forgetful_functor_recovers_bare_intersection_morphism():
    base = _base()
    m = D1FilteredMorphism("m", base, base, (SiteMap("s", "s"),), (D1_DIMENSIONS, D1_DIMENSIONS[:2], ()))
    u = m.to_d1cat_morphism()
    # U forgets the schedule and lands exactly on the empty bare intersection --
    # the content-free object T228 closed on.
    assert u.preserved_dimensions == ()


# --- THE DECISION: filtered colimit is content-bearing ----------------------


def test_chain_composite_filtration_is_the_full_descending_chain():
    chain = build_filtered_descending_chain(6)
    filt = chain_composite_filtration(chain)
    # Layers (by size) should descend 4,3,2,1,0 -- the whole drop schedule kept.
    sizes = [len(layer) for layer in filt]
    assert sizes == [4, 3, 2, 1, 0]
    assert filtration_is_legal(filt)


def test_associated_graded_recovers_drop_schedule():
    chain = build_filtered_descending_chain(6)
    filt = chain_composite_filtration(chain)
    gr = associated_graded(filt)
    # Four singleton drop strata (one dimension dropped per step) + empty bottom.
    drop_strata = gr[:-1]
    assert all(len(s) == 1 for s in drop_strata)
    assert len(drop_strata) == 4
    assert set(d for s in drop_strata for d in s) == set(D1_DIMENSIONS)
    assert gr[-1] == ()  # bottom stratum = bare intersection = empty


def test_filtered_colimit_is_content_bearing_where_bare_is_content_free():
    out = filtered_colimit_is_content_bearing()
    assert out["colimit_object_valid"] is True
    # T228 reading: the bare intersection is content-free.
    assert out["bare_is_content_free"] is True
    assert out["bare_intersection"] == ()
    # T232 reading: the filtered colimit IS content-bearing.
    assert out["filtered_is_content_bearing"] is True
    assert out["schedule_recovers_universe"] is True
    assert set(out["recovered_dropped_dims"]) == set(D1_DIMENSIONS)


# --- HONESTY GUARD: not general cocompleteness at infinity -------------------


def test_non_monotone_pseudofiltration_is_illegal():
    out = non_monotone_pseudofiltration_is_illegal()
    assert out["non_monotone_filtration_legal"] is False
    assert out["non_monotone_morphism_legal"] is False
    # The descending counterpart IS legal -- isolating monotonicity as the line.
    assert out["descending_counterpart_legal"] is True


def test_general_cocompleteness_is_explicitly_left_open():
    # The construction refuses non-descending diagrams, so it does NOT, by
    # itself, establish general cocompleteness at infinity.
    assert general_cocompleteness_still_open() is True


# --- aggregate payload ------------------------------------------------------


def test_run_decision_payload_is_consistent():
    payload = run_decision()
    assert payload["filtered_composition_associative"] is True
    assert payload["filtered_identity_laws"] is True
    assert payload["forgetful_functor_into_d1cat"] is True
    assert payload["colimit"]["filtered_is_content_bearing"] is True
    assert payload["colimit"]["bare_is_content_free"] is True
    assert payload["general_cocompleteness_still_open"] is True
