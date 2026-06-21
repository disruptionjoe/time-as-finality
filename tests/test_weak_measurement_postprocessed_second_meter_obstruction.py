"""Tests for T137: postprocessed second-meter obstruction."""

from __future__ import annotations

import unittest

from models.weak_measurement_postprocessed_second_meter_obstruction import (
    canonical_scenarios,
    classify_scenario,
    fixed_record_split_witness,
    is_postprocessed_from_standard_record,
    run_t137_analysis,
)


class PostprocessedSecondMeterTests(unittest.TestCase):
    def setUp(self) -> None:
        scenarios = canonical_scenarios()
        self.exact_copy = scenarios[0]
        self.noisy_copy = scenarios[1]
        self.independent_meter = scenarios[2]

    def test_exact_copy_is_postprocessed_and_has_no_fixed_record_split(self) -> None:
        self.assertTrue(is_postprocessed_from_standard_record(self.exact_copy))
        self.assertEqual(fixed_record_split_witness(self.exact_copy), (None, 0.0))

    def test_noisy_downstream_meter_is_still_postprocessed(self) -> None:
        self.assertTrue(is_postprocessed_from_standard_record(self.noisy_copy))
        self.assertEqual(fixed_record_split_witness(self.noisy_copy), (None, 0.0))

    def test_branch_sensitive_meter_escapes_postprocessing_gate(self) -> None:
        self.assertFalse(is_postprocessed_from_standard_record(self.independent_meter))
        self.assertEqual(fixed_record_split_witness(self.independent_meter), ("low", 0.8))


class ScenarioClassificationTests(unittest.TestCase):
    def test_postprocessed_scenarios_are_null(self) -> None:
        scenarios = canonical_scenarios()[:2]
        classifications = [classify_scenario(scenario).classification for scenario in scenarios]
        self.assertEqual(classifications, ["null_downstream_transform", "null_downstream_transform"])

    def test_independent_meter_is_only_candidate_class(self) -> None:
        audit = classify_scenario(canonical_scenarios()[2])

        self.assertEqual(audit.classification, "candidate_branch_sensitive_second_meter")
        self.assertTrue(audit.fixed_record_split_exists)
        self.assertEqual(audit.witness_record, "low")


class T137ResultTests(unittest.TestCase):
    def test_result_states_downstream_second_meter_obstruction(self) -> None:
        result = run_t137_analysis()

        self.assertEqual(len(result.audits), 3)
        self.assertIn("downstream classical transform", result.strongest_claim)
        self.assertIn("conditionally determined by the ordinary monitored record", result.q1c_update)
        self.assertIn("hidden branch-relevant structure", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
