"""T411: Departed-Record Capability Discriminator -- the big-swing
fixture of the primary open problem, built on T410's departure boundary.

THE OPEN PROBLEM (open-problems/region-indexed-capability-discriminator
.md) demands two capability states exactly equal under ALL R-supported
statistics -- observational AND under every declared R-supported
intervention -- yet separated by a boundary-crossing task menu, with
the crossing FORCED by the declared setup and the completing datum not
merely undeclared but physically unavailable. Its success criterion,
quoted: "No functional of R-supported statistics, including statistics
under all declared R-supported interventions, separates the two
capability states; but a boundary-crossing task menu separates them."

THE FIXTURE. T392's measurement core (S at phase phi; weak meter M at
theta_meter = pi/3, measured, M = 0 selected, M removed -- pure,
factorized; CNOT S -> REC), then m <= 3 broadcast collisions
REC -> E1_i at theta = pi (T410's free-off collision = exactly
controlled-Ry(pi)) into fresh Gibbs(beta) tier-1 carriers.
  State A (shallow dispersal): stop; tier-1 retained, holding the
    which-way correlations.
  State B (deep dispersal): each E1_i cascades once with a fresh
    Gibbs(beta) tier-2 carrier E2_i, which then DEPARTS (partial
    trace -- T410's boundary). Primary cascade: resonant full SWAP
    (record MOVES; retained state exactly rho_R (x) tau^(x)m).
    Contrast cascade: controlled-Ry(pi) with E1_i control (record
    COPIED deeper; induced channel on E1_i = exact Z-dephasing).
Region R = {S, M, REC}; reach R+ = R + tier-1; positive-control reach
R++ = R+ + tier-2 (retained in that run). Reach IS the physically
retained register set (T410 departure convention); menu at every reach
= ALL CPTP channels on the reach with unlimited work ancillas (pure or
Gibbs; dilation lemma asserted). Task: restore phase-locked
conditional X-visibility >= v* = 0.9.

PREDECLARED LEGS (spec tests/T411-departed-record-capability-
discriminator.md, frozen before this file existed; failure legs are
reportable verdicts):

  1. Equality, observational: rho_R^A = rho_R^B entrywise < 1e-12
     across PHI_CERT + PHI_LOCK_GRID, every beta, m, both cascades.
  2. Equality, interventional: carried by the environment-side channel
     LEMMA (B = (id_R (x) Lambda_E)(A), Lambda_E on tier-1 factors
     only, commutes with every R-supported sequence, trace-preserving);
     numerics assert the lemma operator-level (abstract Kraus, no
     tier-2 register) plus a predeclared family: 12 unitaries, 2
     instruments, 1 sequential composition, 15 seeded Haar rows
     (illustrative), commutation-in-action rows.
  3. Forcing at R: BOTH states final-relative-to-R, certified against
     all channels with unlimited work (phi-independence < 1e-12 and
     trace-norm bound < 1e-12, work-dilation invariant): the task
     cannot be re-posed inside R, so boundary crossing is not optional.
  4. Separation at R+: A restorable-at-R+ (un-write restores
     vis_A = 4 sqrt(3)/7 = 0.989743 >= v*); B final-relative-to-R+
     (SWAP: retained state exactly product, phi-independence < 1e-12,
     the strong all-channel certificate, work-invariant; broadcast
     contrast predicted exact too, with a predeclared fallback to the
     bound / undetermined_by_bound). One functional, one fixed menu,
     opposite verdicts. A's R+ record trace > 0.05 (required by
     T408's menu-support obstruction lemma).
  5. Physical boundary + positive control, priced: B restorable-at-R++
     (achieved vis_A); cascade ledger W = 0 (SWAP), Q = (3/7)
     tanh(beta/2), Sigma two-way identity < 1e-10, typed inf at
     beta = inf; at beta = 0 the cascade books Sigma = H(3/7) =
     0.682908 nats -- exactly the departed mutual information -- with
     zero work and zero heat; restoration work = T410's refund law.
  6. beta = 0 marginal blindness: EVERY proper-subset marginal of the
     R+ register set identical between A and B (< 1e-12, all subsets
     enumerated) while the full joints differ by trace distance
     exactly vis_A/2 = 0.494872; at beta = inf the carrier marginals
     differ by exactly (3/7) tanh(beta/2) = 3/7 and TD (SWAP) =
     (3 + sqrt(57))/14 = 0.753560; mutual-information closed forms.
  7. Absorber battery: named computed controls for T399 (enlargement =
     the priced positive control), T400 (stipulated-flag control;
     compulsion clause disclosed as not modeled), T401 (joint-record
     completion returns a product for B(SWAP); returns the classical
     record for B(broadcast) and the verdict is STILL final --
     record/capability transversality), T402/T403/T405/T406
     (matched-declared-fields; verdict functional label-free),
     T398/T404 (resource projection run on itself; order content
     conceded; two interface residues with T404's conditional
     demotion clauses), T397/SBS (no markers, no key), Lieb-Robinson
     (not a light cone).
  8. Guardrails: Q1D record invariance, no-signalling out of R across
     the full intervention family, teeth (3/7) tanh(beta/2); R1
     untouched.

WHAT THIS DOES NOT EARN: no unconditional physical-boundary claim
(departure-by-trace is the reservoir idealization -- adopted, not
derived; transport rung named-unbuilt); no resolution of the open
problem by itself (promotion pauses for Joe); no thermodynamic theorem
(ledger bookkeeping at the computed states, finite-witness); no new
mathematics or physics (prior-art adjacency flagged from memory,
unverified); no claim promotion. Hostile review is QUEUED for this
artifact, not yet performed. T410 is recorded-tier machinery: every
T410-derived fact used here is re-asserted inside this artifact.

Register order (retained density matrix): S, REC, E1_1..E1_m and, in
R++ runs, E2_1..E2_m. M is projected (M = 0) and removed after the
meter.
"""

from __future__ import annotations

import math
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T392 primitives.
from models.fixed_sbs_key_reversal_divergence import _HADAMARD

# T393 machinery: certificate sweep, lock grid, trace norm, Haar.
from models.causal_forcing_access_asymmetry import (
    PHI_CERT,
    PHI_LOCK_GRID,
    _trace_norm,
    haar_unitary,
)

# T410 substrate (recorded tier -- hostile review queued; every fact
# used here is re-asserted by this artifact's own suite).
from models.thermal_collision_work_reach_frontier import (
    ANALYTIC_TOL,
    BRANCH1_WEIGHT,
    FLATNESS_TOL,
    H2_3_7,
    IDENTITY_TOL,
    P_M0,
    THETA_METER,
    V_STAR,
    VIS_A_ANALYTIC,
    _CNOT4,
    _I2,
    _NUM,
    _P0,
    _P1,
    _PAULI_X2,
    _PAULI_Y2,
    _SWAP4,
    _json_safe,
    collision_u,
    core_conditioned,
    core_full_dm,
    dm_append,
    dm_apply,
    dm_expect,
    dm_kraus,
    dm_ptrace,
    prepare_retained as t410_prepare_retained,
    rel_entropy_nats,
    tau_gibbs,
    trace_distance,
    vn_entropy_bits,
    vn_entropy_nats,
    w_rest_analytic,
)

# --------------------------------------------------------------------------- #
# Predeclared constants (spec-frozen; see the spec file for the trail)
# --------------------------------------------------------------------------- #

S_POS, REC_POS = 0, 1

M_SWEEP = (1, 2, 3)
BETA_SWEEP = (math.inf, 1.0, 0.0)
THETA_BCAST = math.pi

CASCADE_SWAP = "swap"          # primary: record MOVES to tier 2
CASCADE_BROADCAST = "broadcast"  # contrast: record COPIED deeper
CASCADES = (CASCADE_SWAP, CASCADE_BROADCAST)

REACH_R, REACH_RP, REACH_RPP = "R", "R+", "R++"

PHI_INT = (0.0, 1.0, 2.0 * math.pi / 3.0)  # intervention-equality phases
HAAR_SEED = 20260704
HAAR_SAMPLES = 15

RECORD_TRACE_MIN = 0.05  # A's R+ certificate floor (obstruction lemma)
SIGMA_NONNEG_TOL = -1e-10

# Hand-derived corner values (spec, pre-run).
TD_BETA0 = VIS_A_ANALYTIC / 2.0                    # 0.494872...
TD_BETAINF_SWAP = (3.0 + math.sqrt(57.0)) / 14.0   # 0.753560...
SIGMA_CASC_BETA0_M1_NATS = H2_3_7 * math.log(2.0)  # H(3/7) = 0.682908 nats

INFINITE_COST = math.inf

VERDICT_TAGS = (
    "departed_record_capability_discriminator",
    "region_indexed_capability_states",
    "interventional_equality_lemma_carried",
    "boundary_crossing_menu_separation",
    "forcing_certified_inside_R",
    "departure_carried_completion_datum",
    "positive_control_priced",
    "absorber_battery_run",
    "no_claim_promotion",
)

BAND_FEASIBLE = "feasible_zero_cost"
BAND_CERTIFIED = "certified_infeasible"
BAND_UNDETERMINED = "undetermined_by_bound"

MENU_DECLARATION = (
    "ALL CPTP channels supported on the reach, with unlimited work "
    "ancillas in any (necessarily phi-independent) state, pure or "
    "Gibbs; reach = the physically retained register set of the run; "
    "no exclusion clause over co-present registers exists"
)

OPEN_PROBLEM_CRITERION = (
    "No functional of R-supported statistics, including statistics "
    "under all declared R-supported interventions, separates the two "
    "capability states; but a boundary-crossing task menu separates "
    "them."
)

# --------------------------------------------------------------------------- #
# Small exact operators
# --------------------------------------------------------------------------- #

