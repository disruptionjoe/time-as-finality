"""Tests for T410: Thermal Collision Work--Reach Frontier (the
Hamiltonian-bath rung of the capability restoration frontier).

Asserts, to numerical precision, the nine predeclared legs of the spec
(tests/T410-thermal-collision-work-reach-frontier.md, frozen before the
model file existed):

  1. First law + entropy production (exact-identity-backed at the
     computed states; Sigma both ways at finite beta; global balance).
  2. T409 regression corner: (beta = inf, free off) collision unitary
     IS controlled-Ry; frontier block reproduced cross-module.
  3. Temperature-blind frontier (free off): f = cos(theta/2) for every
     diagonal tau_beta; identical frontier at every beta incl. beta = 0.
  4. Certificate transfer to mixed thermal states: degree-1 structure,
     bound = 2x achieved (factor-2 looseness, fourth artifact), bands,
     dilation invariance for pure AND Gibbs work registers, attack
     battery on the predeclared undetermined-band cells (the fireable
     work-substitution leg).
  5. Restoration work: W_rest = -n w_fwd - 3/7 (B3 refund branch);
     round-trip work per retained contact exactly zero.
  6. Zero-bit contacts at beta = 0: marginals I/2, Holevo 0, frontier
     unmoved (contacts, not bits, sharpened).
  7. Thermal complementarity: D_1 = sin(theta/2) tanh(beta/2);
     deficit >= D_u^2, equality iff beta = inf (EGY corner).
  8. Landauer ledger at real beta (T142 conventions; bookkeeping).
  9. Guardrails: Q1D with teeth (3/7) tanh(beta/2); R1 untouched.

Plus discipline: exhaustive retained subsets (all 2^n, n <= 3),
symmetry pruning asserted, purification cross-check, determinism,
register layout, verdict vocabulary, and the disclosed spec-wording
defect (the free-off scope of "W = -Delta<H_int>").

Deterministic; the only sampling (Haar, seed 20260703) is illustrative.
"""

from __future__ import annotations

import math

import numpy as np

from models.thermal_collision_work_reach_frontier import (
    ANALYTIC_TOL,
    ATTACK_BETAS,
    ATTACK_N,
    ATTACK_REACH_SIZES,
    BAND_CERTIFIED,
    BAND_FEASIBLE,
    BAND_UNDETERMINED,
    BETA_SWEEP,
    BRANCH1_WEIGHT,
    FLATNESS_TOL,
    H2_3_7,
    HAAR_SEED,
    IDENTITY_TOL,
    LEDGER_N,
    N_ANC_MAX,
    SIGMA_NONNEG_TOL,
    SPREAD_TOL,
    TAU,
    THETA_METER,
    THETA_SWEEP,
    V_STAR,
    VERDICT_TAGS,
    VIS_A_ANALYTIC,
    branch_overlap_f,
    cached_analysis,
    chi1_closed_form,
    collision_u,
    d1_closed_form,
    deficit_allowance,
    frontier_cell,
    landauer_bound_bits,
    locked_visibility,
    min_certified_deficit,
    prepare_retained,
    stream_ledger,
    tau_gibbs,
    unwrite_protocol,
    w_fwd_closed_form_free_off,
    w_rest_analytic,
)


# --------------------------------------------------------------------------- #
# Fixture / layout / imported constants
# --------------------------------------------------------------------------- #

def test_register_layout_and_budget():
    assert N_ANC_MAX == 5
    assert TAU == 1.0
    assert tuple(THETA_SWEEP) == (0.25 * math.pi, 0.5 * math.pi, math.pi)
    assert BETA_SWEEP == (math.inf, 2.0, 1.0, 0.5, 0.0)
    rho = prepare_retained(5, (1, 2, 3, 4, 5), 1.0, 0.5 * math.pi, 1.0, True)
    assert rho.shape == (2 ** 7, 2 ** 7)  # S, REC + 5 retained carriers
    assert abs(float(np.real(np.trace(rho))) - 1.0) < 1e-12


