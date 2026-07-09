"""FINALITY -- the three-wall ladder at d=3 (the qudit big swing).

Executes the qudit test (spec: open-problems/qudit-ladder-generalization-spec-2026-07-09.md) on the pieces
now buildable. Reuses the verified skeleton primitives (isotropic family, generalized negativity, full
symmetric-extension POCS) and adds the genuinely new piece: the CGLMP Bell operator, the innermost wall for
qudits (CHSH does not generalize).

Walls tested on the isotropic line rho(F):
  entanglement   negativity crosses 0 at F = 1/d          (reliable)
  shareability   full symmetric-extension SDP (POCS)       (calibrated to 2/3 on qubit Werner)
  CGLMP          fixed optimal CGLMP-3 measurements > 2     (nonlocality WITNESS; shareable => no violation)

Self-check discipline (the calibration gate): the CGLMP operator must give ~2.87 on the maximally entangled
qutrit and ~0 on white noise, else it is wrong and we do not proceed.

Run: python -m models.finality_qudit_three_walls   (exit 0)
"""
from __future__ import annotations

import numpy as np

from models.finality_ladder_qudit import (
    is_2_shareable,
    isotropic,
    max_entangled,
    negativity,
)

FAIL: list[str] = []
RNG = np.random.default_rng(20260709)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------- CGLMP Bell operator (fixed optimal measurements) ----------------
def meas_A(d, alpha):
    """columns are the outcome eigenvectors |k>_a = (1/sqrt d) sum_j w^{j(k+alpha)} |j>."""
    j = np.arange(d)[:, None]
    k = np.arange(d)[None, :]
    return np.exp(2j * np.pi / d * j * (k + alpha)) / np.sqrt(d)


def meas_B(d, beta):
    """columns are |l>_b = (1/sqrt d) sum_j w^{j(-l+beta)} |j>."""
    j = np.arange(d)[:, None]
    l = np.arange(d)[None, :]
    return np.exp(2j * np.pi / d * j * (-l + beta)) / np.sqrt(d)


def joint_probs(rho, UA, VB):
    """P[k,l] = <k,l| rho |k,l> for A-basis UA, B-basis VB."""
    d = UA.shape[0]
    P = np.zeros((d, d))
    for k in range(d):
        for l in range(d):
            psi = np.kron(UA[:, k], VB[:, l])
            P[k, l] = np.real(psi.conj() @ rho @ psi)
    return P


def QAB(P, m):
    """P(A_a = B_b + m) = sum_l P[(l+m) mod d, l]."""
    d = P.shape[0]
    return sum(P[(l + m) % d, l] for l in range(d))


