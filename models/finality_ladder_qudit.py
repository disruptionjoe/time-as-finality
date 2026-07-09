"""FINALITY -- qudit generalization of the three-wall ladder (SKELETON).

Sets up the d > 2 test (spec: open-problems/qudit-ladder-generalization-spec-2026-07-09.md). Implements the
pieces that generalize cleanly and correctly to qudits NOW, on the isotropic family, and prints the walls it
can compute. The harder pieces (CGLMP Bell operator, CCNR bound-entanglement witness, random-state statewise
sweep, literature threshold confirmation) are explicit TODOs -- this is a runnable harness, not the finished
test.

KEY SHIFT from two qubits: PPT != separable for d > 2 (bound entanglement), so the 2-qubit
`PPT => shareable` short-circuit is INVALID here. Shareability must come from the full symmetric-extension
SDP. Calibration is anchored on the isotropic family, where separable <=> PPT <=> F <= 1/d is known.

Run: python -m models.finality_ladder_qudit   (exit 0; prints the implemented walls + the TODO list)
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []
D = 3  # qudit dimension (skeleton runs at d=3)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---- isotropic family ----
def max_entangled(d):
    v = np.zeros(d * d, dtype=complex)
    for i in range(d):
        v[i * d + i] = 1.0 / np.sqrt(d)
    return np.outer(v, v.conj())


def isotropic(F, d):
    Phi = max_entangled(d)
    I = np.eye(d * d)
    return F * Phi + (1 - F) / (d * d - 1) * (I - Phi)


# ---- generalized negativity (partial transpose on B) ----
def partial_transpose_B(rho, d):
    T = rho.reshape(d, d, d, d)              # a, b, a', b'
    T = T.transpose(0, 3, 2, 1)              # a, b', a', b  (swap b <-> b')
    return T.reshape(d * d, d * d)


def negativity(rho, d):
    ev = np.linalg.eigvalsh(partial_transpose_B(rho, d))
    return float(sum(-e for e in ev if e < 0))


# ---- generalized symmetric-extension (2-shareability) via POCS in d^3 ----
def tr_Bp(X, d):
    T = X.reshape(d, d, d, d, d, d)          # a, b, bp, a', b', bp'
    M = np.trace(T, axis1=2, axis2=5)         # sum bp==bp' -> a, b, a', b'
    return M.reshape(d * d, d * d)


def swap_BBp(X, d):
    T = X.reshape(d, d, d, d, d, d)
    return T.transpose(0, 2, 1, 3, 5, 4).reshape(d ** 3, d ** 3)


def embed_marg_defect(Dm, d):
    """D (d^2 x d^2 on A,B) -> D (x) (I_d/d) on A,B,B'."""
    Dr = Dm.reshape(d, d, d, d)              # a, b, a', b'
    out = np.zeros((d, d, d, d, d, d), dtype=complex)
    for bp in range(d):
        out[:, :, bp, :, :, bp] = Dr / d      # (x) I_d/d on B'
    return out.reshape(d ** 3, d ** 3)


def project_psd(X):
    X = (X + X.conj().T) / 2
    w, V = np.linalg.eigh(X)
    return (V * np.clip(w, 0, None)) @ V.conj().T


def is_2_shareable(rho_AB, d, iters=500, tol=1e-3):
    """POCS onto PSD and {symmetric under B<->B', Tr_B' = rho_AB}. Feasible <=> 2-shareable.

    NOTE: no PPT=separable short-circuit here -- invalid for d > 2. This is the full extension test.
    """
    X = np.kron(rho_AB, np.eye(d) / d).astype(complex)
    for _ in range(iters):
        X = (X + swap_BBp(X, d)) / 2
        X = X - embed_marg_defect(tr_Bp(X, d) - rho_AB, d)
        X = project_psd(X)
    sym_err = np.linalg.norm(X - swap_BBp(X, d))
    marg_err = np.linalg.norm(tr_Bp(X, d) - rho_AB)
    w = np.linalg.eigvalsh((X + X.conj().T) / 2)
    psd_err = float(-min(w.min(), 0.0))
    return (sym_err + marg_err + psd_err) < tol


