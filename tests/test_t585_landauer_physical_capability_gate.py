"""Focused tests for T585 Landauer physical capability gate."""

from __future__ import annotations

import json
import unittest

from models import t585_landauer_physical_capability_gate as t585


class LandauerPhysicalCapabilityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t585.run_t585_analysis()
        cls.payload = t585.result_to_dict(cls.result)
        cls.audits = {item.audit_id: item for item in cls.result.audits}
        cls.checks = {item.check_id: item for item in cls.result.checks}

    def test_verdict_and_review_boundary(self) -> None:
        self.assertEqual(self.result.verdict, t585.VERDICT)
        self.assertTrue(all(check.passed for check in self.result.checks))
        self.assertEqual(
            self.result.claim_ledger_update,
            "No claim-ledger or Canon Index update is earned.",
        )

    def test_landauer_source_law_separates_memory_states(self) -> None:
        costs = self.result.landauer_costs
        self.assertEqual(costs["known_zero_record"], 0.0)
        self.assertGreater(costs["biased_record"], 0.0)
        self.assertLess(costs["biased_record"], 1.0)
        self.assertEqual(costs["max_entropy_record"], 1.0)
        audit = self.audits["source_law_capability_distinction"]
        self.assertEqual(audit.relation, "SUPERSET")
        self.assertTrue(audit.passed)

    def test_unit_and_gauge_representations_preserve_envelope(self) -> None:
        self.assertEqual(self.audits["joule_unit_representation"].relation, "EQUIVALENT")
        self.assertTrue(self.checks["unit_representation_invariant"].passed)
        self.assertEqual(self.audits["bit_label_gauge_swap"].relation, "EQUIVALENT")
        self.assertTrue(self.checks["bit_label_gauge_invariant"].passed)

    def test_irrelevant_metadata_coarse_graining_is_stable(self) -> None:
        audit = self.audits["irrelevant_metadata_coarse_graining"]
        self.assertEqual(audit.completion_class, "IRRELEVANT_COARSE_GRAINING")
        self.assertTrue(audit.passed)
        self.assertTrue(self.checks["irrelevant_coarse_graining_invariant"].passed)

    def test_completion_controls_absorb_overreads(self) -> None:
        self.assertEqual(
            self.audits["blind_distribution_access_control"].completion_class,
            "ACCESS_COMPLETION",
        )
        self.assertEqual(
            self.audits["low_work_store_budget_control"].completion_class,
            "RESOURCE_BUDGET_COMPLETION",
        )
        self.assertEqual(
            self.audits["same_display_hidden_entropy_completion"].completion_class,
            "NATIVE_STATE_COMPLETION",
        )

    def test_serialized_results_preserve_nonclaims(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t585.render_markdown(self.payload)
        self.assertIn(t585.VERDICT, dumped)
        self.assertIn("Landauer Physical Capability Gate", markdown)
        for forbidden in (
            "time derived",
            "issuance proved",
            "source law proved",
            "cross-repo identity proved",
        ):
            self.assertNotIn(forbidden, dumped)


if __name__ == "__main__":
    unittest.main()
