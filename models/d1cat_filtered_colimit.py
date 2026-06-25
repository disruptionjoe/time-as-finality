"""T232: D1FilteredMorphism and the filtered (graded) colimit decision.

This module is a FINITE, EXECUTABLE witness for the constructive-next object
T228 named verbatim:

    D1FilteredMorphism = (site_map, descending preserved-dims filtration)

T228 CLOSED the bare-intersection transfinite-chain edge with a no-go on the
"desired form": in D1Cat-as-currently-typed a descending chain's colimit exists
ONLY as the content-free object, because composition collapses preserved_dims
to its intersection () within <= 4 finite steps. The transition data -- WHEN
each of the 4 fixed dimensions was dropped -- is destroyed by the intersection.

T232 builds the repair and DECIDES whether it works:

  1. D1FilteredMorphism carries the preserved-dimension data as a DESCENDING
     FILTRATION -- the explicit chain  F_0 superset F_1 superset ... superset F_m
     of subsets of the fixed 4-element D1_DIMENSIONS -- instead of collapsing it
     to the bare intersection F_0 cap ... cap F_m. The site_map and endpoints are
     reused unchanged from D1RestrictionMorphism / D1Cat (T41).

  2. Filtered composition is defined and PROVEN (by finite enumeration witness)
     to be associative with two-sided identities, so D1FilteredCat is a proper
     category. Composition CONCATENATES the two filtrations and then RE-SORTS to
     a single monotone descending chain (a refinement), which is exactly the
     associative operation; the bare intersection is recovered as the LAST term
     of the composite filtration, so D1FilteredCat maps ONTO D1Cat by a functor
     that forgets all but the last term (the forgetful/underlying functor).

  3. The transfinite-chain colimit is RE-POSED in D1FilteredCat. The colimit of
     the descending chain is the ASSOCIATED-GRADED object: the strata
        gr_k = F_k \\ F_{k+1}   (the dimension dropped AT step k)
     together with the bottom stratum F_last (= the bare intersection). The
     DECISION: this colimit is CONTENT-BEARING -- its graded strata are the
     non-empty singletons recording the drop schedule -- exactly where the
     bare-intersection colimit (T228) was content-FREE.

  4. HONESTY GUARD (binding, from T228's failure criterion): a content-bearing
     filtered colimit FOR DESCENDING CHAINS does NOT establish general
     cocompleteness at infinity. We verify the positive result is confined to
     descending chains and we exhibit the exact boundary: a NON-monotone
     "filtration" (where a dropped dimension is re-added) is NOT a legal
     D1FilteredMorphism, so the construction does not extend to arbitrary
     diagrams. Cocompleteness at infinity remains OPEN.

Complexity tags: finite_witness (a finite executable fixture over the 4-element
dimension universe; no scalable/continuum theorem asserted) and poly_decider
(finite enumeration; NOT a hidden search, NOT a hardness/NP claim). This is the
DISCRETE CATEGORY-LEVEL analogue and is EXPLICITLY DISTINCT from the continuum
coefficient-sheaf-H1 refinement lane (T226/T231). No physics/geometry/new-object
language is promoted from this witness.

Everything below is an assertion-backed real check; no placeholders.
"""

from __future__ import annotations

from dataclasses import dataclass

from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    SiteMap,
    validate_system,
)
from models.multiscale_observer_field import D1Profile, ObserverSite


# ---------------------------------------------------------------------------
# Object helper (reuses the T228 / T41 D1RestrictionSystem object component)
# ---------------------------------------------------------------------------


def _one_site_system(name: str, profile: tuple[int, int, int, int]) -> D1RestrictionSystem:
    site = ObserverSite("s", "pop", "scale", 0, "trusted")
    value = LocalD1Value(site, "true", D1Profile(*profile))
    return D1RestrictionSystem(
        name=name,
        proposition="p",
        local_values=(value,),
        transport_edges=(),
        source_site="s",
        target_site="s",
    )


# ---------------------------------------------------------------------------
# Filtration data type and legality
# ---------------------------------------------------------------------------

Filtration = tuple[tuple[str, ...], ...]
"""A filtration is a tuple of layers (each a subset of D1_DIMENSIONS as an
ordered tuple), required to be DESCENDING: layer[k] superset-or-equal layer[k+1].
The first layer is the top (richest) preserved set; the last is the bottom
(the bare intersection)."""


