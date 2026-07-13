"""Tests for T556 Observerse protocol-stack post-absorber route reset gate."""

from __future__ import annotations

import json
import unittest

from models import t555_observerse_protocol_stack_absorber_separation_gate as t555
from models import t556_observerse_protocol_stack_post_absorber_route_reset_gate as t556


class ObserverseProtocolStackPostAbsorberRouteResetGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t556.run_t556_analysis()
        cls.payload = t556.t556_result_to_dict(cls.result)
        cls.decisions = {
            decision.option_id: decision for decision in cls.result.reset_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t556.ARTIFACT)
        self.assertEqual(self.result.verdict, t556.VERDICT)
        self.assertEqual(self.result.route_reset_status, t556.ROUTE_RESET_STATUS)
        self.assertEqual(self.result.source_t555_verdict, t555.VERDICT)
        self.assertEqual(self.result.source_t555_selected_next_packet, t555.NEXT_PACKET)
        self.assertEqual(self.result.source_t555_route_residue, t555.ROUTE_RESIDUE)

    def test_observerse_route_is_parked_not_extended(self) -> None:
        parked = self.decisions[t556.PARKED_ROUTE_ID]
        extension = self.decisions["extend_observerse_protocol_stack_with_more_fixtures"]

        self.assertTrue(parked.selected)
        self.assertEqual(parked.outcome, "SELECTED_ROUTE_RESET")
        self.assertEqual(parked.next_packet, t556.NEXT_PACKET)
        self.assertFalse(extension.selected)
        self.assertEqual(extension.outcome, "REJECTED_ABSORBER_REPLAY")
        self.assertIn("does_not_continue_absorbed_observerse_stack", extension.missing_requirements)

    def test_fresh_family_requires_predeclared_absorbers_and_falsifiers(self) -> None:
        fresh = self.decisions["name_fresh_source_law_family_now"]

        self.assertFalse(fresh.selected)
        self.assertEqual(fresh.outcome, "PAUSED_UNDERDECLARED_FRESH_FAMILY")
        for requirement in (
            "fresh_source_family_named",
            "absorbers_predeclared",
            "source_variables_declared",
            "falsifier_predeclared",
        ):
            self.assertIn(requirement, fresh.missing_requirements)

    def test_taf4_taf8_and_governance_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["taf4_from_observerse_stack"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["taf8_from_internal_stack"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["claim_canon_public_posture_shortcut"].outcome,
            "BLOCKED_GOVERNANCE",
        )

    def test_all_gates_pass_and_select_t557_preflight(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t555_absorber_completion_authority"].passed)
        self.assertTrue(self.gates["parked_route_selected"].passed)
        self.assertEqual(self.result.selected_reset_id, t556.PARKED_ROUTE_ID)
        self.assertEqual(self.result.selected_next_packet, t556.NEXT_PACKET)

    def test_hostile_controls_name_expected_overreads(self) -> None:
        self.assertIn("Continuing T550-T555", self.controls["absorber_completion_control"].blocks)
        self.assertIn("bounded native fixtures", self.controls["more_fixture_accumulation_control"].blocks)
        self.assertIn("fresh source-law route", self.controls["fresh_family_underdeclaration_control"].blocks)
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

    def test_markdown_reports_route_reset_and_next_packet(self) -> None:
        markdown = t556.render_markdown(self.payload)

        self.assertIn("T556 Results", markdown)
        self.assertIn("## Reset Decisions", markdown)
        self.assertIn(t556.PARKED_ROUTE_ID, markdown)
        self.assertIn(t556.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
