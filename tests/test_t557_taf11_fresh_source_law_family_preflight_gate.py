"""Tests for T557 TAF11 fresh source-law family preflight gate."""

from __future__ import annotations

import json
import unittest

from models import t556_observerse_protocol_stack_post_absorber_route_reset_gate as t556
from models import t557_taf11_fresh_source_law_family_preflight_gate as t557


class Taf11FreshSourceLawFamilyPreflightGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t557.run_t557_analysis()
        cls.payload = t557.t557_result_to_dict(cls.result)
        cls.decisions = {
            decision.candidate_id: decision for decision in cls.result.family_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}
        cls.controls = {
            control.control_id: control for control in cls.result.hostile_controls
        }

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t557.ARTIFACT)
        self.assertEqual(self.result.verdict, t557.VERDICT)
        self.assertEqual(self.result.preflight_status, t557.PREFLIGHT_STATUS)
        self.assertEqual(self.result.source_t556_verdict, t556.VERDICT)
        self.assertEqual(self.result.source_t556_selected_next_packet, t556.NEXT_PACKET)

    def test_selected_family_declares_contract(self) -> None:
        selected = self.decisions[t557.SELECTED_FAMILY_ID]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.outcome, "SELECTED_FRESH_FAMILY_PREFLIGHT")
        self.assertEqual(selected.next_packet, t557.NEXT_PACKET)
        self.assertIn("finite_event_cover", self.result.selected_source_variables)
        self.assertIn("ordinary_sheaf_gluing_completion", self.result.selected_mature_absorbers)
        self.assertIn("all_obstructions_glue_under_declared_restrictions", self.result.selected_falsifiers)

    def test_spent_routes_are_rejected(self) -> None:
        self.assertEqual(
            self.decisions["observerse_protocol_stack_replay"].outcome,
            "REJECTED_OBSERVERSE_REPLAY",
        )
        self.assertEqual(
            self.decisions["aprd_replay_as_fresh_family"].outcome,
            "REJECTED_APRD_REPLAY",
        )

    def test_target_import_and_no_family_are_blocked(self) -> None:
        target_import = self.decisions["target_or_cross_repo_import_family"]
        no_family = self.decisions["pause_no_fresh_family_declared"]

        self.assertEqual(target_import.outcome, "BLOCKED_TARGET_OR_CROSS_REPO_IMPORT")
        self.assertIn("no_target_or_cross_repo_import", target_import.missing_requirements)
        self.assertEqual(no_family.outcome, "REJECTED_NO_FAMILY_DECLARED")
        self.assertIn("source_variables_declared", no_family.missing_requirements)

    def test_taf4_taf8_and_governance_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["taf4_from_fresh_family_preflight"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["taf8_from_fresh_family_preflight"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["claim_canon_public_posture_shortcut"].outcome,
            "BLOCKED_GOVERNANCE",
        )

    def test_all_gates_pass_and_select_t558(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t556_route_reset_authority"].passed)
        self.assertTrue(self.gates["exactly_one_fresh_family_selected"].passed)
        self.assertTrue(self.gates["source_variables_absorbers_and_falsifiers_declared"].passed)
        self.assertEqual(self.result.selected_family_id, t557.SELECTED_FAMILY_ID)
        self.assertEqual(self.result.selected_next_packet, t557.NEXT_PACKET)

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

    def test_markdown_reports_family_contract_and_next_packet(self) -> None:
        markdown = t557.render_markdown(self.payload)

        self.assertIn("T557 Results", markdown)
        self.assertIn("## Selected Family Contract", markdown)
        self.assertIn(t557.SELECTED_FAMILY_ID, markdown)
        self.assertIn(t557.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
