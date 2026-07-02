"""T407: Region-Indexed Capability No-Go (first executable C(R) instance).

Lineage: the bounded-region capability assignment named in the meta-synthesis
(audits/2026-07-01-tri-repo-synthesis-hegelian-metasynthesis.md, Section 4;
Hegelian survivor (a): "a region-indexed capability no-go with a declared
within-region intervention menu"). This artifact is the first executable
instance of the object C(R): a fixed bounded region R, a declared finite
intervention menu M supported on R, a declared task set T, and the
achievable-task profile C(R) = (optimal task values over M-protocols),
computed exactly for every configuration of a declared finite family.

THE THREE LEGS (each a reportable verdict; failure of any leg is the result):

  LEG 1 (capability profiles are real and region-indexed). R, M, T are
  declared once, uniformly across all configurations. C(R) is computed
  exactly per configuration; menu-achieved values are asserted equal to
  closed-form optima; the impossibility sides of the undo tasks are certified
  against ALL channels supported on R (T393's certificate pattern), not just
  against the menu.

  LEG 2 (anti-scalar at the capability level). The realized "can-do" order on
  configurations (componentwise comparison of capability profiles) is a
  genuine partial order with incomparable pairs. Its order dimension is
  computed with T394's own checkers (imported): dimension >= 2, hence -- by
  T394 Theorem 2, the T49 Anti-Scalar rung, including T394's tie-collapse
  closure -- NO scalar capability monotone (with or without ties) reproduces
  the enactability order. Witnessed concretely: an exhaustive scan of all
  4,683 weak orders on a 6-profile subfamily finds zero reproducing scalars
  (restriction-complete: any scalar on the family restricts to the
  subfamily), and per-pair trichotomy witnesses name the tasks that defeat
  each branch of f(x) < f(y) / = / >.

  LEG 3 (statistics underdetermine capability, quantified). The declared
  NON-capability probes -- the computational-basis (Z) readout distribution
  over R, the house's own ordinary-record convention (T392), with all its
  marginals, at every swept preparation phase -- are EXACTLY equal (max diff
  asserted < 1e-12, computes to 0.0) across a 16-configuration class that
  realizes ALL 12 distinct capability profiles. Hence no functional of the
  declared R-statistics decides any capability-typed test that varies on that
  class (finite enumeration proof within the family). The featured
  statistics-identical pair is capability-INCOMPARABLE with gaps >= 0.5 in
  both directions. Screening-off failure is certified with T392's own
  Bayes-risk / CMI machinery (imported). Conversely, a capability-identical
  pair differs in statistics: neither typing refines the other.

MODEL (exact statevector, deterministic, no sampling on any verdict path):

  Subsystems, INDEX-SORTED: (c, r1, r2, e1, e2, t), dims (3, 2, 2, 2, 2, 2),
  total Hilbert dimension 96 (< 2^7; inside the 10-qubit budget).

  - c: 3-level control over the k = 3 composition orders {ABC, BAC, CAB}
    (T395's canonical subset, imported), class partition "A before B"
    (class_of = [0, 1, 0]) and fine bit [0, 0, 1] (CAB within class 0).
  - r1, r2: the record register (class bit, fine bit), inside R. Records are
    written as c-controlled PHASE flips on |+> (Z^class on r1, Z^fine on r2),
    except the disclosed z-basis control write (see the family).
  - e1, e2: escape registers, OUTSIDE R (T393's escaped-mode pattern; here
    the region membership is declared once for all configurations, with T393
    cited as the artifact that showed such declarations can be causally
    forced -- re-deriving forcing is not this artifact's job).
  - t: target qubit traversing the composition order (T395's canonical
    operations A = Ry(pi/2), B = Rz(pi/2), C = Rx(pi/2), imported).

  REGION R = (c, r1, r2, t). RECORD SUB-REGION = (r1, r2).

  CONFIGURATION FAMILY (declared exhaustively; no cherry-picking): all 24
  combinations of r1-write in {none, class_phase, class_zbasis} x r2-write in
  {none, fine_phase} x e-write in {none, class, full, burn}. "burn" is the
  T393 B'-style null: a real, order-UNCORRELATED excitation of the escape
  register.

  TASK SET T (declared, four tasks, thresholds predeclared):
  - undo_within: phase-locked normalized visibility of the within-class
    control pair (0, 2), best over menu protocols; pass at v* = 0.9 (V_STAR
    imported from T392/T393, unchanged).
  - undo_cross: same for the cross-class pair (0, 1); pass at v*.
  - order_postdiction: optimal k = 3 order discrimination from the record
    sub-region alone (T395's D pattern); pass at p* = 0.9.
  - class_readout: optimal binary class discrimination from the record
    sub-region (priors 2/3, 1/3); pass at c* = 0.9.

  MENU M (declared once, finite): the 16 ordered compositions of the four
  uncompute generators (all supported on R: c-controlled Z^class on r1,
  c-controlled Z^class H on r1, c-controlled Z^fine on r2, c-controlled
  inverse order unitary on t), including do-nothing; plus the four product
  measurement settings {Z, X} x {Z, X} on the record sub-region with optimal
  classical post-processing.

  FIGURE-OF-MERIT DISCIPLINE (T392's lemma, T393's implementation): undo is
  scored by PHASE-LOCKED visibility over a uniform 8-point phase grid
  (imported T393 grid), which nulls manufactured coherence exactly -- the
  manufactured-coherence cheat is implemented as a null control, not just
  argued. Undo impossibility is certified by (i) exact phi-independence of
  the region-reduced state across a sweep including incommensurate phases
  (imported T393 sweep) and (ii) the T393-style channel-independent
  trace-norm bound covering every CPTP map supported on R at once.

GUARDRAILS (binding):
  - Q1D no-signalling, asserted numerically: the declared R readout is
    exactly independent of the preparation phase, of the escape-register
    writes, and of the target-operation settings (teeth: the same settings
    move the target marginal).
  - R1: untouched. Nothing here is a claim about global temporal order,
    simultaneity, or spacetime; "order" always means composition order.
  - Verdict vocabulary predeclared as module constants, asserted verbatim.

WHAT THIS DOES NOT EARN: no claim promotion, no CLAIM-LEDGER entry; not
TI-side source surplus (Ext_S needs surplus over capability-typed readout,
out of scope by construction here); no hardware or platform claim; the
resource-theory absorber (capability profiles as monotone vectors; "no total
resource order" is standard there) is priced in the spec -- the residue
claimed is the region-indexing, the record-access physicality, and the exact
statistics-flat family, not the theorem-shape.

Reproduction:
    python -m pytest tests/test_region_capability_no_go.py -v
    python -m models.region_capability_no_go
"""

from __future__ import annotations

