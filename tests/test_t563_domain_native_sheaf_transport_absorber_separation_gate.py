"""Tests for T563 domain-native sheaf transport absorber-separation gate."""

from __future__ import annotations

import json
import unittest

from models import t562_domain_native_sheaf_transport_minimality_gate as t562
from models import t563_domain_native_sheaf_transport_absorber_separation_gate as t563


class DomainNativeSheafTransportAbsorberSeparationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t563.run_t563_analysis()
        cls.payload = t563.t563_result_to_dict(cls.result)
        cls.controls = {
            control.absorber_id: control for control in cls.result.absorber_controls
        }
        cls.screens = {
            (screen.fixture_id, screen.absorber_id): screen
            for screen in cls.result.fixture_screens
        }
        cls.fixture_aggregates = {
            aggregate.fixture_id: aggregate
            for aggregate in cls.result.fixture_aggregates
        }
        cls.absorber_aggregates = {
            aggregate.absorber_id: aggregate
            for aggregate in cls.result.absorber_aggregates
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.hostile_controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t563.ARTIFACT)
        self.assertEqual(self.result.verdict, t563.VERDICT)
        self.assertEqual(self.result.absorber_status, t563.ABSORBER_STATUS)
        self.assertEqual(self.result.route_status, t563.ROUTE_STATUS)
        self.assertEqual(self.result.source_t562_selected_next_packet, t562.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t563.NEXT_PACKET)

    def test_t562_minimal_bounded_class_is_preserved(self) -> None:
        self.assertEqual(self.result.source_t562_bounded_class, t563.EXPECTED_BOUNDED_CLASS)
        self.assertEqual(tuple(self.fixture_aggregates), t563.EXPECTED_BOUNDED_CLASS)
        self.assertTrue(self.gates["t562_minimality_authority"].passed)
        self.assertTrue(self.gates["minimal_bounded_class_preserved"].passed)

    def test_all_absorbers_receive_state_and_absorb_native_controls(self) -> None:
        expected_absorbers = {
            "ordinary_sheaf_gluing_completion",
            "resource_transport_monotone_absorber",
            "consensus_state_machine_absorber",
            "record_provenance_completion_absorber",
        }
        self.assertEqual(set(self.controls), expected_absorbers)

        for absorber_id, control in self.controls.items():
            with self.subTest(absorber_id=absorber_id):
                self.assertTrue(control.same_neighbor_data_granted)
                self.assertTrue(control.native_control_absorbed)
                self.assertTrue(control.matched)
                self.assertGreaterEqual(len(control.granted_state), 4)
                self.assertGreaterEqual(len(control.granted_comparisons), 2)
        self.assertTrue(self.gates["absorber_same_neighbor_data_granted"].passed)
        self.assertTrue(self.gates["native_controls_absorbed"].passed)

    def test_each_fixture_separates_from_each_absorber(self) -> None:
        for fixture_id in t563.EXPECTED_BOUNDED_CLASS:
            aggregate = self.fixture_aggregates[fixture_id]
            with self.subTest(fixture_id=fixture_id):
                self.assertTrue(aggregate.all_absorbers_granted)
                self.assertTrue(aggregate.all_absorbers_separated)
                self.assertEqual(set(aggregate.separated_absorber_ids), set(self.controls))
            for absorber_id in self.controls:
                screen = self.screens[(fixture_id, absorber_id)]
                self.assertTrue(screen.same_neighbor_data_granted)
                self.assertTrue(screen.minimal_payload_preserved)
                self.assertTrue(screen.absorber_separated)
                self.assertFalse(screen.strong_reading_absorbed)
                self.assertTrue(screen.matched)

    def test_each_absorber_absorbs_controls_but_not_bounded_class(self) -> None:
        for absorber_id, aggregate in self.absorber_aggregates.items():
            with self.subTest(absorber_id=absorber_id):
                self.assertTrue(aggregate.native_control_absorbed)
                self.assertTrue(aggregate.all_fixtures_separated)
                self.assertEqual(set(aggregate.separated_fixture_ids), set(t563.EXPECTED_BOUNDED_CLASS))
        self.assertTrue(self.gates["bounded_class_separated_from_absorbers"].passed)

    def test_all_gates_pass_and_select_t564(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertEqual(self.result.selected_next_packet, t563.NEXT_PACKET)
        self.assertTrue(self.gates["next_packet_specific"].passed)
        self.assertTrue(self.gates["source_law_not_promoted"].passed)

    def test_hostile_controls_block_overreads(self) -> None:
        self.assertIn("impoverished state", self.hostile_controls["same_neighbor_data_control"].blocks)
        self.assertIn("native control", self.hostile_controls["native_control_control"].blocks)
        self.assertIn("source-law", self.hostile_controls["source_law_overread_control"].blocks)
        self.assertIn("TAF4", self.hostile_controls["taf4_taf8_shortcut_control"].blocks)

    def test_no_claim_canon_public_taf4_taf8_s1_or_cross_repo_movement(self) -> None:
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
            "S1 promoted",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)

    def test_markdown_reports_absorber_separation_and_next_packet(self) -> None:
        markdown = t563.render_markdown(self.payload)

        self.assertIn("T563 Results", markdown)
        self.assertIn("## Absorber Controls", markdown)
        self.assertIn("## Fixture Absorber Screens", markdown)
        self.assertIn("`ordinary_sheaf_gluing_completion`", markdown)
        self.assertIn(t563.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
