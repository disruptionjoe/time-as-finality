"""Tests for T161: detector control-root independence."""

from __future__ import annotations

import unittest

from models.detector_control_root_independence import (
    audit_control_root_profile,
    control_root_fixtures,
    run_t161_analysis,
)


class DetectorControlRootIndependenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t161_analysis()
        self.audits = {audit.profile_name: audit for audit in self.result.audits}
        self.fixtures = {profile.name: profile for profile in control_root_fixtures()}

    def test_distinct_critical_roots_preserve_admissibility(self) -> None:
        audit = self.audits["four_domain_distinct_critical_roots"]

        self.assertTrue(audit.nominal_admissible)
        self.assertTrue(audit.effective_admissible)
        self.assertEqual(audit.nominal_authority_count, 4)
        self.assertEqual(audit.effective_authority_count, 4)
        self.assertEqual(audit.shared_critical_roots, ())

    def test_shared_archive_and_audit_hsm_collapses_partition(self) -> None:
        audit = self.audits["five_domain_shared_archive_audit_hsm"]

        self.assertTrue(audit.nominal_admissible)
        self.assertFalse(audit.effective_admissible)
        self.assertLess(audit.effective_authority_count, audit.nominal_authority_count)
        self.assertIn("root_shared_archive_audit_hsm", audit.shared_critical_roots[0])
        self.assertIn("hidden_control_root_merge", audit.verdict)

    def test_shared_governance_archive_release_root_is_null(self) -> None:
        audit = self.audits["five_domain_shared_governance_archive_release_root"]

        self.assertTrue(audit.nominal_admissible)
        self.assertFalse(audit.effective_admissible)
        self.assertIn(
            "analysis_governor+archive_custodian",
            audit.shared_critical_roots[0],
        )

    def test_shared_noncritical_dashboard_does_not_collapse_partition(self) -> None:
        audit = self.audits["five_domain_shared_noncritical_dashboard"]

        self.assertTrue(audit.effective_admissible)
        self.assertEqual(audit.shared_critical_roots, ())
        self.assertIn("root_shared_dashboard", audit.ignored_noncritical_roots[0])

    def test_direct_and_wrapped_audits_match(self) -> None:
        profile = self.fixtures["four_domain_distinct_critical_roots"]
        direct = audit_control_root_profile(profile)
        wrapped = self.audits["four_domain_distinct_critical_roots"]

        self.assertEqual(direct.effective_partition, wrapped.effective_partition)
        self.assertEqual(direct.verdict, wrapped.verdict)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("authority labels are insufficient", self.result.strongest_claim)
        self.assertIn("control roots", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
