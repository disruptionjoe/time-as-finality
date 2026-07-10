"""Tests for T525: repaired S1 manifoldlikeness suite."""

from __future__ import annotations

import unittest

from models.t525_repaired_s1_manifoldlikeness_suite import (
    VERDICT_NO_SURVIVOR,
    run_t525_analysis,
)


class RepairedS1ManifoldlikenessSuiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t525_analysis()
        cls.by_name = {audit.name: audit for audit in cls.result.candidate_audits}
        cls.bands = {band.event_count: band for band in cls.result.calibration_bands}

    def test_random_controls_pass_after_order_dimension_quarantine(self) -> None:
        self.assertTrue(self.result.random_controls_pass_repaired_suite)
        self.assertEqual(self.bands[16].order_dimension_obstruction_count, 8)
        self.assertEqual(self.bands[20].order_dimension_obstruction_count, 8)
        n16 = self.by_name["random_1p1_sprinkle_n16_seed0"]
        self.assertTrue(n16.order_dimension_quarantined)
        self.assertTrue(n16.repaired_filter_passed)

    def test_hard_negative_controls_remain_rejected(self) -> None:
        self.assertTrue(self.result.hard_negative_controls_rejected)
        self.assertEqual(
            self.by_name["hub_order_control"].original_t126_classification,
            "hub_nonlocality_obstruction",
        )
        self.assertFalse(self.by_name["hub_order_control"].repaired_filter_passed)
        self.assertFalse(self.by_name["degenerate_chain_control"].repaired_filter_passed)
        self.assertFalse(
            self.by_name["complete_bipartite_layer_control"].repaired_filter_passed
        )

    def test_current_finite_colimits_do_not_survive_repaired_suite(self) -> None:
        self.assertFalse(self.result.current_finite_colimits_survive_repaired_suite)
        self.assertEqual(self.result.current_finite_colimit_survivor_count, 0)
        self.assertTrue(self.result.t249_grid_rejected_by_repaired_suite)
        self.assertTrue(self.result.t252_ordinal_rejected_by_repaired_suite)

    def test_t249_and_t252_fail_different_repaired_statistics(self) -> None:
        t249 = self.by_name["t249_grid_colimit"]
        t252 = self.by_name["t252_ordinal_band_control"]

        self.assertTrue(t249.ordering_fraction_in_band)
        self.assertFalse(t249.largest_interval_in_band)
        self.assertIn("largest_interval_outside_random_band", t249.reason)

        self.assertTrue(t252.ordering_fraction_in_band)
        self.assertFalse(t252.width_in_band)
        self.assertIn("width_outside_random_band", t252.reason)

    def test_verdict_and_claim_language_are_scoped(self) -> None:
        self.assertEqual(self.result.verdict, VERDICT_NO_SURVIVOR)
        self.assertIn("S1 remains `requires_added_assumption`", self.result.s1_update)
        self.assertIn("no S1 promotion", self.result.claim_ledger_update)
        self.assertIn("does not derive spacetime", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
