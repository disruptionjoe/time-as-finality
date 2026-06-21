"""Tests for T95: detector stack export map."""

from __future__ import annotations

import unittest

from models.detector_stack_export_map import (
    audit_detector_stack_export_map,
    augmented_preregistered_time_tagging_plan,
    dashboard_summary_export_map,
    hydraharp_white_rabbit_native_timing_only_map,
    posthoc_augmented_time_tagging_map,
    run_t95_analysis,
    signed_archive_without_controls_map,
)
from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS


class DetectorStackExportMapTests(unittest.TestCase):
    def test_augmented_plan_maps_every_t87_table_but_is_not_empirical(self) -> None:
        audit = audit_detector_stack_export_map(
            augmented_preregistered_time_tagging_plan()
        )

        self.assertEqual(
            audit.verdict,
            "admissible_as_preregistered_deployment_plan_only",
        )
        self.assertEqual(audit.failure_reasons, ())
        self.assertEqual(set(audit.instrument_native_tables), {"event_time_tag_stream"})
        self.assertEqual(
            set(audit.middleware_required_tables),
            set(REQUIRED_TABLE_COLUMNS) - {"event_time_tag_stream"},
        )
        self.assertEqual(
            audit.next_allowed_audit,
            "collect_real_event_rows_without_schema_changes",
        )

    def test_native_time_tagger_export_is_not_the_raw_log_contract(self) -> None:
        audit = audit_detector_stack_export_map(
            hydraharp_white_rabbit_native_timing_only_map()
        )

        self.assertEqual(audit.verdict, "inadmissible_for_detector_q1_upgrade")
        self.assertIn("not_locked_to_t87_schema", audit.failure_reasons)
        self.assertIn("missing_required_t87_tables", audit.failure_reasons)
        self.assertIn("missing_required_t87_columns", audit.failure_reasons)
        self.assertEqual(set(audit.instrument_native_tables), {"event_time_tag_stream"})

    def test_signed_archive_without_controls_is_still_inadmissible(self) -> None:
        audit = audit_detector_stack_export_map(signed_archive_without_controls_map())

        self.assertEqual(audit.verdict, "inadmissible_for_detector_q1_upgrade")
        self.assertIn("not_locked_to_t87_schema", audit.failure_reasons)
        self.assertIn("missing_required_t87_tables", audit.failure_reasons)
        self.assertIn("control_pair_manifest", audit.missing_tables)
        self.assertIn("perturbation_trial_log", audit.missing_tables)
        self.assertIn("demotion_decision_log", audit.missing_tables)

    def test_posthoc_complete_map_is_rejected_before_scoring(self) -> None:
        audit = audit_detector_stack_export_map(posthoc_augmented_time_tagging_map())

        self.assertEqual(audit.verdict, "inadmissible_for_detector_q1_upgrade")
        self.assertIn("not_a_pre_data_deployment_plan", audit.failure_reasons)
        self.assertIn("required_tables_not_preregistered", audit.failure_reasons)
        self.assertEqual(set(audit.posthoc_tables), set(REQUIRED_TABLE_COLUMNS))

    def test_dashboard_summary_control_remains_rejected(self) -> None:
        audit = audit_detector_stack_export_map(dashboard_summary_export_map())

        self.assertEqual(audit.verdict, "inadmissible_for_detector_q1_upgrade")
        self.assertIn("not_a_pre_data_deployment_plan", audit.failure_reasons)
        self.assertIn("not_locked_to_t87_schema", audit.failure_reasons)
        self.assertIn("missing_required_t87_tables", audit.failure_reasons)
        self.assertEqual(audit.instrument_native_tables, ())

    def test_run_result_preserves_no_empirical_upgrade_boundary(self) -> None:
        result = run_t95_analysis()

        self.assertIn("feasible only as an augmented", result.strongest_claim)
        self.assertIn("not natively satisfy", result.weakened)
        self.assertIn("No real event rows exist", result.open_blocker)
        self.assertIn("without adding fields after the run", result.q1_update)


if __name__ == "__main__":
    unittest.main()
