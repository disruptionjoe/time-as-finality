"""Tests for T178 detector preserved-rights successor policy screen."""

from __future__ import annotations

import unittest

from models.detector_preserved_rights_successor_policy_screen import (
    audit_successor_policy_profile,
    run_t178_analysis,
    successor_policy_profiles,
)


class DetectorPreservedRightsSuccessorPolicyScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t178_analysis()
        self.audits = {audit.profile_id: audit for audit in self.result.audits}
        self.profiles = {
            profile.profile_id: profile for profile in successor_policy_profiles()
        }

    def test_only_frozen_or_preserved_rights_successor_profiles_live(self) -> None:
        self.assertEqual(
            self.result.live_profiles,
            (
                "fully_frozen_no_successor_policy",
                "predeclared_preserved_rights_legal_hold_successor",
            ),
        )
        self.assertEqual(
            self.audits["fully_frozen_no_successor_policy"].classification,
            "live_frozen_without_successor",
        )
        self.assertEqual(
            self.audits["predeclared_preserved_rights_legal_hold_successor"].classification,
            "live_predeclared_preserved_rights_successor",
        )

    def test_undeclared_break_glass_successor_is_null(self) -> None:
        audit = self.audits["undeclared_break_glass_successor"]

        self.assertEqual(
            audit.classification,
            "null_unpredeclared_or_unlogged_successor",
        )
        self.assertFalse(audit.successor_predeclared)
        self.assertFalse(audit.immutable_transition_log)

    def test_review_pause_successor_is_null(self) -> None:
        audit = self.audits[
            "predeclared_release_pause_pending_governance_clearance"
        ]

        self.assertEqual(
            audit.classification,
            "null_successor_reduces_review_rights",
        )
        self.assertFalse(audit.preserves_review_access)

    def test_guardian_changing_successor_is_null(self) -> None:
        audit = self.audits["predeclared_escrow_rotation_successor"]

        self.assertEqual(
            audit.classification,
            "null_successor_changes_required_guardians",
        )
        self.assertFalse(audit.preserves_guardian_identity)

    def test_direct_and_wrapped_audits_match(self) -> None:
        profile = self.profiles["predeclared_preserved_rights_legal_hold_successor"]
        direct = audit_successor_policy_profile(profile)
        wrapped = self.audits["predeclared_preserved_rights_legal_hold_successor"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(
            direct.preserves_required_guardians,
            wrapped.preserves_required_guardians,
        )

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("Add T178 to Q1B", self.result.claim_ledger_update)
        self.assertIn("preserved-rights successor policy", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
