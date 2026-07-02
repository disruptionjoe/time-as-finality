"""Tests for T409: Capability Restoration Frontier (Tier-2, finite family).

Asserts, to numerical precision, the three legs of the spec:

Leg 1 (dispersion forces reach growth): in the collision model (record
qubit REC broadcasting which-way copies into a bath stream, CNOT-type
collisions of strength theta), threshold restoration of S's phase-locked
visibility (v* = 0.9, T392's) requires reach r(n) that grows monotonically
with collision count -- EXACTLY r(n) = n at theta = pi, with every
insufficient reach subset certified against ALL channels (phi-independence
certificate + trace-norm bound), exhaustively over every subset for
n <= 4 and symmetry-pruned beyond (the pruning itself asserted).

Leg 2 (work does not substitute for reach): both certificates and the
frontier are invariant under adjoining work registers (Stinespring +
trace-norm multiplicativity, asserted numerically); manufactured coherence
is nulled by the locked metric; blind reset pays the Landauer floor and
restores nothing.

Leg 3 (graded frontier + T142 ledger): r_feas(n, theta) = max(0, n - d),
d = floor(ln(v*/vis_A)/ln cos(theta/2)); certified bracket exact above the
bite edge 0.6995 pi and honestly vacuous at weak coupling; exact
complementarity between capability deficit and displaced record
distinguishability; escaped Holevo saturates at h2(3/7) at theta = pi
while the frontier keeps growing (contacts, not bits).

Register order (index-sorted): S, M, REC, B1..B7.
"""

from __future__ import annotations

import math

import numpy as np

from models.capability_restoration_frontier import (
    BAND_CERTIFIED,
    BAND_FEASIBLE,
    BAND_UNDETERMINED,
    BATH,
    CORE_ACTIVE,
    EXHAUSTIVE_N,
    FLATNESS_TOL,
    HAAR_VISIBILITY_CEILING,
    N_BATH_MAX,
    N_QUBITS,
    THETA_BITE_EDGE,
    THETA_CNOT,
    THETA_METER,
    THETA_ONSET_EDGE,
    THETA_SWEEP,
    V_STAR,
    VERDICT_TAGS,
    VIS_A_ANALYTIC,
    WORK_REGISTERS,
    WORK_SCENARIO_REACH,
    cached_analysis,
    deficit_allowance,
    landauer_bound_bits,
    locked_visibility,
    prepare,
    reach_active,
    restoration_protocol,
)

H2_3_7 = -(3 / 7) * math.log2(3 / 7) - (4 / 7) * math.log2(4 / 7)


# --------------------------------------------------------------------------- #
# Fixture / layout / imports
# --------------------------------------------------------------------------- #

def test_register_layout_and_budget():
    assert N_QUBITS == 10  # within the 10-12 qubit budget, exact statevector
    assert N_BATH_MAX == len(BATH) == 7
    assert set(CORE_ACTIVE).isdisjoint(set(BATH))
    psi = prepare("cnot", 7, 1.0)
    assert abs(float(np.real(psi.conj() @ psi)) - 1.0) < 1e-12


def test_house_constants_imported_unchanged():
    assert THETA_METER == math.pi / 3.0  # T392's weak meter, unchanged
    assert V_STAR == 0.9  # T392/T393/T408's threshold, unchanged
    assert abs(VIS_A_ANALYTIC - 4.0 * math.sqrt(3.0) / 7.0) < 1e-15


def test_edges_match_house_constants():
    """The frontier onset edge is T408's protocol-feasibility edge; the
    bound-bite edge is the same 2x-looseness threshold measured in
    T393/T408."""
    assert abs(THETA_ONSET_EDGE / math.pi - 0.273195) < 1e-6
    assert abs(THETA_BITE_EDGE / math.pi - 0.699519) < 1e-6


def test_zero_collisions_is_t392_core():
    """With no collisions, no bath reach is needed: uncopying REC alone
    restores the T392 value exactly."""
    vis = locked_visibility("cnot", 0, restoration_protocol(()))
    assert abs(vis - VIS_A_ANALYTIC) < 1e-12


def test_determinism():
    a1 = prepare("cnot", 5, math.sqrt(2.0), 0.5 * math.pi)
    a2 = prepare("cnot", 5, math.sqrt(2.0), 0.5 * math.pi)
    assert float(np.max(np.abs(a1 - a2))) == 0.0
    v1 = locked_visibility("cnot", 3, restoration_protocol(BATH[:3]))
    v2 = locked_visibility("cnot", 3, restoration_protocol(BATH[:3]))
    assert v1 == v2


