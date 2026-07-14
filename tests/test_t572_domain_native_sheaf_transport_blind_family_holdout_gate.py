"""Tests for T572 blind-family holdout."""

from __future__ import annotations

import json
import unittest

from models import (
    t571_domain_native_sheaf_transport_multi_family_falsifier_rotation_gate as t571,
)
from models import (
    t572_domain_native_sheaf_transport_blind_family_holdout_gate as t572,
)


class DomainNativeSheafTransportBlindFamilyHoldoutGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t572.run_t572_analysis()
        cls.payload = t572.t572_result_to_dict(cls.result)
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
        self.assertEqual(self.result.artifact, t572.ARTIFACT)
        self.assertEqual(self.result.verdict, t572.VERDICT)
        self.assertEqual(self.result.holdout_status, t572.HOLDOUT_STATUS)
        self.assertEqual(self.result.source_law_status, t572.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.route_status, t572.ROUTE_STATUS)
        self.assertEqual(self.result.source_t571_verdict, t571.VERDICT)
        self.assertEqual(self.result.source_t571_selected_next_packet, t571.NEXT_PACKET)
        self.assertTrue(self.result.source_t571_multi_family_rotation_cleared)

    def test_contract_predeclares_true_blind_family(self) -> None:
        contract = self.result.holdout_contract

        self.assertEqual(contract.contract_id, "blind_family_holdout_v1")
        self.assertEqual(contract.source_t571_contract_id, "multi_family_falsifier_rotation_v1")
        self.assertEqual(contract.blind_family_id, "settlement_attestation_blind_family")
        self.assertNotIn(contract.blind_family_id, contract.source_t571_admitted_family_ids)
        self.assertIn("family_replay", contract.forbidden_shortcuts)
        self.assertTrue(self.checks["blind_family_predeclared_and_withheld"].passed)

    def test_blind_survivor_admits_without_replay_or_import(self) -> None:
        expected = ("settlement_attestation_blind_survivor",)

        self.assertEqual(self.result.admitted_probe_ids, expected)
        survivor = self.evaluations["settlement_attestation_blind_survivor"]
        self.assertTrue(survivor.holdout_admissible)
        self.assertTrue(survivor.expectation_matched)
        self.assertEqual(survivor.failed_checks, ())
        self.assertTrue(self.checks["blind_survivor_admitted"].passed)
        self.assertTrue(self.checks["no_replay_import_or_foreign_truth"].passed)

    def test_holdout_falsifiers_reject(self) -> None:
        expected = (
            "blind_family_calibration_replay_falsifier",
            "blind_family_target_import_falsifier",
            "blind_family_optional_payload_falsifier",
            "blind_family_missing_transport_square_falsifier",
            "blind_family_foreign_truth_falsifier",
        )

        self.assertEqual(self.result.rejected_probe_ids, expected)
        for probe_id in expected:
            with self.subTest(probe_id=probe_id):
                evaluation = self.evaluations[probe_id]
                self.assertFalse(evaluation.holdout_admissible)
                self.assertTrue(evaluation.expectation_matched)
        self.assertIn(
            "family_was_withheld",
            self.evaluations["blind_family_calibration_replay_falsifier"].failed_checks,
        )
        self.assertIn(
            "target_blind_language",
            self.evaluations["blind_family_target_import_falsifier"].failed_checks,
        )
        self.assertIn(
            "native_payload_forced",
            self.evaluations["blind_family_optional_payload_falsifier"].failed_checks,
        )
        self.assertIn(
            "noncommuting_transport_square",
            self.evaluations["blind_family_missing_transport_square_falsifier"].failed_checks,
        )
        self.assertIn(
            "no_cross_repo_truth_import",
            self.evaluations["blind_family_foreign_truth_falsifier"].failed_checks,
        )
        self.assertTrue(self.checks["blind_falsifiers_rejected"].passed)

    def test_source_law_not_earned_and_t573_selected(self) -> None:
        self.assertTrue(self.result.blind_family_holdout_cleared)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(self.result.selected_next_packet, t572.NEXT_PACKET)
        self.assertEqual(
            self.routes["promote_source_law_now"].outcome,
            "REJECTED_REVIEW_ONLY_ADVERSARIAL_HOLDOUT_REQUIRED",
        )
        self.assertTrue(self.routes["run_adversarial_blind_family_holdout_gate"].selected)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)
        self.assertTrue(self.gates["adversarial_holdout_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.routes["move_taf4_from_t572"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.routes["execute_taf8_from_t572"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.routes["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["taf4_taf8_s1_boundaries_preserved"].passed)
        self.assertTrue(self.gates["governance_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t573(self) -> None:
        self.assertTrue(all(check.passed for check in self.result.closure_checks))
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t572.render_markdown(self.payload)

        self.assertIn("T572 Results", markdown)
        self.assertIn("## Probe Evaluations", markdown)
        self.assertIn(t572.NEXT_PACKET, markdown)

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
