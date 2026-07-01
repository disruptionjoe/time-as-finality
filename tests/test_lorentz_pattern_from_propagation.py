"""Tests for T379 Lorentz-pattern rendering from propagation constraints."""

from __future__ import annotations

from fractions import Fraction
import unittest

from models.generated_compatibility_substrate import FORBIDDEN_SOURCE_COLUMNS, source_rows
from models.lorentz_pattern_from_propagation import (
    COMPATIBILITY_SIGNAL_SPEED,
    canonical_substrate,
    derive_render_maps,
    canonical_calibrations,
    intervals_are_invariant,
    pair_invariants,
    primitive_signal_speed_checks,
    render_record,
    rendered_interval,
    run_t379_analysis,
    source_has_no_minkowski_columns,
    time_dilation_checks,
    transform_coefficients,
)
from models.generated_compatibility_substrate import derived_ranks, landmark_ids


class LorentzPatternFromPropagationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t379_analysis()
        self.substrate = canonical_substrate()
        self.render_maps = derive_render_maps(canonical_calibrations())
        self.ranks = derived_ranks(self.substrate)
        self.landmarks = landmark_ids(self.substrate)
        self.by_observer = {
            render_map.observer_id: render_map for render_map in self.render_maps
        }

    def test_source_rows_do_not_import_minkowski_coordinates(self) -> None:
        self.assertTrue(self.result.source_has_no_minkowski_columns)
        self.assertTrue(source_has_no_minkowski_columns(self.substrate))
        self.assertFalse(set(self.substrate.source_columns) & FORBIDDEN_SOURCE_COLUMNS)

        for row in source_rows(self.substrate):
            self.assertFalse(set(row) & FORBIDDEN_SOURCE_COLUMNS)

    def test_render_maps_are_derived_from_round_trip_signal_counts(self) -> None:
        self.assertTrue(self.result.render_maps_derived_from_signal_calibration)
        self.assertTrue(self.result.round_trip_balance_satisfied)

        expected = {
            "A_rest": (Fraction(1, 1), Fraction(0, 1), Fraction(1, 1)),
            "B_fast_outbound": (Fraction(2, 1), Fraction(3, 5), Fraction(5, 4)),
            "C_fast_return": (Fraction(1, 2), Fraction(-3, 5), Fraction(5, 4)),
            "D_mild_outbound": (Fraction(3, 2), Fraction(5, 13), Fraction(13, 12)),
        }
        for observer_id, (scale, beta, gamma) in expected.items():
            with self.subTest(observer_id=observer_id):
                render_map = self.by_observer[observer_id]
                self.assertEqual(render_map.signal_scale, scale)
                self.assertEqual(render_map.beta, beta)
                self.assertEqual(render_map.gamma, gamma)
                self.assertEqual(
                    render_map.signal_scale * render_map.outbound_left_ticks,
                    Fraction(render_map.return_right_ticks, 1) / render_map.signal_scale,
                )

    def test_primitive_signal_speed_is_invariant_for_every_observer(self) -> None:
        self.assertTrue(self.result.primitive_signal_speed_invariant)
        for check in primitive_signal_speed_checks(self.render_maps):
            with self.subTest(observer_id=check.observer_id):
                self.assertEqual(check.speed_unit, COMPATIBILITY_SIGNAL_SPEED)
                self.assertEqual(check.left_channel_speed, Fraction(1, 1))
                self.assertEqual(check.right_channel_speed, Fraction(-1, 1))

    def test_lorentz_pattern_coefficients_are_recovered(self) -> None:
        self.assertTrue(self.result.lorentz_pattern_coefficients_recovered)
        rest_map = self.by_observer["A_rest"]

        for render_map in self.render_maps:
            coefficients = transform_coefficients(render_map)
            with self.subTest(observer_id=render_map.observer_id):
                self.assertEqual(coefficients.determinant, Fraction(1, 1))
                self.assertEqual(coefficients.beta, render_map.beta)
                self.assertEqual(coefficients.gamma, render_map.gamma)

                for record_id in (
                    self.landmarks["near"],
                    self.landmarks["left_only"],
                    self.landmarks["right_only"],
                    self.landmarks["future"],
                ):
                    rest_rendered = render_record(record_id, self.ranks, rest_map)
                    rendered = render_record(record_id, self.ranks, render_map)
                    transformed_time = (
                        coefficients.time_from_rest_time * rest_rendered.signal_time
                        + coefficients.time_from_rest_space * rest_rendered.signal_space
                    )
                    transformed_space = (
                        coefficients.space_from_rest_time * rest_rendered.signal_time
                        + coefficients.space_from_rest_space * rest_rendered.signal_space
                    )
                    self.assertEqual(transformed_time, rendered.signal_time)
                    self.assertEqual(transformed_space, rendered.signal_space)

    def test_time_dilation_matches_gamma_for_rest_calibrations(self) -> None:
        self.assertTrue(self.result.time_dilation_recovered)
        for check in time_dilation_checks(self.substrate, self.render_maps):
            with self.subTest(observer_id=check.observer_id):
                self.assertEqual(check.own_space, Fraction(0, 1))
                self.assertEqual(check.dilation_ratio, check.expected_gamma)

    def test_simultaneity_disagreement_follows_from_derived_render_maps(self) -> None:
        self.assertTrue(self.result.simultaneity_disagreement)
        left_only, right_only = self.result.simultaneity_pair
        rest = self.by_observer["A_rest"]
        boosted = self.by_observer["B_fast_outbound"]
        opposite = self.by_observer["C_fast_return"]

        self.assertEqual(
            render_record(left_only, self.ranks, rest).signal_time,
            render_record(right_only, self.ranks, rest).signal_time,
        )
        self.assertNotEqual(
            render_record(left_only, self.ranks, boosted).signal_time,
            render_record(right_only, self.ranks, boosted).signal_time,
        )
        self.assertNotEqual(
            render_record(left_only, self.ranks, opposite).signal_time,
            render_record(right_only, self.ranks, opposite).signal_time,
        )

    def test_interval_invariant_across_generated_substrate(self) -> None:
        rows = pair_invariants(self.substrate, self.render_maps)
        self.assertEqual(self.result.checked_pair_count, 4950)
        self.assertEqual(len(rows), 4950)
        self.assertTrue(self.result.interval_invariant)
        self.assertTrue(intervals_are_invariant(rows))

        origin = self.landmarks["origin"]
        future = self.landmarks["future"]
        for render_map in self.render_maps:
            with self.subTest(observer_id=render_map.observer_id):
                self.assertEqual(
                    rendered_interval(origin, future, self.ranks, render_map),
                    Fraction(9, 1),
                )

    def test_hostile_comparators_keep_claim_boundary_honest(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }

        self.assertFalse(by_id["minkowski_coordinate_import"].absorbs)
        self.assertFalse(by_id["hand_chosen_observer_scale"].absorbs)
        self.assertTrue(by_id["fixed_light_channel_basis"].absorbs)
        self.assertTrue(by_id["linear_reciprocal_rendering"].absorbs)
        self.assertTrue(by_id["finite_generated_closure"].absorbs)
        self.assertFalse(by_id["causal_order_only"].absorbs)

    def test_overall_verdict_is_lorentz_pattern_calibration(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "lorentz_pattern_recovered_from_signal_constraints_but_channel_premises_absorb",
        )
        self.assertIn("perceived time differences", self.result.claim_ledger_update)
        self.assertIn("not a physical derivation", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