def test_all_three_legs_hold():
    legs = cached_analysis()["legs"]
    assert legs["leg1_dispersion_forces_reach_growth"] is True
    assert legs["leg2_work_does_not_substitute"] is True
    assert legs["leg3_graded_frontier_and_ledger"] is True
    assert cached_analysis()["frontier_holds"] is True


# --------------------------------------------------------------------------- #
# Leg 1 -- dispersion forces reach growth
# --------------------------------------------------------------------------- #

def test_frontier_theta_pi_r_equals_n():
    """The headline table: at perfect collision strength the frontier is
    exact and maximal, r(n) = n for every n = 1..7, certified AND feasible
    coinciding (bracket width zero)."""
    fr = cached_analysis()["frontier_theta_pi"]
    assert fr["r_feas_by_n"] == list(range(1, N_BATH_MAX + 1))
    assert fr["r_cert_by_n"] == list(range(1, N_BATH_MAX + 1))
    for row in fr["per_n"]:
        assert row["r_feas"] == row["r_feas_analytic"] == row["n"]


def test_frontier_theta_pi_all_insufficient_reaches_certified():
    """Every reach size below n is certified against ALL channels: exact
    phi-independence of the reach conditional family AND trace-norm bound
    numerically zero."""
    fr = cached_analysis()["frontier_theta_pi"]
    for row in fr["per_n"]:
        for cell in row["rows"]:
            if cell["reach"] < row["n"]:
                assert cell["phi_cert"] < FLATNESS_TOL
                assert cell["bound"] < FLATNESS_TOL
                assert cell["band"] == BAND_CERTIFIED
            else:
                assert cell["band"] == BAND_FEASIBLE
                assert abs(cell["achieved"] - VIS_A_ANALYTIC) < 1e-12


def test_exhaustive_certification_every_subset():
    """For n <= 4 (both exhaustive strengths) EVERY subset of the bath is
    checked: values depend only on subset size (the symmetry-pruning
    justification), the exhaustive frontier equals the canonical one, and
    at theta = pi every proper size is phi-certified."""
    for ex in cached_analysis()["exhaustive_certification"]:
        assert ex["subsets_checked"] == 2 ** ex["n"]
        assert ex["max_same_size_spread"] < 1e-10
        assert ex["r_feas_exhaustive"] == ex["n"]  # d = 0 at both strengths
        if ex["theta_over_pi"] == 1.0:
            for r in range(ex["n"]):
                assert ex["by_size"][r]["max_phi_cert"] < FLATNESS_TOL
                assert ex["by_size"][r]["bands"] == [BAND_CERTIFIED]
    assert tuple(EXHAUSTIVE_N) == (1, 2, 3, 4)


def test_symmetry_pruning_justified_at_full_bath():
    """Permuted same-size reach subsets at n = 7 have IDENTICAL conditional
    states (commuting collisions, permutation-symmetric bath): the
    canonical-subset frontier loses nothing."""
    sym = cached_analysis()["symmetry"]
    assert sym["n"] == 7
    assert sym["max_state_diff"] < FLATNESS_TOL


def test_frontier_monotone_with_slope_one_beyond_onset():
    mono = cached_analysis()["monotonicity"]
    assert mono["monotone_nondecreasing"] is True
    assert mono["slope_one_beyond_onset"] is True
    assert mono["escape_velocity_reach_units_per_collision"] == 1


def test_onset_delay_matches_analytic_deficit_allowance():
    """r_feas(n, theta) = max(0, n - d(theta)) across the whole sweep, with
    the predeclared d values."""
    expected_d = {0.10: 7, 0.15: 3, 0.20: 1, 0.25: 1, 0.50: 0, 0.70: 0,
                  0.75: 0, 1.00: 0}
    mono = cached_analysis()["monotonicity"]
    for theta in THETA_SWEEP:
        f = theta / math.pi
        d = deficit_allowance(theta)
        assert d == expected_d[round(f, 2)]
        table = mono["frontiers"][f"{f:.2f}pi"]
        assert table["r_feas_by_n"] == [
            max(0, n - d) for n in range(1, N_BATH_MAX + 1)
        ]
        # Onset delay exists exactly below the onset edge (T408's constant).
        assert (d >= 1) == (theta <= THETA_ONSET_EDGE)


