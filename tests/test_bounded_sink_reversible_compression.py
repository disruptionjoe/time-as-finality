"""Tests for T106 bounded-sink reversible-compression obstruction."""

from __future__ import annotations

import unittest

from models.bounded_sink_reversible_compression import (
    analyze_ordered_stack_export,
    analyze_orderless_counter_compression,
    rle_capacity_audit,
    run_t106_analysis,
)
from models.cyclic_reconciler_entropy_export import cyclic_reversible_export_policy
from models.persistent_reconciler_cost_boundary import canonical_observation_sequence


class BoundedSinkReversibleCompressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t106_analysis()

    def test_rle_compression_has_finite_capacity_boundary(self) -> None:
        observations = canonical_observation_sequence()
        exported = cyclic_reversible_export_policy(observations, capacity=3).exported_slots
        audit = rle_capacity_audit(exported, capacity_blocks=3)

        self.assertEqual(exported, ((0, 0), (0, 0), (0, 0), (1, 0), (1, 1), (1, 0)))
        self.assertEqual(audit.block_count_sequence, (1, 1, 1, 2, 3, 4))
        self.assertEqual(audit.reconstructed_support_sequence, (0, 0, 0, 1, 3, 4))
        self.assertEqual(audit.required_blocks, 4)
        self.assertFalse(audit.admissible_for_sequence)
        self.assertEqual(audit.first_exhausted_export_index, 5)

    def test_orderless_counter_compression_is_not_reversible(self) -> None:
        orderless = analyze_orderless_counter_compression(max_total_count=6, width=2)

        self.assertFalse(orderless.injective)
        self.assertGreater(orderless.maximum_preimages, 1)
        self.assertGreater(orderless.lost_bits, 0.0)

    def test_ordered_stack_export_is_reversible_only_with_sink_capacity(self) -> None:
        ordered = analyze_ordered_stack_export(horizon=6, width=2)

        self.assertTrue(ordered.injective)
        self.assertEqual(ordered.maximum_preimages, 1)
        self.assertAlmostEqual(ordered.lost_bits, 0.0)

    def test_forward_monotone_disappears_on_closed_bounded_cycle(self) -> None:
        cycle = self.result.closed_cycle_audit

        self.assertEqual(cycle.forward_accounted_support, (0, 1, 3, 4, 4, 5, 7))
        self.assertTrue(cycle.forward_accounted_monotone)
        self.assertEqual(
            cycle.full_cycle_accounted_support,
            (0, 1, 3, 4, 4, 5, 7, 5, 4, 4, 3, 1, 0),
        )
        self.assertFalse(cycle.full_cycle_accounted_monotone)
        self.assertFalse(cycle.strict_cycle_monotone_possible)

    def test_t106_reports_h7_weakening(self) -> None:
        self.assertIn("does not rescue H7", self.result.strongest_claim)
        self.assertIn("further weakens H7", self.result.weakened)
        self.assertIn("conditional constructor theorem", self.result.h7_update)
        self.assertIn("finite-permutation obstruction", self.result.recommended_next)


if __name__ == "__main__":
    unittest.main()
