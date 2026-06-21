"""Tests for T165: T54 survivor sprinkling stress test."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t54_survivor_sprinkling_stress import run_t165_analysis


class T54SurvivorSprinklingStressTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t165_analysis()

    def test_exact_ordinal_ensemble_counts_match_t163_t164(self) -> None:
        self.assertEqual(self.result.total_rank_permutation_cases, 720)
        self.assertEqual(self.result.t126_pass_count, 578)
        self.assertEqual(self.result.t156_pass_count, 305)
        self.assertEqual(self.result.parent_interval_pass_count, 156)
        self.assertEqual(self.result.stable_labeled_survivor_count, 26)
        self.assertEqual(self.result.stable_labeled_survivor_fraction, Fraction(13, 360))
        self.assertEqual(self.result.oriented_survivor_class_count, 15)
        self.assertEqual(self.result.order_dual_survivor_class_count, 9)

    def test_survivor_classes_are_rare_under_uniform_rank_sprinkling(self) -> None:
        self.assertEqual(self.result.largest_oriented_class_size, 2)
        self.assertEqual(self.result.largest_oriented_class_probability, Fraction(1, 360))
        self.assertTrue(self.result.all_oriented_classes_below_one_percent)

    def test_conditioning_stage_counts_are_stable(self) -> None:
        stages = {stage.stage: stage for stage in self.result.conditioning_stages}
        self.assertEqual(
            stages["T126 finite causal-set filter"].unconditional_fraction,
            Fraction(289, 360),
        )
        self.assertEqual(
            stages["T159 all single deletions stable"].conditional_fraction,
            Fraction(1, 6),
        )
        self.assertEqual(
            dict(self.result.parent_deletion_pass_distribution),
            {3: 8, 4: 34, 5: 88, 6: 26},
        )

    def test_claim_language_rejects_spacetime_upgrade(self) -> None:
        self.assertIn("13/360", self.result.strongest_claim)
        self.assertIn("rare tail", self.result.strongest_claim)
        self.assertIn("not as spacetime evidence", self.result.claim_ledger_update)
        self.assertIn("No T54 generative law", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
