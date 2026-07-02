"""T395: Record-Order Trade-off Probe (Direction A, first executable rung).

The Direction-A conjecture (audits/2026-07-01-high-gravity-research-directions.md)
wants a device-independent-style criterion separating "temporal order derived
from stabilized records" from "background time / definite order". The candidate
structure is three nested two-party process classes:

    (1) RECORD-FIXED:       composition order of A and B definite AND written
                            into an accessible stabilized record lambda before
                            readout;
    (2) CAUSALLY SEPARABLE: order definite (possibly mixed) but not
                            necessarily recorded / accessible;
    (3) NONSEPARABLE:       coherent superposition of orders (quantum switch).

This artifact is the first executable probe of the (1)/(3) boundary: does it
carry QUANTITATIVE content beyond existing causal-nonseparability witnesses --
specifically a trade-off between record accessibility and order-indefiniteness
-- and does that trade-off reduce to known interferometric duality?

MODEL (exact statevector, numpy, within the <= 6 qubit budget):

  Two-order family: control qubit c (alpha|0> + beta|1>) selects the
  composition order applied to a target qubit t: branch c=0 applies A then B
  (target B@A|psi>), branch c=1 applies B then A (target A@B|psi>). A record
  qubit r is coupled to the control by controlled-Ry(gamma): gamma=0 no
  record, gamma=pi perfect record. The record is ACCESSIBLE (read in Z at
  readout) -- the finality-relevant D1-style difference from generic
  environment decoherence.

  Subsystem order is INDEX-SORTED throughout: (c, r, t) with c = subsystem 0,
  r = subsystem 1, t = subsystem 2. Every stored or printed tuple reads
  (c, r, t) in that order.

DEFINITIONS (the honest operationalizations):

  D(gamma) -- order-distinguishability, the record-finality proxy: the
  trace-distance distinguishability of the two order-branch conditional
  record states. Equivalently (Helstrom) the optimal equal-prior success of
  postdicting WHICH composition order the target underwent, given the record
  alone, is (1 + D)/2. Why this is the right operationalization of "the
  order is recorded": at gamma=pi the record is a perfect stabilized copy of
  the order degree of freedom and D=1; at gamma=0 no record exists and D=0;
  in between D is exactly the best achievable postdiction advantage of an
  agent whose access is the record. What it does NOT capture: (a) it makes
  no claim that a "realized order" exists per run in the coherent case (no
  hidden-variable reading; Q1D guardrail); (b) it is single-holder -- D1's
  distinct-holder redundancy, robustness, and reversal-cost axes are not
  modeled; (c) the physical readout basis is Z, and the Helstrom optimum
  generally needs a non-Z measurement -- the accessible Z-readout advantage
  D_Z = D**2 is computed and disclosed separately.

  V(gamma) -- interference visibility of the switch: the standard operational
  signature of order-coherence (fringe visibility of the control readout
  under a phase sweep, equal to twice the control coherence
  2*|rho_c[0,1]|). HONEST SCOPE LIMITATION, named: V is NOT a causal
  witness. A genuine causal-nonseparability witness (random robustness) for
  the reduced process requires process-matrix SDP machinery, which is
  explicitly out of scope here and is the named next rung. All verdicts are
  scoped to the visibility signature.

EXACT RELATIONS THIS FAMILY YIELDS (derived analytically in the spec,
asserted numerically here at 1e-12):

    D(gamma)   = sin(gamma/2)
    V(gamma)   = V0 * cos(gamma/2),   V0 = |<t_0|t_1>| = |K| (target
                 order-branch overlap; the target is itself a second,
                 fixed-strength order marker)
    D^2 + (V/V0)^2 = 1                    (normalized duality, exact)
    D_joint^2 + V^2 = 1                   (Englert saturation with the joint
                                           record+target marker, exact)
    D^2 + V^2 + (1 - D^2) * Dt0^2 = 1     (three-way decomposition,
                                           Dt0 = sqrt(1 - V0^2) the fixed
                                           target-marker strength)
    => the candidate bound D^2 + V^2 <= 1 holds with slack exactly equal to
       the unread target-marker term.

REDUCTION AUDIT (the kill-test): an explicit Mach-Zehnder-with-which-path-
marker mapping is implemented (path <-> control/order branch, marker <->
record, internal dof <-> target). The mapped MZ statevector is asserted equal
to the switch statevector across the whole gamma sweep, and the plain-MZ
(D, V) curve coincides with the normalized switch curve pointwise. VERDICT
(predeclared vocabulary): collapse -- the v0.1 record-order bound reduces to
interferometric duality in the two-order family.

K=3 PROBE (the genuinely new territory, scoped as finite observation): three
operations, superposition over a subset of the 3! = 6 orders (a 3-order
canonical subset and the full 6-order coherent sum are both built; control is
a k-level system, dims (k, 2, 2), within the 6-qubit budget). The record has
PARTIAL access: it writes only the order-CLASS (a 2-class coarse-graining),
not the order. Order postdiction becomes a k-class discrimination whose
optimum is capped by the class ceiling, within-class coherence is exactly
gamma-flat, cross-class pairs satisfy the binary duality exactly pairwise,
and every tested global scalarization fails the binary form. This is where
the T49 anti-scalar structure enters: the record's knowledge is a partition
with ties, not a scalar.

GUARDRAILS (binding):
  - Q1D: no-signalling asserted numerically -- the (control, record) readout
    marginals are exactly independent of both parties' operation settings and
    of the control phase.
  - R1: nothing here is a claim about global temporal order or spacetime;
    the artifact is about process composition order only.
  - Verdict vocabulary is predeclared (module constants) and restrained.

WHAT THIS DOES NOT EARN: no claim promotion; no CLAIM-LEDGER entry; no new
inequality; no causal-nonseparability witness; no statement about physical
platforms; k=3 findings are finite observations in a declared family, not
theorems, except where verified exhaustively over the declared finite family
(all 20 three-order subsets x 3 bipartitions, all 31 six-order bipartitions).

Reproduction:
    python -m pytest tests/test_record_order_tradeoff_probe.py -v
    python -m models.record_order_tradeoff_probe
"""

from __future__ import annotations

import math
from itertools import combinations, permutations

import numpy as np

# --------------------------------------------------------------------------- #
# Predeclared constants (fixed before inspecting numbers)
# --------------------------------------------------------------------------- #

PI = math.pi

