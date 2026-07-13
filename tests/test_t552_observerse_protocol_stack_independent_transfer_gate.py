"""Tests for T552 Observerse protocol-stack independent transfer gate."""

from __future__ import annotations

import json
import unittest

from models import t551_observerse_protocol_stack_source_law_stress_packet as t551
from models import t552_observerse_protocol_stack_independent_transfer_gate as t552


class ObserverseProtocolStackIndependentTransferGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t552.run_t552_analysis()
        cls.payload = t552.t552_result_to_dict(cls.result)
        cls.outcomes = {
            outcome.scenario_id: outcome for outcome in cls.result.scenario_outcomes
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_t551_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t552.ARTIFACT)
        self.assertEqual(self.result.verdict, t552.VERDICT)
        self.assertEqual(self.result.transfer_status, t552.TRANSFER_STATUS)
        self.assertEqual(self.result.source_t551_verdict, t551.VERDICT)
        self.assertEqual(
            self.result.source_t551_selected_next_packet,
            t551.NEXT_PACKET,
        )
        self.assertEqual(
            self.result.source_t550_layer_ids,
            ("issuance", "admissibility", "sybil_finality", "consensus", "governance"),
        )

    def test_transfer_fixture_is_independent_from_t551(self) -> None:
        source_ids = set(self.result.source_t551_full_stack_record_ids)
        transfer_ids = set(self.result.transfer_record_ids)

        self.assertTrue(source_ids)
        self.assertTrue(transfer_ids)
        self.assertTrue(source_ids.isdisjoint(transfer_ids))
        self.assertTrue(all(record_id.startswith("x_") for record_id in transfer_ids))
        self.assertNotEqual(
            len(self.result.source_t551_full_stack_record_ids),
            len(self.result.transfer_record_ids),
        )
        self.assertTrue(
            self.gates["independent_transfer_fixture_declared"].passed,
        )

    def test_transfer_predictions_match_all_modes(self) -> None:
        expected_modes = {
            "independent_transfer_rescue": "rescue",
            "transfer_without_issuance": "freeze",
            "transfer_without_admissibility": "incoherence",
            "transfer_without_sybil_finality": "capture",
            "transfer_without_consensus": "fragment",
            "transfer_without_governance_near_term": "ossification",
            "transfer_without_governance_full_horizon": "rescue_with_precomputed_rules",
        }

        self.assertEqual(set(self.outcomes), set(expected_modes))
        for scenario_id, expected in expected_modes.items():
            with self.subTest(scenario_id=scenario_id):
                outcome = self.outcomes[scenario_id]
                self.assertEqual(outcome.expected_mode, expected)
                self.assertEqual(outcome.actual_mode, expected)
                self.assertTrue(outcome.prediction_matched)
                self.assertTrue(outcome.target_blind_prediction)
                self.assertTrue(outcome.transfer_fixture_independent)

    def test_full_stack_rescues_and_ablations_expose_transfer_failures(self) -> None:
        full = self.outcomes["independent_transfer_rescue"]
        no_issuance = self.outcomes["transfer_without_issuance"]
        no_admissibility = self.outcomes["transfer_without_admissibility"]
        no_sybil = self.outcomes["transfer_without_sybil_finality"]
        no_consensus = self.outcomes["transfer_without_consensus"]
        no_governance = self.outcomes["transfer_without_governance_near_term"]

        self.assertGreaterEqual(full.final_record_count, 7)
        self.assertGreaterEqual(full.partition_count, 3)
        self.assertGreater(full.finality_score, 7.0)
        self.assertEqual(no_issuance.final_record_count, 0)
        self.assertGreater(no_admissibility.contradiction_count, 0)
        self.assertGreater(no_sybil.capture_count, 0)
        self.assertLess(no_consensus.shared_fraction, 0.5)
        self.assertGreaterEqual(no_governance.rejected_by_reason["rule_gap"], 3)

    def test_governance_conditional_and_self_confirmation_controls_pass(self) -> None:
        near = self.outcomes["transfer_without_governance_near_term"]
        full_horizon = self.outcomes["transfer_without_governance_full_horizon"]

        self.assertEqual(near.actual_mode, "ossification")
        self.assertEqual(full_horizon.actual_mode, "rescue_with_precomputed_rules")
        self.assertTrue(self.gates["governance_conditional_preserved"].passed)
        self.assertTrue(self.gates["self_confirmation_control_passed"].passed)
        self.assertEqual(
            self.gates["source_law_status_not_earned"].outcome,
            "PASS",
        )

    def test_all_gates_pass_and_select_t553(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(
            self.gates["collapse_rescue_predictions_match"].outcome,
            "PASS",
        )
        self.assertEqual(self.result.selected_next_packet, t552.NEXT_PACKET)

    def test_hostile_controls_block_overreading_and_shortcuts(self) -> None:
        self.assertIn(
            "renamed T551 fixture",
            self.controls["t551_self_confirmation_control"].blocks,
        )
        self.assertIn(
            "Adding, dropping, or renaming layers",
            self.controls["post_hoc_layer_control"].blocks,
        )
        self.assertIn(
            "Dropping governance",
            self.controls["conditional_governance_control"].blocks,
        )
        self.assertIn(
            "Moving TAF4",
            self.controls["taf4_source_law_shortcut_control"].blocks,
        )
        self.assertIn(
            "cross-domain shadow-protection",
            self.controls["taf8_transfer_overread_control"].blocks,
        )

    def test_no_claim_canon_public_taf4_taf8_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("source-law status is not earned", dumped)
        self.assertIn("TAF8 remains waiting", dumped)
        forbidden = (
            "source law established",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
            "TAF8 theorem proved",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)

    def test_markdown_reports_transfer_and_next_packet(self) -> None:
        markdown = t552.render_markdown(self.payload)

        self.assertIn("T552 Results", markdown)
        self.assertIn("## Transfer Independence", markdown)
        self.assertIn("`independent_transfer_rescue`", markdown)
        self.assertIn("`transfer_without_governance_near_term`", markdown)
        self.assertIn(t552.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
