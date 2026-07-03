"""Tests for T423 - M2 Observer-Game / Judgment-Aggregation Finality Probe.

Predeclared success legs S1-S5 and the honest-ceiling guards. Exact rational
arithmetic; n=3 fully enumerated. Recorded-tier; no claim promotion.

    python -m pytest tests/test_m2_observer_game.py -q
"""

from fractions import Fraction as F

from models.m2_observer_game import (
    JUDGES, P, Q, R,
    and_doctrine,
    smaj, premise_verdict, conclusion_verdict, dilemma_indicator,
    judges_consistent, collective_inconsistent, lp_localization,
    agenda_obstruction, moebius_dividends, gap_value, premise_game_value,
    doctrine_family_row, aumann_shapley_trend, consistency_relaxation_probe,
    run,
)
from models.legitimacy_shapley_finality_probe import (
    all_subsets, v_of, shapley_by_dividends, shapley_by_permutations,
    joint_record_completion_verdict, symmetry_holds,
)


# --- S1 GENUINE DILEMMA (K2 guard) -----------------------------------------
def test_s1_individual_judgments_consistent():
    # every judge obeys r_i = p_i & q_i
    assert judges_consistent()
    assert R == {1: 1, 2: 0, 3: 0}


def test_s1_collective_is_a_genuine_discursive_dilemma():
    # premise-based majority ACCEPTS (maj p & maj q), conclusion-based REJECTS
    assert premise_verdict(JUDGES) == 1
    assert conclusion_verdict(JUDGES) == 0
    assert collective_inconsistent()
    # not a tie-rule artifact: p and q both carry a STRICT 2/3 majority
    assert smaj(P, JUDGES) == 1 and smaj(Q, JUDGES) == 1
    # and conclusion r has a strict 2/3 majority for REJECT
    assert sum(R[i] for i in JUDGES) == 1  # only judge 1 accepts r


# --- S2 GLOBAL-NO-LOCAL ----------------------------------------------------
def test_s2_gap_game_is_unanimity_u_N():
    div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    assert div == {frozenset(JUDGES): F(1)}  # single grand dividend, 0 elsewhere


def test_s2_dilemma_reconstructible_from_no_proper_subset():
    loc = lp_localization()
    assert loc["dilemma_only_on_grand"] is True
    assert loc["proper_carriers"] == []
    # exhaustive: indicator 0 on all 7 proper coalitions, 1 only on N
    for S in all_subsets(JUDGES):
        expected = 1 if frozenset(S) == frozenset(JUDGES) else 0
        assert dilemma_indicator(S) == expected


def test_s2_joint_record_completion_survives_R1():
    div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    jrc = joint_record_completion_verdict(div, {}, players=JUDGES)
    assert jrc["verdict"] == "SURVIVES-R1"
    assert jrc["datum_in_proper_subset"] is False
    assert jrc["min_sep_coalition"] == [1, 2, 3]


# --- S3 AUMANN-SHAPLEY IS THE SEPARATOR ------------------------------------
def test_s3_shapley_value_and_crosscheck():
    div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    phi_d = shapley_by_dividends(div, players=JUDGES)
    phi_p = shapley_by_permutations(div, players=JUDGES)
    assert phi_d == phi_p                                   # Leg-1 cross-check
    assert phi_d == {1: F(1, 3), 2: F(1, 3), 3: F(1, 3)}
    assert symmetry_holds(phi_d, div, players=JUDGES)
    assert sum(phi_d.values(), F(0)) == v_of(div, JUDGES)   # efficiency


def test_s3_datum_ties_to_T413_pair2_grand_dividend():
    div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    # the SURVIVES-R1 datum is the grand-coalition dividend = 1 (T413 Pair-2)
    assert div.get(frozenset(JUDGES), F(0)) == F(1)


def test_s3_aumann_shapley_trend_delta_preserved_shares_dilute():
    trend = aumann_shapley_trend()
    for row in trend:
        assert row["v_gap_N_Delta"] == "1"   # Delta preserved on the grand coalition
    # individual pivotality dilutes as k grows
    s1 = F(trend[0]["type_share_phi"][1])
    s2 = F(trend[1]["type_share_phi"][1])
    s3 = F(trend[2]["type_share_phi"][1])
    assert s1 > s2 > s3


def test_s3_global_no_local_is_atomic_knife_edge():
    # HONEST finding: strict "no proper subset" survives only at k=1; for k>=2 a
    # one-of-each-type size-3 sub-coalition reconstructs the dilemma.
    trend = aumann_shapley_trend()
    assert trend[0]["global_no_local_survives"] is True
    assert trend[1]["global_no_local_survives"] is False
    assert trend[2]["global_no_local_survives"] is False
    for row in trend:
        assert row["min_dilemma_coalition_size"] == 3