# gamma sweep: 21 values, endpoints exactly 0 and pi (spec requires >= 20).
GAMMA_SWEEP = np.linspace(0.0, PI, 21)

# phase grid for the operational fringe cross-check (the exact value comes
# from the control coherence; the grid only confirms the operational reading).
PHI_GRID_N = 720
FRINGE_GRID_TOL = 1e-4

# exactness tolerance for every relation claimed "exact"
TOL_EXACT = 1e-12

# no-signalling setting perturbations (arbitrary fixed angles, predeclared)
SETTING_DELTA_A = 0.9
SETTING_DELTA_B = 0.7

# projective-measurement grid for the guessing-probability achievability check
GUESS_GRID_N = 2000
GUESS_GRID_TOL = 1e-4

# predeclared verdict strings (tested verbatim; restrained house vocabulary)
REDUCTION_VERDICT = (
    "collapse: the v0.1 record-order trade-off reduces exactly to "
    "interferometric which-path duality (two-marker Greenberger-Yasin/Englert "
    "structure) in the two-order family; separation, if any, lives at k>=3 "
    "partial-record structure"
)
K3_VERDICT = (
    "binary duality survives pairwise on cross-class pairs, is absent within "
    "class (gamma-flat coherence), and fails as every tested global "
    "scalarization; a perfect class-coarse record caps order postdiction at "
    "2/3 (3 orders) and 1/3 (6 orders) while within-class coherence persists "
    "-- finite observation in this family, not a theorem"
)
ACCESSIBILITY_VERDICT = (
    "record accessibility (measured vs traced) leaves the reduced process on "
    "(control, target) exactly unchanged by linearity of partial trace; the "
    "record-fixed vs causally-separable boundary is capability-relative, not "
    "marginal-statistics-relative, in this family"
)

# --------------------------------------------------------------------------- #
# Linear-algebra primitives (self-contained; general subsystem dims)
# --------------------------------------------------------------------------- #

I2 = np.eye(2, dtype=complex)
KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)
P0 = np.outer(KET0, KET0)
P1 = np.outer(KET1, KET1)


def rx(theta: float) -> np.ndarray:
    c, s = math.cos(theta / 2.0), math.sin(theta / 2.0)
    return np.array([[c, -1j * s], [-1j * s, c]], dtype=complex)


def ry(theta: float) -> np.ndarray:
    c, s = math.cos(theta / 2.0), math.sin(theta / 2.0)
    return np.array([[c, -s], [s, c]], dtype=complex)


def rz(theta: float) -> np.ndarray:
    return np.array(
        [[np.exp(-1j * theta / 2.0), 0.0], [0.0, np.exp(1j * theta / 2.0)]],
        dtype=complex,
    )


def kron_all(*ops: np.ndarray) -> np.ndarray:
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def basis(dim: int, i: int) -> np.ndarray:
    v = np.zeros(dim, dtype=complex)
    v[i] = 1.0
    return v


def dm(vec: np.ndarray) -> np.ndarray:
    return np.outer(vec, vec.conj())


def rdm(state: np.ndarray, dims: tuple, keep: tuple) -> np.ndarray:
    """Reduced density matrix on the `keep` subsystems (index-sorted dims)."""
    n = len(dims)
    keep = tuple(keep)
    perm = list(keep) + [i for i in range(n) if i not in keep]
    t = np.transpose(state.reshape(dims), perm)
    dk = int(np.prod([dims[i] for i in keep])) if keep else 1
    m = t.reshape(dk, -1)
    return m @ m.conj().T


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(rho - sigma)
    return 0.5 * float(np.sum(np.abs(eig)))


def trace_norm(m: np.ndarray) -> float:
    eig = np.linalg.eigvalsh(m)
    return float(np.sum(np.abs(eig)))


# --------------------------------------------------------------------------- #
# Canonical operation pair (documented sweep; two-order family)
# --------------------------------------------------------------------------- #

PSI_TARGET = KET0.copy()  # canonical target input |0>


def order_branch_targets(A: np.ndarray, B: np.ndarray, psi: np.ndarray):
    """Branch target states: c=0 -> A then B (B@A psi); c=1 -> B then A."""
    return B @ A @ psi, A @ B @ psi


def order_overlap_K(A: np.ndarray, B: np.ndarray, psi: np.ndarray) -> complex:
    t0, t1 = order_branch_targets(A, B, psi)
    return complex(np.vdot(t0, t1))


# Candidate pairs swept for the documented canonical choice. Criterion,
# predeclared: pick the pair whose target order-branch overlap magnitude |K|
# sits at the balanced two-marker point 1/sqrt(2) -- |K| = 0 ("maximal
# order-sensitivity") degenerates the visibility curve to V == 0 (trade-off
# invisible), |K| = 1 makes the target order-blind (no second marker).
CANDIDATE_PAIRS = {
    "Ry(pi/2),Rz(pi/2)": (ry(PI / 2), rz(PI / 2)),
    "Ry(pi/2),Rz(pi)": (ry(PI / 2), rz(PI)),
    "Rx(pi/2),Rz(pi/2)": (rx(PI / 2), rz(PI / 2)),
    "Ry(pi/2),Rz(pi/4)": (ry(PI / 2), rz(PI / 4)),
}
CANONICAL_PAIR_NAME = "Ry(pi/2),Rz(pi/2)"
A_CANON, B_CANON = CANDIDATE_PAIRS[CANONICAL_PAIR_NAME]
# third operation for the k=3 probe
C_CANON = rx(PI / 2)


def candidate_pair_table() -> dict:
    table = {}
    for name, (A, B) in CANDIDATE_PAIRS.items():
        K = order_overlap_K(A, B, PSI_TARGET)
        table[name] = {
            "abs_K": abs(K),
            "order_sensitivity": math.sqrt(max(0.0, 1.0 - abs(K) ** 2)),
            "canonical": name == CANONICAL_PAIR_NAME,
        }
    return table


# --------------------------------------------------------------------------- #
# Two-order switch + record model, dims (c, r, t) = (2, 2, 2)
# --------------------------------------------------------------------------- #

DIMS2 = (2, 2, 2)


def record_branch_states(gamma: float):
    """Conditional record states per order branch: r_0 = |0>, r_1 = Ry(gamma)|0>."""
    return KET0.copy(), ry(gamma) @ KET0


