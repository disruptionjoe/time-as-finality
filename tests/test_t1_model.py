import unittest

from models.t1_record_graph import (
    FinalityProfile,
    Observer,
    build_reference_scenario,
    minimal_total_order_counterexample,
)


class T1RecordGraphTests(unittest.TestCase):
    def test_reconstructs_sequential_but_not_spacelike_order(self) -> None:
        graph, observer = build_reference_scenario()
        relation = graph.reconstructed_relation(observer, ("A", "B", "C"), threshold=2)
        self.assertIn(("A", "C"), relation)
        self.assertIn(("B", "C"), relation)
        self.assertNotIn(("A", "B"), relation)
        self.assertNotIn(("B", "A"), relation)

    def test_result_is_invariant_across_topological_orders(self) -> None:
        graph, observer = build_reference_scenario()
        orders = graph.topological_orders()
        self.assertGreater(len(orders), 1)
        expected = graph.reconstructed_relation(observer, ("A", "B", "C"), threshold=2)
        for _order in orders:
            self.assertEqual(
                graph.reconstructed_relation(observer, ("A", "B", "C"), threshold=2),
                expected,
            )

    def test_local_access_loss_does_not_erase_global_record(self) -> None:
        graph, observer = build_reference_scenario()
        limited = Observer(
            observer.observer_id,
            observer.event,
            observer.accessible_holders - {"ha2"},
        )
        self.assertEqual(
            graph.finality_profile(limited, "A", "true", threshold=2).accessible_support,
            1,
        )
        self.assertTrue(graph.records["ra2"].active)
        self.assertEqual(
            graph.finality_profile(observer, "A", "true", threshold=2).accessible_support,
            2,
        )

    def test_physical_reversal_changes_all_observers(self) -> None:
        graph, observer = build_reference_scenario()
        graph.erase_record("rb2")
        self.assertEqual(
            graph.finality_profile(observer, "B", "true", threshold=2).accessible_support,
            1,
        )
        alternate = Observer("O2", observer.event, observer.accessible_holders)
        self.assertEqual(
            graph.finality_profile(alternate, "B", "true", threshold=2).accessible_support,
            1,
        )

    def test_preorder_allows_distinct_profiles_to_be_equivalent(self) -> None:
        graph, observer = build_reference_scenario()
        profile_a = graph.finality_profile(observer, "A", "true", threshold=2)
        profile_c = graph.finality_profile(observer, "C", "true", threshold=2)
        self.assertEqual(profile_a.as_tuple(), profile_c.as_tuple())
        self.assertTrue(profile_a.no_more_final_than(profile_c))
        self.assertTrue(profile_c.no_more_final_than(profile_a))

    def test_preorder_preserves_genuine_incomparability(self) -> None:
        holder_heavy = FinalityProfile(2, 2, 1, 1)
        branch_heavy = FinalityProfile(2, 1, 2, 1)
        self.assertFalse(holder_heavy.no_more_final_than(branch_heavy))
        self.assertFalse(branch_heavy.no_more_final_than(holder_heavy))

    def test_preorder_is_reflexive_and_transitive(self) -> None:
        low = FinalityProfile(1, 1, 1, 0)
        middle = FinalityProfile(2, 1, 2, 1)
        high = FinalityProfile(3, 2, 2, 2)
        self.assertTrue(low.no_more_final_than(low))
        self.assertTrue(low.no_more_final_than(middle))
        self.assertTrue(middle.no_more_final_than(high))
        self.assertTrue(low.no_more_final_than(high))

    def test_graph_and_thermodynamic_reversal_order_can_diverge(self) -> None:
        graph, observer = build_reference_scenario()
        graph_a = graph.finality_profile(
            observer, "A", "true", threshold=2
        ).graph_reversal_cost
        graph_b = graph.finality_profile(
            observer, "B", "true", threshold=2
        ).graph_reversal_cost
        thermal_a = graph.thermodynamic_reversal_proxy(
            observer, "A", "true", threshold=2
        )
        thermal_b = graph.thermodynamic_reversal_proxy(
            observer, "B", "true", threshold=2
        )
        self.assertEqual(graph_a, graph_b)
        self.assertNotEqual(thermal_a, thermal_b)

    def test_minimal_counterexample_refutes_total_order(self) -> None:
        graph, observer = minimal_total_order_counterexample()
        self.assertEqual(
            graph.reconstructed_relation(observer, ("L", "R"), threshold=1),
            frozenset(),
        )
        self.assertEqual(len(graph.events), 3)

    def test_competing_threshold_values_are_not_reconstructed(self) -> None:
        graph, observer = minimal_total_order_counterexample()
        graph.add_record(
            type(graph.records["left-record"])(
                "left-conflict",
                "L",
                "false",
                "right",
                "right-holder",
            )
        )
        self.assertIsNone(graph.reconstruct_value(observer, "L", threshold=1))


if __name__ == "__main__":
    unittest.main()
