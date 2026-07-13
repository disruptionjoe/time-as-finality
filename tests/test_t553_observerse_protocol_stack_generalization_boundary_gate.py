"""Tests for T553 Observerse protocol-stack generalization-boundary gate."""

from __future__ import annotations

import json
import unittest

from models import t552_observerse_protocol_stack_independent_transfer_gate as t552
from models import t553_observerse_protocol_stack_generalization_boundary_gate as t553


class ObserverseProtocolStackGeneralizationBoundaryGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t553.run_t553_analysis()
        cls.payload = t553.t553_result_to_dict(cls.result)
        cls.outcomes = {
            outcome.case_id: outcome for outcome in cls.result.boundary_outcomes
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t553.ARTIFACT)
        self.assertEqual(self.result.verdict, t553.VERDICT)
        self.assertEqual(self.result.generalization_status, t553.GENERALIZATION_STATUS)
        self.assertEqual(
            self.result.source_t552_selected_next_packet,
            t552.NEXT_PACKET,
        )
        self.assertEqual(self.result.frozen_layers, t553.FROZEN_LAYERS)

    def test_bounded_native_class_has_three_members(self) -> None:
        inside = [
            outcome.case_id
            for outcome in self.result.boundary_outcomes
            if outcome.in_generalization_class
        ]

        self.assertEqual(
            inside,
            [
                "t551_bounded_native_fixture",
                "t552_independent_transfer_fixture",
                "third_phase_rotated_native_fixture",
            ],
        )
        self.assertTrue(self.gates["bounded_native_class_has_multiple_members"].passed)

    def test_boundaries_reject_overreach_cases(self) -> None:
        expected = {
            "single_observer_consensus_light_fixture": "boundary_consensus_insufficient",
            "near_term_only_governance_fixture": "boundary_conditional_governance_missing",
            "aprd_retuned_fixture": "blocked_retreated_route",
            "cross_domain_taf8_packet": "out_of_scope_cross_domain",
            "lorentzian_target_import_fixture": "blocked_target_import",
            "source_law_overread_fixture": "blocked_source_law_overread",
        }
        for case_id, status in expected.items():
            with self.subTest(case_id=case_id):
                outcome = self.outcomes[case_id]
                self.assertEqual(outcome.expected_status, status)
                self.assertEqual(outcome.actual_status, status)
                self.assertTrue(outcome.matched)
                self.assertFalse(outcome.in_generalization_class)

    def test_all_gates_pass_and_select_t554(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(self.result.selected_next_packet, t553.NEXT_PACKET)
        self.assertTrue(self.gates["source_law_status_not_earned"].passed)
        self.assertTrue(self.gates["external_and_cross_domain_boundaries_detected"].passed)

    def test_hostile_controls_name_shortcuts(self) -> None:
        self.assertIn("source-law proof", self.controls["source_law_overread_control"].blocks)
        self.assertIn("Lorentzian", self.controls["taf4_target_import_control"].blocks)
        self.assertIn("TAF8", self.controls["taf8_cross_domain_control"].blocks)
        self.assertIn("Retuning APRD", self.controls["aprd_retune_control"].blocks)
        self.assertIn("unconditional", self.controls["conditional_governance_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        self.assertIn("source-law status", dumped)
        self.assertIn("TAF4 remains blocked", dumped)
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

    def test_markdown_reports_boundary_and_next_packet(self) -> None:
        markdown = t553.render_markdown(self.payload)

        self.assertIn("T553 Results", markdown)
        self.assertIn("## Boundary Outcomes", markdown)
        self.assertIn("`third_phase_rotated_native_fixture`", markdown)
        self.assertIn("`source_law_overread_fixture`", markdown)
        self.assertIn(t553.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
