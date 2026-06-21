"""Tests for T136 detector pre-registration manifest."""

from __future__ import annotations

import unittest

from models.detector_preregistration_manifest import (
    audit_preregistration_manifest,
    complete_claim_review_manifest,
    invalid_authority_manifest,
    observed_payload_value_manifest,
    provisional_only_manifest,
    raw_log_only_manifest,
    run_t136_analysis,
)


class DetectorPreregistrationManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t136_analysis()
        self.audits = {audit.manifest_name: audit for audit in self.result.audits}

    def test_complete_manifest_clears_claim_review_gate(self) -> None:
        audit = self.audits["complete_claim_review_manifest"]

        self.assertTrue(audit.claimed_tier_admissible)
        self.assertEqual(audit.max_certifiable_tier, "claim_review")
        self.assertTrue(audit.t97_table_commitments_valid)
        self.assertTrue(audit.wrapper_commitments_valid)
        self.assertTrue(audit.authority_partition_admissible)
        self.assertEqual(audit.failure_reasons, ())

    def test_honest_provisional_manifest_does_not_need_review_extension(self) -> None:
        audit = self.audits["provisional_only_manifest"]

        self.assertTrue(audit.claimed_tier_admissible)
        self.assertEqual(audit.max_certifiable_tier, "provisional_admission")
        self.assertEqual(
            set(audit.missing_claim_review_fields),
            {"witness_references", "reconstruction_paths", "challenge_status"},
        )

    def test_t97_only_manifest_cannot_claim_provisional_admission(self) -> None:
        audit = self.audits["raw_log_only_manifest"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertEqual(audit.max_certifiable_tier, "raw_log_preservation")
        self.assertIn("missing_provisional_wrapper_commitments", audit.failure_reasons)
        self.assertIn("raw_measurement_payload", audit.missing_provisional_fields)
        self.assertIn("authority_domains", audit.missing_provisional_fields)

    def test_claim_review_tier_requires_witness_reconstruction_and_dispute_fields(self) -> None:
        audit = self.audits["claim_review_missing_witness_manifest"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertEqual(audit.max_certifiable_tier, "provisional_admission")
        self.assertIn("missing_claim_review_wrapper_commitments", audit.failure_reasons)
        self.assertEqual(
            set(audit.missing_claim_review_fields),
            {"witness_references", "reconstruction_paths", "challenge_status"},
        )

    def test_posthoc_and_deferred_tiers_fail_predata_gate(self) -> None:
        posthoc = self.audits["posthoc_claim_review_manifest"]
        deferred = self.audits["deferred_tier_manifest"]

        self.assertFalse(posthoc.predata_boundary_respected)
        self.assertFalse(posthoc.claimed_tier_admissible)
        self.assertIn("manifest_not_registered_before_first_event", posthoc.failure_reasons)
        self.assertIn("data_accessed_before_manifest_lock", posthoc.failure_reasons)

        self.assertFalse(deferred.claimed_tier_admissible)
        self.assertIn("invalid_or_undeclared_claimed_tier", deferred.failure_reasons)

    def test_authority_partition_uses_t100_lower_bound(self) -> None:
        audit = self.audits["three_domain_authority_manifest"]

        self.assertFalse(audit.authority_partition_admissible)
        self.assertFalse(audit.claimed_tier_admissible)
        self.assertEqual(audit.authority_count, 3)
        self.assertIn("authority_partition_below_t100_lower_bound", audit.failure_reasons)

    def test_predata_manifest_commits_export_rule_not_observed_payload(self) -> None:
        audit = self.audits["observed_payload_value_manifest"]

        self.assertFalse(audit.claimed_tier_admissible)
        self.assertIn(
            "predata_manifest_claims_observed_payload_values",
            audit.failure_reasons,
        )

    def test_hash_mismatch_is_detected(self) -> None:
        audit = self.audits["manifest_hash_mismatch_case"]

        self.assertFalse(audit.manifest_hash_valid)
        self.assertFalse(audit.claimed_tier_admissible)
        self.assertIn("manifest_hash_mismatch", audit.failure_reasons)

    def test_single_manifest_audit_matches_batch_result(self) -> None:
        direct = audit_preregistration_manifest(complete_claim_review_manifest())

        self.assertTrue(direct.claimed_tier_admissible)
        self.assertEqual(
            direct.failure_reasons,
            self.audits["complete_claim_review_manifest"].failure_reasons,
        )

    def test_fixture_helpers_expose_targeted_negative_controls(self) -> None:
        self.assertEqual(raw_log_only_manifest().claimed_tier, "provisional_admission")
        self.assertEqual(provisional_only_manifest().claimed_tier, "provisional_admission")
        self.assertEqual(invalid_authority_manifest().claimed_tier, "claim_review")
        self.assertEqual(
            observed_payload_value_manifest().claimed_tier,
            "claim_review",
        )

    def test_result_language_keeps_q1b_externally_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("post hoc", self.result.weakened)
        self.assertIn("pre-event manifest gate", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
