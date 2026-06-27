"""Tests for T250: T249 ordering-fraction screen."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t250_t249_ordering_fraction_screen import run_t250_analysis


class T249OrderingFractionScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t250_analysis()

    def test_t249_still_passes_t54_and_t126(self) -> None:
        self.assertEqual(self.result.t249_t54_classification, "canonical")
        self.assertTrue(self.result.t249_t54_theorem_applies)
        self.assertEqual(self.result.t249_t126_classification, "passes_filter_only")
        self.assertTrue(self.result.t249_t126_filter_passed)

    def test_t249_fails_declared_flat_1p1_ordering_fraction_band(self) -> None:
        audit = self.result.t156_audit

        self.assertEqual(audit.ordering_fraction, Fraction(3, 4))
        self.assertEqual(audit.target_fraction, Fraction(1, 2))
        self.assertEqual(audit.tolerance, Fraction(1, 10))
        self.assertEqual(audit.absolute_gap, Fraction(1, 4))
        self.assertEqual(audit.target_verdict, "outside_declared_ordering_fraction_band")
        self.assertEqual(audit.verdict, "t126_pass_but_ordering_fraction_fail")

    def test_result_is_demotion_not_upgrade(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "t249_t126_pass_but_ordering_fraction_fail",
        )
        self.assertIn("fails the declared", self.result.strongest_claim)
        self.assertIn("too ordered", self.result.weakened_or_falsified)
        self.assertIn("Do not update the claim ledger", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
