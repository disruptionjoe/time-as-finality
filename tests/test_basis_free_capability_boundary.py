"""Tests for T408: Basis-Free Flat Pair and the Physical Capability Boundary.

Asserts, to numerical precision, the three parts of the spec:

Part 1 (basis-free flat pair): the FULL record-region state rho_R is
identical between preparations A and B as an operator (< 1e-12; computes to
~1e-16) at every certificate phase, every lightcone step, and every swept
leak amplitude -- so every POVM on R, in every basis, and every R-supported
intervention-then-readout statistic is exactly equal -- while the capability
under the ONE fixed accessible-zone menu splits (A restores 4*sqrt(3)/7 >=
v* = 0.9; B is certified unrecoverable for ALL channels supported on the
zone). The menu-support obstruction lemma is witnessed in both directions.

Part 2 (graded curve): the entire T393-style alpha sweep sits on one
basis-free flat family; achieved recovery equals cos(alpha/2) * 4sqrt(3)/7;
the channel-independent trace-norm bound certifies the no-recovery side at
each alpha where it bites; exact complementarity with the escaped holder's
branch distinguishability sin(alpha/2).

Part 3 (dissipation bookkeeping, T142 conventions): capability restoration
in A is a zero-Landauer-floor correlated uncopy; blind reset erases the
record at a finite floor but restores NO capability (deletion is not
definalization); B's in-zone restoration cost is an empty-feasible-set
infimum typed as an ACCESS obstruction, not a work divergence. Bookkeeping
only; no thermodynamic theorem.

Register order (index-sorted): S, M, F1, F2, F3, F4, AX, C0, C1, C2.
"""

from __future__ import annotations

import math

import numpy as np

from models.basis_free_capability_boundary import (
    ACCESS_ZONE,
    ALPHA_SWEEP,
    ESCAPED,
    FLATNESS_TOL,
    HAAR_VISIBILITY_CEILING,
    HOLDERS_IN_REACH,
    N_QUBITS,
    N_STEPS,
    RECORD_REGION,
    THETA,
    V_STAR,
    VERDICT_FINAL,
    VERDICT_RECOVERABLE,
    VERDICT_TAGS,
    VIS_A_ANALYTIC,
    Z_ACTIVE,
    cached_analysis,
    landauer_bound_bits,
    locked_visibility,
    prepare,
    EXTENDED_UNDO,
)


# --------------------------------------------------------------------------- #
# Fixture / layout
# --------------------------------------------------------------------------- #

def test_register_layout_and_budget():
    assert N_QUBITS == 10  # within the 10-qubit budget, exact statevector
    assert set(RECORD_REGION).issubset(set(ACCESS_ZONE))
    assert set(ESCAPED).isdisjoint(set(ACCESS_ZONE))
    assert set(HOLDERS_IN_REACH).issubset(set(ACCESS_ZONE))
    psi = prepare("A", 1.0)
    assert abs(float(np.real(psi.conj() @ psi)) - 1.0) < 1e-12


def test_shared_core_constants_imported_unchanged():
    assert THETA == math.pi / 3.0  # T392's weak coupling, unchanged
    assert V_STAR == 0.9  # T392/T393's threshold, unchanged
    assert abs(VIS_A_ANALYTIC - 4.0 * math.sqrt(3.0) / 7.0) < 1e-15


def test_alpha_zero_is_prep_A_exactly():
    for phi in (0.0, 1.0):
        diff = float(np.max(np.abs(prepare("B", phi, alpha=0.0) - prepare("A", phi))))
        assert diff < 1e-14


def test_determinism():
    a1 = prepare("B", math.sqrt(2.0))
    a2 = prepare("B", math.sqrt(2.0))
    assert float(np.max(np.abs(a1 - a2))) == 0.0
    v1 = locked_visibility("A", EXTENDED_UNDO)
    v2 = locked_visibility("A", EXTENDED_UNDO)
    assert v1 == v2


# --------------------------------------------------------------------------- #
# Part 1 -- basis-free flat pair
# --------------------------------------------------------------------------- #

def test_region_flatness_operator_equality():
    fl = cached_analysis()["flatness"]
    assert fl["max_operator_diff_over_preps_phases_alphas"] < FLATNESS_TOL
    assert fl["conditional_R_active_diff"] < FLATNESS_TOL
    assert fl["flat"]


