"""Tests for T62: noisy measurement access-boundary discriminator."""

from __future__ import annotations

import unittest

from models.noisy_measurement_access_boundary import (
    analyze_scenario,
    canonical_noisy_scenarios,
    mutual_information_bits,
    run_t62_analysis,
)


class InformationChannelTests(unittest.TestCase):
    def test_binary_readout_information_has_expected_extremes(self) -> None:
        self.assertAlmostEqual(mutual_information_bits(0.5), 0.0)
        self.assertAlmostEqual(mutual_information_bits(1.0), 1.0)
        self.assertGreater(mutual_information_bits(0.99), 0.75)
        self.assertLess(mutual_information_bits(0.68), 0.75)


class ScenarioMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyses = {
            scenario.name: analyze_scenario(scenario)
            for scenario in canonical_noisy_scenarios()
        }

    def test_redundant_accessible_control_aligns_all_predicates(self) -> None:
        analysis = self.analyses["redundant_accessible_control"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.darwinism_redundant_total)
        self.assertTrue(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.total_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 3)
        self.assertEqual(analysis.classification, "alignment_control")

    def test_decoherence_can_occur_without_above_threshold_fragments(self) -> None:
        analysis = self.analyses["decohered_not_darwinist"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertFalse(analysis.predicates.darwinism_redundant_total)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.total_r_delta_raw, 0)
        self.assertEqual(analysis.classification, "decohered_without_redundant_records")

    def test_total_redundancy_does_not_finalize_inaccessible_observer(self) -> None:
        analysis = self.analyses["redundant_but_inaccessible"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.darwinism_redundant_total)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.redundant_but_inaccessible)
        self.assertEqual(analysis.d1_profile.as_tuple(), (0, 0, 0, 0))

    def test_raw_redundancy_can_overcount_independence_partition(self) -> None:
        analysis = self.analyses["raw_duplicate_boundary"]

        self.assertEqual(analysis.accessible_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 2)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.raw_redundancy_overcounts_independence)
        self.assertEqual(
            analysis.classification,
            "raw_redundancy_overcounts_independence",
        )


class T62ResultTests(unittest.TestCase):
    def test_result_weakens_q1_to_access_boundary_discriminator(self) -> None:
        result = run_t62_analysis()
        statuses = {
            evaluation.hypothesis_id: evaluation.status
            for evaluation in result.hypothesis_evaluations
        }

        self.assertEqual(statuses["H1"], "supported")
        self.assertEqual(statuses["H2"], "supported")
        self.assertEqual(statuses["H3"], "weakened")
        self.assertEqual(statuses["H4"], "open")
        self.assertIn("access-boundary discriminator", result.weakened_claim)
        self.assertIn("detector-level", result.recommended_next)

    def test_falsification_condition_is_operational(self) -> None:
        result = run_t62_analysis()

        self.assertIn("access boundaries", result.falsification_condition)
        self.assertIn("independence classes", result.falsification_condition)
        self.assertIn("standard R_delta", result.falsification_condition)


if __name__ == "__main__":
    unittest.main()
