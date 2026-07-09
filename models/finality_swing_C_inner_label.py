"""FINALITY swing C -- inner-label discriminator: MONOGAMY/SHAREABILITY, not CHSH.

Cluster C (inner-label discriminator) from the nested-band finding
(explorations/nested-band-twenty-persona-profound-possibilities-2026-07-08.md +
starter-swing-orchestration-plan-2026-07-08.md). The between-band is a LABELLED sub-region
of a broader TaF-native object: facts present to a group but NOT recoverable by a member's
ADMISSIBLE local operations. Entanglement is the inner label; encryption is another way in;
the outer wall = not recoverable by admissible local ops (one algebra, both band edges).

BET (cluster C): a discriminator SHARPER than CHSH separates the inner (entangled) band from
the outer (encrypted) band, and it must COME APART from CHSH on some physical fixture (else it
is a mere relabel of CHSH>2). The proposed discriminator is MONOGAMY / SHAREABILITY: the
maximum number of parties that can hold the same correlation with A (symmetric-extension order).
  * in-the-clear  (definite local value)     : shareable to infinity, locally readable   (BELOW band)
  * encrypted     (one-time-pad shared key)   : shareable to infinity, NOT locally readable (OUTER band)
  * entangled     (Werner, monogamous)        : NOT 2-shareable                            (INNER band)

CORRECTION TO THE FINDING (this model's main empirical result). The probe (and the exploration
note) asserted the shareability wall sits at p = 1/2, giving the ladder "1/3 < 1/2 < 0.707".
That is WRONG: 1/2 is the Werner projective LOCAL-HIDDEN-VARIABLE threshold (Werner 1989), a
different label. The actual 2-shareability (2-extendibility) wall is DERIVED here by an explicit
symmetric-extension SDP to be p = 2/3, and a valid explicit 2-extension is CONSTRUCTED and
validated at p = 0.60 (> 1/2), directly refuting the 1/2 claim. The corrected ladder is
  p_ent   = 1/3      : negativity turns positive           (entanglement onset, PPT)
  p_share = 2/3      : loses 2-shareability                (MONOGAMY WALL -- the inner label)
  p_chsh  = 1/sqrt2  : CHSH crosses 2                      (Bell violation onset)
all computed here from real density matrices, and STILL distinct and ordered: 1/3 < 2/3 < 0.707.

The core cluster-C bet SURVIVES the correction: because 2/3 < 1/sqrt2, monogamy still COMES APART
from CHSH on the Werner band 2/3 < p <= 1/sqrt2 -- there the state is un-shareable (monogamous ->
INNER by shareability) yet CHSH <= 2 (so CHSH would misfile it as OUTER). Shareability separates
inner from outer exactly where CHSH cannot; it is a genuinely sharper label, not a relabel.

The SDP: by the U(x)U(x)U twirl, any symmetric extension of the U(x)U(x)U-invariant Werner state can
be taken inside the 6-dim S_3 group algebra on 3 qubits (WLOG). Feasibility = max-min-eigenvalue,
over the affine subspace {PSD, swap(B,B')-symmetric, Tr_B' = Werner(p)}, is >= 0. Solved by
nullspace + min-eigenvalue maximization (scipy) and validated by reconstructing the extension.

PASS iff: (i) the three thresholds are distinct/ordered 1/3 < 2/3 < 1/sqrt2; (ii) the derived
2-shareability wall == 2/3 AND the 1/2 claim is refuted by an explicit valid extension at p>1/2;
(iii) the shareability order parameter is MONOTONE non-increasing in-clear -> encrypted -> entangled;
(iv) shareability SEPARATES inner from outer on the 2/3<p<=1/sqrt2 fixture where CHSH>2 does NOT.
Any FAIL -> SystemExit(1).

Run: python -m models.finality_swing_C_inner_label     (exit 0 on success)
"""
from __future__ import annotations

import math
import numpy as np
from scipy.linalg import null_space
from scipy.optimize import minimize

# Reuse the repo's CHSH primitive (correlator form) as an independent cross-check anchor.
from models.finality_two_invariant_band_separation import chsh as chsh_correlator, E_quantum

FAIL: list[str] = []
INF = float("inf")


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# Density-matrix primitives (two qubits)
# ---------------------------------------------------------------------------
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]


