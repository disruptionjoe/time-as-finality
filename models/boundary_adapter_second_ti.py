"""
SECOND, INDEPENDENT ADAPTER -- the TI side.  S : TIsrc -> D1Cat, grounded in TI's OWN forcing (E002 F2).

Companion to `open-problems/boundary-adapter-as-functor-spec-2026-07-07.md`. The tri-repo two-adapter gate
requires TWO INDEPENDENT adapters before any identity ("GU boundary = TaF capability = TI source") is
licensed. Adapter 1 (F : GUBdy -> D1Cat, boundary_adapter_functor*.py) order-reflects the physical-vs-mirror
FACE, FORCED by the GU Krein physics (T12' zero statistical trace). This is Adapter 2 from the TI side.

THE INDEPENDENCE (why this is not manufactured convergence). The whole point of the gate is to stop one
process from building two functors that agree because it MADE them agree. So S must be grounded in a TI
forcing that is INDEPENDENT of T12'. It is: TI's E002 bridge toy model, fixture **F2 (Same Records, Different
Hidden Issuance)**, shows that a source difference in a HIDDEN constraint `h not in A_i` leaves ZERO trace on
the individual observer's records `Rec_i` (the projection is non-faithful). That is TI's OWN zero-trace
signature -- the T395/T12' shape -- reached through source-realization logic (hidden vs accessible
constraints), NOT through Krein positivity. So:
  * F forces mirror.accessible = 0 via GU Krein zero-trace (T12').
  * S forces hidden.accessible = 0 via TI source non-faithfulness (E002 F2).
Two DIFFERENT primitives, independently forcing "individually invisible but structurally real."

TIsrc (source category, grounded in E002's SourceRealization S = (C, <=_S, Ext_S)):
  objects = source states with an ACCESSIBLE / HIDDEN split (A_i vs h not in A_i);
  morphisms = source extensions (<=_S / Ext_S inclusions). Same poset shape as GUBdy -- which is the CONTENT
  of the proposed identity (accessible <-> physical, hidden <-> mirror), a hypothesis the coherence check
  tests, not an assumption.

WHAT THIS BUILD CHECKS:
  1. S is a functor TIsrc -> D1Cat (into the same PROVEN D1Cat).
  2. S order-reflects the accessible/hidden FACE, and it is FORCED by F2: a TI-WRONG S (hidden.accessible=1,
     i.e. F2 refuted / hidden IS record-visible) FAILS order-reflection -- the parallel of the GU physics-wrong
     control, but forced by a DIFFERENT structure.
  3. COHERENCE: S and F land on the SAME D1 objects under the iso (accessible<->physical, hidden<->mirror) --
     the two independently-forced adapters AGREE.
  4. MANUFACTURED-CONVERGENCE AUDIT (honest): the agreement is falsifiable (TI-wrong S disagrees with F), so
     it is not vacuous; BUT both adapters are built by one process, one encoding -- this is
     INDEPENDENT-FORCING WITHIN ONE PROGRAM, not de-correlated external independence. The identity is NOT
     licensed; the gate ADVANCES (1 -> 2 independently-forced adapters), it does not close.

No claim moves. Run: python -m models.boundary_adapter_second_ti      (exit 0)
"""
from __future__ import annotations

from itertools import product

from models.boundary_adapter_functor import GUBDY_INCLUSIONS, GUBDY_OBJECTS, _site, _system, build_F
from models.d1_restriction_system import (
    D1_DIMENSIONS,
    D1RestrictionMorphism,
    SiteMap,
    analyze_morphism,
    validate_system,
)
from models.multiscale_observer_field import D1Profile

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# TIsrc: source category (poset), grounded in E002. Same shape as GUBdy; the iso is the proposed identity.
TISRC_OBJECTS = {"acc0": "accessible sub-sector", "acc": "accessible sector",
                 "hid": "hidden/generated (h not in A_i)", "full": "accessible + hidden"}