_PAULI_Z2 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
_CZ4 = np.diag([1.0, 1.0, 1.0, -1.0]).astype(complex)
_PPLUS = _HADAMARD @ _P0 @ _HADAMARD   # |+><+|
_PMINUS = _HADAMARD @ _P1 @ _HADAMARD  # |-><-|
_KET0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)


def _u_bcast() -> np.ndarray:
    """T410's free-off collision at theta = pi: exactly controlled-Ry(pi)."""
    return collision_u(THETA_BCAST, False)


def e1_positions(m: int) -> tuple:
    return tuple(range(2, 2 + m))


def e2_positions(m: int) -> tuple:
    return tuple(range(2 + m, 2 + 2 * m))


# --------------------------------------------------------------------------- #
# Preparations (departure convention: reach = what the run retains)
# --------------------------------------------------------------------------- #

def prepare(
    variant: str, m: int, phi: float, beta: float, reach: str,
    cascade: str = CASCADE_SWAP,
) -> np.ndarray:
    """Exact retained density matrix, M = 0 conditioned.

    variant 'A': m broadcasts REC -> E1_i, stop.
    variant 'B': broadcasts, then one cascade collision per E1_i with a
    fresh Gibbs tier-2 carrier E2_i (SWAP or controlled-Ry(pi) with E1
    control), E2_i departing immediately unless the run is R++.
    Reach 'R' departs everything after the last collision; 'R+'
    retains tier-1; 'R++' retains both tiers (variant A appends m
    fresh, never-collided carriers so the register sets match).
    Order: S, REC, E1_1..E1_m [, E2_1..E2_m]."""
    if variant not in ("A", "B"):
        raise ValueError(f"variant {variant!r}")
    if m not in M_SWEEP:
        raise ValueError(f"m = {m} outside {M_SWEEP}")
    if reach not in (REACH_R, REACH_RP, REACH_RPP):
        raise ValueError(f"reach {reach!r}")
    rho, _ = core_conditioned(phi)  # pure DM on (S, REC)
    tau_b = tau_gibbs(beta)
    u_b = _u_bcast()
    for _ in range(m):
        k = int(round(math.log2(rho.shape[0])))
        rho = dm_append(rho, tau_b)
        rho = dm_apply(rho, u_b, (REC_POS, k))
    if variant == "B":
        casc = _SWAP4 if cascade == CASCADE_SWAP else u_b
        for i in range(m):
            k = int(round(math.log2(rho.shape[0])))
            rho = dm_append(rho, tau_b)
            rho = dm_apply(rho, casc, (2 + i, k))
            if reach != REACH_RPP:
                rho = dm_ptrace(rho, tuple(range(k)))
    elif reach == REACH_RPP:
        for _ in range(m):
            rho = dm_append(rho, tau_b)  # fresh, uncollided
    if reach == REACH_R:
        rho = dm_ptrace(rho, (S_POS, REC_POS))
    return rho


# --------------------------------------------------------------------------- #
# Protocols (reach-supported; the same code path for both states)
# --------------------------------------------------------------------------- #

def unwrite(rho: np.ndarray, m: int) -> np.ndarray:
    """R+ restoration attempt: controlled-Ry(-pi) REC -> E1_i per
    carrier (exact unitary undo of the broadcast for arbitrary diagonal
    carrier initial states), then CNOT S -> REC uncopy."""
    u_dag = _u_bcast().conj().T
    out = rho
    for pos in e1_positions(m):
        out = dm_apply(out, u_dag, (REC_POS, pos))
    return dm_apply(out, _CNOT4, (S_POS, REC_POS))


def uncascade_unwrite(rho: np.ndarray, m: int, cascade: str) -> np.ndarray:
    """R++ restoration for B: invert each cascade, then un-write."""
    gate = _SWAP4 if cascade == CASCADE_SWAP else _u_bcast().conj().T
    out = rho
    for i in range(m):
        out = dm_apply(out, gate, (2 + i, 2 + m + i))
    return unwrite(out, m)


def identity_protocol(rho: np.ndarray) -> np.ndarray:
    return rho


# --------------------------------------------------------------------------- #
# Figure of merit and certificates (T392/T393, on prepared families)
# --------------------------------------------------------------------------- #

def locked_visibility(prep_fn, protocol) -> float:
    """|mean_phi e^{i phi} 2 rho_S[0,1]| over the uniform lock grid."""
    total = 0.0 + 0.0j
    for phi in PHI_LOCK_GRID:
        out = protocol(prep_fn(phi))
        rho_s = dm_ptrace(out, (S_POS,))
        total += np.exp(1j * phi) * 2.0 * rho_s[0, 1]
    return float(abs(total / len(PHI_LOCK_GRID)))


def phi_independence_cert(prep_fn, phis=PHI_CERT) -> float:
    rhos = [prep_fn(phi) for phi in phis]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def channel_bound(prep_fn, grid=PHI_LOCK_GRID, extra_sigmas=()) -> float:
    """T393's all-channel bound 2(||Re X||_1 + ||Im X||_1),
    X = mean_phi e^{i phi} rho(phi); invariant under adjoined work
    registers (||A (x) sigma||_1 = ||A||_1), asserted numerically."""
    x = None
    for phi in grid:
        rho = prep_fn(phi)
        for sigma in extra_sigmas:
            rho = dm_append(rho, sigma)
        if x is None:
            x = np.zeros_like(rho)
        x = x + np.exp(1j * phi) * rho
    x = x / len(grid)
    herm = (x + x.conj().T) / 2.0
    anti = (x - x.conj().T) / 2.0j
    return 2.0 * (_trace_norm(herm) + _trace_norm(anti))


def verdict_from(prep_fn, protocol, reach: str) -> dict:
    """The ONE label-free verdict functional (spec: same code path for
    both states; input = retained state family + reach protocol only).
    restorable-at-<reach> iff achieved >= v*; else final-relative-to-
    <reach> iff phi cert < 1e-12 OR bound < v*; else undetermined."""
    achieved = locked_visibility(prep_fn, protocol)
    cert = phi_independence_cert(prep_fn)
    bound = channel_bound(prep_fn)
    if achieved >= V_STAR:
        verdict, band = f"restorable-at-{reach}", BAND_FEASIBLE
    elif cert < FLATNESS_TOL or bound < V_STAR:
        verdict, band = f"final-relative-to-{reach}", BAND_CERTIFIED
    else:
        verdict, band = BAND_UNDETERMINED, BAND_UNDETERMINED
    certified_by = (
        "achieving_protocol" if achieved >= V_STAR
        else "phi_independence" if cert < FLATNESS_TOL
        else "trace_norm_bound" if bound < V_STAR
        else "none"
    )
    return {
        "achieved": achieved,
        "phi_cert": cert,
        "bound": bound,
        "band": band,
        "verdict": verdict,
        "certified_by": certified_by,
    }


def _protocol_for(variant: str, m: int, reach: str, cascade: str):
    if reach == REACH_R:
        return identity_protocol
    if reach == REACH_RP:
        return lambda rho: unwrite(rho, m)
    if variant == "A":
        return lambda rho: unwrite(rho, m)
    return lambda rho: uncascade_unwrite(rho, m, cascade)


def verdict_cell(
    variant: str, m: int, beta: float, reach: str,
    cascade: str = CASCADE_SWAP,
) -> dict:
    prep = lambda phi: prepare(variant, m, phi, beta, reach, cascade)
    cell = verdict_from(prep, _protocol_for(variant, m, reach, cascade), reach)
    cell.update(
        {"variant": variant, "m": m, "beta": beta, "reach": reach,
         "cascade": cascade if variant == "B" else None}
    )
    return cell


# --------------------------------------------------------------------------- #
# The environment-side channel lemma (abstract Kraus, no tier-2 register)
# --------------------------------------------------------------------------- #

def replacement_kraus(beta: float):
    """Kraus of Y -> Tr[Y] tau_beta (SWAP-then-depart on tier 2)."""
    tau_b = tau_gibbs(beta)
    ks = []
    for j in (0, 1):
        pj = float(np.real(tau_b[j, j]))
        for k in (0, 1):
            op = np.zeros((2, 2), dtype=complex)
            op[j, k] = math.sqrt(pj)
            ks.append(op)
    return ks


def dephasing_kraus(beta: float):
    """Kraus of Y -> P0 Y P0 + P1 Y P1 (broadcast-then-depart on tier
    2; exact at every beta because Tr[Ry(pi) tau] = 0 for every
    diagonal tau)."""
    return [_P0, _P1]


def lemma_channel(rho: np.ndarray, m: int, beta: float, cascade: str):
    """(id_R (x) Lambda_E) applied to a retained R+ state, via the
    abstract per-carrier Kraus -- an independent construction path (no
    tier-2 register is ever appended)."""
    ks = (
        replacement_kraus(beta) if cascade == CASCADE_SWAP
        else dephasing_kraus(beta)
    )
    out = rho
    for pos in e1_positions(m):
        out = dm_kraus(out, ks, (pos,))
    return out


# --------------------------------------------------------------------------- #
# Predeclared R-supported intervention family (leg 2)
# --------------------------------------------------------------------------- #

def unitary_interventions():
    return (
        ("X_S", _PAULI_X2, (S_POS,)),
        ("Y_S", _PAULI_Y2, (S_POS,)),
        ("Z_S", _PAULI_Z2, (S_POS,)),
        ("H_S", _HADAMARD, (S_POS,)),
        ("X_REC", _PAULI_X2, (REC_POS,)),
        ("Y_REC", _PAULI_Y2, (REC_POS,)),
        ("Z_REC", _PAULI_Z2, (REC_POS,)),
        ("H_REC", _HADAMARD, (REC_POS,)),
        ("CNOT_S_REC", _CNOT4, (S_POS, REC_POS)),  # un-write attempt piece
        ("CNOT_REC_S", _CNOT4, (REC_POS, S_POS)),
        ("CZ_S_REC", _CZ4, (S_POS, REC_POS)),
        ("SWAP_S_REC", _SWAP4, (S_POS, REC_POS)),
    )


