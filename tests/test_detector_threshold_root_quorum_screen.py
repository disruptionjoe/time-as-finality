"""Tests for T175 detector threshold-root quorum screen."""

from __future__ import annotations

import unittest

from models.detector_threshold_root_quorum_screen import (
    audit_threshold_root_policy,
    run_t175_analysis,
    threshold_root_policies,
)


class DetectorThresholdRootQuorumScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t175_analysis()
        self.audits = {audit.policy_id: audit for audit in self.result.audits}
        self.policies = {
            policy.policy_id: policy for policy in threshold_root_policies()
        }

    def test_mandatory_guardian_policy_is_the_only_live_route(self) -> None:
        audit = self.audits["mandatory_archive_and_escrow_release"]

        self.assertEqual(audit.classification, "live_threshold_claim_review_policy")
        self.assertTrue(audit.release_guardians_preserved)
        self.assertTrue(audit.revocation_guardians_preserved)
        self.assertTrue(audit.audit_guardians_preserved)
        self.assertEqual(
            self.result.live_threshold_policies,
            ("mandatory_archive_and_escrow_release",),
        )

    def test_optional_escrow_release_policy_is_null(self) -> None:
        audit = self.audits["optional_escrow_two_of_three_release"]

        self.assertEqual(
            audit.classification,
            "null_release_quorum_bypasses_required_guardian",
        )
        self.assertIn("escrow_custodian", audit.release_bypass_domains)
        self.assertFalse(audit.release_guardians_preserved)

    def test_optional_archive_release_policy_is_null(self) -> None:
        audit = self.audits["optional_archive_three_of_four_release"]

        self.assertEqual(
            audit.classification,
            "null_release_quorum_bypasses_required_guardian",
        )
        self.assertIn("archive_custodian", audit.release_bypass_domains)

    def test_optional_trust_revocation_policy_is_null(self) -> None:
        audit = self.audits["optional_trust_two_of_three_revocation"]

        self.assertEqual(
            audit.classification,
            "null_revocation_or_audit_quorum_bypasses_required_guardian",
        )
        self.assertIn("trust_auditor", audit.revocation_bypass_domains)
        self.assertFalse(audit.revocation_guardians_preserved)

    def test_global_multisig_can_fail_both_release_and_audit(self) -> None:
        audit = self.audits["global_three_of_five_multisig"]

        self.assertEqual(
            audit.classification,
            "null_release_quorum_bypasses_required_guardian",
        )
        self.assertIn("escrow_custodian", audit.release_bypass_domains)
        self.assertIn("trust_auditor", audit.audit_bypass_domains)

    def test_direct_and_wrapped_audits_match(self) -> None:
        policy = self.policies["mandatory_archive_and_escrow_release"]
        direct = audit_threshold_root_policy(policy)
        wrapped = self.audits["mandatory_archive_and_escrow_release"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(direct.release_bypass_domains, wrapped.release_bypass_domains)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("threshold or multisig control is null", self.result.claim_ledger_update)
        self.assertIn("pre-data quorum map", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