import math
import sys
from itertools import combinations, product
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T394 machinery, reused by import: order-dimension checkers (exhaustive
# realizer search, incomparability, reconstruction verification, weak orders
# for the exhaustive scalar refutation).
from models.axis_count_reconstruction_hierarchy import (
    incomparable_pairs,
    is_chain,
    magnitudes_from_realizer,
    minimal_axis_count,
    verify_reconstruction,
    weak_orders,
)

# T393 machinery, reused by import: the predeclared phase grids (uniform
# locking grid; certificate sweep including incommensurate phases). The
# region/escape CONSTRUCTIONS are adapted (T393's helpers are hard-wired to
# its 9-qubit register layout; this model's subsystems are mixed-dimension),
# with the certificate and bound re-implemented generically below and cited.
from models.causal_forcing_access_asymmetry import PHI_CERT, PHI_LOCK_GRID

# T392 machinery, reused by import: the predeclared reversal-success
# threshold and the decision-theoretic certificate machinery (Bayes risk
# over a loss family, conditional mutual information).
from models.fixed_sbs_key_reversal_divergence import (
    V_STAR,
    _bayes_risk,
    _conditional_mutual_information,
)

# T395 machinery, reused by import: the k = 3 switch family (canonical
# 3-order subset, class partition, canonical operations), and the exact
# statevector primitives.
from models.record_order_tradeoff_probe import (
    A_CANON,
    B_CANON,
    C_CANON,
    I2,
    K3_CLASS_OF,
    K3_ORDERS,
    KET0,
    KET1,
    PSI_TARGET,
    basis,
    dm,
    kron_all,
    order_label,
    rdm,
    ry,
    trace_norm,
    u_of_order,
)

# --------------------------------------------------------------------------- #
# Predeclared constants (fixed before inspecting numbers)
# --------------------------------------------------------------------------- #

PI = math.pi
TOL_EXACT = 1e-12

# task pass thresholds: v* imported from T392/T393 (0.9, unchanged); the
# readout thresholds are set to the same round value, declared here.
P_STAR = 0.9
C_STAR = 0.9
TASK_NAMES = ("undo_within", "undo_cross", "order_postdiction", "class_readout")
TASK_THRESHOLDS = (V_STAR, V_STAR, P_STAR, C_STAR)

# Leg-3 capability-gap floor: the featured statistics-identical pair must
# show a gap >= CAP_GAP_MIN on at least one task in EACH direction.
CAP_GAP_MIN = 0.5

# teeth floor for "genuinely phi-dependent" region states (T393's 0.1)
PHI_DEPENDENCE_FLOOR = 0.1

# Haar spot check (illustrative only; the certificate carries the verdict)
HAAR_SAMPLES = 20
HAAR_SEED = 20260701
HAAR_VISIBILITY_CEILING = 0.05

# no-signalling setting perturbations (arbitrary fixed angles, predeclared)
SETTING_DELTA_A = 0.9
SETTING_DELTA_C = 0.7

# --------------------------------------------------------------------------- #
# Register layout and the k = 3 order structure (imported from T395)
# --------------------------------------------------------------------------- #

# Subsystems INDEX-SORTED: (c, r1, r2, e1, e2, t). Every stored or printed
# tuple reads in this order (house convention post-T392 review).
DIMS = (3, 2, 2, 2, 2, 2)
SUBSYSTEM_NAMES = ("c", "r1", "r2", "e1", "e2", "t")
TOTAL_DIM = int(np.prod(DIMS))

REGION = (0, 1, 2, 5)  # R = {c, r1, r2, t}; declared once, for every config
OUTSIDE = (3, 4)  # escape registers, outside R
RECORD = (1, 2)  # record sub-region (declared access for readout tasks)

CLASS_OF = tuple(K3_CLASS_OF)  # (0, 1, 0): "A before B" class (T395)
FINE_OF = (0, 0, 1)  # within-class-0 fine bit (CAB vs ABC)

UNDO_PAIR_WITHIN = (0, 2)  # both class 0
UNDO_PAIR_CROSS = (0, 1)  # class 0 vs class 1

R1_WRITES = ("none", "class_phase", "class_zbasis")
R2_WRITES = ("none", "fine_phase")
E_WRITES = ("none", "class", "full", "burn")
ALL_CONFIGS = tuple(product(R1_WRITES, R2_WRITES, E_WRITES))  # 24, exhaustive

NAMED_CONFIGS = {
    "pristine": ("none", "none", "none"),
    "full_keeper": ("class_phase", "fine_phase", "none"),
    "amnesic_emitter": ("none", "none", "full"),
    "publisher": ("class_phase", "fine_phase", "full"),
    "class_keeper_class_emitter": ("class_phase", "none", "class"),
    "fine_keeper_full_emitter": ("none", "fine_phase", "full"),
    "class_keeper": ("class_phase", "none", "none"),
    "z_keeper": ("class_zbasis", "none", "none"),
    "burn_emitter": ("none", "none", "burn"),
}
FEATURED_PAIR = ("pristine", "publisher")
CONVERSE_PAIR = ("class_keeper", "z_keeper")
VACUITY_PAIR = ("pristine", "z_keeper")
SPOTLIGHT_SUBFAMILY = (
    "pristine",
    "full_keeper",
    "amnesic_emitter",
    "publisher",
    "class_keeper_class_emitter",
    "fine_keeper_full_emitter",
)

# screening-certificate verdict vocabulary (T150 discipline: verdict = fixed
# map from the independently computed capability axis, declared here)
VERDICT_CAPABLE = "cross-undo-capable-at-R"
VERDICT_INCAPABLE = "cross-undo-incapable-at-R"

# three-loss family (T155 discipline: lift verified across a loss family,
# not one scoring rule)
CAPABILITY_LOSS_TABLES = {
    "zero_one": {
        VERDICT_CAPABLE: {VERDICT_CAPABLE: 0.0, VERDICT_INCAPABLE: 1.0},
        VERDICT_INCAPABLE: {VERDICT_CAPABLE: 1.0, VERDICT_INCAPABLE: 0.0},
    },
    "false_capable_costly": {
        VERDICT_CAPABLE: {VERDICT_CAPABLE: 0.0, VERDICT_INCAPABLE: 1.0},
        VERDICT_INCAPABLE: {VERDICT_CAPABLE: 5.0, VERDICT_INCAPABLE: 0.0},
    },
    "false_incapable_costly": {
        VERDICT_CAPABLE: {VERDICT_CAPABLE: 0.0, VERDICT_INCAPABLE: 4.0},
        VERDICT_INCAPABLE: {VERDICT_CAPABLE: 1.0, VERDICT_INCAPABLE: 0.0},
    },
}

# predeclared verdict strings (asserted verbatim in the test suite)
LEG1_VERDICT = (
    "C(R) realized: at one fixed region, one fixed finite intervention menu, "
    "and one declared four-task set, all 24 configurations of the declared "
    "write family have exactly computed capability profiles; menu-achieved "
    "values match closed-form optima exactly and 12 distinct profiles are "
    "realized -- a constructed finite object in this family, not a statement "
    "about physical agents"
)
LEG2_VERDICT = (
    "anti-scalar at the capability level: the realized capability poset is "
    "the exact product of an undo chain and a readout chain (a 3x4 grid) "
    "with incomparable pairs, and its order dimension is exactly 2; by T394 "
    "(Theorem 2, the T49 anti-scalar rung, with T394's tie-collapse closure) "
    "no scalar capability monotone -- with or without ties -- reproduces the "
    "enactability order, while the two exhibited monotone axes reconstruct "
    "it exactly; finite realized structure in this family, not a theorem "
    "about physical agents"
)
LEG3_VERDICT = (
    "statistics underdetermine capability in this family: the declared-"
    "readout statistics are constant (max diff 0.0 at every swept phase) "
    "across a 16-configuration class that realizes ALL 12 capability "
    "profiles, so no functional of the declared R-statistics decides any "
    "capability-typed test that varies on that class; the featured "
    "statistics-identical pair is capability-incomparable with gaps >= 0.5 "
    "in both directions, and a capability-identical pair differs in "
    "statistics -- neither typing refines the other; finite observation in "
    "this family, not a theorem"
)

# --------------------------------------------------------------------------- #
# Single-qubit objects and per-branch register states
# --------------------------------------------------------------------------- #

SQRT2 = math.sqrt(2.0)
KET_PLUS = (KET0 + KET1) / SQRT2
KET_MINUS = (KET0 - KET1) / SQRT2
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
HADAMARD = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex) / SQRT2

OPS3 = (A_CANON, B_CANON, C_CANON)  # T395 canonical operations


def _order_unitary(perm, ops=OPS3) -> np.ndarray:
    """Composition-order unitary, perm[0] applied first (T395 convention)."""
    U = np.eye(2, dtype=complex)
    for idx in perm:
        U = ops[idx] @ U
    return U


def _pow(op: np.ndarray, k: int) -> np.ndarray:
    return op if k else np.eye(op.shape[0], dtype=complex)


def _r1_op(write: str, branch: int) -> np.ndarray:
    if write == "none":
        return I2
    if write == "class_phase":
        return _pow(PAULI_Z, CLASS_OF[branch])
    if write == "class_zbasis":
        # H Z^class maps |+> to |0> / |1> by class: a record whose Z-basis
        # statistics ARE moved (the statistics-visible control write).
        return HADAMARD @ _pow(PAULI_Z, CLASS_OF[branch])
    raise ValueError(write)


def _r2_op(write: str, branch: int) -> np.ndarray:
    if write == "none":
        return I2
    if write == "fine_phase":
        return _pow(PAULI_Z, FINE_OF[branch])
    raise ValueError(write)


def _e_ops(write: str, branch: int) -> tuple:
    if write == "none":
        return I2, I2
    if write == "class":
        return _pow(PAULI_X, CLASS_OF[branch]), I2
    if write == "full":
        return _pow(PAULI_X, CLASS_OF[branch]), _pow(PAULI_X, FINE_OF[branch])
    if write == "burn":
        # real excitation, UNCORRELATED with the order (T393 B' pattern)
        return PAULI_X, I2
    raise ValueError(write)


def _t_state(branch: int, ops=OPS3) -> np.ndarray:
    return _order_unitary(K3_ORDERS[branch], ops) @ PSI_TARGET


