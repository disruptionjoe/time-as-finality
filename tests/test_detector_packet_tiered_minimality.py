"""Tests for T133 detector packet tiered minimality."""

from __future__ import annotations

import unittest

from models.detector_packet_tiered_minimality import (
    CLAIM_REVIEW_EXTENSION_FIELDS,
    PROVISIONAL_ADMISSION_FIELDS,
    RAW_IDENTITY_FIELDS,
    run_t133_analysis,
)


class DetectorPacketTieredMinimalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t133_analysis()
        self.audits = {audit.packet_id: audit for audit in self.result.audits}

    def test_tier_field_sets_match_expected_split(self) -> None:
        self.assertEqual(
            RAW_IDENTITY_FIELDS,
            (
                "detector_identity",
                "run_session_id",
                "causal_ordering_data",
                "raw_measurement_payload",
                "calibration_reference",
            ),
        )
        self.assertEqual(
            PROVISIONAL_ADMISSION_FIELDS,
            RAW_IDENTITY_FIELDS
            + (
                "provenance_chain",
                "signatures",
                "authority_domains",
                "publication_status",
                "revocation_status",
                "key_state",
                "admissibility_tokens",
            ),
        )
        self.assertEqual(
            CLAIM_REVIEW_EXTENSION_FIELDS,
            ("witness_references", "reconstruction_paths", "challenge_status"),
        )

    def test_reference_packet_clears_all_tiers(self) -> None:
        audit = self.audits["same_payload_reference_packet"]

        self.assertTrue(audit.raw_evidence_preserved)
        self.assertTrue(audit.provisionally_admissible)
        self.assertTrue(audit.claim_review_ready)

    def test_provisional_core_failures_block_earliest_tier(self) -> None:
        for packet_id in (
            "missing_provenance_same_payload",
            "authority_collapsed_same_payload",
            "invalid_signature_same_payload",
            "key_compromised_same_payload",
            "revoked_authority_same_payload",
            "publication_delayed_same_payload",
        ):
            audit = self.audits[packet_id]
            self.assertTrue(audit.raw_evidence_preserved, packet_id)
            self.assertFalse(audit.provisionally_admissible, packet_id)
            self.assertFalse(audit.claim_review_ready, packet_id)

    def test_witness_and_reconstruction_fields_are_claim_review_extensions(self) -> None:
        for packet_id, field in (
            ("missing_witnesses_same_payload", "witness_references"),
            ("missing_reconstruction_same_payload", "reconstruction_paths"),
        ):
            audit = self.audits[packet_id]
            self.assertTrue(audit.provisionally_admissible, packet_id)
            self.assertFalse(audit.claim_review_ready, packet_id)
            self.assertIn(field, audit.strict_only_fields_triggered)

    def test_open_challenge_withholds_review_but_not_provisional_intake(self) -> None:
        audit = self.audits["open_challenge_same_payload"]

        self.assertTrue(audit.provisionally_admissible)
        self.assertFalse(audit.claim_review_ready)
        self.assertIn("challenge_status", audit.strict_only_fields_triggered)

    def test_claim_language_explicitly_weakens_flat_packet_burden(self) -> None:
        self.assertIn("tiered, not flat", self.result.strongest_claim)
        self.assertIn("too coarse", self.result.weakened_claim)
        self.assertIn("Q1B remains externally blocked", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
