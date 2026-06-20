"""Tests for T98: detector operator-handoff audit."""

from __future__ import annotations

import unittest

from models.detector_operator_handoff_audit import (
    audit_operator_handoff,
    four_domain_cross_handoff_profile,
    independent_five_domain_profile,
    run_t98_analysis,
    three_person_small_lab_profile,
    two_person_pi_student_profile,
)


class DetectorOperatorHandoffAuditTests(unittest.TestCase):
    def test_independent_five_domain_profile_is_admissible(self) -> None:
        audit = audit_operator_handoff(independent_five_domain_profile())

        self.assertEqual(audit.verdict, "admissible_predata_handoff_profile")
        self.assertTrue(audit.independent_trust_auditor)
        self.assertEqual(audit.failure_reasons, ())
        self.assertEqual(audit.distinct_operator_count, 5)

    def test_four_domain_cross_handoff_profile_is_admissible(self) -> None:
        audit = audit_operator_handoff(four_domain_cross_handoff_profile())

        self.assertEqual(audit.verdict, "admissible_predata_handoff_profile")
        self.assertTrue(audit.independent_trust_auditor)
        self.assertEqual(audit.distinct_operator_count, 4)

    def test_three_person_profile_fails_on_self_audit_and_role_merge(self) -> None:
        audit = audit_operator_handoff(three_person_small_lab_profile())

        self.assertEqual(audit.verdict, "inadmissible_due_role_conflicts")
        self.assertIn("trust_auditor_not_independent", audit.failure_reasons)
        self.assertIn("governance_control_archive_role_merge", audit.failure_reasons)
        self.assertIn("archive_custodian", audit.self_audit_conflicts)
        self.assertIn(
            "analysis_governor=control_designer",
            audit.governance_conflicts,
        )

    def test_two_person_profile_fails_more_strongly(self) -> None:
        audit = audit_operator_handoff(two_person_pi_student_profile())

        self.assertEqual(audit.verdict, "inadmissible_due_role_conflicts")
        self.assertIn("analysis_governor", audit.self_audit_conflicts)
        self.assertIn("archive_custodian", audit.self_audit_conflicts)
        self.assertIn(
            "analysis_governor=archive_custodian",
            audit.governance_conflicts,
        )

    def test_run_result_keeps_detector_branch_operationally_narrow(self) -> None:
        result = run_t98_analysis()

        self.assertIn("four non-conflicting authority domains", result.strongest_claim)
        self.assertIn("self-certification", result.weakened)
        self.assertIn("independent trust auditor", result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()
