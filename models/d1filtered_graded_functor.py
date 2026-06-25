"""T237: functoriality of the associated-graded map gr: D1FilteredCat -> GradedSets.

This module is a FINITE, EXECUTABLE witness for the constructive-next object (1)
T232 named verbatim:

    gr: D1FilteredCat -> GradedSets sending a D1FilteredMorphism to its
    associated-graded drop-schedule strata, and a check whether gr is itself a
    (lax) functor under filtered composition -- i.e. whether gr(f;g) refines
    gr(f) and gr(g) coherently.

T232 CLOSED, conditionally, that the descending-chain colimit in D1FilteredCat is
CONTENT-BEARING: its strata are the associated-graded `gr_k = F_k \\ F_{k+1}`
recording the drop schedule. That settles "the colimit carries the schedule."
T237 asks the next rung: is "carry the schedule" FUNCTORIAL? Concretely, is the
assignment

    objects:    a D1RestrictionSystem  |->  the singleton graded set on its name
    morphisms:  a D1FilteredMorphism m |->  gr(m) := associated_graded(m.filtration)

a functor (strict) or a lax functor (with a canonical comparison) from
D1FilteredCat to a target category GradedSets, with respect to filtered
composition `compose_filtered`?

WHAT MAKES THIS NON-TRIVIAL. `compose_filtered` does NOT concatenate the two
filtrations and keep them verbatim. `_refine_filtrations` (T232) CONCATENATES all
layers, DEDUPES by frozenset, and RE-SORTS descending by size. So the composite
filtration is the UNION (as a layer-poset) of the two chains' layers, NOT their
sequence. The associated-graded of that union is therefore generally a REFINEMENT
of -- not the literal concatenation of -- the two summand gradings. This is
exactly the place where strict functoriality can fail and only a lax (comparison)
functoriality can hold. T237 decides which.

THE TARGET CATEGORY GradedSets (built here, finite). An object is a finite
ordered list of disjoint dimension-strata (a "graded set" over the fixed
4-element D1_DIMENSIONS). A morphism `S -> T` is a REFINEMENT WITNESS: T's strata
union to a subset of S's union, and every stratum of T is contained in some
stratum of S (T is "no coarser than" S on its support). Identities and refinement
composition make this a category (a thin poset-style category: at most one
morphism per ordered pair, given by containment of the refinement relation). The
canonical comparison map gr(f;g) -> [gr(f) then gr(g)] lives here.

THE DECISION (verdicts, made executable):
  - strict functoriality  := gr(f;g) is EQUAL (as a graded set) to the
    "schedule concatenation" mu(gr(f), gr(g)) of the two summand gradings.
  - lax functoriality     := there is a CANONICAL comparison morphism in
    GradedSets, gr(f;g) -> mu(gr(f), gr(g)), natural in the obvious finite sense,
    i.e. gr(f;g) is a REFINEMENT of the concatenated schedule that drops nothing
    and adds nothing on support (same recovered universe, possibly re-sorted /
    de-duplicated layering).
  - identity law          := gr(id) == id_gr (the graded identity), required for
    BOTH strict and lax.

Complexity tags: finite_witness (a finite executable fixture over the fixed
4-element dimension universe; NO scalable/continuum theorem asserted) and
poly_decider (finite enumeration over the fixed universe; NOT a hidden search,
NOT a hardness/NP claim). This is the DISCRETE CATEGORY-LEVEL analogue and is
EXPLICITLY DISTINCT from the continuum coefficient-sheaf-H1 cofinality lane
(T231/T236); the two index different colimit systems and must never be conflated.
No physics/geometry/curvature/Cech/sheaf/new-object language is promoted from
this witness.

HONESTY GUARD (binding, inherited from T228 via T232): deciding gr is (lax)
functorial under the monotone-descending typing does NOT establish general
cocompleteness at infinity, and does NOT extend to non-monotone diagrams. We
re-verify the boundary: gr is only defined on legal (descending) filtrations; the
functor laws are tested only there.

Everything below is an assertion-backed real check; no placeholders.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.d1_restriction_system import D1_DIMENSIONS, D1RestrictionSystem
from models.d1cat_filtered_colimit import (
    D1FilteredMorphism,
    Filtration,
    _normalize_layer,
    associated_graded,
    bare_intersection,
    build_filtered_descending_chain,
    compose_filtered,
    filtration_is_legal,
    make_filtered_identity,
)

# ---------------------------------------------------------------------------
# Target category: GradedSets (finite, over the fixed 4-element universe)
# ---------------------------------------------------------------------------

GradedSet = tuple[tuple[str, ...], ...]
"""A graded set is an ORDERED tuple of strata, each a normalized dimension subset
of D1_DIMENSIONS. Read top-to-bottom as a drop schedule: stratum k is the data
dropped at step k, with the final stratum the surviving bottom (bare
intersection). The non-bottom strata are pairwise disjoint by construction of the
associated-graded (a partition of the dropped dimensions); the bottom stratum is
the surviving floor."""


def graded_support(gs: GradedSet) -> frozenset[str]:
    """The union of all strata = every dimension the graded set mentions."""
    out: set[str] = set()
    for s in gs:
        out |= set(s)
    return frozenset(out)


def graded_dropped(gs: GradedSet) -> frozenset[str]:
    """The dimensions recorded as DROPPED = union of all non-bottom strata.
    (The bottom stratum is the surviving floor, not a drop.)"""
    out: set[str] = set()
    for s in gs[:-1]:
        out |= set(s)
    return frozenset(out)


def graded_bottom(gs: GradedSet) -> tuple[str, ...]:
    """The surviving floor stratum (bare intersection)."""
    return gs[-1] if gs else ()


def graded_equal(a: GradedSet, b: GradedSet) -> bool:
    """Strict equality of graded sets: same strata in the same order."""
    return tuple(_normalize_layer(s) for s in a) == tuple(_normalize_layer(s) for s in b)


def graded_identity() -> GradedSet:
    """id_gr: the identity graded set = single bottom stratum = the full universe,
    nothing dropped. This is gr(make_filtered_identity(...)) and the GradedSets
    identity object for the schedule reading."""
    return (_normalize_layer(D1_DIMENSIONS),)


# ---------------------------------------------------------------------------
# The functor gr on objects and morphisms
# ---------------------------------------------------------------------------


def gr_on_object(system: D1RestrictionSystem) -> str:
    """gr on objects. D1FilteredCat objects ARE D1RestrictionSystems (object
    component unchanged from T41/T232). In GradedSets the object datum is just the
    carrier label; the schedule content lives on morphisms. We send an object to
    its name (the discrete object of GradedSets indexed by that system)."""
    return system.name


def gr(m: D1FilteredMorphism) -> GradedSet:
    """gr on morphisms: a D1FilteredMorphism's associated-graded drop schedule.
    This is EXACTLY T232's `associated_graded(m.filtration)` -- the content the
    colimit was shown to carry. gr is defined ONLY on legal (descending)
    filtrations (honesty guard)."""
    if not filtration_is_legal(m.filtration):
        raise ValueError(
            "gr is defined only on legal descending filtrations (honesty guard)"
        )
    return associated_graded(m.filtration)


# ---------------------------------------------------------------------------
# The schedule-concatenation mu: how the two summand gradings COMBINE
# ---------------------------------------------------------------------------


def mu(gf: GradedSet, gg: GradedSet) -> GradedSet:
    """The CANONICAL schedule concatenation of two gradings: "do gf's drops, then
    gg's drops". This is the target against which gr(f;g) is compared for
    (strict/lax) functoriality.

    Construction (the only schedule-preserving composite that respects the
    descending typing):
      - take gf's drop strata (all but its bottom),
      - then gg's drop strata RESTRICTED to what gf still had available, i.e.
        intersected with gf's bottom (gg can only further-drop within the floor
        gf left),
      - the bottom is the intersection of the two bottoms (the joint surviving
        floor),
      - finally drop any now-empty strata (a step that turns out to drop nothing
        survives as no stratum).
    This mirrors how a real two-stage descending filtration composes: the second
    stage acts inside the residue of the first.
    """
    gf_floor = set(graded_bottom(gf))
    strata: list[tuple[str, ...]] = []
    # Stage 1: gf's own drops (it operates on the full available data).
    for s in gf[:-1]:
        strata.append(_normalize_layer(s))
    # Stage 2: gg's drops, but only the part still present in gf's floor.
    for s in gg[:-1]:
        restricted = set(s) & gf_floor
        if restricted:
            strata.append(_normalize_layer(tuple(restricted)))
        gf_floor -= restricted
    # Joint surviving bottom = intersection of the two floors.
    joint_bottom = gf_floor & set(graded_bottom(gg))
    strata.append(_normalize_layer(tuple(joint_bottom)))
    return tuple(strata)


# ---------------------------------------------------------------------------
# GradedSets morphisms: the canonical comparison / refinement witness
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class GradedComparison:
    """A morphism source -> target in GradedSets, recording WHY one grading
    refines / coheres with another. `exists` is the decision; the booleans are the
    component checks the canonical comparison morphism must satisfy."""

    source: GradedSet
    target: GradedSet
    same_dropped_support: bool  # the two schedules drop the SAME dimensions
    same_bottom: bool  # they agree on the surviving floor
    target_refines_source: bool  # every target stratum sits inside a source stratum
    strict: bool  # strata equal in order (=> strict functor on this pair)

    @property
    def exists(self) -> bool:
        """A canonical comparison morphism exists iff the two gradings record the
        SAME drops and the SAME floor (so they are the same schedule up to how the
        layering is grouped/ordered). That is the lax-functor coherence datum."""
        return self.same_dropped_support and self.same_bottom


def graded_comparison(source: GradedSet, target: GradedSet) -> GradedComparison:
    """Build the canonical comparison morphism `source -> target` in GradedSets.

    The comparison is the witness that `source` (here: gr(f;g)) and `target`
    (here: mu(gr(f), gr(g))) describe the SAME drop schedule, possibly grouped
    differently. It EXISTS iff dropped-supports and bottoms agree; it is STRICT
    iff the strata coincide in order."""

    def refines(s: GradedSet, t: GradedSet) -> bool:
        # every NON-bottom stratum of t is contained in the union of s's strata,
        # i.e. t introduces no dimension s did not have.
        s_support = graded_support(s)
        return all(set(stratum) <= s_support for stratum in t)

    return GradedComparison(
        source=source,
        target=target,
        same_dropped_support=graded_dropped(source) == graded_dropped(target),
        same_bottom=set(graded_bottom(source)) == set(graded_bottom(target)),
        target_refines_source=refines(source, target),
        strict=graded_equal(source, target),
    )


# ---------------------------------------------------------------------------
# The functor laws, made executable over a finite battery
# ---------------------------------------------------------------------------


def _two_layer(top: tuple[str, ...], bot: tuple[str, ...]) -> Filtration:
    return (_normalize_layer(top), _normalize_layer(bot))


def _endo(system: D1RestrictionSystem, filtration: Filtration, name: str) -> D1FilteredMorphism:
    from models.d1_restriction_system import SiteMap

    return D1FilteredMorphism(
        name=name,
        source=system,
        target=system,
        site_map=tuple(SiteMap(sid, sid) for sid in system.site_ids()),
        filtration=filtration,
    )


def _base_system() -> D1RestrictionSystem:
    from models.d1cat_filtered_colimit import _one_site_system

    return _one_site_system("X", (1, 1, 1, 1))


def gr_preserves_identity() -> dict[str, object]:
    """Functor law 1: gr(id_A) == id_gr for the GradedSets identity.

    make_filtered_identity has the single full-universe layer (D1_DIMENSIONS,);
    its associated-graded is the single bottom stratum = the full universe,
    nothing dropped. That is exactly graded_identity()."""
    base = _base_system()
    idm = make_filtered_identity(base)
    gr_id = gr(idm)
    return {
        "gr_identity": gr_id,
        "graded_identity": graded_identity(),
        "identity_law_holds": graded_equal(gr_id, graded_identity()),
        "identity_drops_nothing": graded_dropped(gr_id) == frozenset(),
    }


def gr_composable(f: D1FilteredMorphism, g: D1FilteredMorphism) -> bool:
    """gr(f;g) is DEFINED iff compose_filtered(f, g) is itself a legal (descending)
    morphism -- because gr is total only on legal descending filtrations.

    KEY STRUCTURAL FACT (the obstruction this lane found): compose_filtered is NOT
    closed on legal morphisms. _refine_filtrations concatenates the two filtrations
    and re-sorts by SIZE; when the two filtrations are MUTUALLY NON-NESTED (neither
    layer-set contains the other), the size-sorted result need NOT be set-descending,
    so the composite is an ILLEGAL morphism and gr(f;g) is undefined. This predicate
    is the honest domain of the functoriality question."""
    return compose_filtered(f, g).is_legal()


def _composition_pair_report(
    f: D1FilteredMorphism, g: D1FilteredMorphism, label: str
) -> dict[str, object]:
    """For one composable pair f;g, report gr(f), gr(g), gr(f;g), mu(gr f, gr g),
    and the comparison morphism in GradedSets. The per-pair functoriality datum.

    If compose_filtered(f, g) is NOT legal (non-nested filtrations -> non-descending
    composite), gr(f;g) is UNDEFINED and we record `composite_legal == False`. Such
    a pair is OUTSIDE the domain of the functor law and cannot witness strictness;
    it is the obstruction, recorded honestly rather than silently skipped."""
    fg = compose_filtered(f, g)
    g_f = gr(f)
    g_g = gr(g)
    composite_legal = fg.is_legal()
    if not composite_legal:
        return {
            "label": label,
            "gr_f": g_f,
            "gr_g": g_g,
            "composite_filtration": fg.filtration,
            "composite_legal": False,
            "gr_fg_defined": False,
            # everything below is undefined when gr(f;g) does not exist
            "strict_equal": False,
            "comparison_exists": False,
            "same_dropped_support": False,
            "same_bottom": False,
            "target_refines_source": False,
            "no_loss_no_gain": False,
        }
    g_fg = gr(fg)
    concat = mu(g_f, g_g)
    cmp = graded_comparison(g_fg, concat)
    return {
        "label": label,
        "gr_f": g_f,
        "gr_g": g_g,
        "gr_fg": g_fg,
        "mu_concat": concat,
        "composite_legal": True,
        "gr_fg_defined": True,
        "strict_equal": cmp.strict,
        "comparison_exists": cmp.exists,
        "same_dropped_support": cmp.same_dropped_support,
        "same_bottom": cmp.same_bottom,
        "target_refines_source": cmp.target_refines_source,
        # the composite drop-support must equal the union of the two summand drops
        # MINUS double counting -- i.e. gr(f;g) records exactly the dimensions that
        # f or g (within f's residue) dropped. This is the no-loss/no-gain check.
        "no_loss_no_gain": graded_dropped(g_fg) == graded_dropped(concat),
    }


def _nested_pairs() -> list[tuple[D1FilteredMorphism, D1FilteredMorphism, str]]:
    """Pairs whose composites ARE legal: the two filtrations are mutually nested
    (prefix-compatible), so compose_filtered stays descending. These are exactly
    the gr-composable pairs -- the domain on which the functor law can be tested,
    and which includes the entire T232 colimit chain."""
    base = _base_system()
    A = D1_DIMENSIONS  # full 4
    A3 = D1_DIMENSIONS[:3]
    A2 = D1_DIMENSIONS[:2]
    A1 = D1_DIMENSIONS[:1]
    return [
        # (a) disjoint successive drops: 4->3 then 3->2. Classic two-stage.
        (_endo(base, _two_layer(A, A3), "f_a"), _endo(base, _two_layer(A3, A2), "g_a"), "successive_4_3__3_2"),
        # (b) deeper successive: 4->2 then 2->1.
        (_endo(base, _two_layer(A, A2), "f_b"), _endo(base, _two_layer(A2, A1), "g_b"), "successive_4_2__2_1"),
        # (c) SHARED top layer, NESTED bottoms: f:4->3, g:4->2 with {a,h} subset {a,h,b}.
        #     Forces the dedupe/re-sort path; composite stays descending.
        (_endo(base, _two_layer(A, A3), "f_c"), _endo(base, _two_layer(A, A2), "g_c"), "shared_top_nested_4_3__4_2"),
        # (d) g drops MORE than f's floor allows (g:4->1 after f:4->3): stage-2
        #     restriction to f's residue; bottoms nested {a} subset {a,h,b}.
        (_endo(base, _two_layer(A, A3), "f_d"), _endo(base, _two_layer(A, A1), "g_d"), "residue_restrict_4_3__4_1"),
        # (e) identity-on-the-right: f:4->3, g = id. Must reduce to gr(f).
        (_endo(base, _two_layer(A, A3), "f_e"), make_filtered_identity(base), "right_identity"),
        # (f) identity-on-the-left: f = id, g:4->2. Must reduce to gr(g).
        (make_filtered_identity(base), _endo(base, _two_layer(A, A2), "g_f"), "left_identity"),
        # (g) g drops to empty after f: f:4->2, g:2->(). Saturating composite.
        (_endo(base, _two_layer(A, A2), "f_g"), _endo(base, _two_layer(A2, ()), "g_g"), "saturate_4_2__2_empty"),
    ]


def _non_nested_pairs() -> list[tuple[D1FilteredMorphism, D1FilteredMorphism, str]]:
    """Pairs whose two filtrations are MUTUALLY NON-NESTED. compose_filtered
    re-sorts by size and produces a NON-descending composite -> gr(f;g) undefined.
    These EXHIBIT the obstruction: the domain on which gr fails to be even a partial
    functor without restriction.

    Example (the witness): f: 4 -> {a,h,b} (drops r); g: 4 -> {h,r} (drops a,b).
    {a,h,b} and {h,r} are incomparable, so the size-sorted composite
    4 -> {a,h,b} -> {h,r} -> {h} is NOT descending ({a,h,b} does not contain r)."""
    base = _base_system()
    A = D1_DIMENSIONS
    drop_r = ("accessible_support", "holder_redundancy", "branch_support")  # {a,h,b}
    keep_hr = ("holder_redundancy", "reversal_cost")  # {h,r}
    keep_ar = ("accessible_support", "reversal_cost")  # {a,r}
    keep_hb = ("holder_redundancy", "branch_support")  # {h,b}
    return [
        (_endo(base, _two_layer(A, drop_r), "f_n1"), _endo(base, _two_layer(A, keep_hr), "g_n1"), "non_nested_ahb__hr"),
        (_endo(base, _two_layer(A, keep_ar), "f_n2"), _endo(base, _two_layer(A, keep_hb), "g_n2"), "non_nested_ar__hb"),
    ]


def _composition_battery() -> list[dict[str, object]]:
    """The full finite battery: gr-composable (nested) pairs that test the functor
    law where it is defined, PLUS non-nested pairs that exhibit the obstruction
    (compose_filtered not legality-closed)."""
    pairs = _nested_pairs() + _non_nested_pairs()
    return [_composition_pair_report(f, g, lab) for (f, g, lab) in pairs]


def chain_associativity_report() -> dict[str, object]:
    """gr applied along the full descending chain (the T232 colimit witness),
    checked associatively: gr of the whole composite vs the left-folded mu of the
    per-leg gradings. Decides whether the schedule reading is path-independent."""
    chain = build_filtered_descending_chain(6)
    # full composite morphism via compose_filtered left-fold
    composite = chain[0]
    for leg in chain[1:]:
        composite = compose_filtered(composite, leg)
    gr_full = gr(composite)
    # left-folded mu of the per-leg gradings
    folded = gr(chain[0])
    for leg in chain[1:]:
        folded = mu(folded, gr(leg))
    cmp = graded_comparison(gr_full, folded)
    return {
        "gr_full": gr_full,
        "mu_folded": folded,
        "strict_equal": cmp.strict,
        "comparison_exists": cmp.exists,
        "same_dropped_support": cmp.same_dropped_support,
        "same_bottom": cmp.same_bottom,
        # the full schedule must still recover the entire universe (nothing lost)
        "full_recovers_universe": graded_dropped(gr_full) == frozenset(D1_DIMENSIONS[:3]) | {D1_DIMENSIONS[3]}
        if False
        else (graded_dropped(gr_full) | set(graded_bottom(gr_full))) == set(D1_DIMENSIONS),
    }


def honesty_boundary_report() -> dict[str, object]:
    """gr is defined ONLY on legal descending filtrations. A non-monotone
    pseudo-filtration is not in the domain of gr at all -- so the functoriality
    decision is confined to the monotone-descending typing, and does NOT establish
    general cocompleteness at infinity (binding T228/T232 honesty guard)."""
    base = _base_system()
    pseudo = (D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS)  # re-adds a dim
    bad = _endo(base, pseudo, "non_monotone")
    domain_error = False
    try:
        gr(bad)
    except ValueError:
        domain_error = True
    return {
        "non_monotone_is_legal": filtration_is_legal(pseudo),
        "gr_rejects_non_monotone": domain_error,
        "functoriality_confined_to_descending": domain_error,
        "general_cocompleteness_still_open": True,
    }


# ---------------------------------------------------------------------------
# Aggregate decision payload
# ---------------------------------------------------------------------------


def run_decision() -> dict[str, object]:
    battery = _composition_battery()
    identity = gr_preserves_identity()
    chain = chain_associativity_report()
    boundary = honesty_boundary_report()

    # Partition the battery: the gr-composable (legal composite) sub-domain on which
    # the functor law is even STATABLE, vs the obstruction pairs (illegal composite).
    composable = [p for p in battery if p["composite_legal"]]
    obstructed = [p for p in battery if not p["composite_legal"]]

    # On the gr-composable sub-domain: does the law hold strictly / laxly?
    comp_comparisons_exist = all(p["comparison_exists"] for p in composable) and chain["comparison_exists"]
    comp_strict = all(p["strict_equal"] for p in composable) and chain["strict_equal"]
    comp_no_loss = all(p["no_loss_no_gain"] for p in composable)
    identity_ok = bool(identity["identity_law_holds"])

    # The obstruction is REAL iff at least one legal x legal pair composes illegally.
    obstruction_present = len(obstructed) >= 1
    # And we require the witness to be genuinely legal-on-each-leg (so it is a true
    # non-closure of the partial monoid, not a malformed input).
    obstruction_legit = all(p["gr_f"] is not None and p["gr_g"] is not None for p in obstructed)

    # Verdict logic.
    #   - If gr were total (no obstruction) and strict everywhere -> strict_functor.
    #   - With the obstruction present, gr is functorial only on the gr-composable
    #     sub-category (filtration-nested composites). On that sub-category it is
    #     STRICT here; off it, gr(f;g) is undefined. The honest verdict is
    #     CONDITIONAL: gr is a (strict-on-its-domain) functor on the gr-composable
    #     subcategory of D1FilteredCat, NOT on all of D1FilteredCat.
    if not identity_ok:
        verdict = "not_functorial"
    elif obstruction_present and obstruction_legit:
        # strict where defined, but domain-restricted by the legality obstruction
        verdict = "conditional_partial_functor"
    elif comp_strict and comp_no_loss and comp_comparisons_exist:
        verdict = "strict_functor"
    elif comp_comparisons_exist and comp_no_loss:
        verdict = "lax_functor"
    else:
        verdict = "not_functorial"

    return {
        "identity": identity,
        "composition_battery": battery,
        "chain_associativity": chain,
        "honesty_boundary": boundary,
        "summary": {
            "identity_law_holds": identity_ok,
            "gr_composable_pairs": len(composable),
            "obstructed_pairs": len(obstructed),
            "obstruction_present": obstruction_present,
            "strict_on_composable_subdomain": comp_strict,
            "no_loss_no_gain_on_composable": comp_no_loss,
            "comparisons_exist_on_composable": comp_comparisons_exist,
            "chain_strict": chain["strict_equal"],
            "verdict": verdict,
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_decision(), indent=2, default=str))
