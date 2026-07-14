"""Tests for T578 candidate-package limitation gate."""

from __future__ import annotations

import json
import unittest

from models import (
    t577_domain_native_sheaf_transport_source_law_firebreak_gate as t577,
)
from models import (
    t578_domain_native_sheaf_transport_candidate_package_limitation_gate as t578,
)


class DomainNativeSheafTransportCandidatePackageLimitationGateTests(
    unittest.TestCase
):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t578.run_t578_analysis()
        cls.payload = t578.t578_result_to_dict(cls.result)
        cls.axes = {item.axis_id: item for item in cls.result.limitation_axes}
        cls.pressures = {
            item.pressure_id: item for item in cls.result.package_pressures
        }
        cls.decisions = {
            item.decision_id: item for item in cls.result.route_decisions
        }
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t577_authority(self) -> None:
        self.assertEqual(self.result.artifact, t578.ARTIFACT)
        self.assertEqual(self.result.verdict, t578.VERDICT)
        self.assertEqual(self.result.limitation_status, t578.LIMITATION_STATUS)
        self.assertEqual(self.result.source_law_status, t578.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t577_verdict, t577.VERDICT)
        self.assertEqual(self.result.source_t577_selected_next_packet, t577.NEXT_PACKET)
        self.assertEqual(self.result.source_package_label, t577.PACKAGE_LABEL)
        self.assertTrue(self.gates["t577_authority"].passed)

    def test_limitation_axes_are_exposed(self) -> None:
        expected_axes = {
            "finite_synthetic_scope",
            "route_internality",
            "absorber_panel_incompleteness",
            "downstream_bridge_absence",
            "label_status_gap",
        }

        self.assertEqual(set(self.axes), expected_axes)
        self.assertTrue(all(axis.exposed for axis in self.result.limitation_axes))
        self.assertIn(
            "declared absorber and hostile panels only",
            self.axes["absorber_panel_incompleteness"].limits_to,
        )
        self.assertIn("TAF4 blocked", self.axes["downstream_bridge_absence"].evidence)
        self.assertTrue(self.gates["limitation_axes_exposed"].passed)

    def test_package_remains_review_only_and_not_source_law(self) -> None:
        self.assertTrue(self.result.package_remains_review_only)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(
            self.pressures["source_law_promotion_pressure"].outcome,
            "BLOCKED_BY_LIMITATIONS",
        )
        self.assertEqual(
            self.decisions["promote_source_law_from_package"].outcome,
            "BLOCKED_LIMITATIONS_LOAD_BEARING",
        )
        self.assertTrue(self.gates["package_remains_review_only"].passed)

    def test_claim_canon_public_and_downstream_pressures_are_resisted(self) -> None:
        self.assertEqual(
            self.pressures["claim_canon_public_posture_pressure"].outcome,
            "BLOCKED_BY_GOVERNANCE_FIREWALL",
        )
        self.assertEqual(
            self.pressures["downstream_lane_pressure"].outcome,
            "BLOCKED_BY_NO_BRIDGE",
        )
        self.assertTrue(self.gates["package_pressures_resisted"].passed)
        self.assertTrue(self.gates["protected_boundaries_preserved"].passed)

    def test_out_of_panel_absorber_probe_is_selected_next(self) -> None:
        selected = self.decisions["run_out_of_panel_absorber_probe"]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t578.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t578.NEXT_PACKET)
        self.assertTrue(self.gates["out_of_panel_absorber_probe_selected"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_t578"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_t578"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )

    def test_all_gates_pass_and_markdown_reports_t579(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t578.render_markdown(self.payload)

        self.assertIn("T578 Results", markdown)
        self.assertIn("## Limitation Axes", markdown)
        self.assertIn(t578.NEXT_PACKET, markdown)
        self.assertIn(t578.LIMITATION_STATUS, markdown)

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
