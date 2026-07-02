"""Pytest suite for T395: Record-Order Trade-off Probe.

Exact assertions for the (D, V) trade-off curve endpoints, monotonicity, the
exact analytic relations of the two-order switch+record family, the
duality-reduction verdict (collapse, regression-pinned to the analytically
forced verdict -- the assertions below would fail loudly if the model
stopped collapsing), the Q1D no-signalling guardrail, and
the k=3 partial-record probe including the exhaustive finite-family sweep.

Conventions: subsystems index-sorted (c, r, t); gamma sweep predeclared with
endpoints exactly 0 and pi; tolerance 1e-12 for every relation claimed exact.
"""

import json
import math

import numpy as np
import pytest

from models.record_order_tradeoff_probe import (
    ACCESSIBILITY_VERDICT,
    ALL_ORDERS_6,
    CANONICAL_PAIR_NAME,
    GAMMA_SWEEP,
    K3_CLASS_OF,
    K3_ORDERS,
    K3_VERDICT,
    REDUCTION_VERDICT,
    TOL_EXACT,
    accessibility_invariance,
    asymmetric_control_spot_check,
    candidate_pair_table,
    class_helstrom,
    exhaustive_family_sweep,
    full_resolution_contrast,
    guess_prob_grid_check,
    guess_prob_record_only,
    k3_canonical_analysis,
    k_state_branch_sum,
    k_state_circuit,
    no_signalling_certificate,
    pairwise_normalized_coherences,
    perm_parity,
    reduction_audit,
    run_analysis,
    six_order_analysis,
    switch_state_branch_sum,
    switch_state_circuit,
    two_order_curves,
    visibility_fringe_grid,
    FRINGE_GRID_TOL,
    GUESS_GRID_TOL,
)

PI = math.pi


@pytest.fixture(scope="module")
def curves():
    return two_order_curves()


@pytest.fixture(scope="module")
def audit():
    return reduction_audit()


@pytest.fixture(scope="module")
def k3():
    return k3_canonical_analysis()


# --------------------------------------------------------------------------- #
# Predeclarations and model construction
# --------------------------------------------------------------------------- #

def test_gamma_sweep_predeclared():
    assert len(GAMMA_SWEEP) == 21  # spec requires >= 20
    assert GAMMA_SWEEP[0] == 0.0
    assert abs(GAMMA_SWEEP[-1] - PI) < TOL_EXACT
    assert np.all(np.diff(GAMMA_SWEEP) > 0)


def test_state_normalized_and_circuit_equals_branch_sum():
    for g in GAMMA_SWEEP[::4]:
        for phi in (0.0, 1.3):
            a = switch_state_circuit(g, phi=phi)
            b = switch_state_branch_sum(g, phi=phi)
            assert abs(np.linalg.norm(a) - 1.0) < TOL_EXACT
            assert float(np.max(np.abs(a - b))) < TOL_EXACT


def test_canonical_pair_documented_and_balanced():
    table = candidate_pair_table()
    assert CANONICAL_PAIR_NAME in table
    assert table[CANONICAL_PAIR_NAME]["canonical"] is True
    # canonical pair sits exactly at the balanced two-marker point 1/sqrt(2)
    assert abs(table[CANONICAL_PAIR_NAME]["abs_K"] - 1.0 / math.sqrt(2)) < TOL_EXACT
    # the "maximal order-sensitivity" candidate is documented as degenerate
    assert table["Ry(pi/2),Rz(pi)"]["abs_K"] < TOL_EXACT


# --------------------------------------------------------------------------- #
# Two-order curve: endpoints, monotonicity, exact relations
# --------------------------------------------------------------------------- #

def test_D_endpoints_exact(curves):
    assert abs(curves["D_record"][0] - 0.0) < TOL_EXACT
    assert abs(curves["D_record"][-1] - 1.0) < TOL_EXACT


def test_V_endpoints_exact(curves):
    assert abs(curves["V"][0] - curves["V0"]) < TOL_EXACT
    assert abs(curves["V"][-1] - 0.0) < TOL_EXACT
    assert abs(curves["V0"] - 1.0 / math.sqrt(2)) < TOL_EXACT


def test_D_matches_sin_half_gamma(curves):
    assert curves["max_residual_D_vs_sin_half_gamma"] < TOL_EXACT


def test_V_matches_V0_cos_half_gamma(curves):
    assert curves["max_residual_V_vs_V0_cos_half_gamma"] < TOL_EXACT


def test_monotonicity_D_up_V_down(curves):
    assert curves["D_strictly_increasing"] is True
    assert curves["V_strictly_decreasing"] is True