# --------------------------------------------------------------------------- #
# State construction: branch sum + independent gate-built cross-check
# --------------------------------------------------------------------------- #

def config_state(
    cfg: tuple, phi: float = 0.0, phase_branch: int | None = None, ops=OPS3
) -> np.ndarray:
    """Branch-sum statevector for a configuration on (c, r1, r2, e1, e2, t).

    The control is prepared uniform over the three orders; ``phase_branch``
    (if given) carries the preparation phase e^{i phi} -- the phase the undo
    tasks must recover, placed on the second member of the undo pair.
    """
    r1w, r2w, ew = cfg
    amp = 1.0 / math.sqrt(3.0)
    out = np.zeros(TOTAL_DIM, dtype=complex)
    for i in range(3):
        a = amp * (np.exp(1j * phi) if phase_branch == i else 1.0)
        e1_op, e2_op = _e_ops(ew, i)
        out += a * kron_all(
            basis(3, i),
            _r1_op(r1w, i) @ KET_PLUS,
            _r2_op(r2w, i) @ KET_PLUS,
            e1_op @ KET0,
            e2_op @ KET0,
            _t_state(i, ops),
        )
    return out


def _controlled_on_c(op_for_branch, target: int) -> np.ndarray:
    """Full-space operator sum_i |i><i|_c (x) op_for_branch(i) on `target`."""
    total = np.zeros((TOTAL_DIM, TOTAL_DIM), dtype=complex)
    for i in range(3):
        factors = []
        for k, d in enumerate(DIMS):
            if k == 0:
                factors.append(dm(basis(3, i)))
            elif k == target:
                factors.append(op_for_branch(i))
            else:
                factors.append(np.eye(d, dtype=complex))
        total += kron_all(*factors)
    return total


def config_state_gates(
    cfg: tuple, phi: float = 0.0, phase_branch: int | None = None
) -> np.ndarray:
    """Gate-built construction (independent code path used for cross-checks)."""
    r1w, r2w, ew = cfg
    amps = np.full(3, 1.0 / math.sqrt(3.0), dtype=complex)
    if phase_branch is not None:
        amps[phase_branch] *= np.exp(1j * phi)
    state = kron_all(amps, KET_PLUS, KET_PLUS, KET0, KET0, PSI_TARGET)
    for gate in (
        _controlled_on_c(lambda i: _r1_op(r1w, i), 1),
        _controlled_on_c(lambda i: _r2_op(r2w, i), 2),
        _controlled_on_c(lambda i: _e_ops(ew, i)[0], 3),
        _controlled_on_c(lambda i: _e_ops(ew, i)[1], 4),
        _controlled_on_c(lambda i: _order_unitary(K3_ORDERS[i]), 5),
    ):
        state = gate @ state
    return state


def construction_cross_checks() -> dict:
    """Branch sum == gate built (all configs), and the local order unitary
    matches T395's own u_of_order exactly (provenance)."""
    max_state_diff = 0.0
    for cfg in ALL_CONFIGS:
        for phi, pb in ((0.0, None), (1.1, 1), (2.3, 2)):
            a = config_state(cfg, phi, pb)
            b = config_state_gates(cfg, phi, pb)
            max_state_diff = max(max_state_diff, float(np.max(np.abs(a - b))))
    max_op_diff = max(
        float(np.max(np.abs(_order_unitary(p) - u_of_order(p))))
        for p in K3_ORDERS
    )
    norms_ok = all(
        abs(np.linalg.norm(config_state(cfg)) - 1.0) < TOL_EXACT
        for cfg in ALL_CONFIGS
    )
    return {
        "max_branch_sum_vs_gate_built_diff": max_state_diff,
        "max_order_unitary_vs_t395_diff": max_op_diff,
        "all_norms_one": bool(norms_ok),
    }


# --------------------------------------------------------------------------- #
# The declared intervention menu M (finite, config-independent)
# --------------------------------------------------------------------------- #

MENU_GENERATOR_ORDER = (
    "unwrite_r1_zbasis",
    "unwrite_r1_phase",
    "unwrite_r2_phase",
    "unswitch",
)

_MENU_CACHE: dict | None = None


def menu_generators() -> dict:
    """The four uncompute generators, each supported on R = (c, r1, r2, t)."""
    return {
        "unwrite_r1_zbasis": _controlled_on_c(
            lambda i: _pow(PAULI_Z, CLASS_OF[i]) @ HADAMARD, 1
        ),
        "unwrite_r1_phase": _controlled_on_c(
            lambda i: _pow(PAULI_Z, CLASS_OF[i]), 1
        ),
        "unwrite_r2_phase": _controlled_on_c(
            lambda i: _pow(PAULI_Z, FINE_OF[i]), 2
        ),
        "unswitch": _controlled_on_c(
            lambda i: _order_unitary(K3_ORDERS[i]).conj().T, 5
        ),
    }


def menu_protocols() -> dict:
    """All 16 ordered compositions of generator subsets (incl. do-nothing).

    Application order is the fixed declared order MENU_GENERATOR_ORDER; the
    task value is the max over the menu, so per-configuration protocol choice
    is part of the capability, not a per-configuration redefinition of M.
    """
    global _MENU_CACHE
    if _MENU_CACHE is None:
        gens = menu_generators()
        protocols = {}
        names = MENU_GENERATOR_ORDER
        for mask in range(2 ** len(names)):
            chosen = [names[k] for k in range(len(names)) if (mask >> k) & 1]
            U = np.eye(TOTAL_DIM, dtype=complex)
            for name in chosen:
                U = gens[name] @ U
            protocols["+".join(chosen) if chosen else "id"] = U
        _MENU_CACHE = protocols
    return _MENU_CACHE


MEASUREMENT_SETTINGS = (("Z", "Z"), ("Z", "X"), ("X", "Z"), ("X", "X"))
_SINGLE_BASES = {"Z": (KET0, KET1), "X": (KET_PLUS, KET_MINUS)}


def _record_measurement_vectors(setting: tuple) -> list:
    s1, s2 = setting
    return [
        np.kron(v1, v2)
        for v1 in _SINGLE_BASES[s1]
        for v2 in _SINGLE_BASES[s2]
    ]


# --------------------------------------------------------------------------- #
# Task 1 & 2: phase-locked undo (T393 figure of merit, adapted)
# --------------------------------------------------------------------------- #

def locked_visibility(cfg: tuple, protocol: np.ndarray, pair: tuple) -> float:
    """Phase-locked NORMALIZED visibility of a control coherence pair.

    |mean_phi e^{i phi} 3 rho_c[a, b](phi)| over the uniform T393 grid, after
    the protocol. For a genuine undo of pair (a, b) with the phase prepared
    on branch b, rho_c[a, b] = (1/3) e^{-i phi} (recovered overlap), so the
    locked value equals the recovered normalized coherence; for manufactured
    (phi-independent) coherence the uniform grid nulls it exactly (T392
    lemma, T393 implementation).
    """
    a, b = pair
    total = 0.0 + 0.0j
    for phi in PHI_LOCK_GRID:
        state = protocol @ config_state(cfg, phi=phi, phase_branch=b)
        rho_c = rdm(state, DIMS, (0,))
        total += np.exp(1j * phi) * 3.0 * rho_c[a, b]
    return float(abs(total / len(PHI_LOCK_GRID)))


def undo_value(cfg: tuple, pair: tuple) -> tuple:
    """Best locked visibility over the declared menu; (value, protocol)."""
    best, best_name = 0.0, "id"
    for name, protocol in menu_protocols().items():
        v = locked_visibility(cfg, protocol, pair)
        if v > best:
            best, best_name = v, name
    return best, best_name


# ---- impossibility certificates (adapted from T393, generic dims) -------- #

def region_state(cfg: tuple, phi: float, phase_branch: int) -> np.ndarray:
    """Reduced state on R -- the only object any R-supported channel sees."""
    return rdm(config_state(cfg, phi=phi, phase_branch=phase_branch), DIMS, REGION)


def phi_independence_certificate(cfg: tuple, pair: tuple) -> float:
    """Max pairwise max-abs difference of rho_R(phi) across the T393 sweep
    (incommensurate phases included). If this is < 1e-12, every channel
    output -- and hence every recovered visibility -- is phi-independent, so
    NO channel supported on R achieves any phase-locked recovery (T393's
    certificate pattern)."""
    states = [region_state(cfg, phi, pair[1]) for phi in PHI_CERT]
    diff = 0.0
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            diff = max(diff, float(np.max(np.abs(states[i] - states[j]))))
    return diff


