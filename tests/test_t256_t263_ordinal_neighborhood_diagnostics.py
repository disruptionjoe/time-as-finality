"""Tests for T256-T263 ordinal-neighborhood diagnostics."""

from __future__ import annotations

import unittest
from fractions import Fraction

from models.t256_t263_ordinal_neighborhood_diagnostics import (
    run_t256_analysis,
    run_t257_analysis,
    run_t258_analysis,
    run_t259_analysis,
    run_t260_analysis,
    run_t261_analysis,
    run_t262_analysis,
    run_t263_analysis,
)


class OrdinalNeighborhoodDiagnosticTests(unittest.TestCase):
    def test_t256_parent_and_deletions_have_bounded_interval_profiles(self) -> None:
        result = run_t256_analysis()

        self.assertEqual(result.parent_shape.largest_interval_size, 3)
        self.assertEqual(result.parent_shape.interval_counts_by_size, ((0, 8), (1, 6), (2, 4), (3, 2)))
        self.assertEqual(result.deletion_largest_interval_distribution, ((2, 1), (3, 8)))
        self.assertTrue(all(deletion.shape.t126_filter_passed for deletion in result.deletion_shapes))
        self.assertEqual(result.verdict, "ordinal_interval_profiles_bounded_under_deletion")

    def test_t257_cover_locality_stays_sparse_under_deletion(self) -> None:
        result = run_t257_analysis()

        self.assertEqual(result.parent_shape.cover_relation_count, 8)
        self.assertEqual(result.parent_shape.largest_cover_hub_fraction, Fraction(1, 4))
        self.assertEqual(result.deletion_cover_count_distribution, ((6, 1), (7, 8)))
        self.assertEqual(result.deletion_cover_hub_distribution, ((Fraction(2, 7), 9),))
        self.assertEqual(result.deletion_link_density_distribution, ((Fraction(1, 2), 1), (Fraction(7, 16), 8)))
        self.assertEqual(result.verdict, "ordinal_cover_locality_stable_under_deletion")

    def test_t258_positive_neighbors_are_structurally_mixed(self) -> None:
        result = run_t258_analysis()

        self.assertEqual(result.positive_neighbor_count, 21)
        self.assertEqual(
            result.ordering_fraction_distribution,
            ((Fraction(17, 36), 4), (Fraction(19, 36), 4), (Fraction(5, 12), 4), (Fraction(7, 12), 9)),
        )
        self.assertEqual(result.width_distribution, ((2, 4), (3, 13), (4, 4)))
        self.assertEqual(result.largest_interval_distribution, ((3, 13), (4, 4), (5, 1), (6, 2), (7, 1)))
        self.assertEqual(result.verdict, "positive_mutation_neighbors_keep_band_but_shape_varies")

    def test_t259_inside_band_failures_are_profile_spread_obstructions(self) -> None:
        result = run_t259_analysis()

        self.assertEqual(result.blocked_inside_band_count, 13)
        self.assertEqual(result.classification_distribution, (("order_dimension_obstruction", 13),))
        self.assertEqual(result.profile_spread_obstruction_count, 13)
        self.assertEqual(
            result.ordering_fraction_distribution,
            ((Fraction(17, 36), 2), (Fraction(19, 36), 4), (Fraction(7, 12), 7)),
        )
        self.assertEqual(result.verdict, "inside_band_neighbors_blocked_by_profile_spread")

    def test_t260_outside_band_cases_are_two_low_fraction_edges(self) -> None:
        result = run_t260_analysis()

        self.assertEqual(result.outside_band_count, 2)
        self.assertEqual(result.outside_band_swaps, ((0, 4), (0, 8)))
        self.assertEqual(result.ordering_fraction_distribution, ((Fraction(13, 36), 2),))
        self.assertEqual(result.cover_count_distribution, ((6, 2),))
        self.assertEqual(result.cover_hub_distribution, ((Fraction(1, 4), 2),))
        self.assertEqual(result.verdict, "outside_band_neighbors_are_two_low_fraction_edge_cases")

    def test_t261_grid_is_more_ordered_than_ordinal_control(self) -> None:
        result = run_t261_analysis()

        self.assertEqual(result.grid_shape.strict_pair_count, 27)
        self.assertEqual(result.ordinal_shape.strict_pair_count, 20)
        self.assertEqual(result.strict_pair_delta_grid_minus_ordinal, 7)
        self.assertEqual(result.ordering_fraction_gap_grid_minus_ordinal, Fraction(7, 36))
        self.assertEqual(result.cover_relation_delta_grid_minus_ordinal, 4)
        self.assertEqual(result.largest_interval_delta_grid_minus_ordinal, 4)
        self.assertEqual(result.cover_hub_gap_grid_minus_ordinal, Fraction(1, 4))
        self.assertEqual(result.verdict, "grid_is_more_ordered_and_interval_deeper_than_ordinal_control")

    def test_t262_prefers_exact_nine_event_count_next(self) -> None:
        result = run_t262_analysis()

        self.assertTrue(result.parent_and_deletions_stay_inside_interval_cap)
        self.assertTrue(result.parent_and_deletions_stay_below_cover_hub_cap)
        self.assertEqual(result.mutation_count, 36)
        self.assertEqual(result.positive_neighbor_count, 21)
        self.assertEqual(result.blocked_inside_band_count, 13)
        self.assertEqual(result.outside_band_count, 2)
        self.assertEqual(result.positive_neighbor_rate, Fraction(7, 12))
        self.assertEqual(result.band_neighbor_rate, Fraction(17, 18))
        self.assertEqual(result.selected_next_route, "bounded_exact_n9_class_count_with_shape_labels")
        self.assertEqual(result.verdict, "exact_nine_event_count_preferred_over_more_selected_examples")

    def test_t263_records_completed_eight_task_round(self) -> None:
        result = run_t263_analysis()

        self.assertEqual(result.completed_task_count, 8)
        self.assertEqual(result.round_verdict, "eight_task_ordinal_neighborhood_diagnostic_round_complete")
        self.assertIn("Do not update the claim ledger", result.claim_ledger_update)
        self.assertIn("exact n=9", result.suggested_next)


if __name__ == "__main__":
    unittest.main()