def test_helstrom_success_endpoints(curves):
    assert abs(curves["helstrom_success"][0] - 0.5) < TOL_EXACT
    assert abs(curves["helstrom_success"][-1] - 1.0) < TOL_EXACT


def test_accessible_z_readout_is_D_squared(curves):
    # disclosed sub-optimality of the physical Z readout: D_Z = D^2 exactly
    assert curves["max_residual_Dz_vs_D_squared"] < TOL_EXACT


def test_normalized_duality_exact(curves):
    # D^2 + (V/V0)^2 = 1 -- the transplanted binary duality, exact
    assert curves["max_residual_normalized_duality"] < TOL_EXACT


def test_englert_joint_saturation_exact(curves):
    # D_joint^2 + V^2 = 1 with the joint (record x target) marker, exact
    assert curves["max_residual_englert_joint_saturation"] < TOL_EXACT


def test_three_way_decomposition_exact(curves):
    # D^2 + V^2 + (1 - D^2) Dt0^2 = 1: the candidate bound D^2 + V^2 <= 1
    # holds with slack exactly equal to the unread target-marker term
    assert curves["max_residual_three_way_decomposition"] < TOL_EXACT
    assert curves["max_residual_slack_identity"] < TOL_EXACT
    assert curves["candidate_bound_min_slack"] >= -TOL_EXACT


def test_fringe_grid_matches_exact_visibility():
    for g in (0.0, PI / 3, PI / 2, 0.9 * PI):
        exact = two_order_curves([g])["V"][0]
        grid = visibility_fringe_grid(g)
        assert abs(exact - grid) < FRINGE_GRID_TOL


def test_asymmetric_control_spot_check():
    res = asymmetric_control_spot_check()
    assert res["residual"] < TOL_EXACT


# --------------------------------------------------------------------------- #
# Accessibility (the (1)/(2) boundary) and Q1D no-signalling guardrail
# --------------------------------------------------------------------------- #

def test_accessibility_trace_vs_measure_invariance():
    res = accessibility_invariance()
    assert res["max_diff_traced_vs_measured"] < 1e-14
    assert res["verdict"] == ACCESSIBILITY_VERDICT


def test_no_signalling_cr_marginals_setting_independent():
    res = no_signalling_certificate()
    assert res["max_cr_marginal_diff_over_settings"] < TOL_EXACT
    assert res["max_record_marginal_diff_over_phase"] < TOL_EXACT


def test_no_signalling_check_has_teeth():
    # the settings DO move the target marginal; the invariance is not vacuous
    res = no_signalling_certificate()
    assert res["min_target_marginal_span_over_settings"] > 0.01


# --------------------------------------------------------------------------- #
# Reduction audit (the kill-test) -- verdict asserted as it landed
# --------------------------------------------------------------------------- #

def test_mz_statevector_identity_across_sweep(audit):
    assert audit["max_statevector_diff_switch_vs_mapped_MZ"] < TOL_EXACT


def test_plain_mz_curves_coincide_with_normalized_switch(audit):
    assert audit["max_D_curve_diff_switch_vs_plain_MZ"] < TOL_EXACT
    assert audit["max_normalized_V_curve_diff_switch_vs_plain_MZ"] < TOL_EXACT


def test_reduction_verdict_is_collapse(audit):
    # The kill-test landed as collapse. This test encodes the earned verdict:
    # if the model ever stops collapsing to interferometric duality, this
    # fails loudly and the artifact verdict must be re-earned.
    assert audit["collapsed_to_duality"] is True
    assert audit["verdict"] == REDUCTION_VERDICT


def test_mz_mapping_is_documented(audit):
    for key in ("control c", "record r (controlled-Ry(gamma))"):
        assert key in audit["mapping"]


# --------------------------------------------------------------------------- #
# k=3 probe: partial (class-coarse) record
# --------------------------------------------------------------------------- #

def test_k3_circuit_equals_branch_sum(k3):
    assert k3["max_circuit_vs_branch_sum_diff"] < TOL_EXACT
    for g in (0.0, 1.1, PI):
        st = k_state_branch_sum(K3_ORDERS, K3_CLASS_OF, g)
        assert abs(np.linalg.norm(st) - 1.0) < TOL_EXACT


def test_k3_within_class_coherence_gamma_flat(k3):
    assert k3["structure"]["max_within_class_flatness_dev"] < TOL_EXACT


def test_k3_cross_class_pairwise_duality_exact(k3):
    assert k3["structure"]["max_cross_class_duality_residual"] < TOL_EXACT
    assert k3["structure"]["max_cross_class_cos_scaling_residual"] < TOL_EXACT


