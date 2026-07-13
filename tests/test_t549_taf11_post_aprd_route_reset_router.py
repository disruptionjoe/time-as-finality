"""Tests for T549 TAF11 post-APRD route reset router."""

from __future__ import annotations

import json
import unittest

from models import t548_aprd_cross_family_prediction_stress_packet as t548
from models import t549_taf11_post_aprd_route_reset_router as t549


class TAF11PostAPRDRouteResetRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t549.run_t549_analysis()
        cls.payload = t549.t549_result_to_dict(cls.result)
        cls.decisions = {
            decision.candidate_id: decision
            for decision in cls.result.candidate_decisions
        }

    def test_artifact_identity_and_t548_source_state(self) -> None:
        self.assertEqual(self.result.artifact, t549.ARTIFACT)
        self.assertEqual(self.result.verdict, t549.VERDICT)
        self.assertEqual(self.result.post_aprd_status, t549.POST_APRD_STATUS)
        self.assertEqual(self.result.source_t548_verdict, t548.VERDICT)
        self.assertEqual(
            self.result.source_t548_status,
            t548.APRD_CROSS_FAMILY_STATUS,
        )
        self.assertEqual(self.result.source_t548_cross_family_survivors, ())
        self.assertIn(
            "stress_protocol_stack_missing_sybil_layer",
            self.result.source_t548_narrowed_cases,
        )

    def test_exactly_one_route_is_selected(self) -> None:
        self.assertEqual(self.result.selected_route_ids, (t549.SELECTED_ROUTE,))
        selected = self.decisions[t549.SELECTED_ROUTE]

        self.assertEqual(selected.outcome, "SELECTED_FOR_EXECUTION")
        self.assertTrue(selected.selected_for_next_execution)
        self.assertEqual(selected.track_role, "track_1_next_packet")
        self.assertEqual(selected.missing_requirements, ())
        self.assertEqual(selected.next_packet, t549.NEXT_PACKET)

    def test_selected_route_contract_declares_layers_and_falsifiers(self) -> None:
        selected = self.decisions[t549.SELECTED_ROUTE]
        variables = set(selected.source_variables)

        self.assertIn("issuance_layer", variables)
        self.assertIn("access_control_layer", variables)
        self.assertIn("admissibility_layer", variables)
        self.assertIn("provenance_layer", variables)
        self.assertIn("record_finality_layer", variables)
        self.assertIn("collapse_mode_prediction", variables)
        self.assertIn("post-hoc", selected.predeclared_falsifier)
        self.assertIn("cross-repo truth", selected.predeclared_falsifier)
        self.assertIn("TAF4/source-law status", selected.predeclared_falsifier)

    def test_broad_new_family_and_taf8_pause_are_not_selected(self) -> None:
        broad = self.decisions["fresh_source_law_family_menu"]
        taf8_pause = self.decisions["taf8_pause_until_domain_native_packet"]

        self.assertEqual(broad.outcome, "REVIEW_ONLY_UNDERDECLARED")
        self.assertIn("source_variables_declared", broad.missing_requirements)
        self.assertIn("executable_next_packet_specific", broad.missing_requirements)
        self.assertFalse(broad.selected_for_next_execution)

        self.assertEqual(
            taf8_pause.outcome,
            "PAUSED_TAF8_WAITING_FOR_DOMAIN_NATIVE_PACKET",
        )
        self.assertIn(
            "domain_native_taf8_packet_in_hand",
            taf8_pause.missing_requirements,
        )
        self.assertFalse(taf8_pause.selected_for_next_execution)

    def test_aprd_replay_taf4_track_two_and_governance_are_blocked(self) -> None:
        aprd = self.decisions["deepen_or_retune_aprd_family"]
        taf4 = self.decisions["taf4_from_aprd_continuum_bridge"]
        track_two = self.decisions["taf12_data_packet_wait"]
        governance = self.decisions["s1_claim_or_public_posture_shortcut"]

        self.assertEqual(aprd.outcome, "REJECTED_APRD_REPLAY")
        self.assertIn("no_aprd_route_replay", aprd.missing_requirements)
        self.assertEqual(taf4.outcome, "BLOCKED_TAF4_OVERREAD")
        self.assertIn("no_taf4_movement_from_aprd", taf4.missing_requirements)
        self.assertEqual(track_two.outcome, "PAUSED_TRACK_2")
        self.assertEqual(governance.outcome, "BLOCKED_GOVERNANCE")
        for decision in (aprd, taf4, track_two, governance):
            self.assertFalse(decision.selected_for_next_execution)

    def test_quantum_access_miss_stays_secondary_lane(self) -> None:
        quantum = self.decisions["quantum_access_structure_immediate_theorem"]

        self.assertEqual(quantum.outcome, "REVIEW_ONLY_SECONDARY_LANE")
        self.assertIn("not_secondary_lane_only", quantum.missing_requirements)
        self.assertFalse(quantum.selected_for_next_execution)

    def test_no_claim_or_posture_movement(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        self.assertIn("No claim-ledger update is earned", dumped)
        forbidden = (
            "source law established",
            "claim status changed",
            "Canon Index moved",
            "public posture authorized",
            "external publication authorized",
            "cross-repo truth proved",
            "TAF4 unblocked",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, dumped)

    def test_markdown_reports_selected_route_contract(self) -> None:
        markdown = t549.render_markdown(self.payload)

        self.assertIn("T549 Results", markdown)
        self.assertIn("## Selected Route Contract", markdown)
        self.assertIn(f"`{t549.SELECTED_ROUTE}`", markdown)
        self.assertIn(f"`{t549.NEXT_PACKET}`", markdown)
        self.assertIn("Source T548 cross-family survivors: none", markdown)


if __name__ == "__main__":
    unittest.main()
