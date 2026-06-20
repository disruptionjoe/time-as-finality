"""Tests for T81: measured schema ablation."""

from __future__ import annotations

import unittest

from models.measured_schema_ablation import run_t81_analysis, single_category_ablations


class MeasuredSchemaAblationTests(unittest.TestCase):
    def test_expected_ablation_categories_exist(self) -> None:
        categories = {category for _, category, _ in single_category_ablations()}
        self.assertEqual(
            categories,
            {
                "timing",
                "retention_signature",
                "spoof_resistance",
                "trust_boundaries",
                "perturbation",
                "dag_observability",
                "preregistration",
            },
        )

    def test_only_trust_and_preregistration_are_load_bearing(self) -> None:
        result = run_t81_analysis()
        by_category = {case.category: case for case in result.ablations}

        self.assertTrue(by_category["trust_boundaries"].load_bearing)
        self.assertEqual(
            by_category["trust_boundaries"].verdict,
            "measured_conservative_withhold",
        )
        self.assertTrue(by_category["preregistration"].load_bearing)
        self.assertEqual(
            by_category["preregistration"].verdict,
            "threshold_dependent_failure",
        )

        for category in (
            "timing",
            "retention_signature",
            "spoof_resistance",
            "perturbation",
            "dag_observability",
        ):
            self.assertFalse(by_category[category].load_bearing)
            self.assertEqual(
                by_category[category].verdict,
                "robust_measured_recovery",
            )

    def test_claim_text_records_schema_narrowing(self) -> None:
        result = run_t81_analysis()

        self.assertIn("not justify treating every T76 evidence field", result.strongest_claim)
        self.assertIn("trust-boundary plus pre-registration gate", result.q1_update)


if __name__ == "__main__":
    unittest.main()
