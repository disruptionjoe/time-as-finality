"""Tests for T561 domain-native sheaf transport generalization-boundary gate."""

from __future__ import annotations

import json
import unittest

from models import t560_domain_native_sheaf_transport_independent_transfer_gate as t560
from models import t561_domain_native_sheaf_transport_generalization_boundary_gate as t561


class DomainNativeSheafTransportGeneralizationBoundaryGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t561.run_t561_analysis()
        cls.payload = t561.t561_result_to_dict(cls.result)
        cls.outcomes = {
            outcome.case_id: outcome for outcome in cls.result.boundary_outcomes
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t561.ARTIFACT)
        self.assertEqual(self.result.verdict, t561.VERDICT)
        self.assertEqual(
            self.result.generalization_status,
            t561.GENERALIZATION_STATUS,
        )
        self.assertEqual(
            self.result.source_t560_selected_next_packet,
            t560.NEXT_PACKET,
        )
        self.assertEqual(self.result.selected_next_packet, t561.NEXT_PACKET)

    def test_bounded_domain_native_class_has_three_members(self) -> None:
        self.assertEqual(
            self.result.bounded_survivor_class,
            (
                "t559_record_finality_transport_square_survivor",
                "t560_handoff_rotation_repair_transfer_survivor",
                "third_multicover_seal_handoff_fixture",
            ),
        )
        self.assertTrue(self.gates["bounded_class_has_three_members"].passed)
        self.assertTrue(self.gates["third_fixture_independent"].passed)

    def test_absorber_controls_remain_active(self) -> None:
        expected = {
            "ordinary_gluing_boundary_control": (
                "absorbed_ordinary_sheaf_glue",
                "ordinary_sheaf_gluing_completion",
            ),
            "resource_budget_boundary_control": (
                "absorbed_resource_transport_monotone",
                "resource_transport_monotone_absorber",
            ),
            "consensus_state_machine_boundary_control": (
                "absorbed_consensus_state_machine",
                "consensus_state_machine_absorber",
            ),
            "record_provenance_boundary_control": (
                "absorbed_record_provenance_completion",
                "record_provenance_completion_absorber",
            ),
        }
        for case_id, (status, absorber) in expected.items():
            with self.subTest(case_id=case_id):
                outcome = self.outcomes[case_id]
                self.assertEqual(outcome.actual_status, status)
                self.assertEqual(outcome.absorber, absorber)
                self.assertFalse(outcome.in_generalization_class)

    def test_replay_and_spent_routes_are_rejected(self) -> None:
        expected = {
            "t559_payload_replay_as_new_fixture": "rejected_t559_payload_replay",
            "t560_transfer_replay_as_new_fixture": "rejected_t560_transfer_replay",
            "observerse_replay_boundary": "rejected_observerse_replay",
            "aprd_replay_boundary": "rejected_aprd_replay",
        }
        for case_id, status in expected.items():
            with self.subTest(case_id=case_id):
                outcome = self.outcomes[case_id]
                self.assertEqual(outcome.expected_status, status)
                self.assertEqual(outcome.actual_status, status)
                self.assertTrue(outcome.matched)
                self.assertFalse(outcome.in_generalization_class)
        self.assertTrue(self.gates["replay_and_spent_routes_rejected"].passed)

    def test_declared_falsifiers_are_exercised(self) -> None:
        triggered = {
            falsifier
            for outcome in self.result.boundary_outcomes
            for falsifier in outcome.triggered_falsifiers
        }

        self.assertGreaterEqual(triggered, set(self.result.frozen_falsifiers))
        self.assertEqual(
            self.outcomes["same_variables_relabel_target_boundary"].actual_status,
            "rejected_relabeling_falsifier",
        )
        self.assertEqual(
            self.outcomes["hidden_target_import_boundary"].actual_status,
            "rejected_hidden_target_or_cross_repo_import",
        )
        self.assertTrue(self.gates["all_declared_falsifiers_exercised"].passed)

    def test_taf4_taf8_and_source_law_shortcuts_are_blocked(self) -> None:
        expected = {
            "taf8_cross_domain_boundary": "out_of_scope_taf8_cross_domain",
            "taf4_lorentzian_target_import_boundary": "blocked_taf4_target_import",
            "source_law_overread_boundary": "blocked_source_law_overread",
        }
        for case_id, status in expected.items():
            with self.subTest(case_id=case_id):
                self.assertEqual(self.outcomes[case_id].actual_status, status)
        self.assertTrue(
            self.gates["taf4_taf8_and_source_law_boundaries_detected"].passed
        )

    def test_all_gates_pass(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t559_t560_authority"].passed)
        self.assertTrue(self.gates["family_contract_frozen"].passed)
        self.assertTrue(self.gates["source_survivors_preserved"].passed)
        self.assertTrue(self.gates["next_packet_specific"].passed)

    def test_hostile_controls_name_shortcuts(self) -> None:
        self.assertIn(
            "source-law proof",
            self.controls["source_law_overread_control"].blocks,
        )
        self.assertIn(
            "T559 or T560",
            self.controls["prior_survivor_replay_control"].blocks,
        )
        self.assertIn("Lorentzian", self.controls["taf4_target_import_control"].blocks)
        self.assertIn("TAF8", self.controls["taf8_cross_domain_control"].blocks)
        self.assertIn("Observerse", self.controls["spent_route_control"].blocks)

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

    def test_markdown_reports_boundary_and_next_packet(self) -> None:
        markdown = t561.render_markdown(self.payload)

        self.assertIn("T561 Results", markdown)
        self.assertIn("## Boundary Outcomes", markdown)
        self.assertIn("`third_multicover_seal_handoff_fixture`", markdown)
        self.assertIn("`source_law_overread_boundary`", markdown)
        self.assertIn(t561.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
