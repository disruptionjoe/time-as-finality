"""Tests for T84 cyclic reconciler entropy-export boundary."""

from __future__ import annotations

import unittest

from models.cyclic_reconciler_entropy_export import (
    analyze_cyclic_erasing_update,
    analyze_cyclic_export_update,
    cyclic_erasing_heat_bath_policy,
    cyclic_reversible_export_policy,
    run_t84_analysis,
)
from models.persistent_reconciler_cost_boundary import (
    canonical_observation_sequence,
    raw_support_sequence,
)


class CyclicReconcilerEntropyExportTests(unittest.TestCase):
    def test_cyclic_ring_local_support_is_nonmonotone(self) -> None:
        observations = canonical_observation_sequence()
        policy = cyclic_reversible_export_policy(observations, capacity=3)

        self.assertEqual(raw_support_sequence(observations), (1, 2, 1, 0, 1, 2))
        self.assertEqual(policy.local_support_sequence, (1, 3, 4, 3, 2, 3))
        self.assertFalse(policy.local_monotone)

    def test_reversible_export_restores_monotone_accounting_only_globally(self) -> None:
        observations = canonical_observation_sequence()
        policy = cyclic_reversible_export_policy(observations, capacity=3)
        transition = analyze_cyclic_export_update(capacity=3, width=2)

        self.assertTrue(transition.injective)
        self.assertAlmostEqual(transition.lost_bits, 0.0)
        self.assertEqual(policy.export_support_sequence, (0, 0, 0, 1, 3, 4))
        self.assertEqual(policy.accounted_support_sequence, (1, 3, 4, 4, 5, 7))
        self.assertTrue(policy.accounted_monotone)
        self.assertIn("exported garbage/history", policy.verdict)

    def test_erasing_recycle_is_noninjective_with_positive_loss(self) -> None:
        observations = canonical_observation_sequence()
        policy = cyclic_erasing_heat_bath_policy(observations, capacity=3)
        transition = analyze_cyclic_erasing_update(capacity=3, width=2)

        self.assertFalse(transition.injective)
        self.assertEqual(transition.maximum_preimages, 4)
        self.assertAlmostEqual(transition.lost_bits, 2.0)
        self.assertEqual(policy.recycled_steps, 3)
        self.assertAlmostEqual(policy.generic_recycle_lost_bits, 6.0)
        self.assertFalse(policy.local_monotone)
        self.assertTrue(policy.accounted_monotone)

    def test_run_t84_reports_h7_weakening(self) -> None:
        result = run_t84_analysis()

        self.assertIn("does not produce monotone local", result.strongest_claim)
        self.assertIn("weakened", result.weakened_claim)
        self.assertIn("partially supported", result.h7_update)
        self.assertIn("heat-bath", result.blocker)


if __name__ == "__main__":
    unittest.main()