def kron(mats):
    out = np.array([[1]], dtype=complex)
    for m in mats:
        out = np.kron(out, m)
    return out


SINGLET = np.array([0, 1, -1, 0], dtype=complex) / math.sqrt(2)
RHO_SINGLET = np.outer(SINGLET, SINGLET.conj())


def werner(p):
    return p * RHO_SINGLET + (1 - p) * np.eye(4, dtype=complex) / 4


def partial_transpose_B(rho):
    r = rho.reshape(2, 2, 2, 2)  # a, b, a', b'
    return np.transpose(r, (0, 3, 2, 1)).reshape(4, 4)


def negativity(rho):
    ev = np.linalg.eigvalsh(partial_transpose_B(rho))
    return float(sum(-e for e in ev if e < 0))


def correlation_matrix(rho):
    T = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            T[i, j] = np.real(np.trace(rho @ kron([PAULI[i], PAULI[j]])))
    return T


def chsh_max(rho):
    """Horodecki criterion: max CHSH = 2*sqrt(t1^2 + t2^2), t = two largest singular values of T."""
    s = sorted(np.linalg.svd(correlation_matrix(rho), compute_uv=False), reverse=True)
    return 2 * math.sqrt(s[0] ** 2 + s[1] ** 2)


# ---------------------------------------------------------------------------
# Explicit symmetric-extension SDP for the Werner state.
# 3 qubits: A(0), B(1), B'(2). Work inside the S_3 permutation (group) algebra -- WLOG by the
# U(x)U(x)U twirl (Werner is U(x)U-invariant, so twirling any extension by U(x)U(x)U yields an
# invariant extension with the same marginal). Impose {Tr=1, swap(B,B') symmetric, Tr_B'=Werner(p)},
# then MAXIMIZE the min eigenvalue over the residual affine subspace. 2-shareable iff max-min >= -tol.
# ---------------------------------------------------------------------------
def perm_op(perm):
    """8x8 P with P|b0 b1 b2> = |b_{perm[0]} b_{perm[1]} b_{perm[2]}> (relabel qubit positions)."""
    P = np.zeros((8, 8), dtype=complex)
    for idx in range(8):
        bits = [(idx >> (2 - k)) & 1 for k in range(3)]
        nb = [bits[perm[k]] for k in range(3)]
        P[(nb[0] << 2) | (nb[1] << 1) | nb[2], idx] = 1.0
    return P


_PERMS = {"e": (0, 1, 2), "01": (1, 0, 2), "02": (2, 1, 0),
          "12": (0, 2, 1), "cyc": (1, 2, 0), "cy2": (2, 0, 1)}
_P = {k: perm_op(v) for k, v in _PERMS.items()}
# Hermitian spanning basis of the real 6-dim invariant algebra.
_HB = [_P["e"], _P["01"], _P["02"], _P["12"],
       _P["cyc"] + _P["cy2"], 1j * (_P["cyc"] - _P["cy2"])]
SWAP_BBp = _P["12"]


def partial_trace_Bp(rho8):
    """Trace out qubit 2 (B'); return 4x4 on A,B."""
    return np.einsum("abcABc->abAB", rho8.reshape(2, 2, 2, 2, 2, 2)).reshape(4, 4)


def partial_trace_B(rho8):
    """Trace out qubit 1 (B); return 4x4 on A,B'."""
    return np.einsum("abcAbC->acAC", rho8.reshape(2, 2, 2, 2, 2, 2)).reshape(4, 4)


