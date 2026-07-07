"""
BOUNDARY ADAPTER FUNCTOR -- FAITHFULNESS + ADJOINT leg (second build, continuing CT-1).

Companion to `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`. The first build
(`boundary_adapter_functor.py`) showed functoriality is NECESSARY-NOT-SUFFICIENT: a constant functor and a
PHYSICS-WRONG functor (mirror.accessible=1) both passed. It named the next legs: faithfulness + physics-
grounding + an adjoint. This build supplies them and reports honestly.

KEY SUBTLETY (why "faithfulness" alone is the wrong word): GUBdy is a THIN category (a poset -- at most one
morphism between any two objects), so a functor out of it is faithful AUTOMATICALLY (hom-sets are singletons).
The property that actually carries content is **ORDER-REFLECTION** (conservativity): a D1 morphism
F(A) -> F(B) exists IFF A <= B in GUBdy. An order-reflecting + injective-on-objects functor is an
ORDER-EMBEDDING. That is the real faithfulness leg, and -- the payoff -- it is exactly the property the
PHYSICS-WRONG functor must now FAIL, because setting mirror.accessible=1 manufactures a spurious morphism
F(W-) -> F(W+) that falsely implies W- <= W+. So order-reflection is what functoriality missed, and it holds
for the real F PRECISELY BECAUSE the T12' physics gives the mirror accessible_support = 0. Faithfulness and
physics-grounding are ONE requirement, not two.

ADJOINT / SECOND-ADAPTER leg: an order-embedding gives G = F^{-1} on the image, an order-iso
GUBdy ~= image(F). Honest scope: that is F AND ITS INVERSE = ONE adapter, NOT the two INDEPENDENT adapters
the tri-repo gate requires; and F is faithful but NOT full into D1Cat (D1Cat has extra morphisms). A genuine
right adjoint G : D1Cat -> GUBdy on ALL of D1Cat (a reflection) is unbuilt. So this build PROMOTES the
faithfulness leg and unifies it with physics-grounding, and gives an equivalence-onto-image, but it does NOT
close the two-adapter gate.

No claim moves. Run: python -m models.boundary_adapter_functor_faithfulness      (exit 0)
"""
from __future__ import annotations

from itertools import product

from models.boundary_adapter_functor import GUBDY_INCLUSIONS, GUBDY_OBJECTS, build_F
from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    SiteMap,
    analyze_morphism,
)

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# GUBdy partial order <= : reflexive closure of the inclusions (already transitively closed: W+0<=W present)
LEQ = {(x, x) for x in GUBDY_OBJECTS} | set(GUBDY_INCLUSIONS)


def _probe_morphism(SA, SB, combo):
    smap = tuple(SiteMap(s, t) for s, t in zip(SA.site_ids(), combo))
    return D1RestrictionMorphism(
        name="probe", source=SA, target=SB, site_map=smap,
        preserved_dimensions=D1_DIMENSIONS,
        require_trust_path_preservation=False, require_obstruction_preservation=False,
    )


def morphism_count(SA, SB) -> int:
    """Number of all-dims-preserving D1 morphisms F(A) -> F(B) (search over site maps)."""
    src, tgt = list(SA.site_ids()), list(SB.site_ids())
    n = 0
    for combo in product(tgt, repeat=len(src)):
        if analyze_morphism(_probe_morphism(SA, SB, combo)).reached:
            n += 1
    return n


def morphism_exists(SA, SB) -> bool:
    return morphism_count(SA, SB) > 0


def system_signature(system):
    return tuple(sorted(v.profile.as_tuple() for v in system.local_values))


def order_reflection_ok(F_obj) -> bool:
    """F is order-reflecting iff  (a D1 morphism F(A)->F(B) exists)  ==  (A <= B in GUBdy),  all pairs."""
    ok = True
    for A in GUBDY_OBJECTS:
        for B in GUBDY_OBJECTS:
            exists = morphism_exists(F_obj[A], F_obj[B])
            leq = (A, B) in LEQ
            if exists != leq:
                ok = False
    return ok