def test_house_constants_imported_unchanged():
    assert THETA_METER == math.pi / 3.0  # T392's weak meter, unchanged
    assert V_STAR == 0.9  # T392/T393/T408/T409's threshold, unchanged
    assert abs(VIS_A_ANALYTIC - 4.0 * math.sqrt(3.0) / 7.0) < 1e-15
    assert abs(H2_3_7 - 0.985228) < 1e-6
    assert abs(BRANCH1_WEIGHT - 3.0 / 7.0) < 1e-15


def test_gibbs_corners_exact():
    assert float(np.max(np.abs(
        tau_gibbs(math.inf) - np.diag([1.0, 0.0])
    ))) == 0.0
    assert float(np.max(np.abs(
        tau_gibbs(0.0) - np.eye(2) / 2.0
    ))) == 0.0
    tau1 = tau_gibbs(1.0)
    z = 1.0 + math.exp(-1.0)
    assert abs(float(np.real(tau1[0, 0])) - 1.0 / z) < 1e-15


def test_determinism():
    a1 = prepare_retained(4, (1, 3), math.sqrt(2.0), 0.5 * math.pi, 1.0, True)
    a2 = prepare_retained(4, (1, 3), math.sqrt(2.0), 0.5 * math.pi, 1.0, True)
    assert float(np.max(np.abs(a1 - a2))) == 0.0
    v1 = locked_visibility(
        3, (1, 2), unwrite_protocol((1, 2), math.pi, False),
        math.pi, 1.0, False,
    )
    v2 = locked_visibility(
        3, (1, 2), unwrite_protocol((1, 2), math.pi, False),
        math.pi, 1.0, False,
    )
    assert v1 == v2


def test_all_legs_hold_and_no_halting_failure():
    res = cached_analysis()
    for name, ok in res["legs"].items():
        assert ok is True, name
    assert res["thermal_work_reach_frontier_holds"] is True
    fired = [k for k, v in res["failure_legs"].items() if v["fired"]]
    assert fired == []


def test_construction_expm_vs_block_and_p_m0():
    c = cached_analysis()["construction"]
    assert c["worst_expm_vs_block"] < FLATNESS_TOL
    assert c["tau_inf_is_ground"] == 0.0
    assert c["tau_zero_is_maximally_mixed"] == 0.0
    assert c["worst_p_m0_deviation"] < FLATNESS_TOL  # P(M=0) = 7/8, phi-blind
    assert "scipy" in c["scipy_note"]


def test_purification_cross_check():
    assert cached_analysis()["purification_check"]["max_diff"] < IDENTITY_TOL


# --------------------------------------------------------------------------- #
# Leg 1 -- first law + entropy production
# --------------------------------------------------------------------------- #

def test_first_law_interior_autonomous_and_conventions():
    fl = cached_analysis()["first_law"]
    assert fl["worst_interior_conservation"] < FLATNESS_TOL
    # free ON: switching work = Delta E_free = -Delta<H_int> (< 1e-12).
    assert fl["worst_work_convention_agreement_free_on"] < FLATNESS_TOL
    # free OFF: the spec's parenthetical was mis-scoped -- the deviation
    # equals w_fwd per collision, disclosed as a spec-wording defect.
    assert fl["free_off_convention_deviation_max"] > 0.1  # it fired
    assert "FIRED AND REPORTED" in fl["spec_wording_defect"]
    assert "mis-scoped" in fl["spec_wording_defect"]


def test_entropy_production_identity_both_ways():
    fl = cached_analysis()["first_law"]
    assert fl["worst_sigma_identity_residual"] < IDENTITY_TOL
    assert fl["min_sigma_over_sweep"] >= SIGMA_NONNEG_TOL
    assert "typed inf" in fl["beta_inf_typing"]


def test_ledger_is_phi_blind_and_collision_uniform():
    fl = cached_analysis()["first_law"]
    assert fl["worst_wq_spread_across_collisions"] < FLATNESS_TOL
    assert fl["worst_ledger_phi_dependence"] < FLATNESS_TOL


