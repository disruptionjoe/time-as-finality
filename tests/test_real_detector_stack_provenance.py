"""Tests for T75: real detector stack provenance mapping."""

from __future__ import annotations

import unittest

from models.real_detector_stack_provenance import (
    SAMPLE_COUNT,
    SEED,
    calibration_sources,
    run_t75_analysis,
    selected_stack_posterior,
    unsigned_control_posterior,
)


class RealDetectorStackProvenanceTests(unittest.TestCase):
    def test_selected_stack_is_named_and_source_anchored(self) -> None:
        result = run_t75_analysis()
        source_parameters = {note.parameter for note in calibration_sources()}

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        self.assertEqual(result.selected_stack, "hydraharp_wr_signed_archive")
        self.assertIn("time tagger timing precision", source_parameters)
        self.assertIn("distributed timing", source_parameters)
        self.assertIn("signed archive", source_parameters)

    def test_signed_stack_lands_in_robust_recovery_region(self) -> None:
        result = run_t75_analysis()
        signed = result.mappings[0]

        self.assertEqual(signed.name, selected_stack_posterior().name)
        self.assertEqual(signed.verdict, "robust_recovery")
        self.assertGreaterEqual(signed.outcome.robust_rate, 0.8)
        self.assertGreaterEqual(signed.outcome.computable_d1_rate, 0.8)
        self.assertEqual(signed.outcome.false_independence_rate, 0.0)
        self.assertEqual(signed.outcome.false_dependence_rate, 0.0)

    def test_unsigned_control_does_not_recover_from_timing_alone(self) -> None:
        result = run_t75_analysis()
        unsigned = result.mappings[1]

        self.assertEqual(unsigned.name, unsigned_control_posterior().name)
        self.assertNotEqual(unsigned.verdict, "robust_recovery")
        self.assertLess(unsigned.outcome.robust_rate, 0.5)
        self.assertLess(unsigned.outcome.computable_d1_rate, 0.5)

    def test_q1_update_stays_instrumentation_scoped(self) -> None:
        result = run_t75_analysis()

        self.assertIn("instrumentation/provenance", result.q1_update)
        self.assertIn("not by detector timing alone", result.weakened_claim)
        self.assertIn("plausible engineering posteriors", result.blocker)


if __name__ == "__main__":
    unittest.main()
