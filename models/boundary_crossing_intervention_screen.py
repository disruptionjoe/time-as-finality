"""T399: Boundary-crossing intervention statistics screen.

T398 left a stricter next gate for the region-indexed capability lane:
statistics must agree not only for a declared passive readout, but for every
R-supported intervention/readout, and separation must come only from a
boundary-crossing menu.

This finite screen builds the cleanest possible version of that shape. Two
Bell states have identical region and boundary marginals, so no channel or
statistic supported only on the bounded region R can separate them. A joint
boundary-crossing parity/Bell readout separates them perfectly. The result is
therefore a valid finite discriminator shape, but it is absorbed by ordinary
enlarged-state access: the separator is exactly the cross-boundary correlation
that the R marginal omits.
"""

from __future__ import annotations

import json
import math
from typing import Any

import numpy as np


ARTIFACT = "T399-boundary-crossing-intervention-screen-v0.1"
SOURCE_OPEN_PROBLEM = "open-problems/region-indexed-capability-discriminator.md"
TOL_EXACT = 1e-12

VERDICT = (
    "finite boundary-crossing discriminator shape exists but is absorbed: "
    "the two source states are identical under every R-supported statistic "
    "because their R marginals are equal, while a joint boundary-crossing "
    "menu separates them by accessing ordinary cross-boundary correlation; "
    "this is a boundary-access translation result, not a ledger upgrade"
)

FALSIFICATION_CONDITION = (
    "This screen would fail if the selected pair became distinguishable by "
    "any R-supported statistic, if the boundary-crossing menu did not "
    "separate it, or if the separation could not be explained by the "
    "ordinary enlarged state."
)


SQRT2 = math.sqrt(2.0)
KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)
KET_PLUS = (KET0 + KET1) / SQRT2
KET_MINUS = (KET0 - KET1) / SQRT2
KET_PLUS_I = (KET0 + 1j * KET1) / SQRT2
KET_MINUS_I = (KET0 - 1j * KET1) / SQRT2

I2 = np.eye(2, dtype=complex)
X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
H = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / SQRT2
S = np.array([[1.0, 0.0], [0.0, 1j]], dtype=complex)

REGION_UNITARIES = {
    "I": I2,
    "X": X,
    "Y": Y,
    "Z": Z,
    "H": H,
    "S": S,
    "HS": H @ S,
    "SH": S @ H,
}

MEASUREMENT_BASES = {
    "Z": (KET0, KET1),
    "X": (KET_PLUS, KET_MINUS),
    "Y": (KET_PLUS_I, KET_MINUS_I),
}


