"""Tests for T576 hostile-search scope closure."""

from __future__ import annotations

import json
import unittest

from models import (
    t575_domain_native_sheaf_transport_hostile_counterfamily_search_gate as t575,
)
from models import (
    t576_domain_native_sheaf_transport_hostile_search_scope_closure_gate as t576,
)


class DomainNativeSheafTransportHostileSearchScopeClosureGateTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t576.run_t576_analysis()
        cls.payload = t576.t576_result_to_dict(cls.result)
        cls.axes = {item.axis_id: item for item in cls.result.scope_axes}
        cls.checks = {item.check_id: item for item in cls.result.closure_checks}
        cls.decisions = {
            item.decision_id: item for item in cls.result.route_decisions
        }
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t575_authority(self) -> None:
        self.assertEqual(self.result.artifact, t576.ARTIFACT)
        self.assertEqual(self.result.verdict, t576.VERDICT)
        self.assertEqual(self.result.scope_status, t576.SCOPE_STATUS)
        self.assertEqual(self.result.source_law_status, t576.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t575_verdict, t575.VERDICT)
        self.assertEqual(self.result.source_t575_selected_next_packet, t575.NEXT_PACKET)
        self.assertTrue(self.gates["t575_authority"].passed)

    def test_declared_scope_axes_all_pass(self) -> None:
        expected_axes = {
            "frozen_source_roles",
            "absorber_boundaries",
            "semantic_requirements",
            "rejected_shortcut_classes",
            "independent_survivor_families",
            "route_history_pressure",
        }
        self.assertEqual(set(self.axes), expected_axes)
        self.assertTrue(all(axis.passed for axis in self.result.scope_axes))
        self.assertIn("audit_refinement", self.axes["frozen_source_roles"].observed)
        self.assertIn(
            "record_provenance_completion",
            self.axes["absorber_boundaries"].observed,
        )
        self.assertIn(
            "native_payload_forcing",
            self.axes["semantic_requirements"].observed,
        )

    def test_shortcuts_and_survivor_families_are_covered(self) -> None:
        shortcut_axis = self.axes["rejected_shortcut_classes"]
        survivor_axis = self.axes["independent_survivor_families"]

        self.assertEqual(len(shortcut_axis.required), 6)
        self.assertTrue(set(shortcut_axis.required) <= set(shortcut_axis.observed))
        self.assertEqual(
            set(survivor_axis.required),
            {"escrow_epoch_repair_family", "quorum_manifest_repair_family"},
        )
        self.assertTrue(survivor_axis.passed)
        self.assertTrue(self.checks["survivors_and_rejections_balanced"].passed)

    def test_finite_scope_closed_but_source_law_not_earned(self) -> None:
        self.assertTrue(self.result.finite_scope_closed)
        self.assertTrue(self.result.hostile_search_completed)
        self.assertFalse(self.result.true_counterfamily_found)
        self.assertFalse(self.result.route_breaks)
        self.assertTrue(self.result.route_kept_open)
        self.assertFalse(self.result.source_law_earned)
        self.assertTrue(self.gates["finite_scope_closed_review_only"].passed)

    def test_firebreak_is_selected_and_protected_shortcuts_blocked(self) -> None:
        self.assertEqual(
            self.decisions["promote_source_law_now"].outcome,
            "BLOCKED_FIREBREAK_REQUIRED",
        )
        self.assertEqual(
            self.decisions["close_hostile_search_scope"].outcome,
            "SELECTED_SCOPE_CLOSED_REVIEW_ONLY",
        )
        selected = self.decisions["run_source_law_firebreak"]
        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t576.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t576.NEXT_PACKET)
        self.assertTrue(self.gates["source_law_firebreak_selected_next"].passed)
        self.assertTrue(self.gates["protected_boundaries_preserved"].passed)

    def test_taf4_taf8_s1_and_cross_repo_movement_remain_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_scope_closure"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_scope_closure"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )

    def test_all_gates_pass_and_markdown_reports_t577(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t576.render_markdown(self.payload)

        self.assertIn("T576 Results", markdown)
        self.assertIn("## Scope Axes", markdown)
        self.assertIn(t576.NEXT_PACKET, markdown)

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
