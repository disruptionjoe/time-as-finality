"""Tests for T470: observer-shadow composition gate."""

from __future__ import annotations

import unittest

from models.observer_shadow_composition_gate import (
    T470Result,
    run_t470_analysis,
    t470_result_to_dict,
)


class ObserverShadowCompositionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = run_t470_analysis()
        cls.checks = {check.check_id: check for check in cls.result.checks}

    def test_run_returns_t470_result(self) -> None:
        self.assertIsInstance(self.result, T470Result)

    def test_verdict_is_no_promotion_gate(self) -> None:
        self.assertEqual(
            self.result.verdict,
            "OBSERVER_SHADOW_SCHEMA_BUILT_INDEXED_COMPLETION_REQUIRED_NO_PROMOTION",
        )
        self.assertEqual(self.result.claim_ledger_update, "none")

    def test_shared_schema_expresses_both_families(self) -> None:
        families = {obj.family for obj in self.result.objects}
        self.assertIn("typed_transport", families)
        self.assertIn("losskernel", families)
        self.assertTrue(self.result.shared_schema_expresses_both_families)

    def test_endpoint_only_transport_fails(self) -> None:
        check = self.checks["transport_endpoint_only_collapse"]
        self.assertTrue(check.same_shadow)
        self.assertFalse(check.capability_equivalent)
        self.assertFalse(check.protection_preserved)
        self.assertEqual(check.classification, "composition_requires_path_index")

    def test_path_indexed_transport_repairs_bookkeeping(self) -> None:
        check = self.checks["transport_path_indexed_completion"]
        self.assertFalse(check.same_shadow)
        self.assertTrue(check.protection_preserved)
        self.assertEqual(check.classification, "separated_after_completion")

    def test_losskernel_neighbor_factoring_preserves(self) -> None:
        check = self.checks["losskernel_neighbor_factoring_preserves"]
        self.assertTrue(check.same_shadow)
        self.assertTrue(check.capability_equivalent)
        self.assertTrue(check.protection_preserved)
        self.assertEqual(check.classification, "verdict_preserved")

    def test_losskernel_hidden_source_omission_fails(self) -> None:
        check = self.checks["losskernel_hidden_source_omitted"]
        self.assertTrue(check.same_shadow)
        self.assertFalse(check.capability_equivalent)
        self.assertFalse(check.protection_preserved)
        self.assertEqual(check.classification, "state_completion_required")

    def test_losskernel_hidden_source_completion_repairs_bookkeeping(self) -> None:
        check = self.checks["losskernel_hidden_source_completed"]
        self.assertFalse(check.same_shadow)
        self.assertTrue(check.protection_preserved)
        self.assertEqual(check.classification, "separated_after_completion")

    def test_endpoint_only_global_category_not_supported(self) -> None:
        self.assertFalse(self.result.endpoint_only_global_category_supported)
        self.assertTrue(self.result.indexed_atlas_required)

    def test_serializes_to_dict(self) -> None:
        payload = t470_result_to_dict(self.result)
        self.assertIn("objects", payload)
        self.assertIn("checks", payload)
        self.assertIn("family_summaries", payload)
        self.assertEqual(payload["claim_ledger_update"], "none")


if __name__ == "__main__":
    unittest.main()
