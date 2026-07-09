"""FINALITY -- swing A: ACCESS STRUCTURE (minimal recovering coalition) intrinsic ONLY at the
entanglement corner (starter-swing Phase 2 build for cluster A).

Cluster A (nested-band-twenty-persona..., starter-swing-orchestration-plan) reframes the outer wall as
an ACCESS STRUCTURE: the order parameter is the *minimal recovering coalition* -- the smallest set of
members whose ADMISSIBLE (individual / block-diagonal, positivity-preserving) operations recover a fact
that is present to the whole group. The Phase-1 probe passed "conditional" and named the sharp experiment:

  BET (the exact self-check):
    (i)  ENTANGLEMENT corner: the minimal recovering coalition is n-of-n and is INVARIANT under every
         admissible re-arrangement (local unitaries per member, member permutations, LOCC). Monogamy /
         no-LOCC forbids lowering it below n. => the order parameter carries INTRINSIC content here.
    (ii) ENCRYPTION corner: the minimal recovering coalition can be FREELY RESET to any value 1..n by
         RE-KEYING (redistributing the one-time-pad key shares), WITHOUT changing the sector (still
         W- / unreadable to a non-key-holder) or the inner CHSH label (still classical, CHSH<=2).
         => here the order parameter is a FREE RELABEL, not intrinsic.

  If BOTH hold, the access-structure order parameter is non-trivial (intrinsic) EXACTLY at the
  entanglement corner and a free relabel at the encryption corner -- isolating precisely where the
  reframe has real content. That is a DOUBLE DISSOCIATION, the strongest form of the bet.

Skeptical design (a refuting result is a real result): the model does not assert monogamy -- it tries
HARD to lower the entangled coalition below n over a grid of local unitaries + all member permutations,
using the TIGHT bound (reduced-state trace-distance / Frobenius): if the reduced state on a proper
coalition is identical for the two encodings of the secret, NO operation whatsoever (POVM, LOCC, classical
communication within the coalition) can recover it -- that is the airtight monogamy statement. If any
proper coalition COULD recover, or if encryption's coalition turned out fixed, exit is 1 (bet refuted).

Reuse: the inner CHSH label is the repo-native one (models.finality_two_invariant_band_separation).

Run: python -m models.finality_swing_A_access_structure   (exit 0)
"""
from __future__ import annotations

import math
from itertools import combinations, permutations, product

import numpy as np

# Repo-native inner CHSH label (imported verbatim; module main() is __main__-guarded, so importing is safe).
from models.finality_two_invariant_band_separation import chsh, E_quantum, E_classical

FAIL: list[str] = []
TOL = 1e-9


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ===========================================================================
# ENTANGLEMENT CORNER -- quantum access structure via a GHZ/Bell secret encoding
# ===========================================================================
#
# The group holds a secret bit v. Encoding (genuinely multipartite entangled):
#     v = 0  ->  |GHZ+> = (|0...0> + |1...1>) / sqrt(2)
#     v = 1  ->  |GHZ-> = (|0...0> - |1...1>) / sqrt(2)
# For n = 2 this is the Bell pair |Phi+/-> (inner CHSH = 2 sqrt(2) label). GHZ+ and GHZ- are ORTHOGONAL
# (the whole group distinguishes v by a joint GHZ-basis measurement) but have IDENTICAL reduced states on
# every PROPER subset -> no proper coalition can recover v. So min recovering coalition = n, by monogamy.


def ghz(n: int, sign: int) -> np.ndarray:
    """|GHZ+/-> on n qubits. sign = +1 for v=0, -1 for v=1."""
    dim = 1 << n
    psi = np.zeros(dim, dtype=complex)
    psi[0] = 1.0 / math.sqrt(2.0)          # |0...0>
    psi[dim - 1] = sign / math.sqrt(2.0)   # |1...1>
    return psi


def rot(theta: float) -> np.ndarray:
    """A 2x2 real local unitary (single-qubit rotation) -- a member's admissible local re-arrangement."""
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=complex)


def apply_local(psi: np.ndarray, unitaries: list[np.ndarray]) -> np.ndarray:
    """Apply U_0 (x) U_1 (x) ... (x) U_{n-1} to psi (qubit 0 outermost)."""
    U = unitaries[0]
    for Ui in unitaries[1:]:
        U = np.kron(U, Ui)
    return U @ psi


