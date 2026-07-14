"""Tests for T579 out-of-panel absorber probe gate."""

from __future__ import annotations

import json
import unittest

from models import (
    t578_domain_native_sheaf_transport_candidate_package_limitation_gate as t578,
)
from models import (
    t579_domain_native_sheaf_transport_out_of_panel_absorber_probe_gate as t579,
)


class DomainNativeSheafTransportOutOfPanelAbsorberProbeGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t579.run_t579_analysis()
        cls.payload = t579.t579_result_to_dict(cls.result)
        cls.probes = {item.probe_id: item for item in cls.result.external_probes}
        cls.decisions = {
            item.decision_id: item for item in cls.result.package_decisions
        }
        cls.gates = {item.gate_id: item for item in cls.result.gate_decisions}

    def test_artifact_identity_and_t578_authority(self) -> None:
        self.assertEqual(self.result.artifact, t579.ARTIFACT)
        self.assertEqual(self.result.verdict, t579.VERDICT)
        self.assertEqual(self.result.panel_status, t579.PANEL_STATUS)
        self.assertEqual(self.result.package_status, t579.PACKAGE_STATUS)
        self.assertEqual(self.result.source_law_status, t579.SOURCE_LAW_STATUS)
        self.assertEqual(self.result.source_t578_verdict, t578.VERDICT)
        self.assertEqual(self.result.source_t578_selected_next_packet, t578.NEXT_PACKET)
        self.assertTrue(self.gates["t578_authority"].passed)

    def test_external_panel_is_out_of_prior_scope(self) -> None:
        expected = {
            "stochastic_thermodynamic_maintenance_absorber",
            "detector_metrology_calibration_absorber",
            "causal_set_measure_law_absorber",
            "quantum_access_structure_monogamy_absorber",
        }

        self.assertEqual(set(self.probes), expected)
        self.assertTrue(self.result.panel_is_out_of_prior_scope)
        self.assertTrue(all(not probe.prior_panel_member for probe in self.result.external_probes))
        self.assertTrue(self.gates["panel_out_of_prior_scope"].passed)

    def test_every_probe_absorbs_source_law_overread_without_breaking_review_package(self) -> None:
        self.assertFalse(self.result.package_broken_by_external_panel)
        self.assertTrue(
            all(probe.absorbs_source_law_reading for probe in self.result.external_probes)
        )
        self.assertFalse(any(probe.breaks_package for probe in self.result.external_probes))
        self.assertTrue(self.gates["source_law_absorbed_not_earned"].passed)
        self.assertTrue(self.gates["package_survives_limited_review"].passed)

    def test_package_retained_limited_and_source_law_promotion_blocked(self) -> None:
        self.assertTrue(self.result.package_survives_as_limited_review)
        self.assertFalse(self.result.source_law_earned)
        self.assertEqual(
            self.decisions["promote_source_law_after_external_probe"].outcome,
            "BLOCKED_EXTERNAL_ABSORBERS_LOAD_BEARING",
        )
        self.assertEqual(
            self.decisions["retain_limited_review_package"].outcome,
            "SELECTED_LIMITED_REVIEW_RETENTION",
        )

    def test_external_panel_scope_closure_is_selected_next(self) -> None:
        selected = self.decisions["run_external_panel_scope_closure"]

        self.assertTrue(selected.selected)
        self.assertEqual(selected.next_packet, t579.NEXT_PACKET)
        self.assertEqual(self.result.selected_next_packet, t579.NEXT_PACKET)
        self.assertTrue(self.gates["external_scope_closure_selected"].passed)

    def test_taf4_taf8_s1_cross_repo_and_public_shortcuts_are_blocked(self) -> None:
        self.assertEqual(
            self.decisions["move_taf4_from_t579"].outcome,
            "BLOCKED_TAF4_OVERREAD",
        )
        self.assertEqual(
            self.decisions["execute_taf8_from_t579"].outcome,
            "BLOCKED_TAF8_OVERREAD",
        )
        self.assertEqual(
            self.decisions["move_s1_or_cross_repo_truth"].outcome,
            "BLOCKED_GOVERNANCE",
        )
        self.assertTrue(self.gates["protected_boundaries_preserved"].passed)

    def test_all_gates_pass_and_markdown_reports_t580(self) -> None:
        self.assertTrue(all(gate.passed for gate in self.result.gate_decisions))
        markdown = t579.render_markdown(self.payload)

        self.assertIn("T579 Results", markdown)
        self.assertIn("## External Probes", markdown)
        self.assertIn(t579.NEXT_PACKET, markdown)
        self.assertIn(t579.PANEL_STATUS, markdown)

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