def instrument_branches(rho: np.ndarray, which: str):
    """The two predeclared measure-then-act instruments. Returns
    [(probability, normalized post state), ...]."""
    if which == "I1":  # measure REC in Z; on outcome 1 apply X_S
        projs, feedback, pos = (_P0, _P1), _PAULI_X2, REC_POS
        feed_pos = (S_POS,)
    elif which == "I2":  # measure S in X; on outcome 1 apply Z_REC
        projs, feedback, pos = (_PPLUS, _PMINUS), _PAULI_Z2, S_POS
        feed_pos = (REC_POS,)
    else:
        raise ValueError(which)
    branches = []
    for outcome, proj in enumerate(projs):
        b = dm_kraus(rho, [proj], (pos,))
        p = float(np.real(np.trace(b)))
        if outcome == 1:
            b = dm_apply(b, feedback, feed_pos)
        branches.append((p, b / p))
    return branches


def _r_marginal(rho: np.ndarray) -> np.ndarray:
    return dm_ptrace(rho, (S_POS, REC_POS))


def equality_interventional_report() -> dict:
    rng = np.random.default_rng(HAAR_SEED)
    haar_us = [haar_unitary(8, rng) for _ in range(HAAR_SAMPLES)]
    worst = {
        "lemma_operator_level": 0.0,
        "unitary_family": 0.0,
        "instrument_probs": 0.0,
        "instrument_states": 0.0,
        "sequential_probs": 0.0,
        "sequential_states": 0.0,
        "haar_family": 0.0,
        "commutation_in_action": 0.0,
    }
    pairs = 0
    for m in M_SWEEP:
        for beta in BETA_SWEEP:
            for cascade in CASCADES:
                for phi in PHI_INT:
                    a = prepare("A", m, phi, beta, REACH_RP)
                    b = prepare("B", m, phi, beta, REACH_RP, cascade)
                    pairs += 1
                    # (i) operator-level lemma: abstract Kraus path.
                    worst["lemma_operator_level"] = max(
                        worst["lemma_operator_level"],
                        float(np.max(np.abs(
                            lemma_channel(a, m, beta, cascade) - b
                        ))),
                    )
                    # (ii) unitary interventions: post R marginals.
                    for _, gate, pos in unitary_interventions():
                        ra = _r_marginal(dm_apply(a, gate, pos))
                        rb = _r_marginal(dm_apply(b, gate, pos))
                        worst["unitary_family"] = max(
                            worst["unitary_family"],
                            float(np.max(np.abs(ra - rb))),
                        )
                    # (iii) instruments: branch probs + post R states.
                    for which in ("I1", "I2"):
                        for (pa, sa), (pb, sb) in zip(
                            instrument_branches(a, which),
                            instrument_branches(b, which),
                        ):
                            worst["instrument_probs"] = max(
                                worst["instrument_probs"], abs(pa - pb)
                            )
                            worst["instrument_states"] = max(
                                worst["instrument_states"],
                                float(np.max(np.abs(
                                    _r_marginal(sa) - _r_marginal(sb)
                                ))),
                            )
                    # (iv) sequential composition: I1 -> Haar[0] -> I2.
                    for (p1a, s1a), (p1b, s1b) in zip(
                        instrument_branches(a, "I1"),
                        instrument_branches(b, "I1"),
                    ):
                        wa = dm_append(s1a, _KET0)
                        wb = dm_append(s1b, _KET0)
                        ka = int(round(math.log2(wa.shape[0])))
                        wa = dm_apply(wa, haar_us[0], (0, 1, ka - 1))
                        wb = dm_apply(wb, haar_us[0], (0, 1, ka - 1))
                        for (p2a, s2a), (p2b, s2b) in zip(
                            instrument_branches(wa, "I2"),
                            instrument_branches(wb, "I2"),
                        ):
                            worst["sequential_probs"] = max(
                                worst["sequential_probs"],
                                abs(p1a * p2a - p1b * p2b),
                            )
                            worst["sequential_states"] = max(
                                worst["sequential_states"],
                                float(np.max(np.abs(
                                    _r_marginal(s2a) - _r_marginal(s2b)
                                ))),
                            )
                    # (v) Haar rows (illustrative; never load-bearing).
                    for u_h in haar_us:
                        ha = dm_append(a, _KET0)
                        hb = dm_append(b, _KET0)
                        ka = int(round(math.log2(ha.shape[0])))
                        ha = dm_apply(ha, u_h, (0, 1, ka - 1))
                        hb = dm_apply(hb, u_h, (0, 1, ka - 1))
                        worst["haar_family"] = max(
                            worst["haar_family"],
                            float(np.max(np.abs(
                                _r_marginal(ha) - _r_marginal(hb)
                            ))),
                        )
                # (vi) commutation in action (phi = 1.0 rows):
                # Lambda_E(Phi_R(a)) = Phi_R(Lambda_E(a)).
                a1 = prepare("A", m, 1.0, beta, REACH_RP)
                for _, gate, pos in (
                    unitary_interventions()[0],   # X_S
                    unitary_interventions()[8],   # CNOT_S_REC
                ):
                    for cascade in CASCADES:
                        lhs = lemma_channel(
                            dm_apply(a1, gate, pos), m, beta, cascade
                        )
                        rhs = dm_apply(
                            lemma_channel(a1, m, beta, cascade), gate, pos
                        )
                        worst["commutation_in_action"] = max(
                            worst["commutation_in_action"],
                            float(np.max(np.abs(lhs - rhs))),
                        )
                for cascade in CASCADES:
                    for proj in (_P0, _P1):  # I1 branches, unnormalized
                        ba = dm_kraus(a1, [proj], (REC_POS,))
                        lhs = lemma_channel(ba, m, beta, cascade)
                        rhs = dm_kraus(
                            lemma_channel(a1, m, beta, cascade),
                            [proj], (REC_POS,),
                        )
                        worst["commutation_in_action"] = max(
                            worst["commutation_in_action"],
                            float(np.max(np.abs(lhs - rhs))),
                        )
    return {
        "pairs_checked": pairs,
        "haar_seed": HAAR_SEED,
        "haar_samples": HAAR_SAMPLES,
        "worst": worst,
        "worst_overall": max(worst.values()),
        "lemma": (
            "B's retained R+ state = (id_R (x) Lambda_E)(A's), Lambda_E "
            "acting only on tier-1 factors (replacement for SWAP, exact "
            "Z-dephasing for the broadcast cascade); Lambda_E commutes "
            "with every R-supported CPTP map, instrument, and work-"
            "assisted sequence (disjoint tensor factors) and is trace-"
            "preserving, so ALL R-supported outcome statistics -- "
            "including per-branch continuations -- are identical. The "
            "lemma carries the ALL quantifier; a later R-statistic "
            "depends on a conditioned joint state only through its R "
            "marginal (Tr_E[(Phi (x) id) sigma] = Phi(Tr_E sigma)), so "
            "per-branch R-marginal equality covers arbitrary "
            "continuations. The Haar rows are illustrative; sampling "
            "never carries the equality verdict."
        ),
    }


def equality_observational_report() -> dict:
    worst = 0.0
    checked = 0
    grid = tuple(PHI_CERT) + tuple(PHI_LOCK_GRID)
    for m in M_SWEEP:
        for beta in BETA_SWEEP:
            for cascade in CASCADES:
                for phi in grid:
                    ra = prepare("A", m, phi, beta, REACH_R)
                    rb = prepare("B", m, phi, beta, REACH_R, cascade)
                    worst = max(worst, float(np.max(np.abs(ra - rb))))
                    checked += 1
    return {
        "worst_rho_R_entrywise_diff": worst,
        "comparisons": checked,
        "note": (
            "rho_R^A = rho_R^B exactly: at theta = pi the broadcast "
            "multiplies the S-REC coherence block by f^m = 0, so rho_R "
            "= diag(4/7, 3/7) on {|00>, |11>}, phi-independent and "
            "identical for both states at every beta and m"
        ),
    }


# --------------------------------------------------------------------------- #
# Legs 3 + 4 -- forcing at R; separation at R+
# --------------------------------------------------------------------------- #

def forcing_report() -> dict:
    """Both states final-relative-to-R, certified all-channel with
    work-dilation invariance: the task cannot be re-posed inside R."""
    rows = []
    worst_cert = 0.0
    worst_bound = 0.0
    worst_dilation = 0.0
    for m in M_SWEEP:
        for beta in BETA_SWEEP:
            sig_pure = _KET0
            sig_gibbs = tau_gibbs(beta if not math.isinf(beta) else 1.0)
            for variant, cascade in (("A", CASCADE_SWAP),
                                     ("B", CASCADE_SWAP),
                                     ("B", CASCADE_BROADCAST)):
                prep = lambda phi: prepare(
                    variant, m, phi, beta, REACH_R, cascade
                )
                cell = verdict_from(prep, identity_protocol, REACH_R)
                bound_work = channel_bound(
                    prep, extra_sigmas=(sig_pure, sig_gibbs)
                )
                worst_cert = max(worst_cert, cell["phi_cert"])
                worst_bound = max(worst_bound, cell["bound"])
                worst_dilation = max(
                    worst_dilation, abs(bound_work - cell["bound"])
                )
                rows.append(
                    {"variant": variant, "cascade": cascade, "m": m,
                     "beta": beta, **{k: cell[k] for k in
                                      ("achieved", "phi_cert", "bound",
                                       "verdict")}}
                )
    all_final = all(r["verdict"] == "final-relative-to-R" for r in rows)
    return {
        "rows_checked": len(rows),
        "worst_phi_cert_at_R": worst_cert,
        "worst_bound_at_R": worst_bound,
        "worst_work_dilation_diff": worst_dilation,
        "all_final_relative_to_R": all_final,
        "sample_rows": rows[:6],
        "note": (
            "the restoration task is certified impossible inside R for "
            "BOTH states, against all channels with unlimited work "
            "(pure and Gibbs registers asserted): boundary crossing is "
            "forced by the task, not optional. Disclosed: T400's "
            "compulsion clause (an agent FORCED to attempt) is not "
            "modeled; forcing here is task-relative and certificate-"
            "carried."
        ),
    }