def in_region_channel_bound(cfg: tuple, pair: tuple) -> float:
    """Channel-independent upper bound on the locked visibility of ANY CPTP
    map supported on R (T393's Hoelder + trace-norm-contractivity bound,
    normalization adapted to the 3-level control):

        L = 3 |Tr[Lambda(X) (|b><a|_c (x) I)]|,
        X = mean_phi e^{i phi} rho_R(phi)
        => L <= 3 (||Re X||_1 + ||Im X||_1).
    """
    dim = int(np.prod([DIMS[k] for k in REGION]))
    X = np.zeros((dim, dim), dtype=complex)
    for phi in PHI_LOCK_GRID:
        X = X + np.exp(1j * phi) * region_state(cfg, phi, pair[1])
    X = X / len(PHI_LOCK_GRID)
    herm = (X + X.conj().T) / 2.0
    anti = (X - X.conj().T) / 2.0j
    return 3.0 * (trace_norm(herm) + trace_norm(anti))


# --------------------------------------------------------------------------- #
# Task 3 & 4: record-sub-region readout (T395's D pattern)
# --------------------------------------------------------------------------- #

def record_branch_states(cfg: tuple) -> list:
    """Conditional record-sub-region states per order branch (pure, 4-dim)."""
    r1w, r2w, _ = cfg
    return [
        np.kron(_r1_op(r1w, i) @ KET_PLUS, _r2_op(r2w, i) @ KET_PLUS)
        for i in range(3)
    ]


def _branch_groups(states: list) -> list:
    """Group branches by identical record states; guard: distinct groups must
    be mutually orthogonal (holds for every configuration of this family --
    all writes are Z/X-eigenbasis moves on |+>). The guard makes the closed
    form honest: it raises rather than silently mis-scoring if the family is
    ever extended past orthogonality."""
    groups: list[list[int]] = []
    for i, s in enumerate(states):
        placed = False
        for g in groups:
            ov = abs(np.vdot(states[g[0]], s))
            if ov > 1.0 - 1e-12:
                g.append(i)
                placed = True
                break
            if ov > 1e-12:
                raise ValueError(
                    "record states neither identical nor orthogonal; the "
                    "closed-form optimum does not apply"
                )
        if not placed:
            groups.append([i])
    return groups


def order_postdiction_optimum(cfg: tuple) -> float:
    """Exact optimal k = 3 order postdiction from the record sub-region.

    With branches grouped into mutually orthogonal identical-state groups
    (guarded), the optimum is (#groups)/3: measure the distinguishing basis,
    guess one branch per group (the identical-in-class reduction of T395's
    guess_prob_record_only, here in the fully orthogonal corner)."""
    return len(_branch_groups(record_branch_states(cfg))) / 3.0


def class_readout_optimum(cfg: tuple) -> float:
    """Exact optimal binary class readout (Helstrom, priors 2/3 vs 1/3)."""
    states = record_branch_states(cfg)
    dim = states[0].shape[0]
    sigma0 = np.zeros((dim, dim), dtype=complex)
    sigma1 = np.zeros((dim, dim), dtype=complex)
    for i, s in enumerate(states):
        if CLASS_OF[i] == 0:
            sigma0 += dm(s) / 3.0
        else:
            sigma1 += dm(s) / 3.0
    return 0.5 * (1.0 + trace_norm(sigma0 - sigma1))


def order_postdiction_menu_value(cfg: tuple) -> float:
    """Best order postdiction over the declared measurement settings with
    optimal classical post-processing (computed exactly)."""
    states = record_branch_states(cfg)
    best = 0.0
    for setting in MEASUREMENT_SETTINGS:
        vecs = _record_measurement_vectors(setting)
        p = sum(
            max(abs(np.vdot(v, s)) ** 2 for s in states) / 3.0 for v in vecs
        )
        best = max(best, float(p))
    return best


def class_readout_menu_value(cfg: tuple) -> float:
    """Best class readout over the declared measurement settings with optimal
    classical post-processing (computed exactly)."""
    states = record_branch_states(cfg)
    best = 0.0
    for setting in MEASUREMENT_SETTINGS:
        vecs = _record_measurement_vectors(setting)
        p = 0.0
        for v in vecs:
            m0 = sum(
                abs(np.vdot(v, states[i])) ** 2 / 3.0
                for i in range(3)
                if CLASS_OF[i] == 0
            )
            m1 = sum(
                abs(np.vdot(v, states[i])) ** 2 / 3.0
                for i in range(3)
                if CLASS_OF[i] == 1
            )
            p += max(m0, m1)
        best = max(best, float(p))
    return best


# --------------------------------------------------------------------------- #
# The capability profile C(R) per configuration
# --------------------------------------------------------------------------- #

def capability_profile(cfg: tuple) -> dict:
    """C(R) entry for one configuration: the four task values, the achieving
    protocols, menu-vs-closed-form residuals, and pass flags."""
    u_w, p_w = undo_value(cfg, UNDO_PAIR_WITHIN)
    u_x, p_x = undo_value(cfg, UNDO_PAIR_CROSS)
    post_opt = order_postdiction_optimum(cfg)
    post_menu = order_postdiction_menu_value(cfg)
    cls_opt = class_readout_optimum(cfg)
    cls_menu = class_readout_menu_value(cfg)
    values = (u_w, u_x, post_opt, cls_opt)
    return {
        "writes": {"r1": cfg[0], "r2": cfg[1], "e": cfg[2]},
        "profile": {name: float(v) for name, v in zip(TASK_NAMES, values)},
        "passes": {
            name: bool(v >= thr)
            for name, v, thr in zip(TASK_NAMES, values, TASK_THRESHOLDS)
        },
        "undo_best_protocols": {"undo_within": p_w, "undo_cross": p_x},
        "menu_residuals": {
            "order_postdiction": float(abs(post_menu - post_opt)),
            "class_readout": float(abs(cls_menu - cls_opt)),
        },
    }


def profile_key(entry: dict) -> tuple:
    return tuple(round(entry["profile"][name], 9) for name in TASK_NAMES)


def all_profiles() -> dict:
    return {"|".join(cfg): capability_profile(cfg) for cfg in ALL_CONFIGS}


# --------------------------------------------------------------------------- #
# Leg 1 assembly: profiles + certificates
# --------------------------------------------------------------------------- #

def leg1_analysis(profiles: dict) -> dict:
    named_of = {"|".join(v): k for k, v in NAMED_CONFIGS.items()}
    max_menu_residual = max(
        max(entry["menu_residuals"].values()) for entry in profiles.values()
    )
    distinct = sorted({profile_key(e) for e in profiles.values()})
    u_hierarchy = all(
        e["profile"]["undo_within"] >= e["profile"]["undo_cross"] - 1e-9
        for e in profiles.values()
    )
    for key, entry in profiles.items():
        entry["named"] = named_of.get(key)
    return {
        "n_configurations": len(profiles),
        "distinct_profile_count": len(distinct),
        "distinct_profiles": [list(p) for p in distinct],
        "max_menu_vs_closed_form_residual": float(max_menu_residual),
        "undo_within_ge_undo_cross_everywhere": bool(u_hierarchy),
        "cross_checks": construction_cross_checks(),
    }


def certificate_analysis(profiles: dict) -> dict:
    """Impossibility certificates for every zero-valued undo leg; teeth for
    every passing undo leg; the pristine bound sanity; Haar spot check;
    manufactured-coherence null."""
    zero_legs = {}
    pass_phi_dependence_min = math.inf
    for cfg in ALL_CONFIGS:
        key = "|".join(cfg)
        for task, pair in (
            ("undo_within", UNDO_PAIR_WITHIN),
            ("undo_cross", UNDO_PAIR_CROSS),
        ):
            value = profiles[key]["profile"][task]
            if value < V_STAR:
                zero_legs[f"{key}::{task}"] = {
                    "menu_max": float(value),
                    "phi_independence_max_pairwise_diff": float(
                        phi_independence_certificate(cfg, pair)
                    ),
                    "channel_bound": float(in_region_channel_bound(cfg, pair)),
                }
            else:
                pass_phi_dependence_min = min(
                    pass_phi_dependence_min,
                    phi_independence_certificate(cfg, pair),
                )
    bound_pristine = in_region_channel_bound(
        NAMED_CONFIGS["pristine"], UNDO_PAIR_CROSS
    )
    achieved_pristine = profiles["|".join(NAMED_CONFIGS["pristine"])]["profile"][
        "undo_cross"
    ]
    return {
        "n_zero_legs": len(zero_legs),
        "zero_legs": zero_legs,
        "all_zero_legs_certified": bool(
            all(
                z["phi_independence_max_pairwise_diff"] < TOL_EXACT
                and z["channel_bound"] < V_STAR
                for z in zero_legs.values()
            )
        ),
        "pass_legs_phi_dependence_min": float(pass_phi_dependence_min),
        "pristine_bound_respects_achievable": {
            "channel_bound": float(bound_pristine),
            "achieved": float(achieved_pristine),
        },
        "haar_spot_check": haar_spot_check(),
        "manufactured_coherence_null": manufactured_coherence_null(),
    }


