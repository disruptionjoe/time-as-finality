"""T392: Fixed-SBS-Key Reversal Divergence Witness.

A finite, exactly-simulable statevector model that tests whether the T146 live
class ``extra_environment_candidate`` (T150: ``typed_extra_environment_candidate``)
-- an auxiliary channel tied to extra environment structure not screened off by
the full ordinary event-level record -- is *non-empty*, using reversal cost as
the independently typed TaF axis, at FIXED SBS closure keys.

The construction attacks the one boundary T162 did not close: the honest access
boundary. It builds two preparations that agree exactly on

    1. the full ordinary event-level record (joint Z distribution of the meter
       outcome and the standard final system readout), and
    2. the SBS-importable closure key over the declared fragment family
       F1..F4 (pointer observable, objectivity status, pointer value,
       partition visibility, independence-corrected support count R_delta),

using the repo's OWN closure-key definition imported from
``models.q1a_sbs_factorization_obstruction`` (T162), yet DIVERGE on reversal
cost: preparation A restores X-basis interference visibility after an undo of
the accessible fragment couplings, and preparation B does not, because a single
extra unmonitored ancilla A0 (not in the declared fragment family, not in the
accessible undo set) still holds a copy of the record.

Nothing here is sampled. Every probability is an exact statevector expectation.

WHAT THIS DOES NOT EARN (see the spec's dedicated section): this is a finite
model existence proof only. It does not reinstate Q1C, name a hardware
platform, or clear the T166 packet-intake stack. Q1C stays dormant and any
real reopening pauses for Joe per AGENTS.md.
"""

from __future__ import annotations

import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# The repo's own SBS closure-key machinery (T162 / N10 absorber).
from models.q1a_sbs_factorization_obstruction import (
    POINTER_OBSERVABLE,
    _class_count_for,
)
from models.q1a_fixed_data_witness import D1_INDEPENDENT_SUPPORT_THRESHOLD


# --------------------------------------------------------------------------- #
# Qubit register layout and predeclared constants
# --------------------------------------------------------------------------- #

# Register order (most-significant first for the statevector index).
S, M, F1, F2, F3, F4, A0 = range(7)
N_QUBITS = 7
FRAGMENT_QUBITS = (F1, F2, F3, F4)
FRAGMENT_LABELS = ("F1", "F2", "F3", "F4")

# Weak-coupling angle for the ordinary instrument (controlled-Ry). theta=pi/3
# is a genuinely weak coupling: it does not fully resolve S in the meter.
THETA = math.pi / 3.0

# PREDECLARED reversal-success visibility threshold, fixed BEFORE inspecting
# the numeric gap. The natural preparation-A analytic value is
# 2*cos(theta/2)/(1+cos(theta/2)**2) = 0.98974... at theta=pi/3, comfortably
# above 0.9, so the round predeclared 0.9 is used unchanged.
V_STAR = 0.9

# Symbol for an unattainable reversal cost within the accessible family.
INFINITE_COST = math.inf

_ISQRT2 = 1.0 / math.sqrt(2.0)
_HADAMARD = np.array([[_ISQRT2, _ISQRT2], [_ISQRT2, -_ISQRT2]], dtype=complex)
_EYE2 = np.eye(2, dtype=complex)


# --------------------------------------------------------------------------- #
# Exact statevector primitives (no sampling)
# --------------------------------------------------------------------------- #

def zero_state(n: int = N_QUBITS) -> np.ndarray:
    vec = np.zeros(2 ** n, dtype=complex)
    vec[0] = 1.0
    return vec


def single_qubit_gate(gate: np.ndarray, target: int, n: int = N_QUBITS) -> np.ndarray:
    op = np.array([[1.0]], dtype=complex)
    for q in range(n):
        op = np.kron(op, gate if q == target else _EYE2)
    return op


