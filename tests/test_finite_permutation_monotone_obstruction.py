"""Tests for T110 finite-permutation monotone obstruction."""

from __future__ import annotations

import unittest

from models.finite_permutation_monotone_obstruction import (
    T106_CLOSED_ACCOUNTED_SUPPORT,
    audit_open_branch_scores,
    audit_permutation_scores,
    closed_cycle_transition,
    exhaustive_cycle_check,
    orbit_decomposition,
    run_t110_analysis,
)


class FinitePermutationMonotoneObstructionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t110_analysis()

    def test_permutation_orbits_are_extracted(self) -> None:
        transition = (1, 2, 0, 4, 3)

        self.assertEqual(orbit_decomposition(transition), ((0, 1, 2), (3, 4)))

    def test_closed_t106_cycle_is_not_monotone(self) -> None:
        audit = self.result.t106_closed_cycle_audit

        self.assertEqual(
            audit.orbit_audits[0].score_sequence,
            T106_CLOSED_ACCOUNTED_SUPPORT,
        )
        self.assertFalse(audit.nondecreasing_on_all_edges)
        self.assertTrue(audit.has_strict_increase)
        self.assertTrue(audit.has_decrease)
        self.assertFalse(audit.strict_nondecreasing_possible)

    def test_constant_score_is_the_only_closed_nondecreasing_case(self) -> None:
        audit = audit_permutation_scores(
            closed_cycle_transition(5),
            (2, 2, 2, 2, 2),
        )

        self.assertTrue(audit.nondecreasing_on_all_edges)
        self.assertTrue(audit.constant_on_each_orbit)
        self.assertFalse(audit.has_strict_increase)
        self.assertFalse(audit.strict_nondecreasing_possible)

    def test_exhaustive_cycles_have_no_strict_nondecreasing_assignment(self) -> None:
        for length in range(2, 8):
            check = exhaustive_cycle_check(length, value_count=3)
            self.assertEqual(check.nondecreasing_assignments, check.constant_assignments)
            self.assertEqual(check.constant_assignments, 3)
            self.assertEqual(check.strict_without_decrease_assignments, 0)
            self.assertTrue(check.theorem_holds)

    def test_open_branch_can_be_strict_only_by_not_being_closed(self) -> None:
        audit = audit_open_branch_scores((0, 1, 3, 4, 4, 5, 7))

        self.assertTrue(audit.nondecreasing)
        self.assertGreater(audit.strict_increase_edges, 0)
        self.assertFalse(audit.reversible_closed_system)

    def test_t110_reports_h7_demotion(self) -> None:
        self.assertIn("finite closed reversible system", self.result.strongest_claim)
        self.assertIn("finite permutation obstruction", self.result.improved)
        self.assertIn("H7 is weakened", self.result.weakened)
        self.assertIn("open-system", self.result.open_blocker)


if __name__ == "__main__":
    unittest.main()