def _solve_extension(p):
    """Return (best_min_eig, best_state). Linear constraints via nullspace; PSD via min-eig max."""
    target = werner(p)
    marg = [partial_trace_Bp(H) for H in _HB]
    sym = [SWAP_BBp @ H @ SWAP_BBp - H for H in _HB]
    A_rows, b_rows = [], []
    for r in range(4):
        for c in range(4):
            A_rows.append([marg[i][r, c].real for i in range(6)]); b_rows.append(target[r, c].real)
            A_rows.append([marg[i][r, c].imag for i in range(6)]); b_rows.append(target[r, c].imag)
    for r in range(8):
        for c in range(8):
            A_rows.append([sym[i][r, c].real for i in range(6)]); b_rows.append(0.0)
            A_rows.append([sym[i][r, c].imag for i in range(6)]); b_rows.append(0.0)
    A, b = np.array(A_rows), np.array(b_rows)
    x0, *_ = np.linalg.lstsq(A, b, rcond=None)
    if np.linalg.norm(A @ x0 - b) > 1e-6:
        return -1.0, None  # linear (incl. exact marginal) infeasible
    NS = null_space(A)

    def rho_of(x):
        return sum(x[i] * _HB[i] for i in range(6))

    def min_eig(z):
        return float(np.linalg.eigvalsh(rho_of(x0 + (NS @ z if NS.shape[1] else 0.0)))[0])

    if NS.shape[1] == 0:
        return min_eig(np.zeros(0)), rho_of(x0)
    best, zb = -1e9, None
    for s in range(8):
        z0 = np.random.default_rng(s).standard_normal(NS.shape[1]) * 0.1
        res = minimize(lambda z: -min_eig(z), z0, method="Nelder-Mead",
                       options={"xatol": 1e-9, "fatol": 1e-11, "maxiter": 6000})
        if -res.fun > best:
            best, zb = -res.fun, res.x
    return best, rho_of(x0 + (NS @ zb if NS.shape[1] else 0.0))


def two_shareable(p, tol=1e-6):
    return _solve_extension(p)[0] >= -tol


