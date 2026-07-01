"""Tests for T380 compatibility signal-basis forcing screen."""

from __future__ import annotations

from fractions import Fraction
import unittest

from models.compatibility_signal_basis_screen import (
    CompatibilityVector,
    QuadraticForm,
    canonical_form,
    canonical_scaling_checks,
    c_equals_one_is_unit_normalization,
    evaluate_basis_candidates,
    reciprocal_scaling_preserves_interval,
    rest_rendered_steps,
    run_t380_analysis,
    solve_null_forms,
    substrate_intervals_match_forced_form,
)


class CompatibilitySignalBasisScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t380_analysis()
        self.verdicts = {
            verdict.candidate_id: verdict for verdict in self.result.basis_verdicts
        }

    def test_two_independent_null_channels_force_product_interval(self) -> None:
        verdict = self.verdicts["two_independent_null_channels"]
        self.assertTrue(verdict.passes)
        self.assertEqual(verdict.status, "product_interval_forced_up_to_scale")
        self.assertEqual(verdict.span_dimension, 2)
        self.assertEqual(verdict.null_solution_dimension, 1)
        self.assertEqual(verdict.forced_form, canonical_form())
        self.assertTrue(self.result.two_channel_basis_forces_product_interval)

        form = verdict.forced_form
        self.assertIsNotNone(form)
        self.assertEqual(
            form.evaluate(CompatibilityVector("left", Fraction(1), Fraction(0))),
            Fraction(0),
        )
        self.assertEqual(
            form.evaluate(CompatibilityVector("right", Fraction(0), Fraction(1))),
            Fraction(0),
        )
        self.assertEqual(
            form.evaluate(CompatibilityVector("timelike", Fraction(1), Fraction(1))),
            Fraction(1),
        )

    def test_c_equals_one_is_rest_rendering_unit_normalization(self) -> None:
        self.assertTrue(c_equals_one_is_unit_normalization())
        self.assertTrue(self.result.c_equals_one_is_unit_normalization)
        steps = {step.channel: step for step in rest_rendered_steps()}
        self.assertEqual(steps["left_signal"].speed, Fraction(1))
        self.assertEqual(steps["right_signal"].speed, Fraction(-1))
        self.assertEqual(steps["left_signal"].delta_time, Fraction(1, 2))
        self.assertEqual(steps["right_signal"].delta_time, Fraction(1, 2))

    def test_reciprocal_scaling_preserves_interval_and_nonreciprocal_fails(self) -> None:
        self.assertTrue(reciprocal_scaling_preserves_interval())
        self.assertTrue(self.result.reciprocal_scaling_preserves_interval)
        self.assertTrue(self.result.nonreciprocal_scaling_fails)

        reciprocal_a, reciprocal_b, nonreciprocal = canonical_scaling_checks()
        self.assertEqual(reciprocal_a.determinant, Fraction(1))
        self.assertEqual(reciprocal_b.determinant, Fraction(1))
        self.assertTrue(reciprocal_a.preserves_interval)
        self.assertTrue(reciprocal_b.preserves_interval)
        self.assertEqual(nonreciprocal.determinant, Fraction(4))
        self.assertFalse(nonreciprocal.preserves_interval)

    def test_single_channel_and_collinear_controls_do_not_force_basis(self) -> None:
        single = self.verdicts["single_null_channel"]
        collinear = self.verdicts["collinear_two_channels"]
        self.assertFalse(single.passes)
        self.assertEqual(single.status, "underdetermined")
        self.assertEqual(single.null_solution_dimension, 2)
        self.assertTrue(self.result.single_channel_underdetermined)

        self.assertFalse(collinear.passes)
        self.assertEqual(collinear.status, "not_a_two_direction_basis")
        self.assertEqual(collinear.span_dimension, 1)
        self.assertTrue(self.result.collinear_channels_do_not_form_basis)

    def test_three_noncollinear_null_channels_overconstrain_form(self) -> None:
        verdict = self.verdicts["three_noncollinear_null_channels"]
        self.assertFalse(verdict.passes)
        self.assertEqual(verdict.status, "overconstrained")
        self.assertEqual(verdict.null_solution_dimension, 0)
        self.assertIsNone(verdict.forced_form)
        self.assertTrue(self.result.three_noncollinear_null_channels_fail)

    def test_extra_collinear_channel_is_redundant_not_new_primitive_signal(self) -> None:
        verdict = self.verdicts["extra_collinear_null_channel"]
        self.assertTrue(verdict.passes)
        self.assertEqual(verdict.status, "redundant_channel_factors_through_basis")
        self.assertEqual(verdict.span_dimension, 2)
        self.assertEqual(verdict.null_solution_dimension, 1)
        self.assertEqual(verdict.forced_form, canonical_form())
        self.assertTrue(self.result.extra_collinear_channel_is_redundant)

    def test_forced_form_matches_generated_substrate_intervals(self) -> None:
        matched, checked = substrate_intervals_match_forced_form()
        self.assertTrue(matched)
        self.assertEqual(checked, 4950)
        self.assertTrue(self.result.substrate_intervals_match_forced_form)
        self.assertEqual(self.result.checked_substrate_pair_count, 4950)

    def test_null_form_solver_matches_expected_dimensions(self) -> None:
        left = CompatibilityVector("left", Fraction(1), Fraction(0))
        right = CompatibilityVector("right", Fraction(0), Fraction(1))
        diagonal = CompatibilityVector("diagonal", Fraction(1), Fraction(1))
        self.assertEqual(len(solve_null_forms((left,))), 2)
        self.assertEqual(len(solve_null_forms((left, right))), 1)
        self.assertEqual(len(solve_null_forms((left, right, diagonal))), 0)

    def test_hostile_comparators_keep_basis_boundary_honest(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertFalse(by_id["minkowski_metric_import"].absorbs)
        self.assertTrue(by_id["two_channel_basis_import"].absorbs)
        self.assertTrue(by_id["null_signal_assumption"].absorbs)
        self.assertTrue(by_id["bilinear_interval_premise"].absorbs)
        self.assertFalse(by_id["numeric_c_equals_one"].absorbs)
        self.assertTrue(by_id["compatibility_alone"].absorbs)

    def test_overall_verdict_is_boundary_result_not_full_derivation(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "product_interval_forced_given_two_null_channels_but_signal_basis_not_derived",
        )
        self.assertFalse(self.result.basis_fully_derived_from_compatibility_alone)
        self.assertIn("basis is still the live imported object", self.result.claim_ledger_update)
        self.assertIn("not derived from compatibility alone", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