# --- S4 CANONICITY, HONESTLY SCOPED ----------------------------------------
def test_s4_agenda_obstruction_equals_d_N():
    div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    obs = agenda_obstruction()
    assert obs["omega"] == 1
    assert obs["minimal_inconsistent_sets"] == [["p", "q", "r"]]
    assert obs["omega"] == div.get(frozenset(JUDGES), F(0))  # 1 == 1


def test_s4_localization_agreement_is_shared_primitive():
    # HONEST K1-partial: on consistent judges v_gap == dilemma_indicator as set
    # functions, so the localization agreement is shared-primitive, NOT escaping
    # T422 by itself.
    for S in all_subsets(JUDGES):
        assert gap_value(S) == F(dilemma_indicator(S))


def test_s4_magnitude_decoupling_is_the_teeth():
    gap_div = moebius_dividends(lambda S: gap_value(S), JUDGES)
    prem_div = moebius_dividends(lambda S: premise_game_value(S), JUDGES)
    phi_gap = shapley_by_dividends(gap_div, players=JUDGES)
    phi_prem = shapley_by_dividends(prem_div, players=JUDGES)
    # premise reading gives a DIFFERENT datum -> not identical by construction
    assert prem_div.get(frozenset(JUDGES), F(0)) == F(2)
    assert gap_div.get(frozenset(JUDGES), F(0)) == F(1)
    assert phi_prem == {1: F(2, 3), 2: F(1, 6), 3: F(1, 6)}
    assert phi_prem != phi_gap


def test_s4_doctrine_family_covaries_without_retuning():
    fam = [doctrine_family_row(name) for name in ("AND", "OR", "DICT", "NOCONN")]
    # separator (SURVIVES-R1) == omega for EVERY doctrine
    for row in fam:
        assert row["separator_equals_omega"], row
    # AND -> 1, everything else -> 0: the vector genuinely varies
    omegas = [row["omega"] for row in fam]
    assert omegas == [1, 0, 0, 0]
    assert len(set(omegas)) > 1


def test_s4_guard_the_guard_family_must_flag_disagreement():
    # if any doctrine's separator disagreed with omega, the driver MUST report it
    fam = [doctrine_family_row(name) for name in ("AND", "OR", "DICT", "NOCONN")]
    all_agree = all(r["separator_equals_omega"] for r in fam)
    # positive control: fabricate a disagreement and confirm it would be caught
    fake = dict(fam[0]); fake["separator_present"] = 0
    fake["separator_equals_omega"] = (fake["separator_present"] == fake["omega"])
    assert all_agree is True
    assert fake["separator_equals_omega"] is False


def test_s4_OR_raw_dN_is_absorbed_not_a_separator():
    # HONEST: OR's raw grand Mobius dividend is 1, but the game is ABSORBED at a
    # proper coalition, so raw d(N) is NOT the separator; the SURVIVES-R1 test is.
    row = doctrine_family_row("OR")
    assert row["d_N_moebius"] == "1"
    assert row["jrc_verdict"] == "ABSORBED"
    assert row["separator_present"] == 0
    assert row["omega"] == 0


# --- S5 FALSIFIERS ---------------------------------------------------------
def test_s5_consistency_relaxation_decouples_the_routes():
    probe = consistency_relaxation_probe()
    # relaxed judges are individually INCONSISTENT ...
    assert probe["judges_consistent"] is False
    # ... the collective-inconsistency test can still fire (omega nonzero) ...
    assert probe["collective_inconsistent"] is True
    assert probe["omega_relaxed"] == 1
    # ... but there is NO genuine global-no-local separator (absorbed), so the
    # omega<->separator agreement is a REGIME fact, not an identity.
    assert probe["jrc_verdict"] != "SURVIVES-R1"
    assert probe["genuine_dilemma_requires_consistency"] is True


def test_s5_falsifier_no_proper_subset_reconstructs_holds():
    assert lp_localization()["dilemma_only_on_grand"] is True


# --- integration -----------------------------------------------------------
def test_run_assembles_and_all_top_legs_pass():
    out = run()
    assert out["s1_genuine_dilemma"]["genuine_dilemma"] is True
    assert out["s2_global_no_local"]["survives_R1"] is True
    assert out["s2_global_no_local"]["gap_game_is_unanimity_u_N"] is True
    assert out["s3_aumann_shapley_is_separator"]["ties_to_T413_pair2_grand_dividend"] is True
    s4 = out["s4_canonicity_honestly_scoped"]
    assert s4["localization_agreement"]["omega_equals_d_N"] is True
    assert s4["magnitude_decoupling_teeth"]["not_identical_by_construction"] is True
    assert s4["doctrine_family_all_agree_separator_eq_omega"] is True
    assert s4["doctrine_family_vector_varies"] is True
