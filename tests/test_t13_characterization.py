"""Characterization tests for T13: when does readout factor through summaries?

Proposition A (weight-blind insufficiency): if the weight alphabet contains
any two DISTINCT values u != v, then among the three two-record states with
weights (u,u), (u,v), (v,v) - which share every weight-blind summary - at
least two have different Born readouts. Proof: if |2u| = |u+v| = |2v| then
|u| = |v| and triangle equality forces u = v, a contradiction.

(Note: the naive form "(u,u) vs (u,v) always differ" is FALSE - for any u
there is a measure-zero circle of v with |u+v| = 2|u|, e.g. u=1,
v=2*exp(i*theta) with cos(theta) = -1/4. The generic-pair test passes
because random draws avoid the circle almost surely; the three-state test
covers the exact proposition.)

Proposition B (finite-alphabet sufficiency): over a finite weight alphabet,
the per-class record counts are monotone counters that fully determine the
Born readout. So the separation is from the FINALITY layer specifically, not
from monotone bookkeeping in general - the paper's honesty clause as a test.
"""

from __future__ import annotations

import cmath
import random
import unittest

ALPHABET = (1 + 0j, -1 + 0j, 1j, cmath.exp(1j * cmath.pi / 4))


def born(weights):
    return abs(sum(weights, 0j)) ** 2


class TestPropositionAWeightBlindInsufficiency(unittest.TestCase):
    def test_generic_pairs_yield_witnesses(self):
        rng = random.Random(7)
        for _ in range(300):
            u = cmath.rect(rng.uniform(0.1, 2.0), rng.uniform(0, 2 * cmath.pi))
            v = cmath.rect(rng.uniform(0.1, 2.0), rng.uniform(0, 2 * cmath.pi))
            if abs(u - v) < 1e-9:
                continue
            self.assertNotAlmostEqual(born((u, u)), born((u, v)), places=7)

    def test_exact_proposition_three_state_form(self):
        """For ANY distinct u, v at least two of (u,u), (u,v), (v,v) differ."""
        rng = random.Random(23)
        for _ in range(300):
            u = cmath.rect(rng.uniform(0.1, 2.0), rng.uniform(0, 2 * cmath.pi))
            v = cmath.rect(rng.uniform(0.1, 2.0), rng.uniform(0, 2 * cmath.pi))
            if abs(u - v) < 1e-9:
                continue
            readouts = (born((u, u)), born((u, v)), born((v, v)))
            self.assertFalse(
                abs(readouts[0] - readouts[1]) < 1e-9
                and abs(readouts[1] - readouts[2]) < 1e-9
            )

    def test_exception_circle_exists_naive_form_is_false(self):
        """Witness that the naive '(u,u) vs (u,v) always differ' claim fails."""
        u = 1 + 0j
        theta = cmath.acos(-0.25).real
        v = 2 * cmath.exp(1j * theta)
        self.assertAlmostEqual(born((u, u)), born((u, v)), places=9)
        # The pair is still separated through the third state:
        self.assertNotAlmostEqual(born((u, v)), born((v, v)), places=2)


class TestPropositionBFiniteAlphabetSufficiency(unittest.TestCase):
    def test_class_counts_determine_readout(self):
        rng = random.Random(11)
        for _ in range(300):
            state = tuple(rng.choice(ALPHABET) for _ in range(rng.randint(1, 12)))
            counts = {phi: sum(1 for w in state if w == phi) for phi in ALPHABET}
            from_counts = abs(sum(n * phi for phi, n in counts.items())) ** 2
            self.assertAlmostEqual(from_counts, born(state), places=9)

    def test_class_counts_are_monotone_under_record_addition(self):
        rng = random.Random(3)
        state = []
        previous = {phi: 0 for phi in ALPHABET}
        for _ in range(50):
            state.append(rng.choice(ALPHABET))
            counts = {phi: sum(1 for w in state if w == phi) for phi in ALPHABET}
            for phi in ALPHABET:
                self.assertGreaterEqual(counts[phi], previous[phi])
            previous = counts


if __name__ == "__main__":
    unittest.main()
