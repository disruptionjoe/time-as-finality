"""Tests for T78: pre-registered detector deployment protocol."""

from __future__ import annotations

import unittest

from models.preregistered_detector_deployment_protocol import (
    REQUIRED_CONTROL_ROLES,
    REQUIRED_EVIDENCE_FIELDS,
    REQUIRED_RAW_LOG_SOURCES,
    audit_preregistration,
    complete_lab_preregistration,
    fixture_only_preregistration,
    missing_unsigned_control_preregistration,
    permissive_policy_preregistration,
    posthoc_policy_preregistration,
    run_t78_analysis,
)


class PreregisteredDetectorDeploymentProtocolTests(unittest.TestCase):
    def test_complete_plan_is_admissible_for_real_deployment_audit(self) -> None:
        audit = audit_preregistration(complete_lab_preregistration())

        self.assertEqual(audit.verdict, "admissible_for_real_deployment_audit")
        self.assertEqual(audit.failure_reasons, ())
        self.assertEqual(audit.missing_evidence_fields, ())
        self.assertEqual(audit.missing_control_roles, ())
        self.assertEqual(audit.missing_raw_log_sources, ())
        self.assertEqual(audit.next_allowed_audit, "run_t76_t77_on_real_log")

    def test_required_schema_matches_t76_deployment_evidence_fields(self) -> None:
        plan = complete_lab_preregistration()

        self.assertGreaterEqual(len(REQUIRED_EVIDENCE_FIELDS), 19)
        self.assertTrue(set(REQUIRED_EVIDENCE_FIELDS).issubset(plan.evidence_fields))
        self.assertTrue(set(REQUIRED_CONTROL_ROLES).issubset(plan.control_roles))
        self.assertTrue(set(REQUIRED_RAW_LOG_SOURCES).issubset(plan.raw_log_sources))

    def test_posthoc_policy_is_rejected_even_with_complete_fields(self) -> None:
        audit = audit_preregistration(posthoc_policy_preregistration())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("policy_chosen_after_data", audit.failure_reasons)
        self.assertEqual(audit.missing_evidence_fields, ())

    def test_missing_timing_matched_unsigned_control_is_rejected(self) -> None:
        audit = audit_preregistration(missing_unsigned_control_preregistration())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn(
            "timing_only_unsigned_negative_control",
            audit.missing_control_roles,
        )
        self.assertIn("missing_required_negative_controls", audit.failure_reasons)

    def test_fixture_only_counts_do_not_upgrade_detector_branch(self) -> None:
        audit = audit_preregistration(fixture_only_preregistration())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("fixture_counts_only", audit.failure_reasons)
        self.assertIn("no_real_raw_deployment_log", audit.failure_reasons)

    def test_t77_permissive_policy_corridor_is_rejected(self) -> None:
        audit = audit_preregistration(permissive_policy_preregistration())

        self.assertEqual(audit.verdict, "inadmissible_for_q1_upgrade")
        self.assertIn("policy_outside_t77_safe_corridor", audit.failure_reasons)

    def test_result_weakens_q1_to_real_log_preregistration_gate(self) -> None:
        result = run_t78_analysis()

        self.assertIn("pre-data gate", result.strongest_claim)
        self.assertIn("Fixture counts", result.weakened_claim)
        self.assertIn("real-log", result.q1_update)
        self.assertIn("No real deployment log", result.blocker)


if __name__ == "__main__":
    unittest.main()
