"""Focused tests for T587 T586 causal-collapse boundary attack."""

from __future__ import annotations

import json
import unittest

from models import t587_t586_causal_collapse_boundary_attack as t587


class T586CausalCollapseBoundaryAttackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t587.run_t587_analysis()
        cls.payload = t587.result_to_dict(cls.result)
        cls.comparators = {
            item.comparator_id: item for item in cls.result.comparators
        }
        cls.audits = {item.audit_id: item for item in cls.result.audits}
        cls.checks = {item.check_id: item for item in cls.result.checks}
        cls.boundary = {
            item.class_id: item for item in cls.result.boundary_inputs
        }

    def test_verdict_is_conservative_downgrade(self) -> None:
        self.assertEqual(self.result.verdict, t587.VERDICT)
        self.assertTrue(all(check.passed for check in self.result.checks))
        self.assertIn("downgrade", self.result.adjudication)
        self.assertEqual(
            self.result.claim_ledger_update,
            "No claim-ledger or Canon Index update is earned.",
        )

    def test_untyped_dependency_exactly_reproduces_record_order(self) -> None:
        comparator = self.comparators["ordinary_task_prerequisite_dependency"]
        self.assertEqual(comparator.record_relation_status, "EQUAL")
        self.assertEqual(comparator.collapse_result, "RELATION_LEVEL_COLLAPSE")
        self.assertEqual(comparator.record_minus_comparator, ())
        self.assertEqual(comparator.comparator_minus_record, ())
        self.assertTrue(self.audits["ordinary_dependency_collapse_detected"].passed)

    def test_strongest_dependency_and_causal_order_absorb_record_order(self) -> None:
        strongest = self.comparators["strongest_standard_dependency_order"]
        causal = self.comparators["supplied_causal_order"]
        for comparator in (strongest, causal):
            self.assertEqual(comparator.record_relation_status, "RECORD_SUBRELATION")
            self.assertEqual(comparator.collapse_result, "ABSORBED_AS_TYPED_SUBRELATION")
            self.assertEqual(comparator.record_minus_comparator, ())
            self.assertGreater(len(comparator.comparator_minus_record), 0)
        self.assertTrue(
            self.audits["strongest_dependency_absorbs_record_order"].passed
        )
        self.assertTrue(self.audits["causal_order_absorbs_record_order"].passed)

    def test_boundary_screen_only_admits_issued_records(self) -> None:
        admitted = {
            class_id
            for class_id, item in self.boundary.items()
            if item.counts_as_record_source
        }
        self.assertEqual(
            admitted,
            {"physical_record_production", "native_record_issuance_rule"},
        )
        for class_id in (
            "access_change",
            "physical_intervention",
            "observer_readout",
            "continuous_source_flux",
            "stochastic_input",
        ):
            self.assertFalse(self.boundary[class_id].counts_as_record_source)
        self.assertTrue(self.audits["boundary_input_firebreak"].passed)

    def test_serialized_results_preserve_nonclaims(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t587.render_markdown(self.payload)
        self.assertIn(t587.VERDICT, dumped)
        self.assertIn("T586 Causal-Collapse Boundary Attack", markdown)
        for forbidden in (
            "time proved",
            "issuance proved",
            "source law proved",
            "causal order replaced",
            "cross-repo truth moved",
        ):
            self.assertNotIn(forbidden, dumped)


if __name__ == "__main__":
    unittest.main()
