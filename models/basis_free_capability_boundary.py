"""T408: Basis-Free Flat Pair and the Physical Capability Boundary.

T407 (region-indexed capability no-go) earned a 16-configuration class with
exactly equal DECLARED Z-readout statistics realizing all 12 capability
profiles -- and its standing hostile-review objection, priced in-spec and in
the swing addendum, was: the flatness leg is relative to the declared readout
convention. A different declared basis could have split the class. The
flatness characterized a bookkeeping boundary, not a physical one.

This artifact is the priced v0.2 card, executed: a BASIS-FREE flat pair.

Two preparations A and B share the T392/T393 measurement core (system S with
prepared phase phi, weak meter M at theta = pi/3, fragments F1..F4) plus one
additional, IDENTICAL record-copy event: the F4 record is copied to an annex
qubit AX that stays inside the fixed accessible zone. They differ in exactly
one physical fact: in B the annex record LEAKS onto an outgoing mode (T393's
controlled-Ry emission, alpha = pi for the exact copy) and propagates down
T393's discrete SWAP-chain lightcone, escaping past the zone boundary; in A
nothing is emitted.

Because the leak and the propagation are supported entirely OUTSIDE the
record region R = {S, M, F1..F4}, the full region state rho_R is IDENTICAL
between A and B as an operator -- not just in one declared readout: every
POVM on R, every channel-then-readout composition supported on R, gives
exactly equal statistics (trace distance 0 + CPTP contractivity). Asserted
numerically < 1e-12 at every certificate phase, every lightcone step, every
leak amplitude. Yet the capability under the ONE fixed menu (all channels
supported on the accessible zone Z = R + {AX, C0, C1}; the menu never touches
the escaped tail C2) splits: A's extended undo restores phase-locked
visibility 4*sqrt(3)/7 >= v* = 0.9, while B's recovery is impossible for ALL
channels on Z (phi-independence certificate + T393's channel-independent
trace-norm bound).

THE OBSTRUCTION LEMMA (stated and witnessed, not just argued): capability
under a menu supported on Z is a functional of the phi-indexed conditional
state family on Z, so a pair that is operator-flat ON THE FULL MENU SUPPORT
cannot have a capability gap. The flat surface can be pushed exactly up to
the complement of the menu support and no further. This artifact delivers
both directions: flat-on-R with a certified gap (the construction), and
flat-on-Z forces no gap (tail-unitary witness pairs, computed identity).
The capability difference therefore REQUIRES a statistical trace within the
menu's reach -- here located entirely in annex/fragment coherences, invisible
to every measurement on R and to every Z-basis readout even on Z.

Part 2 (graded curve): T393's partial-amplitude alpha machinery, with the
whole sweep sitting on ONE basis-free-flat family (rho_R identical at every
alpha). The capability boundary appears as a graded physical curve:
achieved recovery cos(alpha/2) * 4sqrt(3)/7, escaped-holder distinguishability
sin(alpha/2), exact complementarity, with the channel-independent bound
certifying the no-recovery side at each swept alpha where it bites.

Part 3 (dissipation bookkeeping, Direction-C entry; NOT a thermodynamic
theorem): T142's erasure-calibration conventions applied to the same family.
Restoring capability in A is a correlated uncopy -- zero Landauer floor, all
handles in-zone. Blind reset of the in-reach holders erases the record
(finite floor, naive 5 ln 2) but restores NO capability: deletion is not
definalization (T144/T145 discipline, computed). In B the in-zone restoration
cost is +infinity by the empty-feasible-set convention -- and the infinity is
typed precisely: the limiting resource is ACCESS to the escaped holder, not
work; no work parameter exists in this closed unitary model to diverge. The
genuine open-system bound (bath dispersion, work/entropy scaling with bath
contact) is T393's named Tier-2 card, NOT built here.

WHAT THIS DOES NOT EARN: no thermodynamic theorem, no hardware or platform,
no claim promotion, no Q1C movement; ledger actions pause for Joe per
AGENTS.md.

Register order (index-sorted, MSB first):
    S, M, F1, F2, F3, F4, AX, C0, C1, C2   (10 qubits, exact statevector)
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T392 primitives (exact statevector machinery; all take an explicit n).
# project_qubit is imported for provenance but replaced below by a
# reshape-based projector (T392's builds a dense 2^n x 2^n matrix per call,
# prohibitive at n = 10; the local one is numerically identical).
from models.fixed_sbs_key_reversal_divergence import (
    THETA,
    V_STAR,
    _HADAMARD,
    project_qubit as _t392_project_qubit,  # noqa: F401  (provenance)
    reduced_density_matrix,
    z_distribution,
    zero_state,
)

# T393 machinery reused by import: the certificate phase sweep (includes
# incommensurate phases), the uniform locking grid, the generic qubit-subset
# applicator, Haar sampling, and the trace norm used by the channel bound.
from models.causal_forcing_access_asymmetry import (
    PHI_CERT,
    PHI_LOCK_GRID,
    _trace_norm,
    apply_on_qubits,
    haar_unitary,
)

# T142 conventions for the Part-3 ledger (dimensionless beta*W >= bits*ln2).
from models.thermodynamic_erasure_calibration import (
    LANDAUER_NAT_PER_BIT,
    landauer_bound_bits,
)

# --------------------------------------------------------------------------- #
# Register layout, geometry, predeclared constants
# --------------------------------------------------------------------------- #

S, M, F1, F2, F3, F4, AX, C0, C1, C2 = range(10)
N_QUBITS = 10
FRAGMENT_QUBITS = (F1, F2, F3, F4)
CHAIN_QUBITS = (C0, C1, C2)

# The record region: where basis-free flatness is asserted (operator level).
RECORD_REGION = (S, M, F1, F2, F3, F4)
R_ACTIVE = (S, F1, F2, F3, F4)  # record region minus the measured meter

# The accessible zone: the ONE fixed menu support, identical for every
# preparation. T393's r = 1 convention: chain sites 0..1 in reach, C2 out.
ACCESS_ZONE = (S, M, F1, F2, F3, F4, AX, C0, C1)
Z_ACTIVE = (S, F1, F2, F3, F4, AX, C0, C1)  # zone minus the measured meter
ESCAPED = (C2,)

# In-reach record holders (the correlated-uncopy handle set for prep A).
HOLDERS_IN_REACH = (F1, F2, F3, F4, AX)

N_STEPS = 2  # discrete lightcone: emitted content sits at C2 after 2 steps

# Part-2 sweep: T393's alphas plus low-amplitude anchors and the near-critical
# 0.7 pi point. alpha = 0 is prep A exactly; alpha = pi is the exact copy.
ALPHA_SWEEP = tuple(
    f * math.pi for f in (0.0, 0.25, 0.5, 0.7, 0.75, 0.9, 0.98, 1.0)
)

VIS_A_ANALYTIC = 4.0 * math.sqrt(3.0) / 7.0  # T392/T393's 0.98974...
ALPHA_FEASIBLE_ANALYTIC = 2.0 * math.acos(V_STAR / VIS_A_ANALYTIC)

HAAR_SAMPLES = 15
HAAR_SEED = 20260702
HAAR_VISIBILITY_CEILING = 0.05
RANDOM_BASIS_SAMPLES = 20
RANDOM_BASIS_SEED = 20260703

FLATNESS_TOL = 1e-12
INFINITE_COST = math.inf

VERDICT_RECOVERABLE = "recoverable-in-access-zone"
VERDICT_FINAL = "final-relative-to-access-zone"
VERDICT_TAGS = (
    "basis_free_flat_pair",
    "menu_support_obstruction",
    "graded_flat_curve",
    "dissipation_bookkeeping_only",
    "no_claim_promotion",
)

# --------------------------------------------------------------------------- #
# Small exact gates, applied via T393's generic qubit-subset applicator
# --------------------------------------------------------------------------- #

_EYE2 = np.eye(2, dtype=complex)
_PAULI_X2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
_SWAP4 = np.array(
    [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ],
    dtype=complex,
)


def _ry(theta: float) -> np.ndarray:
    c, s = math.cos(theta / 2.0), math.sin(theta / 2.0)
    return np.array([[c, -s], [s, c]], dtype=complex)


def _phase_gate(phi: float) -> np.ndarray:
    return np.array([[1.0, 0.0], [0.0, np.exp(1j * phi)]], dtype=complex)


def _controlled(gate: np.ndarray) -> np.ndarray:
    out = np.eye(4, dtype=complex)
    out[2:, 2:] = gate
    return out


_CNOT4 = _controlled(_PAULI_X2)
_CRY_THETA4 = _controlled(_ry(THETA))


def _apply(vec: np.ndarray, gate: np.ndarray, targets) -> np.ndarray:
    return apply_on_qubits(vec, gate, list(targets), N_QUBITS)


def project_qubit(vec: np.ndarray, qubit: int, value: int, n: int = N_QUBITS):
    """Reshape-based projector, numerically identical to T392's
    ``project_qubit`` (asserted in the test suite) but without building a
    dense 2^n x 2^n matrix per call."""
    tensor = np.moveaxis(vec.reshape([2] * n), qubit, 0).copy()
    tensor[1 - value] = 0.0
    out = np.moveaxis(tensor, 0, qubit).reshape(2 ** n)
    prob = float(np.real(out.conj() @ out))
    if prob > 1e-15:
        out = out / math.sqrt(prob)
    return prob, out


_COND_CACHE: dict = {}


def _conditioned(
    kind: str, s_phase: float, m_outcome: int, steps: int, alpha: float | None
):
    """Cached M-conditioned statevector (the object every undo acts on)."""
    key = (
        kind,
        float(s_phase),
        int(m_outcome),
        int(steps),
        None if alpha is None else float(alpha),
    )
    if key not in _COND_CACHE:
        psi = prepare(kind, s_phase=s_phase, steps=steps, alpha=alpha)
        _COND_CACHE[key] = project_qubit(psi, M, m_outcome, N_QUBITS)
    return _COND_CACHE[key]


# --------------------------------------------------------------------------- #
# Preparations
# --------------------------------------------------------------------------- #

_STATE_CACHE: dict = {}


def prepare(
    kind: str, s_phase: float = 0.0, steps: int = N_STEPS, alpha: float | None = None
) -> np.ndarray:
    """Exact statevector for a named preparation after ``steps`` lightcone steps.

    Shared core (EVERY preparation, identical couplings): S in
    (|0> + e^{i s_phase}|1>)/sqrt(2); controlled-Ry(theta) S -> M; CNOT
    Z-copies S -> F1..F4; annex copy CNOT F4 -> AX. The annex copy is the
    same physical record-copy event in A and B -- what differs is only what
    happens OUTSIDE the record region afterwards.

    ``A``       carrier retained: nothing is emitted onto the chain.
    ``B``       carrier leaks: controlled-Ry(alpha) AX -> C0 (T393's partial
                emission; alpha = pi writes the exact Z-copy since C0 starts
                in |0>), then the identical propagation.
    ``Bprime``  emission null control: X on C0, an excitation UNCORRELATED
                with the record, then the identical propagation.
    ``A_tail`` / ``B_tail``  obstruction-lemma witnesses: A (resp. B at the
                default alpha) followed by a unitary on the ESCAPED tail C2
                only -- outside the menu support, so the zone family is
                untouched and every menu value must be identical.

    Propagation (identical circuit for every preparation): SWAP(C0, C1) at
    step 1, SWAP(C1, C2) at step 2 -- T393's discrete lightcone, one site
    per step.
    """
    key = (kind, float(s_phase), int(steps), None if alpha is None else float(alpha))
    if key in _STATE_CACHE:
        return _STATE_CACHE[key]

    psi = zero_state(N_QUBITS)
    psi = _apply(psi, _HADAMARD, [S])
    if s_phase != 0.0:
        psi = _apply(psi, _phase_gate(s_phase), [S])
    psi = _apply(psi, _CRY_THETA4, [S, M])
    for frag in FRAGMENT_QUBITS:
        psi = _apply(psi, _CNOT4, [S, frag])
    psi = _apply(psi, _CNOT4, [F4, AX])  # annex copy: identical in A and B

    if kind in ("A", "A_tail"):
        pass
    elif kind in ("B", "B_tail"):
        a = math.pi if alpha is None else float(alpha)
        psi = _apply(psi, _controlled(_ry(a)), [AX, C0])
    elif kind == "Bprime":
        psi = _apply(psi, _PAULI_X2, [C0])
    else:
        raise ValueError(f"unknown preparation {kind!r}")

    for t in range(steps):
        psi = _apply(psi, _SWAP4, [C0, C1] if t == 0 else [C1, C2])

    if kind == "A_tail":
        psi = _apply(psi, _ry(1.234), [C2])
    if kind == "B_tail":
        psi = _apply(psi, _ry(0.777), [C2])

    _STATE_CACHE[key] = psi
    return psi


# --------------------------------------------------------------------------- #
# States, distances, certificates
# --------------------------------------------------------------------------- #

def full_region_state(
    kind: str, s_phase: float = 0.0, steps: int = N_STEPS, alpha: float | None = None
) -> np.ndarray:
    """The FULL record-region state rho_R (meter included, unconditioned).

    This is the object of the basis-free claim: operator equality of rho_R
    implies equality of EVERY POVM on R and of every channel-then-readout
    composition supported on R (trace distance 0 + CPTP contractivity).
    """
    psi = prepare(kind, s_phase=s_phase, steps=steps, alpha=alpha)
    return reduced_density_matrix(psi, list(RECORD_REGION), N_QUBITS)


def conditional_state(
    kind: str,
    s_phase: float,
    active,
    m_outcome: int = 0,
    steps: int = N_STEPS,
    alpha: float | None = None,
) -> np.ndarray:
    """Reduced state on ``active`` given the meter outcome."""
    prob, conditioned = _conditioned(kind, s_phase, m_outcome, steps, alpha)
    if prob <= 1e-15:
        raise ValueError(f"meter outcome {m_outcome} has zero probability")
    return reduced_density_matrix(conditioned, list(active), N_QUBITS)


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho - sigma)
    return float(0.5 * np.sum(np.abs(eig)))


def max_pairwise_phi_diff(
    kind: str,
    active,
    phis=PHI_CERT,
    m_outcome: int = 0,
    steps: int = N_STEPS,
    alpha: float | None = None,
) -> float:
    """Max entrywise difference of M-conditioned states across the phi sweep."""
    rhos = [
        conditional_state(kind, phi, active, m_outcome, steps, alpha) for phi in phis
    ]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def channel_bound(
    kind: str,
    active=Z_ACTIVE,
    steps: int = N_STEPS,
    alpha: float | None = None,
    grid=PHI_LOCK_GRID,
) -> float:
    """T393's channel-independent upper bound on the phase-locked visibility
    of ANY channel supported on ``active``: 2 (||Re X||_1 + ||Im X||_1) with
    X = mean_phi e^{i phi} rho_active|M=0(phi), by Hoelder plus CPTP
    trace-norm contractivity. Covers every channel at once, no enumeration.
    """
    dim = 2 ** len(active)
    X_op = np.zeros((dim, dim), dtype=complex)
    for phi in grid:
        X_op = X_op + np.exp(1j * phi) * conditional_state(
            kind, phi, active, 0, steps, alpha
        )
    X_op = X_op / len(grid)
    herm = (X_op + X_op.conj().T) / 2.0
    anti = (X_op - X_op.conj().T) / 2.0j
    return 2.0 * (_trace_norm(herm) + _trace_norm(anti))


# --------------------------------------------------------------------------- #
# Undo protocols (all supported on the accessible zone unless stated)
# --------------------------------------------------------------------------- #

def holder_undo(subset):
    """Inverse couplings for a subset of the in-reach record holders.

    Declared order: annex uncopy first (CNOT F4 -> AX, while F4 still holds
    the record), then fragment uncopies in index order.
    """

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = vec
        if AX in subset:
            out = _apply(out, _CNOT4, [F4, AX])
        for frag in FRAGMENT_QUBITS:
            if frag in subset:
                out = _apply(out, _CNOT4, [S, frag])
        return out

    return _undo


EXTENDED_UNDO = holder_undo(HOLDERS_IN_REACH)


def window_undo(step: int, alpha: float | None = None):
    """Best in-zone undo for prep B at lightcone time ``step``.

    Every operation is supported on the accessible zone: C0, C1 are in-zone
    chain sites. At step >= 2 no in-zone operation reaches the escaped site,
    so the protocol degrades to the extended undo alone (and the certificate
    proves nothing in-zone can do better).
    """
    a = math.pi if alpha is None else float(alpha)

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = vec
        if step == 1:
            out = _apply(out, _SWAP4, [C0, C1])  # pull the mode back (in-zone)
        if step <= 1:
            out = _apply(out, _controlled(_ry(-a)), [AX, C0])  # un-leak (in-zone)
        out = _apply(out, _CNOT4, [F4, AX])
        for frag in FRAGMENT_QUBITS:
            out = _apply(out, _CNOT4, [S, frag])
        return out

    return _undo


def enlarged_undo(alpha: float | None = None):
    """Counterfactual undo including the ESCAPED site C2 (NOT in-zone).

    Region-boundary sanity check only, never an admissible protocol.
    """
    a = math.pi if alpha is None else float(alpha)

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = _apply(vec, _SWAP4, [C1, C2])
        out = _apply(out, _SWAP4, [C0, C1])
        out = _apply(out, _controlled(_ry(-a)), [AX, C0])
        out = _apply(out, _CNOT4, [F4, AX])
        for frag in FRAGMENT_QUBITS:
            out = _apply(out, _CNOT4, [S, frag])
        return out

    return _undo


def blind_reset_channel(holders):
    """T142's blind-reset mode as a channel: each holder is measured in Z and
    reset to |0> WITHOUT using the source-copy correlation as an uncopy
    handle. Kraus branches: {P0, X P1} per holder. Supported on the zone.
    """

    def _channel(vec: np.ndarray) -> list:
        branches = [vec]
        for h in holders:
            new_branches = []
            p0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
            p1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
            for b in branches:
                new_branches.append(_apply(b, p0, [h]))
                new_branches.append(_apply(_apply(b, p1, [h]), _PAULI_X2, [h]))
            branches = new_branches
        return branches

    return _channel


def manufactured_coherence_undo(vec: np.ndarray) -> np.ndarray:
    """T392's disclosed raw-visibility exploit (CNOT F1 -> S then H on S):
    manufactures raw coherence carrying zero information about the prepared
    phase. Why the figure of merit is phase-locked."""
    out = _apply(vec, _CNOT4, [F1, S])
    return _apply(out, _HADAMARD, [S])


# --------------------------------------------------------------------------- #
# Figures of merit
# --------------------------------------------------------------------------- #

def locked_visibility(
    kind: str,
    undo_fn,
    m_outcome: int = 0,
    steps: int = N_STEPS,
    alpha: float | None = None,
    grid=PHI_LOCK_GRID,
) -> float:
    """Phase-locked conditional X-visibility |mean_phi e^{i phi} 2 rho_S[0,1]|
    (T392/T393's recovery figure of merit; nulls manufactured coherence)."""
    total = 0.0 + 0.0j
    for phi in grid:
        prob, conditioned = _conditioned(kind, phi, m_outcome, steps, alpha)
        if prob <= 1e-15:
            return 0.0
        out = undo_fn(conditioned)
        if isinstance(out, list):  # Kraus branches (non-unitary channel)
            rho_s = sum(
                reduced_density_matrix(branch, [S], N_QUBITS) for branch in out
            )
        else:
            rho_s = reduced_density_matrix(out, [S], N_QUBITS)
        total += np.exp(1j * phi) * 2.0 * rho_s[0, 1]
    return float(abs(total / len(grid)))


def raw_visibility(
    kind: str,
    undo_fn,
    m_outcome: int = 0,
    steps: int = N_STEPS,
    alpha: float | None = None,
    s_phase: float = 0.0,
) -> float:
    """Raw (phase-blind) visibility after an undo, disclosure column only."""
    prob, conditioned = _conditioned(kind, s_phase, m_outcome, steps, alpha)
    if prob <= 1e-15:
        return 0.0
    out = undo_fn(conditioned)
    if isinstance(out, list):
        rho_s = sum(reduced_density_matrix(branch, [S], N_QUBITS) for branch in out)
    else:
        rho_s = reduced_density_matrix(out, [S], N_QUBITS)
    return float(2.0 * abs(rho_s[0, 1]))


def reversal_cost(kind: str, alpha: float | None = None, v_star: float = V_STAR):
    """Minimal in-reach holder subset size achieving locked visibility >= v*
    (protocol family: subsets of the five inverse couplings). Infinity on the
    B side is grounded in the all-channel certificate, not the family."""
    from itertools import combinations

    for k in range(len(HOLDERS_IN_REACH) + 1):
        for subset in combinations(HOLDERS_IN_REACH, k):
            if locked_visibility(kind, holder_undo(subset), alpha=alpha) >= v_star:
                return float(k)
    return INFINITE_COST


def verdict_from_cost(h_value: float) -> str:
    return VERDICT_FINAL if math.isinf(h_value) else VERDICT_RECOVERABLE


# --------------------------------------------------------------------------- #
# Part 1 -- basis-free flat pair
# --------------------------------------------------------------------------- #

def region_flatness_report() -> dict:
    """Operator equality of the full region state rho_R across preparations,
    phases, lightcone steps, and leak amplitudes; plus the basis-free
    consequences and the illustrative random-basis spot check."""
    max_op_diff = 0.0
    max_tr_dist = 0.0
    for phi in PHI_CERT:
        rho_a = full_region_state("A", phi)
        for kind, alpha in (
            ("B", None),
            ("Bprime", None),
            *[("B", a) for a in ALPHA_SWEEP],
        ):
            rho_other = full_region_state(kind, phi, alpha=alpha)
            max_op_diff = max(max_op_diff, float(np.max(np.abs(rho_a - rho_other))))
            max_tr_dist = max(max_tr_dist, trace_distance(rho_a, rho_other))

    # Flatness at every lightcone step (the difference is outside R at all
    # times, not only at the final one).
    step_diff = 0.0
    for step in range(N_STEPS + 1):
        for phi in PHI_CERT[:3]:
            step_diff = max(
                step_diff,
                float(
                    np.max(
                        np.abs(
                            full_region_state("A", phi, steps=step)
                            - full_region_state("B", phi, steps=step)
                        )
                    )
                ),
            )

    # rho_R is also phi-independent WITHIN each preparation: the annex copy
    # already dephases the record region completely (disclosure).
    phi_flat_a = _phi_flatness_of_region("A")
    phi_flat_b = _phi_flatness_of_region("B")

    # Conditional version (M = 0) on the active record region.
    cond_diff = 0.0
    for phi in PHI_CERT:
        cond_diff = max(
            cond_diff,
            float(
                np.max(
                    np.abs(
                        conditional_state("A", phi, R_ACTIVE)
                        - conditional_state("B", phi, R_ACTIVE)
                    )
                )
            ),
        )

    # Illustrative random-basis spot check (the operator equality is the
    # proof; this is belt-and-suspenders in 20 Haar-random bases on R).
    rng = np.random.default_rng(RANDOM_BASIS_SEED)
    dim = 2 ** len(RECORD_REGION)
    basis_diff = 0.0
    rho_a0 = full_region_state("A", 1.0)
    rho_b0 = full_region_state("B", 1.0)
    for _ in range(RANDOM_BASIS_SAMPLES):
        U = haar_unitary(dim, rng)
        pa = np.real(np.diag(U @ rho_a0 @ U.conj().T))
        pb = np.real(np.diag(U @ rho_b0 @ U.conj().T))
        basis_diff = max(basis_diff, float(np.max(np.abs(pa - pb))))

    # Declared Z-readout over R (house convention), equal a fortiori.
    z_diff = 0.0
    for phi in PHI_CERT[:3]:
        da = z_distribution(prepare("A", phi), list(RECORD_REGION), N_QUBITS)
        db = z_distribution(prepare("B", phi), list(RECORD_REGION), N_QUBITS)
        for k in set(da) | set(db):
            z_diff = max(z_diff, abs(da.get(k, 0.0) - db.get(k, 0.0)))

    return {
        "max_operator_diff_over_preps_phases_alphas": max_op_diff,
        "max_trace_distance": max_tr_dist,
        "max_operator_diff_per_step": step_diff,
        "conditional_R_active_diff": cond_diff,
        "phi_flatness_within_A": phi_flat_a,
        "phi_flatness_within_B": phi_flat_b,
        "random_basis_spot_check": {
            "samples": RANDOM_BASIS_SAMPLES,
            "seed": RANDOM_BASIS_SEED,
            "max_prob_diff": basis_diff,
            "note": "illustrative; the operator equality carries the claim",
        },
        "declared_z_readout_diff": z_diff,
        "flat": max_op_diff < FLATNESS_TOL
        and max_tr_dist < FLATNESS_TOL
        and step_diff < FLATNESS_TOL
        and cond_diff < FLATNESS_TOL,
    }


def _phi_flatness_of_region(kind: str) -> float:
    rhos = [full_region_state(kind, phi) for phi in PHI_CERT]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def capability_report() -> dict:
    """The capability split under the one fixed zone menu, with the A-side
    protocol, the B-side all-channel certificates, and the R-only null."""
    vis_a = locked_visibility("A", EXTENDED_UNDO)
    vis_b = locked_visibility("B", EXTENDED_UNDO)

    # R-only menu null: on the record region alone BOTH preparations are
    # certified unrecoverable -- the annex copy finalizes relative to R.
    r_cert_a = max_pairwise_phi_diff("A", R_ACTIVE)
    r_cert_b = max_pairwise_phi_diff("B", R_ACTIVE)
    r_bound_a = channel_bound("A", active=R_ACTIVE)
    r_bound_b = channel_bound("B", active=R_ACTIVE)

    # Zone certificates: B is phi-independent on the FULL menu support
    # (all-channel impossibility); A is genuinely phi-dependent (teeth).
    z_cert_b = max_pairwise_phi_diff("B", Z_ACTIVE)
    z_cert_a = max_pairwise_phi_diff("A", Z_ACTIVE)
    z_bound_b = channel_bound("B", active=Z_ACTIVE)
    z_bound_a = channel_bound("A", active=Z_ACTIVE)

    # Haar spot check on the zone (illustrative only).
    rng = np.random.default_rng(HAAR_SEED)
    dim = 2 ** len(Z_ACTIVE)
    haar_max = 0.0
    for _ in range(HAAR_SAMPLES):
        U = haar_unitary(dim, rng)
        undo = lambda vec: apply_on_qubits(vec, U, list(Z_ACTIVE), N_QUBITS)  # noqa: E731
        haar_max = max(haar_max, locked_visibility("B", undo))

    manufactured = {
        "raw_visibility": raw_visibility("B", manufactured_coherence_undo),
        "locked_visibility": locked_visibility("B", manufactured_coherence_undo),
    }

    h_a = reversal_cost("A")
    h_b = reversal_cost("B")

    # Every proper holder subset fails for A (all five holders needed).
    from itertools import combinations

    best_four = max(
        locked_visibility("A", holder_undo(sub))
        for sub in combinations(HOLDERS_IN_REACH, 4)
    )

    return {
        "vis_A_locked": vis_a,
        "vis_A_analytic": VIS_A_ANALYTIC,
        "vis_B_locked": vis_b,
        "capability_gap": vis_a - vis_b,
        "r_only_null": {
            "cert_A": r_cert_a,
            "cert_B": r_cert_b,
            "bound_A": r_bound_a,
            "bound_B": r_bound_b,
        },
        "zone_cert_B": z_cert_b,
        "zone_cert_A_teeth": z_cert_a,
        "zone_bound_B": z_bound_b,
        "zone_bound_A_sanity": z_bound_a,
        "haar_spot_check": {
            "samples": HAAR_SAMPLES,
            "seed": HAAR_SEED,
            "max_locked_visibility": haar_max,
        },
        "manufactured_coherence_control": manufactured,
        "H_A": h_a,
        "H_B": h_b,
        "best_four_holder_visibility_A": best_four,
        "verdict_A": verdict_from_cost(h_a),
        "verdict_B": verdict_from_cost(h_b),
    }


def bprime_report() -> dict:
    """Emission null: B' emits a REAL uncorrelated excitation; capability and
    region state must match A exactly."""
    vis_bp = locked_visibility("Bprime", EXTENDED_UNDO)
    vis_a = locked_visibility("A", EXTENDED_UNDO)
    reg_diff = 0.0
    for phi in PHI_CERT[:3]:
        reg_diff = max(
            reg_diff,
            float(
                np.max(
                    np.abs(full_region_state("A", phi) - full_region_state("Bprime", phi))
                )
            ),
        )
    return {
        "vis_Bprime_locked": vis_bp,
        "abs_diff_from_A": abs(vis_bp - vis_a),
        "region_state_diff_from_A": reg_diff,
        "chain_excitation": {k: chain_excitation(k) for k in ("A", "B", "Bprime")},
    }


def chain_excitation(kind: str, alpha: float | None = None) -> float:
    psi = prepare(kind, alpha=alpha)
    total = 0.0
    for site in CHAIN_QUBITS:
        rho = reduced_density_matrix(psi, [site], N_QUBITS)
        total += float(np.real(rho[1, 1]))
    return total


def recovery_window_report() -> dict:
    """In-zone recovery of prep B per lightcone step, plus the counterfactual
    boundary enlargement (T393's window physics on the flat family)."""
    window = {}
    for step in range(N_STEPS + 1):
        window[step] = {
            "locked_visibility_in_zone_undo": locked_visibility(
                "B", window_undo(step), steps=step
            ),
            "zone_cert_diff": max_pairwise_phi_diff("B", Z_ACTIVE, steps=step),
        }
    vis_a = locked_visibility("A", EXTENDED_UNDO)
    vis_enlarged = locked_visibility("B", enlarged_undo())
    enlarged_active = list(Z_ACTIVE) + [C2]
    return {
        "window": window,
        "enlarged_locked_visibility_B": vis_enlarged,
        "abs_diff_from_A": abs(vis_enlarged - vis_a),
        "enlarged_cert_diff_B": max_pairwise_phi_diff("B", enlarged_active),
    }


def obstruction_report() -> dict:
    """The menu-support obstruction lemma, witnessed.

    LEMMA (why a fully flat pair with a gap is impossible): every menu value
    is a functional of the phi-indexed conditional state family on the menu
    support Z. If two preparations have EQUAL zone families, every menu value
    is equal. Witnessed by the tail-unitary pairs (A, A_tail) and (B, B_tail):
    the tail unitary acts only on the escaped site, the zone family is
    identical to machine precision, and the full capability column computes
    identical. CONVERSELY the artifact's main pair is flat on R but NOT on Z
    -- the statistical trace of the capability difference is real, located in
    zone coherences, and (disclosure) invisible even to the full joint
    Z-basis readout on the zone.
    """
    # Tail witnesses: zone family equal, capability column equal.
    tail = {}
    for base, tailed in (("A", "A_tail"), ("B", "B_tail")):
        zone_diff = 0.0
        for phi in PHI_CERT[:3]:
            zone_diff = max(
                zone_diff,
                float(
                    np.max(
                        np.abs(
                            conditional_state(base, phi, Z_ACTIVE)
                            - conditional_state(tailed, phi, Z_ACTIVE)
                        )
                    )
                ),
            )
        tail[base] = {
            "zone_family_diff": zone_diff,
            "vis_diff": abs(
                locked_visibility(base, EXTENDED_UNDO)
                - locked_visibility(tailed, EXTENDED_UNDO)
            ),
            "bound_diff": abs(
                channel_bound(base) - channel_bound(tailed)
            ),
            "H_base": reversal_cost(base),
            "H_tail": reversal_cost(tailed),
        }

    # Where the statistical trace of the A/B difference lives (disclosures).
    zone_tr = max(
        trace_distance(
            conditional_state("A", phi, Z_ACTIVE),
            conditional_state("B", phi, Z_ACTIVE),
        )
        for phi in PHI_CERT[:3]
    )
    # Joint Z-basis readout over the WHOLE zone: still exactly flat.
    z_joint_diff = 0.0
    for phi in PHI_CERT[:3]:
        da = z_distribution(prepare("A", phi), list(ACCESS_ZONE), N_QUBITS)
        db = z_distribution(prepare("B", phi), list(ACCESS_ZONE), N_QUBITS)
        for k in set(da) | set(db):
            z_joint_diff = max(z_joint_diff, abs(da.get(k, 0.0) - db.get(k, 0.0)))
    # Single-qubit marginals on the zone: flat too.
    marg_diff = 0.0
    psi_a = prepare("A", 1.0)
    psi_b = prepare("B", 1.0)
    for q in ACCESS_ZONE:
        ra = reduced_density_matrix(psi_a, [q], N_QUBITS)
        rb = reduced_density_matrix(psi_b, [q], N_QUBITS)
        marg_diff = max(marg_diff, float(np.max(np.abs(ra - rb))))

    return {
        "tail_witnesses": tail,
        "zone_trace_distance_A_vs_B": zone_tr,
        "zone_joint_z_readout_diff": z_joint_diff,
        "zone_single_qubit_marginal_diff": marg_diff,
        "lemma": (
            "capability under a menu supported on Z is a functional of the "
            "phi-indexed conditional state family on Z; operator flatness on "
            "the FULL menu support therefore forces zero capability gap. The "
            "flat surface is maximal at the complement of the menu support: "
            "flat-on-R with a certified gap is constructed, flat-on-Z with a "
            "gap is impossible, and the trace the gap requires lives in zone "
            "coherences invisible to R and to every Z-basis readout on Z."
        ),
    }


# --------------------------------------------------------------------------- #
# Part 2 -- graded curve (T393 alpha machinery on the flat family)
# --------------------------------------------------------------------------- #

def graded_report() -> dict:
    """The capability boundary as a graded physical curve.

    Per swept alpha: rho_R stays operator-flat (the whole curve is one
    basis-free flat family); the extended undo achieves
    cos(alpha/2) * 4sqrt(3)/7 exactly; the escaped holder's branch
    distinguishability is sin(alpha/2); the two satisfy exact
    complementarity; and the channel-independent bound certifies the
    no-recovery side wherever it bites (bound < v*).
    """
    vis_a = locked_visibility("A", EXTENDED_UNDO)
    rows = []
    for alpha in ALPHA_SWEEP:
        achieved = locked_visibility("B", EXTENDED_UNDO, alpha=alpha)
        analytic = math.cos(alpha / 2.0) * vis_a
        bound = channel_bound("B", alpha=alpha)
        region_diff = max(
            float(
                np.max(
                    np.abs(
                        full_region_state("A", phi)
                        - full_region_state("B", phi, alpha=alpha)
                    )
                )
            )
            for phi in PHI_CERT[:3]
        )
        escaped = escaped_holder_report(alpha)
        if achieved >= V_STAR:
            status = "feasible_zero_cost"
        elif bound < V_STAR:
            status = "certified_infeasible"
        else:
            status = "undetermined_by_bound"
        rows.append(
            {
                "alpha_over_pi": alpha / math.pi,
                "emission_probability": math.sin(alpha / 2.0) ** 2,
                "region_flatness_diff": region_diff,
                "achieved_locked_visibility": achieved,
                "analytic_cos_half_alpha_times_vis_A": analytic,
                "channel_bound_zone": bound,
                "capability_gap": vis_a - achieved,
                "escaped_distinguishability": escaped["branch_distinguishability"],
                "escaped_holevo_bits": escaped["holevo_bits"],
                "complementarity_residual": abs(
                    (achieved / vis_a) ** 2
                    + escaped["branch_distinguishability"] ** 2
                    - 1.0
                ),
                "threshold_restoration": status,
            }
        )
    return {
        "v_star": V_STAR,
        "alpha_feasible_analytic": ALPHA_FEASIBLE_ANALYTIC,
        "alpha_feasible_analytic_over_pi": ALPHA_FEASIBLE_ANALYTIC / math.pi,
        "sweep": rows,
        "note": (
            "the bound is not tight in the mid-range; alphas with achieved < "
            "v* <= bound are honestly undetermined by this artifact (T393's "
            "open analytic alpha*(v*) card)"
        ),
    }


def escaped_holder_report(alpha: float | None = None) -> dict:
    """Branch distinguishability and Holevo information of the escaped holder
    C2, conditioned on M = 0 (branch pointer read from F1)."""
    kind = "B"
    _, conditioned = _conditioned(kind, 0.0, 0, N_STEPS, alpha)
    branch_states = []
    branch_probs = []
    for b in (0, 1):
        pb, vec = project_qubit(conditioned, F1, b, N_QUBITS)
        branch_probs.append(pb)
        branch_states.append(reduced_density_matrix(vec, [C2], N_QUBITS))
    dist = trace_distance(branch_states[0], branch_states[1])
    rho_c2 = reduced_density_matrix(conditioned, [C2], N_QUBITS)
    holevo = _vn_entropy_bits(rho_c2) - sum(
        p * _vn_entropy_bits(r) for p, r in zip(branch_probs, branch_states)
    )
    return {
        "branch_probs_given_M0": branch_probs,
        "branch_distinguishability": dist,
        "holevo_bits": holevo,
        "conditional_purity_residual": max(
            _vn_entropy_bits(r) for r in branch_states
        ),
    }


def _vn_entropy_bits(rho: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho)
    eig = eig[eig > 1e-15]
    return float(-np.sum(eig * np.log2(eig)))


# --------------------------------------------------------------------------- #
# Part 3 -- dissipation bookkeeping (T142 conventions; NOT a thermo theorem)
# --------------------------------------------------------------------------- #

def dissipation_ledger() -> dict:
    """Landauer-style bookkeeping on the same family, T142 conventions
    (dimensionless beta*W >= erased_bits * ln 2). Scope: bookkeeping in a
    finite closed unitary model. No bath, no temperature, no open-system
    dynamics -- NOT a thermodynamic theorem. The genuine bound (bath
    dispersion; work/entropy scaling with bath contact) is T393's named
    Tier-2 card, unbuilt.
    """
    vis_a = locked_visibility("A", EXTENDED_UNDO)

    # Record content of the in-reach holders (they are perfectly correlated
    # copies of ONE branch bit).
    psi_a = prepare("A", s_phase=0.0)
    _, cond_a = _conditioned("A", 0.0, 0, N_STEPS, None)
    joint_bits_cond = _vn_entropy_bits(
        reduced_density_matrix(cond_a, list(HOLDERS_IN_REACH), N_QUBITS)
    )
    joint_bits_uncond = _vn_entropy_bits(
        reduced_density_matrix(psi_a, list(HOLDERS_IN_REACH), N_QUBITS)
    )

    # (a) Restore capability in A: correlated uncopy, all handles in-zone.
    restore_a = {
        "mode": "correlated_uncopy",
        "holders_uncomputed": len(HOLDERS_IN_REACH),
        "erased_bits": 0,
        "beta_work_lower_bound": 0.0,
        "achieved_locked_visibility": vis_a,
        "handles_available_in_zone": True,
        "t142_verdict": "reversible_when_full_microstate_available",
    }

    # Blind-reset disclosure: deletion is NOT definalization. The blind reset
    # erases the in-reach record (finite Landauer floor) but restores NO
    # capability -- computed, not argued.
    reset = blind_reset_channel(HOLDERS_IN_REACH)
    vis_after_reset = locked_visibility("A", reset)
    # Residual record after reset: holder state is |0..0> in every branch.
    _, cond = _conditioned("A", 1.0, 0, N_STEPS, None)
    branch_states = []
    for b in (0, 1):
        _, vec = project_qubit(cond, S, b, N_QUBITS)
        branches = reset(vec)
        rho = sum(
            reduced_density_matrix(br, list(HOLDERS_IN_REACH), N_QUBITS)
            for br in branches
        )
        branch_states.append(rho / np.trace(rho))
    residual_record = trace_distance(branch_states[0], branch_states[1])
    blind_a = {
        "mode": "blind_reset",
        "erased_bits_naive_per_holder": len(HOLDERS_IN_REACH),
        "beta_work_lower_bound_naive": landauer_bound_bits(len(HOLDERS_IN_REACH)),
        "joint_record_bits_given_M0": joint_bits_cond,
        "joint_record_bits_unconditioned": joint_bits_uncond,
        "note_correlation_aware": (
            "the five holders are perfectly correlated copies of one branch "
            "bit; a correlation-aware joint reset floor is the joint record "
            "entropy, not 5 bits -- both are bookkeeping readings of T142's "
            "convention, disclosed side by side"
        ),
        "capability_after_reset": vis_after_reset,
        "record_deleted_residual_distinguishability": residual_record,
        "deletion_is_not_definalization": vis_after_reset < 1e-12
        and residual_record < 1e-12,
        "t142_verdict": "standard_erasure_cost_if_uncopy_unavailable",
    }

    # (b) Restore capability in B within the zone: the feasible set is EMPTY
    # (certified), so the minimal cost is an empty-set infimum.
    restore_b = {
        "feasible_in_zone": False,
        "certificates": {
            "zone_phi_independence": max_pairwise_phi_diff("B", Z_ACTIVE),
            "zone_channel_bound": channel_bound("B"),
        },
        "min_cost_convention": "inf (infimum over an empty feasible set)",
        "min_beta_work": INFINITE_COST,
        "limiting_resource": "access to the escaped holder, not work",
        "not_a_work_bound": (
            "the infinity is NOT a divergent Landauer/work requirement: this "
            "closed unitary model has no work parameter that could diverge; "
            "no channel supported on the zone restores the phase at ANY "
            "resource expenditure (phi-independence certificate). Calling it "
            "a 'cost' is an extended-real bookkeeping convention."
        ),
    }

    # Counterfactual boundary enlargement: with C2 in reach the correlated
    # uncopy of all six holders restores capability at zero erasure floor.
    vis_enlarged = locked_visibility("B", enlarged_undo())
    restore_b_counterfactual = {
        "mode": "correlated_uncopy_with_boundary_enlargement",
        "holders_uncomputed": len(HOLDERS_IN_REACH) + 1,
        "erased_bits": 0,
        "beta_work_lower_bound": 0.0,
        "achieved_locked_visibility": vis_enlarged,
        "abs_diff_from_A": abs(vis_enlarged - vis_a),
        "blind_reset_disclosure_bits": len(HOLDERS_IN_REACH) + 1,
        "blind_reset_beta_work_naive": landauer_bound_bits(
            len(HOLDERS_IN_REACH) + 1
        ),
    }

    # Graded correspondence rows are in graded_report(); here the stated
    # correspondence for this family.
    correspondence = (
        "in this finite family, capability loss and escaped record content "
        "correspond exactly: capability retained cos(alpha/2), escaped-holder "
        "branch distinguishability sin(alpha/2) (complementarity residual "
        "< 1e-9 across the sweep), escaped Holevo content rising 0 -> "
        "h2(3/7) bits; the in-zone restoration ledger is 0 (correlated "
        "uncopy) wherever restoration is feasible and an empty-set infimum "
        "(inf) where certified infeasible; blind-reset dissipation at any "
        "alpha buys record deletion, never capability restoration. "
        "Bookkeeping in a finite model, not a thermodynamic theorem."
    )

    return {
        "landauer_nat_per_bit": LANDAUER_NAT_PER_BIT,
        "restore_A": restore_a,
        "blind_reset_A": blind_a,
        "restore_B_in_zone": restore_b,
        "restore_B_counterfactual": restore_b_counterfactual,
        "correspondence": correspondence,
        "tier2_card": (
            "open-system bath dispersion: undo cost scaling with bath "
            "contact (work/entropy of coherent recollection vs bath size) -- "
            "T393's Tier-2, Direction-C-facing, NOT built here"
        ),
    }


# --------------------------------------------------------------------------- #
# Guardrails (Q1D asserted numerically; R1 untouched)
# --------------------------------------------------------------------------- #

def q1d_report() -> dict:
    """No-signalling surfaces, asserted numerically with teeth."""
    # Declared readout invariance (subsumed by flatness; asserted directly).
    z_pref = z_distribution(prepare("A", 0.0), list(RECORD_REGION), N_QUBITS)

    def _zdiff(kind, phi, alpha=None):
        d = z_distribution(
            prepare(kind, phi, alpha=alpha), list(RECORD_REGION), N_QUBITS
        )
        return max(
            abs(z_pref.get(k, 0.0) - d.get(k, 0.0)) for k in set(z_pref) | set(d)
        )

    readout_invariance = max(
        [_zdiff("A", 1.0), _zdiff("B", math.sqrt(2.0)), _zdiff("Bprime", 0.0)]
        + [_zdiff("B", 0.0, alpha=a) for a in ALPHA_SWEEP[:4]]
    )

    # No signalling OUT of the zone: an in-zone undo cannot move the escaped
    # marginal; the counterfactual enlarged undo does (teeth).
    _, cond = _conditioned("B", 1.0, 0, N_STEPS, None)
    rho_c2_before = reduced_density_matrix(cond, [C2], N_QUBITS)
    rho_c2_in_zone = reduced_density_matrix(EXTENDED_UNDO(cond), [C2], N_QUBITS)
    rho_c2_enlarged = reduced_density_matrix(enlarged_undo()(cond), [C2], N_QUBITS)

    zone_teeth = max(
        trace_distance(
            conditional_state("A", phi, Z_ACTIVE),
            conditional_state("B", phi, Z_ACTIVE),
        )
        for phi in PHI_CERT[:3]
    )

    return {
        "declared_readout_invariance": readout_invariance,
        "no_signal_out_in_zone_undo": float(
            np.max(np.abs(rho_c2_before - rho_c2_in_zone))
        ),
        "enlarged_undo_moves_escaped_marginal_teeth": float(
            np.max(np.abs(rho_c2_before - rho_c2_enlarged))
        ),
        "zone_trace_distance_teeth": zone_teeth,
        "r1_note": (
            "R1 untouched: no claim about global temporal order or "
            "spacetime; the discrete SWAP-chain lightcone carries T393/T379's "
            "own caveats"
        ),
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

_ANALYSIS_CACHE: dict = {}


def run_analysis() -> dict:
    flatness = region_flatness_report()
    capability = capability_report()
    bprime = bprime_report()
    window = recovery_window_report()
    obstruction = obstruction_report()
    graded = graded_report()
    ledger = dissipation_ledger()
    q1d = q1d_report()

    statuses = [row["threshold_restoration"] for row in graded["sweep"]]
    holds = (
        flatness["flat"]
        and capability["vis_A_locked"] >= V_STAR
        and capability["vis_B_locked"] <= 1e-12
        and capability["zone_cert_B"] < FLATNESS_TOL
        and capability["zone_bound_B"] < V_STAR
        and capability["zone_cert_A_teeth"] > 0.1
        and capability["r_only_null"]["cert_A"] < FLATNESS_TOL
        and capability["r_only_null"]["cert_B"] < FLATNESS_TOL
        and math.isfinite(capability["H_A"])
        and math.isinf(capability["H_B"])
        and bprime["abs_diff_from_A"] < 1e-12
        and bprime["region_state_diff_from_A"] < FLATNESS_TOL
        and window["window"][0]["locked_visibility_in_zone_undo"] >= V_STAR
        and window["window"][1]["locked_visibility_in_zone_undo"] >= V_STAR
        and window["window"][2]["locked_visibility_in_zone_undo"] <= 1e-12
        and window["abs_diff_from_A"] < 1e-12
        and all(
            t["zone_family_diff"] < FLATNESS_TOL and t["vis_diff"] < 1e-12
            for t in obstruction["tail_witnesses"].values()
        )
        and obstruction["zone_trace_distance_A_vs_B"] > 0.1
        and all(
            row["region_flatness_diff"] < FLATNESS_TOL
            and row["complementarity_residual"] < 1e-9
            for row in graded["sweep"]
        )
        and "feasible_zero_cost" in statuses
        and "certified_infeasible" in statuses
        and ledger["blind_reset_A"]["deletion_is_not_definalization"]
        and not ledger["restore_B_in_zone"]["feasible_in_zone"]
    )

    if holds:
        verdict_language = (
            "the basis-free flat pair holds in this finite family: two "
            "preparations with EXACTLY identical full region states (every "
            "POVM on R equal, every R-supported intervention statistic "
            "equal) split on capability under one fixed accessible-zone "
            "menu, with the zero side certified against all zone channels; "
            "the split is sourced in whether the annex record carrier "
            "escaped the causal boundary, so T407's statistics-flatness is "
            "upgraded from declared-readout-relative to operator-level, and "
            "the residual boundary is the menu support itself (obstruction "
            "lemma: flat-on-menu-support forces no gap). Graded alpha "
            "family sits on one flat surface; dissipation ledger is "
            "bookkeeping only. No claim promotion; decisions pause for Joe."
        )
    else:
        verdict_language = (
            "the basis-free flat pair FAILS in this finite family: either "
            "exact region flatness could not coexist with a certified "
            "capability gap (the T407-noted obstruction would then extend "
            "to the record region: capability difference requires an "
            "in-region statistical trace), or a certificate failed. Report "
            "the failing check; do not weaken assertions to pass."
        )

    return {
        "artifact": "T408-basis-free-capability-boundary-v0.1",
        "labeling_convention": (
            "registers index-sorted (S, M, F1, F2, F3, F4, AX, C0, C1, C2); "
            "all distributions keyed in this order"
        ),
        "theta": THETA,
        "v_star": V_STAR,
        "region": {
            "record_region": ["S", "M", "F1", "F2", "F3", "F4"],
            "access_zone": [
                "S",
                "M",
                "F1",
                "F2",
                "F3",
                "F4",
                "AX",
                "C0",
                "C1",
            ],
            "escaped": ["C2"],
            "n_steps": N_STEPS,
        },
        "flatness": flatness,
        "capability": capability,
        "bprime": bprime,
        "window": window,
        "obstruction": obstruction,
        "graded": graded,
        "ledger": ledger,
        "q1d": q1d,
        "verdict_tags": list(VERDICT_TAGS),
        "physicalization_holds": holds,
        "verdict_language": verdict_language,
    }


def cached_analysis() -> dict:
    if "res" not in _ANALYSIS_CACHE:
        _ANALYSIS_CACHE["res"] = run_analysis()
    return _ANALYSIS_CACHE["res"]


def _json_safe(obj):
    if isinstance(obj, dict):
        return {str(k): _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_json_safe(v) for v in obj]
    if isinstance(obj, float) and math.isinf(obj):
        return "inf"
    if isinstance(obj, (np.floating, np.integer)):
        return float(obj)
    return obj


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(_json_safe(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T408 Basis-Free Flat Pair / Physical Capability Boundary")
    print("=" * 70)
    fl = res["flatness"]
    cap = res["capability"]
    print(f"rho_R operator diff (all preps/phases/alphas): "
          f"{fl['max_operator_diff_over_preps_phases_alphas']:.3e}")
    print(f"rho_R trace distance (max):                    "
          f"{fl['max_trace_distance']:.3e}")
    print(f"random-basis spot check (max prob diff):       "
          f"{fl['random_basis_spot_check']['max_prob_diff']:.3e}")
    print(f"vis A / B (locked, zone menu):                 "
          f"{cap['vis_A_locked']:.6f} / {cap['vis_B_locked']:.3e}")
    print(f"zone cert B / bound B:                         "
          f"{cap['zone_cert_B']:.3e} / {cap['zone_bound_B']:.3e}")
    print(f"R-only null (cert A / cert B):                 "
          f"{cap['r_only_null']['cert_A']:.3e} / "
          f"{cap['r_only_null']['cert_B']:.3e}")
    print(f"H(A) / H(B):                                   "
          f"{cap['H_A']} / {cap['H_B']}")
    print(f"zone trace distance A vs B (the located trace): "
          f"{res['obstruction']['zone_trace_distance_A_vs_B']:.6f}")
    print(f"zone joint Z-readout diff (still flat):         "
          f"{res['obstruction']['zone_joint_z_readout_diff']:.3e}")
    print("graded sweep:")
    for row in res["graded"]["sweep"]:
        print(f"  alpha = {row['alpha_over_pi']:.2f} pi: achieved "
              f"{row['achieved_locked_visibility']:.6f}, bound "
              f"{row['channel_bound_zone']:.4f}, escaped D "
              f"{row['escaped_distinguishability']:.6f}, "
              f"{row['threshold_restoration']}")
    led = res["ledger"]
    print(f"ledger: restore A erased bits {led['restore_A']['erased_bits']}, "
          f"blind reset naive beta*W "
          f"{led['blind_reset_A']['beta_work_lower_bound_naive']:.4f}, "
          f"capability after reset "
          f"{led['blind_reset_A']['capability_after_reset']:.3e}")
    print(f"B in-zone restoration feasible: "
          f"{led['restore_B_in_zone']['feasible_in_zone']} "
          f"(min cost {led['restore_B_in_zone']['min_beta_work']})")
    print("-" * 70)
    print(f"PHYSICALIZATION HOLDS: {res['physicalization_holds']}")
    print(res["verdict_language"])
# end of module
