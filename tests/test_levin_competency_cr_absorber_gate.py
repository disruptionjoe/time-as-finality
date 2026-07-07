"""Tests for T493 Levin/Fields competency C(R) absorber gate."""

from __future__ import annotations

import json
import unittest

from models import levin_competency_cr_absorber_gate as t493


class LevinCompetencyCRAbsorberGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t493.run()
        cls.evaluations = {
            item["candidate_id"]: item
            for item in cls.result["candidate_evaluations"]
        }

    def test_artifact_identity_and_pointer_grade_source_status(self) -> None:
        self.assertEqual(self.result["artifact"], t493.ARTIFACT)
        self.assertEqual(self.result["overall_verdict"]["verdict"], t493.VERDICT)
        self.assertEqual(
            self.result["primary_source_status"],
            "not_checked_pointer_grade_only",
        )
        self.assertTrue(self.result["sources"]["n16"].endswith("N16-levin-competency-capability-neighbor.md"))
        self.assertIn("Calibration and absorber gate only", self.result["honest_ceiling"])

    def test_full_profile_absorbs_current_c_r_without_claim_promotion(self) -> None:
        full = self.evaluations["full_competency_profile_absorber"]
        audit = self.result["absorber_audit"]["full_profile_absorber"]
        profile = audit["profile_summary"]

        self.assertTrue(full["admitted"])
        self.assertEqual(full["label"], "ADMITTED_AS_FULL_PROFILE_ABSORBER_NO_CLAIM")
        self.assertTrue(audit["absorbs_current_c_r"])
        self.assertEqual(audit["same_resource_capability_splits"], [])
        self.assertEqual(profile["n_configurations"], 24)
        self.assertEqual(profile["n_distinct_profiles"], 12)
        self.assertTrue(profile["flat_statistics_spans_all_profiles"])
        self.assertEqual(
            self.result["claim_ledger_update"],
            "none; no claim promotion or demotion",
        )

    def test_single_goal_navigation_statistic_does_not_absorb_c_r(self) -> None:
        single_candidate = self.evaluations["single_goal_navigation_statistic"]
        single_audit = self.result["absorber_audit"]["single_goal_control"]

        self.assertFalse(single_candidate["admitted"])
        self.assertEqual(
            single_candidate["label"],
            "REJECTED_SINGLE_GOAL_STATISTIC_COLLIDES_WITH_C_R",
        )
        self.assertFalse(single_audit["single_goal_absorbs_full_c_r"])
        self.assertGreater(single_audit["collision_count"], 0)
        self.assertEqual(
            single_audit["collisions"][0]["split_task"],
            "undo_cross",
        )

    def test_zero_trace_surplus_is_review_only_not_novelty(self) -> None:
        zero = self.evaluations["t407_zero_trace_surplus_target"]
        review = self.result["absorber_audit"]["zero_trace_surplus_review"]

        self.assertTrue(zero["admitted"])
        self.assertEqual(
            zero["label"],
            "ADMITTED_REVIEW_TARGET_SIMPLE_STATISTICS_ONLY_NO_NOVELTY",
        )
        self.assertEqual(zero["action"], "keep_as_future_surplus_target")
        self.assertTrue(review["admitted_as_review_target"])
        self.assertFalse(review["novelty_claim_admitted"])
        self.assertLess(review["featured_pair_statistics_max_diff"], t493.TOL_EXACT)
        self.assertTrue(review["featured_pair_capability_incomparable"])

    def test_external_mechanism_public_posture_and_cross_repo_shortcuts_blocked(self) -> None:
        mechanism = self.evaluations["external_mechanism_import"]
        posture = self.evaluations["novelty_or_public_posture_shortcut"]
        cross_repo = self.evaluations["cross_repo_active_inference_absorber_update"]

        self.assertFalse(mechanism["admitted"])
        self.assertEqual(
            mechanism["label"],
            "REJECTED_EXTERNAL_MECHANISM_IMPORT_PRIMARY_SOURCES_UNCHECKED",
        )
        self.assertFalse(posture["admitted"])
        self.assertEqual(posture["label"], "BLOCKED_NOVELTY_PUBLIC_POSTURE_SHORTCUT")
        self.assertFalse(cross_repo["admitted"])
        self.assertEqual(cross_repo["label"], "BLOCKED_CROSS_REPO_TRUTH_UPDATE")

    def test_json_serializable_and_avoids_forbidden_promotions(self) -> None:
        dumped = json.dumps(self.result, sort_keys=True)

        self.assertIn(t493.VERDICT, dumped)
        banned = (
            "claim promotion follows",
            "region-indexed discriminator success proved",
            "novelty proved",
            "public posture authorized",
            "cross-repo support proved",
            "active inference imported",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
