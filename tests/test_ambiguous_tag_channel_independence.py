"""Tests for T86: ambiguous-tag channel independence."""

from __future__ import annotations

import unittest

from models.ambiguous_tag_channel_independence import (
    SAMPLE_COUNT,
    SEED,
    ambiguous_tag_channel_cases,
    run_t86_analysis,
)


class AmbiguousTagChannelIndependenceTests(unittest.TestCase):
    def test_expected_fixture_cases_exist(self) -> None:
        cases = {name: (channel, role) for name, channel, role, _ in ambiguous_tag_channel_cases()}

        self.assertEqual(
            cases,
            {
                "all_channels_ambiguous_negative_control": (
                    "none",
                    "negative_control",
                ),
                "clean_perturbation_only_rescue": (
                    "perturbation_response",
                    "positive_test",
                ),
                "backaction_contaminated_perturbation_control": (
                    "perturbation_response",
                    "contamination_control",
                ),
                "clean_dag_only_rescue": (
                    "signed_ancestry_dag",
                    "positive_test",
                ),
                "truncated_dag_control": (
                    "signed_ancestry_dag",
                    "contamination_control",
                ),
            },
        )

    def test_seed_and_sample_count_are_stable(self) -> None:
        result = run_t86_analysis()

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        for case in result.cases:
            self.assertEqual(case.outcome.sample_count, SAMPLE_COUNT)

    def test_all_ambiguous_negative_control_withholds_d1(self) -> None:
        result = run_t86_analysis()
        by_name = {case.name: case for case in result.cases}
        negative = by_name["all_channels_ambiguous_negative_control"]

        self.assertEqual(negative.verdict, "measured_conservative_withhold")
        self.assertEqual(negative.outcome.robust_rate, 0.0)
        self.assertEqual(negative.outcome.computable_d1_rate, 0.0)

    def test_clean_perturbation_and_dag_each_rescue_ambiguous_tags(self) -> None:
        result = run_t86_analysis()
        by_name = {case.name: case for case in result.cases}

        for name in ("clean_perturbation_only_rescue", "clean_dag_only_rescue"):
            case = by_name[name]
            self.assertTrue(case.rescues_with_ambiguous_tags)
            self.assertEqual(case.verdict, "robust_measured_recovery")
            self.assertEqual(case.outcome.robust_rate, 1.0)
            self.assertEqual(case.outcome.computable_d1_rate, 1.0)

    def test_contaminated_channel_controls_do_not_rescue_d1(self) -> None:
        result = run_t86_analysis()
        by_name = {case.name: case for case in result.cases}

        for name in (
            "backaction_contaminated_perturbation_control",
            "truncated_dag_control",
        ):
            case = by_name[name]
            self.assertFalse(case.rescues_with_ambiguous_tags)
            self.assertEqual(case.verdict, "measured_conservative_withhold")
            self.assertEqual(case.outcome.robust_rate, 0.0)
            self.assertEqual(case.outcome.computable_d1_rate, 0.0)

    def test_claim_text_preserves_no_upgrade_boundary(self) -> None:
        result = run_t86_analysis()

        self.assertIn("does not upgrade Q1", result.weakened_claim)
        self.assertIn("real deployment", result.q1_update)
        self.assertIn("constructed fixture counts", result.blocker)


if __name__ == "__main__":
    unittest.main()
