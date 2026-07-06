"""Tests for T474: observer-shadow bridge-admission gate."""

from __future__ import annotations

import unittest

from models.observer_shadow_bridge_admission_gate import (
    T474Result,
    run_t474_analysis,
    t474_result_to_dict,
)


class ObserverShadowBridgeAdmissionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t474_analysis()
        cls.admissions = {
            admission.proposal_id: admission
            for admission in cls.result.admissions
        }
        cls.controls = {
            control.control_id: control for control in cls.result.controls
        }

    def test_run_returns_t474_result(self) -> None:
        self.assertIsInstance(self.result, T474Result)

    def test_verdict_is_atlas_bridge_only(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "CROSS_FAMILY_BRIDGE_GATE_BUILT_ATLAS_BRIDGE_ONLY_NO_CATEGORY",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")
        self.assertFalse(self.result.global_category_theorem_supported)

    def test_required_controls_are_available_from_t473(self) -> None:
        for control_id in (
            "transport_bookkeeping_positive",
            "losskernel_preservation_positive",
            "no_bridge_hostile",
            "upstream_rejection_hostile",
            "absorber_completion_hostile",
        ):
            self.assertTrue(self.controls[control_id].available, control_id)

    def test_no_declared_bridge_remains_rejected(self) -> None:
        admission = self.admissions["no_declared_bridge_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(admission.route_label, "reject_bridge_not_declared")
        self.assertEqual(admission.classification, "missing_bridge_rejection")

    def test_semantic_keyword_bridge_is_rejected(self) -> None:
        admission = self.admissions["semantic_keyword_bridge_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(admission.route_label, "reject_semantic_relabel_bridge")
        self.assertEqual(admission.classification, "semantic_relabel_rejection")
        self.assertEqual(admission.missing_controls, ())

    def test_absorber_completion_bridge_is_rejected(self) -> None:
        admission = self.admissions["absorber_completion_bridge_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(admission.route_label, "reject_absorber_completion_bridge")
        self.assertFalse(admission.counts_as_category_evidence)

    def test_direct_category_bridge_shortcut_is_rejected(self) -> None:
        admission = self.admissions["direct_category_bridge_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(admission.route_label, "reject_direct_category_shortcut")
        self.assertEqual(admission.classification, "category_shortcut_rejection")

    def test_audit_atlas_bridge_is_admitted_but_not_category_evidence(self) -> None:
        admission = self.admissions["audit_atlas_bridge_packet"]
        self.assertTrue(admission.admitted)
        self.assertEqual(admission.route_label, "admit_audit_atlas_bridge_only")
        self.assertTrue(admission.counts_as_cross_family_bridge)
        self.assertFalse(admission.counts_as_category_evidence)
        self.assertTrue(self.result.atlas_bridge_available)
        self.assertFalse(
            self.result.direct_cross_family_category_composition_supported
        )

    def test_only_audit_atlas_bridge_is_admitted(self) -> None:
        self.assertEqual(
            self.result.admitted_bridges,
            ("audit_atlas_bridge_packet",),
        )
        self.assertIn(
            "direct_category_bridge_packet",
            self.result.rejected_bridges,
        )

    def test_serializes_to_dict(self) -> None:
        payload = t474_result_to_dict(self.result)
        self.assertEqual(
            payload["artifact_id"],
            "T474-observer-shadow-bridge-admission-gate-v0.1",
        )
        self.assertIn("controls", payload)
        self.assertIn("admissions", payload)
        self.assertTrue(payload["atlas_bridge_available"])
        self.assertFalse(payload["global_category_theorem_supported"])


if __name__ == "__main__":
    unittest.main()
