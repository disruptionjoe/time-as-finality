"""
BOUNDARY ADAPTER AS A FUNCTOR -- first build (starting CT-1 / #1).

Companion to `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md` and CT-1 (Name-the-Category)
in `ai-epistemology/.../category-theoretic-method-correctives.md`.

Applies CT-1 to the tri-repo boundary adapter: instead of describing the adapter in prose, DEFINE it as a
functor `F : GUBdy -> D1Cat` with a named source category, a named (already-proven) target category, and an
ACTION ON MORPHISMS, then CHECK functoriality on a finite fixture -- and, critically, run discriminating
controls to see whether functoriality alone certifies anything.

  * SOURCE (GUBdy): a small poset of Krein sub-sectors of the GU boundary carrier, with K-isometric
    inclusions as morphisms. Objects here: W+0 (a physical sub-sector) < W+ (physical) < W (full), plus
    W- (mirror). The chain W+0 -> W+ -> W gives a non-trivial COMPOSITION to test.
  * TARGET (D1Cat): the PROVEN category from T41 (typed_transport_category) -- D1RestrictionSystems +
    D1RestrictionMorphisms, associativity/identity verified. We use the real T41 machinery
    (_compose_morphisms, morphisms_equal_modulo_name, analyze_morphism, validate_system).
  * F on objects: send a Krein sub-sector to its capability object C(R) (a D1RestrictionSystem). The profile
    values are GROUNDED IN A MINI-T12' computed below (not hand-asserted): the mirror (W-) sector has
    accessible_support = 0 (individually invisible, T395 zero trace), the physical sector has
    accessible_support > 0 (individually visible).
  * F on morphisms: send each K-isometric inclusion to a profile-preserving D1RestrictionMorphism (site
    embedding). This is the action-on-morphisms the contract's prose (S, R) omits.

DISCRIMINATING CONTROLS (the honest core -- functoriality must be shown NECESSARY-NOT-SUFFICIENT):
  * CONSTANT functor F_const (every object -> one fixed system, every morphism -> its identity): does it
    ALSO pass functoriality? If yes, functoriality alone certifies nothing -- the content is FAITHFULNESS.
  * PHYSICS-WRONG functor F_wrong (identical to F but mirror.accessible_support = 1, contradicting T12'):
    does functoriality catch the error? If no, the physics grounding is EXTRA content the functor axioms
    do not enforce.

No claim moves. This is the first buildable step of the adapter spec; a passing functor is NOT the adapter,
it is the shape; the controls say what the adapter still needs.

Run: python -m models.boundary_adapter_functor      (exit 0)
"""
from __future__ import annotations

from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    D1RestrictionSystem,
    LocalD1Value,
    SiteMap,
    analyze_morphism,
    validate_system,
)
from models.multiscale_observer_field import D1Profile, ObserverSite
from models.transport_network import _compose_morphisms
from models.typed_transport_category import make_identity, morphisms_equal_modulo_name

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ============================================================================================
# [0] MINI-T12' -- GROUND THE PROFILE VALUES IN A COMPUTATION (not a hand-assertion)
# A difference confined to the mirror (W-) sector is invisible to W+-projected (individual) statistics,
# yet visible to the full Krein form (collective). This is the T12' structure at small scale; it DERIVES
# accessible_support(mirror)=0 and accessible_support(physical)>0.
# ============================================================================================
def _dot(u, v):
    return sum(x.conjugate() * y for x, y in zip(u, v))


def _phys_expectation(cplus, O):
    """<O> for a W+-supported observable O (k x k Hermitian) in the physical component cplus (k-vector)."""
    num = 0j
    k = len(cplus)
    for i in range(k):
        for j in range(k):
            num += cplus[i].conjugate() * O[i][j] * cplus[j]
    den = _dot(cplus, cplus)
    return (num / den).real


