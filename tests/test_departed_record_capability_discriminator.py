"""Tests for T411: Departed-Record Capability Discriminator (the
big-swing fixture of the primary open problem, on T410's departure
boundary).

Asserts, to numerical precision, the eight predeclared legs of the spec
(tests/T411-departed-record-capability-discriminator.md, frozen before
the model file existed):

  1. Equality, observational: rho_R^A = rho_R^B entrywise < 1e-12
     across both phase grids, every beta, m, both cascades.
  2. Equality, interventional: the environment-side channel lemma
     asserted operator-level (abstract Kraus, no tier-2 register) plus
     the predeclared family (12 unitaries, 2 instruments, 1 sequential
     composition, 15 seeded Haar rows -- illustrative, commutation
     rows).
  3. Forcing at R: both states final-relative-to-R, all-channel
     certified, work-dilation invariant.
  4. Separation at R+: A restorable-at-R+ (vis_A), B(SWAP)
     final-relative-to-R+ (exact product, exact phi-independence,
     dilation invariant), broadcast contrast certified too; A's R+
     record trace > 0.05 (T408 obstruction-lemma consistency).
  5. Positive control at R++, priced: B restorable (vis_A); cascade
     ledger W = 0 (SWAP), Q = (3/7) tanh(beta/2), Sigma identity both
     ways, Sigma(beta = 0, m = 1) = H(3/7) nats = departed mutual
     information; restoration work = T410's refund law.
  6. beta = 0 marginal blindness: every proper-subset marginal
     identical; full-joint TD = vis_A/2 at beta = 0 and
     (3 + sqrt(57))/14 at beta = inf (SWAP); carrier marginal fades as
     (3/7) tanh(beta/2); mutual-information closed forms.
  7. Absorber battery: stipulated-flag control, matched declared
     fields, label-free verdict functional, resource-projection
     concessions and residues, Lieb-Robinson / not-a-light-cone.
  8. Guardrails: Q1D record invariance, no signalling out of R, teeth
     (3/7) tanh(beta/2), beta = 0 visibility jump; R1 untouched.

Plus discipline: cross-module anchors against T410, determinism,
register layout, verdict vocabulary, and failure-leg consistency.

Deterministic; the only sampling (Haar, seed 20260704) is illustrative.
"""

from __future__ import annotations

import math

import numpy as np

from models.departed_record_capability_discriminator import (
    ANALYTIC_TOL,
    BETA_SWEEP,
    BRANCH1_WEIGHT,
    CASCADE_BROADCAST,
    CASCADE_SWAP,
    FLATNESS_TOL,
    H2_3_7,
    HAAR_SAMPLES,
    HAAR_SEED,
    IDENTITY_TOL,
    M_SWEEP,
    OPEN_PROBLEM_CRITERION,
    REACH_R,
    REACH_RP,
    REACH_RPP,
    RECORD_TRACE_MIN,
    SIGMA_CASC_BETA0_M1_NATS,
    SIGMA_NONNEG_TOL,
    TD_BETA0,
    TD_BETAINF_SWAP,
    THETA_BCAST,
    THETA_METER,
    V_STAR,
    VERDICT_TAGS,
    VIS_A_ANALYTIC,
    cached_analysis,
    cascade_ledger,
    e1_positions,
    e2_positions,
    lemma_channel,
    locked_visibility,
    prepare,
    unwrite,
    verdict_cell,
)


# --------------------------------------------------------------------------- #
# Fixture / layout / imported constants
# --------------------------------------------------------------------------- #

def test_register_layout_and_sweeps():
    assert M_SWEEP == (1, 2, 3)
    assert BETA_SWEEP == (math.inf, 1.0, 0.0)
    assert THETA_BCAST == math.pi
    rho_rp = prepare("A", 3, 1.0, 1.0, REACH_RP)
    assert rho_rp.shape == (2 ** 5, 2 ** 5)  # S, REC, E1_1..3
    rho_rpp = prepare("B", 3, 1.0, 1.0, REACH_RPP, CASCADE_SWAP)
    assert rho_rpp.shape == (2 ** 8, 2 ** 8)  # + E2_1..3
    assert abs(float(np.real(np.trace(rho_rpp))) - 1.0) < 1e-12
    assert e1_positions(3) == (2, 3, 4)
    assert e2_positions(3) == (5, 6, 7)


