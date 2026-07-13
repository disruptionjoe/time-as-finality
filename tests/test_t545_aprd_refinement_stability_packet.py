"""Tests for T545 APRD refinement stability packet."""

from __future__ import annotations

import json
import unittest

from models import t544_aprd_minimality_absorber_separation_gate as t544
from models import t545_aprd_refinement_stability_packet as t545


class APRDRefinementStabilityPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t545.run_t545_analysis()
        cls.payload = t545.t545_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation for evaluation in cls.result.evaluations
        }

    def test_artifact_identity_and_t544_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t545.ARTIFACT)
        self.assertEqual(self.result.verdict, t545.VERDICT)
        self.assertEqual(self.result.aprd_stability_status, t545.APRD_STABILITY_STATUS)
        self.assertEqual(self.result.source_t544_verdict, t544.VERDICT)
        self.assertEqual(self.result.source_t544_status, t544.APRD_GATE_STATUS)

    def test_stability_definition_names_harmless_and_nonharmless_boundaries(self) -> None:
        stable_when = set(self.payload["stability_definition"]["stable_when"])
        not_stability = set(self.payload["stability_definition"]["not_stability"])

        self.assertIn("canonical_debt_set_preserved_by_harmless_refinement", stable_when)
        self.assertIn("canonical_debt_set_preserved_by_harmless_relabeling", stable_when)
        self.assertIn(
            "canonical_debt_set_preserved_by_declared_support_preserving_restriction",
            stable_when,
        )
        self.assertIn("support_loss_hidden_as_relabeling", not_stability)
        self.assertIn("scalar_rank_replacement", not_stability)

    def test_harmless_refinement_and_relabeling_preserve_canonical_debt_sets(self) -> None:
        expected_stable = {
            "t51_refinement_splits_ambient_debt",
            "t51_relabeling_renames_events",
            "t19_refinement_external_witness_cover",
            "record_transport_relabeling_certificate",
        }

        self.assertTrue(expected_stable.issubset(set(self.result.stable_cases)))
        for case_id in expected_stable:
            evaluation = self.evaluations[case_id]
            self.assertEqual(
                evaluation.classification,
                "stable_harmless_presentation",
            )
            self.assertEqual(evaluation.canonical_debt_ids, evaluation.source_debt_ids)
            self.assertTrue(evaluation.stable)

    def test_support_preserving_restriction_is_stable(self) -> None:
        evaluation = self.evaluations["record_transport_support_preserving_restriction"]

        self.assertEqual(
            evaluation.classification,
            "stable_support_preserving_restriction",
        )
        self.assertEqual(evaluation.canonical_debt_ids, evaluation.source_debt_ids)
        self.assertTrue(evaluation.stable)

    def test_support_losing_restriction_narrows_without_promotion(self) -> None:
        evaluation = self.evaluations["t19_support_losing_restriction_narrows"]

        self.assertEqual(
            evaluation.classification,
            "narrowed_by_nonharmless_restriction",
        )
        self.assertFalse(evaluation.stable)
        self.assertTrue(evaluation.narrowed_by_nonharmless_restriction)
        self.assertIn(evaluation.case_id, self.result.narrowed_cases)

    def test_hostile_controls_reject(self) -> None:
        expected_rejections = {
            "hostile_harmless_relabel_changes_debt": "rejected_unstable_harmless_transform",
            "hostile_refinement_adds_padding": "rejected_nonminimal_padding",
            "hostile_hidden_support_change": "rejected_hidden_support_change",
            "hostile_scalar_rank_replacement": "rejected_scalar_rank_collapse",
        }

        self.assertEqual(set(self.result.rejected_controls), set(expected_rejections))
        for case_id, classification in expected_rejections.items():
            evaluation = self.evaluations[case_id]
            self.assertEqual(evaluation.classification, classification)
            self.assertTrue(evaluation.rejected)

    def test_controls_all_pass_and_next_route_is_functoriality(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        self.assertIn(t545.NEXT_PACKET, self.result.recommended_next)
        self.assertIn("functorial naturality", self.result.taf11_update)
        self.assertIn("TAF4 remains blocked", self.result.taf4_update)
        self.assertIn("not as a shadow-protection transfer theorem", self.result.taf8_update)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t545.render_markdown(self.payload)

        self.assertIn("T545 Results", markdown)
        self.assertIn("Stability Definition", markdown)
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
