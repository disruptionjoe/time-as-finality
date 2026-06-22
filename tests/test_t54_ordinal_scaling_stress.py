"""Tests for T167: T54 ordinal scaling stress test."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t54_ordinal_scaling_stress import run_t167_analysis


class T54OrdinalScalingStressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t167_analysis()
        cls.by_size = {
            audit.event_count: audit for audit in cls.result.size_audits
        }

    def test_n5_is_scale_blocked_and_n6_reproduces_t165(self) -> None:
        n5 = self.by_size[5]
        n6 = self.by_size[6]

        self.assertEqual(n5.total_rank_permutation_cases, 120)
        self.assertEqual(n5.t126_classification_counts, (("insufficient_scale", 120),))
        self.assertEqual(n5.stable_labeled_survivor_count, 0)

        self.assertEqual(n6.total_rank_permutation_cases, 720)
        self.assertEqual(n6.t126_pass_count, 578)
        self.assertEqual(n6.t156_pass_count, 305)
        self.assertEqual(n6.parent_interval_pass_count, 156)
        self.assertEqual(n6.stable_labeled_survivor_count, 26)
        self.assertEqual(n6.stable_labeled_survivor_fraction, Fraction(13, 360))
        self.assertEqual(n6.oriented_survivor_class_count, 15)
        self.assertEqual(n6.order_dual_survivor_class_count, 9)

    def test_n7_stable_tail_persists_but_remains_rare(self) -> None:
        n7 = self.by_size[7]

        self.assertEqual(n7.total_rank_permutation_cases, 5040)
        self.assertEqual(n7.t126_pass_count, 4456)
        self.assertEqual(n7.t156_pass_count, 2051)
        self.assertEqual(n7.parent_interval_pass_count, 561)
        self.assertEqual(n7.stable_labeled_survivor_count, 174)
        self.assertEqual(n7.stable_labeled_survivor_fraction, Fraction(29, 840))
        self.assertEqual(n7.oriented_survivor_class_count, 86)
        self.assertEqual(n7.order_dual_survivor_class_count, 45)
        self.assertEqual(n7.largest_oriented_class_size, 4)
        self.assertEqual(n7.largest_oriented_class_probability, Fraction(1, 1260))
        self.assertLess(n7.stable_labeled_survivor_fraction, Fraction(1, 25))

    def test_stable_fraction_does_not_become_typical_at_n7(self) -> None:
        n6 = self.by_size[6]
        n7 = self.by_size[7]

        self.assertLess(
            n7.stable_labeled_survivor_fraction,
            n6.stable_labeled_survivor_fraction,
        )
        self.assertEqual(self.result.one_step_fraction_delta, Fraction(-1, 630))
        self.assertEqual(dict(n7.deletion_pass_distribution), {4: 4, 5: 79, 6: 304, 7: 174})

    def test_claim_language_rejects_continuum_upgrade(self) -> None:
        self.assertIn("rare-tail boundary survives", self.result.strongest_claim)
        self.assertIn("does not become typical", self.result.weakened_or_falsified)
        self.assertIn("S1 remains open_formal_target", self.result.s1_update)
        self.assertIn("not as spacetime evidence", self.result.claim_ledger_update)
        self.assertIn("does not establish a continuum limit", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