def cnot(control: int, target: int, n: int = N_QUBITS) -> np.ndarray:
    dim = 2 ** n
    mat = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = [(i >> (n - 1 - k)) & 1 for k in range(n)]
        if bits[control] == 1:
            bits[target] ^= 1
        j = 0
        for k in range(n):
            j = (j << 1) | bits[k]
        mat[j, i] = 1.0
    return mat


def controlled_ry(theta: float, control: int, target: int, n: int = N_QUBITS) -> np.ndarray:
    ry = np.array(
        [
            [math.cos(theta / 2.0), -math.sin(theta / 2.0)],
            [math.sin(theta / 2.0), math.cos(theta / 2.0)],
        ],
        dtype=complex,
    )
    dim = 2 ** n
    mat = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = [(i >> (n - 1 - k)) & 1 for k in range(n)]
        if bits[control] == 0:
            mat[i, i] = 1.0
            continue
        target_bit = bits[target]
        for new_bit in (0, 1):
            nb = list(bits)
            nb[target] = new_bit
            j = 0
            for k in range(n):
                j = (j << 1) | nb[k]
            mat[j, i] += ry[new_bit, target_bit]
    return mat


def reduced_density_matrix(psi: np.ndarray, keep, n: int = N_QUBITS) -> np.ndarray:
    keep = sorted(keep)
    trace = [q for q in range(n) if q not in keep]
    tensor = psi.reshape([2] * n)
    tensor = np.transpose(tensor, keep + trace)
    dk = 2 ** len(keep)
    dt = 2 ** len(trace)
    flat = tensor.reshape(dk, dt)
    return flat @ flat.conj().T


def z_distribution(psi: np.ndarray, qubits, n: int = N_QUBITS) -> dict:
    """Exact joint Z-basis distribution over ``qubits`` (sorted MSB-first)."""
    qubits = sorted(qubits)
    rho = reduced_density_matrix(psi, qubits, n)
    diag = np.real(np.diag(rho))
    dist = {}
    for idx, prob in enumerate(diag):
        if prob > 1e-15:
            bits = tuple((idx >> (len(qubits) - 1 - k)) & 1 for k in range(len(qubits)))
            dist[bits] = float(prob)
    return dist


def project_qubit(psi: np.ndarray, qubit: int, value: int, n: int = N_QUBITS):
    proj = np.zeros((2, 2), dtype=complex)
    proj[value, value] = 1.0
    projector = single_qubit_gate(proj, qubit, n)
    vec = projector @ psi
    prob = float(np.real(vec.conj() @ vec))
    if prob > 1e-15:
        vec = vec / math.sqrt(prob)
    return prob, vec


def x_visibility_of_S(psi: np.ndarray, n: int = N_QUBITS) -> float:
    """Interference visibility of S in the X basis = 2*|rho_S[0,1]|.

    Equals the coherence magnitude that a Ramsey / X-basis fringe would read;
    1.0 for a pure X eigenstate of S, 0.0 for a fully dephased S.
    """
    rho_s = reduced_density_matrix(psi, [S], n)
    return float(2.0 * abs(rho_s[0, 1]))


# --------------------------------------------------------------------------- #
# Circuit construction
# --------------------------------------------------------------------------- #

def prepare(kind: str, s_phase: float = 0.0) -> np.ndarray:
    """Return the exact statevector for a named preparation.

    ``A``  shallow branching: S->|+>, controlled-Ry meter, four fragment copies.
    ``B``  deep branching: A plus CNOT F4->A0 (extra inaccessible ancilla copy).
    ``Bprime`` null control: A0 copies nothing (product); identical to A.

    ``s_phase`` parameterizes the initial S state as
    ``(|0> + e^{i s_phase}|1>)/sqrt(2)`` for the phi-independence lemma
    (v0.1.1). The default ``0.0`` applies no additional gate, so every
    pre-existing quantity is bit-identical to v0.1.
    """
    psi = single_qubit_gate(_HADAMARD, S) @ zero_state()
    if s_phase != 0.0:
        phase_gate = np.array(
            [[1.0, 0.0], [0.0, np.exp(1j * s_phase)]], dtype=complex
        )
        psi = single_qubit_gate(phase_gate, S) @ psi
    psi = controlled_ry(THETA, S, M) @ psi
    for frag in FRAGMENT_QUBITS:
        psi = cnot(S, frag) @ psi

    if kind == "A":
        return psi
    if kind == "B":
        return cnot(F4, A0) @ psi
    if kind == "Bprime":
        # A0 copies nothing: F4 left uncoupled to A0. Identical to A on the
        # declared register and on A0 (A0 stays |0>). Kept explicit so the null
        # control is a real branch of the same builder.
        return psi.copy()
    raise ValueError(f"unknown preparation {kind!r}")


