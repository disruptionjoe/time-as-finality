"""Tests for T147: Q1A current-family closure."""

from __future__ import annotations

import unittest

from models.q1a_current_family_closure import run_t147_analysis


class Q1ACurrentFamilyClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t147_analysis()

    def test_closure_key_recovers_every_current_d1_verdict(self) -> None:
        self.assertTrue(self.result.closure_classifier_matches_d1)
        self.assertTrue(self.result.d1_factors_through_closure_key)
        self.assertTrue(
            all(case.classifier_matches_d1 for case in self.result.visible_cases)
        )

    def test_branch_and_reversal_dimensions_add_no_verdict_content(self) -> None:
        self.assertTrue(self.result.branch_support_factors_through_closure_key)
        self.assertTrue(self.result.reversal_cost_factors_through_closure_key)
        self.assertFalse(self.result.branch_support_load_bearing)
        self.assertFalse(self.result.reversal_cost_load_bearing)

    def test_raw_redundancy_cannot_replace_the_closure_key(self) -> None:
        self.assertTrue(self.result.raw_redundancy_is_not_sufficient)
        raw_three_fibers = [
            fiber
            for fiber in self.result.fibers
            if 3 in fiber.raw_accessible_redundancies
        ]
        self.assertGreaterEqual(len(raw_three_fibers), 2)
        self.assertTrue(
            any("finalized" in fiber.d1_verdicts for fiber in raw_three_fibers)
        )
        self.assertTrue(
            any("not_finalized" in fiber.d1_verdicts for fiber in raw_three_fibers)
        )

    def test_hidden_partition_control_withholds_under_the_same_rule(self) -> None:
        hidden = self.result.hidden_partition_case
        self.assertFalse(hidden.partition_visible)
        self.assertIsNone(hidden.accessible_provenance_support)
        self.assertEqual(hidden.d1_verdict, "withhold_partition_unavailable")
        self.assertEqual(hidden.closure_verdict, "withhold_partition_unavailable")

    def test_current_family_is_closed_but_not_upgraded(self) -> None:
        self.assertTrue(self.result.current_family_closed_under_declared_dimensions)
        self.assertIn("current enumerated Q1A fixed-data family", self.result.strongest_claim)
        self.assertIn("not presently a measurement-dynamics claim", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
