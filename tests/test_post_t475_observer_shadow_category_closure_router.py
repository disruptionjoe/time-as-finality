"""Tests for T476: post-T475 observer-shadow category closure router."""

from __future__ import annotations

import unittest

from models.post_t475_observer_shadow_category_closure_router import (
    T476Result,
    run_t476_analysis,
    t476_result_to_dict,
)


class PostT475ObserverShadowCategoryClosureRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t476_analysis()
        cls.decisions = {
            decision.proposal_id: decision for decision in cls.result.decisions
        }

    def test_run_returns_t476_result(self) -> None:
        self.assertIsInstance(self.result, T476Result)

    def test_verdict_closes_current_thread_without_promotion(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "POST_T475_OBSERVER_SHADOW_CATEGORY_THREAD_CLOSED_NEW_EVIDENCE_ONLY",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")
        self.assertTrue(self.result.t475_review_metadata_available)
        self.assertTrue(self.result.current_thread_closed)
        self.assertFalse(self.result.global_category_theorem_supported)

    def test_repeated_review_metadata_cannot_upgrade_to_category(self) -> None:
        decision = self.decisions["repeat_t475_review_metadata_upgrade"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_category_or_fibration_shortcut",
        )
        self.assertIn(
            "independent_direct_preservation_proof",
            decision.missing_requirements,
        )
        self.assertFalse(decision.counts_as_category_evidence)
        self.assertTrue(decision.closes_current_thread)

    def test_semantic_and_fibration_shortcuts_are_rejected(self) -> None:
        semantic = self.decisions["semantic_atlas_rename_restart"]
        self.assertFalse(semantic.admitted)
        self.assertEqual(semantic.route_label, "reject_semantic_restart")

        fibration = self.decisions["fibration_label_shortcut"]
        self.assertFalse(fibration.admitted)
        self.assertEqual(
            fibration.route_label,
            "reject_category_or_fibration_shortcut",
        )
        self.assertIn("formal_category_semantics", fibration.missing_requirements)

    def test_absorber_completion_and_capability_identification_are_rejected(self) -> None:
        absorber = self.decisions["absorber_completion_restart"]
        self.assertFalse(absorber.admitted)
        self.assertEqual(
            absorber.route_label,
            "reject_absorber_completion_restart",
        )

        identification = self.decisions["capability_identification_restart"]
        self.assertFalse(identification.admitted)
        self.assertEqual(
            identification.route_label,
            "reject_capability_identification_restart",
        )

    def test_incomplete_controls_are_rejected(self) -> None:
        decision = self.decisions["control_incomplete_minor_variant"]
        self.assertFalse(decision.admitted)
        self.assertEqual(decision.route_label, "reject_missing_reopen_requirements")
        self.assertIn("hostile_bridge_controls", decision.missing_requirements)

    def test_claim_and_public_posture_shortcut_is_blocked(self) -> None:
        decision = self.decisions["claim_posture_shortcut"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "block_governance_or_public_posture_shortcut",
        )
        self.assertEqual(decision.classification, "governance_boundary_block")

    def test_future_direct_preservation_target_is_admitted_for_review_only(self) -> None:
        decision = self.decisions["future_direct_preservation_theorem_packet"]
        self.assertTrue(decision.admitted)
        self.assertTrue(decision.admitted_as_future_review_target)
        self.assertEqual(
            decision.route_label,
            "admit_future_direct_preservation_review_target",
        )
        self.assertFalse(decision.counts_as_category_evidence)

    def test_future_new_family_target_is_admitted_for_review_only(self) -> None:
        decision = self.decisions["future_new_family_atlas_extension_packet"]
        self.assertTrue(decision.admitted)
        self.assertTrue(decision.admitted_as_future_review_target)
        self.assertEqual(
            decision.route_label,
            "admit_future_new_family_review_target",
        )
        self.assertFalse(decision.counts_as_category_evidence)

    def test_only_future_targets_are_admitted(self) -> None:
        self.assertEqual(
            self.result.admitted_future_targets,
            (
                "future_direct_preservation_theorem_packet",
                "future_new_family_atlas_extension_packet",
            ),
        )
        self.assertIn(
            "repeat_t475_review_metadata_upgrade",
            self.result.rejected_restart_packets,
        )

    def test_serializes_to_dict(self) -> None:
        payload = t476_result_to_dict(self.result)
        self.assertEqual(
            payload["artifact_id"],
            "T476-post-t475-observer-shadow-category-closure-router-v0.1",
        )
        self.assertIn("proposals", payload)
        self.assertIn("decisions", payload)
        self.assertTrue(payload["current_thread_closed"])
        self.assertFalse(payload["global_category_theorem_supported"])


if __name__ == "__main__":
    unittest.main()
