"""Tests for T123 same-payload packet FOA witness."""

from __future__ import annotations

import unittest

from models.real_detector_packet_schema_audit import PacketVerdict
from models.same_payload_packet_foa_witness import (
    FULL_FOA,
    RAW_ONLY_FOA,
    WITHHELD_FOA,
    audit_packet_against_reference,
    reference_packet,
    run_t123_analysis,
    same_payload_packet_variants,
)


class SamePayloadPacketFOAWitnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.reference = reference_packet()
        self.result = run_t123_analysis()
        self.audits = {audit.packet_id: audit for audit in self.result.audits}

    def test_all_variants_keep_raw_payload_result_and_coarse_summary_fixed(self) -> None:
        for audit in self.result.audits:
            self.assertTrue(audit.same_raw_payload, audit.packet_id)
            self.assertTrue(audit.same_measurement_result, audit.packet_id)
            self.assertTrue(audit.same_coarse_detector_summary, audit.packet_id)

    def test_reference_packet_has_full_future_operations(self) -> None:
        audit = self.audits["same_payload_reference_packet"]

        self.assertEqual(audit.packet_verdict, PacketVerdict.ADMISSIBLE)
        self.assertTrue(audit.signature_valid)
        self.assertEqual(audit.future_operations, FULL_FOA)
        self.assertFalse(audit.operations_removed_vs_reference)

    def test_required_packet_field_variants_are_present(self) -> None:
        self.assertEqual(
            {packet.packet_id for packet in same_payload_packet_variants()},
            {
                "same_payload_reference_packet",
                "missing_provenance_same_payload",
                "authority_collapsed_same_payload",
                "invalid_signature_same_payload",
                "key_compromised_same_payload",
                "revoked_authority_same_payload",
                "publication_delayed_same_payload",
                "missing_witnesses_same_payload",
                "missing_reconstruction_same_payload",
                "open_challenge_same_payload",
            },
        )

    def test_packet_failures_change_foa_while_immediate_result_is_unchanged(self) -> None:
        for audit in self.result.audits:
            if audit.packet_id == "same_payload_reference_packet":
                continue
            self.assertTrue(audit.immediate_result_unchanged_but_foa_changed)
            self.assertNotEqual(audit.future_operations, FULL_FOA)
            self.assertIn("read_immediate_result", audit.future_operations)
            self.assertIn("retain_raw_payload", audit.future_operations)

    def test_open_challenge_withholds_rather_than_invalidates_raw_result(self) -> None:
        audit = self.audits["open_challenge_same_payload"]

        self.assertEqual(audit.packet_verdict, PacketVerdict.WITHHOLD)
        self.assertEqual(audit.future_operations, WITHHELD_FOA)
        self.assertIn("inspect_dispute", audit.future_operations)
        self.assertIn("certify_packet", audit.operations_removed_vs_reference)

    def test_inadmissible_packet_variants_keep_raw_only_foa(self) -> None:
        for packet_id in (
            "missing_provenance_same_payload",
            "authority_collapsed_same_payload",
            "invalid_signature_same_payload",
            "key_compromised_same_payload",
            "revoked_authority_same_payload",
            "publication_delayed_same_payload",
            "missing_witnesses_same_payload",
            "missing_reconstruction_same_payload",
        ):
            audit = self.audits[packet_id]
            self.assertEqual(audit.packet_verdict, PacketVerdict.INADMISSIBLE)
            self.assertEqual(audit.future_operations, RAW_ONLY_FOA)
            self.assertTrue(audit.operations_removed_vs_reference)

    def test_signature_invalidity_is_detected_even_with_same_payload(self) -> None:
        packet = [
            candidate
            for candidate in same_payload_packet_variants()
            if candidate.packet_id == "invalid_signature_same_payload"
        ][0]
        audit = audit_packet_against_reference(packet, self.reference)

        self.assertFalse(audit.signature_valid)
        self.assertIn("invalid_signature", audit.admissibility_failures)
        self.assertEqual(audit.packet_verdict, PacketVerdict.INADMISSIBLE)

    def test_claim_impact_does_not_promote_q1(self) -> None:
        self.assertIn("No Q1 or detector-physics promotion", self.result.claim_impact_note)
        self.assertIn("Q1B remains externally blocked", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
