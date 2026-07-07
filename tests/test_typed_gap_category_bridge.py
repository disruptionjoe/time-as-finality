"""Tests for T492 typed gap category bridge."""

from __future__ import annotations

import json
import unittest

from models.typed_gap_category_bridge import run, t492_result_to_dict


class TypedGapCategoryBridgeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run()
        self.evaluations = {
            item.candidate_id: item for item in self.result.candidate_evaluations
        }

    def test_common_minimal_schema_is_only_admitted_candidate(self) -> None:
        admitted = [item for item in self.result.candidate_evaluations if item.admitted]

        self.assertEqual(self.result.verdict, "COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED")
        self.assertEqual([item.candidate_id for item in admitted], ["common_minimal_typed_gap_schema"])
        self.assertEqual(admitted[0].label, "ADMITTED_COMMON_TYPED_GAP_SCHEMA_NO_IDENTITY")

    def test_t113_raw_h0_remains_refuted(self) -> None:
        self.assertEqual(self.result.t113_summary.carrier_kind, "nonreflexive_order_pair_sections")
        self.assertIn("refuted", self.result.t113_summary.raw_gap_status)
        self.assertIn("typed subobject", self.result.t113_summary.strongest_reading)

    def test_t92_remains_proposition_typed_and_conditional(self) -> None:
        self.assertEqual(self.result.t92_summary.carrier_kind, "unary_typed_proposition_sections")
        self.assertEqual(self.result.t92_summary.closure_status, "supported_with_explicit_boundaries")
        self.assertIn("does not identify", self.result.t92_summary.blocked_reading)

    def test_identity_and_raw_h0_overclaims_are_rejected(self) -> None:
        raw = self.evaluations["raw_h0_gap_identity"]
        identity = self.evaluations["same_section_object_identity"]

        self.assertFalse(raw.admitted)
        self.assertIn("RAW_H0_REFUTED_BY_T113", raw.label)
        self.assertFalse(identity.admitted)
        self.assertIn("CARRIER_MISMATCH", identity.label)

    def test_bad_promotion_controls_are_rejected(self) -> None:
        torsion = self.evaluations["cohomology_or_physical_torsion_promotion"]
        consciousness = self.evaluations["consciousness_or_complexity_promotion"]

        self.assertFalse(torsion.admitted)
        self.assertIn("COHOMOLOGY_TORSION_PROMOTION_BLOCKED", torsion.label)
        self.assertFalse(consciousness.admitted)
        self.assertIn("CONSCIOUSNESS_COMPLEXITY_PROMOTION_BLOCKED", consciousness.label)

    def test_t92_and_t113_boundary_controls_are_rejected(self) -> None:
        relabel = self.evaluations["semantic_relabeling_as_bridge"]
        reversal = self.evaluations["local_reversal_as_gap"]

        self.assertFalse(relabel.admitted)
        self.assertIn("CARRIER_MISMATCH", relabel.label)
        self.assertFalse(reversal.admitted)
        self.assertIn("RAW_H0_REFUTED_BY_T113", reversal.label)

    def test_result_payload_is_json_serializable(self) -> None:
        payload = t492_result_to_dict(self.result)
        dumped = json.dumps(payload)

        self.assertIn("COMMON_TYPED_GAP_SCHEMA_SUPPORTED_OBJECT_IDENTITY_BLOCKED", dumped)
        self.assertIn("common_minimal_typed_gap_schema", dumped)


if __name__ == "__main__":
    unittest.main()
