"""Tests for T554 Observerse protocol-stack minimality gate."""

from __future__ import annotations

import json
import unittest

from models import t553_observerse_protocol_stack_generalization_boundary_gate as t553
from models import t554_observerse_protocol_stack_minimality_gate as t554


class ObserverseProtocolStackMinimalityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t554.run_t554_analysis()
        cls.payload = t554.t554_result_to_dict(cls.result)
        cls.fixtures = {
            fixture.fixture_id: fixture for fixture in cls.result.admitted_fixtures
        }
        cls.layer_outcomes = {
            (outcome.fixture_id, outcome.layer_id): outcome
            for outcome in cls.result.layer_minimality_outcomes
        }
        cls.aggregates = {
            aggregate.layer_id: aggregate for aggregate in cls.result.layer_aggregates
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t554.ARTIFACT)
        self.assertEqual(self.result.verdict, t554.VERDICT)
        self.assertEqual(self.result.minimality_status, t554.MINIMALITY_STATUS)
        self.assertEqual(
            self.result.source_t553_selected_next_packet,
            t553.NEXT_PACKET,
        )
        self.assertEqual(self.result.frozen_layers, t554.FROZEN_LAYERS)

    def test_admitted_class_is_preserved(self) -> None:
        expected = (
            "t551_bounded_native_fixture",
            "t552_independent_transfer_fixture",
            "third_phase_rotated_native_fixture",
        )

        self.assertEqual(self.result.source_t553_admitted_class_ids, expected)
        self.assertEqual(tuple(self.fixtures), expected)
        self.assertTrue(all(fixture.complete_rescues for fixture in self.fixtures.values()))
        self.assertTrue(self.gates["admitted_class_preserved"].passed)

    def test_every_layer_is_minimal_across_every_fixture(self) -> None:
        for layer_id, expected_drop_mode in t554.EXPECTED_DROP_MODES.items():
            with self.subTest(layer_id=layer_id):
                aggregate = self.aggregates[layer_id]
                self.assertTrue(aggregate.all_fixtures_minimal)
                self.assertEqual(aggregate.expected_drop_mode, expected_drop_mode)
                self.assertEqual(
                    set(aggregate.minimal_fixture_ids),
                    set(self.fixtures),
                )
                for fixture_id in self.fixtures:
                    outcome = self.layer_outcomes[(fixture_id, layer_id)]
                    self.assertEqual(outcome.actual_drop_mode, expected_drop_mode)
                    self.assertTrue(outcome.minimal_in_fixture)
                    self.assertTrue(outcome.matched)

    def test_conditional_governance_is_preserved(self) -> None:
        for fixture in self.fixtures.values():
            with self.subTest(fixture_id=fixture.fixture_id):
                self.assertEqual(fixture.layer_drop_modes["governance"], "ossification")
                self.assertEqual(
                    fixture.full_horizon_governance_mode,
                    "rescue_with_precomputed_rules",
                )
        self.assertTrue(self.gates["conditional_governance_preserved"].passed)

    def test_phase_rotated_fixture_is_not_replay(self) -> None:
        phase = self.fixtures["third_phase_rotated_native_fixture"]

        self.assertNotEqual(
            phase.record_ids,
            self.fixtures["t551_bounded_native_fixture"].record_ids,
        )
        self.assertNotEqual(
            phase.record_ids,
            self.fixtures["t552_independent_transfer_fixture"].record_ids,
        )
        self.assertTrue(self.gates["phase_rotated_fixture_not_replay"].passed)

    def test_all_gates_pass_and_select_t555(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(self.result.selected_next_packet, t554.NEXT_PACKET)
        self.assertTrue(self.gates["every_layer_minimal_across_class"].passed)
        self.assertTrue(self.gates["next_packet_specific"].passed)

    def test_hostile_controls_block_overreads(self) -> None:
        self.assertIn("Dropping", self.controls["layer_drop_control"].blocks)
        self.assertIn("renamed T551", self.controls["phase_rotated_replay_control"].blocks)
        self.assertIn("source-law proof", self.controls["source_law_overread_control"].blocks)
        self.assertIn("Skipping protocol", self.controls["absorber_bypass_control"].blocks)
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

    def test_markdown_reports_minimality_and_next_packet(self) -> None:
        markdown = t554.render_markdown(self.payload)

        self.assertIn("T554 Results", markdown)
        self.assertIn("## Layer Minimality Outcomes", markdown)
        self.assertIn("`third_phase_rotated_native_fixture`", markdown)
        self.assertIn("`governance`", markdown)
        self.assertIn(t554.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
