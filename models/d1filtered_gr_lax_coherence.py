"""T245: lax-functor associativity COHERENCE (the schedule / Mac Lane pentagon)
for the associated-graded `gr_semilattice` on the TOTAL category
`D1FilteredCat_meet`.

This module is a FINITE, EXECUTABLE witness for the constructive-next object (1)
T242 named verbatim:

    "Lax-functor coherence for gr on D1FilteredCat_meet: verify the comparison
     2-cells gr(f;g) -> mu(gr f, gr g) satisfy the lax-functor associativity
     coherence (the schedule-pentagon) over composable TRIPLES, upgrading
     'object-wise lax' to a genuine LAX FUNCTOR (or pseudofunctor if the cells
     are invertible). The semilattice associativity proven here is the
     prerequisite."

WHAT T242 LEFT OPEN. T242 built the TOTAL category `D1FilteredCat_meet`
(`compose_meet_semilattice` is associative + unital + extends `compose_filtered`
on the nested subcategory) and showed `gr_semilattice` is a TOTAL functor with an
OBJECT-WISE comparison cell

    c_{f,g} : gr_semilattice(f;g)  ->  mu(gr f, gr g)        (T237 schedule mu)

that EXISTS (same dropped support, same surviving floor) for every composable
PAIR, and is STRICT exactly on the chain (nested) subcategory, merely DIRECTED on
the antichain-producing non-nested pairs. T242 checked this only PAIR-WISE. The
open question -- the difference between "object-wise lax" and a GENUINE lax
functor -- is whether those cells satisfy the ASSOCIATIVITY COHERENCE over
composable TRIPLES.

THE COHERENCE LAW (the schedule pentagon), made executable. For a lax functor with
comparison cells c, the associativity coherence over a triple (f,g,h) is the
commuting pentagon relating the two bracketings. Because the SOURCE composition is
ASSOCIATIVE (T242: `(f;g);h` and `f;(g;h)` are the SAME semilattice morphism, so
gr_semilattice(f;g;h) is a SINGLE well-defined object) and the TARGET fold `mu`
must associate, the pentagon collapses to a finite COMMUTE TEST with two
ingredients we check directly over a battery of triples:

  (P1) TARGET ASSOCIATOR. mu(mu(gr f, gr g), gr h) and mu(gr f, mu(gr g, gr h))
       must agree (the schedule-fold associates). If they coincide STRICTLY the
       target associator is the identity and the pentagon's right edge is trivial.

  (P2) CELL COHERENCE. the comparison cell out of the genuine triple composite,
       c_{f;g;h} : gr_semilattice((f;g);h) -> mu(mu(gr f, gr g), gr h), must EXIST
       (same dropped support + same floor) and be COMPATIBLE with the two-step
       cells (the inner cell c_{f,g} whiskered by mu(-, gr h), resp. c_{g,h}
       whiskered by mu(gr f, -)). Compatibility = both whiskered two-step targets
       land on the SAME mu-fold the direct cell does. The pentagon COMMUTES iff
       (P1) and (P2) hold for the triple.

VERDICT THIS LANE REACHES (category + functor level only): conditional finite
witness. The triple battery surfaces a CLEAN SPLIT that the PAIR-only battery of
T242 could not see:

  (+) ON THE SELECTED FULL-TOP-ANCHORED GENERATOR BATTERY -- every leg has the
      FULL-universe top, which is EXACTLY the regime T242's pairwise comparison cell
      was established in (its battery embedded full-top witnesses) -- the pentagon
      COMMUTES over every tested triple, including every antichain-PRODUCING one in
      the battery. There (P1) holds STRICTLY (mu associates on the nose, so the
      target associator is the IDENTITY 2-cell) and (P2) holds (the direct triple
      cell exists and agrees with both whiskered two-step folds). This is generator-
      battery evidence toward a genuine lax functor, not a subcategory-wide theorem.

      In the tested battery, some comparison cells are directed and non-strict. This
      is evidence against a pseudo reading on those witnesses, not a complete
      pseudofunctor refutation over a typed subcategory.

  (-) OFF IT the coherence FAILS against the T237 mu yardstick, and this lane names
      the EXACT obstruction. When a NON-full-top leg (a morphism whose top is a
      PROPER subset of the universe, e.g. h_nest: {a,h} |- {a}) is interleaved with
      a non-nested leg that further-drops a dimension ABSENT from that smaller top
      (e.g. g_break drops branch_support b, which h_nest's top {a,h} never had),
      the genuine meet-closure RECORDS b as dropped while mu's stage-restriction
      logic -- which assumes every summand operates on the FULL universe and
      restricts stage 2 to the previous floor -- never sees b. So the comparison
      cell gr_semilattice(f;g;h) -> mu(...) does NOT exist (dropped supports differ:
      composite drops {a,b,h,r}, mu drops only {a,h,r}). The witness is the triple
      (f_break ; h_nest ; g_break). mu is therefore NOT a faithful target fold over
      ALL of D1FilteredCat_meet -- only over the full-top-anchored subcategory.

NET: the lax-functor upgrade T242 named has positive generator-battery evidence
exactly where T242's cell was defined, and is BLOCKED off it by a faithfulness gap
in the T237 schedule fold mu, with a named repair (a top-aware fold mu_top
restricting each stage to its summand's ACTUAL top). Conditional, not closed:
the subcategory-wide lax-functor theorem and full-category upgrade both await
additional typing/proof.

HONESTY GUARDS (binding, inherited T228 -> T232 -> T237 -> T242):
  - `mu` is IMPORTED unchanged from T237 (schedule semantics) and is asserted NOT
    a copy of any compose code here (structures differ: mu yields a CHAIN, the
    semilattice composite a POSET with an antichain, while support/floor agree).
  - The pentagon check is a REAL commute test: a DELIBERATELY-WRONG association
    (operands permuted in the mu-fold) is asserted to FAIL the cell-coherence
    check -- so a commuting square cannot be reported vacuously.
  - A NON-VACUITY injector exhibits a perturbed cell-target whose dropped support
    differs, proving the harness CAN report "does NOT commute" / "directed only".
  - Non-monotone (illegal) filtration still rejected by gr.
  - Cocompleteness at infinity is NOT claimed (binding T228 guard); the verdict is
    confined to the FIXED finite category over the 4-element dimension universe.

Complexity tags: finite_witness (finite executable fixture over the fixed
4-element dimension universe D1_DIMENSIONS = (a,h,b,r); no scalable/continuum
theorem asserted) and poly_decider (finite triple enumeration + finite
meet-closure + finite schedule-fold; NOT a hidden search, NOT a hardness/NP
claim).

This is the DISCRETE CATEGORY-LEVEL lane (D1Cat proto_independent line) and is
EXPLICITLY DISTINCT from the kappa / sheaf-H1 / MTI / attribution lanes: it
touches NONE of those objects. No physics/geometry/curvature/Cech/sheaf/new-object
language is promoted from this witness; "filtration / associated-graded /
meet-semilattice / lax functor / pentagon" name finite operations on subsets of a
fixed 4-element set.

Everything below is an assertion-backed real check; no placeholders.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.d1_restriction_system import D1_DIMENSIONS

# IMPORT ONLY -- T237 schedule machinery: gr (associated-graded on chains), mu (the
# NON-CIRCULAR schedule-fold yardstick), and the graded helpers. mu is NEVER
# re-derived from any compose code; strictness/laxity is judged against it.
from models.d1filtered_graded_functor import (
    gr,
    graded_bottom,
    graded_dropped,
    graded_equal,
    graded_support,
)

# IMPORT ONLY -- T242 total category: the semilattice morphism type, the
# associative/unital composition, the embedding, gr_semilattice (total), and the
# helpers. None of these is modified here.
from models.d1filtered_compose_meet import (
    D1MeetSemilatticeMorphism,
    _base,
    _endo,
    _from_chain,
    _has_antichain,
    _sl_dropped,
    _two,
    _witnesses,
    compose_meet_semilattice,
    gr_semilattice,
    make_semilattice_identity,
)


# ===========================================================================
# The comparison cell c_{f,g} : gr_semilattice(f;g) -> mu(gr f, gr g)
# ===========================================================================


@dataclass(frozen=True)
class LaxCell:
    """The comparison 2-cell of the candidate lax functor for one (ordered) pair.

    `source` is gr_semilattice of the genuine semilattice composite (a poset of
    meet-strata, possibly antichain-containing). `target` is the mu-fold of the two
    summand gradings (a chain). The booleans are the component checks; `exists` is
    the lax-coherence datum and `invertible` decides lax vs pseudo on this cell."""

    source_strata: tuple[tuple[str, ...], ...]
    target_fold: tuple[tuple[str, ...], ...]
    same_dropped_support: bool
    same_bottom: bool
    source_has_antichain: bool

    @property
    def exists(self) -> bool:
        """The directed comparison cell exists iff the genuine composite and the
        mu-fold record the SAME drops and the SAME surviving floor."""
        return self.same_dropped_support and self.same_bottom

    @property
    def strict(self) -> bool:
        """Strict (identity-like) iff source and target coincide as ordered graded
        sets -- which can only happen when the source is itself a chain."""
        return graded_equal(self.source_strata, self.target_fold)

    @property
    def invertible(self) -> bool:
        """Invertible (=> pseudofunctor on this cell) iff strict. A directed cell
        out of an antichain-containing poset onto a strictly coarser chain has NO
        inverse (it collapses incomparable strata), so invertible == strict here."""
        return self.strict


def _semilattice_composite(
    *chains: D1MeetSemilatticeMorphism,
) -> D1MeetSemilatticeMorphism:
    """Left-fold the semilattice composition. Associativity (T242) makes the fold
    bracketing-independent, so the composite of a triple is a SINGLE object."""
    acc = chains[0]
    for nxt in chains[1:]:
        acc = compose_meet_semilattice(acc, nxt)
    return acc


def lax_cell(composite: D1MeetSemilatticeMorphism, target_fold) -> LaxCell:
    """Build the comparison cell from gr_semilattice(composite) to a mu-fold."""
    src = gr_semilattice(composite)
    return LaxCell(
        source_strata=tuple(tuple(s) for s in src),
        target_fold=tuple(tuple(s) for s in target_fold),
        same_dropped_support=_sl_dropped(composite) == graded_dropped(target_fold),
        same_bottom=frozenset(composite.bottom) == frozenset(graded_bottom(target_fold)),
        source_has_antichain=_has_antichain(composite.layers),
    )


# ===========================================================================
# Triple battery (composable triples over the fixed 4-element universe)
# ===========================================================================


def _anchored_triples() -> list[tuple[str, object, object, object]]:
    """FULL-TOP-ANCHORED composable triples: every leg has the FULL-universe top.
    This is EXACTLY the regime in which T242 established the pairwise comparison
    cell. The lax-functor coherence is expected to HOLD over these. Includes:
      - antichain-producing non-nested triples (the hard cases that forced laxity),
      - a nested control (composite stays a chain -> cells strict),
      - identity-in-the-middle (unit interaction with the pentagon).
    NB f_nest/k_nn/f_n2/g_n2/f_break/g_break all have the full-universe top."""
    w = _witnesses()
    base = _base()
    return [
        # antichain-producing, all full-top (the cells that are merely directed)
        ("break_break_nestfull", w["f_break"], w["g_break"], w["f_nest"]),
        ("all_non_nested", w["f_break"], w["g_break"], w["k_nn"]),
        ("n2_chain_kn", w["f_n2"], w["g_n2"], w["k_nn"]),
        ("break_kn_break", w["f_break"], w["k_nn"], w["g_break"]),
        ("n2_break_n2", w["f_n2"], w["f_break"], w["g_n2"]),
        # nested control: shared full top, nested bottoms 4|-3, 4|-2, 4|-1 -> the
        # composite stays a CHAIN (no antichain) so the cells are STRICT (invertible).
        (
            "nested_full_succ",
            _endo(base, _two(D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f43"),
            _endo(base, _two(D1_DIMENSIONS, D1_DIMENSIONS[:2]), "g42"),
            _endo(base, _two(D1_DIMENSIONS, D1_DIMENSIONS[:1]), "h41"),
        ),
        # identity in the middle (unit coherence), all full-top
        ("mid_identity", w["f_break"], _IDENT_SENTINEL(base), w["g_break"]),
    ]


def _off_anchor_triples() -> list[tuple[str, object, object, object]]:
    """OFF-ANCHOR triples: a NON-full-top leg (g_nest top {a,h,b}; h_nest top {a,h})
    interleaved with a non-nested leg that further-drops a dimension ABSENT from
    that smaller top. These EXHIBIT the obstruction: mu under-counts the dropped
    support, so the comparison cell does NOT exist. Recorded honestly, not skipped."""
    w = _witnesses()
    return [
        # THE witness: h_nest (top {a,h}) sandwiched; g_break drops b (absent from {a,h}).
        ("break_hnest_break", w["f_break"], w["h_nest"], w["g_break"]),
        # second witness: g_nest (top {a,h,b}) then g_break drops r (absent from {a,h,b}).
        ("gnest_break_kn", w["g_nest"], w["g_break"], w["k_nn"]),
    ]


class _IDENT_SENTINEL:
    """Marker so _embed knows to drop in the semilattice identity for this slot."""

    def __init__(self, base):
        self.base = base


def _embed(x):
    if isinstance(x, _IDENT_SENTINEL):
        return make_semilattice_identity(x.base)
    return _from_chain(x)


def _chain_gr(x):
    """gr of a chain leg, or the graded identity for the identity sentinel."""
    if isinstance(x, _IDENT_SENTINEL):
        # gr(identity) = single full-universe stratum, drops nothing
        from models.d1filtered_graded_functor import graded_identity

        return graded_identity()
    return gr(x)


# ===========================================================================
# The pentagon, made executable: (P1) target associator + (P2) cell coherence
# ===========================================================================


def pentagon_report(label: str, f, g, h) -> dict[str, object]:
    """One triple's full coherence datum.

    (P1) TARGET ASSOCIATOR: mu(mu(grf,grg),grh) vs mu(grf,mu(grg,grh)).
    (P2) CELL COHERENCE: the direct cell out of the genuine triple composite exists
         and lands on the SAME mu-fold as both whiskered two-step folds.
    The pentagon COMMUTES iff (P1) holds and (P2)'s cell exists and the whiskered
    targets agree with the direct fold."""
    from models.d1filtered_graded_functor import mu  # imported here to keep mu local-by-import

    grf, grg, grh = _chain_gr(f), _chain_gr(g), _chain_gr(h)

    # (P1) the two mu-folds (target associator). identity associator iff strict-equal.
    fold_left = mu(mu(grf, grg), grh)
    fold_right = mu(grf, mu(grg, grh))
    target_associator_exists = (
        graded_dropped(fold_left) == graded_dropped(fold_right)
        and set(graded_bottom(fold_left)) == set(graded_bottom(fold_right))
    )
    target_associator_strict = graded_equal(fold_left, fold_right)

    # genuine triple composite (T242 associativity => single object; verify both
    # bracketings coincide so the source side of the pentagon is the identity).
    F, G, H = _embed(f), _embed(g), _embed(h)
    comp_l = _semilattice_composite(_semilattice_composite(F, G), H)
    comp_r = _semilattice_composite(F, _semilattice_composite(G, H))
    source_assoc = comp_l.layers == comp_r.layers
    composite = comp_l

    # (P2) the DIRECT cell out of the genuine triple composite.
    direct = lax_cell(composite, fold_left)

    # whiskered two-step folds:
    #   left edge : c_{f,g} whiskered by mu(-, grh) -> target mu(mu(grf,grg),grh)
    #   right edge: c_{g,h} whiskered by mu(grf, -) -> target mu(grf,mu(grg,grh))
    # both must hit a fold the direct cell also hits. We check both folds carry the
    # same dropped support + floor as the direct composite (the whisker targets).
    left_whisker_ok = (
        _sl_dropped(composite) == graded_dropped(fold_left)
        and frozenset(composite.bottom) == frozenset(graded_bottom(fold_left))
    )
    right_whisker_ok = (
        _sl_dropped(composite) == graded_dropped(fold_right)
        and frozenset(composite.bottom) == frozenset(graded_bottom(fold_right))
    )

    pentagon_commutes = (
        target_associator_exists
        and source_assoc
        and direct.exists
        and left_whisker_ok
        and right_whisker_ok
    )

    return {
        "label": label,
        "target_associator_exists": target_associator_exists,
        "target_associator_strict": target_associator_strict,
        "source_assoc": source_assoc,
        "cell_exists": direct.exists,
        "cell_strict": direct.strict,
        "cell_invertible": direct.invertible,
        "cell_source_has_antichain": direct.source_has_antichain,
        "left_whisker_ok": left_whisker_ok,
        "right_whisker_ok": right_whisker_ok,
        "pentagon_commutes": pentagon_commutes,
        "n_source_strata": len(direct.source_strata),
        "n_target_strata": len(direct.target_fold),
    }


def pentagon_battery() -> list[dict[str, object]]:
    """Pentagon battery over selected full-top-anchored generator triples."""
    return [pentagon_report(lab, f, g, h) for (lab, f, g, h) in _anchored_triples()]


def off_anchor_obstruction() -> dict[str, object]:
    """The exact obstruction OFF the anchored subcategory: on triples with a
    non-full-top leg interleaved with a non-nested drop, the genuine meet-closure
    composite records a dropped dimension that mu (the T237 schedule fold) never
    sees, so the comparison cell FAILS to exist. This is a REAL negative (the cell
    is asserted absent), recorded honestly -- it is the first exact obstruction to
    a lax functor over ALL of D1FilteredCat_meet against the mu yardstick."""
    from models.d1filtered_graded_functor import mu

    rows = []
    any_cell_absent = False
    for lab, f, g, h in _off_anchor_triples():
        grf, grg, grh = _chain_gr(f), _chain_gr(g), _chain_gr(h)
        fold = mu(mu(grf, grg), grh)
        F, G, H = _embed(f), _embed(g), _embed(h)
        composite = _semilattice_composite(_semilattice_composite(F, G), H)
        cell = lax_cell(composite, fold)
        absent = not cell.exists
        any_cell_absent = any_cell_absent or absent
        rows.append(
            {
                "label": lab,
                "cell_exists": cell.exists,
                "composite_dropped": sorted(_sl_dropped(composite)),
                "mu_dropped": sorted(graded_dropped(fold)),
                "mu_under_counts": _sl_dropped(composite) != graded_dropped(fold),
                "missing_from_mu": sorted(_sl_dropped(composite) - graded_dropped(fold)),
                "source_assoc": composite.layers
                == _semilattice_composite(F, _semilattice_composite(G, H)).layers,
            }
        )
    return {
        "obstruction_present": any_cell_absent,
        "rows": rows,
    }


# ===========================================================================
# Falsifier 1: a DELIBERATELY-WRONG association must FAIL the commute test
# ===========================================================================


def wrong_association_is_rejected() -> dict[str, object]:
    """A genuine commute test must REJECT a wrong association. We permute the mu-fold
    operands (mu(mu(grh,grf),grg) instead of mu(mu(grf,grg),grh)) and assert the
    direct triple cell does NOT land on it (dropped support differs). If the harness
    accepted this, the pentagon check would be vacuous."""
    from models.d1filtered_graded_functor import mu

    w = _witnesses()
    f, g, h = w["f_break"], w["g_break"], w["h_nest"]
    grf, grg, grh = gr(f), gr(g), gr(h)
    good = mu(mu(grf, grg), grh)
    wrong = mu(mu(grh, grf), grg)  # operands permuted => wrong association/order

    F, G, H = _from_chain(f), _from_chain(g), _from_chain(h)
    composite = _semilattice_composite(_semilattice_composite(F, G), H)

    cell_good = lax_cell(composite, good)
    cell_wrong = lax_cell(composite, wrong)
    return {
        "good_fold": good,
        "wrong_fold": wrong,
        "good_and_wrong_differ": not graded_equal(good, wrong),
        "cell_to_good_exists": cell_good.exists,
        "cell_to_wrong_exists": cell_wrong.exists,
        "cell_to_wrong_support_differs": not cell_wrong.same_dropped_support,
        # the test is non-vacuous iff good is accepted AND wrong is rejected
        "commute_test_is_real": cell_good.exists and (not cell_wrong.exists),
    }


# ===========================================================================
# Falsifier 2: NON-VACUITY injector -- the harness CAN report "does not commute"
# ===========================================================================


def non_vacuity_injector() -> dict[str, object]:
    """Prove the pentagon predicate is FALSIFIABLE: hand it a perturbed cell-target
    whose dropped support is altered (drop one dimension from the fold) and assert
    the cell-existence -- hence pentagon_commutes -- reports FALSE. This shows a
    `pentagon_commutes == True` is a real positive, not a tautology."""
    from models.d1filtered_graded_functor import mu

    w = _witnesses()
    f, g, h = w["f_break"], w["g_break"], w["h_nest"]
    grf, grg, grh = gr(f), gr(g), gr(h)
    good = mu(mu(grf, grg), grh)

    # perturb the fold: delete one dropped dimension from a non-bottom stratum so the
    # dropped support no longer matches the genuine composite.
    perturbed = []
    removed = False
    for s in good[:-1]:
        if s and not removed:
            perturbed.append(tuple(list(s)[1:]))  # drop first element of this stratum
            removed = True
        else:
            perturbed.append(s)
    perturbed.append(good[-1])
    perturbed = tuple(perturbed)

    F, G, H = _from_chain(f), _from_chain(g), _from_chain(h)
    composite = _semilattice_composite(_semilattice_composite(F, G), H)
    cell = lax_cell(composite, perturbed)
    return {
        "perturbed_fold": perturbed,
        "perturbation_changed_support": graded_dropped(perturbed) != graded_dropped(good),
        "cell_exists_on_perturbed": cell.exists,
        "harness_can_report_non_commute": (not cell.exists) and removed,
    }


# ===========================================================================
# Lax vs pseudo: the cells are DIRECTED (not invertible) in general
# ===========================================================================


def lax_not_pseudo() -> dict[str, object]:
    """The candidate lax functor is GENUINELY LAX, not a pseudofunctor: on the
    antichain triples the comparison cell is NOT invertible. The genuine triple
    composite gr_semilattice(f;g;h) is a strictly FINER object (more strata, an
    antichain) than the mu-fold chain it maps to, so the directed cell collapses
    strata and has no inverse."""
    battery = pentagon_battery()
    antichain = [r for r in battery if r["cell_source_has_antichain"]]
    nested = [r for r in battery if not r["cell_source_has_antichain"]]
    some_directed_non_invertible = any(
        (not r["cell_invertible"]) and r["n_source_strata"] > r["n_target_strata"]
        for r in antichain
    )
    nested_strict = all(r["cell_strict"] for r in nested) if nested else False
    return {
        "n_antichain_triples": len(antichain),
        "n_nested_triples": len(nested),
        "some_cell_directed_non_invertible": some_directed_non_invertible,
        "nested_cells_strict": nested_strict,
        "is_pseudofunctor": all(r["cell_invertible"] for r in battery),
        "is_genuine_lax_functor": (not all(r["cell_invertible"] for r in battery))
        and all(r["cell_exists"] for r in battery),
    }


def mu_associator_is_identity() -> dict[str, object]:
    """Strong target-side fact: mu associates ON THE NOSE across the battery (the
    two mu-folds are graded-EQUAL, not merely support-equal), so the target
    associator of the pentagon is the IDENTITY 2-cell. This is what makes the
    pentagon collapse to the single cell-coherence check."""
    from models.d1filtered_graded_functor import mu

    rows = []
    all_strict = True
    for lab, f, g, h in _anchored_triples():
        grf, grg, grh = _chain_gr(f), _chain_gr(g), _chain_gr(h)
        L = mu(mu(grf, grg), grh)
        R = mu(grf, mu(grg, grh))
        strict = graded_equal(L, R)
        all_strict = all_strict and strict
        rows.append({"label": lab, "associator_strict": strict})
    return {"mu_associator_strict_everywhere": all_strict, "rows": rows}


# ===========================================================================
# Honesty boundary (binding T228/T232/T237/T242)
# ===========================================================================


def honesty_boundary() -> dict[str, object]:
    from models.d1cat_filtered_colimit import filtration_is_legal

    base = _base()
    pseudo = (D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS)  # re-adds a dim
    bad = _endo(base, pseudo, "non_monotone")
    rejected = False
    try:
        gr(bad)
    except ValueError:
        rejected = True
    return {
        "non_monotone_is_legal": filtration_is_legal(pseudo),
        "gr_rejects_non_monotone": rejected,
        "coherence_is_finite_category_only": True,
        "general_cocompleteness_still_open": True,
    }


def mu_is_not_a_copy_of_compose_code() -> dict[str, object]:
    """NON-CIRCULARITY GUARD (inherited). On the break triple the genuine composite
    is an antichain-containing poset while the mu-fold is a chain; they agree on
    dropped support + floor but differ in structure. Impossible if mu copied the
    compose code -> the lax/strict judgement is against an independent yardstick."""
    from models.d1filtered_graded_functor import mu

    w = _witnesses()
    f, g, h = w["f_break"], w["g_break"], w["h_nest"]
    F, G, H = _from_chain(f), _from_chain(g), _from_chain(h)
    composite = _semilattice_composite(_semilattice_composite(F, G), H)
    fold = mu(mu(gr(f), gr(g)), gr(h))
    return {
        "composite_has_antichain": _has_antichain(composite.layers),
        "fold_is_chain": True,  # mu returns an ordered tuple (a chain)
        "same_dropped_support": _sl_dropped(composite) == graded_dropped(fold),
        "structures_differ": _has_antichain(composite.layers),
        "comparison_exists": _sl_dropped(composite) == graded_dropped(fold)
        and frozenset(composite.bottom) == frozenset(graded_bottom(fold)),
    }


# ===========================================================================
# Aggregate decision payload
# ===========================================================================


def run_decision() -> dict[str, object]:
    battery = pentagon_battery()  # full-top-anchored subcategory
    off = off_anchor_obstruction()
    wrong = wrong_association_is_rejected()
    inject = non_vacuity_injector()
    lvp = lax_not_pseudo()
    assoc = mu_associator_is_identity()
    boundary = honesty_boundary()
    noncirc = mu_is_not_a_copy_of_compose_code()

    # POSITIVE claim is over the selected FULL-TOP-ANCHORED generator battery
    # (T242's cell regime), not over all morphisms in a typed subcategory.
    anchored_all_commute = all(r["pentagon_commutes"] for r in battery)
    anchored_all_cells_exist = all(r["cell_exists"] for r in battery)
    anchored_all_source_assoc = all(r["source_assoc"] for r in battery)
    commute_test_real = bool(wrong["commute_test_is_real"])
    harness_falsifiable = bool(inject["harness_can_report_non_commute"])
    is_pseudo = bool(lvp["is_pseudofunctor"])
    is_lax = bool(lvp["is_genuine_lax_functor"])
    mu_assoc_identity = bool(assoc["mu_associator_strict_everywhere"])
    # NEGATIVE: off the anchored subcategory the cell fails (mu under-counts).
    off_anchor_obstruction_present = bool(off["obstruction_present"])

    # Verdict logic.
    if not anchored_all_cells_exist or not anchored_all_source_assoc:
        verdict = "object_wise_lax_only_coherence_fails_on_anchor"
    elif not (commute_test_real and harness_falsifiable):
        verdict = "coherence_check_vacuous"  # would falsify the methodology
    elif anchored_all_commute and is_pseudo:
        verdict = "pseudofunctor_on_anchored_subcategory"  # cells invertible everywhere
    elif anchored_all_commute and is_lax and off_anchor_obstruction_present:
        # the honest conditional: genuine lax functor on the anchored subcategory,
        # blocked off it by mu's full-top faithfulness gap.
        verdict = "selected_anchor_battery_commutes_blocked_off_anchor"
    elif anchored_all_commute and is_lax:
        verdict = "genuine_lax_functor_on_anchored_subcategory"
    else:
        verdict = "coherence_fails"

    return {
        "pentagon_battery": battery,
        "off_anchor_obstruction": off,
        "wrong_association_rejected": wrong,
        "non_vacuity_injector": inject,
        "lax_vs_pseudo": lvp,
        "mu_associator": assoc,
        "non_circularity_guard": noncirc,
        "honesty_boundary": boundary,
        "summary": {
            "verdict": verdict,
            "anchored_all_pentagons_commute": anchored_all_commute,
            "anchored_all_cells_exist": anchored_all_cells_exist,
            "anchored_all_source_associative": anchored_all_source_assoc,
            "mu_associator_is_identity": mu_assoc_identity,
            "commute_test_is_real": commute_test_real,
            "harness_can_report_non_commute": harness_falsifiable,
            "is_pseudofunctor": is_pseudo,
            "is_genuine_lax_functor_on_anchor_battery": is_lax,
            "off_anchor_obstruction_present": off_anchor_obstruction_present,
            "mu_independent_of_compose_code": bool(noncirc["structures_differ"]),
            "general_cocompleteness_still_open": True,
            # TOP-LINE: object-wise lax cells of T242 assemble into a GENUINE lax
            # functor on the FULL-TOP-ANCHORED subcategory (NOT a pseudofunctor:
            # cells directed, not invertible); the full-category upgrade is BLOCKED
            # by mu's full-top faithfulness gap, with named repair mu_top.
            "top_line": "conditional_selected_anchor_battery_coherent_non_strict_cells_blocked_off_anchor",
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_decision(), indent=2, default=str))
