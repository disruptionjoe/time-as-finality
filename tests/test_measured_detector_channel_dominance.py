"""Tests for T85: measured detector channel dominance."""

from __future__ import annotations

import unittest

from models.measured_detector_channel_dominance import (
    SAMPLE_COUNT,
    SEED,
    hostile_single_category_cases,
    run_t85_analysis,
)


class MeasuredDetectorChannelDominanceTests(unittest.TestCase):
    def test_expected_hostile_categories_exist(self) -> None:
        categories = {category for _, category, _ in hostile_single_category_cases()}
        self.assertEqual(
            categories,
            {
                "spoof_resistance",
                "perturbation",
                "dag_observability",
            },
        )

    def test_baseline_stays_robust(self) -> None:
        result = run_t85_analysis()

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        self.assertEqual(result.baseline_verdict, "robust_measured_recovery")
        self.assertGreaterEqual(result.baseline_outcome.robust_rate, 0.8)

    def test_only_spoof_family_is_independently_decisive(self) -> None:
        result = run_t85_analysis()
        by_category = {case.category: case for case in result.cases}

        self.assertTrue(by_category["spoof_resistance"].independently_decisive)
        self.assertEqual(
            by_category["spoof_resistance"].verdict,
            "measured_conservative_withhold",
        )
        self.assertGreater(by_category["spoof_resistance"].outcome.withhold_rate, 0.4)

        for category in ("perturbation", "dag_observability"):
            self.assertFalse(by_category[category].independently_decisive)
            self.assertEqual(
                by_category[category].verdict,
                "robust_measured_recovery",
            )
            self.assertGreaterEqual(by_category[category].outcome.robust_rate, 0.8)

    def test_claim_text_records_tag_sufficiency_narrowing(self) -> None:
        result = run_t85_analysis()

        self.assertIn("authenticated-tag", result.q1_update)
        self.assertIn("perturbation response", result.weakened_claim)
        self.assertIn("DAG observability", result.weakened_claim)


if __name__ == "__main__":
    unittest.main()
