"""Tests for T105: Q1A accessible-class sufficiency."""

from __future__ import annotations

import unittest

from models.q1a_accessible_class_sufficiency import (
    hidden_partition_case,
    run_t105_analysis,
)


class Q1AAccessibleClassSufficiencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t105_analysis()

    def test_classifier_matches_d1_for_all_visible_cases(self) -> None:
        self.assertTrue(self.result.classifier_matches_all_visible_cases)
        self.assertTrue(all(verdict.classifier_matches_d1 for verdict in self.result.visible_cases))

    def test_same_support_gives_same_verdict_even_when_partitions_differ(self) -> None:
        support_two = [
            verdict
            for verdict in self.result.visible_cases
            if verdict.accessible_provenance_support == 2
        ]
        self.assertGreaterEqual(len(support_two), 2)
        self.assertTrue(all(verdict.d1_verdict == "not_finalized" for verdict in support_two))

    def test_raw_redundancy_three_is_not_sufficient_for_finalization(self) -> None:
        raw_three = [
            verdict
            for verdict in self.result.visible_cases
            if verdict.raw_accessible_redundancy == 3
        ]
        self.assertTrue(any(verdict.d1_verdict == "finalized" for verdict in raw_three))
        self.assertTrue(any(verdict.d1_verdict == "not_finalized" for verdict in raw_three))

    def test_hidden_partition_control_withholds(self) -> None:
        hidden = self.result.hidden_partition_case
        self.assertEqual(hidden.case_id, hidden_partition_case().case_id)
        self.assertIsNone(hidden.accessible_provenance_support)
        self.assertEqual(hidden.d1_verdict, "withhold_partition_unavailable")
        self.assertEqual(hidden.support_classifier_verdict, "withhold_partition_unavailable")

    def test_t105_is_a_reduction_not_a_novelty_upgrade(self) -> None:
        self.assertTrue(self.result.same_support_always_same_verdict)
        self.assertTrue(self.result.raw_redundancy_is_not_sufficient)
        self.assertFalse(self.result.external_distinctness_earned)
        self.assertIn("collapses to one auditable statistic", self.result.strongest_claim)
        self.assertIn("thresholded classifier", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
