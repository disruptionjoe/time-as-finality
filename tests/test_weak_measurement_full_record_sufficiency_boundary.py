"""Tests for T139: full-record sufficiency boundary."""

from __future__ import annotations

import unittest

from models.weak_measurement_full_record_sufficiency_boundary import (
    canonical_scenarios,
    classify_scenario,
    fixed_full_record_split_witness,
    fixed_summary_split_witness,
    is_screened_off_by_coarse_summary,
    is_screened_off_by_full_record,
    run_t139_analysis,
)


class FullRecordBoundaryScenarioTests(unittest.TestCase):
    def setUp(self) -> None:
        scenarios = canonical_scenarios()
        self.coarse_loophole = scenarios[0]
        self.downstream = scenarios[1]
        self.escape = scenarios[2]

    def test_coarse_summary_loophole_disappears_at_full_record_level(self) -> None:
        self.assertTrue(is_screened_off_by_full_record(self.coarse_loophole))
        self.assertFalse(is_screened_off_by_coarse_summary(self.coarse_loophole))
        self.assertEqual(fixed_summary_split_witness(self.coarse_loophole), ("mid", True))
        self.assertEqual(fixed_full_record_split_witness(self.coarse_loophole), (None, False))

    def test_downstream_meter_is_null_at_both_levels(self) -> None:
        self.assertTrue(is_screened_off_by_full_record(self.downstream))
        self.assertTrue(is_screened_off_by_coarse_summary(self.downstream))
        self.assertEqual(fixed_summary_split_witness(self.downstream), (None, False))
        self.assertEqual(fixed_full_record_split_witness(self.downstream), (None, False))

    def test_escape_meter_survives_full_record_conditioning(self) -> None:
        self.assertFalse(is_screened_off_by_full_record(self.escape))
        self.assertFalse(is_screened_off_by_coarse_summary(self.escape))
        self.assertEqual(fixed_summary_split_witness(self.escape), ("mid", True))
        self.assertEqual(fixed_full_record_split_witness(self.escape), ("x0", True))


class FullRecordBoundaryClassificationTests(unittest.TestCase):
    def test_coarse_summary_refinement_is_classified_as_null_loophole(self) -> None:
        audit = classify_scenario(canonical_scenarios()[0])
        self.assertEqual(audit.classification, "null_coarse_summary_loophole")
        self.assertEqual(audit.witness_summary, "mid")
        self.assertIsNone(audit.witness_full_record)

    def test_branch_sensitive_extra_meter_is_only_escape_class(self) -> None:
        audit = classify_scenario(canonical_scenarios()[2])
        self.assertEqual(audit.classification, "candidate_full_record_escape")
        self.assertEqual(audit.witness_full_record, "x0")
        self.assertTrue(audit.fixed_full_record_split_exists)


class T139ResultTests(unittest.TestCase):
    def test_result_promotes_full_event_level_record_gate(self) -> None:
        result = run_t139_analysis()
        self.assertEqual(len(result.audits), 3)
        self.assertIn("full event-level ordinary monitored record", result.strongest_claim)
        self.assertIn("coarsened summary", result.q1c_update)
        self.assertIn("complete ordinary monitored transcript", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