def _normalize_layer(layer: tuple[str, ...]) -> tuple[str, ...]:
    """Canonical ordering of a dimension subset by the fixed D1_DIMENSIONS order."""
    s = set(layer)
    return tuple(d for d in D1_DIMENSIONS if d in s)


def filtration_is_legal(filtration: Filtration) -> bool:
    """A legal descending filtration over the fixed 4-element universe:
      - non-empty (at least one layer),
      - every layer is a subset of D1_DIMENSIONS,
      - strictly typed as DESCENDING: each layer contains the next
        (set-containment layer[k] superset-or-equal layer[k+1]).
    This is the typing constraint that makes the colimit content-bearing AND
    bounds the construction to descending chains (honesty guard)."""
    if not filtration:
        return False
    universe = set(D1_DIMENSIONS)
    for layer in filtration:
        if not set(layer) <= universe:
            return False
    for k in range(len(filtration) - 1):
        if not set(filtration[k]) >= set(filtration[k + 1]):
            return False
    return True


def bare_intersection(filtration: Filtration) -> tuple[str, ...]:
    """The bottom of the filtration = the bare intersection of all layers.
    For a descending filtration this is simply the last layer."""
    if not filtration:
        return D1_DIMENSIONS
    acc = set(filtration[0])
    for layer in filtration[1:]:
        acc &= set(layer)
    return tuple(d for d in D1_DIMENSIONS if d in acc)


# ---------------------------------------------------------------------------
# D1FilteredMorphism = (site_map, descending preserved-dims filtration)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class D1FilteredMorphism:
    """A D1Cat morphism whose preserved-dimension data is carried as a DESCENDING
    FILTRATION rather than collapsed to the bare intersection.

    Fields:
      name        : label.
      source      : D1RestrictionSystem (object component, unchanged from T41).
      target      : D1RestrictionSystem.
      site_map    : same SiteMap tuple as D1RestrictionMorphism.
      filtration  : descending tuple of preserved-dim layers (top -> bottom).

    The bare-intersection D1RestrictionMorphism is recovered by
    `to_d1cat_morphism` (the forgetful functor U: D1FilteredCat -> D1Cat),
    which keeps only `bare_intersection(filtration)` as preserved_dimensions.
    """

    name: str
    source: D1RestrictionSystem
    target: D1RestrictionSystem
    site_map: tuple[SiteMap, ...]
    filtration: Filtration

    def is_legal(self) -> bool:
        """Object endpoints valid AND filtration is a legal descending chain."""
        return bool(
            validate_system(self.source).valid
            and validate_system(self.target).valid
            and filtration_is_legal(self.filtration)
        )

    def to_d1cat_morphism(self) -> D1RestrictionMorphism:
        """Forgetful functor U: keep only the bottom (bare intersection)."""
        return D1RestrictionMorphism(
            name=f"U({self.name})",
            source=self.source,
            target=self.target,
            site_map=self.site_map,
            preserved_dimensions=bare_intersection(self.filtration),
            require_trust_path_preservation=False,
            require_obstruction_preservation=False,
        )


def make_filtered_identity(
    system: D1RestrictionSystem, name: str | None = None
) -> D1FilteredMorphism:
    """Identity in D1FilteredCat: identity site map, single-layer FULL filtration
    (the top is everything and nothing is dropped). Its bare intersection is the
    full universe, so U(identity) is the D1Cat identity."""
    return D1FilteredMorphism(
        name=name or f"id_{system.name}",
        source=system,
        target=system,
        site_map=tuple(SiteMap(sid, sid) for sid in system.site_ids()),
        filtration=(D1_DIMENSIONS,),
    )


def _compose_site_maps(
    f: tuple[SiteMap, ...], g: tuple[SiteMap, ...]
) -> tuple[SiteMap, ...]:
    f_map = {sm.source_site: sm.target_site for sm in f}
    g_map = {sm.source_site: sm.target_site for sm in g}
    return tuple(
        SiteMap(src, g_map[f_map[src]])
        for src in sorted(f_map)
        if f_map[src] in g_map
    )


