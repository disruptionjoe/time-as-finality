"""Tests for T515: three-wall ladder at d=4 + corrected CGLMP-d operator."""
from __future__ import annotations

import unittest

import numpy as np

from models.finality_ladder_qudit import isotropic, max_entangled
from models.finality_qudit_d4_ladder import CGLMP_MAXENT, cglmp
from models.finality_qudit_three_walls import cglmp as cglmp_old


class CGLMPCorrectionTests(unittest.TestCase):
    def test_corrected_cglmp_matches_standard_values(self):
        for d, expected in CGLMP_MAXENT.items():
            self.assertAlmostEqual(cglmp(max_entangled(d), d), expected, places=3)
            self.assertAlmostEqual(cglmp(np.eye(d * d) / (d * d), d), 0.0, places=9)

    def test_old_operator_is_wrong_at_d4(self):
        # d<=3 agree (only k=0); d=4 diverges (untested k>=1 term)
        self.assertAlmostEqual(cglmp_old(max_entangled(3), 3), cglmp(max_entangled(3), 3), places=6)
        self.assertGreater(abs(cglmp_old(max_entangled(4), 4) - CGLMP_MAXENT[4]), 1e-2)

    def test_d4_walls_ordered_and_distinct(self):
        d = 4
        ent = 1.0 / d
        share = (d + 1) / (2 * d)
        Fs = [i / 1000 for i in range(250, 1000)]
        F_cglmp = min((F for F in Fs if cglmp(isotropic(F, d), d) > 2.0), default=1.0)
        self.assertLess(ent, share)
        self.assertLess(share, F_cglmp)
        self.assertGreater(share - ent, 0.02)
        self.assertGreater(F_cglmp - share, 0.02)
        v = (d * d * F_cglmp - 1) / (d * d - 1)
        self.assertAlmostEqual(v, 0.6906, places=2)


if __name__ == "__main__":
    unittest.main()
