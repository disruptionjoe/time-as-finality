"""Tests for T64: Stern-Gerlach detector access-window discriminator."""

from __future__ import annotations

import unittest

from models.stern_gerlach_access_window import (
    analyze_scenario,
    canonical_scenarios,
    local_readout_up_probability,
    mutual_information_bits,
    run_no_signalling_audits,
    run_t64_analysis,
    run_threshold_sweep,
)


class DetectorChannelTests(unittest.TestCase):
    def test_binary_readout_information_extremes_and_thresholds(self) -> None:
        self.assertAlmostEqual(mutual_information_bits(0.5), 0.0)
        self.assertAlmostEqual(mutual_information_bits(1.0), 1.0)
        self.assertGreater(mutual_information_bits(0.985), 0.75)
        self.assertGreater(mutual_information_bits(0.97), 0.75)
        self.assertLess(mutual_information_bits(0.62), 0.75)


class SternGerlachScenarioTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyses = {
            scenario.name: analyze_scenario(scenario)
            for scenario in canonical_scenarios()
        }

    def test_local_lab_after_readout_finalizes_detector_record(self) -> None:
        analysis = self.analyses["local_lab_after_readout"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.darwinism_redundant_total)
        self.assertTrue(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.total_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 3)
        self.assertEqual(analysis.d1_profile.as_tuple(), (3, 3, 1, 2))
        self.assertEqual(analysis.classification, "detector_record_finalized")

    def test_redundant_detector_records_do_not_finalize_inaccessible_observer(
        self,
    ) -> None:
        analysis = self.analyses["redundant_but_before_access"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.darwinism_redundant_total)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.redundant_but_inaccessible)
        self.assertEqual(analysis.d1_profile.as_tuple(), (0, 0, 0, 0))
        self.assertEqual(analysis.classification, "redundant_but_inaccessible")

    def test_single_channel_early_window_is_underfinalized(self) -> None:
        analysis = self.analyses["single_channel_early_window"]

        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.accessible_r_delta_independent, 1)
        self.assertEqual(analysis.classification, "single_channel_underfinalized")

    def test_archive_copy_overcounts_raw_redundancy(self) -> None:
        analysis = self.analyses["duplicate_archive_boundary"]

        self.assertEqual(analysis.accessible_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 2)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.raw_redundancy_overcounts_independence)
        self.assertEqual(
            analysis.classification,
            "raw_redundancy_overcounts_independence",
        )

    def test_high_information_threshold_weakens_q1_verdict(self) -> None:
        analysis = self.analyses["high_threshold_fragility"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.accessible_r_delta_independent, 1)
        self.assertEqual(analysis.classification, "single_channel_underfinalized")


class ThresholdSweepTests(unittest.TestCase):
    def test_threshold_sweep_detects_finality_flips(self) -> None:
        points = run_threshold_sweep()
        verdicts_by_key = {
            (point.information_threshold_bits, point.observer_time): (
                point.observer_finalized
            )
            for point in points
        }

        self.assertTrue(verdicts_by_key[(0.75, 2.5)])
        self.assertFalse(verdicts_by_key[(0.9, 2.5)])
        self.assertTrue(verdicts_by_key[(0.75, 4.5)])
        self.assertFalse(verdicts_by_key[(0.9, 4.5)])


class NoSignallingTests(unittest.TestCase):
    def test_singlet_local_readout_marginal_is_remote_setting_invariant(self) -> None:
        z_remote = local_readout_up_probability(
            local_angle=0.0,
            remote_angle=0.0,
            detector_reliability=0.985,
        )
        x_remote = local_readout_up_probability(
            local_angle=0.0,
            remote_angle=1.5707963267948966,
            detector_reliability=0.985,
        )

        self.assertAlmostEqual(z_remote, 0.5)
        self.assertAlmostEqual(x_remote, 0.5)

    def test_all_no_signalling_audits_pass(self) -> None:
        audits = run_no_signalling_audits()

        self.assertEqual(len(audits), 2)
        for audit in audits:
            self.assertTrue(audit.passed)
            self.assertEqual(audit.max_delta, 0.0)


class T64ResultTests(unittest.TestCase):
    def test_result_weakens_q1_and_keeps_no_signalling_guardrail(self) -> None:
        result = run_t64_analysis()
        statuses = {
            evaluation.hypothesis_id: evaluation.status
            for evaluation in result.hypothesis_evaluations
        }

        self.assertEqual(statuses["H1"], "supported")
        self.assertEqual(statuses["H2"], "supported")
        self.assertEqual(statuses["H3"], "weakened")
        self.assertEqual(statuses["H4"], "supported")
        self.assertEqual(statuses["H5"], "open")
        self.assertGreater(result.threshold_flip_count, 0)
        self.assertIn("bookkeeping", result.weakened_claim)
        self.assertIn("R_delta", result.falsification_condition)
        self.assertIn("POVM", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
