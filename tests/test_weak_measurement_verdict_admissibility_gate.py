"""Tests for T150: weak-measurement verdict-admissibility gate."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.weak_measurement_verdict_admissibility_gate import (
    canonical_verdict_cases,
    classify_verdict_admissibility,
    current_frontier_case,
    run_t150_analysis,
)


class Q1CVerdictAdmissibilityGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = dict(canonical_verdict_cases())
        self.result = run_t150_analysis()

    def test_auxiliary_echo_positive_lift_is_rejected_as_circular(self) -> None:
        audit = classify_verdict_admissibility(
            self.cases["auxiliary_echo_gerrymander"],
            name="auxiliary_echo_gerrymander",
        )

        self.assertEqual(audit.conditional_lift, Fraction(1, 2))
        self.assertEqual(audit.classification, "null_auxiliary_defined_verdict")
        self.assertFalse(audit.active_route)

    def test_rare_target_is_rejected(self) -> None:
        audit = classify_verdict_admissibility(
            self.cases["rare_target_gerrymander"],
            name="rare_target_gerrymander",
        )

        self.assertEqual(audit.conditional_lift, Fraction(1, 10))
        self.assertEqual(audit.smallest_verdict_support, Fraction(1, 10))
        self.assertEqual(audit.classification, "null_rare_verdict_gerrymander")
        self.assertFalse(audit.active_route)

    def test_typed_candidate_routes_survive(self) -> None:
        extra = classify_verdict_admissibility(
            self.cases["typed_extra_environment_candidate"],
            name="typed_extra_environment_candidate",
        )
        enlarged = classify_verdict_admissibility(
            self.cases["typed_enlarged_instrument_candidate"],
            name="typed_enlarged_instrument_candidate",
        )

        self.assertEqual(extra.classification, "candidate_typed_verdict_route")
        self.assertEqual(enlarged.classification, "candidate_typed_verdict_route")
        self.assertTrue(extra.active_route)
        self.assertTrue(enlarged.active_route)

    def test_t149_failure_cannot_be_rescued_by_verdict_typing(self) -> None:
        audit = classify_verdict_admissibility(
            self.cases["same_instrument_positive_lift"],
            name="same_instrument_positive_lift",
        )

        self.assertEqual(audit.classification, "null_t149_architecture_not_cleared")
        self.assertFalse(audit.active_route)

    def test_current_frontier_remains_inactive(self) -> None:
        name, case = current_frontier_case()
        audit = classify_verdict_admissibility(case, name=name)

        self.assertFalse(audit.active_route)
        self.assertFalse(self.result.current_frontier_active)
        self.assertTrue(self.result.all_null_controls_rejected)
        self.assertTrue(self.result.live_cases_clear_target_gate)
        self.assertIn("Positive conditional lift is still not enough", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
