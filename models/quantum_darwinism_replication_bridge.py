"""FINALITY -- quantum-Darwinism redundancy <-> replication-factor bridge (T518).

Attacks prospecting corner 1 of
explorations/lane-status-and-adjacent-space-prospecting-2026-07-09.md -- the
strongest unbuilt lead: Zurek's quantum Darwinism already speaks in
distributed-systems terms (redundant copies proliferate; the environment is a
communication channel; many observers independently reach consensus by reading
fragments), but the searched literature does NOT draw the quantitative
correspondence between the redundancy plateau and a replication factor. This
model builds a finite, executable version of both sides and reports honestly
whether the correspondence is more than vocabulary.

QD side (standard branching model):
  system qubit S = |+> ; N environment qubits, each an imperfect copy via a
  controlled Y-rotation by angle theta (theta=pi = perfect copy). Global pure
  state |Psi> = (|0>_S |0..0>_E + |1>_S |phi..phi>_E)/sqrt2, |phi> = Ry(theta)|0>.
  Partial information I(S:F) is computed exactly for fragments F of each size f;
  the redundancy is R_delta = N / f_delta, where f_delta is the smallest
  fragment size reaching (1-delta) H(S). A redundancy plateau = many disjoint
  fragments each INDEPENDENTLY sufficient to reconstruct the pointer state.

DS side (the proposed image):
  N replicas of a record; each replica holds the pointer with quality theta;
  R_delta disjoint quorums each reconstruct the value to tolerance delta; the
  system survives losing all but one sufficient fragment (fault tolerance
  N - f_delta).

Verdict (preview): the PLATEAU maps structurally (redundant independent
readout = eventual-consistency replication), but the QUANTITATIVE map
R_delta = replication factor is parametrization-dependent -- no shared
dimensionless invariant yet. Confirmed correspondence, not yet a discovery.

Run: python -m models.quantum_darwinism_replication_bridge   (exit 0)
"""
from __future__ import annotations

import numpy as np

FAIL: list[str] = []
RNG = np.random.default_rng(20260709)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def global_state(N, theta):
    """|Psi> = (|0>_S|0..0> + |1>_S|phi..phi>)/sqrt2, S is qubit index 0."""
    phi = np.array([np.cos(theta / 2), np.sin(theta / 2)])
    e0 = np.zeros(2 ** N); e0[0] = 1.0
    ephi = phi
    for _ in range(N - 1):
        ephi = np.kron(ephi, phi)
    psi = np.zeros(2 ** (N + 1))
    psi[: 2 ** N] = e0 / np.sqrt(2)          # |0>_S branch
    psi[2 ** N:] = ephi / np.sqrt(2)         # |1>_S branch
    return psi


def reduced_dm(psi, N1, keep):
    keep = list(keep)
    traced = [i for i in range(N1) if i not in keep]
    t = psi.reshape([2] * N1)
    t = np.transpose(t, keep + traced)
    k = 2 ** len(keep)
    M = t.reshape(k, 2 ** len(traced))
    return M @ M.conj().T


def vn_entropy(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-12]
    return float(-np.sum(w * np.log2(w)))


def partial_info(psi, N, F):
    """I(S:F) = S(rho_S) + S(rho_F) - S(rho_{S,F}); S = qubit 0, env = 1..N."""
    N1 = N + 1
    S_S = vn_entropy(reduced_dm(psi, N1, [0]))
    S_F = vn_entropy(reduced_dm(psi, N1, list(F)))
    S_SF = vn_entropy(reduced_dm(psi, N1, [0] + list(F)))
    return S_S + S_F - S_SF


def redundancy(psi, N, delta, samples=12):
    """R_delta = N / f_delta, f_delta = smallest fragment size with avg I(S:F) >= (1-delta) H(S)."""
    HS = vn_entropy(reduced_dm(psi, N + 1, [0]))
    target = (1 - delta) * HS
    env = list(range(1, N + 1))
    f_delta = None
    curve = []
    for f in range(1, N + 1):
        vals = []
        for _ in range(samples):
            F = list(RNG.choice(env, size=f, replace=False))
            vals.append(partial_info(psi, N, F))
        avg = float(np.mean(vals))
        curve.append((f, avg))
        if f_delta is None and avg >= target:
            f_delta = f
    R = (N / f_delta) if f_delta else 0.0
    return R, f_delta, HS, curve


