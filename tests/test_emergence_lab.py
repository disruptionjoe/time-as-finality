import unittest

from models.emergence_lab import (
    ElementaryCA,
    SecondOrderCA,
    analyze_eca_trace,
    analyze_second_order_trace,
    analyze_transition_map,
    eca_sensitivity_edges,
    exhaustive_preimage_search,
    find_eca_trace_witness,
    find_irreversible_inaccessible_counterexample,
    find_minimal_counterexamples,
    find_observer_divergence,
    find_reversible_record_counterexample,
    int_to_bits,
    profile_dimensions_collapsed,
    second_order_sensitivity_edges,
    sweep_elementary_rules,
)


class EmergenceLabTests(unittest.TestCase):
    def setUp(self) -> None:
        self.width = 5
        self.initial = int_to_bits(0b00100, self.width)
        self.eca = ElementaryCA(110, self.width)
        self.reversible = SecondOrderCA(self.eca)

    def test_rule_110_finite_map_is_irreversible(self) -> None:
        analysis = analyze_transition_map(self.eca)
        self.assertFalse(analysis.injective)
        self.assertLess(analysis.image_count, analysis.state_count)
        self.assertGreater(analysis.lost_bits, 0.0)
        self.assertGreater(analysis.landauer_minimum_joules, 0.0)

    def test_second_order_lift_is_reversible(self) -> None:
        analysis = analyze_transition_map(self.reversible)
        self.assertTrue(analysis.injective)
        self.assertEqual(analysis.image_count, analysis.state_count)
        self.assertAlmostEqual(analysis.lost_bits, 0.0)
        for state in self.reversible.states():
            self.assertEqual(
                self.reversible.inverse_step(self.reversible.step(state)),
                state,
            )

    def test_counterfactual_trace_is_generated_by_dynamics(self) -> None:
        witness = find_eca_trace_witness(self.eca, layers=1)
        self.assertIsNotNone(witness)
        _, _, trace = witness
        self.assertGreater(trace.profile.accessible_support, 0)
        self.assertEqual(
            trace.profile.accessible_support,
            sum(trace.trace_mask),
        )

    def test_actual_causal_edges_are_boolean_sensitive(self) -> None:
        history = self.eca.run(self.initial, 3)
        edges = eca_sensitivity_edges(self.eca, history)
        self.assertTrue(edges)
        for (parent_layer, _), (child_layer, _) in edges:
            self.assertEqual(child_layer, parent_layer + 1)

    def test_reversible_causal_edges_are_boolean_sensitive(self) -> None:
        history = self.reversible.run((self.initial, self.initial), 2)
        edges = second_order_sensitivity_edges(self.reversible, history)
        self.assertTrue(edges)
        for (parent_layer, _, _), (child_layer, _, _) in edges:
            self.assertEqual(child_layer, parent_layer + 1)

    def test_equal_windows_can_have_different_observer_profiles(self) -> None:
        witness = find_eca_trace_witness(self.eca, layers=1, window_width=2)
        self.assertIsNotNone(witness)
        _, _, trace = witness
        divergence = find_observer_divergence(trace, window_width=2)
        self.assertIsNotNone(divergence)

    def test_reversible_dynamics_can_carry_record_with_zero_information_loss(self) -> None:
        counterexample = find_reversible_record_counterexample(
            self.reversible, layers=4
        )
        self.assertIsNotNone(counterexample)
        _, _, trace = counterexample
        self.assertGreater(trace.profile.accessible_support, 0)
        self.assertAlmostEqual(analyze_transition_map(self.reversible).lost_bits, 0.0)

    def test_irreversible_map_can_hide_record_from_bounded_observer(self) -> None:
        counterexample = find_irreversible_inaccessible_counterexample(
            self.eca, layers=1, window_width=1
        )
        self.assertIsNotNone(counterexample)
        initial, seed, window, global_trace = counterexample
        local_trace = analyze_eca_trace(
            self.eca, initial, seed, layers=1, observer_indices=window
        )
        self.assertGreater(global_trace.profile.accessible_support, 0)
        self.assertEqual(local_trace.profile.accessible_support, 0)
        self.assertGreater(analyze_transition_map(self.eca).lost_bits, 0.0)

    def test_raw_profile_dimensions_partially_collapse(self) -> None:
        witness = find_eca_trace_witness(self.eca, layers=1)
        self.assertIsNotNone(witness)
        _, _, trace = witness
        self.assertTrue(profile_dimensions_collapsed(trace.profile))

    def test_computational_reversal_distinguishes_direct_inverse_from_search(self) -> None:
        irreversible_target = self.eca.step(self.initial)
        irreversible_search = exhaustive_preimage_search(
            self.eca, irreversible_target
        )
        reversible_initial = (self.initial, self.initial)
        reversible_target = self.reversible.step(reversible_initial)
        reversible_search = exhaustive_preimage_search(
            self.reversible, reversible_target
        )
        self.assertGreaterEqual(len(irreversible_search.preimages), 1)
        self.assertEqual(len(reversible_search.preimages), 1)
        self.assertEqual(
            self.reversible.inverse_step(reversible_target),
            reversible_initial,
        )
        self.assertGreater(reversible_search.candidates_examined, 1)

    def test_reversible_and_irreversible_substrates_use_same_trace_definition(self) -> None:
        irreversible = analyze_eca_trace(self.eca, self.initial, 2, layers=3)
        reversible = analyze_second_order_trace(
            self.reversible,
            (self.initial, self.initial),
            2,
            layers=3,
        )
        self.assertEqual(len(irreversible.trace_mask), self.width)
        self.assertEqual(len(reversible.trace_mask), self.width)
        self.assertIsInstance(irreversible.profile.as_tuple(), tuple)
        self.assertIsInstance(reversible.profile.as_tuple(), tuple)

    def test_complete_rule_sweep_separates_information_loss_from_record_survival(self) -> None:
        summary = sweep_elementary_rules(
            width=4,
            layers=2,
            observer_window_width=2,
            verify_reversible_lifts=True,
        )
        self.assertEqual(summary.rule_count, 256)
        self.assertTrue(summary.reversible_lifts_all_injective)
        self.assertIsNotNone(summary.same_loss_different_survival)
        self.assertIsNotNone(summary.same_survival_different_loss)
        self.assertLess(abs(summary.lost_bits_trace_survival_correlation), 1.0)

    def test_minimal_counterexamples_are_found_by_search(self) -> None:
        counterexamples = find_minimal_counterexamples(max_width=2)
        reversible = counterexamples[
            "reversible_record_with_zero_information_loss"
        ]
        inaccessible = counterexamples[
            "irreversible_record_inaccessible_to_bounded_observer"
        ]
        divergent = counterexamples["equal_access_observer_divergence"]
        self.assertEqual(reversible["width"], 1)
        self.assertEqual(inaccessible["width"], 2)
        self.assertEqual(divergent["width"], 2)


if __name__ == "__main__":
    unittest.main()