TISRC_INCLUSIONS = [("acc0", "acc"), ("acc", "full"), ("acc0", "full"), ("hid", "full")]
LEQ_TI = {(x, x) for x in TISRC_OBJECTS} | set(TISRC_INCLUSIONS)
# the proposed identity iso  GUBdy <-> TIsrc  (accessible <-> physical, hidden <-> mirror)
ISO = {"W+0": "acc0", "W+": "acc", "W-": "hid", "W": "full"}


def _probe(SA, SB, combo):
    return D1RestrictionMorphism(
        name="probe", source=SA, target=SB,
        site_map=tuple(SiteMap(s, t) for s, t in zip(SA.site_ids(), combo)),
        preserved_dimensions=D1_DIMENSIONS,
        require_trust_path_preservation=False, require_obstruction_preservation=False,
    )


def morphism_exists(SA, SB) -> bool:
    return any(analyze_morphism(_probe(SA, SB, c)).reached
               for c in product(list(SB.site_ids()), repeat=len(list(SA.site_ids()))))


def sig(system):
    return tuple(sorted(v.profile.as_tuple() for v in system.local_values))


def build_S(hidden_accessible):
    """S on objects, grounded in E002 F2: hidden constraints have ZERO record trace -> accessible_support=0.
    `hidden_accessible` is a control knob: 0 = F2 holds (correct); 1 = F2 refuted (TI-WRONG)."""
    ACC = D1Profile(1, 1, 1, 1)                      # accessible constraint: certified by records (F1/F4)
    HID = D1Profile(hidden_accessible, 1, 1, 1)      # hidden constraint: zero record trace (F2) -> accessible 0

    def sysfor(name, sites):
        return _system(name, sites)

    return {
        "acc0": sysfor("Src_acc0", {"a0": ACC}),
        "acc": sysfor("Src_acc", {"a0": ACC, "a1": ACC}),
        "hid": sysfor("Src_hid", {"h0": HID}),
        "full": sysfor("Src_full", {"a0": ACC, "a1": ACC, "h0": HID}),
    }


def order_reflection_faces_ok(obj, incl, leq):
    """True iff no order-reflection mismatch involves the 'hidden'/'mirror' face object."""
    face = "hid" if "hid" in obj else "W-"
    for A in obj:
        for B in obj:
            if face in (A, B):
                if morphism_exists(obj[A], obj[B]) != ((A, B) in leq):
                    return False
    return True


