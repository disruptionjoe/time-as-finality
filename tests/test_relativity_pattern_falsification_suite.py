"""Tests for T383 relativity-pattern falsification suite."""

from __future__ import annotations

import unittest

from models.relativity_pattern_falsification_suite import (
    evaluate_perturbations,
    run_t383_analysis,
)


class RelativityPatternFalsificationSuiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t383_analysis()
        self.verdicts = {
            verdict.perturbation_id: verdict for verdict in evaluate_perturbations()
        }

    def test_baseline_two_null_adapter_survives(self) -> None:
        self.assertTrue(self.result.baseline_survives)
        self.assertEqual(self.result.survivor_ids, ("baseline_two_null",))
        verdict = self.verdicts["baseline_two_null"]
        self.assertEqual(verdict.classification, "survivor")
        self.assertTrue(verdict.interval_preserved)
        self.assertTrue(verdict.signal_speed_invariant)
        self.assertTrue(verdict.two_channel_complete)
        self.assertTrue(verdict.minimal_basis)
        self.assertTrue(verdict.exact_access)

    def test_anisotropic_and_nonreciprocal_scaling_falsify_signal_calibration(self) -> None:
        self.assertTrue(self.result.anisotropic_speed_falsifies)
        self.assertTrue(self.result.nonreciprocal_scaling_falsifies)
        self.assertEqual(
            self.verdicts["anisotropic_signal_speed"].status,
            "falsifies_signal_speed",
        )
        self.assertEqual(
            self.verdicts["nonreciprocal_scaling"].status,
            "falsifies_signal_speed",
        )

    def test_delayed_and_noisy_channels_fail_exact_pattern(self) -> None:
        self.assertTrue(self.result.delayed_channel_falsifies)
        self.assertTrue(self.result.noisy_channel_falsifies_exact_invariance)
        self.assertEqual(
            self.verdicts["delayed_left_channel"].status,
            "falsifies_signal_speed",
        )
        self.assertEqual(
            self.verdicts["deterministic_noise"].classification,
            "falsifier",
        )
        self.assertFalse(self.verdicts["deterministic_noise"].exact_access)

    def test_missing_channel_and_extra_channel_fail_structural_requirements(self) -> None:
        self.assertTrue(self.result.missing_channel_falsifies)
        self.assertTrue(self.result.extra_primitive_channel_falsifies_minimality)
        self.assertEqual(
            self.verdicts["missing_right_channel"].status,
            "falsifies_channel_completeness",
        )
        self.assertEqual(
            self.verdicts["extra_primitive_channel"].status,
            "falsifies_minimality",
        )

    def test_coarse_graining_is_partial_not_exact_success(self) -> None:
        self.assertTrue(self.result.coarse_graining_is_partial)
        self.assertEqual(self.result.partial_ids, ("coarse_grained_access",))
        verdict = self.verdicts["coarse_grained_access"]
        self.assertEqual(verdict.classification, "partial")
        self.assertTrue(verdict.interval_preserved)
        self.assertFalse(verdict.exact_access)

    def test_falsifier_list_contains_expected_perturbations(self) -> None:
        self.assertEqual(
            set(self.result.falsifier_ids),
            {
                "anisotropic_signal_speed",
                "nonreciprocal_scaling",
                "delayed_left_channel",
                "deterministic_noise",
                "missing_right_channel",
                "extra_primitive_channel",
            },
        )

    def test_hostile_comparators_keep_falsification_scope_honest(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }
        self.assertFalse(by_id["robustness"].absorbs)
        self.assertTrue(by_id["finite_perturbation_catalog"].absorbs)
        self.assertFalse(by_id["exact_invariance_requirement"].absorbs)

    def test_overall_verdict_records_premise_sensitivity(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "two_null_pattern_survives_baseline_and_fails_targeted_perturbations",
        )
        self.assertIn("premise-sensitive", self.result.claim_ledger_update)
        self.assertIn("Targeted perturbations", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