def test_house_constants_imported_unchanged():
    assert THETA_METER == math.pi / 3.0  # T392's weak meter, unchanged
    assert V_STAR == 0.9  # T392/T393/T408/T409/T410's threshold, unchanged
    assert abs(VIS_A_ANALYTIC - 4.0 * math.sqrt(3.0) / 7.0) < 1e-15
    assert abs(BRANCH1_WEIGHT - 3.0 / 7.0) < 1e-15
    assert abs(H2_3_7 - 0.985228) < 1e-6
    assert HAAR_SEED == 20260704
    assert HAAR_SAMPLES == 15


def test_predeclared_corner_values():
    assert abs(TD_BETA0 - VIS_A_ANALYTIC / 2.0) < 1e-15
    assert abs(TD_BETAINF_SWAP - (3.0 + math.sqrt(57.0)) / 14.0) < 1e-15
    assert abs(SIGMA_CASC_BETA0_M1_NATS - 0.682908) < 1e-6


def test_determinism():
    a1 = prepare("B", 2, math.sqrt(2.0), 1.0, REACH_RP, CASCADE_BROADCAST)
    a2 = prepare("B", 2, math.sqrt(2.0), 1.0, REACH_RP, CASCADE_BROADCAST)
    assert float(np.max(np.abs(a1 - a2))) == 0.0
    prep = lambda phi: prepare("A", 2, phi, 1.0, REACH_RP)
    v1 = locked_visibility(prep, lambda r: unwrite(r, 2))
    v2 = locked_visibility(prep, lambda r: unwrite(r, 2))
    assert v1 == v2


def test_all_legs_hold_and_no_failure_leg_fired():
    res = cached_analysis()
    for name, ok in res["legs"].items():
        assert ok is True, name
    assert res["departed_record_discriminator_holds"] is True
    fired = [k for k, v in res["failure_legs"].items() if v["fired"]]
    assert fired == []


def test_construction_anchors_cross_module_against_t410():
    c = cached_analysis()["construction"]
    assert c["worst_cross_module_A_Rplus_vs_T410"] < FLATNESS_TOL
    assert c["worst_cross_module_A_R_vs_T410"] < FLATNESS_TOL
    assert c["worst_Rplus_to_R_marginal_consistency"] < FLATNESS_TOL
    assert c["worst_p_m0_deviation"] < FLATNESS_TOL  # P(M=0) = 7/8
    assert "recorded-tier" in c["t410_standing_note"]


# --------------------------------------------------------------------------- #
# Leg 1 -- equality, observational
# --------------------------------------------------------------------------- #

def test_rho_R_identical_between_capability_states():
    eq = cached_analysis()["equality_observational"]
    assert eq["worst_rho_R_entrywise_diff"] < FLATNESS_TOL
    # both grids x 3 m x 3 beta x 2 cascades = 14 x 18 comparisons.
    assert eq["comparisons"] == 14 * 18


def test_rho_R_direct_spot_check():
    """rho_R = diag(4/7, 3/7) on {|00>, |11>}, phi-independent,
    identical for A and B at every beta."""
    for beta in BETA_SWEEP:
        ra = prepare("A", 2, 1.0, beta, REACH_R)
        rb = prepare("B", 2, math.pi / 3.0, beta, REACH_R, CASCADE_SWAP)
        # different phases on purpose: the R state is phi-independent.
        assert float(np.max(np.abs(ra - rb))) < FLATNESS_TOL
        assert abs(float(np.real(ra[0, 0])) - 4.0 / 7.0) < 1e-12
        assert abs(float(np.real(ra[3, 3])) - 3.0 / 7.0) < 1e-12