# ---- TODO stubs (the real remaining build) ----
def cglmp_value(rho, d):
    """TODO: construct the CGLMP-d Bell operator and return its optimal expectation.
    Local bound 2. Replaces CHSH as the innermost wall for qudits."""
    raise NotImplementedError("CGLMP operator not yet implemented -- see spec section 3")


def ccnr_entangled(rho, d):
    """TODO: realignment / CCNR criterion -- a bound-entanglement witness negativity misses for d > 2."""
    raise NotImplementedError("CCNR witness not yet implemented -- see spec shift 2")


def main():
    d = D
    print("#" * 100)
    print(f"# FINALITY -- qudit three-wall ladder SKELETON (d = {d})")
    print("#" * 100)

    # --- entanglement wall: isotropic separable <=> F <= 1/d (reliable anchor) ---
    print(f"\n[1] entanglement wall on the isotropic line (expect F = 1/d = {1/d:.3f})")
    Fs = [i / 100 for i in range(0, 101)]
    negs = [negativity(isotropic(F, d), d) for F in Fs]
    ent_wall = min((F for F, n in zip(Fs, negs) if n > 1e-9), default=1.0)
    check("isotropic is separable (negativity 0) below 1/d", negativity(isotropic(1 / d - 0.03, d), d) < 1e-9)
    check("isotropic is entangled (negativity > 0) above 1/d", negativity(isotropic(1 / d + 0.03, d), d) > 1e-9)
    check("negativity crosses 0 at F = 1/d", abs(ent_wall - 1 / d) <= 0.02, f"empirical wall F={ent_wall:.3f}")

    # --- shareability wall: full symmetric-extension SDP (no shortcut) ---
    print(f"\n[2] shareability wall on the isotropic line (full extension SDP; POCS in d^3 = {d**3})")
    share = [(F, is_2_shareable(isotropic(F, d), d)) for F in [i / 100 for i in range(30, 100, 2)]]
    last_share = max((F for F, s in share if s), default=0.0)
    first_unshare = min((F for F, s in share if not s), default=1.0)
    share_wall = (last_share + first_unshare) / 2
    print(f"      empirical isotropic 2-shareability wall  F_share(d={d}) ~= {share_wall:.3f}")
    check("shareability wall sits strictly ABOVE the entanglement wall (1/d < F_share)",
          share_wall > 1 / d + 0.02, f"1/d={1/d:.3f} < F_share~={share_wall:.3f}")
    check("the extension SDP runs and gives a monotone shareable->unshareable transition",
          last_share < first_unshare + 1e-9)

    # --- what is NOT yet done ---
    print("\n[3] NOT YET IMPLEMENTED (the real remaining build; see spec)")
    todos = [
        "CGLMP-d Bell operator + isotropic CGLMP threshold F_CGLMP(3)  (innermost wall)",
        "CCNR / realignment witness for PPT-bound entanglement (d>2: negativity != separability)",
        "random general d x d statewise sweep of {CGLMP} subset {un-shareable} subset {entangled}",
        "literature confirmation of F_share(3) and F_CGLMP(3) to calibrate the SDP and CGLMP",
    ]
    for t in todos:
        print(f"      TODO: {t}")
    for fn in (cglmp_value, ccnr_entangled):
        try:
            fn(isotropic(0.9, d), d)
            check(f"{fn.__name__} is implemented", True)
        except NotImplementedError:
            print(f"      [stub] {fn.__name__} raises NotImplementedError (expected)")

    print("\n[verdict]")
    print(f"  * Skeleton live at d={d}: entanglement wall (F=1/d) and a full-SDP shareability wall computed")
    print(f"    on the isotropic family, ordered 1/d < F_share as the ladder predicts. Both use no 2-qubit")
    print("    shortcut, so they generalize honestly.")
    print("  * The innermost (CGLMP) wall, the bound-entanglement witness, and the statewise sweep are the")
    print("    remaining build. Next move: confirm F_share(3)/F_CGLMP(3) from literature, implement CGLMP,")
    print("    then run the sweep (spec: open-problems/qudit-ladder-generalization-spec-2026-07-09.md).")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = qudit skeleton runs; two of three walls generalize on the isotropic line; ladder harness ready.")


if __name__ == "__main__":
    main()
