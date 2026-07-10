"""Tests for T524: T126 random-sprinkle diagnostic repair."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t524_t126_random_sprinkle_diagnostic_repair import (
    DEFAULT_SEEDS,
    SUPPORTED_SIZES,
    VERDICT_REPAIRED,
    random_lightcone_sprinkle_datum,
    run_t524_analysis,
)


class T126RandomSprinkleDiagnosticRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t524_analysis()
        cls.by_size = {summary.event_count: summary for summary in cls.result.size_summaries}

    def test_calibration_control_still_passes_t126(self) -> None:
        self.assertEqual(
            self.result.calibration_control_classification,
            "passes_filter_only",
        )
        self.assertTrue(self.result.calibration_control_passed)
        self.assertEqual(
            self.result.calibration_control_ordering_fraction,
            Fraction(7, 15),
        )

    def test_seeded_random_sprinkles_have_no_coordinate_ties(self) -> None:
        for size in SUPPORTED_SIZES:
            for seed in DEFAULT_SEEDS:
                datum = random_lightcone_sprinkle_datum(size, seed)
                self.assertEqual(len(datum.events), size)

    def test_ordering_fraction_gap_decreases_toward_1p1_target(self) -> None:
        self.assertTrue(self.result.mean_ordering_gap_decreases_with_size)
        self.assertEqual(
            [self.by_size[size].mean_absolute_gap_from_half for size in SUPPORTED_SIZES],
            [Fraction(15, 112), Fraction(17, 176), Fraction(29, 480), Fraction(39, 760)],
        )

    def test_order_dimension_rejection_strengthens_with_size(self) -> None:
        self.assertTrue(self.result.order_dimension_rejection_rate_increases_with_size)
        self.assertEqual(
            {
                size: self.by_size[size].order_dimension_obstruction_count
                for size in SUPPORTED_SIZES
            },
            {8: 1, 12: 4, 16: 8, 20: 8},
        )
        self.assertTrue(self.result.larger_sprinkles_all_order_dimension_rejected)

    def test_myrheim_meyer_band_improves_while_t126_rejects(self) -> None:
        self.assertEqual(self.by_size[8].t156_band_pass_count, 2)
        self.assertEqual(self.by_size[20].t156_band_pass_count, 7)
        self.assertEqual(self.by_size[20].t126_pass_count, 0)
        self.assertEqual(
            dict(self.by_size[20].classification_counts),
            {"order_dimension_obstruction": 8},
        )

    def test_verdict_and_claim_language_are_scoped(self) -> None:
        self.assertTrue(self.result.artifact_confirmed)
        self.assertEqual(self.result.verdict, VERDICT_REPAIRED)
        self.assertIn("No S1 status movement", self.result.claim_ledger_update)
        self.assertIn("T223 remains", self.result.claim_ledger_update)
        self.assertIn("not a manifoldlikeness proof", self.result.not_claimed)


if __name__ == "__main__":
    unittest.main()