def _embed_on_region(U: np.ndarray) -> np.ndarray:
    """Embed a unitary on the REGION subsystems into the full space."""
    n = len(DIMS)
    others = [k for k in range(n) if k not in REGION]
    perm = list(REGION) + others
    d_o = int(np.prod([DIMS[k] for k in others]))
    big = np.kron(U, np.eye(d_o, dtype=complex))
    idx = np.arange(TOTAL_DIM).reshape(DIMS).transpose(perm).reshape(-1)
    P = np.zeros((TOTAL_DIM, TOTAL_DIM), dtype=complex)
    P[np.arange(TOTAL_DIM), idx] = 1.0
    return P.T @ big @ P


def haar_spot_check(
    cfg_name: str = "publisher",
    pair: tuple = UNDO_PAIR_CROSS,
    samples: int = HAAR_SAMPLES,
    seed: int = HAAR_SEED,
) -> dict:
    """Illustrative only: Haar-random unitaries on R do not beat the
    certificate (the certificate, not this sampling, carries the verdict)."""
    cfg = NAMED_CONFIGS[cfg_name]
    rng = np.random.default_rng(seed)
    dim = int(np.prod([DIMS[k] for k in REGION]))
    best = 0.0
    for _ in range(samples):
        z = (rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim)))
        q, r = np.linalg.qr(z)
        q = q @ np.diag(np.diag(r) / np.abs(np.diag(r)))
        best = max(best, locked_visibility(cfg, _embed_on_region(q), pair))
    return {
        "config": cfg_name,
        "samples": samples,
        "max_locked_visibility": float(best),
        "ceiling": HAAR_VISIBILITY_CEILING,
    }


def manufactured_coherence_null(
    cfg_name: str = "publisher", pair: tuple = UNDO_PAIR_CROSS
) -> dict:
    """The cheat channel (discard c, re-prepare (|0>+|1>)/sqrt(2)_c -- a valid
    CPTP map supported on R) manufactures raw normalized coherence 1.5 but
    locked visibility exactly 0: the locked metric is not gameable (T392
    lemma; T393 control, re-implemented here)."""
    a, b = pair
    chi = (basis(3, 0) + basis(3, 1)) / SQRT2
    rho_c = dm(chi)
    raw = 3.0 * abs(rho_c[a, b])
    total = sum(np.exp(1j * phi) * 3.0 * rho_c[a, b] for phi in PHI_LOCK_GRID)
    locked = float(abs(total / len(PHI_LOCK_GRID)))
    return {"config": cfg_name, "raw_normalized": float(raw), "locked": locked}


# --------------------------------------------------------------------------- #
# Leg 2: the realized capability poset, dimension, anti-scalar witnesses
# --------------------------------------------------------------------------- #

def _leq(p: tuple, q: tuple) -> bool:
    return all(p[k] <= q[k] + 1e-9 for k in range(len(p)))


def build_capability_poset(profiles: dict) -> dict:
    """Distinct profiles, naturally labeled (sorted by component sum then
    lexicographically -- strict dominance strictly increases the sum, so the
    labeling is natural in T394's sense), with the strict enactability order."""
    distinct = sorted({profile_key(e) for e in profiles.values()},
                      key=lambda p: (sum(p), p))
    label = {p: i for i, p in enumerate(distinct)}
    n = len(distinct)
    rel = frozenset(
        (i, j)
        for i, p in enumerate(distinct)
        for j, q in enumerate(distinct)
        if i != j and _leq(p, q) and not _leq(q, p)
    )
    natural = all(i < j for (i, j) in rel)
    members = {i: [] for i in range(n)}
    for key, entry in profiles.items():
        members[label[profile_key(entry)]].append(key)
    return {
        "n": n,
        "profiles": distinct,
        "labels": label,
        "rel": rel,
        "natural_labeling": natural,
        "members": members,
    }


def grid_product_structure(poset: dict) -> dict:
    """Verify the realized poset is EXACTLY the product order of an undo
    chain and a readout chain (the two interpretable capability axes)."""
    distinct = poset["profiles"]
    u_parts = sorted({p[:2] for p in distinct})
    ro_parts = sorted({p[2:] for p in distinct})
    u_chain = all(
        _leq(u_parts[i], u_parts[i + 1]) for i in range(len(u_parts) - 1)
    )
    ro_chain = all(
        _leq(ro_parts[i], ro_parts[i + 1]) for i in range(len(ro_parts) - 1)
    )
    u_level = {u: i for i, u in enumerate(u_parts)}
    ro_level = {r: i for i, r in enumerate(ro_parts)}
    is_product = True
    for p in distinct:
        for q in distinct:
            if p == q:
                continue
            lhs = _leq(p, q) and not _leq(q, p)
            rhs = (
                u_level[p[:2]] <= u_level[q[:2]]
                and ro_level[p[2:]] <= ro_level[q[2:]]
                and (u_level[p[:2]], ro_level[p[2:]])
                != (u_level[q[:2]], ro_level[q[2:]])
            )
            if lhs != rhs:
                is_product = False
    return {
        "n_undo_levels": len(u_parts),
        "n_readout_levels": len(ro_parts),
        "undo_part_is_chain": bool(u_chain),
        "readout_part_is_chain": bool(ro_chain),
        "is_exact_product_order": bool(is_product),
        "undo_levels": [list(u) for u in u_parts],
        "readout_levels": [list(r) for r in ro_parts],
    }


def scalar_refutation_exhaustive(profiles: dict) -> dict:
    """Exhaustive anti-scalar witness on the spotlight 6-profile subfamily:
    ALL weak orders (total preorders = the order structure of any real-valued
    scalar, ties allowed) are scanned; zero reproduce the enactability order.
    Restriction-complete: a scalar monotone reproducing the full family's
    order restricts to one on every subfamily, so refuting all scalars on the
    subfamily exhaustively refutes all scalars on the family."""
    sub_profiles = []
    for name in SPOTLIGHT_SUBFAMILY:
        key = "|".join(NAMED_CONFIGS[name])
        sub_profiles.append(profile_key(profiles[key]))
    assert len(set(sub_profiles)) == len(sub_profiles)
    order = sorted(range(len(sub_profiles)),
                   key=lambda k: (sum(sub_profiles[k]), sub_profiles[k]))
    relabeled = [sub_profiles[k] for k in order]
    names = [SPOTLIGHT_SUBFAMILY[k] for k in order]
    n = len(relabeled)
    rel = frozenset(
        (i, j)
        for i in range(n)
        for j in range(n)
        if i != j and _leq(relabeled[i], relabeled[j])
        and not _leq(relabeled[j], relabeled[i])
    )
    count = 0
    total = 0
    for lev in weak_orders(n):
        total += 1
        if all(
            ((i, j) in rel) == (lev[i] <= lev[j])
            for i in range(n)
            for j in range(n)
            if i != j
        ):
            count += 1
    return {
        "subfamily": names,
        "subfamily_profiles": [list(p) for p in relabeled],
        "n_weak_orders_scanned": total,
        "n_reproducing_scalars": count,
    }


def scalar_trichotomy_witness(profiles: dict, name_a: str, name_b: str) -> dict:
    """The concrete per-pair anti-scalar witness: for the incomparable pair
    (A, B), name a task where A strictly beats B and one where B strictly
    beats A; then each branch of the scalar trichotomy is defeated:
    f(A) <= f(B) denies A's strict advantage, f(B) <= f(A) denies B's, and a
    real-valued f must satisfy one of the two (totality)."""
    pa = profiles["|".join(NAMED_CONFIGS[name_a])]["profile"]
    pb = profiles["|".join(NAMED_CONFIGS[name_b])]["profile"]
    a_beats = [t for t in TASK_NAMES if pa[t] > pb[t] + 1e-9]
    b_beats = [t for t in TASK_NAMES if pb[t] > pa[t] + 1e-9]
    return {
        "pair": [name_a, name_b],
        "tasks_where_first_strictly_better": a_beats,
        "tasks_where_second_strictly_better": b_beats,
        "incomparable": bool(a_beats and b_beats),
        "max_gap_first_direction": float(
            max((pa[t] - pb[t] for t in a_beats), default=0.0)
        ),
        "max_gap_second_direction": float(
            max((pb[t] - pa[t] for t in b_beats), default=0.0)
        ),
    }


