"""Tests for T40: Holarchy Lab — Emergent Holonic Finality.

Tests verify two theorems:
  1. Holonic Emergence: cross-level constraints can create obstructions from
     micro-compatible systems.
  2. Cross-Level AC5: non-empty forgotten_dims is necessary for holonic PO1
     admissibility.
"""

import unittest
from models.holarchy_lab import (
    T40Result,
    run_t40_analysis,
    build_holonic_flat_scenario,
    build_holonic_compatible_different_scenario,
    build_holonic_emergent_obstruction_scenario,
    build_holonic_micro_obstructed_scenario,
    build_holonic_po1_source,
    build_holonic_po1_target,
    build_holonic_po1_no_forgotten,
    analyze_holonic_network,
    analyze_holonic_po1,
)

_RESULT: T40Result | None = None


def _r() -> T40Result:
    global _RESULT
    if _RESULT is None:
        _RESULT = run_t40_analysis()
    return _RESULT


class TestRunCompletes(unittest.TestCase):
    def test_run_returns_result(self) -> None:
        r = _r()
        self.assertIsInstance(r, T40Result)

    def test_best_hypothesis_is_h_b(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H_B")

    def test_four_scenarios(self) -> None:
        self.assertEqual(len(_r().scenarios), 4)

    def test_two_po1_bridges(self) -> None:
        self.assertEqual(len(_r().holonic_po1_bridges), 2)

    def test_three_hypotheses(self) -> None:
        self.assertEqual(len(_r().hypothesis_evaluations), 3)

    def test_theorems_populated(self) -> None:
        r = _r()
        self.assertTrue(r.theorem_holonic_emergence)
        self.assertTrue(r.theorem_cross_level_ac5)

    def test_boundary_populated(self) -> None:
        self.assertTrue(_r().boundary)

    def test_recommendation_populated(self) -> None:
        self.assertTrue(_r().recommendation)


class TestFlatScenario(unittest.TestCase):
    def test_flat_both_micro_satisfiable(self) -> None:
        net = build_holonic_flat_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.all_micro_satisfiable)

    def test_flat_holonic_satisfiable(self) -> None:
        net = build_holonic_flat_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.holonic_globally_satisfiable)

    def test_flat_no_emergence(self) -> None:
        net = build_holonic_flat_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.emergence_detected)

    def test_flat_two_witnesses(self) -> None:
        net = build_holonic_flat_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.holonic_witness_count, 2)

    def test_flat_obstruction_source_none(self) -> None:
        net = build_holonic_flat_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.obstruction_source, "none")


class TestCompatibleDifferentScenario(unittest.TestCase):
    def test_compatible_different_holonic_satisfiable(self) -> None:
        net = build_holonic_compatible_different_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.holonic_globally_satisfiable)

    def test_compatible_different_no_emergence(self) -> None:
        net = build_holonic_compatible_different_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.emergence_detected)

    def test_compatible_different_two_witnesses(self) -> None:
        net = build_holonic_compatible_different_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.holonic_witness_count, 2)

    def test_different_cross_edge_does_not_automatically_obstruct(self) -> None:
        net = build_holonic_compatible_different_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.holonic_globally_satisfiable,
                        "A 'different' cross-edge alone should not obstruct 2-node network")


class TestEmergentObstructionScenario(unittest.TestCase):
    """Theorem 1: Holonic Emergence."""

    def test_emergent_all_micro_satisfiable(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.all_micro_satisfiable)

    def test_emergent_holonic_not_satisfiable(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.holonic_globally_satisfiable)

    def test_emergent_emergence_detected(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        result = analyze_holonic_network(net)
        self.assertTrue(result.emergence_detected)

    def test_emergent_zero_witnesses(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.holonic_witness_count, 0)

    def test_emergent_obstruction_source(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.obstruction_source, "holonic_emergence")

    def test_emergent_three_nodes(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        self.assertEqual(len(net.nodes), 3)

    def test_emergent_three_edges(self) -> None:
        net = build_holonic_emergent_obstruction_scenario()
        self.assertEqual(len(net.edges), 3)

    def test_emergence_count_matches(self) -> None:
        self.assertEqual(_r().emergence_count, 1)


class TestMicroObstructedScenario(unittest.TestCase):
    def test_micro_obstructed_not_all_micro_satisfiable(self) -> None:
        net = build_holonic_micro_obstructed_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.all_micro_satisfiable)

    def test_micro_obstructed_holonic_not_satisfiable(self) -> None:
        net = build_holonic_micro_obstructed_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.holonic_globally_satisfiable)

    def test_micro_obstructed_no_emergence(self) -> None:
        net = build_holonic_micro_obstructed_scenario()
        result = analyze_holonic_network(net)
        self.assertFalse(result.emergence_detected)

    def test_micro_obstructed_source(self) -> None:
        net = build_holonic_micro_obstructed_scenario()
        result = analyze_holonic_network(net)
        self.assertEqual(result.obstruction_source, "micro_only")