def cglmp(rho, d=3):
    """CGLMP_d expression with the standard optimal settings. Local bound 2."""
    A1, A2 = meas_A(d, 0.0), meas_A(d, 0.5)
    B1, B2 = meas_B(d, 0.25), meas_B(d, -0.25)
    P11 = joint_probs(rho, A1, B1)
    P21 = joint_probs(rho, A2, B1)
    P22 = joint_probs(rho, A2, B2)
    P12 = joint_probs(rho, A1, B2)
    total = 0.0
    for k in range(d // 2):
        w = 1 - 2 * k / (d - 1)
        plus = QAB(P11, k) + QAB(P21, -(k + 1)) + QAB(P22, k) + QAB(P12, k)
        minus = QAB(P11, -(k + 1)) + QAB(P21, k) + QAB(P22, -(k + 1)) + QAB(P12, k + 1)
        total += w * (plus - minus)
    return total


def random_qudit(rng, d):
    G = rng.standard_normal((d * d, d * d)) + 1j * rng.standard_normal((d * d, d * d))
    rho = G @ G.conj().T
    return rho / np.trace(rho).real


def main():
    d = 3
    print("#" * 100)
    print(f"# FINALITY -- three-wall ladder at d={d} (qudit big swing)")
    print("#" * 100)

    # ---- [0] calibration gate: the CGLMP operator must be correct ----
    print("\n[0] CGLMP operator self-check (calibration gate)")
    v_max = cglmp(max_entangled(d), d)
    v_noise = cglmp(np.eye(d * d) / (d * d), d)
    print(f"      CGLMP(maximally entangled) = {v_max:.4f}   (expect ~2.87, the standard qutrit value)")
    print(f"      CGLMP(white noise)         = {v_noise:.4f}   (expect 0)")
    check("CGLMP on maximally entangled qutrit is ~2.87 (operator correct)", 2.80 <= v_max <= 2.95,
          f"{v_max:.4f}")
    check("CGLMP on white noise is ~0", abs(v_noise) < 1e-9, f"{v_noise:.2e}")
    if FAIL:
        print("\n  CGLMP operator failed its self-check; NOT proceeding (uncalibrated tool).")
        print(f"FAILED CHECKS: {FAIL}")
        raise SystemExit(1)

    # ---- [1] three walls on the isotropic line ----
    print("\n[1] the three walls on the isotropic line rho(F)")
    ent_wall = 1.0 / d
    # shareability wall (POCS)
    share = [(F, is_2_shareable(isotropic(F, d), d)) for F in [i / 100 for i in range(34, 100, 2)]]
    F_share = (max((F for F, s in share if s), default=0.0)
               + min((F for F, s in share if not s), default=1.0)) / 2
    # CGLMP wall: scan F for isotropic CGLMP > 2
    Fs = [i / 1000 for i in range(334, 1000)]
    cg = [(F, cglmp(isotropic(F, d), d)) for F in Fs]
    F_cglmp = min((F for F, v in cg if v > 2.0), default=1.0)
    print(f"      entanglement wall  F = 1/d      = {ent_wall:.3f}")
    print(f"      shareability wall  F_share      = {F_share:.3f}  (full extension SDP)")
    print(f"      CGLMP wall         F_CGLMP      = {F_cglmp:.3f}  (fixed optimal CGLMP-3 measurements)")
    check("three walls are ORDERED: 1/d < F_share < F_CGLMP", ent_wall < F_share < F_cglmp,
          f"{ent_wall:.3f} < {F_share:.3f} < {F_cglmp:.3f}")
    check("three walls are DISTINCT (gaps > 0.02 each)", (F_share - ent_wall) > 0.02 and (F_cglmp - F_share) > 0.02)
    check("gap 1 populated: an entangled-but-shareable isotropic state exists (F between 1/d and F_share)",
          negativity(isotropic((ent_wall + F_share) / 2, d), d) > 1e-9
          and is_2_shareable(isotropic((ent_wall + F_share) / 2, d), d))
    check("gap 2 populated: an un-shareable but CGLMP-local isotropic state exists (F between F_share and F_CGLMP)",
          (not is_2_shareable(isotropic((F_share + F_cglmp) / 2, d), d))
          and cglmp(isotropic((F_share + F_cglmp) / 2, d), d) <= 2.0)

    # ---- [2] statewise sweep (key implication I1), incl. a batch that actually VIOLATES ----
    print("\n[2] statewise sweep (I1: CGLMP-violating => un-shareable), with a genuine-violator batch")
    # batch 1: generic random states (for the gaps)
    states = [random_qudit(RNG, d) for _ in range(120)]
    # batch 2: standard-basis-aligned noisy-maxent states -> actually produce CGLMP violators off the
    # strict isotropic line, so I1 is tested NON-vacuously (fixed measurements only witness aligned states)
    Phi = max_entangled(d)
    for _ in range(50):
        q = 0.7 + 0.3 * RNG.random()
        noise = random_qudit(RNG, d)
        states.append(q * Phi + (1 - q) * noise)
    negs = [negativity(s, d) for s in states]
    cgs = [cglmp(s, d) for s in states]
    shares = [is_2_shareable(s, d) for s in states]
    i1_viol = sum(1 for c, sh in zip(cgs, shares) if c > 2 + 1e-9 and sh)
    cglmp_but_sep = sum(1 for c, n in zip(cgs, negs) if c > 2 + 1e-9 and n <= 1e-9)
    ent_and_share = sum(1 for n, sh in zip(negs, shares) if n > 1e-9 and sh)
    unshare_cglmp_local = sum(1 for c, sh in zip(cgs, shares) if (not sh) and c <= 2 + 1e-9)
    n_cglmp = sum(1 for c in cgs if c > 2 + 1e-9)
    print(f"      of {len(states)} states: {n_cglmp} CGLMP-violating, {sum(shares)} shareable")
    check("the sweep actually PRODUCED CGLMP-violating states (I1 tested non-vacuously)", n_cglmp > 0,
          f"{n_cglmp} violators")
    check("I1 holds statewise: NO CGLMP-violating shareable state (monogamy of nonlocality)", i1_viol == 0,
          f"violations={i1_viol}")
    check("NO CGLMP-violating separable state (CGLMP subset entangled)", cglmp_but_sep == 0,
          f"violations={cglmp_but_sep}")
    check("gap 1 non-empty off the isotropic line: entangled-but-shareable states exist", ent_and_share > 0,
          f"{ent_and_share} states")
    check("gap 2 non-empty off the isotropic line: un-shareable but CGLMP-local states exist",
          unshare_cglmp_local > 0, f"{unshare_cglmp_local} states")

    print("\n[verdict]")
    print("  * CGLMP operator passes its self-check (2.87 on maxent, 0 on noise) -- the new wall is correct.")
    print(f"  * THREE DISTINCT NESTED WALLS confirmed at d={d}: 1/d < F_share < F_CGLMP on the isotropic line,")
    print("    with both gaps populated. The ladder generalizes from qubits to qutrits.")
    print("  * Statewise on random 3x3 states, the key implication I1 (CGLMP-violating => un-shareable) holds")
    print("    with zero violations, and both gaps stay non-empty off the isotropic line.")
    print("  * Honest limits: shareability via POCS (not a certified SDP); 'entangled' = NPT (bound")
    print("    entanglement not separately detected); measurements fixed (a nonlocality witness, sufficient).")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print(f"\nexit 0 = three-wall ladder generalizes to d={d}: entanglement < shareability < CGLMP, walls distinct.")


if __name__ == "__main__":
    main()
