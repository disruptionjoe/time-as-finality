"""Tests for T378 generated shared-compatibility substrate fixture."""

from __future__ import annotations

from dataclasses import fields
from fractions import Fraction
import unittest

from models.generated_compatibility_substrate import (
    FORBIDDEN_SOURCE_COLUMNS,
    GeneratedRecord,
    LANDMARK_RANKS,
    append_order_independent,
    canonical_observers,
    causal_order_only_sufficient,
    derived_interval,
    derived_rank_sets,
    derived_ranks,
    generate_compatibility_substrate,
    landmark_ids,
    pair_invariants,
    path_independent_rank_derivation,
    render_record,
    run_t378_analysis,
    source_rows,
)


class GeneratedCompatibilitySubstrateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = run_t378_analysis()
        self.substrate = generate_compatibility_substrate()
        self.observers = canonical_observers()
        self.ranks = derived_ranks(self.substrate)
        self.landmarks = landmark_ids(self.substrate)

    def test_source_rows_do_not_store_time_space_or_rank_columns(self) -> None:
        self.assertTrue(self.result.source_schema_has_no_rank_or_time_columns)
        self.assertTrue(self.result.source_rows_have_no_rank_or_time_fields)
        self.assertFalse(set(self.substrate.source_columns) & FORBIDDEN_SOURCE_COLUMNS)

        for row in source_rows(self.substrate):
            self.assertFalse(set(row) & FORBIDDEN_SOURCE_COLUMNS)

        record_fields = {field.name for field in fields(GeneratedRecord)}
        self.assertNotIn("u_rank", record_fields)
        self.assertNotIn("v_rank", record_fields)
        self.assertNotIn("coord_time", record_fields)

    def test_generator_derives_unique_rank_like_coordinates_from_paths(self) -> None:
        self.assertTrue(self.result.path_independent_rank_derivation)
        self.assertTrue(path_independent_rank_derivation(self.substrate))

        rank_sets = derived_rank_sets(self.substrate)
        for record_id, values in rank_sets.items():
            with self.subTest(record_id=record_id):
                self.assertEqual(len(values), 1)

        for label, expected_rank in LANDMARK_RANKS.items():
            with self.subTest(label=label):
                self.assertEqual(self.ranks[self.landmarks[label]], expected_rank)

    def test_t377_landmark_shape_is_recovered_without_stored_rank_table(self) -> None:
        origin = self.landmarks["origin"]
        near = self.landmarks["near"]
        left_only = self.landmarks["left_only"]
        right_only = self.landmarks["right_only"]
        future = self.landmarks["future"]
        far = self.landmarks["far"]

        self.assertEqual(derived_interval(origin, near, self.ranks), 1)
        self.assertEqual(derived_interval(origin, future, self.ranks), 9)
        self.assertEqual(derived_interval(origin, far, self.ranks), 25)
        self.assertEqual(derived_interval(left_only, right_only, self.ranks), -9)

    def test_observer_family_recovers_same_interval_on_all_pairs(self) -> None:
        rows = pair_invariants(self.substrate, self.observers)
        self.assertEqual(len(rows), self.result.checked_pair_count)
        self.assertEqual(self.result.checked_pair_count, 630)
        self.assertTrue(self.result.rendered_interval_invariant)

        for row in rows:
            for observer_interval in row.observer_intervals:
                with self.subTest(
                    left=row.left_id,
                    right=row.right_id,
                    observer=observer_interval.observer_id,
                ):
                    self.assertEqual(
                        observer_interval.interval,
                        Fraction(row.derived_interval, 1),
                    )

    def test_observers_disagree_on_simultaneity_from_same_substrate(self) -> None:
        self.assertTrue(self.result.simultaneity_disagreement)
        self.assertEqual(self.result.simultaneity_same_observers, ("A_rest",))
        self.assertEqual(
            self.result.simultaneity_different_observers,
            ("B_boost_2", "C_boost_half", "D_boost_three_halves"),
        )

        left_only, right_only = self.result.simultaneity_pair
        rest, boosted, *_ = self.observers
        self.assertEqual(
            render_record(left_only, self.ranks, rest).coord_time,
            render_record(right_only, self.ranks, rest).coord_time,
        )
        self.assertNotEqual(
            render_record(left_only, self.ranks, boosted).coord_time,
            render_record(right_only, self.ranks, boosted).coord_time,
        )

    def test_append_order_or_hidden_foliation_is_not_used(self) -> None:
        self.assertTrue(self.result.append_order_independent)
        self.assertTrue(append_order_independent(self.substrate))

    def test_causal_order_alone_does_not_determine_interval_magnitude(self) -> None:
        rows = pair_invariants(self.substrate, self.observers)
        self.assertFalse(causal_order_only_sufficient(rows))
        self.assertFalse(self.result.causal_order_only_sufficient)

        origin = self.landmarks["origin"]
        near = self.landmarks["near"]
        future = self.landmarks["future"]
        self.assertNotEqual(
            derived_interval(origin, near, self.ranks),
            derived_interval(origin, future, self.ranks),
        )

    def test_hostile_comparators_distinguish_improvements_from_absorbers(self) -> None:
        by_id = {
            verdict.comparator_id: verdict for verdict in self.result.comparator_verdicts
        }

        self.assertFalse(by_id["minkowski_first"].absorbs)
        self.assertFalse(by_id["explicit_uv_rank_schema"].absorbs)
        self.assertFalse(by_id["prewritten_completed_table"].absorbs)
        self.assertTrue(by_id["finite_closure_completion"].absorbs)
        self.assertTrue(by_id["fixed_generator_rule"].absorbs)
        self.assertFalse(by_id["hidden_append_order_or_foliation"].absorbs)
        self.assertFalse(by_id["causal_order_only"].absorbs)

    def test_overall_verdict_is_generated_substrate_calibration(self) -> None:
        self.assertEqual(
            self.result.overall_verdict,
            "generated_shared_substrate_recovers_relativism_but_fixed_rule_absorbed",
        )
        self.assertIn("explicit u/v table absorption", self.result.claim_ledger_update)
        self.assertIn("fixed-rule", self.result.strongest_claim)


if __name__ == "__main__":
    unittest.main()