def test_global_energy_balance_telescopes():
    fl = cached_analysis()["first_law"]
    assert fl["worst_global_balance_residual"] < IDENTITY_TOL


def test_sigma_stream_values_at_reference_point():
    """Spot check the exact identity at (theta = pi, beta = 1, off):
    W = Q = (3/7) tanh(1/2) per collision; Sigma > 0 and equal across
    collisions."""
    led = stream_ledger(4, (1, 2, 3, 4), math.pi, 1.0, False)
    w_expected = (3.0 / 7.0) * math.tanh(0.5)
    for c in led["collisions"]:
        assert abs(c["W_i"] - w_expected) < ANALYTIC_TOL
        assert abs(c["Q_i"] - w_expected) < ANALYTIC_TOL
        assert c["Sigma_i"] > 0.0
        assert c["sigma_identity_residual"] < IDENTITY_TOL


def test_sigma_typed_inf_at_beta_inf():
    led = stream_ledger(2, (1, 2), math.pi, math.inf, False)
    for c in led["collisions"]:
        assert c["Q_i"] > 0.0
        assert math.isinf(c["Sigma_i"])
        assert c["sigma_identity_residual"] is None


# --------------------------------------------------------------------------- #
# Leg 2 -- T409 regression corner
# --------------------------------------------------------------------------- #

def test_free_off_collision_is_exactly_controlled_ry():
    reg = cached_analysis()["regression"]
    assert reg["gate_equals_controlled_ry_max_diff"] < FLATNESS_TOL


def test_regression_frontier_r_equals_n():
    reg = cached_analysis()["regression"]
    assert reg["r_feas_by_n"] == list(range(1, N_ANC_MAX + 1))
    assert reg["r_cert_by_n"] == list(range(1, N_ANC_MAX + 1))
    assert reg["worst_insufficient_phi_cert"] < FLATNESS_TOL
    assert reg["worst_insufficient_bound"] < FLATNESS_TOL
    for v in reg["full_reach_restores"]:
        assert abs(v - VIS_A_ANALYTIC) < ANALYTIC_TOL


def test_regression_cross_module_against_t409():
    reg = cached_analysis()["regression"]
    assert reg["worst_cross_module_diff"] < ANALYTIC_TOL
    assert len(reg["cross_module_cells"]) == sum(
        n + 1 for n in (1, 3, 5)
    ) * 2
    assert "re-scoped" in reg["t409_standing_note"]


# --------------------------------------------------------------------------- #
# Leg 3 -- temperature-blind frontier (free off)
# --------------------------------------------------------------------------- #

def test_branch_overlap_law_free_off():
    """f = |Tr[V_1 tau_beta V_0^dag]| = cos(theta/2) for every diagonal
    tau_beta -- asserted directly at every sweep point."""
    for theta in THETA_SWEEP:
        for beta in BETA_SWEEP:
            assert abs(
                branch_overlap_f(theta, beta, False) - math.cos(theta / 2.0)
            ) < 1e-12


def test_temperature_blind_frontier_tables():
    tb = cached_analysis()["temperature_blind"]
    assert tb["worst_achieved_spread_across_beta"] < SPREAD_TOL
    assert tb["worst_closed_form_residual"] < ANALYTIC_TOL
    assert tb["integer_tables_beta_identical"] is True
    assert tb["d_by_theta"] == {"0.25pi": 1, "0.50pi": 0, "1.00pi": 0}
    assert tb["u_min_cert_by_theta"] == {
        "0.25pi": 10.0, "0.50pi": 3.0, "1.00pi": 1.0
    }


def test_frontier_shapes_per_theta():
    tb = cached_analysis()["temperature_blind"]["frontiers_free_off"]
    assert tb["1.00pi"]["r_feas_by_n"] == [1, 2, 3, 4, 5]
    assert tb["1.00pi"]["r_cert_by_n"] == [1, 2, 3, 4, 5]  # exact bracket
    assert tb["0.50pi"]["r_feas_by_n"] == [1, 2, 3, 4, 5]
    assert tb["0.50pi"]["r_cert_by_n"] == [0, 0, 1, 2, 3]  # width 2
    assert tb["0.25pi"]["r_feas_by_n"] == [0, 1, 2, 3, 4]  # onset delay 1
    assert tb["0.25pi"]["r_cert_by_n"] == [0, 0, 0, 0, 0]  # honestly vacuous


