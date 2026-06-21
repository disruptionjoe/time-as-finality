"""Tests for T141: T1 record-graph admissibility ledger."""

from __future__ import annotations

import unittest

from models.constructor_admissibility_grounding_audit import (
    RESOURCE_ACCOUNTING_ONLY,
    RESOURCE_CONSUMING_POSSIBLE,
    REVERSIBLE_POSSIBLE,
)
from models.t1_record_graph_admissibility_ledger import run_t141_analysis


class T1RecordGraphAdmissibilityLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t141_analysis()
        self.audits = {audit.case_id: audit for audit in self.result.audits}

    def test_required_cases_are_present(self) -> None:
        self.assertEqual(
            set(self.audits),
            {
                "access_grant_existing_record",
                "copy_to_fresh_holder",
                "branch_spread_copy",
                "access_loss_without_erasure_control",
            },
        )

    def test_access_grant_is_strict_increase_but_reversible(self) -> None:
        audit = self.audits["access_grant_existing_record"]
        self.assertTrue(audit.strict_forward_increase)
        self.assertEqual(audit.forward_status, REVERSIBLE_POSSIBLE)
        self.assertEqual(audit.reverse_status, REVERSIBLE_POSSIBLE)
        self.assertEqual(audit.before_profile, (1, 1, 1, 0))
        self.assertEqual(audit.after_profile, (2, 2, 1, 1))

    def test_copy_cases_require_resource_accounting_not_constructor_impossibility(self) -> None:
        for case_id in ("copy_to_fresh_holder", "branch_spread_copy"):
            audit = self.audits[case_id]
            self.assertTrue(audit.strict_forward_increase)
            self.assertEqual(audit.forward_status, RESOURCE_CONSUMING_POSSIBLE)
            self.assertEqual(audit.reverse_status, RESOURCE_CONSUMING_POSSIBLE)
            self.assertEqual(audit.verdict, RESOURCE_ACCOUNTING_ONLY)

    def test_branch_spread_copy_increases_branch_robustness(self) -> None:
        audit = self.audits["branch_spread_copy"]
        self.assertEqual(audit.before_profile, (2, 2, 1, 1))
        self.assertEqual(audit.after_profile, (3, 3, 2, 2))

    def test_access_loss_control_is_not_a_strict_increase(self) -> None:
        audit = self.audits["access_loss_without_erasure_control"]
        self.assertFalse(audit.strict_forward_increase)
        self.assertEqual(audit.forward_status, REVERSIBLE_POSSIBLE)
        self.assertEqual(audit.reverse_status, REVERSIBLE_POSSIBLE)

    def test_no_case_promotes_unqualified_arrow(self) -> None:
        for audit in self.result.audits:
            self.assertFalse(audit.permits_unqualified_physical_arrow)
        self.assertTrue(
            self.result.strict_increase_cases_have_no_constructor_impossible_reverse
        )
        self.assertIn("do not acquire constructor-impossible reverses", self.result.strongest_claim)

    def test_claim_impact_records_t1_grounding_blocker(self) -> None:
        self.assertIn("record substrate", self.result.improved)
        self.assertIn("does not supply a constructor-impossible reverse", self.result.weakened)
        self.assertIn("record substrate", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