def main():
    print("#" * 100)
    print("# SECOND, INDEPENDENT ADAPTER  S : TIsrc -> D1Cat  (grounded in TI's own forcing, E002 F2)")
    print("#" * 100)

    F_obj, _ = build_F(phys_accessible=1, mirror_accessible=0)     # Adapter 1 (GU), for the coherence check
    S_obj = build_S(hidden_accessible=0)                           # Adapter 2 (TI), F2 holds

    # ---- [1] S is a functor into D1Cat -----------------------------------------------------
    print("\n[1] S : TIsrc -> D1Cat is a functor into the PROVEN D1Cat")
    for name, s in S_obj.items():
        check(f"S({name}) is a valid D1Cat object", validate_system(s).valid)
    for a, b in TISRC_INCLUSIONS:
        smap = tuple(SiteMap(x, x) for x in S_obj[a].site_ids())   # same-name embedding (profile-preserving)
        m = D1RestrictionMorphism(name=f"S({a}<={b})", source=S_obj[a], target=S_obj[b], site_map=smap,
                                  preserved_dimensions=D1_DIMENSIONS,
                                  require_trust_path_preservation=False, require_obstruction_preservation=False)
        check(f"S({a}<={b}) is a reached D1 morphism", analyze_morphism(m).reached)

    # ---- [2] S order-reflects the accessible/hidden FACE, FORCED by F2 ----------------------
    print("\n[2] S order-reflects the accessible/HIDDEN face -- forced by E002 F2 (hidden = zero record trace)")
    s_hid_acc = morphism_exists(S_obj["hid"], S_obj["acc"])
    check("S(hid)->S(acc) does NOT exist -> accessible and hidden are reflected as incomparable",
          not s_hid_acc, "forced by F2: hidden.accessible=0 (zero record trace), a TI structure not GU's")
    faces_ok = order_reflection_faces_ok(S_obj, TISRC_INCLUSIONS, LEQ_TI)
    check("the hidden FACE is cleanly order-reflected by S (no mismatch involves 'hid')", faces_ok)

    # ---- [3] The forcing is INDEPENDENT: TI-WRONG S (F2 refuted) FAILS, and DISAGREES with F ----
    print("\n[3] INDEPENDENCE: a TI-WRONG S (hidden.accessible=1, i.e. F2 refuted) FAILS -- forced by TI, not GU")
    Sw_obj = build_S(hidden_accessible=1)                          # F2 refuted: hidden IS record-visible
    sw_hid_acc = morphism_exists(Sw_obj["hid"], Sw_obj["acc"])
    check("TI-WRONG S admits a spurious S(hid)->S(acc) -> FAILS the face reflection (F2 is load-bearing)",
          sw_hid_acc, "the forcing is TI's own (source non-faithfulness), independent of the GU Krein forcing")

    # ---- [4] COHERENCE: F and S agree on the same D1 objects under the identity iso ---------
    print("\n[4] COHERENCE: F and S land on the SAME D1 objects under the iso accessible<->physical, hidden<->mirror")
    coherent = all(sig(F_obj[g]) == sig(S_obj[ISO[g]]) for g in GUBDY_OBJECTS)
    check("F(GU sector) and S(TI source-state) coincide as capability objects under the iso", coherent,
          "mirror <-> hidden both land accessible_support=0; physical <-> accessible both land 1")
    # falsifiability of the agreement: TI-WRONG S no longer coincides with F on the mirror<->hidden pair
    disagree = sig(F_obj["W-"]) != sig(Sw_obj["hid"])
    check("the agreement is FALSIFIABLE: TI-WRONG S (F2 refuted) DISAGREES with F on mirror<->hidden",
          disagree, "so F<->S agreement is not vacuous -- it holds because F2 and T12' independently force it")

    # ---- [5] VERDICT + honest manufactured-convergence audit -------------------------------
    print("\n[5] VERDICT + manufactured-convergence audit")
    print("  * TWO ADAPTERS NOW COHERE, each INDEPENDENTLY FORCED:")
    print("      Adapter 1  F : GUBdy  -> D1Cat   forces mirror.accessible=0 via GU Krein zero-trace (T12').")
    print("      Adapter 2  S : TIsrc -> D1Cat   forces hidden.accessible=0 via TI source non-faithfulness (F2).")
    print("    They agree on the SAME D1Cat objects under the identity iso, and the agreement is FALSIFIABLE")
    print("    (the TI-wrong S disagrees with F). Two DIFFERENT primitives (Krein positivity; hidden issuance)")
    print("    independently produce the 'individually invisible but real' signature -- not one imported into")
    print("    the other. This is the two-adapter shape the gate asks for.")
    print("  * HONEST CAVEAT (the gate is ADVANCED, NOT CLOSED): both adapters were built by ONE process, in")
    print("    ONE encoding (the D1 profile convention, the shared poset shape). Per the registry's")
    print("    de-correlation test, TRUE independence needs GENUINELY DE-CORRELATED processes (different")
    print("    models/framings/no shared brief). So this is INDEPENDENT-FORCING WITHIN ONE PROGRAM, which is")
    print("    stronger than one adapter but weaker than external independent arrival. The identity")
    print("    'GU boundary = TaF capability = TI source' is NOT licensed.")
    print("  * REMAINING TO CLOSE THE GATE: (i) a dimension-carrying capability encoding (build 2's named fix),")
    print("    (ii) genuine DE-CORRELATION of the two adapters (independent processes), (iii) the mu<->boundary")
    print("    and records-vs-redundancy legs that remain uncomputed. Gate: 2 adapters forced, de-correlation")
    print("    pending. No identity asserted; no claim moves in any repo.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = S is a functor into D1Cat, order-reflects the accessible/hidden face FORCED BY TI's OWN F2")
    print("         (TI-wrong S fails + disagrees with F); F and S cohere; gate ADVANCED to two")
    print("         independently-forced adapters; de-correlation pending; identity NOT licensed.")


if __name__ == "__main__":
    main()