def test_deficit_allowance_and_u_min_cert_closed_forms():
    for theta, d_exp, u_exp in (
        (0.25 * math.pi, 1, 10.0),
        (0.5 * math.pi, 0, 3.0),
        (math.pi, 0, 1.0),
    ):
        f = branch_overlap_f(theta, math.inf, False)
        assert deficit_allowance(f) == d_exp
        assert min_certified_deficit(f) == u_exp


# --------------------------------------------------------------------------- #
# Leg 4 -- certificate transfer, bands, dilation, attacks
# --------------------------------------------------------------------------- #

def test_phi_certificate_fires_at_every_temperature():
    """theta = pi, free off: f = 0 for every diagonal tau, so every
    insufficient retained reach is exactly phi-independent at every
    beta -- all-channel impossibility on a MIXED thermal state."""
    cert = cached_analysis()["certificates"]
    assert cert["worst_phi_cert_theta_pi_free_off"] < FLATNESS_TOL


def test_degree1_trigonometric_structure_asserted():
    cert = cached_analysis()["certificates"]
    assert cert["degree1_reconstruction_residual"] < FLATNESS_TOL


def test_bound_is_exactly_twice_achieved_fourth_artifact():
    cert = cached_analysis()["certificates"]
    assert cert["worst_bound_minus_2x_achieved"] < ANALYTIC_TOL
    assert "fourth artifact" in cert["factor2_note"]


def test_free_on_theta_pi_certified_at_every_beta():
    cert = cached_analysis()["certificates"]
    assert cert["worst_free_on_theta_pi_bound_u1"] < V_STAR
    assert (
        cert["worst_free_on_theta_pi_bound_u1"]
        <= cert["free_on_bound_ceiling_analytic"] + ANALYTIC_TOL
    )
    for row in cert["free_on_theta_pi"].values():
        assert row["band"] == BAND_CERTIFIED


def test_dilation_invariance_pure_and_gibbs_work():
    d = cached_analysis()["certificates"]["dilation"]
    assert d["phi_cert_bare"] < FLATNESS_TOL
    assert d["phi_cert_with_work"] < FLATNESS_TOL
    assert d["bound_pure_invariance_diff"] < FLATNESS_TOL
    assert d["bound_gibbs_invariance_diff"] < FLATNESS_TOL
    assert d["frontier_bound_max_diff_with_work"] < FLATNESS_TOL
    assert "necessarily phi-independent" in d["lemma"]
    assert "Stinespring" in d["lemma"]


def test_attack_cells_are_the_predeclared_undetermined_band():
    at = cached_analysis()["certificates"]["attacks"]
    assert at["seed"] == HAAR_SEED
    assert len(at["cells"]) == len(ATTACK_BETAS) * len(ATTACK_REACH_SIZES)
    for c in at["cells"]:
        assert c["band"] == BAND_UNDETERMINED
        assert c["departed"] == ATTACK_N - c["reach"]


def test_manufactured_coherence_nulled_at_finite_temperature():
    at = cached_analysis()["certificates"]["attacks"]
    for c in at["cells"]:
        assert c["manufactured_raw"] > 0.99
        assert c["manufactured_locked"] < FLATNESS_TOL
        assert c["feedback_locked"] < FLATNESS_TOL


def test_work_substitution_leg_reported_consistently():
    """The fireable failure leg: either outcome is a reportable verdict;
    the flag must equal the computed facts, and the verdict language
    must match the fired/not-fired branch."""
    res = cached_analysis()
    at = res["certificates"]["attacks"]
    crossed = any(c["attack_crossed_v_star"] for c in at["cells"])
    assert at["work_substitution_observed"] == crossed
    assert (
        res["failure_legs"]["work_substitutes_for_reach_at_finite_temperature"][
            "fired"
        ]
        == crossed
    )
    assert "undetermined band" in at["scope_note"]
    assert "illustrative" in at["scope_note"]