def test_k3_guess_prob_formula_endpoints_and_monotone(k3):
    s = k3["structure"]
    assert abs(s["guess_prob_at_0"] - 1.0 / 3.0) < TOL_EXACT
    assert abs(s["guess_prob_at_pi"] - 2.0 / 3.0) < TOL_EXACT
    assert k3["P_guess_monotone_nondecreasing"] is True


def test_k3_guess_prob_grid_achievability(k3):
    for check in k3["grid_checks"].values():
        assert check["grid_le_analytic"] is True
        assert check["grid_achieves_within_tol"] is True


def test_k3_perfect_class_record_ceiling(k3):
    # gamma = pi: order postdiction capped at 2/3 (< 1) while within-class
    # coherence persists -- record-fixed at class resolution != order definite
    assert abs(k3["structure"]["guess_prob_at_pi"] - 2.0 / 3.0) < TOL_EXACT
    st = k_state_branch_sum(K3_ORDERS, K3_CLASS_OF, PI)
    nc = pairwise_normalized_coherences(st, 3)
    within = [
        nc[i, j]
        for i in range(3)
        for j in range(i + 1, 3)
        if K3_CLASS_OF[i] == K3_CLASS_OF[j]
    ]
    assert max(within) > 0.5  # intact coherence at perfect class record


def test_k3_class_helstrom_reaches_1_at_pi():
    assert abs(class_helstrom(K3_ORDERS, K3_CLASS_OF, PI) - 1.0) < TOL_EXACT
    assert abs(class_helstrom(K3_ORDERS, K3_CLASS_OF, 0.0) - 2.0 / 3.0) < TOL_EXACT


def test_k3_global_scalarizations_fail_binary_form(k3):
    circle = k3["circle_residuals"]
    assert k3["no_scalarization_stays_on_circle"] is True
    # mean and min undersaturate substantially; max overshoots the circle
    assert circle["mean"]["residual_at_pi"] < -0.5
    assert circle["min"]["residual_at_pi"] < -0.5
    assert abs(circle["max"]["residual_at_pi"] - 0.25) < TOL_EXACT


def test_six_order_parity_ceiling_one_third():
    six = six_order_analysis()
    assert abs(six["P_guess_at_pi"] - 1.0 / 3.0) < TOL_EXACT
    assert six["structure"]["max_within_class_flatness_dev"] < TOL_EXACT
    assert six["structure"]["max_cross_class_duality_residual"] < TOL_EXACT
    assert [perm_parity(p) for p in ALL_ORDERS_6].count(0) == 3


def test_exhaustive_family_sweep_all_pass():
    ex = exhaustive_family_sweep()
    assert ex["n_three_order_configs"] == 60  # C(6,3) x 3 bipartitions
    assert ex["n_six_order_configs"] == 31  # 2^5 - 1 bipartitions
    assert ex["all_pass"] is True
    assert ex["max_within_class_flatness_dev"] < TOL_EXACT
    assert ex["max_cross_class_duality_residual"] < TOL_EXACT
    assert ex["guess_ceiling_2_over_k_everywhere"] is True


def test_full_resolution_contrast():
    fc = full_resolution_contrast()
    # full-resolution perfect record: postdiction 1, all coherence dead
    assert abs(fc["P_guess_full_resolution_at_pi"] - 1.0) < TOL_EXACT
    assert fc["max_pairwise_coherence_at_pi"] < TOL_EXACT
    # class-coarse perfect record: ceiling 2/3, within-class coherence alive
    assert abs(fc["class_coarse_P_guess_at_pi"] - 2.0 / 3.0) < TOL_EXACT
    assert fc["class_coarse_max_within_coherence_at_pi"] > 0.5


# --------------------------------------------------------------------------- #
# Verdict restraint and serializability
# --------------------------------------------------------------------------- #

def test_verdict_strings_are_predeclared_and_restrained():
    res = run_analysis()
    assert res["verdicts"]["reduction"] == REDUCTION_VERDICT
    assert res["verdicts"]["k3"] == K3_VERDICT
    assert res["verdicts"]["accessibility"] == ACCESSIBILITY_VERDICT
    assert "finite observation" in K3_VERDICT
    assert "not a theorem" in K3_VERDICT
    assert "reduces exactly to" in REDUCTION_VERDICT
    # no promotion vocabulary anywhere in the verdicts
    for v in res["verdicts"].values():
        for banned in ("theorem proved", "law", "discovery", "promotes"):
            assert banned not in v


def test_result_dict_is_json_serializable():
    res = run_analysis()
    json.dumps(res)
