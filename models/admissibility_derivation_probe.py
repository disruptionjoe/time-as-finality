"""T415 - Admissibility-Derivation Probe.

Bridge obligation #2 of the governance-Shapley-finality homology: does the game's
DERIVED admissibility rule (T414: symmetry / Arrow-IIA) port to the quantum
separator, discharging T412's "the admissibility rule must be declared" worry?

Distinguishes two candidate ports over the full group of reversible linear
refactorizations GL(3,2):
  (P1) equality-preservation  - admissible iff the defining equality is preserved
  (P2) operational automorphism group - admissible iff a product/coupling-
       preserving automorphism (the correct analog of the game's symmetry axiom)

Finding (predeclared): (P1) is tautological and strictly broader than product
preservation (18 entangling equality-preservers exist), so it cannot justify the
rule; (P2) is the principled port but its physicality is R2 (coupling graph
forced or declared?). Reuses T412 machinery; does not redo it. Cross-domain
material is object of study, never evidence. No claim promotion; ledger untouched.

    python -m models.admissibility_derivation_probe
    python -m pytest tests/test_admissibility_derivation_probe.py -v
"""

from __future__ import annotations

import itertools
import json

import numpy as np

from models.separator_refactorization_gate import (
    N_QUBITS, parity_pair, subset_trace_distances, trace_distance,
    partial_trace, _bits, _index,
)


# ---------------------------------------------------------------------------
# F2 linear algebra on 3-bit refactorizations.
# ---------------------------------------------------------------------------
def _matvec_f2(mat, x):
    """Apply 3x3 F2 matrix `mat` (rows) to bit-vector x -> bit-vector."""
    return tuple(
        (mat[i][0] & x[0]) ^ (mat[i][1] & x[1]) ^ (mat[i][2] & x[2])
        for i in range(N_QUBITS)
    )


def _det_f2(mat):
    a, b, c = mat[0]
    d, e, f = mat[1]
    g, h, i = mat[2]
    # determinant over F2 (expansion; all products mod 2)
    return (a & e & i) ^ (a & f & h) ^ (b & d & i) ^ (b & f & g) ^ (c & d & h) ^ (c & e & g)


def _all_invertible_f2_matrices():
    """Enumerate GL(3,2): all invertible 3x3 matrices over F2 (168)."""
    out = []
    for bits in itertools.product((0, 1), repeat=9):
        mat = (bits[0:3], bits[3:6], bits[6:9])
        if _det_f2(mat) == 1:
            out.append(mat)
    return out


def _is_permutation_matrix(mat):
    """Product-structure-preserving linear map == a qubit permutation matrix:
    exactly one 1 per row and per column."""
    rows_ok = all(sum(mat[i]) == 1 for i in range(3))
    cols_ok = all(sum(mat[r][c] for r in range(3)) == 1 for c in range(3))
    return rows_ok and cols_ok


def _global_parity_preserving(mat):
    """1^T A = 1^T over F2: every column sums to 1 (mod 2)."""
    return all((sum(mat[r][c] for r in range(3)) & 1) == 1 for c in range(3))


def _unitary_from_linear(mat):
    """8x8 basis-permutation unitary induced by the reversible linear map."""
    dim = 2 ** N_QUBITS
    u = np.zeros((dim, dim), dtype=complex)
    for src in range(dim):
        tgt = _index(_matvec_f2(mat, _bits(src)))
        u[tgt, src] = 1.0
    return u


def _apply(u, rho):
    return u @ rho @ u.conj().T


def _equality_preserving(mat, even, odd):
    """Computed: does the relabel keep all proper-subset marginals equal?"""
    u = _unitary_from_linear(mat)
    dists = subset_trace_distances(_apply(u, even), _apply(u, odd))
    return max(dists.values()) == 0.0


# ---------------------------------------------------------------------------
# Named example maps.
# ---------------------------------------------------------------------------
# entangling but global-parity (equality) preserving: y0=x0^x2, y1=x1^x2, y2=x2
ENTANGLING_EQ_PRESERVER = ((1, 0, 1), (0, 1, 1), (0, 0, 1))
# fan-in, global-parity BREAKING: y0=x0^x1^x2
FANIN = ((1, 1, 1), (0, 1, 0), (0, 0, 1))


