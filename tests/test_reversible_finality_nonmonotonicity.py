"""Tests for T80: reversible local dynamics can violate D1 monotonicity."""

from __future__ import annotations

import unittest

from models.reversible_finality_nonmonotonicity import (
    canonical_rule30_witness,
    find_first_nonmonotone_step,
    layer_profile_sequence,
    run_t80_analysis,
    search_reversible_nonmonotone_witness,
)
from models.emergence_lab import ElementaryCA, SecondOrderCA, analyze_transition_map, int_to_bits


class ReversibleFinalityNonmonotonicityTests(unittest.TestCase):
    def test_canonical_witness_is_reversible_and_lossless(self) -> None:
        result = canonical_rule30_witness()

        self.assertTrue(result.transition.injective)
        self.assertEqual(result.transition.image_count, result.transition.state_count)
        self.assertAlmostEqual(result.transition.lost_bits, 0.0)
        self.assertAlmostEqual(result.transition.landauer_minimum_joules, 0.0)
        self.assertTrue(result.direct_inverse_checked)

    def test_raw_trace_profile_decreases_under_physical_step(self) -> None:
        result = canonical_rule30_witness()
        step = result.first_nonmonotone_step

        self.assertEqual(step.before.layer, 1)
        self.assertEqual(step.after.layer, 2)
        self.assertEqual(step.before.profile.as_tuple(), (2, 2, 1, 2))
        self.assertEqual(step.after.profile.as_tuple(), (1, 1, 1, 1))
        self.assertIn("accessible_support", step.decreased_dimensions)
        self.assertIn("terminal_intervention_cost", step.decreased_dimensions)

    def test_t18_classifies_the_physical_step_as_impossible(self) -> None:
        result = canonical_rule30_witness()
        classification = result.first_nonmonotone_step.t18_classification

        self.assertEqual(classification.kind, "strict_definalization")
        self.assertFalse(classification.possible)

    def test_profile_sequence_api_finds_same_nonmonotone_step(self) -> None:
        width = 3
        ca = SecondOrderCA(ElementaryCA(30, width))
        zero = int_to_bits(0, width)
        profiles = layer_profile_sequence(
            ca,
            initial=(zero, zero),
            seed_index=0,
            observer_window=(0, 1),
            layers=5,
        )

        step = find_first_nonmonotone_step(profiles)

        self.assertIsNotNone(step)
        self.assertEqual(step.before.layer, 1)
        self.assertEqual(step.after.layer, 2)

    def test_search_finds_a_reversible_nonmonotone_witness(self) -> None:
        result = search_reversible_nonmonotone_witness(max_width=2, max_layers=3)

        self.assertIsNotNone(result)
        self.assertTrue(result.transition.injective)
        self.assertFalse(result.first_nonmonotone_step.t18_classification.possible)

    def test_persistent_memory_control_is_monotone_but_not_raw_dynamics(self) -> None:
        result = canonical_rule30_witness()
        raw_profiles = [profile.profile.accessible_support for profile in result.layer_profiles]

        self.assertIn((2, 1), tuple(zip(raw_profiles, raw_profiles[1:])))
        self.assertTrue(result.persistent_memory_support_monotone)

    def test_run_t80_reports_claim_boundary(self) -> None:
        result = run_t80_analysis()

        self.assertIn("not monotone", result.strongest_claim)
        self.assertIn("conditional constructor theorem", result.weakened_claim)
        self.assertIn("persistent reconciler", result.recommended_next)

    def test_canonical_witness_uses_reversible_second_order_map(self) -> None:
        ca = SecondOrderCA(ElementaryCA(30, 3))
        transition = analyze_transition_map(ca)

        self.assertTrue(transition.injective)
        for state in ca.states():
            self.assertEqual(ca.inverse_step(ca.step(state)), state)


if __name__ == "__main__":
    unittest.main()
