"""Tests for T422: Representability span of the forcing modes E1 / E2 / E3."""

import pytest

from models.representability_span import (
    ARTIFACT,
    cech_h1,
    circle_nerve,
    full_circle_class,
    e1_winding,
    e3_twist,
    e2_hardness,
    monotone,
    falsifier_search,
    run,
)


@pytest.fixture(scope="module")
def res():
    return run()


# --- the shared engine: coefficient-generic Cech H^1 of C_n -----------------


def test_engine_h1_of_circle_is_A_over_both_coefficient_groups():
    # H^1(C_4; A) = A : loop sum w=1 is a nonzero class in Z and in Z/2 alike,
    # computed by the IDENTICAL function with only `mod` changed.
    nerve = circle_nerve(4, {(3, 0): 1})
    z = full_circle_class(nerve, mod=0)
    z2 = full_circle_class(nerve, mod=2)
    assert z["h0"] == 1 and z2["h0"] == 1
    assert z["n_independent_cycles"] == 1 and z2["n_independent_cycles"] == 1
    assert z["winding"] == 1 and z["h1_trivial"] is False
    assert z2["winding"] == 1 and z2["h1_trivial"] is False


def test_engine_trivial_class_on_a_path():
    # remove the wrap edge -> a path (tree) -> H^1 = 0 regardless of coefficients.
    edges = [(0, 1), (1, 2), (2, 3)]
    trans = {(0, 1): 1, (1, 2): 0, (2, 3): 0}
    r = cech_h1([0, 1, 2, 3], edges, trans, mod=0)
    assert r["n_independent_cycles"] == 0
    assert r["h1_trivial"] is True


# --- S1: E1 and E3 share ONE genuine local-to-global invariant --------------


def test_s1_e1_winding_is_genuine_global_index():
    e1 = e1_winding(n=4)
    assert e1["coefficient_group"] == "Z"
    assert e1["winding"] == 1
    assert e1["class_nonzero"] is True
    assert e1["no_local_witness"] is True             # every proper subcover trivializes
    assert e1["proper_subcover_scan"]["some_proper_subset_witnesses_class"] is False
    assert e1["refinement_stable"] is True            # n->2n invariant
    assert e1["iso_invariant"] is True


def test_s1_e3_twist_same_engine_different_coefficient():
    e3 = e3_twist(n=4)
    assert e3["coefficient_group"] == "Z/2"
    assert e3["monodromy"] == 1
    assert e3["class_nonzero"] is True
    assert e3["no_local_witness"] is True
    assert e3["refinement_stable"] is True
    # T412 cross-check: no proper subset witness (0.0), full joint separates (1.0)
    x = e3["t412_crosscheck"]
    assert x["max_proper_subset_witness"] == 0.0
    assert x["full_joint_separates"] == 1.0
    assert x["matches_T412"] is True


def test_s1_common_invariant_type_same_function():
    # the common home is not gerrymandered: identical function, only mod differs.
    e1, e3 = e1_winding(4), e3_twist(4)
    assert e1["class"]["winding"] == e3["class"]["winding"] == 1
    assert e1["class"]["mod"] == 0 and e3["class"]["mod"] == 2


# --- S2: E2 non-representability, exhibited (not by fiat) --------------------


def test_s2_crt_is_verified_ring_iso_preserving_qr():
    e2 = e2_hardness()
    crt = e2["crt_isomorphism"]
    assert crt["is_genuine_ring_iso"] is True
    assert crt["preserves_addition"] is True
    assert crt["preserves_multiplication"] is True
    assert crt["preserves_QR_on_units"] is True


def test_s2_step1_positive_control_equal_cech_invariants():
    # anti-K3: the object has presentation-INDEPENDENT Cech invariants.
    e2 = e2_hardness()
    pc = e2["step1_positive_control"]
    assert pc["P1_coloring_cech"] == {"h0": 2, "h1": 0, "n_color_classes": 2}
    assert pc["P2_coloring_cech"] == {"h0": 2, "h1": 0, "n_color_classes": 2}
    assert pc["cech_invariants_equal"] is True


def test_s2_forcing_verdict_flips_across_the_iso():
    e2 = e2_hardness()
    assert e2["datum"]["datum_differs"] is True
    assert e2["P1_N_coordinates"]["jacobi_A"] == e2["P1_N_coordinates"]["jacobi_B"] == 1
    assert e2["P1_N_coordinates"]["verdict"] == "FORCED"
    assert e2["P2_CRT_coordinates"]["verdict"] == "DECLARED"
    assert e2["verdict_flips_across_iso"] is True


def test_s2_deformation_scan_not_index_conserved():
    e2 = e2_hardness()
    scan = e2["deformation_scan"]
    assert scan["forcing_indicator"][77] == 1     # 7*11 hard
    assert scan["forcing_indicator"][79] == 0     # prime -> trivial
    assert scan["forcing_not_conserved"] is True


# --- S3: non-interconvertibility monotone -----------------------------------


def test_s3_monotone_separates_e2():
    e1, e3, e2 = e1_winding(4), e3_twist(4), e2_hardness()
    m = monotone(e1, e3, e2)
    assert m["delta_E1"] == 0
    assert m["delta_E3"] == 0
    assert m["delta_E2"] == 1
    assert m["separates_E2_from_E1E3"] is True


def test_s3_positive_control_battery_not_rigged():
    e1, e3, e2 = e1_winding(4), e3_twist(4), e2_hardness()
    m = monotone(e1, e3, e2)
    pc = m["positive_control"]
    assert pc["battery_returns_zero_on_E1E3"] is True   # returns 0 on E1/E3
    assert pc["t412_n_relabels"] == 48
    assert m["t110_orbit_lemma_holds"] is True


# --- S4: falsifier stated and does not trigger ------------------------------


def test_s4_falsifier_does_not_trigger():
    e2 = e2_hardness()
    f = falsifier_search(e2)
    assert f["candidate_that_is_both"] == []
    assert f["falsifier_triggers"] is False


def test_s4_falsifier_would_fire_if_a_both_candidate_existed():
    # guard the guard: if any candidate were both phi-invariant AND
    # hardness-tracking, the falsifier MUST report firing.
    e2 = e2_hardness()
    f = falsifier_search(e2)
    both = [c for c in f["candidates"] if c["phi_invariant"] and c["tracks_hardness"]]
    assert (len(both) > 0) == f["falsifier_triggers"]


# --- top-level verdict + guards ---------------------------------------------


def test_all_success_legs_and_go(res):
    assert res["artifact"] == ARTIFACT
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert all(res["success_legs"].values())
    assert not any(res["kill_legs"].values())
    assert res["verdict"] == "GO"