def leg2_analysis(profiles: dict) -> dict:
    poset = build_capability_poset(profiles)
    n, rel = poset["n"], poset["rel"]
    incomp = incomparable_pairs(n, rel)
    dim, realizer = minimal_axis_count(n, rel)
    reconstruction_ok = verify_reconstruction(n, rel, realizer)
    mags = magnitudes_from_realizer(n, realizer)
    grid = grid_product_structure(poset)
    hasse = _hasse_edges(n, rel)
    return {
        "n_profiles": n,
        "profiles_by_label": [list(p) for p in poset["profiles"]],
        "members_by_label": {str(k): v for k, v in poset["members"].items()},
        "natural_labeling": poset["natural_labeling"],
        "relation_size": len(rel),
        "n_incomparable_pairs": len(incomp),
        "incomparable_pairs": [list(p) for p in incomp],
        "is_chain": bool(is_chain(n, rel)),
        "order_dimension": int(dim),
        "realizer": [list(ext) for ext in realizer],
        "realizer_reconstruction_verified": bool(reconstruction_ok),
        "two_axis_magnitudes": [list(m) for m in mags],
        "grid_product_structure": grid,
        "hasse_edges": [list(e) for e in hasse],
        "scalar_refutation_exhaustive": scalar_refutation_exhaustive(profiles),
        "trichotomy_witnesses": {
            "pristine_vs_publisher": scalar_trichotomy_witness(
                profiles, "pristine", "publisher"
            ),
            "class_keeper_class_emitter_vs_publisher": scalar_trichotomy_witness(
                profiles, "class_keeper_class_emitter", "publisher"
            ),
        },
    }


def _hasse_edges(n: int, rel: frozenset) -> list:
    edges = []
    for (a, b) in sorted(rel):
        if not any((a, c) in rel and (c, b) in rel for c in range(n)):
            edges.append((a, b))
    return edges


# --------------------------------------------------------------------------- #
# Leg 3: declared statistics, equality classes, screening-off failure
# --------------------------------------------------------------------------- #

def declared_readout(
    cfg: tuple, phi: float = 0.0, phase_branch: int | None = None, ops=OPS3
) -> np.ndarray:
    """The declared NON-capability probe: the exact joint computational-basis
    (Z) readout distribution over R = (c, r1, r2, t) -- the house's ordinary
    event-level record convention (T392) -- as an array indexed (c, r1, r2, t).
    All marginals are functionals of this object."""
    p = np.abs(config_state(cfg, phi=phi, phase_branch=phase_branch, ops=ops)) ** 2
    return p.reshape(DIMS).sum(axis=OUTSIDE)


def stats_bundle(cfg: tuple) -> np.ndarray:
    """The full declared-statistics object: the readout distribution at the
    unphased preparation and at every certificate phase for both phase
    placements (the same preparations the capability tasks use)."""
    arrs = [declared_readout(cfg)]
    for pb in (UNDO_PAIR_CROSS[1], UNDO_PAIR_WITHIN[1]):
        for phi in PHI_CERT:
            arrs.append(declared_readout(cfg, phi=phi, phase_branch=pb))
    return np.stack(arrs)


def stats_max_diff(cfg_a: tuple, cfg_b: tuple) -> float:
    return float(np.max(np.abs(stats_bundle(cfg_a) - stats_bundle(cfg_b))))


def statistics_partition() -> dict:
    """Partition the 24 configurations by exact declared-statistics equality."""
    reps: list[tuple] = []
    classes: list[list[str]] = []
    intra = 0.0
    for cfg in ALL_CONFIGS:
        placed = False
        for k, rep in enumerate(reps):
            d = stats_max_diff(cfg, rep)
            if d < TOL_EXACT:
                classes[k].append("|".join(cfg))
                intra = max(intra, d)
                placed = True
                break
        if not placed:
            reps.append(cfg)
            classes.append(["|".join(cfg)])
    inter = math.inf
    for i in range(len(reps)):
        for j in range(i + 1, len(reps)):
            inter = min(inter, stats_max_diff(reps[i], reps[j]))
    return {
        "n_classes": len(classes),
        "class_sizes": [len(c) for c in classes],
        "classes": classes,
        "max_intra_class_diff": float(intra),
        "min_inter_class_diff": float(inter),
    }


def leg3_analysis(profiles: dict) -> dict:
    partition = statistics_partition()
    # the statistics-flat class containing pristine
    pristine_key = "|".join(NAMED_CONFIGS["pristine"])
    flat_class = next(c for c in partition["classes"] if pristine_key in c)
    flat_profiles = {profile_key(profiles[k]) for k in flat_class}
    all_profile_keys = {profile_key(e) for e in profiles.values()}
    # featured pair
    cfg_a, cfg_b = (NAMED_CONFIGS[n] for n in FEATURED_PAIR)
    key_a, key_b = ("|".join(c) for c in (cfg_a, cfg_b))
    pa = profiles[key_a]["profile"]
    pb = profiles[key_b]["profile"]
    gaps = {t: float(pa[t] - pb[t]) for t in TASK_NAMES}
    a_dir = max(pa[t] - pb[t] for t in TASK_NAMES)
    b_dir = max(pb[t] - pa[t] for t in TASK_NAMES)
    # the capability-typed test no statistics functional decides
    test_values = {
        k: bool(profiles[k]["profile"]["undo_cross"] >= V_STAR)
        for k in flat_class
    }
    # converse pair: capability-identical, statistics-distinct
    cc_a, cc_b = (NAMED_CONFIGS[n] for n in CONVERSE_PAIR)
    ck_a, ck_b = ("|".join(c) for c in (cc_a, cc_b))
    converse_profile_diff = max(
        abs(profiles[ck_a]["profile"][t] - profiles[ck_b]["profile"][t])
        for t in TASK_NAMES
    )
    return {
        "statistics_partition": partition,
        "flat_class_size": len(flat_class),
        "n_profiles_realized_in_flat_class": len(flat_profiles),
        "flat_class_realizes_all_profiles": bool(
            flat_profiles == all_profile_keys
        ),
        "featured_pair": {
            "configs": list(FEATURED_PAIR),
            "stats_max_diff": stats_max_diff(cfg_a, cfg_b),
            "profile_first": pa,
            "profile_second": pb,
            "gaps_first_minus_second": gaps,
            "max_gap_each_direction": [float(a_dir), float(b_dir)],
            "gap_floor_met_both_directions": bool(
                a_dir >= CAP_GAP_MIN and b_dir >= CAP_GAP_MIN
            ),
        },
        "capability_test_undecidable_by_statistics": {
            "test": f"undo_cross >= v* ({V_STAR})",
            "flat_class_statistics_constant": True,
            "test_nonconstant_on_flat_class": bool(
                len(set(test_values.values())) == 2
            ),
            "n_pass": sum(test_values.values()),
            "n_fail": len(test_values) - sum(test_values.values()),
        },
        "converse_pair": {
            "configs": list(CONVERSE_PAIR),
            "profile_max_diff": float(converse_profile_diff),
            "stats_max_diff": stats_max_diff(cc_a, cc_b),
        },
        "screening": screening_certificate(),
        "vacuity_control": statistics_distinguish_control(),
        "burn_null": burn_null(profiles),
    }


# ---- screening-off certificate (T392 machinery, imported) ---------------- #

def _mixed_probe_distribution(cfg: tuple) -> dict:
    """Exact outcome distribution of ONE menu probe: (c, t) read in Z, the
    record sub-region read in X (x) X. Outcomes keyed ((c, t), (x1, x2))."""
    state = config_state(cfg)
    tensor = state.reshape(DIMS)
    out: dict = {}
    x_vecs = {0: KET_PLUS, 1: KET_MINUS}
    for c in range(3):
        for x1 in (0, 1):
            for x2 in (0, 1):
                for t in (0, 1):
                    block = tensor[c, :, :, :, :, t]
                    amp = np.einsum(
                        "abcd,a,b->cd",
                        block,
                        x_vecs[x1].conj(),
                        x_vecs[x2].conj(),
                    )
                    prob = float(np.sum(np.abs(amp) ** 2))
                    if prob > 1e-15:
                        out[((c, t), (x1, x2))] = prob
    return out


