"""T393: Causal Forcing of the Access Asymmetry.

Follow-up to T392 (``models/fixed_sbs_key_reversal_divergence.py``), answering
its strongest surviving hostile-review objection: in T392 the extra-environment
ancilla A0 had a STIPULATED access boundary -- (i) outside the declared
fragment family, (ii) outside the coherent undo set, (iii) readable by the
auxiliary channel -- and nothing forced that triple. T392 is therefore a
Tier-3 (engineered) existence result.

T393 tests whether the same asymmetry is FORCED, not engineered, when the
record-carrying degree of freedom is an emitted mode that propagates out of
the apparatus's causal control region on a discrete lightcone (nearest-
neighbor SWAP chain, one site per step -- the repo's own discrete-propagation
device, cf. T377/T379 relativistic fixtures and the T153 causal-diamond
framing). Conditions (i)-(iii) then become consequences of light-cone
geometry:

    (i)   the declared fragment family is principled: records inside the
          control region;
    (ii)  the undo class is principled: ALL channels supported on the control
          region at final time (not a protocol restriction!);
    (iii) readability is principled: a downstream detector intersects the
          escaped mode's forward cone.

Nothing here is sampled for the certificate. Every probability is an exact
statevector quantity; the Haar spot-check is declared illustrative
belt-and-suspenders and the phi-independence certificate, not the sampling,
carries the result.

RECORD-LABELING CONVENTION (T392 review lesson): every outcome tuple stored or
printed by this module is in INDEX-SORTED qubit order. The ordinary record is
the joint Z distribution over {S, M} with S = qubit 0 < M = qubit 1, so the
tuples read ``(S, M)``, e.g. ``(1, 0)`` is ``P(S=1, M=0)``.

FORCING HIERARCHY (typed):
    Tier 1 (causal)        -- escape from the future control cone. THIS ARTIFACT.
    Tier 2 (thermodynamic) -- bath dispersion; undo cost scaling with bath
                              contact. NOT built here; named as the open
                              Direction-C-facing card in the spec.
    Tier 3 (engineered)    -- stipulated access triple. T392.

T393 upgrades the T392 existence result from Tier 3 to Tier 1 CONDITIONAL on
emission occurring. The residual choice is "a record-carrying mode was
emitted", which is standard physics (spontaneous emission during measurement,
photon loss); the B' control shows emission alone is innocuous.

WHAT THIS DOES NOT EARN: no Q1C reinstatement, no platform, no T166 packet,
no T183 stack clearance. Q1C stays dormant; packet/status decisions pause for
Joe per AGENTS.md.
"""

from __future__ import annotations

import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T392 machinery, reused by import (exact statevector primitives, the
# T162-importable SBS-key vocabulary, and the decision-theoretic certificate
# machinery). The primitives all take an explicit qubit-count argument.
from models.fixed_sbs_key_reversal_divergence import (
    LOSS_TABLES,
    THETA,
    V_STAR,
    SBSKey,
    _bayes_risk,
    _conditional_mutual_information,
    _HADAMARD,
    cnot,
    controlled_ry,
    d1_finalized_from_key,
    project_qubit,
    reduced_density_matrix,
    single_qubit_gate,
    verdict_map as _t392_verdict_map,  # imported for provenance; not used
    x_visibility_of_S,
    z_distribution,
    zero_state,
)

# The repo's own SBS closure-key ingredients (T162 / N10 absorber).
from models.q1a_sbs_factorization_obstruction import (
    POINTER_OBSERVABLE,
    _class_count_for,
)

# --------------------------------------------------------------------------- #
# Register layout, causal geometry, and predeclared constants
# --------------------------------------------------------------------------- #

# Index-sorted register order (most-significant first in the statevector).
S, M, F1, F2, F3, F4, C0, C1, C2 = range(9)
N_QUBITS = 9
FRAGMENT_QUBITS = (F1, F2, F3, F4)
FRAGMENT_LABELS = ("F1", "F2", "F3", "F4")
CHAIN_QUBITS = (C0, C1, C2)
CHAIN_LENGTH = 3

# Causal control region at final time: everything the apparatus can still act
# on. Chain sites 0..REGION_RADIUS are inside; the discrete lightcone (one
# site per step) carries the emitted mode past the boundary at ESCAPE_STEP.
# Region membership is TIME-INDEXED by this causal structure, not chosen per
# preparation: the same region and the same propagation circuit apply to every
# preparation.
REGION_RADIUS = 1
CONTROL_REGION = (S, M, F1, F2, F3, F4, C0, C1)
REGION_ACTIVE = (S, F1, F2, F3, F4, C0, C1)  # region minus the measured meter
ESCAPE_STEP = 2
N_STEPS = 2

# v0.1.1 hardening 1 (boundary-location sweep, post-hostile-review): two
# alternative control-region radii, each fixed once for every preparation.
# r=0 shrinks the region (chain site 0 only); r=2 enlarges it to the whole
# chain. The forcing verdict must track the mode's causal position relative
# to WHICHEVER boundary is declared, in both directions.
REGION_ACTIVE_R0 = (S, F1, F2, F3, F4, C0)
REGION_ACTIVE_R2 = (S, F1, F2, F3, F4, C0, C1, C2)

# v0.1.1 hardening 2 (partial-amplitude robustness, staged v0.2 content):
# emission via controlled-Ry(alpha) instead of CNOT; alpha = pi is the exact
# CNOT idealization (the chain target starts in |0>). Thresholded forcing at
# the predeclared v* = 0.9 is certified across this sweep.
PARTIAL_AMPLITUDE_ALPHAS = tuple(f * math.pi for f in (0.75, 0.9, 0.98, 1.0))

# Certificate phi sweep: >= 5 values including incommensurate ones (1.0 and
# sqrt(2) radians are not rational multiples of pi).
PHI_CERT = (0.0, 1.0, math.sqrt(2.0), math.pi / 3.0, 2.0 * math.pi / 3.0, math.pi / 7.0)

# Uniform grid for the phase-locked visibility (the recovery figure of merit).
# A uniform grid nulls any phi-independent (manufactured) coherence exactly:
# sum_k exp(i phi_k) = 0.
PHI_LOCK_GRID = tuple(2.0 * math.pi * k / 8.0 for k in range(8))

# Haar spot-check parameters (ILLUSTRATIVE ONLY; the certificate is the proof).
HAAR_SAMPLES = 50
HAAR_SEED = 20260701
HAAR_VISIBILITY_CEILING = 0.05

INFINITE_COST = math.inf

VERDICT_RECOVERABLE = "recoverable-in-control-region"
VERDICT_FINAL = "final-relative-to-control-region"

# The same three-loss T155 family as T392, relabeled onto the T393 verdict
# vocabulary (T392's tables are keyed by its own verdict strings; reusing them
# unmapped would make every Bayes risk vacuously zero).
_VERDICT_RELABEL = {
    "recoverable-at-access-K": VERDICT_RECOVERABLE,
    "final-relative-to-K": VERDICT_FINAL,
}
T393_LOSS_TABLES = {
    name: {
        _VERDICT_RELABEL[true_v]: {
            _VERDICT_RELABEL[pred_v]: cost for pred_v, cost in row.items()
        }
        for true_v, row in table.items()
    }
    for name, table in LOSS_TABLES.items()
}

_PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)


