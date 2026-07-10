"""FINALITY -- the three-wall ladder at d=4 (T515), and a CGLMP-d correction.

Closes honest-limit #4 of the qudit result ("d=3 only; d>=4 unchecked"):
extends entanglement < shareability < CGLMP to d=4.

IMPORTANT FINDING -- a latent bug in the d=3 CGLMP operator, surfaced at d=4.
The CGLMP sum runs k = 0 .. d/2 - 1. For d in {2,3} only k=0 fires, so the
operator in models.finality_qudit_three_walls was never exercised on its k>=1
terms. At d=4 the k=1 term fires and reveals a sign error in ONE positive term
(P(B2 = A1 + k) was coded as QAB(P12, k); it must be QAB(P12, -k)). With the
fix, CGLMP(maximally entangled) matches the standard CGLMP values EXACTLY at
d=2,3,4,5: 2.8284, 2.8729, 2.8962, 2.9105. The d=3 ladder result is UNAFFECTED
(it only ever used the k=0 term). This model carries the corrected operator.

Walls on the isotropic line rho(F), d=4:
  entanglement  F = 1/d = 0.25                         (negativity)
  shareability  F_share = (d+1)/(2d) = 0.625           (full symmetric-extension POCS + closed form)
  CGLMP         F_CGLMP ~ 0.706  (visibility 0.6906)   (corrected CGLMP-4 witness)

Run: python -m models.finality_qudit_d4_ladder   (exit 0)
"""
from __future__ import annotations

import numpy as np

from models.finality_ladder_qudit import (
    is_2_shareable,
    isotropic,
    max_entangled,
    negativity,
)
from models.finality_qudit_three_walls import joint_probs, meas_A, meas_B, QAB

FAIL: list[str] = []
RNG = np.random.default_rng(20260709)

