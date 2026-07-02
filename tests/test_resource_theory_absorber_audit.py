"""Tests for T404: Resource-Theory Absorber Audit of the T407 C(R) object."""

import json

import pytest

from models.resource_theory_absorber_audit import (
    ARTIFACT,
    DEMOTION_CLAUSE,
    FALSIFICATION_CONDITIONS,
    FROM_MEMORY_FLAGS,
    OVERALL_VERDICT,
    RELATION_TO_T398,
    SOURCE_ARTIFACT,
    VERDICT_CAUSAL_INDEXING,
    VERDICT_DECLARED_RECORD,
    VERDICT_LEG_A,
    VERDICT_PROFILE_MAP,
    run_audit,
)


@pytest.fixture(scope="module")
def res():
    return run_audit()


# ---- identity / scope ----------------------------------------------------- #

def test_artifact_identity_and_no_promotion(res):
    assert res["artifact"] == ARTIFACT
    assert res["source_artifact"] == SOURCE_ARTIFACT == (
        "T407-region-capability-no-go"
    )
    assert res["claim_ledger_update"] == "none; no claim promotion"
    assert res["relation_to_t398"] == RELATION_TO_T398


def test_frame_is_declared_before_numbers(res):
    frame = res["rt_frame"]
    assert "CPTP" in frame["free_operations"]
    assert "fixed once" in frame["free_operations"]
    assert "rho_R" in frame["states"]
    assert "monotone" in frame["preorder_and_monotones"]


# ---- Leg A: anti-scalar absorbed as theorem-shape ------------------------- #

def test_leg_a_majorization_analog_is_incomparable(res):
    analog = res["leg_a_anti_scalar"]["standard_analog"]
    assert analog["p_majorizes_q"] is False
    assert analog["q_majorizes_p"] is False
    assert analog["majorization_incomparable"] is True
    # the two tail monotones order the pair strictly oppositely
    e1_p, e1_q = analog["tail_monotone_E1_p_q"]
    e2_p, e2_q = analog["tail_monotone_E2_p_q"]
    assert e1_p < e1_q and e2_p > e2_q
    assert "FROM MEMORY" in analog["attribution"]


def test_leg_a_shape_identity_with_featured_pair(res):
    leg_a = res["leg_a_anti_scalar"]
    assert leg_a["standard_analog"]["certificate_shape"] == [-1, 1]
    assert leg_a["t397_featured_pair"]["certificate_shape"] == [-1, 1]
    assert leg_a["shape_identical"] is True
    assert leg_a["scalar_impossible_shape"] is True


def test_leg_a_grid_is_monotone_vector_normal_form(res):
    grid = res["leg_a_anti_scalar"]["grid_normal_form"]
    assert grid["n_undo_levels"] == 3
    assert grid["n_readout_levels"] == 4
    assert grid["is_exact_product_order"] is True


def test_leg_a_verdict_is_absorbed(res):
    assert res["verdicts"]["leg_a"] == VERDICT_LEG_A
    assert res["verdicts"]["leg_a"].startswith("absorbed_as_theorem_shape")


# ---- Leg B1: profile-from-state factorization (absorbed content) ---------- #

def test_profile_factorization_holds_exactly(res):
    b1 = res["leg_b1_profile_factorization"]
    assert b1["n_configs"] == 24
    assert b1["n_family_fingerprint_classes"] == 18
    assert b1["n_single_state_classes"] == 18
    assert b1["partitions_equal"] is True
    assert b1["profile_factorization_violations"] == []
    assert b1["profile_factors_through_state"] is True
    assert b1["single_state_suffices_in_family"] is True


def test_merged_fingerprints_are_exactly_burn_none_pairs(res):
    b1 = res["leg_b1_profile_factorization"]
    assert b1["n_merged_classes"] == 6
    assert b1["merged_classes_are_exactly_burn_none_pairs"] is True
    assert b1["statistics_factor_through_state"] is True
    assert b1["statistics_factor_max_violation"] < 1e-12


def test_profile_map_verdict_is_absorbed_not_residue(res):
    assert res["verdicts"]["leg_b_profile_map"] == VERDICT_PROFILE_MAP
    assert "absorbed content, not residue" in VERDICT_PROFILE_MAP


# ---- Leg B2: causal indexing (residue candidate a) ------------------------ #

def test_escape_chains_show_forced_monotone_loss(res):
    chains = res["leg_b2_causal_indexing"]["escape_chains"]
    assert chains["n_chains"] == 6
    assert chains["all_chains_monotone"] is True
    assert chains["n_chains_with_strict_drop"] == 6
    assert chains["burn_null_inert"] is True
    assert chains["burn_null_max_profile_diff"] < 1e-9


def test_free_class_cannot_touch_outside_but_escape_writes_do(res):
    boundary = res["leg_b2_causal_indexing"]["boundary_certificates"]
    assert boundary["free_ops_leave_outside_invariant"] is True
    assert boundary["menu_max_outside_marginal_move"] < 1e-12
    assert boundary["escape_write_outside_move"]["class"] >= 0.25
    assert boundary["escape_write_outside_move"]["full"] >= 0.25
    assert boundary["correlating_escape_writes_exceed_floors"] is True
    assert boundary["escape_write_ce_correlation"]["class"] >= 0.15
    assert boundary["escape_write_ce_correlation"]["none"] < 1e-12
    assert boundary["burn_creates_no_ce_correlation"] is True


