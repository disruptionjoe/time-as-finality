"""Tests for T521: detector manifest template gate."""

from __future__ import annotations

import unittest

from models.detector_authority_domain_bound import DOMAINS
from models.detector_dry_run_packet_skeleton import locked_detector_dry_run_packet_skeleton
from models.detector_manifest_template_gate import (
    OBSERVED_VALUE_KIND,
    VERDICT_PASS,
    audit_template,
    expected_commitment_kind,
)
from models.detector_preregistration_manifest import ALLOWED_TIERS
from models.real_detector_packet_schema_audit import SCHEMA_FIELDS


class DetectorManifestTemplateGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audit = audit_template()

    def test_template_covers_every_t97_table(self) -> None:
        expected = {table.table_name for table in locked_detector_dry_run_packet_skeleton().tables}

        self.assertEqual(set(self.audit.missing_t97_tables), set())
        self.assertTrue(expected)

    def test_template_covers_every_t121_t133_wrapper_field(self) -> None:
        self.assertEqual(set(self.audit.missing_wrapper_fields), set())
        self.assertIn("raw_measurement_payload", SCHEMA_FIELDS)
        self.assertIn("authority_domains", SCHEMA_FIELDS)

    def test_commitment_kinds_match_t136_predata_boundary(self) -> None:
        self.assertEqual(self.audit.wrong_commitment_kinds, ())
        self.assertEqual(expected_commitment_kind("raw_measurement_payload"), "export_rule_commitment")
        self.assertEqual(expected_commitment_kind("revocation_status"), "state_commitment")
        self.assertEqual(expected_commitment_kind("detector_identity"), "schema_commitment")

    def test_authority_domains_and_tiers_are_present(self) -> None:
        self.assertEqual(set(self.audit.missing_authority_domains), set())
        self.assertEqual(set(DOMAINS) - set(self.audit.missing_authority_domains), set(DOMAINS))
        self.assertEqual(set(self.audit.missing_tier_choices), set())
        self.assertEqual(set(ALLOWED_TIERS) - set(self.audit.missing_tier_choices), set(ALLOWED_TIERS))

    def test_template_blocks_observed_payload_values_predata(self) -> None:
        self.assertTrue(self.audit.has_no_data_boundary)
        self.assertFalse(self.audit.has_observed_value_commitment)
        self.assertEqual(OBSERVED_VALUE_KIND, "observed_value_commitment")

    def test_verdict_is_review_only_pass(self) -> None:
        self.assertEqual(self.audit.verdict, VERDICT_PASS)


if __name__ == "__main__":
    unittest.main()
