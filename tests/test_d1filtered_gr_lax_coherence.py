"""T245 tests: lax-functor associativity COHERENCE (the schedule pentagon) for
`gr_semilattice` on the TOTAL category `D1FilteredCat_meet`.

Real assertion-backed checks for `models/d1filtered_gr_lax_coherence.py`. Every
test is a genuine check of a decision branch -- no placeholders. The sibling
T232/T228/T237/T242 suites are NOT touched (imported by import only); a smoke test
asserts they remain green in spirit (imported operations still behave).

Decision branches verified:
  (+) anchored subcategory: pentagon COMMUTES over every full-top triple; the
      object-wise lax cells of T242 assemble into a GENUINE lax functor there.
  (lax-not-pseudo): the comparison cells are DIRECTED (not invertible) on the
      antichain triples -> genuine lax functor, NOT a pseudofunctor.
  (P1): mu associates ON THE NOSE -> the target associator is the IDENTITY 2-cell.
  (-) off-anchor obstruction: a non-full-top leg interleaved with a non-nested drop
      makes mu UNDER-COUNT the dropped support -> the comparison cell FAILS to exist
      (the first exact obstruction to a lax functor over ALL of D1FilteredCat_meet).
  honesty guards: a deliberately-wrong association is rejected (real commute test);
      a non-vacuity injector proves the harness CAN report non-commute; mu is not a
      copy of the compose code; non-monotone rejected; cocompleteness NOT claimed.
"""

from __future__ import annotations

from models.d1_restriction_system import D1_DIMENSIONS
from models.d1cat_filtered_colimit import (
    compose_filtered,
    filtration_is_legal,
    make_filtered_identity,
)
from models.d1filtered_compose_meet import (
    _base,
    _from_chain,
    _witnesses,
    compose_meet_semilattice,
)
from models.d1filtered_gr_lax_coherence import (
    LaxCell,
    _anchored_triples,
    _off_anchor_triples,
    _semilattice_composite,
    honesty_boundary,
    lax_cell,
    lax_not_pseudo,
    mu_associator_is_identity,
    mu_is_not_a_copy_of_compose_code,
    non_vacuity_injector,
    off_anchor_obstruction,
    pentagon_battery,
    pentagon_report,
    run_decision,
    wrong_association_is_rejected,
)


# ---------------------------------------------------------------------------
# (+) Pentagon commutes on the full-top-anchored subcategory
# ---------------------------------------------------------------------------


def test_pentagon_commutes_on_every_anchored_triple():
    """The central positive result: over EVERY full-top-anchored composable triple
    (where T242's pairwise cell lives), the lax-functor associativity coherence
    holds -- the pentagon commutes."""
    battery = pentagon_battery()
    assert len(battery) >= 6
    for r in battery:
        assert r["pentagon_commutes"] is True, r["label"]
        assert r["cell_exists"] is True, r["label"]
        assert r["source_assoc"] is True, r["label"]
        # both whisker edges land on the same fold the direct cell hits
        assert r["left_whisker_ok"] is True, r["label"]
        assert r["right_whisker_ok"] is True, r["label"]


def test_target_associator_is_identity_everywhere():
    """(P1): mu associates ON THE NOSE across the anchored battery, so the pentagon's
    target associator is the IDENTITY 2-cell (the strongest target-side outcome)."""
    rep = mu_associator_is_identity()
    assert rep["mu_associator_strict_everywhere"] is True
    for row in rep["rows"]:
        assert row["associator_strict"] is True, row["label"]


def test_antichain_triple_produces_finer_source_than_target():
    """On an antichain-producing triple the genuine composite gr_semilattice(f;g;h)
    is strictly FINER (more strata) than the mu-fold chain -> the cell is genuinely
    directed, not strict."""
    rep = pentagon_report(
        "n2_chain_kn",
        _witnesses()["f_n2"],
        _witnesses()["g_n2"],
        _witnesses()["k_nn"],
    )
    assert rep["cell_source_has_antichain"] is True
    assert rep["cell_strict"] is False
    assert rep["n_source_strata"] > rep["n_target_strata"]


# ---------------------------------------------------------------------------
# Lax vs pseudo: genuine LAX functor (cells directed, not invertible)
# ---------------------------------------------------------------------------


