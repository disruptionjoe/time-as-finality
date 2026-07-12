"""Tests for T533: C(R) surplus starter packet classifier."""

from __future__ import annotations

import json
import unittest

from models import t533_cr_surplus_starter_packet_classifier as t533


class CRSurplusStarterPacketClassifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t533.run()
        cls.rows = {
            item["packet_id"]: item
            for item in cls.result["classifications"]
        }

    def test_artifact_identity_and_floor(self) -> None:
        floor = self.result["absorber_floor"]

        self.assertEqual(self.result["artifact"], t533.ARTIFACT)
        self.assertEqual(self.result["verdict"], t533.VERDICT)
        self.assertEqual(self.result["sources"]["t500"], t533.SOURCE_T500)
        self.assertEqual(self.result["sources"]["t529"], t533.SOURCE_T529)
        self.assertTrue(floor["t500_current_full_stack_absorbed"])
        self.assertFalse(floor["t500_current_residual_survives_full_stack"])
        self.assertFalse(floor["t529_current_success"])
        self.assertFalse(floor["t529_claim_movement"])

    def test_required_negative_controls_are_rejected(self) -> None:
        simple = self.rows["simple_statistic_flatness_packet"]
        full = self.rows["full_profile_equivalent_task_success_packet"]
        declared = self.rows["declared_only_completion_packet"]
        resource = self.rows["resource_only_completion_packet"]

        self.assertFalse(simple["admitted"])
        self.assertEqual(simple["label"], "REJECTED_SIMPLE_STATISTIC_NOT_FULL_STACK_SURPLUS")
        self.assertFalse(full["admitted"])
        self.assertEqual(full["label"], "ABSORBED_FULL_PROFILE_EQUIVALENT_TASK_SUCCESS_COORDINATE")
        self.assertFalse(declared["admitted"])
        self.assertEqual(declared["label"], "REJECTED_DECLARED_ONLY_NO_REPRODUCIBLE_CERTIFICATES")
        self.assertFalse(resource["admitted"])
        self.assertEqual(resource["label"], "REJECTED_RESOURCE_ONLY_INCOMPLETE_COMPLETION_STACK")
        self.assertIn("full_competency_profile", resource["missing_layers"])
        self.assertIn("permission_profile", resource["missing_layers"])
        self.assertIn("provenance_profile", resource["missing_layers"])

    def test_profile_mismatch_and_post_hoc_witness_are_rejected(self) -> None:
        permission = self.rows["unmatched_permission_control_packet"]
        post_hoc = self.rows["post_hoc_noncompletion_packet"]

        self.assertFalse(permission["admitted"])
        self.assertEqual(permission["label"], "REJECTED_INCOMPLETE_COMPLETION_STACK")
        self.assertIn("permission_profile", permission["missing_layers"])
        self.assertFalse(post_hoc["admitted"])
        self.assertEqual(post_hoc["label"], "REJECTED_NONCOMPLETION_WITNESS_NOT_INDEPENDENT")
        self.assertTrue(post_hoc["stack_complete"])

    def test_single_synthetic_future_target_is_review_only(self) -> None:
        target = self.rows["synthetic_future_noncompletion_review_target"]

        self.assertTrue(target["admitted"])
        self.assertEqual(target["label"], "ADMITTED_SYNTHETIC_FUTURE_REVIEW_TARGET_NO_SUCCESS")
        self.assertEqual(target["action"], "review_only")
        self.assertTrue(target["stack_complete"])
        self.assertTrue(target["residual_survives_stack"])
        self.assertEqual(
            self.result["overall"]["admitted_packet_ids"],
            ["synthetic_future_noncompletion_review_target"],
        )
        self.assertTrue(self.result["overall"]["only_synthetic_future_target_admitted"])
        self.assertFalse(self.result["overall"]["current_c_r_success"])
        self.assertFalse(self.result["overall"]["surplus_over_full_stack_proved"])

    def test_governance_shortcuts_blocked(self) -> None:
        shortcut = self.rows["claim_or_public_posture_shortcut"]

        self.assertFalse(shortcut["admitted"])
        self.assertEqual(shortcut["label"], "BLOCKED_GOVERNANCE_OR_POSTURE_SHORTCUT")
        self.assertFalse(self.result["overall"]["claim_movement"])
        self.assertFalse(self.result["overall"]["canon_or_public_posture_movement"])
        self.assertFalse(self.result["overall"]["external_publication"])
        self.assertFalse(self.result["overall"]["cross_repo_truth_movement"])

    def test_claim_table_labels_computed_and_argued_claims(self) -> None:
        statuses = {item["status"] for item in self.result["claim_table"]}
        claims = {item["claim"]: item for item in self.result["claim_table"]}

        self.assertIn("COMPUTED", statuses)
        self.assertIn("ARGUED", statuses)
        self.assertEqual(
            claims["The synthetic future packet is admissible only as review-only and not as current success."]["confidence"],
            "high",
        )
        self.assertEqual(
            claims["This classifier is the right starter screen for TAF2 after T529."]["confidence"],
            "medium",
        )

    def test_json_serializable_and_forbidden_overreads_absent(self) -> None:
        dumped = json.dumps(self.result, sort_keys=True)

        self.assertIn(t533.VERDICT, dumped)
        banned = (
            "claim promotion follows",
            "C(R) success proved",
            "surplus over the full stack proved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for term in banned:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
