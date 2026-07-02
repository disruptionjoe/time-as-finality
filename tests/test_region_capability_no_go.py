"""Pytest suite for T397: Region-Indexed Capability No-Go.

Exact assertions for the three legs of the C(R) claim:

  Leg 1 -- capability profiles are real and region-indexed: fixed region,
  fixed finite menu, fixed task set; profiles exactly computed; menu values
  equal closed-form optima; impossibility legs certified against ALL
  R-supported channels (phi-independence certificate + trace-norm bound),
  not just against the menu.

  Leg 2 -- anti-scalar at the capability level: the realized capability
  poset has incomparable pairs and order dimension exactly 2 (T394's
  imported checkers); scalar failure is witnessed concretely (exhaustive
  weak-order scan on the spotlight subfamily: 0 of 4,683 reproduce) and per
  pair (trichotomy witnesses), not just by the dimension citation.

  Leg 3 -- statistics underdetermine capability: declared-readout statistics
  exactly equal (0.0) across a 16-configuration class realizing all 12
  profiles; featured statistics-identical pair capability-incomparable with
  gaps >= 0.5 both directions; screening-off failure certified with T392's
  imported Bayes-risk / CMI machinery; null controls prove the certificates
  are not vacuous (a statistics-typed probe DOES distinguish another pair)
  and the T393 B'-analog emission null is clean.

Conventions: subsystems index-sorted (c, r1, r2, e1, e2, t); tolerance 1e-12
for every relation claimed exact; verdict strings predeclared as module
constants and asserted verbatim.
"""

import json
import math

import pytest

from models.record_order_tradeoff_probe import u_of_order
from models.region_capability_no_go import (
    ALL_CONFIGS,
    CAP_GAP_MIN,
    C_STAR,
    FEATURED_PAIR,
    HAAR_VISIBILITY_CEILING,
    LEG1_VERDICT,
    LEG2_VERDICT,
    LEG3_VERDICT,
    MEASUREMENT_SETTINGS,
    MENU_GENERATOR_ORDER,
    NAMED_CONFIGS,
    OUTSIDE,
    P_STAR,
    PHI_CERT,
    PHI_LOCK_GRID,
    RECORD,
    REGION,
    SPOTLIGHT_SUBFAMILY,
    TASK_NAMES,
    TOL_EXACT,
    V_STAR,
    menu_protocols,
    run_analysis,
)

PI = math.pi
THIRD = 1.0 / 3.0
TWO_THIRDS = 2.0 / 3.0

# expected profiles of the named configurations, exact rationals
# (undo_within, undo_cross, order_postdiction, class_readout)
EXPECTED_NAMED_PROFILES = {
    "pristine": (1.0, 1.0, THIRD, TWO_THIRDS),
    "full_keeper": (1.0, 1.0, 1.0, 1.0),
    "amnesic_emitter": (0.0, 0.0, THIRD, TWO_THIRDS),
    "publisher": (0.0, 0.0, 1.0, 1.0),
    "class_keeper_class_emitter": (1.0, 0.0, TWO_THIRDS, 1.0),
    "fine_keeper_full_emitter": (0.0, 0.0, TWO_THIRDS, TWO_THIRDS),
    "class_keeper": (1.0, 1.0, TWO_THIRDS, 1.0),
    "z_keeper": (1.0, 1.0, TWO_THIRDS, 1.0),
    "burn_emitter": (1.0, 1.0, THIRD, TWO_THIRDS),
}


@pytest.fixture(scope="module")
def res():
    return run_analysis()


# --------------------------------------------------------------------------- #
# Predeclarations, region, menu, and construction cross-checks
# --------------------------------------------------------------------------- #

def test_predeclared_constants():
    assert V_STAR == 0.9  # imported from T392/T393, unchanged
    assert P_STAR == 0.9 and C_STAR == 0.9
    assert CAP_GAP_MIN == 0.5
    assert TASK_NAMES == (
        "undo_within",
        "undo_cross",
        "order_postdiction",
        "class_readout",
    )
    assert len(PHI_LOCK_GRID) == 8  # T393's uniform locking grid
    assert len(PHI_CERT) == 6  # T393's certificate sweep
    assert math.sqrt(2.0) in PHI_CERT  # incommensurate phases included
    assert len(ALL_CONFIGS) == 24  # exhaustive declared family


def test_region_declared_once_and_partitioned():
    # R excludes the escape registers; the record sub-region sits inside R
    assert set(REGION) & set(OUTSIDE) == set()
    assert set(RECORD) <= set(REGION)
    assert 0 in REGION and 5 in REGION  # control and target inside R