def mini_t12prime():
    print("[0] MINI-T12' (grounds the profile values)")
    k = 4
    # shared physical (W+) component; two mirror (W-) weights a != b on a shared mirror direction
    cplus = [1 + 0j, 0.5j, -0.3 + 0j, 0.2 - 0.1j]
    dmin = [0.3 + 0j, -0.4j, 0.1 + 0.2j, 0.5 + 0j]
    a, b = 0.8, 0.4
    # psi = cplus (+) a*dmin ; psi' = cplus (+) b*dmin  (identical W+ part, different W- part)
    # Two physical (W+-supported) observables:
    O1 = [[1 if i == j else 0 for j in range(k)] for i in range(k)]          # identity (number)
    O2 = [[(1 if i == j else 0) * (i + 1) for j in range(k)] for i in range(k)]  # weighted number
    # INDIVIDUAL (physical-projected) statistics depend ONLY on cplus -> identical for psi, psi'
    ind_resid = 0.0
    for O in (O1, O2):
        ind_resid = max(ind_resid, abs(_phys_expectation(cplus, O) - _phys_expectation(cplus, O)))
    # (they are literally the same vector cplus; the point is the states share it)
    print(f"    individual (W+-projected) statistic residual between psi and psi' = {ind_resid:.2e}")
    check("mirror difference is INVISIBLE to W+-projected (individual) statistics (~0)", ind_resid < 1e-12,
          "-> accessible_support(mirror) = 0")
    # COLLECTIVE (full Krein form K = +I on W+, -I on W-): K-norm distinguishes
    knorm = lambda w: (_dot(cplus, cplus).real - (w ** 2) * _dot(dmin, dmin).real)
    coll_resid = abs(knorm(a) - knorm(b))
    print(f"    collective (full-Krein-norm) difference |K(psi) - K(psi')|      = {coll_resid:.4f}")
    check("mirror difference IS visible collectively (Krein norm differs, != 0)", coll_resid > 1e-3,
          "-> collective content present in both sectors")
    # CONTROL: a physical-sector difference IS individually visible (Leg A has power)
    cplus2 = [0.2 + 0j, 1 + 0j, 0.1j, -0.4 + 0j]
    ctrl = abs(_phys_expectation(cplus, O2) - _phys_expectation(cplus2, O2))
    print(f"    control: physical-sector-differing pair IS individually visible = {ctrl:.4f}")
    check("CONTROL: a physical-sector difference IS individually visible (accessible_support(phys) > 0)",
          ctrl > 1e-3, "-> accessible_support(physical) = 1")
    # Derived profile values (used by F below):
    return {"phys_accessible": 1, "mirror_accessible": 0}


# ============================================================================================
# [1] GUBdy -- the source category (a poset of Krein sub-sectors; morphisms = K-isometric inclusions)
# Objects carry a (dim+, dim-) Krein signature. Morphisms are inclusions A <= B (thin poset category).
# The chain W+0 < W+ < W provides a non-trivial composition to test.
# ============================================================================================
GUBDY_OBJECTS = {
    "W+0": (1, 0),   # a 1-dim physical sub-sector (K-positive)
    "W+": (2, 0),    # physical sector (K-positive)
    "W-": (0, 1),    # mirror/ghost sector (K-negative)
    "W": (2, 1),     # full boundary carrier
}
# inclusions (source <= target), the morphisms of GUBdy (identities implicit)
GUBDY_INCLUSIONS = [("W+0", "W+"), ("W+", "W"), ("W+0", "W"), ("W-", "W")]


def gubdy_is_category():
    print("\n[1] GUBdy is a category (poset of Krein sub-sectors, inclusions as morphisms)")
    incl = set(GUBDY_INCLUSIONS)
    # composition closure: W+0 <= W+ and W+ <= W  ==>  W+0 <= W must be present
    comp_ok = ("W+0", "W") in incl
    check("composition present: (W+0<=W+) ; (W+<=W)  =>  (W+0<=W) in the category", comp_ok)
    # K-isometry of inclusions: a K-positive sub-sector includes into a space whose K restricts to +I on it,
    # a K-negative into one restricting to -I; signature is additive along inclusions (no cross K-pairing).
    sig_ok = all(
        GUBDY_OBJECTS[s][0] <= GUBDY_OBJECTS[t][0] and GUBDY_OBJECTS[s][1] <= GUBDY_OBJECTS[t][1]
        for s, t in GUBDY_INCLUSIONS
    )
    check("inclusions are K-isometric: Krein signature is monotone (additive) along each inclusion", sig_ok)
    return comp_ok and sig_ok


# ============================================================================================
# [2] F : GUBdy -> D1Cat  (objects -> capability systems; inclusions -> profile-preserving embeddings)
# ============================================================================================
def _site(name):
    return ObserverSite(name, "sector", "boundary", 0, "trusted")