def shareability_threshold():
    lo, hi = 0.30, 0.90
    assert two_shareable(lo) and not two_shareable(hi)
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if two_shareable(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Shareability ORDER PARAMETER fixtures. k_max = max B-parties that share A's correlation.
# ---------------------------------------------------------------------------
def in_the_clear():
    rho = kron([np.array([[1, 0], [0, 0]], dtype=complex)] * 2)  # |00><00|: classical, copyable
    return dict(name="in-clear ", rho=rho, k_max=INF, locally_readable=True)


def encrypted_otp():
    rho = 0.5 * (kron([np.array([[1, 0], [0, 0]])] * 2) + kron([np.array([[0, 0], [0, 1]])] * 2))
    return dict(name="encrypted", rho=rho.astype(complex), k_max=INF, locally_readable=False)


def entangled_band(p):
    return dict(name="entangled", rho=werner(p),
                k_max=INF if two_shareable(p) else 1, locally_readable=False)


def main():
    print("#" * 100)
    print("# FINALITY swing C -- monogamy/shareability as the inner-band label (sharper than CHSH)")
    print("#" * 100)

    p_come_apart = 0.69  # in the corrected come-apart band 2/3 < p <= 1/sqrt2 (~0.667..0.707)

    # ---- (1) three thresholds from real density matrices ----
    print("\n[1] Werner thresholds computed from density matrices (not assumed)")
    grid = np.linspace(0.0, 1.0, 4001)
    p_ent = next(p for p in grid if negativity(werner(p)) > 1e-9)
    p_chsh = next(p for p in grid if chsh_max(werner(p)) > 2 + 1e-9)
    print(f"      negativity onset  p_ent  ~= {p_ent:.4f}   (expect 1/3     = {1/3:.4f})")
    print(f"      CHSH>2 onset      p_chsh ~= {p_chsh:.4f}   (expect 1/sqrt2 = {1/math.sqrt(2):.4f})")
    check("negativity onset ~ 1/3", abs(p_ent - 1/3) < 0.01)
    check("CHSH>2 onset ~ 1/sqrt2", abs(p_chsh - 1/math.sqrt(2)) < 0.01)
    check("CHSH primitive anchors to 2*sqrt2 on the Bell state (repo cross-check)",
          abs(chsh_max(RHO_SINGLET) - chsh_correlator(E_quantum)) < 1e-6,
          f"dm={chsh_max(RHO_SINGLET):.4f} correlator={chsh_correlator(E_quantum):.4f}")

    # ---- (2) derive 2-shareability wall by explicit symmetric-extension SDP; refute the 1/2 claim ----
    print("\n[2] 2-shareability wall from an explicit symmetric-extension SDP (derived, not assumed)")
    p_share = shareability_threshold()
    print(f"      derived 2-shareability threshold p_share ~= {p_share:.4f}   (== 2/3 = {2/3:.4f})")
    check("SDP-derived 2-shareability wall == 2/3", abs(p_share - 2/3) < 0.01)

    print("      CORRECTION: exploration/probe claimed the wall is 1/2. Refute by explicit extension >1/2.")
    me06, rho06 = _solve_extension(0.60)  # p=0.60 > 1/2
    valid06 = (rho06 is not None and me06 > -1e-6
               and np.linalg.norm(partial_trace_Bp(rho06) - werner(0.60)) < 1e-9
               and np.linalg.norm(partial_trace_B(rho06) - werner(0.60)) < 1e-9
               and np.linalg.norm(SWAP_BBp @ rho06 @ SWAP_BBp - rho06) < 1e-9)
    print(f"      explicit 2-extension at p=0.60:  min-eig={me06:+.5f}  both marginals=Werner  symmetric")
    check("p=0.60 (>1/2) HAS a valid explicit symmetric 2-extension => refutes the 1/2 wall claim", valid06)
    check("=> 1/2 is NOT the shareability wall (it is the Werner projective LHV threshold)",
          two_shareable(0.60) and two_shareable(0.55))
    check("Werner(0.70) (>2/3) is NOT 2-shareable (monogamous)", not two_shareable(0.70))

    # ---- thresholds distinct + ordered ----
    print("\n[thresholds] distinct and ordered: p_ent < p_share < p_chsh")
    check("1/3 < 2/3 < 1/sqrt2 realized numerically (corrected ladder)",
          p_ent + 1e-3 < p_share < p_chsh - 1e-3,
          f"{p_ent:.3f} < {p_share:.3f} < {p_chsh:.3f}")

    # ---- (3) shareability order parameter monotone across the three regimes ----
    print("\n[3] shareability order parameter k_max across in-clear -> encrypted -> entangled")
    fx = [in_the_clear(), encrypted_otp(), entangled_band(p_come_apart)]
    for f in fx:
        km = "inf" if f["k_max"] == INF else str(f["k_max"])
        print(f"      {f['name']:10s}  k_max={km:>3s}  CHSH={chsh_max(f['rho']):.3f}  "
              f"locally_readable={f['locally_readable']}")
    seq = [f["k_max"] for f in fx]
    check("k_max is MONOTONE non-increasing in-clear >= encrypted >= entangled",
          all(seq[i] >= seq[i + 1] for i in range(len(seq) - 1)), f"[inf, inf, {seq[-1]}]")

    # ---- (4) shareability separates inner from outer where CHSH cannot ----
    print(f"\n[4] come-apart fixture: Werner p={p_come_apart}  (2/3 < p <= 1/sqrt2)")
    ent, enc = entangled_band(p_come_apart), encrypted_otp()
    chsh_ent = chsh_max(ent["rho"])
    print(f"      entangled p={p_come_apart}:  k_max={ent['k_max']}  CHSH={chsh_ent:.3f}")
    print(f"      encrypted        :  k_max=inf  CHSH={chsh_max(enc['rho']):.3f}")
    chsh_cannot = chsh_ent <= 2 + 1e-9
    share_separates = ent["k_max"] != enc["k_max"]
    check("CHSH does NOT fire on the entangled band state (CHSH<=2)", chsh_cannot, f"CHSH={chsh_ent:.3f}")
    check("shareability SEPARATES inner (finite k_max) from outer (k_max=inf)", share_separates)
    check("=> shareability separates inner/outer EXACTLY where CHSH>2 cannot (comes apart, not a relabel)",
          chsh_cannot and share_separates)

    # ---- verdict ----
    print("\n[verdict]")
    print("  * Monogamy/shareability IS a sharper inner-band label than CHSH -- cluster-C bet CONFIRMED.")
    print("  * BUT the exploration's specific number is REFUTED: the 2-shareability wall is 2/3, not 1/2")
    print("    (1/2 is the Werner projective LHV threshold). Shown by an explicit, validated 2-extension")
    print("    at p=0.60 > 1/2. Corrected threshold ladder: 1/3 (ent) < 2/3 (share) < 0.707 (CHSH).")
    print("  * Because 2/3 < 1/sqrt2, monogamy still comes apart from CHSH on the band 2/3 < p <= 1/sqrt2:")
    print("    un-shareable (INNER) yet CHSH<=2. The come-apart window is narrower than the note implied.")
    print("  * As a single order parameter, k_max = inf for in-the-clear and encrypted (OUTER, copyable)")
    print("    and finite for the entangled INNER band -- monotone across the three regimes.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = swing C inner-label confirmed (monogamy sharper than CHSH; wall corrected to 2/3).")


if __name__ == "__main__":
    main()
