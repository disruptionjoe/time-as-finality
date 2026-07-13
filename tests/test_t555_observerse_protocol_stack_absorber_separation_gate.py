"""Tests for T555 Observerse protocol-stack absorber-separation gate."""

from __future__ import annotations

import json
import unittest

from models import t554_observerse_protocol_stack_minimality_gate as t554
from models import t555_observerse_protocol_stack_absorber_separation_gate as t555


class ObserverseProtocolStackAbsorberSeparationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t555.run_t555_analysis()
        cls.payload = t555.t555_result_to_dict(cls.result)
        cls.screens = {
            screen.absorber_id: screen for screen in cls.result.absorber_screens
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t555.ARTIFACT)
        self.assertEqual(self.result.verdict, t555.VERDICT)
        self.assertEqual(self.result.absorber_status, t555.ABSORBER_STATUS)
        self.assertEqual(self.result.route_residue, t555.ROUTE_RESIDUE)
        self.assertEqual(
            self.result.source_t554_selected_next_packet,
            t554.NEXT_PACKET,
        )

    def test_t554_minimal_payload_is_preserved(self) -> None:
        expected_fixtures = (
            "t551_bounded_native_fixture",
            "t552_independent_transfer_fixture",
            "third_phase_rotated_native_fixture",
        )

        self.assertEqual(self.result.source_t554_admitted_class_ids, expected_fixtures)
        self.assertEqual(self.result.source_t554_minimal_layer_ids, t554.FROZEN_LAYERS)
        self.assertTrue(self.gates["t554_minimality_authority"].passed)
        self.assertTrue(self.gates["bounded_class_payload_preserved"].passed)

    def test_all_absorbers_receive_native_state_and_comparisons(self) -> None:
        expected = {
            "protocol_state_machine_absorber",
            "consensus_distributed_systems_absorber",
            "governance_process_absorber",
            "record_provenance_absorber",
        }

        self.assertEqual(set(self.screens), expected)
        for screen in self.screens.values():
            with self.subTest(absorber_id=screen.absorber_id):
                self.assertTrue(screen.same_neighbor_data_granted)
                self.assertGreaterEqual(len(screen.granted_state), 3)
                self.assertGreaterEqual(len(screen.granted_comparisons), 2)
                self.assertTrue(set(screen.explains_layers).issubset(t554.FROZEN_LAYERS))
        self.assertTrue(self.gates["absorber_state_rights_granted"].passed)

    def test_strong_source_law_reading_is_absorbed_not_separated(self) -> None:
        for screen in self.screens.values():
            with self.subTest(absorber_id=screen.absorber_id):
                self.assertTrue(screen.strong_reading_absorbed)
                self.assertFalse(screen.source_law_separated)
                self.assertTrue(screen.matched)
                self.assertIn(screen.audit_residue, {"translation_residue", "heuristic_residue"})
        self.assertTrue(self.gates["strong_source_law_reading_absorbed"].passed)
        self.assertTrue(self.gates["audit_residue_only"].passed)

    def test_all_gates_pass_and_select_t556(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(self.result.selected_next_packet, t555.NEXT_PACKET)
        self.assertTrue(self.gates["next_packet_specific"].passed)

    def test_hostile_controls_block_overreads(self) -> None:
        self.assertIn("impoverished absorber state", self.controls["same_neighbor_data_control"].blocks)
        self.assertIn("source-law separation", self.controls["source_law_separation_control"].blocks)
        self.assertIn("bounded-native fixtures", self.controls["more_fixture_control"].blocks)
        self.assertIn("TAF4", self.controls["taf4_taf8_shortcut_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_or_cross_repo_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
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

    def test_markdown_reports_absorbers_and_next_packet(self) -> None:
        markdown = t555.render_markdown(self.payload)

        self.assertIn("T555 Results", markdown)
        self.assertIn("## Absorber Screens", markdown)
        self.assertIn("`protocol_state_machine_absorber`", markdown)
        self.assertIn("`consensus_distributed_systems_absorber`", markdown)
        self.assertIn(t555.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
