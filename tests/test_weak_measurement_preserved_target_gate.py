"""Tests for T158: preserved-target honesty gate."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.weak_measurement_preserved_target_gate import (
    canonical_preserved_target_cases,
    classify_preserved_target,
    current_frontier_case,
    run_t158_analysis,
)


class Q1CPreservedTargetGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_preserved_target_cases())
        self.result = run_t158_analysis()

    def test_honest_enlargement_requires_exact_target_preservation(self) -> None:
        audit = classify_preserved_target(
            self.cases["honest_enlarged_instrument_candidate"],
            name="honest_enlarged_instrument_candidate",
        )

        self.assertEqual(audit.classification, "candidate_honest_enlarged_instrument_route")
        self.assertTrue(audit.active_route)
        self.assertEqual(audit.target_projection_error, Fraction(0, 1))
        self.assertEqual(audit.conditional_lift, Fraction(1, 2))

    def test_coarse_preserved_target_is_null(self) -> None:
        audit = classify_preserved_target(
            self.cases["coarse_preserved_target"],
            name="coarse_preserved_target",
        )

        self.assertEqual(audit.classification, "null_coarse_preserved_target")
        self.assertFalse(audit.active_route)

    def test_target_drift_is_rejected(self) -> None:
        audit = classify_preserved_target(
            self.cases["target_drift_under_enlargement"],
            name="target_drift_under_enlargement",
        )

        self.assertEqual(audit.classification, "null_target_drift_under_enlargement")
        self.assertFalse(audit.active_route)
        self.assertEqual(audit.target_projection_error, Fraction(1, 2))

    def test_honest_preservation_without_lift_stays_null(self) -> None:
        audit = classify_preserved_target(
            self.cases["honest_but_no_lift"],
            name="honest_but_no_lift",
        )

        self.assertEqual(audit.classification, "null_honest_but_no_extra_lift")
        self.assertFalse(audit.active_route)
        self.assertEqual(audit.conditional_lift, Fraction(0, 1))

    def test_current_frontier_remains_inactive(self) -> None:
        name, case = current_frontier_case()
        audit = classify_preserved_target(case, name=name)

        self.assertFalse(audit.active_route)
        self.assertFalse(self.result.current_frontier_active)
        self.assertTrue(self.result.all_null_controls_rejected)
        self.assertTrue(self.result.live_cases_honest)
        self.assertIn("preserves that record eventwise", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
