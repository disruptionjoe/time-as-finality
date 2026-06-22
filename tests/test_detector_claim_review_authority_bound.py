"""Tests for T173 detector claim-review authority bound."""

from __future__ import annotations

import unittest

from models.detector_authority_domain_bound import enumerate_partitions
from models.detector_claim_review_authority_bound import (
    CLAIM_REVIEW_DOMAINS,
    run_t173_analysis,
)


class DetectorClaimReviewAuthorityBoundTests(unittest.TestCase):
    def test_partition_enumeration_covers_all_six_domain_partitions(self) -> None:
        partitions = enumerate_partitions(CLAIM_REVIEW_DOMAINS)
        self.assertEqual(len(partitions), 203)

    def test_minimum_admissible_authority_count_is_five(self) -> None:
        result = run_t173_analysis()

        self.assertEqual(result.minimum_admissible_authority_count, 5)
        self.assertTrue(result.no_four_domain_profile_survives)

    def test_exactly_three_minimal_five_domain_profiles_survive(self) -> None:
        result = run_t173_analysis()

        self.assertEqual(
            set(result.admissible_five_domain_profiles),
            {
                "merge_analysis_governor+instrument_operator",
                "merge_archive_custodian+instrument_operator",
                "merge_control_designer+instrument_operator",
            },
        )

    def test_escrow_cannot_merge_with_trust_or_archive(self) -> None:
        result = run_t173_analysis()
        audits = {audit.profile_name: audit for audit in result.audits}

        trust_merge = audits["merge_escrow_custodian+trust_auditor"]
        archive_merge = audits["merge_archive_custodian+escrow_custodian"]

        self.assertFalse(trust_merge.admissible)
        self.assertIn("trust_auditor", trust_merge.escrow_conflicts)
        self.assertFalse(archive_merge.admissible)
        self.assertIn("archive_custodian", archive_merge.escrow_conflicts)

    def test_result_language_records_five_domain_bound(self) -> None:
        result = run_t173_analysis()

        self.assertIn("five-domain lower bound", result.q1b_update)
        self.assertIn("five authority domains", result.claim_ledger_update)
        self.assertIn("named escrow authority", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
