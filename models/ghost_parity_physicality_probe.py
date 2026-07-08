"""
GHOST-PARITY PHYSICALITY PROBE -- pushing the one bet the finality discriminator isolated.

The discriminator (finality_records_vs_redundancy_discriminator.py) reduced the entire finality residual to a
single dichotomy: is physicality defined by POSITIVITY (standard -> the ghost is gauge REDUNDANCY) or by the
full KREIN structure (ghost-parity / Krein quantization -> the ghost is a RECORD)? This probe pushes it.

The record reading has an obvious-looking objection: "if the mirror is PHYSICAL it should be MANIFEST (visible),
not a HIDDEN record." This probe checked it and found something SHARPER and less favorable to the record
reading than expected: whether the physicalized mirror is HIDDEN depends on the OBSERVER'S NORMALIZATION
CONVENTION, and under the honest FULL-SPACE Born rule it is NOT hidden -- physicalizing the ghost (a
positive-definite full-space inner product) makes the mirror weight LEAK into a W+-restricted observer's
normalized statistics (via the denominator ||psi||^2, which a full-space physical state carries). The mirror is
hidden ONLY under a SELF-NORMALIZED / post-selected observer (normalize by the physical component's own norm
||P+ psi||^2 -- exactly the projector-Born convention T12' used). So the "hidden collective record" reading
needs BOTH the Krein-retention quantization AND the self-normalized observer convention: two special bets, not
one. This leans AGAINST the record reading (more contingent than hoped), which is the honest outcome.

The honest bet is stated precisely at the end (BRST-quotient vs Krein-retention, and now also the normalization
convention).

Carrier: minimal Krein space, K = P_ghost = diag(+1_k, -1_k). Two inner products:
  <.|.>_K  the indefinite Krein form (mirror states have NEGATIVE norm -> "ghost").
  <.|.>_I  the standard positive-definite inner product (mirror states have POSITIVE norm -> physical).
The Krein-quantization claim is that <.|.>_I (a positive-definite inner product on the FULL space) is the
physical one; the standard BRST claim is that the physical space is the W+ quotient and the ghost is dropped.

Run: python -m models.ghost_parity_physicality_probe    (exit 0)
"""
from __future__ import annotations

import math

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


K = [1.0, 1.0, -1.0, -1.0]          # Krein form = P_ghost ; W+ = {0,1}, W- = {2,3}


def ip_I(u, v):                      # standard positive-definite inner product
    return sum(u[i] * v[i] for i in range(4))


def ip_K(u, v):                      # indefinite Krein form
    return sum(u[i] * K[i] * v[i] for i in range(4))


def wplus_expect_full(state, O2):
    """W+ observable O2 under the FULL-space Born rule: normalize by the full ||state||^2_I (a full-space
    physical state carries its total norm). This LEAKS the W- weight through the denominator."""
    c = [state[0], state[1]]
    num = sum(c[i] * O2[i][j] * c[j] for i in range(2) for j in range(2))
    return num / ip_I(state, state)


def wplus_expect_selfnorm(state, O2):
    """W+ observable O2 under the SELF-NORMALIZED / post-selected (projector-Born, T12') convention: normalize
    by the physical component's own norm ||P+ state||^2. Depends ONLY on the W+ part -> hidden to W-."""
    c = [state[0], state[1]]
    num = sum(c[i] * O2[i][j] * c[j] for i in range(2) for j in range(2))
    return num / (c[0] * c[0] + c[1] * c[1])