def _swap(a: int, b: int, n: int = N_QUBITS) -> np.ndarray:
    """Permutation matrix swapping qubits a and b (nearest-neighbor lightcone step)."""
    dim = 2 ** n
    mat = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = [(i >> (n - 1 - k)) & 1 for k in range(n)]
        bits[a], bits[b] = bits[b], bits[a]
        j = 0
        for k in range(n):
            j = (j << 1) | bits[k]
        mat[j, i] = 1.0
    return mat


# Precomputed gates (all exact permutation / rotation matrices on 9 qubits).
_H_S = single_qubit_gate(_HADAMARD, S, N_QUBITS)
_CRY_SM = controlled_ry(THETA, S, M, N_QUBITS)
_CNOT_S_F = {frag: cnot(S, frag, N_QUBITS) for frag in FRAGMENT_QUBITS}
_CNOT_F4_C0 = cnot(F4, C0, N_QUBITS)
_X_C0 = single_qubit_gate(_PAULI_X, C0, N_QUBITS)
_SWAP_01 = _swap(C0, C1)
_SWAP_12 = _swap(C1, C2)
_PROPAGATION = (_SWAP_01, _SWAP_12)  # step 1, step 2 of the discrete lightcone


def mode_site_at_step(step: int) -> int:
    """Discrete lightcone: content emitted onto site 0 sits on site ``step``."""
    return min(step, CHAIN_LENGTH - 1)


def lightcone_table() -> list:
    """Time-indexed region membership of the emitted mode's carrier site."""
    rows = []
    for step in range(N_STEPS + 1):
        site = mode_site_at_step(step)
        rows.append(
            {
                "step": step,
                "mode_site": site,
                "in_control_region": site <= REGION_RADIUS,
            }
        )
    return rows


# --------------------------------------------------------------------------- #
# Circuit construction
# --------------------------------------------------------------------------- #

_STATE_CACHE: dict = {}
_EMISSION_GATE_CACHE: dict = {}


def _emission_gate(alpha: float) -> np.ndarray:
    """Controlled-Ry(alpha) from F4 onto chain site 0 (partial emission)."""
    if alpha not in _EMISSION_GATE_CACHE:
        _EMISSION_GATE_CACHE[alpha] = controlled_ry(alpha, F4, C0, N_QUBITS)
    return _EMISSION_GATE_CACHE[alpha]


def prepare(
    kind: str, s_phase: float = 0.0, steps: int = N_STEPS, alpha: float | None = None
) -> np.ndarray:
    """Exact statevector for a named preparation after ``steps`` lightcone steps.

    ``A``       no record escapes: the outgoing mode carries vacuum. The chain
                runs the SAME SWAP circuit (trivially, on |000>).
    ``B``       record escapes: CNOT (F4 -> C0) writes a Z-copy of the record
                onto chain site 0 BEFORE propagation; the copy then propagates
                out of the control region at one site per step.
    ``Bprime``  emission null control: X on chain site 0 (an excitation
                UNCORRELATED with the record; no CNOT from F4), then the same
                propagation. Emission happens, no record escapes.

    ``s_phase`` parameterizes the initial S state as
    ``(|0> + e^{i s_phase}|1>)/sqrt(2)`` for the forcing certificate.
    All preparations share the measurement core and the propagation circuit;
    they differ ONLY in what (if anything) is written to chain site 0.

    ``alpha`` (v0.1.1 hardening 2, preparation B only): when not ``None``,
    the emission is controlled-Ry(alpha) (F4 -> C0) instead of CNOT, writing
    a PARTIAL-amplitude copy (emission probability sin^2(alpha/2)). Since the
    chain target starts in |0>, ``alpha = pi`` reproduces the CNOT statevector
    exactly: the exact-zero forcing form is the alpha = pi idealization.
    """
    key = (kind, float(s_phase), int(steps), None if alpha is None else float(alpha))
    if key in _STATE_CACHE:
        return _STATE_CACHE[key]

    psi = _H_S @ zero_state(N_QUBITS)
    if s_phase != 0.0:
        phase_gate = np.array(
            [[1.0, 0.0], [0.0, np.exp(1j * s_phase)]], dtype=complex
        )
        psi = single_qubit_gate(phase_gate, S, N_QUBITS) @ psi
    psi = _CRY_SM @ psi
    for frag in FRAGMENT_QUBITS:
        psi = _CNOT_S_F[frag] @ psi

    # Emission event at step 0 (inside the control region, on chain site 0).
    if kind == "A":
        pass  # vacuum: nothing written to the chain
    elif kind == "B":
        psi = (_CNOT_F4_C0 if alpha is None else _emission_gate(float(alpha))) @ psi
    elif kind == "Bprime":
        psi = _X_C0 @ psi
    else:
        raise ValueError(f"unknown preparation {kind!r}")

    # Discrete lightcone propagation: identical circuit for every preparation.
    for t in range(steps):
        psi = _PROPAGATION[t] @ psi

    _STATE_CACHE[key] = psi
    return psi


# --------------------------------------------------------------------------- #
# (1) Full ordinary event-level record
# --------------------------------------------------------------------------- #

def ordinary_record_distribution(psi: np.ndarray) -> dict:
    """Joint Z distribution over {S, M}. Tuples are INDEX-SORTED: ``(S, M)``.

    S = qubit 0 < M = qubit 1, so ``(1, 0)`` reads ``P(S=1, M=0)``. Stated
    explicitly per the T392 review lesson.
    """
    return z_distribution(psi, [M, S], N_QUBITS)


def record_max_diff(psi_a: np.ndarray, psi_b: np.ndarray) -> float:
    da = ordinary_record_distribution(psi_a)
    db = ordinary_record_distribution(psi_b)
    keys = set(da) | set(db)
    return max(abs(da.get(k, 0.0) - db.get(k, 0.0)) for k in keys)


# --------------------------------------------------------------------------- #
# (2) SBS closure key AND full SBS signature over F1..F4
# --------------------------------------------------------------------------- #

def _conditional_fragment_trace_distance(psi: np.ndarray, frag: int) -> float:
    """Trace distance between rho_frag|S=0 and rho_frag|S=1 (T392 quantity, n=9)."""
    rho = reduced_density_matrix(psi, [S, frag], N_QUBITS)  # order S (MSB), frag
    block0 = rho[0:2, 0:2]
    block1 = rho[2:4, 2:4]
    p0 = float(np.real(np.trace(block0)))
    p1 = float(np.real(np.trace(block1)))
    cond0 = block0 / p0 if p0 > 1e-12 else block0
    cond1 = block1 / p1 if p1 > 1e-12 else block1
    eig = np.linalg.eigvalsh(cond0 - cond1)
    return float(0.5 * np.sum(np.abs(eig)))