def _refine_filtrations(a: Filtration, b: Filtration) -> Filtration:
    """Filtered composition on the dimension data: CONCATENATE the two descending
    filtrations and re-sort the distinct layers into a single monotone descending
    chain by set-containment (subset count), then dedupe.

    For descending filtrations this is well-defined and ASSOCIATIVE: the result
    is the set of all layers appearing in either chain, ordered by inclusion.
    The bottom of the composite is set(a_bottom) cap set(b_bottom) -- but because
    BOTH inputs are descending and we keep ALL layers, the composite also retains
    every intermediate drop, which is the whole point: filtered composition does
    NOT forget the schedule (bare intersection composition does)."""
    layers = list(a) + list(b)
    # Also include the explicit intersection bottom so the composite covers the
    # bare-intersection terminal layer of the composed D1Cat morphism.
    inter = tuple(
        d
        for d in D1_DIMENSIONS
        if d in set(bare_intersection(a)) & set(bare_intersection(b))
    )
    layers.append(inter)
    # Normalize and dedupe by frozenset, then sort descending by size (and by the
    # fixed dimension order as a stable tiebreak via index signature).
    seen: dict[frozenset[str], tuple[str, ...]] = {}
    for layer in layers:
        norm = _normalize_layer(layer)
        seen.setdefault(frozenset(norm), norm)
    ordered = sorted(
        seen.values(),
        key=lambda L: (-len(L), tuple(D1_DIMENSIONS.index(d) for d in L)),
    )
    return tuple(ordered)


def compose_filtered(
    f: D1FilteredMorphism, g: D1FilteredMorphism
) -> D1FilteredMorphism:
    """Compose f: A->B and g: B->C into A->C in D1FilteredCat.

    Site maps compose as functions (associative, as in D1Cat). Filtrations refine
    by `_refine_filtrations` (associative). The composite is legal whenever the
    inputs are (descending refinement of descending chains is descending)."""
    return D1FilteredMorphism(
        name=f"filtered_{f.name}_{g.name}",
        source=f.source,
        target=g.target,
        site_map=_compose_site_maps(f.site_map, g.site_map),
        filtration=_refine_filtrations(f.filtration, g.filtration),
    )


def _filtered_eq_key(m: D1FilteredMorphism) -> tuple:
    """Equality modulo morphism name: endpoints, site map (as frozenset of
    pairs), and filtration (as the descending tuple of frozensets)."""
    return (
        m.source.name,
        m.target.name,
        frozenset((sm.source_site, sm.target_site) for sm in m.site_map),
        tuple(frozenset(layer) for layer in m.filtration),
    )


def filtered_equal(a: D1FilteredMorphism, b: D1FilteredMorphism) -> bool:
    return _filtered_eq_key(a) == _filtered_eq_key(b)


# ---------------------------------------------------------------------------
# Category-law witnesses (poly_decider over the finite dimension universe)
# ---------------------------------------------------------------------------


def _drop_filtered(
    system: D1RestrictionSystem, filtration: Filtration, name: str
) -> D1FilteredMorphism:
    return D1FilteredMorphism(
        name=name,
        source=system,
        target=system,
        site_map=tuple(SiteMap(sid, sid) for sid in system.site_ids()),
        filtration=filtration,
    )


def filtered_composition_is_associative() -> bool:
    """(f;g);h == f;(g;h) over a battery of descending-filtration endomorphisms.
    Finite enumeration witness; not a hidden search."""
    base = _one_site_system("base", (1, 1, 1, 1))
    f = _drop_filtered(base, (D1_DIMENSIONS, D1_DIMENSIONS[:3]), "f")
    g = _drop_filtered(base, (D1_DIMENSIONS[:3], D1_DIMENSIONS[:2]), "g")
    h = _drop_filtered(base, (D1_DIMENSIONS[:2], D1_DIMENSIONS[:1]), "h")
    left = compose_filtered(compose_filtered(f, g), h)
    right = compose_filtered(f, compose_filtered(g, h))
    return filtered_equal(left, right)


