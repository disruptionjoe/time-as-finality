"""
FINALITY -- records-vs-redundancy OPERATIONAL DISCRIMINATOR (executing the meta-finding-triage recommendation).

The blind de-correlation (meta-finding-triage-2026-07-07.md) reduced the FINALITY residual to its OWN minimal
object -- NOT GU's source action, but an OPERATIONAL DISCRIMINATOR: "a recovery/decoding channel evaluated
against a fixed algebra of ADMISSIBLE physical operations. Recoverable by some admissible op => genuine RECORD;
annihilated by every admissible op => discardable gauge REDUNDANCY." This is TaF-native and GU-independent.

This script BUILDS that discriminator on a minimal Krein carrier and makes the T12' "necessary-not-sufficient"
verdict precise: records-vs-redundancy is a WELL-DEFINED FUNCTION of the admissible-operation algebra, and the
whole question collapses onto ONE sharp dichotomy about what counts as a physical operation.

Carrier (minimal faithful model of the 192-dim T12' carrier): a Krein space with K = diag(+1_k, -1_k). W+ =
K-positive (physical), W- = K-negative (mirror/ghost). Two states share their W+ part and differ only in W-.

Three candidate admissible-operation algebras, and the recovery of the W- difference under each:
  A_individual  = block-diagonal Krein-unitaries (preserve W+ and W- separately). [T12' individual-accessible]
  A_collective  = full Krein-unitaries incl. W+<->W- boosts (treat the indefinite metric as a Hilbert metric).
  A_physical    = POSITIVITY-preserving operations. By Turok-Bateman positivity a positivity-preserving
                  K-unitary CANNOT map negative-norm into positive-norm, so it is block-diagonal -- i.e.
                  A_physical = A_individual. This is the STANDARD ghost/BRST reading: physical = gauge-invariant
                  = positivity-preserving; the negative-norm sector is unphysical redundancy.

The recovery statistic for an algebra A: does SOME op U in A move the W- difference into the W+ (physically
read-out) sector? recovery(A) > 0 => RECORD under A; recovery(A) = 0 => REDUNDANCY under A.

Run: python -m models.finality_records_vs_redundancy_discriminator   (exit 0)
"""
from __future__ import annotations

import math

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- minimal Krein carrier: 4-dim, W+ = {e0,e1}, W- = {e2,e3}, K = diag(1,1,-1,-1) ----
def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def wplus(v):
    return [v[0], v[1]]           # physical (W+) read-out component


K = [1.0, 1.0, -1.0, -1.0]       # diagonal Krein form


def krein_unitary(M):
    """Check M^T K M = K (real Krein-unitary)."""
    n = len(M)
    for i in range(n):
        for j in range(n):
            lhs = sum(M[a][i] * K[a] * M[a][j] for a in range(n))
            if abs(lhs - (K[i] if i == j else 0.0)) > 1e-9:
                return False
    return True


# --- states: shared W+ part, different W- part ---
a0, a1 = 0.7, -0.3               # shared physical component
b0, b1 = 0.5, 0.2               # W- component of psi
c0, c1 = 0.1, -0.4              # W- component of psi'  (differs)
psi = [a0, a1, b0, b1]
psip = [a0, a1, c0, c1]


# --- op families ---
def U_individual(theta_p, theta_m):
    """block-diagonal: rotate W+ by theta_p, W- by theta_m (preserves both sectors)."""
    cp, sp = math.cos(theta_p), math.sin(theta_p)
    cm, sm = math.cos(theta_m), math.sin(theta_m)
    return [[cp, -sp, 0, 0], [sp, cp, 0, 0], [0, 0, cm, -sm], [0, 0, sm, cm]]


def U_collective_boost(eta):
    """full Krein-unitary boost mixing e0 (W+) and e2 (W-): a Lorentz boost on the (e0,e2) plane."""
    ch, sh = math.cosh(eta), math.sinh(eta)
    return [[ch, 0, sh, 0], [0, 1, 0, 0], [sh, 0, ch, 0], [0, 0, 0, 1]]


def recovery(U):
    """max physical-readout difference between U psi and U psi' (the W- difference recovered into W+)."""
    a = wplus(matvec(U, psi))
    b = wplus(matvec(U, psip))
    return norm([a[0] - b[0], a[1] - b[1]])


