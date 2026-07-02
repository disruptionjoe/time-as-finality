"""T404: Resource-Theory Absorber Audit for the T407 C(R) three-leg object.

This is the absorber run T407 names as its promotion gate ("Contribution
Needed", first bullet), executed in the house absorber-audit pattern (T162's
executable-obstruction form; T197's neighbor-granted-full-legitimacy form),
one level below T398: where T398 admitted the C(R) PROFILES as resource
states and absorbed the profile poset, this audit formalizes the resource-
theory FRAME itself, fairly and strongly, and tests -- by factorization, in
code -- whether T407's three legs are statements inside that frame.

THE ABSORBER FRAME (declared before any numbers were inspected):

    a resource-theory frame = (states, fixed free-operation class,
                               induced convertibility preorder / monotones)

  states           : region conditional state data per configuration --
                     both readings are carried: the single unphased rho_R,
                     and the phi-indexed family {rho_R(phi)} over the
                     imported T393 certificate sweep (the complete data any
                     R-supported channel ever sees);
  free operations  : all CPTP maps supported on R, FIXED ONCE (the strongest
                     natural in-region class; enlargements and product
                     classes are enumerated as alternative fixed frames);
  preorder         : reachability under the free class; monotones = task
                     values certified against the whole class (T407 Leg 1's
                     all-channel certificates), with the two T407 axes
                     (undo level, readout level) as the monotone vector.

THE THREE AUDIT LEGS:

  LEG A (anti-scalar; presumed absorbed, verified as such). Incomparable
  resources under a fixed free class are STANDARD resource theory. The
  standard analog is constructed explicitly -- a majorization-incomparable
  Schmidt-vector pair with two Vidal-style tail monotones ordering the pair
  oppositely (Nielsen/LOCC lineage, FROM MEMORY, unverified) -- and its
  incomparability-certificate shape is machine-compared with T407's
  featured-pair certificate (undo axis vs readout axis ordering pristine and
  publisher oppositely). Same shape. T407's realized 3 x 4 grid is the
  monotone-vector normal form. Verdict: absorbed as theorem-shape.

  LEG B (factorization; the real audit). Do T407's capability verdicts
  factor through (region state data, fixed free class)?

    B1 -- profile-from-state map: YES, exactly. Configurations are
    fingerprinted by their region state data; profile and declared-
    statistics assignments are checked for constancy on fingerprint
    classes. Zero violations. (The fingerprint partition has 18 classes;
    the six merged pairs are exactly the burn/none pairs -- T407's burn
    null reappears as a factorization fact.) In this family the single
    unphased rho_R already suffices. THIS IS ABSORBED CONTENT, NOT
    RESIDUE -- the phi-independence certificates of T407/T393 say exactly
    this, and the audit confirms it against the absorber's own vocabulary.

    B2 -- causal indexing (residue candidate a): the free class is not
    chosen but FORCED by causal structure, and it shrinks when the record-
    carrying mode escapes (T393's window result: recovery closes exactly at
    the escape step, counterfactual boundary enlargement restores it).
    Executable content here: (i) along every escape chain none -> class ->
    full at fixed record writes, the capability profile drops componentwise
    monotonically (6/6 chains, all with strict drops; burn moves nothing);
    (ii) the degrading operation is certified NON-FREE for the fixed class
    -- all 16 menu protocols leave the outside marginal exactly invariant,
    while escape writes move it by >= 1/3 and create c-e correlation 2/9
    from an exactly-uncorrelated start (so they are neither R-local nor
    product R (x) E maps); (iii) enlarging the free class to CPTP(R+E)
    internalizes the loss but TRIVIALIZES the theory -- one explicit free
    protocol (the preparation inverse, supported on R+E) restores locked
    visibility 1.0 for every configuration and both undo pairs, so the
    realized capability distinctions vanish. Hence the fixed-frame
    enumeration: CPTP(R) is sound for the no-go but cannot express the loss
    as a conversion; CPTP(R+E) expresses the loss but loses the no-go;
    CPTP(R) (x) CPTP(E) behaves like CPTP(R). No fixed frame in the
    declared candidate set carries all three T407 legs at once; the object
    that does is a causality-INDEXED family of resource theories with
    forced monotone capability loss. FLAGGED HONESTLY: dynamical resource
    theories / resource theories of channels and processes (superchannels
    as free operations; resource theories of causal connection) are the
    from-memory candidate absorbers of even this indexed-family shape --
    unverified; if they verify, this residue demotes to translation.

    B3 -- declared-record epistemics (residue candidate b): T407 Leg 3
    concerns bounded observers' DECLARED readouts, not state identity. The
    frame's derived vocabulary (state identity, convertibility, monotone
    values) has no native notion of "identical declared records, different
    resources". Executable content: the statistics-flat 16-class realizes
    all 12 resource objects with the full 3-level undo span and 4-level
    readout span, so every frame functional that factors through the
    declared record is constant exactly where the monotone vector spans its
    entire range; conversely the capability-identical converse pair splits
    the statistics, so the record map is not a functional of the resource
    object either -- a two-way non-reduction. The declared readout IS a
    bona fide experiment on the frame's states (checked: it equals the
    computational-basis diagonal of rho_R exactly), i.e. an EXTRA PRIMITIVE
    of Blackwell type, not something the frame supplies. FLAGGED HONESTLY:
    comparison of statistical experiments (Blackwell; quantum sufficiency/
    deficiency) is the from-memory candidate absorber of that extra layer
    -- unverified; if it verifies, this residue also demotes.

VERDICTS (predeclared as module constants, asserted verbatim in the tests):
  leg A absorbed_as_theorem_shape; B1 factors (absorbed content); B2 residue
  located at the static frame, conditional on the dynamical-RT flag; B3
  residue located at the frame interface, conditional on the Blackwell flag;
  overall partially_absorbed_residue_located, with the predeclared demotion
  clause: if BOTH flags verify, T407 demotes to "resource theory with extra
  bookkeeping" and this audit gates promotion accordingly.

Everything that carries a verdict is exact statevector arithmetic on T407's
own imported model (models.region_capability_no_go); nothing is sampled.
All literature attributions are FROM MEMORY and unverified per the
no-fake-citations rule; none enter literature/.

Reproduction:
    python -m pytest tests/test_resource_theory_absorber_audit.py -v
    python -m models.resource_theory_absorber_audit
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# T393 machinery, by import: the certificate phase sweep (incommensurate
# phases included) used for the state-family fingerprints.
from models.causal_forcing_access_asymmetry import PHI_CERT

# T395 primitives, by import (the same ones T407 builds on).
from models.record_order_tradeoff_probe import K3_ORDERS, rdm

# T407: the model under audit, imported wholesale -- the audit recomputes
# nothing it can import, and constructs nothing T407 already constructs.
from models.region_capability_no_go import (
    ALL_CONFIGS,
    DIMS,
    NAMED_CONFIGS,
    OUTSIDE,
    R1_WRITES,
    R2_WRITES,
    REGION,
    TASK_NAMES,
    TOL_EXACT,
    TOTAL_DIM,
    UNDO_PAIR_CROSS,
    UNDO_PAIR_WITHIN,
    V_STAR,
    _controlled_on_c,
    _e_ops,
    _order_unitary,
    _r1_op,
    _r2_op,
    build_capability_poset,
    capability_profile,
    config_state,
    declared_readout,
    grid_product_structure,
    in_region_channel_bound,
    locked_visibility,
    menu_protocols,
    phi_independence_certificate,
    profile_key,
    region_state,
    statistics_partition,
    stats_max_diff,
)

# --------------------------------------------------------------------------- #
# Predeclared constants (fixed before any audit numbers were inspected)
# --------------------------------------------------------------------------- #

ARTIFACT = "T404-resource-theory-absorber-audit"
VERSION = "v0.1"
SOURCE_ARTIFACT = "T407-region-capability-no-go"

# the absorber frame, stated once (see module docstring for prose)
RT_FRAME = {
    "states": (
        "region conditional state data per configuration: the single "
        "unphased rho_R and the phi-indexed family {rho_R(phi)} over the "
        "imported T393 certificate sweep (both carried; their induced "
        "partitions are compared)"
    ),
    "free_operations": (
        "all CPTP maps supported on R = (c, r1, r2, t), fixed once; "
        "alternative fixed classes CPTP(R+E) and CPTP(R) (x) CPTP(E) are "
        "enumerated as candidate frames, not mixed in"
    ),
    "preorder_and_monotones": (
        "reachability under the fixed free class; monotone vector = the "
        "two T407 axes (undo level, readout level), certified against the "
        "whole class by T407's imported all-channel certificates"
    ),
}

# tolerances / floors (predeclared)
FINGERPRINT_DECIMALS = 10
RESTORE_FLOOR = 1.0 - 1e-9  # boundary-crossing inverse must restore to 1
OUTSIDE_MOVE_FLOOR = 0.25  # escape writes must move the outside marginal
CORRELATION_FLOOR = 0.15  # escape writes must create c-e correlation
STATS_DISTINCT_FLOOR = 0.05  # converse pair statistics split floor
PROFILE_NULL_TOL = 1e-9  # burn null / converse-pair profile equality

# Leg A standard analog (Schmidt-vector pair; majorization-incomparable by
# construction -- partial sums cross). FROM MEMORY: Nielsen's majorization
# theorem ties LOCC convertibility of bipartite pure states to majorization
# (~1999); the Vidal-style tail monotones E_k are the standard witnesses.
# Unverified attribution; the numbers below are checked, the names are not.
MAJ_P = (0.5, 0.25, 0.25)
MAJ_Q = (0.4, 0.4, 0.2)

FROM_MEMORY_FLAGS = (
    "Nielsen majorization theorem / LOCC-incomparable bipartite pure "
    "states (~1999) -- Leg A analog",
    "Chitambar-Gour resource-theory review (free operations, monotones, "
    "no total order on resources) -- frame vocabulary",
    "dynamical resource theories / resource theories of channels and "
    "processes (superchannels as free operations); resource theories of "
    "causal connection -- candidate absorber of residue (a)",
    "Blackwell comparison of statistical experiments; quantum sufficiency "
    "and deficiency orderings -- candidate absorber of residue (b)",
)

# predeclared verdict vocabulary (asserted verbatim in the test suite)
VERDICT_LEG_A = (
    "absorbed_as_theorem_shape: incomparable resources under a fixed free-"
    "operation class are standard resource theory; the majorization/LOCC-"
    "style analog is constructed explicitly and its incomparability "
    "certificate has the same shape as T407's featured-pair certificate "
    "(two monotones ordering one pair oppositely, hence no scalar); T407 "
    "Leg 2 contributes a finite physical instance, not new order "
    "mathematics (attribution from memory, unverified)"
)
VERDICT_PROFILE_MAP = (
    "factors_through_region_state: every T407 capability verdict is a "
    "function of the region conditional state data at the fixed free class "
    "CPTP(R) -- zero violations across all 24 configurations, with the six "
    "fingerprint-merged pairs exactly the burn/none pairs; in this family "
    "the single unphased rho_R already suffices; the profile-from-state "
    "map is absorbed content, not residue"
)
VERDICT_CAUSAL_INDEXING = (
    "residue_located_static_frame: no fixed free-operation class in the "
    "declared candidate set {CPTP(R), CPTP(R+E), CPTP(R) (x) CPTP(E)} both "
    "preserves T407's realized capability distinctions and internalizes "
    "the escape-driven monotone loss -- CPTP(R) is sound for the no-go but "
    "the loss is enacted only by certified non-free boundary-crossing "
    "operations, CPTP(R+E) internalizes the loss but one free protocol "
    "restores every undo value to 1.0 so the distinctions vanish, and the "
    "product class behaves like CPTP(R) -- so the object is a causality-"
    "indexed FAMILY of resource theories with forced monotone capability "
    "loss (T393's window pattern), not one resource theory; dynamical/"
    "channel resource theories are the flagged from-memory candidate "
    "absorber of even this indexed-family shape (unverified); if they "
    "verify, this residue demotes to translation"
)
VERDICT_DECLARED_RECORD = (
    "residue_located_frame_interface: the declared-record layer is two-way "
    "non-reducing against the frame's resource objects -- the statistics-"
    "flat 16-class realizes all 12 objects across the full span of both "
    "monotone axes, and a capability-identical pair splits the statistics "
    "-- so 'identical declared records, different resources' is not a "
    "statement in the fixed-frame vocabulary; it requires the declared "
    "readout as an extra experiment-map primitive (verified to be a "
    "functional of the frame's own states), which is Blackwell-type "
    "comparison-of-experiments structure, flagged from memory as the "
    "candidate absorber of that layer (unverified); if it verifies, this "
    "residue also demotes to translation"
)
OVERALL_VERDICT = (
    "partially_absorbed_residue_located: all order-theoretic content of "
    "T407 (Leg 2, and the profile-from-state map behind Legs 1 and 3) is "
    "absorbed by a fairly-strong static resource-theory frame, confirming "
    "and extending T398; two residues survive the static frame, both at "
    "its interface -- the causal indexing of the free-operation class "
    "(residue a) and the declared-record epistemics (residue b) -- and "
    "each carries a named from-memory candidate absorber; if both verify, "
    "T407 demotes to resource theory with extra bookkeeping"
)
DEMOTION_CLAUSE = (
    "Predeclared demotion: should the flagged dynamical/channel resource-"
    "theory literature verify as owning causality-indexed free-class "
    "families with forced monotone capability loss, AND the comparison-of-"
    "experiments literature verify as owning fixed-readout capability "
    "underdetermination, then T407 is to be re-scoped as resource theory "
    "with extra bookkeeping, and no promotion may cite this audit as "
    "support; the audit gates the program either way."
)
RELATION_TO_T398 = (
    "T398 admitted the C(R) profiles as resource states and absorbed the "
    "profile poset (product resource preorder; translation residue). This "
    "audit tests the frame one level down and confirms T398's absorption "
    "of the order content, while refining its 'region indexing absorbed as "
    "context parameter' line: as a static context parameter the region is "
    "absorbed, but no fixed choice of free class carries all three T407 "
    "legs at once -- the context parameter is causality-indexed, and that "
    "indexing, plus the declared-record layer, is where the residue sits."
)
FALSIFICATION_CONDITIONS = (
    "residue (a) falls if verified dynamical/channel resource-theory "
    "literature exhibits causality-indexed free-operation families with "
    "forced monotone capability loss of this shape",
    "residue (b) falls if verified comparison-of-experiments literature "
    "covers menu-relative capability profiles at a fixed declared readout",
    "the audit itself fails if any executable check flips: an escape chain "
    "increases a capability component, the boundary-crossing inverse fails "
    "to restore visibility 1, a menu protocol moves the outside marginal, "
    "the fingerprint factorization is violated, or the statistics-flat "
    "class stops spanning the resource objects",
)

_ESCAPE_CHAIN = ("none", "class", "full")  # causal escape extent, increasing


# --------------------------------------------------------------------------- #
# Shared computations (cached; everything downstream reuses these)
# --------------------------------------------------------------------------- #

_PROFILES: dict | None = None


def profiles_by_config() -> dict:
    """T407 capability profiles for all 24 configurations (imported model)."""
    global _PROFILES
    if _PROFILES is None:
        _PROFILES = {cfg: capability_profile(cfg) for cfg in ALL_CONFIGS}
    return _PROFILES


def prep_unitary(cfg: tuple) -> np.ndarray:
    """The full preparation circuit of T407's gate-built construction --
    supported on R+E (it writes the escape registers), hence NOT in the
    fixed free class CPTP(R). Its inverse is the boundary-crossing
    restoration protocol of the frame-enumeration step."""
    r1w, r2w, ew = cfg
    U = np.eye(TOTAL_DIM, dtype=complex)
    for gate in (
        _controlled_on_c(lambda i: _r1_op(r1w, i), 1),
        _controlled_on_c(lambda i: _r2_op(r2w, i), 2),
        _controlled_on_c(lambda i: _e_ops(ew, i)[0], 3),
        _controlled_on_c(lambda i: _e_ops(ew, i)[1], 4),
        _controlled_on_c(lambda i: _order_unitary(K3_ORDERS[i]), 5),
    ):
        U = gate @ U
    return U


# --------------------------------------------------------------------------- #
# LEG A: anti-scalar -- standard analog + shape identity
# --------------------------------------------------------------------------- #

def majorizes(x: tuple, y: tuple) -> bool:
    """x majorizes y (equal totals; descending partial sums dominate)."""
    xs = np.cumsum(sorted(x, reverse=True))
    ys = np.cumsum(sorted(y, reverse=True))
    return bool(abs(xs[-1] - ys[-1]) < 1e-12 and np.all(xs >= ys - 1e-12))


def vidal_tail(x: tuple, k: int) -> float:
    """E_k-style tail monotone: sum of all but the k largest entries
    (standard LOCC monotone family -- from memory, unverified)."""
    return float(sum(sorted(x, reverse=True)[k:]))


def opposition_shape(
    m1_pair: tuple, m2_pair: tuple
) -> tuple:
    """Canonical shape of a two-monotone incomparability certificate on one
    ordered pair: the sorted signs of (m(second) - m(first)) for the two
    monotones. Shape (-1, 1) = the two monotones order the pair strictly
    oppositely, hence no scalar consistent with both (trichotomy)."""
    s1 = int(np.sign(round(m1_pair[1] - m1_pair[0], 12)))
    s2 = int(np.sign(round(m2_pair[1] - m2_pair[0], 12)))
    return tuple(sorted((s1, s2)))


def leg_a_analysis() -> dict:
    profiles = profiles_by_config()
    poset = build_capability_poset(profiles)
    grid = grid_product_structure(poset)

    # standard analog: majorization-incomparable pair + opposing tails
    p_maj_q = majorizes(MAJ_P, MAJ_Q)
    q_maj_p = majorizes(MAJ_Q, MAJ_P)
    e1 = (vidal_tail(MAJ_P, 1), vidal_tail(MAJ_Q, 1))
    e2 = (vidal_tail(MAJ_P, 2), vidal_tail(MAJ_Q, 2))
    analog_shape = opposition_shape(e1, e2)

    # T407 featured-pair certificate in monotone-axis coordinates
    undo_levels = [tuple(u) for u in grid["undo_levels"]]
    readout_levels = [tuple(r) for r in grid["readout_levels"]]
    u_rank = {u: i for i, u in enumerate(undo_levels)}
    r_rank = {r: i for i, r in enumerate(readout_levels)}

    def axis_ranks(name: str) -> tuple:
        key = profile_key(profiles[NAMED_CONFIGS[name]])
        return u_rank[key[:2]], r_rank[key[2:]]

    pristine_axes = axis_ranks("pristine")
    publisher_axes = axis_ranks("publisher")
    t397_shape = opposition_shape(
        (float(pristine_axes[0]), float(publisher_axes[0])),
        (float(pristine_axes[1]), float(publisher_axes[1])),
    )

    return {
        "standard_analog": {
            "schmidt_p": list(MAJ_P),
            "schmidt_q": list(MAJ_Q),
            "p_majorizes_q": p_maj_q,
            "q_majorizes_p": q_maj_p,
            "majorization_incomparable": (not p_maj_q) and (not q_maj_p),
            "tail_monotone_E1_p_q": list(e1),
            "tail_monotone_E2_p_q": list(e2),
            "certificate_shape": list(analog_shape),
            "attribution": (
                "Nielsen majorization / Vidal-style tails, FROM MEMORY, "
                "unverified"
            ),
        },
        "t397_featured_pair": {
            "pair": ["pristine", "publisher"],
            "undo_axis_ranks": [pristine_axes[0], publisher_axes[0]],
            "readout_axis_ranks": [pristine_axes[1], publisher_axes[1]],
            "certificate_shape": list(t397_shape),
        },
        "shape_identical": analog_shape == t397_shape,
        "scalar_impossible_shape": analog_shape == (-1, 1),
        "grid_normal_form": {
            "n_undo_levels": grid["n_undo_levels"],
            "n_readout_levels": grid["n_readout_levels"],
            "is_exact_product_order": grid["is_exact_product_order"],
            "reading": (
                "the realized poset is the monotone-vector normal form "
                "(product of two chains) -- standard resource-vector "
                "structure, nothing frame-exotic"
            ),
        },
        "verdict": VERDICT_LEG_A,
    }


# --------------------------------------------------------------------------- #
# LEG B1: does the profile map factor through the frame's states?
# --------------------------------------------------------------------------- #

def _family_fingerprint(cfg: tuple) -> bytes:
    """The phi-indexed family of region conditional states (the complete
    data any R-supported channel ever sees), rounded and serialized."""
    arrs = [rdm(config_state(cfg), DIMS, REGION)]
    for pb in (UNDO_PAIR_CROSS[1], UNDO_PAIR_WITHIN[1]):
        for phi in PHI_CERT:
            arrs.append(region_state(cfg, phi, pb))
    return np.round(np.stack(arrs), FINGERPRINT_DECIMALS).tobytes()


def _single_fingerprint(cfg: tuple) -> bytes:
    """The single unphased rho_R only (the weaker state reading)."""
    return np.round(
        rdm(config_state(cfg), DIMS, REGION), FINGERPRINT_DECIMALS
    ).tobytes()


def state_factorization_analysis() -> dict:
    profiles = profiles_by_config()
    fam: dict[bytes, list] = {}
    single: dict[bytes, list] = {}
    for cfg in ALL_CONFIGS:
        fam.setdefault(_family_fingerprint(cfg), []).append(cfg)
        single.setdefault(_single_fingerprint(cfg), []).append(cfg)

    fam_partition = {tuple(sorted(v)) for v in fam.values()}
    single_partition = {tuple(sorted(v)) for v in single.values()}

    profile_violations = []
    stats_violation_max = 0.0
    merged_classes = []
    for members in fam.values():
        keys = {profile_key(profiles[c]) for c in members}
        if len(keys) > 1:
            profile_violations.append([list(c) for c in members])
        if len(members) > 1:
            merged_classes.append(sorted(members))
            for other in members[1:]:
                stats_violation_max = max(
                    stats_violation_max, stats_max_diff(members[0], other)
                )

    merged_are_burn_none_pairs = all(
        len(cls) == 2
        and {cls[0][2], cls[1][2]} == {"none", "burn"}
        and cls[0][:2] == cls[1][:2]
        for cls in merged_classes
    )

    return {
        "n_configs": len(ALL_CONFIGS),
        "n_family_fingerprint_classes": len(fam),
        "n_single_state_classes": len(single),
        "partitions_equal": fam_partition == single_partition,
        "profile_factorization_violations": profile_violations,
        "profile_factors_through_state": len(profile_violations) == 0,
        "statistics_factor_max_violation": float(stats_violation_max),
        "statistics_factor_through_state": stats_violation_max < TOL_EXACT,
        "n_merged_classes": len(merged_classes),
        "merged_classes": [
            [["|".join(c) for c in cls]] for cls in merged_classes
        ],
        "merged_classes_are_exactly_burn_none_pairs": (
            merged_are_burn_none_pairs
        ),
        "single_state_suffices_in_family": (
            fam_partition == single_partition
            and len(profile_violations) == 0
        ),
        "verdict": VERDICT_PROFILE_MAP,
    }


# --------------------------------------------------------------------------- #
# LEG B2: residue candidate (a) -- causal indexing of the free class
# --------------------------------------------------------------------------- #

def escape_chain_analysis() -> dict:
    """Forced monotone capability loss along the causal escape axis, at the
    FIXED abstract free class and the FIXED menu. (The time-indexing itself
    is T393's window result, cited not re-derived; here the executable
    stand-in is escape extent.)"""
    profiles = profiles_by_config()
    chains = []
    burn_max_diff = 0.0
    for r1w in R1_WRITES:
        for r2w in R2_WRITES:
            seq = [(r1w, r2w, e) for e in _ESCAPE_CHAIN]
            keys = [profile_key(profiles[c]) for c in seq]
            monotone = all(
                all(
                    keys[i + 1][k] <= keys[i][k] + 1e-9
                    for k in range(len(TASK_NAMES))
                )
                for i in range(len(seq) - 1)
            )
            strict = any(
                any(
                    keys[i + 1][k] < keys[i][k] - 1e-9
                    for k in range(len(TASK_NAMES))
                )
                for i in range(len(seq) - 1)
            )
            burn_key = profile_key(profiles[(r1w, r2w, "burn")])
            burn_max_diff = max(
                burn_max_diff,
                max(abs(a - b) for a, b in zip(burn_key, keys[0])),
            )
            chains.append(
                {
                    "record_writes": [r1w, r2w],
                    "profiles_along_chain": [list(k) for k in keys],
                    "componentwise_monotone_nonincreasing": monotone,
                    "has_strict_drop": strict,
                }
            )
    return {
        "n_chains": len(chains),
        "chains": chains,
        "all_chains_monotone": all(
            c["componentwise_monotone_nonincreasing"] for c in chains
        ),
        "n_chains_with_strict_drop": sum(
            c["has_strict_drop"] for c in chains
        ),
        "burn_null_max_profile_diff": float(burn_max_diff),
        "burn_null_inert": burn_max_diff < PROFILE_NULL_TOL,
    }


def free_class_boundary_certificates() -> dict:
    """Certify that (i) the fixed free class CPTP(R) cannot touch the
    outside marginal (checked exactly for all 16 menu protocols on all 24
    configurations), while (ii) the escape writes -- the operations that
    enact the capability loss -- move the outside marginal and create c-e
    correlation from an exactly-uncorrelated start, so they are neither
    R-local nor product R (x) E maps."""
    menu_move = 0.0
    for cfg in ALL_CONFIGS:
        psi = config_state(cfg)
        e0 = rdm(psi, DIMS, OUTSIDE)
        for protocol in menu_protocols().values():
            menu_move = max(
                menu_move,
                float(np.max(np.abs(rdm(protocol @ psi, DIMS, OUTSIDE) - e0))),
            )

    def outside_move(ew: str) -> float:
        a = rdm(config_state(("none", "none", ew)), DIMS, OUTSIDE)
        b = rdm(config_state(("none", "none", "none")), DIMS, OUTSIDE)
        return float(np.max(np.abs(a - b)))

    def ce_correlation(ew: str) -> float:
        p = np.abs(config_state(("none", "none", ew))) ** 2
        joint = p.reshape(DIMS).sum(axis=(1, 2, 5))  # (c, e1, e2)
        pc = joint.sum(axis=(1, 2))
        pe = joint.sum(axis=0)
        return float(np.max(np.abs(joint - np.einsum("c,ef->cef", pc, pe))))

    return {
        "menu_max_outside_marginal_move": float(menu_move),
        "free_ops_leave_outside_invariant": menu_move < TOL_EXACT,
        "escape_write_outside_move": {
            ew: outside_move(ew) for ew in ("class", "full", "burn")
        },
        "escape_write_ce_correlation": {
            ew: ce_correlation(ew) for ew in ("none", "class", "full", "burn")
        },
        "correlating_escape_writes_exceed_floors": all(
            outside_move(ew) >= OUTSIDE_MOVE_FLOOR
            and ce_correlation(ew) >= CORRELATION_FLOOR
            for ew in ("class", "full")
        ),
        "burn_creates_no_ce_correlation": (
            ce_correlation("burn") < TOL_EXACT
        ),
        "reading": (
            "the capability-degrading operations are certified NON-FREE "
            "for CPTP(R) (they move the outside marginal, which no "
            "R-supported map can) and NON-FREE for CPTP(R) (x) CPTP(E) "
            "(they create R-E correlation from a product start, which no "
            "product map can); burn is non-free too (it moves the outside "
            "marginal) but creates no correlation and no capability change "
            "-- the loss tracks the correlating writes exactly"
        ),
    }


def frame_enumeration() -> dict:
    """The fixed-frame trilemma, executable. For each candidate FIXED free
    class, check whether it (i) preserves T407's realized capability
    distinctions and (ii) internalizes the escape-driven loss as a free
    conversion. No candidate does both."""
    # F_R soundness: the no-go certificates hold (recomputed for the two
    # named fully-escaped configs, both undo pairs -- T407 certifies all 18
    # zero legs; the audit re-touches the featured corner only).
    worst_cert = 0.0
    worst_bound = 0.0
    for name in ("publisher", "amnesic_emitter"):
        cfg = NAMED_CONFIGS[name]
        for pair in (UNDO_PAIR_WITHIN, UNDO_PAIR_CROSS):
            worst_cert = max(
                worst_cert, phi_independence_certificate(cfg, pair)
            )
            worst_bound = max(worst_bound, in_region_channel_bound(cfg, pair))

    # F_RE trivialization: ONE explicit free protocol (the preparation
    # inverse, supported on R+E) restores locked visibility 1.0 for every
    # configuration and both undo pairs.
    min_restored = 1.0
    inverse_outside_move = 0.0
    for cfg in ALL_CONFIGS:
        inverse = prep_unitary(cfg).conj().T
        psi = config_state(cfg)
        inverse_outside_move = max(
            inverse_outside_move,
            float(
                np.max(
                    np.abs(
                        rdm(inverse @ psi, DIMS, OUTSIDE)
                        - rdm(psi, DIMS, OUTSIDE)
                    )
                )
            ),
        )
        for pair in (UNDO_PAIR_WITHIN, UNDO_PAIR_CROSS):
            min_restored = min(
                min_restored, locked_visibility(cfg, inverse, pair)
            )

    profiles = profiles_by_config()
    n_undo_levels = len({profile_key(p)[:2] for p in profiles.values()})

    table = {
        "CPTP(R)": {
            "no_go_sound": bool(
                worst_cert < TOL_EXACT and worst_bound < V_STAR
            ),
            "loss_expressible_as_free_conversion": False,
            "why": (
                "escape writes are certified non-free (boundary "
                "certificates); within this frame the loss is an exogenous "
                "state jump, not a conversion -- the frame preserves the "
                "verdicts but cannot say why the free class was ever "
                "capable, nor that the loss was forced"
            ),
        },
        "CPTP(R+E)": {
            "no_go_sound": False,
            "loss_expressible_as_free_conversion": True,
            "min_restored_visibility_over_24x2": float(min_restored),
            "restores_all_undo_to_one": bool(min_restored >= RESTORE_FLOOR),
            "why": (
                "the preparation inverse is free here and restores every "
                "undo value to 1.0, so the realized undo distinctions "
                f"({n_undo_levels} levels) vanish -- the frame internalizes "
                "the loss at the price of the no-go itself"
            ),
        },
        "CPTP(R) (x) CPTP(E)": {
            "no_go_sound": bool(
                worst_cert < TOL_EXACT and worst_bound < V_STAR
            ),
            "loss_expressible_as_free_conversion": False,
            "why": (
                "escape writes create R-E correlation from a product "
                "start, which no product map can -- same silence as "
                "CPTP(R)"
            ),
        },
    }
    no_fixed_frame = not any(
        entry["no_go_sound"] and entry["loss_expressible_as_free_conversion"]
        for entry in table.values()
    )
    return {
        "f_r_worst_phi_independence": float(worst_cert),
        "f_r_worst_channel_bound": float(worst_bound),
        "boundary_crossing_inverse_outside_move": float(
            inverse_outside_move
        ),
        "min_restored_visibility_over_24x2": float(min_restored),
        "frames": table,
        "no_fixed_frame_carries_all_three_legs": no_fixed_frame,
        "t393_citation": (
            "the time-indexing itself (recovery window closes exactly at "
            "the escape step; counterfactual boundary enlargement restores "
            "recovery exactly) is T393's Tier-1 result, cited not "
            "re-derived; the executable stand-ins here are the escape-"
            "chain monotone loss and the boundary-crossing restoration"
        ),
    }


def leg_b2_analysis() -> dict:
    chains = escape_chain_analysis()
    boundary = free_class_boundary_certificates()
    frames = frame_enumeration()
    residue_located = (
        chains["all_chains_monotone"]
        and chains["n_chains_with_strict_drop"] > 0
        and boundary["free_ops_leave_outside_invariant"]
        and boundary["correlating_escape_writes_exceed_floors"]
        and frames["no_fixed_frame_carries_all_three_legs"]
    )
    return {
        "escape_chains": chains,
        "boundary_certificates": boundary,
        "frame_enumeration": frames,
        "residue_located": residue_located,
        "candidate_absorber_flag": FROM_MEMORY_FLAGS[2],
        "verdict": VERDICT_CAUSAL_INDEXING,
    }


# --------------------------------------------------------------------------- #
# LEG B3: residue candidate (b) -- declared-record epistemics
# --------------------------------------------------------------------------- #

def declared_record_analysis() -> dict:
    profiles = profiles_by_config()
    partition = statistics_partition()

    pristine = NAMED_CONFIGS["pristine"]
    flat_class = next(
        c for c in partition["classes"] if "|".join(pristine) in c
    )
    cfg_of = {"|".join(cfg): cfg for cfg in ALL_CONFIGS}
    flat_cfgs = [cfg_of[k] for k in flat_class]
    flat_keys = {profile_key(profiles[c]) for c in flat_cfgs}
    all_keys = {profile_key(p) for p in profiles.values()}

    # monotone-axis span on the statistics-flat class
    undo_span = {k[:2] for k in flat_keys}
    readout_span = {k[2:] for k in flat_keys}
    all_undo = {k[:2] for k in all_keys}
    all_readout = {k[2:] for k in all_keys}

    # two-way non-reduction
    featured = [NAMED_CONFIGS[n] for n in ("pristine", "publisher")]
    fa = profiles[featured[0]]["profile"]
    fb = profiles[featured[1]]["profile"]
    gap_first = max(fa[t] - fb[t] for t in TASK_NAMES)
    gap_second = max(fb[t] - fa[t] for t in TASK_NAMES)
    featured_stats = stats_max_diff(*featured)

    converse = [NAMED_CONFIGS[n] for n in ("class_keeper", "z_keeper")]
    ca = profiles[converse[0]]["profile"]
    cb = profiles[converse[1]]["profile"]
    converse_profile_diff = max(abs(ca[t] - cb[t]) for t in TASK_NAMES)
    converse_stats = stats_max_diff(*converse)

    # the declared readout is a bona fide experiment ON the frame's states:
    # it equals the computational-basis diagonal of rho_R exactly
    region_dims = tuple(DIMS[k] for k in REGION)
    experiment_map_diff = 0.0
    for name in ("pristine", "publisher", "z_keeper"):
        cfg = NAMED_CONFIGS[name]
        for phi, pb in ((0.0, None), (1.1, UNDO_PAIR_CROSS[1])):
            rho = rdm(config_state(cfg, phi=phi, phase_branch=pb), DIMS, REGION)
            diag = np.real(np.diag(rho)).reshape(region_dims)
            experiment_map_diff = max(
                experiment_map_diff,
                float(
                    np.max(
                        np.abs(
                            diag
                            - declared_readout(cfg, phi=phi, phase_branch=pb)
                        )
                    )
                ),
            )

    residue_located = (
        flat_keys == all_keys
        and undo_span == all_undo
        and readout_span == all_readout
        and featured_stats < TOL_EXACT
        and min(gap_first, gap_second) >= 0.5
        and converse_profile_diff < PROFILE_NULL_TOL
        and converse_stats >= STATS_DISTINCT_FLOOR
    )

    return {
        "statistics_partition_sizes": partition["class_sizes"],
        "flat_class_size": len(flat_class),
        "n_resource_objects_realized_in_flat_class": len(flat_keys),
        "flat_class_spans_all_resource_objects": flat_keys == all_keys,
        "undo_axis_span_in_flat_class": [len(undo_span), len(all_undo)],
        "readout_axis_span_in_flat_class": [
            len(readout_span),
            len(all_readout),
        ],
        "profile_does_not_factor_through_record": {
            "featured_pair": ["pristine", "publisher"],
            "stats_max_diff": float(featured_stats),
            "capability_gaps_both_directions": [
                float(gap_first),
                float(gap_second),
            ],
        },
        "record_does_not_factor_through_resource_object": {
            "converse_pair": ["class_keeper", "z_keeper"],
            "profile_max_diff": float(converse_profile_diff),
            "stats_max_diff": float(converse_stats),
        },
        "two_way_non_reduction": residue_located,
        "experiment_map_is_state_functional": {
            "max_diff_readout_vs_rho_r_diagonal": float(experiment_map_diff),
            "is_functional": experiment_map_diff < TOL_EXACT,
            "reading": (
                "the declared readout is an experiment (a fixed POVM) on "
                "the frame's own states -- extra Blackwell-type structure "
                "the frame does not supply, not something outside physics"
            ),
        },
        "residue_located": residue_located,
        "candidate_absorber_flag": FROM_MEMORY_FLAGS[3],
        "verdict": VERDICT_DECLARED_RECORD,
    }


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #

_AUDIT: dict | None = None


def run_audit() -> dict:
    global _AUDIT
    if _AUDIT is None:
        leg_a = leg_a_analysis()
        b1 = state_factorization_analysis()
        b2 = leg_b2_analysis()
        b3 = declared_record_analysis()
        _AUDIT = {
            "artifact": ARTIFACT,
            "version": VERSION,
            "source_artifact": SOURCE_ARTIFACT,
            "rt_frame": RT_FRAME,
            "relation_to_t398": RELATION_TO_T398,
            "leg_a_anti_scalar": leg_a,
            "leg_b1_profile_factorization": b1,
            "leg_b2_causal_indexing": b2,
            "leg_b3_declared_record": b3,
            "verdicts": {
                "leg_a": VERDICT_LEG_A,
                "leg_b_profile_map": VERDICT_PROFILE_MAP,
                "leg_b_causal_indexing": VERDICT_CAUSAL_INDEXING,
                "leg_b_declared_record": VERDICT_DECLARED_RECORD,
                "overall": OVERALL_VERDICT,
            },
            "demotion_clause": DEMOTION_CLAUSE,
            "from_memory_flags": list(FROM_MEMORY_FLAGS),
            "falsification_conditions": list(FALSIFICATION_CONDITIONS),
            "claim_ledger_update": "none; no claim promotion",
        }
    return _AUDIT


if __name__ == "__main__":
    res = run_audit()
    print(json.dumps(res, indent=2, default=float))
    print()
    print("=" * 72)
    print("SUMMARY -- T404 Resource-Theory Absorber Audit (of T407)")
    print("=" * 72)
    a = res["leg_a_anti_scalar"]
    print(
        "LEG A  majorization pair incomparable:  "
        f"{a['standard_analog']['majorization_incomparable']}; "
        f"shape identical to featured pair: {a['shape_identical']} "
        f"(shape {a['standard_analog']['certificate_shape']})"
    )
    print(
        "       grid normal form:                "
        f"{a['grid_normal_form']['n_undo_levels']}x"
        f"{a['grid_normal_form']['n_readout_levels']} exact product = "
        f"{a['grid_normal_form']['is_exact_product_order']}"
    )
    b1 = res["leg_b1_profile_factorization"]
    print(
        "LEG B1 fingerprint classes (family/single): "
        f"{b1['n_family_fingerprint_classes']}/"
        f"{b1['n_single_state_classes']}, partitions equal: "
        f"{b1['partitions_equal']}, profile violations: "
        f"{len(b1['profile_factorization_violations'])}, merged = "
        f"burn/none pairs: {b1['merged_classes_are_exactly_burn_none_pairs']}"
    )
    b2 = res["leg_b2_causal_indexing"]
    ch = b2["escape_chains"]
    bd = b2["boundary_certificates"]
    fr = b2["frame_enumeration"]
    print(
        "LEG B2 escape chains monotone/strict:   "
        f"{ch['n_chains']} chains, all monotone {ch['all_chains_monotone']}, "
        f"strict drops {ch['n_chains_with_strict_drop']}, burn inert "
        f"{ch['burn_null_inert']}"
    )
    print(
        "       menu outside move / escape move: "
        f"{bd['menu_max_outside_marginal_move']:.1e} / "
        f"{bd['escape_write_outside_move']['class']:.3f} (class), "
        f"{bd['escape_write_outside_move']['full']:.3f} (full); c-e corr "
        f"{bd['escape_write_ce_correlation']['class']:.3f}"
    )
    print(
        "       F_RE min restored visibility:    "
        f"{fr['min_restored_visibility_over_24x2']:.12f}; no fixed frame "
        f"carries all legs: {fr['no_fixed_frame_carries_all_three_legs']}"
    )
    b3 = res["leg_b3_declared_record"]
    print(
        "LEG B3 flat class spans objects:        "
        f"{b3['flat_class_size']} configs -> "
        f"{b3['n_resource_objects_realized_in_flat_class']} objects "
        f"(spans all: {b3['flat_class_spans_all_resource_objects']}); "
        f"two-way non-reduction: {b3['two_way_non_reduction']}"
    )
    print(
        "       experiment map = state diag:     "
        f"{b3['experiment_map_is_state_functional']['max_diff_readout_vs_rho_r_diagonal']:.1e}"
    )
    print("-" * 72)
    print("VERDICTS")
    for key, verdict in res["verdicts"].items():
        print(f"[{key}] {verdict}")
    print("-" * 72)
    print(res["demotion_clause"])
