"""Tests for T518: quantum-Darwinism redundancy <-> replication bridge."""
from __future__ import annotations

import unittest

import numpy as np

from models.quantum_darwinism_replication_bridge import (
    global_state,
    partial_info,
    redundancy,
    reduced_dm,
    vn_entropy,
)


class DarwinismBridgeTests(unittest.TestCase):
    def test_system_carries_one_bit(self):
        N = 6
        HS = vn_entropy(reduced_dm(global_state(N, np.pi), N + 1, [0]))
        self.assertAlmostEqual(HS, 1.0, places=6)

    def test_perfect_copy_one_fragment_sufficient(self):
        N = 6
        self.assertAlmostEqual(partial_info(global_state(N, np.pi), N, [1]), 1.0, places=6)

    def test_redundancy_plateau_and_monotone_decrease(self):
        N = 6
        R_perfect, _, _, _ = redundancy(global_state(N, np.pi), N, 0.1)
        R_poor, _, _, _ = redundancy(global_state(N, 0.2 * np.pi), N, 0.1)
        self.assertGreaterEqual(R_perfect, N / 2)
        self.assertLessEqual(R_poor, R_perfect + 1e-9)

    def test_redundancy_not_delta_invariant(self):
        N = 6
        R_a, _, _, _ = redundancy(global_state(N, 0.6 * np.pi), N, 0.05)
        R_b, _, _, _ = redundancy(global_state(N, 0.6 * np.pi), N, 0.20)
        self.assertNotAlmostEqual(R_a, R_b, places=6)


if __name__ == "__main__":
    unittest.main()