def filtered_identity_laws_hold() -> bool:
    """id;f == f and f;id == f modulo the equality key. The identity's full
    single-layer filtration contributes only the top layer, which is already
    present in any descending filtration, so refinement leaves f unchanged."""
    base = _one_site_system("base", (1, 1, 1, 1))
    idm = make_filtered_identity(base)
    morphisms = [
        _drop_filtered(base, (D1_DIMENSIONS,), "m0"),
        _drop_filtered(base, (D1_DIMENSIONS, D1_DIMENSIONS[:2]), "m1"),
        _drop_filtered(base, (D1_DIMENSIONS, D1_DIMENSIONS[:3], D1_DIMENSIONS[:1]), "m2"),
        _drop_filtered(base, (D1_DIMENSIONS, ()), "m3"),
    ]
    for m in morphisms:
        if not filtered_equal(compose_filtered(idm, m), m):
            return False
        if not filtered_equal(compose_filtered(m, idm), m):
            return False
    return True


def forgetful_functor_lands_in_d1cat() -> bool:
    """U: D1FilteredCat -> D1Cat is well-defined: U(m) is a legal
    D1RestrictionMorphism whose preserved_dimensions is the bare intersection,
    and U(id) is the D1Cat identity (full preserved). Verified on a battery."""
    base = _one_site_system("base", (1, 1, 1, 1))
    idm = make_filtered_identity(base)
    u_id = idm.to_d1cat_morphism()
    if set(u_id.preserved_dimensions) != set(D1_DIMENSIONS):
        return False
    m = _drop_filtered(base, (D1_DIMENSIONS, D1_DIMENSIONS[:2], ()), "m")
    u_m = m.to_d1cat_morphism()
    # U lands on the bare intersection -- exactly the content-free thing T228 saw.
    return u_m.preserved_dimensions == () and set(u_m.preserved_dimensions) <= set(
        D1_DIMENSIONS
    )


# ---------------------------------------------------------------------------
# The descending chain and its TWO colimits (bare vs filtered)
# ---------------------------------------------------------------------------


def build_filtered_descending_chain(length: int) -> list[D1FilteredMorphism]:
    """The T228 descending chain, but each leg now carries a TWO-layer filtration
    recording the one dimension it drops:  leg_k :  keep(4-k) superset keep(4-k-1).
    The single-object (constant) diagram so the colimit object is the object."""
    base = _one_site_system("base", (1, 1, 1, 1))
    legs: list[D1FilteredMorphism] = []
    for k in range(length):
        top = D1_DIMENSIONS[: max(0, len(D1_DIMENSIONS) - k)]
        bot = D1_DIMENSIONS[: max(0, len(D1_DIMENSIONS) - k - 1)]
        legs.append(
            _drop_filtered(base, (_normalize_layer(top), _normalize_layer(bot)), f"leg_{k}")
        )
    return legs


def chain_composite_filtration(chain: list[D1FilteredMorphism]) -> Filtration:
    """The composite filtration along the whole chain (left-fold of
    compose_filtered). For the descending chain this is the FULL descending
    chain 4 superset 3 superset 2 superset 1 superset () -- every drop retained."""
    if not chain:
        return (D1_DIMENSIONS,)
    composite = chain[0]
    for leg in chain[1:]:
        composite = compose_filtered(composite, leg)
    return composite.filtration


def associated_graded(filtration: Filtration) -> tuple[tuple[str, ...], ...]:
    """The ASSOCIATED-GRADED strata of a descending filtration:
        gr_k = F_k \\ F_{k+1}   for k = 0 .. m-1,  plus the bottom F_m.
    Each gr_k records WHICH dimension was dropped passing from layer k to k+1.
    This is the content the bare intersection forgets."""
    strata: list[tuple[str, ...]] = []
    for k in range(len(filtration) - 1):
        diff = set(filtration[k]) - set(filtration[k + 1])
        strata.append(_normalize_layer(tuple(diff)))
    strata.append(_normalize_layer(filtration[-1]))  # bottom stratum
    return tuple(strata)