# standard CGLMP maximally-entangled-state values (Collins-Gisin-Linden-Massar-Popescu 2002)
CGLMP_MAXENT = {2: 2.8284, 3: 2.8729, 4: 2.8962, 5: 2.9105}


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def cglmp(rho, d):
    """Corrected CGLMP_d expression with the standard optimal settings. Local bound 2.

    Fix vs models.finality_qudit_three_walls.cglmp: the fourth positive term is
    P(B2 = A1 + k) = P(A1 = B2 - k) = QAB(P12, -k), NOT QAB(P12, k). Identical
    for k=0 (d<=3); corrected for k>=1 (d>=4).
    """
    A1, A2 = meas_A(d, 0.0), meas_A(d, 0.5)
    B1, B2 = meas_B(d, 0.25), meas_B(d, -0.25)
    P11 = joint_probs(rho, A1, B1)
    P21 = joint_probs(rho, A2, B1)
    P22 = joint_probs(rho, A2, B2)
    P12 = joint_probs(rho, A1, B2)
    total = 0.0
    for k in range(d // 2):
        w = 1 - 2 * k / (d - 1)
        plus = QAB(P11, k) + QAB(P21, -(k + 1)) + QAB(P22, k) + QAB(P12, -k)
        minus = QAB(P11, -(k + 1)) + QAB(P21, k) + QAB(P22, -(k + 1)) + QAB(P12, k + 1)
        total += w * (plus - minus)
    return total


def random_qudit(rng, d):
    G = rng.standard_normal((d * d, d * d)) + 1j * rng.standard_normal((d * d, d * d))
    rho = G @ G.conj().T
    return rho / np.trace(rho).real


def main():
    d = 4
    print("#" * 100)
    print(f"# FINALITY -- three-wall ladder at d={d} (with CGLMP-d correction)")
    print("#" * 100)

    # ---- [0] calibration gate: corrected CGLMP must match the standard values at d=2..5 ----
    print("\n[0] CGLMP-d operator self-check (calibration gate) -- corrected operator")
    for dd in (2, 3, 4, 5):
        v = cglmp(max_entangled(dd), dd)
        vn = cglmp(np.eye(dd * dd) / (dd * dd), dd)
        print(f"      d={dd}: CGLMP(maxent)={v:.4f} (expect {CGLMP_MAXENT[dd]})   noise={vn:.2e}")
        check(f"corrected CGLMP(maxent) matches standard value at d={dd}",
              abs(v - CGLMP_MAXENT[dd]) < 5e-4, f"{v:.4f} vs {CGLMP_MAXENT[dd]}")
        check(f"CGLMP(white noise)=0 at d={dd}", abs(vn) < 1e-9)
    # demonstrate the old operator was wrong at d=4
    from models.finality_qudit_three_walls import cglmp as cglmp_old
    v_old4 = cglmp_old(max_entangled(4), 4)
    check("the d=3-era CGLMP operator is INCORRECT at d=4 (motivates the fix)",
          abs(v_old4 - CGLMP_MAXENT[4]) > 1e-2, f"old d=4 value={v_old4:.4f} (should be 2.8962)")
    if FAIL:
        print("\n  CGLMP operator failed its self-check; NOT proceeding (uncalibrated tool).")
        print(f"FAILED CHECKS: {FAIL}")
        raise SystemExit(1)

    # ---- [1] three walls on the isotropic line at d=4 ----
    # d^3 = 64: POCS needs more iterations than the d=3 default to converge (500 -> biased low).
    ITERS = 1500
    print(f"\n[1] the three walls on the isotropic line rho(F) at d={d}  (shareability POCS iters={ITERS})")
    ent_wall = 1.0 / d
    share = [(F, is_2_shareable(isotropic(F, d), d, iters=ITERS))
             for F in [round(0.25 + 0.025 * i, 3) for i in range(1, 20)]]
    F_share = (max((F for F, sh in share if sh), default=0.0)
               + min((F for F, sh in share if not sh), default=1.0)) / 2
    closed_form_share = (d + 1) / (2 * d)
    Fs = [i / 1000 for i in range(250, 1000)]
    cg = [(F, cglmp(isotropic(F, d), d)) for F in Fs]
    F_cglmp = min((F for F, v in cg if v > 2.0), default=1.0)
    v_cglmp = (d * d * F_cglmp - 1) / (d * d - 1)
    print(f"      entanglement wall  F = 1/d      = {ent_wall:.3f}")
    print(f"      shareability wall  F_share      = {F_share:.3f}  (POCS; closed form (d+1)/2d = {closed_form_share:.3f})")
    print(f"      CGLMP wall         F_CGLMP      = {F_cglmp:.3f}  (visibility {v_cglmp:.4f}; lit v_crit(4) ~ 0.6906)")
    check("three walls are ORDERED: 1/d < F_share < F_CGLMP", ent_wall < F_share < F_cglmp,
          f"{ent_wall:.3f} < {F_share:.3f} < {F_cglmp:.3f}")
    check("three walls are DISTINCT (gaps > 0.02 each)",
          (F_share - ent_wall) > 0.02 and (F_cglmp - F_share) > 0.02)
    check("shareability wall matches the closed form (d+1)/2d within POCS tolerance",
          abs(F_share - closed_form_share) < 0.02, f"{F_share:.3f} vs {closed_form_share:.3f}")
    check("CGLMP wall visibility matches literature v_crit(4) ~ 0.6906 within 0.005",
          abs(v_cglmp - 0.6906) < 0.005, f"{v_cglmp:.4f}")
    mid1 = (ent_wall + F_share) / 2
    mid2 = (F_share + F_cglmp) / 2
    check("gap 1 populated: an entangled-but-shareable isotropic state exists",
          negativity(isotropic(mid1, d), d) > 1e-9 and is_2_shareable(isotropic(mid1, d), d, iters=ITERS))
    check("gap 2 populated: an un-shareable but CGLMP-local isotropic state exists",
          (not is_2_shareable(isotropic(mid2, d), d, iters=ITERS)) and cglmp(isotropic(mid2, d), d) <= 2.0)

    # ---- [2] statewise sweep at d=4 (key implication I1) ----
    # sweep uses the default POCS iters; under-convergence only UNDER-counts shareable states, so it
    # cannot manufacture a spurious I1 violation (violation = CGLMP-violating AND shareable).
    print(f"\n[2] statewise sweep at d={d} (I1: CGLMP-violating => un-shareable), with a genuine-violator batch")
    states = [random_qudit(RNG, d) for _ in range(30)]
    Phi = max_entangled(d)
    for _ in range(25):
        q = 0.75 + 0.25 * RNG.random()
        states.append(q * Phi + (1 - q) * random_qudit(RNG, d))
    negs = [negativity(s, d) for s in states]
    cgs = [cglmp(s, d) for s in states]
    shares = [is_2_shareable(s, d) for s in states]
    n_cglmp = sum(1 for c in cgs if c > 2 + 1e-9)
    i1_viol = sum(1 for c, sh in zip(cgs, shares) if c > 2 + 1e-9 and sh)
    cglmp_but_sep = sum(1 for c, n in zip(cgs, negs) if c > 2 + 1e-9 and n <= 1e-9)
    print(f"      of {len(states)} states: {n_cglmp} CGLMP-violating, {sum(shares)} shareable")
    check("the sweep actually PRODUCED CGLMP-violating states (I1 tested non-vacuously)", n_cglmp > 0,
          f"{n_cglmp} violators")
    check("I1 holds statewise at d=4: NO CGLMP-violating shareable state (monogamy of nonlocality)",
          i1_viol == 0, f"violations={i1_viol}")
    check("NO CGLMP-violating separable state at d=4 (CGLMP subset entangled)", cglmp_but_sep == 0,
          f"violations={cglmp_but_sep}")

    print("\n[verdict]")
    print(f"  * The corrected CGLMP-d operator matches the standard values at d=2,3,4,5 EXACTLY;")
    print("    the d=3-era operator was wrong at d>=4 (untested k>=1 term). d=3 ladder unaffected.")
    print(f"  * THREE DISTINCT NESTED WALLS confirmed at d={d}: 1/d < (d+1)/2d < F_CGLMP, both gaps")
    print("    populated, and I1 (CGLMP-violating => un-shareable) holds statewise on genuine violators.")
    print("  * The three-wall ladder now holds at d = 2, 3, 4; the Werner/isotropic NUMBERS move with d")
    print("    (walls 1/d and (d+1)/2d both shrink), but the STRUCTURE is dimension-independent.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print(f"\nexit 0 = three-wall ladder generalizes to d={d}; CGLMP-d operator corrected and calibrated.")


if __name__ == "__main__":
    main()