class TestHolonicPO1(unittest.TestCase):
    """Theorem 2: Cross-Level AC5."""

    def test_po1_main_source_satisfiable(self) -> None:
        src = build_holonic_po1_source()
        result = analyze_holonic_network(src)
        self.assertTrue(result.holonic_globally_satisfiable)

    def test_po1_main_target_obstructed(self) -> None:
        tgt = build_holonic_po1_target()
        result = analyze_holonic_network(tgt)
        self.assertFalse(result.holonic_globally_satisfiable)

    def test_po1_main_admissible(self) -> None:
        src = build_holonic_po1_source()
        tgt = build_holonic_po1_target()
        bridge = analyze_holonic_po1(
            source=src,
            target=tgt,
            forgotten_dims=("a1-b2-compatibility",),
            case_name="test_main",
        )
        self.assertTrue(bridge.holonic_po1_admissible)

    def test_po1_main_ac5_fires(self) -> None:
        src = build_holonic_po1_source()
        tgt = build_holonic_po1_target()
        bridge = analyze_holonic_po1(
            source=src, target=tgt,
            forgotten_dims=("a1-b2-compatibility",),
            case_name="test_main_ac5",
        )
        self.assertTrue(bridge.ac5_fires)

    def test_po1_main_ac7_holds(self) -> None:
        src = build_holonic_po1_source()
        tgt = build_holonic_po1_target()
        bridge = analyze_holonic_po1(
            source=src, target=tgt,
            forgotten_dims=("a1-b2-compatibility",),
            case_name="test_main_ac7",
        )
        self.assertTrue(bridge.ac7_holds)

    def test_po1_no_forgotten_not_admissible(self) -> None:
        src, tgt = build_holonic_po1_no_forgotten()
        bridge = analyze_holonic_po1(
            source=src, target=tgt,
            forgotten_dims=(),
            case_name="test_no_forgotten",
        )
        self.assertFalse(bridge.holonic_po1_admissible)

    def test_po1_no_forgotten_ac5_does_not_fire(self) -> None:
        src, tgt = build_holonic_po1_no_forgotten()
        bridge = analyze_holonic_po1(
            source=src, target=tgt,
            forgotten_dims=(),
            case_name="test_no_forgotten_ac5",
        )
        self.assertFalse(bridge.ac5_fires)

    def test_po1_no_forgotten_source_still_satisfiable(self) -> None:
        src, _ = build_holonic_po1_no_forgotten()
        result = analyze_holonic_network(src)
        self.assertTrue(result.holonic_globally_satisfiable)

    def test_po1_no_forgotten_target_obstructed(self) -> None:
        _, tgt = build_holonic_po1_no_forgotten()
        result = analyze_holonic_network(tgt)
        self.assertFalse(result.holonic_globally_satisfiable)

    def test_po1_admissible_count(self) -> None:
        self.assertEqual(_r().po1_admissible_count, 1)


class TestHypotheses(unittest.TestCase):

    def _hyp(self, hid: str):  # type: ignore[return]
        for h in _r().hypothesis_evaluations:
            if h.hypothesis_id == hid:
                return h
        self.fail(f"hypothesis {hid!r} not found")

    def test_h_a_rejected(self) -> None:
        self.assertEqual(self._hyp("H_A").verdict, "rejected")

    def test_h_b_best_supported(self) -> None:
        self.assertEqual(self._hyp("H_B").verdict, "best_supported")

    def test_h_c_supported(self) -> None:
        self.assertEqual(self._hyp("H_C").verdict, "supported")

    def test_h_a_has_evidence_against(self) -> None:
        self.assertGreater(len(self._hyp("H_A").evidence_against), 0)

    def test_h_b_has_evidence_for(self) -> None:
        self.assertGreater(len(self._hyp("H_B").evidence_for), 0)

    def test_best_supported_matches_field(self) -> None:
        self.assertEqual(_r().best_supported_hypothesis, "H_B")


if __name__ == "__main__":
    unittest.main()
