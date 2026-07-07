"""Tests for T501 typed translation / object-identity stack gate."""

from __future__ import annotations

import json
import unittest

from models.typed_translation_object_identity_stack_gate import run


class TypedTranslationObjectIdentityStackGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_actual_t92_t113_bridge_is_schema_only(self) -> None:
        actual = self.decisions["t92_t113_schema_translation"]

        self.assertEqual(
            self.payload["verdict"],
            "TYPED_TRANSLATION_OBJECT_IDENTITY_STACK_BUILT_SCHEMA_PRESERVATION_ONLY",
        )
        self.assertTrue(actual["admitted"])
        self.assertEqual(
            actual["label"],
            "COMPOSITE_ABSORBER_EXPLANATION_SCHEMA_TRANSLATION_ONLY",
        )
        self.assertTrue(actual["interface_preserved"])
        self.assertFalse(actual["object_identity_passes"])
        self.assertFalse(actual["direct_preservation_passes"])
        self.assertFalse(actual["residual_survives_stack"])

    def test_object_identity_overread_is_rejected(self) -> None:
        overread = self.decisions["same_object_identity_overread"]

        self.assertFalse(overread["admitted"])
        self.assertEqual(overread["label"], "REJECTED_OBJECT_IDENTITY_CRITERION_FAILS")
        self.assertTrue(overread["interface_preserved"])
        self.assertFalse(overread["object_identity_passes"])

    def test_raw_h0_and_relabeling_shortcuts_are_rejected(self) -> None:
        raw = self.decisions["raw_h0_classifier_overread"]
        relabel = self.decisions["semantic_relabeling_identity"]
        gauge = self.decisions["gauge_coordinate_choice_identity"]

        self.assertFalse(raw["admitted"])
        self.assertEqual(raw["label"], "REJECTED_RAW_H0_CLASSIFIER_REVIVAL")
        self.assertFalse(relabel["admitted"])
        self.assertEqual(relabel["label"], "REJECTED_SEMANTIC_RELABELING_IDENTITY")
        self.assertFalse(gauge["admitted"])
        self.assertEqual(gauge["label"], "REJECTED_GAUGE_COORDINATE_IDENTITY")

    def test_promotion_shortcuts_are_blocked(self) -> None:
        torsion = self.decisions["cohomology_physical_torsion_shortcut"]
        consciousness = self.decisions["consciousness_complexity_shortcut"]
        posture = self.decisions["claim_public_posture_shortcut"]

        self.assertFalse(torsion["admitted"])
        self.assertEqual(
            torsion["label"],
            "REJECTED_COHOMOLOGY_OR_PHYSICAL_TORSION_SHORTCUT",
        )
        self.assertFalse(consciousness["admitted"])
        self.assertEqual(
            consciousness["label"],
            "REJECTED_CONSCIOUSNESS_OR_COMPLEXITY_SHORTCUT",
        )
        self.assertFalse(posture["admitted"])
        self.assertEqual(posture["label"], "BLOCKED_GOVERNANCE_OR_EXTERNAL_SHORTCUT")
        self.assertIn("claim_or_public_posture", posture["blocked_shortcuts"])
        self.assertIn("external_publication", posture["blocked_shortcuts"])
        self.assertIn("cross_repo_truth", posture["blocked_shortcuts"])

    def test_incomplete_stack_is_rejected(self) -> None:
        incomplete = self.decisions["incomplete_schema_only_packet"]

        self.assertFalse(incomplete["admitted"])
        self.assertEqual(incomplete["label"], "REJECTED_INCOMPLETE_TRANSLATION_STACK")
        self.assertIn("relabeling_quotient", incomplete["missing_layers"])
        self.assertIn("object_identity_criterion", incomplete["missing_layers"])
        self.assertIn("gauge_coordinate_quotient", incomplete["missing_layers"])

    def test_synthetic_exact_object_packet_is_review_only(self) -> None:
        synthetic = self.decisions["synthetic_exact_object_preservation_packet"]

        self.assertTrue(synthetic["admitted"])
        self.assertEqual(
            synthetic["label"],
            "ADMITTED_FUTURE_REVIEW_TARGET_OBJECT_IDENTITY_AND_RESIDUAL",
        )
        self.assertTrue(synthetic["object_identity_passes"])
        self.assertTrue(synthetic["direct_preservation_passes"])
        self.assertTrue(synthetic["residual_survives_stack"])
        self.assertEqual(synthetic["action"], "review_only")

    def test_typed_systems_keep_t92_t113_distinct(self) -> None:
        systems = self.payload["systems"]

        self.assertNotEqual(
            systems["t113_order_pair"]["carrier_kind"],
            systems["t92_unary_proposition"]["carrier_kind"],
        )
        self.assertNotEqual(
            systems["t113_order_pair"]["target_kind"],
            systems["t92_unary_proposition"]["target_kind"],
        )
        self.assertEqual(
            systems["t113_order_pair"]["schema_slots"],
            systems["t92_unary_proposition"]["schema_slots"],
        )

    def test_payload_is_json_serializable(self) -> None:
        dumped = json.dumps(self.payload)

        self.assertIn(
            "TYPED_TRANSLATION_OBJECT_IDENTITY_STACK_BUILT_SCHEMA_PRESERVATION_ONLY",
            dumped,
        )
        self.assertIn("t92_t113_schema_translation", dumped)


if __name__ == "__main__":
    unittest.main()
