"""Tests for T560 domain-native sheaf transport independent-transfer gate."""

from __future__ import annotations

import json
import unittest

from models import t559_domain_native_sheaf_transport_packet_burden_gate as t559
from models import t560_domain_native_sheaf_transport_independent_transfer_gate as t560


class DomainNativeSheafTransportIndependentTransferGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t560.run_t560_analysis()
        cls.payload = t560.t560_result_to_dict(cls.result)
        cls.decisions = {
            decision.case_id: decision for decision in cls.result.case_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t560.ARTIFACT)
        self.assertEqual(self.result.verdict, t560.VERDICT)
        self.assertEqual(self.result.transfer_status, t560.TRANSFER_STATUS)
        self.assertEqual(self.result.source_t559_verdict, t559.VERDICT)
        self.assertEqual(self.result.source_t559_selected_next_packet, t559.NEXT_PACKET)

    def test_frozen_contract_and_t559_payload_are_preserved(self) -> None:
        source_t559 = t559.run_t559_analysis()

        self.assertEqual(self.result.frozen_source_variables, source_t559.frozen_source_variables)
        self.assertEqual(self.result.frozen_mature_absorbers, source_t559.frozen_mature_absorbers)
        self.assertEqual(self.result.frozen_falsifiers, source_t559.frozen_falsifiers)
        self.assertEqual(
            self.result.source_t559_admitted_packets,
            ("record_finality_transport_square_payload",),
        )

    def test_t559_replay_and_spent_routes_are_rejected(self) -> None:
        self.assertEqual(
            self.decisions["t559_payload_replay_control"].outcome,
            "REJECTED_T559_PAYLOAD_REPLAY",
        )
        self.assertEqual(
            self.decisions["observerse_replay_control"].outcome,
            "REJECTED_OBSERVERSE_REPLAY",
        )
        self.assertEqual(
            self.decisions["aprd_replay_control"].outcome,
            "REJECTED_APRD_REPLAY",
        )

    def test_absorber_controls_are_exercised(self) -> None:
        self.assertEqual(
            self.decisions["ordinary_gluing_transfer_control"].outcome,
            "ABSORBED_ORDINARY_SHEAF_GLUE",
        )
        self.assertEqual(
            self.decisions["resource_budget_transfer_control"].outcome,
            "ABSORBED_RESOURCE_TRANSPORT_MONOTONE",
        )
        self.assertEqual(
            self.decisions["consensus_state_machine_transfer_control"].outcome,
            "ABSORBED_CONSENSUS_STATE_MACHINE",
        )
        self.assertEqual(
            self.decisions["record_provenance_transfer_control"].outcome,
            "ABSORBED_RECORD_PROVENANCE_COMPLETION",
        )

    def test_declared_falsifiers_and_formal_shortcuts_are_exercised(self) -> None:
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
        self.assertEqual(
            self.decisions["formal_residue_without_payload_control"].outcome,
            "REJECTED_NO_DOMAIN_NATIVE_PAYLOAD",
        )

    def test_independent_transfer_is_admitted_review_only(self) -> None:
        admitted = self.decisions["handoff_rotation_repair_transfer_payload"]

        self.assertTrue(admitted.admitted)
        self.assertEqual(
            admitted.outcome,
            "ADMITTED_INDEPENDENT_DOMAIN_NATIVE_TRANSFER_REVIEW_ONLY",
        )
        self.assertEqual(
            self.result.independent_transfer_packets,
            ("handoff_rotation_repair_transfer_payload",),
        )
        self.assertEqual(self.result.selected_next_packet, t560.NEXT_PACKET)

    def test_all_gates_pass(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t559_independent_transfer_authority"].passed)
        self.assertTrue(self.gates["family_contract_frozen"].passed)
        self.assertTrue(self.gates["independent_transfer_fixture_declared"].passed)
        self.assertTrue(self.gates["admitted_transfer_survives_absorber_screen"].passed)

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

    def test_markdown_reports_transfer_and_next_packet(self) -> None:
        markdown = t560.render_markdown(self.payload)

        self.assertIn("T560 Results", markdown)
        self.assertIn("handoff_rotation_repair_transfer_payload", markdown)
        self.assertIn("t559_payload_replay_control", markdown)
        self.assertIn(t560.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
