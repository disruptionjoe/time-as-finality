"""T242 tests: legality-closed filtered composition + totality of gr.

Real assertion-backed checks for `models/d1filtered_compose_meet.py`. Every test
is a genuine check of a decision branch, no placeholders. The sibling T232/T228/
T237 suite is NOT touched here (imported by import only).

Decision branches verified:
  (A) chain variant: legal on the breaking witness BUT non-associative -> NO-GO.
  (B) semilattice variant: legal + associative + unital + extends filtered on
      nested -> TOTAL category (codomain changed from chains to meet-semilattices).
  (B') gr is a TOTAL but GENUINELY LAX functor on the semilattice category.
  honesty guards: non-circular mu; non-monotone rejected; antichain is the exact
      structural reason chains fail.
"""

from __future__ import annotations

import pytest

from models.d1_restriction_system import D1_DIMENSIONS
from models.d1cat_filtered_colimit import (
    compose_filtered,
    filtered_equal,
    filtration_is_legal,
    make_filtered_identity,
)
from models.d1filtered_compose_meet import (
    _base,
    _endo,
    _from_chain,
    _has_antichain,
    _sl_dropped,
    _sl_eq,
    _two,
    _witnesses,
    chain_variant_is_non_associative,
    chain_variant_legal_on_breaking_witness,
    compose_meet_chain,
    compose_meet_semilattice,
    gr_semilattice,
    gr_total_functor_battery,
    honesty_boundary,
    make_semilattice_identity,
    meet_closure_has_antichain,
    meet_closure_set,
    mu_is_not_a_copy_of_compose_code,
    run_decision,
    semilattice_extends_filtered_on_nested,
    semilattice_identity_laws,
    semilattice_is_associative,
    semilattice_legal_on_breaking_witness,
)
from models.d1filtered_graded_functor import gr, graded_bottom, graded_dropped, mu


# ---------------------------------------------------------------------------
# Combinatorial core: the meet-closure of two chains is a poset w/ an antichain
# ---------------------------------------------------------------------------


def test_meet_closure_of_breaking_witness_has_antichain():
    """THE structural reason a chain-valued total composition is impossible:
    the meet-closure of f:4|-{a,h,b} and g:4|-{h,r} contains the INCOMPARABLE
    pair {a,h,b} vs {h,r}. A filtration is a chain, so this cannot be a filtration."""
    w = _witnesses()
    f, g = w["f_break"], w["g_break"]
    assert meet_closure_has_antichain(f.filtration, g.filtration) is True
    S = meet_closure_set(f.filtration, g.filtration)
    ahb = frozenset(("accessible_support", "holder_redundancy", "branch_support"))
    hr = frozenset(("holder_redundancy", "reversal_cost"))
    assert ahb in S and hr in S
    assert not (ahb <= hr or hr <= ahb)  # genuinely incomparable


def test_meet_closure_of_nested_pair_is_a_chain():
    """On nested inputs the meet-closure is totally ordered (no antichain), so the
    semilattice composite IS a chain there."""
    w = _witnesses()
    assert meet_closure_has_antichain(w["f_nest"].filtration, w["g_nest"].filtration) is False


# ---------------------------------------------------------------------------
# (A) chain variant: legal on the breaking witness, but NON-ASSOCIATIVE
# ---------------------------------------------------------------------------


def test_chain_variant_legal_where_compose_filtered_is_not():
    rep = chain_variant_legal_on_breaking_witness()
    assert rep["inputs_legal"] is True
    assert rep["compose_filtered_illegal"] is True  # the original obstruction
    assert rep["chain_variant_legal"] is True  # repair is legal...
    assert rep["chain_variant_descending"] is True
    assert rep["meet_closure_has_antichain"] is True


def test_chain_variant_is_non_associative_NO_GO():
    """...but legality is bought at the cost of associativity: forcing a chain out
    of the antichain-containing closure is bracketing-dependent. This is the recorded
    NO-GO for a chain-valued total category."""
    rep = chain_variant_is_non_associative()
    assert rep["chain_variant_non_associative"] is True
    # the explicit counterexample triple (break;break;nested) must disagree
    bad = [t for t in rep["witness_triples"] if t["label"] == "break_then_nested"][0]
    assert bad["associative"] is False
    assert bad["both_legal"] is True  # both bracketings ARE legal, just unequal
    assert bad["left_filtration"] != bad["right_filtration"]
    # control: the all-nested triple still composes associatively as a chain
    ctrl = [t for t in rep["witness_triples"] if t["label"] == "nested_control"][0]
    assert ctrl["associative"] is True


def test_chain_variant_explicit_bracketing_counterexample():
    """Hard-pin the exact divergence so the no-go cannot silently regress."""
    w = _witnesses()
    f, g, h = w["f_break"], w["g_break"], w["h_nest"]
    left = compose_meet_chain(compose_meet_chain(f, g), h)
    right = compose_meet_chain(f, compose_meet_chain(g, h))
    assert left.is_legal() and right.is_legal()
    assert not filtered_equal(left, right)


# ---------------------------------------------------------------------------
# (B) semilattice variant: legal + associative + unital + extends filtered
# ---------------------------------------------------------------------------


def test_semilattice_legal_on_breaking_witness():
    rep = semilattice_legal_on_breaking_witness()
    assert rep["embed_inputs_legal"] is True
    assert rep["semilattice_composite_legal"] is True
    assert rep["composite_has_antichain"] is True  # genuine poset, not a chain
    assert rep["second_non_nested_legal"] is True


def test_semilattice_is_associative_on_non_nested_triples():
    """The meet-closure is bracketing-independent, so the semilattice composition
    IS associative -- including on the very triples that break the chain variant."""
    rep = semilattice_is_associative()
    assert rep["all_associative"] is True
    # specifically the chain-variant-breaking triple is now associative
    brk = [t for t in rep["triples"] if t["label"] == "break_then_nested"][0]
    assert brk["associative"] is True and brk["left_legal"] and brk["right_legal"]


