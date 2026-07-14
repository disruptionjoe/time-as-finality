"""Tests for T558 sheaf obstruction transport source-law packet."""

from __future__ import annotations

import json
import unittest

from models import t557_taf11_fresh_source_law_family_preflight_gate as t557
from models import t558_sheaf_obstruction_transport_source_law_packet as t558


class SheafObstructionTransportSourceLawPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t558.run_t558_analysis()
        cls.payload = t558.t558_result_to_dict(cls.result)
        cls.decisions = {
            decision.case_id: decision for decision in cls.result.case_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t558.ARTIFACT)
        self.assertEqual(self.result.verdict, t558.VERDICT)
        self.assertEqual(self.result.packet_status, t558.PACKET_STATUS)
        self.assertEqual(self.result.source_t557_verdict, t557.VERDICT)
        self.assertEqual(self.result.source_t557_selected_family, t557.SELECTED_FAMILY_ID)
        self.assertEqual(self.result.source_t557_selected_next_packet, t557.NEXT_PACKET)

    def test_t557_contract_is_frozen(self) -> None:
        source_t557 = t557.run_t557_analysis()

        self.assertEqual(self.result.frozen_source_variables, source_t557.selected_source_variables)
        self.assertEqual(self.result.frozen_mature_absorbers, source_t557.selected_mature_absorbers)
        self.assertEqual(self.result.frozen_falsifiers, source_t557.selected_falsifiers)

    def test_all_mature_absorbers_receive_control_cases(self) -> None:
        self.assertEqual(
            self.decisions["ordinary_gluing_completion_control"].outcome,
            "ABSORBED_ORDINARY_SHEAF_GLUE",
        )
        self.assertEqual(
            self.decisions["resource_transport_monotone_control"].outcome,
            "ABSORBED_RESOURCE_TRANSPORT_MONOTONE",
        )
        self.assertEqual(
            self.decisions["consensus_state_machine_control"].outcome,
            "ABSORBED_CONSENSUS_STATE_MACHINE",
        )
        self.assertEqual(
            self.decisions["record_provenance_completion_control"].outcome,
            "ABSORBED_RECORD_PROVENANCE_COMPLETION",
        )

    def test_declared_falsifiers_are_exercised(self) -> None:
        triggered = {
            falsifier
            for decision in self.result.case_decisions
            for falsifier in decision.triggered_falsifiers
        }

        self.assertGreaterEqual(triggered, set(self.result.frozen_falsifiers))
        self.assertEqual(
            self.decisions["same_variables_relabel_target_control"].outcome,
            "REJECTED_RELABELING_FALSIFIER",
        )
        self.assertEqual(
            self.decisions["hidden_target_import_control"].outcome,
            "REJECTED_HIDDEN_TARGET_OR_CROSS_REPO_IMPORT",
        )

    def test_spent_routes_are_rejected(self) -> None:
        self.assertEqual(
            self.decisions["observerse_replay_control"].outcome,
            "REJECTED_OBSERVERSE_REPLAY",
        )
        self.assertEqual(
            self.decisions["aprd_replay_control"].outcome,
            "REJECTED_APRD_REPLAY",
        )

    def test_only_formal_residue_is_admitted(self) -> None:
        formal = self.decisions["formal_noncommuting_transport_fixture"]

        self.assertTrue(formal.admitted)
        self.assertEqual(
            formal.outcome,
            "FORMAL_RESIDUE_ONLY_DOMAIN_NATIVE_BURDEN_REMAINS",
        )
        self.assertEqual(
            self.result.formal_residue_cases,
            ("formal_noncommuting_transport_fixture",),
        )
        self.assertEqual(self.result.selected_next_packet, t558.NEXT_PACKET)

    def test_all_gates_pass(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t557_preflight_authority"].passed)
        self.assertTrue(self.gates["family_contract_frozen"].passed)
        self.assertTrue(self.gates["all_mature_absorbers_exercised"].passed)
        self.assertTrue(self.gates["all_declared_falsifiers_exercised"].passed)
        self.assertTrue(self.gates["formal_residue_bounded"].passed)

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

    def test_markdown_reports_formal_residue_and_next_packet(self) -> None:
        markdown = t558.render_markdown(self.payload)

        self.assertIn("T558 Results", markdown)
        self.assertIn("## Frozen T557 Contract", markdown)
        self.assertIn("formal_noncommuting_transport_fixture", markdown)
        self.assertIn(t558.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
