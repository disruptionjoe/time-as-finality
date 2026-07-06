"""Tests for T473: observer-shadow indexed-composition gate."""

from __future__ import annotations

import unittest

from models.observer_shadow_indexed_composition_gate import (
    T473Result,
    run_t473_analysis,
    t473_result_to_dict,
)


class ObserverShadowIndexedCompositionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t473_analysis()
        cls.route_cases = {case.case_id: case for case in cls.result.route_cases}

    def test_run_returns_t473_result(self) -> None:
        self.assertIsInstance(self.result, T473Result)

    def test_verdict_is_bookkeeping_only(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "INDEXED_COMPOSITION_GATE_BUILT_ASSOCIATIVE_BOOKKEEPING_ONLY",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")
        self.assertFalse(self.result.global_category_theorem_supported)

    def test_transport_fixture_is_associative_up_to_structural_fields(self) -> None:
        fixture = self.result.transport_fixture
        self.assertTrue(fixture.structurally_associative)
        self.assertTrue(fixture.forgotten_index_associative)
        self.assertFalse(fixture.category_evidence)
        self.assertEqual(
            fixture.classification,
            "finite_indexed_transport_composition_associative",
        )

    def test_transport_indexed_bookkeeping_is_association_invariant(self) -> None:
        case = self.route_cases["transport_indexed_bookkeeping_threefold"]
        self.assertTrue(case.association_invariant)
        self.assertTrue(case.admitted)
        self.assertEqual(case.final_route, "indexed_bookkeeping_route")
        self.assertEqual(case.classification, "associative_indexed_bookkeeping_only")
        self.assertFalse(case.category_evidence)

    def test_losskernel_preservation_controls_compose_as_finite_control(self) -> None:
        case = self.route_cases["losskernel_preservation_threefold"]
        self.assertTrue(case.association_invariant)
        self.assertTrue(case.admitted)
        self.assertEqual(case.final_route, "preservation_control_route")
        self.assertTrue(case.counts_as_preservation_control)
        self.assertFalse(case.category_evidence)

    def test_absorber_completion_taints_composition(self) -> None:
        case = self.route_cases["losskernel_absorber_taints_composition"]
        self.assertTrue(case.association_invariant)
        self.assertTrue(case.admitted)
        self.assertEqual(case.final_route, "absorber_completion_route")
        self.assertEqual(
            case.classification,
            "absorber_completion_blocks_category_evidence",
        )
        self.assertFalse(case.counts_as_preservation_control)
        self.assertFalse(case.category_evidence)

    def test_rejected_t472_packet_blocks_composition(self) -> None:
        case = self.route_cases["endpoint_rejection_blocks_composition"]
        self.assertFalse(case.admitted)
        self.assertEqual(case.final_route, "reject_unadmitted_packet")
        self.assertEqual(case.classification, "blocked_by_t472_rejection")

    def test_cross_family_composition_requires_bridge(self) -> None:
        case = self.route_cases["cross_family_bridge_missing"]
        self.assertFalse(case.admitted)
        self.assertEqual(case.final_route, "reject_no_cross_family_bridge")
        self.assertEqual(case.classification, "blocked_by_missing_cross_family_bridge")
        self.assertFalse(self.result.cross_family_composition_supported)

    def test_summary_flags_block_category_reading(self) -> None:
        self.assertTrue(self.result.indexed_bookkeeping_associative_in_fixture)
        self.assertFalse(self.result.absorber_completion_category_evidence)
        self.assertFalse(self.result.global_category_theorem_supported)
        self.assertIn("observer-shadow category theorem", self.result.not_earned)

    def test_serializes_to_dict(self) -> None:
        payload = t473_result_to_dict(self.result)
        self.assertEqual(
            payload["artifact_id"],
            "T473-observer-shadow-indexed-composition-gate-v0.1",
        )
        self.assertIn("transport_fixture", payload)
        self.assertIn("route_cases", payload)
        self.assertFalse(payload["global_category_theorem_supported"])


if __name__ == "__main__":
    unittest.main()
