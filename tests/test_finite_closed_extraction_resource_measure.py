"""Tests for the finite-closed extraction-resource measure support artifact."""

from models.finite_closed_extraction_resource_measure import (
    run,
    t411_departed_record_shadow,
    t413_grand_coalition_shadow,
    t417_quadratic_residuosity_shadow,
)


def test_each_witness_has_visible_boundary_but_closed_code_determines_datum():
    for witness in (
        t411_departed_record_shadow(),
        t413_grand_coalition_shadow(),
        t417_quadratic_residuosity_shadow(),
    ):
        assert witness.datum_factors_through_visible_signature() is False
        assert witness.boundary_pairs()
        assert witness.closed_code_determines_datum() is True


def test_single_instance_lookup_upper_bounds_are_finite():
    for witness in (
        t411_departed_record_shadow(),
        t413_grand_coalition_shadow(),
        t417_quadratic_residuosity_shadow(),
    ):
        assert witness.finite_lookup_upper_bound() == 2


def test_t417_records_conditional_family_level_escape():
    witness = t417_quadratic_residuosity_shadow()
    summary = witness.summary()

    assert summary["gap_mode"] == "E2_hardness_assumption_plus_E1_family_growth"
    assert summary["assumption"] == "Quadratic Residuosity Assumption / factoring hardness"
    assert summary["family_costs"] == [2, 6, 10, 28, 58]
    assert summary["family_costs_strictly_increase"] is True
    assert summary["single_instance_lookup_cost_is_finite"] is True


def test_declared_single_instance_gap_is_not_physical_by_itself():
    t411 = t411_departed_record_shadow().summary()
    t413 = t413_grand_coalition_shadow().summary()

    assert t411["gap_mode"] == "E0_declared_or_crackable"
    assert t411["single_instance_lookup_upper_bound"] == 2
    assert t413["single_instance_lookup_upper_bound"] == 2
    assert t413["family_costs_strictly_increase"] is True


def test_run_summary_keeps_scope_theorem_candidate_and_unpromoted():
    summary = run()

    assert summary["claim_ledger_update"] == "none; support artifact only"
    assert summary["scope_theorem_status"] == "candidate; no promotion"
    assert summary["all_closed_codes_determine_datum"] is True
    assert summary["all_have_visible_boundary_pair"] is True
    assert summary["all_single_instance_bounds_finite"] is True
