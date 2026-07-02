"""T416: Coupling-Graph Forcing Gate.

T412 showed that the parity separator needs a factorization/coupling
admissibility rule. T415 then showed that the principled port of the game
symmetry axiom is the operational automorphism group, but that its physicality
bottoms out at R2: is the coupling graph physically forced or declared?

This gate separates three evidence packets over the same GL(3,2) refactorization
universe used by T415:

1. separator-only evidence;
2. independent singleton-operation support evidence;
3. singleton-operation support plus a path coupling graph.

Verdict: the separator itself does not force the operational automorphism group.
Independent operation/coupling evidence can force it locally, but that evidence
is an extra R2 burden, not a consequence of the separator.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.admissibility_derivation_probe import (
    ENTANGLING_EQ_PRESERVER,
    FANIN,
    _all_invertible_f2_matrices,
    _equality_preserving,
    _global_parity_preserving,
    _is_permutation_matrix,
)
from models.separator_refactorization_gate import N_QUBITS, parity_pair


ARTIFACT = "T416-coupling-graph-forcing-gate-v0.1"
PATH_COUPLING_EDGES = frozenset((frozenset((0, 1)), frozenset((1, 2))))
VERDICT = (
    "R2 is not discharged by separator statistics: separator-only evidence "
    "admits the T415 equality-preserving class, including entangling "
    "refactorizations. Independent singleton-operation evidence forces the "
    "product atom structure up to permutation, and independent path-coupling "
    "evidence further restricts admissibility to graph automorphisms."
)


def _column_support(mat: tuple[tuple[int, ...], ...], source_factor: int) -> tuple[int, ...]:
    return tuple(row for row in range(N_QUBITS) if mat[row][source_factor] == 1)


def support_signature(mat: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    """Output supports reached by toggling each source factor."""
    return tuple(_column_support(mat, col) for col in range(N_QUBITS))


def preserves_singleton_operations(mat: tuple[tuple[int, ...], ...]) -> bool:
    """Every physical one-factor toggle remains a one-factor toggle."""
    return all(len(support) == 1 for support in support_signature(mat))


def source_to_target_permutation(
    mat: tuple[tuple[int, ...], ...]
) -> tuple[int, ...] | None:
    if not preserves_singleton_operations(mat):
        return None
    return tuple(support[0] for support in support_signature(mat))


def _map_edges(
    edges: frozenset[frozenset[int]], permutation: tuple[int, ...]
) -> frozenset[frozenset[int]]:
    return frozenset(frozenset(permutation[node] for node in edge) for edge in edges)


def preserves_path_coupling_graph(mat: tuple[tuple[int, ...], ...]) -> bool:
    permutation = source_to_target_permutation(mat)
    if permutation is None:
        return False
    return _map_edges(PATH_COUPLING_EDGES, permutation) == PATH_COUPLING_EDGES


def _matrix_rows(mat: tuple[tuple[int, ...], ...]) -> list[str]:
    return ["".join(str(bit) for bit in row) for row in mat]


def _packet(
    name: str,
    matrices: list[tuple[tuple[int, ...], ...]],
    equality_preserving: list[tuple[tuple[int, ...], ...]],
) -> dict[str, Any]:
    entangling_eq = [m for m in matrices if m in equality_preserving and not _is_permutation_matrix(m)]
    return {
        "name": name,
        "admissible_count_linear": len(matrices),
        "admissible_count_with_local_bit_flips_if_affine_extended": len(matrices) * (2**N_QUBITS),
        "entangling_equality_preservers_admitted": len(entangling_eq),
        "admits_entangling_equality_preserver": bool(entangling_eq),
        "sample_entangling_equality_preserver": (
            _matrix_rows(entangling_eq[0]) if entangling_eq else None
        ),
    }


def run_coupling_graph_forcing_gate() -> dict[str, Any]:
    states = parity_pair()
    even = states["even_parity"]
    odd = states["odd_parity"]
    group = _all_invertible_f2_matrices()

    equality_preserving = [m for m in group if _equality_preserving(m, even, odd)]
    product_atoms = [m for m in group if preserves_singleton_operations(m)]
    path_graph = [m for m in group if preserves_path_coupling_graph(m)]

    entangling_eq = [m for m in equality_preserving if not _is_permutation_matrix(m)]

    named_entangling = {
        "map": "y0=x0^x2, y1=x1^x2, y2=x2",
        "rows": _matrix_rows(ENTANGLING_EQ_PRESERVER),
        "equality_preserving": ENTANGLING_EQ_PRESERVER in equality_preserving,
        "global_parity_preserving": _global_parity_preserving(ENTANGLING_EQ_PRESERVER),
        "preserves_singleton_operations": preserves_singleton_operations(
            ENTANGLING_EQ_PRESERVER
        ),
        "support_signature": support_signature(ENTANGLING_EQ_PRESERVER),
    }
    named_fanin = {
        "map": "y0=x0^x1^x2, y1=x1, y2=x2",
        "rows": _matrix_rows(FANIN),
        "equality_preserving": FANIN in equality_preserving,
        "global_parity_preserving": _global_parity_preserving(FANIN),
        "preserves_singleton_operations": preserves_singleton_operations(FANIN),
        "support_signature": support_signature(FANIN),
    }

    return {
        "artifact": ARTIFACT,
        "source": [
            "tests/T412-separator-refactorization-gate.md",
            "tests/T414-certificate-identity-bridge.md",
            "tests/T415-admissibility-derivation-probe.md",
            "explorations/governance-shapley-finality-homology-note-2026-07-02.md",
        ],
        "claim_ledger_update": "none; no claim promotion",
        "r2_question": (
            "Is the operational structure - tensor product, singleton operations, "
            "or coupling graph - physically forced rather than selected to save "
            "the separator?"
        ),
        "universe": {
            "refactorizations": "GL(3,2) reversible linear refactorizations",
            "count": len(group),
            "local_bit_flips": (
                "not enumerated here because T415 is linear; they multiply the "
                "support-preserving counts by 8 and do not change support or graph"
            ),
        },
        "counts": {
            "GL_3_2": len(group),
            "separator_equality_preserving": len(equality_preserving),
            "entangling_equality_preserving": len(entangling_eq),
            "singleton_operation_support_preserving": len(product_atoms),
            "path_coupling_graph_preserving": len(path_graph),
        },
        "evidence_packets": {
            "separator_only": {
                **_packet("separator_only", equality_preserving, equality_preserving),
                "status": "does_not_force_product_or_coupling_structure",
                "independent_of_target_separator": False,
            },
            "singleton_operation_support": {
                **_packet("singleton_operation_support", product_atoms, equality_preserving),
                "status": "forces_product_atoms_up_to_permutation_if_independent",
                "independent_of_target_separator": True,
            },
            "path_coupling_graph": {
                **_packet("path_coupling_graph", path_graph, equality_preserving),
                "status": "forces_declared_path_graph_up_to_reversal_if_independent",
                "independent_of_target_separator": True,
                "edges": [sorted(edge) for edge in sorted(PATH_COUPLING_EDGES, key=sorted)],
                "automorphism_permutations": [
                    list(source_to_target_permutation(m)) for m in path_graph
                ],
            },
        },
        "named_attacks": {
            "entangling_equality_preserver": named_entangling,
            "fanin_localizer": named_fanin,
        },
        "decision_rule": {
            "separator_only": "insufficient_for_R2",
            "singleton_operations": "sufficient_for_product_atoms_only_if_independently_measured_or_physically_supplied",
            "coupling_graph": "sufficient_for_graph_automorphisms_only_if_independently_measured_or_physically_supplied",
        },
        "verdict": VERDICT,
        "demotion_condition": (
            "If the only available evidence for the factorization is that it "
            "makes the separator global, the R2 burden is unpaid and the "
            "separator remains factorization-relative."
        ),
    }


def main() -> None:
    result = run_coupling_graph_forcing_gate()
    out = Path(__file__).resolve().parents[1] / "results" / (
        "T416-coupling-graph-forcing-gate-v0.1.json"
    )
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
