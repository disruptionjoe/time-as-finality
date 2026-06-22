"""Tests for T176 detector challenge-window freeze screen."""

from __future__ import annotations

import unittest

from models.detector_challenge_window_freeze_screen import (
    audit_challenge_window_freeze_profile,
    challenge_window_freeze_profiles,
    run_t176_analysis,
)


class DetectorChallengeWindowFreezeScreenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t176_analysis()
        self.audits = {audit.profile_id: audit for audit in self.result.audits}
        self.profiles = {
            profile.profile_id: profile for profile in challenge_window_freeze_profiles()
        }

    def test_frozen_policy_is_the_only_live_route(self) -> None:
        audit = self.audits["fully_frozen_challenge_window_policy"]

        self.assertEqual(
            audit.classification,
            "live_frozen_challenge_window_policy",
        )
        self.assertFalse(audit.challenge_window_mutable)
        self.assertEqual(
            self.result.live_frozen_profiles,
            ("fully_frozen_challenge_window_policy",),
        )

    def test_break_glass_release_override_is_null(self) -> None:
        audit = self.audits["governance_break_glass_release_override"]

        self.assertEqual(
            audit.classification,
            "null_mutable_challenge_window_rights",
        )
        self.assertIn("release_quorums", audit.mutable_targets)
        self.assertIn(
            "temporary_override_bypassing_archive_and_escrow",
            audit.mutable_effects,
        )

    def test_midwindow_escrow_replacement_is_null(self) -> None:
        audit = self.audits["midwindow_escrow_replacement"]

        self.assertEqual(
            audit.classification,
            "null_mutable_challenge_window_rights",
        )
        self.assertIn("guardian_roster", audit.mutable_targets)
        self.assertIn("trust_auditor", audit.mutable_authorities)

    def test_trust_suspension_is_null(self) -> None:
        audit = self.audits["trust_suspension_before_revocation"]

        self.assertEqual(
            audit.classification,
            "null_mutable_challenge_window_rights",
        )
        self.assertIn("revocation_quorums", audit.mutable_targets)
        self.assertIn("temporary_trust_suspension", audit.mutable_effects)

    def test_direct_and_wrapped_audits_match(self) -> None:
        profile = self.profiles["fully_frozen_challenge_window_policy"]
        direct = audit_challenge_window_freeze_profile(profile)
        wrapped = self.audits["fully_frozen_challenge_window_policy"]

        self.assertEqual(direct.classification, wrapped.classification)
        self.assertEqual(direct.mutable_targets, wrapped.mutable_targets)

    def test_result_language_keeps_q1b_blocked(self) -> None:
        self.assertIn("Q1B remains externally blocked", self.result.q1b_update)
        self.assertIn("pre-data challenge-window freeze", self.result.claim_ledger_update)
        self.assertIn("freeze policy", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