# --------------------------------------------------------------------------- #
# (1) Full ordinary event-level record
# --------------------------------------------------------------------------- #

def ordinary_record_distribution(psi: np.ndarray) -> dict:
    """Full ordinary event-level record = joint Z distribution over {S, M}.

    M is the meter outcome; S is the standard final system readout in Z.
    NOTE (v0.1.1 label fix): ``z_distribution`` sorts qubit indices, and
    S = qubit 0 < M = qubit 1, so the stored outcome tuples are ordered
    ``(S, M)``, not ``(M, S)``. E.g. the tuple ``(1, 0)`` reads
    ``P(S=1, M=0)``. This is the declared ordinary instrument's complete
    event-level transcript. A0 is extra environment and is deliberately
    excluded.
    """
    return z_distribution(psi, [M, S])


def records_equal(psi_a: np.ndarray, psi_b: np.ndarray, tol: float = 1e-12) -> bool:
    da = ordinary_record_distribution(psi_a)
    db = ordinary_record_distribution(psi_b)
    keys = set(da) | set(db)
    return all(abs(da.get(k, 0.0) - db.get(k, 0.0)) <= tol for k in keys)


# --------------------------------------------------------------------------- #
# (2) SBS-importable closure key over the DECLARED fragment family F1..F4
# --------------------------------------------------------------------------- #

def _conditional_fragment_trace_distance(psi: np.ndarray, frag: int) -> float:
    """Distinguishability of a fragment's conditional pointer states.

    Trace distance between rho_frag|S=0 and rho_frag|S=1. A perfect Z-copy
    gives 1.0. This is the per-fragment distinguishability the SBS closure key
    reads.
    """
    rho = reduced_density_matrix(psi, [S, frag])  # order S (MSB), frag (LSB)
    block0 = rho[0:2, 0:2]
    block1 = rho[2:4, 2:4]
    p0 = float(np.real(np.trace(block0)))
    p1 = float(np.real(np.trace(block1)))
    cond0 = block0 / p0 if p0 > 1e-12 else block0
    cond1 = block1 / p1 if p1 > 1e-12 else block1
    eig = np.linalg.eigvalsh(cond0 - cond1)
    return float(0.5 * np.sum(np.abs(eig)))


@dataclass(frozen=True)
class SBSKey:
    """The repo's SBS closure key, computed on this statevector.

    Mirrors ``models.q1a_sbs_factorization_obstruction.SBSVerdict.sbs_closure_key``:
    pointer observable, objectivity status, accessible pointer value, partition
    visibility, and the independence-corrected support count (R_delta) over the
    declared fragment family.
    """

    pointer_observable: str
    objectivity_status: str
    pointer_value: str
    partition_visible: bool
    support_count: int  # R_delta

    def as_tuple(self):
        return (
            self.pointer_observable,
            self.objectivity_status,
            self.pointer_value,
            self.partition_visible,
            self.support_count,
        )


def sbs_closure_key(psi: np.ndarray, *, distinguishability_tol: float = 1e-9) -> SBSKey:
    """Compute the T162-style SBS closure key over declared fragments F1..F4.

    The declared provenance partition is the maximally independent one
    (each fragment its own class), matching the T162 finalized enumeration;
    the independence-corrected support count R_delta is then computed with the
    repo's own ``_class_count_for`` over the accessible fragment set.
    """
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
    if partition_visible:
        support_count = _class_count_for(accessible, independent_partition)
    else:
        support_count = 0

    return SBSKey(
        pointer_observable=POINTER_OBSERVABLE,
        objectivity_status=objectivity_status,
        pointer_value=pointer_value,
        partition_visible=partition_visible,
        support_count=support_count,
    )


