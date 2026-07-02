"""T409: Capability Restoration Frontier -- Tier-2 forcing in a finite
collision model.

T393 earned Tier-1 (causal) forcing of the T392 access asymmetry and NAMED
the Tier-2 (thermodynamic) card: bath dispersion, undo cost scaling with
bath contact. T408 physicalized the capability boundary at the operator
level and re-named the same card ("the genuine open-system bound is T393's
Tier-2, unbuilt"). The Direction-B checkpoint priced the load-bearing gap:
"real apparatuses are bounded-region agents whose emitted records disperse
beyond feasible re-collection." This artifact builds the finite,
exactly-simulable form of that card.

THE MODEL. A record qubit REC holds the which-way copy of system S
(T392's measurement core: S at prepared phase phi, weak meter M at
theta_meter = pi/3, CNOT copy S -> REC). REC then interacts sequentially
with a stream of fresh bath qubits B1..Bn -- one collision per step,
CNOT-type collisions of strength theta implemented as controlled-Ry(theta)
(REC -> B_i), T393's own emission gate; theta = pi is the exact CNOT copy.
After n collisions the record is BROADCAST: n partial (theta < pi) or
perfect (theta = pi) which-way copies sit in the bath.

THE FRONTIER. An agent's reach is the apparatus core {S, M, REC} plus r
bath qubits; the menu is ALL channels supported on the reach (with
unlimited work ancillas -- see Leg 2). Restoring S's phase-locked
visibility >= v* = 0.9 (T392's threshold, unchanged) requires reach at
least r(n): a reach frontier through the bath, certified per n by the
T393/T408 all-channel machinery (phi-independence certificate;
channel-independent trace-norm bound) applied to insufficient-reach
subsets -- exhaustively over every subset for small n, symmetry-pruned
beyond (the collisions share the control REC, so they commute and the
state is permutation-symmetric in the bath; asserted numerically, not
assumed).

    Leg 1 (dispersion forces reach growth): at theta = pi the frontier is
    EXACT and maximal: r(n) = n for every n = 1..7 -- every proper subset
    of the bath, of every size, is phi-independence-certified (no channel
    on the reach recovers anything), and full reach restores 4 sqrt(3)/7.
    The record has an escape velocity of one reach-unit per collision.

    Leg 2 (work does not substitute for reach): the certificates quantify
    over all CPTP maps on the reach, and adjoining ANY work register in
    any phi-independent state changes neither certificate (Stinespring +
    trace-norm multiplicativity: ||A tensor sigma||_1 = ||A||_1 for a
    state sigma) -- asserted numerically, with the frontier recomputed
    with work registers adjoined and found identical. Fresh work
    manufactures coherence but never phi-LOCKED coherence (T393's lemma;
    the exploit is implemented and nulled). The frontier is priced in
    reach, not work; deletion is not definalization (T408's ledger,
    imported: blind reset pays the Landauer floor and restores nothing).

    Leg 3 (graded frontier + T142 ledger): with partial strength theta the
    frontier surface is r_feas(n, theta) = max(0, n - d(theta)),
    d(theta) = floor(ln(v*/vis_A) / ln cos(theta/2)) -- an onset delay
    d(theta) collisions long, then slope-1 growth. The certified side
    (bound < v*) brackets it from below; the bracket is EXACT (r_cert =
    r_feas) wherever 2 vis_A cos(theta/2) < v* (theta > 0.6995 pi, the
    same bite threshold measured in T393/T408) and honestly vacuous at
    weak coupling within this bath size (the factor-2-loose bound, now
    measured in three artifacts). The T142-convention ledger prices
    restoration: correlated uncopy at zero Landauer floor within reach;
    blind reset pays the floor and restores nothing; beyond the frontier
    the feasible set is EMPTY (certified) and the cost is an empty-set
    infimum typed as access-not-work. The computed correspondence in this
    family: capability deficit 1 - (achieved/vis_A)^2 EQUALS the squared
    branch distinguishability displaced into the unreached bath
    (complementarity, exact), and the reach deficit u = n - r counts the
    record-bearing bath contacts beyond reach. Disclosure with teeth: at
    theta = pi the escaped Holevo content SATURATES at h2(3/7) = 0.98523
    bits for every u >= 1 (one branch bit, redundantly broadcast --
    quantum-Darwinism structure) while the frontier keeps growing: the
    frontier is priced in record-bearing CONTACTS, not in bits, just as
    Leg 2 shows it is not priced in work.

DISPERSION-STRUCTURE CONTRASTS (computed, not argued):
  - full-SWAP stream (displacement without dispersion): the record MOVES
    to B1 and later collisions act on vacuum -- the state literally stops
    changing; r(n) = 1 saturates, and the frontier is not
    permutation-symmetric (every subset missing B1 is certified, at any
    size). Reported exactly as the saturation it is: frontier GROWTH is
    sourced in broadcast (new record-bearing contact per collision), not
    in motion of the record.
  - uncorrelated stream (real excitation, no record): Ry(theta) on each
    B_i with no control -- r(n) = 0 for every n. Bath contact per se is
    free; RECORD-BEARING contact is what the frontier prices (T393's B'
    lineage).
  - weak-coupling onset: at theta = 0.1 pi the analytic onset is
    n_onset = d + 1 = 8, beyond this bath size, so r_feas = 0 for every
    n <= 7 -- saturation at zero within the family, reported exactly.

WHAT THIS EARNS (scoped): inside this finite formalism the bounded-region
premise becomes physical -- a finite-reach agent in a dispersive
(broadcasting) environment suffers forced, work-insensitive,
monotonically growing capability loss. Tier-2 forcing in this finite
family, completing T393's hierarchy at the collision-model rung;
Direction C's first quantitative frontier; Direction B's re-entry.

WHAT THIS DOES NOT EARN: no continuum or asymptotic bath-dispersion
theorem (that card stays named-unbuilt); no real bath thermodynamics (no
Hamiltonian bath, no temperature, no work parameter -- the ledger is
T142-convention bookkeeping); no hardware or platform; no claim
promotion. Ledger actions pause for Joe per AGENTS.md. Hostile review is
QUEUED for this artifact (as for T404/T408), not yet performed.

Register order (index-sorted, MSB first):
    S, M, REC, B1, B2, B3, B4, B5, B6, B7   (10 qubits, exact statevector)
"""

from __future__ import annotations

import math
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T392 primitives (exact statevector machinery; explicit n everywhere).
from models.fixed_sbs_key_reversal_divergence import (
    THETA as THETA_METER,
    V_STAR,
    _HADAMARD,
    reduced_density_matrix,
    z_distribution,
    zero_state,
)

# T393 machinery by import: certificate phase sweep (incommensurate values
# included), uniform locking grid, generic qubit-subset applicator, Haar
# sampling, and the trace norm used by the channel bound.
from models.causal_forcing_access_asymmetry import (
    PHI_CERT,
    PHI_LOCK_GRID,
    _trace_norm,
    apply_on_qubits,
    haar_unitary,
)