def test_menu_is_finite_and_config_independent():
    protocols = menu_protocols()
    assert len(protocols) == 2 ** len(MENU_GENERATOR_ORDER) == 16
    assert "id" in protocols  # do-nothing included
    assert len(MEASUREMENT_SETTINGS) == 4


def test_construction_cross_checks(res):
    cc = res["leg1"]["cross_checks"]
    assert cc["max_branch_sum_vs_gate_built_diff"] < TOL_EXACT
    assert cc["max_order_unitary_vs_t395_diff"] < TOL_EXACT  # T395 provenance
    assert cc["all_norms_one"] is True


# --------------------------------------------------------------------------- #
# Leg 1: profiles real, menu-achieved, certified
# --------------------------------------------------------------------------- #

def test_named_profiles_exact(res):
    for name, expected in EXPECTED_NAMED_PROFILES.items():
        key = "|".join(NAMED_CONFIGS[name])
        got = res["profiles"][key]["profile"]
        for task, val in zip(TASK_NAMES, expected):
            assert abs(got[task] - val) < 1e-9, (name, task, got[task], val)


def test_menu_achieves_closed_form_optima(res):
    assert res["leg1"]["max_menu_vs_closed_form_residual"] < TOL_EXACT


def test_twelve_distinct_profiles(res):
    assert res["leg1"]["n_configurations"] == 24
    assert res["leg1"]["distinct_profile_count"] == 12


def test_undo_hierarchy_within_ge_cross(res):
    # escaping the class kills cross-class undo before within-class undo
    assert res["leg1"]["undo_within_ge_undo_cross_everywhere"] is True


def test_pass_fail_pattern_typed(res):
    pr = res["profiles"]["|".join(NAMED_CONFIGS["pristine"])]["passes"]
    pub = res["profiles"]["|".join(NAMED_CONFIGS["publisher"])]["passes"]
    mid = res["profiles"][
        "|".join(NAMED_CONFIGS["class_keeper_class_emitter"])
    ]["passes"]
    assert pr == {
        "undo_within": True,
        "undo_cross": True,
        "order_postdiction": False,
        "class_readout": False,
    }
    assert pub == {
        "undo_within": False,
        "undo_cross": False,
        "order_postdiction": True,
        "class_readout": True,
    }
    assert mid == {
        "undo_within": True,
        "undo_cross": False,
        "order_postdiction": False,
        "class_readout": True,
    }


def test_zero_legs_all_certified_against_all_channels(res):
    cert = res["certificates"]
    assert cert["n_zero_legs"] == 18
    assert cert["all_zero_legs_certified"] is True
    for leg in cert["zero_legs"].values():
        # (i) the region state is exactly phi-independent: no R-supported
        # channel output can depend on the prepared phase (T393 pattern)
        assert leg["phi_independence_max_pairwise_diff"] < TOL_EXACT
        # (ii) the channel-independent trace-norm bound is numerically zero,
        # far below v*: every CPTP map on R is covered at once
        assert leg["channel_bound"] < 1e-9
        assert leg["menu_max"] < 1e-9


def test_pass_legs_have_phi_dependence_teeth(res):
    # where undo succeeds, the region state is genuinely phi-dependent
    assert res["certificates"]["pass_legs_phi_dependence_min"] > 0.1


def test_channel_bound_respects_achievability(res):
    sanity = res["certificates"]["pristine_bound_respects_achievable"]
    assert sanity["channel_bound"] >= sanity["achieved"] - TOL_EXACT


def test_haar_spot_check_illustrative(res):
    haar = res["certificates"]["haar_spot_check"]
    assert haar["max_locked_visibility"] < HAAR_VISIBILITY_CEILING


def test_manufactured_coherence_null(res):
    # raw coherence is gameable by a discard-and-reprepare channel on R;
    # the phase-locked figure of merit nulls it exactly (T392 lemma)
    mc = res["certificates"]["manufactured_coherence_null"]
    assert mc["raw_normalized"] > 1.0
    assert mc["locked"] < TOL_EXACT


# --------------------------------------------------------------------------- #
# Leg 2: the realized capability poset and the anti-scalar witnesses
# --------------------------------------------------------------------------- #

def test_poset_shape(res):
    l2 = res["leg2"]
    assert l2["n_profiles"] == 12
    assert l2["natural_labeling"] is True
    assert l2["relation_size"] == 48
    assert l2["n_incomparable_pairs"] == 18
    assert l2["relation_size"] + l2["n_incomparable_pairs"] == 66  # C(12,2)
    assert l2["is_chain"] is False


