"""Tests for T562 domain-native sheaf transport minimality gate."""

from __future__ import annotations

import json
import unittest

from models import t561_domain_native_sheaf_transport_generalization_boundary_gate as t561
from models import t562_domain_native_sheaf_transport_minimality_gate as t562


class DomainNativeSheafTransportMinimalityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t562.run_t562_analysis()
        cls.payload = t562.t562_result_to_dict(cls.result)
        cls.fixtures = {
            fixture.fixture_id: fixture for fixture in cls.result.admitted_fixtures
        }
        cls.source_outcomes = {
            (outcome.fixture_id, outcome.variable_id): outcome
            for outcome in cls.result.source_variable_outcomes
        }
        cls.boundary_outcomes = {
            (outcome.fixture_id, outcome.condition_id): outcome
            for outcome in cls.result.boundary_condition_outcomes
        }
        cls.source_aggregates = {
            aggregate.item_id: aggregate
            for aggregate in cls.result.source_variable_aggregates
        }
        cls.boundary_aggregates = {
            aggregate.item_id: aggregate
            for aggregate in cls.result.boundary_condition_aggregates
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t562.ARTIFACT)
        self.assertEqual(self.result.verdict, t562.VERDICT)
        self.assertEqual(self.result.minimality_status, t562.MINIMALITY_STATUS)
        self.assertEqual(
            self.result.source_t561_selected_next_packet,
            t561.NEXT_PACKET,
        )
        self.assertEqual(self.result.selected_next_packet, t562.NEXT_PACKET)

    def test_bounded_class_is_preserved(self) -> None:
        self.assertEqual(self.result.source_t561_bounded_class, t562.EXPECTED_BOUNDED_CLASS)
        self.assertEqual(tuple(self.fixtures), t562.EXPECTED_BOUNDED_CLASS)
        self.assertTrue(all(fixture.complete_admits for fixture in self.fixtures.values()))
        self.assertTrue(self.gates["bounded_class_preserved"].passed)

    def test_every_source_variable_is_minimal_across_every_fixture(self) -> None:
        for variable_id, expected_drop in t562.EXPECTED_SOURCE_VARIABLE_DROP_MODES.items():
            with self.subTest(variable_id=variable_id):
                aggregate = self.source_aggregates[variable_id]
                self.assertTrue(aggregate.all_fixtures_minimal)
                self.assertEqual(aggregate.expected_drop_status, expected_drop)
                self.assertEqual(set(aggregate.minimal_fixture_ids), set(self.fixtures))
                for fixture_id in self.fixtures:
                    outcome = self.source_outcomes[(fixture_id, variable_id)]
                    self.assertEqual(outcome.actual_drop_status, expected_drop)
                    self.assertTrue(outcome.minimal_in_fixture)
                    self.assertTrue(outcome.matched)

    def test_core_boundary_conditions_are_minimal(self) -> None:
        for condition_id, expected_drop in t562.CORE_BOUNDARY_DROP_MODES.items():
            with self.subTest(condition_id=condition_id):
                aggregate = self.boundary_aggregates[condition_id]
                self.assertEqual(aggregate.item_kind, "core_boundary")
                self.assertEqual(aggregate.expected_drop_status, expected_drop)
                self.assertTrue(aggregate.all_fixtures_minimal)
                for fixture_id in self.fixtures:
                    outcome = self.boundary_outcomes[(fixture_id, condition_id)]
                    self.assertEqual(outcome.actual_drop_status, expected_drop)
                    self.assertTrue(outcome.matched)

    def test_absorber_and_falsifier_boundaries_are_minimal(self) -> None:
        expected = {
            **t562.ABSORBER_DROP_MODES,
            **t562.FALSIFIER_DROP_MODES,
        }
        for condition_id, expected_drop in expected.items():
            with self.subTest(condition_id=condition_id):
                aggregate = self.boundary_aggregates[condition_id]
                self.assertEqual(aggregate.expected_drop_status, expected_drop)
                self.assertTrue(aggregate.all_fixtures_minimal)
                self.assertEqual(set(aggregate.minimal_fixture_ids), set(self.fixtures))
        self.assertTrue(self.gates["absorber_and_falsifier_boundaries_covered"].passed)
        self.assertTrue(self.gates["every_boundary_condition_minimal_across_class"].passed)

    def test_all_gates_pass_and_select_t563(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t561_boundary_authority"].passed)
        self.assertTrue(self.gates["complete_contract_admits_all_fixtures"].passed)
        self.assertTrue(self.gates["every_source_variable_minimal_across_class"].passed)
        self.assertTrue(self.gates["next_packet_specific"].passed)
        self.assertEqual(self.result.selected_next_packet, t562.NEXT_PACKET)

    def test_hostile_controls_block_overreads(self) -> None:
        self.assertIn(
            "Dropping",
            self.controls["source_variable_drop_control"].blocks,
        )
        self.assertIn(
            "Skipping mature absorber",
            self.controls["absorber_boundary_drop_control"].blocks,
        )
        self.assertIn(
            "Skipping gluing",
            self.controls["falsifier_boundary_drop_control"].blocks,
        )
        self.assertIn(
            "source-law proof",
            self.controls["source_law_overread_control"].blocks,
        )
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
        markdown = t562.render_markdown(self.payload)

        self.assertIn("T562 Results", markdown)
        self.assertIn("## Source Variable Minimality Outcomes", markdown)
        self.assertIn("## Boundary Condition Minimality Outcomes", markdown)
        self.assertIn("`finite_event_cover`", markdown)
        self.assertIn("`ordinary_sheaf_gluing_completion`", markdown)
        self.assertIn(t562.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