# --------------------------------------------------------------------------- #
# Leg 2 -- equality, interventional (lemma-carried)
# --------------------------------------------------------------------------- #

def test_lemma_operator_level_abstract_kraus():
    ei = cached_analysis()["equality_interventional"]
    assert ei["worst"]["lemma_operator_level"] < FLATNESS_TOL
    assert "ALL quantifier" in ei["lemma"]
    assert "illustrative" in ei["lemma"]


def test_intervention_family_equalities():
    ei = cached_analysis()["equality_interventional"]
    assert ei["worst"]["unitary_family"] < FLATNESS_TOL
    assert ei["worst"]["instrument_probs"] < FLATNESS_TOL
    assert ei["worst"]["instrument_states"] < FLATNESS_TOL
    assert ei["worst"]["sequential_probs"] < FLATNESS_TOL
    assert ei["worst"]["sequential_states"] < FLATNESS_TOL
    assert ei["worst"]["haar_family"] < FLATNESS_TOL
    assert ei["worst"]["commutation_in_action"] < FLATNESS_TOL
    assert ei["worst_overall"] < FLATNESS_TOL
    # 3 m x 3 beta x 2 cascades x 3 phases.
    assert ei["pairs_checked"] == 54


def test_lemma_channel_direct_spot_check():
    """(id_R (x) Lambda_E)(A) == B for both cascades at a fresh point."""
    for cascade in (CASCADE_SWAP, CASCADE_BROADCAST):
        a = prepare("A", 2, 0.7, 1.0, REACH_RP)
        b = prepare("B", 2, 0.7, 1.0, REACH_RP, cascade)
        assert float(np.max(np.abs(
            lemma_channel(a, 2, 1.0, cascade) - b
        ))) < FLATNESS_TOL


# --------------------------------------------------------------------------- #
# Leg 3 -- forcing at R
# --------------------------------------------------------------------------- #

def test_task_certified_impossible_inside_R_for_both_states():
    fo = cached_analysis()["forcing"]
    assert fo["all_final_relative_to_R"] is True
    assert fo["worst_phi_cert_at_R"] < FLATNESS_TOL
    assert fo["worst_bound_at_R"] < FLATNESS_TOL
    assert fo["worst_work_dilation_diff"] < FLATNESS_TOL
    assert "not modeled" in fo["note"]  # T400 compulsion clause disclosed


# --------------------------------------------------------------------------- #
# Leg 4 -- separation at R+
# --------------------------------------------------------------------------- #

def test_A_restorable_at_Rplus_every_beta_and_m():
    se = cached_analysis()["separation"]
    assert se["A_all_restorable_at_Rplus"] is True
    assert se["worst_A_restore_vs_visA"] < ANALYTIC_TOL
    for row in se["A_rows"]:
        assert row["verdict"] == "restorable-at-R+"
        assert row["achieved"] >= V_STAR


def test_B_swap_final_at_Rplus_exact_product_strong_certificate():
    se = cached_analysis()["separation"]
    assert se["B_swap_all_final_at_Rplus"] is True
    assert se["worst_B_swap_product_residual"] < FLATNESS_TOL
    assert se["worst_B_swap_phi_cert"] < FLATNESS_TOL
    assert se["worst_B_unwrite_locked"] < FLATNESS_TOL
    for row in se["B_swap_rows"]:
        assert row["verdict"] == "final-relative-to-R+"
        assert row["certified_by"] == "phi_independence"


def test_B_broadcast_contrast_certified():
    se = cached_analysis()["separation"]
    assert se["B_broadcast_all_final_at_Rplus"] is True
    # the spec's hand derivation predicted the exact certificate; the
    # fallback path exists but was not needed.
    assert se["B_broadcast_fallback_used"] is False
    assert se["worst_B_broadcast_phi_cert"] < FLATNESS_TOL


def test_dilation_invariance_pure_and_gibbs_work():
    se = cached_analysis()["separation"]
    assert se["dilation_cert_with_work"] < FLATNESS_TOL
    assert se["dilation_bound_diff_with_work"] < FLATNESS_TOL