def test_region_flatness_all_povm_reading():
    """Trace distance < 1e-12 certifies EVERY POVM on R and every R-supported
    channel-then-readout composition at once (CPTP contractivity); the seeded
    random-basis spot check is illustrative belt-and-suspenders."""
    fl = cached_analysis()["flatness"]
    assert fl["max_trace_distance"] < FLATNESS_TOL
    assert fl["random_basis_spot_check"]["max_prob_diff"] < FLATNESS_TOL


def test_region_flatness_at_every_lightcone_step():
    fl = cached_analysis()["flatness"]
    assert fl["max_operator_diff_per_step"] < FLATNESS_TOL


def test_region_phi_independence_disclosure():
    """The annex copy dephases the record region completely: rho_R is also
    phi-independent WITHIN each preparation (the phase lives in annex/chain
    correlations, not in R)."""
    fl = cached_analysis()["flatness"]
    assert fl["phi_flatness_within_A"] < FLATNESS_TOL
    assert fl["phi_flatness_within_B"] < FLATNESS_TOL


def test_declared_z_readout_flat_a_fortiori():
    fl = cached_analysis()["flatness"]
    assert fl["declared_z_readout_diff"] < FLATNESS_TOL


def test_capability_split_under_one_fixed_menu():
    cap = cached_analysis()["capability"]
    assert cap["vis_A_locked"] >= V_STAR
    assert abs(cap["vis_A_locked"] - VIS_A_ANALYTIC) < 1e-12
    assert cap["vis_B_locked"] <= 1e-12
    assert cap["capability_gap"] > 0.98


def test_zone_certificate_and_channel_bound_B():
    """All-channel impossibility on the FULL menu support: the M-conditioned
    zone state of B is exactly phi-independent, and the channel-independent
    trace-norm bound is numerically zero (far below v*)."""
    cap = cached_analysis()["capability"]
    assert cap["zone_cert_B"] < FLATNESS_TOL
    assert cap["zone_bound_B"] < V_STAR
    assert cap["zone_bound_B"] < 1e-12


def test_zone_phi_dependence_teeth_A():
    cap = cached_analysis()["capability"]
    assert cap["zone_cert_A_teeth"] > 0.1
    assert cap["zone_bound_A_sanity"] >= cap["vis_A_locked"] - 1e-12


def test_r_only_menu_null_annex_necessity():
    """On the record region alone BOTH preparations are certified
    unrecoverable: the flat surface is not where recovery happens, and A's
    capability genuinely needs the annex."""
    null = cached_analysis()["capability"]["r_only_null"]
    assert null["cert_A"] < FLATNESS_TOL
    assert null["cert_B"] < FLATNESS_TOL
    assert null["bound_A"] < V_STAR
    assert null["bound_B"] < V_STAR


def test_reversal_cost_axis_and_verdict_split():
    cap = cached_analysis()["capability"]
    assert cap["H_A"] == 5.0  # all four fragments AND the annex needed
    assert cap["best_four_holder_visibility_A"] <= 1e-12
    assert math.isinf(cap["H_B"])
    assert cap["verdict_A"] == VERDICT_RECOVERABLE
    assert cap["verdict_B"] == VERDICT_FINAL


def test_haar_spot_check_illustrative():
    haar = cached_analysis()["capability"]["haar_spot_check"]
    assert haar["max_locked_visibility"] < HAAR_VISIBILITY_CEILING


def test_manufactured_coherence_null():
    manu = cached_analysis()["capability"]["manufactured_coherence_control"]
    assert manu["raw_visibility"] > 0.99  # the exploit scores on raw...
    assert manu["locked_visibility"] < 1e-12  # ...and is nulled when locked


def test_bprime_emission_null():
    bp = cached_analysis()["bprime"]
    assert bp["abs_diff_from_A"] < 1e-12
    assert bp["region_state_diff_from_A"] < FLATNESS_TOL
    assert bp["chain_excitation"]["Bprime"] > 0.99  # the emission is real
    assert bp["chain_excitation"]["A"] < 1e-12