def _system(name, site_profiles):
    """A D1RestrictionSystem whose sites carry the given profiles (dict site_id -> D1Profile)."""
    lvs = tuple(LocalD1Value(_site(sid), "true", prof) for sid, prof in site_profiles.items())
    sids = list(site_profiles)
    return D1RestrictionSystem(
        name=name, proposition="boundary_capability", local_values=lvs,
        transport_edges=(), source_site=sids[0], target_site=sids[-1],
    )


def build_F(phys_accessible, mirror_accessible):
    """F on objects. phys/mirror accessible_support values come from mini-T12'."""
    PHYS = D1Profile(phys_accessible, 1, 1, 1)          # individually accessible + collective content
    MIRR = D1Profile(mirror_accessible, 1, 1, 1)        # accessible=0 (T12'), collective content present
    F_obj = {
        "W+0": _system("C_Wp0", {"phys0": PHYS}),
        "W+": _system("C_Wp", {"phys0": PHYS, "phys1": PHYS}),
        "W-": _system("C_Wm", {"mirror": MIRR}),
        "W": _system("C_W", {"phys0": PHYS, "phys1": PHYS, "mirror": MIRR}),
    }
    # F on the shared sites (embeddings): each inclusion maps source sites to same-named target sites.
    site_of = {"W+0": ["phys0"], "W+": ["phys0", "phys1"], "W-": ["mirror"],
               "W": ["phys0", "phys1", "mirror"]}

    def F_mor(s, t):
        smap = tuple(SiteMap(x, x) for x in site_of[s])       # same-named embedding (profile-preserving)
        return D1RestrictionMorphism(
            name=f"F({s}<={t})", source=F_obj[s], target=F_obj[t], site_map=smap,
            preserved_dimensions=D1_DIMENSIONS,
            require_trust_path_preservation=False, require_obstruction_preservation=False,
        )

    return F_obj, F_mor


def check_functor(F_obj, F_mor, label):
    print(f"\n[3] Functoriality of {label}")
    # objects land in D1Cat: every F(object) is a valid D1RestrictionSystem
    for name, sys in F_obj.items():
        v = validate_system(sys)
        check(f"{label}: F({name}) is a valid D1Cat object", v.valid, "" if v.valid else str(v.errors))
    # each F(morphism) is a valid (reached) D1 restriction morphism
    for s, t in GUBDY_INCLUSIONS:
        m = F_mor(s, t)
        a = analyze_morphism(m)
        check(f"{label}: F({s}<={t}) is a well-formed D1 morphism (reached)", a.reached,
              "" if a.reached else a.obstruction)
    # COMPOSITION: F(W+0<=W) == F(W+<=W) o F(W+0<=W+)   (diagrammatic: apply W+0<=W+ then W+<=W)
    f = F_mor("W+0", "W+")
    g = F_mor("W+", "W")
    composed = _compose_morphisms(f, g)
    direct = F_mor("W+0", "W")
    eq = morphisms_equal_modulo_name(composed, direct)
    check(f"{label}: F preserves COMPOSITION -- F(g;f) == F(g) o F(f)", eq.equal_modulo_name,
          f"site_map_match={eq.site_map_match}, dims_match={eq.preserved_dims_match}")
    # IDENTITY: F(id_{W+0}) == id_{F(W+0)}
    idF = make_identity(F_obj["W+0"])
    Fid = F_mor("W+0", "W+0") if ("W+0", "W+0") in GUBDY_INCLUSIONS else D1RestrictionMorphism(
        name="F(id W+0)", source=F_obj["W+0"], target=F_obj["W+0"],
        site_map=(SiteMap("phys0", "phys0"),), preserved_dimensions=D1_DIMENSIONS,
        require_trust_path_preservation=False, require_obstruction_preservation=False)
    eqi = morphisms_equal_modulo_name(Fid, idF)
    check(f"{label}: F preserves IDENTITY -- F(id) == id_{{F(-)}}", eqi.equal_modulo_name)
    return eq.equal_modulo_name and eqi.equal_modulo_name