def sbs_closure_key(psi: np.ndarray, *, distinguishability_tol: float = 1e-9) -> SBSKey:
    """T162-style SBS closure key over the declared fragments F1..F4 (n=9)."""
    distinguishabilities = [
        _conditional_fragment_trace_distance(psi, frag) for frag in FRAGMENT_QUBITS
    ]
    all_distinguishable = all(
        d >= 1.0 - distinguishability_tol for d in distinguishabilities
    )
    if all_distinguishable:
        objectivity_status = "sbs_objective"
        pointer_value = POINTER_OBSERVABLE
    else:
        objectivity_status = "sbs_failed_distinguishability"
        pointer_value = "none"
    partition_visible = objectivity_status == "sbs_objective"
    accessible = frozenset(FRAGMENT_LABELS)
    independent_partition = tuple((label,) for label in FRAGMENT_LABELS)
    support_count = (
        _class_count_for(accessible, independent_partition) if partition_visible else 0
    )
    return SBSKey(
        pointer_observable=POINTER_OBSERVABLE,
        objectivity_status=objectivity_status,
        pointer_value=pointer_value,
        partition_visible=partition_visible,
        support_count=support_count,
    )


def full_sbs_signature(psi: np.ndarray) -> dict:
    """Closure key PLUS the per-fragment distinguishabilities PLUS the full
    event-level Z distribution over the declared register (S, M, F1..F4).

    Tuples in the declared distribution are index-sorted:
    ``(S, M, F1, F2, F3, F4)``.
    """
    return {
        "closure_key": sbs_closure_key(psi).as_tuple(),
        "fragment_distinguishabilities": tuple(
            _conditional_fragment_trace_distance(psi, frag)
            for frag in FRAGMENT_QUBITS
        ),
        "declared_z_distribution": z_distribution(
            psi, [S, M, F1, F2, F3, F4], N_QUBITS
        ),
    }


def sbs_signature_max_diff(psi_a: np.ndarray, psi_b: np.ndarray) -> float:
    """Max absolute difference across every numeric entry of the signature.

    Returns ``inf`` if the discrete parts (closure keys) differ.
    """
    sig_a = full_sbs_signature(psi_a)
    sig_b = full_sbs_signature(psi_b)
    if sig_a["closure_key"] != sig_b["closure_key"]:
        return math.inf
    diff = max(
        abs(x - y)
        for x, y in zip(
            sig_a["fragment_distinguishabilities"],
            sig_b["fragment_distinguishabilities"],
        )
    )
    da = sig_a["declared_z_distribution"]
    db = sig_b["declared_z_distribution"]
    for k in set(da) | set(db):
        diff = max(diff, abs(da.get(k, 0.0) - db.get(k, 0.0)))
    return diff


# --------------------------------------------------------------------------- #
# (3) The forcing theorem: undo class = ALL channels on the control region
# --------------------------------------------------------------------------- #

def region_conditional_state(
    kind: str, s_phase: float, m_outcome: int = 0, steps: int = N_STEPS
) -> np.ndarray:
    """rho on the control region (minus the measured meter), given M = m.

    THIS is the object every admissible undo channel acts on: any CPTP map
    supported on the control region at final time -- unitary or not, with or
    without in-region ancillas -- sees exactly this state and nothing else.
    If it carries no dependence on the prepared phase phi, no admissible
    channel output can depend on phi, so no channel can recover the phase.
    """
    psi = prepare(kind, s_phase=s_phase, steps=steps)
    prob, conditioned = project_qubit(psi, M, m_outcome, N_QUBITS)
    if prob <= 1e-15:
        raise ValueError(f"meter outcome {m_outcome} has zero probability")
    return reduced_density_matrix(conditioned, list(REGION_ACTIVE), N_QUBITS)


def enlarged_conditional_state(
    kind: str, s_phase: float, m_outcome: int = 0, steps: int = N_STEPS
) -> np.ndarray:
    """Counterfactually unrestricted region: control region PLUS the escaped site."""
    psi = prepare(kind, s_phase=s_phase, steps=steps)
    prob, conditioned = project_qubit(psi, M, m_outcome, N_QUBITS)
    if prob <= 1e-15:
        raise ValueError(f"meter outcome {m_outcome} has zero probability")
    return reduced_density_matrix(
        conditioned, list(REGION_ACTIVE) + [C2], N_QUBITS
    )


def max_pairwise_phi_diff(
    state_fn, kind: str, phis=PHI_CERT, m_outcome: int = 0, steps: int = N_STEPS
) -> float:
    """Max entrywise difference of conditional states across the phi sweep."""
    rhos = [state_fn(kind, phi, m_outcome, steps) for phi in phis]
    diff = 0.0
    for i in range(len(rhos)):
        for j in range(i + 1, len(rhos)):
            diff = max(diff, float(np.max(np.abs(rhos[i] - rhos[j]))))
    return diff


def apply_on_qubits(vec: np.ndarray, U: np.ndarray, targets, n: int = N_QUBITS) -> np.ndarray:
    """Apply a unitary defined on ``targets`` (in listed order) to a statevector."""
    targets = list(targets)
    others = [q for q in range(n) if q not in targets]
    perm = targets + others
    tensor = vec.reshape([2] * n).transpose(perm)
    mat = tensor.reshape(2 ** len(targets), -1)
    mat = U @ mat
    tensor = mat.reshape([2] * n)
    inv = np.argsort(perm)
    return tensor.transpose(inv).reshape(2 ** n)


def phi_locked_visibility(
    kind: str,
    undo_fn,
    m_outcome: int = 0,
    steps: int = N_STEPS,
    grid=PHI_LOCK_GRID,
    alpha: float | None = None,
) -> float:
    """Phase-locked conditional X-visibility: |mean_phi e^{i phi} 2 rho_S[0,1]|.

    The recovery figure of merit. For a genuine undo, the restored S coherence
    is ``(vis/2) e^{-i phi}`` so the locked value equals the raw visibility.
    For MANUFACTURED coherence (phi-independent, cf. the T392 disclosure that
    raw visibility alone is gameable), the uniform grid nulls it exactly.
    ``undo_fn`` maps the M-conditioned statevector to either a statevector
    (unitary protocols) or a density-matrix-summable list of Kraus-applied
    vectors.
    """
    total = 0.0 + 0.0j
    for phi in grid:
        psi = prepare(kind, s_phase=phi, steps=steps, alpha=alpha)
        prob, conditioned = project_qubit(psi, M, m_outcome, N_QUBITS)
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


def raw_visibility_after(
    kind: str, undo_fn, m_outcome: int = 0, steps: int = N_STEPS, s_phase: float = 0.0
) -> float:
    """Raw (phase-blind) X-visibility after an undo, for disclosure columns."""
    psi = prepare(kind, s_phase=s_phase, steps=steps)
    prob, conditioned = project_qubit(psi, M, m_outcome, N_QUBITS)
    if prob <= 1e-15:
        return 0.0
    out = undo_fn(conditioned)
    if isinstance(out, list):
        rho_s = sum(reduced_density_matrix(branch, [S], N_QUBITS) for branch in out)
        return float(2.0 * abs(rho_s[0, 1]))
    return x_visibility_of_S(out, N_QUBITS)