def test_recovery_window_closes_at_escape():
    win = cached_analysis()["window"]["window"]
    assert win[0]["locked_visibility_in_zone_undo"] >= V_STAR
    assert win[1]["locked_visibility_in_zone_undo"] >= V_STAR
    assert win[N_STEPS]["locked_visibility_in_zone_undo"] <= 1e-12
    # The certificate fires exactly when (and only when) the mode is out.
    assert win[0]["zone_cert_diff"] > 0.1
    assert win[1]["zone_cert_diff"] > 0.1
    assert win[N_STEPS]["zone_cert_diff"] < FLATNESS_TOL


def test_counterfactual_boundary_enlargement():
    win = cached_analysis()["window"]
    assert win["abs_diff_from_A"] < 1e-12
    assert win["enlarged_cert_diff_B"] > 0.1


def test_obstruction_lemma_tail_witnesses():
    """Flat-on-menu-support forces no gap: a unitary on the escaped tail
    leaves the zone family identical and every capability value identical."""
    tails = cached_analysis()["obstruction"]["tail_witnesses"]
    for base in ("A", "B"):
        t = tails[base]
        assert t["zone_family_diff"] < FLATNESS_TOL
        assert t["vis_diff"] < 1e-12
        assert t["bound_diff"] < 1e-12
        assert (t["H_base"] == t["H_tail"]) or (
            math.isinf(t["H_base"]) and math.isinf(t["H_tail"])
        )


def test_obstruction_trace_location():
    """The statistical trace the capability gap requires is real (zone trace
    distance ~ 0.49), lives in zone coherences, and is invisible both to
    every measurement on R and to the full joint Z-basis readout on the
    whole zone (and to every single-qubit zone marginal)."""
    obs = cached_analysis()["obstruction"]
    assert obs["zone_trace_distance_A_vs_B"] > 0.1
    assert obs["zone_joint_z_readout_diff"] < FLATNESS_TOL
    assert obs["zone_single_qubit_marginal_diff"] < FLATNESS_TOL


# --------------------------------------------------------------------------- #
# Part 2 -- graded curve
# --------------------------------------------------------------------------- #

def test_graded_region_flatness_every_alpha():
    rows = cached_analysis()["graded"]["sweep"]
    assert len(rows) == len(ALPHA_SWEEP)
    for row in rows:
        assert row["region_flatness_diff"] < FLATNESS_TOL


def test_graded_achieved_matches_analytic_and_is_monotone():
    rows = cached_analysis()["graded"]["sweep"]
    prev = None
    for row in rows:
        assert abs(
            row["achieved_locked_visibility"]
            - row["analytic_cos_half_alpha_times_vis_A"]
        ) < 1e-9
        if prev is not None:
            assert row["achieved_locked_visibility"] <= prev + 1e-12
        prev = row["achieved_locked_visibility"]


def test_graded_bound_certification_classes():
    """The three-band structure of the graded boundary: protocol-feasible at
    low alpha, all-channel-certified infeasible at high alpha, and an honest
    undetermined band where the bound does not bite (T393's open alpha* card)."""
    rows = {round(r["alpha_over_pi"], 4): r for r in cached_analysis()["graded"]["sweep"]}
    assert rows[0.0]["threshold_restoration"] == "feasible_zero_cost"
    assert rows[0.25]["threshold_restoration"] == "feasible_zero_cost"
    assert rows[0.5]["threshold_restoration"] == "undetermined_by_bound"
    for f in (0.7, 0.75, 0.9, 0.98, 1.0):
        assert rows[f]["threshold_restoration"] == "certified_infeasible"
        assert rows[f]["channel_bound_zone"] < V_STAR
    for row in rows.values():
        assert row["channel_bound_zone"] >= row["achieved_locked_visibility"] - 1e-9


def test_graded_complementarity_exact():
    rows = cached_analysis()["graded"]["sweep"]
    for row in rows:
        assert row["complementarity_residual"] < 1e-9
        alpha = row["alpha_over_pi"] * math.pi
        assert abs(
            row["escaped_distinguishability"] - math.sin(alpha / 2.0)
        ) < 1e-9


def test_escaped_holevo_curve():
    rows = cached_analysis()["graded"]["sweep"]
    h2_3_7 = -(3 / 7) * math.log2(3 / 7) - (4 / 7) * math.log2(4 / 7)
    assert rows[0]["escaped_holevo_bits"] < 1e-9
    assert abs(rows[-1]["escaped_holevo_bits"] - h2_3_7) < 1e-9
    prev = -1.0
    for row in rows:
        assert row["escaped_holevo_bits"] >= prev - 1e-12
        prev = row["escaped_holevo_bits"]