def test_saturation_reported_exactly():
    """theta = 0.1 pi: the analytic onset (n = 8) exceeds the bath size, so
    r_feas = 0 throughout -- located and reported, not hidden."""
    sats = cached_analysis()["monotonicity"]["saturations"]
    assert len(sats) == 1
    assert abs(sats[0]["theta_over_pi"] - 0.1) < 1e-12
    assert "onset n = 8" in sats[0]["detail"]


def test_swap_probe_displacement_without_dispersion():
    """The full-SWAP stream saturates at r(n) = 1: the record moves once
    and later collisions change NOTHING (state freeze exact); the frontier
    is subset-specific (B1 or nothing). Frontier growth is sourced in
    broadcast, not motion."""
    sw = cached_analysis()["swap_probe"]
    assert sw["later_collisions_change_nothing_max_diff"] == 0.0
    for n, vis in sw["restore_via_B1_by_n"].items():
        assert vis >= V_STAR
    for n, cert in sw["empty_reach_phi_cert_by_n"].items():
        assert cert < FLATNESS_TOL
    # Exhaustive at n = 3: containing B1 restores; missing B1 certified at
    # EVERY size (the frontier is not permutation-symmetric here).
    for key, cell in sw["exhaustive_n3"].items():
        if cell["contains_B1"]:
            assert cell["achieved"] >= V_STAR
        else:
            assert cell["phi_cert"] < FLATNESS_TOL
            assert cell["bound"] < FLATNESS_TOL
    assert sw["r_feas_by_n"] == [1, 1, 1, 1, 1]


def test_uncorrelated_null_bath_contact_is_free():
    """Record-free collisions (real excitation, no record): restoration
    needs no bath reach at any n. RECORD-BEARING contact is what the
    frontier prices."""
    null = cached_analysis()["uncorrelated_null"]
    assert null["r_feas"] == 0
    for n, row in null["rows"].items():
        assert row["achieved_at_reach_0"] >= V_STAR
        assert row["bath_excitation"] > 0.4  # the contact is real (teeth)


# --------------------------------------------------------------------------- #
# Leg 2 -- work does not substitute for reach
# --------------------------------------------------------------------------- #

def test_certificates_invariant_under_work_registers():
    """Adjoining fresh work registers changes neither certificate: the
    phi-independence certificate fires identically on reach + work, and
    the trace-norm bound is exactly ancilla-invariant
    (||A tensor sigma||_1 = ||A||_1)."""
    w = cached_analysis()["work"]
    assert w["phi_cert_bare"] < FLATNESS_TOL
    assert w["phi_cert_with_work"] < FLATNESS_TOL
    assert w["bound_ancilla_invariance_diff"] < FLATNESS_TOL


def test_frontier_reach_absolute_under_work():
    """Every frontier bound at n = 4 recomputed with both work registers
    adjoined is identical: the frontier is reach-absolute at fixed reach --
    unlimited work buys nothing."""
    w = cached_analysis()["work"]
    assert w["frontier_bound_max_diff_with_work"] < FLATNESS_TOL
    assert "Stinespring" in w["dilation_lemma"]
    assert "priced in reach, not work" in w["dilation_lemma"]


def test_manufactured_coherence_nulled():
    """Fresh work manufactures coherence but never phi-LOCKED coherence
    (T393's lemma): the |+>-injection exploit scores raw 1.0 and locked 0."""
    manu = cached_analysis()["work"]["manufactured_coherence"]
    assert manu["raw_visibility"] > 0.99
    assert manu["locked_visibility"] < 1e-12


def test_feedback_channel_nulled():
    """The menu is all channels, not just unitaries: the representative
    measure-and-feedback channel is covered by the certificate."""
    assert cached_analysis()["work"]["feedback_channel_locked"] < 1e-12


def test_haar_spot_check_illustrative():
    haar = cached_analysis()["work"]["haar_spot_check"]
    assert haar["max_locked_visibility"] < HAAR_VISIBILITY_CEILING
    assert "illustrative" in haar["note"]


def test_beyond_frontier_all_channel_certificates():
    """The beyond-frontier scenario (n = 4 perfect contacts, reach 2) is
    certified for ALL reach channels, work included."""
    certs = cached_analysis()["ledger"]["restore_beyond_frontier"]["certificates"]
    assert certs["phi_independence"] < FLATNESS_TOL
    assert certs["channel_bound"] < FLATNESS_TOL
    assert set(WORK_SCENARIO_REACH).isdisjoint(set(WORK_REGISTERS))
    assert set(reach_active(WORK_SCENARIO_REACH)).isdisjoint(set(WORK_REGISTERS))


