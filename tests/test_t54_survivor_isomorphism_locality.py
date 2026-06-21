"""Tests for T164: T54 survivor isomorphism/locality audit."""

from __future__ import annotations

import unittest

from models.t54_survivor_isomorphism_locality import run_t164_analysis


class T54SurvivorIsomorphismLocalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t164_analysis()

    def test_stable_survivors_quotient_to_expected_class_counts(self) -> None:
        self.assertEqual(self.result.stable_labeled_survivor_count, 26)
        self.assertEqual(self.result.oriented_isomorphism_class_count, 15)
        self.assertEqual(self.result.order_dual_quotient_class_count, 9)
        self.assertEqual(self.result.largest_oriented_class_size, 2)
        self.assertEqual(self.result.singleton_oriented_class_count, 4)

    def test_survivor_classes_are_thin_height_three_controls(self) -> None:
        self.assertTrue(self.result.all_classes_height_three)
        self.assertTrue(self.result.all_classes_parent_intervals_thin)
        self.assertTrue(self.result.all_classes_low_cover_hub)
        self.assertTrue(
            all(
                audit.locality_label == "thin_height3_control"
                for audit in self.result.class_audits
            )
        )

    def test_structural_distributions_are_stable(self) -> None:
        self.assertEqual(
            dict(self.result.strict_pair_count_by_oriented_class),
            {6: 1, 7: 7, 8: 7},
        )
        self.assertEqual(len(self.result.cover_degree_profiles_by_oriented_class), 6)

    def test_claim_language_rejects_spacetime_upgrade(self) -> None:
        self.assertIn("15 oriented", self.result.strongest_claim)
        self.assertIn("not as spacetime evidence", self.result.claim_ledger_update)
        self.assertIn("No random-sprinkling comparison", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
