"""Tests for T393: Causal Forcing of the Access Asymmetry.

Asserts, to numerical precision, the seven verified items of the spec:

1. Full ordinary event-level record identical between preparations A and B
   (max diff exactly 0).
2. T162 SBS closure key AND full SBS signature over F1..F4 identical (max
   diff exactly 0), both D1-finalized.
3. THE FORCING THEOREM: for the undo class = ALL channels supported on the
   control region at final time, prep B admits no recovery -- certified by
   exact phi-independence of the region conditional state (sweep over >= 5
   phi values including incommensurate ones, max pairwise diff < 1e-12),
   plus an ILLUSTRATIVE Haar spot-check (>= 50 random in-region unitaries,
   none restoring phase-locked conditional X-visibility above 0.05). The
   certificate, not the sampling, carries the result. Prep A: full in-region
   undo restores visibility to the T392 value 4*sqrt(3)/7.
4. Typed axis: H(A) finite, H(B) = inf grounded in the causal certificate;
   both verdict classes populated.
5. Auxiliary channel = Z readout at the far end of the chain: positive lift
   across the T155 three-loss family, CMI > 0; T137 downstream-transform
   null exactly zero.
6. B' null control (uncorrelated emission): bitwise identical to A on all
   verdict-relevant quantities, while the emission itself is real.
7. Region-boundary sanity: enlarging the undo support across the causal
   boundary restores recovery in B exactly; the recovery window closes
   exactly at the escape step.

Record-labeling convention: all outcome tuples are index-sorted; ordinary
record tuples read (S, M) with S = qubit 0 < M = qubit 1.
"""

from __future__ import annotations

import math

import numpy as np

from models.causal_forcing_access_asymmetry import (
    CONTROL_REGION,
    ESCAPE_STEP,
    FRAGMENT_QUBITS,
    HAAR_SAMPLES,
    HAAR_VISIBILITY_CEILING,
    N_STEPS,
    PHI_CERT,
    REGION_RADIUS,
    V_STAR,
    boundary_enlarged_undo,
    boundary_enlargement,
    bprime_control,
    cached_analysis,
    chain_excitation,
    d1_finalized_from_key,
    emission_confound_mixture,
    feedback_channel_check,
    fragment_undo,
    full_sbs_signature,
    lightcone_table,
    manufactured_coherence_control,
    max_pairwise_phi_diff,
    mode_site_at_step,
    ordinary_record_distribution,
    phi_locked_visibility,
    prepare,
    raw_visibility_after,
    record_max_diff,
    region_conditional_state,
    reversal_cost,
    sbs_closure_key,
    sbs_signature_max_diff,
    screening_certificate,
    verdict_from_cost,
)

TOL = 1e-12
T392_VISIBILITY = 4.0 * math.sqrt(3.0) / 7.0  # = 2 cos(t/2)/(1+cos(t/2)^2), t=pi/3


# --------------------------------------------------------------------------- #
# (0) Causal geometry is time-indexed, not chosen per preparation
# --------------------------------------------------------------------------- #

def test_lightcone_table_time_indexes_region_membership():
    rows = lightcone_table()
    assert [r["mode_site"] for r in rows] == [0, 1, 2]
    assert [r["in_control_region"] for r in rows] == [True, True, False]
    assert mode_site_at_step(ESCAPE_STEP) > REGION_RADIUS
    # The declared control region is fixed once, for every preparation.
    assert len(CONTROL_REGION) == 8


# --------------------------------------------------------------------------- #
# (1) Ordinary-record equality
# --------------------------------------------------------------------------- #

def test_ordinary_event_level_record_identical_A_vs_B():
    psi_a = prepare("A")
    psi_b = prepare("B")
    assert ordinary_record_distribution(psi_a), "record must be nonempty"
    assert record_max_diff(psi_a, psi_b) == 0.0


def test_ordinary_record_is_a_normalized_distribution():
    for kind in ("A", "B", "Bprime"):
        dist = ordinary_record_distribution(prepare(kind))
        assert abs(sum(dist.values()) - 1.0) <= TOL


# --------------------------------------------------------------------------- #
# (2) SBS closure key AND full SBS signature equality
# --------------------------------------------------------------------------- #

def test_sbs_closure_keys_identical_and_finalized():
    key_a = sbs_closure_key(prepare("A"))
    key_b = sbs_closure_key(prepare("B"))
    assert key_a.as_tuple() == key_b.as_tuple()
    for key in (key_a, key_b):
        assert key.objectivity_status == "sbs_objective"
        assert key.partition_visible is True
        assert key.support_count == 4
        assert d1_finalized_from_key(key) is True