def switch_state_circuit(
    gamma: float,
    phi: float = 0.0,
    A: np.ndarray = None,
    B: np.ndarray = None,
    psi: np.ndarray = None,
    alpha: complex = None,
    beta: complex = None,
) -> np.ndarray:
    """Gate-built switch+record state on (c, r, t).

    Circuit: prepare c = alpha|0> + beta e^{i phi}|1>, r = |0>, t = psi;
    apply controlled-Ry(gamma) (c -> r), then the order switch
    |0><0|_c (x) I_r (x) (B@A) + |1><1|_c (x) I_r (x) (A@B).
    The two controls are both diagonal in c and commute.
    """
    A = A_CANON if A is None else A
    B = B_CANON if B is None else B
    psi = PSI_TARGET if psi is None else psi
    alpha = 1.0 / math.sqrt(2.0) if alpha is None else alpha
    beta = 1.0 / math.sqrt(2.0) if beta is None else beta
    c_in = alpha * KET0 + beta * np.exp(1j * phi) * KET1
    state = kron_all(c_in, KET0, psi)
    coupler = kron_all(P0, I2, I2) + kron_all(P1, ry(gamma), I2)
    switch = kron_all(P0, I2, B @ A) + kron_all(P1, I2, A @ B)
    return switch @ (coupler @ state)


def switch_state_branch_sum(
    gamma: float,
    phi: float = 0.0,
    A: np.ndarray = None,
    B: np.ndarray = None,
    psi: np.ndarray = None,
    alpha: complex = None,
    beta: complex = None,
) -> np.ndarray:
    """Branch-sum construction (independent code path used for cross-checks)."""
    A = A_CANON if A is None else A
    B = B_CANON if B is None else B
    psi = PSI_TARGET if psi is None else psi
    alpha = 1.0 / math.sqrt(2.0) if alpha is None else alpha
    beta = 1.0 / math.sqrt(2.0) if beta is None else beta
    r0, r1 = record_branch_states(gamma)
    t0, t1 = order_branch_targets(A, B, psi)
    return alpha * kron_all(KET0, r0, t0) + beta * np.exp(1j * phi) * kron_all(
        KET1, r1, t1
    )


def D_record(gamma: float) -> float:
    """Trace-distance order-distinguishability of the record (Helstrom proxy)."""
    r0, r1 = record_branch_states(gamma)
    return trace_distance(dm(r0), dm(r1))


def helstrom_success(gamma: float) -> float:
    """Optimal equal-prior order-postdiction success from the record alone."""
    return 0.5 * (1.0 + D_record(gamma))


def D_z_readout(gamma: float) -> float:
    """Accessible Z-readout postdiction advantage (2 * P_success - 1).

    The physical readout is Z on the record; the best outcome->order guessing
    strategy achieves P = (1/2) * sum_o max_b p(o | branch b).
    """
    r0, r1 = record_branch_states(gamma)
    p0 = np.abs(r0) ** 2
    p1 = np.abs(r1) ** 2
    p_succ = 0.5 * sum(max(p0[o], p1[o]) for o in range(2))
    return 2.0 * p_succ - 1.0


def visibility_exact(gamma: float, **kw) -> float:
    """Exact fringe visibility = 2 |rho_c[0,1]| (control coherence)."""
    state = switch_state_circuit(gamma, **kw)
    rho_c = rdm(state, DIMS2, (0,))
    return 2.0 * abs(rho_c[0, 1])


def visibility_fringe_grid(gamma: float, n_phi: int = PHI_GRID_N) -> float:
    """Operational fringe visibility from an explicit phi sweep of P(c = +)."""
    ps = []
    for phi in np.linspace(0.0, 2.0 * PI, n_phi, endpoint=False):
        t = switch_state_circuit(gamma, phi=phi).reshape(DIMS2)
        plus = (t[0] + t[1]) / math.sqrt(2.0)
        ps.append(float(np.sum(np.abs(plus) ** 2)))
    pmax, pmin = max(ps), min(ps)
    return (pmax - pmin) / (pmax + pmin)


def D_joint(gamma: float) -> float:
    """Trace-distance distinguishability of the joint (record, target) marker."""
    r0, r1 = record_branch_states(gamma)
    t0, t1 = order_branch_targets(A_CANON, B_CANON, PSI_TARGET)
    j0, j1 = np.kron(r0, t0), np.kron(r1, t1)
    return trace_distance(dm(j0), dm(j1))


def two_order_curves(gammas=GAMMA_SWEEP) -> dict:
    """The (D, V) trade-off curve and every exact relation, on the sweep."""
    gammas = np.asarray(gammas, dtype=float)
    V0 = abs(order_overlap_K(A_CANON, B_CANON, PSI_TARGET))
    Dt0 = math.sqrt(max(0.0, 1.0 - V0**2))
    D = np.array([D_record(g) for g in gammas])
    Dz = np.array([D_z_readout(g) for g in gammas])
    V = np.array([visibility_exact(g) for g in gammas])
    Dj = np.array([D_joint(g) for g in gammas])
    P_hel = 0.5 * (1.0 + D)
    resid_D = float(np.max(np.abs(D - np.sin(gammas / 2.0))))
    resid_V = float(np.max(np.abs(V - V0 * np.cos(gammas / 2.0))))
    resid_Dz = float(np.max(np.abs(Dz - D**2)))
    resid_norm_duality = float(np.max(np.abs(D**2 + (V / V0) ** 2 - 1.0)))
    resid_englert = float(np.max(np.abs(Dj**2 + V**2 - 1.0)))
    resid_three_way = float(
        np.max(np.abs(D**2 + V**2 + (1.0 - D**2) * Dt0**2 - 1.0))
    )
    slack = 1.0 - (D**2 + V**2)
    resid_slack = float(np.max(np.abs(slack - (1.0 - V0**2) * (1.0 - D**2))))
    return {
        "gammas": list(map(float, gammas)),
        "V0": V0,
        "Dt0": Dt0,
        "D_record": list(map(float, D)),
        "D_z_readout": list(map(float, Dz)),
        "V": list(map(float, V)),
        "D_joint": list(map(float, Dj)),
        "helstrom_success": list(map(float, P_hel)),
        "max_residual_D_vs_sin_half_gamma": resid_D,
        "max_residual_V_vs_V0_cos_half_gamma": resid_V,
        "max_residual_Dz_vs_D_squared": resid_Dz,
        "max_residual_normalized_duality": resid_norm_duality,
        "max_residual_englert_joint_saturation": resid_englert,
        "max_residual_three_way_decomposition": resid_three_way,
        "max_residual_slack_identity": resid_slack,
        "candidate_bound_min_slack": float(np.min(slack)),
        "D_strictly_increasing": bool(np.all(np.diff(D) > 0.0)),
        "V_strictly_decreasing": bool(np.all(np.diff(V) < 0.0)),
    }