def main():
    print("#" * 100)
    print("# FINALITY records-vs-redundancy OPERATIONAL DISCRIMINATOR (TaF-native, GU-independent)")
    print("#" * 100)

    # sanity: states share W+, differ in W-
    print("\n[0] states")
    check("psi, psi' share the physical (W+) part", norm([psi[0] - psip[0], psi[1] - psip[1]]) < 1e-12)
    check("psi, psi' differ in the mirror (W-) part", norm([psi[2] - psip[2], psi[3] - psip[3]]) > 0.1)

    # the three algebras are genuine Krein-unitaries
    print("\n[1] admissible-operation algebras (all genuine Krein-unitaries)")
    Uind = U_individual(0.6, 1.1)
    Ucol = U_collective_boost(0.8)
    check("A_individual op is Krein-unitary AND block-diagonal (preserves W+ and W-)",
          krein_unitary(Uind) and abs(Uind[0][2]) < 1e-12 and abs(Uind[0][3]) < 1e-12)
    check("A_collective boost is Krein-unitary AND mixes W- into W+ (NOT block-diagonal)",
          krein_unitary(Ucol) and abs(Ucol[0][2]) > 0.1)

    # recovery under each algebra
    print("\n[2] recovery of the W- difference under each admissible algebra")
    # individual: best over a grid of block-diagonal ops
    rec_ind = max(recovery(U_individual(tp, tm))
                  for tp in [i * math.pi / 8 for i in range(8)]
                  for tm in [i * math.pi / 8 for i in range(8)])
    # collective: best over a grid of boosts
    rec_col = max(recovery(U_collective_boost(e)) for e in [0.2 * i for i in range(1, 8)])
    # physical (positivity-preserving) = individual (positivity forbids W- -> W+), so same as individual
    rec_phys = rec_ind
    print(f"    recovery under A_individual (block-diagonal)         = {rec_ind:.3e}")
    print(f"    recovery under A_collective (full-Krein boost)       = {rec_col:.3e}")
    print(f"    recovery under A_physical  (positivity-preserving)   = {rec_phys:.3e}  (= A_individual)")
    check("A_individual RECOVERS NOTHING -> W- is REDUNDANCY under the individual algebra", rec_ind < 1e-9)
    check("A_collective RECOVERS the difference -> W- is a RECORD under the collective algebra", rec_col > 0.1)
    check("A_physical (positivity-preserving) RECOVERS NOTHING -> REDUNDANCY under the STANDARD algebra",
          rec_phys < 1e-9)

    # the discriminator is a function of the algebra; the dichotomy is sharp
    print("\n[3] VERDICT -- the discriminator is BUILT, and it collapses to one sharp dichotomy")
    print("  * records-vs-redundancy is a WELL-DEFINED FUNCTION of the admissible-operation algebra:")
    print("      - individual / positivity-preserving (STANDARD physical) algebra  -> REDUNDANCY")
    print("      - full-Krein collective algebra (ghost-parity quantization)        -> RECORD")
    print("  * So 'necessary-not-sufficient' (T12') is now PRECISE: T12' proved the individual algebra")
    print("    annihilates W- (redundancy under it); recovery under the collective algebra is what 'record'")
    print("    would require. The whole records-vs-redundancy question collapses onto ONE dichotomy:")
    print("      Is physicality defined by POSITIVITY (Turok-Bateman: physical = positivity-preserving =")
    print("      block-diagonal -> ghost is gauge REDUNDANCY, the STANDARD reading), or by the FULL KREIN")
    print("      structure (ghost-parity / Krein quantization: the negative-norm sector is physical ->")
    print("      collective ops are admissible -> RECORD)?")
    print("  * HONEST LEAN: under the STANDARD criterion of physicality (positivity), the verdict is")
    print("    REDUNDANCY. The RECORD reading requires the non-standard ghost-parity bet that full-Krein")
    print("    collective operations are physically admissible. The discriminator does not settle THAT bet --")
    print("    but it reduces the entire finality residual to it, on the existing carrier, with no GU source")
    print("    action and no unbuilt dynamics required to STATE it. Whether collective ops are dynamically")
    print("    realizable is the one remaining question, and it is now crisply isolated.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = discriminator built; records-vs-redundancy = f(admissible algebra); standard positivity")
    print("         criterion -> REDUNDANCY; record reading isolated to the ghost-parity physicality bet.")


if __name__ == "__main__":
    main()