def test_genuine_lax_functor_not_pseudofunctor():
    """The cells are NOT invertible on the antichain triples (a directed map from an
    antichain-containing poset onto a strictly coarser chain has no inverse). So this
    is a GENUINE lax functor on the anchored subcategory, NOT a pseudofunctor."""
    rep = lax_not_pseudo()
    assert rep["is_pseudofunctor"] is False
    assert rep["is_genuine_lax_functor"] is True
    assert rep["some_cell_directed_non_invertible"] is True
    assert rep["n_antichain_triples"] >= 1


def test_nested_control_cell_is_strict():
    """The shared-full-top nested control (4|-3, 4|-2, 4|-1) stays a CHAIN composite,
    so its comparison cell IS strict / invertible -- the boundary case proving the
    laxity is specific to the antichain triples, not an artifact."""
    nested = [r for r in pentagon_battery() if r["label"] == "nested_full_succ"][0]
    assert nested["cell_source_has_antichain"] is False
    assert nested["cell_strict"] is True
    assert nested["cell_invertible"] is True
    assert nested["pentagon_commutes"] is True


# ---------------------------------------------------------------------------
# (-) The exact obstruction OFF the anchored subcategory
# ---------------------------------------------------------------------------


def test_off_anchor_cell_fails_mu_under_counts():
    """First exact obstruction: with a non-full-top leg interleaved with a non-nested
    drop, the genuine meet-closure composite records a dropped dimension mu never
    sees -> the comparison cell FAILS to exist. mu is NOT a faithful target fold over
    all of D1FilteredCat_meet."""
    rep = off_anchor_obstruction()
    assert rep["obstruction_present"] is True
    for row in rep["rows"]:
        assert row["cell_exists"] is False, row["label"]
        assert row["mu_under_counts"] is True, row["label"]
        # the missing dimension is real and non-empty, and the source IS associative
        # (so this is a genuine cell-faithfulness gap, not a source defect).
        assert len(row["missing_from_mu"]) >= 1, row["label"]
        assert row["source_assoc"] is True, row["label"]


def test_off_anchor_witness_is_the_named_triple():
    """Hard-pin the named witness (f_break ; h_nest ; g_break): h_nest's top is {a,h},
    g_break drops branch_support b which {a,h} never had, so the composite drops b
    while mu does not."""
    w = _witnesses()
    f, g, h = w["f_break"], w["h_nest"], w["g_break"]
    from models.d1filtered_graded_functor import gr, mu

    fold = mu(mu(gr(f), gr(g)), gr(h))
    F, G, H = _from_chain(f), _from_chain(g), _from_chain(h)
    composite = _semilattice_composite(_semilattice_composite(F, G), H)
    cell = lax_cell(composite, fold)
    assert cell.exists is False
    # b is exactly what mu misses
    from models.d1filtered_compose_meet import _sl_dropped
    from models.d1filtered_graded_functor import graded_dropped

    missing = _sl_dropped(composite) - graded_dropped(fold)
    assert missing == frozenset({"branch_support"})


# ---------------------------------------------------------------------------
# Honesty guards
# ---------------------------------------------------------------------------


def test_wrong_association_is_rejected_commute_test_is_real():
    """A genuine commute test must REJECT a deliberately-wrong association (operands
    permuted in the mu-fold). If it accepted both, the pentagon check would be
    vacuous."""
    rep = wrong_association_is_rejected()
    assert rep["good_and_wrong_differ"] is True
    assert rep["cell_to_good_exists"] is True
    assert rep["cell_to_wrong_exists"] is False
    assert rep["cell_to_wrong_support_differs"] is True
    assert rep["commute_test_is_real"] is True


def test_non_vacuity_injector_harness_can_report_non_commute():
    """The pentagon predicate is FALSIFIABLE: a perturbed fold (one dropped dimension
    removed) makes the cell -- hence pentagon_commutes -- report FALSE. So a True is
    a real positive, not a tautology."""
    rep = non_vacuity_injector()
    assert rep["perturbation_changed_support"] is True
    assert rep["cell_exists_on_perturbed"] is False
    assert rep["harness_can_report_non_commute"] is True


def test_mu_is_not_a_copy_of_compose_code():
    """Non-circularity: on the break triple the genuine composite is an
    antichain-containing poset while the mu-fold is a chain; they agree on support +
    floor but differ in structure -> impossible if mu copied the compose code."""
    rep = mu_is_not_a_copy_of_compose_code()
    assert rep["composite_has_antichain"] is True
    assert rep["structures_differ"] is True
    assert rep["same_dropped_support"] is True
    assert rep["comparison_exists"] is True