def fragment_undo(subset):
    """Inverse of the S->Fi couplings for an accessible fragment subset."""

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = vec
        for frag in subset:
            out = _CNOT_S_F[frag] @ out
        return out

    return _undo


def in_region_undo_at_step(step: int):
    """Best in-region undo protocol available at time ``step`` (prep B).

    Every operation used is supported on the control region only:
    C0, C1 are in-region chain sites; F4, S, F1..F3 are in-region. At
    step >= ESCAPE_STEP no in-region operation can reach the escaped site,
    so the protocol degrades to the fragment undo alone (and the certificate
    proves NOTHING in-region can do better).
    """

    def _undo(vec: np.ndarray) -> np.ndarray:
        out = vec
        if step == 1:
            out = _SWAP_01 @ out  # pull the mode back from C1 to C0 (in-region)
        if step <= 1:
            out = _CNOT_F4_C0 @ out  # un-write the emitted copy (in-region)
        for frag in FRAGMENT_QUBITS:
            out = _CNOT_S_F[frag] @ out
        return out

    return _undo


def boundary_enlarged_undo(vec: np.ndarray) -> np.ndarray:
    """Counterfactual undo with the ESCAPED site included (NOT in-region).

    Inverts the full emission + propagation circuit, then the fragment
    couplings. Uses C2, which lies outside the control region: this is the
    region-boundary sanity check, not an admissible protocol.
    """
    out = _SWAP_12 @ vec
    out = _SWAP_01 @ out
    out = _CNOT_F4_C0 @ out
    for frag in FRAGMENT_QUBITS:
        out = _CNOT_S_F[frag] @ out
    return out


def haar_unitary(dim: int, rng) -> np.ndarray:
    z = (rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim)))
    z /= math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diagonal(r)
    return q * (d / np.abs(d))


def haar_spot_check(kind: str = "B", samples: int = HAAR_SAMPLES, seed: int = HAAR_SEED) -> dict:
    """ILLUSTRATIVE belt-and-suspenders: Haar-random unitaries on the in-region
    qubits, none of which may restore phase-locked visibility above the
    ceiling. The phi-independence certificate, not this sampling, carries the
    forcing result.
    """
    rng = np.random.default_rng(seed)
    dim = 2 ** len(REGION_ACTIVE)
    max_locked = 0.0
    max_raw = 0.0
    for _ in range(samples):
        U = haar_unitary(dim, rng)
        undo = lambda vec: apply_on_qubits(vec, U, REGION_ACTIVE)  # noqa: E731
        max_locked = max(max_locked, phi_locked_visibility(kind, undo))
        max_raw = max(max_raw, raw_visibility_after(kind, undo))
    return {
        "samples": samples,
        "seed": seed,
        "max_phi_locked_visibility": max_locked,
        "max_raw_visibility_disclosure": max_raw,
    }


def manufactured_coherence_control() -> dict:
    """T392's disclosed raw-visibility exploit, run in-region on prep B.

    CNOT (F1 -> S) then H on S manufactures raw visibility 1.0 while carrying
    zero information about the prepared phase. This is WHY the recovery
    figure of merit is phase-locked: the exploit's locked visibility is
    exactly nulled.
    """
    cnot_f1_s = cnot(F1, S, N_QUBITS)

    def _undo(vec: np.ndarray) -> np.ndarray:
        return _H_S @ (cnot_f1_s @ vec)

    return {
        "raw_visibility": raw_visibility_after("B", _undo),
        "phi_locked_visibility": phi_locked_visibility("B", _undo),
    }


def feedback_channel_check() -> float:
    """One representative NON-unitary in-region channel (measure C0 in Z, feed
    back X on S, then fragment undo): the undo class is all channels, not just
    unitaries, and the certificate covers this branch too.
    """
    p0 = np.zeros((2, 2), dtype=complex)
    p0[0, 0] = 1.0
    p1 = np.zeros((2, 2), dtype=complex)
    p1[1, 1] = 1.0
    k0 = single_qubit_gate(p0, C0, N_QUBITS)
    k1 = single_qubit_gate(_PAULI_X, S, N_QUBITS) @ single_qubit_gate(p1, C0, N_QUBITS)
    frag = fragment_undo(FRAGMENT_QUBITS)

    def _channel(vec: np.ndarray) -> list:
        return [frag(k0 @ vec), frag(k1 @ vec)]

    return phi_locked_visibility("B", _channel)


# --------------------------------------------------------------------------- #
# (4) Typed axis H and verdict map
# --------------------------------------------------------------------------- #

@lru_cache(maxsize=None)
def reversal_cost(kind: str, v_star: float = V_STAR, steps: int = N_STEPS) -> float:
    """Minimal accessible undo-set size k achieving PHASE-LOCKED visibility >= v*.

    The protocol family is subsets of the in-region inverse couplings
    (T392-comparable). For preparation B the infinity returned here is
    grounded in the causal certificate: the region conditional state is
    exactly phi-independent, so not only this family but EVERY channel
    supported on the control region fails.
    """
    for k in range(len(FRAGMENT_QUBITS) + 1):
        for subset in combinations(FRAGMENT_QUBITS, k):
            if phi_locked_visibility(kind, fragment_undo(subset), steps=steps) >= v_star:
                return float(k)
    return INFINITE_COST


def verdict_from_cost(h_value: float) -> str:
    if math.isinf(h_value):
        return VERDICT_FINAL
    return VERDICT_RECOVERABLE


# --------------------------------------------------------------------------- #
# (5) Auxiliary channel at the far end of the chain
# --------------------------------------------------------------------------- #

def _joint_prep_record_aux(aux_qubit: int = C2, preps=("A", "B"), prior=None) -> dict:
    """Exact joint P(prep, R=(M,S), aux) with the aux readout at the FAR END
    of the chain (outside the region, inside the escaped mode's forward cone).
    """
    if prior is None:
        prior = tuple(1.0 / len(preps) for _ in preps)
    table = defaultdict(float)
    for prep, weight in zip(preps, prior):
        psi = prepare(prep)
        order = sorted([M, S, aux_qubit])
        dist = z_distribution(psi, order, N_QUBITS)
        idx_m = order.index(M)
        idx_s = order.index(S)
        idx_a = order.index(aux_qubit)
        for bits, prob in dist.items():
            r = (bits[idx_m], bits[idx_s])
            a = bits[idx_a]
            table[(prep, r, a)] += weight * prob
    return dict(table)


def _verdicts_for(preps) -> dict:
    return {prep: verdict_from_cost(reversal_cost(prep)) for prep in preps}


