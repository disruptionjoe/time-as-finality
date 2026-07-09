"""FINALITY -- P1: the constructor axiom on the shareability-bounded band.

Starter-swing P1 said the "reverse the correlation" axiom is viable ONLY if (a) restricted to the
reversible+deterministic+state-preserving task and (b) graded by a QRT monotone, not by binary constructor
theory. This model states the restricted task and settles where its possible->impossible flip lands,
relative to the shareability inner wall from swing C (models/finality_swing_C_inner_label.py).

Task T_reversible: "by a LOCAL UNITARY (reversible, deterministic, no measurement), map the shared state to
a PRODUCT state." Local unitaries preserve every entanglement monotone, and a product target has negativity
0; so T_reversible is POSSIBLE iff the state is already separable, IMPOSSIBLE iff entangled. That is the
clean Deutsch-Marletto possible/impossible pair, and negativity (a QRT monotone) is the grading.

Carrier: the 2-qubit singlet Werner family rho_p = p |psi-><psi-| + (1-p) I/4, swept in p. Three thresholds
are visible on one family:
    p = 1/3      entanglement onset      (negativity crosses 0)        <- the CONSTRUCTOR wall
    p = 2/3      2-shareability / monogamy wall   (from swing C)       <- the inner label (k_max finite)
    p = 1/sqrt2  CHSH violation           (~0.707)                     <- the deepest wall

Run: python -m models.finality_constructor_axiom_band   (exit 0)
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []
TOL = 1e-9


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# --- 2-qubit machinery ---
I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]

PSI_MINUS = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
RHO_SINGLET = np.outer(PSI_MINUS, PSI_MINUS.conj())


def werner(p):
    return p * RHO_SINGLET + (1 - p) * np.eye(4) / 4


def partial_transpose_B(rho):
    r = rho.reshape(2, 2, 2, 2)               # iA, iB, jA, jB
    r = r.transpose(0, 3, 2, 1)               # swap iB <-> jB
    return r.reshape(4, 4)


def negativity(rho):
    ev = np.linalg.eigvalsh(partial_transpose_B(rho))
    return float(sum(-e for e in ev if e < 0))   # |sum of negative eigenvalues|


def chsh_max(rho):
    """Horodecki: CHSH_max = 2 sqrt(sum of two largest eigenvalues of T^T T)."""
    T = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            op = np.kron(PAULI[i], PAULI[j])
            T[i, j] = np.real(np.trace(rho @ op))
    evals = np.linalg.eigvalsh(T.T @ T)
    return float(2 * np.sqrt(evals[-1] + evals[-2]))


def dephase_B(rho):
    """irreversible local dephasing of qubit B in the Z basis (a NON-reversible admissible local op)."""
    IZ = np.kron(I2, SZ)
    return (rho + IZ @ rho @ IZ) / 2


def constructor_impossible(rho):
    """T_reversible (local unitary to a product state) is IMPOSSIBLE iff the state is entangled."""
    return negativity(rho) > TOL


ENT_WALL = 1.0 / 3.0
SHARE_WALL = 2.0 / 3.0          # from swing C (symmetric-extension SDP)
CHSH_WALL = 1.0 / np.sqrt(2)   # ~0.7071


def main():
    print("#" * 100)
    print("# FINALITY P1 -- constructor axiom (reversible task) on the shareability-bounded band")
    print("#" * 100)

    ps = [i / 100 for i in range(0, 101)]
    negs = [negativity(werner(p)) for p in ps]
    imposs = [constructor_impossible(werner(p)) for p in ps]

    # --- [1] constructor flip == negativity crossing 0 == entanglement onset (p = 1/3) ---
    print("\n[1] constructor possible->impossible flip vs the QRT monotone (negativity)")
    flip_p = next(p for p, im in zip(ps, imposs) if im)   # smallest p that is impossible
    check("constructor task is POSSIBLE below and IMPOSSIBLE above a single flip", all(
        imposs[i] <= imposs[i + 1] for i in range(len(imposs) - 1)))
    check("the flip coincides with negativity crossing 0 at p = 1/3", abs(flip_p - ENT_WALL) <= 0.011,
          f"flip at p={flip_p:.2f}, entanglement wall=1/3={ENT_WALL:.3f}")
    check("below the wall negativity = 0 (separable, task possible)", negativity(werner(0.30)) < TOL)
    check("above the wall negativity > 0 (entangled, task impossible)", negativity(werner(0.40)) > TOL)

    # --- [2] negativity supplies the grading the binary verdict lacks ---
    print("\n[2] QRT grading")
    entangled_ps = [(p, n) for p, n in zip(ps, negs) if p > ENT_WALL + 0.02]
    mono = all(entangled_ps[i][1] <= entangled_ps[i + 1][1] + 1e-12 for i in range(len(entangled_ps) - 1))
    distinct = len({round(n, 6) for _, n in entangled_ps}) > 20
    check("negativity is monotone increasing in p across the entangled region", mono)
    check("negativity takes many distinct values (a genuine continuum, not a binary)", distinct,
          f"{len({round(n,6) for _,n in entangled_ps})} distinct values")

    # --- [3] the constructor wall is the OUTERMOST of three nested walls ---
    print("\n[3] three nested walls on one family")
    print(f"      entanglement (negativity) wall  p = 1/3   = {ENT_WALL:.3f}   <- constructor task flips here")
    print(f"      shareability (monogamy) wall    p = 2/3   = {SHARE_WALL:.3f}   (swing C)")
    print(f"      CHSH wall                        p = 1/sqrt2 = {CHSH_WALL:.3f}")
    check("ordering 1/3 < 2/3 < 1/sqrt2 holds", ENT_WALL < SHARE_WALL < CHSH_WALL)
    # a state strictly between the constructor wall and the shareability wall: entangled yet shareable
    mid = werner(0.50)
    check("at p=0.50: constructor IMPOSSIBLE (entangled) yet BELOW the shareability wall",
          constructor_impossible(mid) and 0.50 < SHARE_WALL,
          "entangled-but-shareable band: constructor wall is strictly outside the monogamous inner band")
    check("at p=0.50: CHSH does NOT yet fire (CHSH_max <= 2)", chsh_max(mid) <= 2.0 + 1e-9,
          f"CHSH_max(0.50)={chsh_max(mid):.3f}")

    # --- [4] the reversible restriction is necessary (loose 'reverse' is false) ---
    print("\n[4] why the task MUST be restricted to reversible+deterministic")
    ent = werner(0.90)
    n_before = negativity(ent)
    n_after = negativity(dephase_B(ent))
    check("an entangled state has negativity > 0 (constructor task impossible reversibly)", n_before > TOL,
          f"N={n_before:.3f}")
    check("an IRREVERSIBLE local op (dephasing) drives negativity to 0 -> 'remove correlation' becomes POSSIBLE",
          n_after < TOL, f"N after dephasing={n_after:.3e}")
    check("=> the impossibility holds ONLY for the reversible+deterministic+state-preserving task",
          n_before > TOL and n_after < TOL,
          "loose 'reverse' (allow measurement/dephasing) is FALSE; the restriction is load-bearing")

    print("\n[verdict]")
    print("  * The constructor axiom, restricted to the reversible+deterministic+state-preserving task,")
    print("    states as a clean Deutsch-Marletto pair: POSSIBLE severally iff separable, IMPOSSIBLE iff")
    print("    entangled. Its flip coincides EXACTLY with the QRT monotone (negativity) crossing 0.")
    print("  * Negativity supplies the grading constructor theory (binary) cannot -- fix (b) confirmed.")
    print("  * The reversible restriction is load-bearing: an irreversible local op disentangles, so the")
    print("    loose axiom is false -- fix (a) confirmed.")
    print("  * PLACEMENT: the constructor task pins the ENTANGLEMENT wall (p=1/3), the OUTERMOST of three")
    print("    nested walls (entanglement 1/3 < shareability 2/3 < CHSH 1/sqrt2). It bounds entanglement,")
    print("    NOT the monogamous inner band that swing C's k_max labels. So the band has a graded LADDER of")
    print("    walls, each with its own monotone: negativity (constructor), shareability k_max (monogamy),")
    print("    CHSH. P1 supplies the outermost rung and its grading.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = constructor axiom built on the bounded band; pins the entanglement wall, graded by negativity.")


if __name__ == "__main__":
    main()
