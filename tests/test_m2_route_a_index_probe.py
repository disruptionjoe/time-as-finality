"""Tests for T424 - M2 Route-A Decisive Fiber-Variation Index Probe.

Fiber test (per index) + separator-agreement + guard-the-guard, over all 64
consistent n=3 profiles and the doctrine family {AND, OR, DICT, NOCONN, XOR}.
Exact arithmetic except I_sf (numpy, grid-refinement determinism cross-check).
Recorded-tier; no claim promotion.

    python -m pytest tests/test_m2_route_a_index_probe.py -q
"""

import ast
import sys
from pathlib import Path

from models.m2_route_a_index_probe import (
    JUDGES, DOCTRINES, CANON_COALITIONS,
    enumerate_profiles, columns, vgap_vector, fiber_key, finality_separator,
    fiber_partition, i_chi, i_sf, i_fr, i_fake_relabel, i_fake_independent,
    edge_sign, EDGES, rank_rational, rank_gf2, run, run_doctrine, overall_verdict,
)

PROFILES = enumerate_profiles()
AND = DOCTRINES["AND"]


# --- ONE-WAY-RULE import audit (static + runtime) --------------------------
def test_import_audit_only_taf_native():
    src = Path("models/m2_route_a_index_probe.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
        elif isinstance(node, ast.Import):
            for a in node.names:
                imported.add(a.name.split(".")[0])
    # static: only stdlib + numpy + TaF-native `models`
    allowed = {"__future__", "fractions", "itertools", "json", "numpy", "models"}
    assert imported <= allowed, imported - allowed
    # the imported model modules must be TaF-native T413 / T423 only
    taf_modules = [m for m in imported if m == "models"]
    assert taf_modules == ["models"]
    # runtime: no forbidden sibling module ever loaded
    forbidden = ("gu", "gu_formalization", "temporal_issuance", "ai_epistemology",
                 "architecture_of_legitimacy")
    for name in list(sys.modules):
        assert not any(name == f or name.startswith(f + ".") for f in forbidden), name


def test_import_audit_source_names_taf_imports():
    src = Path("models/m2_route_a_index_probe.py").read_text(encoding="utf-8")
    assert "models.legitimacy_shapley_finality_probe" in src   # T413
    assert "models.m2_observer_game" in src                    # T423


# --- profiles: enumerated and consistent by construction -------------------
def test_profiles_enumerated_and_consistent():
    assert len(PROFILES) == 64                    # 4^3
    assert len(set(PROFILES)) == 64
    # r_i = doctrine(p_i,q_i) by construction -> every profile individually consistent
    for prof in PROFILES:
        p, q, r = columns(prof, AND)
        for i in JUDGES:
            assert r[i] == AND(p[i], q[i])


# --- reference primitive: the v_gap fiber label ----------------------------
def test_vgap_fiber_label_deterministic_and_canonical():
    assert len(CANON_COALITIONS) == 8
    # canonical order is (size, then sorted members) and stable
    assert CANON_COALITIONS[0] == () and CANON_COALITIONS[-1] == (1, 2, 3)
    for prof in PROFILES[:8]:
        assert vgap_vector(prof, AND) == vgap_vector(prof, AND)


def test_and_class_collapses_to_two_fibers_separator_tracks_fiber():
    fibers = fiber_partition(PROFILES, AND)
    assert len(fibers) == 2
    # exactly one fiber is the u_N pattern (0,...,0,1) with 6 profiles = the dilemmas
    sizes = sorted(len(v) for v in fibers.values())
    assert sizes == [6, 58]
    zero = tuple([0] * 8)
    uN = tuple([0] * 7 + [1])
    assert set(fibers) == {zero, uN}
    for key, serials in fibers.items():
        seps = {finality_separator(PROFILES[s], AND) for s in serials}
        assert len(seps) == 1                      # separator is constant on each fiber
        assert (seps == {1}) == (key == uN)


def test_frozen_t423_dilemma_is_a_separator_profile():
    target = ((1, 1), (1, 0), (0, 1))              # p=(1,1,0), q=(1,0,1)
    assert vgap_vector(target, AND) == tuple([0] * 7 + [1])
    assert finality_separator(target, AND) == 1


# --- I_chi: combinatorial-Hodge Euler characteristic -----------------------
def test_i_chi_exact_and_gf2_consistent_all_profiles():
    for prof in PROFILES:
        c = i_chi(prof)
        assert c["euler_consistent"]               # chi = b0 - b1 + b2 = |C0|-|C1|+|C2|
        assert c["gf2_betti_match"]                # integer Betti == GF(2) Betti


def test_i_chi_nonconstant_on_vgap_fibers():
    fibers = fiber_partition(PROFILES, AND)
    vals = {s: i_chi(PROFILES[s])["value"] for s in range(64)}
    # some fiber holds >1 distinct chi value -> I_chi is NOT a function of v_gap
    nonconstant = any(len({vals[s] for s in ser}) > 1 for ser in fibers.values())
    assert nonconstant
    assert set(vals.values()) == {1, 2}


def test_i_chi_does_not_separate_the_finality_datum():
    # chi = 1 carries BOTH dilemma and non-dilemma profiles -> different data
    sep1 = {i_chi(PROFILES[s])["value"] for s in range(64)
            if finality_separator(PROFILES[s], AND) == 1}
    sep0 = {i_chi(PROFILES[s])["value"] for s in range(64)
            if finality_separator(PROFILES[s], AND) == 0}
    assert sep1 == {1}
    assert 1 in sep0                               # collision -> cannot threshold


# --- I_sf: spectral-flow / APS-eta channel (null at n=3) -------------------
def test_i_sf_gapless_and_grid_stable():
    for prof in PROFILES:
        sf = i_sf(prof)
        assert sf["gapless_at_n3"]                 # min gap ~ 0 -> gapless triangle
        assert sf["grid_stable"]                   # deterministic under refinement


def test_i_sf_is_a_null_channel_reg_winding_constant():
    vals = {i_sf(prof)["value"] for prof in PROFILES}
    assert vals == {1}                             # single value across the class


def test_i_sf_gapless_residue_equals_frustration_cocycle():
    # the only profile-dependent residue at the gapless point re-reads I_fr's cocycle
    for prof in PROFILES:
        residue_class = 0 if i_sf(prof)["gapless_residue_P"] == 1 else 1
        assert residue_class == i_fr(prof)["gf2_cocycle_class"]


# --- I_fr: signed-graph frustration (the genuine loophole) -----------------
def test_i_fr_mingauge_matches_gf2_cocycle_all_profiles():
    for prof in PROFILES:
        assert i_fr(prof)["gf2_matches_mingauge"]


def test_i_fr_necessary_but_not_sufficient_for_the_dilemma():
    fr1 = {s for s in range(64) if i_fr(PROFILES[s])["value"] == 1}
    dil = {s for s in range(64) if finality_separator(PROFILES[s], AND) == 1}
    assert dil <= fr1                              # NECESSARY: every dilemma is frustrated
    assert len(fr1 - dil) == 18                    # NOT sufficient: 18 non-dilemmas too
    assert len(fr1) == 24


def test_i_fr_nonconstant_on_AND_but_relabel_on_XOR():
    fib_and = fiber_partition(PROFILES, AND)
    v_and = {s: i_fr(PROFILES[s])["value"] for s in range(64)}
    assert any(len({v_and[s] for s in ser}) > 1 for ser in fib_and.values())
    # in the XOR class frustration IS a function of v_gap (constant on fibers)
    fib_xor = fiber_partition(PROFILES, DOCTRINES["XOR"])
    assert all(len({v_and[s] for s in ser}) == 1 for ser in fib_xor.values())


# --- guard-the-guard (MANDATORY, both directions) --------------------------
def test_guard_relabel_detector_positive_control():
    # a pure function of v_gap MUST test constant on every fiber
    fibers = fiber_partition(PROFILES, AND)
    vals = {s: i_fake_relabel(PROFILES[s], AND) for s in range(64)}
    assert all(len({vals[s] for s in ser}) == 1 for ser in fibers.values())


def test_guard_independence_detector_positive_control():
    # a distinct-per-profile index MUST test non-constant on some fiber (>=2 profiles)
    fibers = fiber_partition(PROFILES, AND)
    vals = {s: i_fake_independent(s) for s in range(64)}
    assert any(len({vals[s] for s in ser}) > 1 for ser in fibers.values())


def test_guard_reported_in_every_doctrine_report():
    for name in DOCTRINES:
        g = run_doctrine(name)["guard_the_guard"]
        assert g["relabel_detector_positive_control"]["pass"] is True
        assert g["independence_detector_positive_control"]["pass"] is True


# --- Horn verdicts + overall verdict ---------------------------------------
def test_and_class_horn_verdicts():
    rep = run_doctrine("AND")
    assert rep["per_index"]["I_chi"]["verdict"]["horn"] == 1.5
    assert rep["per_index"]["I_fr"]["verdict"]["horn"] == 1.5
    assert rep["per_index"]["I_sf"]["verdict"]["horn"] == "null"
    for name in ("I_chi", "I_sf", "I_fr"):
        assert rep["per_index"][name]["verdict"]["go"] is False


def test_and_class_has_invariance_witnesses_for_independent_channels():
    rep = run_doctrine("AND")
    for name in ("I_chi", "I_fr"):
        w = rep["per_index"][name]["invariance_witness"]
        assert w is not None
        # deformation with v_gap FIXED (shared fiber) but index MOVED
        assert w["profile_a"]["index"] != w["profile_b"]["index"]


def test_overall_verdict_is_no_go_redesign():
    out = run()
    ov = out["overall_verdict"]
    assert ov["verdict"] == "REDESIGN"
    assert not any(ov["per_index_go_AND"].values())


def test_run_is_deterministic():
    assert run() == run()


# --- exact linear-algebra helpers ------------------------------------------
def test_rank_helpers_agree_on_incidence_shapes():
    M = [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]       # triangle boundary, rank 2
    assert rank_rational(M) == 2
    assert rank_gf2(M) == 2
    assert rank_rational([]) == 0 and rank_gf2([[0]]) == 0