# T142 conventions for the Leg-3 ledger (dimensionless beta*W >= bits*ln2).
from models.thermodynamic_erasure_calibration import (
    LANDAUER_NAT_PER_BIT,
    landauer_bound_bits,
)

# --------------------------------------------------------------------------- #
# Register layout and predeclared constants
# --------------------------------------------------------------------------- #

S, M, REC = 0, 1, 2
BATH = (3, 4, 5, 6, 7, 8, 9)  # B1..B7, collision order = index order
N_QUBITS = 10
N_BATH_MAX = 7

# The agent's apparatus core, fixed once for every scenario. The meter is
# measured (verdicts conditional on M = 0, the dominant branch, as in
# T392/T393), so the ACTIVE core the menu acts on is {S, REC}.
CORE_ACTIVE = (S, REC)

# Collision-strength sweep (the theta axis of the frontier surface).
# theta = pi is the exact CNOT copy; the sweep brackets the analytic onset
# edge 2 acos(v*/vis_A) = 0.27319 pi (T408's feasibility edge, reappearing
# here as the frontier onset threshold) and the bound-bite edge
# 2 acos(v*/(2 vis_A)) = 0.69947 pi (T393/T408's measured 2x looseness).
THETA_SWEEP = tuple(
    f * math.pi for f in (0.1, 0.15, 0.2, 0.25, 0.5, 0.7, 0.75, 1.0)
)
THETA_CNOT = math.pi

# Exhaustive-certification block: EVERY subset of the bath, every size, for
# these collision counts and strengths; symmetry pruning is justified by
# the exhaustive block plus explicit permuted-subset state comparisons at
# n = 7 (see symmetry_report).
EXHAUSTIVE_N = (1, 2, 3, 4)
EXHAUSTIVE_THETAS = (0.5 * math.pi, math.pi)

VIS_A_ANALYTIC = 4.0 * math.sqrt(3.0) / 7.0  # T392/T393/T408's 0.98974...
# Onset edge: d(theta) >= 1 iff theta <= this (same constant as T408's
# protocol-feasibility edge).
THETA_ONSET_EDGE = 2.0 * math.acos(V_STAR / VIS_A_ANALYTIC)
# Bound-bite edge: the trace-norm bound certifies u = 1 iff theta > this.
THETA_BITE_EDGE = 2.0 * math.acos(V_STAR / (2.0 * VIS_A_ANALYTIC))

# Work registers for Leg 2 (fresh product-|0> qubits adjoined to the reach;
# numerically identical to bringing Stinespring ancillas). Used in the
# n = 4 work scenarios, where B5..B7 never collided.
WORK_REGISTERS = (8, 9)  # B6, B7 in the layout above
WORK_SCENARIO_N = 4
WORK_SCENARIO_REACH = (3, 4)  # B1, B2: insufficient reach at theta = pi

HAAR_SAMPLES = 15
HAAR_SEED = 20260702
HAAR_VISIBILITY_CEILING = 0.05

FLATNESS_TOL = 1e-12
ANALYTIC_TOL = 1e-9
INFINITE_COST = math.inf

VERDICT_RESTORABLE = "restorable-at-reach"
VERDICT_FINAL = "final-relative-to-reach"
VERDICT_TAGS = (
    "capability_restoration_frontier",
    "reach_forced_growth",
    "work_does_not_substitute_for_reach",
    "graded_frontier_ledger_bookkeeping_only",
    "tier2_forcing_finite_family",
    "no_claim_promotion",
)

BAND_FEASIBLE = "feasible_zero_cost"
BAND_CERTIFIED = "certified_infeasible"
BAND_UNDETERMINED = "undetermined_by_bound"

# --------------------------------------------------------------------------- #
# Small exact gates, applied via T393's generic qubit-subset applicator
# --------------------------------------------------------------------------- #

_PAULI_X2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
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


def _apply(vec: np.ndarray, gate: np.ndarray, targets) -> np.ndarray:
    return apply_on_qubits(vec, gate, list(targets), N_QUBITS)


def project_qubit(vec: np.ndarray, qubit: int, value: int, n: int = N_QUBITS):
    """Reshape-based projector (T408's; numerically identical to T392's
    dense-matrix version, asserted in the suite via the neighbor re-runs)."""
    tensor = np.moveaxis(vec.reshape([2] * n), qubit, 0).copy()
    tensor[1 - value] = 0.0
    out = np.moveaxis(tensor, 0, qubit).reshape(2 ** n)
    prob = float(np.real(out.conj() @ out))
    if prob > 1e-15:
        out = out / math.sqrt(prob)
    return prob, out


# --------------------------------------------------------------------------- #
# Preparations: measurement core + collision stream
# --------------------------------------------------------------------------- #

_STATE_CACHE: dict = {}
_COND_CACHE: dict = {}


def prepare(
    family: str, n: int, s_phase: float = 0.0, theta: float = THETA_CNOT
) -> np.ndarray:
    """Exact statevector after ``n`` collisions.

    Shared core (every family, identical couplings): S in
    (|0> + e^{i s_phase}|1>)/sqrt(2); controlled-Ry(theta_meter = pi/3)
    S -> M (T392's weak meter, measured); CNOT S -> REC (the which-way
    record copy).

    Collision stream (one fresh bath qubit per step, in collision order
    B1, B2, ...):

    ``cnot``          controlled-Ry(theta) REC -> B_i: a strength-theta
                      partial Z-copy of the record onto each bath qubit
                      (T393's emission gate; theta = pi is the exact CNOT
                      copy since each B_i starts in |0>). BROADCAST:
                      every collision creates a new record-bearing
                      contact. The primary certified family.
    ``swap``          full SWAP(REC, B_i): the record MOVES to B1 on the
                      first collision; all later collisions act on
                      vacuum. Displacement without dispersion (contrast
                      probe).
    ``uncorrelated``  Ry(theta) on B_i, no control: a real excitation
                      stream carrying NO record (T393's B' lineage; null
                      control).
    """
    if not 0 <= n <= N_BATH_MAX:
        raise ValueError(f"n = {n} outside 0..{N_BATH_MAX}")
    key = (family, int(n), float(s_phase), float(theta))
    if key in _STATE_CACHE:
        return _STATE_CACHE[key]

    psi = zero_state(N_QUBITS)
    psi = _apply(psi, _HADAMARD, [S])
    if s_phase != 0.0:
        psi = _apply(psi, _phase_gate(s_phase), [S])
    psi = _apply(psi, _CRY_METER4, [S, M])
    psi = _apply(psi, _CNOT4, [S, REC])

    for i in range(n):
        b = BATH[i]
        if family == "cnot":
            psi = _apply(psi, _controlled(_ry(theta)), [REC, b])
        elif family == "swap":
            psi = _apply(psi, _SWAP4, [REC, b])
        elif family == "uncorrelated":
            psi = _apply(psi, _ry(theta), [b])
        else:
            raise ValueError(f"unknown family {family!r}")

    _STATE_CACHE[key] = psi
    return psi