def sbs_keys_equal(psi_a: np.ndarray, psi_b: np.ndarray) -> bool:
    return sbs_closure_key(psi_a).as_tuple() == sbs_closure_key(psi_b).as_tuple()


def d1_finalized_from_key(key: SBSKey) -> bool:
    """The repo's D1 finalization test given the closure key (T162 semantics)."""
    return (
        key.objectivity_status == "sbs_objective"
        and key.partition_visible
        and key.support_count >= D1_INDEPENDENT_SUPPORT_THRESHOLD
    )


# --------------------------------------------------------------------------- #
# (3) Reversal divergence: predeclared undo protocol on accessible set
# --------------------------------------------------------------------------- #

def undo_fragments(psi: np.ndarray, accessible) -> np.ndarray:
    """Apply the inverse of the S->fragment couplings for accessible fragments.

    Each coupling was a CNOT, which is self-inverse. The S-M coupling is NOT
    reversed: M has been measured (we condition on its outcome instead), so the
    undo protocol never has access to it. A0 is never in ``accessible`` -- it
    is not a declared fragment.
    """
    vec = psi.copy()
    for frag in accessible:
        vec = cnot(S, frag) @ vec
    return vec


def visibility_after_undo(psi: np.ndarray, m_outcome: int, accessible) -> tuple:
    """Condition on the meter outcome, run the undo, read X visibility of S."""
    prob, conditioned = project_qubit(psi, M, m_outcome)
    if prob <= 1e-15:
        return prob, 0.0
    undone = undo_fragments(conditioned, accessible)
    return prob, x_visibility_of_S(undone)


@dataclass(frozen=True)
class ReversalReport:
    preparation: str
    per_outcome: dict
    best_branch_visibility: float


def declared_conditional_state(psi: np.ndarray, m_outcome: int = 0) -> np.ndarray:
    """rho_{S, F1..F4 | M = m_outcome}: the full accessible conditional state.

    Ground object of the phi-independence lemma (v0.1.1): this is everything
    any accessible protocol -- inverse-coupling or otherwise -- can act on
    once the meter outcome is fixed. If it carries no information about the
    prepared S phase, no accessible protocol can recover that phase.
    """
    prob, conditioned = project_qubit(psi, M, m_outcome)
    if prob <= 1e-15:
        raise ValueError(f"meter outcome {m_outcome} has zero probability")
    return reduced_density_matrix(conditioned, [S, F1, F2, F3, F4])


def reversal_report(psi: np.ndarray, preparation: str) -> ReversalReport:
    per = {}
    best = 0.0
    for m_outcome in (0, 1):
        prob, vis_after = visibility_after_undo(psi, m_outcome, FRAGMENT_QUBITS)
        _, vis_before = visibility_after_undo(psi, m_outcome, ())
        per[m_outcome] = {
            "prob": prob,
            "vis_before": vis_before,
            "vis_after": vis_after,
        }
        if prob > 1e-15:
            best = max(best, vis_after)
    return ReversalReport(
        preparation=preparation, per_outcome=per, best_branch_visibility=best
    )


# --------------------------------------------------------------------------- #
# (4) Typed axis H = reversal cost, and verdict map V = g(H)
# --------------------------------------------------------------------------- #

def reversal_cost(psi: np.ndarray, m_outcome: int, v_star: float = V_STAR) -> float:
    """Minimal size k of an accessible undo set achieving visibility >= v*.

    The accessible undo set is drawn ONLY from declared fragments F1..F4. A0 is
    honestly inaccessible. If no accessible subset reaches v*, cost is infinite
    (final relative to the accessible family).
    """
    prob, conditioned = project_qubit(psi, M, m_outcome)
    if prob <= 1e-15:
        return INFINITE_COST
    for k in range(len(FRAGMENT_QUBITS) + 1):
        for subset in combinations(FRAGMENT_QUBITS, k):
            undone = undo_fragments(conditioned, subset)
            if x_visibility_of_S(undone) >= v_star:
                return float(k)
    return INFINITE_COST