# --------------------------------------------------------------------------- #
# Leg 5 -- restoration work (B3 refund)
# --------------------------------------------------------------------------- #

def test_restoration_work_refund_law():
    rw = cached_analysis()["restoration_work"]
    assert rw["worst_refund_law_residual"] < ANALYTIC_TOL
    assert rw["worst_roundtrip_work"] < IDENTITY_TOL
    assert rw["worst_free_off_closed_form_residual"] < ANALYTIC_TOL


def test_restoration_branch_selected_by_the_numbers():
    rw = cached_analysis()["restoration_work"]
    assert rw["branch_selected"] == "B3_restoration_work_refund"
    assert "REFUND" in rw["headline"]
    assert "currency remains reach" in rw["headline"]
    # w_fwd at the T409 corner is 3/7 exactly.
    assert abs(rw["w_fwd_reference_theta_pi_beta_inf"] - 3.0 / 7.0) < 1e-12


def test_w_rest_closed_form_values():
    """W_rest = -n w_fwd - 3/7; at (theta = pi, beta = 1, off):
    w_fwd = (3/7) tanh(1/2)."""
    rw = cached_analysis()["restoration_work"]
    w = (3.0 / 7.0) * math.tanh(0.5)
    for n, w_rest in enumerate(rw["W_rest_by_n_reference"], start=1):
        assert abs(w_rest - (-n * w - 3.0 / 7.0)) < ANALYTIC_TOL
    assert abs(rw["W_rest_slope_in_n_reference"] + w) < ANALYTIC_TOL
    assert abs(
        w_rest_analytic(4, math.pi, 1.0, False) - (-4 * w - 3.0 / 7.0)
    ) < 1e-12
    assert abs(
        w_fwd_closed_form_free_off(math.pi, 1.0) - w
    ) < 1e-15


def test_writing_into_infinite_temperature_bath_is_free():
    """beta = 0: w_fwd = 0 (tanh(0) = 0) -- forward contact costs no
    switching work; W_rest = -3/7 exactly (the uncopy refund)."""
    led = stream_ledger(3, (1, 2, 3), math.pi, 0.0, False)
    for c in led["collisions"]:
        assert abs(c["W_i"]) < 1e-12
        assert abs(c["Q_i"]) < 1e-12
    assert abs(led["restoration"]["W_rest"] + 3.0 / 7.0) < ANALYTIC_TOL


# --------------------------------------------------------------------------- #
# Leg 6 -- zero-bit contacts (beta = 0 corner)
# --------------------------------------------------------------------------- #

def test_beta0_marginals_and_branch_blocks_carry_nothing():
    zb = cached_analysis()["zero_bit_contacts"]
    assert zb["beta0_worst_single_marginal_vs_half"] < FLATNESS_TOL
    assert zb["beta0_branch_block_diff"] < FLATNESS_TOL
    assert zb["chi_beta0_max"] < FLATNESS_TOL


def test_frontier_persists_at_beta0():
    zb = cached_analysis()["zero_bit_contacts"]
    assert zb["beta0_frontier_r_feas"] == list(range(1, N_ANC_MAX + 1))
    assert zb["beta0_frontier_r_cert"] == list(range(1, N_ANC_MAX + 1))
    assert zb["beta0_frontier_r_feas"] == zb["beta_inf_frontier_r_feas"]


