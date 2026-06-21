"""Tests for T121 real detector packet schema audit."""

from __future__ import annotations

import unittest

from models.real_detector_packet_schema_audit import (
    PacketVerdict,
    REQUIRED_ADMISSIBILITY_TOKENS,
    SCHEMA_FIELDS,
    validate_packet,
    finite_packet_cases,
    run_t121_analysis,
    valid_packet,
)


class RealDetectorPacketSchemaAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t121_analysis()
        self.audits = {audit.packet_id: audit for audit in self.result.audits}

    def test_schema_contains_required_user_fields(self) -> None:
        self.assertEqual(
            set(SCHEMA_FIELDS),
            {
                "detector_identity",
                "run_session_id",
                "causal_ordering_data",
                "raw_measurement_payload",
                "calibration_reference",
                "provenance_chain",
                "signatures",
                "authority_domains",
                "publication_status",
                "revocation_status",
                "key_state",
                "witness_references",
                "reconstruction_paths",
                "admissibility_tokens",
                "challenge_status",
            },
        )

    def test_valid_packet_is_admissible_and_preserves_full_operations(self) -> None:
        audit = validate_packet(valid_packet())

        self.assertTrue(audit.raw_payload_valid)
        self.assertEqual(audit.packet_verdict, PacketVerdict.ADMISSIBLE)
        self.assertFalse(audit.admissibility_failures)
        self.assertIn("use_for_detector_claim_review", audit.future_operations)
        self.assertTrue(REQUIRED_ADMISSIBILITY_TOKENS <= valid_packet().admissibility_tokens)

    def test_all_required_finite_cases_are_present(self) -> None:
        self.assertEqual(
            {packet.packet_id for packet in finite_packet_cases()},
            {
                "valid_packet",
                "missing_provenance",
                "key_compromised",
                "revoked_authority",
                "publication_delayed",
                "authority_domains_collapsed",
                "valid_raw_data_inadmissible_packet",
                "same_raw_data_reduced_future_rights",
            },
        )

    def test_negative_cases_keep_raw_data_valid_but_block_or_withhold_packet(self) -> None:
        for packet_id, audit in self.audits.items():
            self.assertTrue(audit.raw_payload_valid, packet_id)
            if packet_id != "valid_packet":
                self.assertNotEqual(audit.packet_verdict, PacketVerdict.ADMISSIBLE)
                self.assertNotIn("use_for_detector_claim_review", audit.future_operations)

    def test_missing_provenance_is_existing_protocol_failure(self) -> None:
        audit = self.audits["missing_provenance"]

        self.assertEqual(audit.packet_verdict, PacketVerdict.INADMISSIBLE)
        self.assertIn("missing_provenance_chain", audit.admissibility_failures)
        self.assertIn(
            "T87/T97 raw-log provenance contract",
            audit.handled_by_existing_protocol_artifacts,
        )

    def test_key_compromise_and_revocation_reveal_schema_requirements(self) -> None:
        key = self.audits["key_compromised"]
        revoked = self.audits["revoked_authority"]

        self.assertIn("signing_key_compromised", key.admissibility_failures)
        self.assertTrue(key.missing_schema_requirements_revealed)
        self.assertIn("authority_or_packet_revoked", revoked.admissibility_failures)
        self.assertTrue(revoked.missing_schema_requirements_revealed)

    def test_same_raw_data_can_change_future_operation_rights(self) -> None:
        valid = self.audits["valid_packet"]
        disputed = self.audits["same_raw_data_reduced_future_rights"]

        self.assertEqual(disputed.packet_verdict, PacketVerdict.WITHHOLD)
        self.assertGreater(len(valid.future_operations), len(disputed.future_operations))
        self.assertIn("future_operations_withheld_pending_dispute", disputed.failures_change_future_operation_availability)

    def test_claim_impact_does_not_promote_detector_claims(self) -> None:
        self.assertIn("No Q1 or detector-physics promotion", self.result.claim_impact_recommendation)
        self.assertIn("infrastructure", self.result.claim_impact_recommendation)


if __name__ == "__main__":
    unittest.main()