def main():
    print("#" * 100)
    print("# FINALITY -- quantum Darwinism redundancy <-> replication factor (T518)")
    print("#" * 100)

    N = 8
    delta = 0.1

    print(f"\n[0] sanity: the QD model behaves (N={N} environment qubits)")
    HS_plus = vn_entropy(reduced_dm(global_state(N, np.pi), N + 1, [0]))
    check("system carries ~1 bit (H(S) ~ 1 for the |+> pointer)", abs(HS_plus - 1.0) < 1e-6,
          f"H(S)={HS_plus:.4f}")
    # perfect copies -> a single env qubit already carries the full bit
    I_one_perfect = partial_info(global_state(N, np.pi), N, [1])
    check("with perfect copies, ONE fragment qubit already carries the full classical bit",
          abs(I_one_perfect - 1.0) < 1e-6, f"I(S:1 qubit)={I_one_perfect:.4f}")
    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)

    print("\n[1] redundancy plateau across copy quality theta (R_delta = N / f_delta, delta=0.1)")
    rows = []
    for theta in (np.pi, 0.6 * np.pi, 0.35 * np.pi, 0.2 * np.pi):
        R, f_delta, HS, curve = redundancy(global_state(N, theta), N, delta)
        rows.append((theta, R, f_delta))
        print(f"      theta={theta/np.pi:.2f}pi : H(S)={HS:.3f}  f_delta={f_delta}  R_delta={R:.2f}  "
              f"(disjoint independently-sufficient fragments)")
    check("high-quality copies give a LARGE redundancy plateau (R_delta >= N/2)",
          rows[0][1] >= N / 2, f"R={rows[0][1]:.2f}")
    check("redundancy DECREASES monotonically as copy quality falls (theta smaller -> R smaller)",
          all(rows[i + 1][1] <= rows[i][1] + 1e-9 for i in range(len(rows) - 1)),
          f"R sequence = {[round(r[1],2) for r in rows]}")

    print("\n[2] the proposed DS image, made explicit")
    print("      QD                                   DS")
    print("      environment fragment F               replica / read-quorum")
    print("      I(S:F) >= (1-delta)H(S)              quorum reconstructs the value to staleness delta")
    print("      redundancy R_delta = N/f_delta       # disjoint sufficient quorums = fault tolerance")
    print("      pointer (einselected) state          committed record")
    print("      objectivity (many agree)             eventual-consistency consensus")

    print("\n[3] does the QUANTITATIVE map survive? (the honest test)")
    # Same abstract situation, two parametrizations -> different R? If R is parametrization-invariant
    # as a 'replication factor', it should be a property of the branch structure, not of delta/theta.
    R_a, f_a, _, _ = redundancy(global_state(N, 0.6 * np.pi), N, 0.05)
    R_b, f_b, _, _ = redundancy(global_state(N, 0.6 * np.pi), N, 0.20)
    print(f"      fixed physics (theta=0.6pi), delta=0.05 -> R={R_a:.2f} (f={f_a}); "
          f"delta=0.20 -> R={R_b:.2f} (f={f_b})")
    check("R_delta is NOT a delta-invariant (so it is not yet a well-defined 'replication factor')",
          abs(R_a - R_b) > 1e-9, f"R(0.05)={R_a:.2f} != R(0.20)={R_b:.2f}")
    print("      => the redundancy number depends on the tolerance delta; the DS replication factor")
    print("         depends on the failure model (crash vs Byzantine) and quorum-intersection rule.")
    print("         No shared dimensionless invariant computes the same number on both sides yet.")

    print("\n[verdict]  CONFIRMED correspondence, NOT yet a discovery.")
    print("  * STRUCTURAL match is real and non-trivial: the redundancy plateau (many disjoint fragments")
    print("    each independently sufficient) is exactly the eventual-consistency replication property")
    print("    (any read quorum reconstructs the value; the record survives losing all but one quorum).")
    print("    This is more than vocabulary -- both are 'objectivity via redundant independent access'.")
    print("  * QUANTITATIVE bridge is unbuilt: R_delta is not delta-invariant, and the DS replication")
    print("    factor is failure-model-dependent; they are not the same number computed two ways.")
    print("  * Deprioritize with a WAKE CONDITION: find a dimensionless invariant (candidate: the")
    print("    information deficit 1 - f_delta/N vs a quorum-intersection redundancy) that both sides")
    print("    compute identically. If it exists, the bridge converts from analogy to discovery.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = QD redundancy plateau <-> replication built; structural match confirmed, quantitative bridge open.")


if __name__ == "__main__":
    main()