def test_semilattice_identity_laws():
    rep = semilattice_identity_laws()
    assert rep["both"] is True
    assert rep["left_identity_law"] is True and rep["right_identity_law"] is True


def test_semilattice_extends_filtered_on_nested():
    """No regression: on filtration-nested pairs the semilattice composite's layer
    set equals compose_filtered's, and is itself a chain."""
    rep = semilattice_extends_filtered_on_nested()
    assert rep["all_agree_on_nested"] is True
    for d in rep["detail"]:
        assert d["agree"] is True
        assert d["old_legal"] is True


def test_semilattice_associativity_direct():
    """Direct triple check (not via the report) on the all-non-nested triple."""
    w = _witnesses()
    F, G, K = _from_chain(w["f_break"]), _from_chain(w["g_break"]), _from_chain(w["k_nn"])
    left = compose_meet_semilattice(compose_meet_semilattice(F, G), K)
    right = compose_meet_semilattice(F, compose_meet_semilattice(G, K))
    assert _sl_eq(left, right)
    assert left.is_legal() and right.is_legal()


# ---------------------------------------------------------------------------
# (B') gr is a TOTAL but GENUINELY LAX functor on the semilattice category
# ---------------------------------------------------------------------------


def test_gr_total_strict_on_nested_lax_on_non_nested():
    rep = gr_total_functor_battery()
    # strict where the composite is still a chain (old gr-composable subcategory)
    assert rep["nested_strict"] is True
    # total + comparison exists on the newly-legal non-nested pairs...
    assert rep["non_nested_comparison_exists"] is True
    # ...but NOT strict there (the antichain regrouping) -> genuinely lax
    assert rep["non_nested_strict"] is False
    assert rep["non_nested_any_antichain"] is True
    assert rep["totality_forces_lax"] is True


def test_gr_semilattice_agrees_with_mu_on_support_and_floor():
    """The lax comparison datum: gr_semilattice(f;g) and mu(gr f, gr g) drop the
    SAME dimensions and share the SAME surviving floor (so a comparison morphism
    exists), even though the strata are grouped differently."""
    w = _witnesses()
    F, G = _from_chain(w["f_break"]), _from_chain(w["g_break"])
    FG = compose_meet_semilattice(F, G)
    concat = mu(gr(w["f_break"]), gr(w["g_break"]))
    assert _sl_dropped(FG) == graded_dropped(concat)
    assert frozenset(FG.bottom) == frozenset(graded_bottom(concat))
    # full universe recovered (nothing lost), drops + floor partition the universe
    assert (_sl_dropped(FG) | frozenset(FG.bottom)) == frozenset(D1_DIMENSIONS)


def test_gr_semilattice_on_chain_coincides_with_associated_graded():
    """When the semilattice IS a chain (nested pair), gr_semilattice equals the
    T237 strict associated-graded (gr). Anchors the strict-where-chain claim."""
    w = _witnesses()
    F, G = _from_chain(w["f_nest"]), _from_chain(w["g_nest"])
    FG = compose_meet_semilattice(F, G)
    assert _has_antichain(FG.layers) is False
    # gr of the equivalent chain composite (compose_filtered is legal here)
    chain_fg = compose_filtered(w["f_nest"], w["g_nest"])
    assert gr_semilattice(FG) == gr(chain_fg)


# ---------------------------------------------------------------------------
# Honesty guards
# ---------------------------------------------------------------------------


def test_mu_is_not_a_copy_of_compose_code():
    """Non-circularity: mu (T237, schedule semantics) yields a CHAIN; the
    semilattice composite yields an antichain-containing POSET. They agree on support
    + floor but differ in structure -> impossible if mu copied the compose code."""
    rep = mu_is_not_a_copy_of_compose_code()
    assert rep["semilattice_has_antichain"] is True
    assert rep["structures_differ"] is True
    assert rep["same_dropped_support"] is True and rep["same_bottom"] is True
    assert rep["comparison_exists"] is True


def test_honesty_boundary_non_monotone_rejected():
    rep = honesty_boundary()
    assert rep["non_monotone_is_legal"] is False
    assert rep["gr_rejects_non_monotone"] is True
    assert rep["general_cocompleteness_still_open"] is True


def test_non_monotone_filtration_is_illegal_directly():
    pseudo = (D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS)  # re-adds a dim
    assert filtration_is_legal(pseudo) is False
    bad = _endo(_base(), pseudo, "bad")
    with pytest.raises(ValueError):
        gr(bad)


# ---------------------------------------------------------------------------
# Aggregate verdict
# ---------------------------------------------------------------------------


def test_aggregate_verdict_is_conditional_codomain_change():
    out = run_decision()
    s = out["summary"]
    assert s["chain_variant_verdict"] == "chain_variant_legal_but_non_associative_NO_GO"
    assert s["semilattice_total_category"] is True
    assert s["functor_verdict"] == "lax_total_functor_on_semilattice_category"
    assert s["gr_total_lax_on_semilattice"] is True
    assert s["mu_independent_of_compose_code"] is True
    assert s["general_cocompleteness_still_open"] is True
    assert s["top_line"] == "conditional_total_category_requires_codomain_change_gr_lax"


def test_sibling_imports_unbroken():
    """Smoke: imported sibling operations still behave (import-only contract)."""
    base = _base()
    idm = make_filtered_identity(base)
    assert idm.is_legal()
    f = _endo(base, _two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    assert compose_filtered(idm, f).is_legal()  # nested composite stays legal
    sl_id = make_semilattice_identity(base)
    assert sl_id.is_legal()
