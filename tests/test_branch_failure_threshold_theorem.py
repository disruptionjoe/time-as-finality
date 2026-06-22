"""Tests for T181 branch-failure threshold theorem."""

from __future__ import annotations

import unittest

from models.branch_failure_threshold_theorem import (
    BRANCH_IDS,
    branch_support_count,
    max_tolerated_branch_failures,
    run_t181_analysis,
    support_threshold,
    survive_k_branch_failures,
    survive_named_outage,
    topology_family,
)


class BranchFailureThresholdTheoremTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t181_analysis()
        self.thresholds = {
            audit.task_name: audit for audit in self.result.threshold_audits
        }
        self.boundaries = {
            (audit.task_name, audit.projection_name): audit
            for audit in self.result.boundary_audits
        }

    def test_threshold_predicates_match_survival_tasks_for_all_k(self) -> None:
        profiles = topology_family()

        for k in range(len(BRANCH_IDS)):
            audit = self.thresholds[f"survive_{k}_branch_failures"]
            self.assertTrue(audit.factors_through_capability)
            for profile in profiles:
                self.assertEqual(
                    support_threshold(profile, k),
                    survive_k_branch_failures(profile, k),
                )

    def test_exact_branch_count_is_nonminimal_for_fixed_one_failure_task(self) -> None:
        threshold = self.thresholds["survive_1_branch_failures"]
        exact = self.boundaries[
            ("survive_one_branch_failure", "exact_branch_support_count")
        ]

        self.assertTrue(threshold.factors_through_capability)
        self.assertTrue(exact.factors_through_capability)
        self.assertLess(threshold.projection_value_count, exact.projection_value_count)

    def test_exact_branch_count_is_needed_for_margin_capability(self) -> None:
        threshold = self.boundaries[
            ("max_tolerated_branch_failures", "support_threshold_ge_2")
        ]
        exact = self.boundaries[
            ("max_tolerated_branch_failures", "exact_branch_support_count")
        ]

        self.assertFalse(threshold.factors_through_capability)
        self.assertIsNotNone(threshold.witness_pair)
        self.assertTrue(exact.factors_through_capability)

    def test_branch_identity_is_needed_for_named_outage_capability(self) -> None:
        count = self.boundaries[
            ("survive_named_outage_A_C", "exact_branch_support_count")
        ]
        identity = self.boundaries[
            ("survive_named_outage_A_C", "support_branch_identity_set")
        ]

        self.assertFalse(count.factors_through_capability)
        self.assertIsNotNone(count.witness_pair)
        self.assertTrue(identity.factors_through_capability)

    def test_named_outage_witness_has_same_count_but_different_capability(self) -> None:
        profiles = {profile.profile_id: profile for profile in topology_family()}
        audit = self.boundaries[
            ("survive_named_outage_A_C", "exact_branch_support_count")
        ]
        left = profiles[audit.witness_pair[0]]
        right = profiles[audit.witness_pair[1]]
        failed = frozenset({"A", "C"})

        self.assertEqual(branch_support_count(left), branch_support_count(right))
        self.assertNotEqual(
            survive_named_outage(left, failed),
            survive_named_outage(right, failed),
        )

    def test_margin_witness_has_same_threshold_but_different_margin(self) -> None:
        profiles = {profile.profile_id: profile for profile in topology_family()}
        audit = self.boundaries[
            ("max_tolerated_branch_failures", "support_threshold_ge_2")
        ]
        left = profiles[audit.witness_pair[0]]
        right = profiles[audit.witness_pair[1]]

        self.assertEqual(support_threshold(left, 1), support_threshold(right, 1))
        self.assertNotEqual(
            max_tolerated_branch_failures(left),
            max_tolerated_branch_failures(right),
        )

    def test_result_language_keeps_h7_demoted(self) -> None:
        self.assertIn("not H7 physical-arrow evidence", self.result.claim_ledger_update)
        self.assertIn("Exact count is over-specified", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
