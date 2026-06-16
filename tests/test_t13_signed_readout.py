"""Unit tests for T13: signed and interfering readout."""

from __future__ import annotations

import cmath
import random
import unittest

from models.t13_signed_readout import (
    ReadoutRecordGraph,
    build_observer_consistency_pair,
    build_w1_pair,
    build_w2_chain,
    sorkin_i2,
    sorkin_i3,
    sorkin_i3_coefficients,
)

THRESHOLD = 1


class TestPhase1TrivialSignedReadout(unittest.TestCase):
    """The Jordan-decomposition objection, stated as a passing test."""

    def test_linear_readout_factors_through_two_monotone_counters(self) -> None:
        graph, observer, chain = build_w2_chain()
        previous_p, previous_n = 0, 0
        for event in chain:
            p, n = graph.signed_counters(observer, "X", "true", event)
            linear = graph.readout_linear(observer, "X", "true", event)
            self.assertEqual(linear, p - n)  # fully recoverable: trivial
            self.assertGreaterEqual(p, previous_p)  # counters monotone
            self.assertGreaterEqual(n, previous_n)
            previous_p, previous_n = p, n


class TestW1ProfileBlindness(unittest.TestCase):
    """Identical finality profiles, different readouts: the non-factorization witness."""

    def test_identical_profiles_different_readouts(self) -> None:
        constructive, destructive, observer = build_w1_pair()
        profile_c = constructive.finality_profile(observer, "X", "true", THRESHOLD)
        profile_d = destructive.finality_profile(observer, "X", "true", THRESHOLD)
        self.assertEqual(profile_c.as_tuple(), profile_d.as_tuple())
        readout_c = constructive.readout_born(observer, "X", "true")
        readout_d = destructive.readout_born(observer, "X", "true")
        self.assertEqual(readout_c, 4.0)
        self.assertEqual(readout_d, 0.0)
        # Therefore no function from finality profiles to readouts exists.

    def test_reconstruction_layer_is_weight_blind(self) -> None:
        constructive, destructive, observer = build_w1_pair()
        self.assertEqual(
            constructive.reconstruct_value(observer, "X", THRESHOLD),
            destructive.reconstruct_value(observer, "X", THRESHOLD),
        )


class TestW2AntiMonotoneChain(unittest.TestCase):
    """Profile strictly grows along the chain while Born readout cancels mid-chain."""

    def test_profile_monotone_readout_cancels(self) -> None:
        graph, observer, chain = build_w2_chain()
        profiles = [graph.finality_profile(observer, "X", "true", THRESHOLD, e).as_tuple() for e in chain]
        readouts = [graph.readout_born(observer, "X", "true", e) for e in chain]
        for earlier, later in zip(profiles, profiles[1:]):
            self.assertTrue(all(a <= b for a, b in zip(earlier, later)))
            self.assertNotEqual(earlier, later)  # strictly growing
        self.assertEqual(readouts, [1.0, 0.0, 1.0])  # full cancellation mid-chain
        # Therefore no monotone map from profiles to readouts exists.

    def test_evidence_count_monotone(self) -> None:
        graph, observer, chain = build_w2_chain()
        counts = [len(graph.accessible_records(observer, "X", "true", e)) for e in chain]
        self.assertEqual(counts, [1, 2, 3])


class TestSorkinHierarchy(unittest.TestCase):
    """Readout is level-2: pairwise interference present, triple sum rule holds."""

    def test_i2_nonzero_interference_present(self) -> None:
        self.assertEqual(sorkin_i2((1 + 0j,), (1 + 0j,)), 2.0)
        self.assertEqual(sorkin_i2((1 + 0j,), (-1 + 0j,)), -2.0)

    def test_i3_vanishes_identically(self) -> None:
        rng = random.Random(13)
        for _ in range(200):
            sets = tuple(
                tuple(
                    cmath.rect(rng.uniform(0.1, 2.0), rng.uniform(0, 2 * cmath.pi))
                    for _ in range(rng.randint(1, 4))
                )
                for _ in range(3)
            )
            self.assertAlmostEqual(sorkin_i3(*sets), 0.0, places=9)

    def test_i3_coefficients_cancel_symbolically(self) -> None:
        self.assertEqual(set(sorkin_i3_coefficients().values()), {0})


class TestObserverConsistency(unittest.TestCase):
    def test_divergence_attributable_to_access_alone(self) -> None:
        graph, full, partial = build_observer_consistency_pair()
        self.assertEqual(graph.readout_born(full, "X", "true"), 1.0)
        self.assertEqual(graph.readout_born(partial, "X", "true"), 4.0)
        same_access = graph.readout_born(
            graph_observer_with(full, frozenset({"h1", "h3"})), "X", "true"
        )
        self.assertEqual(same_access, graph.readout_born(partial, "X", "true"))

    def test_profiles_monotone_for_both_observers(self) -> None:
        graph, full, partial = build_observer_consistency_pair()
        for observer in (full, partial):
            chain = ("e1", "e2", "e3")
            profiles = [
                graph.finality_profile(observer, "X", "true", THRESHOLD, e).as_tuple()
                for e in chain
            ]
            for earlier, later in zip(profiles, profiles[1:]):
                self.assertTrue(all(a <= b for a, b in zip(earlier, later)))


def graph_observer_with(observer, holders):
    from models.t1_record_graph import Observer

    return Observer(observer.observer_id + "_alt", observer.event, holders)


if __name__ == "__main__":
    unittest.main()