def test_featured_pairs_are_incomparable(res):
    l2 = res["leg2"]
    labels = {tuple(p): i for i, p in enumerate(l2["profiles_by_label"])}
    prof = res["profiles"]

    def label_of(name):
        e = prof["|".join(NAMED_CONFIGS[name])]["profile"]
        return labels[tuple(round(e[t], 9) for t in TASK_NAMES)]

    incomp = {tuple(p) for p in l2["incomparable_pairs"]}
    pairs = [
        ("pristine", "publisher"),
        ("pristine", "class_keeper_class_emitter"),
        ("class_keeper_class_emitter", "publisher"),
    ]
    for a, b in pairs:
        la, lb = label_of(a), label_of(b)
        assert (min(la, lb), max(la, lb)) in incomp, (a, b)


def test_order_dimension_exactly_two_via_t394(res):
    l2 = res["leg2"]
    # dim >= 2: incomparable pair exists (T394 Theorem 2, the T49 rung)
    assert l2["n_incomparable_pairs"] > 0
    # dim == 2: T394's exhaustive realizer search (imported checker)
    assert l2["order_dimension"] == 2
    assert l2["realizer_reconstruction_verified"] is True
    assert len(l2["realizer"]) == 2
    assert len(l2["two_axis_magnitudes"]) == 12


def test_grid_product_structure(res):
    gp = res["leg2"]["grid_product_structure"]
    assert gp["n_undo_levels"] == 3
    assert gp["n_readout_levels"] == 4
    assert gp["undo_part_is_chain"] is True
    assert gp["readout_part_is_chain"] is True
    assert gp["is_exact_product_order"] is True
    # Hasse edge count of the 3x4 grid: 3*(4-1) + 4*(3-1) = 17
    assert len(res["leg2"]["hasse_edges"]) == 17


def test_exhaustive_scalar_refutation(res):
    sr = res["leg2"]["scalar_refutation_exhaustive"]
    assert set(sr["subfamily"]) == set(SPOTLIGHT_SUBFAMILY)
    assert sr["n_weak_orders_scanned"] == 4683  # all total preorders on 6
    assert sr["n_reproducing_scalars"] == 0
    # restriction-completeness: 6 distinct profiles in the subfamily
    assert len({tuple(p) for p in sr["subfamily_profiles"]}) == 6


def test_trichotomy_witnesses_concrete(res):
    tw = res["leg2"]["trichotomy_witnesses"]["pristine_vs_publisher"]
    assert tw["incomparable"] is True
    assert set(tw["tasks_where_first_strictly_better"]) == {
        "undo_within",
        "undo_cross",
    }
    assert set(tw["tasks_where_second_strictly_better"]) == {
        "order_postdiction",
        "class_readout",
    }
    assert tw["max_gap_first_direction"] > CAP_GAP_MIN
    assert tw["max_gap_second_direction"] > CAP_GAP_MIN
    tw2 = res["leg2"]["trichotomy_witnesses"][
        "class_keeper_class_emitter_vs_publisher"
    ]
    assert tw2["incomparable"] is True


# --------------------------------------------------------------------------- #
# Leg 3: statistics underdetermine capability
# --------------------------------------------------------------------------- #

def test_statistics_partition_two_classes(res):
    sp = res["leg3"]["statistics_partition"]
    assert sp["n_classes"] == 2
    assert sorted(sp["class_sizes"]) == [8, 16]
    assert sp["max_intra_class_diff"] < TOL_EXACT
    assert sp["min_inter_class_diff"] > 0.05  # the partition has teeth


def test_flat_class_realizes_all_profiles(res):
    l3 = res["leg3"]
    assert l3["flat_class_size"] == 16
    assert l3["n_profiles_realized_in_flat_class"] == 12
    assert l3["flat_class_realizes_all_profiles"] is True


def test_featured_pair_stats_equal_capability_incomparable(res):
    fp = res["leg3"]["featured_pair"]
    assert fp["configs"] == list(FEATURED_PAIR)
    assert fp["stats_max_diff"] < TOL_EXACT
    a_dir, b_dir = fp["max_gap_each_direction"]
    assert a_dir >= CAP_GAP_MIN and b_dir >= CAP_GAP_MIN
    assert fp["gap_floor_met_both_directions"] is True
    # incomparability of the featured pair, from the gaps themselves
    gaps = fp["gaps_first_minus_second"]
    assert any(g > 1e-9 for g in gaps.values())
    assert any(g < -1e-9 for g in gaps.values())


