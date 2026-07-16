"""Focused tests for T586 record-capability order gate."""

from __future__ import annotations

import json
import unittest

from models import t586_record_capability_order_gate as t586


class RecordCapabilityOrderGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = t586.run_t586_analysis()
        cls.payload = t586.result_to_dict(cls.result)
        cls.audits = {item.audit_id: item for item in cls.result.audits}
        cls.checks = {item.check_id: item for item in cls.result.checks}
        cls.closure = frozenset(cls.result.order_report.closure)

    def test_verdict_and_review_boundary(self) -> None:
        self.assertEqual(self.result.verdict, t586.VERDICT)
        self.assertTrue(all(check.passed for check in self.result.checks))
        self.assertEqual(
            self.result.claim_ledger_update,
            "No claim-ledger or Canon Index update is earned.",
        )

    def test_record_dependency_closure_is_expected_partial_order(self) -> None:
        expected = frozenset(
            {
                ("seed_known_record", "copy_known_record"),
                ("seed_known_record", "erase_standard_record"),
                ("seed_known_record", "certify_erased_record"),
                ("copy_known_record", "erase_standard_record"),
                ("copy_known_record", "certify_erased_record"),
                ("erase_standard_record", "certify_erased_record"),
            }
        )
        self.assertEqual(self.closure, expected)
        self.assertTrue(self.result.order_report.strict_partial_order)
        self.assertEqual(self.result.order_report.failure_class, "NONE")

    def test_independent_event_stays_incomparable(self) -> None:
        self.assertNotIn(("prepare_biased_reference", "seed_known_record"), self.closure)
        self.assertNotIn(("seed_known_record", "prepare_biased_reference"), self.closure)
        self.assertTrue(self.checks["record_order_is_partial_not_total"].passed)

    def test_cycle_counterexample_is_rejected(self) -> None:
        cycle = self.result.cycle_counterexample
        self.assertFalse(cycle.strict_partial_order)
        self.assertEqual(cycle.failure_class, "CIRCULAR_RECORD_DEPENDENCY")
        self.assertTrue(self.audits["cycle_counterexample_rejected"].passed)

    def test_controls_do_not_reduce_order_to_clock_entropy_or_causal_superset(self) -> None:
        self.assertTrue(self.audits["clock_label_control"].passed)
        self.assertEqual(self.audits["clock_label_control"].relation, "CLOCK_LABELS_NOT_USED")
        self.assertTrue(self.audits["entropy_scalar_control"].passed)
        self.assertTrue(self.audits["causal_overread_control"].passed)
        self.assertTrue(self.audits["irreversible_computation_control"].passed)

    def test_source_input_is_t585_review_only_fixture(self) -> None:
        self.assertTrue(self.checks["t585_verdict_available"].passed)
        self.assertTrue(self.checks["t585_erasure_capability_nontrivial"].passed)
        self.assertIn("T585", self.result.source_input)

    def test_serialized_results_preserve_nonclaims(self) -> None:
        dumped = json.dumps(self.payload, sort_keys=True)
        markdown = t586.render_markdown(self.payload)
        self.assertIn(t586.VERDICT, dumped)
        self.assertIn("Record-Capability Order Gate", markdown)
        for forbidden in (
            "physical time proved",
            "issuance proved",
            "causal order replaced",
            "cross-repo truth moved",
        ):
            self.assertNotIn(forbidden, dumped)


if __name__ == "__main__":
    unittest.main()
