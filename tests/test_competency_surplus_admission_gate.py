"""Tests for T529 competency-surplus admission gate."""

from __future__ import annotations

import json
import unittest

from models import competency_surplus_admission_gate as t529


class CompetencySurplusAdmissionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t529.run()
        cls.evaluations = {
            item["packet_id"]: item
            for item in cls.result["packet_evaluations"]
        }

    def test_artifact_identity_and_absorber_floor(self) -> None:
        floor = self.result["absorber_floor"]

        self.assertEqual(self.result["artifact"], t529.ARTIFACT)
        self.assertEqual(self.result["overall_verdict"]["verdict"], t529.VERDICT)
        self.assertTrue(floor["t493_full_profile_absorbs_current_c_r"])
        self.assertEqual(floor["t493_same_resource_capability_splits"], [])
        self.assertEqual(floor["t493_distinct_c_r_profiles"], 12)
        self.assertTrue(floor["t493_statistics_flat_spans_all_profiles"])
        self.assertGreater(floor["t493_single_goal_collision_count"], 0)
        self.assertFalse(floor["t493_single_goal_absorbs_full_c_r"])
        self.assertTrue(floor["t494_primary_source_scope_checked"])

    def test_current_simple_statistics_surplus_is_review_only_not_competency_surplus(self) -> None:
        current = self.evaluations["current_t407_simple_statistics_surplus"]

        self.assertTrue(current["admitted"])
        self.assertEqual(
            current["label"],
            "ADMITTED_SIMPLE_STATISTICS_REVIEW_ONLY_NOT_COMPETENCY_SURPLUS",
        )
        self.assertEqual(current["action"], "keep_as_simple_statistics_review_target")
        self.assertFalse(
            self.result["overall_verdict"][
                "current_simple_statistics_surplus_is_competency_surplus"
            ]
        )

    def test_full_profile_and_weak_statistic_packets_are_rejected_or_absorbed(self) -> None:
        full = self.evaluations["full_competency_profile_equivalent"]
        weak = self.evaluations["weak_single_statistic_proxy"]

        self.assertFalse(full["admitted"])
        self.assertEqual(full["label"], "ABSORBED_BY_FULL_COMPETENCY_PROFILE")
        self.assertFalse(weak["admitted"])
        self.assertEqual(weak["label"], "ABSORBED_BY_FULL_COMPETENCY_PROFILE")

    def test_synthetic_future_target_requires_profile_match_and_independent_witness(self) -> None:
        target = self.evaluations["synthetic_competency_surplus_review_target"]
        post_hoc = self.evaluations["post_hoc_hidden_residual"]

        self.assertTrue(target["admitted"])
        self.assertEqual(
            target["label"],
            "ADMITTED_COMPETENCY_SURPLUS_FUTURE_REVIEW_TARGET",
        )
        self.assertTrue(
            self.result["overall_verdict"][
                "synthetic_future_review_target_admitted"
            ]
        )
        self.assertFalse(post_hoc["admitted"])
        self.assertEqual(post_hoc["label"], "REJECTED_POST_HOC_OR_UNWITNESSED_RESIDUAL")

    def test_source_mechanism_and_governance_shortcuts_blocked(self) -> None:
        unchecked = self.evaluations["unchecked_source_status_packet"]
        mechanism = self.evaluations["active_inference_mechanism_import"]
        shortcut = self.evaluations["claim_public_cross_repo_shortcut"]

        self.assertFalse(unchecked["admitted"])
        self.assertEqual(unchecked["label"], "REJECTED_UNCHECKED_COMPETENCY_SOURCE_STATUS")
        self.assertFalse(mechanism["admitted"])
        self.assertEqual(mechanism["label"], "REJECTED_EXTERNAL_MECHANISM_IMPORT")
        self.assertFalse(shortcut["admitted"])
        self.assertEqual(shortcut["label"], "BLOCKED_GOVERNANCE_OR_CROSS_REPO_SHORTCUT")

    def test_json_serializable_and_forbidden_movements_absent(self) -> None:
        dumped = json.dumps(self.result, sort_keys=True)

        self.assertIn(t529.VERDICT, dumped)
        self.assertFalse(self.result["overall_verdict"]["current_discriminator_success"])
        self.assertFalse(self.result["overall_verdict"]["claim_movement"])
        self.assertFalse(self.result["overall_verdict"]["canon_or_public_posture_movement"])
        self.assertFalse(self.result["overall_verdict"]["cross_repo_movement"])
        banned = (
            "claim promotion follows",
            "public posture authorized",
            "cross-repo support proved",
            "external publication authorized",
            "active inference imported",
            "competency surplus proved",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