# --------------------------------------------------------------------------- #
# Leg 3 -- graded frontier + T142 ledger
# --------------------------------------------------------------------------- #

def test_graded_achieved_matches_analytic():
    """achieved = vis_A * cos(theta/2)^u across the correspondence rows."""
    for row in cached_analysis()["ledger"]["correspondence_rows"]:
        theta = row["theta_over_pi"] * math.pi
        expected = VIS_A_ANALYTIC * math.cos(theta / 2.0) ** row["unreached_contacts"]
        assert abs(row["achieved"] - expected) < 1e-9


def test_complementarity_capability_deficit_equals_displaced_record():
    """The computed correspondence: capability deficit 1 - (ach/vis_A)^2
    EQUALS the squared branch distinguishability displaced into the
    unreached bath, exactly, at every row of both strengths."""
    for row in cached_analysis()["ledger"]["correspondence_rows"]:
        assert row["complementarity_residual"] < 1e-9
        theta = row["theta_over_pi"] * math.pi
        u = row["unreached_contacts"]
        d_analytic = math.sqrt(max(0.0, 1.0 - math.cos(theta / 2.0) ** (2 * u)))
        assert abs(row["displaced_distinguishability"] - d_analytic) < 1e-9


def test_bound_is_exactly_twice_achieved_disclosure():
    """The trace-norm bound computes to exactly 2x the achieved value in
    this family -- the same factor-2 looseness measured in T393 and T408,
    now in a third artifact; disclosed, and the reason the certified
    bracket is honest rather than tight."""
    from models.capability_restoration_frontier import frontier_for_theta
    f5 = frontier_for_theta(0.5 * math.pi)
    for row in f5["per_n"][-1]["rows"]:
        assert abs(row["bound"] - 2.0 * row["achieved"]) < 1e-9


def test_certified_bracket_at_half_pi():
    """theta = 0.5 pi: r_feas = n but r_cert = max(0, n - 2) -- the bracket
    width is the bound's factor-2 looseness, reported honestly."""
    table = cached_analysis()["monotonicity"]["frontiers"]["0.50pi"]
    assert table["r_feas_by_n"] == [1, 2, 3, 4, 5, 6, 7]
    assert table["r_cert_by_n"] == [0, 0, 1, 2, 3, 4, 5]


def test_bite_threshold_exact_above_vacuous_below():
    """Above the bite edge (0.6995 pi) the bracket is EXACT (r_cert =
    r_feas); at weak coupling (<= 0.25 pi) certification is vacuous within
    this bath size (u_min_cert in {10, 16, 29, 64} > 7) -- both reported."""
    mono = cached_analysis()["monotonicity"]["frontiers"]
    for f in (0.70, 0.75, 1.00):
        table = mono[f"{f:.2f}pi"]
        assert table["r_feas_by_n"] == table["r_cert_by_n"]
        assert (f * math.pi) > THETA_BITE_EDGE
    for f in (0.10, 0.15, 0.20, 0.25):
        table = mono[f"{f:.2f}pi"]
        assert table["r_cert_by_n"] == [0] * N_BATH_MAX
        assert float(table["u_min_cert"]) > N_BATH_MAX


def test_three_bands_realized_on_one_frontier_column():
    """At theta = 0.5 pi, n = 7 the reach column realizes all three bands:
    certified (r <= 4), undetermined (r = 5, 6), feasible (r = 7)."""
    from models.capability_restoration_frontier import frontier_for_theta
    rows = frontier_for_theta(0.5 * math.pi)["per_n"][-1]["rows"]
    bands = [row["band"] for row in rows]
    assert bands == [BAND_CERTIFIED] * 5 + [BAND_UNDETERMINED] * 2 + [BAND_FEASIBLE]


def test_escaped_holevo_saturates_contacts_not_bits():
    """At theta = pi the escaped Holevo content is h2(3/7) = 0.985228 bits
    for EVERY u >= 1 (one branch bit, redundantly broadcast) while the
    frontier keeps growing r(n) = n: the frontier is priced in
    record-bearing CONTACTS, not in escaped bits."""
    rows = [
        r
        for r in cached_analysis()["ledger"]["correspondence_rows"]
        if r["theta_over_pi"] == 1.0
    ]
    for row in rows:
        if row["unreached_contacts"] >= 1:
            assert abs(row["escaped_holevo_bits"] - H2_3_7) < 1e-9
        else:
            assert abs(row["escaped_holevo_bits"]) < 1e-9
    fr = cached_analysis()["frontier_theta_pi"]["r_feas_by_n"]
    assert all(b - a == 1 for a, b in zip(fr, fr[1:]))  # still growing


