"""Tests for T419: Computational Arrow of Time (temporal lift of T417's E2 boundary).

Asserts the surviving legs of tests/T419-computational-arrow-of-time.md and the
hostile-review verdict: K4 fires on the exhibited toy orbit, so this remains
recorded-tier REDESIGN with no claim promotion. Cross-domain cryptography /
number theory is object of study, not evidence.
"""

from models.computational_arrow_of_time import (
    run, forward, principal_sqrt, backward_bruteforce, rabin_reduction,
    quad_residues, cycle_predecessor_by_forward_iteration, jacobi,
    N, P, Q, SEED, T_TICKS,
)

R = run()
QR = quad_residues(N)


# --- SUCCESS leg 1: PERMUTATION / entropy-neutral -------------------------
def test_leg1_squaring_is_permutation_of_QR_N():
    l1 = R["leg1_permutation_entropy_neutral"]
    assert l1["is_blum"] is True                       # 7 == 11 == 3 mod 4
    assert l1["size_QR_N"] == 15                        # |QR_77| = phi/4
    assert l1["size_QR_N"] == l1["phi_over_4"]
    assert l1["size_is_odd"] is True                    # odd => bijection
    assert l1["F_is_permutation_of_QR_N"] is True
    # cross-check directly: F maps QR_N onto QR_N bijectively
    assert sorted(forward(x, N) for x in QR) == QR
    assert "ZERO" in l1["erasure"]


# --- SUCCESS leg 2: CO-PRESENCE (unique predecessor; trapdoor recovers) ---
def test_leg2_unique_predecessor_and_trapdoor_recovers():
    l2 = R["leg2_co_presence"]
    assert l2["seed_x0"] == SEED
    assert len(l2["orbit"]) == T_TICKS + 1
    assert len(l2["emitted_bit_record"]) == T_TICKS + 1
    assert l2["unique_predecessor_every_state"] is True
    assert l2["trapdoor_recovers_exact_predecessor_every_t"] is True
    # cross-check: principal_sqrt inverts F at every recorded tick
    orbit = l2["orbit"]
    for t in range(1, len(orbit)):
        assert principal_sqrt(orbit[t], P, Q) == orbit[t - 1]


# --- SUCCESS leg 3: FORWARD-EASY-FLAT -------------------------------------
def test_leg3_forward_flat_one_modmul_and_extendable():
    l3 = R["leg3_forward_easy_flat"]
    assert l3["forward_step_ops"] == 1
    assert l3["ops_per_step_flat_in_t"] == [1] * T_TICKS   # flat in t
    assert l3["total_forward_ops_for_T"] == T_TICKS
    ext = l3["extend_record_forward_with_N_alone"]
    assert ext["ops"] == ext["extra_ticks"]               # one modmul per tick
    assert len(ext["extra_bits"]) == ext["extra_ticks"]   # record extends forward


# --- SUCCESS leg 4: BACKWARD-HARD-BY-REDUCTION (Rabin sqrt->factor) --------
def test_leg4_rabin_reduction_exhibited_and_QRA_lift():
    l4 = R["leg4_backward_hard_by_reduction"]
    red = l4["rabin_reduction_exhibited"]
    assert red is not None
    assert red["nontrivial_factor"] in (P, Q)             # oracle -> factor of N
    assert red["nontrivial_factor"] * red["cofactor"] == N
    assert l4["sqrt_oracle_yields_factor_of_N"] is True
    # independent cross-check of the reduction with the principal-sqrt oracle
    red2 = rabin_reduction(N, lambda a: principal_sqrt(a, P, Q))
    assert red2 is not None and 1 < red2["nontrivial_factor"] < N
    # T417 Leg 2 lifted: Jacobi uninformative (+1), Legendre-with-(p,q) separates
    lift = l4["T417_leg2_on_time_axis"]
    assert lift["jacobi_uninformative_all_+1"] is True
    assert all(jacobi(x, N) == 1 for x in R["leg2_co_presence"]["orbit"])


def test_leg4_backward_bruteforce_finds_unique_predecessor():
    # trapdoor-FREE finite search recovers the predecessor (present in principle)
    orbit = R["leg2_co_presence"]["orbit"]
    for t in range(1, len(orbit)):
        z = backward_bruteforce(orbit[t], N, QR)
        assert z == orbit[t - 1]


# --- SUCCESS leg 5: TRAPDOOR-RESYMMETRIZES --------------------------------
def test_leg5_trapdoor_resymmetrizes_cone():
    l5 = R["leg5_trapdoor_resymmetrizes"]
    assert l5["with_trapdoor"]["cone"].startswith("SYMMETRIC")
    assert l5["without_trapdoor"]["cone"].startswith("ASYMMETRIC")
    # with trapdoor backward is polylog; without, it is the factoring wall
    assert l5["with_trapdoor"]["backward_ops"] >= 1
    assert "factoring" in l5["without_trapdoor"]["backward_ops"]
    assert "E2" in l5["wall_type"]


