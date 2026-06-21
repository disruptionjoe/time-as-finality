"""Tests for T97: detector dry-run packet skeleton."""

from __future__ import annotations

import unittest

from models.detector_dry_run_packet_skeleton import (
    audit_detector_dry_run_packet,
    locked_detector_dry_run_packet_skeleton,
    missing_control_roles_packet,
    placeholder_population_attempt_packet,
    posthoc_packet_skeleton,
    run_t97_analysis,
    schema_drift_packet,
)
from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS


class DetectorDryRunPacketSkeletonTests(unittest.TestCase):
    def test_locked_packet_covers_t87_schema_without_empirical_upgrade(self) -> None:
        audit = audit_detector_dry_run_packet(
            locked_detector_dry_run_packet_skeleton()
        )

        self.assertEqual(audit.verdict, "schema_complete_predata_scaffold_only")
        self.assertEqual(audit.evidence_verdict, "withhold_detector_q1_upgrade")
        self.assertEqual(audit.failure_reasons, ())
        self.assertEqual(audit.missing_tables, ())
        self.assertEqual(audit.missing_columns, ())
        self.assertEqual(audit.extra_columns, ())
        self.assertEqual(set(audit.placeholder_tables), set(REQUIRED_TABLE_COLUMNS))
        self.assertEqual(audit.real_row_tables, ())
        self.assertEqual(
            audit.t87_failure_reasons_if_scored_now,
            ("no_real_raw_deployment_log",),
        )

    def test_placeholder_population_attempt_is_rejected(self) -> None:
        audit = audit_detector_dry_run_packet(placeholder_population_attempt_packet())

        self.assertEqual(audit.verdict, "inadmissible_dry_run_packet")
        self.assertIn(
            "attempts_to_populate_counts_from_placeholders",
            audit.failure_reasons,
        )
        self.assertEqual(audit.evidence_verdict, "withhold_detector_q1_upgrade")

    def test_schema_drift_is_rejected_even_before_data(self) -> None:
        audit = audit_detector_dry_run_packet(schema_drift_packet())

        self.assertEqual(audit.verdict, "inadmissible_dry_run_packet")
        self.assertIn("unregistered_schema_columns", audit.failure_reasons)
        self.assertIn("event_time_tag_stream.operator_note", audit.extra_columns)

    def test_posthoc_packet_is_rejected(self) -> None:
        audit = audit_detector_dry_run_packet(posthoc_packet_skeleton())

        self.assertEqual(audit.verdict, "inadmissible_dry_run_packet")
        self.assertIn(
            "packet_not_locked_before_first_event",
            audit.failure_reasons,
        )
        self.assertIn("data_accessed_before_packet_lock", audit.failure_reasons)

    def test_missing_hostile_controls_are_rejected(self) -> None:
        audit = audit_detector_dry_run_packet(missing_control_roles_packet())

        self.assertEqual(audit.verdict, "inadmissible_dry_run_packet")
        self.assertIn("missing_t86_control_roles", audit.failure_reasons)
        self.assertIn(
            "all_channels_ambiguous_negative_control",
            audit.missing_control_roles,
        )
        self.assertIn("dag_truncation_false_edge_control", audit.missing_control_roles)

    def test_run_result_preserves_scaffold_not_evidence_boundary(self) -> None:
        result = run_t97_analysis()

        self.assertIn("pre-data scaffold", result.strongest_claim)
        self.assertIn("not evidence", result.q1_update)
        self.assertIn("Template rows", result.weakened)
        self.assertIn("Placeholder rows", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
