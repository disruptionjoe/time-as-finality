"""Tests for T53 observer-colimit descent boundary audit."""

from __future__ import annotations

import unittest

from models.observer_colimit_descent_boundary import run_t53_analysis


class ObserverColimitDescentBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t53_analysis()
        self.cases = {case.case_name: case for case in self.result.cases}

    def test_positive_control_is_unique_axis_reconstructable(self) -> None:
        case = self.cases["t51_positive_control"]
        self.assertEqual(case.verdict, "canonical_axis_reconstructable")
        self.assertTrue(case.unique_completion)
        self.assertTrue(case.has_axis_valid_completion)
        self.assertFalse(case.has_axis_failing_completion)

    def test_ambiguous_identity_is_underdetermined(self) -> None:
        case = self.cases["ambiguous_event_identity"]
        self.assertEqual(case.verdict, "underdetermined_noncanonical")
        self.assertFalse(case.unique_completion)
        self.assertGreaterEqual(case.distinct_compatible_signatures, 2)
        self.assertGreaterEqual(len(case.compatible_completion_names), 2)

    def test_axis_failure_keeps_partial_order(self) -> None:
        case = self.cases["axis_failing_valid_colimit"]
        self.assertEqual(case.verdict, "valid_partial_order_axis_failure")
        self.assertTrue(case.unique_completion)
        self.assertTrue(case.has_axis_failing_completion)
        self.assertFalse(case.has_axis_valid_completion)
        completion = case.evaluations[0]
        self.assertTrue(completion.partial_order.is_partial_order)
        self.assertFalse(completion.axis_monotonicity.am_holds)
        self.assertEqual(completion.axis_monotonicity.missing_count, 1)

    def test_hidden_record_repair_detected(self) -> None:
        case = self.cases["hidden_record_repair"]
        self.assertEqual(case.verdict, "repairable_by_hidden_record")
        self.assertTrue(case.has_hidden_record_repair)
        self.assertTrue(case.has_axis_valid_completion)
        self.assertTrue(case.has_axis_failing_completion)

    def test_nondefinable_overlap_boundary_detected(self) -> None:
        case = self.cases["nondefinable_overlap_boundary"]
        self.assertEqual(case.verdict, "nondefinable_projection")
        self.assertEqual(case.compatible_completion_names, ())

    def test_hypothesis_verdicts(self) -> None:
        hypotheses = {h.hypothesis_id: h.status for h in self.result.hypothesis_evaluations}
        self.assertEqual(hypotheses["H0"], "refuted")
        self.assertEqual(hypotheses["H1"], "refuted")
        self.assertEqual(hypotheses["H2"], "supported")
        self.assertEqual(hypotheses["H3"], "supported")
        self.assertEqual(hypotheses["H4"], "supported")
        self.assertEqual(hypotheses["H5"], "partially_supported")


if __name__ == "__main__":
    unittest.main()