# --------------------------------------------------------------------------- #
# Accessibility: measured vs traced record (the (1)/(2) boundary)
# --------------------------------------------------------------------------- #

def accessibility_invariance(gammas=GAMMA_SWEEP) -> dict:
    """Reduced (c, t) process state: traced record vs measured-and-forgotten.

    Elementary but load-bearing: Tr_r rho == Tr_r (sum_o Pi_o rho Pi_o)
    identically, so whether the record is read (and by whom) is invisible to
    every marginal of the reduced process. The record-fixed (1) vs
    causally-separable (2) boundary therefore cannot live in process
    statistics at fixed gamma; it lives in the record holder's postdiction
    capability D(gamma). Asserted numerically to machine precision.
    """
    max_diff = 0.0
    for g in gammas:
        state = switch_state_circuit(g)
        rho = dm(state)
        pi0 = kron_all(I2, P0, I2)
        pi1 = kron_all(I2, P1, I2)
        rho_meas = pi0 @ rho @ pi0 + pi1 @ rho @ pi1
        t_traced = rdm(state, DIMS2, (0, 2))
        # rdm of a mixed state, computed directly
        big = rho_meas.reshape(2, 2, 2, 2, 2, 2)
        t_meas = np.einsum("arb crd->ab cd".replace(" ", ""), big)  # trace r
        t_meas = t_meas.reshape(4, 4)
        max_diff = max(max_diff, float(np.max(np.abs(t_traced - t_meas))))
    return {"max_diff_traced_vs_measured": max_diff, "verdict": ACCESSIBILITY_VERDICT}


# --------------------------------------------------------------------------- #
# Q1D no-signalling certificate
# --------------------------------------------------------------------------- #

def no_signalling_certificate(
    gammas=(0.0, PI / 4, PI / 2, 3 * PI / 4, PI), phis=(0.0, 1.1)
) -> dict:
    """(c, r) readout marginals are exactly independent of the operation
    settings of both parties, and the record marginal is independent of the
    control phase. The applicable no-signalling surface for this architecture
    (a single target traverses both operations, so Bell-style spacelike
    marginal independence is not the relevant constraint; what must hold is
    that the order/record readout cannot be steered by local operation
    choices). The target marginal DOES depend on the settings -- reported, so
    the invariance check has teeth.
    """
    max_cr_diff = 0.0
    min_target_span = np.inf
    max_record_phi_diff = 0.0
    for g in gammas:
        for phi in phis:
            cr_dists = []
            t_dists = []
            for x in (0, 1):
                for y in (0, 1):
                    Ax = A_CANON @ np.linalg.matrix_power(rz(SETTING_DELTA_A), x)
                    By = B_CANON @ np.linalg.matrix_power(rx(SETTING_DELTA_B), y)
                    state = switch_state_circuit(g, phi=phi, A=Ax, B=By)
                    t = state.reshape(DIMS2)
                    p_cr = np.sum(np.abs(t) ** 2, axis=2)  # joint (c, r) in Z
                    p_t = np.sum(np.abs(t) ** 2, axis=(0, 1))  # target in Z
                    cr_dists.append(p_cr)
                    t_dists.append(p_t)
            for i in range(len(cr_dists)):
                for j in range(i + 1, len(cr_dists)):
                    max_cr_diff = max(
                        max_cr_diff, float(np.max(np.abs(cr_dists[i] - cr_dists[j])))
                    )
            span = max(
                float(np.max(np.abs(t_dists[i] - t_dists[j])))
                for i in range(len(t_dists))
                for j in range(i + 1, len(t_dists))
            )
            min_target_span = min(min_target_span, span)
        # record marginal independent of control phase (fixed settings)
        p_r = []
        for phi in phis:
            t = switch_state_circuit(g, phi=phi).reshape(DIMS2)
            p_r.append(np.sum(np.abs(t) ** 2, axis=(0, 2)))
        max_record_phi_diff = max(
            max_record_phi_diff, float(np.max(np.abs(p_r[0] - p_r[1])))
        )
    return {
        "max_cr_marginal_diff_over_settings": max_cr_diff,
        "max_record_marginal_diff_over_phase": max_record_phi_diff,
        "min_target_marginal_span_over_settings": float(min_target_span),
    }


# --------------------------------------------------------------------------- #
# Reduction audit: explicit Mach-Zehnder-with-which-path-marker mapping
# --------------------------------------------------------------------------- #

MZ_MAPPING = {
    "control c": "path degree of freedom p (which arm)",
    "order branch c=0 (A then B)": "path 0",
    "order branch c=1 (B then A)": "path 1",
    "record r (controlled-Ry(gamma))": "which-path marker m (same coupling)",
    "target t (branch states B@A psi / A@B psi)": (
        "internal dof carried by the photon: a second, fixed-strength "
        "which-path marker with branch overlap K"
    ),
    "D(gamma)": "which-path distinguishability of the marker (Englert D)",
    "V(gamma)": "fringe visibility (Englert V)",
}


def mz_state(gamma: float, phi: float, internal_pair) -> np.ndarray:
    """Mach-Zehnder photon: path p, marker m (controlled-Ry(gamma)), internal
    dof i with branch states internal_pair. Dims (p, m, i) = (2, 2, 2)."""
    i0, i1 = internal_pair
    m0, m1 = KET0.copy(), ry(gamma) @ KET0
    return (
        kron_all(KET0, m0, i0) + np.exp(1j * phi) * kron_all(KET1, m1, i1)
    ) / math.sqrt(2.0)


def plain_mz_curves(gammas=GAMMA_SWEEP) -> dict:
    """Plain MZ with marker only (no internal dof): D = sin, V = cos."""
    D, V = [], []
    for g in gammas:
        m0, m1 = KET0.copy(), ry(g) @ KET0
        D.append(trace_distance(dm(m0), dm(m1)))
        state = (np.kron(KET0, m0) + np.kron(KET1, m1)) / math.sqrt(2.0)
        rho_p = rdm(state, (2, 2), (0,))
        V.append(2.0 * abs(rho_p[0, 1]))
    return {"D": list(map(float, D)), "V": list(map(float, V))}


