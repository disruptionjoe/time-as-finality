"""Tests for T520: copy-law single-use-key absorber screen."""
from __future__ import annotations

import unittest

import numpy as np

from models.finality_encrypted_clone_single_use_key import (
    accessible_info_about_source,
    dm,
    encrypted_marginal,
    finality_reading,
    finality_vector,
    psi,
    resource_ledger,
    resource_vector,
    I2,
)


class EncryptedCloneAbsorberTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = psi(0.9, 0.4)

    def test_encrypted_marginal_is_maximally_mixed(self):
        self.assertTrue(np.allclose(encrypted_marginal(dm(self.source)), 0.5 * I2))

    def test_encrypted_band_is_unreadable(self):
        # accessible info about the source through the encrypted marginal = 0
        self.assertAlmostEqual(accessible_info_about_source(dm(self.source)), 0.0, places=12)

    def test_clones_are_unreadable_band_relabel(self):
        fr = finality_reading(self.source, 6, key_authority=1)
        self.assertAlmostEqual(fr["rec_individual"], 0.5)
        self.assertTrue(fr["band_unreadable"])

    def test_single_use_A_is_conserved(self):
        # the candidate quantity clears lane-B failure mode 2 (J+R went 1->6)
        fr = finality_reading(self.source, 6, key_authority=1)
        self.assertEqual(fr["A_band"], 1)
        self.assertEqual(fr["A_global"], 1)
        self.assertTrue(fr["A_conserved"])

    def test_controls_conserve_A_at_their_own_value(self):
        self.assertEqual(finality_reading(self.source, 6, 2)["A_band"], 2)
        self.assertEqual(finality_reading(self.source, 6, 0)["A_band"], 0)

    def test_every_finality_verdict_reproduced_by_resource_monotone(self):
        # the decisive absorber test: finality vector == resource vector
        for auth in (0, 1, 2):
            for n in (1, 2, 3, 6):
                fr = finality_reading(self.source, n, key_authority=auth)
                rl = resource_ledger(n, monotone_M=auth)
                self.assertEqual(finality_vector(fr), resource_vector(rl))

    def test_resource_ledger_reproduces_exactly_once_distinction(self):
        # 'exactly one authoritative copy' is itself a monotone value, not a
        # finality-only quantity
        self.assertEqual(resource_ledger(6, 1)["total_recoveries"], 1)
        self.assertEqual(resource_ledger(6, 2)["total_recoveries"], 2)
        self.assertFalse(resource_ledger(6, 0)["recoverable_now"])

    def test_absorbed_no_residue(self):
        residue = False
        for auth in (0, 1, 2):
            for n in (1, 2, 3, 6):
                fr = finality_reading(self.source, n, key_authority=auth)
                rl = resource_ledger(n, monotone_M=auth)
                if finality_vector(fr) != resource_vector(rl):
                    residue = True
        self.assertFalse(residue, "no verdict-bearing residue -> absorbed")


if __name__ == "__main__":
    unittest.main()
