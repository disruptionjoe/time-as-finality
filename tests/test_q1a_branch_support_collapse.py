"""Tests for T109: Q1A branch-support collapse audit."""

from __future__ import annotations

import unittest

from models.q1a_branch_support_collapse import run_t109_analysis


class Q1ABranchSupportCollapseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t109_analysis()

    def test_rooted_branch_support_is_trivial_on_all_nonzero_support_cases(self) -> None:
        self.assertTrue(self.result.rooted_branch_support_constant_on_nonzero_support_cases)
        nonzero = [
            case
            for case in self.result.visible_cases
            if (case.accessible_provenance_support or 0) > 0
        ]
        self.assertGreater(len(nonzero), 0)
        self.assertTrue(all(case.rooted_branch_support == 1 for case in nonzero))

    def test_rooted_branch_support_only_changes_at_zero_access_boundary(self) -> None:
        self.assertTrue(self.result.rooted_branch_support_varies_only_with_zero_access_boundary)
        zero_support = [
            case for case in self.result.visible_cases if case.accessible_provenance_support == 0
        ]
        self.assertGreater(len(zero_support), 0)
        self.assertTrue(all(case.rooted_branch_support == 0 for case in zero_support))

    def test_no_same_support_class_is_split_by_branch_support(self) -> None:
        self.assertFalse(self.result.rooted_branch_support_splits_same_support_class)

    def test_branch_history_change_is_already_an_invalid_fixed_data_case(self) -> None:
        self.assertTrue(self.result.branch_history_changes_leave_fixed_data_gate)

    def test_t109_closes_the_branch_support_escape_hatch(self) -> None:
        self.assertFalse(self.result.any_load_bearing_branch_support_witness_in_current_family)
        self.assertIn("not a surviving independent lever", self.result.strongest_claim)
        self.assertIn("single-root triviality", self.result.q1a_update)


if __name__ == "__main__":
    unittest.main()
