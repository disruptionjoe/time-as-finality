"""Tests for T96: detector feasibility checklist."""

from __future__ import annotations

import unittest

from models.detector_feasibility_checklist import (
    audit_detector_feasibility,
    run_t96_analysis,
    t75_t87_t95_feasibility_checklist,
)
from models.real_run_raw_log_contract import REQUIRED_TABLE_COLUMNS


class DetectorFeasibilityChecklistTests(unittest.TestCase):
    def test_checklist_covers_every_t87_table(self) -> None:
        checklist = t75_t87_t95_feasibility_checklist()

        self.assertEqual(
            {item.table_name for item in checklist.items},
            set(REQUIRED_TABLE_COLUMNS),
        )

    def test_only_event_timing_is_native_to_named_stack(self) -> None:
        audit = audit_detector_feasibility(t75_t87_t95_feasibility_checklist())

        self.assertEqual(audit.native_tables, ("event_time_tag_stream",))
        self.assertEqual(
            set(audit.middleware_tables),
            {"signature_verification_log", "ancestry_dag_edge_export"},
        )

    def test_route_is_governance_heavy_and_blocked_on_controls(self) -> None:
        audit = audit_detector_feasibility(t75_t87_t95_feasibility_checklist())

        self.assertEqual(
            audit.route_status,
            "feasible_as_governance_heavy_dry_run_only",
        )
        self.assertEqual(
            set(audit.custom_control_tables),
            {
                "control_pair_manifest",
                "tag_ambiguity_challenge_log",
                "perturbation_trial_log",
            },
        )
        self.assertEqual(
            set(audit.governance_tables),
            {
                "preregistration_manifest",
                "trust_boundary_audit_log",
                "demotion_decision_log",
            },
        )
        self.assertEqual(
            set(audit.blocker_tables),
            {
                "control_pair_manifest",
                "tag_ambiguity_challenge_log",
                "perturbation_trial_log",
                "demotion_decision_log",
            },
        )

    def test_run_result_preserves_record_governance_reading(self) -> None:
        result = run_t96_analysis()

        self.assertIn("governance-heavy dry-run protocol", result.strongest_claim)
        self.assertIn("Only one required T87 table is native", result.weakened)
        self.assertIn("no locked dry-run packet with real rows", result.open_blocker)
        self.assertIn("dry-run admissibility program", result.q1_update)


if __name__ == "__main__":
    unittest.main()