def _full_z_distribution(cfg: tuple) -> dict:
    """Exact declared readout as a dict keyed by (c, r1, r2, t)."""
    arr = declared_readout(cfg)
    out = {}
    for idx, prob in np.ndenumerate(arr):
        if prob > 1e-15:
            out[idx] = float(prob)
    return out


def screening_certificate() -> dict:
    """T392-pattern screening certificate for the featured pair, using
    T392's own _bayes_risk and _conditional_mutual_information (imported).

    Decision problem: equal-prior mixture of the two configurations; verdict
    V = the capability verdict (fixed map from the certified undo_cross
    axis). Certified: (i) the FULL declared readout carries exactly zero
    verdict information (equal distributions; zero lift on all three losses;
    I(V; S) = 0); (ii) one declared menu probe gives strictly positive lift
    on all three losses and positive conditional mutual information given
    the probe's own statistics-typed part; (iii) a T137-style downstream
    transform of the statistics is null."""
    cfg_a, cfg_b = (NAMED_CONFIGS[n] for n in FEATURED_PAIR)
    verdicts = {
        FEATURED_PAIR[0]: VERDICT_CAPABLE,
        FEATURED_PAIR[1]: VERDICT_INCAPABLE,
    }
    # joint over the FULL declared readout (statistics-only experiment)
    joint_stats: dict = {}
    for name, cfg in zip(FEATURED_PAIR, (cfg_a, cfg_b)):
        for s, prob in _full_z_distribution(cfg).items():
            joint_stats[(name, s, "none")] = joint_stats.get(
                (name, s, "none"), 0.0
            ) + 0.5 * prob
    # joint over the mixed menu probe: (c, t) in Z [statistics-typed part],
    # record in X (x) X [capability-typed part]
    joint_probe: dict = {}
    for name, cfg in zip(FEATURED_PAIR, (cfg_a, cfg_b)):
        for (s_ct, o_r), prob in _mixed_probe_distribution(cfg).items():
            joint_probe[(name, s_ct, o_r)] = joint_probe.get(
                (name, s_ct, o_r), 0.0
            ) + 0.5 * prob

    def risks(joint, feature_fn):
        return {
            loss: float(_bayes_risk(joint, verdicts, feature_fn, table))
            for loss, table in CAPABILITY_LOSS_TABLES.items()
        }

    prior_risk = risks(joint_stats, lambda r, a: "prior-only")
    stats_risk = risks(joint_stats, lambda r, a: r)
    probe_ct_risk = risks(joint_probe, lambda r, a: r)
    probe_full_risk = risks(joint_probe, lambda r, a: (r, a))
    cmi_stats = float(
        _conditional_mutual_information(
            {(n_, "none", s): p for (n_, s, _), p in joint_stats.items()},
            verdicts,
            lambda r, a: a,
        )
    )
    cmi_probe = float(
        _conditional_mutual_information(joint_probe, verdicts, lambda r, a: a)
    )
    # T137 null: a deterministic downstream transform of the statistics part
    null_risk = risks(joint_probe, lambda r, a: (r[0] + r[1]) % 2)
    cmi_null = float(
        _conditional_mutual_information(
            joint_probe, verdicts, lambda r, a: (r[0] + r[1]) % 2
        )
    )
    return {
        "verdict_map": verdicts,
        "prior_only_risk": prior_risk,
        "full_declared_readout_risk": stats_risk,
        "statistics_lift": {
            k: float(prior_risk[k] - stats_risk[k]) for k in prior_risk
        },
        "mutual_information_verdict_vs_statistics_bits": cmi_stats,
        "probe_statistics_part_risk": probe_ct_risk,
        "probe_full_risk": probe_full_risk,
        "probe_lift": {
            k: float(probe_ct_risk[k] - probe_full_risk[k]) for k in probe_ct_risk
        },
        "cmi_verdict_probe_given_statistics_bits": cmi_probe,
        "t137_null_risk": null_risk,
        "t137_null_lift": {
            k: float(probe_ct_risk[k] - null_risk[k]) for k in probe_ct_risk
        },
        "t137_null_cmi_bits": cmi_null,
    }


def statistics_distinguish_control() -> dict:
    """Vacuity control: the SAME statistics-typed functional family does
    distinguish another pair (pristine vs z_keeper), so the Leg-3 equality
    certificates are not vacuous."""
    cfg_a, cfg_b = (NAMED_CONFIGS[n] for n in VACUITY_PAIR)
    verdicts = {VACUITY_PAIR[0]: VERDICT_CAPABLE, VACUITY_PAIR[1]: VERDICT_INCAPABLE}
    joint: dict = {}
    for name, cfg in zip(VACUITY_PAIR, (cfg_a, cfg_b)):
        for s, prob in _full_z_distribution(cfg).items():
            joint[(name, s, "none")] = joint.get((name, s, "none"), 0.0) + 0.5 * prob
    risk = float(
        _bayes_risk(joint, verdicts, lambda r, a: r, CAPABILITY_LOSS_TABLES["zero_one"])
    )
    return {
        "pair": list(VACUITY_PAIR),
        "stats_max_diff": stats_max_diff(cfg_a, cfg_b),
        "zero_one_risk_from_statistics": risk,
        "zero_one_lift_from_statistics": float(0.5 - risk),
    }


def burn_null(profiles: dict) -> dict:
    """T393 B'-analog: a real, order-uncorrelated emission moves nothing.
    The burn configuration's profile equals pristine's exactly and its
    declared statistics equal pristine's exactly, while the emission itself
    is real (escape-register excitation probability 1 vs 0)."""
    key_p = "|".join(NAMED_CONFIGS["pristine"])
    key_b = "|".join(NAMED_CONFIGS["burn_emitter"])
    profile_diff = max(
        abs(profiles[key_p]["profile"][t] - profiles[key_b]["profile"][t])
        for t in TASK_NAMES
    )

    def excitation(cfg):
        p = np.abs(config_state(cfg)) ** 2
        return float(p.reshape(DIMS).sum(axis=(0, 1, 2, 4, 5))[1])

    return {
        "profile_max_diff_vs_pristine": float(profile_diff),
        "stats_max_diff_vs_pristine": stats_max_diff(
            NAMED_CONFIGS["pristine"], NAMED_CONFIGS["burn_emitter"]
        ),
        "excitation_probability_burn": excitation(NAMED_CONFIGS["burn_emitter"]),
        "excitation_probability_pristine": excitation(NAMED_CONFIGS["pristine"]),
    }


# --------------------------------------------------------------------------- #
# Guardrails: Q1D no-signalling (asserted numerically), R1 untouched
# --------------------------------------------------------------------------- #

def no_signalling_certificate() -> dict:
    """Q1D surface for this architecture, asserted numerically:
    (i) the declared R readout is exactly independent of the preparation
        phase (phi never appears in any Z probability);
    (ii) exactly independent of the escape-register writes (outside-region
        couplings cannot steer the declared readout) -- this is the equality
        certificate read as a no-signalling statement;
    (iii) exactly independent of the target-operation settings on the
        (c, r1, r2) marginal, while the target marginal DOES move (teeth).
    Disclosed: a single target traverses all operations; the asserted
    surface is non-steerability of the declared readout, not Bell-style
    spacelike independence."""
    # (i) phase independence of the declared readout
    max_phi_diff = 0.0
    for cfg in (NAMED_CONFIGS["pristine"], NAMED_CONFIGS["publisher"]):
        base = declared_readout(cfg)
        for pb in (1, 2):
            for phi in PHI_CERT:
                max_phi_diff = max(
                    max_phi_diff,
                    float(np.max(np.abs(declared_readout(cfg, phi, pb) - base))),
                )
    # (ii) escape-write independence at fixed in-region writes
    max_escape_diff = 0.0
    for r1w in ("none", "class_phase"):
        for r2w in R2_WRITES:
            bundles = [
                stats_bundle((r1w, r2w, ew)) for ew in E_WRITES
            ]
            for i in range(len(bundles)):
                for j in range(i + 1, len(bundles)):
                    max_escape_diff = max(
                        max_escape_diff,
                        float(np.max(np.abs(bundles[i] - bundles[j]))),
                    )
    # (iii) setting independence of the (c, r1, r2) marginal; teeth = at
    # least one setting change moves the target marginal substantially
    max_cr_diff = 0.0
    cfg = NAMED_CONFIGS["class_keeper"]
    cr_dists, t_dists = [], []
    for x in (0, 1):
        for y in (0, 1):
            ops = (
                A_CANON @ np.linalg.matrix_power(ry(SETTING_DELTA_A), x),
                B_CANON,
                C_CANON @ np.linalg.matrix_power(ry(SETTING_DELTA_C), y),
            )
            p = declared_readout(cfg, ops=ops)
            cr_dists.append(p.sum(axis=3))
            t_dists.append(p.sum(axis=(0, 1, 2)))
    for i in range(len(cr_dists)):
        for j in range(i + 1, len(cr_dists)):
            max_cr_diff = max(
                max_cr_diff, float(np.max(np.abs(cr_dists[i] - cr_dists[j])))
            )
    max_t_span = max(
        float(np.max(np.abs(t_dists[i] - t_dists[j])))
        for i in range(len(t_dists))
        for j in range(i + 1, len(t_dists))
    )
    return {
        "max_readout_diff_over_phase": max_phi_diff,
        "max_readout_diff_over_escape_writes": max_escape_diff,
        "max_c_r_marginal_diff_over_settings": max_cr_diff,
        "max_target_marginal_span_over_settings": float(max_t_span),
    }


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #

