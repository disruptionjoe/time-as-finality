"""Tests for T544 APRD minimality and absorber separation gate."""

from __future__ import annotations

import json
import unittest

from models import t543_aprd_reconstruction_boundary_descent_packet as t543
from models import t544_aprd_minimality_absorber_separation_gate as t544


class APRDMinimalityAbsorberSeparationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t544.run_t544_analysis()
        cls.payload = t544.t544_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation for evaluation in cls.result.evaluations
        }

    def test_artifact_identity_and_t543_source_route(self) -> None:
        self.assertEqual(self.result.artifact, t544.ARTIFACT)
        self.assertEqual(self.result.verdict, t544.VERDICT)
        self.assertEqual(self.result.aprd_gate_status, t544.APRD_GATE_STATUS)
        self.assertEqual(self.result.source_t543_verdict, t543.VERDICT)
        self.assertEqual(self.result.source_t543_status, t543.APRD_STATUS)

    def test_gate_definition_keeps_aprd_set_valued_and_predeclared(self) -> None:
        properties = set(self.payload["gate_definition"]["required_properties"])

        self.assertIn("debt_object_fixed_before_outcomes", properties)
        self.assertIn("set_valued_debt_ids_not_scalar_rank", properties)
        self.assertIn("same_neighbor_data_completion_tested", properties)
        self.assertIn("at_least_one_non_detector_fixture_survives_completion", properties)
        self.assertIn("every_surviving_debt_atom_is_load_bearing", properties)

    def test_detector_absorber_remains_native_absorbed(self) -> None:
        detector = self.evaluations["t66_detector_threshold_absorber_control"]

        self.assertEqual(
            detector.classification,
            "native_absorbed_after_same_neighbor_completion",
        )
        self.assertTrue(detector.absorbed_by_native_completion)
        self.assertFalse(detector.non_detector_survivor)
        self.assertIn(detector.case_id, self.result.native_absorber_cases)

    def test_non_detector_minimal_survivors_clear(self) -> None:
        expected = {
            "t51_t58_observer_b_non_detector_separator",
            "t19_self_finality_external_witness_separator",
            "record_transport_same_rank_separator",
        }

        self.assertEqual(set(self.result.non_detector_survivors), expected)
        for case_id in expected:
            evaluation = self.evaluations[case_id]
            self.assertEqual(evaluation.classification, "minimal_nonabsorbed_separator")
            self.assertTrue(evaluation.minimal)
            self.assertTrue(evaluation.non_detector_survivor)
            self.assertEqual(
                set(evaluation.residual_debt_ids),
                set(evaluation.separation_requires),
            )

    def test_aprd_does_not_reduce_to_scalar_rank(self) -> None:
        t51 = self.evaluations["t51_t58_observer_b_non_detector_separator"]
        transport = self.evaluations["record_transport_same_rank_separator"]
        scalar = self.evaluations["scalar_rank_collapse_control"]

        self.assertEqual(t51.scalar_rank_signature, transport.scalar_rank_signature)
        self.assertNotEqual(t51.debt_ids, transport.debt_ids)
        self.assertTrue(self.result.same_rank_distinct_debt_pair_found)
        self.assertEqual(scalar.classification, "rejected_scalar_rank_collapse")

    def test_minimality_and_posthoc_controls_reject(self) -> None:
        padded = self.evaluations["padded_aprd_minimality_control"]
        posthoc = self.evaluations["post_hoc_outcome_leakage_control"]
        positive = self.evaluations["full_access_positive_control"]

        self.assertEqual(padded.classification, "rejected_nonminimal_padding")
        self.assertEqual(posthoc.classification, "rejected_post_hoc_outcome_leakage")
        self.assertEqual(positive.classification, "positive_control_no_debt")
        self.assertFalse(positive.residual_debt_ids)

    def test_controls_all_pass_and_next_route_is_refinement_stability(self) -> None:
        self.assertTrue(all(control.passed for control in self.result.controls))
        self.assertIn(t544.NEXT_PACKET, self.result.recommended_next)
        self.assertIn("refinement stability", self.result.taf11_update)
        self.assertIn("not a shadow-protection transfer theorem", self.result.taf8_update)

    def test_payload_and_markdown_do_not_move_governance_surfaces(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t544.render_markdown(self.payload)

        self.assertIn("T544 Results", markdown)
        self.assertIn("Gate Definition", markdown)
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
