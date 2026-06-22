"""Tests for T174 forgotten-dims persistence-gap screen."""

from __future__ import annotations

import unittest

from models.ts_forgotten_dims_pg_screen import (
    PGScenario,
    audit_pg_scenario,
    generate_pg_trajectory,
    run_t174_analysis,
)


class ForgottenDimsPGScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t174_analysis()
        self.audits = {audit.scenario_id: audit for audit in self.result.audits}

    def test_scheduled_baseline_has_residual_pg(self) -> None:
        audit = self.audits["scheduled_persistence_baseline"]

        self.assertEqual(audit.micro_last_obstructed, 24)
        self.assertEqual(audit.meso_last_obstructed, 29)
        self.assertEqual(audit.holonic_last_obstructed, 34)
        self.assertEqual(audit.micro_relative_pg, 10)
        self.assertEqual(audit.inherited_meso_gap, 5)
        self.assertEqual(audit.residual_pg_after_lower_recovery, 5)
        self.assertEqual(audit.verdict, "scheduled_residual_pg_positive_control")

    def test_forgotten_dims_without_explicit_persistence_has_no_residual_pg(self) -> None:
        audit = self.audits["no_explicit_persistence_with_forgotten_dims"]

        self.assertEqual(audit.forgotten_dims, ("cross-level-recovery-detail",))
        self.assertEqual(audit.micro_relative_pg, 5)
        self.assertEqual(audit.inherited_meso_gap, 5)
        self.assertEqual(audit.residual_pg_after_lower_recovery, 0)
        self.assertFalse(audit.forgotten_dims_alone_generated_residual_pg)
        self.assertEqual(audit.verdict, "no_residual_pg_from_forgotten_dims")

    def test_no_forgotten_dims_control_has_no_residual_pg(self) -> None:
        audit = self.audits["no_forgotten_dims_control"]

        self.assertEqual(audit.forgotten_dims, ())
        self.assertEqual(audit.residual_pg_after_lower_recovery, 0)
        self.assertFalse(audit.residual_requires_explicit_retention)
        self.assertEqual(audit.verdict, "no_residual_pg_without_forgotten_dims")

    def test_explicit_retention_positive_control_generates_residual_pg(self) -> None:
        audit = self.audits["explicit_recovery_retention_positive_control"]

        self.assertEqual(audit.residual_pg_after_lower_recovery, 5)
        self.assertTrue(audit.residual_requires_explicit_retention)
        self.assertFalse(audit.forgotten_dims_alone_generated_residual_pg)
        self.assertEqual(audit.verdict, "explicit_retention_generates_residual_pg")

    def test_result_records_negative_boundary_without_claim_update(self) -> None:
        self.assertEqual(self.result.no_explicit_residual_pg, 0)
        self.assertEqual(self.result.no_explicit_micro_relative_pg, 5)
        self.assertIn("does not generate residual holonic persistence", self.result.strongest_result)
        self.assertEqual(
            self.result.claim_ledger_update,
            "None. T174 is a negative boundary screen, not a claim-status change.",
        )
        self.assertIn("MINI-GOAL-TS-003", self.result.suggested_next)

    def test_trajectory_rule_is_current_lower_only_for_no_explicit_case(self) -> None:
        scenario = PGScenario(
            scenario_id="unit_no_explicit",
            holonic_rule="propagate_current_lower",
            forgotten_dims=("detail",),
        )
        trajectory = generate_pg_trajectory(scenario)

        for step in trajectory:
            self.assertEqual(
                step.holonic_obstructed,
                step.micro_obstructed or step.meso_obstructed,
            )

    def test_audit_rejects_unknown_holonic_rule(self) -> None:
        scenario = PGScenario(scenario_id="bad", holonic_rule="unknown")

        with self.assertRaises(ValueError):
            audit_pg_scenario(scenario)


if __name__ == "__main__":
    unittest.main()
