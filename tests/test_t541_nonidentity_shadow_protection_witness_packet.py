"""Tests for T541 nonidentity shadow-protection witness packet."""

from __future__ import annotations

import json
import unittest

from models import t541_nonidentity_shadow_protection_witness_packet as t541


class NonidentityShadowProtectionWitnessPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = t541.run_t541_analysis()
        cls.decisions = {
            decision["packet_id"]: decision for decision in cls.payload["decisions"]
        }

    def test_artifact_identity_and_boundaries(self) -> None:
        self.assertEqual(self.payload["artifact"], t541.ARTIFACT)
        self.assertEqual(self.payload["verdict"], t541.VERDICT)
        self.assertEqual(self.payload["theorem_status"], t541.THEOREM_STATUS)
        self.assertFalse(self.payload["overall"]["cross_domain_theorem_earned"])
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])

    def test_current_catalogue_pair_still_fails_theorem_burden(self) -> None:
        current = self.decisions["current_t499_t501_catalogue_pair"]

        self.assertEqual(current["decision"], "not_admitted")
        self.assertTrue(current["spine_passes"])
        self.assertFalse(current["kappa_nonidentity_passes"])
        self.assertFalse(current["typed_gap_transfer_passes"])
        self.assertIn("kappa_source_rank_not_fixed", current["blockers"])
        self.assertIn("kappa_native_witness_not_nonidentity", current["blockers"])
        self.assertIn(
            "typed_gap_direct_preservation_theorem_missing", current["blockers"]
        )

    def test_synthetic_packet_is_review_only(self) -> None:
        synthetic = self.decisions["synthetic_t466_t501_nonidentity_packet"]

        self.assertEqual(synthetic["decision"], "admitted_review_only")
        self.assertEqual(
            synthetic["route_label"],
            "SYNTHETIC_PACKET_SHAPE_ONLY_THEOREM_NOT_EARNED",
        )
        self.assertTrue(synthetic["spine_passes"])
        self.assertTrue(synthetic["kappa_nonidentity_passes"])
        self.assertTrue(synthetic["typed_gap_transfer_passes"])
        self.assertFalse(synthetic["theorem_ready"])
        self.assertTrue(self.payload["overall"]["synthetic_packet_admitted_review_only"])

    def test_domain_native_future_packet_is_theorem_review_only(self) -> None:
        future = self.decisions["domain_native_future_theorem_candidate"]

        self.assertEqual(future["decision"], "admitted_theorem_candidate")
        self.assertTrue(future["theorem_ready"])
        self.assertEqual(
            future["allowed_action"],
            "review theorem proof before any claim movement",
        )
        self.assertTrue(
            self.payload["overall"][
                "domain_native_future_packet_would_reach_theorem_review"
            ]
        )
        self.assertFalse(self.payload["overall"]["cross_domain_theorem_earned"])

    def test_identity_and_retuning_shortcuts_are_rejected(self) -> None:
        identity = self.decisions["identity_by_construction_shortcut"]
        retuned = self.decisions["retuned_missing_controls_pair"]

        self.assertEqual(identity["decision"], "rejected")
        self.assertIn("identity_by_construction", identity["blockers"])
        self.assertEqual(retuned["decision"], "not_admitted")
        self.assertEqual(retuned["route_label"], "PREDECLARED_SPINE_BURDEN_NOT_MET")
        self.assertIn("same_spine_not_predeclared", retuned["blockers"])
        self.assertIn("per_domain_retuning", retuned["blockers"])

    def test_governance_shortcut_blocks(self) -> None:
        shortcut = self.decisions["claim_public_posture_shortcut"]

        self.assertEqual(shortcut["decision"], "blocked")
        self.assertEqual(
            shortcut["route_label"], "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT"
        )
        self.assertIn("claim_movement_requested", shortcut["blockers"])
        self.assertIn("public_posture_requested", shortcut["blockers"])
        self.assertIn("external_publication_requested", shortcut["blockers"])

    def test_payload_and_markdown_avoid_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t541.render_markdown(self.payload)

        self.assertIn("T541 Results", markdown)
        self.assertIn("synthetic_t466_t501_nonidentity_packet", dumped)
        forbidden = (
            "cross-domain theorem proved",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
