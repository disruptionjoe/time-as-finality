"""FINALITY -- CCNR / realignment witness: upgrade the ladder's outer wall (T514).

Closes honest-limit #2 of the qudit three-wall ladder
(explorations/qudit-three-wall-ladder-result-2026-07-09.md): the outer wall was
"NPT-entangled" (negativity > 0), NOT "entangled", because for d > 2 negativity
misses PPT bound entanglement. This model adds the computable cross-norm /
realignment (CCNR) criterion -- a genuine bound-entanglement witness -- and
certifies that it detects a known 3x3 PPT bound-entangled state (the Tiles UPB
state) that negativity provably cannot see.

CCNR criterion (Rudolph; Chen-Wu): for the realignment R(rho) with
R(rho)[(a a'), (b b')] = rho[(a b), (a' b')], every SEPARABLE state has
||R(rho)||_1 (sum of singular values) <= 1. So ||R(rho)||_1 > 1 => entangled.
It is a sufficient (not necessary) witness, independent of the PPT test.

Calibration gates (the model refuses to proceed if any fail):
  * separable product state           -> CCNR <= 1
  * isotropic separability point F=1/d -> CCNR = 1 exactly (boundary)
  * NPT-entangled isotropic F=0.9      -> CCNR > 1 (agrees with negativity)
  * Tiles UPB bound-entangled state    -> negativity ~ 0 but CCNR > 1 (the payoff)

Run: python -m models.finality_ccnr_bound_entanglement_witness   (exit 0)
"""
from __future__ import annotations

import numpy as np

from models.finality_ladder_qudit import isotropic, negativity

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------- realignment / CCNR ----------------
def realign(rho, d):
    """R(rho)[(a a'), (b b')] = rho[(a b), (a' b')]. rho indexed (a b),(a' b')."""
    T = rho.reshape(d, d, d, d)          # a, b, a', b'
    R = T.transpose(0, 2, 1, 3)          # a, a', b, b'
    return R.reshape(d * d, d * d)


def ccnr(rho, d):
    """||R(rho)||_1 = sum of singular values. Separable => <= 1."""
    return float(np.sum(np.linalg.svd(realign(rho, d), compute_uv=False)))


# ---------------- known 3x3 PPT bound-entangled state: Tiles UPB ----------------
def _ket(i, d=3):
    v = np.zeros(d)
    v[i] = 1.0
    return v


def tiles_bound_entangled():
    """Bennett et al. Tiles unextendible-product-basis (UPB) bound-entangled state.

    rho = (I - P)/4 where P projects onto the 5 orthonormal Tiles UPB vectors in
    3x3. rho is PPT (negativity 0) and entangled -- the canonical CCNR target.
    """
    k = _ket
    psis = [
        np.kron(k(0), (k(0) - k(1)) / np.sqrt(2)),
        np.kron(k(2), (k(1) - k(2)) / np.sqrt(2)),
        np.kron((k(0) - k(1)) / np.sqrt(2), k(2)),
        np.kron((k(1) - k(2)) / np.sqrt(2), k(0)),
        np.kron((k(0) + k(1) + k(2)) / np.sqrt(3), (k(0) + k(1) + k(2)) / np.sqrt(3)),
    ]
    P = sum(np.outer(p, p) for p in psis)
    return (np.eye(9) - P) / 4.0


def summarize():
    d = 3
    prod = np.kron(np.diag([0.5, 0.3, 0.2]), np.diag([0.6, 0.1, 0.3]))
    iso_sep = isotropic(1.0 / d, d)
    iso_ent = isotropic(0.9, d)
    tiles = tiles_bound_entangled()
    return {
        "separable_product": {"negativity": negativity(prod, d), "ccnr": ccnr(prod, d)},
        "isotropic_sep_point_F=1/d": {"negativity": negativity(iso_sep, d), "ccnr": ccnr(iso_sep, d)},
        "isotropic_entangled_F=0.9": {"negativity": negativity(iso_ent, d), "ccnr": ccnr(iso_ent, d)},
        "tiles_bound_entangled": {"negativity": negativity(tiles, d), "ccnr": ccnr(tiles, d)},
    }


def main():
    d = 3
    print("#" * 100)
    print("# FINALITY -- CCNR / realignment bound-entanglement witness (outer-wall upgrade, T514)")
    print("#" * 100)

    s = summarize()

    print("\n[0] calibration gates")
    check("separable product state has CCNR <= 1", s["separable_product"]["ccnr"] <= 1 + 1e-9,
          f"CCNR={s['separable_product']['ccnr']:.4f}")
    check("isotropic separability point F=1/d sits exactly on the CCNR boundary (CCNR=1)",
          abs(s["isotropic_sep_point_F=1/d"]["ccnr"] - 1.0) < 1e-6,
          f"CCNR={s['isotropic_sep_point_F=1/d']['ccnr']:.6f}")
    check("NPT-entangled isotropic F=0.9 is flagged by CCNR (>1), agreeing with negativity",
          s["isotropic_entangled_F=0.9"]["ccnr"] > 1 and s["isotropic_entangled_F=0.9"]["negativity"] > 1e-9,
          f"CCNR={s['isotropic_entangled_F=0.9']['ccnr']:.4f}, neg={s['isotropic_entangled_F=0.9']['negativity']:.4f}")
    if FAIL:
        print("\n  CCNR witness failed calibration; NOT proceeding.")
        print(f"FAILED CHECKS: {FAIL}")
        raise SystemExit(1)

    print("\n[1] the payoff: a PPT bound-entangled state negativity CANNOT see")
    tn = s["tiles_bound_entangled"]["negativity"]
    tc = s["tiles_bound_entangled"]["ccnr"]
    print(f"      Tiles UPB state: negativity = {tn:.2e}   CCNR = {tc:.4f}")
    check("Tiles state is PPT (negativity ~ 0) -- invisible to the old outer wall", abs(tn) < 1e-9,
          f"neg={tn:.2e}")
    check("Tiles state is caught by CCNR (>1) -- the upgraded outer wall sees it", tc > 1 + 1e-6,
          f"CCNR={tc:.4f}")

    print("\n[2] effect on the isotropic-line ladder (the ladder result itself)")
    print("      On the isotropic family PPT <=> separable, so CCNR and negativity give the SAME")
    print("      outer wall at F = 1/d. The qudit ladder result is UNCHANGED on the isotropic line.")
    check("CCNR and negativity agree on the isotropic entanglement wall (both cross at F=1/d)",
          abs(s["isotropic_sep_point_F=1/d"]["ccnr"] - 1.0) < 1e-6
          and abs(negativity(isotropic(1.0 / d - 0.03, d), d)) < 1e-9)

    print("\n[verdict]")
    print("  * CCNR passes all calibration gates and DETECTS the Tiles PPT bound-entangled state")
    print("    (negativity=0, CCNR=1.09) -- a genuine entanglement witness independent of PPT.")
    print("  * Honest-limit #2 of the qudit ladder is closed: the outer wall is now 'entangled'")
    print("    (NPT OR CCNR), not merely 'NPT-entangled'. Bound entanglement off the isotropic line")
    print("    is now detectable; the isotropic-line ladder is unchanged (PPT=sep there).")
    print("  * Scope: CCNR is sufficient, not necessary; PPT-entangled states it misses may remain.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = CCNR witness verified; outer wall upgraded to a real entanglement detector.")


if __name__ == "__main__":
    main()