def reduction_audit(gammas=GAMMA_SWEEP) -> dict:
    """The kill-test: does the switch+record (D, V) structure coincide with
    the interferometric which-path/visibility duality under the explicit
    mapping? Three exact checks:
      (a) statevector identity: the mapped MZ state (internal dof loaded with
          the order-branch targets) equals the gate-built switch state;
      (b) plain-MZ curve coincidence: (D_switch, V_switch / V0) equals
          (D_MZ, V_MZ) pointwise;
      (c) Englert saturation with the joint marker (in two_order_curves).
    If all hold at 1e-12 the verdict is collapse (predeclared vocabulary).
    """
    t0, t1 = order_branch_targets(A_CANON, B_CANON, PSI_TARGET)
    max_state_diff = 0.0
    for g in gammas:
        for phi in (0.0, 0.7, 2.3):
            sw = switch_state_circuit(g, phi=phi)
            mz = mz_state(g, phi, (t0, t1))
            max_state_diff = max(max_state_diff, float(np.max(np.abs(sw - mz))))
    curves = two_order_curves(gammas)
    mzc = plain_mz_curves(gammas)
    V0 = curves["V0"]
    d_diff = float(
        np.max(np.abs(np.array(curves["D_record"]) - np.array(mzc["D"])))
    )
    v_diff = float(
        np.max(np.abs(np.array(curves["V"]) / V0 - np.array(mzc["V"])))
    )
    collapsed = (
        max_state_diff < TOL_EXACT
        and d_diff < TOL_EXACT
        and v_diff < TOL_EXACT
        and curves["max_residual_englert_joint_saturation"] < TOL_EXACT
    )
    return {
        "mapping": MZ_MAPPING,
        "max_statevector_diff_switch_vs_mapped_MZ": max_state_diff,
        "max_D_curve_diff_switch_vs_plain_MZ": d_diff,
        "max_normalized_V_curve_diff_switch_vs_plain_MZ": v_diff,
        "collapsed_to_duality": bool(collapsed),
        "verdict": REDUCTION_VERDICT if collapsed else (
            "residue: switch+record (D, V) structure does NOT coincide with "
            "the mapped interferometric duality; characterize before any claim"
        ),
    }


# --------------------------------------------------------------------------- #
# k=3 probe: partial (class-coarse) record over order superpositions
# --------------------------------------------------------------------------- #

OPS3 = None  # set below (A, B, C canonical)
OP_LABELS = "ABC"


def _ops3():
    global OPS3
    if OPS3 is None:
        OPS3 = (A_CANON, B_CANON, C_CANON)
    return OPS3


def u_of_order(perm) -> np.ndarray:
    """Unitary for applying ops in sequence perm[0] first, then perm[1], ..."""
    ops = _ops3()
    U = np.eye(2, dtype=complex)
    for idx in perm:
        U = ops[idx] @ U
    return U


def order_label(perm) -> str:
    return "".join(OP_LABELS[i] for i in perm)


ALL_ORDERS_6 = list(permutations(range(3)))  # 3! = 6 orders

# canonical 3-order subset and class partition: class by "A before B"
K3_ORDERS = [(0, 1, 2), (1, 0, 2), (2, 0, 1)]  # ABC, BAC, CAB
K3_CLASS_OF = [0, 1, 0]  # ABC: A<B -> 0; BAC: B<A -> 1; CAB: A<B -> 0

# 6-order canonical partition: permutation parity (even = 0)
def perm_parity(perm) -> int:
    inv = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return inv % 2


def class_record_states(gamma: float):
    """Class-coarse record states: class 0 -> |0>, class 1 -> Ry(gamma)|0>."""
    return KET0.copy(), ry(gamma) @ KET0


def k_state_branch_sum(orders, class_of, gamma: float, phases=None) -> np.ndarray:
    """Uniform coherent sum over `orders`, record writing only the class.

    Dims (k, 2, 2): control k-level (k <= 6, embeddable in <= 3 qubits;
    total Hilbert dimension <= 24, within the 6-qubit budget), record qubit,
    target qubit. Subsystems index-sorted (control, record, target).
    """
    k = len(orders)
    r_states = class_record_states(gamma)
    amp = 1.0 / math.sqrt(k)
    out = np.zeros(k * 2 * 2, dtype=complex)
    for i, perm in enumerate(orders):
        ph = 1.0 if phases is None else np.exp(1j * phases[i])
        t = u_of_order(perm) @ PSI_TARGET
        out += amp * ph * kron_all(basis(k, i), r_states[class_of[i]], t)
    return out


def k_state_circuit(orders, class_of, gamma: float) -> np.ndarray:
    """Gate-built version: controlled record coupler then controlled order
    unitary, applied to (uniform control) x |0>_r x psi_t. Cross-check path."""
    k = len(orders)
    c_in = np.ones(k, dtype=complex) / math.sqrt(k)
    state = kron_all(c_in, KET0, PSI_TARGET)
    r_states_ops = (np.eye(2, dtype=complex), ry(gamma))
    coupler = sum(
        kron_all(dm(basis(k, i)), r_states_ops[class_of[i]], I2)
        for i in range(k)
    )
    switch = sum(
        kron_all(dm(basis(k, i)), I2, u_of_order(orders[i])) for i in range(k)
    )
    return switch @ (coupler @ state)


def pairwise_normalized_coherences(state: np.ndarray, k: int) -> np.ndarray:
    """|rho_c[i,j]| / sqrt(rho_c[i,i] rho_c[j,j]) = |<r_j|r_i><t_j|t_i>|."""
    rho_c = rdm(state, (k, 2, 2), (0,))
    out = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            if i != j:
                den = math.sqrt(abs(rho_c[i, i].real * rho_c[j, j].real))
                out[i, j] = abs(rho_c[i, j]) / den if den > 0 else 0.0
    return out


def guess_prob_record_only(orders, class_of, gamma: float) -> float:
    """Optimal k-hypothesis order postdiction from the class-coarse record.

    All branches in a class share ONE record state (sigma for class 0, tau
    for class 1), so any POVM's success sum_o max_i tr(E_o rho_i)/k collapses
    to the binary structure: P = (1/k) (1 + ||tau - sigma||_pos-part)
    = (1/k) (1 + trace_distance). Achievable with the binary Helstrom
    measurement plus an arbitrary in-class representative guess; the
    achievability is independently confirmed on a projective-measurement grid
    (guess_prob_grid_check). Ceiling at gamma = pi: 2/k, strictly below 1
    whenever k > 2 -- the partial-access record ceiling.
    """
    k = len(orders)
    sigma, tau = class_record_states(gamma)
    return (1.0 / k) * (1.0 + trace_distance(dm(sigma), dm(tau)))


