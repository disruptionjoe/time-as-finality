"""Tests for T66: POVM detector calibration obstruction."""

from __future__ import annotations

import unittest

from models.povm_detector_calibration_obstruction import (
    analyze_scenario,
    canonical_scenarios,
    local_povm_readout_up_probability,
    povm_mutual_information_bits,
    run_no_signalling_audits,
    run_t66_analysis,
)


class POVMInformationTests(unittest.TestCase):
    def test_binary_povm_information_extremes(self) -> None:
        self.assertAlmostEqual(povm_mutual_information_bits(1.0, 0.0), 1.0)
        self.assertAlmostEqual(povm_mutual_information_bits(0.5, 0.5), 0.0)
        self.assertAlmostEqual(povm_mutual_information_bits(0.9, 0.9), 0.0)

    def test_canonical_response_scores_cross_expected_thresholds(self) -> None:
        self.assertGreater(povm_mutual_information_bits(0.995, 0.015), 0.9)
        self.assertGreater(povm_mutual_information_bits(0.985, 0.035), 0.75)
        self.assertLess(povm_mutual_information_bits(0.985, 0.035), 0.9)
        self.assertLess(povm_mutual_information_bits(0.62, 0.50), 0.75)


class ScenarioMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyses = {
            scenario.name: analyze_scenario(scenario)
            for scenario in canonical_scenarios()
        }

    def test_calibrated_local_lab_finalizes_at_default_threshold(self) -> None:
        analysis = self.analyses["povm_local_lab_after_readout"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.povm_redundant_total)
        self.assertTrue(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.total_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 3)
        self.assertEqual(analysis.d1_profile.as_tuple(), (3, 3, 1, 1))
        self.assertEqual(analysis.classification, "povm_record_finalized")

    def test_same_povm_response_fails_at_high_threshold(self) -> None:
        analysis = self.analyses["same_povm_high_threshold"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertFalse(analysis.predicates.povm_redundant_total)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertEqual(analysis.total_r_delta_raw, 2)
        self.assertEqual(analysis.classification, "povm_below_redundancy_threshold")

    def test_redundant_povm_records_do_not_finalize_inaccessible_observer(
        self,
    ) -> None:
        analysis = self.analyses["povm_redundant_but_inaccessible"]

        self.assertTrue(analysis.predicates.decohered_pointer)
        self.assertTrue(analysis.predicates.povm_redundant_total)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.redundant_but_inaccessible)
        self.assertEqual(analysis.d1_profile.as_tuple(), (0, 0, 0, 0))
        self.assertEqual(analysis.classification, "povm_redundant_but_inaccessible")

    def test_archive_copy_overcounts_independence(self) -> None:
        analysis = self.analyses["archive_copy_partition"]

        self.assertEqual(analysis.accessible_r_delta_raw, 3)
        self.assertEqual(analysis.accessible_r_delta_independent, 2)
        self.assertFalse(analysis.predicates.observer_finalized)
        self.assertTrue(analysis.predicates.raw_redundancy_overcounts_independence)
        self.assertEqual(analysis.classification, "povm_independence_obstruction")

    def test_same_povm_independent_archive_flips_finality(self) -> None:
        copy_analysis = self.analyses["archive_copy_partition"]
        independent_analysis = self.analyses["archive_independent_partition"]

        self.assertFalse(copy_analysis.predicates.observer_finalized)
        self.assertTrue(independent_analysis.predicates.observer_finalized)
        self.assertEqual(copy_analysis.accessible_r_delta_raw, 3)
        self.assertEqual(independent_analysis.accessible_r_delta_raw, 3)
        self.assertEqual(independent_analysis.accessible_r_delta_independent, 3)


class NoSignallingTests(unittest.TestCase):
    def test_local_povm_readout_marginal_is_remote_setting_invariant(self) -> None:
        fragment = canonical_scenarios()[0].fragments[0]
        z_remote = local_povm_readout_up_probability(
            local_angle=0.0,
            remote_angle=0.0,
            fragment=fragment,
        )
        x_remote = local_povm_readout_up_probability(
            local_angle=0.0,
            remote_angle=1.5707963267948966,
            fragment=fragment,
        )

        self.assertAlmostEqual(z_remote, 0.505)
        self.assertAlmostEqual(x_remote, 0.505)

    def test_all_no_signalling_audits_pass(self) -> None:
        audits = run_no_signalling_audits()

        self.assertEqual(len(audits), 2)
        for audit in audits:
            self.assertTrue(audit.passed)
            self.assertEqual(audit.max_delta, 0.0)


class T66ResultTests(unittest.TestCase):
    def test_result_records_threshold_and_independence_obstructions(self) -> None:
        result = run_t66_analysis()
        statuses = {
            evaluation.hypothesis_id: evaluation.status
            for evaluation in result.hypothesis_evaluations
        }

        self.assertEqual(statuses["H1"], "supported")
        self.assertEqual(statuses["H2"], "weakened")
        self.assertEqual(statuses["H3"], "weakened")
        self.assertEqual(statuses["H4"], "supported_guardrail")
        self.assertEqual(statuses["H5"], "open")
        self.assertTrue(result.threshold_obstruction.same_povm_response)
        self.assertTrue(result.threshold_obstruction.verdict_flips)
        self.assertTrue(result.independence_obstruction.same_povm_response)
        self.assertTrue(result.independence_obstruction.same_access_window)
        self.assertTrue(result.independence_obstruction.verdict_flips)

    def test_falsification_condition_is_operational(self) -> None:
        result = run_t66_analysis()

        self.assertIn("information threshold", result.falsification_condition)
        self.assertIn("provenance", result.falsification_condition)
        self.assertIn("standard R_delta", result.falsification_condition)


if __name__ == "__main__":
    unittest.main()
