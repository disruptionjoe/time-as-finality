"""Tests for T127: same-neighbor-data LossKernel audit."""

from __future__ import annotations

import unittest

from models.same_neighbor_data_losskernel_audit import (
    case_verdict,
    cases,
    derived_obligation,
    neighbor_signature,
    run_t127_analysis,
)


class SameNeighborDataLossKernelAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {case.name: case for case in cases()}
        self.result = run_t127_analysis()
        self.pairs = {audit.pair_id: audit for audit in self.result.pair_audits}
        self.single = {
            audit.case_name: audit for audit in self.result.single_case_audits
        }

    def test_positive_attempt_is_absorbed_before_losskernel(self) -> None:
        audit = self.pairs["positive_attempt"]

        self.assertEqual(audit.classification, "absorbed_by_neighbor")
        self.assertFalse(audit.same_neighbor_data)
        self.assertEqual(audit.first_absorber, "csp_explanation")
        self.assertIn("csp", audit.differing_neighbor_fields)
        self.assertNotEqual(audit.left_obligation, audit.right_obligation)

    def test_label_only_control_keeps_same_verdict(self) -> None:
        left = self.cases["label_only_control_a"]
        right = self.cases["label_only_control_b"]
        audit = self.pairs["label_only_control"]

        self.assertEqual(derived_obligation(left), derived_obligation(right))
        self.assertEqual(case_verdict(left), case_verdict(right))
        self.assertEqual(audit.classification, "label_only")

    def test_endpoint_difference_control_is_rejected(self) -> None:
        audit = self.pairs["endpoint_difference_control"]

        self.assertEqual(audit.classification, "invalid_quotient")
        self.assertEqual(audit.right_verdict, "inadmissible_no_target_obstruction")

    def test_path_metadata_control_is_not_strict_separation(self) -> None:
        audit = self.pairs["path_metadata_control"]

        self.assertEqual(audit.classification, "invalid_quotient")
        self.assertEqual(audit.first_absorber, "path_sensitive_bookkeeping")

    def test_same_neighbor_alias_forces_same_obligation(self) -> None:
        left = self.cases["same_neighbor_alias_a"]
        right = self.cases["same_neighbor_alias_b"]
        audit = self.pairs["same_neighbor_alias"]

        self.assertEqual(neighbor_signature(left), neighbor_signature(right))
        self.assertEqual(derived_obligation(left), derived_obligation(right))
        self.assertTrue(audit.same_neighbor_data)
        self.assertEqual(audit.classification, "demote")

    def test_absorbed_loss_control_is_demoted(self) -> None:
        audit = self.single["absorbed_loss_control"]

        self.assertEqual(audit.classification, "demote")
        self.assertEqual(audit.obligation, ())
        self.assertEqual(audit.verdict, "demote_non_attribution_relevant_loss")

    def test_result_is_negative_for_strict_separation(self) -> None:
        self.assertFalse(self.result.strict_separation_found)
        self.assertTrue(self.result.positive_attempt_absorbed)
        self.assertTrue(self.result.same_neighbor_alias_collapses)
        self.assertIn("No strict same-neighbor-data LossKernel witness survives", self.result.strongest_claim)
        self.assertIn("current finite fixture family", self.result.claim_ledger_update)


if __name__ == "__main__":
    unittest.main()