def test_fixed_frame_enumeration_trilemma(res):
    frames = res["leg_b2_causal_indexing"]["frame_enumeration"]
    table = frames["frames"]
    # F_R: sound for the no-go, silent on the loss
    assert table["CPTP(R)"]["no_go_sound"] is True
    assert table["CPTP(R)"]["loss_expressible_as_free_conversion"] is False
    assert frames["f_r_worst_phi_independence"] < 1e-12
    assert frames["f_r_worst_channel_bound"] < 0.9
    # F_RE: internalizes the loss, loses the no-go (explicit free protocol
    # restores every undo value to 1.0)
    assert table["CPTP(R+E)"]["loss_expressible_as_free_conversion"] is True
    assert table["CPTP(R+E)"]["no_go_sound"] is False
    assert table["CPTP(R+E)"]["restores_all_undo_to_one"] is True
    assert frames["min_restored_visibility_over_24x2"] >= 1.0 - 1e-9
    assert frames["boundary_crossing_inverse_outside_move"] >= 0.25
    # F_product: same silence as F_R
    assert (
        table["CPTP(R) (x) CPTP(E)"]["loss_expressible_as_free_conversion"]
        is False
    )
    # the trilemma
    assert frames["no_fixed_frame_carries_all_three_legs"] is True


def test_causal_indexing_residue_located_with_honest_flag(res):
    b2 = res["leg_b2_causal_indexing"]
    assert b2["residue_located"] is True
    assert res["verdicts"]["leg_b_causal_indexing"] == VERDICT_CAUSAL_INDEXING
    assert VERDICT_CAUSAL_INDEXING.startswith("residue_located_static_frame")
    assert "dynamical" in VERDICT_CAUSAL_INDEXING
    assert "unverified" in VERDICT_CAUSAL_INDEXING
    assert "T393" in b2["frame_enumeration"]["t393_citation"]


# ---- Leg B3: declared-record epistemics (residue candidate b) ------------- #

def test_flat_class_spans_all_resource_objects(res):
    b3 = res["leg_b3_declared_record"]
    assert sorted(b3["statistics_partition_sizes"]) == [8, 16]
    assert b3["flat_class_size"] == 16
    assert b3["n_resource_objects_realized_in_flat_class"] == 12
    assert b3["flat_class_spans_all_resource_objects"] is True
    assert b3["undo_axis_span_in_flat_class"] == [3, 3]
    assert b3["readout_axis_span_in_flat_class"] == [4, 4]


def test_two_way_non_reduction(res):
    b3 = res["leg_b3_declared_record"]
    fwd = b3["profile_does_not_factor_through_record"]
    assert fwd["stats_max_diff"] < 1e-12
    assert min(fwd["capability_gaps_both_directions"]) >= 0.5
    bwd = b3["record_does_not_factor_through_resource_object"]
    assert bwd["profile_max_diff"] < 1e-9
    assert bwd["stats_max_diff"] >= 0.05
    assert b3["two_way_non_reduction"] is True


def test_experiment_map_is_a_state_functional(res):
    exp = res["leg_b3_declared_record"]["experiment_map_is_state_functional"]
    assert exp["max_diff_readout_vs_rho_r_diagonal"] < 1e-12
    assert exp["is_functional"] is True


def test_declared_record_residue_located_with_honest_flag(res):
    b3 = res["leg_b3_declared_record"]
    assert b3["residue_located"] is True
    assert res["verdicts"]["leg_b_declared_record"] == VERDICT_DECLARED_RECORD
    assert VERDICT_DECLARED_RECORD.startswith(
        "residue_located_frame_interface"
    )
    assert "Blackwell" in VERDICT_DECLARED_RECORD
    assert "unverified" in VERDICT_DECLARED_RECORD


# ---- overall verdict structure -------------------------------------------- #

def test_overall_verdict_and_demotion_clause(res):
    assert res["verdicts"]["overall"] == OVERALL_VERDICT
    assert OVERALL_VERDICT.startswith("partially_absorbed_residue_located")
    assert "resource theory with extra bookkeeping" in OVERALL_VERDICT
    assert res["demotion_clause"] == DEMOTION_CLAUSE
    assert "resource theory with extra bookkeeping" in DEMOTION_CLAUSE
    assert "gates the program" in DEMOTION_CLAUSE


def test_from_memory_flags_and_falsification_conditions(res):
    assert res["from_memory_flags"] == list(FROM_MEMORY_FLAGS)
    assert len(FROM_MEMORY_FLAGS) == 4
    assert any("Nielsen" in f for f in FROM_MEMORY_FLAGS)
    assert any("Chitambar-Gour" in f for f in FROM_MEMORY_FLAGS)
    assert any("dynamical" in f for f in FROM_MEMORY_FLAGS)
    assert any("Blackwell" in f for f in FROM_MEMORY_FLAGS)
    assert res["falsification_conditions"] == list(FALSIFICATION_CONDITIONS)
    assert len(FALSIFICATION_CONDITIONS) == 3


def test_no_inflation_vocabulary(res):
    banned = ("theorem proved", "new physics", "law of", "claim promotion:")
    for text in (
        *res["verdicts"].values(),
        res["demotion_clause"],
        *res["falsification_conditions"],
    ):
        assert all(term not in text for term in banned)


def test_result_dict_is_json_serializable(res):
    json.dumps(res, default=float, sort_keys=True)
