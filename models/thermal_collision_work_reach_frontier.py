"""T410: Thermal Collision Work--Reach Frontier -- the Hamiltonian-bath
rung of the capability restoration frontier.

T393 named the Tier-2 (thermodynamic) card; T409 built its closed-unitary
finite rung and its 2026-07-02 hostile review (aggregate verdict
survives-with-corrections; T409 internally established in RE-SCOPED
standing: a repo-internal calibration of the certificate toolkit on a
quantum-Darwinism-type collision family) located exactly what was
missing: (a) T409's reach was a declared, graded bookkeeping boundary --
nothing dynamical prevented access to the "unreached" bath qubits; and
(b) T409's "work does not substitute for reach" failure leg was
mathematically unfireable. This artifact builds T409's own named-unbuilt
next rung: a switched-Hamiltonian repeated-interaction (collision) model
with Gibbs bath ancillas, a genuine omega-unit work parameter,
temperature, heat, and entropy production -- where the boundary is
DEPARTURE (each carrier is traced out of the model after its collision
unless physically retained; reach IS the retained register set; no menu
line ever forbids touching a co-present register) and the
work-substitution failure leg is fireable in the predeclared
undetermined-band cells.

THE MODEL. T392's measurement core: S in (|0> + e^{i phi}|1>)/sqrt(2);
controlled-Ry(theta_meter = pi/3) S -> M (meter measured; all verdicts
conditional on M = 0, the dominant branch, P(M=0) = 7/8 phi-independent;
M then removed -- pure, factorized); CNOT S -> REC. Then n <= 5
collisions: fresh ancilla B_i appended in tau_beta = diag(p0, p1)
(H_B = omega |1><1|, ground |0>, hbar = omega = 1; beta = inf gives
|0><0| exactly -- the T409 corner; beta = 0 gives I/2), collision window
U_i = expm(-i tau (f H_REC + f H_Bi + H_int)), H_int = g |1><1|_REC (x)
sigma_y^(Bi), tau = 1, g = theta/(2 tau), free-term toggle f in {0, 1}.
Free-off corner: U_i = controlled-Ry(theta) EXACTLY -- zero translation
loss against T409. After its collision the carrier DEPARTS (partial
trace) unless retained.

PREDECLARED LEGS (spec tests/T410-thermal-collision-work-reach-frontier.md,
frozen before this file existed; failure legs are reportable verdicts):

  1. First law + entropy production, exact-identity-backed at the
     computed states: W_i = Delta<H_REC> + Delta<H_Bi> (switching
     convention; = -Delta<H_int>; interior autonomous), Sigma_i =
     Delta S_complex + beta Q_i = I(complex:B_i) + D(rho_B'||tau_beta)
     asserted both ways at finite beta, >= -1e-10 everywhere; global
     balance telescopes.
  2. T409 regression corner (beta = inf, off, theta = pi): frontier
     block reproduced; cross-module comparison against T409's own
     frontier_row.
  3. Temperature-blind frontier (free off): f = |Tr[V_1 tau V_0^dag]| =
     cos(theta/2) for EVERY diagonal tau -- achieved(u) = vis_A
     cos(theta/2)^u at every beta including beta = 0; r_feas =
     max(0, n - d), d = (1, 0, 0) at theta = (0.25, 0.5, 1) pi.
  4. Certificate transfer to mixed thermal states: phi-independence
     certificate (degree-1 trigonometric structure stated and the
     3-phase reconstruction asserted) + trace-norm bound = exactly 2x
     achieved (factor-2 looseness, fourth artifact); bands
     feasible_zero_cost / certified_infeasible / undetermined_by_bound;
     dilation invariance asserted for BOTH |0><0| and Gibbs work
     ancillas (any work-register state is necessarily phi-independent);
     free-on theta = pi certified at every beta via
     bound <= 2 vis_A |A_blk| = 0.617983 < v*.
  5. Restoration work -- three branches predeclared in the spec (B1
     positive slope / B2 flat / B3 refund, the analytic prediction):
     W_rest(n, theta, beta) = -n w_fwd - (3/7) omega with w_fwd =
     (3/7)(Tr[H_B V_1 tau V_1^dag] - Tr[H_B tau]) (free-off:
     (3/7) sin^2(theta/2) tanh(beta/2)); round-trip work per retained
     contact exactly 0; forward writing work and departure-locked
     entropy production carry the genuine scaling with bath contact.
  6. Zero-bit contacts (beta = 0): every departed carrier's marginal
     exactly I/2, branch blocks identical, escaped Holevo exactly 0 --
     while r_feas = r_cert = n persists at theta = pi. Contacts, not
     bits, sharpened: the escaped bits go DOWN with temperature, the
     frontier does not move.
  7. Thermal complementarity: D_1 = sin(theta/2) tanh(beta/2);
     deficit >= D_u^2, equality iff beta = inf (the EGY-duality corner,
     named per the T409 review's prior-art completion).
  8. Landauer leg, T142 conventions at real beta (bookkeeping, not a
     theorem): correlated uncopy erases 0 bits and refunds work; blind
     reset pays the naive floor and restores nothing; beyond-frontier
     min cost = inf typed ACCESS-not-work (a work parameter now exists
     and is computed to be unable to substitute).
  9. Guardrails: Q1D with teeth (3/7) tanh(beta/2); R1 untouched (a
     reach frontier, not a light cone; Lieb-Robinson named from
     memory, unverified).

WHAT THIS DOES NOT EARN: no continuum/weak-coupling/transport theorem
(work BUYING reach stays named-unbuilt); no thermodynamic theorem (the
ledger is exact-identity-backed bookkeeping at the computed states,
finite-witness); no unconditional discharge of T407's declared-vs-
physical objection (departure is the standard reservoir idealization,
adopted, not derived); no hardware; no claim promotion -- ledger
actions pause for Joe per AGENTS.md. Hostile review is QUEUED for this
artifact, not yet performed.

Register order (retained density matrix): S, REC, then retained
carriers in collision order. M is projected (M = 0) and removed after
the meter. Ancillas are appended at the last position for their
collision window.
"""

from __future__ import annotations

