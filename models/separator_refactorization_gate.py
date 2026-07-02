"""T412: Separator Refactorization Gate.

The physical-boundary post-mortem named one linchpin test for the surviving
T411 fallback: does the "global in no proper subset" separator survive all
admissible refactorizations of the reach, or only support/light-cone
functionals?

This harness makes the admissibility split explicit. A three-bit parity pair
has identical marginals on every nonempty proper subset, while the full joint
parity separates perfectly. That property survives product-structure-preserving
relabels: qubit permutations, local bit flips, and product-basis changes. It
does not survive an arbitrary entangling refactorization: a reversible parity
fan-in maps the global parity into one output factor, making a single-qubit
marginal separate perfectly.

Verdict: the separator is a real interface signature only relative to a
declared operational tensor product / coupling graph. If arbitrary entangling
refactorizations count as admissible, the anti-relabel fallback collapses.
No claim promotion.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any

import numpy as np


ARTIFACT = "T412-separator-refactorization-gate-v0.1"
TOL = 1e-12
N_QUBITS = 3

VERDICT = (
    "the global-correlation separator survives product-structure-preserving "
    "relabels, but arbitrary entangling refactorization localizes the datum "
    "into one factor; the fallback therefore needs an explicit "
    "factorization/coupling-preservation admissibility rule, not physical-"
    "boundary language"
)


def _bits(index: int, n: int = N_QUBITS) -> tuple[int, ...]:
    return tuple((index >> (n - 1 - i)) & 1 for i in range(n))


def _index(bits: tuple[int, ...]) -> int:
    out = 0
    for bit in bits:
        out = (out << 1) | int(bit)
    return out


def _round(value: float) -> float:
    value = float(np.real_if_close(value))
    if abs(value) < TOL:
        return 0.0
    if abs(value - 1.0) < TOL:
        return 1.0
    if abs(value - 0.5) < TOL:
        return 0.5
    return round(value, 12)


def _density_from_indices(indices: list[int]) -> np.ndarray:
    dim = 2**N_QUBITS
    rho = np.zeros((dim, dim), dtype=complex)
    weight = 1.0 / len(indices)
    for index in indices:
        rho[index, index] = weight
    return rho


def parity_pair() -> dict[str, np.ndarray]:
    even, odd = [], []
    for index in range(2**N_QUBITS):
        target = even if sum(_bits(index)) % 2 == 0 else odd
        target.append(index)
    return {
        "even_parity": _density_from_indices(even),
        "odd_parity": _density_from_indices(odd),
    }


def partial_trace(rho: np.ndarray, keep: tuple[int, ...]) -> np.ndarray:
    keep = tuple(keep)
    traced = tuple(i for i in range(N_QUBITS) if i not in keep)
    tensor = rho.reshape([2] * (2 * N_QUBITS))
    perm = list(keep) + list(traced) + [i + N_QUBITS for i in keep] + [
        i + N_QUBITS for i in traced
    ]
    moved = np.transpose(tensor, perm)
    d_keep = 2 ** len(keep)
    d_traced = 2 ** len(traced)
    moved = moved.reshape(d_keep, d_traced, d_keep, d_traced)
    return np.einsum("abcb->ac", moved)


def trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    return _round(0.5 * float(np.sum(np.linalg.svd(a - b, compute_uv=False))))


def proper_subsets() -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for size in range(1, N_QUBITS):
        out.extend(tuple(combo) for combo in itertools.combinations(range(N_QUBITS), size))
    return out


def subset_trace_distances(a: np.ndarray, b: np.ndarray) -> dict[str, float]:
    out = {}
    for subset in proper_subsets():
        key = "".join(str(i) for i in subset)
        out[key] = trace_distance(partial_trace(a, subset), partial_trace(b, subset))
    return out


def full_parity_distribution(rho: np.ndarray) -> dict[str, float]:
    diag = np.real(np.diag(rho))
    even = sum(diag[i] for i in range(2**N_QUBITS) if sum(_bits(i)) % 2 == 0)
    odd = 1.0 - even
    return {"even": _round(even), "odd": _round(odd)}


def _unitary_from_bit_map(map_bits) -> np.ndarray:
    dim = 2**N_QUBITS
    unitary = np.zeros((dim, dim), dtype=complex)
    for source in range(dim):
        target = _index(tuple(map_bits(_bits(source))))
        unitary[target, source] = 1.0
    return unitary


def _apply(unitary: np.ndarray, rho: np.ndarray) -> np.ndarray:
    return unitary @ rho @ unitary.conj().T


def product_relabel_unitaries() -> list[np.ndarray]:
    """All qubit permutations plus local computational-basis flips."""
    out = []
    for perm in itertools.permutations(range(N_QUBITS)):
        for flip_mask in range(2**N_QUBITS):
            flips = _bits(flip_mask)

            def mapper(bits, perm=perm, flips=flips):
                return tuple(bits[perm[i]] ^ flips[i] for i in range(N_QUBITS))

            out.append(_unitary_from_bit_map(mapper))
    return out


def product_basis_unitary() -> np.ndarray:
    h = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / np.sqrt(2.0)
    phase = np.array([[1.0, 0.0], [0.0, 1j]], dtype=complex)
    return np.kron(np.kron(h, phase), h)


def parity_fanin_refactorization() -> np.ndarray:
    """Entangling change of factors: y0 = x0 xor x1 xor x2."""

    def mapper(bits):
        return (bits[0] ^ bits[1] ^ bits[2], bits[1], bits[2])

    return _unitary_from_bit_map(mapper)


def _max(values) -> float:
    return _round(max(values))


def run_separator_refactorization_gate() -> dict[str, Any]:
    states = parity_pair()
    even = states["even_parity"]
    odd = states["odd_parity"]
    subset_distances = subset_trace_distances(even, odd)
    full_td = trace_distance(even, odd)

    product_maxima = []
    for unitary in product_relabel_unitaries():
        relabeled_even = _apply(unitary, even)
        relabeled_odd = _apply(unitary, odd)
        product_maxima.append(
            _max(subset_trace_distances(relabeled_even, relabeled_odd).values())
        )

    basis_u = product_basis_unitary()
    basis_even = _apply(basis_u, even)
    basis_odd = _apply(basis_u, odd)
    basis_subsets = subset_trace_distances(basis_even, basis_odd)

    fanin = parity_fanin_refactorization()
    fanin_even = _apply(fanin, even)
    fanin_odd = _apply(fanin, odd)
    fanin_subsets = subset_trace_distances(fanin_even, fanin_odd)
    fanin_q0_even = partial_trace(fanin_even, (0,))
    fanin_q0_odd = partial_trace(fanin_odd, (0,))

    product_preserving_survives = _max(product_maxima) == 0.0
    arbitrary_refactorization_collapses = fanin_subsets["0"] == 1.0

    return {
        "artifact": ARTIFACT,
        "source": [
            "explorations/physical-boundary-hegelian-persona-pass-2026-07-02.md",
            "results/T411-departed-record-capability-discriminator-v0.1-results.md",
            "open-problems/region-indexed-capability-discriminator.md",
        ],
        "claim_ledger_update": "none; no claim promotion",
        "residue_label": "factorization_guardrail_required",
        "fixture": {
            "description": "three-qubit even/odd parity mixed-state pair",
            "proper_subsets": ["".join(str(i) for i in s) for s in proper_subsets()],
            "t411_shadow": (
                "canonical finite shadow of T411 beta=0: no proper subset "
                "carries the datum, while the full joint does"
            ),
        },
        "declared_factorization": {
            "proper_subset_trace_distances": subset_distances,
            "max_proper_subset_trace_distance": _max(subset_distances.values()),
            "full_trace_distance": full_td,
            "full_parity_readout": {
                "even_state": full_parity_distribution(even),
                "odd_state": full_parity_distribution(odd),
                "binary_success": _round(0.5 * (1.0 + full_td)),
            },
        },
        "structure_preserving_relabels": {
            "class": "qubit permutations + local bit flips; product-basis spot check",
            "n_permutation_flip_relabels": len(product_maxima),
            "max_proper_subset_trace_distance_after_relabels": _max(product_maxima),
            "product_basis_spot_check": {
                "max_proper_subset_trace_distance": _max(basis_subsets.values()),
                "proper_subset_trace_distances": basis_subsets,
                "full_trace_distance": trace_distance(basis_even, basis_odd),
            },
            "survives": product_preserving_survives,
        },
        "entangling_refactorization_attack": {
            "map": "y0 = x0 xor x1 xor x2; y1 = x1; y2 = x2",
            "proper_subset_trace_distances": fanin_subsets,
            "localized_factor": "0",
            "localized_factor_trace_distance": trace_distance(fanin_q0_even, fanin_q0_odd),
            "localized_factor_even_state": np.real_if_close(fanin_q0_even).tolist(),
            "localized_factor_odd_state": np.real_if_close(fanin_q0_odd).tolist(),
            "full_trace_distance_after_refactorization": trace_distance(
                fanin_even, fanin_odd
            ),
            "collapses_if_admissible": arbitrary_refactorization_collapses,
        },
        "admissibility_verdict": {
            "product_structure_preserving_relabels": "pass",
            "arbitrary_entangling_refactorizations": "fail",
            "rule_needed": (
                "admissible relabels must preserve the operational tensor "
                "product, coupling graph, or declared access factorization"
            ),
        },
        "verdict": VERDICT,
        "demotion_condition": (
            "If a future result allows arbitrary entangling refactorization as "
            "an admissible change of reach description, the R1 anti-relabel "
            "separator demotes to a coordinate-dependent global-correlation "
            "exhibit."
        ),
    }


def main() -> None:
    result = run_separator_refactorization_gate()
    out = Path(__file__).resolve().parents[1] / "results" / (
        "T412-separator-refactorization-gate-v0.1.json"
    )
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
