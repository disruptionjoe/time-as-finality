"""Unit tests for T15: generated integrated finality stress lab."""

from __future__ import annotations

import unittest

from models.t15_generated_integrated_finality import (
    GeneratedCaseConfig,
    build_generated_case,
    evaluate_case,
    generated_configs,
    run_t15_analysis,
)


class GeneratedIntegratedFinalityTests(unittest.TestCase):
    def test_generator_is_deterministic_and_nonempty(self) -> None:
        first = generated_configs()
        second = generated_configs()
        self.assertEqual(first, second)
        self.assertEqual(len(first), 448)

    def test_t14_style_success_is_found_in_generated_family(self) -> None:
        config = GeneratedCaseConfig(
            "t14-style",
            core_size=3,
            weights=(1, -1, 1),
            masked_phase_indices=frozenset({1}),
            include_forged=True,
            include_valid_dissent=True,
        )
        evaluation = evaluate_case(config)
        self.assertTrue(evaluation.coupling_diverges)
        self.assertTrue(evaluation.expression_preserves_identity)
        self.assertTrue(evaluation.forged_rejected)
        self.assertTrue(evaluation.valid_dissent_visible)
        self.assertTrue(evaluation.profile_readout_separation)

    def test_same_profile_different_readout_can_be_generated_minimally(self) -> None:
        config = GeneratedCaseConfig("minimal", 2, (1, -1))
        evaluation = evaluate_case(config)
        self.assertEqual(evaluation.core_profile, (2, 2, 1, 2))
        self.assertEqual(evaluation.core_readout, 0.0)
        self.assertEqual(evaluation.constructive_readout, 4.0)
        self.assertTrue(evaluation.profile_readout_separation)

    def test_proof_filter_removes_forgery_not_valid_dissent(self) -> None:
        graph, observers = build_generated_case(
            GeneratedCaseConfig(
                "adversarial",
                3,
                (1, -1, 1),
                include_forged=True,
                include_valid_dissent=True,
            )
        )
        raw_ids = {record.record_id for record in graph.visible_records(observers["raw_social"])}
        verified_ids = {
            record.record_id for record in graph.visible_records(observers["verified_social"])
        }
        self.assertIn("r-forged", raw_ids)
        self.assertNotIn("r-forged", verified_ids)
        self.assertIn("r-valid-dissent", verified_ids)

    def test_analysis_reports_successes_and_breakpoints(self) -> None:
        result = run_t15_analysis()
        self.assertGreater(result["fractions"]["robust_success"], 0.0)
        self.assertGreater(result["fractions"]["profile_readout_separation"], 0.5)
        self.assertEqual(result["fractions"]["forged_rejection_when_present"], 1.0)
        self.assertEqual(result["fractions"]["valid_dissent_visible_when_present"], 1.0)
        self.assertIsNotNone(
            result["minimal_breakpoints"]["valid_dissent_survives_proof_filter"]
        )
        self.assertTrue(result["verdict"]["t14_is_not_single_case_only"])


if __name__ == "__main__":
    unittest.main()