def screening_certificate(preps=("A", "B"), prior=None) -> dict:
    """Decision-risk lift and CMI for the far-end detector, plus the T137 null."""
    verdict_by_prep = _verdicts_for(preps)
    joint = _joint_prep_record_aux(C2, preps, prior)

    support = defaultdict(float)
    for (prep, _r, _a), prob in joint.items():
        support[verdict_by_prep[prep]] += prob
    both_populated = len(support) == 2 and all(m > 0.0 for m in support.values())

    aux_feature = lambda r, a: a  # noqa: E731
    r_only = lambda r, a: r  # noqa: E731
    null_risk_feature = lambda r, a: (r, r[0] ^ r[1])  # noqa: E731

    lift_by_loss = {}
    all_positive = True
    for name, table in T393_LOSS_TABLES.items():
        risk_r = _bayes_risk(joint, verdict_by_prep, r_only, table)
        risk_ra = _bayes_risk(
            joint, verdict_by_prep, lambda r, a: (r, a), table
        )
        lift = risk_r - risk_ra
        lift_by_loss[name] = {"risk_R": risk_r, "risk_R_aux": risk_ra, "lift": lift}
        if lift <= 1e-12:
            all_positive = False

    null_lift_by_loss = {}
    null_all_zero = True
    for name, table in T393_LOSS_TABLES.items():
        risk_r = _bayes_risk(joint, verdict_by_prep, r_only, table)
        risk_rn = _bayes_risk(joint, verdict_by_prep, null_risk_feature, table)
        lift = risk_r - risk_rn
        null_lift_by_loss[name] = {"risk_R": risk_r, "risk_R_aux": risk_rn, "lift": lift}
        if abs(lift) > 1e-12:
            null_all_zero = False

    cmi = _conditional_mutual_information(joint, verdict_by_prep, aux_feature)
    null_cmi = _conditional_mutual_information(
        joint, verdict_by_prep, lambda r, a: r[0] ^ r[1]
    )

    return {
        "verdict_by_prep": verdict_by_prep,
        "class_support": dict(support),
        "both_classes_populated": both_populated,
        "lift_by_loss": lift_by_loss,
        "all_losses_positive_lift": all_positive,
        "cmi_bits": cmi,
        "cmi_positive": cmi > 1e-12,
        "null_lift_by_loss": null_lift_by_loss,
        "null_all_zero_lift": null_all_zero,
        "null_cmi_bits": null_cmi,
    }


def emission_confound_mixture() -> dict:
    """DISCLOSURE: the uniform three-preparation mixture {A, B, B'}.

    At the uniform prior the 0-1 and false-final-costly lifts of the far-end
    detector degenerate to exactly zero (mass coincidence at this symmetric
    prior), while the CMI stays positive and the false-recover-costly loss
    keeps positive lift. The T155 lift claim of this artifact is scoped to
    the declared A/B family, matching T392; this mixture is disclosed, not
    claimed.
    """
    preps = ("A", "B", "Bprime")
    verdict_by_prep = _verdicts_for(preps)
    joint = _joint_prep_record_aux(C2, preps)
    aux_feature = lambda r, a: a  # noqa: E731
    r_only = lambda r, a: r  # noqa: E731
    lift_by_loss = {}
    for name, table in T393_LOSS_TABLES.items():
        risk_r = _bayes_risk(joint, verdict_by_prep, r_only, table)
        risk_ra = _bayes_risk(joint, verdict_by_prep, lambda r, a: (r, a), table)
        lift_by_loss[name] = {"risk_R": risk_r, "risk_R_aux": risk_ra, "lift": risk_r - risk_ra}
    cmi = _conditional_mutual_information(joint, verdict_by_prep, aux_feature)
    return {
        "verdict_by_prep": verdict_by_prep,
        "lift_by_loss": lift_by_loss,
        "cmi_bits": cmi,
        "note": (
            "disclosed boundary: at the uniform {A,B,B'} prior the 0-1 and "
            "false-final-costly lifts are exactly zero while CMI and the "
            "false-recover-costly lift remain positive; the artifact's lift "
            "claim is scoped to the declared A/B family per T392"
        ),
    }


# --------------------------------------------------------------------------- #
# (6) B' emission null control
# --------------------------------------------------------------------------- #

def chain_excitation(kind: str) -> float:
    """Total expected excitation number on the chain (the energy signature)."""
    psi = prepare(kind)
    total = 0.0
    for site in CHAIN_QUBITS:
        rho = reduced_density_matrix(psi, [site], N_QUBITS)
        total += float(np.real(rho[1, 1]))
    return total


def bprime_control() -> dict:
    """B' carries a REAL emitted excitation, uncorrelated with the record.

    Must be bitwise identical to A on every verdict-relevant quantity, while
    the global statevector genuinely differs (the excitation escaped): this
    kills 'emission per se, or its energy signature, is doing the work'.
    """
    psi_a = prepare("A")
    psi_bp = prepare("Bprime")

    region_diff = 0.0
    for phi in PHI_CERT:
        rho_a = region_conditional_state("A", phi)
        rho_bp = region_conditional_state("Bprime", phi)
        region_diff = max(region_diff, float(np.max(np.abs(rho_a - rho_bp))))

    h_a = reversal_cost("A")
    h_bp = reversal_cost("Bprime")

    return {
        "record_max_diff": record_max_diff(psi_a, psi_bp),
        "sbs_signature_max_diff": sbs_signature_max_diff(psi_a, psi_bp),
        "region_conditional_state_max_diff": region_diff,
        "full_undo_locked_visibility_A": phi_locked_visibility(
            "A", fragment_undo(FRAGMENT_QUBITS)
        ),
        "full_undo_locked_visibility_Bprime": phi_locked_visibility(
            "Bprime", fragment_undo(FRAGMENT_QUBITS)
        ),
        "H_A": h_a,
        "H_Bprime": h_bp,
        "verdict_A": verdict_from_cost(h_a),
        "verdict_Bprime": verdict_from_cost(h_bp),
        "emission_is_real_global_statevector_diff": float(
            np.max(np.abs(psi_a - psi_bp))
        ),
        "chain_excitation": {
            "A": chain_excitation("A"),
            "B": chain_excitation("B"),
            "Bprime": chain_excitation("Bprime"),
        },
    }


# --------------------------------------------------------------------------- #
# (7) Recovery window and region-boundary sanity
# --------------------------------------------------------------------------- #

def recovery_window() -> dict:
    """Phase-locked recovery of prep B by IN-REGION undo, per lightcone step.

    While the emitted mode is still inside the control region (steps 0 and 1)
    the in-region undo recovers the T392 visibility; at the escape step it
    cannot. Same circuit, same region, only time differs: the asymmetry
    tracks the light-cone, not a declaration.
    """
    window = {}
    for step in range(N_STEPS + 1):
        window[step] = {
            "mode_site": mode_site_at_step(step),
            "in_control_region": mode_site_at_step(step) <= REGION_RADIUS,
            "locked_visibility_in_region_undo": phi_locked_visibility(
                "B", in_region_undo_at_step(step), steps=step
            ),
        }
    return window