def test_A_record_trace_required_by_obstruction_lemma():
    se = cached_analysis()["separation"]
    assert se["min_A_record_trace_cert"] > RECORD_TRACE_MIN
    assert "obstruction" in se["obstruction_lemma_note"]


def test_opposite_verdicts_one_functional_direct():
    cell_a = verdict_cell("A", 1, 1.0, REACH_RP)
    cell_b = verdict_cell("B", 1, 1.0, REACH_RP, CASCADE_SWAP)
    assert cell_a["verdict"] == "restorable-at-R+"
    assert cell_b["verdict"] == "final-relative-to-R+"
    assert abs(cell_a["achieved"] - VIS_A_ANALYTIC) < ANALYTIC_TOL
    assert cell_b["achieved"] < FLATNESS_TOL


# --------------------------------------------------------------------------- #
# Leg 5 -- positive control at R++, priced
# --------------------------------------------------------------------------- #

def test_positive_control_restores_at_Rpp():
    pc = cached_analysis()["positive_control"]
    assert pc["all_B_restorable_at_Rpp"] is True
    assert pc["worst_restore_vs_visA"] < ANALYTIC_TOL
    for row in pc["rows"]:
        assert row["verdict"] == "restorable-at-R++"


def test_cascade_ledger_swap_closed_forms():
    pc = cached_analysis()["positive_control"]
    assert pc["worst_swap_cascade_work"] < FLATNESS_TOL
    assert pc["worst_Q_closed_form_residual"] < ANALYTIC_TOL
    assert pc["worst_sigma_identity_residual"] < IDENTITY_TOL
    assert pc["min_Sigma_over_sweep"] >= SIGMA_NONNEG_TOL
    assert "typed inf" in pc["beta_inf_typing"]


def test_beta0_cascade_books_departed_mutual_information():
    """W = 0, Q = 0, yet Sigma = H(3/7) nats = the departed mutual
    information (predeclared as expected, not spun as pricing)."""
    pc = cached_analysis()["positive_control"]
    assert abs(
        pc["sigma_beta0_m1_nats"] - SIGMA_CASC_BETA0_M1_NATS
    ) < ANALYTIC_TOL
    assert pc["sigma_beta0_equals_departed_mi_residual"] < IDENTITY_TOL
    assert "NOT" in pc["beta0_note"]
    led = cascade_ledger(1, 0.0, CASCADE_SWAP)
    assert abs(led["total_W"]) < FLATNESS_TOL
    assert abs(led["total_Q"]) < FLATNESS_TOL
    assert abs(led["total_Sigma_nats"] - SIGMA_CASC_BETA0_M1_NATS) < 1e-9


def test_cascade_heat_values_per_beta():
    for beta, q_exp in ((math.inf, 3.0 / 7.0),
                        (1.0, (3.0 / 7.0) * math.tanh(0.5)),
                        (0.0, 0.0)):
        led = cascade_ledger(2, beta, CASCADE_SWAP)
        for c in led["collisions"]:
            assert abs(c["Q_i"] - q_exp) < ANALYTIC_TOL
            assert abs(c["W_i"]) < FLATNESS_TOL


def test_restoration_work_refund_law_cross_module():
    pc = cached_analysis()["positive_control"]
    assert pc["worst_unswap_work"] < FLATNESS_TOL
    assert pc["worst_unwrite_refund_law_residual"] < ANALYTIC_TOL


def test_conditionality_conceded_in_positive_control():
    pc = cached_analysis()["positive_control"]
    assert "adopted, not derived" in pc["conditionality"]
    assert "named-unbuilt" in pc["conditionality"]


# --------------------------------------------------------------------------- #
# Leg 6 -- beta = 0 marginal blindness
# --------------------------------------------------------------------------- #

def test_every_proper_subset_marginal_blind_at_beta0():
    mb = cached_analysis()["marginal_blindness"]
    assert mb["worst_proper_subset_marginal_diff_beta0"] < FLATNESS_TOL
    # (2^3-2 + 2^4-2 + 2^5-2) x 2 cascades x 2 phases = 200.
    assert mb["proper_subsets_checked_beta0"] == 200


