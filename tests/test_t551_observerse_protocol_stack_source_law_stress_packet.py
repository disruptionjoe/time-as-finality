"""Tests for T551 Observerse protocol-stack source-law stress packet."""

from __future__ import annotations

import json
import unittest

from models import t550_observerse_protocol_stack_ablation_preflight_packet as t550
from models import t551_observerse_protocol_stack_source_law_stress_packet as t551


class ObserverseProtocolStackSourceLawStressPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t551.run_t551_analysis()
        cls.payload = t551.t551_result_to_dict(cls.result)
        cls.outcomes = {
            outcome.scenario_id: outcome for outcome in cls.result.scenario_outcomes
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_t550_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t551.ARTIFACT)
        self.assertEqual(self.result.verdict, t551.VERDICT)
        self.assertEqual(self.result.stress_status, t551.STRESS_STATUS)
        self.assertEqual(self.result.source_t550_verdict, t550.VERDICT)
        self.assertEqual(
            self.result.source_t550_selected_next_packet,
            t550.NEXT_PACKET,
        )
        self.assertEqual(
            self.result.source_t550_layer_ids,
            ("issuance", "admissibility", "sybil_finality", "consensus", "governance"),
        )

    def test_native_fixture_predictions_match_all_modes(self) -> None:
        expected_modes = {
            "full_stack_rescue": "rescue",
            "without_issuance": "freeze",
            "without_admissibility": "incoherence",
            "without_sybil_finality": "capture",
            "without_consensus": "fragment",
            "without_governance_near_term": "ossification",
            "without_governance_full_horizon": "rescue_with_precomputed_rules",
        }

        self.assertEqual(set(self.outcomes), set(expected_modes))
        for scenario_id, expected in expected_modes.items():
            with self.subTest(scenario_id=scenario_id):
                outcome = self.outcomes[scenario_id]
                self.assertEqual(outcome.expected_mode, expected)
                self.assertEqual(outcome.actual_mode, expected)
                self.assertTrue(outcome.prediction_matched)
                self.assertTrue(outcome.target_blind_prediction)

    def test_full_stack_rescues_and_ablations_expose_failure_modes(self) -> None:
        full = self.outcomes["full_stack_rescue"]
        no_issuance = self.outcomes["without_issuance"]
        no_admissibility = self.outcomes["without_admissibility"]
        no_sybil = self.outcomes["without_sybil_finality"]
        no_consensus = self.outcomes["without_consensus"]
        no_governance = self.outcomes["without_governance_near_term"]

        self.assertGreaterEqual(full.final_record_count, 5)
        self.assertGreater(full.finality_score, 4.0)
        self.assertEqual(no_issuance.final_record_count, 0)
        self.assertGreater(no_admissibility.contradiction_count, 0)
        self.assertGreater(no_sybil.capture_count, 0)
        self.assertLess(no_consensus.shared_fraction, 0.5)
        self.assertGreaterEqual(no_governance.rejected_by_reason["rule_gap"], 3)

    def test_governance_conditional_is_preserved(self) -> None:
        near = self.outcomes["without_governance_near_term"]
        full_horizon = self.outcomes["without_governance_full_horizon"]

        self.assertEqual(near.actual_mode, "ossification")
        self.assertEqual(full_horizon.actual_mode, "rescue_with_precomputed_rules")
        self.assertTrue(self.gates["governance_conditional_preserved"].passed)
        self.assertEqual(
            self.gates["source_law_status_not_earned"].outcome,
            "PASS",
        )

    def test_all_gates_pass_and_select_t552(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(
            self.gates["collapse_rescue_predictions_match"].outcome,
            "PASS",
        )
        self.assertEqual(self.result.selected_next_packet, t551.NEXT_PACKET)

    def test_hostile_controls_block_overreading_and_shortcuts(self) -> None:
        self.assertIn(
            "source-law proof",
            self.controls["t527_t550_overread_control"].blocks,
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
            "Repairing APRD",
            self.controls["aprd_retune_control"].blocks,
        )
        self.assertIn(
            "Moving TAF4",
            self.controls["taf4_source_law_shortcut_control"].blocks,
        )

    def test_no_claim_canon_public_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("source-law status is not earned", dumped)
        forbidden = (
            "source law established",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)

    def test_markdown_reports_scenarios_and_next_packet(self) -> None:
        markdown = t551.render_markdown(self.payload)

        self.assertIn("T551 Results", markdown)
        self.assertIn("## Scenario Outcomes", markdown)
        self.assertIn("`full_stack_rescue`", markdown)
        self.assertIn("`without_governance_near_term`", markdown)
        self.assertIn(t551.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
