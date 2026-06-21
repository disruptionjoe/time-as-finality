"""Tests for T157: T54 ordering-fraction bridge."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.finality_descent_theorem import complete_observer_descent_datum
from models.myrheim_meyer_ordering_fraction_screen import (
    deterministic_flat_interval_control,
)
from models.t54_ordering_fraction_bridge import (
    flat_1p1_t54_datum,
    run_t157_analysis,
)


class T54OrderingFractionBridgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t157_analysis()
        self.by_name = {audit.name: audit for audit in self.result.audits}

    def test_flat_candidate_is_a_genuine_t54_completion(self) -> None:
        completion = complete_observer_descent_datum(flat_1p1_t54_datum())
        control = deterministic_flat_interval_control()

        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertIsNotNone(completion.partial_order)
        self.assertEqual(
            frozenset(completion.partial_order.order_pairs),
            control.relation,
        )

    def test_flat_t54_candidate_reaches_t126_and_matches_target(self) -> None:
        audit = self.by_name["t157_flat_1p1_t54_colimit"]

        self.assertTrue(audit.t54_theorem_applies)
        self.assertEqual(audit.t54_classification, "canonical")
        self.assertEqual(audit.t126_classification, "passes_filter_only")
        self.assertTrue(audit.t126_filter_passed)
        self.assertEqual(audit.event_count, 6)
        self.assertEqual(audit.strict_pair_count, 7)
        self.assertEqual(audit.ordering_fraction, Fraction(7, 15))
        self.assertEqual(audit.absolute_gap, Fraction(1, 30))
        self.assertEqual(
            audit.verdict,
            "t54_colimit_matches_ordering_fraction_control_only",
        )

    def test_product_grid_remains_over_ordered_after_t54_completion(self) -> None:
        audit = self.by_name["t157_product_grid_2x3_t54_colimit"]

        self.assertTrue(audit.t54_theorem_applies)
        self.assertTrue(audit.t126_filter_passed)
        self.assertEqual(audit.ordering_fraction, Fraction(4, 5))
        self.assertEqual(audit.verdict, "t54_colimit_fails_ordering_fraction_target")

    def test_chain_control_blocks_before_target_interpretation(self) -> None:
        audit = self.by_name["t157_chain_6_t54_colimit"]

        self.assertTrue(audit.t54_theorem_applies)
        self.assertEqual(audit.t126_classification, "rank_width_obstruction")
        self.assertFalse(audit.t126_filter_passed)
        self.assertEqual(audit.verdict, "blocked_at_t126")

    def test_aggregate_claim_language_remains_non_upgrade(self) -> None:
        self.assertTrue(self.result.t54_flat_candidate_reaches_t126_scale)
        self.assertTrue(self.result.t54_flat_candidate_matches_target_band)
        self.assertTrue(self.result.t54_product_grid_control_fails_target_band)
        self.assertTrue(self.result.t54_chain_control_blocked_before_target)
        self.assertTrue(self.result.previous_t156_open_blocker_removed)
        self.assertIn("does not upgrade S1", self.result.weakened_or_falsified)
        self.assertIn("does not estimate dimension", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
