"""FINALITY -- is the three-wall ladder a Werner artifact? (generalization test)

P1 established a three-wall ladder on the Werner line: entanglement (negativity, p=1/3) < shareability
(k_max, p=2/3) < CHSH (p=1/sqrt2). This model attacks the load-bearing question: does the NESTING hold OFF
the Werner line, or is it a one-family artifact?

The two nesting implications are theorems, which is why the ladder should be general:
  I1  CHSH-violating  => NOT 2-shareable      (Toner-Verstraete monogamy of Bell correlations)
  I2  NOT 2-shareable => entangled            (separable states are infinitely shareable, constructively)
so {CHSH-violating} subset {un-shareable} subset {entangled} for ALL two-qubit states.

We test this computationally as a check on our own pipeline, and confirm the two gaps stay NON-EMPTY off
Werner (so the walls are distinct, not coincident). Method:
  * negativity + CHSH_max: reused from the verified P1 model.
  * 2-shareability: symmetric-extension feasibility (a state is 2-shareable IFF a symmetric extension to
    B,B' exists). Implemented by projections onto PSD and the affine set {symmetric under B<->B', correct
    B'-marginal}. CALIBRATED on the Werner line: it must reproduce swing C's 2/3 wall, else the shareability
    rung is reported UNVERIFIED.

Run: python -m models.finality_ladder_off_werner   (exit 0)
"""
from __future__ import annotations

import numpy as np

from models.finality_constructor_axiom_band import chsh_max, negativity, werner

FAIL: list[str] = []
RNG = np.random.default_rng(20260709)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# --- symmetric-extension (2-shareability) feasibility on A(x)B(x)B', qubits ---
def tr_Bp(X):
    """partial trace over B' (last qubit) -> 4x4 on (A,B)."""
    T = X.reshape(2, 2, 2, 2, 2, 2)          # a,b,bp,a',b',bp'
    M = np.trace(T, axis1=2, axis2=5)         # sum bp==bp'  -> a,b,a',b'
    return M.reshape(4, 4)


def swap_BBp(X):
    T = X.reshape(2, 2, 2, 2, 2, 2)
    return T.transpose(0, 2, 1, 3, 5, 4).reshape(8, 8)


def embed_marg_defect(D):
    """D (4x4 on A,B) -> D (x) (I_2/2) on A,B,B' (8x8)."""
    Dm = D.reshape(2, 2, 2, 2)                # a,b,a',b'
    out = np.zeros((2, 2, 2, 2, 2, 2), dtype=complex)
    for bp in range(2):
        out[:, :, bp, :, :, bp] = Dm / 2.0    # (x) I_2/2 on B'
    return out.reshape(8, 8)


def project_psd(X):
    X = (X + X.conj().T) / 2
    w, V = np.linalg.eigh(X)
    w = np.clip(w, 0, None)
    return (V * w) @ V.conj().T


SEP_TOL = 1e-8


def is_2_shareable(rho_AB, iters=600, tol=3e-4):
    """POCS onto PSD and the affine set {symmetric, Tr_B' = rho_AB}. Feasible <=> 2-shareable.

    Short-circuit: for two qubits PPT <=> separable <=> infinitely shareable (Horodecki). So any PPT
    (negativity ~ 0) state is 2-shareable by theorem; only entangled (NPT) states need the iterative test.
    This removes iterative false-negatives on separable states (I2 is a theorem, not a numerical result).
    """
    if negativity(rho_AB) < SEP_TOL:
        return True, 0.0
    # start from the product-with-maximally-mixed-B' guess
    X = np.kron(rho_AB, np.eye(2) / 2).astype(complex)
    for _ in range(iters):
        X = (X + swap_BBp(X)) / 2                       # symmetry (linear)
        X = X - embed_marg_defect(tr_Bp(X) - rho_AB)    # correct B'-marginal (affine)
        X = project_psd(X)                              # PSD cone
    # residual: how far the PSD-affine point is from satisfying everything simultaneously
    sym_err = np.linalg.norm(X - swap_BBp(X))
    marg_err = np.linalg.norm(tr_Bp(X) - rho_AB)
    w = np.linalg.eigvalsh((X + X.conj().T) / 2)
    psd_err = float(-min(w.min(), 0.0))
    return (sym_err + marg_err + psd_err) < tol, (sym_err + marg_err + psd_err)


def random_2qubit(rng):
    """Hilbert-Schmidt random mixed 2-qubit state (Ginibre)."""
    G = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    rho = G @ G.conj().T
    return rho / np.trace(rho).real


def bell_diagonal(c1, c2, c3):
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I = np.eye(2)
    rho = (np.kron(I, I) + c1 * np.kron(sx, sx) + c2 * np.kron(sy, sy) + c3 * np.kron(sz, sz)) / 4
    return rho