def guess_prob_grid_check(orders, class_of, gamma: float, n_grid: int = GUESS_GRID_N):
    """Best success over a grid of 2-outcome projective record measurements.

    The record branch states are real (Ry rotations of |0>), so the optimal
    projector lies in the real (x-z Bloch) plane, which the grid covers.
    Returns (best_grid_success, analytic_success).
    """
    k = len(orders)
    sigma, tau = class_record_states(gamma)
    rhos = [dm(sigma) if class_of[i] == 0 else dm(tau) for i in range(k)]
    best = 0.0
    for theta in np.linspace(0.0, PI, n_grid):
        v = np.array([math.cos(theta / 2.0), math.sin(theta / 2.0)], dtype=complex)
        E_plus = dm(v)
        E_minus = np.eye(2, dtype=complex) - E_plus
        p = (
            max(float(np.trace(E_plus @ r).real) for r in rhos)
            + max(float(np.trace(E_minus @ r).real) for r in rhos)
        ) / k
        best = max(best, p)
    return best, guess_prob_record_only(orders, class_of, gamma)


def class_helstrom(orders, class_of, gamma: float) -> float:
    """Optimal class postdiction (binary, class-size priors) from the record."""
    k = len(orders)
    m1 = sum(class_of)
    p0, p1 = (k - m1) / k, m1 / k
    sigma, tau = class_record_states(gamma)
    return 0.5 * (1.0 + trace_norm(p0 * dm(sigma) - p1 * dm(tau)))


def k_structural_checks(orders, class_of, gammas=GAMMA_SWEEP) -> dict:
    """Within-class flatness, cross-class pairwise duality, guess formula."""
    k = len(orders)
    base = pairwise_normalized_coherences(
        k_state_branch_sum(orders, class_of, 0.0), k
    )
    max_within_dev = 0.0
    max_cross_duality_resid = 0.0
    max_cross_scaling_resid = 0.0
    degenerate_pairs = 0
    for i, j in combinations(range(k), 2):
        if base[i, j] <= 1e-9:
            degenerate_pairs += 1
    for g in gammas:
        st = k_state_branch_sum(orders, class_of, g)
        nc = pairwise_normalized_coherences(st, k)
        s2 = math.sin(g / 2.0) ** 2
        for i, j in combinations(range(k), 2):
            if class_of[i] == class_of[j]:
                max_within_dev = max(max_within_dev, abs(nc[i, j] - base[i, j]))
            else:
                max_cross_scaling_resid = max(
                    max_cross_scaling_resid,
                    abs(nc[i, j] - math.cos(g / 2.0) * base[i, j]),
                )
                if base[i, j] > 1e-9:
                    max_cross_duality_resid = max(
                        max_cross_duality_resid,
                        abs(s2 + (nc[i, j] / base[i, j]) ** 2 - 1.0),
                    )
    p0 = guess_prob_record_only(orders, class_of, 0.0)
    p_pi = guess_prob_record_only(orders, class_of, PI)
    return {
        "k": k,
        "orders": [order_label(p) for p in orders],
        "class_of": list(class_of),
        "max_within_class_flatness_dev": max_within_dev,
        "max_cross_class_duality_residual": max_cross_duality_resid,
        "max_cross_class_cos_scaling_residual": max_cross_scaling_resid,
        "degenerate_pairs_skipped_for_duality": degenerate_pairs,
        "guess_prob_at_0": p0,
        "guess_prob_at_pi": p_pi,
        "guess_ceiling_is_2_over_k": abs(p_pi - 2.0 / k) < TOL_EXACT,
    }


def k3_canonical_analysis(gammas=GAMMA_SWEEP) -> dict:
    """Full canonical k=3 analysis, including global scalarization probes."""
    orders, class_of = K3_ORDERS, K3_CLASS_OF
    k = len(orders)
    struct = k_structural_checks(orders, class_of, gammas)
    # circuit-vs-branch-sum cross-check
    max_circ_diff = max(
        float(
            np.max(
                np.abs(
                    k_state_branch_sum(orders, class_of, g)
                    - k_state_circuit(orders, class_of, g)
                )
            )
        )
        for g in gammas
    )
    base = pairwise_normalized_coherences(
        k_state_branch_sum(orders, class_of, 0.0), k
    )
    pair_base = {
        f"{order_label(orders[i])}|{order_label(orders[j])}": float(base[i, j])
        for i, j in combinations(range(k), 2)
    }
    # curves
    P_guess = [guess_prob_record_only(orders, class_of, g) for g in gammas]
    P_class = [class_helstrom(orders, class_of, g) for g in gammas]
    D_glob = [(p - 1.0 / k) / (1.0 - 1.0 / k) for p in P_guess]
    # global scalarizations of "visibility": normalized pairwise coherences
    scalarizations = {"mean": [], "min": [], "max": []}
    for g in gammas:
        st = k_state_branch_sum(orders, class_of, g)
        nc = pairwise_normalized_coherences(st, k)
        vals = [
            nc[i, j] / base[i, j]
            for i, j in combinations(range(k), 2)
            if base[i, j] > 1e-9
        ]
        scalarizations["mean"].append(float(np.mean(vals)))
        scalarizations["min"].append(float(np.min(vals)))
        scalarizations["max"].append(float(np.max(vals)))
    circle = {}
    for name, vs in scalarizations.items():
        resid = [d**2 + v**2 - 1.0 for d, v in zip(D_glob, vs)]
        circle[name] = {
            "max_circle_residual": float(np.max(np.abs(resid))),
            "residual_at_pi": float(resid[-1]),
            "stays_on_circle": bool(np.max(np.abs(resid)) < 1e-9),
        }
    # grid achievability for the guessing formula (three representative gammas)
    grid_checks = {}
    for g in (0.0, PI / 2, PI):
        best, analytic = guess_prob_grid_check(orders, class_of, g)
        grid_checks[f"gamma={g:.6f}"] = {
            "grid_best": best,
            "analytic": analytic,
            "grid_le_analytic": bool(best <= analytic + 1e-9),
            "grid_achieves_within_tol": bool(analytic - best < GUESS_GRID_TOL),
        }
    return {
        "structure": struct,
        "max_circuit_vs_branch_sum_diff": max_circ_diff,
        "pair_baseline_coherences": pair_base,
        "P_guess": list(map(float, P_guess)),
        "P_guess_monotone_nondecreasing": bool(
            np.all(np.diff(P_guess) >= -TOL_EXACT)
        ),
        "P_class_helstrom": list(map(float, P_class)),
        "D_glob": list(map(float, D_glob)),
        "scalarizations": {k_: list(map(float, v)) for k_, v in scalarizations.items()},
        "circle_residuals": circle,
        "no_scalarization_stays_on_circle": bool(
            not any(c["stays_on_circle"] for c in circle.values())
        ),
        "grid_checks": grid_checks,
    }