def test_full_joint_trace_distance_closed_forms():
    mb = cached_analysis()["marginal_blindness"]
    assert mb["worst_td_beta0_residual"] < ANALYTIC_TOL
    assert mb["worst_td_betainf_residual"] < ANALYTIC_TOL
    for m in M_SWEEP:
        assert abs(
            mb["td_full_joint_beta0_by_m"][str(m)] - TD_BETA0
        ) < ANALYTIC_TOL
        assert abs(
            mb["td_full_joint_betainf_swap_by_m"][str(m)]
            - TD_BETAINF_SWAP
        ) < ANALYTIC_TOL


def test_carrier_marginal_local_trace_fades_as_tanh():
    mb = cached_analysis()["marginal_blindness"]
    assert mb["worst_carrier_marginal_closed_form_residual"] < ANALYTIC_TOL
    rows = mb["carrier_marginal_rows"]
    assert abs(
        rows["inf"]["carrier_marginal_diff"] - 3.0 / 7.0
    ) < ANALYTIC_TOL
    assert rows["0.0"]["carrier_marginal_diff"] < FLATNESS_TOL


def test_cascade_variants_merge_at_beta0():
    mb = cached_analysis()["marginal_blindness"]
    assert mb["worst_cascade_variant_merge_beta0"] < FLATNESS_TOL


def test_mutual_information_closed_forms():
    mb = cached_analysis()["marginal_blindness"]
    assert mb["worst_mi_closed_form_residual"] < ANALYTIC_TOL
    assert mb["worst_I_B_swap"] < FLATNESS_TOL
    row1 = mb["mutual_information_bits"]["1"]
    assert abs(row1["inf"]["I_A"] - 2.0 * H2_3_7) < ANALYTIC_TOL
    assert abs(row1["0.0"]["I_A"] - H2_3_7) < ANALYTIC_TOL
    assert abs(row1["inf"]["I_B_broadcast"] - H2_3_7) < ANALYTIC_TOL
    assert row1["0.0"]["I_B_broadcast"] < FLATNESS_TOL
    assert "no answer" in mb["finding"]


# --------------------------------------------------------------------------- #
# Leg 7 -- absorber battery
# --------------------------------------------------------------------------- #

def test_stipulated_flag_moves_nothing():
    bt = cached_analysis()["battery"]
    assert bt["t400_stipulated_flag"]["flag_state_diff"] == 0.0
    assert bt["t400_stipulated_flag"]["flag_moved_capability"] is False
    assert "not modeled" in bt["t400_stipulated_flag"]["answer"]


def test_matched_declared_fields_and_label_free_verdict():
    bt = cached_analysis()["battery"]
    mf = bt["t402_t406_matched_fields"]
    assert mf["declared_fields_equal"] is True
    assert mf["verdict_swaps_with_input"] is True
    assert "ledger entry" in mf["differing_item"]
    assert "never stipulated" in mf["differing_item"]


def test_joint_record_completion_answered_both_ways():
    bt = cached_analysis()["battery"]
    ans = bt["t401_joint_record"]["answer"]
    assert "product" in ans
    assert "transverse" in ans


def test_resource_projection_concession_and_residues():
    bt = cached_analysis()["battery"]
    rp = bt["t398_t404_resource_projection"]
    assert rp["profile_A"] == ("final-relative-to-R", "restorable-at-R+")
    assert rp["profile_B"] == (
        "final-relative-to-R", "final-relative-to-R+", "restorable-at-R++"
    )
    assert "conceded" in rp["conceded"]
    assert "superchannels" in rp["residue_a_causal_indexing"]
    assert "demotes" in rp["residue_a_causal_indexing"]
    assert "Blackwell" in rp["residue_b_locally_hidden"]


