"""Tests for T519: QD redundancy / replication invariant gate."""
from __future__ import annotations

import unittest

import numpy as np

from models.quantum_darwinism_replication_invariant_gate import (
    byzantine_intersection_safe,
    crash_survival_fraction,
    exact_redundancy,
    min_byzantine_quorum,
)


class DarwinismInvariantGateTests(unittest.TestCase):
    def test_exact_redundancy_perfect_copy(self):
        row = exact_redundancy(6, np.pi, 0.1)
        self.assertEqual(row["f_delta"], 1)
        self.assertAlmostEqual(row["info_deficit"], 5 / 6)

    def test_candidate_is_delta_sensitive(self):
        row_a = exact_redundancy(6, 0.6 * np.pi, 0.05)
        row_b = exact_redundancy(6, 0.6 * np.pi, 0.20)
        self.assertNotAlmostEqual(row_a["info_deficit"], row_b["info_deficit"], places=6)

    def test_crash_survival_matches_deficit_when_q_equals_f_delta(self):
        row = exact_redundancy(6, 0.6 * np.pi, 0.1)
        self.assertAlmostEqual(crash_survival_fraction(6, row["f_delta"]), row["info_deficit"])

    def test_byzantine_quorum_condition(self):
        self.assertFalse(byzantine_intersection_safe(8, 5, 2))
        self.assertTrue(byzantine_intersection_safe(8, 6, 2))
        self.assertEqual(min_byzantine_quorum(8, 2), 6)

    def test_byzantine_reading_not_same_as_perfect_copy_deficit(self):
        row = exact_redundancy(8, np.pi, 0.1)
        bft_survival = crash_survival_fraction(8, min_byzantine_quorum(8, 2))
        self.assertGreater(row["info_deficit"], bft_survival)


if __name__ == "__main__":
    unittest.main()