def six_order_analysis(gammas=GAMMA_SWEEP) -> dict:
    """Full 6-order coherent sum with the parity class partition."""
    orders = ALL_ORDERS_6
    class_of = [perm_parity(p) for p in orders]
    struct = k_structural_checks(orders, class_of, gammas)
    return {
        "structure": struct,
        "class_partition": "permutation parity (even = 0)",
        "P_guess_at_pi": guess_prob_record_only(orders, class_of, PI),
    }


def exhaustive_family_sweep(gammas=GAMMA_SWEEP) -> dict:
    """Exhaustive verification over the declared finite family.

    (a) all C(6,3) = 20 three-order subsets x all 3 bipartitions into two
        nonempty classes (sizes {2,1}) = 60 configurations;
    (b) the full 6-order sum x all 31 bipartitions into two nonempty classes.
    For every configuration: within-class coherences exactly gamma-flat,
    cross-class coherences exactly cos(gamma/2)-scaled (pairwise duality where
    the baseline is nonzero), and the guess ceiling exactly 2/k at gamma=pi.
    """
    results = {"three_subsets": 0, "six_order_partitions": 0}
    max_within = 0.0
    max_duality = 0.0
    max_scaling = 0.0
    degenerate = 0
    all_ceiling = True
    for subset in combinations(ALL_ORDERS_6, 3):
        for one_idx in range(3):  # class 1 singleton position: 3 bipartitions
            class_of = [1 if i == one_idx else 0 for i in range(3)]
            s = k_structural_checks(list(subset), class_of, gammas)
            max_within = max(max_within, s["max_within_class_flatness_dev"])
            max_duality = max(max_duality, s["max_cross_class_duality_residual"])
            max_scaling = max(max_scaling, s["max_cross_class_cos_scaling_residual"])
            degenerate += s["degenerate_pairs_skipped_for_duality"]
            all_ceiling = all_ceiling and s["guess_ceiling_is_2_over_k"]
            results["three_subsets"] += 1
    for mask in range(1, 2**5):  # order 0 fixed in class 0 -> 31 bipartitions
        class_of = [0] + [(mask >> i) & 1 for i in range(5)]
        s = k_structural_checks(ALL_ORDERS_6, class_of, gammas)
        max_within = max(max_within, s["max_within_class_flatness_dev"])
        max_duality = max(max_duality, s["max_cross_class_duality_residual"])
        max_scaling = max(max_scaling, s["max_cross_class_cos_scaling_residual"])
        degenerate += s["degenerate_pairs_skipped_for_duality"]
        all_ceiling = all_ceiling and s["guess_ceiling_is_2_over_k"]
        results["six_order_partitions"] += 1
    all_pass = (
        max_within < TOL_EXACT
        and max_duality < TOL_EXACT
        and max_scaling < TOL_EXACT
        and all_ceiling
    )
    return {
        "n_three_order_configs": results["three_subsets"],
        "n_six_order_configs": results["six_order_partitions"],
        "max_within_class_flatness_dev": max_within,
        "max_cross_class_duality_residual": max_duality,
        "max_cross_class_cos_scaling_residual": max_scaling,
        "total_degenerate_pairs_skipped": degenerate,
        "guess_ceiling_2_over_k_everywhere": bool(all_ceiling),
        "all_pass": bool(all_pass),
    }


def full_resolution_contrast() -> dict:
    """Contrast config: a FULL-resolution record (k-level record register,
    r_i = |i> at gamma = pi) over the canonical 3-order subset. Shows the
    k=3 ceiling is a consequence of class-coarse access, not of k itself:
    the full-resolution perfect record achieves postdiction 1 and kills ALL
    pairwise coherence (the binary-duality corner), while the class-coarse
    perfect record achieves 2/3 with within-class coherence intact.
    """
    orders = K3_ORDERS
    k = len(orders)
    # dims (k, k, 2): control k-level, record k-level, target qubit
    out = np.zeros(k * k * 2, dtype=complex)
    for i, perm in enumerate(orders):
        t = u_of_order(perm) @ PSI_TARGET
        out += (1.0 / math.sqrt(k)) * kron_all(basis(k, i), basis(k, i), t)
    rho_c = rdm(out, (k, k, 2), (0,))
    max_coh = max(
        abs(rho_c[i, j]) for i, j in combinations(range(k), 2)
    )
    # postdiction via the record's own basis measurement (orthogonal records)
    p_succ = 0.0
    st = out.reshape(k, k, 2)
    for i in range(k):
        p_succ += float(np.sum(np.abs(st[:, i, :][i]) ** 2))
    return {
        "P_guess_full_resolution_at_pi": p_succ,
        "max_pairwise_coherence_at_pi": float(max_coh),
        "class_coarse_P_guess_at_pi": guess_prob_record_only(
            K3_ORDERS, K3_CLASS_OF, PI
        ),
        "class_coarse_max_within_coherence_at_pi": float(
            np.max(
                pairwise_normalized_coherences(
                    k_state_branch_sum(K3_ORDERS, K3_CLASS_OF, PI), k
                )
            )
        ),
    }


# --------------------------------------------------------------------------- #
# Asymmetric-control spot check (Greenberger-Yasin predictability axis, noted)
# --------------------------------------------------------------------------- #