def test_alpha_feasibility_threshold_analytic():
    graded = cached_analysis()["graded"]
    expected = 2.0 * math.acos(V_STAR / VIS_A_ANALYTIC)
    assert abs(graded["alpha_feasible_analytic"] - expected) < 1e-12
    for row in graded["sweep"]:
        alpha = row["alpha_over_pi"] * math.pi
        if row["threshold_restoration"] == "feasible_zero_cost":
            assert alpha <= expected + 1e-9
        else:
            assert alpha > expected


# --------------------------------------------------------------------------- #
# Part 3 -- dissipation bookkeeping (T142 conventions)
# --------------------------------------------------------------------------- #

def test_ledger_restore_A_correlated_uncopy():
    led = cached_analysis()["ledger"]["restore_A"]
    assert led["mode"] == "correlated_uncopy"
    assert led["erased_bits"] == 0
    assert led["beta_work_lower_bound"] == 0.0
    assert led["achieved_locked_visibility"] >= V_STAR
    assert led["holders_uncomputed"] == 5
    assert led["t142_verdict"] == "reversible_when_full_microstate_available"


def test_ledger_blind_reset_deletion_is_not_definalization():
    led = cached_analysis()["ledger"]["blind_reset_A"]
    assert led["capability_after_reset"] < 1e-12
    assert led["record_deleted_residual_distinguishability"] < 1e-12
    assert led["deletion_is_not_definalization"]
    assert led["beta_work_lower_bound_naive"] == landauer_bound_bits(5)
    h2_3_7 = -(3 / 7) * math.log2(3 / 7) - (4 / 7) * math.log2(4 / 7)
    assert abs(led["joint_record_bits_given_M0"] - h2_3_7) < 1e-9
    assert abs(led["joint_record_bits_unconditioned"] - 1.0) < 1e-9


def test_ledger_B_in_zone_empty_feasible_set():
    led = cached_analysis()["ledger"]["restore_B_in_zone"]
    assert led["feasible_in_zone"] is False
    assert math.isinf(led["min_beta_work"])
    assert led["certificates"]["zone_phi_independence"] < FLATNESS_TOL
    assert led["certificates"]["zone_channel_bound"] < V_STAR
    assert "access" in led["limiting_resource"]
    assert "not work" in led["limiting_resource"]
    assert "NOT a divergent" in led["not_a_work_bound"]


def test_ledger_counterfactual_enlargement():
    led = cached_analysis()["ledger"]["restore_B_counterfactual"]
    assert led["holders_uncomputed"] == 6
    assert led["erased_bits"] == 0
    assert led["achieved_locked_visibility"] >= V_STAR
    assert led["abs_diff_from_A"] < 1e-12
    assert led["blind_reset_beta_work_naive"] == landauer_bound_bits(6)


def test_ledger_scope_is_bookkeeping_only():
    led = cached_analysis()["ledger"]
    assert "not a thermodynamic theorem" in led["correspondence"]
    assert "Tier-2" in led["tier2_card"]
    assert "NOT built here" in led["tier2_card"]


# --------------------------------------------------------------------------- #
# Guardrails and verdict discipline
# --------------------------------------------------------------------------- #

def test_q1d_guardrail_asserted_numerically():
    q1d = cached_analysis()["q1d"]
    assert q1d["declared_readout_invariance"] < FLATNESS_TOL
    assert q1d["no_signal_out_in_zone_undo"] < FLATNESS_TOL
    assert q1d["enlarged_undo_moves_escaped_marginal_teeth"] > 0.1
    assert q1d["zone_trace_distance_teeth"] > 0.1
    assert "R1 untouched" in q1d["r1_note"]


def test_verdict_language_and_tags():
    res = cached_analysis()
    assert res["physicalization_holds"] is True
    assert tuple(res["verdict_tags"]) == VERDICT_TAGS
    assert "no_claim_promotion" in res["verdict_tags"]
    lang = res["verdict_language"]
    assert "basis-free flat pair holds in this finite family" in lang
    assert "pause for Joe" in lang
    assert "No claim promotion" in lang


def test_zone_menu_never_touches_escaped_tail():
    assert set(Z_ACTIVE).isdisjoint(set(ESCAPED))
    assert set(ACCESS_ZONE).isdisjoint(set(ESCAPED))