def _kron(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


def _dm(vec: np.ndarray) -> np.ndarray:
    return np.outer(vec, vec.conj())


def _round_float(value: float) -> float:
    value = float(np.real_if_close(value))
    if abs(value) < TOL_EXACT:
        return 0.0
    if abs(value - 1.0) < TOL_EXACT:
        return 1.0
    if abs(value - 0.5) < TOL_EXACT:
        return 0.5
    return round(value, 12)


def bell_states() -> dict[str, np.ndarray]:
    return {
        "phi_plus": (_kron(KET0, KET0) + _kron(KET1, KET1)) / SQRT2,
        "phi_minus": (_kron(KET0, KET0) - _kron(KET1, KET1)) / SQRT2,
        "psi_plus": (_kron(KET0, KET1) + _kron(KET1, KET0)) / SQRT2,
        "psi_minus": (_kron(KET0, KET1) - _kron(KET1, KET0)) / SQRT2,
    }


def _reduce_region(rho: np.ndarray) -> np.ndarray:
    tensor = rho.reshape(2, 2, 2, 2)
    return np.einsum("rbsb->rs", tensor)


def _reduce_boundary(rho: np.ndarray) -> np.ndarray:
    tensor = rho.reshape(2, 2, 2, 2)
    return np.einsum("rbrc->bc", tensor)


def _trace_norm(mat: np.ndarray) -> float:
    return float(np.sum(np.linalg.svd(mat, compute_uv=False)))


def _trace_distance(rho_a: np.ndarray, rho_b: np.ndarray) -> float:
    return 0.5 * _trace_norm(rho_a - rho_b)


def _single_qubit_distribution(rho: np.ndarray, basis: tuple[np.ndarray, ...]) -> list[float]:
    return [
        _round_float(np.vdot(vec, rho @ vec).real)
        for vec in basis
    ]


def _region_stat_table(vec: np.ndarray) -> dict[str, list[float]]:
    rho_r = _reduce_region(_dm(vec))
    out = {}
    for unitary_name, unitary in REGION_UNITARIES.items():
        moved = unitary @ rho_r @ unitary.conj().T
        for basis_name, basis in MEASUREMENT_BASES.items():
            out[f"{unitary_name}->{basis_name}"] = _single_qubit_distribution(
                moved, basis
            )
    return out


def _boundary_stat_table(vec: np.ndarray) -> dict[str, list[float]]:
    rho_b = _reduce_boundary(_dm(vec))
    return {
        basis_name: _single_qubit_distribution(rho_b, basis)
        for basis_name, basis in MEASUREMENT_BASES.items()
    }


def _max_table_diff(a: dict[str, list[float]], b: dict[str, list[float]]) -> float:
    diff = 0.0
    for key in a:
        diff = max(diff, max(abs(x - y) for x, y in zip(a[key], b[key])))
    return _round_float(diff)


def _parity_distribution(vec: np.ndarray) -> dict[str, float]:
    probs = np.abs(vec.reshape(2, 2)) ** 2
    even = float(probs[0, 0] + probs[1, 1])
    odd = float(probs[0, 1] + probs[1, 0])
    return {"even": _round_float(even), "odd": _round_float(odd)}


def _bell_distribution(vec: np.ndarray) -> dict[str, float]:
    return {
        name: _round_float(abs(np.vdot(bell, vec)) ** 2)
        for name, bell in bell_states().items()
    }


def _binary_success_from_trace_distance(td: float) -> float:
    return _round_float(0.5 * (1.0 + td))


def _main_pair_audit() -> dict[str, Any]:
    states = bell_states()
    a_name, b_name = "phi_plus", "psi_plus"
    a, b = states[a_name], states[b_name]
    rho_a, rho_b = _dm(a), _dm(b)
    rho_ra, rho_rb = _reduce_region(rho_a), _reduce_region(rho_b)
    rho_ba, rho_bb = _reduce_boundary(rho_a), _reduce_boundary(rho_b)

    region_table_a = _region_stat_table(a)
    region_table_b = _region_stat_table(b)
    boundary_table_a = _boundary_stat_table(a)
    boundary_table_b = _boundary_stat_table(b)

    region_td = _round_float(_trace_distance(rho_ra, rho_rb))
    boundary_td = _round_float(_trace_distance(rho_ba, rho_bb))
    full_td = _round_float(_trace_distance(rho_a, rho_b))

    return {
        "pair": [a_name, b_name],
        "region_trace_distance": region_td,
        "boundary_local_trace_distance": boundary_td,
        "full_trace_distance": full_td,
        "all_R_supported_statistic_bound": region_td,
        "all_boundary_local_statistic_bound": boundary_td,
        "region_only_binary_success": _binary_success_from_trace_distance(region_td),
        "boundary_local_binary_success": _binary_success_from_trace_distance(boundary_td),
        "full_state_binary_success": _binary_success_from_trace_distance(full_td),
        "finite_region_intervention_menu": {
            "unitaries": list(REGION_UNITARIES),
            "measurement_bases": list(MEASUREMENT_BASES),
            "n_statistics": len(REGION_UNITARIES) * len(MEASUREMENT_BASES),
            "max_diff": _max_table_diff(region_table_a, region_table_b),
            "sample_phi_plus": region_table_a,
            "sample_psi_plus": region_table_b,
        },
        "boundary_local_statistics": {
            "max_diff": _max_table_diff(boundary_table_a, boundary_table_b),
            "phi_plus": boundary_table_a,
            "psi_plus": boundary_table_b,
        },
        "boundary_crossing_menu": {
            "joint_Z_parity_readout": {
                "phi_plus": _parity_distribution(a),
                "psi_plus": _parity_distribution(b),
                "separates_pair": True,
                "binary_success": 1.0,
            },
            "bell_basis_readout": {
                "phi_plus": _bell_distribution(a),
                "psi_plus": _bell_distribution(b),
                "separates_pair": True,
                "binary_success": 1.0,
            },
        },
    }


def _controls() -> dict[str, Any]:
    states = bell_states()
    region_visible_a = _kron(KET0, KET0)
    region_visible_b = _kron(KET1, KET0)
    rho_ra = _reduce_region(_dm(region_visible_a))
    rho_rb = _reduce_region(_dm(region_visible_b))
    region_visible_td = _round_float(_trace_distance(rho_ra, rho_rb))

    phase_a = states["phi_plus"]
    phase_b = states["phi_minus"]
    phase_region_td = _round_float(
        _trace_distance(_reduce_region(_dm(phase_a)), _reduce_region(_dm(phase_b)))
    )
    phase_boundary_td = _round_float(
        _trace_distance(_reduce_boundary(_dm(phase_a)), _reduce_boundary(_dm(phase_b)))
    )
    phase_full_td = _round_float(_trace_distance(_dm(phase_a), _dm(phase_b)))

    return {
        "region_visible_pair": {
            "pair": ["00_product", "10_product"],
            "region_trace_distance": region_visible_td,
            "region_only_binary_success": _binary_success_from_trace_distance(
                region_visible_td
            ),
            "purpose": (
                "teeth control: the finite R statistics can distinguish a pair "
                "when the R marginal actually differs"
            ),
        },
        "phase_correlation_pair": {
            "pair": ["phi_plus", "phi_minus"],
            "region_trace_distance": phase_region_td,
            "boundary_local_trace_distance": phase_boundary_td,
            "full_trace_distance": phase_full_td,
            "joint_Z_parity_max_diff": _max_table_diff(
                {"parity": list(_parity_distribution(phase_a).values())},
                {"parity": list(_parity_distribution(phase_b).values())},
            ),
            "bell_basis_separates": _bell_distribution(phase_a) != _bell_distribution(phase_b),
            "purpose": (
                "null control: not every cross-boundary distinction is visible "
                "to parity; the Bell menu is the full boundary-crossing readout"
            ),
        },
    }


def _absorber_audit(main: dict[str, Any]) -> dict[str, Any]:
    return {
        "ordinary_enlarged_state_completion": {
            "status": "absorbs",
            "reason": (
                "The full RB states are orthogonal. Once the boundary system "
                "and joint RB measurements are admitted, separation is an "
                "ordinary enlarged-state fact."
            ),
            "full_trace_distance": main["full_trace_distance"],
        },
        "R_supported_intervention_underdescription": {
            "status": "certified_no_separator",
            "reason": (
                "Equal R marginals imply equality for every R-supported "
                "channel followed by every R-supported statistic."
            ),
            "all_R_supported_statistic_bound": main["all_R_supported_statistic_bound"],
        },
        "boundary_relocation": {
            "status": "absorbs_as_access_boundary",
            "reason": (
                "The separation appears exactly when the task menu crosses the "
                "declared boundary; it does not require a new capability object."
            ),
        },
        "SBS_or_closure_key": {
            "status": "not_invoked",
            "reason": (
                "The fixture is a two-qubit correlation screen with no stable "
                "broadcast-structure claim and no claim that an SBS key is fixed."
            ),
        },
    }


def run_boundary_crossing_intervention_screen() -> dict[str, Any]:
    main = _main_pair_audit()
    controls = _controls()
    return {
        "artifact": ARTIFACT,
        "source_open_problem": SOURCE_OPEN_PROBLEM,
        "setup": {
            "region_R": ["first_qubit"],
            "boundary_B": ["second_qubit"],
            "main_pair": "Bell states phi_plus and psi_plus",
            "R_supported_interventions": (
                "arbitrary channels/statistics on R are covered by equality "
                "of the R marginals; the finite unitary/readout table is a "
                "concrete check"
            ),
            "boundary_crossing_menu": [
                "joint Z parity readout",
                "Bell-basis readout",
            ],
        },
        "main_pair_audit": main,
        "controls": controls,
        "absorber_audit": _absorber_audit(main),
        "verdict": VERDICT,
        "residue_label": "absorbed_boundary_access_translation",
        "claim_ledger_update": "none; no claim promotion",
        "recommended_next": [
            "Treat this as a clean finite boundary-access screen, not a promoted residue.",
            "For stronger Direction-A work, require a nontrivial task where the boundary crossing is physically forced rather than merely admitted.",
            "Keep external-facing resource/correlation language behind a separate prior-art note.",
        ],
        "falsification_condition": FALSIFICATION_CONDITION,
    }


if __name__ == "__main__":
    print(json.dumps(run_boundary_crossing_intervention_screen(), indent=2, sort_keys=True))