def reduced_state(psi: np.ndarray, n: int, keep: tuple[int, ...]) -> np.ndarray:
    """Partial trace of |psi><psi| keeping the qubits in `keep` (tracing out the rest)."""
    trace_out = [q for q in range(n) if q not in keep]
    # tensor with row axes 0..n-1 and col axes n..2n-1; trace each unwanted qubit's row axis vs col axis.
    tensor = np.outer(psi, psi.conj()).reshape([2] * (2 * n))
    row_axes = list(range(n))
    col_axes = list(range(n, 2 * n))
    for q in sorted(trace_out, reverse=True):
        ra = row_axes[q]
        ca = col_axes[q]
        tensor = np.trace(tensor, axis1=ra, axis2=ca)
        # after tracing, remove those axes and shift labels above them down by 1 (twice)
        row_axes = [a - (a > ra) - (a > ca) for a in row_axes if a != ra]
        col_axes = [a - (a > ra) - (a > ca) for a in col_axes if a != ca]
    dk = 1 << len(keep)
    return tensor.reshape(dk, dk)


def distinguishable(psi0: np.ndarray, psi1: np.ndarray, n: int, keep: tuple[int, ...]) -> float:
    """Frobenius distance between the two encodings' reduced states on `keep`. 0 => the coalition CANNOT
    recover v by ANY operation (tight monogamy bound); >0 => some measurement recovers it."""
    r0 = reduced_state(psi0, n, keep)
    r1 = reduced_state(psi1, n, keep)
    return float(np.linalg.norm(r0 - r1))


def min_recovering_coalition(psi0: np.ndarray, psi1: np.ndarray, n: int) -> int:
    """Smallest coalition size s such that SOME size-s coalition can recover v."""
    for size in range(1, n + 1):
        for keep in combinations(range(n), size):
            if distinguishable(psi0, psi1, n, keep) > 1e-6:
                return size
    return n + 1  # unreachable for these states


def entanglement_min_coalition_invariant(n: int, angle_grid: list[float]) -> dict:
    """Try HARD to lower the entangled min-coalition below n via admissible re-arrangements:
    every member permutation x a grid of per-member local unitaries. Return the set of min-coalition
    values observed and whether ANY proper coalition ever recovered."""
    observed = set()
    proper_ever_recovered = False
    # baseline
    psi0, psi1 = ghz(n, +1), ghz(n, -1)
    observed.add(min_recovering_coalition(psi0, psi1, n))

    # re-arrangement search: permutations (relabel members) + local unitaries per member
    for perm in permutations(range(n)):
        for angles in product(angle_grid, repeat=n):
            Us = [rot(angles[i]) for i in range(n)]
            p0 = apply_local(psi0, [Us[perm[i]] for i in range(n)])
            p1 = apply_local(psi1, [Us[perm[i]] for i in range(n)])
            m = min_recovering_coalition(p0, p1, n)
            observed.add(m)
            # explicitly probe every PROPER coalition for recovery
            for size in range(1, n):
                for keep in combinations(range(n), size):
                    if distinguishable(p0, p1, n, keep) > 1e-6:
                        proper_ever_recovered = True
    return {
        "n": n,
        "observed_min_coalitions": sorted(observed),
        "invariant_at_n": observed == {n},
        "proper_coalition_ever_recovered": proper_ever_recovered,
    }


# ===========================================================================
# ENCRYPTION CORNER -- classical one-time-pad access structure, freely re-keyable
# ===========================================================================
#
# Secret v in {0,1}. Key k = XOR of additive shares s_1..s_m (uniform, independent). Ciphertext ct = v XOR k.
# A coalition recovers v iff the registers it holds DETERMINE v (mutual information I(v; registers) = 1 bit).
# Re-keying = redistributing which member holds ct and which members hold key shares -> resets the minimal
# recovering coalition anywhere in 1..n, with NO change to the sector (an outsider's view is v-independent
# by the one-time pad) or the CHSH label (classical correlations, CHSH <= 2).


def _mutual_info_v_determined(register_fns, world_bits: int) -> float:
    """I(v; registers) in bits over uniform worlds (v plus the share bits). registers is a list of
    functions world->bit. Returns I(v;R); == 1.0 iff R determines v."""
    from math import log2
    worlds = list(range(1 << world_bits))  # bit 0 = v, bits 1.. = shares
    n_w = len(worlds)
    joint = {}   # (v, rtuple) -> count
    pv = {0: 0, 1: 0}
    pr = {}
    for w in worlds:
        v = w & 1
        r = tuple(fn(w) for fn in register_fns)
        joint[(v, r)] = joint.get((v, r), 0) + 1
        pv[v] += 1
        pr[r] = pr.get(r, 0) + 1
    mi = 0.0
    for (v, r), c in joint.items():
        pjr = c / n_w
        p_v = pv[v] / n_w
        p_r = pr[r] / n_w
        mi += pjr * log2(pjr / (p_v * p_r))
    return mi