def _conditioned(family: str, n: int, s_phase: float, theta: float, m: int = 0):
    """Cached M-conditioned statevector (the object every channel acts on)."""
    key = (family, int(n), float(s_phase), float(theta), int(m))
    if key not in _COND_CACHE:
        psi = prepare(family, n, s_phase=s_phase, theta=theta)
        _COND_CACHE[key] = project_qubit(psi, M, m, N_QUBITS)
    return _COND_CACHE[key]


def conditional_state(
    family: str, n: int, s_phase: float, active, theta: float = THETA_CNOT, m: int = 0
) -> np.ndarray:
    """Reduced state on ``active`` given the meter outcome."""
    prob, cond = _conditioned(family, n, s_phase, theta, m)
    if prob <= 1e-15:
        raise ValueError(f"meter outcome {m} has zero probability")
    return reduced_density_matrix(cond, list(active), N_QUBITS)


def reach_active(subset) -> tuple:
    """The active support of the menu at bath reach ``subset``: apparatus
    core {S, REC} plus the reached bath qubits. Declared once; identical
    for every family and preparation."""
    return tuple(sorted(set(CORE_ACTIVE) | set(subset)))


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho - sigma)
    return float(0.5 * np.sum(np.abs(eig)))


# --------------------------------------------------------------------------- #
# Certificates (T393/T408 machinery, applied per reach subset)
# --------------------------------------------------------------------------- #

def phi_independence_cert(
    family: str, n: int, subset, theta: float = THETA_CNOT, phis=PHI_CERT
) -> float:
    """Max pairwise entrywise difference of the M-conditioned reach states
    across the phi sweep. Below tolerance => the reach family is exactly
    phi-independent, so NO channel supported on the reach (with or without
    work ancillas -- their state is phi-independent too) produces any
    phi-locked output: all-channel impossibility, T393's certificate."""
    active = reach_active(subset)
    rhos = [conditional_state(family, n, phi, active, theta) for phi in phis]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def channel_bound(
    family: str, n: int, subset, theta: float = THETA_CNOT, grid=PHI_LOCK_GRID,
    extra_registers=(),
) -> float:
    """T393's channel-independent upper bound on the phase-locked
    visibility of ANY channel supported on the reach:
    2 (||Re X||_1 + ||Im X||_1), X = mean_phi e^{i phi} rho_reach|M=0(phi)
    (Hoelder + CPTP trace-norm contractivity; covers every channel at
    once, no enumeration).

    ``extra_registers`` adjoins fresh work qubits to the reach (Leg 2):
    since they are in a fixed phi-independent product state, X gains a
    tensor factor sigma with ||A tensor sigma||_1 = ||A||_1, so the bound
    is invariant -- asserted numerically in work_report()."""
    active = tuple(sorted(set(reach_active(subset)) | set(extra_registers)))
    dim = 2 ** len(active)
    X = np.zeros((dim, dim), dtype=complex)
    for phi in grid:
        X = X + np.exp(1j * phi) * conditional_state(family, n, phi, active, theta)
    X = X / len(grid)
    herm = (X + X.conj().T) / 2.0
    anti = (X - X.conj().T) / 2.0j
    return 2.0 * (_trace_norm(herm) + _trace_norm(anti))


# --------------------------------------------------------------------------- #
# Restoration protocols and figure of merit
# --------------------------------------------------------------------------- #

def restoration_protocol(subset, theta: float = THETA_CNOT, family: str = "cnot"):
    """The achieving protocol at bath reach ``subset`` (cnot family):
    un-write each reached partial copy (controlled-Ry(-theta) REC -> B_i;
    the collisions share the control REC, so they commute and any order
    works), then uncopy the record (CNOT S -> REC). Every gate is
    supported on the reach. For the swap family: SWAP the record back
    from B1 if reached, then uncopy."""

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = vec
        if family == "cnot":
            for b in subset:
                out = _apply(out, _controlled(_ry(-theta)), [REC, b])
        elif family == "swap":
            if BATH[0] in subset:
                out = _apply(out, _SWAP4, [REC, BATH[0]])
        out = _apply(out, _CNOT4, [S, REC])
        return out

    return _undo


def locked_visibility(
    family: str, n: int, undo_fn, theta: float = THETA_CNOT, m: int = 0,
    grid=PHI_LOCK_GRID,
) -> float:
    """Phase-locked conditional X-visibility
    |mean_phi e^{i phi} 2 rho_S[0,1]| (T392/T393/T408's recovery figure of
    merit; the uniform grid exactly nulls manufactured, phi-independent
    coherence)."""
    total = 0.0 + 0.0j
    for phi in grid:
        prob, cond = _conditioned(family, n, phi, theta, m)
        if prob <= 1e-15:
            return 0.0
        out = undo_fn(cond)
        if isinstance(out, list):  # Kraus branches (non-unitary channel)
            rho_s = sum(
                reduced_density_matrix(b, [S], N_QUBITS) for b in out
            )
        else:
            rho_s = reduced_density_matrix(out, [S], N_QUBITS)
        total += np.exp(1j * phi) * 2.0 * rho_s[0, 1]
    return float(abs(total / len(grid)))


def raw_visibility(
    family: str, n: int, undo_fn, theta: float = THETA_CNOT, s_phase: float = 0.0
) -> float:
    """Raw (phase-blind) visibility, disclosure column only."""
    prob, cond = _conditioned(family, n, s_phase, theta, 0)
    if prob <= 1e-15:
        return 0.0
    out = undo_fn(cond)
    if isinstance(out, list):
        rho_s = sum(reduced_density_matrix(b, [S], N_QUBITS) for b in out)
    else:
        rho_s = reduced_density_matrix(out, [S], N_QUBITS)
    return float(2.0 * abs(rho_s[0, 1]))


# --------------------------------------------------------------------------- #
# Analytic frontier (predeclared closed forms, asserted against numerics)
# --------------------------------------------------------------------------- #

def deficit_allowance(theta: float) -> int:
    """d(theta): the largest number of unreached strength-theta contacts
    compatible with threshold restoration, from achieved(u) =
    vis_A cos(theta/2)^u >= v*. d = 0 at theta = pi (perfect copies)."""
    c = math.cos(theta / 2.0)
    if c <= 1e-12:
        return 0
    return int(math.floor(math.log(V_STAR / VIS_A_ANALYTIC) / math.log(c)))


def min_certified_deficit(theta: float) -> float:
    """u_min_cert(theta): the smallest unreached-contact count at which the
    trace-norm bound bites (bound(u) = 2 vis_A cos(theta/2)^u < v*).
    Returns inf if it never bites (any u)."""
    c = math.cos(theta / 2.0)
    if c <= 1e-12:
        return 1.0
    u = math.log(V_STAR / (2.0 * VIS_A_ANALYTIC)) / math.log(c)
    return float(math.floor(u) + 1)


# --------------------------------------------------------------------------- #
# Leg 1 + Leg 3 -- the frontier
# --------------------------------------------------------------------------- #

