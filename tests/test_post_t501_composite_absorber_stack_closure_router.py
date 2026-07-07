"""Tests for T502 post-T501 composite absorber-stack closure router."""

from __future__ import annotations

import json
import unittest

from models.post_t501_composite_absorber_stack_closure_router import run


class PostT501CompositeAbsorberStackClosureRouterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_closes_completed_stack_without_promotion(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "POST_T501_COMPOSITE_ABSORBER_STACK_CLOSED_NEW_EVIDENCE_ONLY",
        )
        self.assertTrue(self.payload["overall"]["all_five_lanes_executable"])
        self.assertTrue(self.payload["overall"]["current_stack_lanes_closed"])
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])
        self.assertFalse(self.payload["overall"]["cross_repo_truth_movement"])

    def test_all_prior_lane_anchors_are_preserved(self) -> None:
        anchors = self.payload["anchors"]["lanes"]

        self.assertTrue(anchors["bounded_retrieval"]["anchor_ok"])
        self.assertEqual(
            anchors["bounded_retrieval"]["verdict"],
            "BOUNDED_RETRIEVAL_SOURCE_CHECKED_STACK_BUILT_COMPOSITE_EXPLANATION",
        )
        self.assertTrue(anchors["authoritative_settlement"]["anchor_ok"])
        self.assertTrue(anchors["kappa_template"]["anchor_ok"])
        self.assertTrue(anchors["competency_resource_permission"]["anchor_ok"])
        self.assertTrue(anchors["typed_translation_identity"]["anchor_ok"])

    def test_minor_restarts_and_theorem_overreads_are_rejected(self) -> None:
        last2 = self.decisions["bounded_retrieval_last2_rerun"]
        theorem = self.decisions["bounded_retrieval_theorem_import_shortcut"]
        settlement = self.decisions["settlement_local_marker_residual_restart"]
        kappa = self.decisions["kappa_prediction_overread"]

        self.assertFalse(last2["admitted"])
        self.assertEqual(last2["route_label"], "REJECTED_COMPLETED_LANE_MINOR_RESTART")
        self.assertTrue(last2["closes_completed_lane"])

        self.assertFalse(theorem["admitted"])
        self.assertEqual(
            theorem["route_label"],
            "REJECTED_THEOREM_OR_PREDICTION_OVERREAD",
        )

        self.assertFalse(settlement["admitted"])
        self.assertEqual(
            settlement["route_label"],
            "REJECTED_COMPLETED_LANE_MINOR_RESTART",
        )

        self.assertFalse(kappa["admitted"])
        self.assertEqual(kappa["route_label"], "REJECTED_THEOREM_OR_PREDICTION_OVERREAD")

    def test_single_layer_schema_and_synthetic_control_overreads_are_rejected(self) -> None:
        cr = self.decisions["cr_single_statistic_restart"]
        identity = self.decisions["typed_gap_same_schema_identity_overread"]
        synthetic = self.decisions["synthetic_control_as_evidence_shortcut"]
        analogy = self.decisions["analogy_only_composite_packet"]

        self.assertFalse(cr["admitted"])
        self.assertEqual(cr["route_label"], "REJECTED_SINGLE_LAYER_STACK_RESTART")

        self.assertFalse(identity["admitted"])
        self.assertEqual(
            identity["route_label"],
            "REJECTED_OBJECT_IDENTITY_FROM_SCHEMA_OVERREAD",
        )

        self.assertFalse(synthetic["admitted"])
        self.assertEqual(synthetic["route_label"], "REJECTED_SYNTHETIC_CONTROL_OVERREAD")

        self.assertFalse(analogy["admitted"])
        self.assertEqual(analogy["route_label"], "REJECTED_ANALOGY_ONLY_RESTART")

    def test_governance_external_and_cross_repo_shortcuts_are_blocked(self) -> None:
        posture = self.decisions["claim_public_posture_shortcut"]
        external = self.decisions["external_cross_repo_shortcut"]

        self.assertFalse(posture["admitted"])
        self.assertEqual(posture["route_label"], "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT")
        self.assertFalse(posture["counts_as_claim_evidence"])

        self.assertFalse(external["admitted"])
        self.assertEqual(external["route_label"], "BLOCKED_EXTERNAL_OR_CROSS_REPO_SHORTCUT")
        self.assertFalse(external["counts_as_claim_evidence"])

    def test_future_lane_packets_are_review_only(self) -> None:
        expected = [
            (
                "future_bounded_retrieval_lower_bound_packet",
                "ADMIT_FUTURE_BOUNDED_RETRIEVAL_THEOREM_REVIEW_TARGET",
            ),
            (
                "future_authoritative_protocol_packet",
                "ADMIT_FUTURE_AUTHORITATIVE_PROTOCOL_REVIEW_TARGET",
            ),
            (
                "future_kappa_nonidentity_packet",
                "ADMIT_FUTURE_KAPPA_NONIDENTITY_REVIEW_TARGET",
            ),
            (
                "future_full_stack_cr_residual_packet",
                "ADMIT_FUTURE_FULL_STACK_CR_RESIDUAL_REVIEW_TARGET",
            ),
            (
                "future_exact_object_preservation_packet",
                "ADMIT_FUTURE_EXACT_OBJECT_PRESERVATION_REVIEW_TARGET",
            ),
        ]

        for packet_id, route in expected:
            decision = self.decisions[packet_id]
            self.assertTrue(decision["admitted"])
            self.assertEqual(decision["route_label"], route)
            self.assertTrue(decision["future_review_target"])
            self.assertFalse(decision["counts_as_claim_evidence"])
            self.assertEqual(decision["action"], "review_only")

    def test_future_target_set_is_exact(self) -> None:
        self.assertEqual(
            self.payload["overall"]["admitted_future_targets"],
            [
                "future_bounded_retrieval_lower_bound_packet",
                "future_authoritative_protocol_packet",
                "future_kappa_nonidentity_packet",
                "future_full_stack_cr_residual_packet",
                "future_exact_object_preservation_packet",
            ],
        )
        self.assertIn("bounded_retrieval_last2_rerun", self.payload["overall"]["rejected_packets"])
        self.assertIn("typed_gap_same_schema_identity_overread", self.payload["overall"]["rejected_packets"])

    def test_future_reopen_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_reopen_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn(
            "cite the completed lane anchor from T497, T498, T499, T500, or T501",
            minimum,
        )
        self.assertIn(
            "show controlled capability spread after the full stack or demote to composite explanation",
            minimum,
        )
        self.assertIn("kappa promotion", blocked)
        self.assertIn("same-object typed-gap identity", blocked)
        self.assertIn("external publication", blocked)

    def test_payload_is_json_serializable(self) -> None:
        dumped = json.dumps(self.payload)

        self.assertIn(
            "POST_T501_COMPOSITE_ABSORBER_STACK_CLOSED_NEW_EVIDENCE_ONLY",
            dumped,
        )
        self.assertIn("future_exact_object_preservation_packet", dumped)


if __name__ == "__main__":
    unittest.main()
