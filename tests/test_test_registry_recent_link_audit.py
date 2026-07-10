"""Tests for T522: recent test registry link audit."""

from __future__ import annotations

import json
import unittest

from models.test_registry_recent_link_audit import (
    MIN_RECENT_TEST_ID,
    VERDICT_PASS,
    audit_recent_registry,
)


class TestRegistryRecentLinkAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audit = audit_recent_registry()

    def test_recent_registry_rows_are_present_and_contiguous(self) -> None:
        self.assertEqual(self.audit.min_test_id, MIN_RECENT_TEST_ID)
        self.assertGreaterEqual(self.audit.max_test_id, 526)
        self.assertEqual(self.audit.missing_ids, ())
        self.assertEqual(self.audit.duplicate_ids, ())

    def test_recent_specs_and_result_markdown_exist(self) -> None:
        self.assertEqual(self.audit.missing_spec_paths, ())
        self.assertEqual(self.audit.spec_id_mismatches, ())
        self.assertEqual(self.audit.missing_result_links, ())
        self.assertEqual(self.audit.missing_result_paths, ())

    def test_executable_suite_links_recent_result_artifacts(self) -> None:
        self.assertEqual(self.audit.missing_executable_suite_links, ())

    def test_no_home_paths_in_audited_registry_text(self) -> None:
        self.assertEqual(self.audit.home_path_hits, ())

    def test_verdict_payload_is_serializable(self) -> None:
        self.assertEqual(self.audit.verdict, VERDICT_PASS)
        payload = self.audit.to_payload()
        self.assertEqual(payload["artifact_id"], "T522-test-registry-recent-link-audit-v0.1")
        json.dumps(payload, sort_keys=True)


if __name__ == "__main__":
    unittest.main()