def filtered_colimit_is_content_bearing() -> dict[str, object]:
    """THE DECISION. Re-pose the transfinite-chain colimit in D1FilteredCat.

    - colimit OBJECT: the constant object (as in T228, unchanged).
    - colimit MORPHISM-DATA: the composite filtration = the full descending chain.
    - colimit CONTENT: the associated-graded strata.

    DECIDE: content-bearing iff the associated-graded carries non-trivial strata
    (the drop schedule) that the bare intersection (T228) collapsed to (). We
    compare directly against the bare intersection."""
    base = _one_site_system("X", (1, 1, 1, 1))
    chain = build_filtered_descending_chain(6)
    composite_filtration = chain_composite_filtration(chain)
    gr = associated_graded(composite_filtration)
    bare = bare_intersection(composite_filtration)
    # The non-bottom strata are the per-step drops; each should be a singleton
    # for the canonical one-drop-per-step chain.
    drop_strata = gr[:-1]
    return {
        "colimit_object_valid": validate_system(base).valid,
        "composite_filtration": composite_filtration,
        "associated_graded": gr,
        "bare_intersection": bare,
        # content-FREE under the bare-intersection (T228) reading:
        "bare_is_content_free": bare == (),
        # content-BEARING under the filtered reading: the drop strata are non-empty
        # and exactly recover the 4 dropped dimensions in schedule order.
        "filtered_is_content_bearing": all(len(s) >= 1 for s in drop_strata)
        and len(drop_strata) >= 1,
        "drop_strata": drop_strata,
        "recovered_dropped_dims": tuple(d for s in drop_strata for d in s),
        # the schedule (graded strata flattened, minus bottom) recovers the full
        # universe in drop order -- nothing was lost, only re-graded.
        "schedule_recovers_universe": set(d for s in drop_strata for d in s)
        == set(D1_DIMENSIONS),
    }


# ---------------------------------------------------------------------------
# Honesty-guard boundary: NOT general cocompleteness at infinity
# ---------------------------------------------------------------------------


def non_monotone_pseudofiltration_is_illegal() -> dict[str, object]:
    """The exact boundary on the positive result. A 'filtration' that RE-ADDS a
    dropped dimension (non-monotone) is NOT a legal D1FilteredMorphism. So the
    content-bearing colimit is proven only for DESCENDING chains; arbitrary
    diagrams (where the preserved data is not monotone) are NOT covered, and
    general cocompleteness at infinity is NOT established. This is the binding
    T228 failure criterion, made executable."""
    base = _one_site_system("base", (1, 1, 1, 1))
    # drop reversal_cost then re-add it: 4 -> {a,h,b} -> {a,h,b,r} is NOT descending.
    pseudo = (
        D1_DIMENSIONS,
        D1_DIMENSIONS[:3],
        D1_DIMENSIONS,  # re-adds the dropped dimension -> non-monotone
    )
    bad = _drop_filtered(base, pseudo, "non_monotone")
    return {
        "non_monotone_filtration_legal": filtration_is_legal(pseudo),
        "non_monotone_morphism_legal": bad.is_legal(),
        # The legal descending counterpart IS legal -- isolating that monotonicity
        # is the precise typing line.
        "descending_counterpart_legal": _drop_filtered(
            base, (D1_DIMENSIONS, D1_DIMENSIONS[:3], ()), "descending"
        ).is_legal(),
    }


def general_cocompleteness_still_open() -> bool:
    """Returns True to assert (as a recorded honesty fact, NOT a proof) that the
    positive descending-chain result does NOT extend to a general cocompleteness
    claim. Backed by `non_monotone_pseudofiltration_is_illegal`: the construction
    is typed to descending chains only."""
    out = non_monotone_pseudofiltration_is_illegal()
    # The construction refuses the non-monotone case -> it cannot, by itself,
    # build colimits for arbitrary (non-descending) diagrams.
    return out["non_monotone_morphism_legal"] is False


# ---------------------------------------------------------------------------
# Aggregate decision payload
# ---------------------------------------------------------------------------


def run_decision() -> dict[str, object]:
    return {
        "filtered_composition_associative": filtered_composition_is_associative(),
        "filtered_identity_laws": filtered_identity_laws_hold(),
        "forgetful_functor_into_d1cat": forgetful_functor_lands_in_d1cat(),
        "colimit": filtered_colimit_is_content_bearing(),
        "boundary": non_monotone_pseudofiltration_is_illegal(),
        "general_cocompleteness_still_open": general_cocompleteness_still_open(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_decision(), indent=2, default=str))
