"""Tests for T540: cross-domain shadow-protection transfer gate."""

from __future__ import annotations

import json
import unittest

from models import kappa_composite_residual_template_gate as t499
from models import t540_cross_domain_shadow_protection_transfer_gate as t540
from models import typed_translation_object_identity_stack_gate as t501


class CrossDomainShadowProtectionTransferGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = t540.run_t540_analysis()
        cls.decisions = {
            decision["candidate_id"]: decision
            for decision in cls.payload["decisions"]
        }

    def test_artifact_identity_and_source_ceilings(self) -> None:
        self.assertEqual(self.payload["artifact"], t540.ARTIFACT)
        self.assertEqual(self.payload["verdict"], t540.VERDICT)
        self.assertEqual(
            self.payload["theorem_status"],
            "NOT_EARNED_CURRENT_CATALOGUES_NEED_NONIDENTITY_PACKET",
        )
        self.assertEqual(self.payload["source_summary"]["t499_verdict"], t499.VERDICT)
        self.assertEqual(self.payload["source_summary"]["t501_verdict"], t501.VERDICT)
        self.assertFalse(self.payload["source_summary"]["kappa_promotion_earned"])

    def test_current_catalogue_pair_is_scaffold_only(self) -> None:
        current = self.decisions["current_t499_t501_catalogue_pair"]

        self.assertEqual(current["decision"], "admitted_scaffold_only")
        self.assertTrue(current["scaffold_passes"])
        self.assertFalse(current["theorem_preconditions_pass"])
        self.assertIn("kappa_nonidentity_burden_not_cleared", current["blockers"])
        self.assertIn(
            "typed_gap_transfer_morphism_not_cleared", current["blockers"]
        )
        self.assertIn(
            "direct_spread_or_preservation_theorem_missing", current["blockers"]
        )
        self.assertTrue(self.payload["overall"]["current_catalogue_scaffold_passes"])
        self.assertFalse(
            self.payload["overall"]["current_catalogue_theorem_preconditions_pass"]
        )

    def test_identity_by_construction_is_rejected_even_when_other_fields_pass(self) -> None:
        shortcut = self.decisions["identity_by_construction_shortcut"]

        self.assertEqual(shortcut["decision"], "rejected")
        self.assertEqual(shortcut["route_label"], "IDENTITY_BY_CONSTRUCTION_BLOCKED")
        self.assertTrue(shortcut["scaffold_passes"])
        self.assertFalse(shortcut["theorem_preconditions_pass"])
        self.assertIn("identity_by_construction", shortcut["blockers"])

    def test_retuning_and_missing_native_controls_are_not_admitted(self) -> None:
        retuned = self.decisions["retuned_domain_specific_pair"]
        missing = self.decisions["missing_native_controls_pair"]

        self.assertEqual(retuned["decision"], "not_admitted")
        self.assertIn("same_proof_spine_missing", retuned["blockers"])
        self.assertIn("per_domain_retuning", retuned["blockers"])
        self.assertEqual(missing["decision"], "not_admitted")
        self.assertIn("positive_preservation_controls_missing", missing["blockers"])
        self.assertIn("negative_nonfactorization_fixtures_missing", missing["blockers"])
        self.assertIn("native_absorbers_not_granted", missing["blockers"])

    def test_synthetic_full_burden_pair_is_review_only(self) -> None:
        synthetic = self.decisions["synthetic_full_burden_pair"]

        self.assertEqual(synthetic["decision"], "admitted_future_review_target")
        self.assertEqual(synthetic["route_label"], "TAF8_THEOREM_PACKET_SHAPE_ONLY")
        self.assertTrue(synthetic["scaffold_passes"])
        self.assertTrue(synthetic["theorem_preconditions_pass"])
        self.assertEqual(tuple(synthetic["blockers"]), ())
        self.assertEqual(
            synthetic["allowed_action"],
            "future review target only; no claim movement",
        )
        self.assertTrue(
            self.payload["overall"]["synthetic_full_burden_admitted_for_review"]
        )

    def test_governance_shortcut_blocks_without_claim_movement(self) -> None:
        shortcut = self.decisions["claim_public_posture_shortcut"]

        self.assertEqual(shortcut["decision"], "blocked")
        self.assertEqual(
            shortcut["route_label"],
            "FORBIDDEN_GOVERNANCE_OR_EXTERNAL_SHORTCUT",
        )
        self.assertIn("claim_movement_requested", shortcut["blockers"])
        self.assertIn("public_posture_requested", shortcut["blockers"])
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])
        self.assertFalse(self.payload["overall"]["cross_repo_truth_movement"])

    def test_payload_and_markdown_report_no_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t540.render_markdown(self.payload)

        self.assertIn("T540 Results", markdown)
        self.assertIn("current_t499_t501_catalogue_pair", markdown)
        self.assertIn("T541_nonidentity_shadow_protection_witness_packet", dumped)
        forbidden = (
            "cross-domain theorem proved",
            "kappa promoted",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
        )
        for term in forbidden:
            self.assertNotIn(term, dumped)


if __name__ == "__main__":
    unittest.main()