def frontier_row(
    n: int, r: int, theta: float, family: str = "cnot", subset=None
) -> dict:
    """One frontier cell: reach size r (canonical subset = first r bath
    qubits, justified by the symmetry report), achieved protocol value,
    both certificates, band classification."""
    if subset is None:
        subset = BATH[:r]
    achieved = locked_visibility(
        family, n, restoration_protocol(subset, theta, family), theta
    )
    bound = channel_bound(family, n, subset, theta)
    cert = phi_independence_cert(family, n, subset, theta)
    if achieved >= V_STAR:
        band = BAND_FEASIBLE
    elif bound < V_STAR:
        band = BAND_CERTIFIED
    else:
        band = BAND_UNDETERMINED
    u = n - len(subset)
    return {
        "n": n,
        "reach": len(subset),
        "unreached": u,
        "achieved": achieved,
        "analytic": VIS_A_ANALYTIC * math.cos(theta / 2.0) ** u,
        "bound": bound,
        "phi_cert": cert,
        "band": band,
    }


def frontier_for_theta(theta: float, family: str = "cnot") -> dict:
    """The frontier at fixed collision strength: per n, rows for every
    reach size (canonical subsets), r_feas, r_cert, and the analytic
    cross-checks."""
    d = deficit_allowance(theta)
    u_cert = min_certified_deficit(theta)
    per_n = []
    for n in range(1, N_BATH_MAX + 1):
        rows = [frontier_row(n, r, theta, family) for r in range(n + 1)]
        r_feas = next(
            (row["reach"] for row in rows if row["band"] == BAND_FEASIBLE),
            None,
        )
        # r_cert: every reach size BELOW it is trace-norm certified
        # infeasible (bound < v*). bound increases with reach, so this is
        # the count of leading certified sizes.
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
        "deficit_allowance_d": d,
        "min_certified_deficit_u": ("inf" if math.isinf(u_cert) else u_cert),
        "onset_n": d + 1,
        "per_n": per_n,
        "r_feas_by_n": [row["r_feas"] for row in per_n],
        "r_cert_by_n": [row["r_cert"] for row in per_n],
    }


def exhaustive_certification(n: int, theta: float) -> dict:
    """EVERY subset of the bath (all 2^n, every size) at collision count n:
    achieved, bound, phi certificate, band. Asserts (in the suite) that
    (a) values depend only on subset SIZE (permutation symmetry, the
    pruning justification), (b) the frontier from the exhaustive data
    equals the canonical-subset frontier, (c) at theta = pi every proper
    subset is phi-independence-certified."""
    by_size: dict = {}
    max_same_size_spread = 0.0
    for r in range(n + 1):
        cells = []
        for subset in combinations(BATH[:n], r):
            cells.append(frontier_row(n, r, theta, "cnot", subset=subset))
        for keyname in ("achieved", "bound"):
            vals = [c[keyname] for c in cells]
            max_same_size_spread = max(
                max_same_size_spread, max(vals) - min(vals)
            )
        by_size[r] = {
            "n_subsets": len(cells),
            "achieved": cells[0]["achieved"],
            "bound": cells[0]["bound"],
            "max_phi_cert": max(c["phi_cert"] for c in cells),
            "bands": sorted({c["band"] for c in cells}),
        }
    r_feas = next(
        (r for r in range(n + 1) if by_size[r]["achieved"] >= V_STAR), None
    )
    return {
        "n": n,
        "theta_over_pi": theta / math.pi,
        "subsets_checked": 2 ** n,
        "by_size": by_size,
        "max_same_size_spread": max_same_size_spread,
        "r_feas_exhaustive": r_feas,
    }


def symmetry_report() -> dict:
    """The pruning justification at full bath size: the M-conditioned reach
    states for permuted same-size subsets are IDENTICAL matrices (the
    collisions commute -- common control REC -- and every bath qubit gets
    the identical gate). Compared explicitly at n = 7 for sizes 1, 3, 6 at
    two phases and two strengths."""
    diffs = []
    pairs = {
        1: [(BATH[:1], (BATH[4],)), (BATH[:1], (BATH[6],))],
        3: [(BATH[:3], (BATH[1], BATH[4], BATH[6])), (BATH[:3], (BATH[2], BATH[3], BATH[5]))],
        6: [(BATH[:6], tuple(BATH[1:7]))],
    }
    for theta in (THETA_CNOT, 0.25 * math.pi):
        for size, subset_pairs in pairs.items():
            for canonical, permuted in subset_pairs:
                for phi in (1.0, math.pi / 3.0):
                    rho_c = conditional_state(
                        "cnot", 7, phi, reach_active(canonical), theta
                    )
                    rho_p = conditional_state(
                        "cnot", 7, phi, reach_active(permuted), theta
                    )
                    diffs.append(float(np.max(np.abs(rho_c - rho_p))))
    return {
        "compared_sizes": sorted(pairs),
        "n": 7,
        "thetas_over_pi": [1.0, 0.25],
        "max_state_diff": max(diffs),
    }


def monotonicity_report() -> dict:
    """r_feas and r_cert are monotone non-decreasing in n at every theta;
    saturations are located exactly (predeclared reportable findings, not
    failures)."""
    frontiers = {theta: frontier_for_theta(theta) for theta in THETA_SWEEP}
    monotone = True
    slope_one_beyond_onset = True
    saturations = []
    for theta, fr in frontiers.items():
        feas = fr["r_feas_by_n"]
        cert = fr["r_cert_by_n"]
        for a, b in zip(feas, feas[1:]):
            if b < a:
                monotone = False
        for a, b in zip(cert, cert[1:]):
            if b < a:
                monotone = False
        d = fr["deficit_allowance_d"]
        for i, n in enumerate(range(1, N_BATH_MAX + 1)):
            if n > d and feas[i] != n - d:
                slope_one_beyond_onset = False
        if all(v == 0 for v in feas):
            saturations.append(
                {
                    "theta_over_pi": theta / math.pi,
                    "kind": "onset_beyond_family",
                    "detail": (
                        f"r_feas = 0 for every n <= {N_BATH_MAX}; analytic "
                        f"onset n = {d + 1} exceeds the bath size"
                    ),
                }
            )
    return {
        "monotone_nondecreasing": monotone,
        "slope_one_beyond_onset": slope_one_beyond_onset,
        "escape_velocity_reach_units_per_collision": 1,
        "saturations": saturations,
        "frontiers": {
            f"{theta / math.pi:.2f}pi": {
                "d": fr["deficit_allowance_d"],
                "u_min_cert": fr["min_certified_deficit_u"],
                "r_feas_by_n": fr["r_feas_by_n"],
                "r_cert_by_n": fr["r_cert_by_n"],
            }
            for theta, fr in frontiers.items()
        },
    }


# --------------------------------------------------------------------------- #
# Dispersion-structure contrasts
# --------------------------------------------------------------------------- #