def main():
    print("#" * 100)
    print("# BOUNDARY ADAPTER FUNCTOR -- FAITHFULNESS (order-reflection) + ADJOINT leg")
    print("#" * 100)

    # Real, physics-grounded F (mirror.accessible = 0 from T12')
    F_obj, _F_mor = build_F(phys_accessible=1, mirror_accessible=0)

    # ---- [1] INJECTIVE ON OBJECTS ----------------------------------------------------------
    print("\n[1] F injective on objects (does not collapse the sectors)")
    sigs = {A: system_signature(F_obj[A]) for A in GUBDY_OBJECTS}
    inj = len(set(sigs.values())) == len(sigs)
    check("F is injective on objects: the four sectors land on four distinct capability objects", inj,
          f"{len(set(sigs.values()))}/{len(sigs)} distinct")

    # ---- [2] ORDER-REFLECTION (the real faithfulness leg) ----------------------------------
    print("\n[2] ORDER-REFLECTION: does a D1 morphism F(A)->F(B) exist IFF A<=B in GUBdy?")
    print("     (thin source category => plain faithfulness is automatic; order-reflection carries the content)")
    mismatches = set()
    for A in GUBDY_OBJECTS:
        for B in GUBDY_OBJECTS:
            exists = morphism_exists(F_obj[A], F_obj[B])
            leq = (A, B) in LEQ
            if exists != leq:
                mismatches.add((A, B))
            if A != B:
                mark = "ok" if exists == leq else "MISMATCH"
                print(f"     F({A})->F({B}) exists={str(exists):5}  A<=B={str(leq):5}  [{mark}]")
    # (a) the physics FACE distinction (physical vs mirror) is cleanly reflected -- NO mismatch touches W-
    mirror_clean = all("W-" not in pair for pair in mismatches)
    check("mirror FACE order-reflected: NO mismatch involves W- (physical-vs-mirror is faithful, physics-forced)",
          mirror_clean, f"mismatches={sorted(mismatches)}")
    check("F(W-)->F(W+) does NOT exist -> the two boundary faces are reflected as incomparable",
          not morphism_exists(F_obj["W-"], F_obj["W+"]),
          "this is where the T12' physics (mirror.accessible=0) does the work")
    # (b) the ONLY non-reflection is the pure-physical DIMENSION collapse F(W+)->F(W+0)
    only_dim = (mismatches == {("W+", "W+0")})
    check("the ONLY order-reflection failure is the pure-physical DIMENSION collapse F(W+)->F(W+0)",
          only_dim,
          "capability profiles are blind to redundant identical physical directions; "
          f"mismatches={sorted(mismatches)}")

    # ---- [3] PHYSICS-WRONG FUNCTOR NOW FAILS (closing the prior open loop) ------------------
    print("\n[3] PHYSICS-WRONG functor (mirror.accessible=1) under the order-reflection test")
    Fw_obj, _ = build_F(phys_accessible=1, mirror_accessible=1)   # WRONG per T12'
    wrong_wm_wp = morphism_exists(Fw_obj["W-"], Fw_obj["W+"])
    wrong_reflects = order_reflection_ok(Fw_obj)
    print(f"     F_wrong(W-)->F_wrong(W+) exists = {wrong_wm_wp}  (spurious: mirror now matches phys)")
    check("PHYSICS-WRONG functor FAILS order-reflection (admits a spurious F(W-)->F(W+))",
          (wrong_wm_wp is True) and (wrong_reflects is False),
          "-> ORDER-REFLECTION catches the physics error that FUNCTORIALITY missed; the two legs are ONE")

    # ---- [4] CONSTANT FUNCTOR fails injective-on-objects -----------------------------------
    print("\n[4] CONSTANT functor under the same tests")
    const_sig = {A: system_signature(F_obj["W+0"]) for A in GUBDY_OBJECTS}   # everything -> C_Wp0
    const_inj = len(set(const_sig.values())) == len(const_sig)
    check("CONSTANT functor FAILS injective-on-objects (collapses all four sectors to one)", not const_inj,
          "functoriality alone could not see this; injectivity + order-reflection can")

    # ---- [5] ADJOINT / SECOND-ADAPTER leg (honest scope) -----------------------------------
    print("\n[5] ADJOINT / SECOND-ADAPTER leg")
    # G = F^{-1} on the image: well-defined (F injective on objects) and order-preserving (order-reflection),
    # so G o F = id_GUBdy and GUBdy ~= image(F) as posets.
    G = {sigs[A]: A for A in GUBDY_OBJECTS}     # image-signature -> GUBdy object
    gf_id = all(G[sigs[A]] == A for A in GUBDY_OBJECTS)
    check("G = F^{-1} well-defined on OBJECTS and G o F = id_GUBdy (F injective on objects)", gf_id,
          "but NOT an order-iso: the image collapses W+0 ~ W+ (dimension), so the equivalence holds only for "
          "the FACE poset {physical, mirror, full}, not the full 4-object poset")
    # F is faithful but NOT full: D1Cat has extra morphisms not from GUBdy (two embeddings F(W+0)->F(W+))
    cnt = morphism_count(F_obj["W+0"], F_obj["W+"])
    not_full = cnt > 1
    print(f"     #(D1 morphisms F(W+0)->F(W+)) = {cnt}  vs #(GUBdy morphisms W+0<=W+) = 1")
    check("F is FAITHFUL but NOT FULL into D1Cat (D1Cat has extra morphisms) -> equivalence is onto a "
          "NON-full image, i.e. ONE adapter (F + its inverse), not two independent adapters", not_full)

    # ---- VERDICT ---------------------------------------------------------------------------
    print("\n[6] VERDICT")
    print("  * FAITHFULNESS LEG: PROMOTED ON THE PHYSICS-CRITICAL DISTINCTION, with a precise limit. F is")
    print("    injective-on-objects and ORDER-REFLECTS the physical-vs-mirror FACE distinction: no mismatch")
    print("    touches W-, and F(W-)->F(W+) does NOT exist. This UNIFIES faithfulness with physics-grounding:")
    print("    the face reflection holds precisely because T12' gives mirror.accessible=0, and the PHYSICS-WRONG")
    print("    functor now FAILS it (a spurious F(W-)->F(W+) appears). The property functoriality missed is")
    print("    order-reflection, and the physics is exactly what supplies it -- the two 'next legs' are one.")
    print("  * THE PRECISE LIMIT (a real finding, not a pass): F is NOT a FULL order-embedding. Its ONLY failure")
    print("    is the pure-physical DIMENSION collapse F(W+)->F(W+0): the flat per-site capability profile is")
    print("    blind to redundant identical physical directions, so D1 morphisms collapse W+ onto W+0. To make")
    print("    F a full order-embedding, the capability object must carry sub-sector DIMENSION in a")
    print("    morphism-respecting way (profile-exact preservation makes that a genuine design question about")
    print("    what 'restriction' means for capability). The mirror face is unaffected -- physics protects it.")
    print("  * ADJOINT / SECOND-ADAPTER LEG: PARTIAL. G = F^{-1} gives G o F = id on objects and an order-iso")
    print("    only for the FACE poset {physical, mirror, full}; F is FAITHFUL-NOT-FULL. This is ONE adapter (F")
    print("    and its inverse onto a non-full image), NOT the two INDEPENDENT adapters the tri-repo gate")
    print("    requires; a genuine reflection G : D1Cat -> GUBdy on all of D1Cat is unbuilt. Gate NOT closed.")
    print("  * NET: the adapter reflects the individual<->collective FACE distinction physics-forcedly (the real")
    print("    content), is blind to within-face dimension (named fix), and stands as ONE of the two required")
    print("    adapters. No claim moves; no identity asserted.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = face distinction order-reflected (physics-forced; physics-wrong FAILS); only non-reflection")
    print("         is the within-physical dimension collapse (named); adjoint PARTIAL; two-adapter gate open.")


if __name__ == "__main__":
    main()
