"""Tests for T475: observer-shadow bridge-review gate."""

from __future__ import annotations

import unittest

from models.observer_shadow_bridge_review_gate import (
    T475Result,
    run_t475_analysis,
    t475_result_to_dict,
)


class ObserverShadowBridgeReviewGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t475_analysis()
        cls.decisions = {
            decision.packet_id: decision for decision in cls.result.decisions
        }

    def test_run_returns_t475_result(self) -> None:
        self.assertIsInstance(self.result, T475Result)

    def test_verdict_is_review_metadata_only(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "BRIDGE_REVIEW_GATE_BUILT_REVIEW_METADATA_ONLY_NO_CATEGORY",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")
        self.assertTrue(self.result.t474_admitted_bridge_available)
        self.assertFalse(self.result.global_category_theorem_supported)

    def test_upstream_rejected_bridge_cannot_support_review(self) -> None:
        decision = self.decisions["no_admitted_bridge_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_upstream_bridge_not_admitted",
        )
        self.assertEqual(decision.classification, "upstream_bridge_rejection")

    def test_semantic_review_packet_is_rejected_upstream(self) -> None:
        decision = self.decisions["semantic_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_upstream_bridge_not_admitted",
        )

    def test_absorber_completion_review_is_rejected_upstream(self) -> None:
        decision = self.decisions["absorber_completion_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_upstream_bridge_not_admitted",
        )

    def test_control_incomplete_packet_is_rejected(self) -> None:
        decision = self.decisions["control_incomplete_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(decision.route_label, "reject_missing_review_controls")
        self.assertIn("no_bridge_hostile", decision.missing_review_controls)
        self.assertIn(
            "absorber_completion_hostile",
            decision.missing_review_controls,
        )

    def test_direct_composition_review_is_rejected(self) -> None:
        decision = self.decisions["direct_composition_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_direct_composition_or_category_review",
        )
        self.assertEqual(decision.classification, "direct_composition_rejection")
        self.assertFalse(decision.counts_as_category_evidence)

    def test_capability_identification_review_is_rejected(self) -> None:
        decision = self.decisions["capability_identification_review_packet"]
        self.assertFalse(decision.admitted)
        self.assertEqual(
            decision.route_label,
            "reject_capability_object_identification",
        )
        self.assertEqual(
            decision.classification,
            "capability_identification_rejection",
        )

    def test_audit_atlas_review_packet_is_admitted_as_metadata_only(self) -> None:
        decision = self.decisions["audit_atlas_review_packet"]
        self.assertTrue(decision.admitted)
        self.assertEqual(decision.route_label, "admit_review_metadata_only")
        self.assertTrue(decision.counts_as_cross_family_review)
        self.assertFalse(decision.counts_as_direct_composition)
        self.assertFalse(decision.counts_as_category_evidence)
        self.assertTrue(self.result.cross_family_review_supported)
        self.assertFalse(self.result.direct_cross_family_composition_supported)

    def test_only_audit_atlas_review_packet_is_admitted(self) -> None:
        self.assertEqual(
            self.result.admitted_review_packets,
            ("audit_atlas_review_packet",),
        )
        self.assertIn(
            "direct_composition_review_packet",
            self.result.rejected_review_packets,
        )

    def test_serializes_to_dict(self) -> None:
        payload = t475_result_to_dict(self.result)
        self.assertEqual(
            payload["artifact_id"],
            "T475-observer-shadow-bridge-review-gate-v0.1",
        )
        self.assertIn("packets", payload)
        self.assertIn("decisions", payload)
        self.assertTrue(payload["cross_family_review_supported"])
        self.assertFalse(payload["global_category_theorem_supported"])


if __name__ == "__main__":
    unittest.main()
