"""Tests for T149: weak-measurement conditional-sufficiency gate."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.weak_measurement_conditional_sufficiency_gate import (
    bayes_error,
    canonical_conditional_cases,
    classify_conditional_sufficiency,
    current_frontier_case,
    run_t149_analysis,
)


class Q1CConditionalSufficiencyGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_conditional_cases())
        self.result = run_t149_analysis()

    def test_screened_and_independent_meters_have_zero_conditional_lift(self) -> None:
        screened = classify_conditional_sufficiency(
            self.cases["screened_copy_meter"],
            name="screened_copy_meter",
        )
        independent = classify_conditional_sufficiency(
            self.cases["independent_noise_meter"],
            name="independent_noise_meter",
        )

        self.assertEqual(screened.conditional_lift, Fraction(0, 1))
        self.assertEqual(independent.conditional_lift, Fraction(0, 1))
        self.assertEqual(screened.classification, "null_conditionally_sufficient_record")
        self.assertEqual(independent.classification, "null_conditionally_sufficient_record")
        self.assertFalse(screened.active_route)
        self.assertFalse(independent.active_route)

    def test_positive_lift_cases_have_exact_risk_gap(self) -> None:
        case = self.cases["extra_environment_candidate"]
        self.assertEqual(bayes_error(case.events, ("record",)), Fraction(1, 2))
        self.assertEqual(bayes_error(case.events, ("record", "auxiliary")), Fraction(0, 1))

        audit = classify_conditional_sufficiency(case, name="extra_environment_candidate")
        self.assertEqual(audit.conditional_lift, Fraction(1, 2))
        self.assertEqual(
            audit.classification,
            "candidate_extra_environment_conditional_lift",
        )
        self.assertTrue(audit.active_route)

    def test_same_instrument_positive_lift_is_underdeclared(self) -> None:
        audit = classify_conditional_sufficiency(
            self.cases["same_instrument_positive_lift"],
            name="same_instrument_positive_lift",
        )

        self.assertEqual(audit.conditional_lift, Fraction(1, 2))
        self.assertEqual(audit.classification, "underdeclared_same_instrument_lift")
        self.assertFalse(audit.active_route)

    def test_enlarged_instrument_needs_preserved_comparison_target(self) -> None:
        underdeclared = classify_conditional_sufficiency(
            self.cases["underdeclared_enlarged_instrument"],
            name="underdeclared_enlarged_instrument",
        )
        candidate = classify_conditional_sufficiency(
            self.cases["enlarged_instrument_candidate"],
            name="enlarged_instrument_candidate",
        )

        self.assertEqual(
            underdeclared.classification,
            "underdeclared_instrument_enlargement",
        )
        self.assertFalse(underdeclared.active_route)
        self.assertEqual(
            candidate.classification,
            "candidate_enlarged_instrument_conditional_lift",
        )
        self.assertTrue(candidate.active_route)

    def test_current_frontier_remains_inactive(self) -> None:
        name, case = current_frontier_case()
        audit = classify_conditional_sufficiency(case, name=name)

        self.assertEqual(audit.classification, "null_conditionally_sufficient_record")
        self.assertFalse(audit.active_route)
        self.assertFalse(self.result.current_frontier_active)
        self.assertTrue(self.result.all_null_controls_rejected)
        self.assertTrue(self.result.live_cases_have_positive_lift)
        self.assertIn("conditional decision-sufficiency test", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
