"""Tests for T159: T54 interval-abundance and jackknife screen."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t54_interval_jackknife_screen import run_t159_analysis


class T54IntervalJackknifeScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t159_analysis()
        self.by_name = {audit.name: audit for audit in self.result.audits}

    def test_flat_parent_passes_prior_and_interval_support_screens(self) -> None:
        audit = self.by_name["t157_flat_1p1_t54_colimit"]

        self.assertTrue(audit.t54_theorem_applies)
        self.assertEqual(audit.t126_classification, "passes_filter_only")
        self.assertEqual(audit.t156_verdict, "passes_ordering_fraction_control_only")
        self.assertEqual(audit.ordering_fraction, Fraction(7, 15))
        self.assertEqual(audit.interval_counts_by_size, ((0, 5), (1, 2)))
        self.assertEqual(audit.largest_interval_size, 1)
        self.assertTrue(audit.parent_interval_support_passed)

    def test_flat_control_is_fragile_under_single_event_deletion(self) -> None:
        audit = self.by_name["t157_flat_1p1_t54_colimit"]
        deletion_by_event = {
            deletion.removed_event: deletion
            for deletion in audit.deletion_audits
        }

        self.assertEqual(audit.deletion_case_count, 6)
        self.assertEqual(audit.deletion_pass_count, 5)
        self.assertEqual(audit.deletion_pass_rate, Fraction(5, 6))
        self.assertFalse(audit.deletion_stability_passed)
        self.assertEqual(audit.verdict, "calibration_only_fragile_jackknife")
        self.assertEqual(deletion_by_event["p4"].ordering_fraction, Fraction(1, 5))
        self.assertFalse(deletion_by_event["p4"].ordering_band_passed)

    def test_product_grid_fails_parent_interval_support(self) -> None:
        audit = self.by_name["t157_product_grid_2x3_t54_colimit"]

        self.assertEqual(audit.t156_verdict, "t126_pass_but_ordering_fraction_fail")
        self.assertEqual(audit.interval_counts_by_size, ((0, 7), (1, 2), (2, 2), (4, 1)))
        self.assertEqual(audit.largest_interval_size, 4)
        self.assertFalse(audit.parent_interval_support_passed)
        self.assertEqual(audit.verdict, "blocked_at_ordering_fraction")

    def test_chain_control_blocks_before_interval_jackknife(self) -> None:
        audit = self.by_name["t157_chain_6_t54_colimit"]

        self.assertEqual(audit.t126_classification, "rank_width_obstruction")
        self.assertFalse(audit.t126_filter_passed)
        self.assertEqual(audit.verdict, "blocked_before_interval_jackknife")

    def test_aggregate_claim_language_demotes_t157_survivor(self) -> None:
        self.assertTrue(self.result.flat_parent_interval_support_passes)
        self.assertTrue(self.result.flat_jackknife_stability_fails)
        self.assertTrue(self.result.product_grid_parent_interval_support_fails)
        self.assertTrue(self.result.chain_control_blocked_before_interval_screen)
        self.assertTrue(self.result.t157_survivor_demoted_to_calibration_only)
        self.assertIn("calibration artifact", self.result.strongest_claim)
        self.assertIn("finite fragility diagnostic only", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
