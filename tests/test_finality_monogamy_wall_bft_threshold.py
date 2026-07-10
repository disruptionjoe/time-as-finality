"""Tests for T517: monogamy wall vs BFT 2/3 threshold (falsification)."""
from __future__ import annotations

import unittest
from fractions import Fraction

from models.finality_monogamy_wall_bft_threshold import F_share, v_share


class MonogamyBFTFalsificationTests(unittest.TestCase):
    def test_qubit_visibility_wall_is_two_thirds(self):
        self.assertEqual(v_share(2), Fraction(2, 3))

    def test_visibility_form_closed(self):
        for d in range(2, 7):
            self.assertEqual(v_share(d), Fraction(d + 2, 2 * (d + 1)))

    def test_wall_drifts_not_pinned_at_two_thirds(self):
        walls = [v_share(d) for d in range(2, 9)]
        self.assertTrue(all(walls[i + 1] < walls[i] for i in range(len(walls) - 1)))
        self.assertLess(float(v_share(100_000)), 2 / 3)
        self.assertAlmostEqual(float(v_share(100_000)), 0.5, places=4)

    def test_qutrit_wall_is_five_eighths_not_two_thirds(self):
        self.assertEqual(v_share(3), Fraction(5, 8))

    def test_coincidence_moves_between_parametrizations(self):
        # F-parametrization coincidence is at d=3, not d=2 -> coincidence signature
        self.assertEqual(F_share(3), Fraction(2, 3))
        self.assertNotEqual(F_share(2), Fraction(2, 3))


if __name__ == "__main__":
    unittest.main()
