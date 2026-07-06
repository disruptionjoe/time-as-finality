"""Tests for T472: observer-shadow index admission gate."""

from __future__ import annotations

import unittest

from models.observer_shadow_index_admission_gate import (
    T472Result,
    run_t472_analysis,
    t472_result_to_dict,
)


class ObserverShadowIndexAdmissionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t472_analysis()
        cls.admissions = {
            admission.packet_id: admission for admission in cls.result.admissions
        }

    def test_run_returns_t472_result(self) -> None:
        self.assertIsInstance(self.result, T472Result)

    def test_verdict_is_no_promotion_gate(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "OBSERVER_SHADOW_INDEX_GATE_BUILT_COMPLETION_SEPARATED_NO_PROMOTION",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")
        self.assertFalse(self.result.global_category_theorem_supported)

    def test_transport_endpoint_only_packet_is_rejected(self) -> None:
        admission = self.admissions["transport_endpoint_only_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(
            admission.route_label,
            "reject_missing_load_bearing_indices",
        )
        self.assertIn("path_label", admission.missing_indices)
        self.assertIn("accumulated_forgotten_structure", admission.missing_indices)

    def test_transport_path_indexed_packet_is_admitted_as_bookkeeping(self) -> None:
        admission = self.admissions["transport_path_indexed_packet"]
        self.assertTrue(admission.admitted)
        self.assertEqual(admission.route_label, "admitted_indexed_completion")
        self.assertFalse(admission.same_shadow)
        self.assertTrue(admission.protection_preserved)
        self.assertFalse(admission.counts_as_preservation_control)

    def test_losskernel_neighbor_packet_is_genuine_preservation_control(self) -> None:
        admission = self.admissions["losskernel_neighbor_preservation_packet"]
        self.assertTrue(admission.admitted)
        self.assertEqual(admission.route_label, "admitted_preservation_control")
        self.assertTrue(admission.same_shadow)
        self.assertTrue(admission.capability_equivalent)
        self.assertTrue(admission.counts_as_preservation_control)

    def test_losskernel_hidden_source_omission_is_rejected(self) -> None:
        admission = self.admissions["losskernel_hidden_source_omitted_packet"]
        self.assertFalse(admission.admitted)
        self.assertEqual(admission.route_label, "reject_missing_load_bearing_indices")
        self.assertIn("hidden_source_datum", admission.missing_indices)

    def test_losskernel_hidden_source_completion_routes_to_absorber(self) -> None:
        admission = self.admissions["losskernel_hidden_source_completed_packet"]
        self.assertTrue(admission.admitted)
        self.assertEqual(admission.route_label, "absorber_completion_recorded")
        self.assertFalse(admission.counts_as_preservation_control)
        self.assertIn(admission.packet_id, self.result.absorber_completions)

    def test_summary_buckets_are_separated(self) -> None:
        self.assertEqual(
            self.result.admitted_preservation_controls,
            ("losskernel_neighbor_preservation_packet",),
        )
        self.assertEqual(
            self.result.admitted_indexed_completions,
            ("transport_path_indexed_packet",),
        )
        self.assertEqual(
            self.result.absorber_completions,
            ("losskernel_hidden_source_completed_packet",),
        )
        self.assertIn("transport_endpoint_only_packet", self.result.rejected_packets)
        self.assertIn(
            "losskernel_hidden_source_omitted_packet",
            self.result.rejected_packets,
        )

    def test_serializes_to_dict(self) -> None:
        payload = t472_result_to_dict(self.result)
        self.assertEqual(
            payload["artifact_id"],
            "T472-observer-shadow-index-admission-gate-v0.1",
        )
        self.assertIn("admissions", payload)
        self.assertFalse(payload["global_category_theorem_supported"])


if __name__ == "__main__":
    unittest.main()
