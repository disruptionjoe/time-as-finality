"""Tests for T118: Q1A reversal-cost collapse audit."""

from __future__ import annotations

import unittest

from models.q1a_reversal_cost_collapse import run_t118_analysis


class Q1AReversalCostCollapseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t118_analysis()

    def test_proxy_is_defined_only_for_visible_partition_cases(self) -> None:
        self.assertTrue(self.result.proxy_defined_exactly_when_partition_visible)
        self.assertTrue(
            all(case.reversal_cost_proxy is not None for case in self.result.visible_cases)
        )
        self.assertIsNone(self.result.hidden_partition_case.reversal_cost_proxy)

    def test_proxy_equals_support_on_visible_cases(self) -> None:
        self.assertTrue(self.result.proxy_equals_support_on_all_visible_cases)
        self.assertTrue(
            all(
                case.reversal_cost_proxy == case.accessible_provenance_support
                for case in self.result.visible_cases
            )
        )

    def test_same_support_class_is_never_split_by_reversal_cost(self) -> None:
        self.assertFalse(self.result.proxy_splits_same_support_class)

    def test_branch_history_change_is_still_an_invalid_fixed_data_case(self) -> None:
        self.assertTrue(self.result.branch_history_changes_leave_fixed_data_gate)

    def test_t118_closes_the_reversal_cost_escape_hatch(self) -> None:
        self.assertFalse(self.result.any_load_bearing_reversal_cost_witness_in_current_family)
        self.assertIn("not a surviving independent lever", self.result.strongest_claim)
        self.assertIn("accessible provenance-support count itself", self.result.q1a_update)


if __name__ == "__main__":
    unittest.main()