def dominant_meter_outcome(psi: np.ndarray) -> int:
    """The meter outcome carrying the dominant objective pointer branch."""
    probs = {m: project_qubit(psi, M, m)[0] for m in (0, 1)}
    return max(probs, key=probs.get)


def typed_axis_H(psi: np.ndarray, v_star: float = V_STAR) -> float:
    """Independently typed TaF axis: reversal cost on the dominant meter branch."""
    return reversal_cost(psi, dominant_meter_outcome(psi), v_star)


def verdict_map(h_value: float) -> str:
    """V = g(H): recoverable-at-access-K vs final-relative-to-K."""
    if math.isinf(h_value):
        return "final-relative-to-K"
    return "recoverable-at-access-K"


# --------------------------------------------------------------------------- #
# (5) Decision-theoretic screening-off failure certificate
# --------------------------------------------------------------------------- #

def _joint_prep_record_aux(aux_qubit: int, prior=(0.5, 0.5)) -> dict:
    """Exact joint P(prep, R=(M,S), aux) over prep in {A, B}."""
    table = defaultdict(float)
    for prep, weight in zip(("A", "B"), prior):
        psi = prepare(prep)
        order = sorted([M, S, aux_qubit])
        dist = z_distribution(psi, order)
        idx_m = order.index(M)
        idx_s = order.index(S)
        idx_a = order.index(aux_qubit)
        for bits, prob in dist.items():
            r = (bits[idx_m], bits[idx_s])
            a = bits[idx_a]
            table[(prep, r, a)] += weight * prob
    return dict(table)


def _verdict_by_prep() -> dict:
    return {
        "A": verdict_map(typed_axis_H(prepare("A"))),
        "B": verdict_map(typed_axis_H(prepare("B"))),
    }


LOSS_TABLES = {
    "zero_one": {
        "recoverable-at-access-K": {
            "recoverable-at-access-K": 0.0,
            "final-relative-to-K": 1.0,
        },
        "final-relative-to-K": {
            "recoverable-at-access-K": 1.0,
            "final-relative-to-K": 0.0,
        },
    },
    "false_recover_costly": {
        "recoverable-at-access-K": {
            "recoverable-at-access-K": 0.0,
            "final-relative-to-K": 1.0,
        },
        "final-relative-to-K": {
            "recoverable-at-access-K": 5.0,
            "final-relative-to-K": 0.0,
        },
    },
    "false_final_costly": {
        "recoverable-at-access-K": {
            "recoverable-at-access-K": 0.0,
            "final-relative-to-K": 4.0,
        },
        "final-relative-to-K": {
            "recoverable-at-access-K": 1.0,
            "final-relative-to-K": 0.0,
        },
    },
}


def _bayes_risk(joint: dict, verdict_by_prep: dict, feature_fn, loss_table) -> float:
    groups = defaultdict(lambda: defaultdict(float))
    for (prep, r, a), prob in joint.items():
        verdict = verdict_by_prep[prep]
        groups[feature_fn(r, a)][verdict] += prob
    classes = list(loss_table.keys())
    total = 0.0
    for _, verdict_mass in groups.items():
        best = None
        for prediction in classes:
            expected = sum(
                verdict_mass.get(true_v, 0.0) * loss_table[true_v][prediction]
                for true_v in classes
            )
            best = expected if best is None else min(best, expected)
        total += best
    return total


