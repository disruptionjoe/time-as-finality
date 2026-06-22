"""Tests for T171 detector row-review substitution screen."""

from __future__ import annotations

import unittest

from models.detector_row_review_substitution_screen import (
    CLAIM_REVIEW_OPERATIONS,
    audit_row_review_substitute,
    row_review_substitutes,
    run_t171_analysis,
)


class DetectorRowReviewSubstitutionScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t171_analysis()
        self.audits = {audit.substitute_id: audit for audit in self.result.audits}
        self.substitutes = {
            substitute.substitute_id: substitute for substitute in row_review_substitutes()
        }

    def test_summary_and_proof_only_variants_are_scaffold(self) -> None:
        for substitute_id in ("aggregate_summary_only", "signed_proof_certificate_only"):
            audit = self.audits[substitute_id]
            self.assertEqual(
                audit.classification,
                "scaffold_only_summary_or_proof_substitute",
            )
            self.assertIn("reconstruct_event", audit.operations_missing_vs_claim_review)
            self.assertIn("challenge_packet", audit.operations_missing_vs_claim_review)

    def test_private_escrow_without_review_is_scaffold(self) -> None:
        audit = self.audits["private_escrow_with_auditor_statement"]
        self.assertEqual(
            audit.classification,
            "scaffold_only_private_escrow_without_review",
        )
        self.assertIn("verify_lineage", audit.operations_missing_vs_claim_review)
        self.assertIn("use_for_detector_claim_review", audit.operations_missing_vs_claim_review)

    def test_partial_and_late_row_routes_are_scaffold(self) -> None:
        sampled = self.audits["sampled_public_rows"]
        delayed = self.audits["delayed_full_rows_after_challenge_window"]

        self.assertEqual(sampled.classification, "scaffold_only_partial_row_visibility")
        self.assertIn("reconstruct_event", sampled.operations_missing_vs_claim_review)
        self.assertEqual(delayed.classification, "scaffold_only_late_review_window")
        self.assertIn("challenge_packet", delayed.operations_missing_vs_claim_review)
        self.assertIn("certify_packet", delayed.operations_missing_vs_claim_review)

    def test_full_reviewable_rows_are_the_only_live_route(self) -> None:
        audit = self.audits["reviewable_full_rows_with_independent_escrow"]
        self.assertEqual(audit.classification, "live_reviewable_row_path")
        self.assertEqual(audit.preserved_operations, CLAIM_REVIEW_OPERATIONS)
        self.assertEqual(
            self.result.live_row_review_substitutes,
            ("reviewable_full_rows_with_independent_escrow",),
        )

    def test_direct_and_wrapped_audits_match(self) -> None:
        substitute = self.substitutes["reviewable_full_rows_with_independent_escrow"]
        direct = audit_row_review_substitute(substitute)
        wrapped = self.audits["reviewable_full_rows_with_independent_escrow"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(direct.preserved_operations, wrapped.preserved_operations)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("Only full reviewable rows", self.result.claim_ledger_update)
        self.assertIn("demote Q1B", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