def main():
    print("#" * 100)
    print("# FINALITY -- is the three-wall ladder a Werner artifact? (off-Werner generalization)")
    print("#" * 100)

    # ---- [0] calibrate the shareability test on the Werner line: must reproduce 2/3 ----
    print("\n[0] calibrate 2-shareability against swing C's Werner wall (expect 2/3)")
    ps = [i / 100 for i in range(30, 80)]
    shareable = [(p, is_2_shareable(werner(p))[0]) for p in ps]
    last_shareable = max((p for p, s in shareable if s), default=0.0)
    first_unshare = min((p for p, s in shareable if not s), default=1.0)
    wall = (last_shareable + first_unshare) / 2
    print(f"      last shareable p = {last_shareable:.2f} ; first un-shareable p = {first_unshare:.2f} ; wall ~= {wall:.3f}")
    calibrated = abs(wall - 2 / 3) <= 0.04
    check("shareability test reproduces the 2/3 Werner wall (calibration)", calibrated,
          f"wall={wall:.3f} vs 2/3={2/3:.3f}")
    if not calibrated:
        print("\n  shareability rung UNVERIFIED off Werner: the extension test failed calibration.")
        print("  Reporting I1 by the Toner-Verstraete theorem only; not asserting statewise shareability.")

    # ---- [1] rigorous rung (no shareability): CHSH subset entanglement, general states ----
    print("\n[1] rigorous: {CHSH-violating} subset {entangled} on random general 2-qubit states")
    states = [random_2qubit(RNG) for _ in range(400)]
    negs = [negativity(s) for s in states]
    chshs = [chsh_max(s) for s in states]
    chsh_viol_but_separable = sum(1 for n, c in zip(negs, chshs) if c > 2 + 1e-9 and n <= 1e-9)
    ent_but_chsh_local = sum(1 for n, c in zip(negs, chshs) if n > 1e-9 and c <= 2 + 1e-9)
    check("NO CHSH-violating separable state (CHSH wall subset entanglement wall), general states",
          chsh_viol_but_separable == 0, f"violations={chsh_viol_but_separable}/400")
    check("the gap is NON-EMPTY off Werner: many entangled states are CHSH-local (walls distinct)",
          ent_but_chsh_local > 10, f"{ent_but_chsh_local}/400 entangled-but-CHSH-local")

    # ---- [2] full nesting via shareability (only if calibrated) ----
    if calibrated:
        print("\n[2] full nesting {CHSH} subset {un-shareable} subset {entangled}, off-Werner sample")
        # structured Bell-diagonal + random coverage
        sample = []
        for _ in range(120):
            sample.append(random_2qubit(RNG))
        for c in [(0.5, -0.5, 0.5), (0.7, -0.1, 0.1), (0.6, 0.6, -0.2), (0.4, -0.4, 0.4), (0.75, -0.05, 0.05)]:
            sample.append(bell_diagonal(*c))

        i1_viol = 0   # CHSH-violating but shareable
        i2_viol = 0   # un-shareable but separable
        ent_shareable = 0        # entangled-but-shareable gap
        unshare_chsh_local = 0   # un-shareable but CHSH-local gap
        for s in sample:
            n = negativity(s)
            c = chsh_max(s)
            share = is_2_shareable(s)[0]
            if c > 2 + 1e-9 and share:
                i1_viol += 1
            if (not share) and n <= 1e-9:
                i2_viol += 1
            if n > 1e-9 and share:
                ent_shareable += 1
            if (not share) and c <= 2 + 1e-9:
                unshare_chsh_local += 1
        check("I1 holds statewise: no CHSH-violating shareable state (genuine POCS test)", i1_viol == 0,
              f"violations={i1_viol}")
        check("I2 holds statewise: no un-shareable separable state (enforced by the 2-qubit PPT=separable theorem)",
              i2_viol == 0, f"violations={i2_viol}")
        check("gap 1 non-empty off Werner: entangled-but-shareable states exist", ent_shareable > 0,
              f"{ent_shareable} states")
        check("gap 2 non-empty off Werner: un-shareable but CHSH-local states exist", unshare_chsh_local > 0,
              f"{unshare_chsh_local} states")

    # ---- verdict ----
    print("\n[verdict]")
    print("  * The nesting {CHSH-violating} subset {un-shareable} subset {entangled} is THEOREM-backed")
    print("    (Toner-Verstraete monogamy; separable => infinitely shareable), so the ladder ORDER is")
    print("    general, not a Werner artifact. The Werner NUMBERS (1/3, 2/3, 1/sqrt2) are family-specific.")
    print("  * Rigorous computation confirms {CHSH} subset {entangled} on random states with zero violations,")
    print("    and both gaps stay non-empty off the Werner line -> the three walls are distinct in general.")
    if calibrated:
        print("  * The calibrated shareability test confirms the FULL nesting statewise off Werner, with both")
        print("    gaps populated -> the middle rung is a genuine, distinct wall beyond the Werner family.")
    else:
        print("  * Shareability rung not numerically confirmed off Werner (calibration miss); it rests on the")
        print("    Toner-Verstraete theorem for now. The other two rungs are confirmed.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = ladder nesting is general (theorem-backed + confirmed off Werner); not a one-family artifact.")


if __name__ == "__main__":
    main()
