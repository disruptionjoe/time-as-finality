"""Tests for T548 APRD cross-family prediction stress packet."""

from __future__ import annotations

import json
import unittest

from models import t547_aprd_held_out_prediction_packet as t547
from models import t548_aprd_cross_family_prediction_stress_packet as t548


class APRDCrossFamilyPredictionStressPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t548.run_t548_analysis()
        cls.payload = t548.t548_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation for evaluation in cls.result.evaluations
        }

    def test_artifact_identity_and_t547_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t548.ARTIFACT)
        self.assertEqual(self.result.verdict, t548.VERDICT)
        self.assertEqual(
            self.result.aprd_cross_family_status,
            t548.APRD_CROSS_FAMILY_STATUS,
        )
        self.assertEqual(self.result.source_t547_verdict, t547.VERDICT)
        self.assertEqual(
            self.result.source_t547_status,
            t547.APRD_PREDICTION_STATUS,
        )

    def test_stress_definition_names_no_retuning_boundary(self) -> None:
        success_requires = set(self.payload["stress_definition"]["success_requires"])

        self.assertIn("known_family_regression_still_matches", success_requires)
        self.assertIn("distinct_family_prediction_matches_without_new_rule", success_requires)
        self.assertIn("no_manual_family_rule_injection", success_requires)
        self.assertIn("no_cross_repo_truth_import", success_requires)
        self.assertIn("no_taf4_or_source_law_overread", success_requires)

    def test_known_family_regression_still_matches(self) -> None:
        evaluation = self.evaluations[
            "regression_t547_record_transport_missing_certificate"
        ]

        self.assertEqual(evaluation.classification, "known_family_regression_matched")
        self.assertEqual(
            evaluation.predicted_debt_ids,
            ("missing:transport_compatibility_certificate",),
        )
        self.assertEqual(evaluation.predicted_debt_ids, evaluation.actual_debt_ids)
        self.assertTrue(evaluation.known_family_regression)

    def test_distinct_candidate_families_narrow(self) -> None:
        expected_narrowed = {
            "stress_quantum_access_missing_shareability_witness",
            "stress_protocol_stack_missing_sybil_layer",
        }

        self.assertEqual(set(self.result.narrowed_cases), expected_narrowed)
        self.assertEqual(self.result.cross_family_survivors, ())
        for case_id in expected_narrowed:
            evaluation = self.evaluations[case_id]
            self.assertEqual(
                evaluation.classification,
                "narrowed_unknown_family_requires_native_rule",
            )
            self.assertEqual(
                evaluation.predicted_debt_ids,
                ("missing:unknown_native_family_rule",),
            )
            self.assertTrue(evaluation.narrowed)
            self.assertFalse(evaluation.cross_family_survivor)

    def test_cross_family_shortcut_controls_reject(self) -> None:
        expected_rejections = {
            "control_manual_family_rule_injection": "rejected_posthoc_family_rule_injection",
            "control_outcome_label_leakage": "rejected_outcome_label_leakage",
            "control_proxy_label_reading": "rejected_proxy_label_reading",
            "control_hidden_support_change": "rejected_hidden_support_change",
            "control_cross_repo_truth_import": "rejected_cross_repo_truth_import",
            "control_taf4_source_law_overread": "rejected_taf4_or_source_law_overread",
        }

        self.assertEqual(set(self.result.rejected_controls), set(expected_rejections))
        for case_id, classification in expected_rejections.items():
            evaluation = self.evaluations[case_id]
            self.assertEqual(evaluation.classification, classification)
            self.assertTrue(evaluation.rejected)

    def test_controls_all_pass_and_next_route_resets_taf11(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        self.assertIn(t548.NEXT_PACKET, self.result.recommended_next)
        self.assertIn("APRD is narrowed", self.result.taf11_update)
        self.assertIn("TAF4 remains blocked", self.result.taf4_update)
        self.assertIn("negative control", self.result.taf8_update)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t548.render_markdown(self.payload)

        self.assertIn("T548 Results", markdown)
        self.assertIn("Cross-family survivors: none", markdown)
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
