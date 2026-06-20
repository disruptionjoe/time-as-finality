"""Tests for T82 persistent-reconciler cost boundary."""

from __future__ import annotations

import unittest

from models.persistent_reconciler_cost_boundary import (
    analyze_append_update,
    analyze_or_update,
    analyze_xor_update,
    canonical_observation_sequence,
    irreversible_or_policy,
    raw_support_sequence,
    reversible_append_policy,
    reversible_xor_policy,
    run_t82_analysis,
)


class PersistentReconcilerCostBoundaryTests(unittest.TestCase):
    def test_t80_observation_sequence_is_raw_nonmonotone(self) -> None:
        observations = canonical_observation_sequence()

        self.assertEqual(
            observations,
            ((1, 0), (1, 1), (1, 0), (0, 0), (1, 0), (1, 1)),
        )
        self.assertEqual(raw_support_sequence(observations), (1, 2, 1, 0, 1, 2))

    def test_or_memory_is_monotone_but_noninjective(self) -> None:
        observations = canonical_observation_sequence()
        policy = irreversible_or_policy(observations)
        transition = analyze_or_update(width=2)

        self.assertTrue(policy.monotone_support)
        self.assertEqual(policy.support_sequence, (1, 2, 2, 2, 2, 2))
        self.assertFalse(transition.injective)
        self.assertGreater(transition.lost_bits, 0.0)

    def test_xor_memory_is_reversible_but_nonmonotone(self) -> None:
        observations = canonical_observation_sequence()
        policy = reversible_xor_policy(observations)
        transition = analyze_xor_update(width=2)

        self.assertFalse(policy.monotone_support)
        self.assertEqual(policy.support_sequence, (1, 1, 2, 2, 1, 1))
        self.assertTrue(transition.injective)
        self.assertAlmostEqual(transition.lost_bits, 0.0)

    def test_append_only_ledger_is_injective_but_consumes_blank_slots(self) -> None:
        observations = canonical_observation_sequence()
        policy = reversible_append_policy(observations)
        transition = analyze_append_update(horizon=6, width=2)

        self.assertTrue(policy.monotone_support)
        self.assertEqual(policy.support_sequence, (1, 3, 4, 4, 5, 7))
        self.assertTrue(transition.injective)
        self.assertAlmostEqual(transition.lost_bits, 0.0)
        self.assertIn("12 blank memory bits", policy.resource_boundary)

    def test_short_append_ledger_exposes_finite_horizon_boundary(self) -> None:
        observations = canonical_observation_sequence()
        policy = reversible_append_policy(observations, horizon=3)

        self.assertTrue(policy.monotone_support)
        self.assertEqual(policy.support_sequence, (1, 3, 4))
        self.assertIn("Exhausted at observation layer 3", policy.resource_boundary)

    def test_run_t82_reports_h7_boundary(self) -> None:
        result = run_t82_analysis()

        self.assertIn("blank ledger state", result.strongest_claim)
        self.assertIn("resource-accounted", result.h7_update)
        self.assertIn("entropy export", result.recommended_next)


if __name__ == "__main__":
    unittest.main()
