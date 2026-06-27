"""Tests for T251: T249 deletion stability screen."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t251_t249_deletion_stability import run_t251_analysis


class T249DeletionStabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t251_analysis()

    def test_parent_already_fails_ordering_band(self) -> None:
        self.assertEqual(self.result.parent_ordering_fraction, Fraction(3, 4))
        self.assertFalse(self.result.parent_band_passed)

    def test_all_single_event_deletions_are_audited(self) -> None:
        self.assertEqual(self.result.deletion_case_count, 9)
        self.assertEqual(
            {audit.removed_event for audit in self.result.deletion_audits},
            {"p00", "p01", "p02", "p10", "p11", "p12", "p20", "p21", "p22"},
        )

    def test_all_deletions_pass_t126_but_fail_ordering_band(self) -> None:
        self.assertEqual(self.result.deletion_t126_pass_count, 9)
        self.assertEqual(self.result.deletion_band_pass_count, 0)
        self.assertEqual(self.result.deletion_band_pass_rate, Fraction(0, 1))
        for audit in self.result.deletion_audits:
            with self.subTest(removed=audit.removed_event):
                self.assertEqual(audit.t126_classification, "passes_filter_only")
                self.assertTrue(audit.t126_filter_passed)
                self.assertFalse(audit.ordering_band_passed)
                self.assertEqual(audit.verdict, "t126_pass_but_ordering_fraction_fail")

    def test_deletion_fractions_are_stably_high(self) -> None:
        fractions = {audit.ordering_fraction for audit in self.result.deletion_audits}

        self.assertEqual(fractions, {Fraction(19, 28), Fraction(3, 4), Fraction(23, 28)})

    def test_result_is_specific_finite_demotion(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "stable_over_ordering_under_single_deletion",
        )
        self.assertIn("all nine deletions", self.result.strongest_claim)
        self.assertIn("not as spacetime-facing", self.result.s1_update)
        self.assertIn("Do not update the claim ledger", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