def boundary_enlargement() -> dict:
    """Counterfactually enlarge the undo support to include the escaped site."""
    vis_a = phi_locked_visibility("A", fragment_undo(FRAGMENT_QUBITS))
    vis_b_enlarged = phi_locked_visibility("B", boundary_enlarged_undo)
    return {
        "locked_visibility_A_in_region": vis_a,
        "locked_visibility_B_with_escaped_site": vis_b_enlarged,
        "abs_diff": abs(vis_a - vis_b_enlarged),
        "enlarged_state_phi_dependence_B": max_pairwise_phi_diff(
            enlarged_conditional_state, "B"
        ),
    }


# --------------------------------------------------------------------------- #
# (8) v0.1.1 hardening 1: boundary-location sweep
# --------------------------------------------------------------------------- #

def region_conditional_state_for(active_qubits):
    """Factory: the M-conditioned reduced state on an ARBITRARY active-qubit
    set, signature-compatible with ``max_pairwise_phi_diff``. Used by the
    boundary-location sweep to re-run the forcing certificate for control
    regions other than the primary r = 1 declaration.
    """

    def _state(
        kind: str, s_phase: float, m_outcome: int = 0, steps: int = N_STEPS
    ) -> np.ndarray:
        psi = prepare(kind, s_phase=s_phase, steps=steps)
        prob, conditioned = project_qubit(psi, M, m_outcome, N_QUBITS)
        if prob <= 1e-15:
            raise ValueError(f"meter outcome {m_outcome} has zero probability")
        return reduced_density_matrix(conditioned, list(active_qubits), N_QUBITS)

    return _state


def boundary_location_sweep() -> dict:
    """Rerun the forcing certificate for a smaller (r=0) and a larger (r=2)
    control region, in both directions.

    Answer to the stipulation-regress attack ("the region is still declared"):
    for EVERY tested boundary placement the certificate tracks the mode's
    causal position relative to that boundary -- phi-independence exactly when
    the mode is past the declared boundary, genuine phi-dependence while it is
    inside. With r = 0 the mode is already outside at step 1; with r = 2 the
    whole chain is inside and the region state stays phi-dependent even at
    step 2. The residual premise is only that the apparatus has SOME bounded
    control region, not where its boundary sits.
    """
    state_r0 = region_conditional_state_for(REGION_ACTIVE_R0)
    state_r2 = region_conditional_state_for(REGION_ACTIVE_R2)
    return {
        "region_active_r0": ["S", "F1", "F2", "F3", "F4", "C0"],
        "region_active_r2": ["S", "F1", "F2", "F3", "F4", "C0", "C1", "C2"],
        "r0_step1_mode_outside_cert_diff_B": max_pairwise_phi_diff(
            state_r0, "B", steps=1
        ),
        "r0_step0_mode_inside_cert_diff_B": max_pairwise_phi_diff(
            state_r0, "B", steps=0
        ),
        "r2_step2_mode_inside_cert_diff_B": max_pairwise_phi_diff(
            state_r2, "B", steps=2
        ),
    }


# --------------------------------------------------------------------------- #
# (9) v0.1.1 hardening 2: partial-amplitude robustness (staged v0.2 content)
# --------------------------------------------------------------------------- #

def _trace_norm(hermitian: np.ndarray) -> float:
    """Trace norm of a Hermitian matrix (sum of absolute eigenvalues)."""
    return float(np.sum(np.abs(np.linalg.eigvalsh(hermitian))))


def in_region_channel_bound(
    kind: str,
    region_active=REGION_ACTIVE,
    steps: int = N_STEPS,
    alpha: float | None = None,
    grid=PHI_LOCK_GRID,
) -> float:
    """Channel-independent upper bound on the phase-locked visibility of ANY
    channel supported on ``region_active``.

    For any CPTP map Lambda on the region, the locked visibility is
    ``L = |2 Tr[Lambda(X) (|1><0|_S x I)]`` with
    ``X = mean_phi e^{i phi} rho_region|M(phi)``. By Hoelder
    (``|| |1><0| x I ||_op = 1``) and trace-norm contractivity of CPTP maps
    on Hermitian operators (applied to the Hermitian and anti-Hermitian parts
    of X separately):

        L <= 2 (||Re X||_1 + ||Im X||_1).

    This bounds every in-region channel at once -- unitary or not, with or
    without in-region ancillas -- with no channel enumeration.
    """
    dim = 2 ** len(region_active)
    X = np.zeros((dim, dim), dtype=complex)
    for phi in grid:
        psi = prepare(kind, s_phase=phi, steps=steps, alpha=alpha)
        prob, conditioned = project_qubit(psi, M, 0, N_QUBITS)
        if prob <= 1e-15:
            raise ValueError("meter outcome 0 has zero probability")
        X = X + np.exp(1j * phi) * reduced_density_matrix(
            conditioned, list(region_active), N_QUBITS
        )
    X = X / len(grid)
    hermitian_part = (X + X.conj().T) / 2.0
    anti_part = (X - X.conj().T) / 2.0j
    return 2.0 * (_trace_norm(hermitian_part) + _trace_norm(anti_part))


