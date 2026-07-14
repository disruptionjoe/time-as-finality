"""Tests for T566 domain-native sheaf transport typed generator gate."""

from __future__ import annotations

import json
import unittest

from models import t565_domain_native_sheaf_transport_predictive_holdout_gate as t565
from models import t566_domain_native_sheaf_transport_typed_generator_gate as t566


class DomainNativeSheafTransportTypedGeneratorGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t566.run_t566_analysis()
        cls.payload = t566.t566_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.case_id: evaluation
            for evaluation in cls.result.candidate_evaluations
        }
        cls.audits = {
            audit.audit_id: audit for audit in cls.result.generator_audits
        }
        cls.burdens = {
            burden.burden_id: burden for burden in cls.result.remaining_burdens
        }
        cls.routes = {
            decision.decision_id: decision
            for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t566.ARTIFACT)
        self.assertEqual(self.result.verdict, t566.VERDICT)
        self.assertEqual(self.result.generator_status, t566.GENERATOR_STATUS)
        self.assertEqual(self.result.source_law_status, t566.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t566.ROUTE_STATUS)
        self.assertEqual(self.result.source_t565_verdict, t565.VERDICT)
        self.assertEqual(self.result.source_t565_selected_next_packet, t565.NEXT_PACKET)
        self.assertTrue(self.result.source_t565_predictive_holdout_cleared)

    def test_generator_type_declares_all_required_fields(self) -> None:
        generator = self.result.generator_type

        self.assertEqual(generator.required_fields, t566.REQUIRED_GENERATOR_FIELDS)
        self.assertEqual(generator.required_source_variables, t565.FROZEN_SOURCE_VARIABLES)
        self.assertEqual(generator.required_absorber_ids, t565.FROZEN_ABSORBER_IDS)
        self.assertEqual(generator.forbidden_shortcuts, t565.FORBIDDEN_SHORTCUTS)
        self.assertIn("before outcome reading", generator.selection_rule)
        self.assertTrue(self.gates["generator_type_declared"].passed)
        self.assertTrue(self.audits["generator_type_declared"].passed)

    def test_generator_admits_only_complete_future_candidate(self) -> None:
        admitted = self.evaluations["new_multiphase_escrow_repair_holdout"]

        self.assertTrue(admitted.admissible)
        self.assertEqual(admitted.status, "ADMISSIBLE_TYPED_HOLDOUT_CANDIDATE")
        self.assertEqual(admitted.failed_checks, ())
        self.assertIn("source_variables_complete", admitted.passed_checks)
        self.assertIn("absorber_boundaries_complete", admitted.passed_checks)
        self.assertTrue(self.gates["future_candidate_admitted"].passed)
        self.assertTrue(self.audits["admits_complete_future_candidate"].passed)

    def test_generator_rejects_incomplete_shortcut_posthoc_and_replay_controls(self) -> None:
        expected_failures = {
            "missing_transport_square_control": "source_variables_complete",
            "target_import_shortcut_control": "forbidden_shortcuts_absent",
            "posthoc_outcome_reading_control": "predeclared_before_outcome_reading",
            "prior_fixture_replay_control": "not_prior_fixture_replay",
        }

        for case_id, failed_check in expected_failures.items():
            with self.subTest(case_id=case_id):
                evaluation = self.evaluations[case_id]
                self.assertFalse(evaluation.admissible)
                self.assertEqual(evaluation.status, "REJECTED_BY_TYPED_GENERATOR")
                self.assertIn(failed_check, evaluation.failed_checks)
        self.assertTrue(self.gates["controls_rejected"].passed)
        self.assertTrue(self.audits["rejects_incomplete_or_shortcut_candidates"].passed)

    def test_typed_generator_clears_review_packet_but_not_public_status(self) -> None:
        self.assertTrue(self.result.typed_source_generator_cleared)
        self.assertTrue(self.result.source_law_review_packet_complete)
        self.assertFalse(self.result.source_law_public_or_canon_status_earned)
        self.assertTrue(self.burdens["typed_source_generator"].cleared)
        self.assertTrue(self.burdens["source_law_review_packet"].cleared)
        self.assertTrue(self.burdens["hostile_review_before_governance_movement"].blocking)
        self.assertTrue(self.gates["review_packet_complete_not_promoted"].passed)

    def test_hostile_review_is_selected_next(self) -> None:
        self.assertTrue(self.routes["run_hostile_review_gate"].selected)
        self.assertEqual(
            self.routes["run_hostile_review_gate"].next_packet,
            t566.NEXT_PACKET,
        )
        self.assertEqual(self.result.selected_next_packet, t566.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_claim_or_canon_now"].outcome,
            "REJECTED_REVIEW_ONLY_PACKET",
        )
        self.assertTrue(self.gates["hostile_review_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_governance_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t566"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t566"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_hostile_controls_name_expected_failure_modes(self) -> None:
        self.assertIn("omits", self.controls["underdeclared_generator_control"].blocks)
        self.assertIn("target labels", self.controls["target_import_control"].blocks)
        self.assertIn("after reading", self.controls["posthoc_control"].blocks)
        self.assertIn("T565 replay", self.controls["replay_control"].blocks)
        self.assertIn("Promoting claim", self.controls["review_only_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_s1_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("TAF4 remains blocked", dumped)
        self.assertIn("TAF8 remains waiting", dumped)
        forbidden = (
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

    def test_all_gates_pass_and_markdown_reports_next_packet(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t566.render_markdown(self.payload)

        self.assertIn("T566 Results", markdown)
        self.assertIn("## Generator Type", markdown)
        self.assertIn("## Candidate Evaluations", markdown)
        self.assertIn(t566.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