def run():
    states = parity_pair()
    even, odd = states["even_parity"], states["odd_parity"]

    base_subsets = subset_trace_distances(even, odd)
    baseline = {
        "max_proper_subset_td": max(base_subsets.values()),
        "full_joint_td": trace_distance(even, odd),
    }

    group = _all_invertible_f2_matrices()
    eq, gp, perm, ent_eq = [], [], [], []
    partition_matches = True
    for mat in group:
        e = _equality_preserving(mat, even, odd)
        g = _global_parity_preserving(mat)
        p = _is_permutation_matrix(mat)
        if e:
            eq.append(mat)
        if g:
            gp.append(mat)
        if p:
            perm.append(mat)
        if e != g:
            partition_matches = False
        if e and not p:
            ent_eq.append(mat)

    # named examples
    ee_u = _unitary_from_linear(ENTANGLING_EQ_PRESERVER)
    ee_sub = subset_trace_distances(_apply(ee_u, even), _apply(ee_u, odd))
    fi_u = _unitary_from_linear(FANIN)
    fi_sub = subset_trace_distances(_apply(fi_u, even), _apply(fi_u, odd))
    fi_q0 = trace_distance(
        partial_trace(_apply(fi_u, even), (0,)), partial_trace(_apply(fi_u, odd), (0,))
    )

    # (P1) circularity: full-joint TD invariant under EVERY group element (unitary)
    full_td_invariant_all = all(
        trace_distance(_apply(_unitary_from_linear(m), even), _apply(_unitary_from_linear(m), odd)) == 1.0
        for m in group
    )

    return {
        "artifact": "T415-admissibility-derivation-probe-v0.1",
        "source": [
            "results/T412-separator-refactorization-gate-v0.1-results.md",
            "results/T414-certificate-identity-bridge-v0.1-results.md",
            "explorations/governance-shapley-finality-homology-note-2026-07-02.md",
        ],
        "claim_ledger_update": "none; no claim promotion",
        "baseline_reproduces_T412": baseline,
        "counts": {
            "GL_3_2": len(group),
            "equality_preserving": len(eq),
            "global_parity_preserving": len(gp),
            "product_preserving_permutations": len(perm),
            "entangling_equality_preserving": len(ent_eq),
        },
        "leg2_equality_iff_global_parity": partition_matches,
        "leg4_teeth_entangling_equality_preserver": {
            "map": "y0=x0^x2, y1=x1^x2, y2=x2 (CNOT(2->0)CNOT(2->1))",
            "is_permutation": _is_permutation_matrix(ENTANGLING_EQ_PRESERVER),
            "global_parity_preserving": _global_parity_preserving(ENTANGLING_EQ_PRESERVER),
            "max_proper_subset_td": max(ee_sub.values()),   # 0.0 -> equality preserved
            "equality_preserving": max(ee_sub.values()) == 0.0,
        },
        "leg4_fanin_breaks_equality": {
            "map": "y0=x0^x1^x2 (parity fan-in)",
            "global_parity_preserving": _global_parity_preserving(FANIN),
            "max_proper_subset_td": max(fi_sub.values()),   # 1.0 -> localized
            "factor0_td": fi_q0,
        },
        "leg5_P1_circularity": {
            "full_joint_td_invariant_under_all_relabels": full_td_invariant_all,
            "equality_preservation_is_tautological": full_td_invariant_all,
            "note": ("full-joint TD is unitarily invariant, so 'equality-preserving' "
                     "means only 'keeps proper-subset TD 0' = 'keeps the separator a "
                     "separator'; and it admits 18 entangling maps a local agent may "
                     "lack -> cannot independently justify the admissibility rule"),
        },
        "leg6_P2_operational_automorphism": {
            "principled_admissible_class": "operational automorphism group (product/coupling-preserving = T412 class)",
            "game_analog": "the symmetry axiom (automorphisms of the game = player permutations)",
            "separator_survives": baseline["max_proper_subset_td"] == 0.0,
            "is_free_declaration": False,
            "is_operational_commitment": True,
            "physicality_reduces_to": "R2 (is the coupling graph / factorization physically forced?)",
        },
        "verdict": (
            "bridge obligation #2 STRUCTURALLY BRIDGED (game symmetry axiom <-> "
            "quantum operational-automorphism admissibility) but NOT discharged to "
            "physicality: it bottoms out at R2. The naive equality-preservation port "
            "(P1) is refuted as circular; the principled port (P2) is an operational "
            "commitment, R2-conditional."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, default=str))
