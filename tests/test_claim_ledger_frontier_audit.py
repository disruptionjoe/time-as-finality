"""Tests for T523: claim-ledger frontier audit."""

from __future__ import annotations

import json
import unittest

from models.claim_ledger_frontier_audit import (
    EXPECTED_MAX_TEST_ID,
    EXPECTED_UNTRIAGED_RANGES,
    VERDICT_PASS,
    audit_claim_ledger_frontier,
)


class ClaimLedgerFrontierAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audit = audit_claim_ledger_frontier()

    def test_registry_ceiling_matches_coverage_note(self) -> None:
        self.assertEqual(self.audit.max_test_id, EXPECTED_MAX_TEST_ID)
        self.assertEqual(self.audit.coverage_note_max_test_id, self.audit.max_test_id)

    def test_untriaged_frontier_is_declared_narrowly(self) -> None:
        self.assertEqual(self.audit.declared_untriaged_ranges, EXPECTED_UNTRIAGED_RANGES)

    def test_already_routed_no_row_segments_are_not_recounted_as_frontier(self) -> None:
        self.assertTrue(self.audit.t517_t519_no_row_receipt_present)
        self.assertTrue(self.audit.t521_t523_infrastructure_no_row_present)

    def test_no_claim_row_is_created_for_the_audit_itself(self) -> None:
        self.assertTrue(self.audit.twl_claim_row_present)
        self.assertFalse(self.audit.t523_claim_row_present)

    def test_payload_is_serializable_and_passes(self) -> None:
        self.assertEqual(self.audit.blockers, ())
        self.assertEqual(self.audit.verdict, VERDICT_PASS)
        payload = self.audit.to_payload()
        self.assertEqual(payload["artifact_id"], "T523-claim-ledger-frontier-audit-v0.1")
        json.dumps(payload, sort_keys=True)


if __name__ == "__main__":
    unittest.main()