def test_escaped_holevo_monotone_in_unreached_contacts():
    for row in cached_analysis()["ledger"]["correspondence_rows"]:
        assert row["holevo_monotone_from_prev"]


def test_ledger_restore_within_reach_correlated_uncopy():
    led = cached_analysis()["ledger"]["restore_within_reach"]
    assert led["mode"] == "correlated_uncopy"
    assert led["erased_bits"] == 0
    assert led["beta_work_lower_bound"] == 0.0
    assert led["achieved_locked_visibility"] >= V_STAR
    assert led["holders_uncomputed"] == 5
    assert led["t142_verdict"] == "reversible_when_full_microstate_available"


def test_ledger_blind_reset_deletion_is_not_definalization():
    led = cached_analysis()["ledger"]["blind_reset"]
    assert led["capability_after_reset"] < 1e-12
    assert led["record_deleted_residual_distinguishability"] < 1e-12
    assert led["deletion_is_not_definalization"]
    assert led["beta_work_lower_bound_naive"] == landauer_bound_bits(5)
    assert abs(led["joint_record_bits_given_M0"] - H2_3_7) < 1e-9
    assert abs(led["joint_record_bits_unconditioned"] - 1.0) < 1e-9


def test_ledger_beyond_frontier_empty_feasible_set():
    led = cached_analysis()["ledger"]["restore_beyond_frontier"]
    assert led["feasible_at_reach"] is False
    assert math.isinf(led["min_beta_work"])
    assert "not work" in led["limiting_resource"]
    assert "NOT a divergent" in led["not_a_work_bound"]


def test_ledger_scope_is_bookkeeping_only():
    led = cached_analysis()["ledger"]
    assert "not a thermodynamic theorem" in led["correspondence"]
    assert "CONTACTS, not in escaped bits" in led["correspondence"]
    assert "named-unbuilt" in led["tier2_scope"]


# --------------------------------------------------------------------------- #
# Guardrails and verdict discipline
# --------------------------------------------------------------------------- #

def test_q1d_guardrail_asserted_numerically():
    q1d = cached_analysis()["q1d"]
    assert q1d["declared_record_invariance"] < FLATNESS_TOL
    assert q1d["no_signal_out_reach_protocol"] < FLATNESS_TOL
    # The counterfactual enlarged protocol moves the unreached marginal by
    # 3/7 (teeth -- the same number T408 earned).
    assert abs(
        q1d["enlarged_protocol_moves_unreached_marginal_teeth"] - 3.0 / 7.0
    ) < 1e-9
    assert "R1 untouched" in q1d["r1_note"]
    assert "not a light cone" in q1d["r1_note"]
    assert "Lieb-Robinson" in q1d["r1_note"]


def test_verdict_language_and_tags():
    res = cached_analysis()
    assert res["frontier_holds"] is True
    assert tuple(res["verdict_tags"]) == VERDICT_TAGS
    assert "no_claim_promotion" in res["verdict_tags"]
    lang = res["verdict_language"]
    assert "capability restoration frontier holds" in lang
    assert "pause for Joe" in lang
    assert "no claim promotion" in lang
    assert "named-unbuilt" in lang


def test_perfect_strength_matches_exact_cnot():
    """theta = pi collisions reproduce the exact-CNOT broadcast statevector
    (the strength axis is anchored, T393's alpha = pi convention)."""
    psi_a = prepare("cnot", 3, 1.0, THETA_CNOT)
    assert abs(float(np.real(psi_a.conj() @ psi_a)) - 1.0) < 1e-12
    # branch structure: conditioned on S, bath holds |000> vs |111>
    from models.capability_restoration_frontier import project_qubit
    _, v1 = project_qubit(psi_a, 0, 1, N_QUBITS)
    from models.fixed_sbs_key_reversal_divergence import reduced_density_matrix
    rho_b = reduced_density_matrix(v1, [3, 4, 5], N_QUBITS)
    assert abs(float(np.real(rho_b[7, 7])) - 1.0) < 1e-12  # |111><111|
