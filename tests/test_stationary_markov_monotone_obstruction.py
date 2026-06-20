"""Tests for T122 stationary Markov monotone obstruction."""

from __future__ import annotations

import unittest

from models.stationary_markov_monotone_obstruction import (
    absorbing_append_control,
    audit_markov_scenario,
    biased_cycle_control,
    deterministic_function_check,
    detailed_balance_control,
    run_t122_analysis,
)


class StationaryMarkovMonotoneObstructionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t122_analysis()

    def test_detailed_balance_control_has_zero_weighted_drift_not_monotone(self) -> None:
        audit = audit_markov_scenario(detailed_balance_control())

        self.assertAlmostEqual(audit.stationary_weighted_drift, 0.0)
        self.assertEqual(audit.stationary_support, (0, 1))
        self.assertFalse(audit.nonnegative_on_stationary_support)
        self.assertFalse(audit.theorem_violation)
        self.assertEqual(audit.classification, "not_a_monotone")

    def test_biased_stationary_cycle_does_not_give_scalar_arrow(self) -> None:
        audit = audit_markov_scenario(biased_cycle_control())

        self.assertAlmostEqual(audit.stationary_weighted_drift, 0.0)
        self.assertTrue(audit.strict_positive_on_stationary_support)
        self.assertFalse(audit.nonnegative_on_stationary_support)
        self.assertIn("not_a_monotone", audit.classification)

    def test_absorbing_append_strict_drift_is_transient_only(self) -> None:
        audit = audit_markov_scenario(absorbing_append_control())

        self.assertAlmostEqual(audit.stationary_weighted_drift, 0.0)
        self.assertEqual(audit.stationary_support, (3,))
        self.assertFalse(audit.strict_positive_on_stationary_support)
        self.assertTrue(audit.strict_positive_off_stationary_support)
        self.assertFalse(audit.theorem_violation)
        self.assertEqual(audit.classification, "transient_only_monotonicity")

    def test_deterministic_function_exhaustion_has_no_recurrent_strict_monotones(self) -> None:
        for state_count in range(2, 5):
            check = deterministic_function_check(state_count, value_count=3)

            self.assertTrue(check.theorem_holds)
            self.assertEqual(check.recurrent_strict_monotone_assignments, 0)
            self.assertGreater(check.transient_only_strict_assignments, 0)

    def test_no_fixture_violates_stationary_obstruction(self) -> None:
        audits = (
            self.result.detailed_balance_control,
            self.result.biased_cycle_control,
            self.result.absorbing_append_control,
        )

        self.assertFalse(any(audit.theorem_violation for audit in audits))
        self.assertIn("stationary Markov obstruction", self.result.h7_update)
        self.assertIn("piP=pi", self.result.claim_ledger_update)
        self.assertIn("constructor/resource-accounting", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
