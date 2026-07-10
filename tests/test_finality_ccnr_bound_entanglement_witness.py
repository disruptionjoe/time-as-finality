"""Tests for T514: CCNR / realignment bound-entanglement witness."""
from __future__ import annotations

import unittest

import numpy as np

from models.finality_ccnr_bound_entanglement_witness import ccnr, tiles_bound_entangled
from models.finality_ladder_qudit import isotropic, negativity


class CCNRWitnessTests(unittest.TestCase):
    def test_separable_product_below_one(self):
        prod = np.kron(np.diag([0.5, 0.3, 0.2]), np.diag([0.6, 0.1, 0.3]))
        self.assertLessEqual(ccnr(prod, 3), 1.0 + 1e-9)

    def test_isotropic_separability_point_on_boundary(self):
        self.assertAlmostEqual(ccnr(isotropic(1 / 3, 3), 3), 1.0, places=5)

    def test_npt_entangled_flagged(self):
        self.assertGreater(ccnr(isotropic(0.9, 3), 3), 1.0)

    def test_tiles_bound_entangled_caught_but_ppt(self):
        rho = tiles_bound_entangled()
        self.assertLess(abs(negativity(rho, 3)), 1e-9)   # PPT: negativity misses it
        self.assertGreater(ccnr(rho, 3), 1.0 + 1e-6)     # CCNR catches it


if __name__ == "__main__":
    unittest.main()