def main():
    print("#" * 100)
    print("# GHOST-PARITY PHYSICALITY PROBE -- is the 'physical-and-hidden record' reading coherent?")
    print("#" * 100)

    e2 = [0.0, 0.0, 1.0, 0.0]        # a pure mirror (ghost) state
    # states sharing W+ part, differing in W-
    psi = [0.7, -0.3, 0.5, 0.2]
    psip = [0.7, -0.3, 0.1, -0.4]

    print("\n[1] the two inner products disagree on the mirror's norm")
    check("mirror state has NEGATIVE norm under the Krein form (a 'ghost')", ip_K(e2, e2) < 0,
          f"<e2|e2>_K = {ip_K(e2, e2):+.1f}")
    check("mirror state has POSITIVE norm under the standard inner product (physical if <.|.>_I is chosen)",
          ip_I(e2, e2) > 0, f"<e2|e2>_I = {ip_I(e2, e2):+.1f}")
    print("    -> Krein quantization's claim: <.|.>_I (positive-definite, full-space) is the PHYSICAL product,")
    print("       under which the mirror is an ordinary physical state -- NOT quotiented away.")

    print("\n[2] a positive-definite physical inner product EXISTS on the full space (Krein quant. is available)")
    # <.|.>_I is manifestly positive-definite on all 4 dims
    posdef = all(ip_I(b, b) > 0 for b in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]))
    check("<.|.>_I is positive-definite on the FULL space (a genuine Hilbert-space structure incl. the ghost)",
          posdef)

    print("\n[3] IS the physicalized mirror hidden? It DEPENDS on the observer's normalization (the real finding)")
    O_a = [[1.0, 0.0], [0.0, 0.0]]      # a W+-supported observable
    O_b = [[0.3, 0.4], [0.4, -0.2]]     # another W+-supported observable
    dfull_a = abs(wplus_expect_full(psi, O_a) - wplus_expect_full(psip, O_a))
    dfull_b = abs(wplus_expect_full(psi, O_b) - wplus_expect_full(psip, O_b))
    dself_a = abs(wplus_expect_selfnorm(psi, O_a) - wplus_expect_selfnorm(psip, O_a))
    dself_b = abs(wplus_expect_selfnorm(psi, O_b) - wplus_expect_selfnorm(psip, O_b))
    print(f"    FULL-space Born rule (normalize by ||psi||^2_I):    O_a diff = {dfull_a:.3e}, O_b diff = {dfull_b:.3e}")
    print(f"    SELF-NORMALIZED / projector-Born (T12' convention): O_a diff = {dself_a:.3e}, O_b diff = {dself_b:.3e}")
    check("under the FULL-space Born rule the mirror weight LEAKS -> physicalizing the ghost makes it VISIBLE",
          dfull_a > 1e-6 and dfull_b > 1e-6, "so 'physical-and-hidden' FAILS under honest full-space normalization")
    check("under the SELF-NORMALIZED (T12') convention the mirror is HIDDEN -> hidden-ness is convention-dependent",
          dself_a < 1e-9 and dself_b < 1e-9, "the record reading needs THIS convention, not the full Born rule")

    print("\n[4] a full-space observer distinguishes them either way (the W- difference is genuinely present)")
    N_minus = [0, 0, 1, 1]              # mirror-number observable (diagonal), a full-space observable
    coll = abs(sum(psi[i] * N_minus[i] * psi[i] for i in range(4)) / ip_I(psi, psi)
               - sum(psip[i] * N_minus[i] * psip[i] for i in range(4)) / ip_I(psip, psip))
    check("a full-space observer distinguishes them (the W- difference is genuinely present, not degenerate)",
          coll > 0.01, f"collective mirror-number difference = {coll:.3f}")

    print("\n[5] VERDICT -- the probe refuted the too-easy coherence claim; the record reading got MORE contingent")
    print("  * THE REAL FINDING (leans AGAINST the record reading): 'physical-and-hidden' is NOT robustly")
    print("    coherent. If you PHYSICALIZE the ghost (Krein-retention, positive full-space inner product), the")
    print("    honest FULL-space Born rule LEAKS the mirror weight into a W+-restricted observer's statistics --")
    print("    the ghost becomes partially VISIBLE, not a hidden record. The mirror is hidden ONLY under the")
    print("    SELF-NORMALIZED / projector-Born convention (the one T12' used), which treats the physical sector")
    print("    as self-contained. So the record reading needs TWO special bets, not one: (i) Krein-retention")
    print("    quantization AND (ii) the self-normalized observer convention. The two contingencies compound.")
    print("  * THE SHARPENED BET stands and is now DOUBLY-gated:")
    print("      quantization: BRST-QUOTIENT (ghost = gauge artifact -> REDUNDANCY, the standard default) vs")
    print("                    KREIN-RETENTION (ghost = physical dof; Bender-Mannheim/Turok-Bateman);")
    print("      normalization: FULL Born (ghost leaks -> visible, NOT a hidden record) vs")
    print("                    SELF-NORMALIZED projector-Born (ghost hidden -> the record reading's needed frame).")
    print("    The record-as-HIDDEN-collective-record reading survives ONLY in the corner {Krein-retention AND")
    print("    self-normalized}. The default corner {BRST-quotient AND full-Born} gives REDUNDANCY.")
    print("  * WHAT DECIDES the quantization leg (narrower than 'the source action'): whether the mirror sector")
    print("    is BRST-exact (gauge -> quotient -> redundancy) or BRST-cohomology-nontrivial (physical dof).")
    print("    Fixed by the CONSTRAINT/gauge structure -- a named piece of the dynamics, not the full")
    print("    stabilized-twisted source action. HONEST NET: pushing the bet did NOT vindicate the record")
    print("    reading -- it made it MORE contingent (two compounding special assumptions) while the default")
    print("    reading stays REDUNDANCY. It did shrink the quantization gate to a smaller, named object.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = physical-and-hidden is NORMALIZATION-CONTINGENT (full Born leaks; only self-norm hides);")
    print("         record reading survives only in {Krein-retention AND self-normalized}; default = REDUNDANCY;")
    print("         pushing the bet made it MORE contingent, not less. Honest lean against the home team.")


if __name__ == "__main__":
    main()