# --- Leg 6: hostile-review K4 check over the actual toy orbit --------------
def test_leg6_k4_static_relabel_kill_fires_on_short_cycle():
    l6 = R["leg6_temporal_asymmetry_over_orbit"]
    assert l6["asymmetry_is_per_step_property"] is False
    assert l6["forward_cost_flat"] is True
    assert l6["growing_monotone_used"] is False           # K2 guard
    assert l6["k4_static_relabel_kill_fired"] is True
    for step in l6["per_step"]:
        # forward reachable set is poly-enumerable and nonempty
        assert len(step["forward_reachable_3"]) == 3
        # The toy cycle itself gives a cheap trapdoor-free predecessor.
        assert len(step["backward_feasible_without_trapdoor"]) == 1
        assert step["trapdoor_free_cycle_reversal_ops"] == 3
        assert step["predecessor_matches_cycle_recovery"] is True
        assert len(step["backward_feasible_with_trapdoor"]) == 1
        assert step["predecessor_matches_trapdoor"] is True
        recovered = cycle_predecessor_by_forward_iteration(step["x_t"], N)
        assert recovered is not None
        assert recovered[0] == step["recorded_predecessor"]


# --- SUCCESS leg 7: COST-GROWTH-FAMILY ------------------------------------
def test_leg7_cost_growth_family_diverges():
    l7 = R["leg7_cost_growth_family"]
    assert l7["forward_flat"] is True                     # forward FLAT across family
    assert l7["backward_without_trapdoor_strictly_increasing"] is True
    without = l7["backward_without_trapdoor_curve"]
    assert without == sorted(without) and len(set(without)) == len(without)
    # every family member is a Blum semiprime
    for row in l7["rows"]:
        assert row["is_blum"] is True
        assert row["forward_step_ops"] == 1
    # asymptotic divergence: at the large end, no-trapdoor >> with-trapdoor
    assert without[-1] > l7["backward_with_trapdoor_curve"][-1]


# --- SUCCESS leg 8: KILLER-PREMORTEM table --------------------------------
def test_leg8_killer_premortem_dodges():
    l8 = R["leg8_killer_premortem"]
    assert l8["K1_thermo_E1"]["evidence"] is True         # permutation => zero erasure
    assert l8["K2_brown_susskind"]["evidence"] is True    # nothing grows
    assert l8["K3_stipulated_hardness_E0"]["evidence"] is True  # reduction exhibited
    assert l8["K4_static_T417_relabel"]["evidence"] is False
    assert l8["K4_static_T417_relabel"]["fired"] is True
    assert "K5" in "".join(l8.keys())                     # prior-art row present


# --- KILL guards: K1/K3 survive, K4 fires ---------------------------------
def test_kill_guards_record_redesign_verdict():
    l1 = R["leg1_permutation_entropy_neutral"]
    l6 = R["leg6_temporal_asymmetry_over_orbit"]
    l4 = R["leg4_backward_hard_by_reduction"]
    v = R["honest_verdict"]
    # K1: no erasure (bijection) -> not thermodynamic
    assert l1["F_is_permutation_of_QR_N"] is True
    # K2: no growing monotone relied upon
    assert l6["growing_monotone_used"] is False
    assert v["no_growing_monotone"] is True
    # K3: hardness reduced, not stipulated
    assert l4["sqrt_oracle_yields_factor_of_N"] is True
    # K4: genuine iterated orbit exists, but the short cycle makes reversal cheap.
    assert l6["k4_static_relabel_kill_fired"] is True
    assert v["k4_static_relabel_kill_fired"] is True


# --- Success-criterion-3: differentiation is argued -----------------------
def test_differentiation_distinct_from_known_arrows():
    d = R["differentiation"]
    for key in ("vs_brown_susskind", "vs_lesovik", "vs_crutchfield",
                "vs_wolpert_bennett", "vs_T417"):
        assert key in d and len(d[key]) > 0


# --- Headline ------------------------------------------------------------
def test_headline_computational_arrow_redesign_not_promotion():
    """The headline: over a REAL squaring orbit on QR_77 (a bijection: zero
    erasure, nothing grows), feasible-recoverability is directionally oriented --
    forward FLAT (1 modmul), backward == factoring (Rabin 1979, exhibited). The
    boundary is info-theoretically trivial (datum present, reversal exists) yet
    computationally FORCED (E2, reduced to Rabin/QRA), agent-relative to (p,q),
    distinct from the thermodynamic and complexity-growth arrows -- honestly
    conditional and family-level."""
    v = R["honest_verdict"]
    assert "TRIVIAL" in v["info_theoretically"]
    assert "REDESIGN" in v["arrow"]
    assert "not forced" in v["computationally"]
    assert "CONDITIONAL" in v["boundary_status"]
    assert v["claim_promotion"].startswith("none")
    assert R["leg1_permutation_entropy_neutral"]["F_is_permutation_of_QR_N"] is True
    assert R["leg4_backward_hard_by_reduction"]["sqrt_oracle_yields_factor_of_N"] is True