def test_full_sbs_signature_identical_A_vs_B():
    psi_a = prepare("A")
    psi_b = prepare("B")
    assert sbs_signature_max_diff(psi_a, psi_b) == 0.0
    # Every declared fragment is a perfect pointer copy in both preparations.
    for sig in (full_sbs_signature(psi_a), full_sbs_signature(psi_b)):
        for dist in sig["fragment_distinguishabilities"]:
            assert abs(dist - 1.0) <= 1e-9


# --------------------------------------------------------------------------- #
# (3) The forcing theorem
# --------------------------------------------------------------------------- #

def test_full_in_region_undo_restores_A_to_t392_value():
    undo = fragment_undo(FRAGMENT_QUBITS)
    locked = phi_locked_visibility("A", undo)
    raw = raw_visibility_after("A", undo)
    assert abs(locked - T392_VISIBILITY) <= 1e-9
    assert abs(raw - T392_VISIBILITY) <= 1e-9
    assert locked >= V_STAR


def test_in_region_undo_fails_in_B():
    undo = fragment_undo(FRAGMENT_QUBITS)
    assert phi_locked_visibility("B", undo) <= TOL
    assert raw_visibility_after("B", undo) <= TOL


def test_forcing_certificate_phi_independence_in_B():
    # THE PROOF: the region conditional state -- the object EVERY channel
    # supported on the control region acts on -- is exactly independent of
    # the prepared phase phi in preparation B. Sweep includes incommensurate
    # values (1.0 and sqrt(2) radians).
    assert len(PHI_CERT) >= 5
    assert 1.0 in PHI_CERT and math.sqrt(2.0) in PHI_CERT
    assert max_pairwise_phi_diff(region_conditional_state, "B") < 1e-12
    # ... while in A the same object is genuinely phi-dependent.
    assert max_pairwise_phi_diff(region_conditional_state, "A") > 0.1


def test_haar_spot_check_is_illustrative_and_null():
    # BELT-AND-SUSPENDERS ONLY: the phi-independence certificate above is
    # what carries the result; this sampling merely illustrates it.
    res = cached_analysis()
    assert res.haar["samples"] >= 50
    assert res.haar["samples"] == HAAR_SAMPLES
    assert res.haar["max_phi_locked_visibility"] < HAAR_VISIBILITY_CEILING


def test_manufactured_coherence_is_disclosed_and_nulled_by_phase_locking():
    # T392's disclosed exploit: raw visibility 1.0 is manufacturable in-region
    # in prep B, which is exactly why raw visibility is NOT the recovery
    # figure of merit. The phase-locked metric nulls it.
    ctrl = manufactured_coherence_control()
    assert ctrl["raw_visibility"] > 0.99
    assert ctrl["phi_locked_visibility"] <= TOL


def test_non_unitary_in_region_channel_also_fails():
    # The undo class is ALL channels, not just unitaries: a representative
    # measure-and-feed-back channel on in-region qubits recovers nothing.
    assert feedback_channel_check() <= TOL


# --------------------------------------------------------------------------- #
# (4) Typed axis H and verdict map
# --------------------------------------------------------------------------- #

def test_typed_axis_H_finite_for_A_infinite_for_B():
    h_a = reversal_cost("A")
    h_b = reversal_cost("B")
    assert math.isfinite(h_a)
    assert h_a == 4.0  # all four accessible fragments needed
    assert math.isinf(h_b)


def test_verdict_map_splits_with_both_classes_populated():
    v_a = verdict_from_cost(reversal_cost("A"))
    v_b = verdict_from_cost(reversal_cost("B"))
    assert v_a == "recoverable-in-control-region"
    assert v_b == "final-relative-to-control-region"
    cert = screening_certificate()
    assert cert["both_classes_populated"] is True
    assert len(cert["class_support"]) == 2
    for mass in cert["class_support"].values():
        assert mass > 0.0


# --------------------------------------------------------------------------- #
# (5) Auxiliary channel at the far end of the chain
# --------------------------------------------------------------------------- #

def test_far_end_detector_gives_positive_lift_across_loss_family():
    cert = screening_certificate()
    assert cert["all_losses_positive_lift"] is True
    assert len(cert["lift_by_loss"]) >= 3
    for name, vals in cert["lift_by_loss"].items():
        assert vals["lift"] > 0.0, f"loss {name} showed no lift"
        # T392 comparability: identical structure, identical exact lift.
        assert abs(vals["lift"] - 0.25) <= 1e-9


def test_conditional_mutual_information_matches_t392():
    cert = screening_certificate()
    assert cert["cmi_positive"] is True
    assert abs(cert["cmi_bits"] - 0.5) <= 1e-9


