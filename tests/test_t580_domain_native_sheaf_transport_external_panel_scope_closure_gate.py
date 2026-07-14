"""Tests for T580 external-panel scope closure gate."""

from __future__ import annotations

import json
import unittest

from models import (
    t579_domain_native_sheaf_transport_out_of_panel_absorber_probe_gate as t579,
)
from models import (
    t580_domain_native_sheaf_transport_external_panel_scope_closure_gate as t580,
)


class DomainNativeSheafTransportExternalPanelScopeClosureGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t580.run_t580_analysis()
        cls.payload = t580.t580_result_to_dict(cls.result)
        cls.axes = {item.axis_id: item for item in cls.result.scope_axes}
        cls.decisions = {item.decision_id: item for item in cls.result.scope_decisions}
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t579_authority(self) -> None:
        self.assertEqual(self.result.artifact, t580.ARTIFACT)
        self.assertEqual(self.result.verdict, t580.VERDICT)
        self.assertEqual(self.result.scope_status, t580.SCOPE_STATUS)
        self.assertEqual(self.result.package_status, t580.PACKAGE_STATUS)
        self.assertEqual(self.result.source_law_status, t580.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t579_verdict, t579.VERDICT)
        self.assertEqual(self.result.source_t579_selected_next_packet, t579.NEXT_PACKET)
        self.assertTrue(self.gates["t579_authority"].passed)

    def test_all_review_scope_axes_are_declared_and_covered(self) -> None:
        expected = {
            "internal_route_scope",
            "external_absorber_scope",
            "empirical_detector_scope",
            "continuum_taf4_scope",
            "cross_domain_taf8_scope",
            "future_reopen_scope",
        }

        self.assertEqual(set(self.axes), expected)
        self.assertTrue(all(axis.covered_for_review for axis in self.result.scope_axes))
        self.assertTrue(self.gates["review_scope_axes_declared"].passed)

    def test_scope_closure_does_not_expand_panel_without_new_packet(self) -> None:
        self.assertTrue(self.result.current_external_panel_closed)
        self.assertFalse(self.result.immediate_expansion_required)
        self.assertEqual(
            self.decisions["expand_absorber_panel_now"].outcome,
            "BLOCKED_AS_CHURN_WITHOUT_NEW_PACKET",
        )
        self.assertTrue(self.gates["no_immediate_panel_expansion"].passed)

    def test_scope_closure_is_not_source_law_promotion(self) -> None:
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(
            self.decisions["promote_taf11_source_law"].outcome,
            "BLOCKED_SCOPE_CLOSURE_IS_NOT_PROMOTION",
        )
        self.assertTrue(self.gates["scope_closure_not_promotion"].passed)

    def test_review_package_closeout_router_is_selected_next(self) -> None:
        selected = self.decisions["route_to_review_package_closeout"]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t580.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t580.NEXT_PACKET)
        self.assertTrue(self.gates["closeout_router_selected"].passed)

    def test_downstream_and_governance_shortcuts_are_blocked(self) -> None:
        for axis in self.result.scope_axes:
            self.assertTrue(axis.stronger_reading_blocked)
        self.assertEqual(
            self.decisions["move_taf4_taf8_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["protected_movements_blocked"].passed)

    def test_all_gates_pass_and_markdown_reports_t581(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t580.render_markdown(self.payload)

        self.assertIn("T580 Results", markdown)
        self.assertIn("## Scope Axes", markdown)
        self.assertIn(t580.NEXT_PACKET, markdown)
        self.assertIn(t580.SCOPE_STATUS, markdown)

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
