"""Tests for T516: closed form for the isotropic 2-shareability wall."""
from __future__ import annotations

import unittest

from models.finality_isotropic_shareability_closed_form import bracket_share_wall, closed_form
from models.finality_ladder_qudit import is_2_shareable, isotropic


class ClosedFormTests(unittest.TestCase):
    def test_predictions(self):
        self.assertAlmostEqual(closed_form(2), 0.750)
        self.assertAlmostEqual(closed_form(3), 2 / 3)
        self.assertAlmostEqual(closed_form(4), 0.625)

    def test_structural_facts(self):
        self.assertTrue(all(closed_form(d) > 1.0 / d for d in range(2, 9)))
        self.assertTrue(all(closed_form(d + 1) < closed_form(d) for d in range(2, 20)))
        self.assertAlmostEqual(closed_form(10_000), 0.5, places=3)

    def test_pocs_brackets_contain_closed_form(self):
        for d in (2, 3, 4):
            last_sh, first_un = bracket_share_wall(d)
            cf = closed_form(d)
            self.assertIsNotNone(last_sh)
            self.assertIsNotNone(first_un)
            self.assertLessEqual(last_sh - 1e-9, cf)
            self.assertLessEqual(cf, first_un + 1e-9)

    def test_d3_wall_matches_ladder_pocs_value(self):
        d = 3
        cf = closed_form(d)
        self.assertTrue(is_2_shareable(isotropic(cf - 0.02, d), d, iters=800))
        self.assertFalse(is_2_shareable(isotropic(cf + 0.02, d), d, iters=800))


if __name__ == "__main__":
    unittest.main()