def test_escaped_holevo_plateau_at_beta_inf_and_closed_form():
    zb = cached_analysis()["zero_bit_contacts"]
    for chi in zb["chi_bits_by_beta_then_u"]["inf"]:
        assert abs(chi - H2_3_7) < ANALYTIC_TOL  # T409's plateau
    assert zb["worst_chi1_closed_form_residual"] < ANALYTIC_TOL
    # chi falls with temperature at every u (contacts, not bits).
    for u_idx in range(LEDGER_N):
        chis = [
            zb["chi_bits_by_beta_then_u"][str(b)][u_idx] for b in BETA_SWEEP
        ]
        assert all(a >= b - 1e-12 for a, b in zip(chis, chis[1:]))
    assert abs(chi1_closed_form(math.inf) - H2_3_7) < 1e-12
    assert chi1_closed_form(0.0) == 0.0
    assert "no answer" in zb["finding"]


# --------------------------------------------------------------------------- #
# Leg 7 -- thermal complementarity
# --------------------------------------------------------------------------- #

def test_d1_closed_form_and_deficit_bound():
    comp = cached_analysis()["complementarity"]
    assert comp["worst_D1_closed_form_residual"] < ANALYTIC_TOL
    assert comp["min_gap_deficit_minus_D2"] >= SIGMA_NONNEG_TOL
    assert comp["worst_equality_residual_at_beta_inf"] < ANALYTIC_TOL
    assert "Englert-Greenberger-Yasin" in comp["note"]
    assert abs(d1_closed_form(math.pi, math.inf) - 1.0) < 1e-15
    assert d1_closed_form(math.pi, 0.0) == 0.0


def test_thermal_gap_strictly_positive_at_finite_beta():
    """At finite beta and u >= 1 the gap deficit - D_u^2 is strictly
    positive: the capability deficit is temperature-blind, the locally
    readable record is not."""
    rows = cached_analysis()["complementarity"]["rows"]
    for row in rows:
        if not math.isinf(row["beta"]) and row["departed_u"] >= 1:
            assert row["gap_deficit_minus_D2"] > 1e-6


# --------------------------------------------------------------------------- #
# Leg 8 -- Landauer ledger
# --------------------------------------------------------------------------- #

def test_ledger_correlated_uncopy_vs_blind_reset():
    led = cached_analysis()["landauer"]
    for entry in led["per_beta"].values():
        rw = entry["restore_within_reach"]
        assert rw["mode"] == "correlated_uncopy"
        assert rw["erased_bits"] == 0
        assert rw["landauer_floor_nats"] == 0.0
        assert rw["achieved_locked_visibility"] >= V_STAR
        br = entry["blind_reset"]
        assert br["capability_after_reset"] < FLATNESS_TOL
        assert br["residual_branch_distinguishability"] < FLATNESS_TOL
        assert br["deletion_is_not_definalization"] is True
        assert br["beta_work_floor_naive_nats"] == landauer_bound_bits(5)


def test_ledger_thermal_record_entropies():
    led = cached_analysis()["landauer"]
    joint_inf = led["per_beta"]["inf"]["blind_reset"][
        "joint_record_bits_given_M0"
    ]
    assert abs(joint_inf - H2_3_7) < ANALYTIC_TOL  # T409's number
    # heat per collision at beta = inf is 3/7 (theta = pi).
    assert abs(led["per_beta"]["inf"]["heat_per_collision"] - 3.0 / 7.0) < 1e-9


def test_ledger_beyond_frontier_access_not_work():
    led = cached_analysis()["landauer"]["restore_beyond_frontier"]
    assert led["feasible_at_reach"] is False
    assert led["certificates"]["phi_independence"] < FLATNESS_TOL
    assert led["certificates"]["channel_bound"] < FLATNESS_TOL
    assert math.isinf(led["min_work"])
    assert "ACCESS-not-work" in led["typing"]
    assert "not a work divergence" in led["typing"]
    assert "not a" in cached_analysis()["landauer"]["scope"].lower() or (
        "NOT a" in cached_analysis()["landauer"]["scope"]
    )


# --------------------------------------------------------------------------- #
# Leg 9 -- guardrails
# --------------------------------------------------------------------------- #

