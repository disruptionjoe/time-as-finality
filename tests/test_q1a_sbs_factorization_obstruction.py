"""Tests for T162: Q1A SBS closure-key obstruction."""

from __future__ import annotations

import unittest

from models.q1a_sbs_factorization_obstruction import run_t162_analysis


class Q1ASBSFactorizationObstructionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t162_analysis()

    def test_current_d1_verdicts_factor_through_sbs_closure_key(self) -> None:
        self.assertTrue(self.result.d1_factors_through_sbs_closure_key)
        self.assertFalse(self.result.same_full_sbs_data_split_found)
        self.assertTrue(self.result.q1a_current_family_has_no_same_sbs_split)

    def test_raw_redundancy_still_cannot_replace_audited_support(self) -> None:
        self.assertTrue(self.result.raw_redundancy_is_not_sufficient)
        raw_three_fibers = [
            fiber for fiber in self.result.fibers if 3 in fiber.raw_redundancies
        ]
        self.assertTrue(
            any("finalized" in fiber.d1_verdicts for fiber in raw_three_fibers)
        )
        self.assertTrue(
            any("not_finalized" in fiber.d1_verdicts for fiber in raw_three_fibers)
        )

    def test_sbs_objectivity_failures_do_not_upgrade_q1a(self) -> None:
        self.assertTrue(self.result.objectivity_failures_withhold)
        self.assertEqual(
            {
                verdict.d1_verdict
                for verdict in self.result.objectivity_failure_controls
            },
            {"withhold_sbs_objectivity_failed"},
        )

    def test_hidden_partition_still_withholds(self) -> None:
        hidden = self.result.hidden_partition_case
        self.assertTrue(hidden.partition_visible is False)
        self.assertEqual(hidden.sbs_objectivity_verdict, "sbs_objective")
        self.assertEqual(hidden.d1_verdict, "withhold_partition_unavailable")

    def test_factorization_is_nontrivial_but_not_a_physics_upgrade(self) -> None:
        self.assertTrue(self.result.nontrivial_same_key_variants_exist)
        self.assertIn("no same-SBS-data verdict split", self.result.strongest_claim)
        self.assertIn("weakens Q1A", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
