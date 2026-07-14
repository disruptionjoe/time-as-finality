"""Tests for T575 hostile counterfamily search."""

from __future__ import annotations

import json
import unittest

from models import (
    t574_domain_native_sheaf_transport_source_law_route_adjudication_gate as t574,
)
from models import (
    t575_domain_native_sheaf_transport_hostile_counterfamily_search_gate as t575,
)


class DomainNativeSheafTransportHostileCounterfamilySearchGateTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t575.run_t575_analysis()
        cls.payload = t575.t575_result_to_dict(cls.result)
        cls.evaluations = {
            item.candidate_id: item for item in cls.result.evaluations
        }
        cls.criteria = {
            item.criterion_id: item for item in cls.result.search_criteria
        }
        cls.decisions = {
            item.decision_id: item for item in cls.result.route_decisions
        }
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t574_authority(self) -> None:
        self.assertEqual(self.result.artifact, t575.ARTIFACT)
        self.assertEqual(self.result.verdict, t575.VERDICT)
        self.assertEqual(self.result.search_status, t575.SEARCH_STATUS)
        self.assertEqual(self.result.source_law_status, t575.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t574_verdict, t574.VERDICT)
        self.assertEqual(self.result.source_t574_selected_next_packet, t574.NEXT_PACKET)
        self.assertTrue(self.gates["t574_authority"].passed)

    def test_hostile_panel_has_survivors_and_rejected_controls(self) -> None:
        self.assertEqual(len(self.result.evaluations), 8)
        self.assertGreaterEqual(len(self.result.survivor_candidate_ids), 2)
        self.assertGreaterEqual(len(self.result.rejected_candidate_ids), 6)
        self.assertIn(
            "escrow_epoch_repair_hostile_survivor",
            self.result.survivor_candidate_ids,
        )
        self.assertIn(
            "trivial_same_neighbor_gluing_control",
            self.result.rejected_candidate_ids,
        )
        self.assertTrue(self.criteria["survivor_controls_present"].passed)
        self.assertTrue(self.criteria["hostile_controls_rejected"].passed)

    def test_no_true_counterfamily_found_and_route_remains_open(self) -> None:
        self.assertFalse(self.result.true_counterfamily_found)
        self.assertFalse(self.result.route_breaks)
        self.assertTrue(self.result.route_kept_open)
        self.assertEqual(self.result.true_counterfamily_ids, ())
        self.assertTrue(self.criteria["no_true_counterfamily_found"].passed)
        self.assertTrue(self.gates["true_counterfamily_absent"].passed)
        self.assertTrue(self.gates["route_remains_review_only"].passed)

    def test_source_law_promotion_blocked_and_scope_closure_selected(self) -> None:
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(
            self.decisions["promote_source_law_now"].outcome,
            "BLOCKED_PROMOTION_BAR_NOT_MET",
        )
        self.assertEqual(
            self.decisions["retire_route_due_to_true_counterfamily"].outcome,
            "PAUSED_NO_TRUE_COUNTERFAMILY_FOUND",
        )
        selected = self.decisions["run_hostile_search_scope_closure_gate"]
        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t575.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t575.NEXT_PACKET)
        self.assertTrue(self.gates["scope_closure_selected_next"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_t575"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_t575"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["protected_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t576(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t575.render_markdown(self.payload)

        self.assertIn("T575 Results", markdown)
        self.assertIn("## Candidate Evaluations", markdown)
        self.assertIn(t575.NEXT_PACKET, markdown)

    def test_json_serializable_and_avoids_forbidden_promotions(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)

        json.dumps(self.payload, sort_keys=True)
        self.assertIn("No claim-ledger update is earned", dumped)
        forbidden = (
            "source law proved",
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


if __name__ == "__main__":
    unittest.main()