def partial_amplitude_robustness(alphas=PARTIAL_AMPLITUDE_ALPHAS) -> dict:
    """Thresholded forcing under partial emission amplitude.

    Emission is controlled-Ry(alpha) (F4 -> C0); emission probability
    sin^2(alpha/2). Exact facts certified per alpha:

    - the fragment-undo locked recovery in prep B_alpha equals
      cos(alpha/2) * (4 sqrt(3) / 7) to numerical precision (the surviving
      no-emission amplitude carries all the recoverable phase);
    - the channel-independent bound of ``in_region_channel_bound`` is below
      the predeclared v* = 0.9 for every alpha >= 0.75 pi, so NO in-region
      channel reaches threshold recovery: forcing at threshold v* is robust,
      and the exact-zero form is the alpha = pi idealization of that fact.
    """
    vis_a = phi_locked_visibility("A", fragment_undo(FRAGMENT_QUBITS))
    sweep = []
    for alpha in alphas:
        locked = phi_locked_visibility(
            "B", fragment_undo(FRAGMENT_QUBITS), alpha=alpha
        )
        bound = in_region_channel_bound("B", alpha=alpha)
        sweep.append(
            {
                "alpha_over_pi": alpha / math.pi,
                "emission_probability": math.sin(alpha / 2.0) ** 2,
                "fragment_undo_locked_visibility": locked,
                "analytic_cos_half_alpha_times_vis_A": math.cos(alpha / 2.0) * vis_a,
                "in_region_channel_bound": bound,
                "bound_below_v_star": bound < V_STAR,
            }
        )
    return {
        "v_star": V_STAR,
        "bound_construction": (
            "2*(||Re X||_1 + ||Im X||_1), X = mean_phi e^{i phi} "
            "rho_region|M=0(phi); Hoelder + CPTP trace-norm contractivity"
        ),
        "channel_bound_A_sanity": in_region_channel_bound("A"),
        "channel_bound_B_cnot": in_region_channel_bound("B"),
        "alpha_pi_equals_cnot_statevector_diff": float(
            np.max(np.abs(prepare("B", alpha=math.pi) - prepare("B")))
        ),
        "sweep": sweep,
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class ForcingResult:
    theta: float
    v_star: float
    lightcone: list
    record_max_diff_AB: float
    ordinary_record_A: dict
    ordinary_record_B: dict
    sbs_signature_max_diff_AB: float
    sbs_key_A: tuple
    sbs_key_B: tuple
    d1_finalized_A: bool
    d1_finalized_B: bool
    declared_coherence_max_diff_AB: float
    vis_A_locked: float
    vis_A_raw: float
    vis_B_locked: float
    vis_B_raw: float
    visibility_gap: float
    cert_phi_values: tuple
    cert_max_pairwise_diff_B: float
    cert_max_pairwise_diff_A: float
    haar: dict
    manufactured: dict
    feedback_channel_locked: float
    H_A: float
    H_B: float
    verdict_A: str
    verdict_B: str
    screening: dict
    confound_mixture: dict
    bprime: dict
    window: dict
    boundary: dict
    boundary_sweep: dict
    partial_amplitude: dict
    forcing_holds: bool
    verdict_language: str


def run_analysis() -> ForcingResult:
    psi_a = prepare("A")
    psi_b = prepare("B")

    rec_diff = record_max_diff(psi_a, psi_b)
    sig_diff = sbs_signature_max_diff(psi_a, psi_b)
    key_a = sbs_closure_key(psi_a)
    key_b = sbs_closure_key(psi_b)

    # Disclosure: the emission changes declared-register COHERENCES (invisible
    # to the Z-basis record and the pointer-basis SBS signature).
    rho_decl_a = reduced_density_matrix(psi_a, [S, M, F1, F2, F3, F4], N_QUBITS)
    rho_decl_b = reduced_density_matrix(psi_b, [S, M, F1, F2, F3, F4], N_QUBITS)
    coherence_diff = float(np.max(np.abs(rho_decl_a - rho_decl_b)))

    full_undo = fragment_undo(FRAGMENT_QUBITS)
    vis_a_locked = phi_locked_visibility("A", full_undo)
    vis_a_raw = raw_visibility_after("A", full_undo)
    vis_b_locked = phi_locked_visibility("B", full_undo)
    vis_b_raw = raw_visibility_after("B", full_undo)
    gap = vis_a_locked - vis_b_locked

    cert_b = max_pairwise_phi_diff(region_conditional_state, "B")
    cert_a = max_pairwise_phi_diff(region_conditional_state, "A")

    haar = haar_spot_check()
    manufactured = manufactured_coherence_control()
    feedback_locked = feedback_channel_check()

    h_a = reversal_cost("A")
    h_b = reversal_cost("B")

    screening = screening_certificate()
    confound = emission_confound_mixture()
    bprime = bprime_control()
    window = recovery_window()
    boundary = boundary_enlargement()
    boundary_sweep = boundary_location_sweep()
    partial_amplitude = partial_amplitude_robustness()

    forcing_holds = (
        rec_diff == 0.0
        and sig_diff == 0.0
        and cert_b < 1e-12
        and cert_a > 0.1
        and vis_a_locked >= V_STAR
        and vis_b_locked <= 1e-12
        and haar["max_phi_locked_visibility"] < HAAR_VISIBILITY_CEILING
        and math.isfinite(h_a)
        and math.isinf(h_b)
        and verdict_from_cost(h_a) != verdict_from_cost(h_b)
        and screening["both_classes_populated"]
        and screening["all_losses_positive_lift"]
        and screening["cmi_positive"]
        and screening["null_all_zero_lift"]
        and bprime["record_max_diff"] == 0.0
        and bprime["sbs_signature_max_diff"] == 0.0
        and bprime["region_conditional_state_max_diff"] == 0.0
        and bprime["verdict_A"] == bprime["verdict_Bprime"]
        and window[0]["locked_visibility_in_region_undo"] >= V_STAR
        and window[1]["locked_visibility_in_region_undo"] >= V_STAR
        and window[ESCAPE_STEP]["locked_visibility_in_region_undo"] <= 1e-12
        and boundary["abs_diff"] < 1e-12
        and boundary["enlarged_state_phi_dependence_B"] > 0.1
    )

    if forcing_holds:
        verdict_language = (
            "forcing holds at the causal tier in this finite family: when the "
            "record-carrying mode is emitted onto the discrete lightcone and "
            "propagates past the control-region boundary, the T392 access "
            "asymmetry follows from causal geometry alone -- the region "
            "conditional state is exactly phase-independent, so NO channel "
            "supported on the control region recovers the prepared phase, "
            "while the same in-region undo recovers it before escape and a "
            "counterfactual enlargement across the boundary recovers it "
            "after. The upgrade from the engineered tier to the causal tier "
            "is conditional on emission occurring; the B-prime control shows "
            "emission alone, without record correlation, splits nothing."
        )
    else:
        verdict_language = (
            "forcing fails at the causal tier in this finite family: no "
            "placement of the emission coupling satisfied the fixed-record "
            "and fixed-signature equalities with a nonzero forcing gap, or a "
            "certificate check failed. The T392 asymmetry remains engineered "
            "(Tier 3) on current evidence."
        )

    return ForcingResult(
        theta=THETA,
        v_star=V_STAR,
        lightcone=lightcone_table(),
        record_max_diff_AB=rec_diff,
        ordinary_record_A=ordinary_record_distribution(psi_a),
        ordinary_record_B=ordinary_record_distribution(psi_b),
        sbs_signature_max_diff_AB=sig_diff,
        sbs_key_A=key_a.as_tuple(),
        sbs_key_B=key_b.as_tuple(),
        d1_finalized_A=d1_finalized_from_key(key_a),
        d1_finalized_B=d1_finalized_from_key(key_b),
        declared_coherence_max_diff_AB=coherence_diff,
        vis_A_locked=vis_a_locked,
        vis_A_raw=vis_a_raw,
        vis_B_locked=vis_b_locked,
        vis_B_raw=vis_b_raw,
        visibility_gap=gap,
        cert_phi_values=PHI_CERT,
        cert_max_pairwise_diff_B=cert_b,
        cert_max_pairwise_diff_A=cert_a,
        haar=haar,
        manufactured=manufactured,
        feedback_channel_locked=feedback_locked,
        H_A=h_a,
        H_B=h_b,
        verdict_A=verdict_from_cost(h_a),
        verdict_B=verdict_from_cost(h_b),
        screening=screening,
        confound_mixture=confound,
        bprime=bprime,
        window=window,
        boundary=boundary,
        boundary_sweep=boundary_sweep,
        partial_amplitude=partial_amplitude,
        forcing_holds=forcing_holds,
        verdict_language=verdict_language,
    )


_ANALYSIS_CACHE: dict = {}


def cached_analysis() -> ForcingResult:
    """Memoized run_analysis for the test suite (pure function of the model)."""
    if "res" not in _ANALYSIS_CACHE:
        _ANALYSIS_CACHE["res"] = run_analysis()
    return _ANALYSIS_CACHE["res"]


# --------------------------------------------------------------------------- #
# Serialization
# --------------------------------------------------------------------------- #

def _hval(h: float):
    return "inf" if math.isinf(h) else h


def result_to_dict(res: ForcingResult) -> dict:
    return {
        "artifact": "T393-causal-forcing-of-access-asymmetry-v0.1",
        "labeling_convention": (
            "all outcome tuples are index-sorted; ordinary record tuples read "
            "(S, M) with S = qubit 0, M = qubit 1"
        ),
        "theta": res.theta,
        "v_star": res.v_star,
        "region": {
            "control_region_qubits": ["S", "M", "F1", "F2", "F3", "F4", "C0", "C1"],
            "chain_length": CHAIN_LENGTH,
            "region_radius_r": REGION_RADIUS,
            "escape_step": ESCAPE_STEP,
        },
        "lightcone": res.lightcone,
        "record_max_diff_AB": res.record_max_diff_AB,
        "ordinary_record_A": {
            "".join(map(str, k)): v for k, v in res.ordinary_record_A.items()
        },
        "ordinary_record_B": {
            "".join(map(str, k)): v for k, v in res.ordinary_record_B.items()
        },
        "sbs_signature_max_diff_AB": res.sbs_signature_max_diff_AB,
        "sbs_key_A": list(res.sbs_key_A),
        "sbs_key_B": list(res.sbs_key_B),
        "d1_finalized_A": res.d1_finalized_A,
        "d1_finalized_B": res.d1_finalized_B,
        "declared_coherence_max_diff_AB_disclosure": res.declared_coherence_max_diff_AB,
        "reversal": {
            "vis_A_locked": res.vis_A_locked,
            "vis_A_raw": res.vis_A_raw,
            "vis_B_locked": res.vis_B_locked,
            "vis_B_raw": res.vis_B_raw,
            "visibility_gap": res.visibility_gap,
        },
        "forcing_certificate": {
            "phi_values": list(res.cert_phi_values),
            "max_pairwise_diff_B": res.cert_max_pairwise_diff_B,
            "max_pairwise_diff_A": res.cert_max_pairwise_diff_A,
        },
        "haar_spot_check_illustrative": res.haar,
        "manufactured_coherence_control": res.manufactured,
        "feedback_channel_locked_visibility": res.feedback_channel_locked,
        "H_A": _hval(res.H_A),
        "H_B": _hval(res.H_B),
        "verdict_A": res.verdict_A,
        "verdict_B": res.verdict_B,
        "screening": {
            **res.screening,
            "cmi_bits": res.screening["cmi_bits"],
        },
        "emission_confound_mixture_disclosure": res.confound_mixture,
        "bprime_control": {
            **res.bprime,
            "H_A": _hval(res.bprime["H_A"]),
            "H_Bprime": _hval(res.bprime["H_Bprime"]),
        },
        "recovery_window": {
            str(step): vals for step, vals in res.window.items()
        },
        "boundary_enlargement": res.boundary,
        "boundary_location_sweep": res.boundary_sweep,
        "partial_amplitude_robustness": res.partial_amplitude,
        "forcing_holds": res.forcing_holds,
        "verdict_language": res.verdict_language,
    }


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(result_to_dict(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY -- T393 Causal Forcing of the Access Asymmetry")
    print("=" * 70)
    print(f"ordinary record max diff (A vs B):   {res.record_max_diff_AB}")
    print(f"full SBS signature max diff (A/B):   {res.sbs_signature_max_diff_AB}")
    print(f"  key A: {res.sbs_key_A}")
    print(f"  key B: {res.sbs_key_B}")
    print(f"locked visibility A (in-region):     {res.vis_A_locked:.6f}")
    print(f"locked visibility B (in-region):     {res.vis_B_locked:.6f}")
    print(f"visibility gap (A - B):              {res.visibility_gap:.6f}")
    print(f"certificate max diff B (phi sweep):  {res.cert_max_pairwise_diff_B:.3e}")
    print(f"certificate max diff A (phi sweep):  {res.cert_max_pairwise_diff_A:.6f}")
    print(f"Haar spot-check max locked ({res.haar['samples']} U):  "
          f"{res.haar['max_phi_locked_visibility']:.3e}")
    print(f"manufactured-coherence raw/locked:   "
          f"{res.manufactured['raw_visibility']:.6f} / "
          f"{res.manufactured['phi_locked_visibility']:.3e}")
    print(f"H(A) / H(B):                         {res.H_A} / {res.H_B}")
    print(f"verdict A / B:                       {res.verdict_A} / {res.verdict_B}")
    for name, vals in res.screening["lift_by_loss"].items():
        print(f"  lift[{name}]: {vals['lift']:.6f}")
    print(f"CMI I(V; C2 | R) bits:               {res.screening['cmi_bits']:.6f}")
    print(f"T137 null lift all zero:             {res.screening['null_all_zero_lift']}")
    print(f"B' verdict-relevant max diffs:       "
          f"record {res.bprime['record_max_diff']}, "
          f"signature {res.bprime['sbs_signature_max_diff']}, "
          f"region state {res.bprime['region_conditional_state_max_diff']}")
    print(f"B' emission real (global sv diff):   "
          f"{res.bprime['emission_is_real_global_statevector_diff']:.6f}")
    print("recovery window (in-region undo):")
    for step, vals in res.window.items():
        print(f"  step {step}: mode at site {vals['mode_site']} "
              f"(in region: {vals['in_control_region']}), "
              f"locked vis {vals['locked_visibility_in_region_undo']:.6f}")
    print(f"boundary enlargement recovers B:     "
          f"{res.boundary['locked_visibility_B_with_escaped_site']:.6f} "
          f"(|diff from A| = {res.boundary['abs_diff']:.3e})")
    print("boundary-location sweep (v0.1.1 hardening 1):")
    print(f"  r=0, step 1 (mode at C1, outside): cert diff B = "
          f"{res.boundary_sweep['r0_step1_mode_outside_cert_diff_B']:.3e}")
    print(f"  r=0, step 0 (mode at C0, inside):  cert diff B = "
          f"{res.boundary_sweep['r0_step0_mode_inside_cert_diff_B']:.6f}")
    print(f"  r=2, step 2 (mode at C2, inside):  cert diff B = "
          f"{res.boundary_sweep['r2_step2_mode_inside_cert_diff_B']:.6f}")
    print(f"partial-amplitude robustness (v0.1.1 hardening 2, "
          f"v* = {res.partial_amplitude['v_star']}):")
    for row in res.partial_amplitude["sweep"]:
        print(f"  alpha = {row['alpha_over_pi']:.2f} pi: frag-undo locked "
              f"{row['fragment_undo_locked_visibility']:.6f} "
              f"(analytic {row['analytic_cos_half_alpha_times_vis_A']:.6f}), "
              f"channel bound {row['in_region_channel_bound']:.4f} "
              f"(< v*: {row['bound_below_v_star']})")
    print("-" * 70)
    print(f"FORCING HOLDS (causal tier): {res.forcing_holds}")
    print(res.verdict_language)
# end of module
