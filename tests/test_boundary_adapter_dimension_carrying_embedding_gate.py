"""Tests for T506 boundary-adapter dimension-carrying embedding gate."""

from __future__ import annotations

import json
import unittest

from models.boundary_adapter_dimension_carrying_embedding_gate import run


class BoundaryAdapterDimensionCarryingEmbeddingGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = run()
        self.decisions = {
            item["packet_id"]: item for item in self.payload["decisions"]
        }

    def test_verdict_and_scope_are_review_only(self) -> None:
        self.assertEqual(
            self.payload["verdict"],
            "DIMENSION_CARRYING_EMBEDDING_GATE_BUILT_REVIEW_ONLY",
        )
        self.assertTrue(self.payload["overall"]["review_target_only"])
        self.assertFalse(self.payload["overall"]["claim_movement"])
        self.assertFalse(self.payload["overall"]["public_posture_movement"])
        self.assertFalse(self.payload["overall"]["external_publication"])
        self.assertFalse(self.payload["overall"]["cross_repo_truth_movement"])
        self.assertFalse(self.payload["overall"]["sibling_repo_inspection"])
        self.assertFalse(self.payload["overall"]["current_two_adapter_gate_closed"])

    def test_flat_baseline_rejects_known_dimension_collapse(self) -> None:
        decision = self.decisions["flat_profile_baseline"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_FLAT_PROFILE_DIMENSION_COLLAPSE",
        )
        self.assertFalse(decision["dimension_collapse_blocked"])
        self.assertIn("W+->W+0", decision["spurious_morphisms"])
        self.assertTrue(
            self.payload["overall"]["flat_baseline_rejected_for_dimension_collapse"]
        )

    def test_exact_dimension_encoding_is_admitted_and_order_reflecting(self) -> None:
        decision = self.decisions["exact_dimension_carrying_embedding"]

        self.assertTrue(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "ADMITTED_DIMENSION_CARRYING_EMBEDDING_REVIEW_TARGET",
        )
        self.assertTrue(decision["order_reflects_full_poset"])
        self.assertTrue(decision["inclusions_preserved"])
        self.assertEqual(decision["spurious_morphisms"], ())
        self.assertEqual(decision["missing_inclusions"], ())
        self.assertTrue(
            self.payload["overall"]["exact_dimension_encoding_order_reflects_full_poset"]
        )

    def test_exact_dimension_encoding_blocks_pure_physical_dimension_collapse(self) -> None:
        decision = self.decisions["exact_dimension_carrying_embedding"]

        self.assertTrue(decision["dimension_collapse_blocked"])
        self.assertTrue(
            self.payload["overall"]["exact_dimension_encoding_blocks_wplus_to_wplus0"]
        )
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_exact_dimension_encoding_preserves_mirror_face_guard(self) -> None:
        decision = self.decisions["exact_dimension_carrying_embedding"]

        self.assertTrue(decision["mirror_face_protected"])
        self.assertTrue(decision["flat_baseline_control_present"])
        self.assertTrue(decision["physics_wrong_control_present"])

    def test_cardinality_only_control_is_rejected_for_face_collapse(self) -> None:
        decision = self.decisions["cardinality_only_physics_wrong_control"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_CARDINALITY_ONLY_FACE_COLLAPSE",
        )
        self.assertTrue(decision["dimension_collapse_blocked"])
        self.assertFalse(decision["mirror_face_protected"])
        self.assertIn("W-->W+0", decision["spurious_morphisms"])
        self.assertTrue(self.payload["overall"]["cardinality_only_control_rejected"])

    def test_noninjective_dimension_control_is_rejected(self) -> None:
        decision = self.decisions["noninjective_dimension_token_control"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "REJECTED_NONINJECTIVE_DIMENSION_ENCODING",
        )
        self.assertIn("injective_site_map", decision["missing_requirements"])
        self.assertFalse(decision["dimension_collapse_blocked"])
        self.assertTrue(
            self.payload["overall"]["noninjective_dimension_control_rejected"]
        )

    def test_posthoc_retyping_shortcut_is_rejected(self) -> None:
        decision = self.decisions["posthoc_retyping_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(decision["label"], "REJECTED_POSTHOC_DIMENSION_RETUNING")
        self.assertIn("predeclared_dimension_encoding", decision["missing_requirements"])

    def test_claim_and_cross_repo_shortcuts_are_blocked(self) -> None:
        decision = self.decisions["claim_cross_repo_shortcut"]

        self.assertFalse(decision["admitted"])
        self.assertEqual(
            decision["label"],
            "BLOCKED_CLAIM_OR_PUBLIC_POSTURE_SHORTCUT",
        )
        self.assertEqual(decision["action"], "stop")
        self.assertFalse(decision["counts_as_claim_evidence"])

    def test_future_minimum_and_not_earned_are_explicit(self) -> None:
        minimum = self.payload["future_dimension_packet_minimum"]
        blocked = self.payload["not_earned"]

        self.assertIn("predeclare dimension atoms before selecting the adapter target", minimum)
        self.assertIn("require injective site maps or an explicit no-many-to-one substitute", minimum)
        self.assertIn("real GU source category", blocked)
        self.assertIn("GU/TI/TaF adapter identity", blocked)
        self.assertIn("two-adapter gate closure", blocked)
        self.assertIn("cross-repo truth movement", blocked)

    def test_payload_is_json_serializable_without_forbidden_overreads(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn(
            "DIMENSION_CARRYING_EMBEDDING_GATE_BUILT_REVIEW_ONLY",
            dumped,
        )
        forbidden = (
            "adapter identity proven",
            "two-adapter gate closed",
            "real GU category established",
            "cross-repo truth established",
            "public posture authorized",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