def separation_report() -> dict:
    """One functional, one fixed menu (R+), opposite verdicts."""
    rows_a, rows_b_swap, rows_b_bcast = [], [], []
    worst_a_restore = 0.0
    min_a_cert = math.inf
    worst_b_product = 0.0
    worst_b_cert_swap = 0.0
    worst_b_cert_bcast = 0.0
    worst_b_unwrite = 0.0
    worst_dilation_cert = 0.0
    worst_dilation_bound = 0.0
    for m in M_SWEEP:
        taus = [tau_gibbs(b) for b in BETA_SWEEP]
        for beta, tau_b in zip(BETA_SWEEP, taus):
            cell_a = verdict_cell("A", m, beta, REACH_RP)
            worst_a_restore = max(
                worst_a_restore, abs(cell_a["achieved"] - VIS_A_ANALYTIC)
            )
            min_a_cert = min(min_a_cert, cell_a["phi_cert"])
            rows_a.append(cell_a)

            cell_b = verdict_cell("B", m, beta, REACH_RP, CASCADE_SWAP)
            worst_b_cert_swap = max(worst_b_cert_swap, cell_b["phi_cert"])
            rows_b_swap.append(cell_b)
            # exact product structure (the joint-record completion
            # returns nothing): B(SWAP) R+ state = rho_R (x) tau^(x)m.
            for phi in (1.0, math.pi / 3.0):
                b = prepare("B", m, phi, beta, REACH_RP, CASCADE_SWAP)
                target = prepare("A", m, phi, beta, REACH_R)
                for _ in range(m):
                    target = dm_append(target, tau_b)
                worst_b_product = max(
                    worst_b_product, float(np.max(np.abs(b - target)))
                )
            # the same un-write that restores A returns nothing on B.
            prep_b = lambda phi: prepare(
                "B", m, phi, beta, REACH_RP, CASCADE_SWAP
            )
            worst_b_unwrite = max(
                worst_b_unwrite,
                locked_visibility(prep_b, lambda r: unwrite(r, m)),
            )
            # dilation invariance of B's certificate and bound (pure +
            # Gibbs work registers adjoined as constant factors).
            sig_pure = _KET0
            sig_gibbs = tau_gibbs(beta if not math.isinf(beta) else 1.0)
            rhos = [
                dm_append(dm_append(prep_b(phi), sig_pure), sig_gibbs)
                for phi in PHI_CERT
            ]
            cert_work = 0.0
            for i in range(len(rhos)):
                for j in range(i + 1, len(rhos)):
                    cert_work = max(
                        cert_work,
                        float(np.max(np.abs(rhos[i] - rhos[j]))),
                    )
            worst_dilation_cert = max(worst_dilation_cert, cert_work)
            bound_work = channel_bound(
                prep_b, extra_sigmas=(sig_pure, sig_gibbs)
            )
            worst_dilation_bound = max(
                worst_dilation_bound, abs(bound_work - cell_b["bound"])
            )

            cell_c = verdict_cell("B", m, beta, REACH_RP, CASCADE_BROADCAST)
            worst_b_cert_bcast = max(worst_b_cert_bcast, cell_c["phi_cert"])
            rows_b_bcast.append(cell_c)
    a_all_restorable = all(
        r["verdict"] == "restorable-at-R+" for r in rows_a
    )
    b_swap_all_final = all(
        r["verdict"] == "final-relative-to-R+" for r in rows_b_swap
    )
    b_bcast_all_final = all(
        r["verdict"] == "final-relative-to-R+" for r in rows_b_bcast
    )
    b_bcast_fallback_used = any(
        r["certified_by"] != "phi_independence" for r in rows_b_bcast
    )
    return {
        "A_rows": rows_a,
        "B_swap_rows": rows_b_swap,
        "B_broadcast_rows": rows_b_bcast,
        "A_all_restorable_at_Rplus": a_all_restorable,
        "worst_A_restore_vs_visA": worst_a_restore,
        "min_A_record_trace_cert": min_a_cert,
        "record_trace_floor": RECORD_TRACE_MIN,
        "B_swap_all_final_at_Rplus": b_swap_all_final,
        "worst_B_swap_product_residual": worst_b_product,
        "worst_B_swap_phi_cert": worst_b_cert_swap,
        "worst_B_unwrite_locked": worst_b_unwrite,
        "dilation_cert_with_work": worst_dilation_cert,
        "dilation_bound_diff_with_work": worst_dilation_bound,
        "B_broadcast_all_final_at_Rplus": b_bcast_all_final,
        "worst_B_broadcast_phi_cert": worst_b_cert_bcast,
        "B_broadcast_fallback_used": b_bcast_fallback_used,
        "obstruction_lemma_note": (
            "A's nonzero R+ record trace is REQUIRED by T408's "
            "menu-support obstruction lemma: a capability gap needs a "
            "statistical trace within the separating menu's support; "
            "the flat surface (R) is exactly the complement of that "
            "support"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 5 -- positive control at R++, priced (T410 ledger conventions)
# --------------------------------------------------------------------------- #

def cascade_ledger(m: int, beta: float, cascade: str, phi: float = 1.0) -> dict:
    """Replay B's preparation, booking each cascade collision:
    W = Delta<H_E1 + H_E2> (switching convention; the cascade touches
    only that pair), Q = Delta<H_E2>, Sigma = Delta S_complex + beta Q,
    cross-checked against I(complex : E2)_after + D(rho_E2' || tau) at
    finite beta; typed inf at beta = inf with Q > 0."""
    rho, _ = core_conditioned(phi)
    tau_b = tau_gibbs(beta)
    u_b = _u_bcast()
    for _ in range(m):
        k = int(round(math.log2(rho.shape[0])))
        rho = dm_append(rho, tau_b)
        rho = dm_apply(rho, u_b, (REC_POS, k))
    casc = _SWAP4 if cascade == CASCADE_SWAP else u_b
    e_tau = float(np.real(np.trace(_NUM @ tau_b)))
    finite = not math.isinf(beta)
    collisions = []
    mi_departed_total = 0.0
    for i in range(m):
        k = int(round(math.log2(rho.shape[0])))
        s_before = vn_entropy_nats(rho)
        joint = dm_append(rho, tau_b)
        e1_pos, e2_pos = 2 + i, k
        e_pair_before = (
            dm_expect(joint, _NUM, e1_pos) + dm_expect(joint, _NUM, e2_pos)
        )
        joint = dm_apply(joint, casc, (e1_pos, e2_pos))
        e_pair_after = (
            dm_expect(joint, _NUM, e1_pos) + dm_expect(joint, _NUM, e2_pos)
        )
        w_i = e_pair_after - e_pair_before
        q_i = dm_expect(joint, _NUM, e2_pos) - e_tau
        rho_c = dm_ptrace(joint, tuple(range(k)))
        rho_e2 = dm_ptrace(joint, (e2_pos,))
        s_after = vn_entropy_nats(rho_c)
        d_s = s_after - s_before
        mutual = s_after + vn_entropy_nats(rho_e2) - vn_entropy_nats(joint)
        mi_departed_total += mutual
        rec = {"i": i + 1, "W_i": w_i, "Q_i": q_i,
               "delta_S_complex_nats": d_s,
               "mutual_information_nats": mutual}
        if finite:
            sigma = d_s + beta * q_i
            rec["Sigma_i"] = sigma
            rec["sigma_identity_residual"] = abs(
                sigma - (mutual + rel_entropy_nats(rho_e2, tau_b))
            )
        else:
            rec["Sigma_i"] = INFINITE_COST if q_i > 1e-12 else d_s
            rec["sigma_identity_residual"] = None
        collisions.append(rec)
        rho = rho_c  # E2 departs
    sigmas = [c["Sigma_i"] for c in collisions
              if not math.isinf(c["Sigma_i"])]
    return {
        "m": m, "beta": beta, "cascade": cascade,
        "collisions": collisions,
        "total_W": sum(c["W_i"] for c in collisions),
        "total_Q": sum(c["Q_i"] for c in collisions),
        "total_Sigma_nats": (
            sum(sigmas) if len(sigmas) == m else INFINITE_COST
        ),
        "total_mutual_information_departed_nats": mi_departed_total,
        "min_Sigma": min(sigmas) if sigmas else None,
        "worst_identity_residual": max(
            (c["sigma_identity_residual"] for c in collisions
             if c["sigma_identity_residual"] is not None),
            default=None,
        ),
    }


def restoration_work(m: int, beta: float, cascade: str, phi: float = 1.0):
    """R++ restoration bookkeeping: un-cascade work per pair, then the
    un-write (T410's refund law, asserted cross-module)."""
    rho = prepare("B", m, phi, beta, REACH_RPP, cascade)
    free_pos = (REC_POS,) + e1_positions(m) + e2_positions(m)

    def e_free(r):
        return sum(dm_expect(r, _NUM, p) for p in free_pos)

    gate = _SWAP4 if cascade == CASCADE_SWAP else _u_bcast().conj().T
    w_uncascade = 0.0
    for i in range(m):
        before = e_free(rho)
        rho = dm_apply(rho, gate, (2 + i, 2 + m + i))
        w_uncascade += e_free(rho) - before
    u_dag = _u_bcast().conj().T
    w_unwrite = 0.0
    for pos in e1_positions(m):
        before = e_free(rho)
        rho = dm_apply(rho, u_dag, (REC_POS, pos))
        w_unwrite += e_free(rho) - before
    before = e_free(rho)
    rho = dm_apply(rho, _CNOT4, (S_POS, REC_POS))
    w_unwrite += e_free(rho) - before
    return w_uncascade, w_unwrite


def positive_control_report() -> dict:
    rows = []
    worst_restore = 0.0
    worst_w_swap = 0.0
    worst_q_closed_form = 0.0
    worst_identity = 0.0
    min_sigma = math.inf
    worst_unswap_work = 0.0
    worst_refund_law = 0.0
    sigma_beta0_m1 = None
    mi_beta0_m1 = None
    ledgers = []
    for m in M_SWEEP:
        for beta in BETA_SWEEP:
            for cascade in CASCADES:
                cell = verdict_cell("B", m, beta, REACH_RPP, cascade)
                worst_restore = max(
                    worst_restore, abs(cell["achieved"] - VIS_A_ANALYTIC)
                )
                rows.append(cell)
                led = cascade_ledger(m, beta, cascade)
                ledgers.append(led)
                if cascade == CASCADE_SWAP:
                    worst_w_swap = max(worst_w_swap, abs(led["total_W"]))
                    q_cf = BRANCH1_WEIGHT * (
                        1.0 if math.isinf(beta) else math.tanh(beta / 2.0)
                    )
                    worst_q_closed_form = max(
                        worst_q_closed_form,
                        max(abs(c["Q_i"] - q_cf) for c in led["collisions"]),
                    )
                    if beta == 0.0 and m == 1:
                        sigma_beta0_m1 = led["total_Sigma_nats"]
                        mi_beta0_m1 = led[
                            "total_mutual_information_departed_nats"
                        ]
                if led["worst_identity_residual"] is not None:
                    worst_identity = max(
                        worst_identity, led["worst_identity_residual"]
                    )
                if led["min_Sigma"] is not None:
                    min_sigma = min(min_sigma, led["min_Sigma"])
                w_unc, w_unw = restoration_work(m, beta, cascade)
                if cascade == CASCADE_SWAP:
                    worst_unswap_work = max(worst_unswap_work, abs(w_unc))
                worst_refund_law = max(
                    worst_refund_law,
                    abs(w_unw - w_rest_analytic(m, THETA_BCAST, beta, False)),
                )
        # A at R++ stays restorable (fresh uncollided tier-2 appended).
        cell_a = verdict_cell("A", m, 1.0, REACH_RPP)
        worst_restore = max(
            worst_restore, abs(cell_a["achieved"] - VIS_A_ANALYTIC)
        )
    all_restorable = all(r["verdict"] == "restorable-at-R++" for r in rows)
    return {
        "rows": rows,
        "all_B_restorable_at_Rpp": all_restorable,
        "worst_restore_vs_visA": worst_restore,
        "cascade_ledgers": ledgers,
        "worst_swap_cascade_work": worst_w_swap,
        "worst_Q_closed_form_residual": worst_q_closed_form,
        "worst_sigma_identity_residual": worst_identity,
        "min_Sigma_over_sweep": min_sigma,
        "sigma_beta0_m1_nats": sigma_beta0_m1,
        "sigma_beta0_m1_predeclared": SIGMA_CASC_BETA0_M1_NATS,
        "sigma_beta0_equals_departed_mi_residual": (
            abs(sigma_beta0_m1 - mi_beta0_m1)
            if sigma_beta0_m1 is not None else None
        ),
        "worst_unswap_work": worst_unswap_work,
        "worst_unwrite_refund_law_residual": worst_refund_law,
        "beta_inf_typing": (
            "at beta = inf with Q > 0, Sigma_casc is typed inf "
            "(zero-temperature limit; D(rho'||pure) divergent) -- "
            "extended-real bookkeeping, disclosed, not asserted"
        ),
        "beta0_note": (
            "the beta = 0 corner is predeclared as expected and NOT "
            "spun as entropy pricing: W = 0 and Q = 0, yet Sigma_casc "
            "= H(3/7) = 0.682908 nats = exactly the mutual information "
            "the departing tier carries away (the identity's I term "
            "with D = 0): the ledger books the record's departure as "
            "entropy production with zero work and zero heat flow"
        ),
        "conditionality": (
            "departure-by-trace is the standard reservoir idealization "
            "-- adopted, not derived (T410's concession, inherited "
            "verbatim); boundary physicality is conditional on the "
            "model class; the transport rung (work literally buying "
            "reach) stays named-unbuilt"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 6 -- beta = 0 marginal blindness (the sharpest tooth)
# --------------------------------------------------------------------------- #

def _mutual_information_bits(rho: np.ndarray, m: int) -> float:
    r = dm_ptrace(rho, (S_POS, REC_POS))
    e = dm_ptrace(rho, e1_positions(m))
    return (
        vn_entropy_bits(r) + vn_entropy_bits(e) - vn_entropy_bits(rho)
    )


def marginal_blindness_report() -> dict:
    worst_subset = 0.0
    subsets_checked = 0
    for m in M_SWEEP:
        n_reg = 2 + m
        for cascade in CASCADES:
            for phi in (1.0, math.pi / 3.0):
                a = prepare("A", m, phi, 0.0, REACH_RP)
                b = prepare("B", m, phi, 0.0, REACH_RP, cascade)
                for size in range(1, n_reg):
                    for keep in combinations(range(n_reg), size):
                        worst_subset = max(
                            worst_subset,
                            float(np.max(np.abs(
                                dm_ptrace(a, keep) - dm_ptrace(b, keep)
                            ))),
                        )
                        subsets_checked += 1
    td_beta0, td_betainf_swap, td_betainf_bcast = {}, {}, {}
    worst_td0 = worst_tdinf = 0.0
    for m in M_SWEEP:
        a0 = prepare("A", m, 1.0, 0.0, REACH_RP)
        b0 = prepare("B", m, 1.0, 0.0, REACH_RP, CASCADE_SWAP)
        td_beta0[str(m)] = trace_distance(a0, b0)
        worst_td0 = max(worst_td0, abs(td_beta0[str(m)] - TD_BETA0))
        ai = prepare("A", m, 1.0, math.inf, REACH_RP)
        bi = prepare("B", m, 1.0, math.inf, REACH_RP, CASCADE_SWAP)
        td_betainf_swap[str(m)] = trace_distance(ai, bi)
        worst_tdinf = max(
            worst_tdinf, abs(td_betainf_swap[str(m)] - TD_BETAINF_SWAP)
        )
        ci = prepare("B", m, 1.0, math.inf, REACH_RP, CASCADE_BROADCAST)
        td_betainf_bcast[str(m)] = trace_distance(ai, ci)  # reported
    # carrier-marginal local trace: (3/7) tanh(beta/2), fading to 0.
    marginal_rows = {}
    worst_marginal_cf = 0.0
    for beta in BETA_SWEEP:
        a = prepare("A", 2, 1.0, beta, REACH_RP)
        b = prepare("B", 2, 1.0, beta, REACH_RP, CASCADE_SWAP)
        diff = float(np.max(np.abs(
            dm_ptrace(a, (2,)) - dm_ptrace(b, (2,))
        )))
        cf = BRANCH1_WEIGHT * (
            1.0 if math.isinf(beta) else math.tanh(beta / 2.0)
        )
        worst_marginal_cf = max(worst_marginal_cf, abs(diff - cf))
        marginal_rows[str(beta)] = {
            "carrier_marginal_diff": diff, "closed_form_3_7_tanh": cf,
        }
    # the two cascades produce identical retained states at beta = 0.
    worst_variant_merge = 0.0
    for m in M_SWEEP:
        for phi in (1.0, math.pi / 3.0):
            worst_variant_merge = max(
                worst_variant_merge,
                float(np.max(np.abs(
                    prepare("B", m, phi, 0.0, REACH_RP, CASCADE_SWAP)
                    - prepare("B", m, phi, 0.0, REACH_RP, CASCADE_BROADCAST)
                ))),
            )
    # mutual-information closed forms (bits).
    mi_rows = {}
    worst_mi_cf = 0.0
    worst_mi_b_swap = 0.0
    for m in M_SWEEP:
        row = {}
        for beta in BETA_SWEEP:
            a = prepare("A", m, 1.0, beta, REACH_RP)
            b = prepare("B", m, 1.0, beta, REACH_RP, CASCADE_SWAP)
            c = prepare("B", m, 1.0, beta, REACH_RP, CASCADE_BROADCAST)
            mi_a = _mutual_information_bits(a, m)
            mi_b = _mutual_information_bits(b, m)
            mi_c = _mutual_information_bits(c, m)
            row[str(beta)] = {"I_A": mi_a, "I_B_swap": mi_b,
                              "I_B_broadcast": mi_c}
            worst_mi_b_swap = max(worst_mi_b_swap, abs(mi_b))
            if math.isinf(beta):
                worst_mi_cf = max(
                    worst_mi_cf,
                    abs(mi_a - 2.0 * H2_3_7),
                    abs(mi_c - H2_3_7),
                )
            elif beta == 0.0:
                worst_mi_cf = max(
                    worst_mi_cf, abs(mi_a - H2_3_7), abs(mi_c)
                )
        mi_rows[str(m)] = row
    return {
        "proper_subsets_checked_beta0": subsets_checked,
        "worst_proper_subset_marginal_diff_beta0": worst_subset,
        "td_full_joint_beta0_by_m": td_beta0,
        "td_beta0_predeclared": TD_BETA0,
        "worst_td_beta0_residual": worst_td0,
        "td_full_joint_betainf_swap_by_m": td_betainf_swap,
        "td_betainf_predeclared_swap": TD_BETAINF_SWAP,
        "worst_td_betainf_residual": worst_tdinf,
        "td_full_joint_betainf_broadcast_by_m": td_betainf_bcast,
        "carrier_marginal_rows": marginal_rows,
        "worst_carrier_marginal_closed_form_residual": worst_marginal_cf,
        "worst_cascade_variant_merge_beta0": worst_variant_merge,
        "mutual_information_bits": mi_rows,
        "worst_mi_closed_form_residual": worst_mi_cf,
        "worst_I_B_swap": worst_mi_b_swap,
        "finding": (
            "at beta = 0 EVERY proper-subset marginal of the retained "
            "R+ register set is identical between the two capability "
            "states -- 'which registers hold the discriminating datum' "
            "has no answer short of everything -- while the full joints "
            "differ by trace distance exactly vis_A/2 and the "
            "capability verdicts split; the LOCAL trace of dispersal "
            "depth fades as (3/7) tanh(beta/2) to exactly zero while "
            "both equality certificates and both capability verdicts "
            "are beta-blind. Flagged from memory, unverified: "
            "no-hiding-theorem lineage (Braunstein-Pati); discord-type "
            "locally-hidden correlations."
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 7 -- absorber-control battery
# --------------------------------------------------------------------------- #

def declared_fields(variant: str, m: int) -> dict:
    """The declared (bookkeeping) description of a capability state.
    Deliberately variant-INDEPENDENT except for its dict identity: the
    physical cascade history is NOT a declared field (it is a physical
    process with a ledger entry, disclosed separately)."""
    return {
        "registers_R": ("S", "M", "REC"),
        "registers_R_plus": ("S", "M", "REC")
        + tuple(f"E1_{i}" for i in range(1, m + 1)),
        "registers_R_plus_plus": ("S", "M", "REC")
        + tuple(f"E1_{i}" for i in range(1, m + 1))
        + tuple(f"E2_{i}" for i in range(1, m + 1)),
        "hamiltonians": (
            "H_REC = H_E = omega |1><1| (hbar = omega = 1); "
            "H_S = H_M = 0 (T410 declared assignment)"
        ),
        "collision_window": "tau = 1.0, g = theta/(2 tau), free terms off",
        "broadcast": "controlled-Ry(pi) REC -> E1_i",
        "carrier_initial_state": "tau_beta (Gibbs)",
        "menu": MENU_DECLARATION,
        "task": (
            "restore phase-locked conditional X-visibility >= v* = 0.9"
        ),
        "conditioning": "M = 0 dominant branch",
        "phase_grids": "PHI_CERT / PHI_LOCK_GRID (T393, unchanged)",
        "verdict_functional": (
            "one shared, label-free code path; inputs: retained state "
            "family + reach protocol only"
        ),
    }


def battery_report() -> dict:
    # T400 / T403-style stipulated-flag control: two copies of the SAME
    # physical preparation with different stipulated flags.
    s_provisional = prepare("A", 1, 1.0, 1.0, REACH_RP)
    s_sealed = prepare("A", 1, 1.0, 1.0, REACH_RP)
    flag_state_diff = float(np.max(np.abs(s_provisional - s_sealed)))
    prep = lambda phi: prepare("A", 1, phi, 1.0, REACH_RP)
    v1 = verdict_from(prep, lambda r: unwrite(r, 1), REACH_RP)
    v2 = verdict_from(prep, lambda r: unwrite(r, 1), REACH_RP)
    flag_verdict_moved = (v1["verdict"] != v2["verdict"]) or (
        abs(v1["achieved"] - v2["achieved"]) > 0.0
    )
    # matched declared fields (T402/T403/T405/T406 control).
    fields_equal = all(
        declared_fields("A", m) == declared_fields("B", m) for m in M_SWEEP
    )
    # verdict follows the state, not the label: apply the one
    # functional to both retained families at R+ (m = 1, beta = 1).
    prep_a = lambda phi: prepare("A", 1, phi, 1.0, REACH_RP)
    prep_b = lambda phi: prepare("B", 1, phi, 1.0, REACH_RP, CASCADE_SWAP)
    proto = lambda r: unwrite(r, 1)
    v_a = verdict_from(prep_a, proto, REACH_RP)["verdict"]
    v_b = verdict_from(prep_b, proto, REACH_RP)["verdict"]
    verdict_swaps_with_input = (
        v_a == "restorable-at-R+" and v_b == "final-relative-to-R+"
    )
    # resource projection (T398/T404) run on itself.
    profile_a = ("final-relative-to-R", "restorable-at-R+")
    profile_b = (
        "final-relative-to-R", "final-relative-to-R+", "restorable-at-R++"
    )
    return {
        "t399_enlarged_state": {
            "answer": (
                "the positive control IS the leg: enlargement (R++) "
                "restores B and its price is tabulated (leg 5). The "
                "claim is never 'the reviewer cannot compute'; at FIXED "
                "R+ -- full access to everything the B run retains -- "
                "the split is sourced in dispersal depth whose B-side "
                "trace is exactly zero (the product state). Against "
                "boundary relocation: B is final relative to EVERYTHING "
                "retained in its run; the R++ run is a different, "
                "counterfactual retention, run as the priced positive "
                "control."
            ),
        },
        "t400_stipulated_flag": {
            "flag_state_diff": flag_state_diff,
            "flag_moved_capability": bool(flag_verdict_moved),
            "answer": (
                "two copies of the same physical preparation carrying "
                "different stipulated flags are bit-identical and get "
                "identical verdicts: a stipulated label alone moves "
                "nothing; in T411 every declared field is matched and "
                "the capability still splits. The task functional reads "
                "no label. Disclosed: T400's compulsion clause (agent "
                "FORCED to attempt) is not modeled; forcing is task-"
                "relative and certificate-carried (leg 3)."
            ),
        },
        "t401_joint_record": {
            "answer": (
                "granting the COMPLETE retained joint state at R+ "
                "gives, for B(SWAP), an exact product (mutual "
                "information 0 -- leg 6): the completion is exhausted "
                "and returns nothing; completing further requires the "
                "departed tier, i.e. the open-system premise itself. "
                "Sharper, via the broadcast contrast: joint-record "
                "completion there DOES return the which-way datum "
                "(classical h2(3/7) bits at beta = inf) and the "
                "verdict is STILL final-relative-to-R+, certified -- "
                "the record datum and the capability are transverse; "
                "joint-record completion cannot absorb the split."
            ),
        },
        "t402_t406_matched_fields": {
            "declared_fields_equal": bool(fields_equal),
            "verdict_swaps_with_input": bool(verdict_swaps_with_input),
            "differing_item": (
                "the physical cascade history only (B: m cascade "
                "collisions with fresh Gibbs tier-2 carriers, departed) "
                "-- carried as a physical process with an energy/"
                "entropy ledger entry (leg 5), not as a declared "
                "bookkeeping field; operation unavailability "
                "(restoration infeasibility) is DERIVED by the one "
                "label-free verdict functional from the retained state, "
                "never stipulated as a flag, latch topology, or "
                "transition relation"
            ),
        },
        "t398_t404_resource_projection": {
            "profile_A": profile_a,
            "profile_B": profile_b,
            "conceded": (
                "admitted as resource objects, the per-reach capability "
                "profiles' ORDER content absorbs exactly as T398 "
                "showed (ordinary non-total convertibility) -- conceded"
            ),
            "residue_a_causal_indexing": (
                "work -- the athermality frame's own currency -- is "
                "certified unable to purchase what reach purchases "
                "(dilation-invariant certificates, pure and Gibbs work "
                "registers, legs 3-4); inherits T404 residue (a) WITH "
                "its predeclared conditional demotion clause: candidate "
                "absorbers dynamical resource theories / superchannels "
                "-- named, from memory, unverified; if verified as "
                "absorbing, this residue demotes per T404's clause"
            ),
            "residue_b_locally_hidden": (
                "the beta = 0 sharpening (leg 6: no proper subset holds "
                "the datum); candidate absorber Blackwell comparison of "
                "experiments -- named, from memory, unverified; same "
                "conditional demotion clause"
            ),
        },
        "t397_sbs_markers": {
            "answer": (
                "no class markers and no SBS closure key exist in the "
                "fixture: the task is a threshold on a computed "
                "functional of the post-protocol state, not a readout "
                "of any label; the stipulated-flag control is the "
                "numeric witness"
            ),
        },
        "lieb_robinson": {
            "answer": (
                "no geometry exists (all-to-one contact graph); the "
                "boundary is a departure boundary, not a light cone "
                "(Lieb-Robinson named as an absorber risk, from "
                "memory, unverified)"
            ),
        },
        "re_scope_clause": (
            "if the assembled object is standard (environment-assisted "
            "recovery / quantum Darwinism / data processing on a "
            "dilation), the artifact re-scopes to a repo-internal "
            "calibration of the certificate toolkit"
        ),
    }


# --------------------------------------------------------------------------- #
# Leg 8 -- guardrails (Q1D with teeth; R1 untouched)
# --------------------------------------------------------------------------- #

def q1d_report() -> dict:
    # Declared ordinary record P(S, M): invariant (broadcasts and
    # cascades never touch S or M), on the UNCONDITIONED state.
    ref = np.real(np.diag(dm_ptrace(core_full_dm(1.0), (0, 1))))
    configs = (
        ("A", 3, 1.0, CASCADE_SWAP),
        ("B", 2, 0.0, CASCADE_SWAP),
        ("B", 3, math.inf, CASCADE_BROADCAST),
        ("B", 1, 1.0, CASCADE_SWAP),
    )
    worst_record = 0.0
    for variant, m, beta, cascade in configs:
        rho = core_full_dm(1.0)  # S, M, REC (REC at position 2)
        tau_b = tau_gibbs(beta)
        u_b = _u_bcast()
        for _ in range(m):
            k = int(round(math.log2(rho.shape[0])))
            rho = dm_append(rho, tau_b)
            rho = dm_apply(rho, u_b, (2, k))
        if variant == "B":
            casc = _SWAP4 if cascade == CASCADE_SWAP else u_b
            for i in range(m):
                k = int(round(math.log2(rho.shape[0])))
                rho = dm_append(rho, tau_b)
                rho = dm_apply(rho, casc, (3 + i, k))
                rho = dm_ptrace(rho, tuple(range(k)))
        dist = np.real(np.diag(dm_ptrace(rho, (0, 1))))
        worst_record = max(worst_record, float(np.max(np.abs(dist - ref))))

    # No signalling out of R: every leg-2 R intervention leaves every
    # tier-1 marginal untouched (max over the family).
    worst_no_signal = 0.0
    for beta in BETA_SWEEP:
        a = prepare("A", 2, 1.0, beta, REACH_RP)
        before = [dm_ptrace(a, (p,)) for p in e1_positions(2)]
        for _, gate, pos in unitary_interventions():
            after = dm_apply(a, gate, pos)
            for p, ref_m in zip(e1_positions(2), before):
                worst_no_signal = max(
                    worst_no_signal,
                    float(np.max(np.abs(dm_ptrace(after, (p,)) - ref_m))),
                )
    # Teeth: the counterfactual R+ un-write moves tier-1 marginals by
    # exactly (3/7) tanh(beta/2).
    teeth_rows = {}
    worst_teeth_cf = 0.0
    for beta in BETA_SWEEP:
        a = prepare("A", 2, 1.0, beta, REACH_RP)
        after = unwrite(a, 2)
        tooth = max(
            float(np.max(np.abs(
                dm_ptrace(after, (p,)) - dm_ptrace(a, (p,))
            )))
            for p in e1_positions(2)
        )
        cf = BRANCH1_WEIGHT * (
            1.0 if math.isinf(beta) else math.tanh(beta / 2.0)
        )
        worst_teeth_cf = max(worst_teeth_cf, abs(tooth - cf))
        teeth_rows[str(beta)] = {
            "enlarged_protocol_moves_tier1_marginal": tooth,
            "teeth_analytic_3_7_tanh": cf,
        }
    # beta = 0 tooth carried by the visibility jump 0 -> vis_A.
    prep_r = lambda phi: prepare("A", 2, phi, 0.0, REACH_R)
    prep_rp = lambda phi: prepare("A", 2, phi, 0.0, REACH_RP)
    jump = {
        "achieved_at_R": locked_visibility(prep_r, identity_protocol),
        "achieved_at_Rplus": locked_visibility(
            prep_rp, lambda r: unwrite(r, 2)
        ),
    }
    return {
        "declared_record_invariance": worst_record,
        "worst_no_signal_out_of_R": worst_no_signal,
        "teeth_by_beta": teeth_rows,
        "worst_teeth_closed_form_residual": worst_teeth_cf,
        "beta0_visibility_jump": jump,
        "r1_note": (
            "R1 untouched: no claim about global temporal order or "
            "spacetime; the fixture is a discrete interaction sequence "
            "with a departure boundary, not a light cone "
            "(Lieb-Robinson is a named absorber risk, flagged from "
            "memory, unverified)"
        ),
    }


# --------------------------------------------------------------------------- #
# Construction anchors (cross-module against T410; product structure)
# --------------------------------------------------------------------------- #

def construction_report() -> dict:
    worst_cross_rp = 0.0
    worst_cross_r = 0.0
    for m in M_SWEEP:
        for beta in BETA_SWEEP:
            for phi in (1.0, math.pi / 3.0):
                a_rp = prepare("A", m, phi, beta, REACH_RP)
                t410_rp = t410_prepare_retained(
                    m, tuple(range(1, m + 1)), phi, THETA_BCAST, beta, False
                )
                worst_cross_rp = max(
                    worst_cross_rp, float(np.max(np.abs(a_rp - t410_rp)))
                )
                a_r = prepare("A", m, phi, beta, REACH_R)
                t410_r = t410_prepare_retained(
                    m, (), phi, THETA_BCAST, beta, False
                )
                worst_cross_r = max(
                    worst_cross_r, float(np.max(np.abs(a_r - t410_r)))
                )
    # marginal consistency: tracing the R+ state reproduces the R run.
    worst_marg = 0.0
    for variant, cascade in (("A", CASCADE_SWAP), ("B", CASCADE_SWAP),
                             ("B", CASCADE_BROADCAST)):
        rp = prepare(variant, 2, 1.0, 1.0, REACH_RP, cascade)
        r = prepare(variant, 2, 1.0, 1.0, REACH_R, cascade)
        worst_marg = max(
            worst_marg,
            float(np.max(np.abs(dm_ptrace(rp, (0, 1)) - r))),
        )
    probs = [core_conditioned(phi)[1] for phi in PHI_CERT]
    return {
        "worst_cross_module_A_Rplus_vs_T410": worst_cross_rp,
        "worst_cross_module_A_R_vs_T410": worst_cross_r,
        "worst_Rplus_to_R_marginal_consistency": worst_marg,
        "p_m0_values": probs,
        "worst_p_m0_deviation": max(abs(p - P_M0) for p in probs),
        "t410_standing_note": (
            "T410 is recorded-tier machinery (hostile review QUEUED); "
            "every T410-derived fact used here is re-asserted inside "
            "this artifact's own suite"
        ),
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

_ANALYSIS_CACHE: dict = {}


def run_analysis() -> dict:
    construction = construction_report()
    eq_obs = equality_observational_report()
    eq_int = equality_interventional_report()
    forcing = forcing_report()
    separation = separation_report()
    positive = positive_control_report()
    blindness = marginal_blindness_report()
    battery = battery_report()
    q1d = q1d_report()

    leg1 = eq_obs["worst_rho_R_entrywise_diff"] < FLATNESS_TOL
    leg2 = eq_int["worst_overall"] < FLATNESS_TOL
    leg3 = (
        forcing["all_final_relative_to_R"]
        and forcing["worst_phi_cert_at_R"] < FLATNESS_TOL
        and forcing["worst_bound_at_R"] < FLATNESS_TOL
        and forcing["worst_work_dilation_diff"] < FLATNESS_TOL
    )
    b_swap_certified = (
        separation["B_swap_all_final_at_Rplus"]
        and separation["worst_B_swap_phi_cert"] < FLATNESS_TOL
    )
    leg4 = (
        separation["A_all_restorable_at_Rplus"]
        and separation["worst_A_restore_vs_visA"] < ANALYTIC_TOL
        and separation["min_A_record_trace_cert"] > RECORD_TRACE_MIN
        and b_swap_certified
        and separation["worst_B_swap_product_residual"] < FLATNESS_TOL
        and separation["worst_B_unwrite_locked"] < FLATNESS_TOL
        and separation["dilation_cert_with_work"] < FLATNESS_TOL
        and separation["dilation_bound_diff_with_work"] < FLATNESS_TOL
        and separation["B_broadcast_all_final_at_Rplus"]
    )
    leg5 = (
        positive["all_B_restorable_at_Rpp"]
        and positive["worst_restore_vs_visA"] < ANALYTIC_TOL
        and positive["worst_swap_cascade_work"] < FLATNESS_TOL
        and positive["worst_Q_closed_form_residual"] < ANALYTIC_TOL
        and positive["worst_sigma_identity_residual"] < IDENTITY_TOL
        and positive["min_Sigma_over_sweep"] >= SIGMA_NONNEG_TOL
        and abs(
            positive["sigma_beta0_m1_nats"] - SIGMA_CASC_BETA0_M1_NATS
        ) < ANALYTIC_TOL
        and positive["sigma_beta0_equals_departed_mi_residual"]
        < IDENTITY_TOL
        and positive["worst_unswap_work"] < FLATNESS_TOL
        and positive["worst_unwrite_refund_law_residual"] < ANALYTIC_TOL
    )
    leg6 = (
        blindness["worst_proper_subset_marginal_diff_beta0"] < FLATNESS_TOL
        and blindness["worst_td_beta0_residual"] < ANALYTIC_TOL
        and blindness["worst_td_betainf_residual"] < ANALYTIC_TOL
        and blindness["worst_carrier_marginal_closed_form_residual"]
        < ANALYTIC_TOL
        and blindness["worst_cascade_variant_merge_beta0"] < FLATNESS_TOL
        and blindness["worst_mi_closed_form_residual"] < ANALYTIC_TOL
        and blindness["worst_I_B_swap"] < FLATNESS_TOL
    )
    leg7 = (
        battery["t400_stipulated_flag"]["flag_state_diff"] == 0.0
        and not battery["t400_stipulated_flag"]["flag_moved_capability"]
        and battery["t402_t406_matched_fields"]["declared_fields_equal"]
        and battery["t402_t406_matched_fields"]["verdict_swaps_with_input"]
    )
    leg8 = (
        q1d["declared_record_invariance"] < FLATNESS_TOL
        and q1d["worst_no_signal_out_of_R"] < FLATNESS_TOL
        and q1d["worst_teeth_closed_form_residual"] < ANALYTIC_TOL
        and q1d["beta0_visibility_jump"]["achieved_at_R"] < FLATNESS_TOL
        and abs(
            q1d["beta0_visibility_jump"]["achieved_at_Rplus"]
            - VIS_A_ANALYTIC
        ) < ANALYTIC_TOL
    )
    discipline = (
        construction["worst_cross_module_A_Rplus_vs_T410"] < FLATNESS_TOL
        and construction["worst_cross_module_A_R_vs_T410"] < FLATNESS_TOL
        and construction["worst_Rplus_to_R_marginal_consistency"]
        < FLATNESS_TOL
        and construction["worst_p_m0_deviation"] < FLATNESS_TOL
    )

    # Predeclared failure legs (reportable verdicts, not patches).
    failure_legs = {
        "equality_fails": {
            "fired": not (leg1 and leg2),
            "halting": True,
        },
        "separation_fails_A": {
            "fired": not separation["A_all_restorable_at_Rplus"],
        },
        "separation_not_certified_B": {
            "fired_primary_swap": not b_swap_certified,
            "fired_contrast_broadcast": not separation[
                "B_broadcast_all_final_at_Rplus"
            ],
            "fired": (not b_swap_certified) or (
                not separation["B_broadcast_all_final_at_Rplus"]
            ),
            "note": (
                "primary (SWAP) firing withdraws the discriminator "
                "claim; contrast (broadcast) firing is reported as "
                "undetermined_by_bound for that row only"
            ),
        },
        "positive_control_fails": {
            "fired": not positive["all_B_restorable_at_Rpp"],
            "halting": True,
        },
        "marginal_blindness_fails": {
            "fired": blindness["worst_proper_subset_marginal_diff_beta0"]
            >= FLATNESS_TOL,
        },
        "separator_factors_through_declared_field": {
            "fired": (
                not battery["t402_t406_matched_fields"][
                    "declared_fields_equal"
                ]
            ) or battery["t400_stipulated_flag"]["flag_moved_capability"],
        },
        "boundary_physicality_reduces_to_declaration": {
            # fires if any separation/forcing FINAL verdict is not
            # carried by an all-channel certificate on the physically
            # retained state (i.e. would need a declared menu
            # restriction or a protocol-failure-only argument).
            "fired": not (leg3 and b_swap_certified),
            "conditionality_conceded": (
                "independently of firing: departure-by-trace is the "
                "reservoir idealization, adopted, not derived -- the "
                "boundary is physical GIVEN the model class; this leg "
                "polices the stronger, in-model failure mode"
            ),
        },
    }

    legs = {
        "leg1_equality_observational": leg1,
        "leg2_equality_interventional": leg2,
        "leg3_forcing_at_R": leg3,
        "leg4_separation_at_Rplus": leg4,
        "leg5_positive_control_priced": leg5,
        "leg6_beta0_marginal_blindness": leg6,
        "leg7_absorber_battery": leg7,
        "leg8_guardrails": leg8,
        "discipline_construction_anchors": discipline,
    }
    halting_fired = any(
        v.get("halting") and v["fired"] for v in failure_legs.values()
    )
    reportable_fired = sorted(
        k for k, v in failure_legs.items() if v["fired"]
    )
    holds = all(legs.values()) and not halting_fired and not reportable_fired

    if holds:
        verdict_language = (
            "the departed-record capability discriminator holds in this "
            "finite family: two capability states on T410's thermal "
            "collision substrate are exactly equal under ALL R-supported "
            "statistics -- observational and under every R-supported "
            "intervention, the ALL quantifier carried by the "
            "environment-side channel lemma and asserted on the "
            "predeclared operational family -- while one fixed "
            "boundary-crossing menu separates them: A is "
            "restorable-at-R+ and B is final-relative-to-R+, the final "
            "verdict carried by the exact phi-independence certificate "
            "against all channels with unlimited work, pure or Gibbs. "
            "Crossing is forced (the task is certified impossible "
            "inside R for both states); the completing datum -- "
            "dispersal depth -- departed with the traced-out tier-2 "
            "carriers and has exactly zero retained trace (B's R+ state "
            "is an exact product), so joint-record completion returns "
            "nothing, and at beta = 0 no proper subset of the reach "
            "holds the datum at all; enlargement restores capability "
            "and is priced in the ledger (the positive control). This "
            "realizes the open problem's success criterion at the "
            "declared R, in this finite fixture, relative to the "
            "declared reaches and menu -- finite-witness. The boundary "
            "is physical GIVEN the repeated-interaction reservoir "
            "idealization, which is adopted, not derived (T407's "
            "standing objection is NOT claimed discharged "
            "unconditionally); the transport rung -- work literally "
            "buying reach, an unconditional physical boundary -- stays "
            "named-unbuilt, as do the T404-interface residues' "
            "verifications. Whether this fixture discharges the open "
            "problem is a review decision; no claim promotion; no "
            "CLAIM-LEDGER entry; ledger actions pause for Joe per "
            "AGENTS.md."
        )
    else:
        verdict_language = (
            "the departed-record capability discriminator FAILS or a "
            "predeclared failure leg fired in this finite family: "
            f"failed legs {sorted(k for k, v in legs.items() if not v)}, "
            f"fired failure legs {reportable_fired}. Report the failing "
            "leg exactly as the finding: equality_fails or "
            "positive_control_fails halt with a defect report and NO "
            "discriminator claim; a fired "
            "boundary_physicality_reduces_to_declaration leg is "
            "reported as 'separation exists but boundary physicality "
            "reduces to declaration -- absorbed'. Do not weaken "
            "assertions to pass. No claim promotion; ledger actions "
            "pause for Joe. The transport rung stays named-unbuilt."
        )

    return {
        "artifact": "T411-departed-record-capability-discriminator-v0.1",
        "labeling_convention": (
            "retained density matrix ordered (S, REC, E1_1..E1_m and, "
            "in R++ runs, E2_1..E2_m); M measured, M = 0 selected, "
            "removed (pure, factorized); carriers DEPART (partial "
            "trace) per the run's declared reach: R departs both "
            "tiers, R+ departs tier-2, R++ retains both"
        ),
        "open_problem_criterion": OPEN_PROBLEM_CRITERION,
        "theta_meter": THETA_METER,
        "v_star": V_STAR,
        "vis_A_analytic": VIS_A_ANALYTIC,
        "theta_broadcast": THETA_BCAST,
        "m_sweep": list(M_SWEEP),
        "beta_sweep": [str(b) for b in BETA_SWEEP],
        "cascades": list(CASCADES),
        "menu_declaration": MENU_DECLARATION,
        "construction": construction,
        "equality_observational": eq_obs,
        "equality_interventional": eq_int,
        "forcing": forcing,
        "separation": separation,
        "positive_control": positive,
        "marginal_blindness": blindness,
        "battery": battery,
        "q1d": q1d,
        "legs": legs,
        "failure_legs": failure_legs,
        "verdict_tags": list(VERDICT_TAGS),
        "departed_record_discriminator_holds": holds,
        "verdict_language": verdict_language,
    }


def cached_analysis() -> dict:
    if "res" not in _ANALYSIS_CACHE:
        _ANALYSIS_CACHE["res"] = run_analysis()
    return _ANALYSIS_CACHE["res"]


if __name__ == "__main__":
    import json
    import time

    t0 = time.time()
    res = run_analysis()
    elapsed = time.time() - t0
    print(json.dumps(_json_safe(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T411 Departed-Record Capability Discriminator")
    print("=" * 70)
    print(f"model wall time: {elapsed:.1f} s (predeclared budget < 300 s)")
    eq = res["equality_observational"]
    print(f"Leg 1 -- observational equality: worst rho_R diff "
          f"{eq['worst_rho_R_entrywise_diff']:.2e} "
          f"({eq['comparisons']} comparisons)")
    ei = res["equality_interventional"]
    print(f"Leg 2 -- interventional equality (lemma-carried): worst "
          f"{ei['worst_overall']:.2e} over {ei['pairs_checked']} pairs")
    fo = res["forcing"]
    print(f"Leg 3 -- forcing at R: all final = "
          f"{fo['all_final_relative_to_R']}; worst cert "
          f"{fo['worst_phi_cert_at_R']:.2e}; worst bound "
          f"{fo['worst_bound_at_R']:.2e}")
    se = res["separation"]
    print(f"Leg 4 -- separation at R+: A restorable = "
          f"{se['A_all_restorable_at_Rplus']} (worst vs vis_A "
          f"{se['worst_A_restore_vs_visA']:.2e}); B(SWAP) final = "
          f"{se['B_swap_all_final_at_Rplus']} (cert "
          f"{se['worst_B_swap_phi_cert']:.2e}, product residual "
          f"{se['worst_B_swap_product_residual']:.2e}); B(broadcast) "
          f"final = {se['B_broadcast_all_final_at_Rplus']}")
    pc = res["positive_control"]
    print(f"Leg 5 -- positive control: B restorable at R++ = "
          f"{pc['all_B_restorable_at_Rpp']}; Sigma(beta=0, m=1) = "
          f"{pc['sigma_beta0_m1_nats']:.6f} nats (predeclared "
          f"{pc['sigma_beta0_m1_predeclared']:.6f})")
    mb = res["marginal_blindness"]
    print(f"Leg 6 -- beta=0 blindness: worst proper-subset diff "
          f"{mb['worst_proper_subset_marginal_diff_beta0']:.2e} over "
          f"{mb['proper_subsets_checked_beta0']} subsets; TD(beta=0) = "
          f"{mb['td_full_joint_beta0_by_m']['1']:.6f} (predeclared "
          f"{mb['td_beta0_predeclared']:.6f})")
    print("-" * 70)
    print(f"LEGS: {res['legs']}")
    print(f"FAILURE LEGS FIRED: "
          f"{[k for k, v in res['failure_legs'].items() if v['fired']]}")
    print(f"DEPARTED-RECORD DISCRIMINATOR HOLDS: "
          f"{res['departed_record_discriminator_holds']}")
    print(res["verdict_language"])
# end of module
