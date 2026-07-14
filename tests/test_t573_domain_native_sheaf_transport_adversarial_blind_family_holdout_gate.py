"""Tests for T573 adversarial blind-family holdout."""

from __future__ import annotations

import json
import unittest

from models import (
    t572_domain_native_sheaf_transport_blind_family_holdout_gate as t572,
)
from models import (
    t573_domain_native_sheaf_transport_adversarial_blind_family_holdout_gate as t573,
)


class DomainNativeSheafTransportAdversarialBlindHoldoutGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t573.run_t573_analysis()
        cls.payload = t573.t573_result_to_dict(cls.result)
        cls.evaluations = {
            evaluation.probe_id: evaluation for evaluation in cls.result.evaluations
        }
        cls.checks = {
            check.check_id: check for check in cls.result.closure_checks
        }
        cls.routes = {
            decision.decision_id: decision for decision in cls.result.route_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t573.ARTIFACT)
        self.assertEqual(self.result.verdict, t573.VERDICT)
        self.assertEqual(self.result.holdout_status, t573.HOLDOUT_STATUS)
        self.assertEqual(self.result.source_law_status, t573.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t573.ROUTE_STATUS)
        self.assertEqual(self.result.source_t572_verdict, t572.VERDICT)
        self.assertEqual(self.result.source_t572_selected_next_packet, t572.NEXT_PACKET)
        self.assertTrue(self.result.source_t572_blind_family_holdout_cleared)

    def test_contract_changes_surface_genre_without_changing_frozen_roles(self) -> None:
        source = t572.run_t572_analysis()
        contract = self.result.holdout_contract

        self.assertEqual(contract.contract_id, "adversarial_blind_family_holdout_v1")
        self.assertEqual(contract.source_t572_blind_family_id, "settlement_attestation_blind_family")
        self.assertEqual(contract.adversarial_family_id, "redaction_dispute_audit_adversarial_family")
        self.assertEqual(contract.source_roles, source.holdout_contract.source_roles)
        self.assertEqual(contract.absorber_boundaries, source.holdout_contract.absorber_boundaries)
        self.assertEqual(contract.semantic_requirements, source.holdout_contract.semantic_requirements)
        self.assertIn("absorber_complete_triviality", contract.forbidden_shortcuts)
        self.assertTrue(self.checks["adversarial_genre_shift_predeclared"].passed)

    def test_adversarial_survivor_admits_without_replay_import_or_completion(self) -> None:
        expected = ("redaction_dispute_adversarial_survivor",)

        self.assertEqual(self.result.admitted_probe_ids, expected)
        survivor = self.evaluations["redaction_dispute_adversarial_survivor"]
        self.assertTrue(survivor.adversarial_holdout_admissible)
        self.assertTrue(survivor.expectation_matched)
        self.assertEqual(survivor.failed_checks, ())
        self.assertTrue(self.checks["adversarial_survivor_admitted"].passed)
        self.assertTrue(self.checks["no_replay_import_completion_or_foreign_truth"].passed)

    def test_adversarial_falsifiers_reject(self) -> None:
        expected = (
            "adversarial_settlement_replay_falsifier",
            "adversarial_target_import_falsifier",
            "adversarial_optional_payload_falsifier",
            "adversarial_commuting_square_falsifier",
            "adversarial_absorber_complete_falsifier",
            "adversarial_foreign_truth_falsifier",
        )

        self.assertEqual(self.result.rejected_probe_ids, expected)
        for probe_id in expected:
            with self.subTest(probe_id=probe_id):
                evaluation = self.evaluations[probe_id]
                self.assertFalse(evaluation.adversarial_holdout_admissible)
                self.assertTrue(evaluation.expectation_matched)
        self.assertIn(
            "adversarial_surface_genre",
            self.evaluations["adversarial_settlement_replay_falsifier"].failed_checks,
        )
        self.assertIn(
            "target_blind_language",
            self.evaluations["adversarial_target_import_falsifier"].failed_checks,
        )
        self.assertIn(
            "native_payload_forced",
            self.evaluations["adversarial_optional_payload_falsifier"].failed_checks,
        )
        self.assertIn(
            "noncommuting_transport_square",
            self.evaluations["adversarial_commuting_square_falsifier"].failed_checks,
        )
        self.assertIn(
            "no_absorber_complete_triviality",
            self.evaluations["adversarial_absorber_complete_falsifier"].failed_checks,
        )
        self.assertIn(
            "no_cross_repo_truth_import",
            self.evaluations["adversarial_foreign_truth_falsifier"].failed_checks,
        )
        self.assertTrue(self.checks["adversarial_falsifiers_rejected"].passed)

    def test_source_law_not_earned_and_t574_selected(self) -> None:
        self.assertTrue(self.result.adversarial_holdout_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t573.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_ROUTE_ADJUDICATION_REQUIRED",
        )
        self.assertTrue(self.routes["run_source_law_route_adjudication_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["route_adjudication_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t573"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t573"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t574(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t573.render_markdown(self.payload)

        self.assertIn("T573 Results", markdown)
        self.assertIn("## Probe Evaluations", markdown)
        self.assertIn(t573.NEXT_PACKET, markdown)

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