def asymmetric_control_spot_check() -> dict:
    """One asymmetric-control configuration: V = 2 |alpha| |beta| |O| with
    O the joint (record x target) branch overlap. The predictability axis
    P = ||alpha|^2 - |beta|^2| of Greenberger-Yasin is known structure and is
    disclosed, not swept: D here is defined at equal priors throughout."""
    alpha, beta = math.cos(0.3), math.sin(0.3)
    g = 1.1
    state = switch_state_circuit(g, alpha=alpha, beta=beta)
    rho_c = rdm(state, DIMS2, (0,))
    V = 2.0 * abs(rho_c[0, 1])
    r0, r1 = record_branch_states(g)
    t0, t1 = order_branch_targets(A_CANON, B_CANON, PSI_TARGET)
    O = np.vdot(np.kron(r0, t0), np.kron(r1, t1))
    return {
        "alpha": alpha,
        "beta": beta,
        "gamma": g,
        "V": float(V),
        "prediction_2_alpha_beta_absO": float(2.0 * alpha * beta * abs(O)),
        "residual": float(abs(V - 2.0 * alpha * beta * abs(O))),
    }


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #

def run_analysis() -> dict:
    curves = two_order_curves()
    audit = reduction_audit()
    k3 = k3_canonical_analysis()
    six = six_order_analysis()
    exhaustive = exhaustive_family_sweep()
    contrast = full_resolution_contrast()
    return {
        "artifact": "T395-record-order-tradeoff-probe",
        "version": "v0.1",
        "conventions": {
            "subsystem_order": "(c, r, t) index-sorted; tuples read (c, r, t)",
            "order_branch_c0": "A then B (target B@A|psi>)",
            "order_branch_c1": "B then A (target A@B|psi>)",
            "gamma_sweep": f"{len(GAMMA_SWEEP)} values on [0, pi]",
        },
        "candidate_pair_table": candidate_pair_table(),
        "canonical_pair": CANONICAL_PAIR_NAME,
        "two_order": curves,
        "accessibility": accessibility_invariance(),
        "no_signalling": no_signalling_certificate(),
        "asymmetric_control_spot_check": asymmetric_control_spot_check(),
        "reduction_audit": audit,
        "k3_canonical": k3,
        "six_order": six,
        "exhaustive_family_sweep": exhaustive,
        "full_resolution_contrast": contrast,
        "verdicts": {
            "reduction": audit["verdict"],
            "k3": K3_VERDICT,
            "accessibility": ACCESSIBILITY_VERDICT,
        },
    }


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(res, indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T395 Record-Order Trade-off Probe")
    print("=" * 70)
    two = res["two_order"]
    print(f"canonical pair:                    {res['canonical_pair']} "
          f"(|K| = V0 = {two['V0']:.6f})")
    print(f"D(0), D(pi):                       {two['D_record'][0]:.6f}, "
          f"{two['D_record'][-1]:.6f}")
    print(f"V(0), V(pi):                       {two['V'][0]:.6f}, "
          f"{two['V'][-1]:.6f}")
    print(f"D = sin(g/2) max residual:         "
          f"{two['max_residual_D_vs_sin_half_gamma']:.3e}")
    print(f"V = V0 cos(g/2) max residual:      "
          f"{two['max_residual_V_vs_V0_cos_half_gamma']:.3e}")
    print(f"D^2 + (V/V0)^2 = 1 max residual:   "
          f"{two['max_residual_normalized_duality']:.3e}")
    print(f"D_joint^2 + V^2 = 1 max residual:  "
          f"{two['max_residual_englert_joint_saturation']:.3e}")
    print(f"three-way decomposition residual:  "
          f"{two['max_residual_three_way_decomposition']:.3e}")
    print(f"D_Z = D^2 max residual:            "
          f"{two['max_residual_Dz_vs_D_squared']:.3e}")
    print(f"accessibility (trace vs measure):  "
          f"{res['accessibility']['max_diff_traced_vs_measured']:.3e}")
    ns = res["no_signalling"]
    print(f"no-signalling (c,r) marginal diff: "
          f"{ns['max_cr_marginal_diff_over_settings']:.3e} "
          f"(target span {ns['min_target_marginal_span_over_settings']:.4f} -- "
          f"check has teeth)")
    ra = res["reduction_audit"]
    print(f"switch vs mapped-MZ statevector:   "
          f"{ra['max_statevector_diff_switch_vs_mapped_MZ']:.3e}")
    print(f"plain-MZ curve coincidence (D, V): "
          f"{ra['max_D_curve_diff_switch_vs_plain_MZ']:.3e}, "
          f"{ra['max_normalized_V_curve_diff_switch_vs_plain_MZ']:.3e}")
    print(f"REDUCTION AUDIT COLLAPSED:         {ra['collapsed_to_duality']}")
    k3 = res["k3_canonical"]
    s = k3["structure"]
    print("-" * 70)
    print(f"k=3 canonical subset:              {s['orders']} "
          f"classes {s['class_of']} (class by 'A before B')")
    print(f"  within-class flatness dev:       "
          f"{s['max_within_class_flatness_dev']:.3e}")
    print(f"  cross-class pairwise duality:    "
          f"{s['max_cross_class_duality_residual']:.3e}")
    print(f"  P_guess(0), P_guess(pi):         {s['guess_prob_at_0']:.6f}, "
          f"{s['guess_prob_at_pi']:.6f}  (ceiling 2/3)")
    for name, c in k3["circle_residuals"].items():
        print(f"  scalarization '{name}': circle residual at pi = "
              f"{c['residual_at_pi']:+.6f} (on circle: {c['stays_on_circle']})")
    print(f"  no scalarization stays on circle: "
          f"{k3['no_scalarization_stays_on_circle']}")
    six = res["six_order"]
    print(f"6-order parity partition:          P_guess(pi) = "
          f"{six['P_guess_at_pi']:.6f}  (ceiling 1/3)")
    ex = res["exhaustive_family_sweep"]
    print(f"exhaustive family sweep:           "
          f"{ex['n_three_order_configs']} three-order + "
          f"{ex['n_six_order_configs']} six-order configs, all_pass = "
          f"{ex['all_pass']}")
    fc = res["full_resolution_contrast"]
    print(f"full-resolution contrast at pi:    P_guess = "
          f"{fc['P_guess_full_resolution_at_pi']:.6f}, max coherence = "
          f"{fc['max_pairwise_coherence_at_pi']:.3e} (vs class-coarse "
          f"{fc['class_coarse_P_guess_at_pi']:.6f} with within-class "
          f"coherence {fc['class_coarse_max_within_coherence_at_pi']:.6f})")
    print("-" * 70)
    print("VERDICTS")
    for k_, v in res["verdicts"].items():
        print(f"[{k_}] {v}")