def _conditional_mutual_information(joint: dict, verdict_by_prep: dict, feature_fn) -> float:
    p_r = defaultdict(float)
    p_vr = defaultdict(float)
    p_ar = defaultdict(float)
    p_var = defaultdict(float)
    for (prep, r, a), prob in joint.items():
        v = verdict_by_prep[prep]
        f = feature_fn(r, a)
        p_r[r] += prob
        p_vr[(v, r)] += prob
        p_ar[(f, r)] += prob
        p_var[(v, f, r)] += prob
    info = 0.0
    for (v, f, r), prob in p_var.items():
        if prob <= 0.0:
            continue
        num = prob / p_r[r]
        den = (p_vr[(v, r)] / p_r[r]) * (p_ar[(f, r)] / p_r[r])
        if den <= 0.0:
            continue
        info += prob * math.log2(num / den)
    return info


@dataclass(frozen=True)
class ScreeningCertificate:
    verdict_by_prep: dict
    class_support: dict
    both_classes_populated: bool
    lift_by_loss: dict
    all_losses_positive_lift: bool
    cmi_class1: float
    cmi_positive: bool
    null_lift_by_loss: dict
    null_all_zero_lift: bool
    null_cmi: float


def screening_certificate() -> ScreeningCertificate:
    verdict_by_prep = _verdict_by_prep()
    joint = _joint_prep_record_aux(A0)

    support = defaultdict(float)
    for (prep, _r, _a), prob in joint.items():
        support[verdict_by_prep[prep]] += prob
    both_populated = all(mass > 0.0 for mass in support.values()) and len(support) == 2

    aux_feature = lambda r, a: a  # noqa: E731
    r_only = lambda r, a: r  # noqa: E731
    null_feature = lambda r, a: (r, r[0] ^ r[1])  # noqa: E731

    lift_by_loss = {}
    all_positive = True
    for name, table in LOSS_TABLES.items():
        risk_r = _bayes_risk(joint, verdict_by_prep, r_only, table)
        risk_ra = _bayes_risk(
            joint, verdict_by_prep, lambda r, a: (r, aux_feature(r, a)), table
        )
        lift = risk_r - risk_ra
        lift_by_loss[name] = {"risk_R": risk_r, "risk_R_aux": risk_ra, "lift": lift}
        if lift <= 1e-12:
            all_positive = False

    null_lift_by_loss = {}
    null_all_zero = True
    for name, table in LOSS_TABLES.items():
        risk_r = _bayes_risk(joint, verdict_by_prep, r_only, table)
        risk_ra = _bayes_risk(joint, verdict_by_prep, null_feature, table)
        lift = risk_r - risk_ra
        null_lift_by_loss[name] = {"risk_R": risk_r, "risk_R_aux": risk_ra, "lift": lift}
        if abs(lift) > 1e-12:
            null_all_zero = False

    cmi_class1 = _conditional_mutual_information(joint, verdict_by_prep, aux_feature)
    null_cmi = _conditional_mutual_information(
        joint, verdict_by_prep, lambda r, a: r[0] ^ r[1]
    )

    return ScreeningCertificate(
        verdict_by_prep=verdict_by_prep,
        class_support=dict(support),
        both_classes_populated=both_populated,
        lift_by_loss=lift_by_loss,
        all_losses_positive_lift=all_positive,
        cmi_class1=cmi_class1,
        cmi_positive=cmi_class1 > 1e-12,
        null_lift_by_loss=null_lift_by_loss,
        null_all_zero_lift=null_all_zero,
        null_cmi=null_cmi,
    )


# --------------------------------------------------------------------------- #
# (6) Null controls
# --------------------------------------------------------------------------- #

def _h_equal(h1: float, h2: float) -> bool:
    if math.isinf(h1) or math.isinf(h2):
        return math.isinf(h1) and math.isinf(h2)
    return math.isclose(h1, h2, abs_tol=1e-12)


