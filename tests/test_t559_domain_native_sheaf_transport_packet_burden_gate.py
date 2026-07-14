"""Tests for T559 domain-native sheaf transport packet burden gate."""

from __future__ import annotations

import json
import unittest

from models import t558_sheaf_obstruction_transport_source_law_packet as t558
from models import t559_domain_native_sheaf_transport_packet_burden_gate as t559


class DomainNativeSheafTransportPacketBurdenGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t559.run_t559_analysis()
        cls.payload = t559.t559_result_to_dict(cls.result)
        cls.decisions = {
            decision.case_id: decision for decision in cls.result.case_decisions
        }
        cls.gates = {gate.gate_id: gate for gate in cls.result.gate_decisions}

    def test_artifact_identity_and_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t559.ARTIFACT)
        self.assertEqual(self.result.verdict, t559.VERDICT)
        self.assertEqual(self.result.packet_status, t559.PACKET_STATUS)
        self.assertEqual(self.result.source_t558_verdict, t558.VERDICT)
        self.assertEqual(self.result.source_t558_selected_next_packet, t558.NEXT_PACKET)

    def test_frozen_contract_is_preserved(self) -> None:
        source_t558 = t558.run_t558_analysis()

        self.assertEqual(self.result.frozen_source_variables, source_t558.frozen_source_variables)
        self.assertEqual(self.result.frozen_mature_absorbers, source_t558.frozen_mature_absorbers)
        self.assertEqual(self.result.frozen_falsifiers, source_t558.frozen_falsifiers)

    def test_absorber_controls_are_exercised(self) -> None:
        self.assertEqual(
            self.decisions["ordinary_gluing_domain_payload_control"].outcome,
            "ABSORBED_ORDINARY_SHEAF_GLUE",
        )
        self.assertEqual(
            self.decisions["resource_budget_transport_control"].outcome,
            "ABSORBED_RESOURCE_TRANSPORT_MONOTONE",
        )
        self.assertEqual(
            self.decisions["consensus_state_machine_payload_control"].outcome,
            "ABSORBED_CONSENSUS_STATE_MACHINE",
        )
        self.assertEqual(
            self.decisions["record_provenance_completion_payload_control"].outcome,
            "ABSORBED_RECORD_PROVENANCE_COMPLETION",
        )

    def test_declared_falsifiers_and_spent_routes_are_exercised(self) -> None:
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
            self.decisions["observerse_replay_control"].outcome,
            "REJECTED_OBSERVERSE_REPLAY",
        )
        self.assertEqual(
            self.decisions["aprd_replay_control"].outcome,
            "REJECTED_APRD_REPLAY",
        )

    def test_domain_native_payload_is_admitted_review_only(self) -> None:
        admitted = self.decisions["record_finality_transport_square_payload"]

        self.assertTrue(admitted.admitted)
        self.assertEqual(
            admitted.outcome,
            "ADMITTED_DOMAIN_NATIVE_BURDEN_PACKET_REVIEW_ONLY",
        )
        self.assertEqual(
            self.result.admitted_domain_native_packets,
            ("record_finality_transport_square_payload",),
        )
        self.assertEqual(self.result.selected_next_packet, t559.NEXT_PACKET)

    def test_all_gates_pass(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        self.assertTrue(self.gates["t558_domain_native_burden_authority"].passed)
        self.assertTrue(self.gates["family_contract_frozen"].passed)
        self.assertTrue(self.gates["domain_native_payload_present"].passed)
        self.assertTrue(self.gates["admitted_payload_survives_absorber_screen"].passed)

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

    def test_markdown_reports_payload_and_next_packet(self) -> None:
        markdown = t559.render_markdown(self.payload)

        self.assertIn("T559 Results", markdown)
        self.assertIn("## Frozen Contract", markdown)
        self.assertIn("record_finality_transport_square_payload", markdown)
        self.assertIn(t559.NEXT_PACKET, markdown)


if __name__ == "__main__":
    unittest.main()
