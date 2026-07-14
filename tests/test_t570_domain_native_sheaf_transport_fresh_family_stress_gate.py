"""Tests for T570 fresh-family semantic-generator stress."""

from __future__ import annotations

import json
import unittest

from models import (
    t569_domain_native_sheaf_transport_independent_reimplementation_gate as t569,
)
from models import (
    t570_domain_native_sheaf_transport_fresh_family_stress_gate as t570,
)


class DomainNativeSheafTransportFreshFamilyStressGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t570.run_t570_analysis()
        cls.payload = t570.t570_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.candidate_id: evaluation for evaluation in cls.result.evaluations
        }
        cls.checks = {
            check.check_id: check for check in cls.result.closure_checks
        }
        cls.routes = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t570.ARTIFACT)
        self.assertEqual(self.result.verdict, t570.VERDICT)
        self.assertEqual(self.result.fresh_family_status, t570.FRESH_FAMILY_STATUS)
        self.assertEqual(self.result.source_law_status, t570.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t570.ROUTE_STATUS)
        self.assertEqual(self.result.source_t569_verdict, t569.VERDICT)
        self.assertEqual(self.result.source_t569_selected_next_packet, t569.NEXT_PACKET)
        self.assertTrue(self.result.source_t569_independent_reimplementation_cleared)

    def test_projection_recodes_roles_without_literal_source_fields(self) -> None:
        projection = self.result.fresh_family_projection
        fresh_fields = tuple(field for _, field in projection.source_role_to_fresh_field)

        self.assertEqual(projection.projection_id, "fresh_role_recoding_projection_v1")
        self.assertEqual(projection.source_contract_id, "semantic_source_variable_complete_holdout_generator_v2")
        self.assertEqual(projection.literal_source_variable_names_used_as_fields, ())
        self.assertEqual(len(set(fresh_fields)), len(fresh_fields))
        self.assertIn("certificate_window_cover", fresh_fields)
        self.assertTrue(self.checks["fresh_projection_changes_surface_vocabulary"].passed)
        self.assertTrue(self.gates["fresh_projection_not_literal_replay"].passed)

    def test_fresh_families_are_admitted(self) -> None:
        expected = (
            "calibration_chain_role_recoding_family",
            "archive_manifest_handoff_role_recoding_family",
        )

        self.assertEqual(self.result.admitted_family_ids, expected)
        for candidate_id in expected:
            with self.subTest(candidate_id=candidate_id):
                evaluation = self.evaluations[candidate_id]
                self.assertTrue(evaluation.fresh_family_admissible)
                self.assertTrue(evaluation.role_projection_complete)
                self.assertFalse(evaluation.literal_replay_rejected)
                self.assertEqual(evaluation.failed_checks, ())
        self.assertTrue(self.checks["fresh_families_admitted"].passed)

    def test_replay_semantic_target_and_completion_controls_reject(self) -> None:
        expected = (
            "same_family_surface_relabel_replay_control",
            "missing_transport_square_fresh_name_control",
            "target_geometry_import_family_control",
            "optional_payload_family_control",
            "absorber_complete_trivial_completion_control",
        )

        self.assertEqual(self.result.rejected_control_ids, expected)
        for candidate_id in expected:
            with self.subTest(candidate_id=candidate_id):
                evaluation = self.evaluations[candidate_id]
                self.assertFalse(evaluation.fresh_family_admissible)
        self.assertTrue(
            self.evaluations[
                "same_family_surface_relabel_replay_control"
            ].literal_replay_rejected
        )
        self.assertIn(
            "noncommuting_transport_square",
            self.evaluations["missing_transport_square_fresh_name_control"].failed_checks,
        )
        self.assertIn(
            "target_blind_language",
            self.evaluations["target_geometry_import_family_control"].failed_checks,
        )
        self.assertIn(
            "native_payload_forced",
            self.evaluations["optional_payload_family_control"].failed_checks,
        )
        self.assertTrue(self.checks["fresh_controls_rejected"].passed)
        self.assertTrue(self.checks["literal_replay_control_active"].passed)
        self.assertTrue(self.checks["semantic_and_target_controls_active"].passed)

    def test_source_law_not_earned_and_t571_selected(self) -> None:
        self.assertTrue(self.result.fresh_family_stress_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t570.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_MULTI_FAMILY_FALSIFIER_REQUIRED",
        )
        self.assertTrue(self.routes["run_multi_family_falsifier_rotation_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["multi_family_falsifier_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t570"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t570"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t571(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t570.render_markdown(self.payload)

        self.assertIn("T570 Results", markdown)
        self.assertIn("## Fresh-Family Projection", markdown)
        self.assertIn(t570.NEXT_PACKET, markdown)

    def test_json_serializable_and_avoids_forbidden_promotions(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        json.dumps(self.payload, sort_keys=True)
        self.assertIn("No claim-ledger update is earned", dumped)
        forbidden = (
            "source law proved",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
            "TAF8 theorem proved",
            "S1 promoted",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)


if __name__ == "__main__":
    unittest.main()