def bprime_zero_divergence() -> dict:
    """Preparation B' (A0 copies nothing) shows zero divergence from A."""
    psi_a = prepare("A")
    psi_bp = prepare("Bprime")
    return {
        "statevector_identical": bool(np.allclose(psi_a, psi_bp, atol=1e-12)),
        "records_equal": records_equal(psi_a, psi_bp),
        "sbs_keys_equal": sbs_keys_equal(psi_a, psi_bp),
        "reversal_equal": math.isclose(
            reversal_report(psi_a, "A").best_branch_visibility,
            reversal_report(psi_bp, "Bprime").best_branch_visibility,
            abs_tol=1e-12,
        ),
        "H_equal": _h_equal(typed_axis_H(psi_a), typed_axis_H(psi_bp)),
    }


# --------------------------------------------------------------------------- #
# Top-level analysis
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class WitnessResult:
    theta: float
    v_star: float
    ordinary_records_equal: bool
    ordinary_record_A: dict
    ordinary_record_B: dict
    sbs_keys_equal: bool
    sbs_key_A: tuple
    sbs_key_B: tuple
    d1_finalized_A: bool
    d1_finalized_B: bool
    reversal_A: ReversalReport
    reversal_B: ReversalReport
    visibility_gap: float
    H_A: float
    H_B: float
    verdict_A: str
    verdict_B: str
    screening: ScreeningCertificate
    bprime: dict
    witness_holds: bool
    verdict_language: str


def run_analysis() -> WitnessResult:
    psi_a = prepare("A")
    psi_b = prepare("B")

    key_a = sbs_closure_key(psi_a)
    key_b = sbs_closure_key(psi_b)

    rev_a = reversal_report(psi_a, "A")
    rev_b = reversal_report(psi_b, "B")
    gap = rev_a.best_branch_visibility - rev_b.best_branch_visibility

    h_a = typed_axis_H(psi_a)
    h_b = typed_axis_H(psi_b)

    screening = screening_certificate()
    bprime = bprime_zero_divergence()

    records_eq = records_equal(psi_a, psi_b)
    keys_eq = key_a.as_tuple() == key_b.as_tuple()

    witness_holds = (
        records_eq
        and keys_eq
        and gap > 0.5
        and verdict_map(h_a) != verdict_map(h_b)
        and screening.both_classes_populated
        and screening.all_losses_positive_lift
        and screening.cmi_positive
        and screening.null_all_zero_lift
        and bprime["statevector_identical"]
    )

    if witness_holds:
        verdict_language = (
            "witness holds in this finite family: at a fixed ordinary "
            "event-level record and a fixed SBS closure key over F1..F4, the "
            "reversal-cost axis splits the D1-relative-to-access verdict, and "
            "an auxiliary channel on extra environment structure (A0) gives "
            "positive, non-screened-off decision-risk lift across the tested "
            "loss family. The T146 live class extra_environment_candidate "
            "(T150: typed_extra_environment_candidate) is non-empty in this "
            "finite model."
        )
    else:
        verdict_language = (
            "collapse extended: no construction in this family produced a "
            "reversal split at fixed ordinary record and fixed SBS key with a "
            "non-screened-off auxiliary lift. The T146 class "
            "extra_environment_candidate remains unwitnessed."
        )

    return WitnessResult(
        theta=THETA,
        v_star=V_STAR,
        ordinary_records_equal=records_eq,
        ordinary_record_A=ordinary_record_distribution(psi_a),
        ordinary_record_B=ordinary_record_distribution(psi_b),
        sbs_keys_equal=keys_eq,
        sbs_key_A=key_a.as_tuple(),
        sbs_key_B=key_b.as_tuple(),
        d1_finalized_A=d1_finalized_from_key(key_a),
        d1_finalized_B=d1_finalized_from_key(key_b),
        reversal_A=rev_a,
        reversal_B=rev_b,
        visibility_gap=gap,
        H_A=h_a,
        H_B=h_b,
        verdict_A=verdict_map(h_a),
        verdict_B=verdict_map(h_b),
        screening=screening,
        bprime=bprime,
        witness_holds=witness_holds,
        verdict_language=verdict_language,
    )


# --------------------------------------------------------------------------- #
# Serialization
# --------------------------------------------------------------------------- #

