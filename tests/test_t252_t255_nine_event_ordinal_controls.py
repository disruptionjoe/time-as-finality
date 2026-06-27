"""Tests for T252-T255 nine-event ordinal controls."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t252_t255_nine_event_ordinal_controls import (
    NINE_EVENT_ORDINAL_PERMUTATION,
    run_t252_analysis,
    run_t253_analysis,
    run_t254_analysis,
    run_t255_analysis,
)


class NineEventOrdinalControlTests(unittest.TestCase):
    def test_t252_constructs_t54_native_band_witness(self) -> None:
        result = run_t252_analysis()
        assert result.t126_audit.diagnostics is not None

        self.assertEqual(result.permutation, NINE_EVENT_ORDINAL_PERMUTATION)
        self.assertEqual(result.completion.classification, "canonical")
        self.assertTrue(result.completion.theorem_applies)
        self.assertEqual(result.t126_audit.classification, "passes_filter_only")
        self.assertTrue(result.t126_audit.manifold_filter_passed)
        self.assertEqual(result.t126_audit.diagnostics.event_count, 9)
        self.assertEqual(result.t126_audit.diagnostics.strict_pair_count, 20)
        self.assertEqual(result.t126_audit.diagnostics.comparable_fraction, Fraction(5, 9))
        self.assertEqual(result.t156_audit.verdict, "passes_ordering_fraction_control_only")
        self.assertEqual(result.verdict, "nine_event_t54_ordinal_band_control")

    def test_t253_deletion_stability_for_selected_witness(self) -> None:
        result = run_t253_analysis()

        self.assertTrue(result.parent_band_passed)
        self.assertEqual(result.deletion_case_count, 9)
        self.assertEqual(result.deletion_t126_pass_count, 9)
        self.assertEqual(result.deletion_band_pass_count, 9)
        self.assertEqual(result.deletion_band_pass_rate, Fraction(1, 1))
        self.assertEqual(
            {audit.ordering_fraction for audit in result.deletion_audits},
            {Fraction(3, 7), Fraction(4, 7)},
        )
        self.assertEqual(result.verdict, "nine_event_ordinal_deletion_stable_band_control")

    def test_t254_compares_grid_and_ordinal_same_scale_controls(self) -> None:
        result = run_t254_analysis()

        self.assertEqual(result.grid_ordering_fraction, Fraction(3, 4))
        self.assertFalse(result.grid_band_passed)
        self.assertEqual(result.grid_deletion_band_pass_count, 0)
        self.assertEqual(result.ordinal_ordering_fraction, Fraction(5, 9))
        self.assertTrue(result.ordinal_band_passed)
        self.assertEqual(result.ordinal_deletion_band_pass_count, 9)
        self.assertEqual(result.verdict, "same_scale_contrast_control_only")

    def test_t255_mutation_neighborhood_is_mixed(self) -> None:
        result = run_t255_analysis()

        self.assertEqual(result.mutation_count, 36)
        self.assertEqual(result.t126_pass_and_band_count, 21)
        self.assertEqual(result.t126_pass_outside_band_count, 2)
        self.assertEqual(result.t126_blocked_inside_band_count, 13)
        self.assertEqual(result.band_total_count, 34)
        self.assertEqual(result.verdict, "mutation_neighborhood_mixed_but_band_common")

    def test_claim_language_stays_control_only(self) -> None:
        for result in (
            run_t252_analysis(),
            run_t253_analysis(),
            run_t254_analysis(),
            run_t255_analysis(),
        ):
            self.assertIn("Do not update the claim ledger", result.claim_ledger_update)
            self.assertIn("not_claimed", result.__dataclass_fields__)


if __name__ == "__main__":
    unittest.main()