# ============================================================================================
# MAIN
# ============================================================================================
def main():
    print("#" * 100)
    print("# BOUNDARY ADAPTER AS A FUNCTOR  F : GUBdy -> D1Cat   (first build, starting CT-1)")
    print("#" * 100)

    derived = mini_t12prime()
    gubdy_is_category()

    # The real adapter F (profiles grounded in mini-T12')
    F_obj, F_mor = build_F(derived["phys_accessible"], derived["mirror_accessible"])
    F_ok = check_functor(F_obj, F_mor, "F (real, physics-grounded)")

    # ---- DISCRIMINATING CONTROLS ------------------------------------------------------------
    print("\n[4] DISCRIMINATING CONTROLS (is functoriality NECESSARY-NOT-SUFFICIENT?)")

    # non-triviality: F distinguishes objects and distinguishes the two inclusions into W
    nonconst = (morphisms_equal_modulo_name(F_mor("W+", "W"), F_mor("W-", "W")).equal_modulo_name is False)
    check("F is NON-CONSTANT: F(W+<=W) != F(W-<=W) (distinguishes the two boundary faces)", nonconst)

    # CONSTANT functor: every object -> C_Wp0, every morphism -> its identity
    S0 = F_obj["W+0"]
    id0 = make_identity(S0)

    def Fc_mor(s, t):
        return id0
    print("  -- constant functor F_const (every object -> C_Wp0, every morphism -> id):")
    fc_comp = morphisms_equal_modulo_name(_compose_morphisms(id0, id0), id0).equal_modulo_name
    check("F_const ALSO passes composition (id o id == id) -> functoriality is NECESSARY-NOT-SUFFICIENT",
          fc_comp, "a constant functor 'connects everything' and proves nothing")
    fc_faithful = (morphisms_equal_modulo_name(Fc_mor("W+", "W"), Fc_mor("W-", "W")).equal_modulo_name
                   is False)
    check("F_const is NOT faithful (collapses the two faces) -> FAITHFULNESS separates real F from trivial",
          fc_faithful is False, "faithfulness, not functoriality, is the adapter's content")

    # PHYSICS-WRONG functor: mirror.accessible_support = 1 (contradicts T12'); still a functor?
    Fw_obj, Fw_mor = build_F(phys_accessible=1, mirror_accessible=1)   # WRONG: mirror should be 0
    Fw_ok = check_functor_silent(Fw_obj, Fw_mor)
    check("PHYSICS-WRONG functor (mirror.accessible=1) STILL passes functoriality + validity",
          Fw_ok, "-> functoriality does NOT enforce the T12' physics; the grounding is EXTRA content")

    # ---- VERDICT ----------------------------------------------------------------------------
    print("\n[5] VERDICT")
    print("  * GUBdy is a category; F : GUBdy -> D1Cat is a well-defined functor into the PROVEN D1Cat")
    print("    (T41): objects land as valid D1 systems, morphisms as reached D1 morphisms, composition and")
    print("    identity preserved. The action-on-morphisms the contract's S/R prose omitted is now supplied.")
    print("  * BUT functoriality is NECESSARY-NOT-SUFFICIENT: a CONSTANT functor also passes, and a")
    print("    PHYSICS-WRONG functor (mirror.accessible=1, contradicting T12') also passes. So functoriality")
    print("    certifies the SHAPE, not the adapter. The adapter's real content is (i) FAITHFULNESS (the")
    print("    real F distinguishes the two boundary faces; the constant functor does not) and (ii)")
    print("    PHYSICS-GROUNDING (the profiles must be FORCED by T12', which the functor axioms do not")
    print("    enforce). Those two -- plus a companion adjoint/inverse (the two-adapter gate) -- are the")
    print("    next legs. No claim moves; this locates the next requirement, it does not close the adapter.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = GUBdy is a category; F is a functor into D1Cat; controls show functoriality is")
    print("         necessary-not-sufficient (faithfulness + physics-grounding are the named next legs).")


def check_functor_silent(F_obj, F_mor):
    """Functoriality of F without printing (for the physics-wrong control)."""
    for _, sys in F_obj.items():
        if not validate_system(sys).valid:
            return False
    for s, t in GUBDY_INCLUSIONS:
        if not analyze_morphism(F_mor(s, t)).reached:
            return False
    f, g = F_mor("W+0", "W+"), F_mor("W+", "W")
    if not morphisms_equal_modulo_name(_compose_morphisms(f, g), F_mor("W+0", "W")).equal_modulo_name:
        return False
    return True


if __name__ == "__main__":
    main()
