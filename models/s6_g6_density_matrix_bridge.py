"""G6: finite density-matrix system-environment bridge for S6.

This is the first S6 follow-up that uses an explicit finite quantum state
instead of an analytic record-channel profile. A system qubit starts in
|+>, five environment qubits start in |0>, and fixed controlled rotations
entangle the pointer value with each environment fragment.

The result is still a toy model. It is a finite state-vector / reduced-density
matrix fixture, not a Hamiltonian/Lindblad/SBS theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, log2, pi, sin, sqrt
from typing import Any


FRAGMENTS: tuple[str, ...] = tuple(f"E{i}" for i in range(5))
COUPLINGS: tuple[float, ...] = (1.0, 0.85, 0.7, 0.55, 0.4)
STRENGTHS: tuple[float, ...] = (0.0, 0.4, 0.8, 1.0, 1.2, 1.4, 1.6)
MI_THRESHOLD = 0.2
DESCENT_SUPPORT = 4
EXPECTED_POINTER = 1
EXPECTED_EDGES: tuple[tuple[str, str], ...] = (
    ("prep", "measure"),
    ("measure", "record"),
)


@dataclass(frozen=True)
class FragmentDensity:
    name: str
    coupling: float
    theta: float
    density: tuple[tuple[complex, complex], tuple[complex, complex]]
    correct_probability: float
    mutual_information: float
    redundant: bool


@dataclass(frozen=True)
class DensityLevel:
    strength: float
    system_density: tuple[tuple[complex, complex], tuple[complex, complex]]
    offdiag_magnitude: float
    fragments: tuple[FragmentDensity, ...]
    redundant_count: int
    gluing_error: float
    descent_stable: bool
    eta_loss: tuple[str, ...]


def run_g6_density_matrix_bridge() -> dict[str, Any]:
    sweep = tuple(analyze_strength(strength) for strength in STRENGTHS)
    threshold = next(level for level in sweep if level.descent_stable)
    checks = {
        "state_density_computed": all(
            abs(_trace(level.system_density).real - 1.0) < 1e-9 for level in sweep
        ),
        "decoherence_monotone": _monotone_nonincreasing(
            [level.offdiag_magnitude for level in sweep]
        ),
        "redundancy_threshold_detected": (
            threshold.strength == 1.2
            and threshold.redundant_count == DESCENT_SUPPORT
            and threshold.offdiag_magnitude < 0.05
        ),
        "descent_record_stabilized": threshold.descent_stable,
        "eta_loss_detected": "phase_sensitive_branch" in threshold.eta_loss,
    }
    return {
        "test": "s6-g6-density-matrix-bridge-v0.1",
        "tag": ["finite_witness", "density_matrix_toy", "no_claim_promotion"],
        "guardrail": (
            "Finite controlled-rotation state-vector fixture only: not a "
            "Hamiltonian, not Lindblad dynamics, not an SBS theorem, and not "
            "source-side issuance evidence."
        ),
        "parameters": {
            "fragments": list(FRAGMENTS),
            "couplings": list(COUPLINGS),
            "strengths": list(STRENGTHS),
            "mutual_information_threshold": MI_THRESHOLD,
            "descent_support": DESCENT_SUPPORT,
            "expected_edges": [list(edge) for edge in EXPECTED_EDGES],
        },
        "checks": checks,
        "all_checks_passed": all(checks.values()),
        "threshold": _level_to_dict(threshold),
        "sweep": [_level_to_dict(level) for level in sweep],
        "effect_verdict": {
            "Issue[S]": False,
            "Project[O]": True,
            "Finalize[R]": True,
            "Lose[K]": True,
        },
        "strongest_result": (
            "An explicit finite system-environment state reaches the S6 descent "
            "threshold at strength=1.2: four fragments carry >=0.2 bits of "
            "pointer information, the system off-diagonal magnitude falls below "
            "0.05, and the pointer/provenance record stabilizes while phase "
            "capability is lost."
        ),
        "first_obstruction": (
            "The fixture uses controlled rotations with fixed strengths. It is "
            "density-matrix evidence for executability, not physical evidence for "
            "a generic quantum-to-classical bridge."
        ),
        "next_step": (
            "Add SBS-style conditional distinguishability and independence scores "
            "over the same density-matrix fragments."
        ),
    }


def analyze_strength(strength: float) -> DensityLevel:
    state = state_vector(strength)
    total_qubits = 1 + len(FRAGMENTS)
    system_density = reduced_qubit_density(state, total_qubits, 0)
    fragments = tuple(
        _fragment_density(state, total_qubits, index + 1, name, coupling, strength)
        for index, (name, coupling) in enumerate(zip(FRAGMENTS, COUPLINGS))
    )
    redundant_count = sum(1 for fragment in fragments if fragment.redundant)
    descent_stable = (
        redundant_count >= DESCENT_SUPPORT
        and abs(system_density[0][1]) < 0.05
    )
    return DensityLevel(
        strength=strength,
        system_density=system_density,
        offdiag_magnitude=abs(system_density[0][1]),
        fragments=fragments,
        redundant_count=redundant_count,
        gluing_error=(len(FRAGMENTS) - redundant_count) / len(FRAGMENTS),
        descent_stable=descent_stable,
        eta_loss=("phase_sensitive_branch",) if descent_stable else (),
    )


def state_vector(strength: float) -> tuple[complex, ...]:
    total_qubits = 1 + len(FRAGMENTS)
    vector = [0j for _ in range(2**total_qubits)]
    alpha = 1 / sqrt(2)
    beta = 1 / sqrt(2)

    vector[0] = alpha
    for env_bits in range(2 ** len(FRAGMENTS)):
        amplitude = beta
        bits: list[int] = []
        for env_index, coupling in enumerate(COUPLINGS):
            theta = _theta(strength, coupling)
            bit = (env_bits >> (len(FRAGMENTS) - 1 - env_index)) & 1
            bits.append(bit)
            amplitude *= sin(theta) if bit else cos(theta)
        basis_bits = [1] + bits
        vector[_basis_index(basis_bits)] = amplitude

    norm = sqrt(sum(abs(value) ** 2 for value in vector))
    return tuple(value / norm for value in vector)


def reduced_qubit_density(
    state: tuple[complex, ...],
    total_qubits: int,
    keep_qubit: int,
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    rho = [[0j, 0j], [0j, 0j]]
    for left_index, left_amp in enumerate(state):
        if left_amp == 0:
            continue
        for right_index, right_amp in enumerate(state):
            if right_amp == 0:
                continue
            if _other_bits_equal(left_index, right_index, total_qubits, keep_qubit):
                left_bit = _bit(left_index, total_qubits, keep_qubit)
                right_bit = _bit(right_index, total_qubits, keep_qubit)
                rho[left_bit][right_bit] += left_amp * right_amp.conjugate()
    return ((rho[0][0], rho[0][1]), (rho[1][0], rho[1][1]))


def _fragment_density(
    state: tuple[complex, ...],
    total_qubits: int,
    qubit: int,
    name: str,
    coupling: float,
    strength: float,
) -> FragmentDensity:
    density = reduced_qubit_density(state, total_qubits, qubit)
    theta = _theta(strength, coupling)
    correct_probability = sin(theta) ** 2
    mutual_information = _binary_pointer_information(correct_probability)
    return FragmentDensity(
        name=name,
        coupling=coupling,
        theta=theta,
        density=density,
        correct_probability=correct_probability,
        mutual_information=mutual_information,
        redundant=mutual_information >= MI_THRESHOLD,
    )


def _binary_pointer_information(p_one_given_pointer: float) -> float:
    # S is unbiased. Fragment measurement Y has P(Y=1|S=0)=0 and
    # P(Y=1|S=1)=p_one_given_pointer.
    marginal_one = 0.5 * p_one_given_pointer
    return _binary_entropy(marginal_one) - 0.5 * _binary_entropy(
        p_one_given_pointer
    )


def _binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def _theta(strength: float, coupling: float) -> float:
    return min(pi / 2, strength * coupling)


def _basis_index(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def _bit(index: int, total_qubits: int, qubit: int) -> int:
    return (index >> (total_qubits - 1 - qubit)) & 1


def _other_bits_equal(
    left_index: int,
    right_index: int,
    total_qubits: int,
    keep_qubit: int,
) -> bool:
    for qubit in range(total_qubits):
        if qubit == keep_qubit:
            continue
        if _bit(left_index, total_qubits, qubit) != _bit(
            right_index, total_qubits, qubit
        ):
            return False
    return True


def _trace(matrix: tuple[tuple[complex, complex], tuple[complex, complex]]) -> complex:
    return matrix[0][0] + matrix[1][1]


def _monotone_nonincreasing(values: list[float]) -> bool:
    return all(left >= right for left, right in zip(values, values[1:]))


def _complex_to_pair(value: complex) -> list[float]:
    return [round(value.real, 6), round(value.imag, 6)]


def _matrix_to_pairs(
    matrix: tuple[tuple[complex, complex], tuple[complex, complex]]
) -> list[list[list[float]]]:
    return [[_complex_to_pair(value) for value in row] for row in matrix]


def _level_to_dict(level: DensityLevel) -> dict[str, Any]:
    return {
        "strength": level.strength,
        "system_density": _matrix_to_pairs(level.system_density),
        "offdiag_magnitude": round(level.offdiag_magnitude, 6),
        "redundant_count": level.redundant_count,
        "gluing_error": round(level.gluing_error, 6),
        "descent_stable": level.descent_stable,
        "eta_loss": list(level.eta_loss),
        "fragments": [
            {
                "name": fragment.name,
                "coupling": fragment.coupling,
                "theta": round(fragment.theta, 6),
                "density": _matrix_to_pairs(fragment.density),
                "correct_probability": round(fragment.correct_probability, 6),
                "mutual_information": round(fragment.mutual_information, 6),
                "redundant": fragment.redundant,
            }
            for fragment in level.fragments
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_g6_density_matrix_bridge(), indent=2, sort_keys=True))
