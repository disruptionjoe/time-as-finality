import unittest

from models.compositional_finality import (
    ExpressionMark,
    compose,
    depth_sweep,
    epigenetic_history_counterexample,
    evidence_join,
    evidence_join_laws,
    exhaustive_composition_sweep,
    expressed_tokens,
    finality_profile,
    find_coarse_graining_order_change,
    find_conflict_counterexample,
    find_duplicate_inflation_counterexample,
    find_local_to_global_counterexample,
    find_profile_join_counterexample,
    grouping_variants,
    leaf,
    nested,
    provenance_support,
    randomized_grouping_trials,
)


class CompositionalFinalityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = tuple(leaf(name, "P", "true") for name in ("a", "b", "c"))

    def test_evidence_join_is_a_join_semilattice_on_compatible_states(self) -> None:
        states = tuple(evidence_join(record) for record in self.records)
        laws = evidence_join_laws(states)
        self.assertTrue(all(laws.values()))

    def test_neutral_recursive_grouping_preserves_evidence(self) -> None:
        variants = grouping_variants(self.records)
        states = {evidence_join(variant) for variant in variants}
        self.assertEqual(len(states), 1)

    def test_finality_profile_is_not_the_evidence_join(self) -> None:
        counterexample = find_profile_join_counterexample()
        self.assertEqual(counterexample.size, 2)
        self.assertNotEqual(
            counterexample.detail["componentwise_lub"],
            counterexample.detail["merged"],
        )

    def test_locally_final_conflicts_can_destroy_global_decision(self) -> None:
        counterexample = find_conflict_counterexample()
        self.assertIsNone(counterexample.detail["merged_decision"])

    def test_provenance_prevents_duplicate_support_inflation(self) -> None:
        counterexample = find_duplicate_inflation_counterexample()
        self.assertEqual(counterexample.detail["naive_token_support"], 2)
        self.assertEqual(counterexample.detail["provenance_support"], 1)

    def test_coarse_graining_can_change_finality_order(self) -> None:
        counterexample = find_coarse_graining_order_change()
        self.assertNotEqual(
            counterexample.detail["left_before"],
            counterexample.detail["left_after"],
        )

    def test_locally_consistent_assignments_may_not_glue(self) -> None:
        counterexample = find_local_to_global_counterexample()
        self.assertFalse(counterexample.detail["global_section_exists"])

    def test_epigenetic_marks_change_expression_not_identity(self) -> None:
        counterexample = epigenetic_history_counterexample()
        self.assertEqual(counterexample.detail["unmarked_support"], 1)
        self.assertEqual(counterexample.detail["silenced_support"], 0)
        self.assertEqual(counterexample.detail["reactivated_support"], 1)
        self.assertTrue(
            counterexample.detail["record_identity_preserved_while_silenced"]
        )

    def test_parent_mark_is_inherited_and_child_can_reprogram(self) -> None:
        base = leaf("source", "P", "true", expression_tags=("mark",))
        silenced = compose(
            "silenced",
            (nested(base, 8),),
            local_marks=(ExpressionMark("mark", False),),
        )
        reactivated = compose(
            "silenced-then-reactivated",
            (
                compose(
                    "reactivation-site",
                    (nested(base, 8),),
                    local_marks=(ExpressionMark("mark", True),),
                ),
            ),
            local_marks=(ExpressionMark("mark", False),),
        )
        self.assertEqual(finality_profile(silenced, "P", "true", 1).accessible_support, 0)
        self.assertEqual(finality_profile(reactivated, "P", "true", 1).accessible_support, 1)
        self.assertEqual(
            provenance_support(expressed_tokens(reactivated)),
            frozenset({"source"}),
        )

    def test_no_fixed_recursive_depth_is_assumed(self) -> None:
        result = depth_sweep(max_depth=1024)
        self.assertEqual(result["depths_tested"], 1025)
        self.assertTrue(result["neutral_invariant"])
        self.assertTrue(result["silencing_inherited_at_every_positive_depth"])

    def test_complete_small_state_sweep_separates_join_from_profile(self) -> None:
        result = exhaustive_composition_sweep(source_count=4)
        self.assertEqual(result["nonempty_states"], 15)
        self.assertEqual(result["ordered_pairs"], 225)
        self.assertEqual(result["transparent_merge_monotonicity_fraction"], 1.0)
        self.assertEqual(
            result["transparent_merge_decision_preservation_fraction"], 1.0
        )
        self.assertLess(
            result["profile_merge_equals_componentwise_lub_fraction"], 1.0
        )
        self.assertEqual(
            result["provenance_checkpoint_support_preservation_fraction"], 1.0
        )
        self.assertLess(
            result["provenance_checkpoint_holder_preservation_fraction"], 1.0
        )

    def test_context_placement_breaks_plain_grouping_invariance(self) -> None:
        result = randomized_grouping_trials(trials=60)
        self.assertEqual(result["neutral_grouping_invariance_fraction"], 1.0)
        self.assertGreater(result["context_placement_dependence_fraction"], 0.0)


if __name__ == "__main__":
    unittest.main()
