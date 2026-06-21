"""Tests for T163: exhaustive six-event T54 rank-pair family census."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t54_rank_pair_family_census import (
    T157_BASELINE_PERMUTATION,
    run_t163_analysis,
)


class T54RankPairFamilyCensusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t163_analysis()

    def test_exhaustive_family_counts_match_current_pipeline(self) -> None:
        self.assertEqual(self.result.total_cases, 720)
        self.assertEqual(self.result.t156_fail_count, 273)
        self.assertEqual(self.result.parent_interval_fail_count, 149)
        self.assertEqual(self.result.fragile_jackknife_count, 130)
        self.assertEqual(self.result.stable_survivor_count, 26)
        self.assertEqual(self.result.stable_survivor_fraction, Fraction(13, 360))

    def test_t126_family_breakdown_is_stable(self) -> None:
        counts = dict(self.result.t126_classification_counts)

        self.assertEqual(counts["passes_filter_only"], 578)
        self.assertEqual(counts["hub_nonlocality_obstruction"], 110)
        self.assertEqual(counts["interval_profile_obstruction"], 20)
        self.assertEqual(counts["order_dimension_obstruction"], 10)
        self.assertEqual(counts["rank_width_obstruction"], 2)

    def test_t157_baseline_remains_fragile_inside_larger_family(self) -> None:
        self.assertEqual(T157_BASELINE_PERMUTATION, (1, 6, 4, 5, 2, 3))
        self.assertEqual(self.result.t157_baseline_bucket, "t159_fragile_jackknife")
        self.assertFalse(self.result.t157_baseline_stable)

    def test_claim_language_records_both_positive_and_negative_update(self) -> None:
        self.assertIn("26 survive", self.result.strongest_claim)
        self.assertIn("130", self.result.strongest_claim)
        self.assertIn("T157 construction is fragile", self.result.weakened_or_falsified)
        self.assertIn("S1 remains open_formal_target", self.result.s1_update)


if __name__ == "__main__":
    unittest.main()
