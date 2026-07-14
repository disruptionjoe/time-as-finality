"""Tests for T567 domain-native sheaf transport source-law hostile review gate."""

from __future__ import annotations

import json
import unittest

from models import t566_domain_native_sheaf_transport_typed_generator_gate as t566
from models import (
    t567_domain_native_sheaf_transport_source_law_hostile_review_gate as t567,
)


class DomainNativeSheafTransportSourceLawHostileReviewGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t567.run_t567_analysis()
        cls.payload = t567.t567_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.adversary_id: evaluation
            for evaluation in cls.result.hostile_evaluations
        }
        cls.checks = {
            check.check_id: check for check in cls.result.review_checks
        }
        cls.routes = {
            decision.decision_id: decision
            for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t567.ARTIFACT)
        self.assertEqual(self.result.verdict, t567.VERDICT)
        self.assertEqual(self.result.hostile_review_status, t567.HOSTILE_REVIEW_STATUS)
        self.assertEqual(self.result.source_law_status, t567.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t567.ROUTE_STATUS)
        self.assertEqual(self.result.source_t566_verdict, t566.VERDICT)
        self.assertEqual(self.result.source_t566_selected_next_packet, t566.NEXT_PACKET)
        self.assertTrue(self.result.source_t566_review_packet_complete)
        self.assertTrue(self.result.t566_field_selector_survives_narrow_contract)

    def test_valid_same_field_alternates_survive_hostile_review(self) -> None:
        expected = (
            "alternate_multisig_delay_repair_survivor",
            "alternate_checkpoint_quorum_repair_survivor",
        )

        self.assertEqual(self.result.valid_alternate_survivor_ids, expected)
        for adversary_id in expected:
            with self.subTest(adversary_id=adversary_id):
                evaluation = self.evaluations[adversary_id]
                self.assertTrue(evaluation.t566_selector_admissible)
                self.assertTrue(evaluation.hostile_review_admissible)
                self.assertEqual(evaluation.status, "SURVIVES_HOSTILE_REVIEW")
                self.assertEqual(evaluation.failed_checks, ())
        self.assertTrue(self.checks["valid_same_field_alternates_survive"].passed)
        self.assertTrue(self.gates["same_field_alternates_survive"].passed)

    def test_semantic_gap_adversaries_are_admitted_by_t566_but_rejected_by_hostile_review(self) -> None:
        expected = (
            "absorber_complete_trivial_gluing_case",
            "disguised_lorentzian_target_import",
        )

        self.assertEqual(self.result.semantic_gap_adversary_ids, expected)
        for adversary_id in expected:
            with self.subTest(adversary_id=adversary_id):
                evaluation = self.evaluations[adversary_id]
                self.assertTrue(evaluation.t566_selector_admissible)
                self.assertFalse(evaluation.hostile_review_admissible)
                self.assertEqual(
                    evaluation.status,
                    "T566_SELECTOR_ADMITS_HOSTILE_REJECTS",
                )
        self.assertIn(
            "semantic_nontriviality",
            self.evaluations["absorber_complete_trivial_gluing_case"].failed_checks,
        )
        self.assertIn(
            "target_blind_language",
            self.evaluations["disguised_lorentzian_target_import"].failed_checks,
        )
        self.assertTrue(self.result.semantic_generator_burden_exposed)
        self.assertTrue(self.gates["semantic_gaps_detected"].passed)

    def test_original_t566_controls_still_reject(self) -> None:
        missing = self.evaluations["missing_obstruction_witness_underdeclared_control"]
        posthoc = self.evaluations["posthoc_outcome_reading_control"]

        self.assertFalse(missing.t566_selector_admissible)
        self.assertFalse(missing.hostile_review_admissible)
        self.assertIn("t566_field_selector_admits", missing.failed_checks)
        self.assertFalse(posthoc.t566_selector_admissible)
        self.assertFalse(posthoc.hostile_review_admissible)
        self.assertIn("t566_field_selector_admits", posthoc.failed_checks)
        self.assertTrue(self.checks["original_t566_controls_still_reject"].passed)

    def test_source_law_not_earned_and_t568_selected(self) -> None:
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t567.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_SEMANTIC_GENERATOR_BURDEN",
        )
        self.assertTrue(self.routes["run_semantic_generator_strengthening_gate"].selected)
        self.assertEqual(
            self.routes["run_semantic_generator_strengthening_gate"].next_packet,
            t567.NEXT_PACKET,
        )
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["semantic_strengthening_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t567"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t567"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t568(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t567.render_markdown(self.payload)

        self.assertIn("T567 Results", markdown)
        self.assertIn("## Hostile Evaluations", markdown)
        self.assertIn(t567.NEXT_PACKET, markdown)

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
