"""T424 - M2 Route-A Decisive Fiber-Variation Index Probe.

The decisive test of whether Route A (an index / cohomology reading) escapes the
relabel bar that capped T422 and killed T423-Route-B. T423 showed the two Route-B
descriptions collapsed to ONE majority primitive (`v_gap(S) == dilemma_indicator(S)`
as set functions). This probe asks, for three INDEPENDENT index channels, whether
each is merely a function of the `v_gap` set function (RELABEL -> Horn 2) or a
genuine independent channel that equals the finality separator across the class
(Horn 1 / GO).

Cross-domain material (combinatorial Hodge / index theory, judgment aggregation,
signed-graph balance theory) is the OBJECT OF STUDY, never evidence for physics or
a sibling repo. ONE-WAY RULE: GU / temporal-issuance / ai-epistemology /
architecture-of-legitimacy are adjacency / template / vocabulary only. The ONLY
code imports are TaF-native: T413 (`models.legitimacy_shapley_finality_probe`) and
T423 (`models.m2_observer_game`) -- the majority/verdict/gap machinery reused
verbatim.

Exact arithmetic (integer / fractions.Fraction / GF(2)) everywhere except the
spectral-flow channel I_sf (numpy eigvalsh, float, with a grid-refinement
determinism cross-check). Deterministic; n=3, 64 profiles per doctrine fully
enumerated. Run:

    python -m models.m2_route_a_index_probe
    python -m pytest tests/test_m2_route_a_index_probe.py -q
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import json

import numpy as np

# ---- ONLY imports: TaF-native T413 + T423 machinery -----------------------
from models.legitimacy_shapley_finality_probe import (
    all_subsets,
    joint_record_completion_verdict,
    shapley_by_dividends,
)
from models.m2_observer_game import (
    smaj,
    premise_verdict,
    conclusion_verdict,
    gap_value,
    moebius_dividends,
)

JUDGES = (1, 2, 3)

# Canonical coalition order (size, then sorted members) -- fixes the fiber label.
CANON_COALITIONS = tuple(
    sorted((tuple(sorted(S)) for S in all_subsets(JUDGES)), key=lambda t: (len(t), t))
)


# ---------------------------------------------------------------------------
# Doctrine family.  Each doctrine is a function used BOTH to derive r_i and as
# the premise-aggregation connective (so premise_verdict(S) = doc(maj p, maj q)).
# ---------------------------------------------------------------------------
def d_and(a, b):
    return 1 if (a and b) else 0


def d_or(a, b):
    return 1 if (a or b) else 0


def d_dict(a, b):
    return 1 if a else 0            # r = p (dictator on the first premise)


def d_noconn(a, b):
    return 0                        # no connection: r_i = 0, premise verdict 0


def d_xor(a, b):
    return 1 if (a != b) else 0     # r = p XOR q (non-trivial cohomology control)


DOCTRINES = {
    "AND": d_and,
    "OR": d_or,
    "DICT": d_dict,
    "NOCONN": d_noconn,
    "XOR": d_xor,
}


# ---------------------------------------------------------------------------
# Profiles.  A profile = ((p1,q1),(p2,q2),(p3,q3)); r derived from the doctrine
# so EVERY profile is individually consistent by construction.
# ---------------------------------------------------------------------------
def enumerate_profiles():
    """All 64 (p_i,q_i) assignments, in a fixed serial order (serial id 0..63)."""
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    profs = []
    for s1, s2, s3 in product(states, states, states):
        profs.append((s1, s2, s3))
    return profs


def columns(profile, doctrine):
    """Return the p, q, r columns (dicts keyed by judge id) for a profile."""
    p = {JUDGES[k]: profile[k][0] for k in range(3)}
    q = {JUDGES[k]: profile[k][1] for k in range(3)}
    r = {JUDGES[k]: doctrine(profile[k][0], profile[k][1]) for k in range(3)}
    return p, q, r


# ---------------------------------------------------------------------------
# Reference primitive: the v_gap set function -> fiber key.
# ---------------------------------------------------------------------------
def vgap_vector(profile, doctrine):
    """v_gap(S) over all 8 coalitions in canonical order (reuses T423 gap_value)."""
    p, q, r = columns(profile, doctrine)
    return tuple(int(gap_value(frozenset(S), p, q, r, doctrine)) for S in CANON_COALITIONS)


def fiber_key(profile, doctrine):
    """Canonical hash of the v_gap set function -- the relabel primitive."""
    return vgap_vector(profile, doctrine)


def finality_separator(profile, doctrine):
    """1 iff the gap game SURVIVES-R1 (the T413 grand-coalition finality datum)."""
    p, q, r = columns(profile, doctrine)
    div = moebius_dividends(lambda S: gap_value(S, p, q, r, doctrine), JUDGES)
    jrc = joint_record_completion_verdict(div, {}, players=JUDGES)
    return 1 if jrc.get("verdict") == "SURVIVES-R1" else 0


# ---------------------------------------------------------------------------
# Exact linear algebra helpers (integer/rational rank; GF(2) rank).
# ---------------------------------------------------------------------------
def rank_rational(rows):
    """Exact rank of an integer/rational matrix via Fraction Gaussian elimination.
    `rows` is a list of lists. Empty matrix -> rank 0."""
    M = [[F(x) for x in row] for row in rows]
    if not M or not M[0]:
        return 0
    nrows, ncols = len(M), len(M[0])
    rank = 0
    pcol = 0
    for pcol in range(ncols):
        piv = None
        for r in range(rank, nrows):
            if M[r][pcol] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pivval = M[rank][pcol]
        M[rank] = [x / pivval for x in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][pcol] != 0:
                factor = M[r][pcol]
                M[r] = [a - factor * b for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


def rank_gf2(rows):
    """Exact GF(2) rank (entries taken mod 2)."""
    M = [[int(x) % 2 for x in row] for row in rows]
    if not M or not M[0]:
        return 0
    nrows, ncols = len(M), len(M[0])
    rank = 0
    for pcol in range(ncols):
        piv = None
        for r in range(rank, nrows):
            if M[r][pcol]:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(nrows):
            if r != rank and M[r][pcol]:
                M[r] = [(a ^ b) for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


# ---------------------------------------------------------------------------
# Signed interaction structure (shared by I_fr and I_sf, and the complement by
# I_chi).  cross(i,j) iff judges i,j disagree on BOTH premises (antipodal states)
# -- a genuine pairwise interaction / cycle-product read, NOT a marginal.
# ---------------------------------------------------------------------------
EDGES = ((0, 1), (1, 2), (2, 0))     # triangle edges on judge indices 0,1,2
WRAP_EDGE_INDEX = 2                   # edge (2,0) carries the phase twist


def crosses(profile, i, j):
    (pi, qi), (pj, qj) = profile[i], profile[j]
    return (pi != pj) and (qi != qj)


def edge_sign(profile, i, j):
    """s_ij = -1 if i,j cross on both premises, else +1 (the interaction sign)."""
    return -1 if crosses(profile, i, j) else 1


# ---------------------------------------------------------------------------
# I_chi -- combinatorial-Hodge Euler characteristic of the premise-compatibility
# clique complex.
# ---------------------------------------------------------------------------
def compatibility_complex(profile):
    """Nodes = 3 judges. Edge {i,j} iff i,j do NOT cross (compatible). 2-cell iff
    all three edges present. Returns (C0, C1, C2) simplex lists."""
    C0 = [(0,), (1,), (2,)]
    C1 = [e for e in EDGES if edge_sign(profile, *e) == 1]
    all_three = len(C1) == 3
    C2 = [(0, 1, 2)] if all_three else []
    return C0, C1, C2


def boundary_d0(C0, C1):
    """d0: C1 -> C0 incidence, |C0| x |C1| (partial_1)."""
    idx = {v[0]: k for k, v in enumerate(C0)}
    M = [[0] * len(C1) for _ in C0]
    for c, (i, j) in enumerate(C1):
        M[idx[i]][c] += -1
        M[idx[j]][c] += 1
    return M


def boundary_d1(C1, C2):
    """d1: C2 -> C1 incidence, |C1| x |C2| (partial_2), oriented (i,j,k)."""
    eidx = {frozenset(e): k for k, e in enumerate(C1)}
    M = [[0] * len(C2) for _ in C1]
    for c, (i, j, k) in enumerate(C2):
        # boundary of (i,j,k) = (j,k) - (i,k) + (i,j)
        for (a, b), coeff in (((j, k), 1), ((i, k), -1), ((i, j), 1)):
            key = frozenset((a, b))
            if key in eidx:
                M[eidx[key]][c] += coeff
    return M


def i_chi(profile):
    """Euler characteristic chi = b0 - b1 + b2, with exact + GF(2) Betti numbers."""
    C0, C1, C2 = compatibility_complex(profile)
    d0 = boundary_d0(C0, C1)
    d1 = boundary_d1(C1, C2)
    r0 = rank_rational(d0)                 # rank partial_1
    r1 = rank_rational(d1)                 # rank partial_2
    b0 = len(C0) - r0
    b1 = len(C1) - r0 - r1
    b2 = len(C2) - r1
    chi_betti = b0 - b1 + b2
    chi_count = len(C0) - len(C1) + len(C2)
    # GF(2) cross-check of the Betti numbers
    r0_2 = rank_gf2(d0)
    r1_2 = rank_gf2(d1)
    b0_2 = len(C0) - r0_2
    b1_2 = len(C1) - r0_2 - r1_2
    b2_2 = len(C2) - r1_2
    gf2_ok = (b0_2, b1_2, b2_2) == (b0, b1, b2)
    return {
        "value": chi_count,
        "chi_betti": chi_betti,
        "chi_count": chi_count,
        "betti": (b0, b1, b2),
        "euler_consistent": chi_betti == chi_count,
        "gf2_betti_match": gf2_ok,
    }


# ---------------------------------------------------------------------------
# I_sf -- spectral flow of a twisted Hermitian Dirac on the judge triangle.
# ---------------------------------------------------------------------------
def _incidence(profile, theta, wrap_weight=1.0):
    """B(theta): 3x3 signed node-edge incidence of the judge triangle with a phase
    twist e^{i theta} on the wrap edge; wrap_weight opens the gap when > 1."""
    B = np.zeros((3, 3), dtype=complex)   # rows = nodes, cols = edges
    for c, (i, j) in enumerate(EDGES):
        s = edge_sign(profile, i, j)
        if c == WRAP_EDGE_INDEX:
            B[i, c] += -1.0
            B[j, c] += s * wrap_weight * np.exp(1j * theta)
        else:
            B[i, c] += -1.0
            B[j, c] += s
    return B


def _dirac(profile, theta, wrap_weight=1.0):
    """D(theta) = [[0, B],[B^dagger, 0]] Hermitian 6x6 (chiral)."""
    B = _incidence(profile, theta, wrap_weight)
    D = np.zeros((6, 6), dtype=complex)
    D[0:3, 3:6] = B
    D[3:6, 0:3] = B.conj().T
    return D


def _min_gap(profile, wrap_weight, nsteps):
    """Smallest |eigenvalue| of D(theta) over the theta loop (numpy eigvalsh)."""
    thetas = np.linspace(0.0, 2.0 * np.pi, nsteps, endpoint=False)
    return min(float(np.min(np.abs(np.linalg.eigvalsh(_dirac(profile, t, wrap_weight)))))
               for t in thetas)


def _det_winding(profile, wrap_weight, nsteps):
    """Winding number of theta -> det B(theta) about 0 (the APS/SSH spectral flow),
    computed by unwrapped phase accumulation over the closed theta loop."""
    thetas = np.linspace(0.0, 2.0 * np.pi, nsteps, endpoint=False)
    vals = [np.linalg.det(_incidence(profile, t, wrap_weight)) for t in thetas]
    vals.append(vals[0])                        # close the loop
    ang = np.unwrap(np.angle(np.array(vals)))
    return int(round((ang[-1] - ang[0]) / (2.0 * np.pi)))


def i_sf(profile):
    """Spectral-flow / APS-eta channel.  At n=3 the untwisted triangle Dirac is
    GAPLESS (det B(theta) = -1 + P*e^{i theta} passes through 0 for every profile),
    so the spectral flow is not robustly defined at the gapless point.  Under a
    gap-opening regularization (wrap_weight = 2) the winding becomes the reported,
    deterministic value; the gapless residue merely re-reads the triangle sign
    product P = the frustration cocycle -> NOT an independent channel."""
    P = edge_sign(profile, *EDGES[0]) * edge_sign(profile, *EDGES[1]) \
        * edge_sign(profile, *EDGES[2])
    gap_untwisted = _min_gap(profile, 1.0, 360)
    reg_wind_coarse = _det_winding(profile, 2.0, 360)
    reg_wind_fine = _det_winding(profile, 2.0, 720)
    return {
        "value": reg_wind_fine,                 # regularized spectral flow
        "coarse": reg_wind_coarse,
        "grid_stable": reg_wind_coarse == reg_wind_fine,
        "min_gap_untwisted": gap_untwisted,     # ~0 for all profiles -> gapless
        "gapless_at_n3": gap_untwisted < 1e-9,
        "gapless_residue_P": P,                 # equals the I_fr cocycle sign
    }


# ---------------------------------------------------------------------------
# I_fr -- signed-graph frustration index (the genuine loophole).
# ---------------------------------------------------------------------------
def i_fr(profile):
    """Frustration = min negative-edge count over all 2^3 gauge switches;
    GF(2) cross-check via the triangle sign product (cocycle class)."""
    signs = {e: edge_sign(profile, *e) for e in EDGES}
    best = None
    for g in product((1, -1), repeat=3):     # gauge sigma on the 3 nodes
        neg = 0
        for (i, j) in EDGES:
            if g[i] * g[j] * signs[(i, j)] == -1:
                neg += 1
        best = neg if best is None else min(best, neg)
    # GF(2) cocycle class: triangle balanced iff product of signs = +1
    prod = signs[EDGES[0]] * signs[EDGES[1]] * signs[EDGES[2]]
    gf2_class = 0 if prod == 1 else 1        # 0 = balanced, 1 = frustrated
    return {
        "value": best,
        "frustrated": best > 0,
        "triangle_sign_product": prod,
        "gf2_cocycle_class": gf2_class,
        "gf2_matches_mingauge": (gf2_class == (1 if best > 0 else 0)),
    }


# ---------------------------------------------------------------------------
# Guard-the-guard fabricated indices.
# ---------------------------------------------------------------------------
def i_fake_relabel(profile, doctrine):
    """POSITIVE control for the relabel detector: a pure function of v_gap by
    construction -> MUST be constant on every fiber."""
    return sum(vgap_vector(profile, doctrine))


def i_fake_independent(serial):
    """POSITIVE control for the independence detector: the distinct profile serial
    id -> MUST be non-constant on any fiber holding >= 2 profiles."""
    return serial


# ---------------------------------------------------------------------------
# Fiber test.
# ---------------------------------------------------------------------------
def _distribution(index_values):
    """Count of profiles per index value (string keys for JSON)."""
    dist = {}
    for v in index_values.values():
        dist[str(v)] = dist.get(str(v), 0) + 1
    return dict(sorted(dist.items()))


def fiber_partition(profiles, doctrine):
    """Group profile serials by fiber key (identical v_gap set function)."""
    fibers = {}
    for serial, prof in enumerate(profiles):
        fibers.setdefault(fiber_key(prof, doctrine), []).append(serial)
    return fibers


def fiber_test(index_values, fibers):
    """index_values: dict serial->int. Returns constancy report over the fibers."""
    nonconstant = []
    for key, serials in fibers.items():
        vals = {index_values[s] for s in serials}
        if len(vals) > 1:
            nonconstant.append((key, sorted(vals)))
    return {
        "n_fibers": len(fibers),
        "n_fibers_nonconstant": len(nonconstant),
        "constant_on_all_fibers": len(nonconstant) == 0,
        "nonconstant_examples": [
            {"fiber": list(k), "index_values": v} for k, v in nonconstant[:6]
        ],
    }


def separator_agreement(index_values, sep_values):
    """For a NON-constant index: does its value perfectly predict the separator
    across the whole class?  A collision (same index value carrying both
    separator=1 and separator=0) is off-fixture DISAGREEMENT -> different data.
    If the class has NO separator profiles, the agreement question is VACUOUS."""
    by_value = {}
    for s, iv in index_values.items():
        by_value.setdefault(iv, set()).add(sep_values[s])
    collisions = {iv: sorted(seps) for iv, seps in by_value.items() if len(seps) > 1}
    values_where_sep1 = {index_values[s] for s in index_values if sep_values[s] == 1}
    values_where_sep0 = {index_values[s] for s in index_values if sep_values[s] == 0}
    n_sep1 = sum(1 for s in sep_values if sep_values[s] == 1)
    vacuous = n_sep1 == 0
    perfectly_separates = (None if vacuous
                           else len(values_where_sep1 & values_where_sep0) == 0)
    return {
        "vacuous_no_separator_in_class": vacuous,
        "n_separator_profiles": n_sep1,
        "perfectly_predicts_separator": perfectly_separates,
        "index_values_carrying_sep1": sorted(values_where_sep1),
        "index_values_carrying_sep0": sorted(values_where_sep0),
        "colliding_values": collisions,
        "n_distinct_index_values": len(by_value),
    }


# ---------------------------------------------------------------------------
# Per-index Horn verdict.
# ---------------------------------------------------------------------------
def horn_verdict(name, ftest, sep_report, invariance_witness, n_distinct_values):
    if n_distinct_values <= 1:
        return {
            "index": name,
            "fiber_constant": True,
            "horn": "null",
            "reading": ("DEGENERATE / NULL channel: a single value across the whole "
                        "class -> carries no signal (not available at this witness "
                        "size)."),
            "go": False,
        }
    if ftest["constant_on_all_fibers"]:
        return {
            "index": name,
            "fiber_constant": True,
            "horn": 2,
            "reading": "RELABEL: I = f(v_gap); index-side linearity lemma fires.",
            "go": False,
        }
    # non-constant channel: escapes the relabel bar
    if sep_report is not None and sep_report["vacuous_no_separator_in_class"]:
        return {
            "index": name,
            "fiber_constant": False,
            "horn": "1-indep",
            "reading": ("INDEPENDENT of v_gap, but this class has NO finality "
                        "separator -> agreement is vacuous (not a GO)."),
            "go": False,
        }
    if sep_report is not None and sep_report["perfectly_predicts_separator"] \
            and invariance_witness is not None:
        return {
            "index": name,
            "fiber_constant": False,
            "horn": 1,
            "reading": "INDEPENDENT and agrees with the separator across the class.",
            "go": True,
        }
    return {
        "index": name,
        "fiber_constant": False,
        "horn": 1.5,
        "reading": ("INDEPENDENT of v_gap (escapes the relabel bar) but disagrees "
                    "off-fixture: the same index value carries both separator=1 "
                    "and separator=0 profiles (different data) -> still no GO."),
        "go": False,
    }


def invariance_witness_for(index_values, fibers, profiles, doctrine):
    """A deformation that moves I while v_gap is FIXED (two profiles in one fiber
    with different index value) -- proof the channel carries info beyond v_gap."""
    for key, serials in fibers.items():
        vals = {s: index_values[s] for s in serials}
        distinct = sorted(set(vals.values()))
        if len(distinct) > 1:
            a = next(s for s in serials if vals[s] == distinct[0])
            b = next(s for s in serials if vals[s] == distinct[-1])
            return {
                "shared_v_gap_fiber": list(key),
                "profile_a": {"serial": a, "profile": profiles[a],
                              "index": index_values[a]},
                "profile_b": {"serial": b, "profile": profiles[b],
                              "index": index_values[b]},
            }
    return None


# ---------------------------------------------------------------------------
# Assemble the run.
# ---------------------------------------------------------------------------
def run_doctrine(doctrine_name):
    doctrine = DOCTRINES[doctrine_name]
    profiles = enumerate_profiles()
    fibers = fiber_partition(profiles, doctrine)
    sep_values = {s: finality_separator(profiles[s], doctrine)
                  for s in range(len(profiles))}

    chi_vals = {s: i_chi(profiles[s])["value"] for s in range(len(profiles))}
    sf_vals = {s: i_sf(profiles[s])["value"] for s in range(len(profiles))}
    fr_vals = {s: i_fr(profiles[s])["value"] for s in range(len(profiles))}
    fake_rel = {s: i_fake_relabel(profiles[s], doctrine)
                for s in range(len(profiles))}
    fake_ind = {s: i_fake_independent(s) for s in range(len(profiles))}

    channels = {"I_chi": chi_vals, "I_sf": sf_vals, "I_fr": fr_vals}
    per_index = {}
    for name, vals in channels.items():
        ft = fiber_test(vals, fibers)
        n_distinct = len(set(vals.values()))
        sep = None if ft["constant_on_all_fibers"] else \
            separator_agreement(vals, sep_values)
        witness = None if ft["constant_on_all_fibers"] else \
            invariance_witness_for(vals, fibers, profiles, doctrine)
        per_index[name] = {
            "n_distinct_values": n_distinct,
            "value_distribution": _distribution(vals),
            "fiber_test": ft,
            "separator_agreement": sep,
            "invariance_witness": witness,
            "verdict": horn_verdict(name, ft, sep, witness, n_distinct),
        }

    # guard-the-guard
    gg_relabel = fiber_test(fake_rel, fibers)
    gg_independent = fiber_test(fake_ind, fibers)
    guard = {
        "relabel_detector_positive_control": {
            "index": "i_fake_relabel = sum(v_gap)",
            "must_be": "constant_on_all_fibers",
            "observed_constant": gg_relabel["constant_on_all_fibers"],
            "pass": gg_relabel["constant_on_all_fibers"] is True,
        },
        "independence_detector_positive_control": {
            "index": "i_fake_independent = profile serial id",
            "must_be": "non-constant (>=1 fiber varies)",
            "observed_nonconstant_fibers": gg_independent["n_fibers_nonconstant"],
            "pass": gg_independent["n_fibers_nonconstant"] > 0,
        },
    }

    n_sep = sum(sep_values.values())
    return {
        "doctrine": doctrine_name,
        "n_profiles": len(profiles),
        "n_fibers": len(fibers),
        "n_separator_profiles": n_sep,
        "per_index": per_index,
        "guard_the_guard": guard,
    }


def overall_verdict(doctrine_reports):
    """GO iff some index is Horn 1 in the AND class. Else REDESIGN/ABANDON."""
    and_report = doctrine_reports["AND"]
    horns = {name: and_report["per_index"][name]["verdict"]["horn"]
             for name in ("I_chi", "I_sf", "I_fr")}
    gos = {name: and_report["per_index"][name]["verdict"]["go"]
           for name in ("I_chi", "I_sf", "I_fr")}
    any_go = any(gos.values())
    all_relabel_or_null = all(h in (2, "null") for h in horns.values())
    if any_go:
        verdict = "GO"
        reason = ("a genuine independent index equals the separator across the "
                  "class with an invariance witness -- the frustration escape "
                  "valve is real.")
    elif all_relabel_or_null:
        verdict = "REDESIGN"
        reason = ("every index is a relabel of v_gap (Horn 2) or a degenerate/null "
                  "channel. The index-side linearity lemma fires: same wall a third "
                  "time (T422 / T423 / Route-A).")
    else:
        verdict = "REDESIGN"
        reason = ("no index is a clean relabel-free separator. In the AND dilemma "
                  "class each channel is one of: a degenerate/null channel (I_sf: "
                  "the twisted triangle is gapless at n=3, spectral flow re-reads "
                  "the frustration cocycle), a genuine relabel (Horn 2), or "
                  "INDEPENDENT-of-v_gap-but-different-data (Horn 1.5): it escapes "
                  "the relabel bar yet the same index value carries BOTH "
                  "separator=1 and separator=0 profiles, so it cannot be "
                  "thresholded to the finality separator. The frustration escape "
                  "valve fires on every genuine dilemma (necessary) but ALSO on "
                  "non-dilemma profiles (not sufficient). Confirms the unified "
                  "index-side lemma; the wall stands a third time "
                  "(T422 / T423 / Route-A).")
    return {
        "verdict": verdict,
        "reason": reason,
        "per_index_horn_AND": horns,
        "per_index_go_AND": gos,
    }


def run():
    reports = {name: run_doctrine(name) for name in DOCTRINES}
    verdict = overall_verdict(reports)
    return {
        "artifact": "T424-m2-route-a-index-probe-v0.1",
        "canonical_coalitions": [list(c) for c in CANON_COALITIONS],
        "overall_verdict": verdict,
        "doctrine_reports": reports,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
