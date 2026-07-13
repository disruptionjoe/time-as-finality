"""Tests for T547 APRD held-out prediction packet."""

from __future__ import annotations

import json
import unittest

from models import t546_aprd_functoriality_naturality_packet as t546
from models import t547_aprd_held_out_prediction_packet as t547


class APRDHeldOutPredictionPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t547.run_t547_analysis()
        cls.payload = t547.t547_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation for evaluation in cls.result.evaluations
        }

    def test_artifact_identity_and_t546_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t547.ARTIFACT)
        self.assertEqual(self.result.verdict, t547.VERDICT)
        self.assertEqual(
            self.result.aprd_prediction_status,
            t547.APRD_PREDICTION_STATUS,
        )
        self.assertEqual(self.result.source_t546_verdict, t546.VERDICT)
        self.assertEqual(
            self.result.source_t546_status,
            t546.APRD_FUNCTORIALITY_STATUS,
        )

    def test_prediction_definition_names_frozen_rule_and_shortcuts(self) -> None:
        frozen_rule = set(self.payload["prediction_definition"]["frozen_rule"])
        rejected_shortcuts = set(
            self.payload["prediction_definition"]["rejected_shortcuts"]
        )

        self.assertIn("read_required_support_before_target_label", frozen_rule)
        self.assertIn("do_not_read_actual_debt_ids_until_validation", frozen_rule)
        self.assertIn("do_not_retune_rules_after_target_fixture_selection", frozen_rule)
        self.assertIn("outcome_label_leakage", rejected_shortcuts)
        self.assertIn("proxy_label_reading", rejected_shortcuts)
        self.assertIn("finite_prediction_read_as_source_law", rejected_shortcuts)

    def test_clear_native_fixture_predicts_no_debt(self) -> None:
        evaluation = self.evaluations["heldout_record_transport_complete_clear"]

        self.assertEqual(
            evaluation.classification,
            "held_out_clear_prediction_matched",
        )
        self.assertEqual(evaluation.predicted_debt_ids, ())
        self.assertEqual(evaluation.actual_debt_ids, ())
        self.assertTrue(evaluation.accepted_prediction)
        self.assertTrue(evaluation.clear_prediction)

    def test_debt_bearing_native_fixtures_predict_debt(self) -> None:
        expected_predictions = {
            "heldout_record_transport_missing_certificate": (
                "missing:transport_compatibility_certificate",
            ),
            "heldout_t51_missing_provenance_record": (
                "missing:provenance_record:r_A_locked",
            ),
            "heldout_t19_missing_external_witness": (
                "missing:R_self_finality_external_witness",
            ),
        }

        self.assertEqual(set(self.result.debt_prediction_cases), set(expected_predictions))
        for case_id, expected_debt in expected_predictions.items():
            evaluation = self.evaluations[case_id]
            self.assertEqual(
                evaluation.classification,
                "held_out_debt_prediction_matched",
            )
            self.assertEqual(evaluation.predicted_debt_ids, expected_debt)
            self.assertEqual(evaluation.actual_debt_ids, expected_debt)
            self.assertTrue(evaluation.prediction_matched)
            self.assertTrue(evaluation.debt_prediction)

    def test_prediction_shortcut_controls_reject(self) -> None:
        expected_rejections = {
            "control_outcome_label_leakage": "rejected_outcome_label_leakage",
            "control_proxy_label_reading": "rejected_proxy_label_reading",
            "control_posthoc_retuning": "rejected_posthoc_retuning",
            "control_hidden_support_change": "rejected_hidden_support_change",
            "control_non_native_cross_family_fixture": (
                "rejected_non_native_heldout_fixture"
            ),
            "control_source_law_overclaim": "rejected_source_law_overclaim",
        }

        self.assertEqual(set(self.result.rejected_controls), set(expected_rejections))
        for case_id, classification in expected_rejections.items():
            evaluation = self.evaluations[case_id]
            self.assertEqual(evaluation.classification, classification)
            self.assertTrue(evaluation.rejected)

    def test_controls_all_pass_and_next_route_is_cross_family_stress(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        self.assertIn(t547.NEXT_PACKET, self.result.recommended_next)
        self.assertIn("cross-family stress", self.result.taf11_update)
        self.assertIn("TAF4 remains blocked", self.result.taf4_update)
        self.assertIn("not as a shadow-protection transfer theorem", self.result.taf8_update)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t547.render_markdown(self.payload)

        self.assertIn("T547 Results", markdown)
        self.assertIn("Prediction Definition", markdown)
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
