"""Tests for T249: larger T54/T126 canonical colimit witness."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t249_larger_t54_t126_colimit import run_t249_analysis


class LargerT54T126ColimitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t249_analysis()

    def test_t54_completion_is_canonical_at_nine_events(self) -> None:
        completion = self.result.completion

        self.assertEqual(completion.classification, "canonical")
        self.assertTrue(completion.theorem_applies)
        self.assertEqual(completion.condition_failures, ())
        self.assertEqual(len(completion.global_events), 9)

    def test_quotient_union_is_exact_product_order(self) -> None:
        completion = self.result.completion
        assert completion.partial_order is not None

        strict_pairs = {
            (left, right)
            for left, right in completion.partial_order.order_pairs
            if left != right
        }
        self.assertEqual(len(strict_pairs), 27)
        self.assertTrue(self.result.product_order_exact)
        self.assertTrue(completion.axis_monotonicity.am_holds)

    def test_observer_patches_have_no_phantom_gap_residue(self) -> None:
        for summary in self.result.local_gap_summaries:
            with self.subTest(observer=summary.observer):
                self.assertTrue(summary.local_is_suborder)
                self.assertEqual(summary.gap_count, 0)
                self.assertEqual(summary.local_pair_count, summary.ambient_pair_count)

    def test_t126_filter_is_reached_above_scale_floor(self) -> None:
        audit = self.result.t126_audit

        self.assertTrue(audit.causal_set_candidate)
        self.assertEqual(audit.classification, "passes_filter_only")
        self.assertTrue(audit.manifold_filter_passed)
        assert audit.diagnostics is not None
        self.assertEqual(audit.diagnostics.event_count, 9)
        self.assertEqual(audit.diagnostics.comparable_fraction, Fraction(3, 4))
        self.assertEqual(audit.diagnostics.height, 5)
        self.assertEqual(audit.diagnostics.width, 3)

    def test_claim_language_stays_filter_only(self) -> None:
        self.assertIn("passes_filter_only", self.result.strongest_claim)
        self.assertIn("not an embedding theorem", self.result.weakened)
        self.assertIn("Do not update the claim ledger", self.result.claim_ledger_update)
        self.assertIn("Myrheim-Meyer", self.result.suggested_next)


if __name__ == "__main__":
    unittest.main()