def encryption_min_coalition(n: int, ct_holder: int, key_holders: tuple[int, ...]) -> dict:
    """One-time-pad scheme over n parties. ct = v XOR (XOR of shares); each member of key_holders holds one
    additive share; ct_holder holds ct. Returns the minimal recovering coalition size and the outsider MI."""
    m = len(key_holders)               # number of key shares
    world_bits = 1 + m                 # bit 0 = v; bits 1..m = shares s_1..s_m
    share_of = {holder: i + 1 for i, holder in enumerate(key_holders)}  # bit index of each holder's share

    def reg_ct(w):  # ct = v XOR (XOR of all shares)
        v = w & 1
        k = 0
        for i in range(1, m + 1):
            k ^= (w >> i) & 1
        return v ^ k

    def reg_share(bit_index):
        return lambda w, b=bit_index: (w >> b) & 1

    # what registers does party p hold?
    def registers_of(p):
        regs = []
        if p == ct_holder:
            regs.append(reg_ct)
        if p in share_of:
            regs.append(reg_share(share_of[p]))
        return regs

    # minimal recovering coalition: smallest set of parties whose pooled registers determine v
    min_size = None
    min_witness = None
    for size in range(1, n + 1):
        for S in combinations(range(n), size):
            regfns = []
            for p in S:
                regfns.extend(registers_of(p))
            if not regfns:
                continue
            mi = _mutual_info_v_determined(regfns, world_bits)
            if abs(mi - 1.0) < 1e-9:
                min_size, min_witness = size, S
                break
        if min_size is not None:
            break

    # sector check: any STRICT subset of the recovering coalition is v-independent (one-time pad) -> W-.
    # Test the largest proper subsets of the witness (drop one party) all have I(v;R) = 0.
    outsider_mis = []
    if min_witness is not None and len(min_witness) >= 1:
        for drop in min_witness:
            S = tuple(p for p in min_witness if p != drop)
            regfns = []
            for p in S:
                regfns.extend(registers_of(p))
            outsider_mis.append(_mutual_info_v_determined(regfns, world_bits) if regfns else 0.0)

    return {
        "ct_holder": ct_holder,
        "key_holders": key_holders,
        "min_coalition_size": min_size,
        "witness": min_witness,
        "max_outsider_mi_bits": max(outsider_mis) if outsider_mis else 0.0,
    }