def _reversal_to_dict(rep: ReversalReport) -> dict:
    return {
        "preparation": rep.preparation,
        "per_outcome": {
            str(m): {
                "prob": vals["prob"],
                "vis_before": vals["vis_before"],
                "vis_after": vals["vis_after"],
            }
            for m, vals in rep.per_outcome.items()
        },
        "best_branch_visibility": rep.best_branch_visibility,
    }


def _screening_to_dict(cert: ScreeningCertificate) -> dict:
    return {
        "verdict_by_prep": cert.verdict_by_prep,
        "class_support": cert.class_support,
        "both_classes_populated": cert.both_classes_populated,
        "lift_by_loss": cert.lift_by_loss,
        "all_losses_positive_lift": cert.all_losses_positive_lift,
        "cmi_class1_bits": cert.cmi_class1,
        "cmi_positive": cert.cmi_positive,
        "null_lift_by_loss": cert.null_lift_by_loss,
        "null_all_zero_lift": cert.null_all_zero_lift,
        "null_cmi_bits": cert.null_cmi,
    }


def result_to_dict(result: WitnessResult) -> dict:
    def _hval(h):
        return "inf" if math.isinf(h) else h

    return {
        "theta": result.theta,
        "v_star": result.v_star,
        "ordinary_records_equal": result.ordinary_records_equal,
        "ordinary_record_A": {"".join(map(str, k)): v for k, v in result.ordinary_record_A.items()},
        "ordinary_record_B": {"".join(map(str, k)): v for k, v in result.ordinary_record_B.items()},
        "sbs_keys_equal": result.sbs_keys_equal,
        "sbs_key_A": list(result.sbs_key_A),
        "sbs_key_B": list(result.sbs_key_B),
        "d1_finalized_A": result.d1_finalized_A,
        "d1_finalized_B": result.d1_finalized_B,
        "reversal_A": _reversal_to_dict(result.reversal_A),
        "reversal_B": _reversal_to_dict(result.reversal_B),
        "visibility_gap": result.visibility_gap,
        "H_A": _hval(result.H_A),
        "H_B": _hval(result.H_B),
        "verdict_A": result.verdict_A,
        "verdict_B": result.verdict_B,
        "screening": _screening_to_dict(result.screening),
        "bprime": result.bprime,
        "witness_holds": result.witness_holds,
        "verdict_language": result.verdict_language,
    }


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(result_to_dict(res), indent=2))
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"ordinary records equal (A vs B):   {res.ordinary_records_equal}")
    print(f"SBS closure keys equal (A vs B):   {res.sbs_keys_equal}")
    print(f"  key A: {res.sbs_key_A}")
    print(f"  key B: {res.sbs_key_B}")
    print(f"D1 finalized from key (A / B):     {res.d1_finalized_A} / {res.d1_finalized_B}")
    print(f"reversal visibility A (best):      {res.reversal_A.best_branch_visibility:.6f}")
    print(f"reversal visibility B (best):      {res.reversal_B.best_branch_visibility:.6f}")
    print(f"visibility gap (A - B):            {res.visibility_gap:.6f}")
    print(f"reversal cost H(A) / H(B):         {res.H_A} / {res.H_B}")
    print(f"verdict A / B:                     {res.verdict_A} / {res.verdict_B}")
    print(f"both verdict classes populated:    {res.screening.both_classes_populated}")
    for name, vals in res.screening.lift_by_loss.items():
        print(f"  lift[{name}]: {vals['lift']:.6f}  (R={vals['risk_R']:.4f} -> R,A={vals['risk_R_aux']:.4f})")
    print(f"CMI I(V;A0|R) bits:                {res.screening.cmi_class1:.6f}")
    print(f"T137 null lift (all zero):         {res.screening.null_all_zero_lift}")
    print(f"B' zero divergence (identical):    {res.bprime['statevector_identical']}")
    print("-" * 70)
    print(f"WITNESS HOLDS: {res.witness_holds}")
    print(res.verdict_language)
