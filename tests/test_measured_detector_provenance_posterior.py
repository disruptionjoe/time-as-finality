"""Tests for T76: measured detector-provenance posterior adapter."""

from __future__ import annotations

import unittest

from models.measured_detector_provenance_posterior import (
    SAMPLE_COUNT,
    SEED,
    ProportionEvidence,
    calibrated_signed_deployment_fixture,
    evidence_to_prior_family,
    run_t76_analysis,
    unsigned_timing_only_control_fixture,
)


class MeasuredDetectorProvenancePosteriorTests(unittest.TestCase):
    def test_evidence_schema_maps_counts_to_t74_ranges(self) -> None:
        signed = calibrated_signed_deployment_fixture()
        posterior = evidence_to_prior_family(signed)

        self.assertEqual(posterior.name, "measured_signed_time_tag_stack")
        self.assertEqual(posterior.local_sigma.low, 0.001)
        self.assertEqual(posterior.local_sigma.high, 0.005)
        self.assertGreaterEqual(posterior.verification.low, 0.99)
        self.assertLessEqual(posterior.forgery.high, 0.01)
        self.assertEqual(posterior.declared_threshold_prob, 1.0)

    def test_invalid_measured_count_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ProportionEvidence(11, 10, "bad count").posterior_range()

        with self.assertRaises(ValueError):
            ProportionEvidence(0, 0, "missing count").posterior_range()

    def test_signed_measured_fixture_lands_in_recovery_region(self) -> None:
        result = run_t76_analysis()
        signed = result.audits[0]

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        self.assertEqual(signed.evidence.name, "measured_signed_time_tag_stack")
        self.assertEqual(signed.verdict, "robust_measured_recovery")
        self.assertEqual(signed.outcome.robust_rate, 1.0)
        self.assertEqual(signed.outcome.false_independence_rate, 0.0)
        self.assertEqual(signed.outcome.false_dependence_rate, 0.0)

    def test_timing_only_control_withholds_d1(self) -> None:
        result = run_t76_analysis()
        signed = result.audits[0]
        unsigned = result.audits[1]

        self.assertEqual(unsigned.evidence.name, unsigned_timing_only_control_fixture().name)
        self.assertEqual(unsigned.verdict, "measured_conservative_withhold")
        self.assertEqual(unsigned.posterior.local_sigma, signed.posterior.local_sigma)
        self.assertEqual(unsigned.posterior.archive_sigma, signed.posterior.archive_sigma)
        self.assertEqual(unsigned.posterior.batching_window, signed.posterior.batching_window)
        self.assertEqual(unsigned.outcome.robust_rate, 0.0)
        self.assertEqual(unsigned.outcome.computable_d1_rate, 0.0)

    def test_incomplete_preregistration_control_blocks_upgrade(self) -> None:
        result = run_t76_analysis()
        incomplete = result.audits[2]

        self.assertEqual(
            incomplete.evidence.name,
            "signed_stack_incomplete_preregistration_control",
        )
        self.assertEqual(incomplete.verdict, "threshold_dependent_failure")
        self.assertEqual(incomplete.posterior.declared_threshold_prob, 0.7)
        self.assertGreater(incomplete.outcome.threshold_dependent_rate, 0.1)
        self.assertLess(incomplete.outcome.robust_rate, 0.8)

    def test_q1_update_stays_measurement_protocol_scoped(self) -> None:
        result = run_t76_analysis()

        self.assertIn("measured, pre-registered", result.q1_update)
        self.assertIn("timing resolution alone", result.q1_update)
        self.assertIn("measured-posterior adapter", result.weakened_claim)


if __name__ == "__main__":
    unittest.main()