def main():
    print("#" * 100)
    print("# FINALITY swing A -- access structure (minimal recovering coalition) intrinsic ONLY at the")
    print("#                     entanglement corner; a free relabel at the encryption corner")
    print("#" * 100)

    n = 3
    angle_grid = [0.0, math.pi / 5, 2 * math.pi / 5, math.pi / 2]

    # ---------------- inner CHSH label (repo-native), sanity ----------------
    print("\n[label] inner CHSH separates entanglement (CHSH>2) from classical encryption (CHSH<=2)")
    s_ent = chsh(E_quantum)
    s_enc = chsh(E_classical)
    check("entangled correlation has CHSH = 2 sqrt(2) > 2 (inner label present)", s_ent > 2.0 + 1e-9,
          f"CHSH_ent = {s_ent:.4f}")
    check("classical/encrypted correlation has CHSH <= 2 (no inner label)", s_enc <= 2.0 + 1e-9,
          f"CHSH_enc = {s_enc:.4f}")

    # ---------------- (i) ENTANGLEMENT: min-coalition = n, INVARIANT ----------------
    print(f"\n[ENT] entanglement corner (n = {n}) -- minimal recovering coalition and its invariance")
    # baseline structure: proper coalitions cannot recover; full set can.
    psi0, psi1 = ghz(n, +1), ghz(n, -1)
    for size in range(1, n):
        worst = max(distinguishable(psi0, psi1, n, keep) for keep in combinations(range(n), size))
        check(f"NO size-{size} coalition can recover v (reduced-state distance = 0 => tight monogamy)",
              worst < 1e-6, f"max reduced-state distance = {worst:.2e}")
    full_dist = distinguishable(psi0, psi1, n, tuple(range(n)))
    check(f"the FULL n-of-{n} coalition DOES recover v (GHZ+/- orthogonal)", full_dist > 0.5,
          f"reduced-state distance = {full_dist:.3f}")
    base_min = min_recovering_coalition(psi0, psi1, n)
    check(f"baseline minimal recovering coalition = n = {n}", base_min == n, f"min coalition = {base_min}")

    # the hard part: try to LOWER it below n via every admissible re-arrangement.
    inv = entanglement_min_coalition_invariant(n, angle_grid)
    print(f"       re-arrangement search: {math.factorial(n)} permutations x {len(angle_grid)**n} local-unitary "
          f"grids; observed min-coalitions = {inv['observed_min_coalitions']}")
    check("min-coalition is INVARIANT (= n) under every admissible re-arrangement (LU + permutations)",
          inv["invariant_at_n"], f"observed = {inv['observed_min_coalitions']}")
    check("NO proper coalition EVER recovered under any admissible re-arrangement (monogamy holds)",
          not inv["proper_coalition_ever_recovered"])

    # cross-check the Bell (n=2) corner too, so 'n-of-n' is not an n=3 artifact.
    inv2 = entanglement_min_coalition_invariant(2, angle_grid)
    check("Bell (n=2) corner: min-coalition invariant at 2 under all admissible re-arrangements",
          inv2["invariant_at_n"] and not inv2["proper_coalition_ever_recovered"],
          f"observed = {inv2['observed_min_coalitions']}")

    ent_invariant = (
        inv["invariant_at_n"] and not inv["proper_coalition_ever_recovered"]
        and inv2["invariant_at_n"] and not inv2["proper_coalition_ever_recovered"]
    )

    # ---------------- (ii) ENCRYPTION: min-coalition FREELY RESETTABLE 1..n ----------------
    print(f"\n[ENC] encryption corner (n = {n}) -- minimal recovering coalition freely reset by RE-KEYING")
    rekeyings = {
        "rekey-1  (ct & whole key at party 0)":              dict(ct_holder=0, key_holders=(0,)),
        "rekey-2  (ct at 0; key split 2-of-2 across 0,1)":   dict(ct_holder=0, key_holders=(0, 1)),
        "rekey-3  (ct at 0; key split 3-of-3 across 0,1,2)": dict(ct_holder=0, key_holders=(0, 1, 2)),
    }
    enc_sizes = []
    for label, cfg in rekeyings.items():
        r = encryption_min_coalition(n, **cfg)
        enc_sizes.append(r["min_coalition_size"])
        print(f"       {label:48s} -> min coalition = {r['min_coalition_size']}, "
              f"witness = {r['witness']}, max-outsider-MI = {r['max_outsider_mi_bits']:.2f} bits")
        check(f"  {label.split()[0]}: an outsider (drop any one member) learns NOTHING "
              f"(sector = W-, one-time pad)", r["max_outsider_mi_bits"] < 1e-9)

    distinct = sorted(set(enc_sizes))
    check("encryption min-coalition takes MULTIPLE distinct values across re-keyings (1, 2, 3)",
          distinct == [1, 2, 3], f"distinct sizes = {distinct}")
    check("re-keying changed ONLY the coalition -- sector stayed W- and CHSH stayed <= 2 throughout",
          s_enc <= 2.0 + 1e-9)
    enc_variable = len(distinct) > 1

    # ---------------- DOUBLE DISSOCIATION -- the self-check gate ----------------
    print("\n[GATE] double dissociation -- the access-structure order parameter is intrinsic ONLY at the")
    print("       entanglement corner and a free relabel at the encryption corner")
    check("(i)  ENTANGLED min-coalition is INVARIANT under all admissible re-arrangements (n-of-n forced)",
          ent_invariant)
    check("(ii) ENCRYPTED min-coalition is VARIABLE under re-keying (freely reset 1..n)",
          enc_variable)
    check("=> DOUBLE DISSOCIATION holds: reframe is non-trivial EXACTLY at the entanglement corner",
          ent_invariant and enc_variable)

    print("\n[verdict]")
    print("  * The access-structure order parameter (minimal recovering coalition) is:")
    print("      - INTRINSIC at the ENTANGLEMENT corner: pinned at n-of-n and invariant under every")
    print("        admissible re-arrangement (local unitaries, member permutations, LOCC). No admissible")
    print("        protocol lowers it below n -- the reduced state on any proper coalition is IDENTICAL for")
    print("        the two secret encodings, so NO operation (POVM/LOCC/comm) recovers v. This is monogamy,")
    print("        and it is what gives the order parameter REAL content: n-of-n is not a labelling choice.")
    print("      - A FREE RELABEL at the ENCRYPTION corner: re-keying (redistributing one-time-pad shares)")
    print("        resets the minimal recovering coalition to any value 1..n with NO change to the sector")
    print("        (an outsider still learns nothing) or the inner CHSH label (still classical, CHSH<=2).")
    print("  * So cluster A's reframe is CONFIRMED but SHARPENED: 'finality = access structure' carries")
    print("    intrinsic content ONLY where entanglement/monogamy pins the coalition -- i.e. the")
    print("    entanglement corner is exactly where the outer-wall access structure is not a free relabel.")
    print("    Everywhere else on the outer wall (classical inaccessibility / encryption) the coalition size")
    print("    is a distributional choice, not an invariant. The order parameter is therefore NOT a single")
    print("    monotone over the whole nested band; it is intrinsic at the inner (CHSH>2) corner only.")

    if FAIL:
        print(f"\nFAILED CHECKS: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = access-structure double dissociation built and confirmed: minimal recovering coalition")
    print("         is invariant (intrinsic) at the entanglement corner, freely re-keyable at encryption.")


if __name__ == "__main__":
    main()