def test_capability_test_undecidable_by_statistics(res):
    ct = res["leg3"]["capability_test_undecidable_by_statistics"]
    # the capability-typed test varies on a class where every declared
    # statistic is constant: no statistics-typed functional decides it
    assert ct["flat_class_statistics_constant"] is True
    assert ct["test_nonconstant_on_flat_class"] is True
    assert ct["n_pass"] > 0 and ct["n_fail"] > 0
    assert ct["n_pass"] + ct["n_fail"] == 16


def test_screening_statistics_carry_zero(res):
    sc = res["leg3"]["screening"]
    for lift in sc["statistics_lift"].values():
        assert abs(lift) < TOL_EXACT
    assert sc["mutual_information_verdict_vs_statistics_bits"] < TOL_EXACT
    # the declared readout is exactly useless: risk equals the prior risk
    for loss in sc["prior_only_risk"]:
        assert abs(
            sc["full_declared_readout_risk"][loss] - sc["prior_only_risk"][loss]
        ) < TOL_EXACT


def test_screening_probe_positive_across_loss_family(res):
    sc = res["leg3"]["screening"]
    # T155 discipline: positive lift on the whole three-loss family
    for lift in sc["probe_lift"].values():
        assert lift > 0.3
    assert abs(sc["probe_lift"]["zero_one"] - 1.0 / 3.0) < 1e-9
    assert abs(sc["cmi_verdict_probe_given_statistics_bits"] - 2.0 / 3.0) < 1e-9


def test_t137_downstream_null(res):
    sc = res["leg3"]["screening"]
    for lift in sc["t137_null_lift"].values():
        assert abs(lift) < TOL_EXACT
    assert sc["t137_null_cmi_bits"] < TOL_EXACT


def test_vacuity_control_statistics_do_distinguish_another_pair(res):
    vc = res["leg3"]["vacuity_control"]
    assert vc["stats_max_diff"] > 0.05
    assert abs(vc["zero_one_lift_from_statistics"] - 0.25) < 1e-9


def test_converse_pair_capability_identical_statistics_distinct(res):
    cp = res["leg3"]["converse_pair"]
    assert cp["profile_max_diff"] < 1e-9  # C(R) identifies them
    assert cp["stats_max_diff"] > 0.05  # statistics distinguish them
    # so neither typing refines the other in this family


def test_burn_null_emission_alone_is_innocuous(res):
    bn = res["leg3"]["burn_null"]
    assert bn["profile_max_diff_vs_pristine"] < 1e-9
    assert bn["stats_max_diff_vs_pristine"] < TOL_EXACT
    # while the emission itself is real (T393 B' pattern)
    assert abs(bn["excitation_probability_burn"] - 1.0) < 1e-9
    assert bn["excitation_probability_pristine"] < TOL_EXACT


# --------------------------------------------------------------------------- #
# Guardrails and verdict restraint
# --------------------------------------------------------------------------- #

def test_q1d_no_signalling(res):
    ns = res["no_signalling"]
    assert ns["max_readout_diff_over_phase"] < TOL_EXACT
    assert ns["max_readout_diff_over_escape_writes"] < TOL_EXACT
    assert ns["max_c_r_marginal_diff_over_settings"] < TOL_EXACT
    # teeth: the same setting changes move the target marginal
    assert ns["max_target_marginal_span_over_settings"] > 0.05


def test_verdict_strings_predeclared_and_restrained(res):
    assert res["verdicts"]["leg1"] == LEG1_VERDICT
    assert res["verdicts"]["leg2"] == LEG2_VERDICT
    assert res["verdicts"]["leg3"] == LEG3_VERDICT
    assert "not a statement about physical agents" in LEG1_VERDICT
    assert "not a theorem about physical agents" in LEG2_VERDICT
    assert "finite observation in this family, not a theorem" in LEG3_VERDICT
    for v in res["verdicts"].values():
        for banned in ("theorem proved", "law", "discovery", "promotes"):
            assert banned not in v


def test_t395_order_machinery_provenance():
    # the k = 3 family is T395's canonical subset, used via its own builder
    from models.region_capability_no_go import K3_ORDERS, CLASS_OF

    assert list(K3_ORDERS) == [(0, 1, 2), (1, 0, 2), (2, 0, 1)]
    assert CLASS_OF == (0, 1, 0)
    assert u_of_order((0, 1, 2)) is not None


def test_result_dict_is_json_serializable(res):
    json.dumps(res, default=float)