def test_t137_downstream_transform_null_is_exactly_zero():
    cert = screening_certificate()
    assert cert["null_all_zero_lift"] is True
    for name, vals in cert["null_lift_by_loss"].items():
        assert abs(vals["lift"]) <= TOL, f"null loss {name} leaked lift"
    assert abs(cert["null_cmi_bits"]) <= TOL


def test_emission_confound_mixture_disclosure():
    # Honest boundary, disclosed rather than hidden: at the uniform {A,B,B'}
    # prior the 0-1 and false-final-costly lifts degenerate to exactly zero,
    # while CMI and the false-recover-costly lift stay positive. The T155
    # claim is scoped to the declared A/B family (matching T392).
    mix = emission_confound_mixture()
    assert abs(mix["lift_by_loss"]["zero_one"]["lift"]) <= TOL
    assert abs(mix["lift_by_loss"]["false_final_costly"]["lift"]) <= TOL
    assert mix["lift_by_loss"]["false_recover_costly"]["lift"] > 0.3
    assert mix["cmi_bits"] > 0.2


# --------------------------------------------------------------------------- #
# (6) B' emission null control
# --------------------------------------------------------------------------- #

def test_bprime_identical_to_A_on_all_verdict_relevant_quantities():
    ctrl = bprime_control()
    assert ctrl["record_max_diff"] == 0.0
    assert ctrl["sbs_signature_max_diff"] == 0.0
    assert ctrl["region_conditional_state_max_diff"] == 0.0
    assert abs(
        ctrl["full_undo_locked_visibility_A"]
        - ctrl["full_undo_locked_visibility_Bprime"]
    ) <= TOL
    assert ctrl["H_A"] == ctrl["H_Bprime"] == 4.0
    assert ctrl["verdict_A"] == ctrl["verdict_Bprime"]


def test_bprime_emission_is_real_but_innocuous():
    # Emission happens in B' (a full excitation escapes -- MORE chain energy
    # than B carries), yet nothing verdict-relevant splits: emission per se,
    # and its energy signature, are not doing the work.
    ctrl = bprime_control()
    assert ctrl["emission_is_real_global_statevector_diff"] > 0.1
    assert abs(chain_excitation("A") - 0.0) <= TOL
    assert abs(chain_excitation("B") - 0.5) <= TOL
    assert abs(chain_excitation("Bprime") - 1.0) <= TOL


# --------------------------------------------------------------------------- #
# (7) Recovery window and region-boundary sanity
# --------------------------------------------------------------------------- #

def test_recovery_window_closes_exactly_at_escape_step():
    res = cached_analysis()
    for step in range(N_STEPS + 1):
        vals = res.window[step]
        if step < ESCAPE_STEP:
            assert vals["in_control_region"] is True
            assert vals["locked_visibility_in_region_undo"] >= V_STAR
        else:
            assert vals["in_control_region"] is False
            assert vals["locked_visibility_in_region_undo"] <= TOL


def test_boundary_enlargement_restores_recovery_in_B():
    # Counterfactually include the escaped site: recovery returns EXACTLY to
    # the preparation-A value. The split is the causal boundary, nothing else.
    res = boundary_enlargement()
    assert res["locked_visibility_B_with_escaped_site"] >= V_STAR
    assert res["abs_diff"] < 1e-12
    assert res["enlarged_state_phi_dependence_B"] > 0.1
    # And directly: the enlarged undo on the conditioned state.
    assert phi_locked_visibility("B", boundary_enlarged_undo) >= V_STAR


# --------------------------------------------------------------------------- #
# Top-level verdict
# --------------------------------------------------------------------------- #

def test_forcing_holds_end_to_end():
    res = cached_analysis()
    assert res.record_max_diff_AB == 0.0
    assert res.sbs_signature_max_diff_AB == 0.0
    assert res.cert_max_pairwise_diff_B < 1e-12
    assert res.cert_max_pairwise_diff_A > 0.1
    assert res.vis_A_locked >= V_STAR
    assert res.vis_B_locked <= TOL
    assert res.visibility_gap > 0.5
    assert res.verdict_A != res.verdict_B
    assert res.screening["all_losses_positive_lift"] is True
    assert res.screening["cmi_positive"] is True
    assert res.screening["null_all_zero_lift"] is True
    assert res.forcing_holds is True


def test_verdict_language_is_restrained_house_vocabulary():
    res = cached_analysis()
    text = res.verdict_language.lower()
    assert "prove" not in text
    assert "finite" in text
    assert "causal" in text
    assert "conditional on emission" in text


