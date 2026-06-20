"""Tests for T101: Q1 branch adjudication."""

from __future__ import annotations

import unittest

from models.q1_branch_adjudication import run_t101_analysis


class Q1BranchAdjudicationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t101_analysis()
        self.branches = {branch.branch_id: branch for branch in self.result.branches}

    def test_q1_umbrella_must_split_before_paper_language(self) -> None:
        umbrella = self.branches["q1_umbrella"]

        self.assertTrue(self.result.q1_should_split_before_paper_language)
        self.assertEqual(
            umbrella.current_status,
            "too_broad_for_single_partially_supported_claim",
        )
        self.assertIn("Split Q1 into subclaims", umbrella.next_gate)

    def test_no_branch_earns_new_measurement_dynamics(self) -> None:
        self.assertTrue(self.result.no_branch_earns_new_measurement_dynamics)
        self.assertIn("None currently earns new measurement dynamics", self.result.strongest_claim)

    def test_detector_branch_is_protocol_and_externally_blocked(self) -> None:
        detector = self.branches["detector_provenance_protocol"]

        self.assertTrue(self.result.detector_branch_externally_blocked)
        self.assertEqual(
            detector.current_status,
            "externally_blocked_protocol_admissibility",
        )
        self.assertIn("four non-conflicting authority domains", detector.kill_condition)
        self.assertIn("empirical detector support", detector.not_earned.lower())

    def test_weak_measurement_is_reinstatement_only(self) -> None:
        weak = self.branches["weak_measurement_discriminator"]

        self.assertTrue(self.result.weak_measurement_reinstatement_only)
        self.assertEqual(weak.current_status, "dormant_reinstatement_only")
        self.assertIn("independent-axis declaration", weak.next_gate)

    def test_contextuality_branch_is_guardrail_only(self) -> None:
        contextuality = self.branches["contextuality_guardrail"]

        self.assertTrue(self.result.contextuality_branch_is_guardrail_only)
        self.assertEqual(contextuality.current_status, "context_only_not_prediction")
        self.assertIn("not already captured", contextuality.reinstatement_condition)

    def test_all_live_branches_have_kill_conditions(self) -> None:
        for branch in self.result.branches:
            self.assertTrue(branch.kill_condition)
            self.assertNotIn("TBD", branch.kill_condition)

    def test_q1_update_names_subclaims(self) -> None:
        self.assertIn("Q1A access-boundary", self.result.q1_update)
        self.assertIn("Q1B detector provenance", self.result.q1_update)
        self.assertIn("Q1C dormant", self.result.q1_update)
        self.assertIn("Q1D contextuality", self.result.q1_update)


if __name__ == "__main__":
    unittest.main()