import math
import sys
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import expm

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T392 primitives (measurement core constants and statevector helpers for
# the purification cross-check).
from models.fixed_sbs_key_reversal_divergence import (
    THETA as THETA_METER,
    V_STAR,
    _HADAMARD,
    reduced_density_matrix,
    zero_state,
)

# T393 machinery: certificate phase sweep, uniform locking grid, generic
# statevector applicator (purification path), Haar sampling, trace norm.
from models.causal_forcing_access_asymmetry import (
    PHI_CERT,
    PHI_LOCK_GRID,
    _trace_norm,
    apply_on_qubits,
    haar_unitary,
)

# T142 conventions for the Landauer leg.
from models.thermodynamic_erasure_calibration import (
    LANDAUER_NAT_PER_BIT,
    landauer_bound_bits,
)

# T409: regression comparison only (cited in its re-scoped,
# internally-established standing; audits/2026-07-02-t409-hostile-review.md).
from models.capability_restoration_frontier import frontier_row as t409_frontier_row

# --------------------------------------------------------------------------- #
# Predeclared constants (spec-frozen; see the spec file for the trail)
# --------------------------------------------------------------------------- #

S_POS, REC_POS = 0, 1  # positions in the retained density matrix

TAU = 1.0  # collision window, omega-units
N_ANC_MAX = 5
BETA_SWEEP = (math.inf, 2.0, 1.0, 0.5, 0.0)
THETA_SWEEP = (0.25 * math.pi, 0.5 * math.pi, math.pi)
TOGGLES = (False, True)  # free Hamiltonian terms off / on
EXHAUSTIVE_N = (1, 2, 3)

VIS_A_ANALYTIC = 4.0 * math.sqrt(3.0) / 7.0  # 0.989743...
BRANCH1_WEIGHT = 3.0 / 7.0  # P(S = 1 | M = 0); REC excitation weight
P_M0 = 7.0 / 8.0

FLATNESS_TOL = 1e-12
ANALYTIC_TOL = 1e-9
IDENTITY_TOL = 1e-10
SIGMA_NONNEG_TOL = -1e-10
SPREAD_TOL = 1e-10

HAAR_SAMPLES = 15
HAAR_SEED = 20260703
HAAR_VISIBILITY_CEILING = 0.05

# Work-substitution attack cells (the fireable region -- undetermined band).
ATTACK_THETA = 0.5 * math.pi
ATTACK_BETAS = (math.inf, 1.0, 0.0)
ATTACK_N = 4
ATTACK_REACH_SIZES = (2, 3)

# Ledger scenarios.
LEDGER_N = 4
LEDGER_HOLDER_BETAS = (math.inf, 1.0, 0.0)
SIGMA_IDENTITY_BETAS = (2.0, 1.0, 0.5, 0.0)

# Purification cross-check configuration (predeclared).
PURITY_CHECK = {
    "n": 2,
    "retained": (2,),  # retain B2, B1 departs
    "beta": 1.0,
    "theta": 0.5 * math.pi,
    "phis": (1.0, math.pi / 3.0),
}

INFINITE_COST = math.inf

VERDICT_RESTORABLE = "restorable-at-reach"
VERDICT_FINAL = "final-relative-to-reach"
VERDICT_TAGS = (
    "thermal_collision_work_reach_frontier",
    "hamiltonian_bath_finite_rung",
    "departure_carried_boundary",
    "temperature_blind_reach_frontier",
    "restoration_work_refund_within_reach",
    "entropy_locked_at_departure",
    "ledger_bookkeeping_not_theorem",
    "no_claim_promotion",
)

BAND_FEASIBLE = "feasible_zero_cost"
BAND_CERTIFIED = "certified_infeasible"
BAND_UNDETERMINED = "undetermined_by_bound"

# --------------------------------------------------------------------------- #
# Small exact operators
# --------------------------------------------------------------------------- #

_I2 = np.eye(2, dtype=complex)
_PAULI_X2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
_PAULI_Y2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
_P0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
_P1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
_NUM = _P1  # H = omega |1><1| with omega = 1
_SWAP4 = np.array(
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex
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
_CRY_METER4 = _controlled(_ry(THETA_METER))


def tau_gibbs(beta: float) -> np.ndarray:
    """Gibbs state of H_B = omega |1><1| (ground |0>, gap omega = 1).
    beta = inf -> |0><0| exactly (the T409 corner); beta = 0 -> I/2."""
    if math.isinf(beta):
        return np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    z = 1.0 + math.exp(-beta)
    return np.array(
        [[1.0 / z, 0.0], [0.0, math.exp(-beta) / z]], dtype=complex
    )


def _tanh_half(beta: float) -> float:
    return 1.0 if math.isinf(beta) else math.tanh(beta / 2.0)


# --------------------------------------------------------------------------- #
# Collision unitary: scipy expm vs analytic REC-block construction
# --------------------------------------------------------------------------- #

@lru_cache(maxsize=None)
def collision_unitary(theta: float, free_on: bool) -> tuple:
    """4x4 unitary on (REC, B) for one collision window.

    U = expm(-i tau (f H_REC + f H_B + H_int)), H_int = g P1 (x) sigma_y,
    g = theta / (2 tau), f = 1 if free_on else 0. Returns
    (U_expm, U_block) as a nested-tuple pair for caching; the two
    constructions are asserted equal in construction_report()."""
    g = theta / (2.0 * TAU)
    f = 1.0 if free_on else 0.0
    h_full = (
        f * np.kron(_NUM, _I2)
        + f * np.kron(_I2, _NUM)
        + g * np.kron(_P1, _PAULI_Y2)
    )
    u_expm = expm(-1j * TAU * h_full)
    # Analytic REC-conditional block form (independent construction):
    # U = |0><0| (x) V0 + e^{-i tau f} |1><1| (x) V1
    v0 = expm(-1j * TAU * (f * _NUM))
    v1 = expm(-1j * TAU * (f * _NUM + g * _PAULI_Y2))
    u_block = np.kron(_P0, v0) + np.exp(-1j * TAU * f) * np.kron(_P1, v1)
    return (
        tuple(map(tuple, u_expm)),
        tuple(map(tuple, u_block)),
    )


def collision_u(theta: float, free_on: bool) -> np.ndarray:
    return np.array(collision_unitary(theta, free_on)[0], dtype=complex)


def collision_blocks(theta: float, free_on: bool):
    """(V0, V1): the REC-conditional 2x2 block unitaries (branch phase
    excluded; it is constant in phi and cannot move the locked metric)."""
    g = theta / (2.0 * TAU)
    f = 1.0 if free_on else 0.0
    v0 = expm(-1j * TAU * (f * _NUM))
    v1 = expm(-1j * TAU * (f * _NUM + g * _PAULI_Y2))
    return v0, v1


# --------------------------------------------------------------------------- #
# Analytic closed forms (predeclared in the spec)
# --------------------------------------------------------------------------- #

def branch_overlap_f(theta: float, beta: float, free_on: bool) -> float:
    """f = |Tr[V_1 tau_beta V_0^dag]| -- the per-departed-carrier record
    coherence factor. Free-off closed form: cos(theta/2) for EVERY
    diagonal tau (temperature-blind)."""
    v0, v1 = collision_blocks(theta, free_on)
    return float(abs(np.trace(v1 @ tau_gibbs(beta) @ v0.conj().T)))


def deficit_allowance(f: float) -> int:
    """d(f): largest departed-contact count compatible with threshold
    restoration, from achieved(u) = vis_A f^u >= v*."""
    if f <= 1e-12:
        return 0
    return int(math.floor(math.log(V_STAR / VIS_A_ANALYTIC) / math.log(f)))


def min_certified_deficit(f: float) -> float:
    """u_min_cert(f): smallest departed-contact count at which the
    trace-norm bound bites (2 vis_A f^u < v*)."""
    if f <= 1e-12:
        return 1.0
    u = math.log(V_STAR / (2.0 * VIS_A_ANALYTIC)) / math.log(f)
    return float(math.floor(u) + 1)


def w_fwd_analytic(theta: float, beta: float, free_on: bool) -> float:
    """Per-contact forward writing work (switching convention), block
    evaluation: (3/7)(Tr[H_B V_1 tau V_1^dag] - Tr[H_B tau]).
    Free-off closed form: (3/7) sin^2(theta/2) tanh(beta/2)."""
    _, v1 = collision_blocks(theta, free_on)
    tau_b = tau_gibbs(beta)
    return float(
        BRANCH1_WEIGHT
        * np.real(
            np.trace(_NUM @ (v1 @ tau_b @ v1.conj().T)) - np.trace(_NUM @ tau_b)
        )
    )


def w_fwd_closed_form_free_off(theta: float, beta: float) -> float:
    return BRANCH1_WEIGHT * math.sin(theta / 2.0) ** 2 * _tanh_half(beta)


def w_rest_analytic(n_retained: int, theta: float, beta: float, free_on: bool) -> float:
    """W_rest = -r w_fwd - 3/7 (the B3 refund law, derived in the spec)."""
    return -n_retained * w_fwd_analytic(theta, beta, free_on) - BRANCH1_WEIGHT


def d1_closed_form(theta: float, beta: float) -> float:
    """One-carrier displaced branch distinguishability, free off."""
    return math.sin(theta / 2.0) * _tanh_half(beta)


def _h2_bits(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return float(-p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p))


H2_3_7 = _h2_bits(3.0 / 7.0)  # 0.985228...


def chi1_closed_form(beta: float) -> float:
    """One-carrier escaped Holevo at theta = pi, free off (bits):
    chi_1 = h2(4/7 p0 + 3/7 p1) - h2(p0)."""
    tau_b = tau_gibbs(beta)
    p0 = float(np.real(tau_b[0, 0]))
    p1 = float(np.real(tau_b[1, 1]))
    return _h2_bits(4.0 / 7.0 * p0 + 3.0 / 7.0 * p1) - _h2_bits(p0)


# --------------------------------------------------------------------------- #
# Density-matrix machinery
# --------------------------------------------------------------------------- #

_EMBED_CACHE: dict = {}


def embed_unitary(gate: np.ndarray, positions, m: int) -> np.ndarray:
    """Full 2^m x 2^m embedding of a k-qubit gate at ``positions``."""
    key = (gate.tobytes(), tuple(positions), m)
    if key in _EMBED_CACHE:
        return _EMBED_CACHE[key]
    k = len(positions)
    rest = [q for q in range(m) if q not in positions]
    big = np.kron(gate, np.eye(2 ** (m - k), dtype=complex))
    src = list(positions) + rest  # qubit carried by each axis of ``big``
    order = list(np.argsort(src))
    t = big.reshape([2] * (2 * m))
    t = np.transpose(t, order + [m + o for o in order])
    out = np.ascontiguousarray(t.reshape(2 ** m, 2 ** m))
    _EMBED_CACHE[key] = out
    return out


def dm_apply(rho: np.ndarray, gate: np.ndarray, positions) -> np.ndarray:
    m = int(round(math.log2(rho.shape[0])))
    u = embed_unitary(gate, positions, m)
    return u @ rho @ u.conj().T


def dm_kraus(rho: np.ndarray, kraus_list, positions) -> np.ndarray:
    m = int(round(math.log2(rho.shape[0])))
    out = np.zeros_like(rho)
    for k in kraus_list:
        u = embed_unitary(k, positions, m)
        out = out + u @ rho @ u.conj().T
    return out


def dm_ptrace(rho: np.ndarray, keep) -> np.ndarray:
    """Partial trace keeping ``keep`` positions (sorted order preserved)."""
    m = int(round(math.log2(rho.shape[0])))
    remove = [q for q in range(m) if q not in keep]
    t = rho.reshape([2] * (2 * m))
    mm = m
    for q in sorted(remove, reverse=True):
        t = np.trace(t, axis1=q, axis2=mm + q)
        mm -= 1
    return t.reshape(2 ** mm, 2 ** mm)


def dm_append(rho: np.ndarray, tau: np.ndarray) -> np.ndarray:
    return np.kron(rho, tau)


def dm_expect(rho: np.ndarray, op2: np.ndarray, position: int) -> float:
    m = int(round(math.log2(rho.shape[0])))
    full = embed_unitary(op2, (position,), m)
    return float(np.real(np.trace(full @ rho)))


def vn_entropy_nats(rho: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho)
    eig = eig[eig > 1e-15]
    return float(-np.sum(eig * np.log(eig)))


def vn_entropy_bits(rho: np.ndarray) -> float:
    return vn_entropy_nats(rho) / math.log(2.0)


def rel_entropy_nats(rho: np.ndarray, tau: np.ndarray) -> float:
    """D(rho || tau) for diagonal full-rank tau (finite beta only)."""
    ln_tau = np.diag(np.log(np.real(np.diag(tau))))
    return float(-vn_entropy_nats(rho) - np.real(np.trace(rho @ ln_tau)))


def trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(a - b)
    return float(0.5 * np.sum(np.abs(eig)))


# --------------------------------------------------------------------------- #
# Preparations: core + collision stream with departure
# --------------------------------------------------------------------------- #

_CORE_CACHE: dict = {}


def core_conditioned(phi: float):
    """(rho on (S, REC), P(M = 0)). Statevector core, meter measured,
    M = 0 selected; M is then pure |0> and factorized, so it is removed."""
    key = float(phi)
    if key in _CORE_CACHE:
        return _CORE_CACHE[key]
    psi = zero_state(3)  # S, M, REC
    psi = apply_on_qubits(psi, _HADAMARD, [0], 3)
    if phi != 0.0:
        psi = apply_on_qubits(psi, _phase_gate(phi), [0], 3)
    psi = apply_on_qubits(psi, _CRY_METER4, [0, 1], 3)
    psi = apply_on_qubits(psi, _CNOT4, [0, 2], 3)
    # project M = 0
    tensor = psi.reshape(2, 2, 2).copy()
    tensor[:, 1, :] = 0.0
    flat = tensor.reshape(8)
    prob = float(np.real(flat.conj() @ flat))
    flat = flat / math.sqrt(prob)
    rho = reduced_density_matrix(flat, [0, 2], 3)  # keep S, REC
    _CORE_CACHE[key] = (rho, prob)
    return _CORE_CACHE[key]


def core_full_dm(phi: float) -> np.ndarray:
    """Unconditioned core density matrix on (S, M, REC) -- Q1D use."""
    psi = zero_state(3)
    psi = apply_on_qubits(psi, _HADAMARD, [0], 3)
    if phi != 0.0:
        psi = apply_on_qubits(psi, _phase_gate(phi), [0], 3)
    psi = apply_on_qubits(psi, _CRY_METER4, [0, 1], 3)
    psi = apply_on_qubits(psi, _CNOT4, [0, 2], 3)
    return np.outer(psi, psi.conj())


def prepare_retained(
    n: int, retained, phi: float, theta: float, beta: float, free_on: bool
) -> np.ndarray:
    """Exact retained density matrix after ``n`` collisions, conditioned
    on M = 0. ``retained`` = collision indices (1-based) kept; every
    other carrier DEPARTS (is traced out) immediately after its
    collision. Order: (S, REC, retained carriers in collision order)."""
    if not 0 <= n <= N_ANC_MAX:
        raise ValueError(f"n = {n} outside 0..{N_ANC_MAX}")
    retained = tuple(sorted(retained))
    if any(i < 1 or i > n for i in retained):
        raise ValueError(f"retained {retained} outside 1..{n}")
    rho, _ = core_conditioned(phi)
    tau_b = tau_gibbs(beta)
    u = collision_u(theta, free_on)
    for i in range(1, n + 1):
        m = int(round(math.log2(rho.shape[0])))
        rho = dm_append(rho, tau_b)
        rho = dm_apply(rho, u, (REC_POS, m))
        if i not in retained:
            rho = dm_ptrace(rho, tuple(range(m)))
    return rho


def retained_positions(retained) -> tuple:
    """Positions of the retained carriers in the retained DM."""
    return tuple(2 + k for k in range(len(retained)))


# --------------------------------------------------------------------------- #
# Protocols
# --------------------------------------------------------------------------- #

def unwrite_protocol(retained, theta: float, free_on: bool):
    """The restoration protocol at the given retained reach: apply
    U_i^dag per retained carrier (reach-supported; the collisions share
    the control REC in its Z basis, so they commute and any order
    works), then uncopy the record (CNOT S -> REC)."""
    u_dag = collision_u(theta, free_on).conj().T

    def _proto(rho: np.ndarray) -> np.ndarray:
        out = rho
        for pos in retained_positions(retained):
            out = dm_apply(out, u_dag, (REC_POS, pos))
        out = dm_apply(out, _CNOT4, (S_POS, REC_POS))
        return out

    return _proto


def identity_protocol(rho: np.ndarray) -> np.ndarray:
    return rho


def manufactured_coherence_protocol(rho: np.ndarray) -> np.ndarray:
    """Unlimited-work exploit (null control): adjoin a fresh work qubit,
    put it in |+>, SWAP it into S. Raw visibility ~1; carries ZERO
    information about the prepared phase, so the locked metric nulls it."""
    m = int(round(math.log2(rho.shape[0])))
    out = dm_append(rho, np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex))
    out = dm_apply(out, _HADAMARD, (m,))
    out = dm_apply(out, _SWAP4, (m, S_POS))
    return out


def feedback_protocol(retained, theta: float, free_on: bool):
    """Representative non-unitary reach channel: measure REC in Z, feed
    back X on S, then the reach protocol (the menu is all channels)."""
    proto = unwrite_protocol(retained, theta, free_on)

    def _channel(rho: np.ndarray) -> np.ndarray:
        b0 = dm_kraus(rho, [_P0], (REC_POS,))
        b1 = dm_kraus(rho, [_P1], (REC_POS,))
        b1 = dm_apply(b1, _PAULI_X2, (S_POS,))
        return proto(b0 + b1)

    return _channel


def blind_reset_protocol(holder_positions):
    """T142's blind reset as a channel: each holder measured in Z and
    reset to |0> WITHOUT using the source-copy correlation."""

    def _channel(rho: np.ndarray) -> np.ndarray:
        out = rho
        for pos in holder_positions:
            out = dm_kraus(out, [_P0, _PAULI_X2 @ _P1], (pos,))
        return out

    return _channel


# --------------------------------------------------------------------------- #
# Figure of merit and certificates
# --------------------------------------------------------------------------- #

def locked_visibility(
    n: int, retained, protocol, theta: float, beta: float, free_on: bool,
    grid=PHI_LOCK_GRID,
) -> float:
    """Phase-locked conditional X-visibility |mean_phi e^{i phi}
    2 rho_S[0,1]| (T392's figure of merit; the uniform grid exactly
    nulls manufactured phi-independent coherence)."""
    total = 0.0 + 0.0j
    for phi in grid:
        rho = prepare_retained(n, retained, phi, theta, beta, free_on)
        out = protocol(rho)
        rho_s = dm_ptrace(out, (S_POS,))
        total += np.exp(1j * phi) * 2.0 * rho_s[0, 1]
    return float(abs(total / len(grid)))


def raw_visibility(
    n: int, retained, protocol, theta: float, beta: float, free_on: bool,
    phi: float = 0.0,
) -> float:
    rho = prepare_retained(n, retained, phi, theta, beta, free_on)
    out = protocol(rho)
    rho_s = dm_ptrace(out, (S_POS,))
    return float(2.0 * abs(rho_s[0, 1]))


def phi_independence_cert(
    n: int, retained, theta: float, beta: float, free_on: bool, phis=PHI_CERT
) -> float:
    """Max pairwise entrywise difference of the retained M-conditioned
    states across the phase sweep. rho(phi) is a degree-1 trigonometric
    polynomial in phi (single phase gate; P(M=0) phi-independent), so
    flatness at >= 3 phases forces flatness at ALL phi; below tolerance
    NO channel on the reach (with work ancillas in any -- necessarily
    phi-independent -- state) produces phi-locked output."""
    rhos = [
        prepare_retained(n, retained, phi, theta, beta, free_on) for phi in phis
    ]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def channel_bound(
    n: int, retained, theta: float, beta: float, free_on: bool,
    grid=PHI_LOCK_GRID, extra_sigmas=(),
) -> float:
    """T393's channel-independent bound on the phase-locked visibility of
    ANY CPTP map on the retained reach: 2 (||Re X||_1 + ||Im X||_1),
    X = mean_phi e^{i phi} rho_retained|M=0(phi). Mixed states included
    (Hoelder + CPTP trace-norm contractivity). ``extra_sigmas`` adjoins
    work registers in fixed states (|0><0| or Gibbs): X gains tensor
    factors with ||A (x) sigma||_1 = ||A||_1, so the bound is invariant
    -- asserted numerically in certificate_transfer_report()."""
    dim = None
    x = None
    for phi in grid:
        rho = prepare_retained(n, retained, phi, theta, beta, free_on)
        for sigma in extra_sigmas:
            rho = dm_append(rho, sigma)
        if x is None:
            dim = rho.shape[0]
            x = np.zeros((dim, dim), dtype=complex)
        x = x + np.exp(1j * phi) * rho
    x = x / len(grid)
    herm = (x + x.conj().T) / 2.0
    anti = (x - x.conj().T) / 2.0j
    return 2.0 * (_trace_norm(herm) + _trace_norm(anti))


def degree1_reconstruction_residual(
    n: int, retained, theta: float, beta: float, free_on: bool
) -> float:
    """Assert the degree-1 trigonometric structure: reconstruct
    rho(phi) = A + e^{i phi} B + e^{-i phi} C from three nodes and
    predict the six PHI_CERT phases."""
    nodes = (0.3, 1.7, 3.1)
    rhos = [
        prepare_retained(n, retained, phi, theta, beta, free_on)
        for phi in nodes
    ]
    dim = rhos[0].shape[0]
    m = np.array(
        [[1.0, np.exp(1j * p), np.exp(-1j * p)] for p in nodes], dtype=complex
    )
    stacked = np.array([r.reshape(-1) for r in rhos])
    coeffs = np.linalg.solve(m, stacked)  # rows: A, B, C (flattened)
    a, b, c = (coeffs[k].reshape(dim, dim) for k in range(3))
    worst = 0.0
    for phi in PHI_CERT:
        pred = a + np.exp(1j * phi) * b + np.exp(-1j * phi) * c
        actual = prepare_retained(n, retained, phi, theta, beta, free_on)
        worst = max(worst, float(np.max(np.abs(pred - actual))))
    return worst


# --------------------------------------------------------------------------- #
# Frontier cells and tables
# --------------------------------------------------------------------------- #

def frontier_cell(
    n: int, retained, theta: float, beta: float, free_on: bool
) -> dict:
    achieved = locked_visibility(
        n, retained, unwrite_protocol(retained, theta, free_on),
        theta, beta, free_on,
    )
    bound = channel_bound(n, retained, theta, beta, free_on)
    cert = phi_independence_cert(n, retained, theta, beta, free_on)
    if achieved >= V_STAR:
        band = BAND_FEASIBLE
    elif bound < V_STAR:
        band = BAND_CERTIFIED
    else:
        band = BAND_UNDETERMINED
    u = n - len(retained)
    f = branch_overlap_f(theta, beta, free_on)
    return {
        "n": n,
        "reach": len(retained),
        "departed": u,
        "achieved": achieved,
        "analytic": VIS_A_ANALYTIC * f ** u,
        "bound": bound,
        "phi_cert": cert,
        "band": band,
        "verdict": VERDICT_RESTORABLE if band == BAND_FEASIBLE else (
            VERDICT_FINAL if band == BAND_CERTIFIED else BAND_UNDETERMINED
        ),
    }


def frontier_for(theta: float, beta: float, free_on: bool) -> dict:
    """Frontier at one sweep point: canonical prefix retained sets
    (justified by the symmetry report), r_feas / r_cert per n, analytic
    cross-checks from the branch-overlap law."""
    f = branch_overlap_f(theta, beta, free_on)
    d = deficit_allowance(f)
    u_cert = min_certified_deficit(f)
    per_n = []
    for n in range(1, N_ANC_MAX + 1):
        rows = [
            frontier_cell(n, tuple(range(1, r + 1)), theta, beta, free_on)
            for r in range(n + 1)
        ]
        r_feas = next(
            (row["reach"] for row in rows if row["band"] == BAND_FEASIBLE),
            None,
        )
        r_cert = 0
        for row in rows:
            if row["band"] == BAND_CERTIFIED:
                r_cert = row["reach"] + 1
            else:
                break
        per_n.append(
            {
                "n": n,
                "rows": rows,
                "r_feas": r_feas,
                "r_cert": r_cert,
                "r_feas_analytic": max(0, n - d),
                "r_cert_analytic": (
                    max(0, n - int(u_cert) + 1) if u_cert <= n else 0
                ),
            }
        )
    return {
        "theta_over_pi": theta / math.pi,
        "beta": beta,
        "free_on": free_on,
        "branch_overlap_f": f,
        "deficit_allowance_d": d,
        "min_certified_deficit_u": ("inf" if math.isinf(u_cert) else u_cert),
        "per_n": per_n,
        "r_feas_by_n": [row["r_feas"] for row in per_n],
        "r_cert_by_n": [row["r_cert"] for row in per_n],
    }


# --------------------------------------------------------------------------- #
# Ledger stream: first law, entropy production, restoration work
# --------------------------------------------------------------------------- #

def stream_ledger(
    n: int, retained, theta: float, beta: float, free_on: bool,
    phi: float = 0.0, restore: bool = True,
) -> dict:
    """Full thermodynamic bookkeeping of one M=0-conditioned trajectory.

    Per collision (switching convention; H_int off at both endpoints):
      W_i = Delta<H_REC> + Delta<H_Bi>   (= -Delta<H_int>; interior
            autonomous: Delta<H_window> = 0, both asserted)
      Q_i = Delta<H_Bi>
      Sigma_i = Delta S_complex + beta Q_i, cross-checked against the
            exact identity I(complex:B_i)_after + D(rho_B'||tau_beta)
            at finite beta; typed inf at beta = inf with Q_i > 0.
    Departure locks the collision's Sigma_i in (the un-write option
    lapses). Restoration (if requested): U_i^dag per retained carrier +
    CNOT uncopy, work tracked per gate. Global balance: appended and
    departed carrier energies counted at their boundary values."""
    retained = tuple(sorted(retained))
    rho, _ = core_conditioned(phi)
    tau_b = tau_gibbs(beta)
    u_coll = collision_u(theta, free_on)
    g = theta / (2.0 * TAU)
    f_flag = 1.0 if free_on else 0.0
    h_window = (
        f_flag * np.kron(_NUM, _I2)
        + f_flag * np.kron(_I2, _NUM)
        + g * np.kron(_P1, _PAULI_Y2)
    )
    h_int = g * np.kron(_P1, _PAULI_Y2)

    e_tau = float(np.real(np.trace(_NUM @ tau_b)))
    e_start = dm_expect(rho, _NUM, REC_POS)  # core CNOT already paid
    energy_in_appended = 0.0
    energy_out_departed = 0.0
    total_work = 0.0

    collisions = []
    kept_positions = []
    finite = not math.isinf(beta)
    for i in range(1, n + 1):
        m = int(round(math.log2(rho.shape[0])))
        s_complex_before = vn_entropy_nats(rho)
        joint = dm_append(rho, tau_b)
        energy_in_appended += e_tau
        b_pos = m
        e_free_before = (
            dm_expect(joint, _NUM, REC_POS) + dm_expect(joint, _NUM, b_pos)
        )
        h_win_full = embed_unitary(h_window, (REC_POS, b_pos), m + 1)
        h_int_full = embed_unitary(h_int, (REC_POS, b_pos), m + 1)
        e_win_before = float(np.real(np.trace(h_win_full @ joint)))
        e_int_before = float(np.real(np.trace(h_int_full @ joint)))
        joint = dm_apply(joint, u_coll, (REC_POS, b_pos))
        e_free_after = (
            dm_expect(joint, _NUM, REC_POS) + dm_expect(joint, _NUM, b_pos)
        )
        e_win_after = float(np.real(np.trace(h_win_full @ joint)))
        e_int_after = float(np.real(np.trace(h_int_full @ joint)))

        w_i = e_free_after - e_free_before
        q_i = dm_expect(joint, _NUM, b_pos) - e_tau
        rho_b_after = dm_ptrace(joint, (b_pos,))
        rho_c_after = dm_ptrace(joint, tuple(range(m)))
        s_complex_after = vn_entropy_nats(rho_c_after)
        d_s = s_complex_after - s_complex_before
        mutual = (
            s_complex_after
            + vn_entropy_nats(rho_b_after)
            - vn_entropy_nats(joint)
        )
        rec = {
            "i": i,
            "W_i": w_i,
            "Q_i": q_i,
            "delta_S_complex_nats": d_s,
            "interior_conservation_residual": abs(e_win_after - e_win_before),
            "work_convention_agreement": abs(w_i - (e_int_before - e_int_after)),
            "mutual_information_nats": mutual,
            "departs": i not in retained,
        }
        if finite:
            sigma = d_s + beta * q_i
            d_rel = rel_entropy_nats(rho_b_after, tau_b)
            rec["Sigma_i"] = sigma
            rec["sigma_identity_residual"] = abs(sigma - (mutual + d_rel))
            rec["relative_entropy_nats"] = d_rel
        else:
            rec["Sigma_i"] = (
                INFINITE_COST if q_i > 1e-12 else d_s
            )  # beta = inf: typed, not asserted (D(rho'||pure) divergent)
            rec["sigma_identity_residual"] = None
        total_work += w_i
        if i not in retained:
            energy_out_departed += dm_expect(joint, _NUM, b_pos)
            rho = dm_ptrace(joint, tuple(range(m)))
        else:
            rho = joint
            kept_positions.append(2 + len(kept_positions))
        collisions.append(rec)

    restoration = None
    if restore:
        u_dag = u_coll.conj().T
        w_gates = []
        for k, pos in enumerate(retained_positions(retained)):
            e_before = dm_expect(rho, _NUM, REC_POS) + sum(
                dm_expect(rho, _NUM, p) for p in retained_positions(retained)
            )
            rho = dm_apply(rho, u_dag, (REC_POS, pos))
            e_after = dm_expect(rho, _NUM, REC_POS) + sum(
                dm_expect(rho, _NUM, p) for p in retained_positions(retained)
            )
            w_gates.append(e_after - e_before)
        e_before = dm_expect(rho, _NUM, REC_POS) + sum(
            dm_expect(rho, _NUM, p) for p in retained_positions(retained)
        )
        rho = dm_apply(rho, _CNOT4, (S_POS, REC_POS))
        e_after = dm_expect(rho, _NUM, REC_POS) + sum(
            dm_expect(rho, _NUM, p) for p in retained_positions(retained)
        )
        w_uncopy = e_after - e_before
        w_rest = sum(w_gates) + w_uncopy
        total_work += w_rest
        fwd_ws = [c["W_i"] for c in collisions if not c["departs"]]
        roundtrip = max(
            (abs(wf + wg) for wf, wg in zip(fwd_ws, w_gates)), default=0.0
        )
        restoration = {
            "per_unwrite_gate_work": w_gates,
            "uncopy_work": w_uncopy,
            "W_rest": w_rest,
            "W_rest_analytic": w_rest_analytic(
                len(retained), theta, beta, free_on
            ),
            "roundtrip_work_per_contact_max_abs": roundtrip,
        }

    e_final = dm_expect(rho, _NUM, REC_POS) + sum(
        dm_expect(rho, _NUM, p) for p in retained_positions(retained)
    )
    balance_residual = abs(
        e_start + energy_in_appended + total_work
        - (e_final + energy_out_departed)
    )
    sigmas = [
        c["Sigma_i"] for c in collisions if not math.isinf(c["Sigma_i"])
    ]
    return {
        "n": n,
        "retained": list(retained),
        "theta_over_pi": theta / math.pi,
        "beta": beta,
        "free_on": free_on,
        "collisions": collisions,
        "restoration": restoration,
        "w_fwd_analytic": w_fwd_analytic(theta, beta, free_on),
        "global_balance_residual": balance_residual,
        "min_sigma": (min(sigmas) if sigmas else None),
        "cumulative_sigma_monotone": all(
            s >= SIGMA_NONNEG_TOL for s in sigmas
        ),
    }


# --------------------------------------------------------------------------- #
# Purification cross-check (thermofield double, statevector path)
# --------------------------------------------------------------------------- #

def purification_check() -> dict:
    """DM path vs thermofield statevector path at the predeclared
    configuration (n = 2, retain {B2}, beta = 1.0, theta = 0.5 pi,
    both toggles). Layout: S, M, REC, B1, B1t, B2, B2t (7 qubits)."""
    cfg = PURITY_CHECK
    beta, theta = cfg["beta"], cfg["theta"]
    tau_b = tau_gibbs(beta)
    p0 = float(np.real(tau_b[0, 0]))
    ry_tf = _ry(2.0 * math.atan2(math.sqrt(1.0 - p0), math.sqrt(p0)))
    worst = 0.0
    for free_on in TOGGLES:
        u_coll = collision_u(theta, free_on)
        for phi in cfg["phis"]:
            psi = zero_state(7)
            psi = apply_on_qubits(psi, _HADAMARD, [0], 7)
            psi = apply_on_qubits(psi, _phase_gate(phi), [0], 7)
            psi = apply_on_qubits(psi, _CRY_METER4, [0, 1], 7)
            psi = apply_on_qubits(psi, _CNOT4, [0, 2], 7)
            # thermofield doubles: B1 (3) with B1t (4); B2 (5) with B2t (6)
            for b, bt in ((3, 4), (5, 6)):
                psi = apply_on_qubits(psi, ry_tf, [bt], 7)
                psi = apply_on_qubits(psi, _CNOT4, [bt, b], 7)
            psi = apply_on_qubits(psi, u_coll, [2, 3], 7)  # REC-B1
            psi = apply_on_qubits(psi, u_coll, [2, 5], 7)  # REC-B2
            # condition M = 0
            tensor = np.moveaxis(psi.reshape([2] * 7), 1, 0).copy()
            tensor[1] = 0.0
            flat = np.moveaxis(tensor, 0, 1).reshape(2 ** 7)
            prob = float(np.real(flat.conj() @ flat))
            flat = flat / math.sqrt(prob)
            # retained complex: S, REC, B2 (B1 departed; doubles traced)
            rho_pure_path = reduced_density_matrix(flat, [0, 2, 5], 7)
            rho_dm_path = prepare_retained(
                cfg["n"], cfg["retained"], phi, theta, beta, free_on
            )
            worst = max(
                worst, float(np.max(np.abs(rho_pure_path - rho_dm_path)))
            )
    return {"config": {k: str(v) for k, v in cfg.items()}, "max_diff": worst}


# --------------------------------------------------------------------------- #
# Leg 1 -- first law + entropy production
# --------------------------------------------------------------------------- #

def first_law_report() -> dict:
    """Ledger identities across the sweep at n = LEDGER_N, full
    retention (restoration included) and half retention (departures)."""
    rows = []
    worst_interior = 0.0
    worst_convention_free_on = 0.0
    worst_convention_free_off_deviation = 0.0
    worst_sigma_identity = 0.0
    min_sigma = math.inf
    worst_balance = 0.0
    worst_wq_spread = 0.0
    worst_phi_dependence = 0.0
    for theta in THETA_SWEEP:
        for beta in BETA_SWEEP:
            for free_on in TOGGLES:
                for retained in (
                    tuple(range(1, LEDGER_N + 1)),
                    (1, 2),
                ):
                    led = stream_ledger(
                        LEDGER_N, retained, theta, beta, free_on
                    )
                    ws = [c["W_i"] for c in led["collisions"]]
                    qs = [c["Q_i"] for c in led["collisions"]]
                    worst_wq_spread = max(
                        worst_wq_spread,
                        max(ws) - min(ws),
                        max(qs) - min(qs),
                    )
                    worst_interior = max(
                        worst_interior,
                        max(
                            c["interior_conservation_residual"]
                            for c in led["collisions"]
                        ),
                    )
                    conv = max(
                        c["work_convention_agreement"]
                        for c in led["collisions"]
                    )
                    if free_on:
                        worst_convention_free_on = max(
                            worst_convention_free_on, conv
                        )
                    else:
                        worst_convention_free_off_deviation = max(
                            worst_convention_free_off_deviation, conv
                        )
                    if led["min_sigma"] is not None:
                        min_sigma = min(min_sigma, led["min_sigma"])
                    if beta in SIGMA_IDENTITY_BETAS:
                        worst_sigma_identity = max(
                            worst_sigma_identity,
                            max(
                                c["sigma_identity_residual"]
                                for c in led["collisions"]
                            ),
                        )
                    worst_balance = max(
                        worst_balance, led["global_balance_residual"]
                    )
                    # ledger phi-independence (predeclared): rerun at
                    # phi = 1.0, W/Q streams must match.
                    if (
                        theta == math.pi
                        and free_on is False
                        and retained == tuple(range(1, LEDGER_N + 1))
                    ):
                        led_phi = stream_ledger(
                            LEDGER_N, retained, theta, beta, free_on, phi=1.0
                        )
                        worst_phi_dependence = max(
                            worst_phi_dependence,
                            max(
                                abs(a["W_i"] - b["W_i"])
                                + abs(a["Q_i"] - b["Q_i"])
                                for a, b in zip(
                                    led["collisions"], led_phi["collisions"]
                                )
                            ),
                        )
                    rows.append(
                        {
                            "theta_over_pi": theta / math.pi,
                            "beta": beta,
                            "free_on": free_on,
                            "retained": list(retained),
                            "W_per_collision": ws[0],
                            "Q_per_collision": qs[0],
                            "w_fwd_analytic": led["w_fwd_analytic"],
                            "min_Sigma": led["min_sigma"],
                            "Sigma_stream": [
                                c["Sigma_i"] for c in led["collisions"]
                            ],
                            "balance_residual": led[
                                "global_balance_residual"
                            ],
                        }
                    )
    return {
        "scenario_n": LEDGER_N,
        "rows": rows,
        "worst_interior_conservation": worst_interior,
        "worst_work_convention_agreement_free_on": worst_convention_free_on,
        "free_off_convention_deviation_max": worst_convention_free_off_deviation,
        "spec_wording_defect": (
            "FIRED AND REPORTED (predeclared cross-check located a "
            "mis-scoped parenthetical in the frozen spec): the spec's "
            "leg-1 sentence 'equivalently W_i = -Delta<H_int>' is TRUE "
            "only with free terms ON, where H_int is the only switched "
            "term and interior conservation of H_free + H_int gives "
            "W = Delta E_free = -Delta<H_int> (asserted < 1e-12). With "
            "free terms OFF the window generator is H_int alone: interior "
            "conservation gives Delta<H_int> = 0 (asserted, the same "
            "residual), the switched object is the ENTIRE window "
            "generator, and W = Delta E_free by definition -- the "
            "free-off deviation |W - (-Delta<H_int>)| equals w_fwd per "
            "collision (max over the sweep reported above), which is what "
            "revealed the mis-scoping. No computed quantity, closed form, "
            "or leg verdict is affected; the spec file is left frozen and "
            "the defect is disclosed here and in the results file."
        ),
        "worst_sigma_identity_residual": worst_sigma_identity,
        "min_sigma_over_sweep": min_sigma,
        "worst_global_balance_residual": worst_balance,
        "worst_wq_spread_across_collisions": worst_wq_spread,
        "worst_ledger_phi_dependence": worst_phi_dependence,
        "beta_inf_typing": (
            "at beta = inf with Q_i > 0, Sigma_i is typed inf "
            "(zero-temperature limit; D(rho'||pure) divergent) -- "
            "extended-real bookkeeping, disclosed, not numerically asserted"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 2 -- T409 regression corner
# --------------------------------------------------------------------------- #

def regression_report() -> dict:
    """(beta = inf, free off): the collision unitary IS controlled-Ry
    (asserted), and the frontier block reproduces T409's, cross-module."""
    u_off = collision_u(math.pi, False)
    cry = _controlled(_ry(math.pi))
    gate_diff = float(np.max(np.abs(u_off - cry)))

    fr = frontier_for(math.pi, math.inf, False)
    worst_cert = max(
        cell["phi_cert"]
        for row in fr["per_n"]
        for cell in row["rows"]
        if cell["reach"] < row["n"]
    )
    worst_bound = max(
        cell["bound"]
        for row in fr["per_n"]
        for cell in row["rows"]
        if cell["reach"] < row["n"]
    )
    full_reach_restores = [
        row["rows"][-1]["achieved"] for row in fr["per_n"]
    ]

    cross = []
    worst_cross = 0.0
    for theta in (0.5 * math.pi, math.pi):
        for n in (1, 3, 5):
            for r in range(n + 1):
                t409 = t409_frontier_row(n, r, theta)
                t410 = frontier_cell(
                    n, tuple(range(1, r + 1)), theta, math.inf, False
                )
                d_ach = abs(t409["achieved"] - t410["achieved"])
                d_bnd = abs(t409["bound"] - t410["bound"])
                d_crt = abs(t409["phi_cert"] - t410["phi_cert"])
                worst_cross = max(worst_cross, d_ach, d_bnd)
                cross.append(
                    {
                        "theta_over_pi": theta / math.pi,
                        "n": n,
                        "reach": r,
                        "achieved_diff": d_ach,
                        "bound_diff": d_bnd,
                        "cert_diff": d_crt,
                    }
                )
    return {
        "gate_equals_controlled_ry_max_diff": gate_diff,
        "r_feas_by_n": fr["r_feas_by_n"],
        "r_cert_by_n": fr["r_cert_by_n"],
        "worst_insufficient_phi_cert": worst_cert,
        "worst_insufficient_bound": worst_bound,
        "full_reach_restores": full_reach_restores,
        "vis_A_analytic": VIS_A_ANALYTIC,
        "cross_module_cells": cross,
        "worst_cross_module_diff": worst_cross,
        "t409_standing_note": (
            "T409 cited in its re-scoped, internally-established standing "
            "(hostile review 2026-07-02, survives-with-corrections)"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 3 -- temperature-blind frontier (free off)
# --------------------------------------------------------------------------- #

def temperature_blind_report() -> dict:
    frontiers = {}
    worst_spread = 0.0
    worst_closed_form = 0.0
    tables_match = True
    d_by_theta = {}
    u_cert_by_theta = {}
    for theta in THETA_SWEEP:
        per_beta = {}
        for beta in BETA_SWEEP:
            fr = frontier_for(theta, beta, False)
            per_beta[str(beta)] = fr
            for row in fr["per_n"]:
                for cell in row["rows"]:
                    worst_closed_form = max(
                        worst_closed_form,
                        abs(cell["achieved"] - cell["analytic"]),
                    )
        ref = per_beta[str(BETA_SWEEP[0])]
        for beta in BETA_SWEEP[1:]:
            fr = per_beta[str(beta)]
            if (
                fr["r_feas_by_n"] != ref["r_feas_by_n"]
                or fr["r_cert_by_n"] != ref["r_cert_by_n"]
            ):
                tables_match = False
            for row_a, row_b in zip(ref["per_n"], fr["per_n"]):
                for cell_a, cell_b in zip(row_a["rows"], row_b["rows"]):
                    worst_spread = max(
                        worst_spread,
                        abs(cell_a["achieved"] - cell_b["achieved"]),
                        abs(cell_a["bound"] - cell_b["bound"]),
                    )
        d_by_theta[f"{theta / math.pi:.2f}pi"] = ref["deficit_allowance_d"]
        u_cert_by_theta[f"{theta / math.pi:.2f}pi"] = ref[
            "min_certified_deficit_u"
        ]
        frontiers[f"{theta / math.pi:.2f}pi"] = {
            "r_feas_by_n": ref["r_feas_by_n"],
            "r_cert_by_n": ref["r_cert_by_n"],
            "d": ref["deficit_allowance_d"],
            "u_min_cert": ref["min_certified_deficit_u"],
            "beta_identical": tables_match,
        }
    return {
        "frontiers_free_off": frontiers,
        "worst_achieved_spread_across_beta": worst_spread,
        "worst_closed_form_residual": worst_closed_form,
        "integer_tables_beta_identical": tables_match,
        "d_by_theta": d_by_theta,
        "u_min_cert_by_theta": u_cert_by_theta,
        "law": (
            "f = |Tr[V_1 tau_beta V_0^dag]| = cos(theta/2) for every "
            "diagonal tau_beta (free terms off): departure at ANY "
            "temperature prices the same reach"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 4 -- certificate transfer, bands, dilation, attacks
# --------------------------------------------------------------------------- #

def certificate_transfer_report() -> dict:
    # (a) phi-certificate fires exactly where f = 0: theta = pi, free off,
    # every beta, every insufficient reach at n = 4.
    worst_cert_theta_pi = 0.0
    for beta in BETA_SWEEP:
        for r in range(ATTACK_N):
            worst_cert_theta_pi = max(
                worst_cert_theta_pi,
                phi_independence_cert(
                    ATTACK_N, tuple(range(1, r + 1)), math.pi, beta, False
                ),
            )
    # (b) degree-1 trigonometric reconstruction.
    recon = degree1_reconstruction_residual(3, (1,), 0.5 * math.pi, 1.0, False)
    # (c) bound = 2x achieved across a spread of cells (both toggles).
    worst_factor2 = 0.0
    for theta in THETA_SWEEP:
        for beta in (math.inf, 1.0, 0.0):
            for free_on in TOGGLES:
                for r in range(ATTACK_N + 1):
                    cell = frontier_cell(
                        ATTACK_N, tuple(range(1, r + 1)), theta, beta, free_on
                    )
                    worst_factor2 = max(
                        worst_factor2,
                        abs(cell["bound"] - 2.0 * cell["achieved"]),
                    )
    # (d) free-on theta = pi certified at every beta (bound <= 2 vis_A
    # |A_blk| = 0.617983 < v*, by convexity in (p0, p1)).
    free_on_pi = {}
    worst_free_on_bound = 0.0
    for beta in BETA_SWEEP:
        cell = frontier_cell(ATTACK_N, (1, 2, 3), math.pi, beta, True)
        free_on_pi[str(beta)] = {
            "f": branch_overlap_f(math.pi, beta, True),
            "bound_u1": cell["bound"],
            "band": cell["band"],
        }
        worst_free_on_bound = max(worst_free_on_bound, cell["bound"])
    # (e) dilation invariance: |0><0| AND Gibbs work ancillas.
    beta_dil = 1.0
    ret = (1, 2)
    cert_bare = phi_independence_cert(ATTACK_N, ret, math.pi, beta_dil, False)
    bound_bare = channel_bound(ATTACK_N, ret, math.pi, beta_dil, False)
    sig_pure = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    sig_gibbs = tau_gibbs(beta_dil)
    bound_pure = channel_bound(
        ATTACK_N, ret, math.pi, beta_dil, False,
        extra_sigmas=(sig_pure, sig_pure),
    )
    bound_gibbs = channel_bound(
        ATTACK_N, ret, math.pi, beta_dil, False,
        extra_sigmas=(sig_gibbs, sig_gibbs),
    )
    # cert with work registers adjoined (constant tensor factor).
    rhos = [
        dm_append(
            dm_append(
                prepare_retained(ATTACK_N, ret, phi, math.pi, beta_dil, False),
                sig_pure,
            ),
            sig_gibbs,
        )
        for phi in PHI_CERT
    ]
    cert_work = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            cert_work = max(
                cert_work, float(np.max(np.abs(rhos[i] - rhos[j])))
            )
    # frontier bounds with work adjoined, n = 4, all reach sizes.
    worst_frontier_work_diff = 0.0
    for theta in (0.5 * math.pi, math.pi):
        for r in range(ATTACK_N + 1):
            b0 = channel_bound(
                ATTACK_N, tuple(range(1, r + 1)), theta, beta_dil, False
            )
            b1 = channel_bound(
                ATTACK_N, tuple(range(1, r + 1)), theta, beta_dil, False,
                extra_sigmas=(sig_pure, sig_gibbs),
            )
            worst_frontier_work_diff = max(
                worst_frontier_work_diff, abs(b1 - b0)
            )
    # (f) attack battery on the predeclared undetermined-band cells.
    attacks = work_substitution_attacks()
    return {
        "worst_phi_cert_theta_pi_free_off": worst_cert_theta_pi,
        "degree1_reconstruction_residual": recon,
        "worst_bound_minus_2x_achieved": worst_factor2,
        "factor2_note": (
            "bound = 2x achieved in this family (block-off-diagonal X; "
            "||V_0 tau V_1^dag||_1 = 1) -- the same factor-2 looseness "
            "measured in T393/T408/T409, now at finite temperature; "
            "fourth artifact"
        ),
        "free_on_theta_pi": free_on_pi,
        "worst_free_on_theta_pi_bound_u1": worst_free_on_bound,
        "free_on_bound_ceiling_analytic": 2.0 * VIS_A_ANALYTIC * 0.312194,
        "dilation": {
            "phi_cert_bare": cert_bare,
            "phi_cert_with_work": cert_work,
            "bound_bare": bound_bare,
            "bound_with_pure_work": bound_pure,
            "bound_with_gibbs_work": bound_gibbs,
            "bound_pure_invariance_diff": abs(bound_pure - bound_bare),
            "bound_gibbs_invariance_diff": abs(bound_gibbs - bound_bare),
            "frontier_bound_max_diff_with_work": worst_frontier_work_diff,
            "lemma": (
                "any reach channel assisted by finitely many work registers "
                "in any (necessarily phi-independent) state IS a reach "
                "channel (Stinespring); adjoining a fixed sigma sends X to "
                "X (x) sigma with ||A (x) sigma||_1 = ||A||_1 -- the "
                "unlimited-work claim is carried by the lemma; the numerics "
                "assert two registers (one pure, one Gibbs), disclosed"
            ),
        },
        "attacks": attacks,
    }


def work_substitution_attacks() -> dict:
    """The fireable failure leg. Predeclared cells: theta = 0.5 pi (off),
    beta in {inf, 1.0, 0.0}, n = 4, retained prefixes r in {2, 3} -- all
    undetermined-by-bound, hence genuinely open pre-run. The leg fires
    iff any attack restores >= v* below r_feas."""
    rng = np.random.default_rng(HAAR_SEED)
    cells = []
    fired = False
    max_attack = 0.0
    for beta in ATTACK_BETAS:
        for r in ATTACK_REACH_SIZES:
            retained = tuple(range(1, r + 1))
            base = frontier_cell(ATTACK_N, retained, ATTACK_THETA, beta, False)
            manu_raw = raw_visibility(
                ATTACK_N, retained, manufactured_coherence_protocol,
                ATTACK_THETA, beta, False,
            )
            manu_locked = locked_visibility(
                ATTACK_N, retained, manufactured_coherence_protocol,
                ATTACK_THETA, beta, False,
            )
            feed = locked_visibility(
                ATTACK_N, retained,
                feedback_protocol(retained, ATTACK_THETA, False),
                ATTACK_THETA, beta, False,
            )
            # Haar battery on retained + two work registers (one |0>, one
            # Gibbs(beta)); illustrative -- sampling never carries an
            # impossibility verdict.
            sig_pure = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
            sig_gibbs = tau_gibbs(beta)
            n_active = 2 + r + 2
            dim = 2 ** n_active
            haar_best = 0.0
            haar_us = [haar_unitary(dim, rng) for _ in range(HAAR_SAMPLES)]
            for u_h in haar_us:
                def _attack(rho, _u=u_h):
                    out = dm_append(dm_append(rho, sig_pure), sig_gibbs)
                    return dm_apply(out, _u, tuple(range(n_active)))
                haar_best = max(
                    haar_best,
                    locked_visibility(
                        ATTACK_N, retained, _attack, ATTACK_THETA, beta, False
                    ),
                )
            cell_max = max(manu_locked, feed, haar_best)
            max_attack = max(max_attack, cell_max)
            crossed = cell_max >= V_STAR
            fired = fired or crossed
            cells.append(
                {
                    "beta": beta,
                    "reach": r,
                    "departed": ATTACK_N - r,
                    "band": base["band"],
                    "unwrite_achieved": base["achieved"],
                    "bound": base["bound"],
                    "manufactured_raw": manu_raw,
                    "manufactured_locked": manu_locked,
                    "feedback_locked": feed,
                    "haar_max_locked": haar_best,
                    "haar_samples": HAAR_SAMPLES,
                    "attack_crossed_v_star": crossed,
                }
            )
    return {
        "theta_over_pi": ATTACK_THETA / math.pi,
        "seed": HAAR_SEED,
        "cells": cells,
        "max_attack_visibility": max_attack,
        "work_substitution_observed": fired,
        "scope_note": (
            "fireable only in the undetermined band; in certified cells "
            "the substitution is excluded by the bound (disclosed pre-run "
            "in the spec -- the T409 predeclaration-theater lesson); "
            "illustrative sampling, the certificates carry every "
            "impossibility verdict"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 5 -- restoration work (branch selection B1/B2/B3)
# --------------------------------------------------------------------------- #

def restoration_work_report() -> dict:
    rows = []
    worst_law = 0.0
    worst_roundtrip = 0.0
    worst_closed_form = 0.0
    any_positive_w_fwd = False
    for theta in THETA_SWEEP:
        for beta in BETA_SWEEP:
            for free_on in TOGGLES:
                led = stream_ledger(
                    LEDGER_N, tuple(range(1, LEDGER_N + 1)), theta, beta,
                    free_on,
                )
                rest = led["restoration"]
                w_rest = rest["W_rest"]
                w_analytic = rest["W_rest_analytic"]
                worst_law = max(worst_law, abs(w_rest - w_analytic))
                worst_roundtrip = max(
                    worst_roundtrip, rest["roundtrip_work_per_contact_max_abs"]
                )
                if not free_on:
                    worst_closed_form = max(
                        worst_closed_form,
                        abs(
                            led["w_fwd_analytic"]
                            - w_fwd_closed_form_free_off(theta, beta)
                        ),
                    )
                if led["w_fwd_analytic"] > 1e-6:
                    any_positive_w_fwd = True
                rows.append(
                    {
                        "theta_over_pi": theta / math.pi,
                        "beta": beta,
                        "free_on": free_on,
                        "w_fwd": led["w_fwd_analytic"],
                        "W_rest": w_rest,
                        "W_rest_analytic": w_analytic,
                        "uncopy_work": rest["uncopy_work"],
                    }
                )
    # W_rest scaling in n at the reference point (theta = pi, beta = 1, off).
    scaling = []
    for n in range(1, N_ANC_MAX + 1):
        led = stream_ledger(n, tuple(range(1, n + 1)), math.pi, 1.0, False)
        scaling.append(led["restoration"]["W_rest"])
    slope = (scaling[-1] - scaling[0]) / (N_ANC_MAX - 1)

    refund_law_holds = worst_law < ANALYTIC_TOL
    flat = all(abs(r["W_rest"]) < 1e-9 for r in rows)
    positive_slope = slope > 1e-9
    if refund_law_holds and any_positive_w_fwd and not flat and not positive_slope:
        branch = "B3_restoration_work_refund"
        headline = (
            "restoration within reach REFUNDS the forward switching work "
            "exactly (unitary undo); the genuine work/entropy scaling with "
            "bath contact lives in the forward writing cost (linear in n, "
            "slope w_fwd(theta, beta)) and in the per-departed-contact "
            "entropy production locked in at departure; net round-trip "
            "work per retained contact exactly zero; the frontier's "
            "currency remains reach"
        )
    elif flat:
        branch = "B2_restoration_work_flat"
        headline = (
            "restoration is thermodynamically free given reach; work "
            "strictly orthogonal to reach (B2 fired -- reported, headline "
            "switched per the predeclared branch table)"
        )
    else:
        branch = "B1_restoration_work_positive_slope"
        headline = (
            "restoration cost acquires genuine work scaling with bath "
            "contact (B1 fired -- reported, headline switched per the "
            "predeclared branch table)"
        )
    return {
        "rows": rows,
        "worst_refund_law_residual": worst_law,
        "worst_roundtrip_work": worst_roundtrip,
        "worst_free_off_closed_form_residual": worst_closed_form,
        "W_rest_by_n_reference": scaling,
        "W_rest_slope_in_n_reference": slope,
        "w_fwd_reference_theta_pi_beta_inf": w_fwd_analytic(
            math.pi, math.inf, False
        ),
        "branch_selected": branch,
        "headline": headline,
    }


# --------------------------------------------------------------------------- #
# Legs 6 + 7 -- zero-bit contacts and thermal complementarity
# --------------------------------------------------------------------------- #

def _branch_block_states(
    n: int, u: int, theta: float, beta: float, free_on: bool,
    phi: float = 0.0,
):
    """Branch probabilities and branch-conditional states of the last-u
    carrier block, on a diagnostic full-retention run (pre-departure)."""
    rho = prepare_retained(
        n, tuple(range(1, n + 1)), phi, theta, beta, free_on
    )
    m = int(round(math.log2(rho.shape[0])))
    block = tuple(range(m - u, m))
    probs, states = [], []
    for b, proj in ((0, _P0), (1, _P1)):
        pb_rho = dm_kraus(rho, [proj], (S_POS,))
        pb = float(np.real(np.trace(pb_rho)))
        probs.append(pb)
        states.append(dm_ptrace(pb_rho / pb, block))
    return probs, states


def _holevo_bits(probs, states) -> float:
    mix = probs[0] * states[0] + probs[1] * states[1]
    return vn_entropy_bits(mix) - sum(
        p * vn_entropy_bits(s) for p, s in zip(probs, states)
    )


def zero_bit_contacts_report() -> dict:
    """Leg 6: at theta = pi (free off) the escaped Holevo content FALLS
    with temperature -- exactly 0 at beta = 0, where every carrier
    marginal is I/2 and the branch blocks are identical -- while the
    frontier does not move."""
    n = LEDGER_N
    chi_table = {}
    for beta in BETA_SWEEP:
        per_u = []
        for u in range(1, n + 1):
            probs, states = _branch_block_states(n, u, math.pi, beta, False)
            per_u.append(_holevo_bits(probs, states))
        chi_table[str(beta)] = per_u
    chi1_closed = {str(b): chi1_closed_form(b) for b in BETA_SWEEP}
    worst_chi1 = max(
        abs(chi_table[str(b)][0] - chi1_closed[str(b)]) for b in BETA_SWEEP
    )
    # beta = 0 corner: marginals and branch blocks.
    rho0 = prepare_retained(
        n, tuple(range(1, n + 1)), 1.0, math.pi, 0.0, False
    )
    m = int(round(math.log2(rho0.shape[0])))
    worst_marginal = 0.0
    half = np.eye(2, dtype=complex) / 2.0
    for pos in range(2, m):
        marg = dm_ptrace(rho0, (pos,))
        worst_marginal = max(worst_marginal, float(np.max(np.abs(marg - half))))
    probs0, states0 = _branch_block_states(n, n, math.pi, 0.0, False)
    branch_block_diff = float(np.max(np.abs(states0[0] - states0[1])))
    chi_beta0_max = max(chi_table["0.0"])
    # frontier persists at beta = 0 (theta = pi, off).
    fr0 = frontier_for(math.pi, 0.0, False)
    fr_inf = frontier_for(math.pi, math.inf, False)
    return {
        "scenario_n": n,
        "chi_bits_by_beta_then_u": chi_table,
        "chi1_closed_form_by_beta": chi1_closed,
        "worst_chi1_closed_form_residual": worst_chi1,
        "h2_3_7_bits": H2_3_7,
        "chi_beta0_max": chi_beta0_max,
        "beta0_worst_single_marginal_vs_half": worst_marginal,
        "beta0_branch_block_diff": branch_block_diff,
        "beta0_frontier_r_feas": fr0["r_feas_by_n"],
        "beta0_frontier_r_cert": fr0["r_cert_by_n"],
        "beta_inf_frontier_r_feas": fr_inf["r_feas_by_n"],
        "finding": (
            "contacts, not bits, sharpened: at beta = 0 every departed "
            "carrier holds EXACTLY zero locally readable record (marginal "
            "I/2, branch blocks identical, Holevo 0) and the record lives "
            "only in joint coherences between retained and departed "
            "registers -- 'which register holds the record bits' has no "
            "answer -- while r_feas = r_cert = n persists (f = 0 for "
            "every diagonal tau). Flagged from memory, unverified: "
            "mixed/hazy-environment quantum Darwinism (Zwolak-Quan-Zurek "
            "lineage); discord-type locally-hidden correlations."
        ),
    }


def complementarity_report() -> dict:
    """Leg 7: deficit >= D_u^2 with equality iff beta = inf (the
    EGY-duality corner, named); D_1 = sin(theta/2) tanh(beta/2)."""
    n = LEDGER_N
    rows = []
    worst_d1 = 0.0
    min_gap = math.inf
    worst_equality_at_inf = 0.0
    for theta in (0.5 * math.pi, math.pi):
        for beta in BETA_SWEEP:
            for u in range(0, n + 1):
                retained = tuple(range(1, n - u + 1))
                achieved = locked_visibility(
                    n, retained, unwrite_protocol(retained, theta, False),
                    theta, beta, False,
                )
                deficit = 1.0 - (achieved / VIS_A_ANALYTIC) ** 2
                if u == 0:
                    d_u = 0.0
                else:
                    _, states = _branch_block_states(n, u, theta, beta, False)
                    d_u = trace_distance(states[0], states[1])
                gap = deficit - d_u ** 2
                min_gap = min(min_gap, gap)
                if math.isinf(beta):
                    worst_equality_at_inf = max(worst_equality_at_inf, abs(gap))
                if u == 1:
                    worst_d1 = max(
                        worst_d1, abs(d_u - d1_closed_form(theta, beta))
                    )
                rows.append(
                    {
                        "theta_over_pi": theta / math.pi,
                        "beta": beta,
                        "departed_u": u,
                        "achieved": achieved,
                        "capability_deficit": deficit,
                        "displaced_D_u": d_u,
                        "gap_deficit_minus_D2": gap,
                    }
                )
    return {
        "scenario_n": n,
        "rows": rows,
        "worst_D1_closed_form_residual": worst_d1,
        "min_gap_deficit_minus_D2": min_gap,
        "worst_equality_residual_at_beta_inf": worst_equality_at_inf,
        "note": (
            "equality at beta = inf is the Englert-Greenberger-Yasin "
            "duality corner (named per the T409 hostile-review prior-art "
            "completion; from memory, unverified). The thermal gap at "
            "finite beta is leg 6 in trace-distance form: the capability "
            "deficit is temperature-blind, the locally readable record "
            "is not."
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 8 -- Landauer ledger (T142 conventions at real beta)
# --------------------------------------------------------------------------- #

def landauer_report() -> dict:
    n = LEDGER_N
    theta = math.pi
    retained = tuple(range(1, n + 1))
    holder_pos = (REC_POS,) + retained_positions(retained)
    per_beta = {}
    for beta in LEDGER_HOLDER_BETAS:
        led = stream_ledger(n, retained, theta, beta, False)
        vis_full = locked_visibility(
            n, retained, unwrite_protocol(retained, theta, False),
            theta, beta, False,
        )
        # blind reset
        reset = blind_reset_protocol(holder_pos)
        vis_reset = locked_visibility(n, retained, reset, theta, beta, False)
        rho = prepare_retained(n, retained, 1.0, theta, beta, False)
        branch_states = []
        for proj in (_P0, _P1):
            pb_rho = dm_kraus(rho, [proj], (S_POS,))
            pb = float(np.real(np.trace(pb_rho)))
            after = reset(pb_rho / pb)
            branch_states.append(dm_ptrace(after, holder_pos))
        residual = trace_distance(branch_states[0], branch_states[1])
        joint_bits = vn_entropy_bits(dm_ptrace(rho, holder_pos))
        per_holder_bits = [
            vn_entropy_bits(dm_ptrace(rho, (p,))) for p in holder_pos
        ]
        per_beta[str(beta)] = {
            "restore_within_reach": {
                "mode": "correlated_uncopy",
                "holders": len(holder_pos),
                "erased_bits": 0,
                "landauer_floor_nats": 0.0,
                "computed_W_rest": led["restoration"]["W_rest"],
                "achieved_locked_visibility": vis_full,
                "note": (
                    "a work refund is consistent with a floor of zero: "
                    "nothing is erased (records returned to source, "
                    "carriers to tau_beta)"
                ),
            },
            "blind_reset": {
                "mode": "blind_reset",
                "erased_bits_naive_per_holder": len(holder_pos),
                "beta_work_floor_naive_nats": landauer_bound_bits(
                    len(holder_pos)
                ),
                "joint_record_bits_given_M0": joint_bits,
                "per_holder_marginal_bits": per_holder_bits,
                "capability_after_reset": vis_reset,
                "residual_branch_distinguishability": residual,
                "deletion_is_not_definalization": bool(
                    vis_reset < FLATNESS_TOL and residual < FLATNESS_TOL
                ),
            },
            "heat_per_collision": led["collisions"][0]["Q_i"],
        }
    # beyond the frontier: n = 4, reach 2 (< frontier 4), theta = pi.
    short = (1, 2)
    beyond = {
        "scenario": "n = 4 perfect contacts, reach 2 of 4, theta = pi",
        "feasible_at_reach": False,
        "certificates": {
            "phi_independence": phi_independence_cert(
                n, short, theta, 1.0, False
            ),
            "channel_bound": channel_bound(n, short, theta, 1.0, False),
        },
        "min_cost_convention": "inf (infimum over an empty feasible set)",
        "min_work": INFINITE_COST,
        "typing": (
            "ACCESS-not-work: a work parameter now EXISTS in this model "
            "and is computed to be unable to substitute (leg 4); the "
            "infinity is still not a work divergence -- departed carriers "
            "are outside the support of every retained-reach channel"
        ),
    }
    return {
        "scenario": {"n": n, "theta_over_pi": 1.0, "holders": len(holder_pos)},
        "landauer_nat_per_bit": LANDAUER_NAT_PER_BIT,
        "per_beta": per_beta,
        "restore_beyond_frontier": beyond,
        "scope": (
            "T142-convention bookkeeping generalized to real beta; "
            "exact-identity-backed at the computed states; NOT a "
            "thermodynamic theorem"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 9 -- guardrails (Q1D with teeth; R1 untouched)
# --------------------------------------------------------------------------- #

def _sm_z_distribution(rho_sm: np.ndarray) -> np.ndarray:
    return np.real(np.diag(rho_sm))


def q1d_report() -> dict:
    # Declared ordinary record P(S, M): invariant across beta, theta,
    # toggle, n (collisions never touch S or M) -- computed on the
    # UNCONDITIONED streamed state.
    ref = _sm_z_distribution(dm_ptrace(core_full_dm(1.0), (0, 1)))
    configs = (
        (4, math.pi, math.inf, False),
        (4, 0.5 * math.pi, 1.0, True),
        (5, 0.25 * math.pi, 0.0, False),
        (2, math.pi, 0.5, True),
    )
    worst_record = 0.0
    for n, theta, beta, free_on in configs:
        rho = core_full_dm(1.0)  # S, M, REC
        tau_b = tau_gibbs(beta)
        u = collision_u(theta, free_on)
        for i in range(n):
            m = int(round(math.log2(rho.shape[0])))
            rho = dm_append(rho, tau_b)
            rho = dm_apply(rho, u, (2, m))  # REC at position 2 here
            rho = dm_ptrace(rho, tuple(range(m)))  # all depart (worst case)
        dist = _sm_z_distribution(dm_ptrace(rho, (0, 1)))
        worst_record = max(worst_record, float(np.max(np.abs(dist - ref))))

    # No signalling out of reach + teeth, on the pre-trace joint state.
    n = LEDGER_N
    theta = math.pi
    teeth_rows = {}
    worst_no_signal = 0.0
    worst_teeth_residual = 0.0
    for beta in (math.inf, 1.0, 0.0):
        rho = prepare_retained(n, tuple(range(1, n + 1)), 1.0, theta, beta, False)
        m = int(round(math.log2(rho.shape[0])))
        outside = m - 1  # B4: outside the reach-2 protocol's support
        before = dm_ptrace(rho, (outside,))
        after_reach = dm_ptrace(
            unwrite_protocol((1, 2), theta, False)(rho), (outside,)
        )
        after_enlarged = dm_ptrace(
            unwrite_protocol(tuple(range(1, n + 1)), theta, False)(rho),
            (outside,),
        )
        no_signal = float(np.max(np.abs(before - after_reach)))
        teeth = float(np.max(np.abs(before - after_enlarged)))
        teeth_analytic = BRANCH1_WEIGHT * _tanh_half(beta)
        worst_no_signal = max(worst_no_signal, no_signal)
        worst_teeth_residual = max(
            worst_teeth_residual, abs(teeth - teeth_analytic)
        )
        teeth_rows[str(beta)] = {
            "no_signal_out_reach_protocol": no_signal,
            "enlarged_protocol_moves_outside_marginal": teeth,
            "teeth_analytic_3_7_tanh": teeth_analytic,
        }
    # beta = 0 tooth carried by the visibility jump (marginal blindness).
    vis_r3 = locked_visibility(
        n, (1, 2, 3), unwrite_protocol((1, 2, 3), theta, False),
        theta, 0.0, False,
    )
    vis_r4 = locked_visibility(
        n, tuple(range(1, n + 1)),
        unwrite_protocol(tuple(range(1, n + 1)), theta, False),
        theta, 0.0, False,
    )
    return {
        "declared_record_invariance": worst_record,
        "teeth_by_beta": teeth_rows,
        "worst_no_signal_out": worst_no_signal,
        "worst_teeth_closed_form_residual": worst_teeth_residual,
        "beta0_visibility_jump": {
            "achieved_reach_3_of_4": vis_r3,
            "achieved_reach_4_of_4": vis_r4,
            "note": (
                "at beta = 0 the marginal tooth vanishes (leg-6 marginal "
                "blindness); the tooth is the restored-visibility jump"
            ),
        },
        "r1_note": (
            "R1 untouched: no claim about global temporal order or "
            "spacetime; the collision stream is a discrete interaction "
            "sequence, and the frontier is a reach frontier through the "
            "bath, not a light cone (Lieb-Robinson is a named absorber "
            "risk, flagged from memory, unverified)"
        ),
    }


# --------------------------------------------------------------------------- #
# Discipline: exhaustive subsets and symmetry pruning
# --------------------------------------------------------------------------- #

def exhaustive_report() -> dict:
    """ALL 2^n retained subsets for n <= 3, at every sweep point: values
    depend only on subset SIZE; the exhaustive frontier equals the
    canonical-prefix frontier."""
    worst_spread = 0.0
    mismatches = 0
    blocks = []
    for theta in THETA_SWEEP:
        for beta in BETA_SWEEP:
            for free_on in TOGGLES:
                for n in EXHAUSTIVE_N:
                    by_size = {}
                    for r in range(n + 1):
                        cells = [
                            frontier_cell(n, sub, theta, beta, free_on)
                            for sub in combinations(range(1, n + 1), r)
                        ]
                        for keyname in ("achieved", "bound"):
                            vals = [c[keyname] for c in cells]
                            worst_spread = max(
                                worst_spread, max(vals) - min(vals)
                            )
                        by_size[r] = cells[0]
                    r_feas_ex = next(
                        (
                            r
                            for r in range(n + 1)
                            if by_size[r]["achieved"] >= V_STAR
                        ),
                        None,
                    )
                    f = branch_overlap_f(theta, beta, free_on)
                    d = deficit_allowance(f)
                    expected = max(0, n - d)
                    if r_feas_ex != expected:
                        mismatches += 1
                    blocks.append(
                        {
                            "theta_over_pi": theta / math.pi,
                            "beta": beta,
                            "free_on": free_on,
                            "n": n,
                            "subsets_checked": 2 ** n,
                            "r_feas_exhaustive": r_feas_ex,
                            "r_feas_analytic": expected,
                        }
                    )
    return {
        "worst_same_size_spread": worst_spread,
        "frontier_mismatches": mismatches,
        "blocks_checked": len(blocks),
        "subsets_per_block_total": sum(b["subsets_checked"] for b in blocks),
        "blocks": blocks[:12],  # sample rows for the JSON; all asserted
    }


def symmetry_report() -> dict:
    """Pruning justification at n = 4, 5 (predeclared pairs): permuted
    same-size retained subsets have IDENTICAL retained states."""
    pairs = {
        5: [
            ((1,), (3,)),
            ((1,), (5,)),
            ((1, 2), (2, 4)),
            ((1, 2), (3, 5)),
            ((1, 2, 3, 4), (2, 3, 4, 5)),
        ],
        4: [((1, 2), (2, 4))],
    }
    points = (
        (0.5 * math.pi, 1.0, False),
        (0.5 * math.pi, 1.0, True),
        (math.pi, 0.5, False),
        (0.25 * math.pi, math.inf, True),
    )
    worst = 0.0
    count = 0
    for n, subset_pairs in pairs.items():
        for canonical, permuted in subset_pairs:
            for theta, beta, free_on in points:
                for phi in (1.0, math.pi / 3.0):
                    rho_c = prepare_retained(
                        n, canonical, phi, theta, beta, free_on
                    )
                    rho_p = prepare_retained(
                        n, permuted, phi, theta, beta, free_on
                    )
                    worst = max(worst, float(np.max(np.abs(rho_c - rho_p))))
                    count += 1
    return {
        "pairs_compared": count,
        "ns": sorted(pairs),
        "max_state_diff": worst,
    }


def construction_report() -> dict:
    """expm vs analytic REC-block construction; Gibbs corners; P(M=0)."""
    worst = 0.0
    for theta in THETA_SWEEP:
        for free_on in TOGGLES:
            u_e, u_b = collision_unitary(theta, free_on)
            worst = max(
                worst,
                float(
                    np.max(
                        np.abs(
                            np.array(u_e, dtype=complex)
                            - np.array(u_b, dtype=complex)
                        )
                    )
                ),
            )
    gate_diff = float(
        np.max(np.abs(collision_u(math.pi, False) - _controlled(_ry(math.pi))))
    )
    tau_inf = tau_gibbs(math.inf)
    tau_zero = tau_gibbs(0.0)
    probs = [core_conditioned(phi)[1] for phi in PHI_CERT]
    return {
        "worst_expm_vs_block": worst,
        "free_off_equals_controlled_ry": gate_diff,
        "tau_inf_is_ground": float(np.max(np.abs(tau_inf - _P0))),
        "tau_zero_is_maximally_mixed": float(
            np.max(np.abs(tau_zero - _I2 / 2.0))
        ),
        "p_m0_values": probs,
        "worst_p_m0_deviation": max(abs(p - P_M0) for p in probs),
        "scipy_note": (
            "first scipy use in models/ (scipy.linalg.expm), disclosed in "
            "the spec; asserted against the analytic block construction"
        ),
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

_ANALYSIS_CACHE: dict = {}


def run_analysis() -> dict:
    construction = construction_report()
    first_law = first_law_report()
    regression = regression_report()
    temperature_blind = temperature_blind_report()
    certificates = certificate_transfer_report()
    restoration = restoration_work_report()
    zero_bit = zero_bit_contacts_report()
    complementarity = complementarity_report()
    landauer = landauer_report()
    q1d = q1d_report()
    exhaustive = exhaustive_report()
    symmetry = symmetry_report()
    purification = purification_check()

    leg1 = (
        first_law["worst_interior_conservation"] < FLATNESS_TOL
        and first_law["worst_work_convention_agreement_free_on"]
        < FLATNESS_TOL
        and first_law["worst_sigma_identity_residual"] < IDENTITY_TOL
        and first_law["min_sigma_over_sweep"] >= SIGMA_NONNEG_TOL
        and first_law["worst_global_balance_residual"] < IDENTITY_TOL
        and first_law["worst_wq_spread_across_collisions"] < FLATNESS_TOL
        and first_law["worst_ledger_phi_dependence"] < FLATNESS_TOL
    )
    leg2 = (
        regression["gate_equals_controlled_ry_max_diff"] < FLATNESS_TOL
        and regression["r_feas_by_n"] == list(range(1, N_ANC_MAX + 1))
        and regression["r_cert_by_n"] == list(range(1, N_ANC_MAX + 1))
        and regression["worst_insufficient_phi_cert"] < FLATNESS_TOL
        and regression["worst_insufficient_bound"] < FLATNESS_TOL
        and all(
            abs(v - VIS_A_ANALYTIC) < ANALYTIC_TOL
            for v in regression["full_reach_restores"]
        )
        and regression["worst_cross_module_diff"] < ANALYTIC_TOL
    )
    leg3 = (
        temperature_blind["worst_achieved_spread_across_beta"] < SPREAD_TOL
        and temperature_blind["worst_closed_form_residual"] < ANALYTIC_TOL
        and temperature_blind["integer_tables_beta_identical"]
        and temperature_blind["d_by_theta"]
        == {"0.25pi": 1, "0.50pi": 0, "1.00pi": 0}
        and temperature_blind["u_min_cert_by_theta"]
        == {"0.25pi": 10.0, "0.50pi": 3.0, "1.00pi": 1.0}
    )
    attacks = certificates["attacks"]
    leg4 = (
        certificates["worst_phi_cert_theta_pi_free_off"] < FLATNESS_TOL
        and certificates["degree1_reconstruction_residual"] < FLATNESS_TOL
        and certificates["worst_bound_minus_2x_achieved"] < ANALYTIC_TOL
        and certificates["worst_free_on_theta_pi_bound_u1"] < V_STAR
        and certificates["dilation"]["phi_cert_with_work"] < FLATNESS_TOL
        and certificates["dilation"]["bound_pure_invariance_diff"]
        < FLATNESS_TOL
        and certificates["dilation"]["bound_gibbs_invariance_diff"]
        < FLATNESS_TOL
        and certificates["dilation"]["frontier_bound_max_diff_with_work"]
        < FLATNESS_TOL
        and all(
            c["manufactured_raw"] > 0.99
            and c["manufactured_locked"] < FLATNESS_TOL
            and c["feedback_locked"] < FLATNESS_TOL
            for c in attacks["cells"]
        )
    )
    leg5 = (
        restoration["worst_refund_law_residual"] < ANALYTIC_TOL
        and restoration["worst_roundtrip_work"] < IDENTITY_TOL
        and restoration["worst_free_off_closed_form_residual"] < ANALYTIC_TOL
    )
    leg6 = (
        zero_bit["worst_chi1_closed_form_residual"] < ANALYTIC_TOL
        and zero_bit["chi_beta0_max"] < FLATNESS_TOL
        and zero_bit["beta0_worst_single_marginal_vs_half"] < FLATNESS_TOL
        and zero_bit["beta0_branch_block_diff"] < FLATNESS_TOL
        and zero_bit["beta0_frontier_r_feas"]
        == zero_bit["beta_inf_frontier_r_feas"]
        and all(
            abs(zero_bit["chi_bits_by_beta_then_u"]["inf"][u - 1] - H2_3_7)
            < ANALYTIC_TOL
            for u in range(1, LEDGER_N + 1)
        )
    )
    leg7 = (
        complementarity["worst_D1_closed_form_residual"] < ANALYTIC_TOL
        and complementarity["min_gap_deficit_minus_D2"] >= SIGMA_NONNEG_TOL
        and complementarity["worst_equality_residual_at_beta_inf"]
        < ANALYTIC_TOL
    )
    leg8 = all(
        entry["restore_within_reach"]["erased_bits"] == 0
        and entry["restore_within_reach"]["achieved_locked_visibility"]
        >= V_STAR
        and entry["blind_reset"]["capability_after_reset"] < FLATNESS_TOL
        and entry["blind_reset"]["residual_branch_distinguishability"]
        < FLATNESS_TOL
        and entry["blind_reset"]["deletion_is_not_definalization"]
        for entry in landauer["per_beta"].values()
    ) and (
        landauer["restore_beyond_frontier"]["certificates"][
            "phi_independence"
        ]
        < FLATNESS_TOL
        and math.isinf(landauer["restore_beyond_frontier"]["min_work"])
    )
    leg9 = (
        q1d["declared_record_invariance"] < FLATNESS_TOL
        and q1d["worst_no_signal_out"] < FLATNESS_TOL
        and q1d["worst_teeth_closed_form_residual"] < ANALYTIC_TOL
        and abs(
            q1d["teeth_by_beta"]["inf"][
                "enlarged_protocol_moves_outside_marginal"
            ]
            - 3.0 / 7.0
        )
        < ANALYTIC_TOL
    )
    discipline = (
        exhaustive["worst_same_size_spread"] < SPREAD_TOL
        and exhaustive["frontier_mismatches"] == 0
        and symmetry["max_state_diff"] < FLATNESS_TOL
        and purification["max_diff"] < IDENTITY_TOL
        and construction["worst_expm_vs_block"] < FLATNESS_TOL
        and construction["worst_p_m0_deviation"] < FLATNESS_TOL
    )

    failure_legs = {
        "work_substitutes_for_reach_at_finite_temperature": {
            "fired": bool(attacks["work_substitution_observed"]),
            "max_attack_visibility": attacks["max_attack_visibility"],
            "scope": attacks["scope_note"],
        },
        "restoration_work_positive_slope": {
            "fired": restoration["branch_selected"]
            == "B1_restoration_work_positive_slope",
        },
        "restoration_work_flat": {
            "fired": restoration["branch_selected"]
            == "B2_restoration_work_flat",
        },
        "thermal_frontier_collapse": {
            "fired": not (
                temperature_blind["integer_tables_beta_identical"]
                and temperature_blind["worst_achieved_spread_across_beta"]
                < SPREAD_TOL
            ),
        },
        "entropy_production_violation": {
            "fired": first_law["min_sigma_over_sweep"] < SIGMA_NONNEG_TOL,
            "halting": True,
        },
        "t409_regression_failure": {"fired": not leg2, "halting": True},
    }

    legs = {
        "leg1_first_law_entropy_production": leg1,
        "leg2_t409_regression_corner": leg2,
        "leg3_temperature_blind_frontier": leg3,
        "leg4_certificate_transfer_bands": leg4,
        "leg5_restoration_work_refund": leg5,
        "leg6_zero_bit_contacts": leg6,
        "leg7_thermal_complementarity": leg7,
        "leg8_landauer_ledger": leg8,
        "leg9_guardrails": leg9,
        "discipline_exhaustive_symmetry_purification": discipline,
    }
    halting_fired = any(
        v.get("halting") and v["fired"] for v in failure_legs.values()
    )
    reportable_fired = [
        k for k, v in failure_legs.items() if v["fired"]
    ]
    frontier_holds = all(legs.values()) and not halting_fired

    if frontier_holds and not reportable_fired:
        verdict_language = (
            "the thermal-collision work-reach frontier holds in this "
            "finite repeated-interaction family: the switched-Hamiltonian "
            "Gibbs-ancilla stream reproduces T409's frontier exactly at "
            "its zero-temperature free-off corner and extends it with a "
            "genuine work parameter, temperature, heat, and entropy "
            "production (first law and the Sigma identity "
            "exact-identity-backed at the computed states); with free "
            "terms off the frontier is temperature-blind (departure at "
            "any temperature prices the same reach, r_feas = r_cert = n "
            "at theta = pi at every beta including beta = 0, where every "
            "departed carrier holds exactly zero locally readable record "
            "bits); both certificates transfer to mixed thermal states "
            "and are invariant under work registers in any -- necessarily "
            "phi-independent -- state, pure or Gibbs; restoration within "
            "reach is a work REFUND (round-trip work per retained contact "
            "exactly zero) while forward contact costs work and locks in "
            "entropy production at departure -- the work/entropy scaling "
            "with bath contact demanded by the named-unbuilt card is "
            "computed, and it prices CONTACT and DEPARTURE, not "
            "restoration-within-reach: the frontier's currency remains "
            "reach. The boundary is physical GIVEN the repeated-"
            "interaction reservoir idealization, which is adopted, not "
            "derived; the continuum/transport rung -- work literally "
            "buying reach -- stays named-unbuilt. Bookkeeping, not a "
            "thermodynamic theorem; finite-witness; no claim promotion; "
            "no CLAIM-LEDGER entry; ledger actions pause for Joe per "
            "AGENTS.md."
        )
    else:
        verdict_language = (
            "the thermal-collision work-reach frontier FAILS or a "
            "predeclared failure leg fired in this finite family: "
            f"failed legs {sorted(k for k, v in legs.items() if not v)}, "
            f"fired failure legs {sorted(reportable_fired)}. Report the "
            "failing leg exactly as the finding (a fired work-substitution "
            "or branch-switch leg is the headline, not a defect); halting "
            "legs (entropy_production_violation, t409_regression_failure) "
            "mean a bookkeeping or translation defect: halt and report, "
            "claim nothing. Do not weaken assertions to pass. No claim "
            "promotion; ledger actions pause for Joe. The continuum/"
            "transport rung stays named-unbuilt."
        )

    return {
        "artifact": "T410-thermal-collision-work-reach-frontier-v0.1",
        "labeling_convention": (
            "retained density matrix ordered (S, REC, retained carriers "
            "in collision order); M measured, M = 0 selected, removed "
            "(pure, factorized); carriers DEPART (partial trace) after "
            "their collision unless retained"
        ),
        "theta_meter": THETA_METER,
        "v_star": V_STAR,
        "vis_A_analytic": VIS_A_ANALYTIC,
        "tau_window": TAU,
        "hamiltonians": (
            "H_REC = H_B = omega |1><1| (hbar = omega = 1); H_S = H_M = 0 "
            "(declared assignment, disclosed); H_int = g |1><1|_REC (x) "
            "sigma_y, g = theta/(2 tau), switched at window endpoints"
        ),
        "beta_sweep": [str(b) for b in BETA_SWEEP],
        "theta_sweep_over_pi": [t / math.pi for t in THETA_SWEEP],
        "construction": construction,
        "purification_check": purification,
        "first_law": first_law,
        "regression": regression,
        "temperature_blind": temperature_blind,
        "certificates": certificates,
        "restoration_work": restoration,
        "zero_bit_contacts": zero_bit,
        "complementarity": complementarity,
        "landauer": landauer,
        "q1d": q1d,
        "exhaustive": exhaustive,
        "symmetry": symmetry,
        "legs": legs,
        "failure_legs": failure_legs,
        "verdict_tags": list(VERDICT_TAGS),
        "thermal_work_reach_frontier_holds": frontier_holds,
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
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


if __name__ == "__main__":
    import json
    import time

    t0 = time.time()
    res = run_analysis()
    elapsed = time.time() - t0
    print(json.dumps(_json_safe(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T410 Thermal Collision Work-Reach Frontier")
    print("=" * 70)
    print(f"model wall time: {elapsed:.1f} s (predeclared budget < 300 s)")
    reg = res["regression"]
    print("Leg 2 -- T409 regression corner (beta = inf, off, theta = pi):")
    print(f"  gate = controlled-Ry diff: {reg['gate_equals_controlled_ry_max_diff']:.1e}")
    print(f"  r_feas: {reg['r_feas_by_n']}  r_cert: {reg['r_cert_by_n']}")
    print(f"  worst cross-module diff vs T409: {reg['worst_cross_module_diff']:.2e}")
    tb = res["temperature_blind"]
    print("Leg 3 -- temperature-blind frontier (free off):")
    for label, table in tb["frontiers_free_off"].items():
        print(f"  theta {label}: d={table['d']}, u_min_cert={table['u_min_cert']}, "
              f"r_feas={table['r_feas_by_n']}, r_cert={table['r_cert_by_n']}")
    print(f"  worst achieved spread across beta: "
          f"{tb['worst_achieved_spread_across_beta']:.2e}")
    fl = res["first_law"]
    print("Leg 1 -- first law + entropy production:")
    print(f"  worst Sigma-identity residual: "
          f"{fl['worst_sigma_identity_residual']:.2e}; min Sigma: "
          f"{fl['min_sigma_over_sweep']:.2e}")
    print(f"  worst global balance residual: "
          f"{fl['worst_global_balance_residual']:.2e}")
    rw = res["restoration_work"]
    print("Leg 5 -- restoration work:")
    print(f"  branch selected: {rw['branch_selected']}")
    print(f"  W_rest by n (theta=pi, beta=1, off): "
          f"{[f'{w:.4f}' for w in rw['W_rest_by_n_reference']]}")
    print(f"  w_fwd(pi, inf) = {rw['w_fwd_reference_theta_pi_beta_inf']:.6f} "
          f"(3/7 = {3/7:.6f})")
    zb = res["zero_bit_contacts"]
    print("Leg 6 -- zero-bit contacts:")
    print(f"  chi(beta=inf, u>=1) ~ h2(3/7) = {H2_3_7:.6f} bits; "
          f"chi(beta=0) max = {zb['chi_beta0_max']:.1e}")
    print(f"  beta=0 frontier r_feas: {zb['beta0_frontier_r_feas']}")
    at = res["certificates"]["attacks"]
    print(f"Leg 4 -- work-substitution attacks (fireable cells): fired = "
          f"{at['work_substitution_observed']}, max = "
          f"{at['max_attack_visibility']:.4f}")
    print("-" * 70)
    print(f"LEGS: {res['legs']}")
    print(f"FAILURE LEGS FIRED: "
          f"{[k for k, v in res['failure_legs'].items() if v['fired']]}")
    print(f"THERMAL WORK-REACH FRONTIER HOLDS: "
          f"{res['thermal_work_reach_frontier_holds']}")
    print(res["verdict_language"])
# end of module
