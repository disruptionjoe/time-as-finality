"""Tests for T77: measured detector policy sensitivity."""

from __future__ import annotations

import unittest

from models.measured_detector_policy_sensitivity import (
    SAMPLE_COUNT,
    SEED,
    policy_scenarios,
    run_t77_analysis,
)


class MeasuredDetectorPolicySensitivityTests(unittest.TestCase):
    def test_policy_scenarios_are_ordered_by_strictness(self) -> None:
        strict, baseline, permissive = policy_scenarios()

        self.assertGreater(strict.policy.confidence_floor.low, baseline.policy.confidence_floor.high)
        self.assertLess(strict.policy.max_false_risk.high, baseline.policy.max_false_risk.low)
        self.assertLess(permissive.policy.confidence_floor.high, baseline.policy.confidence_floor.low)
        self.assertGreater(permissive.policy.max_false_risk.low, baseline.policy.max_false_risk.high)

    def test_signed_fixture_stays_robust_across_policy_choices(self) -> None:
        result = run_t77_analysis()
        audits = {
            (audit.policy_name, audit.deployment_name): audit
            for audit in result.audits
        }

        strict = audits[("strict", "measured_signed_time_tag_stack")]
        baseline = audits[("baseline", "measured_signed_time_tag_stack")]
        permissive = audits[("permissive", "measured_signed_time_tag_stack")]

        self.assertEqual(result.seed, SEED)
        self.assertEqual(result.sample_count, SAMPLE_COUNT)
        self.assertEqual(strict.outcome.robust_rate, 1.0)
        self.assertEqual(baseline.outcome.robust_rate, 1.0)
        self.assertEqual(permissive.outcome.robust_rate, 1.0)

    def test_permissive_policy_leaks_unsigned_false_positives(self) -> None:
        result = run_t77_analysis()
        audit = next(
            audit
            for audit in result.audits
            if audit.policy_name == "permissive"
            and audit.deployment_name == "timing_only_unsigned_control"
        )

        self.assertGreater(audit.outcome.robust_rate, 0.0)
        self.assertEqual(audit.verdict, "withhold_under_policy")

    def test_incomplete_preregistration_remains_policy_limited(self) -> None:
        result = run_t77_analysis()
        audit = next(
            audit
            for audit in result.audits
            if audit.policy_name == "permissive"
            and audit.deployment_name
            == "signed_stack_incomplete_preregistration_control"
        )

        self.assertGreater(audit.outcome.threshold_dependent_rate, 0.0)
        self.assertNotEqual(audit.verdict, "robust_under_policy")

    def test_q1_update_mentions_policy_corridor(self) -> None:
        result = run_t77_analysis()

        self.assertIn("policy corridor", result.q1_update)
        self.assertIn("signed-versus-unsigned separation", result.q1_update)
        self.assertIn("control separation", result.weakened_claim)


if __name__ == "__main__":
    unittest.main()