# --------------------------------------------------------------------------- #
# (8) v0.1.1 hardening 1: boundary-location sweep (post-hostile-review)
# --------------------------------------------------------------------------- #

from models.causal_forcing_access_asymmetry import (  # noqa: E402
    PARTIAL_AMPLITUDE_ALPHAS,
    boundary_location_sweep,
    in_region_channel_bound,
    partial_amplitude_robustness,
)


def test_boundary_sweep_smaller_region_forces_at_its_own_escape_step():
    # Stipulation-regress answer, earned: with a SMALLER control region
    # (r = 0), the mode is already outside at step 1, and the same exact
    # phi-independence certificate fires there -- the forcing tracks the
    # declared boundary, wherever it is placed.
    sweep = boundary_location_sweep()
    assert sweep["r0_step1_mode_outside_cert_diff_B"] < 1e-12


def test_boundary_sweep_smaller_region_stays_phi_dependent_while_inside():
    # ... and in the other direction: at step 0 the mode is still inside the
    # r = 0 region, and the region state is genuinely phi-dependent.
    sweep = boundary_location_sweep()
    assert sweep["r0_step0_mode_inside_cert_diff_B"] > 0.1


def test_boundary_sweep_larger_region_does_not_force_while_mode_inside():
    # With an ENLARGED region (r = 2) the whole chain is in-region: the mode
    # never escapes, and the region state stays phi-dependent even at step 2.
    # Every tested boundary placement yields the corresponding verdict in
    # both directions; the residual premise is only that the apparatus has
    # SOME bounded control region.
    sweep = boundary_location_sweep()
    assert sweep["r2_step2_mode_inside_cert_diff_B"] > 0.1


# --------------------------------------------------------------------------- #
# (9) v0.1.1 hardening 2: partial-amplitude robustness (staged v0.2 content)
# --------------------------------------------------------------------------- #

def test_partial_amplitude_locked_recovery_matches_analytic_form():
    # Emission via controlled-Ry(alpha): the fragment-undo locked recovery in
    # prep B_alpha equals cos(alpha/2) * (4 sqrt(3) / 7) to numerical
    # precision -- the surviving no-emission amplitude carries all the
    # recoverable phase.
    res = partial_amplitude_robustness()
    assert [row["alpha_over_pi"] for row in res["sweep"]] == [
        alpha / math.pi for alpha in PARTIAL_AMPLITUDE_ALPHAS
    ]
    for row in res["sweep"]:
        analytic = math.cos(row["alpha_over_pi"] * math.pi / 2.0) * T392_VISIBILITY
        assert abs(row["fragment_undo_locked_visibility"] - analytic) <= 1e-9
        assert abs(
            row["fragment_undo_locked_visibility"]
            - row["analytic_cos_half_alpha_times_vis_A"]
        ) <= 1e-9


def test_partial_amplitude_channel_bound_certifies_thresholded_forcing():
    # Channel-INDEPENDENT upper bound (Hoelder + CPTP trace-norm
    # contractivity) on ANY in-region channel's locked visibility: below the
    # predeclared v* = 0.9 for every alpha >= 0.75 pi. Forcing at threshold
    # v* is certified across the sweep; the exact-zero form is the
    # alpha = pi idealization of this robust fact.
    res = partial_amplitude_robustness()
    assert res["v_star"] == V_STAR == 0.9
    bounds = {
        round(row["alpha_over_pi"], 2): row["in_region_channel_bound"]
        for row in res["sweep"]
    }
    for row in res["sweep"]:
        assert row["in_region_channel_bound"] < V_STAR
        assert row["bound_below_v_star"] is True
    # Reviewer-validated magnitudes (hostile-review scratch).
    assert abs(bounds[0.75] - 0.76) <= 0.01
    assert abs(bounds[0.9] - 0.31) <= 0.01
    assert abs(bounds[0.98] - 0.062) <= 0.01
    assert bounds[1.0] <= 1e-12
    # Wiring check: the reported value is the direct bound computation.
    direct = in_region_channel_bound("B", alpha=0.75 * math.pi)
    assert abs(bounds[0.75] - direct) <= 1e-12


def test_partial_amplitude_alpha_pi_is_the_cnot_idealization():
    # alpha = pi reproduces the CNOT preparation statevector exactly (the
    # chain target starts in |0>), and the bound is not vacuous: prep A's
    # achievable recovery respects its own channel bound, while the exact
    # CNOT preparation's bound is numerically zero.
    res = partial_amplitude_robustness()
    assert res["alpha_pi_equals_cnot_statevector_diff"] <= 1e-12
    assert res["channel_bound_B_cnot"] <= 1e-12
    assert res["channel_bound_A_sanity"] >= T392_VISIBILITY
