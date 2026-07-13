"""Tests for T546 APRD functoriality and naturality packet."""

from __future__ import annotations

import json
import unittest

from models import t545_aprd_refinement_stability_packet as t545
from models import t546_aprd_functoriality_naturality_packet as t546


class APRDFunctorialityNaturalityPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t546.run_t546_analysis()
        cls.payload = t546.t546_result_to_dict(cls.result)
        cls.morphisms = {
            evaluation.case_id: evaluation
            for evaluation in cls.result.morphism_evaluations
        }
        cls.composites = {
            evaluation.case_id: evaluation
            for evaluation in cls.result.composite_evaluations
        }

    def test_artifact_identity_and_t545_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t546.ARTIFACT)
        self.assertEqual(self.result.verdict, t546.VERDICT)
        self.assertEqual(
            self.result.aprd_functoriality_status,
            t546.APRD_FUNCTORIALITY_STATUS,
        )
        self.assertEqual(self.result.source_t545_verdict, t545.VERDICT)
        self.assertEqual(self.result.source_t545_status, t545.APRD_STABILITY_STATUS)

    def test_functoriality_definition_names_naturality_and_failure_boundaries(self) -> None:
        natural_when = set(self.payload["functoriality_definition"]["natural_when"])
        not_natural = set(self.payload["functoriality_definition"]["not_natural"])

        self.assertIn("identity_morphisms_preserve_aprd_assignment", natural_when)
        self.assertIn("native_pullback_preserves_source_debt_set", natural_when)
        self.assertIn("declared_composites_equal_direct_pullback", natural_when)
        self.assertIn("non_native_cross_domain_morphism", not_natural)
        self.assertIn("composite_pullback_mismatch", not_natural)
        self.assertIn("outcome_selected_target_repair", not_natural)

    def test_identity_and_native_morphism_pullbacks_are_natural(self) -> None:
        expected_natural = {
            "identity_t51_t58_debt_object",
            "identity_t19_external_witness",
            "t51_native_relabel_pullback_natural",
            "record_transport_relabel_pullback_natural",
            "record_transport_support_preserving_restriction_natural",
        }

        self.assertTrue(expected_natural.issubset(set(self.result.natural_morphism_cases)))
        for case_id in expected_natural:
            evaluation = self.morphisms[case_id]
            self.assertEqual(evaluation.classification, "natural_aprd_morphism")
            self.assertEqual(evaluation.pulled_back_debt_ids, evaluation.source_debt_ids)
            self.assertTrue(evaluation.natural)

    def test_declared_composites_equal_direct_pullback(self) -> None:
        expected_functorial = {
            "record_transport_two_step_restriction_composite",
            "t51_relabel_then_identity_composite",
        }

        self.assertEqual(set(self.result.functorial_composite_cases), expected_functorial)
        for case_id in expected_functorial:
            evaluation = self.composites[case_id]
            self.assertEqual(
                evaluation.classification,
                "functorial_composite_preserved",
            )
            self.assertEqual(
                evaluation.composed_pullback_debt_ids,
                evaluation.direct_pullback_debt_ids,
            )
            self.assertEqual(evaluation.direct_pullback_debt_ids, evaluation.source_debt_ids)
            self.assertTrue(evaluation.functorial)

    def test_support_losing_morphism_narrows_without_promotion(self) -> None:
        evaluation = self.morphisms["t19_support_losing_morphism_narrows"]

        self.assertEqual(
            evaluation.classification,
            "narrowed_by_support_losing_morphism",
        )
        self.assertFalse(evaluation.natural)
        self.assertTrue(evaluation.narrowed)
        self.assertIn(evaluation.case_id, self.result.narrowed_cases)

    def test_hostile_functoriality_controls_reject(self) -> None:
        expected_rejections = {
            "hostile_non_native_t19_to_transport_map": "rejected_non_native_morphism",
            "hostile_hidden_support_change_as_natural": "rejected_hidden_support_change",
            "hostile_unmapped_target_debt": "rejected_unmapped_target_debt",
            "hostile_outcome_selected_target_repair": (
                "rejected_outcome_selected_target_repair"
            ),
            "hostile_composite_drops_provenance": "rejected_composite_mismatch",
        }

        self.assertTrue(set(expected_rejections).issubset(set(self.result.rejected_controls)))
        for case_id, classification in expected_rejections.items():
            if case_id in self.morphisms:
                evaluation = self.morphisms[case_id]
            else:
                evaluation = self.composites[case_id]
            self.assertEqual(evaluation.classification, classification)
            self.assertTrue(evaluation.rejected)

    def test_controls_all_pass_and_next_route_is_held_out_prediction(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        self.assertIn(t546.NEXT_PACKET, self.result.recommended_next)
        self.assertIn("held-out predictive pressure", self.result.taf11_update)
        self.assertIn("TAF4 remains blocked", self.result.taf4_update)
        self.assertIn("not as a shadow-protection transfer theorem", self.result.taf8_update)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t546.render_markdown(self.payload)

        self.assertIn("T546 Results", markdown)
        self.assertIn("Functoriality Definition", markdown)
        forbidden = (
            "source law established",
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