def run_analysis() -> dict:
    profiles = all_profiles()
    leg1 = leg1_analysis(profiles)
    certificates = certificate_analysis(profiles)
    leg2 = leg2_analysis(profiles)
    leg3 = leg3_analysis(profiles)
    return {
        "artifact": "T407-region-capability-no-go",
        "version": "v0.1",
        "conventions": {
            "subsystem_order": "(c, r1, r2, e1, e2, t) index-sorted, dims (3,2,2,2,2,2)",
            "region_R": [SUBSYSTEM_NAMES[k] for k in REGION],
            "outside": [SUBSYSTEM_NAMES[k] for k in OUTSIDE],
            "record_subregion": [SUBSYSTEM_NAMES[k] for k in RECORD],
            "orders": [order_label(p) for p in K3_ORDERS],
            "class_partition": "A-before-B (class_of = [0, 1, 0]), T395 canonical",
            "tasks": list(TASK_NAMES),
            "thresholds": {
                name: float(thr)
                for name, thr in zip(TASK_NAMES, TASK_THRESHOLDS)
            },
            "v_star_provenance": "V_STAR imported from T392/T393, unchanged",
            "menu": {
                "unitary_generators": list(MENU_GENERATOR_ORDER),
                "n_unitary_protocols": len(menu_protocols()),
                "measurement_settings": ["x".join(s) for s in MEASUREMENT_SETTINGS],
            },
            "config_family": "3 r1-writes x 2 r2-writes x 4 e-writes = 24, exhaustive",
            "cap_gap_min": CAP_GAP_MIN,
        },
        "named_configs": {k: "|".join(v) for k, v in NAMED_CONFIGS.items()},
        "profiles": profiles,
        "leg1": leg1,
        "certificates": certificates,
        "leg2": leg2,
        "leg3": leg3,
        "no_signalling": no_signalling_certificate(),
        "verdicts": {
            "leg1": LEG1_VERDICT,
            "leg2": LEG2_VERDICT,
            "leg3": LEG3_VERDICT,
        },
    }


if __name__ == "__main__":
    import json

    res = run_analysis()
    print(json.dumps(res, indent=2, default=float))
    print()
    print("=" * 72)
    print("SUMMARY -- T407 Region-Indexed Capability No-Go")
    print("=" * 72)
    l1, cert, l2, l3 = (
        res["leg1"],
        res["certificates"],
        res["leg2"],
        res["leg3"],
    )
    print(f"configurations / distinct profiles:   "
          f"{l1['n_configurations']} / {l1['distinct_profile_count']}")
    print(f"menu vs closed-form max residual:     "
          f"{l1['max_menu_vs_closed_form_residual']:.3e}")
    print(f"branch-sum vs gate-built max diff:    "
          f"{l1['cross_checks']['max_branch_sum_vs_gate_built_diff']:.3e}")
    print(f"zero undo legs / all certified:       "
          f"{cert['n_zero_legs']} / {cert['all_zero_legs_certified']}")
    worst_bound = max(
        z["channel_bound"] for z in cert["zero_legs"].values()
    )
    worst_cert = max(
        z["phi_independence_max_pairwise_diff"]
        for z in cert["zero_legs"].values()
    )
    print(f"  worst phi-independence diff:        {worst_cert:.3e}")
    print(f"  worst all-channel bound (< v*):     {worst_bound:.3e}")
    print(f"  pass-leg phi-dependence floor:      "
          f"{cert['pass_legs_phi_dependence_min']:.4f}")
    mc = cert["manufactured_coherence_null"]
    print(f"  manufactured coherence raw/locked:  "
          f"{mc['raw_normalized']:.3f} / {mc['locked']:.3e}")
    print(f"  haar spot check max (ceiling 0.05): "
          f"{cert['haar_spot_check']['max_locked_visibility']:.3e}")
    print("-" * 72)
    print(f"capability poset: n = {l2['n_profiles']}, "
          f"comparable pairs = {l2['relation_size']}, "
          f"incomparable pairs = {l2['n_incomparable_pairs']}")
    gp = l2["grid_product_structure"]
    print(f"  exact product order (undo x readout): "
          f"{gp['is_exact_product_order']} "
          f"({gp['n_undo_levels']} x {gp['n_readout_levels']} grid)")
    print(f"  order dimension (T394 checker):     {l2['order_dimension']}")
    sr = l2["scalar_refutation_exhaustive"]
    print(f"  weak orders scanned / reproducing:  "
          f"{sr['n_weak_orders_scanned']} / {sr['n_reproducing_scalars']}")
    tw = l2["trichotomy_witnesses"]["pristine_vs_publisher"]
    print(f"  trichotomy witness (pristine|publisher): "
          f"{tw['tasks_where_first_strictly_better']} vs "
          f"{tw['tasks_where_second_strictly_better']}")
    print("-" * 72)
    sp = l3["statistics_partition"]
    print(f"statistics classes (sizes):           {sp['class_sizes']} "
          f"(intra max {sp['max_intra_class_diff']:.1e}, "
          f"inter min {sp['min_inter_class_diff']:.3f})")
    print(f"flat class realizes all profiles:     "
          f"{l3['flat_class_realizes_all_profiles']} "
          f"({l3['n_profiles_realized_in_flat_class']} of "
          f"{l1['distinct_profile_count']})")
    fp = l3["featured_pair"]
    print(f"featured pair {fp['configs']}: stats diff = "
          f"{fp['stats_max_diff']:.1e}, gaps both directions "
          f"{fp['max_gap_each_direction']} (floor {CAP_GAP_MIN})")
    sc = l3["screening"]
    print(f"  I(V; declared readout):             "
          f"{sc['mutual_information_verdict_vs_statistics_bits']:.3e} bits")
    print(f"  probe lift (0-1 loss):              "
          f"{sc['probe_lift']['zero_one']:.4f}")
    print(f"  I(V; probe | probe statistics):     "
          f"{sc['cmi_verdict_probe_given_statistics_bits']:.4f} bits")
    print(f"  T137 downstream null lift/CMI:      "
          f"{sc['t137_null_lift']['zero_one']:.1e} / "
          f"{sc['t137_null_cmi_bits']:.1e}")
    vc = l3["vacuity_control"]
    print(f"  vacuity control {vc['pair']}: statistics lift "
          f"{vc['zero_one_lift_from_statistics']:.4f}")
    cp = l3["converse_pair"]
    print(f"  converse pair {cp['configs']}: profile diff "
          f"{cp['profile_max_diff']:.1e}, stats diff {cp['stats_max_diff']:.3f}")
    bn = l3["burn_null"]
    print(f"  burn null: profile diff {bn['profile_max_diff_vs_pristine']:.1e}, "
          f"stats diff {bn['stats_max_diff_vs_pristine']:.1e}, "
          f"excitation {bn['excitation_probability_burn']:.1f}")
    ns = res["no_signalling"]
    print(f"Q1D: readout diff over phase/escape:  "
          f"{ns['max_readout_diff_over_phase']:.1e} / "
          f"{ns['max_readout_diff_over_escape_writes']:.1e} "
          f"(setting teeth {ns['max_target_marginal_span_over_settings']:.3f})")
    print("-" * 72)
    print("VERDICTS")
    for k, v in res["verdicts"].items():
        print(f"[{k}] {v}")