def test_enlargement_and_markers_and_light_cone_answers():
    bt = cached_analysis()["battery"]
    assert "priced" in bt["t399_enlarged_state"]["answer"]
    assert "no class markers" in bt["t397_sbs_markers"]["answer"].lower()
    assert "not a light cone" in bt["lieb_robinson"]["answer"]
    assert "re-scopes" in bt["re_scope_clause"]


# --------------------------------------------------------------------------- #
# Leg 8 -- guardrails
# --------------------------------------------------------------------------- #

def test_q1d_guardrail_asserted_numerically():
    q1d = cached_analysis()["q1d"]
    assert q1d["declared_record_invariance"] < FLATNESS_TOL
    assert q1d["worst_no_signal_out_of_R"] < FLATNESS_TOL
    assert q1d["worst_teeth_closed_form_residual"] < ANALYTIC_TOL
    teeth_inf = q1d["teeth_by_beta"]["inf"][
        "enlarged_protocol_moves_tier1_marginal"
    ]
    assert abs(teeth_inf - 3.0 / 7.0) < ANALYTIC_TOL  # the house tooth
    teeth_0 = q1d["teeth_by_beta"]["0.0"][
        "enlarged_protocol_moves_tier1_marginal"
    ]
    assert teeth_0 < FLATNESS_TOL  # marginal blindness at beta = 0


def test_beta0_tooth_is_the_visibility_jump():
    jump = cached_analysis()["q1d"]["beta0_visibility_jump"]
    assert jump["achieved_at_R"] < FLATNESS_TOL
    assert abs(jump["achieved_at_Rplus"] - VIS_A_ANALYTIC) < ANALYTIC_TOL


def test_r1_untouched_not_a_light_cone():
    note = cached_analysis()["q1d"]["r1_note"]
    assert "R1 untouched" in note
    assert "not a light cone" in note
    assert "Lieb-Robinson" in note


# --------------------------------------------------------------------------- #
# Discipline -- verdict vocabulary, failure legs, open-problem mapping
# --------------------------------------------------------------------------- #

def test_verdict_language_and_tags():
    res = cached_analysis()
    assert tuple(res["verdict_tags"]) == VERDICT_TAGS
    assert res["verdict_tags"][-1] == "no_claim_promotion"
    lang = res["verdict_language"]
    assert "departed-record capability discriminator holds" in lang
    assert "pause for Joe" in lang
    assert "no claim promotion" in lang
    assert "named-unbuilt" in lang
    assert "adopted, not derived" in lang  # the conditionality concession
    assert "finite-witness" in lang


def test_open_problem_criterion_quoted_and_realized():
    res = cached_analysis()
    assert res["open_problem_criterion"] == OPEN_PROBLEM_CRITERION
    assert "R-supported interventions" in OPEN_PROBLEM_CRITERION
    assert "boundary-crossing task menu" in OPEN_PROBLEM_CRITERION


def test_failure_legs_consistent_with_computed_facts():
    res = cached_analysis()
    fl = res["failure_legs"]
    se = res["separation"]
    assert fl["equality_fails"]["halting"] is True
    assert fl["positive_control_fails"]["halting"] is True
    assert fl["separation_not_certified_B"]["fired_primary_swap"] == (
        not se["B_swap_all_final_at_Rplus"]
        or not se["worst_B_swap_phi_cert"] < FLATNESS_TOL
    )
    assert (
        "conditionality_conceded"
        in fl["boundary_physicality_reduces_to_declaration"]
    )


def test_menu_has_no_co_present_exclusion():
    res = cached_analysis()
    assert "ALL CPTP" in res["menu_declaration"]
    assert "no exclusion clause" in res["menu_declaration"]


def test_verdicts_are_reach_relative_vocabulary():
    cell = verdict_cell("B", 1, math.inf, REACH_RP, CASCADE_SWAP)
    assert cell["verdict"] == "final-relative-to-R+"
    cell = verdict_cell("B", 1, math.inf, REACH_RPP, CASCADE_SWAP)
    assert cell["verdict"] == "restorable-at-R++"
    cell = verdict_cell("A", 1, math.inf, REACH_R)
    assert cell["verdict"] == "final-relative-to-R"
