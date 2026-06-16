"""Unit tests for the T12 coupling-profile experiment."""

from __future__ import annotations

import unittest

from models.t12_coupling import build_t12_scenario, omniscient_relation

PROPS = ("A", "B", "C", "D")
THRESHOLD = 2


class TestT12Coupling(unittest.TestCase):
    def setUp(self) -> None:
        self.graph, self.population = build_t12_scenario()
        self.by_id = {observer.observer_id: observer for observer in self.population}
        self.truth = omniscient_relation(self.graph, PROPS, THRESHOLD)

    def relation(self, observer_id: str):
        return self.graph.observer_relation(self.by_id[observer_id], PROPS, THRESHOLD)

    def test_divergence_same_graph_different_orders(self) -> None:
        r1, r2, r3 = self.relation("O1"), self.relation("O2"), self.relation("O3")
        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1, r3)
        self.assertNotEqual(r2, r3)
        self.assertIn(("B", "C"), r1)
        self.assertNotIn(("B", "C"), r2)
        self.assertIn(("D", "C"), r2)
        self.assertNotIn(("D", "C"), r1)

    def test_soundness_no_inversions_against_omniscient_relation(self) -> None:
        for observer in self.population:
            relation = self.graph.observer_relation(observer, PROPS, THRESHOLD)
            for left, right in relation:
                self.assertNotIn(
                    (right, left),
                    self.truth,
                    f"{observer.observer_id} inverted {left}<{right}",
                )

    def test_overlap_agreement_between_observer_pairs(self) -> None:
        for first in self.population:
            for second in self.population:
                shared = {
                    proposition
                    for proposition in PROPS
                    if self.graph.reconstructible(first, proposition, THRESHOLD)
                    and self.graph.reconstructible(second, proposition, THRESHOLD)
                }
                r_first = {
                    pair
                    for pair in self.graph.observer_relation(first, PROPS, THRESHOLD)
                    if set(pair) <= shared
                }
                r_second = {
                    pair
                    for pair in self.graph.observer_relation(second, PROPS, THRESHOLD)
                    if set(pair) <= shared
                }
                for left, right in r_first:
                    self.assertNotIn((right, left), r_second)

    def test_invisibility_outside_profile(self) -> None:
        self.assertFalse(self.graph.reconstructible(self.by_id["O1"], "D", THRESHOLD))
        self.assertFalse(self.graph.reconstructible(self.by_id["O2"], "B", THRESHOLD))
        self.assertFalse(self.graph.reconstructible(self.by_id["O3"], "B", THRESHOLD))

    def test_hardness_and_reach_separate_record_grades(self) -> None:
        reach = {p: self.graph.reach(p, self.population) for p in PROPS}
        hardness = {p: self.graph.hardness(p, self.population, THRESHOLD) for p in PROPS}
        self.assertEqual((reach["A"], hardness["A"]), (1.0, 1.0))  # matter-grade
        self.assertEqual((reach["C"], hardness["C"]), (1.0, 1.0))  # matter-grade
        self.assertEqual((reach["B"], hardness["B"]), (0.25, 1.0))  # narrow unconditional
        self.assertEqual((reach["D"], hardness["D"]), (0.5, 0.5))  # idea-grade

    def test_reconstruction_does_not_imply_binding(self) -> None:
        o4 = self.by_id["O4"]
        self.assertTrue(self.graph.reconstructible(o4, "D", THRESHOLD))
        self.assertFalse(self.graph.constrained(o4, "D", THRESHOLD))

    def test_profiles_are_only_varied_factor(self) -> None:
        events = {observer.event for observer in self.population}
        self.assertEqual(events, {"observe"})


if __name__ == "__main__":
    unittest.main()
