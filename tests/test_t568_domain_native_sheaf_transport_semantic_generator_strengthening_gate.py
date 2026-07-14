"""Tests for T568 semantic generator strengthening gate."""

from __future__ import annotations

import json
import unittest

from models import (
    t567_domain_native_sheaf_transport_source_law_hostile_review_gate as t567,
)
from models import (
    t568_domain_native_sheaf_transport_semantic_generator_strengthening_gate as t568,
)


class DomainNativeSheafTransportSemanticGeneratorStrengtheningGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t568.run_t568_analysis()
        cls.payload = t568.t568_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.adversary_id: evaluation
            for evaluation in cls.result.strengthened_evaluations
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
        self.assertEqual(self.result.artifact, t568.ARTIFACT)
        self.assertEqual(self.result.verdict, t568.VERDICT)
        self.assertEqual(self.result.generator_status, t568.GENERATOR_STATUS)
        self.assertEqual(self.result.source_law_status, t568.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t568.ROUTE_STATUS)
        self.assertEqual(self.result.source_t567_verdict, t567.VERDICT)
        self.assertEqual(self.result.source_t567_selected_next_packet, t567.NEXT_PACKET)
        self.assertTrue(self.result.source_t567_semantic_burden_exposed)

    def test_strengthened_generator_declares_semantic_screens(self) -> None:
        generator = self.result.strengthened_generator_type

        self.assertEqual(generator.semantic_requirements, t568.SEMANTIC_REQUIREMENTS)
        self.assertIn("nontrivial obstruction", generator.selection_rule)
        self.assertIn("noncommuting transport square", generator.selection_rule)
        self.assertIn("target-language import", generator.selection_rule)

    def test_valid_same_field_survivors_remain_admitted(self) -> None:
        expected = (
            "alternate_multisig_delay_repair_survivor",
            "alternate_checkpoint_quorum_repair_survivor",
        )

        self.assertEqual(self.result.preserved_survivor_ids, expected)
        for adversary_id in expected:
            with self.subTest(adversary_id=adversary_id):
                evaluation = self.evaluations[adversary_id]
                self.assertTrue(evaluation.prior_t566_selector_admissible)
                self.assertTrue(evaluation.prior_hostile_review_admissible)
                self.assertTrue(evaluation.strengthened_generator_admissible)
                self.assertEqual(evaluation.failed_checks, ())
        self.assertTrue(self.checks["native_survivors_preserved"].passed)
        self.assertTrue(self.gates["native_survivors_preserved"].passed)

    def test_t567_semantic_gaps_are_closed(self) -> None:
        expected = (
            "absorber_complete_trivial_gluing_case",
            "disguised_lorentzian_target_import",
        )

        self.assertEqual(self.result.closed_semantic_gap_ids, expected)
        for adversary_id in expected:
            with self.subTest(adversary_id=adversary_id):
                evaluation = self.evaluations[adversary_id]
                self.assertTrue(evaluation.prior_t566_selector_admissible)
                self.assertFalse(evaluation.prior_hostile_review_admissible)
                self.assertFalse(evaluation.strengthened_generator_admissible)
                self.assertEqual(
                    evaluation.status,
                    "T567_GAP_CLOSED_BY_SEMANTIC_GENERATOR",
                )
        self.assertTrue(self.checks["t567_semantic_gaps_closed"].passed)
        self.assertTrue(self.gates["semantic_generator_closes_named_gaps"].passed)

    def test_semantic_screens_catch_triviality_and_target_import(self) -> None:
        trivial = self.evaluations["absorber_complete_trivial_gluing_case"]
        target_import = self.evaluations["disguised_lorentzian_target_import"]

        self.assertIn("nontrivial_obstruction_witness", trivial.failed_checks)
        self.assertIn("noncommuting_transport_square", trivial.failed_checks)
        self.assertIn("native_payload_forced", trivial.failed_checks)
        self.assertIn("target_blind_language", target_import.failed_checks)
        self.assertTrue(self.checks["semantic_nontriviality_screen_active"].passed)
        self.assertTrue(self.checks["target_language_screen_active"].passed)

    def test_original_t566_controls_still_reject(self) -> None:
        missing = self.evaluations["missing_obstruction_witness_underdeclared_control"]
        posthoc = self.evaluations["posthoc_outcome_reading_control"]

        self.assertFalse(missing.prior_t566_selector_admissible)
        self.assertFalse(missing.strengthened_generator_admissible)
        self.assertEqual(missing.status, "REJECTED_BY_INHERITED_T566_SELECTOR")
        self.assertFalse(posthoc.prior_t566_selector_admissible)
        self.assertFalse(posthoc.strengthened_generator_admissible)
        self.assertEqual(posthoc.status, "REJECTED_BY_INHERITED_T566_SELECTOR")

    def test_source_law_not_earned_and_t569_selected(self) -> None:
        self.assertTrue(self.result.semantic_generator_strengthened)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t568.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_INDEPENDENT_REIMPLEMENTATION_REQUIRED",
        )
        self.assertTrue(self.routes["run_independent_reimplementation_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["independent_reimplementation_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t568"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t568"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t569(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t568.render_markdown(self.payload)

        self.assertIn("T568 Results", markdown)
        self.assertIn("## Strengthened Generator", markdown)
        self.assertIn(t568.NEXT_PACKET, markdown)

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