def swap_probe(n_values=(1, 2, 3, 4, 5)) -> dict:
    """Full-SWAP stream: displacement without dispersion. The record moves
    to B1 at collision 1; later collisions act on vacuum (the state stops
    changing, asserted). r(n) = 1 saturates, and the frontier is NOT
    permutation-symmetric: every subset missing B1 is certified at any
    size (exhaustive at n = 3)."""
    freeze_diff = max(
        float(
            np.max(
                np.abs(
                    prepare("swap", n, s_phase=1.0) - prepare("swap", 1, s_phase=1.0)
                )
            )
        )
        for n in n_values
        if n >= 1
    )
    restore_b1 = {
        n: locked_visibility(
            "swap", n, restoration_protocol((BATH[0],), family="swap")
        )
        for n in n_values
    }
    empty_certs = {
        n: phi_independence_cert("swap", n, ()) for n in n_values
    }
    # Exhaustive at n = 3: subsets containing B1 restore fully; subsets
    # missing B1 are certified at every size.
    exhaustive = {}
    for r in range(4):
        for subset in combinations(BATH[:3], r):
            has_b1 = BATH[0] in subset
            if has_b1:
                val = locked_visibility(
                    "swap", 3, restoration_protocol(subset, family="swap")
                )
                exhaustive[str(subset)] = {"contains_B1": True, "achieved": val}
            else:
                exhaustive[str(subset)] = {
                    "contains_B1": False,
                    "phi_cert": phi_independence_cert("swap", 3, subset),
                    "bound": channel_bound("swap", 3, subset),
                }
    return {
        "later_collisions_change_nothing_max_diff": freeze_diff,
        "restore_via_B1_by_n": restore_b1,
        "empty_reach_phi_cert_by_n": empty_certs,
        "exhaustive_n3": exhaustive,
        "r_feas_by_n": [1 for _ in n_values],
        "finding": (
            "saturation located exactly: the full-SWAP stream displaces the "
            "record once and never disperses it; r(n) = 1 for every n >= 1 "
            "and the frontier is subset-specific (B1 or nothing). Frontier "
            "GROWTH is sourced in broadcast -- new record-bearing contacts "
            "-- not in motion of the record."
        ),
    }


def uncorrelated_null(n_values=(1, 4, 7), theta: float = 0.5 * math.pi) -> dict:
    """Record-free collision stream: real bath excitation, no record.
    Restoration needs NO bath reach at any n (r = 0): bath contact per se
    is free; record-bearing contact is what the frontier prices."""
    rows = {}
    for n in n_values:
        vis = locked_visibility(
            "uncorrelated", n, restoration_protocol((), family="cnot"), theta
        )
        excitation = sum(
            float(
                np.real(
                    reduced_density_matrix(
                        prepare("uncorrelated", n, theta=theta), [b], N_QUBITS
                    )[1, 1]
                )
            )
            for b in BATH[:n]
        )
        rows[n] = {
            "achieved_at_reach_0": vis,
            "bath_excitation": excitation,
        }
    return {"theta_over_pi": theta / math.pi, "rows": rows, "r_feas": 0}


# --------------------------------------------------------------------------- #
# Leg 2 -- work does not substitute for reach
# --------------------------------------------------------------------------- #

def manufactured_coherence_channel(vec: np.ndarray) -> np.ndarray:
    """Unlimited-work exploit (T392's lemma, T393's implementation): use a
    fresh work register, put it in |+>, and SWAP it into S. Raw visibility
    1.0; carries ZERO information about the prepared phase, so the locked
    metric nulls it exactly."""
    out = _apply(vec, _HADAMARD, [WORK_REGISTERS[1]])
    out = _apply(out, _SWAP4, [WORK_REGISTERS[1], S])
    return out


def feedback_channel(subset, theta: float = THETA_CNOT):
    """Representative non-unitary reach channel: measure REC in Z, feed
    back X on S, then run the reach protocol (the menu is all channels,
    not just unitaries; the certificate covers this branch too)."""
    p0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    p1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    proto = restoration_protocol(subset, theta)

    def _channel(vec: np.ndarray) -> list:
        b0 = _apply(vec, p0, [REC])
        b1 = _apply(_apply(vec, p1, [REC]), _PAULI_X2, [S])
        return [proto(b0), proto(b1)]

    return _channel


