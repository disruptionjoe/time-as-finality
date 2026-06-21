"""Tests for T134 detector dry-run tier gate."""

from __future__ import annotations

import unittest

from models.detector_dry_run_tier_gate import (
    FIELD_COVERAGE_BY_T97,
    run_t134_analysis,
)


class DetectorDryRunTierGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t134_analysis()
        self.audits = {audit.case_name: audit for audit in self.result.audits}

    def test_t97_native_coverage_exposes_wrapper_gaps(self) -> None:
        self.assertEqual(
            FIELD_COVERAGE_BY_T97["raw_measurement_payload"],
            "missing_from_t97_raw_log_scaffold",
        )
        self.assertEqual(
            FIELD_COVERAGE_BY_T97["revocation_status"],
            "missing_from_t97_raw_log_scaffold",
        )
        self.assertEqual(
            FIELD_COVERAGE_BY_T97["admissibility_tokens"],
            "partial_via_policy_schema_and_demotion_hashes",
        )

    def test_predata_t97_scaffold_is_not_evidence_admission(self) -> None:
        audit = self.audits["locked_t97_predata_scaffold_only"]

        self.assertTrue(audit.raw_log_scaffold_ready)
        self.assertFalse(audit.real_t97_rows_present)
        self.assertFalse(audit.raw_evidence_preserved)
        self.assertFalse(audit.provisionally_admissible)
        self.assertIn("no_real_t97_rows", audit.blocking_reasons)
        self.assertIn("missing_t121_t133_packet_wrapper", audit.blocking_reasons)

    def test_filled_t97_rows_alone_are_necessary_not_sufficient(self) -> None:
        audit = self.audits["filled_t97_raw_log_only"]

        self.assertTrue(audit.real_t97_rows_present)
        self.assertTrue(audit.raw_log_scaffold_ready)
        self.assertFalse(audit.provisionally_admissible)
        self.assertIn("raw_measurement_payload", audit.missing_native_provisional_fields)
        self.assertIn("authority_domains", audit.missing_native_provisional_fields)
        self.assertIn("reconstruction_paths", audit.missing_native_claim_review_fields)
        self.assertIn("missing_t121_t133_packet_wrapper", audit.blocking_reasons)

    def test_complete_wrapper_clears_all_tiers_as_integration_target(self) -> None:
        audit = self.audits["filled_t97_with_reference_wrapper"]

        self.assertTrue(audit.real_t97_rows_present)
        self.assertTrue(audit.raw_evidence_preserved)
        self.assertTrue(audit.provisionally_admissible)
        self.assertTrue(audit.claim_review_ready)
        self.assertEqual(audit.blocking_reasons, ())

    def test_missing_provenance_blocks_provisional_admission(self) -> None:
        audit = self.audits["filled_t97_missing_provenance_wrapper"]

        self.assertFalse(audit.provisionally_admissible)
        self.assertFalse(audit.claim_review_ready)
        self.assertIn("provenance_chain", audit.wrapper_provisional_failures)
        self.assertIn(
            "wrapper_provisional_failure:provenance_chain",
            audit.blocking_reasons,
        )

    def test_witness_and_challenge_failures_preserve_intake_only(self) -> None:
        missing_witnesses = self.audits["filled_t97_missing_witnesses_wrapper"]
        open_challenge = self.audits["filled_t97_open_challenge_wrapper"]

        self.assertTrue(missing_witnesses.provisionally_admissible)
        self.assertFalse(missing_witnesses.claim_review_ready)
        self.assertIn("witness_references", missing_witnesses.wrapper_claim_review_failures)

        self.assertTrue(open_challenge.provisionally_admissible)
        self.assertFalse(open_challenge.claim_review_ready)
        self.assertIn("challenge_status", open_challenge.wrapper_claim_review_failures)

    def test_result_language_keeps_q1b_externally_blocked(self) -> None:
        self.assertIn("necessary but not sufficient", self.result.strongest_claim)
        self.assertIn("weakens", self.result.weakened)
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)


if __name__ == "__main__":
    unittest.main()