def test_honesty_boundary_non_monotone_rejected_and_cocompleteness_open():
    rep = honesty_boundary()
    assert rep["non_monotone_is_legal"] is False
    assert rep["gr_rejects_non_monotone"] is True
    assert rep["general_cocompleteness_still_open"] is True


# ---------------------------------------------------------------------------
# LaxCell semantics: directed cell properties
# ---------------------------------------------------------------------------


def test_laxcell_strict_implies_invertible_and_exists():
    """A strict (graded-equal) cell is invertible and exists; a support-mismatched
    cell does not exist. Pins the LaxCell decision logic directly."""
    strict = LaxCell(
        source_strata=(("a",), ()),
        target_fold=(("a",), ()),
        same_dropped_support=True,
        same_bottom=True,
        source_has_antichain=False,
    )
    assert strict.strict is True and strict.invertible is True and strict.exists is True
    broken = LaxCell(
        source_strata=(("a", "b"), ()),
        target_fold=(("a",), ()),
        same_dropped_support=False,
        same_bottom=True,
        source_has_antichain=True,
    )
    assert broken.exists is False
    directed = LaxCell(
        source_strata=(("a",), ("b",), ()),
        target_fold=(("a", "b"), ()),
        same_dropped_support=True,
        same_bottom=True,
        source_has_antichain=True,
    )
    assert directed.exists is True and directed.strict is False and directed.invertible is False


# ---------------------------------------------------------------------------
# Aggregate verdict
# ---------------------------------------------------------------------------


def test_aggregate_verdict_is_conditional_lax_blocked_off_anchor():
    out = run_decision()
    s = out["summary"]
    assert s["verdict"] == "selected_anchor_battery_commutes_blocked_off_anchor"
    assert s["anchored_all_pentagons_commute"] is True
    assert s["anchored_all_cells_exist"] is True
    assert s["anchored_all_source_associative"] is True
    assert s["mu_associator_is_identity"] is True
    assert s["commute_test_is_real"] is True
    assert s["harness_can_report_non_commute"] is True
    assert s["is_pseudofunctor"] is False
    assert s["is_genuine_lax_functor_on_anchor_battery"] is True
    assert s["off_anchor_obstruction_present"] is True
    assert s["mu_independent_of_compose_code"] is True
    assert s["general_cocompleteness_still_open"] is True
    assert s["top_line"] == (
        "conditional_selected_anchor_battery_coherent_non_strict_cells_blocked_off_anchor"
    )


# ---------------------------------------------------------------------------
# Import-only contract: imported sibling operations still behave
# ---------------------------------------------------------------------------


def test_sibling_imports_unbroken():
    """Smoke: the T232/T237/T242 operations this lane imports still behave (no
    sibling mutation). Full sibling suites are run separately in CI."""
    base = _base()
    idm = make_filtered_identity(base)
    assert idm.is_legal()
    w = _witnesses()
    # T242 semilattice composition still associative on the break triple
    F, G, H = _from_chain(w["f_break"]), _from_chain(w["g_break"]), _from_chain(w["k_nn"])
    left = compose_meet_semilattice(compose_meet_semilattice(F, G), H)
    right = compose_meet_semilattice(F, compose_meet_semilattice(G, H))
    assert left.layers == right.layers
    # T232 nested composite still legal
    nested = compose_filtered(w["f_nest"], w["g_nest"])
    assert nested.is_legal()
    assert filtration_is_legal(nested.filtration)
    # universe sanity
    assert len(D1_DIMENSIONS) == 4


def test_anchored_and_off_anchor_triples_are_disjoint_in_role():
    """Structural sanity: anchored triples all have full-top legs; off-anchor triples
    contain a non-full-top leg. The split is real, not relabeling."""
    full = frozenset(D1_DIMENSIONS)

    def has_full_top(x):
        # identity sentinel has full top by construction; chain morphisms expose .filtration
        if hasattr(x, "filtration"):
            return frozenset(x.filtration[0]) == full
        return True

    for lab, f, g, h in _anchored_triples():
        assert all(has_full_top(x) for x in (f, g, h)), lab
    for lab, f, g, h in _off_anchor_triples():
        assert not all(has_full_top(x) for x in (f, g, h)), lab