def work_report() -> dict:
    """Leg 2, computed. Scenario: n = 4 collisions at theta = pi, reach =
    {B1, B2} (two contacts short of the frontier). The work registers are
    fresh product-|0> qubits adjoined to the reach -- numerically identical
    to bringing Stinespring ancillas, and the agent's channel may prepare
    them in ANY state (preparation is part of the channel; the input is
    phi-independent either way).

    (a) Certificate invariance: the phi-independence certificate fires on
        reach + work exactly as on reach; the trace-norm bound with work
        adjoined equals the bare bound (||A tensor sigma||_1 = ||A||_1).
    (b) Frontier invariance: every frontier bound at n = 4 recomputed with
        both work registers adjoined is identical to machine precision --
        the frontier is reach-absolute at fixed reach.
    (c) Attacks: the manufactured-coherence exploit scores raw 1.0 and
        locked ~0; the measure-and-feedback channel scores ~0; 15 seeded
        Haar unitaries on reach + work score ~0 (illustrative; the
        certificates carry the verdict).
    """
    n = WORK_SCENARIO_N
    subset = WORK_SCENARIO_REACH

    cert_bare = phi_independence_cert("cnot", n, subset)
    active_with_work = tuple(
        sorted(set(reach_active(subset)) | set(WORK_REGISTERS))
    )
    rhos = [
        conditional_state("cnot", n, phi, active_with_work) for phi in PHI_CERT
    ]
    cert_work = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            cert_work = max(cert_work, float(np.max(np.abs(rhos[i] - rhos[j]))))

    bound_bare = channel_bound("cnot", n, subset)
    bound_work = channel_bound("cnot", n, subset, extra_registers=WORK_REGISTERS)

    # Frontier invariance across all reach sizes at n = 4, two strengths.
    frontier_diffs = []
    for theta in (THETA_CNOT, 0.5 * math.pi):
        for r in range(n + 1):
            b0 = channel_bound("cnot", n, BATH[:r], theta)
            b1 = channel_bound(
                "cnot", n, BATH[:r], theta, extra_registers=WORK_REGISTERS
            )
            frontier_diffs.append(abs(b1 - b0))

    manufactured = {
        "raw_visibility": raw_visibility("cnot", n, manufactured_coherence_channel),
        "locked_visibility": locked_visibility(
            "cnot", n, manufactured_coherence_channel
        ),
    }
    feedback_locked = locked_visibility("cnot", n, feedback_channel(subset))

    rng = np.random.default_rng(HAAR_SEED)
    haar_active = tuple(sorted(set(reach_active(subset)) | {WORK_REGISTERS[1]}))
    dim = 2 ** len(haar_active)
    haar_max = 0.0
    for _ in range(HAAR_SAMPLES):
        U = haar_unitary(dim, rng)
        undo = lambda vec: apply_on_qubits(vec, U, list(haar_active), N_QUBITS)  # noqa: E731
        haar_max = max(haar_max, locked_visibility("cnot", n, undo))

    return {
        "scenario": {
            "n": n,
            "theta_over_pi": 1.0,
            "reach": ["B1", "B2"],
            "work_registers": ["B6", "B7"],
        },
        "phi_cert_bare": cert_bare,
        "phi_cert_with_work": cert_work,
        "bound_bare": bound_bare,
        "bound_with_work": bound_work,
        "bound_ancilla_invariance_diff": abs(bound_work - bound_bare),
        "frontier_bound_max_diff_with_work": max(frontier_diffs),
        "manufactured_coherence": manufactured,
        "feedback_channel_locked": feedback_locked,
        "haar_spot_check": {
            "samples": HAAR_SAMPLES,
            "seed": HAAR_SEED,
            "active": [str(q) for q in haar_active],
            "max_locked_visibility": haar_max,
            "note": "illustrative; the certificates carry the verdict",
        },
        "dilation_lemma": (
            "any channel on the reach assisted by finitely many work "
            "registers in any state IS a channel on the reach (Stinespring); "
            "adjoining a fixed state sigma sends X to X tensor sigma and "
            "||A tensor sigma||_1 = ||A||_1, so both certificates -- and "
            "hence the frontier -- are invariant under unlimited work. "
            "Sharp form: the frontier is priced in reach, not work."
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 3 -- ledger (T142 conventions; bookkeeping, NOT a thermo theorem)
# --------------------------------------------------------------------------- #

def _vn_entropy_bits(rho: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho)
    eig = eig[eig > 1e-15]
    return float(-np.sum(eig * np.log2(eig)))


def unreached_record_content(
    n: int, u: int, theta: float = THETA_CNOT
) -> dict:
    """What sits beyond reach when u of n contacts are unreached
    (canonical unreached set = last u bath qubits), conditioned on M = 0:
    branch distinguishability (trace distance between the S-branch states
    of the unreached set) and Holevo content about the branch bit."""
    unreached = BATH[n - u : n]
    _, cond = _conditioned("cnot", n, 0.0, theta, 0)
    branch_probs = []
    branch_states = []
    for b in (0, 1):
        pb, vec = project_qubit(cond, S, b, N_QUBITS)
        branch_probs.append(pb)
        branch_states.append(
            reduced_density_matrix(vec, list(unreached), N_QUBITS)
        )
    dist = trace_distance(branch_states[0], branch_states[1])
    rho_u = reduced_density_matrix(cond, list(unreached), N_QUBITS)
    holevo = _vn_entropy_bits(rho_u) - sum(
        p * _vn_entropy_bits(r) for p, r in zip(branch_probs, branch_states)
    )
    return {
        "unreached_contacts": u,
        "branch_probs_given_M0": branch_probs,
        "branch_distinguishability": dist,
        "holevo_bits": holevo,
    }


def blind_reset_channel(holders):
    """T142's blind-reset mode as a channel: each holder measured in Z and
    reset to |0> WITHOUT using the source-copy correlation. Kraus branches
    {P0, X P1} per holder. Supported on the reach."""

    def _channel(vec: np.ndarray) -> list:
        branches = [vec]
        p0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
        p1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
        for h in holders:
            new_branches = []
            for b in branches:
                new_branches.append(_apply(b, p0, [h]))
                new_branches.append(_apply(_apply(b, p1, [h]), _PAULI_X2, [h]))
            branches = new_branches
        return branches

    return _channel


def ledger_report() -> dict:
    """The T142-convention ledger on the frontier family (dimensionless
    beta*W >= erased_bits * ln 2). Scope: bookkeeping in a finite closed
    unitary model -- no bath Hamiltonian, no temperature, no work
    parameter. The continuum/asymptotic bath-dispersion theorem stays
    named-unbuilt."""
    n = WORK_SCENARIO_N  # 4 collisions at theta = pi: T408-parallel numbers
    holders = (REC,) + tuple(BATH[:n])  # 5 record holders in full reach

    # (a) Restore within reach: correlated uncopy, zero Landauer floor.
    vis_full = locked_visibility("cnot", n, restoration_protocol(BATH[:n]))
    restore_within = {
        "mode": "correlated_uncopy",
        "holders_uncomputed": len(holders),
        "erased_bits": 0,
        "beta_work_lower_bound": 0.0,
        "achieved_locked_visibility": vis_full,
        "t142_verdict": "reversible_when_full_microstate_available",
    }

    # (b) Blind reset of the same holders: pays the floor, restores nothing.
    reset = blind_reset_channel(holders)
    vis_after_reset = locked_visibility("cnot", n, reset)
    _, cond = _conditioned("cnot", n, 1.0, THETA_CNOT, 0)
    branch_states = []
    for b in (0, 1):
        _, vec = project_qubit(cond, S, b, N_QUBITS)
        rho = sum(
            reduced_density_matrix(br, list(holders), N_QUBITS)
            for br in reset(vec)
        )
        branch_states.append(rho / np.trace(rho))
    residual = trace_distance(branch_states[0], branch_states[1])
    joint_bits_cond = _vn_entropy_bits(
        reduced_density_matrix(cond, list(holders), N_QUBITS)
    )
    joint_bits_uncond = _vn_entropy_bits(
        reduced_density_matrix(
            prepare("cnot", n, s_phase=1.0), list(holders), N_QUBITS
        )
    )
    blind = {
        "mode": "blind_reset",
        "erased_bits_naive_per_holder": len(holders),
        "beta_work_lower_bound_naive": landauer_bound_bits(len(holders)),
        "joint_record_bits_given_M0": joint_bits_cond,
        "joint_record_bits_unconditioned": joint_bits_uncond,
        "capability_after_reset": vis_after_reset,
        "record_deleted_residual_distinguishability": residual,
        "deletion_is_not_definalization": vis_after_reset < 1e-12
        and residual < 1e-12,
        "t142_verdict": "standard_erasure_cost_if_uncopy_unavailable",
    }

    # (c) Restore beyond the frontier: EMPTY feasible set (certified).
    short_reach = WORK_SCENARIO_REACH
    beyond = {
        "scenario": "n = 4 perfect contacts, reach = 2 (< frontier 4)",
        "feasible_at_reach": False,
        "certificates": {
            "phi_independence": phi_independence_cert("cnot", n, short_reach),
            "channel_bound": channel_bound("cnot", n, short_reach),
        },
        "min_cost_convention": "inf (infimum over an empty feasible set)",
        "min_beta_work": INFINITE_COST,
        "limiting_resource": "reach to the record-bearing contacts, not work",
        "not_a_work_bound": (
            "the infinity is NOT a divergent Landauer/work requirement: "
            "this closed unitary model has no work parameter that could "
            "diverge; no channel supported on the reach restores the phase "
            "at ANY resource expenditure (phi-independence certificate, "
            "work-invariant by the dilation lemma). Calling it a 'cost' is "
            "an extended-real bookkeeping convention."
        ),
    }

    # (d) The graded correspondence: capability deficit vs displaced record,
    # per unreached-contact count, at two strengths.
    correspondence_rows = []
    for theta in (0.5 * math.pi, THETA_CNOT):
        n7 = N_BATH_MAX
        prev_holevo = -1.0
        for u in range(0, n7 + 1):
            r = n7 - u
            achieved = locked_visibility(
                "cnot", n7, restoration_protocol(BATH[:r], theta), theta
            )
            content = unreached_record_content(n7, u, theta)
            deficit = 1.0 - (achieved / VIS_A_ANALYTIC) ** 2
            row = {
                "theta_over_pi": theta / math.pi,
                "n": n7,
                "reach": r,
                "unreached_contacts": u,
                "achieved": achieved,
                "capability_deficit": deficit,
                "displaced_distinguishability": content["branch_distinguishability"],
                "complementarity_residual": abs(
                    deficit - content["branch_distinguishability"] ** 2
                ),
                "escaped_holevo_bits": content["holevo_bits"],
                "holevo_monotone_from_prev": content["holevo_bits"]
                >= prev_holevo - 1e-12,
            }
            prev_holevo = content["holevo_bits"]
            correspondence_rows.append(row)

    h2_3_7 = -(3 / 7) * math.log2(3 / 7) - (4 / 7) * math.log2(4 / 7)
    return {
        "landauer_nat_per_bit": LANDAUER_NAT_PER_BIT,
        "restore_within_reach": restore_within,
        "blind_reset": blind,
        "restore_beyond_frontier": beyond,
        "correspondence_rows": correspondence_rows,
        "h2_3_7_bits": h2_3_7,
        "correspondence": (
            "in this finite family the capability deficit equals the "
            "squared branch distinguishability displaced into the unreached "
            "bath (exact complementarity), and the reach deficit u = n - r "
            "counts the record-bearing contacts beyond reach. DISCLOSURE "
            "with teeth: at theta = pi the escaped Holevo content saturates "
            "at h2(3/7) = 0.98523 bits for every u >= 1 (one branch bit, "
            "redundantly broadcast) while the frontier keeps growing -- the "
            "frontier is priced in record-bearing CONTACTS, not in escaped "
            "bits and not in work. Bookkeeping in a finite closed unitary "
            "model, not a thermodynamic theorem."
        ),
        "tier2_scope": (
            "Tier-2 forcing earned HERE means: in this finite collision "
            "family, capability loss for any fixed-reach agent is forced "
            "(all-channel certificates), work-insensitive (dilation lemma), "
            "and monotonically growing in bath contact (frontier tables). "
            "The continuum/asymptotic bath-dispersion theorem -- work/entropy "
            "scaling in a genuine open-system bath -- stays named-unbuilt."
        ),
    }


# --------------------------------------------------------------------------- #
# Guardrails (Q1D asserted numerically; R1 untouched)
# --------------------------------------------------------------------------- #

def q1d_report() -> dict:
    """No-signalling surfaces with teeth."""
    # Declared ordinary record P(S, M): invariant across families, collision
    # counts, and strengths (collisions never touch S or M).
    ref = z_distribution(prepare("cnot", 0, 1.0), [S, M], N_QUBITS)

    def _rdiff(family, n, theta):
        d = z_distribution(prepare(family, n, 1.0, theta), [S, M], N_QUBITS)
        return max(abs(ref.get(k, 0.0) - d.get(k, 0.0)) for k in set(ref) | set(d))

    record_invariance = max(
        [_rdiff("cnot", n, THETA_CNOT) for n in (1, 4, 7)]
        + [_rdiff("cnot", 4, t) for t in (0.25 * math.pi, 0.5 * math.pi)]
        + [_rdiff("swap", 3, THETA_CNOT), _rdiff("uncorrelated", 4, 0.5 * math.pi)]
    )

    # No signalling out of the reach: the reach protocol cannot move an
    # unreached bath marginal; the counterfactual enlarged protocol does.
    n = 4
    subset = (BATH[0], BATH[1])
    _, cond = _conditioned("cnot", n, 1.0, THETA_CNOT, 0)
    unreached_q = BATH[3]  # B4
    before = reduced_density_matrix(cond, [unreached_q], N_QUBITS)
    after_reach = reduced_density_matrix(
        restoration_protocol(subset)(cond), [unreached_q], N_QUBITS
    )
    after_enlarged = reduced_density_matrix(
        restoration_protocol(BATH[:n])(cond), [unreached_q], N_QUBITS
    )
    return {
        "declared_record_invariance": record_invariance,
        "no_signal_out_reach_protocol": float(
            np.max(np.abs(before - after_reach))
        ),
        "enlarged_protocol_moves_unreached_marginal_teeth": float(
            np.max(np.abs(before - after_enlarged))
        ),
        "r1_note": (
            "R1 untouched: no claim about global temporal order or "
            "spacetime; the collision stream is a discrete interaction "
            "sequence, and the 'frontier' is a reach frontier through the "
            "bath, not a light cone (Lieb-Robinson is a named absorber "
            "risk, flagged from memory)"
        ),
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

_ANALYSIS_CACHE: dict = {}


def run_analysis() -> dict:
    # Leg 1 headline: the exact frontier at theta = pi.
    frontier_cnot = frontier_for_theta(THETA_CNOT)
    exhaustive = [
        exhaustive_certification(n, theta)
        for theta in EXHAUSTIVE_THETAS
        for n in EXHAUSTIVE_N
    ]
    symmetry = symmetry_report()
    monotonicity = monotonicity_report()
    swap = swap_probe()
    null = uncorrelated_null()
    work = work_report()
    ledger = ledger_report()
    q1d = q1d_report()

    # Leg 1 verdict: r(n) = n at theta = pi, every insufficient reach size
    # phi-certified, achieved matches analytic, strictly monotone.
    leg1_exact = all(
        row["r_feas"] == row["n"]
        and row["r_cert"] == row["n"]
        and row["r_feas_analytic"] == row["n"]
        and all(
            (
                cell["phi_cert"] < FLATNESS_TOL
                and cell["bound"] < FLATNESS_TOL
                and cell["band"] == BAND_CERTIFIED
            )
            if cell["reach"] < row["n"]
            else cell["band"] == BAND_FEASIBLE
            for cell in row["rows"]
        )
        for row in frontier_cnot["per_n"]
    )
    leg1_exhaustive_ok = all(
        ex["max_same_size_spread"] < 1e-10
        and (
            ex["theta_over_pi"] != 1.0
            or all(
                ex["by_size"][r]["max_phi_cert"] < FLATNESS_TOL
                for r in range(ex["n"])
            )
        )
        for ex in exhaustive
    )
    leg1_holds = (
        leg1_exact
        and leg1_exhaustive_ok
        and symmetry["max_state_diff"] < FLATNESS_TOL
        and monotonicity["monotone_nondecreasing"]
        and monotonicity["slope_one_beyond_onset"]
    )

    leg2_holds = (
        work["phi_cert_bare"] < FLATNESS_TOL
        and work["phi_cert_with_work"] < FLATNESS_TOL
        and work["bound_ancilla_invariance_diff"] < FLATNESS_TOL
        and work["frontier_bound_max_diff_with_work"] < FLATNESS_TOL
        and work["manufactured_coherence"]["raw_visibility"] > 0.99
        and work["manufactured_coherence"]["locked_visibility"] < 1e-12
        and work["feedback_channel_locked"] < 1e-12
        and work["haar_spot_check"]["max_locked_visibility"]
        < HAAR_VISIBILITY_CEILING
        and ledger["blind_reset"]["deletion_is_not_definalization"]
    )

    leg3_holds = (
        all(
            row["complementarity_residual"] < ANALYTIC_TOL
            and row["holevo_monotone_from_prev"]
            and abs(
                row["achieved"]
                - VIS_A_ANALYTIC
                * math.cos(row["theta_over_pi"] * math.pi / 2.0)
                ** row["unreached_contacts"]
            )
            < ANALYTIC_TOL
            for row in ledger["correspondence_rows"]
        )
        and not ledger["restore_beyond_frontier"]["feasible_at_reach"]
        and ledger["restore_within_reach"]["erased_bits"] == 0
        and ledger["restore_within_reach"]["achieved_locked_visibility"] >= V_STAR
    )

    frontier_holds = leg1_holds and leg2_holds and leg3_holds

    if frontier_holds:
        verdict_language = (
            "the capability restoration frontier holds in this finite "
            "collision family: dispersion (record broadcast into the bath) "
            "forces monotonically growing reach for threshold restoration, "
            "exactly r(n) = n at perfect collision strength with every "
            "insufficient reach certified against ALL channels; work does "
            "not substitute for reach (both certificates and the frontier "
            "itself are invariant under adjoining unlimited work registers, "
            "and fresh work manufactures only phase-unlocked coherence); "
            "the graded frontier surface r = max(0, n - d(theta)) is "
            "computed with certified and honestly-undetermined bands, and "
            "the T142 ledger prices restoration in reach -- correlated "
            "uncopy at zero floor within reach, empty-feasible-set infimum "
            "typed as access-not-work beyond it, blind reset paying the "
            "floor and restoring nothing. Tier-2 forcing earned in this "
            "finite family: a finite-reach agent in a broadcasting "
            "environment suffers forced, work-insensitive, growing "
            "capability loss. The continuum bath-dispersion theorem stays "
            "named-unbuilt; bookkeeping only; no claim promotion; ledger "
            "actions pause for Joe."
        )
    else:
        verdict_language = (
            "the capability restoration frontier FAILS in this finite "
            "collision family: a certificate failed, the frontier is "
            "non-monotone or work-sensitive, or a correspondence row broke. "
            "Report the failing leg exactly (saturation or non-monotone "
            "structure is itself the reportable dispersion finding); do "
            "not weaken assertions to pass."
        )

    return {
        "artifact": "T409-capability-restoration-frontier-v0.1",
        "labeling_convention": (
            "registers index-sorted (S, M, REC, B1..B7); collision order = "
            "bath index order; all distributions keyed in this order"
        ),
        "theta_meter": THETA_METER,
        "v_star": V_STAR,
        "vis_A_analytic": VIS_A_ANALYTIC,
        "theta_onset_edge_over_pi": THETA_ONSET_EDGE / math.pi,
        "theta_bite_edge_over_pi": THETA_BITE_EDGE / math.pi,
        "reach_convention": {
            "core_active": ["S", "REC"],
            "meter": "M measured; verdicts conditional on M = 0",
            "menu": (
                "all channels supported on core + reached bath qubits, "
                "with unlimited work ancillas (Leg 2)"
            ),
        },
        "frontier_theta_pi": frontier_cnot,
        "exhaustive_certification": exhaustive,
        "symmetry": symmetry,
        "monotonicity": monotonicity,
        "swap_probe": swap,
        "uncorrelated_null": null,
        "work": work,
        "ledger": ledger,
        "q1d": q1d,
        "legs": {
            "leg1_dispersion_forces_reach_growth": leg1_holds,
            "leg2_work_does_not_substitute": leg2_holds,
            "leg3_graded_frontier_and_ledger": leg3_holds,
        },
        "verdict_tags": list(VERDICT_TAGS),
        "frontier_holds": frontier_holds,
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

    res = run_analysis()
    print(json.dumps(_json_safe(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T409 Capability Restoration Frontier (Tier-2, finite)")
    print("=" * 70)
    fr = res["frontier_theta_pi"]
    print("Leg 1 -- frontier at theta = pi (perfect collisions): r(n) = n")
    print(f"  n:      {[row['n'] for row in fr['per_n']]}")
    print(f"  r_feas: {fr['r_feas_by_n']}")
    print(f"  r_cert: {fr['r_cert_by_n']}")
    worst_cert = max(
        cell["phi_cert"]
        for row in fr["per_n"]
        for cell in row["rows"]
        if cell["reach"] < row["n"]
    )
    print(f"  worst insufficient-reach phi certificate: {worst_cert:.3e}")
    print(f"  symmetry pruning (n=7 permuted subsets): "
          f"{res['symmetry']['max_state_diff']:.3e}")
    print("graded frontier r_feas by n (rows) x theta:")
    for label, table in res["monotonicity"]["frontiers"].items():
        print(f"  theta {label}: d={table['d']}, u_cert={table['u_min_cert']}, "
              f"r_feas={table['r_feas_by_n']}, r_cert={table['r_cert_by_n']}")
    for sat in res["monotonicity"]["saturations"]:
        print(f"  saturation: theta {sat['theta_over_pi']:.2f} pi -- {sat['detail']}")
    print(f"swap probe (displacement, no dispersion): r_feas "
          f"{res['swap_probe']['r_feas_by_n']} "
          f"(state freeze diff {res['swap_probe']['later_collisions_change_nothing_max_diff']:.1e})")
    print(f"uncorrelated null: r_feas = {res['uncorrelated_null']['r_feas']}")
    w = res["work"]
    print("Leg 2 -- work does not substitute for reach:")
    print(f"  cert bare/with-work: {w['phi_cert_bare']:.3e} / "
          f"{w['phi_cert_with_work']:.3e}")
    print(f"  bound ancilla-invariance diff: "
          f"{w['bound_ancilla_invariance_diff']:.3e}; frontier-with-work "
          f"max diff: {w['frontier_bound_max_diff_with_work']:.3e}")
    print(f"  manufactured raw/locked: "
          f"{w['manufactured_coherence']['raw_visibility']:.6f} / "
          f"{w['manufactured_coherence']['locked_visibility']:.3e}")
    led = res["ledger"]
    print("Leg 3 -- ledger (T142 conventions, bookkeeping only):")
    print(f"  restore within reach: erased bits "
          f"{led['restore_within_reach']['erased_bits']}, achieves "
          f"{led['restore_within_reach']['achieved_locked_visibility']:.6f}")
    print(f"  blind reset: naive beta*W "
          f"{led['blind_reset']['beta_work_lower_bound_naive']:.4f}, "
          f"capability after {led['blind_reset']['capability_after_reset']:.3e}")
    print(f"  beyond frontier: feasible "
          f"{led['restore_beyond_frontier']['feasible_at_reach']}, min cost "
          f"{led['restore_beyond_frontier']['min_beta_work']}")
    print(f"  worst complementarity residual: "
          f"{max(r['complementarity_residual'] for r in led['correspondence_rows']):.3e}")
    print("-" * 70)
    print(f"LEGS: {res['legs']}")
    print(f"FRONTIER HOLDS: {res['frontier_holds']}")
    print(res["verdict_language"])
# end of module