def test_q1d_guardrail_asserted_numerically():
    q1d = cached_analysis()["q1d"]
    assert q1d["declared_record_invariance"] < FLATNESS_TOL
    assert q1d["worst_no_signal_out"] < FLATNESS_TOL
    assert q1d["worst_teeth_closed_form_residual"] < ANALYTIC_TOL
    teeth_inf = q1d["teeth_by_beta"]["inf"][
        "enlarged_protocol_moves_outside_marginal"
    ]
    assert abs(teeth_inf - 3.0 / 7.0) < ANALYTIC_TOL  # T408/T409's tooth
    # teeth shrink with temperature: (3/7) tanh(beta/2).
    teeth_1 = q1d["teeth_by_beta"]["1.0"][
        "enlarged_protocol_moves_outside_marginal"
    ]
    assert abs(teeth_1 - (3.0 / 7.0) * math.tanh(0.5)) < ANALYTIC_TOL
    teeth_0 = q1d["teeth_by_beta"]["0.0"][
        "enlarged_protocol_moves_outside_marginal"
    ]
    assert teeth_0 < FLATNESS_TOL  # marginal blindness at beta = 0


def test_beta0_tooth_is_the_visibility_jump():
    jump = cached_analysis()["q1d"]["beta0_visibility_jump"]
    assert jump["achieved_reach_3_of_4"] < FLATNESS_TOL
    assert abs(jump["achieved_reach_4_of_4"] - VIS_A_ANALYTIC) < ANALYTIC_TOL


def test_r1_untouched_not_a_light_cone():
    note = cached_analysis()["q1d"]["r1_note"]
    assert "R1 untouched" in note
    assert "not a light cone" in note
    assert "Lieb-Robinson" in note


# --------------------------------------------------------------------------- #
# Discipline -- exhaustive subsets, symmetry, bands, verdict
# --------------------------------------------------------------------------- #

def test_exhaustive_retained_subsets_small_n():
    ex = cached_analysis()["exhaustive"]
    assert ex["worst_same_size_spread"] < SPREAD_TOL
    assert ex["frontier_mismatches"] == 0
    # 3 thetas x 5 betas x 2 toggles x n in {1,2,3} = 90 blocks;
    # 2 + 4 + 8 = 14 subsets per (point, n) triple.
    assert ex["blocks_checked"] == 90
    assert ex["subsets_per_block_total"] == 30 * 14


def test_symmetry_pruning_asserted_before_canonical_use():
    sym = cached_analysis()["symmetry"]
    assert sym["max_state_diff"] < FLATNESS_TOL
    assert sym["ns"] == [4, 5]
    assert sym["pairs_compared"] == 48  # 6 pairs x 4 points x 2 phases


def test_three_bands_realized():
    """theta = 0.5 pi, beta = 1.0, free off, n = 5: certified,
    undetermined, and feasible bands all realized on one column."""
    bands = [
        frontier_cell(5, tuple(range(1, r + 1)), 0.5 * math.pi, 1.0, False)[
            "band"
        ]
        for r in range(6)
    ]
    assert bands == (
        [BAND_CERTIFIED] * 3 + [BAND_UNDETERMINED] * 2 + [BAND_FEASIBLE]
    )


def test_verdict_language_and_tags():
    res = cached_analysis()
    assert tuple(res["verdict_tags"]) == VERDICT_TAGS
    assert res["verdict_tags"][-1] == "no_claim_promotion"
    lang = res["verdict_language"]
    assert "thermal-collision work-reach frontier holds" in lang
    assert "pause for Joe" in lang
    assert "no claim promotion" in lang
    assert "named-unbuilt" in lang
    assert "adopted, not derived" in lang  # the conditionality concession
    assert "finite-witness" in lang


def test_verdicts_are_reach_relative():
    """Per-cell verdicts use the house vocabulary: restorable-at-reach /
    final-relative-to-reach."""
    cell_final = frontier_cell(3, (1,), math.pi, 1.0, False)
    assert cell_final["verdict"] == "final-relative-to-reach"
    cell_ok = frontier_cell(3, (1, 2, 3), math.pi, 1.0, False)
    assert cell_ok["verdict"] == "restorable-at-reach"
