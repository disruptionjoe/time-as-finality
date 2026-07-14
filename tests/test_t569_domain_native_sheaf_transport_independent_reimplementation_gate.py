"""Tests for T569 independent semantic-generator reimplementation."""

from __future__ import annotations

import json
import unittest

from models import (
    t568_domain_native_sheaf_transport_semantic_generator_strengthening_gate as t568,
)
from models import (
    t569_domain_native_sheaf_transport_independent_reimplementation_gate as t569,
)


class DomainNativeSheafTransportIndependentReimplementationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t569.run_t569_analysis()
        cls.payload = t569.t569_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.candidate_id: evaluation for evaluation in cls.result.evaluations
        }
        cls.checks = {
            check.check_id: check for check in cls.result.closure_checks
        }
        cls.routes = {
            decision.decision_id: decision
            for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t569.ARTIFACT)
        self.assertEqual(self.result.verdict, t569.VERDICT)
        self.assertEqual(
            self.result.reimplementation_status,
            t569.REIMPLEMENTATION_STATUS,
        )
        self.assertEqual(self.result.source_law_status, t569.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t569.ROUTE_STATUS)
        self.assertEqual(self.result.source_t568_verdict, t568.VERDICT)
        self.assertEqual(self.result.source_t568_selected_next_packet, t568.NEXT_PACKET)
        self.assertTrue(self.result.source_t568_semantic_generator_strengthened)

    def test_independent_spec_reconstructs_contract_without_fixture_labels(self) -> None:
        spec = self.result.independent_generator_spec

        self.assertEqual(spec.source_contract_id, "semantic_source_variable_complete_holdout_generator_v2")
        self.assertEqual(spec.semantic_requirements, t568.SEMANTIC_REQUIREMENTS)
        self.assertEqual(spec.fixture_label_fields_used, ())
        self.assertIn("uses no prior fixture label", spec.selection_rule)
        self.assertTrue(self.checks["independent_spec_uses_no_fixture_labels"].passed)

    def test_independent_selector_matches_contract_on_fresh_panel(self) -> None:
        self.assertTrue(all(item.selectors_match for item in self.result.evaluations))
        self.assertTrue(self.checks["contract_equivalence_on_fresh_panel"].passed)
        self.assertTrue(self.gates["contract_equivalence_matches"].passed)

    def test_fresh_native_holdouts_are_admitted(self) -> None:
        expected = (
            "escrow_window_rotation_holdout",
            "checkpoint_quorum_handoff_holdout",
        )

        self.assertEqual(self.result.admitted_candidate_ids, expected)
        for candidate_id in expected:
            with self.subTest(candidate_id=candidate_id):
                evaluation = self.evaluations[candidate_id]
                self.assertTrue(evaluation.independent_selector_admissible)
                self.assertTrue(evaluation.contract_selector_admissible)
                self.assertEqual(evaluation.failed_checks, ())
        self.assertTrue(self.checks["fresh_native_holdouts_admitted"].passed)

    def test_semantic_target_and_replay_controls_reject(self) -> None:
        expected = (
            "same_neighbor_trivial_gluing_control",
            "target_geometry_language_import_control",
            "payload_optional_near_miss_control",
            "fixture_label_alias_control",
        )

        self.assertEqual(self.result.rejected_control_ids, expected)
        for candidate_id in expected:
            with self.subTest(candidate_id=candidate_id):
                evaluation = self.evaluations[candidate_id]
                self.assertFalse(evaluation.independent_selector_admissible)
                self.assertFalse(evaluation.contract_selector_admissible)
        self.assertIn(
            "target_blind_language",
            self.evaluations["target_geometry_language_import_control"].failed_checks,
        )
        self.assertIn(
            "fixture_label_independent",
            self.evaluations["fixture_label_alias_control"].failed_checks,
        )
        self.assertTrue(self.checks["semantic_controls_rejected"].passed)
        self.assertTrue(self.checks["target_and_fixture_replay_controls_active"].passed)

    def test_source_law_not_earned_and_t570_selected(self) -> None:
        self.assertTrue(self.result.independent_reimplementation_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t569.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_FRESH_FAMILY_STRESS_REQUIRED",
        )
        self.assertTrue(self.routes["run_fresh_family_stress_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["fresh_family_stress_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t569"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t569"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t570(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t569.render_markdown(self.payload)

        self.assertIn("T569 Results", markdown)
        self.assertIn("## Independent Generator", markdown)
        self.assertIn(t569.NEXT_PACKET, markdown)

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
