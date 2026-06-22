"""Tests for T180 branch-support threshold minimality."""

from __future__ import annotations

import unittest

from models.branch_support_threshold_minimality import (
    backup_branch_threshold,
    run_t180_analysis,
    survive_one_branch_failure,
    topology_family,
)


class BranchSupportThresholdMinimalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t180_analysis()
        self.profiles = {profile.profile_id: profile for profile in topology_family()}
        self.audits = {audit.projection_name: audit for audit in self.result.audits}

    def test_threshold_projection_factors_through_current_task(self) -> None:
        audit = self.audits["backup_branch_threshold"]

        self.assertTrue(audit.factors_through_capability)
        self.assertEqual(audit.value_count, 2)
        self.assertEqual(audit.verdict, "factors_through_capability")

    def test_exact_branch_support_is_not_minimal(self) -> None:
        self.assertTrue(self.result.exact_branch_support_nonminimal)
        exact = self.audits["exact_branch_support"]
        threshold = self.audits["backup_branch_threshold"]

        self.assertTrue(exact.factors_through_capability)
        self.assertGreater(exact.value_count, threshold.value_count)

    def test_support_two_and_three_are_capability_equivalent(self) -> None:
        dual = self.profiles["dual_branch_triplicate"]
        triple = self.profiles["triple_branch_triplicate"]

        self.assertEqual(backup_branch_threshold(dual), backup_branch_threshold(triple))
        self.assertTrue(survive_one_branch_failure(dual))
        self.assertTrue(survive_one_branch_failure(triple))

    def test_non_support_signatures_fail(self) -> None:
        holder_audit = self.audits["holder_count_only"]
        chain_audit = self.audits["causal_chain_count_only"]
        nonsupport_audit = self.audits["nonsupport_topology_signature"]

        self.assertFalse(holder_audit.factors_through_capability)
        self.assertEqual(
            holder_audit.witness_pair,
            ("single_branch_triplicate", "dual_branch_triplicate"),
        )
        self.assertFalse(chain_audit.factors_through_capability)
        self.assertEqual(
            chain_audit.witness_pair,
            ("single_branch_triplicate", "dual_branch_triplicate"),
        )
        self.assertFalse(nonsupport_audit.factors_through_capability)
        self.assertEqual(
            nonsupport_audit.witness_pair,
            ("single_branch_triplicate", "dual_branch_triplicate"),
        )

    def test_result_language_records_the_weakening(self) -> None:
        self.assertIn("not the minimal topology coordinate", self.result.strongest_claim)
        self.assertIn("exact numeric branch_support", self.result.weakened)


if __name__ == "__main__":
    unittest.main()
