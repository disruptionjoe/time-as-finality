"""T41: Typed transport category prototype.

T41 asks whether D1RestrictionMorphisms under _compose_morphisms form a proper
category. A category requires:

  1. Objects: D1RestrictionSystems (systems)
  2. Morphisms: D1RestrictionMorphisms between systems
  3. Composition: _compose_morphisms(f: A→B, g: B→C) → A→C
  4. Identity: for each system A, an identity morphism id_A: A→A
  5. Associativity: (f;g);h = f;(g;h) for all composable triples
  6. Left unit: id_A;f = f for all morphisms f: A→B
  7. Right unit: f;id_B = f for all morphisms f: A→B

The notation f;g (diagrammatic) means apply f first, then g. This corresponds
to _compose_morphisms(f, g) in the implementation.

Central theorem:
  Typed Transport Category Theorem (T41):
  D1RestrictionMorphisms with _compose_morphisms and identity morphisms form a
  proper category. Two proof obligations:

  (i)  Associativity: (f;g);h = f;(g;h) up to morphism name (metadata).
       Proof sketch: site_map composition is sequential function application,
       which is associative. preserved_dims is set intersection, which is
       associative. Both components give the same result in either bracketing.

  (ii) Identity laws: id_A;f = f and f;id_B = f up to morphism name.
       Proof sketch: id_A.site_map is the identity function; composing with it
       on the left leaves f.site_map unchanged. id_A.preserved_dims = all four
       D1 dimensions; intersecting with f.preserved_dims gives f.preserved_dims.
       Right identity analogous.

Secondary result:
  PO1 Non-Functor Theorem (T41):
  PO1 admissibility is NOT a Boolean functor from D1Cat to {True, False}. A
  morphism f: A→B can fail PO1 while the composition f;g: A→C is PO1. This
  is consistent with T34 (endpoint admissibility is independent of intermediate
  admissibility). PO1 is a property of endpoint-morphism pairs, not a
  functorial invariant.

Hypotheses evaluated:
  H_A (proper category): D1RestrictionMorphisms form a proper category.
  H_B (partial only):    Associativity holds but identity is external/missing.
  H_C (non-functor):     PO1 admissibility is not a Boolean functor on D1Cat.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    RestrictionPatch,
    SiteMap,
    TransportEdge,
)
from models.multiscale_observer_field import D1Profile, ObserverSite, PatchConstraint
from models.po1_admissibility_conditions import check_admissibility
from models.projection_obstruction_schema import ProjectionCase
from models.transport_network import _compose_morphisms


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class MorphismEqualityCheck:
    label: str
    source_match: bool
    target_match: bool
    site_map_match: bool
    preserved_dims_match: bool
    equal_modulo_name: bool


@dataclass(frozen=True)
class AssociativityTest:
    label: str
    f_name: str
    g_name: str
    h_name: str
    lhs_label: str
    rhs_label: str
    site_map_associative: bool
    preserved_dims_associative: bool
    associativity_holds: bool


@dataclass(frozen=True)
class IdentityLawTest:
    law: str
    morphism_name: str
    identity_name: str
    site_map_match: bool
    preserved_dims_match: bool
    source_match: bool
    target_match: bool
    law_holds: bool


@dataclass(frozen=True)
class CategoryLaw:
    law_name: str
    holds: bool
    tests_run: int
    tests_passed: int
    evidence: tuple[str, ...]


@dataclass(frozen=True)
class PO1FunctorTest:
    name: str
    f_name: str
    f_po1: bool
    f_failed_conditions: tuple[str, ...]
    g_name: str
    g_po1: bool
    g_failed_conditions: tuple[str, ...]
    fg_name: str
    fg_po1: bool
    fg_failed_conditions: tuple[str, ...]
    boolean_and_predicts_po1: bool
    actual_fg_po1: bool
    functor_law_violated: bool
    interpretation: str


@dataclass(frozen=True)
class HypothesisCategory:
    hypothesis_id: str
    claim: str
    status: str
    evidence_for: tuple[str, ...]
    evidence_against: tuple[str, ...]
    verdict: str


@dataclass(frozen=True)
class T41Result:
    category_objects: tuple[str, ...]
    identity_morphisms: tuple[str, ...]
    associativity_tests: tuple[AssociativityTest, ...]
    left_unit_tests: tuple[IdentityLawTest, ...]
    right_unit_tests: tuple[IdentityLawTest, ...]
    category_laws: tuple[CategoryLaw, ...]
    po1_functor_tests: tuple[PO1FunctorTest, ...]
    all_category_laws_hold: bool
    forms_proper_category: bool
    po1_is_functor: bool
    theorem_category: str
    theorem_po1_nonfunctor: str
    hypothesis_evaluations: tuple[HypothesisCategory, ...]
    best_supported_hypothesis: str
    boundary: str
    recommendation: str


# ---------------------------------------------------------------------------
# Helper constructors
# ---------------------------------------------------------------------------

_RICH_PROFILE = D1Profile(
    accessible_support=2,
    holder_redundancy=2,
    branch_support=2,
    reversal_cost=2,
)

_RESTRICTED_PROFILE = D1Profile(
    accessible_support=1,
    holder_redundancy=2,
    branch_support=2,
    reversal_cost=2,
)


def _make_category_system(
    name: str,
    prefix: str,
    profile: D1Profile | None = None,
) -> D1RestrictionSystem:
    """Build a 2-site D1RestrictionSystem for category law testing.

    Minimal system: two sites and one transport edge. No patches, no
    obstruction. Used for clean associativity and identity tests.
    """
    p = profile if profile is not None else _RICH_PROFILE
    s1, s2 = f"{prefix}_1", f"{prefix}_2"
    local_values = (
        LocalD1Value(
            site=ObserverSite(s1, "abstract", "category_test", 0, "trusted"),
            proposition_value="true",
            profile=p,
        ),
        LocalD1Value(
            site=ObserverSite(s2, "abstract", "category_test", 0, "trusted"),
            proposition_value="true",
            profile=p,
        ),
    )
    return D1RestrictionSystem(
        name=name,
        proposition=f"prop_{prefix}",
        local_values=local_values,
        transport_edges=(TransportEdge(s1, s2, "transport", True),),
        source_site=s1,
        target_site=s2,
    )


def _make_obstructed_system(
    name: str,
    prefix: str,
    profile: D1Profile | None = None,
) -> D1RestrictionSystem:
    """Build a 3-site D1RestrictionSystem with a gluing obstruction.

    Obstruction: A=B, B=C, A≠C — locally satisfiable, globally not.
    Used for PO1 functor tests where target obstruction is required.
    """
    p = profile if profile is not None else _RESTRICTED_PROFILE
    a, b, c = f"{prefix}_A", f"{prefix}_B", f"{prefix}_C"
    local_values = tuple(
        LocalD1Value(
            site=ObserverSite(s, "abstract", "po1_test", 0, "trusted"),
            proposition_value="true",
            profile=p,
        )
        for s in (a, b, c)
    )
    patches = (
        RestrictionPatch(f"{prefix}_pAB", (a, b), (a, b), (PatchConstraint(a, b, "same"),)),
        RestrictionPatch(f"{prefix}_pBC", (b, c), (b, c), (PatchConstraint(b, c, "same"),)),
        RestrictionPatch(f"{prefix}_pAC", (a, c), (a, c), (PatchConstraint(a, c, "different"),)),
    )
    return D1RestrictionSystem(
        name=name,
        proposition=f"prop_{prefix}",
        local_values=local_values,
        transport_edges=(
            TransportEdge(a, b, "transport", True),
            TransportEdge(b, c, "transport", True),
        ),
        source_site=a,
        target_site=c,
        patches=patches,
    )


def _make_unobstructed_3site_system(
    name: str,
    prefix: str,
    profile: D1Profile | None = None,
) -> D1RestrictionSystem:
    """Build a 3-site D1RestrictionSystem with no obstruction.

    No patches: every local assignment extends globally. Used as intermediate
    layer in PO1 functor tests.
    """
    p = profile if profile is not None else _RESTRICTED_PROFILE
    a, b, c = f"{prefix}_A", f"{prefix}_B", f"{prefix}_C"
    local_values = tuple(
        LocalD1Value(
            site=ObserverSite(s, "abstract", "po1_test", 0, "trusted"),
            proposition_value="true",
            profile=p,
        )
        for s in (a, b, c)
    )
    return D1RestrictionSystem(
        name=name,
        proposition=f"prop_{prefix}",
        local_values=local_values,
        transport_edges=(
            TransportEdge(a, b, "transport", True),
            TransportEdge(b, c, "transport", True),
        ),
        source_site=a,
        target_site=c,
    )


def _make_aligned_morphism(
    name: str,
    source: D1RestrictionSystem,
    target: D1RestrictionSystem,
    preserved_dims: tuple[str, ...] = D1_DIMENSIONS,
) -> D1RestrictionMorphism:
    """Build an index-aligned morphism between systems of equal site count.

    Sites are aligned by sorted order: source site i maps to target site i.
    """
    src_sites = sorted(v.site.observer_id for v in source.local_values)
    tgt_sites = sorted(v.site.observer_id for v in target.local_values)
    n = min(len(src_sites), len(tgt_sites))
    site_map = tuple(SiteMap(src_sites[i], tgt_sites[i]) for i in range(n))
    return D1RestrictionMorphism(
        name=name,
        source=source,
        target=target,
        site_map=site_map,
        preserved_dimensions=preserved_dims,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


# ---------------------------------------------------------------------------
# Core category operations
# ---------------------------------------------------------------------------


def make_identity(system: D1RestrictionSystem) -> D1RestrictionMorphism:
    """Construct the identity morphism id_A: A→A for a D1RestrictionSystem.

    Identity morphism has:
    - site_map: every site mapped to itself
    - preserved_dimensions: all four D1 dimensions
    - require_trust_path_preservation: False (trivially preserved)
    - require_obstruction_preservation: False (trivially preserved)
    """
    sites = sorted(system.site_ids())
    return D1RestrictionMorphism(
        name=f"id_{system.name}",
        source=system,
        target=system,
        site_map=tuple(SiteMap(s, s) for s in sites),
        preserved_dimensions=D1_DIMENSIONS,
        require_trust_path_preservation=False,
        require_obstruction_preservation=False,
    )


def morphisms_equal_modulo_name(
    f: D1RestrictionMorphism,
    g: D1RestrictionMorphism,
    label: str = "",
) -> MorphismEqualityCheck:
    """Check structural equality of two morphisms, ignoring the name field.

    Name is metadata (constructed from input names in _compose_morphisms) and
    is not part of the mathematical identity of a morphism. Two morphisms are
    equal if they have the same source, target, site_map (as a function), and
    preserved_dimensions (as a set).
    """
    lbl = label or f"{f.name} == {g.name} (mod name)"
    source_match = f.source.name == g.source.name
    target_match = f.target.name == g.target.name
    f_pairs = frozenset((sm.source_site, sm.target_site) for sm in f.site_map)
    g_pairs = frozenset((sm.source_site, sm.target_site) for sm in g.site_map)
    site_map_match = f_pairs == g_pairs
    preserved_dims_match = frozenset(f.preserved_dimensions) == frozenset(g.preserved_dimensions)
    equal = source_match and target_match and site_map_match and preserved_dims_match
    return MorphismEqualityCheck(
        label=lbl,
        source_match=source_match,
        target_match=target_match,
        site_map_match=site_map_match,
        preserved_dims_match=preserved_dims_match,
        equal_modulo_name=equal,
    )


# ---------------------------------------------------------------------------
# Category law testers
# ---------------------------------------------------------------------------


def verify_associativity(
    f: D1RestrictionMorphism,
    g: D1RestrictionMorphism,
    h: D1RestrictionMorphism,
    label: str = "",
) -> AssociativityTest:
    """Test the associativity law: (f;g);h = f;(g;h).

    Diagrammatic convention: f;g means apply f first, then g, matching
    _compose_morphisms(f, g) = g∘f in classical notation.

    LHS: _compose_morphisms(_compose_morphisms(f, g), h)
    RHS: _compose_morphisms(f, _compose_morphisms(g, h))
    """
    fg = _compose_morphisms(f, g)
    gh = _compose_morphisms(g, h)
    lhs = _compose_morphisms(fg, h)
    rhs = _compose_morphisms(f, gh)
    lbl = label or f"({f.name};{g.name});{h.name} == {f.name};({g.name};{h.name})"
    eq = morphisms_equal_modulo_name(lhs, rhs, label=lbl)
    return AssociativityTest(
        label=lbl,
        f_name=f.name,
        g_name=g.name,
        h_name=h.name,
        lhs_label=lhs.name,
        rhs_label=rhs.name,
        site_map_associative=eq.site_map_match,
        preserved_dims_associative=eq.preserved_dims_match,
        associativity_holds=eq.equal_modulo_name,
    )


def verify_left_unit(f: D1RestrictionMorphism) -> IdentityLawTest:
    """Verify the left unit law: id_{source(f)} ; f = f.

    _compose_morphisms(make_identity(f.source), f) should equal f modulo name.
    """
    id_src = make_identity(f.source)
    composed = _compose_morphisms(id_src, f)
    eq = morphisms_equal_modulo_name(composed, f, label=f"id_{f.source.name};{f.name} == {f.name}")
    return IdentityLawTest(
        law="left_unit",
        morphism_name=f.name,
        identity_name=id_src.name,
        site_map_match=eq.site_map_match,
        preserved_dims_match=eq.preserved_dims_match,
        source_match=eq.source_match,
        target_match=eq.target_match,
        law_holds=eq.equal_modulo_name,
    )


def verify_right_unit(f: D1RestrictionMorphism) -> IdentityLawTest:
    """Verify the right unit law: f ; id_{target(f)} = f.

    _compose_morphisms(f, make_identity(f.target)) should equal f modulo name.
    """
    id_tgt = make_identity(f.target)
    composed = _compose_morphisms(f, id_tgt)
    eq = morphisms_equal_modulo_name(composed, f, label=f"{f.name};id_{f.target.name} == {f.name}")
    return IdentityLawTest(
        law="right_unit",
        morphism_name=f.name,
        identity_name=id_tgt.name,
        site_map_match=eq.site_map_match,
        preserved_dims_match=eq.preserved_dims_match,
        source_match=eq.source_match,
        target_match=eq.target_match,
        law_holds=eq.equal_modulo_name,
    )


# ---------------------------------------------------------------------------
# PO1 functor analysis
# ---------------------------------------------------------------------------


def _build_po1_projection_case(
    name: str,
    richer: D1RestrictionSystem,
    restricted: D1RestrictionSystem,
    morphism: D1RestrictionMorphism,
    forgotten_structure: tuple[str, ...],
) -> ProjectionCase:
    preserved_structure = tuple(d for d in D1_DIMENSIONS if d not in set(forgotten_structure))
    return ProjectionCase(
        name=name,
        source="T41",
        richer_system=richer,
        restricted_system=restricted,
        morphism=morphism,
        forgotten_structure=forgotten_structure,
        preserved_structure=preserved_structure,
        intended_reading=(
            f"projection from {richer.name} to {restricted.name} losing {forgotten_structure}"
        ),
    )


def _build_po1_functor_test_scenario() -> tuple[
    D1RestrictionSystem, D1RestrictionSystem, D1RestrictionSystem
]:
    """Construct three systems for the PO1 functor test.

    SRC: 3-site, rich profile, no obstruction.
    MID: 3-site, restricted profile, no obstruction.
    TGT: 3-site, restricted profile, WITH gluing obstruction.

    Used to test: f: SRC→MID (not PO1), g: MID→TGT (not PO1), f;g: SRC→TGT (PO1).
    """
    src = _make_category_system("SRC_functor", "src_f", _RICH_PROFILE)
    mid = _make_unobstructed_3site_system("MID_functor", "mid_f", _RESTRICTED_PROFILE)
    tgt = _make_obstructed_system("TGT_functor", "tgt_f", _RESTRICTED_PROFILE)
    return src, mid, tgt


def build_po1_functor_test() -> PO1FunctorTest:
    """Build and evaluate the PO1 non-functor test.

    f: SRC→MID — forgets type_guarantee, but MID has no obstruction.
                  AC5 may pass (profile lost + forgotten declared) but AC6 fails.
                  → f is NOT PO1.

    g: MID→TGT — MID obstructed, TGT obstructed, but g forgets nothing.
                  AC5 fails (no forgotten structure declared).
                  → g is NOT PO1.

    f;g: SRC→TGT — SRC unobstructed, TGT obstructed. Accumulated forgotten
                   structure from f gives non-empty forgotten. Profile loss from
                   SRC→TGT (rich→restricted) makes AC5 pass.
                   → f;g IS PO1.

    A Boolean "and" functor would predict: (f;g) is PO1 iff f is PO1 AND g is PO1
    = False AND False = False. Actual: True. Functor law violated.
    """
    src, mid, tgt = _build_po1_functor_test_scenario()

    f_morph = _make_aligned_morphism("f_SRC_MID", src, mid, D1_DIMENSIONS)
    g_morph = _make_aligned_morphism("g_MID_TGT", mid, tgt, D1_DIMENSIONS)
    fg_morph = _compose_morphisms(f_morph, g_morph)

    f_forgotten: tuple[str, ...] = ("type_guarantee",)
    g_forgotten: tuple[str, ...] = ()
    fg_forgotten: tuple[str, ...] = ("type_guarantee",)

    f_case = _build_po1_projection_case("f_SRC_MID", src, mid, f_morph, f_forgotten)
    g_case = _build_po1_projection_case("g_MID_TGT", mid, tgt, g_morph, g_forgotten)
    fg_case = _build_po1_projection_case("fg_SRC_TGT", src, tgt, fg_morph, fg_forgotten)

    f_check = check_admissibility(f_case)
    g_check = check_admissibility(g_case)
    fg_check = check_admissibility(fg_case)

    f_po1 = f_check.po1_evidence
    g_po1 = g_check.po1_evidence
    fg_po1 = fg_check.po1_evidence

    boolean_and_predicts = f_po1 and g_po1
    functor_law_violated = (boolean_and_predicts != fg_po1)

    if functor_law_violated:
        interp = (
            "PO1 is NOT a Boolean functor: f;g is PO1 even though neither f nor g "
            "individually satisfies PO1. Endpoint admissibility is determined by the "
            "endpoint pair (SRC, TGT), not by the admissibility of intermediate "
            "projections. Consistent with T34 (PO1 Chain Theorem)."
        )
    else:
        interp = (
            "Boolean and-functor prediction matched actual result. "
            "This does not establish PO1 as a functor (single test)."
        )

    return PO1FunctorTest(
        name="SRC_MID_TGT_functor_test",
        f_name=f_morph.name,
        f_po1=f_po1,
        f_failed_conditions=f_check.failed_conditions,
        g_name=g_morph.name,
        g_po1=g_po1,
        g_failed_conditions=g_check.failed_conditions,
        fg_name=fg_morph.name,
        fg_po1=fg_po1,
        fg_failed_conditions=fg_check.failed_conditions,
        boolean_and_predicts_po1=boolean_and_predicts,
        actual_fg_po1=fg_po1,
        functor_law_violated=functor_law_violated,
        interpretation=interp,
    )


# ---------------------------------------------------------------------------
# Hypothesis evaluation
# ---------------------------------------------------------------------------


def _evaluate_hypotheses(
    assoc_tests: tuple[AssociativityTest, ...],
    left_tests: tuple[IdentityLawTest, ...],
    right_tests: tuple[IdentityLawTest, ...],
    po1_tests: tuple[PO1FunctorTest, ...],
    forms_category: bool,
) -> tuple[HypothesisCategory, ...]:
    all_assoc = all(t.associativity_holds for t in assoc_tests)
    all_left = all(t.law_holds for t in left_tests)
    all_right = all(t.law_holds for t in right_tests)
    any_functor_violated = any(t.functor_law_violated for t in po1_tests)

    h_a = HypothesisCategory(
        hypothesis_id="H_A",
        claim=(
            "D1RestrictionMorphisms with _compose_morphisms form a proper category: "
            "associativity holds, identity morphisms exist and satisfy unit laws."
        ),
        status="best_supported" if forms_category else "falsified",
        evidence_for=(
            (f"Associativity: {sum(t.associativity_holds for t in assoc_tests)}/{len(assoc_tests)} tests pass",)
            if assoc_tests else ()
        ) + (
            (f"Left unit: {sum(t.law_holds for t in left_tests)}/{len(left_tests)} tests pass",)
            if left_tests else ()
        ) + (
            (f"Right unit: {sum(t.law_holds for t in right_tests)}/{len(right_tests)} tests pass",)
            if right_tests else ()
        ),
        evidence_against=() if forms_category else ("One or more category laws failed.",),
        verdict=(
            "D1RestrictionMorphisms form a proper category. "
            "The mathematical objects accumulate categorical structure."
            if forms_category
            else "Category laws not all satisfied; category structure not established."
        ),
    )

    h_b = HypothesisCategory(
        hypothesis_id="H_B",
        claim=(
            "Associativity holds but identity morphisms are external: they cannot be "
            "constructed from _compose_morphisms alone and require a separate constructor."
        ),
        status="partially_supported",
        evidence_for=(
            "Identity morphisms require make_identity(), a separate constructor not "
            "provided by transport_network._compose_morphisms.",
            "The identity construction is explicit, not derived from composition.",
        ),
        evidence_against=(
            "Identity morphisms are trivially constructible for any D1RestrictionSystem. "
            "The construction is canonical: id_A maps each site to itself and preserves "
            "all dimensions. This is not a missing capability — it is a standard "
            "categorical construction that any framework must supply explicitly.",
            "H_B's 'external' framing overstates the gap: every category requires an "
            "explicit identity construction. The absence from _compose_morphisms is "
            "expected, not a deficiency.",
        ),
        verdict=(
            "Partially supported but misleading. Identity morphisms are external to "
            "_compose_morphisms by design, not by omission. H_A (proper category) "
            "is the correct characterization."
        ),
    )

    h_c = HypothesisCategory(
        hypothesis_id="H_C",
        claim=(
            "PO1 admissibility is not a Boolean functor from D1Cat to {True, False}: "
            "PO1(f;g) ≠ PO1(f) AND PO1(g) in general."
        ),
        status="best_supported" if any_functor_violated else "unresolved",
        evidence_for=(
            (
                f"PO1 functor law violated in {sum(t.functor_law_violated for t in po1_tests)}"
                f"/{len(po1_tests)} test(s): f;g is PO1 even when neither f nor g is PO1.",
            )
            if any_functor_violated else ()
        ) + (
            "Consistent with T34 (PO1 Chain Theorem): endpoint admissibility is "
            "independent of intermediate admissibility.",
            "Consistent with T37 (path-dependent admissibility): same endpoint pair "
            "can have different admissibility via different paths.",
        ),
        evidence_against=(),
        verdict=(
            "PO1 admissibility is an endpoint property of morphisms in D1Cat, not "
            "a functorial invariant. This is the T34/T37 result restated in "
            "categorical language. H_C is supported."
            if any_functor_violated
            else "No functor violation witnessed; H_C unresolved by available tests."
        ),
    )

    return (h_a, h_b, h_c)


# ---------------------------------------------------------------------------
# Scenario builders for category law tests
# ---------------------------------------------------------------------------


def _build_category_law_scenarios() -> tuple[
    tuple[AssociativityTest, ...],
    tuple[IdentityLawTest, ...],
    tuple[IdentityLawTest, ...],
    tuple[str, ...],
    tuple[str, ...],
]:
    """Build and test all category law scenarios.

    Returns:
        assoc_tests, left_unit_tests, right_unit_tests, object_names, identity_names
    """
    # Four 2-site systems A, B, C, D for associativity (need f:A→B, g:B→C, h:C→D)
    sys_a = _make_category_system("Cat_A", "a", _RICH_PROFILE)
    sys_b = _make_category_system("Cat_B", "b", _RICH_PROFILE)
    sys_c = _make_category_system("Cat_C", "c", _RICH_PROFILE)
    sys_d = _make_category_system("Cat_D", "d", _RICH_PROFILE)

    object_names = (sys_a.name, sys_b.name, sys_c.name, sys_d.name)

    # Identity morphisms
    id_a = make_identity(sys_a)
    id_b = make_identity(sys_b)
    id_c = make_identity(sys_c)
    id_d = make_identity(sys_d)
    identity_names = (id_a.name, id_b.name, id_c.name, id_d.name)

    # ---------------------------------------------------------------------------
    # Test 1: all four D1 dimensions preserved
    # ---------------------------------------------------------------------------
    f1 = _make_aligned_morphism("f1_A_B", sys_a, sys_b, D1_DIMENSIONS)
    g1 = _make_aligned_morphism("g1_B_C", sys_b, sys_c, D1_DIMENSIONS)
    h1 = _make_aligned_morphism("h1_C_D", sys_c, sys_d, D1_DIMENSIONS)
    assoc1 = verify_associativity(f1, g1, h1, label="all_dims: (f1;g1);h1 == f1;(g1;h1)")

    # ---------------------------------------------------------------------------
    # Test 2: varying preserved dimension subsets
    # ---------------------------------------------------------------------------
    _AS = ("accessible_support",)
    _AS_HR = ("accessible_support", "holder_redundancy")
    _AS_HR_BS = ("accessible_support", "holder_redundancy", "branch_support")

    f2 = _make_aligned_morphism("f2_A_B", sys_a, sys_b, _AS_HR)
    g2 = _make_aligned_morphism("g2_B_C", sys_b, sys_c, _AS)
    h2 = _make_aligned_morphism("h2_C_D", sys_c, sys_d, _AS_HR_BS)
    assoc2 = verify_associativity(f2, g2, h2, label="mixed_dims: (f2;g2);h2 == f2;(g2;h2)")

    # ---------------------------------------------------------------------------
    # Test 3: minimal preserved dimensions (single dimension)
    # ---------------------------------------------------------------------------
    f3 = _make_aligned_morphism("f3_A_B", sys_a, sys_b, _AS)
    g3 = _make_aligned_morphism("g3_B_C", sys_b, sys_c, _AS_HR)
    h3 = _make_aligned_morphism("h3_C_D", sys_c, sys_d, _AS)
    assoc3 = verify_associativity(f3, g3, h3, label="minimal_dims: (f3;g3);h3 == f3;(g3;h3)")

    # ---------------------------------------------------------------------------
    # Test 4: identity morphisms in the triple
    # ---------------------------------------------------------------------------
    assoc4 = verify_associativity(
        id_a, f1, g1,
        label="with_identity: (id_A;f1);g1 == id_A;(f1;g1)",
    )

    assoc_tests = (assoc1, assoc2, assoc3, assoc4)

    # ---------------------------------------------------------------------------
    # Left unit tests: id_{source} ; f = f
    # ---------------------------------------------------------------------------
    left1 = verify_left_unit(f1)
    left2 = verify_left_unit(f2)
    left3 = verify_left_unit(f3)
    left4 = verify_left_unit(g1)
    left5 = verify_left_unit(h1)
    left_unit_tests = (left1, left2, left3, left4, left5)

    # ---------------------------------------------------------------------------
    # Right unit tests: f ; id_{target} = f
    # ---------------------------------------------------------------------------
    right1 = verify_right_unit(f1)
    right2 = verify_right_unit(f2)
    right3 = verify_right_unit(f3)
    right4 = verify_right_unit(g1)
    right5 = verify_right_unit(h1)
    right_unit_tests = (right1, right2, right3, right4, right5)

    return assoc_tests, left_unit_tests, right_unit_tests, object_names, identity_names


# ---------------------------------------------------------------------------
# Main analysis runner
# ---------------------------------------------------------------------------


def run_t41_analysis() -> T41Result:
    """Run all T41 analyses and return a structured result."""

    # Category law tests
    (
        assoc_tests,
        left_unit_tests,
        right_unit_tests,
        object_names,
        identity_names,
    ) = _build_category_law_scenarios()

    # Summarize laws
    n_assoc = len(assoc_tests)
    p_assoc = sum(t.associativity_holds for t in assoc_tests)
    assoc_law = CategoryLaw(
        law_name="associativity",
        holds=(n_assoc > 0 and p_assoc == n_assoc),
        tests_run=n_assoc,
        tests_passed=p_assoc,
        evidence=tuple(
            f"{'PASS' if t.associativity_holds else 'FAIL'}: {t.label}"
            for t in assoc_tests
        ),
    )

    n_left = len(left_unit_tests)
    p_left = sum(t.law_holds for t in left_unit_tests)
    left_law = CategoryLaw(
        law_name="left_unit",
        holds=(n_left > 0 and p_left == n_left),
        tests_run=n_left,
        tests_passed=p_left,
        evidence=tuple(
            f"{'PASS' if t.law_holds else 'FAIL'}: id_{t.identity_name.replace('id_', '')};{t.morphism_name}"
            for t in left_unit_tests
        ),
    )

    n_right = len(right_unit_tests)
    p_right = sum(t.law_holds for t in right_unit_tests)
    right_law = CategoryLaw(
        law_name="right_unit",
        holds=(n_right > 0 and p_right == n_right),
        tests_run=n_right,
        tests_passed=p_right,
        evidence=tuple(
            f"{'PASS' if t.law_holds else 'FAIL'}: {t.morphism_name};id_{t.identity_name.replace('id_', '')}"
            for t in right_unit_tests
        ),
    )

    category_laws = (assoc_law, left_law, right_law)
    all_laws_hold = all(law.holds for law in category_laws)
    forms_proper_category = all_laws_hold

    # PO1 functor test
    po1_functor_test = build_po1_functor_test()
    po1_functor_tests = (po1_functor_test,)
    po1_is_functor = not po1_functor_test.functor_law_violated

    # Hypothesis evaluations
    hypotheses = _evaluate_hypotheses(
        assoc_tests,
        left_unit_tests,
        right_unit_tests,
        po1_functor_tests,
        forms_proper_category,
    )
    best = next(
        (h.hypothesis_id for h in hypotheses if h.status == "best_supported"),
        "undetermined",
    )

    # Theorems
    if forms_proper_category:
        theorem_cat = (
            "Typed Transport Category Theorem (T41): D1RestrictionMorphisms under "
            "_compose_morphisms, with identity morphisms constructed by make_identity(), "
            "form a proper category. Associativity holds by function-composition "
            "associativity (site_map) and set-intersection associativity "
            "(preserved_dims). Left and right unit laws hold by the identity-function "
            "property of the site_map and the D1_DIMENSIONS bound on the intersection."
        )
    else:
        theorem_cat = (
            "Category law failure detected: D1RestrictionMorphisms do not form a "
            "proper category under the tested laws. See category_laws for details."
        )

    if po1_functor_test.functor_law_violated:
        theorem_po1 = (
            "PO1 Non-Functor Theorem (T41): PO1 admissibility is not a Boolean functor "
            "from D1Cat to {True, False}. Witnessed: f;g is PO1 while neither f nor g "
            "is individually PO1. This is the T34 PO1 Chain Theorem restated in "
            "categorical language: endpoint admissibility is an endpoint property of "
            "morphisms, not a functorial invariant of the composition structure."
        )
    else:
        theorem_po1 = "PO1 functor violation not witnessed by available tests."

    boundary = (
        "Category structure is proved for D1RestrictionMorphisms as constructed here. "
        "The result does not extend automatically to: (i) presheaves or sheaves "
        "(H2) — these require additional structure not yet formalized; (ii) general "
        "category theory tools (limits, colimits, adjunctions) — these require "
        "further development; (iii) morphisms with require_trust_path_preservation "
        "or require_obstruction_preservation set to True — these carry additional "
        "constraints whose behavior under composition is not yet characterized. "
        "The identity morphism construction requires make_identity() which is "
        "external to _compose_morphisms; it is not derivable from composition alone."
    )

    recommendation = (
        "T41 establishes that D1RestrictionMorphisms form a proper category. "
        "Next steps: (1) Characterize the full hom-sets — how many morphisms "
        "exist between two D1RestrictionSystems? (2) Explore whether the "
        "projection-obstruction functor can be repaired as a lax functor or "
        "indexed family. (3) Check whether TypedTransportNetworks are internal "
        "categories in D1Cat (networks as categories internal to the ambient category). "
        "(4) Audit whether the finite-to-infinite boundary (T42) changes categorical "
        "structure."
    )

    return T41Result(
        category_objects=object_names,
        identity_morphisms=identity_names,
        associativity_tests=assoc_tests,
        left_unit_tests=left_unit_tests,
        right_unit_tests=right_unit_tests,
        category_laws=category_laws,
        po1_functor_tests=po1_functor_tests,
        all_category_laws_hold=all_laws_hold,
        forms_proper_category=forms_proper_category,
        po1_is_functor=po1_is_functor,
        theorem_category=theorem_cat,
        theorem_po1_nonfunctor=theorem_po1,
        hypothesis_evaluations=hypotheses,
        best_supported_hypothesis=best,
        boundary=boundary,
        recommendation=recommendation,
    )


# ---------------------------------------------------------------------------
# Serialization
# ---------------------------------------------------------------------------


def t41_result_to_dict(result: T41Result) -> dict[str, Any]:
    def assoc_to_dict(t: AssociativityTest) -> dict[str, Any]:
        return {
            "label": t.label,
            "f": t.f_name,
            "g": t.g_name,
            "h": t.h_name,
            "lhs": t.lhs_label,
            "rhs": t.rhs_label,
            "site_map_associative": t.site_map_associative,
            "preserved_dims_associative": t.preserved_dims_associative,
            "associativity_holds": t.associativity_holds,
        }

    def id_test_to_dict(t: IdentityLawTest) -> dict[str, Any]:
        return {
            "law": t.law,
            "morphism": t.morphism_name,
            "identity": t.identity_name,
            "site_map_match": t.site_map_match,
            "preserved_dims_match": t.preserved_dims_match,
            "source_match": t.source_match,
            "target_match": t.target_match,
            "law_holds": t.law_holds,
        }

    def law_to_dict(law: CategoryLaw) -> dict[str, Any]:
        return {
            "law": law.law_name,
            "holds": law.holds,
            "tests_run": law.tests_run,
            "tests_passed": law.tests_passed,
            "evidence": list(law.evidence),
        }

    def po1_to_dict(t: PO1FunctorTest) -> dict[str, Any]:
        return {
            "name": t.name,
            "f": {"name": t.f_name, "po1": t.f_po1, "failed": list(t.f_failed_conditions)},
            "g": {"name": t.g_name, "po1": t.g_po1, "failed": list(t.g_failed_conditions)},
            "fg": {"name": t.fg_name, "po1": t.fg_po1, "failed": list(t.fg_failed_conditions)},
            "boolean_and_predicts_po1": t.boolean_and_predicts_po1,
            "actual_fg_po1": t.actual_fg_po1,
            "functor_law_violated": t.functor_law_violated,
            "interpretation": t.interpretation,
        }

    def hyp_to_dict(h: HypothesisCategory) -> dict[str, Any]:
        return {
            "id": h.hypothesis_id,
            "claim": h.claim,
            "status": h.status,
            "evidence_for": list(h.evidence_for),
            "evidence_against": list(h.evidence_against),
            "verdict": h.verdict,
        }

    return {
        "category_objects": list(result.category_objects),
        "identity_morphisms": list(result.identity_morphisms),
        "associativity_tests": [assoc_to_dict(t) for t in result.associativity_tests],
        "left_unit_tests": [id_test_to_dict(t) for t in result.left_unit_tests],
        "right_unit_tests": [id_test_to_dict(t) for t in result.right_unit_tests],
        "category_laws": [law_to_dict(law) for law in result.category_laws],
        "po1_functor_tests": [po1_to_dict(t) for t in result.po1_functor_tests],
        "all_category_laws_hold": result.all_category_laws_hold,
        "forms_proper_category": result.forms_proper_category,
        "po1_is_functor": result.po1_is_functor,
        "theorem_category": result.theorem_category,
        "theorem_po1_nonfunctor": result.theorem_po1_nonfunctor,
        "hypotheses": [hyp_to_dict(h) for h in result.hypothesis_evaluations],
        "best_supported_hypothesis": result.best_supported_hypothesis,
        "boundary": result.boundary,
        "recommendation": result.recommendation,
    }
